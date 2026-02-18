---
title: "Day 44: qemu + gdb = so great"
date: 2013-12-17
url: https://jvns.ca/blog/2013/12/17/day-44-gdb-is-great/
slug: day-44-gdb-is-great
word_count: 331
---


Today I did some more debugging and cleaning up. Previously I was
setting up my IDT (interrupt descriptor table) with assembly, but I
wanted to do it with Rust, because I don’t really know assembly and
the less of it I have in my OS, the less of a liability it is. I’d
tried to do this before, but it wasn’t working.


What turned out to be wrong:

- I had `1 << 16 - 1` instead of `(1 << 16) - 1`, so my mask wasn’t
working properly
- I had the wrong function name for the interrupt handler
- That was it!


This actually ended up being really easy to debug! “Really easy” as in
“it took all day, but I did not feel like hiding under the table at
any point”. I have a symbol table, and `idt` is in it, so I just
needed to do iterations on


```
gdb) x/4x &idt

```


and compare the contents of memory from Working Code with the
Non-Working Code.


`x/` means “examine”, and `4x` means “as hex, 4 times`. Here’s some
[documentation for examining memory](https://sourceware.org/gdb/onlinedocs/gdb/Memory.html).


Comparing sections of memory and figuring out why they’re wrong is
tedious, but pretty straightforward – I had a good handle on what
all my code was doing. Pretty exciting. Best friends, gdb.


`gdb` isn’t totally the best interface – I can certainly imagine
having better ones. But it is Very Useful. So far I know how to

- Find the address of a symbol in memory
- Look at memory (as ints, as hex, as ASCII)
- Search memory
- Set breakpoints (and look at assembly that I don’t understand)
- Make core dumps to look at later


These are pretty awesome superpowers already, and I’m sure there are
tons more.


So now my interrupt handlers are set up in Rust! This will make it
much easier for me to implement `int 80`, and therefore move towards
being able to run programs! Excellent! Onwards!
