---
title: "Porting Doom to Helios"
date: 2022-07-01
url: https://drewdevault.com/2022/07/01/Porting-DOOM-to-Helios.html
slug: Porting-DOOM-to-Helios
word_count: 2379
---

[Doom](https://en.wikipedia.org/wiki/Doom_(1993_video_game))  was an incredibly popular video game by Id software which, six years
following its release, was made  [open source](https://github.com/id-Software/DOOM)  under the GPLv2 license. Thanks to
this release, combined with the solid software design and lasting legacy of
backwards compatibility in C, Doom has been ported to countless platforms by
countless programmers. And I recently added myself to this number :)

I’m working on a new kernel called  [Helios](https://sr.ht/~sircmpwn/helios) , and I thought that porting Doom
would present a good opportunity for proving the kernel design — you never
know if you have a good design until you try to use it for real. Doom is a good
target because it does not require much to get working, but it is a useful (and
fun) program to port. It calls for the following features:

1. A working C programming environment
2. Dynamic memory allocation
3. A place to draw the screen (a framebuffer)
4. Keyboard input

As I was working, I gradually came to understand that Helios was pretty close to
supporting all of these features, and thought that the time to give Doom a shot
was coming soon. In my  [last status update](https://drewdevault.com/2022/06/15/Status-update-June-2022.html) , I shared a picture of a Helios
userspace program utilizing the framebuffer provided by multiboot, ticking one
box. We’ve had dynamic memory allocation in userspace working since June 8th.
The last pieces were a keyboard driver and a C library.

I started with the keyboard driver, since that would let me continue to work on
Hare for a little bit longer, providing a more direct benefit to the long-term
goals (rather than the short-term goal of “get Doom to work”). Since Helios is a
micro-kernel, the keyboard driver is implemented in userspace. A PS/2 keyboard
driver requires two features which are reserved to ring 0: I/O ports and IRQ
handling. To simplify the interface to the essentials for this use-case,
pressing or releasing a key causes IRQ 1 to be fired on the PIC, then reading
from port 0x60 provides a scancode. We already had support for working with I/O
ports in userspace, so the blocker here was IRQ handling.

Helios implements IRQs similarly to seL4, by using a “notification” object (an
IPC primitive) which is signalled by the kernel when an IRQ occurs. I was
pleased to have this particular blocker, as developing out our IPC
implementation further was a welcome task. The essential usage of a notification
involves two operations: wait and signal. The former blocks until the
notification is signalled, and the later signals the notification and unblocks
any tasks which are waiting on it. Unlike sending messages to endpoints, signal
never blocks.

After putting these pieces together, I was able to write a simple PS/2 keyboard
driver which echos pressed keys to the kernel console:

```
const irq1_notify = helios::newnotification()?;
const irq1 = helios::irqcontrol_issue(rt::INIT_CAP_IRQCONTROL, irq1_notify, 1)?;
const ps2 = helios::iocontrol_issue(rt::INIT_CAP_IOCONTROL, 0x60, 0x64)?;

for (true) {
	helios::wait(irq1_notify)?;
	const scancode = helios::ioport_in8(ps2, 0x60)?;
	helios::irq_ack(irq1)!;
};
```

This creates a notification capability to wait on IRQs, then creates a
capability for IRQ 1 registered for that notification. It also issues an I/O
port capability for the PS/2 ports, 0x60-0x64 (inclusive). Then it loops,
waiting until an interrupt occurs, reading the scancode from the port, and
printing it. Simple!

I now turned my attention to a C library for Doom. The first step for writing
userspace programs in C for a new operating system is to produce a suitable C
cross-compiler toolchain. I adapted the instructions from  [this OSdev wiki
tutorial](https://wiki.osdev.org/GCC_Cross-Compiler)  for my needs and produced
the working patches for  [binutils](https://git.sr.ht/~sircmpwn/binutils/commit/b104dee8b4d5f6fb57d585132775e22f0eba80df)  and  [gcc](https://git.sr.ht/~sircmpwn/gcc/commit/20df2b4d99670f2db51f84dc57d2253fd71d0b2b) . I started on a simple C library
that included  [some assembly glue](https://git.sr.ht/~sircmpwn/mercury/tree/f80bb66373ab12a66a9a86894d212cbbdfcf53bf/item/libc/syscall.s)  for syscalls,  [an entry point](https://git.sr.ht/~sircmpwn/mercury/tree/f80bb66373ab12a66a9a86894d212cbbdfcf53bf/item/libc/crt) , and
 [a couple of syscall wrappers](https://git.sr.ht/~sircmpwn/mercury/tree/1217b54b7bd09bebcd672d1e9cdae14f2e2e545f/item/libc/syscalls.c) . With great anticipation, I wrote the
following C program and loaded it into Helios:

```
#include <helios/syscall.h>
#include <string.h>

int main() {
	const char *message = "Hello from userspace in C!\n";
	sys_writecons(message, strlen(message));
	return 0;
}
```

```
$ qemu-system-x86_64 -m 1G -no-reboot -no-shutdown \
	-drive file=boot.iso,format=raw \
	-display none \
	-chardev stdio,id=char0 \
	-serial chardev:char0
Booting Helios kernel
Hello from userspace in C!
```

Woohoo! After a little bit more work setting up the basics, I started rigging
 [doomgeneric](https://github.com/ozkl/doomgeneric)  (a Doom fork designed to be easy to port) up to my cross
environment and seeing what would break.

As it turned out, a lot of stuff would break. doomgeneric is designed to be
portable, but it actually depends on a lot of stuff to be available from the C
environment: stdio, libmath, string.h stuff, etc. Not too much, but more than I
cared to write from scratch. So, I started pulling in large swaths of  [musl
libc](https://musl.libc.org) , trimming out as much as I could, and wriggling it into a buildable state.
I also wrote a lot of shims to fake out having a real Unix system to run it in,
like this code for defining stdout & stderr to just write to the kernel console:

```
static size_t writecons(FILE *f, const unsigned char *buf, size_t size) {
	sys_writecons(f->wbase, f->wpos - f->wbase);
	sys_writecons(buf, size);
	f->wend = f->buf + f->buf_size;
	f->wpos = f->wbase = f->buf;
	return size;
}

#undef stdout
static unsigned char stdoutbuf[BUFSIZ+UNGET];
hidden FILE __stdout_FILE = {
	.buf = stdoutbuf+UNGET,
	.buf_size = sizeof stdoutbuf-UNGET,
	.fd = 1,
	.flags = F_PERM | F_NORD,
	.lbf = '\n',
	.write = &writecons,
	.seek = NULL,
	.close = NULL,
	.lock = -1,
};
FILE *const stdout = &__stdout_FILE;
FILE *volatile __stdout_used = &__stdout_FILE;

#undef stderr
static unsigned char stderrbuf[UNGET];
hidden FILE __stderr_FILE = {
	.buf = stderrbuf+UNGET,
	.buf_size = 0,
	.fd = 2,
	.flags = F_PERM | F_NORD,
	.lbf = -1,
	.write = &writecons,
	.seek = NULL,
	.close = NULL,
	.lock = -1,
};
FILE *const stderr = &__stderr_FILE;
FILE *volatile __stderr_used = &__stderr_FILE;
```

The result of all of this hacking and slashing is quite a mess, and none of this
is likely to be useful in the long term. I did this work over the course of a
couple of afternoons just to get everything “working” enough to support Doom,
but an actual useful C programming environment for Helios is likely some ways
off. Much of the near-term work will be in Mercury, which will be a Hare
environment for writing drivers, and we won’t see a serious look at better C
support until we get to Luna, the POSIX compatibility layer a few milestones
away.

Anyway, in addition to pulling in lots of musl libc, I had to write some
original code to create C implementations of the userspace end for working with
Helios kernel services. Some of this is pretty straightforward, such as the
equivalent of the helios::ioport_issue code from the keyboard driver you saw
earlier:

```
cap_t
iocontrol_issue(cap_t ctrl, uint16_t min, uint16_t max)
{
	uint64_t tag = mktag(IO_ISSUE, 1, 1);
	cap_t cap = capalloc();
	ipc_buffer->caddr = cap;
	struct sysret ret = sys_send(ctrl, tag, min, max, 0);
	assert(ret.status == 0);
	return cap;
}
```

A more complex example is the code which maps a page of physical memory into the
current process’s virtual address space. In Helios, similar to L4, userspace
must allocate its own page tables. However, these page tables are semantically
 *owned*  by userspace, but they’re not actually  *reachable*  by userspace —
the page tables themselves are not mapped into their address space (for obvious
reasons, I hope). A consequence of this is that the user cannot examine the page
tables to determine which, if any, intermediate page tables have to be allocated
in order to perform a desired memory mapping. The solution is to try the mapping
anyway, and if the page tables are missing, the kernel will reply telling you
which table it needs to complete the mapping request. You allocate the
appropriate table and try again.

Some of this workload falls on userspace. I had already done this part in Hare,
but I had to revisit it in C:

```
struct sysret
page_map(cap_t page, cap_t vspace, uintptr_t vaddr)
{
	uint64_t tag = mktag(PAGE_MAP, 1, 1);
	ipc_buffer->caps[0] = vspace;
	return sys_send(page, tag, (uint64_t)vaddr, 0, 0);
}

static void
map_table(uintptr_t vaddr, enum pt_type kind)
{
	int r;
	cap_t table;
	switch (kind) {
	case PT_PDPT:
		r = retype(&table, CT_PDPT);
		break;
	case PT_PD:
		r = retype(&table, CT_PD);
		break;
	case PT_PT:
		r = retype(&table, CT_PT);
		break;
	default:
		assert(0);
	}
	assert(r == 0);

	struct sysret ret = page_map(table, INIT_CAP_VSPACE, vaddr);
	if (ret.status == -MISSING_TABLES) {
		map_table(vaddr, ret.value);
		map_table(vaddr, kind);
	}
}

void *
map(cap_t page, uintptr_t vaddr)
{
	while (1) {
		struct sysret ret = page_map(page, INIT_CAP_VSPACE, vaddr);
		if (ret.status == -MISSING_TABLES) {
			map_table(vaddr, ret.value);
		} else {
			assert(ret.status == 0);
			break;
		}
	}
	return (void *)vaddr;
}
```

Based on this work, I was able to implement a very stupid malloc, which rounds
all allocations up to 4096 and never frees them. Hey! It works, okay?

```
uintptr_t base = 0x8000000000;

static cap_t
page_alloc()
{
	cap_t page;
	int r = retype(&page, CT_PAGE);
	assert(r == 0);
	return page;
}

void *
malloc(size_t n)
{
	if (n % 4096 != 0) {
		n += 4096 - (n % 4096);
	}
	uintptr_t ret = base;
	while (n != 0) {
		cap_t page = page_alloc();
		map(page, base);
		base += 4096;
		n -= 4096;
	}
	return (void *)ret;
}
```

There is also  [devmap](https://git.sr.ht/~sircmpwn/mercury/tree/f80bb66373ab12a66a9a86894d212cbbdfcf53bf/item/libc/helios/device.c) , which you can read in your own time, which is used for
mapping device memory into your address space. This is neccessary to map the
framebuffer. It’s more complex because it has to allocate a  *specific*  physical
page address into userspace, rather than whatever page happens to be free.

So, to revisit our progress, we have:

✓ A working C programming environment

✓ Dynamic memory allocation

✓ A place to draw the screen (a framebuffer)

✓ Keyboard input

It’s time for Doom, baby. Doomgeneric expects the porter to implement the
following functions:

* DG_Init
* DG_DrawFrame
* DG_GetKey
* DG_SetWindowTitle
* DG_SleepMs
* DG_GetTicksMs

Easy peasy. Uh, except for that last one. I forgot that our requirements list
should have included a means of sleeping for a specific period of time.
Hopefully that won’t be a problem later.

I started with DG_Init, allocating the pieces that we’ll need and stashing the
important bits in some globals.

```
int fb_width, fb_height, fb_pitch;
uint8_t *fb;
cap_t irq1_notify;
cap_t irq1;
cap_t ps2;

void DG_Init()
{
	uintptr_t vbeaddr = bootinfo->arch->vbe_mode_info;
	uintptr_t vbepage = vbeaddr / 4096 * 4096;
	struct vbe_mode_info *vbe = devmap(vbepage, 1) + (vbeaddr % 4096);
	fb_width = vbe->width;
	fb_height = vbe->height;
	fb_pitch = vbe->pitch;
	assert(vbe->bpp == 32);
	unsigned int npage = (vbe->pitch * vbe->height) / 4096;
	fb = devmap((uintptr_t)vbe->framebuffer, npage);

	irq1_notify = mknotification();
	irq1 = irqcontrol_issue(INIT_CAP_IRQCONTROL, irq1_notify, 1);
	ps2 = iocontrol_issue(INIT_CAP_IOCONTROL, 0x60, 0x64);
}
```

If the multiboot loader is configured to set up a framebuffer, it gets handed
off to the kernel, and Helios provides it to userspace as mappable device
memory, so that saves us from doing all of the annoying VBE crap (or heaven
forbid, write an actual video driver). This lets us map the framebuffer into our
process. Second, we do the same notification+IRQ+IOControl thing we did from the
keyboard driver you saw earlier, except in C, so that we can process scancodes
later.

Next is DG_DrawFrame, which is pretty straightforward. We just copy scanlines
from the internal buffer to the framebuffer whenever it asks us to.

```
void DG_DrawFrame()
{
  for (int i = 0; i < DOOMGENERIC_RESY; ++i) {
    memcpy(fb + i * fb_pitch, DG_ScreenBuffer + i * DOOMGENERIC_RESX, DOOMGENERIC_RESX * 4);
  }
}
```

Then we have DG_GetKey, similar to our earlier keyboard driver, plus actually
interpeting the scancodes we get, plus making use of a new non-blocking wait
syscall I added to Helios:

```
int DG_GetKey(int *pressed, unsigned char *doomKey)
{
	struct sysret ret = sys_nbwait(irq1_notify);
	if (ret.status != 0) {
		return 0;
	}

	uint8_t scancode = ioport_in8(ps2, 0x60);
	irq_ack(irq1);

	uint8_t mask = (1 << 7);
	*pressed = (scancode & mask) == 0;
	scancode = scancode & ~mask;
	switch (scancode) {
	case K_AD05:
		*doomKey = KEY_ENTER;
		break;
	case K_AE08:
		*doomKey = KEY_UPARROW;
		break;
	case K_AD07:
		*doomKey = KEY_LEFTARROW;
		break;
	case K_AD08:
		*doomKey = KEY_DOWNARROW;
		break;
	case K_AD09:
		*doomKey = KEY_RIGHTARROW;
		break;
	case K_AB03:
		*doomKey = KEY_FIRE;
		break;
	case K_AB06:
		*doomKey = KEY_USE;
		break;
	case 1:
		*doomKey = KEY_ESCAPE;
		break;
	}

	return *doomKey;
}
```

Then, uh, we have a problem. Here’s what I ended up doing for DG_SleepMs:

```
uint32_t ticks = 0;

void DG_SleepMs(uint32_t ms)
{
	// TODO: sleep properly
	int64_t _ms = ms;
	while (_ms > 0) {
		sys_yield();
		ticks += 5;
		_ms -= 5;
	}
}

uint32_t DG_GetTicksMs()
{
	return ticks;
}
```

Some fellow on IRC said he’d implement a sleep syscall for Helios, but didn’t
have time before I was ready to carry on with this port. So instead of trampling
on his feet, I just yielded the thread (which immediately returns to the caller,
since there are no other threads at this point) and pretend it took 5ms to do
so, hoping for the best. It does not work! This port plays at wildly different
speeds depending on the performance of the hardware you run it on.

I’m not too torn up about it, though. My goal was not to make a particularly
nice or fully featured port of Doom. The speed is problematic, I hardcoded the
shareware doom1.wad as the only supported level, you can’t save the game, and it
crashes when you try to pick up the shotgun. But it does its job: it
demonstrates the maturity of the kernel’s features thus far and provides good
feedback on the API design and real-world utility.

If you’d like to try it, you can  [download a bootable ISO](https://redacted.moe/f/0f2b716a.iso) .

You can run it on qemu like so:

```
$ qemu-system-x86_64 -m 1G -no-reboot -no-shutdown \
		-drive file=doom.iso,format=raw \
		-display sdl \
		-chardev stdio,id=char0 \
		-serial chardev:char0
```

Enter to start, WASD to move, right shift to fire, space to open doors. It
 *might*  work on real hardware, but the framebuffer stuff is pretty hacky and not
guaranteed to work on most stuff, and the PS/2 keyboard driver will only work
with a USB keyboard if you have legacy USB emulation configured in your BIOS,
and even then it might not work well. YMMV. It works on my ThinkPad X230. Have
fun!
