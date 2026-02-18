---
title: "When to comment that code"
date: 2023-03-09
url: https://drewdevault.com/2023/03/09/2023-03-09-Comment-or-no-comment.html
slug: 2023-03-09-Comment-or-no-comment
word_count: 1832
---

My software tends to have a surprisingly low number of comments. One of my
projects,  [scdoc](https://git.sr.ht/~sircmpwn/scdoc) , has 25 comments among its 1,133 lines of C code, or 2%,
compared to the average of 19%. 1  Naturally, I insist that my code is
well-written in spite of this divergence from the norm. Allow me to explain.

The philosophy and implementation of code comments varies widely in the
industry, and some view comment density as a proxy for code quality. 2  I’ll
state my views here, but will note that yours may differ and I find that
acceptable; I am not here to suggest that your strategy is wrong and I will
happily adopt it when I write a patch for your codebase.

Let’s begin with an illustrative example from one of my projects:

```
// Reads the next entry from an EFI [[FILE_PROTOCOL]] handle of an open
// directory. The return value is statically allocated and will be overwritten
// on the next call.
export fn readdir(dir: *FILE_PROTOCOL) (*FILE_INFO | void | error) = {
	// size(FILE_INFO) plus reserve up to 512 bytes for file name (FAT32
	// maximum, times two for wstr encoding)
	static let buf: [FILE_INFO_SIZE + 512]u8 = [0...];
	const n = read(dir, buf)?;
	if (n == 0) {
		return;
	};
	return &buf[0]: *FILE_INFO;
};
```

This code illustrates two of my various approaches to writing comments. The
first comment is a documentation comment: the intended audience is the consumer
of this API. The call-site has access to the following information:

* This comment
* The name of the function, and the module in which it resides (efi::readdir)
* The parameter names and types
* The return type

The goal is for the user of this function to gather enough information from
these details to correctly utilize this API.

The module in which it resides suggests that this function interacts with the
EFI (Extensible Firmware Interface) standard, and the user would be wise to pair
a reading of this code (or API) with skimming the relevant standard. Indeed, the
strategic naming of the FILE_PROTOCOL and FILE_INFO types (notably written in
defiance of the Hare style guide), provide hints to the relevant parts of the
EFI specification to read for a complete understanding of this code.

The name of the function is also carefully chosen to carry some weight: it is a
reference to the Unix readdir function, which brings with it an intuition about
its purpose and usage for programmers familiar with a Unix environment.

The return type also provides hints about the function’s use: it may return
either a FILE_INFO pointer, void (nothing), or an error. Without reading the
documentation string, and taking the name and return type into account, we might
(correctly) surmise that we need to call this function repeatedly to read file
details out of a directory until it returns void, indicating that all entries
have been processed, handling any errors which might occur along the way.

We have established a lot of information about this function without actually
reading the comment; in my philosophy of programming I view this information as
a critical means for the author to communicate to the user, and we can lean on
it to reduce the need for explicit documentation. Nevertheless, the
documentation comment adds something here. The first sentence is a relatively
information-sparse summary of the function’s purpose, and mainly exists to tick
a box in the Hare style guide. 3  The second sentence is the only real reason
this comment exists: to clarify an important detail for the user which is not
apparent from the function signature, namely the storage semantics associated
with the return value.

Let’s now study the second comment’s purpose:

```
// size(FILE_INFO) plus reserve up to 512 bytes for file name (FAT32
// maximum, times two for wstr encoding)
static let buf: [FILE_INFO_SIZE + 512]u8 = [0...];
```

This comment exists to explain the use of the magic constant of 512. The
audience of this comment is someone reading the  *implementation*  of this
function. This audience has access to a different context than the user of the
function, for instance they are expected to have a more comprehensive knowledge
of EFI and are  *definitely*  expected to be reading the specification to a much
greater degree of detail. We can and should lean on that context to make our
comments more concise and useful.

An alternative writing which does not rely on this context, and which in
my view is strictly worse, may look like the following:

```
// The FILE_INFO structure includes the file details plus a variable length
// array for the filename. The underlying filesystem is always FAT32 per the
// EFI specification, which has a maximum filename length of 256 characters. The
// filename is encoded as a wide-string (UCS-2), which encodes two bytes per
// character, and is not NUL-terminated, so we need to reserve up to 512 bytes
// for the filename.
static let buf: [FILE_INFO_SIZE + 512]u8 = [0...];
```

The target audience of this comment should have a reasonable understanding of
EFI. We simply need to clarify that this constant is the FAT32 max filename
length, times two to account for the wstr encoding, and our magic constant is
sufficiently explained.

Let’s move on to another kind of comment I occasionally write: medium-length
prose. These often appear at the start of a function or the start of a file and
serve to add context to the implementation, to justify the code’s existence or
explain why it works. Another sample:

```
fn init_pagetables() void = {
	// 0xFFFF0000xxxxxxxx - 0xFFFF0200xxxxxxxx: identity map
	// 0xFFFF0200xxxxxxxx - 0xFFFF0400xxxxxxxx: identity map (dev)
	// 0xFFFF8000xxxxxxxx - 0xFFFF8000xxxxxxxx: kernel image
	//
	// L0[0x000]    => L1_ident
	// L0[0x004]    => L1_devident
	// L1_ident[*]  => 1 GiB identity mappings
	// L0[0x100]    => L1_kernel
	// L1_kernel[0] => L2_kernel
	// L2_kernel[0] => L3_kernel
	// L3_kernel[0] => 4 KiB kernel pages
	L0[0x000] = PT_TABLE | &L1_ident: uintptr | PT_AF;
	L0[0x004] = PT_TABLE | &L1_devident: uintptr | PT_AF;
	L0[0x100] = PT_TABLE | &L1_kernel: uintptr | PT_AF;
	L1_kernel[0] = PT_TABLE | &L2_kernel: uintptr | PT_AF;
	L2_kernel[0] = PT_TABLE | &L3_kernel: uintptr | PT_AF;
	for (let i = 0u64; i < len(L1_ident): u64; i += 1) {
		L1_ident[i] = PT_BLOCK | (i * 0x40000000): uintptr |
			PT_NORMAL | PT_AF | PT_ISM | PT_RW;
	};
	for (let i = 0u64; i < len(L1_devident): u64; i += 1) {
		L1_devident[i] = PT_BLOCK | (i * 0x40000000): uintptr |
			PT_DEVICE | PT_AF | PT_ISM | PT_RW;
	};
};
```

This comment shares a trait with the previous example: its purpose, in part, is
to justify magic constants. It explains the indices of the arrays by way of the
desired address space, and a perceptive reader will notice that 1 GiB =
1073741824 bytes = 0x40000000 bytes.

To fully understand this, we must again consider the intended audience. This
is an implementation comment, so the reader is an  *implementer* . They will need
to possess some familiarity with the behavior of page tables to be productive in
this code, and they likely have the ARM manual up on their second monitor. This
comment simply fills in the blanks for an informed reader.

There are two additional kinds of comments I often write: TODO and XXX.

A TODO comment indicates some important implementation deficiency; it  *must*  be
addressed at some point in the future and generally indicates that the function
does not meet its stated interface and is often accompanied by an assertion, or
a link to a ticket on the bug tracker, or both.

```
assert(ep.send == null); // TODO: support multiple senders
```

This function should support multiple senders, but does not; an assertion here
prevents the code from running under conditions it does not yet support and the
TODO comment indicates that this should be addressed in the future. The target
audience for this comment is someone who brings about these conditions and runs
into the assertion failure.

```
fn memory_empty(mem: *memory) bool = {
	// XXX: This O(n) linked list traversal is bad
	let next = mem.next;
	let pages = 0u;
	for (next != FREELIST_END; pages += 1) {
		const addr = mem.phys + (next * mem::PAGESIZE): uintptr;
		const ptr = mem::phys_tokernel(addr): *uint;
		next = *ptr;
	};
	return pages == mem.pages;
};
```

Here we find an example of an XXX comment. This code is correct: it implements
the function’s interface perfectly. However, given its expected usage, a
performance of O(n) is not great: this function is expected to be used in hot
paths. This comment documents the deficiency, and provides a hint to a reader
that might be profiling this code in regards to a possible improvement.

One final example:

```
// Invalidates the TLB for a virtual address.
export fn invalidate(virt: uintptr) void = {
	// TODO: Notify other cores (XXX SMP)
	invlpg(virt);
};
```

This is an atypical usage of XXX, but one which I still occasionally reach for.
Here we have a TODO comment which indicates a case which this code does not
consider, but which must be addressed in the future: it will have to raise an
IPI to get other cores to invalidate the affected virtual address. However, this
is one of many changes which fall under a broader milestone of SMP support, and
the “XXX SMP” comment is here to make it easy to grep through the codebase for
any places which are known to require attention while implementing SMP support.
An XXX comment is often written for the purpose of being easily found with grep.

That sums up most of the common reasons I will write a comment in my software.
Each comment is written considering a target audience and the context provided
by the code in which it resides, and aims to avoid stating redundant information
within these conditions. It’s for this reason that my code is sparse on
comments: I find the information outside of the comments equally important and
aim to be concise such that a comment is not redundant with information found
elsewhere.

Hopefully this post inspired some thought in you, to consider your comments
deliberately and to be more aware of your ability to communicate information in
other ways. Even if you chose to write your comments more densely than I do, I
hope you will take care to communicate well through other mediums in your code
as well.

1. O. Arafat and D. Riehle, “The comment density of open source software code,” 2009 31st International Conference on Software Engineering - Companion Volume, Vancouver, BC, Canada, 2009, pp. 195-198, doi: 10.1109/ICSE-COMPANION.2009.5070980. ↩︎
2. I hold this view weakly, but reverse of the norm: I consider a high
comment density a sign that the code quality may be poor. ↩︎
3. Which states that all exported functions that the module consumer is
expected to use should have a comment, and that exported but undocumented
symbols are exported to fulfill an implementation detail and not to provide a
useful interface. ↩︎
