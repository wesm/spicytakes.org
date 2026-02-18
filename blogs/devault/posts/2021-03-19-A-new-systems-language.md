---
title: "We are building a new systems programming language"
date: 2021-03-19
url: https://drewdevault.com/2021/03/19/A-new-systems-language.html
slug: A-new-systems-language
word_count: 524
---

It’s an open secret: the “secret project” I’ve been talking about is a new
systems programming language. It’s been underway since December ‘19, and we hope
to release the first version in early 2022. The language is pretty small —
we have a mostly complete specification which clocks in at 60 pages. It has
manual memory management, no runtime, and it uses a superset of the C ABI,
making it easy to link with libraries and C code. It should be suitable almost
anywhere C is useful: compilers, system utilities, operating systems, network
servers and clients, and so on.

```
use io;

export fn main() void = {
	const greetings = [
		"Hello, world!",
		"¡Hola Mundo!",
		"Γειά σου Κόσμε!",
		"Привет мир!",
		"こんにちは世界！",
	];
	for (let i = 0z; i < len(greetings); i += 1) {
		io::println(greetings[i]);
	};
};
```

We could compare our language to many other languages, but let’s start with how
it compares to C:

* More robust error handling via tagged unions
* Improved, Unicode-aware string support
* Memory safe array, slice, and pointer types (and unsafe versions, if needed)
* Direct compatibility with the C ABI for trivial C interop
* A simpler, context-free, expression-oriented syntax
* A standard library free of the constraints of POSIX or the C standard

Our language currently supports Linux on x86_64 or aarch64, and we plan on
expanding this to the BSDs, Haiku, and Plan 9; as well as i686, riscv64 and
riscv32, and ppc64 before the release.

I plan to continue keeping the other details a secret until the release —
we want the first release to be a complete, stable, production-ready programming
language with all of the trimmings. The first time most people will hear about
this language will also be the first time they can ship working code with it.

However, if you want to get involved sooner, there’s a way: we need your help.
So far, we’ve written most of the spec, the first of two compilers, and about
15,000 lines of the standard library. The standard library is what needs the
most help, and I’m seeking volunteers to get involved.

The standard library mandate begins with the following:

> The xxxx standard library shall provide: 
> Useful features to complement xxxx language features
> An interface to the host operating system
> Implementations of broadly useful algorithms
> Implementations of broadly useful formats and protocols
> Introspective meta-features for xxxx-aware programs
>  Each of these services shall: 
> Have a concise and straightforward interface
> Correctly and completely implement the useful subset of the required behavior
> Provide complete documentation for each exported symbol
> Be sufficiently tested to provide confidence in the implementation

We have a number of focus areas for standard library development. I expect most
contributors, at least at first, to stick to one or two of these areas. The
focus areas we’re looking into now are:

If any of this sounds up your alley, we’d love your help! Please  [write me an
email](mailto:sir@cmpwn.com)  describing your interest areas and previous systems
programming experience.

**Update 2021-03-20** : We’re targeting the first release in early 2022, not 2021.
