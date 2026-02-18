---
title: "Status update, October 2022"
date: 2022-10-15
url: https://drewdevault.com/2022/10/15/Status-update-October-2022.html
slug: Status-update-October-2022
word_count: 989
---

After a few busy and stressful months, I decided to set aside October to rest.
Of course, for me, rest does not mean a cessation of programming, but rather a
shift in priorities towards more fun and experimental projects. Consequently, it
has been a great month for Helios!

Hare upstream has enjoyed some minor improvements, such as from Pierre Curto’s
patch to support parsing IPv6 addresses with a port (e.g. “[::1]:80”) and Kirill
Primak’s improvements to the UTF-8 decoder. On the whole, improvements have been
conservative. However, queued up for integration once qbe upstream support is
merged is support for @threadlocal variables, which are useful for Helios and for
ABI compatibility with C. I also drafted up a proof-of-concept for @inline
functions, but it still needs work.

Now for the main event: Helios. The large-scale redesign and refactoring I
mentioned in the previous status update is essentially complete, and the kernel
reached (and exceeded) feature parity with the previous status quo. Since Helios
has been my primary focus for the past couple of weeks, I have a lot of news to
share about it.

First, I got back into userspace a few days after the last status update, and
shortly thereafter implemented a new scheduler. I then began to rework the
userspace API (uapi) in the kernel, which differs substantially from its prior
incarnation. The kernel object implementations present themselves as a library
for kernel use, and the new uapi module handles all interactions with this
module from userspace, providing a nice separation of concerns. The uapi module
handles more than syscalls now — it also implements send/recv for kernel
objects, for instance. As of a few days ago, uapi also supports delivering
faults to userspace supervisor processes:

```
@test fn task::pagefault() void = {
	const fault = helios::newendpoint()!;
	defer helios::destroy(fault)!;

	const thread = threads::new(&_task_pagefault)!;
	threads::set_fault(thread, fault)!;
	threads::start(thread)!;

	const fault = helios::recv_fault(fault);
	assert(fault.addr == 0x100);

	const page = helios::newpage()!;
	defer helios::destroy(page)!;
	helios::map(rt::vspace, 0, map_flags::W | map_flags::FIXED, page)!;

	threads::resume(thread)!;
	threads::join(thread)!;
};

fn _task_pagefault() void = {
	let ptr: *int = 0x100: uintptr: *int;
	*ptr = 1337;
	assert(*ptr == 1337);
};
```

The new userspace threading API is much improved over the hack job in the
earlier design. It supports TLS and many typical threading operations, such as
join and detach. This API exists mainly for testing the kernel via Vulcan, and
is not anticipated to see much use beyond this (though I will implement pthreads
for the POSIX C environment at some point). For more details, see  [this blog
post](https://drewdevault.com/2022/10/02/Kernel-hacking-with-Hare-part-2.html) . Alongside this and other userspace libraries, Vulcan has been fleshed
out into a kernel test suite once again, which I have been frequently testing on
real hardware:

[Here’s an ISO](https://redacted.moe/f/f95549d6.iso)  you can boot on your own x86_64
hardware to see if it works for you, too. If you have problems, take a picture
of the issue, boot Linux and  [email me](mailto:sir@cmpwn.com)  said picture, the
output of lscpu, and any other details you deem relevant.

The kernel now supports automatic capability address allocation, which is a
marked improvement over seL4. The new physical page allocator is also much
improved, as it supports allocation and freeing and can either allocate pages
sparsely or continuously depending on the need. Mapping these pages in userspace
was also much improved, with a better design of the userspace virtual memory map
and a better heap, complete with a (partial) implementation of mmap.

I have also broken ground on the next component of the OS,  [Mercury](https://git.sr.ht/~sircmpwn/mercury) , which
provides a more complete userspace environment for writing drivers. It has a
simple tar-based initramfs based on Hare’s format::tar implementation, which I
wrote in June for this purpose. It can load ELF files from this tarball into new
processes, and implements some extensions that are useful for driver loading.
Consequently, the first Mercury driver is up and running:

This driver includes a simple driver manifest, which is embedded into its ELF
file and processed by the driver loader to declaratively specify the
capabilities it needs:

```
[driver]
name=pcserial
desc=Serial driver for x86_64 PCs

[cspace]
radix=12

[capabilities]
0:endpoint =
1:ioport = min=3F8, max=400
2:ioport = min=2E8, max=2F0
3:note = 
4:irq = irq=3, note=3
5:irq = irq=4, note=3
```

The driver loader prepares capabilities for the COM1 and COM2 I/O ports, as well
as IRQ handlers for IRQ 3 and 4, based on this manifest, then loads them into
the capability table for the driver process. The driver is sandboxed very
effectively by this: it can  *only*  use these capabilities. It cannot allocate
memory, modify its address space, or even destroy any of these capabilities. If
a bad actor was on the other end of the serial port and exploited a bug, the
worst thing it could do is crash the serial driver, which would then be rebooted
by the supervisor. On Linux and other monolithic kernels like it, exploiting the
serial driver compromises the entire operating system.

The resulting serial driver implementation is pretty small and straightforward,
 [if you’d like to have a look](https://git.sr.ht/~sircmpwn/mercury/tree/master/item/drivers/x86_64/serial) .

This manifest format will be expanded in the future for additional kinds of
drivers, such as with details specific to each bus (i.e. PCI vendor information
or USB details), and will also have details for device trees when RISC-V and
ARM support (the former is already underway) are brought upstream.

Next steps are to implement an I/O abstraction on top of IPC endpoints, which
first requires call & reply support — the latter was implemented last
night and requires additional testing. Following this, I plan on writing a
getty-equivalent which utilizes this serial driver, and a future VGA terminal
driver, to provide an environment in which a shell can be run. Then I’ll
implement a ramfs to host commands for the shell to run, and we’ll really be
cookin’ at that point. Disk drivers and filesystem drivers will be next.

That’s all for now. Quite a lot of progress! I’ll see you next time.
