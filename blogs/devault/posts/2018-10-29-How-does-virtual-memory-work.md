---
title: "How does virtual memory work?"
date: 2018-10-29
url: https://drewdevault.com/2018/10/29/How-does-virtual-memory-work.html
slug: How-does-virtual-memory-work
word_count: 770
---

Virtual memory is an essential part of your computer, and has been for several
decades. In my  [earlier article on pointers](/2016/05/28/Understanding-pointers.html) , I compared memory to a
giant array of octets (bytes), and explained some of the abstractions we make
on top of that. In actual fact, memory is more complicated than a flat array of
bytes, and in this article I’ll explain how.

An astute reader of my earlier article may have considered that pointers on,
say, an x86_64 system, are 64 bits long 1 . With this, we can address up to
18,446,744,073,709,551,616 bytes (16 exbibytes 2 ) of memory. I only have 16
GiB of RAM on this computer, so what gives? What’s the rest of the address space
for? The answer: all kinds of things! Only a small subset of your address space
is mapped to physical RAM. A system on your computer called the MMU, or Memory
Management Unit, is responsible for managing the abstraction that enables this
and other uses of your address space. This abstraction is called virtual memory.

The kernel interacts directly with the MMU, and provides syscalls like
[mmap(2)][mmap] for userspace programs to do the same. Virtual memory is
typically allocated a page at a time, and given a purpose on allocation, along
with various flags (documented on the mmap page). When you call  `malloc` , libc
uses the mmap syscall to allocate pages of heap, then assigns a subset of that
to the memory you asked for. However, since many programs can run concurrently
on your system and may request pages of RAM at any time, your physical RAM can
get fragmented.  Each time the kernel hits a context switch 3 , it swaps out
the page table for the next process.

This is used in this way to give each process its own clean address space and to
provide memory isolation between processes, preventing them from accessing each
other’s memory. Sometimes, however, in the case of shared memory, the same
physical memory is deliberately shared with multiple processes.  Many pages can
also be any combination readable, writable, or executable - the latter meaning
that you could jump to it and execute it as native code.  Your compiled program
is a file, after all - mmap some executable pages, load it into memory, jump to
it, and huzzah: you’re running your program 4 . This is how JITs, dynamic
recompiling emulators, etc, do their job. A common way to reduce risk here,
popular on *BSD, is enforcing W^X (writable XOR executable), so that a page can
be either writable or executable, but never both.

Sometimes all of the memory you think you have isn’t actually there, too. If you
blow your RAM budget across your whole system, swap gets involved. This is when
pages of RAM are “swapped” to disk - as soon as your program tries to access it
again, a page fault occurs, transferring control to the kernel. The kernel
restores from swap, damning some other poor process to the fate, and returns
control to your program.

Another very common use for virtual memory is for memory mapped I/O. This can
be, for example, mapping a file to memory so you can efficiently read and write
to disk. You can map other sorts of hardware, too, such as video memory. On 8086
(which is what your computer probably pretends to be when it initially
boots 5 ), a simple 96x64 cell text buffer is available at address  `0xB8000` .
On my TI-Nspire CX calculator, I can read the current time from the real-time
clock at  `0x90090000` .

In summary, MMUs arrived almost immediately on the computing scene, and have
become increasingly sophisticated ever since. Virtual memory is a powerful tool
which grants userspace programmers elegant, convenient, and efficient access to
the underlying hardware.

1. Fun fact: most x86_64 implementations actually use 48 bit addresses internally, for a maximum theoretical limit of 256 TiB of RAM. ↩︎
2. I had to look that SI prefix up. This number is 264, by the way. ↩︎
3. This means to switch between which process/thread is currently running on a single CPU. I’ll write an article about this sometime.
[mmap]: [http://man7.org/linux/man-pages/man2/mmap.2.html](http://man7.org/linux/man-pages/man2/mmap.2.html) ↩︎
4. There are actually at least a dozen other steps involved in this process. I’ll write an article about loaders at some point, too. ↩︎
5. You can make it stop pretending to do this with [an annoying complicated sequence of esoteric machine code instructions](https://wiki.osdev.org/Protected_Mode). An even more annoying sequence is required to [enter 64-bit mode](https://wiki.osdev.org/Setting_Up_Long_Mode). It gets even better if you want to set up [multiple CPU cores](https://wiki.osdev.org/Symmetric_Multiprocessing)! ↩︎
