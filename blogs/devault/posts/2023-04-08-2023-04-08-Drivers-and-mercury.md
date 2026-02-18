---
title: "Writing Helios drivers in the Mercury driver environment"
date: 2023-04-08
url: https://drewdevault.com/2023/04/08/2023-04-08-Drivers-and-mercury.html
slug: 2023-04-08-Drivers-and-mercury
word_count: 3034
---

*[Helios](https://git.sr.ht/~sircmpwn/helios) is a microkernel written in the [Hare](https://harelang.org) programming language and is
part of the larger [Ares](https://ares-os.org) operating system. You can watch
my FOSDEM 2023 talk introducing Helios [on PeerTube](https://spacepub.space/w/wpKXfhqqr7FajEAf4B2Vc2).*

Let’s take a look at the new Mercury driver development environment for Helios.

As you may remember from my FOSDEM talk, the Ares operating system is built out
of several layers which provide progressively higher-level environments for an
operating system. At the bottom is the Helios microkernel, and today we’re going
to talk about the second layer: the  [Mercury](https://git.sr.ht/~sircmpwn/mercury)  environment, which is used for
writing and running device drivers in userspace. Let’s take a look at a serial
driver written against Mercury and introduce some of the primitives used by
driver authors in the Mercury environment.

Drivers for Mercury are written as normal ELF executables with an extra section
called .manifest, which includes a file similar to the following (the provided
example is for the serial driver we’ll be examining today):

```
[driver]
name=pcserial
desc=Serial driver for x86_64 PCs

[capabilities]
0:ioport = min=3F8, max=400
1:ioport = min=2E8, max=2F0
2:note = 
3:irq = irq=3, note=2
4:irq = irq=4, note=2
_:cspace = self
_:vspace = self
_:memory = pages=32

[services]
devregistry=
```

Helios uses a capability-based design, in which access to system resources (such
as I/O ports, IRQs, or memory) is governed by capability objects. Each process
has a  *capability space* , which is a table of capabilities assigned to that
process, and when performing operations (such as writing to an I/O port) the
user provides the index of the desired capability in a register when invoking
the appropriate syscall.

The manifest first specifies a list of capabilities required to operate the
serial port. It requests, assigned static capability addresses, capabilities for
the required I/O ports and IRQs, as well as a notification object which the IRQs
will be delivered to. Some capability types, such as I/O ports, have
configuration parameters, in this case the minimum and maximum port numbers
which are relevant. The IRQ capabilities require a reference to a notification
as well.

Limiting access to these capabilities provides very strong isolation between
device drivers. On a monolithic kernel like Linux, a bug in the serial driver
could compromise the entire system, but a vulnerability in our driver could, at
worst, write garbage to your serial port. This model also provides better
security than something like OpenBSD’s pledge by declaratively specifying what
we need and nothing else.

Following the statically allocated capabilities, we request our own capability
space and virtual address space, the former so we can copy and destroy our
capabilities, and the latter so that we can map shared memory to perform reads
and writes for clients. We also request 32 pages of memory, which we use to
allocate page tables to perform those mappings; this will be changed later.
These capabilities do not require any specific address for the driver to work,
so we use “_” to indicate that any slot will suit our needs.

Mercury uses some vendor extensions over the System-V ABI to communicate
information about these capabilities to the runtime. Notes about each of the
_’d capabilities are provided by the auxiliary vector, and picked up by the
Mercury runtime – for instance, the presence of a memory capability is detected
on startup and is used to set up the allocator; the presence of a vspace
capability is automatically wired up to the mmap implementation.

Each of these capabilities is implemented by the kernel, but additional services
are available in userspace via endpoint capabilities. Each of these endpoints
implements a particular API, as defined by a protocol definition file. This
driver requires access to the device registry, so that it can create devices for
its serial ports and expose them to clients.

These protocol definitions are written in a domain-specific language and parsed
by  [ipcgen](https://git.sr.ht/~sircmpwn/ipcgen)  to generate client and server implementations of each. Here’s a
simple protocol to start us off:

```
namespace io;

# The location with respect to which a seek operation is performed.
enum whence {
	# From the start of the file
	SET,
	# From the current offset
	CUR,
	# From the end of the file
	END,
};

# An object with file-like semantics.
interface file {
	# Reads up to amt bytes of data from a file.
	call read{pages: page...}(buf: uintptr, amt: size) size;

	# Writes up to amt bytes of data to a file.
	call write{pages: page...}(buf: uintptr, amt: size) size;

	# Seeks a file to a given offset, returning the new offset.
	call seek(offs: i64, w: whence) size;
};
```

Each interface includes a list of methods, each of which can take a number of
capabilities and parameters, and return a value. The “read” call here, when
implemented by a file-like object, accepts a list of memory pages to perform the
read or write with (shared memory), as well as a pointer to the buffer address
and size. Error handling is still a to-do.

ipcgen consumes these files and writes client or server code as appropriate.
These are generated as part of the Mercury build process and end up in
*_gen.ha files. The generated client code is filed away into the relevant
modules (this protocol ends up at io/file_gen.ha), alongside various
hand-written files which provide additional functionality and often wrap the IPC
calls in a higher-level interface. The server implementations end up in the
“serv” module, e.g. serv/io/file_gen.ha.

Let’s look at some of the generated client code for io::file objects:

```
// This file was generated by ipcgen; do not modify by hand
use helios;
use rt;

// ID for the file IPC interface.
export def FILE_ID: u32 = 0x9A533BB3;

// Labels for operations against file objects.
export type file_label = enum u64 {
	READ = FILE_ID << 16u64 | 1,
	WRITE = FILE_ID << 16u64 | 2,
	SEEK = FILE_ID << 16u64 | 3,
};

export fn file_read(
	ep: helios::cap,
	pages: []helios::cap,
	buf: uintptr,
	amt: size,
) size = {
	// ...
};
```

Each interface has a unique ID (generated from the FNV-1a hash of its fully
qualified name), which is bitwise-OR’d with a list of operations to form call
labels. The interface ID is used elsewhere; we’ll refer to it again later. Then
each method generates an implementation which arranges the IPC details as
necessary and invokes the “call” syscall against the endpoint capability.

The generated server code is a bit more involved. Some of the details are
similar – FILE_ID is generated again, for instance – but there are some
additional details as well. First is the generation of a vtable defining the
functions implementing each operation:

```
// Implementation of a [[file]] object.
export type file_iface = struct {
	read: *fn_file_read,
	write: *fn_file_write,
	seek: *fn_file_seek,
};
```

We also define a file object which is subtyped by the implementation to store
implementation details, and which provides to the generated code the required
bits of state.

```
// Instance of an file object. Users may subtype this object to add
// instance-specific state.
export type file = struct {
	_iface: *file_iface,
	_endpoint: helios::cap,
};
```

Here’s an example of a subtype of file used by the initramfs to store additional
state:

```
// An open file in the bootstrap filesystem
type bfs_file = struct {
	serv::io::file,
	fs: *bfs,
	ent: tar::entry,
	cur: io::off,
	padding: size,
};
```

The embedded serv::io::file structure here is populated with an implementation
of file_iface, here simplified for illustrative purposes:

```
const bfs_file_impl = serv_io::file_iface {
	read = &bfs_file_read,
	write = &bfs_file_write,
	seek = &bfs_file_seek,
};

fn bfs_file_read(
	obj: *serv_io::file,
	pages: []helios::cap,
	buf: uintptr,
	amt: size,
) size = {
	let file = obj: *bfs_file;
	const fs = file.fs;
	const offs = (buf & rt::PAGEMASK): size;
	defer helios::destroy(pages...)!;

	assert(offs + amt <= len(pages) * rt::PAGESIZE);
	const buf = helios::map(rt::vspace, 0, map_flags::W, pages...)!: *[*]u8;

	let buf = buf[offs..offs+amt];
	// Not shown: reading the file data into this buffer
};
```

The implementation can prepare a file object and call dispatch on it to process
client requests: this function blocks until a request arrives, decodes it, and
invokes the appropriate function. Often this is incorporated into an event loop
with poll to service many objects at once.

```
// Prepare a file object
const ep = helios::newendpoint()!;
append(fs.files, bfs_file {
	_iface = &bfs_file_impl,
	_endpoint = ep,
	fs = fs,
	ent = ent,
	cur = io::tell(fs.buf)!,
	padding = fs.rd.padding,
});

// ...

// Process requests associated with this file
serv::io::file_dispatch(file);
```

Okay, enough background: back to the serial driver. It needs to implement the
following protocol:

```
namespace dev;
use io;

# TODO: Add busy error and narrow semantics

# Note: TWO is interpreted as 1.5 for some char lengths (5)
enum stop_bits {
	ONE,
	TWO,
};

enum parity {
	NONE,
	ODD,
	EVEN,
	MARK,
	SPACE,
};

# A serial device, which implements the file interface for reading from and
# writing to a serial port. Typical implementations may only support one read
# in-flight at a time, returning errors::busy otherwise.
interface serial :: io::file {
	# Returns the baud rate in Hz.
	call get_baud() uint;

	# Returns the configured number of bits per character.
	call get_charlen() uint;

	# Returns the configured number of stop bits.
	call get_stopbits() stop_bits;

	# Returns the configured parity setting.
	call get_parity() parity;

	# Sets the baud rate in Hz.
	call set_baud(hz: uint) void;

	# Sets the number of bits per character. Must be 5, 6, 7, or 8.
	call set_charlen(bits: uint) void;

	# Configures the number of stop bits to use.
	call set_stopbits(bits: stop_bits) void;

	# Configures the desired parity.
	call set_parity(parity: parity) void;
};
```

This protocol  *inherits*  the io::file interface, so the serial port is usable
like any other file for reads and writes. It additionally defines
serial-specific methods, such as configuring the baud rate or parity. The
generated interface we’ll have to implement looks something like this, embedding
the io::file_iface struct:

```
export type serial_iface = struct {
	io::file_iface,
	get_baud: *fn_serial_get_baud,
	get_charlen: *fn_serial_get_charlen,
	get_stopbits: *fn_serial_get_stopbits,
	get_parity: *fn_serial_get_parity,
	set_baud: *fn_serial_set_baud,
	set_charlen: *fn_serial_set_charlen,
	set_stopbits: *fn_serial_set_stopbits,
	set_parity: *fn_serial_set_parity,
}
```

Time to dive into the implementation. Recall the driver manifest, which provides
the serial driver with a suitable environment:

```
[driver]
name=pcserial
desc=Serial driver for x86_64 PCs

[capabilities]
0:ioport = min=3F8, max=400
1:ioport = min=2E8, max=2F0
2:note = 
3:irq = irq=3, note=2
4:irq = irq=4, note=2
_:cspace = self
_:vspace = self
_:memory = pages=32

[services]
devregistry=
```

I/O ports for reading and writing to the serial devices, IRQs for receiving
serial-related interrupts, a device registry to add our serial devices to the
system, and a few extra things for implementation needs. Some of these are
statically allocated, some of them are provided via the auxiliary vector.
Our  [serial driver](https://git.sr.ht/~sircmpwn/mercury/tree/5e12977a0cb773331b9b3b8421da63b85eed232c/item/cmd/serial)  opens by defining constants for the statically
allocated capabilities:

```
def IOPORT_A: helios::cap = 0;
def IOPORT_B: helios::cap = 1;
def IRQ: helios::cap = 2;
def IRQ3: helios::cap = 3;
def IRQ4: helios::cap = 4;
```

The first thing we do on startup is create a serial device.

```
export fn main() void = {
	let serial0: helios::cap = 0;
	const registry = helios::service(sys::DEVREGISTRY_ID);
	sys::devregistry_new(registry, dev::SERIAL_ID, &serial0);
	helios::destroy(registry)!;
	// ...
```

The device registry is provided via the aux vector, and we can use
helios::service to look it up by its interface ID. Then we use the
devregistry::new operation to create a serial device:

```
# Device driver registry.
interface devregistry {
	# Creates a new device implementing the given interface ID using the
	# provided endpoint capability and returns its assigned serial number.
	call new{; out}(iface: u64) uint;
};
```

After this we can destroy the registry – we won’t need it again and it’s best
to get rid of it so that we can work with the minimum possible privileges at
runtime. After this we initialize the serial port, acknowledge any interrupts
that might have been pending before we got started, an enter the main loop.

```
com_init(&ports[0], serial0);

helios::irq_ack(IRQ3)!;
helios::irq_ack(IRQ4)!;

let poll: [_]pollcap = [
	pollcap { cap = IRQ, events = pollflags::RECV, ... },
	pollcap { cap = serial0, events = pollflags::RECV, ... },
];
for (true) {
	helios::poll(poll)!;
	if (poll[0].revents & pollflags::RECV != 0) {
		dispatch_irq();
	};
	if (poll[1].revents & pollflags::RECV != 0) {
		dispatch_serial(&ports[0]);
	};
};
```

The dispatch_serial function is of interest, as this provides the
implementation of the serial object we just created with the device registry.

```
type comport = struct {
	dev::serial,
	port: u16,
	rbuf: [4096]u8,
	wbuf: [4096]u8,
	rpending: []u8,
	wpending: []u8,
};

fn dispatch_serial(dev: *comport) void = {
	dev::serial_dispatch(dev);
};

const serial_impl = dev::serial_iface {
	read = &serial_read,
	write = &serial_write,
	seek = &serial_seek,
        get_baud = &serial_get_baud,
        get_charlen = &serial_get_charlen,
        get_stopbits = &serial_get_stopbits,
        get_parity = &serial_get_parity,
        set_baud = &serial_set_baud,
        set_charlen = &serial_set_charlen,
        set_stopbits = &serial_set_stopbits,
        set_parity = &serial_set_parity,
};

fn serial_read(
	obj: *io::file,
	pages: []helios::cap,
	buf: uintptr,
	amt: size,
) size = {
	const port = obj: *comport;
	const offs = (buf & rt::PAGEMASK): size;
	const buf = helios::map(rt::vspace, 0, map_flags::W, pages...)!: *[*]u8;
	const buf = buf[offs..offs+amt];

	if (len(port.rpending) != 0) {
		defer helios::destroy(pages...)!;
		return rconsume(port, buf);
	};

	pages_static[..len(pages)] = pages[..];
	pending_read = read {
		reply = helios::store_reply(helios::CADDR_UNDEF)!,
		pages = pages_static[..len(pages)],
		buf = buf,
	};
	return 0;
};

// (other functions omitted)
```

We’ll skip much of the implementation details for this specific driver, but I’ll
show you how read works at least. It’s relatively straightforward: first we mmap
the buffer provided by the caller. If there’s already readable data pending from
the serial port (stored in that rpending slice in the comport struct, which is a
slice of the statically-allocated rbuf field), we copy it into the buffer and
return the number of bytes we had ready. Otherwise, we stash details about the
caller, storing the special reply capability in our cspace (this is one of the
reasons we need cspace = self in our manifest) so we can reply to this call
once data is available. Then we return to the main loop.

The main loop also wakes up on an interrupt, and we have an interrupt unmasked
on the serial device to wake us whenever there’s data ready to be read.
Eventually this gets us here, which finishes the call we saved earlier:

```
// Reads data from the serial port's RX FIFO.
fn com_read(com: *comport) size = {
	let n: size = 0;
	for (comin(com.port, LSR) & RBF == RBF; n += 1) {
		const ch = comin(com.port, RBR);
		if (len(com.rpending) < len(com.rbuf)) {
			// If the buffer is full we just drop chars
			static append(com.rpending, ch);
		};
	};

	if (pending_read.reply != 0) {
		const n = rconsume(com, pending_read.buf);
		helios::send(pending_read.reply, 0, n)!;
		pending_read.reply = 0;
		helios::destroy(pending_read.pages...)!;
	};

	return n;
};
```

I hope that gives you a general idea of how drivers work in this environment!
I encourage you to read the full implementation if you’re curious to know more
about the serial driver in particular – it’s just 370 lines of code.

The last thing I want to show you is how the driver gets executed in the first
place. When Helios boots up, it starts /sbin/sysinit, which is provided by
Mercury and offers various low-level userspace runtime services, such as the
device registry and bootstrap filesystem we saw earlier. After setting up its
services, sysinit executes /sbin/usrinit, which is provided by the next layer
up (Gaia, eventually) and sets up the rest of the system according to user
policy, mounting filesystems and starting up drivers and such. At the moment,
usrinit is fairly simple, and just runs a little demo. Here it is in full:

```
use dev;
use fs;
use helios;
use io;
use log;
use rt;
use sys;

export fn main() void = {
	const fs = helios::service(fs::FS_ID);
	const procmgr = helios::service(sys::PROCMGR_ID);
	const devmgr = helios::service(sys::DEVMGR_ID);
	const devload = helios::service(sys::DEVLOADER_ID);

	log::printfln("[usrinit] Running /sbin/drv/serial");
	let proc: helios::cap = 0;
	const image = fs::open(fs, "/sbin/drv/serial")!;
	sys::procmgr_new(procmgr, &proc);
	sys::devloader_load(devload, proc, image);
	sys::process_start(proc);

	let serial: helios::cap = 0;
	log::printfln("[usrinit] open device serial0");
	sys::devmgr_open(devmgr, dev::SERIAL_ID, 0, &serial);

	let buf: [rt::PAGESIZE]u8 = [0...];
	for (true) {
		const n = match (io::read(serial, buf)!) {
		case let n: size =>
			yield n;
		case io::EOF =>
			break;
		};

		// CR => LF
		for (let i = 0z; i < n; i += 1) {
			if (buf[i] == '\r') {
				buf[i] = '\n';
			};
		};

		// echo
		io::write(serial, buf[..n])!;
	};
};
```

Each of the services shown at the start are automatically provided in usrinit’s
aux vector by sysinit, and includes all of the services required to bootstrap
the system. This includes a filesystem (the initramfs), a process manager (to
start up new processes), the device manager, and the driver loader service.

usrinit starts by opening up /sbin/drv/serial (the serial driver, of course)
from the provided initramfs using fs::open, which is a convenience wrapper
around the filesystem protocol. Then we create a new process with the process
manager, which by default has an empty address space – we could load a normal
process into it with sys::process_load, but we want to load a driver, so we
use the devloader interface instead. Then we start the process and boom: the
serial driver is online.

The serial driver registers itself with the device registry, which means that we
can use the device manager to open the 0th device which implements the serial
interface. Since this is compatible with the io::file interface, it can simply
be used normally with io::read and io::write to utilize the serial port. The
main loop simply echos data read from the serial port back out. Simple!

That’s a quick introduction to the driver environment provided by Mercury. I
intend to write a few more drivers soon myself – PC keyboard, framebuffer,
etc – and set up a simple shell. We have seen a few sample drivers written
pre-Mercury which would be nice to bring into this environment, such as virtio
networking and block devices. It will be nice to see them re-introduced in an
environment where they can provide useful services to the rest of userspace.

If you’re interested in learning more about Helios or Mercury, consult
 [ares-os.org](https://ares-os.org)  for documentation – though beware of the
many stub pages. If you have any questions or want to get involved in writing
some drivers yourself, jump into our IRC channel: #helios on Libera Chat.
