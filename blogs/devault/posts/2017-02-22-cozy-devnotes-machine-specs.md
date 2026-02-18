---
title: "Compiler devnotes: Machine specs"
date: 2017-02-22
url: https://drewdevault.com/2017/02/22/cozy-devnotes-machine-specs.html
slug: cozy-devnotes-machine-specs
word_count: 1869
---

I have a number of long-term projects that I plan for on long timelines, on the
order of decades or more. One of these projects is cozy, a C toolchain. I
haven’t talked about this project in public before, so I’ll start by introducing
you to the project. The main C toolchains in the “actually usable” category are
GNU and LLVM, but I’m satisfied with neither and I want to build my own
toolchain. I see no reason why compilers should be deep magic. Here are my goals
for cozy:

* Self hosting and written in C
* An easy to grok codebase and internal design
* Focused on C. No built-in support for other languages
* Adding new targets architectures and ports should be straightforward
* Modular build pipeline with lots of opportunities for external integrations
* Trivially cross-compiles without building another version of the toolchain
* Includes a decent optimizer

Some other plans include opinionated warnings about code and minimal support for
language extensions. Ambitious goals, right? That’s why this project is on my
long-term schedule. I’ve found that large projects are entirely feasible, so
long as you (1) start them and (2) keep working on them for a long time. I don’t
need to rush this - gcc and clang may not be ideal, but they work today. In
support of these goals, I’ll be writing these dev notes to explain my design
choices and gather feedback — please  [email me](mailto:sir@cmpwn.com)  if
you have some!

Since I want to place an emphasis on portability and retargetability, I’m
starting by designing the machine spec and its support code, which is used to
add support for new architectures. I don’t like gcc’s lisp specs, and I  *really* 
don’t like LLVM’s “huge pile of C++” approach. I think a really good machine
spec meets these goals:

* Easy to write and human friendly
* More about data than code, but
* Easily extended with C to support architecture-specific nuances
* Provides loads of useful metadata about the target architecture
* Exposes information about the speed and side-effects of each instruction
* Can also be used to generate an assembler and disassembler
* Easily reused to create derivative architectures

Adding a new architecture should be a weekend project, and when you’re done the
entire toolchain should both support and run on your new architecture. I set out
to come up with a new syntax that could potentially meet these goals. I started
with the Z80 architecture in mind because it’s simple, I’m intimately familiar
with it, and I want cozy to be able to target 8-bit machines just as easily as
32 or 64 bit.

For reference, here are the gcc and LLVM guides on adding new targets:

* [gcc - Anatomy of a Target Back End](https://gcc.gnu.org/onlinedocs/gccint/Back-End.html)
* [Writing an LLVM Backend](http://llvm.org/docs/WritingAnLLVMBackend.html)

The cozy machine spec is a cross between ini files, yaml, and a custom syntax.
The format is somewhat complex, but once understood is intuitive and flexible.
At the top level, it looks like an ini file:

```
[metadata]
# ...

[registers]
# ...

[macros]
# ...

[instructions]
# ...
```

### Metadata

The  **metadata**  section contains some high-level information about the
architecture design, and is the simplest section to understand. It currently
looks like this for z80:

```
[metadata]
name: z80
bits: 8
endianness: little
signedness: twos-complement
cache: none
pipeline: none
```

This isn’t comprehensive, and I’ll be adding more metadata as it becomes
necessary. On LLVM, this sort of information is encoded into a string that looks
something like this:  `"e-p:16:8:8-i8:8:8-i16:8:8-n8:16"` . This string is passed
into the  `LLVMTargetMachine`  base constructor in C++. I think we can do a hell
of a lot better than that!

### Registers

The  **registers**  section describes the registers on this architecture.

```
[registers]
BC: 16
    B: 8
    C: 8; offset=8
DE: 16
    D: 8
    E: 8; offset=8
HL: 16
    H: 8
    L: 8; offset=8
SP: 16; stack
PC: 16; program
```

Here we can start to see some interesting syntax and get an idea of the design
of cozy machine specs. The contents of each section are keys, which have values,
attributes, and children. The format looks like this:

```
key: value; attributes, ...
    children...
```

In this example, we’ve defined the BC, DE, HL, SP, and PC registers. HL, DE, and
BC are general purpose 16-bit registers, and each can also be used as two
separate 8-bit registers. The attributes for these sub-registers indicates their
offsets in the parent register. We also define the stack and program registers,
SP and PC, which use the stack and program attributes to indicate their special
purposes.

We can also describe CPU flags in this section:

```
[registers]
AF: 16; special
    A: 8; accumulator
    F: 8; flags, offset 8;; flag
        _C:  1
        _N:  1; offset 1
        _PV: 1; offset 2
        _3:  1; offset 3, undocumented
        _H:  1; offset 4
        _5:  1; offset 5, undocumented
        _Z:  1; offset 6
        _S:  1; offset 7
```

Here we introduce another feature of cozy specs with  `F: 8; flags, offset 8;; flag` . Using  `;;`  adds those attributes to all children of this key, so each of
_C, _N, etc have the  `flag`  attribute.

Take note of the “undocumented” attribute here. Some of the metadata included
in a spec can be applied to cozy tools. Some of it, however, is there for other
tools to utilize. We have a good opportunity to make a machine-readable
description of the architecture, so I’ve opted to include a lot of extra details
in machine specs that third parties could utilize (though there might be a
-fno-undocumented compiler flag some day, I guess).

### Macros

The  **macros**  section is heavily tied to the instructions section. Most instruction
sets are quite large, and I don’t want to burden spec authors with writing out
the entire thing. We can speed up their work by providing macros.

z80 instructions have a few sets of common patterns in their encodings. Register
groups are often represented by the same set of bits, and we can make our
instruction set specification more concise by taking advantage of this. For
example, here’s a macro that we can use for instructions that can use either the
BC, DE, HL, or SP registers:

```
[macros]
reg_BCDEHLSP:
    BC: 00
    DE: 01
    HL: 10
    SP: 11
```

We have the name of the macro as the top-level key, in this case  `reg_BCDEHLSP` .
We can later refer to this macro with  `@reg_BCDEHLSP` . Then, we have each of the
cases it can match on, and the binary values these correspond to when encoded in
an instruction.

### Instructions

The instructions section brings everything together and defines the actual
instructions available on this architecture. Instructions can be organized into
groups at the spec author’s pleasure, which can be referenced by derivative
architectures. Here we can take a look at the “load” group:

```
[instructions]
.load:
    ld:
        @reg_BCDEHLSP, @imm[16]: 00 $1 0001 $2
```

On z80, the  `ld`  instruction is similar to the  `mov`  instruction on Intel
architectures. It assigns the second argument to the first. This could be used
to assign registers to each other (e.g.  `ld a, b`  to set A = B), to set
registers to constants, and so on. Our example here uses our macro from earlier
to match instructions like this:

```
ld hl, 0x1234
```

The value for this key may reference the arguments with variables. $1 here
equals  `10` , from the macro. The  `imm`  built-in is implemented in C to match
constants and provides $2. An assembler could use this information to assemble
our example instruction into this machine code:

```
00100001 00110100 00010010
```

Which will load HL with the value 0x1234 when executed.

### Lots more metadata

Now that we have the basics down, let’s dive into some deeper details. Cozy
specs are designed to provide most of the information the  *entire toolchain* 
needs to support an architecture. The information we have so far could be used
to generate assemblers and disassemblers, but I want this file to be able to
generate things like optimizers as well. You can add the necessary metadata to
each instruction by utilizing attributes.

Consider the z80 instruction LDIR, which stands for
“load/decrement/increment/repeat”. This instruction is used for memcpy
operations. To use it, you set the HL register to a source address, the DE
register to a destination address, and BC to a length. This instruction looks
like this in the spec:

```
ldir: 11101101 10110000; uses[HL, DE, BC], \
    affects[HL[+BC], DE[+BC], BC[0]], \
    flags[_H:0,_N:0,_PV:0], cycles[16 + BC * 5]
```

That’s a lot of attributes! The purpose of these attributes are to give the
toolchain insights into the registers this instruction uses, its side effects,
and how fast it is. These attributes can help us compare the efficiency of
different approaches and understand the how the state of registers evolves
during a function, which leads to all sorts of useful optimizations.

The  `affects`  attribute, for example, tells us how each register is affected by
this instruction. We can see that after this instruction, HL and DE will have
had BC added to them, and BC will have been set to 0. We can make all sorts of
optimizations based on this knowledge. Here are some examples:

```
char *dest, *src;
int len = 10;
memcpy(dest, src, len);
src += len;
```

The compiler can assign  `src`  to HL,  `dest`  to DE, and  `len`  to BC. We can then
optimize out the final statement entirely because we know that the LDIR
instruction will have already added BC to HL for us.

```
char *dest, *src;
int len = 10;
memcpy(dest, src, len);
int foobar = 0;
```

In this case, the register allocator can just assign BC to  `foobar`  and avoid
initializing it because we know it’s already going to be zero. Many other
optimizations are made possible when we are keeping track of the side effects of
each instruction.

## Next steps

I’ve iterated over this spec design for a while now, and I’m pretty happy with
it. I would love to hear your feedback. Assuming that this looks good, my next
step is writing more specs, and a tool that parses and compiles them to C. These
C files are going to be linked into  `libcozyspec` , which will provide an API to
access all of this metadata from C. It will also include an instruction matcher,
which will be utilized by the next step - writing the assembler.

The assembler is going to take a while, because I don’t want to go the gas route
of making a half-baked assembler that’s more useful for compiling the C
compiler’s output than for anything else. I want to make an assembler that
assembly programmers would  *want*  to use.

I have not yet designed an intermediate bytecode for the compiler to use, but
one will have to be made. The machine spec will likely change somewhat to
accommodate this. Some of the conversion from internal bytecode to target
assembly can likely be inferred from metadata, but some will have to be done
manually for each architecture.

[Here’s the entire z80 spec](https://sr.ht/7_Pe.txt)  I’ve been working on, for
your reading pleasure.
