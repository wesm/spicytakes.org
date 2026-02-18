---
title: "Status update, July 2022"
date: 2022-07-18
url: https://drewdevault.com/2022/07/18/Status-update-July-2022.html
slug: Status-update-July-2022
word_count: 523
---

Hello there! It’s been a hot July week in Amsterdam, and I expect hotter days
are still to come. I wish air conditioning was more popular in Europe, but alas.
This month of FOSS development enjoyed a lot of small improvements in a lot of
different projects.

For Hare, I have introduced a number of improvements. I wrote a new standard
library module for string templates,  [strings::template](https://docs.harelang.org/strings/template) , and a new third-party
library for working with pixel buffers,  [pixbuf](https://git.sr.ht/~sircmpwn/pixbuf) . The templating is pretty
simple — as is typical for the standard library — but allows a
fairly wide range of formatting options. We’ll be extending this a little bit
more in the future, but it will not be a complete solution like you see in
things like Jinja2. Nevertheless, it makes some use-cases, like code generation,
a lot cleaner, without introducing a weighty or complex dependency.

pixbuf is pretty neat, and is the first in a line of work I have planned for
graphics on Hare. It’s similar to pixman, but with a much smaller scope —
it only deals with pixel buffers, handling pixel format conversions and doing
small operations like fill and copy. In the future I will add simple buffer
compositing as well, and extending modules like  [hare-png](https://git.sr.ht/~sircmpwn/hare-png)  to support loading
data into these buffers. Later, I plan on writing a simple vector graphics
library, capable at least of rendering  [TinyVG](https://tinyvg.tech)  images and perhaps later TinySVG
as well. I’m also working on  [hare-wayland](https://git.sr.ht/~sircmpwn/hare-wayland)  again, to provide a place to display
these buffers.

I also introduced  [format::tar](https://docs.harelang.org/format/tar) , which will serve as the basis of
initramfs-alike functionality for Helios. On the subject of Helios, much work
has been completed. I have implemented a PCI driver and a small proof-of-concept
AHCI driver (for reading from SATA disks). Alexey Yerin has also been hard at
work on the RISC-V port, and has successfully implemented an e1000 ethernet
driver which can send and receive ICMP (ping) packets. I also completed IRQ
control for userspace, so that userspace device drivers can process interrupts,
and used it to write a keyboard driver for a functional  [DOOM port](https://drewdevault.com/2022/07/01/Porting-DOOM-to-Helios.html) . The full
DOOM port required a fair bit of work — check out that blog post for the
complete details. The idle thread was also added, so that all processes can be
blocked waiting on interrupts, signals, endpoints, etc. Non-blocking send,
receive, and wait syscalls were also added this month.

I’m working on splitting memory capabilities into separate device- and
general-purpose capabilities, then adding support for destroying capabilities
when they’re no longer required. I also implemented pre-emptive multi-tasking
early this month, and the vulcan test suite now has several multi-threaded tests
to verify IPC functionality. However, a couple of pieces are missing — the
ability to create and work with new cspaces and vspaces — in order to
spawn new processes. I’ll be focusing on these tasks in the coming weeks. With
these pieces in place, we can start working on Mercury and Vulcan: the driver
system.

I’ll save the SourceHut news for the “what’s cooking” post later today, so
that’s all for now. Until next time!
