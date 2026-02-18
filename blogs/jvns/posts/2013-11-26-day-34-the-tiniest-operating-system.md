---
title: "Day 34: The tiniest operating system"
date: 2013-11-26
url: https://jvns.ca/blog/2013/11/26/day-34-the-tiniest-operating-system/
slug: day-34-the-tiniest-operating-system
word_count: 163
---


One of my as-yet-unrealized goals for Hacker School is to write an
operating system, at least a tiny one.


Today I decided to actually start in earnest, because this operating
system isn’t going to write itself! I’ve decided to write an OS for
x86, because I like the idea of being able to run it on my computer in
real life.


I immediately found a super-fantastic resource:
[MikeOS](http://mikeos.berlios.de/write-your-own-os.html), which has
really simple instructions. The only issue I had with them was that I
had to run `kvm` instead of `qemu` to get it to run in the emulator.


If you install `build-essential`, `nasm`, and `qemu`, and clone
[this gist](https://gist.github.com/jvns/7668292), you too will have
the tiniest operating system!


So far all I’ve learned is how to use
[a particular BIOS interrupt handler](https://en.wikipedia.org/wiki/INT_10H),
which lets me write characters to the screen and change the background colour.


Here’s what my OS looks like so far. It prints something, and makes
the background a pinkish colour.


![](https://jvns.ca/images/my-first-os.png)
