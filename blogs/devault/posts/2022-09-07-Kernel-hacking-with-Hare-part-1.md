---
title: "Notes from kernel hacking in Hare, part 1"
date: 2022-09-07
url: https://drewdevault.com/2022/09/07/Kernel-hacking-with-Hare-part-1.html
slug: Kernel-hacking-with-Hare-part-1
word_count: 1769
---

One of the goals for the  [Hare](https://harelang.org/)  programming language is to be able to write
kernels, such as my  [Helios](https://git.sr.ht/~sircmpwn/helios)  project. Kernels are complex beasts which exist
in a somewhat unique problem space and have constraints that many userspace
programs are not accustomed to. To illustrate this, I’m going to highlight a
scenario where Hare’s low-level types and manual memory management approach
shines to enable a difficult use-case.

Helios is a micro-kernel. During system initialization, its job is to load the
initial task into memory, prepare the initial set of kernel objects for its use,
provide it with information about the system, then jump to userspace and fuck
off until someone needs it again. I’m going to focus on the “providing
information” step here.

The information the kernel needs to provide includes details about the
capabilities that init has access to (such as working with I/O ports),
information about system memory, the address of the framebuffer, and so on. This
information is provided to init in the bootinfo structure, which is mapped into
its address space, and passed to init via a register which points to this
structure. 1

```
// The bootinfo structure.
export type bootinfo = struct {
	argv: str,

	// Capability ranges
	memory: cap_range,
	devmem: cap_range,
	userimage: cap_range,
	stack: cap_range,
	bootinfo: cap_range,
	unused: cap_range,

	// Other details
	arch: *arch_bootinfo,
	ipcbuf: uintptr,
	modules: []module_desc,
	memory_info: []memory_desc,
	devmem_info: []memory_desc,
	tls_base: uintptr,
	tls_size: size,
};
```

Parts of this structure are static (such as the capability number ranges for
each capability assigned to init), and others are dynamic - such as structures
describing the memory layout (N items where N is the number of memory regions),
or the kernel command line. But, we’re in a kernel – dynamically allocating
data is not so straightforward, especially for units smaller than a page! 2 
Moreover, the data structures allocated here need to be visible to userspace,
and kernel memory is typically not available to userspace. A further
complication is the three different address spaces we’re working with here: a
bootinfo object has a physical memory address, a kernel address, and a userspace
address — three addresses to refer to a single object in different
contexts.

Here’s an example of what the code shown in this article is going to produce:

This is a single page of physical memory which has been allocated for the
bootinfo data, where each cell is a byte. The bootinfo structure itself comes
first, in blue. Following this is an arch-specific bootinfo structure, in green:

```
// x86_64-specific boot information
export type arch_bootinfo = struct {
	// Page table capabilities
	pdpt: cap_range,
	pd: cap_range,
	pt: cap_range,

	// vbe_mode_info physical address from multiboot (or zero)
	vbe_mode_info: uintptr,
};
```

After this, in purple, is the kernel command line. These three structures are
always consistently allocated for any boot configuration, so the code which
sets up the bootinfo page (the code we’re going to read now) always provisions
them. Following these three items is a large area of free space (indicated in
brown) which will be used to populate further dynamically allocated bootinfo
structures, such as descriptions of physical memory regions.

The code to set this up is  `bootinfo_init` , which is responsible for allocating
a suitable page, filling in the bootinfo structure, and preparing a vector to
dynamically allocate additional data on this page. It also sets up the arch
bootinfo and argv, so the page looks like this diagram when the function
returns. And here it is, in its full glory:

```
// Initializes the bootinfo context.
export fn bootinfo_init(heap: *heap, argv: str) bootinfo_ctx = {
	let cslot = caps::cslot { ... };
	let page = objects::init(ctype::PAGE, &cslot, &heap.memory)!;
	let phys = objects::page_phys(page);
	let info = mem::phys_tokernel(phys): *bootinfo;

	const bisz = size(bootinfo);
	let bootvec = (info: *[*]u8)[bisz..arch::PAGESIZE][..0];

	let ctx = bootinfo_ctx {
		page = cslot,
		info = info,
		arch = null: *arch_bootinfo, // Fixed up below
		bootvec = bootvec,
	};

	let (vec, user) = mkbootvec(&ctx, size(arch_bootinfo), size(uintptr));
	ctx.arch = vec: *[*]u8: *arch_bootinfo;
	info.arch = user: *arch_bootinfo;

	let (vec, user) = mkbootvec(&ctx, len(argv), 1);
	vec[..] = strings::toutf8(argv)[..];
	info.argv = *(&types::string {
		data = user: *[*]u8,
		length = len(argv),
		capacity = len(argv),
	}: *str);

	return ctx;
};
```

The first three lines are fairly straightforward. Helios uses capability-based
security, similar in design to  [seL4](https://sel4.systems/) . All kernel objects — such as
pages of physical memory — are utilized through the capability system. The
first two lines set aside a slot to store the page capability in, then allocate
a page using that slot. The next two lines grab the page’s physical address and
use  `mem::phys_tokernel`  to convert it to an address in the kernel’s virtual
address space, so that the kernel can write data to this page.

The next two lines are where it starts to get a little bit interesting:

```
const bisz = size(bootinfo);
let bootvec = (info: *[*]u8)[bisz..arch::PAGESIZE][..0];
```

This casts the “info” variable (of type *bootinfo) to a pointer to an
 *unbounded*  array of bytes (*[*]u8). This is a little bit dangerous! Hare’s
arrays are bounds tested by default and using an unbounded type disables this
safety feature. We want to get a bounded slice again soon, which is what the
first slicing operator here does:  `[bisz..arch::PAGESIZE]` . This obtains a
 *bounded*  slice of bytes which starts from the end of the bootinfo structure and
continues to the end of the page.

The last expression, another slicing expression, is a little bit unusual. A
slice type in Hare has the following internal representation:

```
type slice = struct {
	data: nullable *void,
	length: size,
	capacity: size,
};
```

When you slice an unbounded array, you get a slice whose length and capacity
fields are equal to the length of the slicing operation, in this case
 `arch::PAGESIZE - bisz` . But when you slice a  *bounded*  slice, the length field
takes on the length of the slicing expression but the capacity field is
calculated from the original slice. So by slicing our new bounded slice to the
0th index ([..0]), we obtain the following slice:

```
slice {
	data = &(info: *[*]bootinfo)[1]: *[*]u8,
	length = 0,
	capacity = arch::PAGESIZE - bisz,
};
```

In plain English, this is a slice whose base address is the address following
the bootinfo structure and whose capacity is the remainder of the free space on
its page, with a length of zero. This is something we can use  static append  with! 3

```
// Allocates a buffer in the bootinfo vector, returning the kernel vector and a
// pointer to the structure in the init vspace.
fn mkbootvec(info: *bootinfo_ctx, sz: size, al: size) ([]u8, uintptr) = {
	const prevlen = len(info.bootvec);
	let padding = 0z;
	if (prevlen % al != 0) {
		padding = al - prevlen % al;
	};
	static append(info.bootvec, [0...], sz + padding);
	const vec = info.bootvec[prevlen + padding..];
	return (vec, INIT_BOOTINFO_ADDR + size(bootinfo): uintptr prevlen: uintptr);
};
```

In Hare, slices can be dynamically grown and shrunk using the  *append* ,
 *insert* , and  *delete*  keywords. This is pretty useful, but not applicable for
our kernel — remember, no dynamic memory allocation. Attempting to use
append in Helios would cause a linking error because the necessary runtime code
is absent from the kernel’s Hare runtime. However, you can also  *statically* 
append to a slice, as shown here. So long as the slice has a sufficient capacity
to store the appended data, a static append or insert will succeed. If not, an
assertion is thrown at runtime, much like a normal bounds test.

This function makes good use of it to dynamically allocate memory from the
bootinfo page. Given a desired size and alignment, it statically appends a
suitable number of zeroes to the page, takes a slice of the new data, and
returns both that slice (in the kernel’s address space) and the address that
data will have in the user address space. If we return to the earlier function,
we can see how this is used to allocate space for the arch_bootinfo structure:

```
let (vec, user) = mkbootvec(&ctx, size(arch_bootinfo), size(uintptr));
ctx.arch = vec: *[*]u8: *arch_bootinfo;
info.arch = user: *arch_bootinfo;
```

The “ctx” variable is used by the kernel to keep track of its state while
setting up the init task, and we stash the kernel’s pointer to this data
structure in there, and the user’s pointer in the bootinfo structure itself.

This is also used to place argv into the bootinfo page:

```
let (vec, user) = mkbootvec(&ctx, len(argv), 1);
vec[..] = strings::toutf8(argv)[..];
info.argv = *(&types::string {
	data = user: *[*]u8,
	length = len(argv),
	capacity = len(argv),
}: *str);
```

Here we allocate a vector whose length is the length of the argument string,
with an alignment of one, and then copy argv into it as a UTF-8 slice. Slice
copy expressions like this one are a type-safe and memory-safe way to memcpy in
Hare. Then we do something a bit more interesting.

Like slices, strings have an internal representation in Hare which includes a
data pointer, length, and capacity. The types module provides a struct with this
representation so that you can do low-level string manipulation in Hare should
the task call for it. Hare’s syntax allows us to take the address of a literal
value, such as a types::string struct, using the & operator. Then we cast it to
a pointer to a string and dereference it. Ta-da! We set the bootinfo argv field
to a str value which uses the user address of the argument vector.

Some use-cases call for this level of fine control over the precise behavior of
your program. Hare’s goal is to accommodate this need with little fanfare. Here
we’ve drawn well outside of the lines of Hare’s safety features, but sometimes
it’s useful and necessary to do so. And Hare provides us with the tools to get
the safety harness back on quickly, such as we saw with the construction of the
bootvec slice. This code is pretty weird but to an experienced Hare programmer
(which, I must admit, the world has very few of) it should make sense.

I hope you found this interesting! I’m going back to kernel hacking. Next up is
loading the userspace ELF image into its address space. I had this working
before but decided to rewrite it. Wish me good luck!

1. %rdi, if you were curious. Helios uses the System-V ABI, where %rdi is
used as the first parameter to a function call. This isn’t exactly a function
call but the precedent is useful. ↩︎
2. 4096 bytes. ↩︎
3. Thanks to [Rahul of W3Bits](https://w3bits.com/rainbow-text/) for this CSS. ↩︎
