---
title: "Redesigning my microkernel from the ground up"
date: 2026-01-12
url: https://drewdevault.com/2026/01/12/2026-01-12-Hermes-from-the-ground-up.html
slug: 2026-01-12-Hermes-from-the-ground-up
word_count: 954
---

[As you may recall](/2022/06/13/helios.html) , circa 2022-2023 I was working on a
microkernel written in Hare named Helios. Helios was largely inspired by and
modelled after the design of  [seL4](https://sel4.systems/)  and was my first
major foray into modern OS development that was serious enough to get to a
somewhat useful state of functionality, with drives for some real hardware,
filesystems, and an environment for running user programs of a reasonable level
of sophistication.

Helios development went strong for a while but eventually it slowed and
eventually halted in a state of design hell. Since Helios was my first major OS
project at this scale and with this much ambition, the design and implementation
ended up with a lot of poor assumptions that made it a pretty weak foundation
for building a complete OS upon. In late 2023 I more or less gave up on it and
moved my OS development work out of the realm of writing code and back into the
realm of thinking really hard about how to design operating systems.

What followed was a couple of years of design thinking, developing small scale
design experiments, and doing deeper research into prior art – reading papers
and studying existing kernels. It was also during this period that I wrote
 [Bunnix](/2024/05/24/2024-05-24-Bunnix.html) , a working Unix clone, motivated in part by a desire to gain some
first-hand experience working in the design and implementation of Unix-style
operating systems – a fertile environment for learning a lot of the nuts and
bolts of OS implementations by working against a complete and proven design.

In August I was finally prepared to have another go. I decided to start over
from scratch, importing and adapting and rewriting code from Helios and Bunnix
on an as-needed basis to speed things up, and writing from scratch anything
where the lessons learned in hindsight outweighed the benefits of adapting
existing code. 1

The result is  [Hermes](https://git.sr.ht/~sircmpwn/hermes) .

Hermes has not yet reached feature parity with Helios, lacking some IPC features
and an aarch64 port, but already it’s significantly more robust and thoughtfully
designed than Helios.

The big glitzy feature that most obviously distinguishes Hermes from Helios is
that Hermes supports symmetric multiprocessing (SMP), which is to say, running
on multiple CPU cores. This time around, I finally listened to the advice I’d
been hearing in osdev circles for years and implemented SMP as early as possible
to avoid dealing with tons of problems adding multiprocessing to an otherwise
mature kernel.

The multicore scheduler at the heart of Hermes is surprisingly simple, actually.
It uses relatively ordinary per-CPU run queues. Each new task, once scheduleable,
is scheduled, in order of preference, on (1) the CPU matching its affinity, (2)
any currently idle CPU, or (3) a random CPU. If a CPU would idle, it first tries
to  [steal](https://en.wikipedia.org/wiki/Work_stealing)  a pending task from another CPU. The most important
parts of the scheduler are less than 200 lines of code ( [[1]](https://git.sr.ht/~sircmpwn/hermes/tree/main/item/sched/sched.ha) ,  [[2]](https://git.sr.ht/~sircmpwn/hermes/tree/main/item/sched/runq.ha) ).

The less obviously impressive improvements from Helios to Hermes are numerous.
The syscall and IPC ABIs were rethought from the ground up – one of the major
goals of the redesign. I also moved from an seL4-style capability derivation
graph – which is quite complex to implement and reason about – to reference
counting to manage the lifetimes of kernel resources. Resource management in
general is much simpler and should improve the performance of the kernel
substantially.

I’ve also taken a much different approach to organizing the code, to allow the
kernel and many of the things around it – its bootloaders and the userspace
that runs the kernel test suite – share a lot more code than was possible in
Helios, making a lot of the non-kernel code a lot easier to write and maintain.

The userspace is also a substantial upgrade in design from Helios, or at least I
hope it will be when more of it takes shape. Rather than developing a
specialized Hare standard library, independent of the upstream Hare standard
library, for writing drivers and low-level services, I have started with a port
of the upstream Hare standard library and built low-level driver and service
support libraries around it. The userspace is streamlined considerably by doing
so, giving these low-level components access to a more comfortable and
featureful programming environment and reducing the complexity of the system by
making various components more uniform in their design.

Finally, I’ve taken a much more serious approach to testing Hermes and making
it as robust and complete as possible in real-world use-cases. I borrowed the
EFI bootloader from Bunnix and repurposed it for Hermes, opening up a lot of
newer hardware, and I have written a more comprehensive test suite and run and
verified it on much more real-world hardware. I have about ten devices which all
(consistently!) pass the Hermes test suite. Feel free to  [try it out on
yours](https://redacted.moe/dl/69a8581c.iso)  as well and let me know how it goes!

That’s all there is to say for now, but I hope to keep you in the loop as I
continue working on this for a while. The userspace is starting to take shape
and soon(™) I hope to start building out block device drivers, some filesystems,
and enough support code to run a shell and a handful of useful programs. In the
meantime, feel free to poke around the code and play around with it. There is
also some  [early documentation](https://hermes.ares-os.org/)  available for you
to read if you wish. I’m hanging out in #ares on Libera Chat if you have any
questions.

1. I also took the opportunity to acknowledge critics of my internally inconsistent naming scheme, and started choosing codenames within a single pantheon. ↩︎
