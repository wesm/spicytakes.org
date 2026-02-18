---
title: "Day 43: SOMETHING IS ERASING MY PROGRAM WHILE IT’S RUNNING (oh wait oops)"
date: 2013-12-16
url: https://jvns.ca/blog/2013/12/16/day-43-hopefully-the-last-day-spent-fixing-linker-problems/
slug: day-43-hopefully-the-last-day-spent-fixing-linker-problems
word_count: 360
---


alternate title: “Hopefully the last day I spend all day trying to
compile my code properly”


(context: I’m working on writing an OS, and am experiencing a
mysterious recurring bug. After many days, I have found the reason!)


Today I went through the following:

1. Decide to try to write some code
2. Upgrade Rust, since my version is 8 days old
3. Oh no, the new Rust breaks my oldish version of [rust-core](http://github.com/thestinger/rust-core)
4. Upgrade rust-core
5. Oh no, the new rust-core requires me to compile in a different way
6. Spend a bunch of time messing with `clang` and friends to get
everything to compile again
7. Everything compiles. Yay!
8. Try to run code
9. Encounter mystery bug again, where my array mysteriously contains
0s instead of its actual contents
10. Make sad faces
11. Go talk to [Allison](http://akaptur.github.io). Allison is the best.
12. Allison asks: “What linker debugging strategies do you have?”
  1. Change the linker script randomly (actual thing that has worked)
  2. Change variable attributes from ‘private’ to ‘public’ at random
(actual other thing that has worked)
  3. Look at the linker map or symbol table (not helpful, so far)
  4. Attach gdb to qemu and inspect the contents of memory (!!!)


gdb is great. It let me

- search my memory for “QWERTY” (not there! why not?)
- look at the memory at a given address (lots of zeros! huh!)
- Do a core dump, and compare it to the original file. Lots of zeros!
Why is half my program gone?


SURPRISE MY CODE IS NOT WORKING BECAUSE SOMETHING IS ERASING IT.


Can we talk about this?

1. I have code
2. I can compile my code
3. Half of my binary gets overwritten with 0s at runtime. Why. What
did I do to deserve this?
4. No wonder the order I put the binary in matters.


It is a wonder that this code even runs, man. Man.


**Edit**: I found why my binary has lots of 0s in it at runtime. It is
because I was only loading 12k of it in `loader.asm`. Hopefully this
will serve as a lesson to someone.
