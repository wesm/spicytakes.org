---
title: "A Hare code generator for finding ioctl numbers"
date: 2022-05-14
url: https://drewdevault.com/2022/05/14/generating-ioctls.html
slug: generating-ioctls
word_count: 2315
---

Modern Unix derivatives have this really bad idea called  [ioctl](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html) . It’s a
function which performs arbitrary operations on a file descriptor. It is
essentially the kitchen sink of modern Unix derivatives, particularly Linux, in
which they act almost like a second set of extra syscalls. For example, to get
the size of the terminal window, you use an ioctl specific to TTY file
descriptors:

```
let wsz = rt::winsize { ... };
match (rt::ioctl(fd, rt::TIOCGWINSZ, &wsz: *void)) {
case let e: rt::errno =>
	switch (e: int) {
	case rt::EBADFD =>
		return errors::invalid;
	case rt::ENOTTY =>
		return errors::unsupported;
	case =>
		abort("Unexpected error from ioctl");
	};
case int =>
	return ttysize {
		rows = wsz.ws_row,
		columns = wsz.ws_col,
	};
};
```

This code performs the ioctl syscall against the provided file descriptor “fd”,
using the “TIOCGWINSZ” operation, and setting the parameter to a pointer to a
winsize structure. There are thousands of ioctls provided by Linux, and each of
them is assigned a constant like TIOCGWINSZ (0x5413). Some constants, including
this one, are assigned somewhat arbitrarily. However, some are assigned with
some degree of structure.

Consider for instance the ioctl TUNSETOWNER, which is used for tun/tap network
devices. This ioctl is assigned the number 0x400454cc, but this is not selected
arbitrarily. It’s assigned with a macro, which we can find in
/usr/include/linux/if_tun.h:

```
#define TUNSETOWNER   _IOW('T', 204, int)
```

The _IOW macro, along with similar ones like _IO, _IOR, and _IOWR, are
defined in /usr/include/asm-generic/ioctl.h. They combine this letter, number,
and parameter type (or rather its size), and the direction (R, W, WR, or
neither), OR’d together into an unsigned 32-bit number:

```
#define _IOC_WRITE	1U

#define _IOC_TYPECHECK(t) (sizeof(t))

#define _IOC(dir,type,nr,size) \
	(((dir)  << _IOC_DIRSHIFT) | \
	 ((type) << _IOC_TYPESHIFT) | \
	 ((nr)   << _IOC_NRSHIFT) | \
	 ((size) << _IOC_SIZESHIFT))

#define _IOW(type,nr,size)	_IOC(_IOC_WRITE,(type),(nr),(_IOC_TYPECHECK(size)))
```

It would be useful to define ioctl numbers in a similar fashion for Hare
programs. However, Hare lacks macros, so we cannot re-implement this in exactly
the same manner. Instead, we can use code generation.

*[Hare](https://harelang.org) is a new systems programming language I’ve been
working on for a couple of years. Check out the [announcement](https://harelang.org/blog/2022-04-25-announcing-hare/) for more
detail.*

Again using the tun interface as an example, our goal is to turn the following
input file:

```
type sock_filter = struct {
	code: u16,
	jt: u8,
	jf: u8,
	k: u32,
};

type sock_fprog = struct {
	length: u16,
	filter: *sock_filter,
};

def TUNSETNOCSUM: u32 = @_IOW('T', 200, int);
def TUNSETDEBUG: u32 = @_IOW('T', 201, int);
def TUNSETIFF: u32 = @_IOW('T', 202, int);
def TUNSETPERSIST: u32 = @_IOW('T', 203, int);
def TUNSETOWNER: u32 = @_IOW('T', 204, int);
def TUNSETLINK: u32 = @_IOW('T', 205, int);
def TUNSETGROUP: u32 = @_IOW('T', 206, int);
def TUNGETFEATURES: u32 = @_IOR('T', 207, uint);
def TUNSETOFFLOAD: u32 = @_IOW('T', 208, uint);
def TUNSETTXFILTER: u32 = @_IOW('T', 209, uint);
def TUNGETIFF: u32 = @_IOR('T', 210, uint);
def TUNGETSNDBUF: u32 = @_IOR('T', 211, int);
def TUNSETSNDBUF: u32 = @_IOW('T', 212, int);
def TUNATTACHFILTER: u32 = @_IOW('T', 213, sock_fprog);
def TUNDETACHFILTER: u32 = @_IOW('T', 214, sock_fprog);
def TUNGETVNETHDRSZ: u32 = @_IOR('T', 215, int);
def TUNSETVNETHDRSZ: u32 = @_IOW('T', 216, int);
def TUNSETQUEUE: u32 = @_IOW('T', 217, int);
def TUNSETIFINDEX: u32 = @_IOW('T', 218, uint);
def TUNGETFILTER: u32 = @_IOR('T', 219, sock_fprog);
def TUNSETVNETLE: u32 = @_IOW('T', 220, int);
def TUNGETVNETLE: u32 = @_IOR('T', 221, int);
def TUNSETVNETBE: u32 = @_IOW('T', 222, int);
def TUNGETVNETBE: u32 = @_IOR('T', 223, int);
def TUNSETSTEERINGEBPF: u32 = @_IOR('T', 224, int);
def TUNSETFILTEREBPF: u32 = @_IOR('T', 225, int);
def TUNSETCARRIER: u32 = @_IOW('T', 226, int);
def TUNGETDEVNETNS: u32 = @_IO('T', 227);
```

Into the following output file:

```
type sock_filter = struct {
	code: u16,
	jt: u8,
	jf: u8,
	k: u32,
};

type sock_fprog = struct {
	length: u16,
	filter: *sock_filter,
};

def TUNSETNOCSUM: u32 = 0x400454c8;
def TUNSETDEBUG: u32 = 0x400454c9;
def TUNSETIFF: u32 = 0x400454ca;
def TUNSETPERSIST: u32 = 0x400454cb;
def TUNSETOWNER: u32 = 0x400454cc;
def TUNSETLINK: u32 = 0x400454cd;
def TUNSETGROUP: u32 = 0x400454ce;
def TUNGETFEATURES: u32 = 0x800454cf;
def TUNSETOFFLOAD: u32 = 0x400454d0;
def TUNSETTXFILTER: u32 = 0x400454d1;
def TUNGETIFF: u32 = 0x800454d2;
def TUNGETSNDBUF: u32 = 0x800454d3;
def TUNSETSNDBUF: u32 = 0x400454d4;
def TUNATTACHFILTER: u32 = 0x401054d5;
def TUNDETACHFILTER: u32 = 0x401054d6;
def TUNGETVNETHDRSZ: u32 = 0x800454d7;
def TUNSETVNETHDRSZ: u32 = 0x400454d8;
def TUNSETQUEUE: u32 = 0x400454d9;
def TUNSETIFINDEX: u32 = 0x400454da;
def TUNGETFILTER: u32 = 0x801054db;
def TUNSETVNETLE: u32 = 0x400454dc;
def TUNGETVNETLE: u32 = 0x800454dd;
def TUNSETVNETBE: u32 = 0x400454de;
def TUNGETVNETBE: u32 = 0x800454df;
def TUNSETSTEERINGEBPF: u32 = 0x800454e0;
def TUNSETFILTEREBPF: u32 = 0x800454e1;
def TUNSETCARRIER: u32 = 0x400454e2;
def TUNGETDEVNETNS: u32 = 0x54e3;
```

I wrote the  [ioctlgen](https://git.sr.ht/~sircmpwn/hare/tree/master/item/cmd/ioctlgen/main.ha)  tool for this purpose, and since it demonstrates a number
of interesting Hare features, I thought it would make for a cool blog post. This
program must do the following things:

* Scan through the file looking for @_IO* constructs
* Parse these @_IO* constructs
* Determine the size of the type specified by the third parameter
* Compute the ioctl number based on these inputs
* Write the computed constant to the output
* Pass everything else through unmodified

The implementation begins thusly:

```
let ioctlre: regex::regex = regex::regex { ... };
let typedefre: regex::regex = regex::regex { ... };

@init fn init() void = {
	ioctlre = regex::compile(`@(_IO[RW]*)\((.*)\)`)!;
	typedefre = regex::compile(`^(export )?type `)!;
};

@fini fn fini() void = {
	regex::finish(&ioctlre);
	regex::finish(&typedefre);
};
```

This sets aside two regular expressions: one that identifies type aliases (so
that we can parse them to determine their size later), and one that identifies
our @_IO* pseudo-macros. I also defined some types to store each of the
details necessary to compute the ioctl assignment:

```
type dir = enum u32 {
	IO = 0,
	IOW = 1,
	IOR = 2,
	IOWR = IOW | IOR,
};

type ioctl = (dir, rune, u32, const nullable *types::_type);
```

Hare’s standard library includes tools for parsing and analyzing Hare programs
in the  [hare namespace](https://docs.harelang.org/hare) . We’ll need to use these to work with types in this
program. At the start of the program, we initialize a “type store” from
hare::types, which provides a mechanism with which Hare types can be processed
and stored. The representation of Hare types varies depending on the
architecture (for example, pointer types have different sizes on 32-bit and
64-bit systems), so we have to specify the architecture we want. In the future
it will be necessary to make this configurable, but for now I just hard-coded
x86_64:

```
const store = types::store(types::x86_64, null, null);
defer types::store_free(store);
```

The two “null” parameters are not going to be used here, but are designed to
facilitate evaluating expressions in type definitions, such as  `[8 * 16]int` .
Leaving them null is permissible, but disables the ability to do this sort of
thing.

Following this, we enter a loop which processes the input file line-by-line,
testing each line against our regular expressions and doing some logic on them
if they match. Let’s start with the code for handling new types:

```
for (true) {
	const line = match (bufio::scanline(os::stdin)!) {
	case io::EOF =>
		break;
	case let line: []u8 =>
		yield strings::fromutf8(line);
	};
	defer free(line);

	if (regex::test(&typedefre, line)!) {
		bufio::unreadrune(os::stdin, '\n');
		bufio::unread(os::stdin, strings::toutf8(line));
		loadtype(store);
		continue;
	};

	// ...to be continued...
```

If we encounter a line which matches our type declaration regular expression,
then we unread that line back into the (buffered) standard input stream, then
call this “loadtype” function to parse and load it into the type store.

```
fn loadtype(store: *types::typestore) void = {
	const tee = io::tee(os::stdin, os::stdout);
	const lex = lex::init(&tee, "<ioctl>");
	const decl = match (parse::decl(&lex)) {
	case let err: parse::error =>
		fmt::fatal("Error parsing type declaration:",
			parse::strerror(err));
	case let decl: ast::decl =>
		yield decl;
	};

	const tdecl = decl.decl as []ast::decl_type;
	if (len(tdecl) != 1) {
		fmt::fatal("Multiple type declarations are unsupported");
	};
	const tdecl = tdecl[0];
	const of = types::lookup(store, &tdecl._type)!;
	types::newalias(store, tdecl.ident, of);
};
```

Hare includes a Hare lexer and parser in the standard library, which we’re
making use of here. The first thing we do is use  [io::tee](https://docs.harelang.org/io#tee)  to copy any data the
parser reads into stdout, passing it through to the output file. Then we set up
a lexer and parse the type declaration. A type declaration looks something like
this:

```
type sock_fprog = struct {
	length: u16,
	filter: *sock_filter,
};
```

The types::lookup call looks up the struct type, and newalias creates a new
type alias based on that type with the given name (sock_filter). Adding this to
the type store will let us resolve the type when we encounter it later on, for
example in this line:

```
def TUNGETFILTER: u32 = @_IOR('T', 219, sock_fprog);
```

Back to the main loop, we have another regex test to check if we’re looking at a
line with one of these pseudo-macros:

```
let groups = match (regex::find(&ioctlre, line)!) {
case void =>
	fmt::println(line)!;
	continue;
case let cap: []regex::capture =>
	yield cap;
};
defer free(groups);

const dir = switch (groups[1].content) {
case "_IO" =>
	yield dir::IO;
case "_IOR" =>
	yield dir::IOR;
case "_IOW" =>
	yield dir::IOW;
case "_IOWR" =>
	yield dir::IOWR;
case =>
	fmt::fatalf("Unknown ioctl direction {}", groups[1].content);
};
const ioctl = parseioctl(store, dir, groups[2].content);
```

Recall that the regex from earlier is  `@(_IO[RW]*)\((.*)\)` . This has two
capture groups: one for “_IO” or “_IOW” and so on, and another for the list of
“parameters” (the zeroth “capture group” is the entire match string). We use the
first capture group to grab the ioctl direction, then we pass that into
“parseioctl” along with the type store and the second capture group.

This “parseioctl” function is kind of neat:

```
fn parseioctl(store: *types::typestore, d: dir, params: str) ioctl = {
	const buf = bufio::fixed(strings::toutf8(params), io::mode::READ);
	const lex = lex::init(&buf, "<ioctl>");

	const rn = expect(&lex, ltok::LIT_RUNE).1 as rune;
	expect(&lex, ltok::COMMA);
	const num = expect(&lex, ltok::LIT_ICONST).1 as i64;

	if (d == dir::IO) {
		return (d, rn, num: u32, null);
	};

	expect(&lex, ltok::COMMA);
	const ty = match (parse::_type(&lex)) {
	case let ty: ast::_type =>
		yield ty;
	case let err: parse::error =>
		fmt::fatal("Error:", parse::strerror(err));
	};

	const ty = match (types::lookup(store, &ty)) {
	case let err: types::error =>
		fmt::fatal("Error:", types::strerror(err));
	case types::deferred =>
		fmt::fatal("Error: this tool does not support forward references");
	case let ty: const *types::_type =>
		yield ty;
	};

	return (d, rn, num: u32, ty);
};

fn expect(lex: *lex::lexer, want: ltok) lex::token = {
	match (lex::lex(lex)) {
	case let err: lex::error =>
		fmt::fatal("Error:", lex::strerror(err));
	case let tok: lex::token =>
		if (tok.0 != want) {
			fmt::fatalf("Error: unexpected {}", lex::tokstr(tok));
		};
		return tok;
	};
};
```

Here we’ve essentially set up a miniature parser based on a Hare lexer to parse
our custom parameter list grammar. We create a  [fixed reader](https://docs.harelang.org/bufio#fixed)  from the capture
group string, then create a lexer based on this and start pulling tokens out of
it. The first parameter is a rune, so we grab a LIT_RUNE token and extract the
Hare rune value from it, then after a COMMA token we repeat this with
LIT_ICONST to get the integer constant. dir::IO ioctls don’t have a type
parameter, so can return early in this case.

Otherwise, we use  [hare::parse::_type](https://docs.harelang.org/hare/parse#_type)  to parse the type parameter, producing
a  [hare::ast::_type](https://docs.harelang.org/hare/ast#_type) . We then pass this to the type store to look up technical
details about this type, such as its size, alignment, storage representation,
and so on. This converts the AST type — which only has lexical information
— into an actual type, including semantic information about the type.

Equipped with this information, we can calculate the ioctl’s assigned number:

```
def IOC_NRBITS: u32 = 8;
def IOC_TYPEBITS: u32 = 8;
def IOC_SIZEBITS: u32 = 14; // XXX: Arch-specific
def IOC_DIRBITS: u32 = 2; // XXX: Arch-specific

def IOC_NRSHIFT: u32 = 0;
def IOC_TYPESHIFT: u32 = IOC_NRSHIFT + IOC_NRBITS;
def IOC_SIZESHIFT: u32 = IOC_TYPESHIFT + IOC_TYPEBITS;
def IOC_DIRSHIFT: u32 = IOC_SIZESHIFT + IOC_SIZEBITS;

fn ioctlno(io: *ioctl) u32 = {
	const typesz = match (io.3) {
	case let ty: const *types::_type =>
		yield ty.sz;
	case null =>
		yield 0z;
	};
	return (io.0: u32 << IOC_DIRSHIFT) |
		(io.1: u32 << IOC_TYPESHIFT) |
		(io.2 << IOC_NRSHIFT) |
		(typesz: u32 << IOC_SIZESHIFT);
};
```

And, back in the main loop, print it to the output:

```
const prefix = strings::sub(line, 0, groups[1].start - 1);
fmt::printfln("{}0x{:x};", prefix, ioctlno(&ioctl))!;
```

Now we have successfully converted this:

```
type sock_filter = struct {
	code: u16,
	jt: u8,
	jf: u8,
	k: u32,
};

type sock_fprog = struct {
	length: u16,
	filter: *sock_filter,
};

def TUNATTACHFILTER: u32 = @_IOW('T', 213, sock_fprog);
```

Into this:

```
def TUNATTACHFILTER: u32 = 0x401054d5;
```

A quick C program verifies our result:

```
#include <linux/ioctl.h>
#include <linux/if_tun.h>
#include <stdio.h>

int main() {
	printf("TUNATTACHFILTER: 0x%lx\n", TUNATTACHFILTER);
}
```

And:

```
TUNATTACHFILTER: 0x401054d5
```

It works!

Critics may draw attention to the fact that we could have saved ourselves much
of this work if Hare had first-class macros, but macros are not aligned with
Hare’s design goals, so an alternative solution is called for. This particular
program is useful only in a small set of specific circumstances (and mainly for
Hare developers themselves, less so for most users), but it solves the problem
pretty neatly given the constraints it has to work within.

I think this is a nice case study in a few useful features available from the
Hare standard library. In addition to POSIX Extended Regular Expression support
via the  [regex](https://docs.harelang.org/regex)  module, the  [hare namespace](https://docs.harelang.org/hare)  offers many tools to provide Hare
programs with relatively deep insights into the language itself. We can use
hare::lex to parse the custom grammar for our pseudo-macros, use hare::parse to
parse type declarations, and use hare::types to compute the semantic details
of each type. I also like many of the “little things” on display here, such as
unreading data back into the buffered stdin reader, or using io::tee to copy
data to stdout during parsing.

I hope you found it interesting!
