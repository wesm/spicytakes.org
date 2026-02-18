---
title: "Some things my kernel can't do"
date: 2014-01-03
url: https://jvns.ca/blog/2014/01/03/what-my-kernel-doesnt-do/
slug: what-my-kernel-doesnt-do
word_count: 391
---


I’m working on a talk for [CUSEC](http://2014.cusec.net/) about how
kernel programming is something that normal humans can do (albeit with
some pain and suffering).


Most people will be pretty unfamiliar with what a kernel is or does.
I’m thinking of explaining it in terms of the kernel I wrote at Hacker
School, and what it can’t do.


Kernel programming has become a lot more concrete to me – I now
totally feel like I could write a production OS if I were given some
hardware, 20 years and an army of volunteers.


So here are some pretty “basic” things that my kernel can’t do. I’m
not trying to give an exhaustive list here, but a flavor for what’s
involved.


The idea is that once you know what a kernel does, you can pick a
Thing and a Kernel, and then dive into it and ask “okay, what *is* the
Linux kernel’s system for tracking processes?”. Then you can find this
page
[about the process table in Linux 2.4](http://www.tldp.org/LDP/lki/lki-2.html),
read some of it, and it’s probably different in the 3.x kernel, but
now you know more.

- Communicate with the hard drive
  - Even if it could, it doesn’t understand any filesystems
- Communicate with the network card to connect to the Internet
  - Even if it could, it doesn’t understand any network protocols like
TCP/IP
- Get out of text-only mode to display graphics
- Run programs securely, so that they can’t overwrite each others'
memory
- Run more than one program at a time (“scheduling”)
- Know what time it is
- Allow a process to sleep for a fixed amount of time
- Put the computer to sleep / turn off the computer


Some higher-level things that depend on those:

- Have a system for tracking processes
- Have a way to manage processes (like signals)
- File permissions
- Provide a way for user programs to interact with hardware (like
`/dev/*`)


These are all pretty approachable concepts (I think). I think I’m not
going to talk about virtual memory because I don’t know if I can
explain it well.


That’s a pretty long list. What *can* my kernel do?

- [Print to the screen](http://jvns.ca/blog/2013/11/29/writing-an-os-using-rustboot-and-rust-core/)
- [Understand keyboard inputs](http://jvns.ca/blog/2013/12/04/day-37-how-a-keyboard-works/)
- [Run programs, almost](http://jvns.ca/blog/2013/12/19/day-45-reading-elf-headers/)
(this isn’t working yet, but I think I’m not too far away)


So not much :)
