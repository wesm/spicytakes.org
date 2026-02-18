---
title: "Day 3: What does the Linux kernel even do?"
date: 2013-10-02
url: https://jvns.ca/blog/2013/10/02/day-3-what-does-the-linux-kernel-even-do/
slug: day-3-what-does-the-linux-kernel-even-do
word_count: 214
---


We had a really fun session this morning where we got together and made
a list of the different functions that Linux kernel takes care of.
Tomorrow we’re going to go into more details on some specific parts of
the kernel. So exciting.


(there are comments now! If some of these things are wrong, comment?)


Here are the systems we came up with, in no particular order:

- memory management (RAM)
- device drivers (keyboard, network, graphics card, mouse, monitors,
wireless cards, etc.)
- starting processes
- thread scheduling

- filesystems (ext3, ext4, reiserfs, fat32, etc.)
- VFS: interface that lets you get files no matter what filesystem
you’re using
- UNIX APIs (system calls: here’s [a list](http://asm.sourceforge.net/syscall.html))
- POSIX security model (permissions)
- virtual machines, containers (like LXC)
- networking (bridging, firewalls, protocol implementations like TCP/IP,
UDP, ethernet, ICMP, RPC, wireless).
- IPC (interprocess communication)
- signals (SIGINT, SIGKILL)
- interrupt handlers – handles events from the hardware (packet
received, keypress, timers, graphics card ready, data ready, hard
drive finished reading). Hardware is sometimes handled in other ways
like DMA.
- Timers (when I call `sleep()`)
- Timekeeping (when I ask for the time)
- architecture-specific stuff (amd64, powerpc, x86, MIPS, ARM)
- power management
- loading kernel modules
- kernel debugging tools
