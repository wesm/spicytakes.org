---
title: "Implementing a MIME database in XXXX"
date: 2022-01-28
url: https://drewdevault.com/2022/01/28/Implementing-mime-in-xxxx.html
slug: Implementing-mime-in-xxxx
word_count: 2517
---

*This is a (redacted) post from the internal blog of a new systems
programming language we’re developing. The project is being kept under wraps
until we’re done with it, so for this post I’ll be calling it XXXX. If you are interested in participating, [send me an email](mailto:sir@cmpwn.com) with some details about your
background and I’ll get back to you.*

Recently, I have been working on implementing a parser for media types (commonly
called MIME types) and a database which maps media types to file extensions and
vice-versa. I thought this would be an interesting module to blog about, given
that it’s only about 250 lines of code, does something useful and interesting,
and demonstrates a few interesting  xxxx  concepts.

The format for media types is more-or-less defined by  [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045) , specifically
 [section 5.1](https://datatracker.ietf.org/doc/html/rfc2045#section-5.1) . The specification is not great. The grammar shown here is copied
and pasted from parts of larger grammars in older RFCs, RFCs which are equally
poorly defined. For example, the quoted-string nonterminal is never defined
here, but instead comes from RFC 822, which defines it but also states that it
can be “folded”, which technically makes the following a valid Media Type:

```
text/plain;charset="hello
 world"
```

Or so I would presume, but the qtext terminal “cannot include CR”, which is the
mechanism by which folding is performed in the first place, and… bleh. Let’s
just implement a “reasonable subset” of the spec instead and side-step the whole
folding issue. 1  This post will first cover parsing media types, then address
our second goal: providing a database which maps media types to file extensions
and vice versa.

## Parsing Media Types

So, here’s what we’re going to implement today: we want to parse the following
string:

```
text/plain; charset=utf-8; foo="bar baz"
```

The code for that I came up with for is as follows:

```
// Parses a Media Type, returning a tuple of the content type (e.g.
// "text/plain") and a parameter parser object, or [[errors::invalid]] if the
// input cannot be parsed.
//
// To enumerate the Media Type parameter list, pass the type_params object into
// [[next_param]]. If you do not need the parameter list, you can safely discard
// the object. Note that any format errors following the ";" token will not
// cause [[errors::invalid]] to be returned unless [[next_param]] is used to
// enumerate all of the parameters.
export fn parse(in: str) ((str, type_params) | errors::invalid) = {
	const items = strings::cut(in, ";");
	const mtype = items.0, params = items.1;
	const items = strings::cut(mtype, "/");
	if (len(items.0) < 1 || len(items.1) < 1) {
		return errors::invalid;
	};
	typevalid(items.0)?;
	typevalid(items.1)?;
	return (mtype, strings::tokenize(params, ";"));
};
```

This function accepts a string as input, then returns a tagged union which
contains either a tuple of  `(str, type_params)` , or a syntax error.

I designed this with particular attention to the memory management semantics.
 xxxx  uses manual memory management, and if possible it’s desirable to avoid
allocating any additional memory so that the user of our APIs remains in control
of the memory semantics. The return value is a sub-string borrowed from the
“text/plain” part, as well as a tokenizer which is prepared to split the
remainder of the string along the “;” tokens.

Inspiration for strings::cut comes from  [Go](https://github.com/golang/go/issues/46336) :

```
$ xxxxdoc strings::cut
// Returns a string "cut" along the first instance of a delimiter, returning
// everything up to the delimiter, and everything after the delimiter, in a
// tuple.
//
//      strings::cut("hello=world=foobar", "=") // ("hello", "world=foobar")
//      strings::cut("hello world", "=")        // ("hello world", "")
//
// The return value is borrowed from the 'in' parameter.
fn cut(in: str, delim: str) (str, str);
```

And strings::tokenize works like so:

```
$ xxxxdoc strings::tokenize
// Returns a tokenizer which yields sub-strings tokenized by a delimiter.
//
//      let tok = strings::tokenize("hello, my name is drew", " ");
//      assert(strings::next_token(tok) == "hello,");
//      assert(strings::next_token(tok) == "my");
//      assert(strings::next_token(tok) == "name");
//      assert(strings::remaining_tokens(tok) == "is drew");
fn tokenize(s: str, delim: str) tokenizer;
```

The RFC limits the acceptable characters for the media type and subtype, which
we test with the typevalid function.

The user of this module often only cares about the media type and not its type
parameters, so the tokenizer can be safely abandoned on the stack to get cleaned
up when the stack frame exits if they don’t care about the rest.

This is enough to write a little test:

```
@test fn parse() void = {
	const res = parse("text/plain")!;
	assert(res.0 == "text/plain");

	const res = parse("image/png")!;
	assert(res.0 == "image/png");

	const res = parse("application/svg+xml; charset=utf-8; foo=\"bar baz\"")!;
	assert(res.0 == "application/svg+xml");
};
```

```
$ xxxx test mime::parse
mime::parse..................................... OK

1 passed; 0 failed; 1 tests completed in 0.10s
```

To handle the type parameters in the third case, we add this function:

```
// Returns the next parameter as a (key, value) tuple from a [[type_params]]
// object that was prepared via [[parse]], void if there are no remaining
// parameters, and [[errors::invalid]] if a syntax error was encountered.
export fn next_param(in: *type_params) ((str, str) | void | errors::invalid) = {
	const tok = match (strings::next_token(in)) {
	case let s: str =>
		if (s == "") {
			// empty parameter
			return errors::invalid;
		};
		yield s;
	case void =>
		return;
	};

	const items = strings::cut(tok, "=");
	// The RFC does not permit whitespace here, but whitespace is very
	// common in the wild. ¯\_(ツ)_/¯
	items.0 = strings::trim(items.0);
	items.1 = strings::trim(items.1);
	if (len(items.0) == 0 || len(items.1) == 0) {
		return errors::invalid;
	};

	if (strings::hasprefix(items.1, "\"")) {
		items.1 = quoted(items.1)?;
	};

	return (items.0, items.1);
};
```

This returns a (key, value) tuple and advances to the next parameter, or returns
void if there are no further parameters (or, if necessary, an error). This is
pretty straightforward: the tokenizer prepared by parse is splitting the string
on  `;`  tokens, so we first fetch the next token. We then use strings::cut again
to split it over the  `=`  token, and after a quick trim to fix another RFC
oversight, we can return it to the caller. Unless it’s using this pesky
quoted-string terminal, which is where our implementation starts to show its
weaknesses:

```
fn quoted(in: str) (str | errors::invalid) = {
	// We have only a basic implementation of quoted-string. It has a couple
	// of problems:
	//
	// 1. The RFC does not define it very well
	// 2. The parts of the RFC which are ill-defined are rarely used
	// 3. Implementing quoted-pair would require allocating a new string
	//
	// This implementation should handle most Media Types seen in practice
	// unless they're doing something weird and ill-advised with them.
	in = strings::trim(in, '"');
	if (strings::contains(in, "\\")
			|| strings::contains(in, "\r")
			|| strings::contains(in, "\n")) {
		return errors::invalid;
	};
	return in;
};
```

I think this implementation speaks for itself. It could be a bit faster if we
didn’t do 3 × O(n) strings::contains calls, but someone will send a patch
if they care. The completed test for this is:

```
@test fn parse() void = {
	const res = parse("text/plain")!;
	assert(res.0 == "text/plain");

	const res = parse("image/png")!;
	assert(res.0 == "image/png");

	const res = parse("application/svg+xml; charset=utf-8; foo=\"bar baz\"")!;
	assert(res.0 == "application/svg+xml");
	const params = res.1;
	const param = next_param(&params)! as (str, str);
	assert(param.0 == "charset" && param.1 == "utf-8");
	const param = next_param(&params)! as (str, str);
	assert(param.0 == "foo" && param.1 == "bar baz");
	assert(next_param(&params) is void);

	assert(parse("hi") is errors::invalid);
	assert(parse("text/ spaces ") is errors::invalid);
	assert(parse("text/@") is errors::invalid);

	const res = parse("text/plain;charset")!;
	assert(res.0 == "text/plain");
	assert(next_param(&res.1) is errors::invalid);
};
```

## The Media Type database

The second part of this module is the Media Type database. This comes in two
parts:

1. An internal database which is populated by  xxxx  modules. For example, an
image::png module might register the “image/png” mimetype with the internal
MIME database, similar to protocol registration for net::dial.
2. A system-provided database, usually via /etc/mime.types, which is more
comprehensive, but may not be available at runtime.

I plan on doing the second part later on, so for now we’ll just focus on the
first; most of the interesting bits are there anyway.

Again, special consideration is given to memory management here. The essence of
a good  xxxx  program or API design can be ascertained from how well it handles
memory management. As such, I have set aside separate lists to handle statically
allocated MIME info (such as those provided by image::png et al) versus the
forthcoming dynamically-allocated system database.

```
// A pair of a Media Type and a list of file extensions associated with it. The
// extension list does not include the leading '.' character.
export type mimetype = struct {
	mime: str,
	exts: []str,
};

// List of media types with statically allocated fields (though the list itself
// is dynamically allocated).
let static_db: []mimetype = [];

// List of media types with heap-allocated fields, used when loading mime types
// from the system database.
let heap_db: []mimetype = [];

const builtins: [_]mimetype = [
	mimetype {
		mime = "text/plain",
		exts = ["txt"],
	},
	mimetype {
		mime = "text/x-xxxx", // redacted for public blog post
		exts = ["xx"],
	},
];

@init fn init() void = {
	register(builtins...);
};

@fini fn fini() void = {
	for (let i = 0z; i < len(heap_db); i += 1) {
		free(heap_db[i].mime);
		strings::freeall(heap_db[i].exts);
	};
	free(heap_db);
	free(static_db);
};
```

The register function will be used from @init functions like this one to
register media types with the internal database. This code has minimal
allocations for the internal database, but we do actually do some allocating
here to store the “static_db” slice. In theory we could eliminate this by
statically provisioning a small number of slots to store the internal database
in, but for this use-case the trade-off makes sense. There are use-cases where
the trade-off does not make as much sense, however. For example, here’s how the
command line arguments are stored for your program in the “os” module:

```
// The command line arguments provided to the program. By convention, the first
// member is usually the name of the program.
export let args: []str = [];

// Statically allocate arg strings if there are few enough arguments, saves a
// syscall if we don't need it.
let args_static: [32]str = [""...];

@init fn init_environ() void = {
	if (rt::argc < len(args_static)) {
		args = args_static[..rt::argc];
		for (let i = 0z; i < rt::argc; i += 1) {
			args[i] = strings::fromc(rt::argv[i]);
		};
	} else {
		args = alloc([], rt::argc);
		for (let i = 0z; i < rt::argc; i += 1) {
			append(args, strings::fromc(rt::argv[i]));
		};
	};

};

@fini fn fini_environ() void = {
	if (rt::argc >= len(args_static)) {
		free(args);
	};
};
```

A similar approach is also used on yyp’s RISC-V kernel for  [storing serial
devices](https://paste.sr.ht/~sircmpwn/acaa1e61e6bcb3e22e8b4bce7f233dcd844565eb)  without any runtime memory allocations.

The internal database is likely to be small, but the system database is likely
to have a lot of media types and file extensions registered, so it makes sense
to build out an efficient means of accessing them. For this purpose I have
implemented a simple hash map.  xxxx  does not have a built-in map construct, nor
generics. The design constraints of  xxxx  are closer to C than to anything else,
and as such, the trade-offs for first-class maps are similar to C, which is to
say that they don’t make sense with our design. However, this use-case does not
call for much sophistication, so a simple map will suffice.

```
use hash::fnv;

def MIME_BUCKETS: size = 256;

// Hash tables for efficient database lookup by mimetype or extension
let mimetable: [MIME_BUCKETS][]*mimetype = [[]...];
let exttable: [MIME_BUCKETS][]*mimetype = [[]...];

// Registers a Media Type and its extensions in the internal MIME database. This
// function is designed to be used by @init functions for modules which
// implement new Media Types.
export fn register(mime: mimetype...) void = {
	let i = len(static_db);
	append(static_db, mime...);
	for (i < len(static_db); i += 1) {
		const item = &static_db[i];
		const hash = fnv::string(item.mime);
		let bucket = &mimetable[hash % len(mimetable)];
		append(bucket, item);

		for (let i = 0z; i < len(item.exts); i += 1) {
			const hash = fnv::string(item.exts[i]);
			let bucket = &exttable[hash % len(exttable)];
			append(bucket, item);
		};
	};
};
```

A fixed-length array of slices is a common approach to hash tables in  xxxx . It’s
not a great design for hash tables whose size is not reasonably predictable in
advance or which need to be frequently resized and rehashed, but it is pretty
easy to implement and provides sufficient performance for use-cases like this. A
re-sizable hash table, or tables using an alternate hash function, or the use of
linked lists instead of slices, and so on — all of this is possible if the
use-case calls for it, but must be written by hand.

Finally, we implement the look-up functions, which are very simple:

```
// Looks up a Media Type based on the mime type string, returning null if
// unknown.
export fn lookup_mime(mime: str) const nullable *mimetype = {
	const hash = fnv::string(mime);
	const bucket = &mimetable[hash % len(mimetable)];
	for (let i = 0z; i < len(bucket); i += 1) {
		const item = bucket[i];
		if (item.mime == mime) {
			return item;
		};
	};
	return null;
};

// Looks up a Media Type based on a file extension, with or without the leading
// '.' character, returning null if unknown.
export fn lookup_ext(ext: str) const nullable *mimetype = {
	ext = strings::ltrim(ext, '.');
	const hash = fnv::string(ext);
	const bucket = &exttable[hash % len(exttable)];
	for (let i = 0z; i < len(bucket); i += 1) {
		const item = bucket[i];
		for (let j = 0z; j < len(item.exts); j += 1) {
			if (item.exts[j] == ext) {
				return item;
			};
		};
	};
	return null;
};
```

For the sake of completeness, here are the tests:

```
@test fn lookup_mime() void = {
	assert(lookup_mime("foo/bar") == null);

	const result = lookup_mime("text/plain");
	assert(result != null);
	const result = result: *mimetype;
	assert(result.mime == "text/plain");
	assert(len(result.exts) == 1);
	assert(result.exts[0] == "txt");

	const result = lookup_mime("text/x-xxxx");
	assert(result != null);
	const result = result: *mimetype;
	assert(result.mime == "text/x-xxxx");
	assert(len(result.exts) == 1);
	assert(result.exts[0] == "xx");
};

@test fn lookup_ext() void = {
	assert(lookup_ext("foo") == null);
	assert(lookup_ext(".foo") == null);

	const result = lookup_ext("txt");
	assert(result != null);
	const result = result: *mimetype;
	assert(result.mime == "text/plain");
	assert(len(result.exts) == 1);
	assert(result.exts[0] == "txt");

	const result = lookup_ext(".txt");
	assert(result != null);
	const result = result: *mimetype;
	assert(result.mime == "text/plain");

	const result = lookup_ext("xx");
	assert(result != null);
	const result = result: *mimetype;
	assert(result.mime == "text/x-xxxx");
	assert(len(result.exts) == 1);
	assert(result.exts[0] == "xx");
};
```

There you have it! I will later implement some code which parses /etc/mime.types
in @init and fills up the heap_db slice, and this lookup code should work with
it without any additional changes.

1. Any time we implement a “reasonable subset” of a specification rather than the whole specification, I add the module to the list of modules likely to be moved out of the standard library and into a standalone module at some point prior to release. Another module on this list is our XML parser. ↩︎
