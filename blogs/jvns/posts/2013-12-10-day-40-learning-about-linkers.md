---
title: "Day 40: Linkers are amazing."
date: 2013-12-10
url: https://jvns.ca/blog/2013/12/10/day-40-learning-about-linkers/
slug: day-40-learning-about-linkers
word_count: 2307
---


I have a linker bug in my kernel which is kind of infuriating me. So
I’ve spent the whole day so far reading the first 11 parts of this
[excellent 20-part series about how linkers work](http://lwn.net/Articles/276782/)
by Ian Lance Taylor.


Here are some notes on the series. This is gigantic and basically just
for my own reference, but summarizes what he talks about in the first
half of the series.


I’m not going to describe the basics of what a linker does because I
know already. I talk a little about linkers in
[How to call Rust from assembly](http://jvns.ca/blog/2013/12/01/how-to-call-rust-from-assembly/),
and I found this
[Beginner’s guide to linkers](http://www.lurklurk.org/linkers/linkers.html)
pretty helpful. Parts [[1]](http://www.airs.com/blog/archives/38) and
[[2]](http://www.airs.com/blog/archives/39) of the essay also discuss
“what’s a linker?”.


For context: Right now I have a bug while statically linking a
single-threaded ELF file. So I will read about dynamic linking and
threading and things other than ELF, but I will mostly ignore it.


# 1. Basic linker data types: symbols, relocations, and contents


There are **symbols**, **relocations** and **contents** in object
files. I knew about symbols and contents already, but relocations are
new to me. The contents are the contents of a variable or function. A
key insight here is that the linker doesn’t actually care too much
about the contents – it’s just concerned with putting the contents in
the right place.


Linkers don’t care about your functions and variables! They’re just
bytes. :) In the first article he talks about linker speed – a
benchmark you could compare a linker to is `cat`, because it’s just
combining the bytes together, and making some replacements along the
way.


**Relocations** were new to me. The story here is that when you have
an object file, the assembly code often refer to a symbol like this:


```
call awesome_function

```


`awesome_function` might be undefined – it could be a function
defined in a library that we’re planning to link against later.


So after linking, `awesome_function` will be somewhere new, and we
need to put a memory address in `call awesome_function`! So there’s a
**relocation table** which keeps track of everything that needs to be
moved.


To make this a bit more concrete, I looked at `man objdump`. Turns out
you can look at the relocations in an object file by running `objdump -r file.o`. When you look at the relocations in an ELF file, there are
a bunch of scary-looking things like `R_386_PC32` and `R_386_GOTPC`.
Here’s
[a page explaining what those things mean](http://netwinder.osuosl.org/users/p/patb/public_html/elf_relocs.html).
For example, I got this as an output from `objdump -r`


```
00001a76 R_386_GOTPC       _GLOBAL_OFFSET_TABLE_
00001a7f R_386_GOTOFF      _ZN3mem4base18he097c5c5c82e35fah4v0.0E
00001a95 R_386_GOTOFF      _ZN3mem4base18he097c5c5c82e35fah4v0.0E
00001ac4 R_386_PC32        __morestack

```


I think the last line of that means “At `00001ac4`, there’s a
reference to `__morestack`. I’m going to need you to figure out the
distance from `00001ac4` to `__morestack` and add it to the dword at
`00001ac4`.


Basically `R_386_PC32` and friends are different rules that the linker
has to follow. Some possible things that relocation rules might do:

- Put a relative memory address somewhere
- Put an absolute memory address somewhere
- Add something to the Global Offset Table (GOT)
- Add something to the Procedure Lookup Table (PLT)


I don’t know what the GOT/PLT are yet but hopefully as I keep reading
I’ll learn. (I did! See part 4)


From [Part 2](http://www.airs.com/blog/archives/39).


# 2. Object file formats


Apparently there are many different kinds of object file formats
(COFF, ELF, PE, a.out, IEEE-695, Mach-O, etc.). They can be either
**section-based** or **record-based**. I only care about ELF. ELF is
section-based. This means that the file is split up into sections.


You can use `readelf --sections myfile.o` to list the sections in an
ELF file, and `objdump -t` to list the symbol table and which section
each symbol belongs to.


Here are [the sections](http://sprunge.us/hEDd) and
[the symbol table](http://sprunge.us/ZIgG) for an OCaml object file I
found on my machine. You can see that the sections that have
most of the symbols in them are `.data`, `.text`, and `.bss`. And
there’s a section called `.symtab`, which I guess is the symbol table!
Neat.


`.text` is the “code” of the program, and `.data`, `.bss`, and
`.rodata` contain different kinds of globals.


# 3. Debugging symbols


It says


> The ELF object file format stores debugging information in sections
> with special names.


It mentions debugging formats like “stabs strings” and “the DWARF
debugging format”, but not going down that rabbit hole right now.


File formats and debugging symbols were in
[Part 3](http://www.airs.com/blog/archives/40).


# 4. Shared libraries and position independence


A shared library is a `.dll` on Windows or a `.so` file on Linux.


The deal with a shared library is when you create the library, you
don’t know what address in memory it’s going to be loaded at. (it
depends on what the dynamic linker decides to do). So some calculation
(addition!) needs to happen no matter what.


So there are two different strategies to deal with this.


**Strategy 1**: Make it **position dependent**. This basically means
“write a huge relocation table and let the dynamic linker figure out
where everything should go”. Because there is a huge relocation
table, this means the library will take longer to load.


**Strategy 2**: Make it **position independent**. This means “don’t
write a relocation table, but every time you call a function or
reference a variable, look up where it should be in a table”. So the
library loads more quickly, but runs more slowly. Tradeoffs!


This brings us back to the “Global Offset Table” and “Procedure Lookup
Table” from before! So in position independent code, the “Global
Offset Table” is where look up our global and static variables, and
the “Procedure Lookup Table” is where we look up functions.


The other super important thing here (discussed more in
[Part 6](http://www.airs.com/blog/archives/43)) is that in position
independent code, the assembly instructions always the *same*, and
only the PLT and the GOT need be different. This means that if you
have a huge library two different processes can reference the same
(read-only) assembly instructions and they only need to have their own
copy of the PLT and GOT.


This is super neat! In my object file, I have


```
00001a76 R_386_GOTPC       _GLOBAL_OFFSET_TABLE_

```


I guess that means the object file I am looking at is position
independent!


Another neat thing about position independent code is that the dynamic
linker can do lazy loading – it can wait to put the address of a
function in the PLT until it is actually loaded. So if you run a
program that links against all of the math library, but only calls
`sin`, it only needs to figure out the address of `sin`.


All this about shared libraries is in
[Part 4](http://www.airs.com/blog/archives/41).


# 5. What can go wrong with shared libraries


There’s a super interesting discussion of a kind of bug you can have
with shared libraries in
[Part 5](http://www.airs.com/blog/archives/42).


In C, you can take the address of a function (`&f`). The natural
address for `f` is its entry in the PLT, because that’s where you jump
to when the function is called. But different shared libraries have
different `PLT`s, so you might end up with two different addresses for
the function, and if you compared them you would get different
answers. Oh no! I did not know that this was even a thing. Cool!


You can go read about the solution in the essay.


All this stuff about dynamic linking is really interesting and
complicated, but I’m actually reading this in an effort to solve a
static linking problem that I have, so I’m not reading it with 100%
attention.


# 6. ELF symbol visibility and types


I didn’t know that symbols had visibility and types! I thought
everything was global and pretty much the same type. I don’t care too
much about this right now, though.


Also from [Part 5](http://www.airs.com/blog/archives/42).


# 7. Linkers are architecture-dependent


How a linker deals with relocations depends on the architecture of the
machine the binaries are for! When you’re writing an OS, you need a
cross-compiler that targets your target architecture. But you also
need a cross-linker! Here’s why.


C code: `g = 0`.


Corresponding 386 code: `movl 0 g`.


Corresponding RISC code:


```
li 1,0 // Set register 1 to 0
lis 9,g@ha // Load high-adjusted part of g into register 9
stw 1,g@l(9) // Store register 1 to address in register 9 plus low adjusted part g

```


Here `g` is referenced twice! So the linker is going to need to know
about how RISC works and the relocation is going to look different
than it would on 386.


This was [Part 6](http://www.airs.com/blog/archives/43).


# 8. Thread Local Storage


[Part 7](http://www.airs.com/blog/archives/44) is an extremely cool
explanation of how ELF systems have special support for making
threading more efficient. I had no idea this was a thing the linker
did. Linkers are crazy.


The idea here is that you can just mark a variable thread-local in C
like this:


```
__thread int i;

```


and the compiler and linker will do a bunch of stuff so that every
thread has its own copy of the variable.


The alternative here (I think) is to use `pthread_key_create`,
`pthread_get_specific` and `pthread_set_specific`. I’ve never used
pthreads, but this is cool and definitely seems easier. There’s a
discussion of when it is more efficient in the essay. (tl;dr: never
slower, sometimes faster)


# 9. ELF segments


More on “oh man ELF is complicated!”
[Part 8](http://www.airs.com/blog/archives/45) has a description of
all the section and segment types.


Okay, so what is a **segment**, anyway? We talked about **sections**
before – we said that they were `.text`, `.data`, `.rodata`, etc. –
to separate out read-only data from read-write data from program code.
**Segments** are collections of sections.


ELF is an format for object files, and also executables. Apparently
the operating system doesn’t use the sections at all to run programs,
just the segments.


I’m a bit confused here, so let’s make this more concrete by looking
at a simple “Hello World” C program. I couldn’t figure out how to use
`objdump` to look at segments, but my awesome friend
[Dave](https://twitter.com/djvasi) suggested using `readelf` instead.
That totally works!


Here’s the
[the entire output of `readelf --segments a.out`](http://sprunge.us/JFZJ).
Here’s an excerpt:


```
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .text .fini .rodata .eh_frame_hdr .eh_frame 
   03     .ctors .dtors .jcr .dynamic .got .got.plt .data .bss 
   04     .dynamic 
   05     .note.ABI-tag .note.gnu.build-id 
   06     .eh_frame_hdr 
   07     
   08     .ctors .dtors .jcr .dynamic .got 

```


So here it looks like `.text` is in a segment with a bunch of stuff,
and `.data` and `.bss` are in a segment together. There are a bunch of
possible segment types. One of the most important ones seems to be
`LOAD`. I think that means “load into memory”. The two segments marked
`LOAD` are segment `02` and `03`. This makes sense, because those are
the segments with `.text` and `.data` in them!


The other segment types in [the output of readelf](http://sprunge.us/JFZJ) are:

- `INTERP`: Which dynamic loader to use
(`/lib64/ld-linux-x86-64.so.2`). I checked and this is an actual
file. <3.
- `NOTE`: I guess this is a note.
- `GNU_EH_FRAME`, `GNU_STACK`, `GNU_RELRO`: Some GNU extensions. I
don’t really know.
- `DYNAMIC`: Some stuff that the dynamic linker needs.
- `PHDR`: I quote: “This indicates the address and size of the segment
table. This is not too useful in practice as you have to have
already found the segment table before you can find this segment.”
lulz. What.


The last thing I want to note about this example is that section `02`
(the one with `.text` and `.rodata` in it) has flags `RE`, so it can
be executed. I’m wondering if you could trick the program into
executing something from `.rodata`, and if that could be bad. Section
`03` has flags `RW`, so it can be written to but not executed.


So the reason that `.text` and `.data` aren’t in the same section is
that `.text` has to be read-only and `.data` needs to be read-write.


Here’s another example of [the segments](http://sprunge.us/HIGL) and
[the symbol table](http://sprunge.us/VAUH) in the same program, but
this time statically linked. There are way less segments (the file is
less complicated), but the symbol table is much bigger.


Okay I think I’m pretty good with segments. This is cool!


# 9. Symbol versions


Apparently in an ELF file, you can have two different versions of the
same symbol, in case the function signature has changed! This is
crazy. I thought that if you had `sin`, there was only one `sin`.


Could you abuse this to have polymorphism in object files without
doing name mangling? Huh.


The actual use case described for this is providing two versions for
`stat`: `LIBC_1.0` and `LIBC_2.0` after it changed to support 64-bit
file offsets (whatever that means).


From [Part 9](http://www.airs.com/blog/archives/46).


# 10. Parallel linking


You can do linking in parallel to some extent. Also, once the output
file is laid out and its size is determined, you can use `mmap` and do
the I/O in parallel that way. Yay `mmap`!


From [Part 10](http://www.airs.com/blog/archives/47).


# 11. Archives


Apparently you can package a whole bunch of object files together into
an **archive**. This is what files with the `.a` extension are. Neat!
I’ve seen those, but didn’t know what they were. They’re created with
the `ar` utility.


I looked for archive files on my computer using `locate .a | egrep '.a$' | head`, and I found one in `/etc/alternatives/libblas.a`. It
kind of makes sense that BLAS is made of a whole bunch of object
files.


I used `objdump -t /etc/alternatives/libblas.a` to look at is symbol
table. In [the output](http://sprunge.us/YCgc), it lists the symbol
table for each object file. Here’s
[just the list of object files](http://sprunge.us/XNjd).
`libblas.a` is made up of 313 object files.


From [Part 11](http://www.airs.com/blog/archives/48).
