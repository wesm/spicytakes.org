---
title: "Tips for debugging your new programming language"
date: 2021-08-11
url: https://drewdevault.com/2021/08/11/Debugging-your-new-PL.html
slug: Debugging-your-new-PL
word_count: 691
---

Say you’re building a new (compiled) programming language from scratch. You’ll
inevitably have to debug programs written in it, and worse, many of these
problems will lead you into deep magic, as you uncover problems with your
compiler or runtime. And as you find yourself diving into the arcane arts, your
tools may be painfully lacking: how do you debug code written in a language for
which debuggers and other tooling simply has not been written yet?

In the implementation of my own programming language, I have faced this problem
many times, and developed, by necessity, some skills around debugging with
crippled tools that may lack an awareness of your language. Of course, the
ultimate goal is to build out first-class debugging support, but we must have a
language in the first place before we can write tools to debug it. If you find
yourself in this situation, here are my recommendations.

First, I’ll echo the timeless words of Brian Kernighan:

> The most effective debugging tool is still careful thought, coupled with
> judiciously placed print statements.

— Unix for Beginners (1979)

Classic debugging techniques are of heightened importance in this environment:
first seek to isolate the problem code, then to understand the problem code,
then form, and test, a hypothesis — usually with a thoughtful print
statement. Often, this is enough.

Unfortunately, you may have to fire up gdb. gdb is often painful in the best of
situations, but if you have to use it without debug symbols, you may find
yourself shutting off the computer and seeking out rural real estate on which
you can establish a new career in farming. If you can stomach it, I can offer
some advice.

First, you’re going to be working in assembly, so make sure you’re familiar with
how it works. I would recommend keeping the ISA manual and your ABI
specification handy. If you’re smart and your language sets up stack frames
properly (this is easy, do it early), you should at least have a backtrace,
breakpoints at functions, and globals, though all of these will be untyped. You
can write C casts to add some ad-hoc types to examine data in your process,
like “print *(int *)$rdi”.

You’ll also get used to the ‘x’ command, which eXamines memory. The command
format is “x/NT”, where N is the number of objects, and T is the object type: w
for word (int), g for giantword (long), and h and b for halfword (short) and
byte, respectively: “x/8g $rdi” will interpret rdi as an address where 8 longs
are stored and print them out in hexadecimal. Of particular use is the “i”
format, for “instruction”, which will disassemble from the given address:

```
(gdb) x/8i $rip
=> 0x5555555565c8 <rt.memcpy+4>:	mov    $0x0,%eax
   0x5555555565cd <rt.memcpy+9>:	cmp    %rdx,%rax
   0x5555555565d0 <rt.memcpy+12>:	jae    0x5555555565df <rt.memcpy+27>
   0x5555555565d2 <rt.memcpy+14>:	movzbl (%rsi,%rax,1),%ecx
   0x5555555565d6 <rt.memcpy+18>:	mov    %cl,(%rdi,%rax,1)
   0x5555555565d9 <rt.memcpy+21>:	add    $0x1,%rax
   0x5555555565dd <rt.memcpy+25>:	jmp    0x5555555565cd <rt.memcpy+9>
   0x5555555565df <rt.memcpy+27>:	leave  
```

You can set breakpoints on the addresses you find here (e.g. “b
*0x5555555565d0”), and step through one instruction at a time with the “si”
command.

I also tend to do some silly workarounds to avoid having to read too much
assembly. If I want to set a breakpoint in some specific place, I might do the
following:

```
fn _break() void = void;

export fn main() void = {
    // ...some code...

    // Point of interest
    let x = y[z * q];
    _break();
    somefunc(x);

    // ...some code...
};
```

Then I can instruct gdb to “b _break” to break when this function is called,
use “finish” to step out of the call frame, and I’ve arrived at the point of
interest without having to rely on line numbers being available in my binary.

Overall, this is a fairly miserable process which can take 5-10× longer
than normal debugging, but with these tips you should at least find your
problems solvable. Good motivation to develop better debugging tools for your
new language, eh? A future blog post might go over some of this with DWARF and
possibly how to teach gdb to understand a new language natively. In the
meantime, good luck!
