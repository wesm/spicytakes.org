---
title: "Day 4: Processes vs threads, and kernel modules!"
date: 2013-10-04
url: https://jvns.ca/blog/2013/10/04/day-4-processes-vs-threads/
slug: day-4-processes-vs-threads
word_count: 302
---


There was Linux Kernel Club again yesterday! We spent about half our
time having [Daphne](https://github.com/lifeissweetgood) explain the
difference between a process and a thread which clarified my brain a
bit. Here’s what I understood:


Processes each have their own PID and *address space*, threads share the
PID and address space of a single process.


## What is *address space*?


Each process has a piece of memory that it’s allowed to use, so that
processes can’t step on each others’ toes.


This includes

- the *code* or *text* of the program
- the program’s *data* (strings and constants)
- the *heap* (grows dynamically, where the memory allocated using `malloc` lives)
- the stack (a fixed size, where local variables and functions calls
live. Relevant terms: *stack overflow*, *stack trace*)
- the environment variables
- the command line arguments


There also appear to be a bunch more things listed on
[this page on kernel.org](https://www.kernel.org/doc/gorman/html/understand/understand007.html).
I’m not sure what most of them mean, but see the list starting with
``The meaning of each of the field in this sizable struct is as follows: ‘’.


## Why threads?


Good things:

- They can communicate more easily between each other, because they can
just write to the same memory
- Don’t need to make a copy of the address space for each new thread


Bad things:

- Because they write to the same memory, you can have all kinds of race
conditions. So you need to use mutexes and things.


## Kernel modules


We also talked about kernel modules. The consensus was that writing a
kernel module is a really good way to get started with Linux kernel
development, so I think I’m going to try to write one on Monday!


We talked a bit about exploits and rootkits and dastardly things that
kernel modules can do.
