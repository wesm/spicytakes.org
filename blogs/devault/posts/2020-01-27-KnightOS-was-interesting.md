---
title: "KnightOS was an interesting operating system"
date: 2020-01-27
url: https://drewdevault.com/2020/01/27/KnightOS-was-interesting.html
slug: KnightOS-was-interesting
word_count: 720
---

[KnightOS](https://knightos.org)  is an operating system I started writing about
10 years ago, for Texas Instruments line of z80 calculators — the TI-73,
TI-83+, TI-84+, and similar calculators are supported. It still gets the rare
improvements, but these days myself and most of the major contributors are just
left with starry eyed empty promises to themselves that one day they’ll do one
of those big refactorings we’ve been planning… for 4 or 5 years now.

Still, it was a really interesting operating system which was working under some
challenging constraints, and overcame them to offer a rather nice Unix-like
environment, with a filesystem, preemptive multiprocessing  *and*  multithreading,
assembly and C programming environments, and more. The entire system was written
in handwritten z80 assembly, almost 50,000 lines of it, on a compiler toolchain
we built from scratch.

There was only 64 KiB of usable RAM. The kernel stored  *all*  of its state in
1024 bytes of statically allocated RAM. Many subsystems used overlapping parts
of this memory, which was carefully planned for to avoid conflicts. The
userspace memory allocator used a simple linked list for tracking allocations,
to minimize the overhead of each allocation and maximize the usable space for
userspace programs. There was no MMU in the sense that we have on modern
computers, so any program could freely overwrite any other programs. In fact,
the “userspace” task switching GUI would read the kernel’s process table
directly to make a list of running programs.

The non-volatile storage was NOR Flash, which presents some interesting
constraints. In the worst case we only had 512 KiB of storage, and even in the
best case just 4MiB (this for a device released in 2013). This space was shared
with the kernel, whose core code was less than 4KiB, and including high-address
subsystems still clocked in at less than 16KiB. Due to the constraints of NOR
Flash, a custom filesystem was designed which did all daily operations by only
 *resetting*  bits in the underlying storage. In order to  *set*  any bits, we had
to set the entire 64 KiB sector to 1. Overhead was also kept to a bare minimum
here to maximize storage space available to users.

Writing to Flash storage also renders it unreadable while the operation is in
progress. The kernel normally executes directly from Flash, resident at the
bottom of the memory. Therefore, in order to modify Flash, the kernel’s Flash
driver copies part of itself to RAM, jumps to it, and then jumps back after the
operation is complete. Recall that all of the kernel’s memory is statically
allocated, and there’s not much of it — we used only 128 bytes for the
code which runs in RAM, and it’s shared with some other stuff that we had to
plan around. In order to meet these constraints, we employ  *self modifying code* 
— the Flash driver copies some of itself into RAM, then pre-computes some
information and  *modifies*  that machine code in-place before jumping to it.

We also had some basic networking support. The calculator has a 2.5mm jack,
similar to headphone jacks — if you had a 3.5mm adapter, we had a music
player which would play MIDI or WAV files. The kernel had direct control of the
voltages on the ring and tip, and had to bitbang them directly in software 1 .
Based on this we built some basic networking support, which supported
calculator-to-calculator and calculator-to-PC information exchange. Later models
had a mini-USB controller (which, funnily enough, can also be bitbanged in
software), but we never ended up writing a driver for it.

The KnightOS kernel also includes some code which is the first time I ever wrote
 [“here be dragons”](https://github.com/KnightOS/kernel/blob/e257f54e021ee743306a2a4a5a152860728fb3f8/src/00/restarts.asm#L129-L130) 
into a comment, and I don’t think I’ve topped it since.

Despite these constraints, KnightOS is completely booted up to a useful
Unix-like (with a graphical interface) faster than you can lift your finger off
of the power button. The battery could last the entire semester, if you’re
lucky. Can the device you’re reading this on claim the same? 2

1. Newer hardware revisions had some support hardware which was capable of transferring a single byte without software intervention. ↩︎
2. The device I’m writing this blog post with is 3500× faster than my calculator, has 262,144× more RAM, and 2.1×106 times more storage space. ↩︎
