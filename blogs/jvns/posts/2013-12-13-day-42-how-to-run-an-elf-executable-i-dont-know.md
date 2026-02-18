---
title: "Day 42: How to run a simple ELF executable, from scratch (I don't know)"
date: 2013-12-13
url: https://jvns.ca/blog/2013/12/13/day-42-how-to-run-an-elf-executable-i-dont-know/
slug: day-42-how-to-run-an-elf-executable-i-dont-know
word_count: 447
---


I want to compile a 32-bit “Hello, world!” statically-linked ELF
binary for Linux, and try to run it in my
[operating system](http://github.com/jvns/puddle). I’m trying to
understand what I’ll have to do. The goal is to get everything just
barely working, so that it will print the string to the screen and not
crash the whole system.


I asked a question about this a little while ago, and got
[lots of helpful responses](https://gist.github.com/jvns/7688286/).
Now I need to make it a bit more concrete, though.


I’ve discovered that this “set stuff up so that a program can run”
business is called **loading**, and what I’m doing is writing a
**loader**. Sweet.


Right now I’m doing this before implementing paging and virtual memory
and not after, because this seems more fun than virtual memory for
now. If this is a very bad idea, I would like to know.


## Things I’ll have to do

1. Compile “hello-c” for a 32-bit OS, with `gcc -m32 -static`
2. Parse the ELF headers (using
[the wikipedia article](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format),
and
[this great picture](https://code.google.com/p/corkami/wiki/ELF101)
as a reference)
3. Add an interrupt handler for `int 80` (or `sysenter`, we’ll see!),
so that I can handle system calls.
4. Write the actual system call implementations, as few as possible.
5. Find `e_entry`, the entry point of the binary.
6. Initialize registers? How?
7. Change *something*, so that the memory addresses in the binary
aren’t broken. Maybe? I still don’t 100% understand this.
8. Finally: Jump to `_start`, the memory address in `e_entry`. I want
to just do `jmp address` here. Then my program will run?


## Things I won’t have to do (yet)

1. Read the file into memory – I’m planning to just keep the file as
a bunch of bytes in RAM to start, or possibly have a simple RAM
filesystem later.
2. Security, and making sure process can’t trample on each others'
address spaces.
3. Scheduling.
4. Set up a special heap for the process. I’m just going to allocate
everyone’s memory in the same part of physical memory for now. And
never free. Yeah.


## Questions I have

1. Do I need to make sure my binary is
[position independent](http://www.airs.com/blog/archives/43)?
2. Do I need to implement virtual memory & paging? (I think not)
3. Do I need to have a separate “user space” for the code to run in,
or will it run in kernel space? (I think it will run in kernel
space)
4. Do I need to change something in the GOT and/or PLT to make the
addresses work right? (I think yes? maybe?) Is there even a PLT in
a static executable, or is that just for dynamic linking? Eep. Hmm.
