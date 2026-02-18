---
title: "Lessons to learn from C"
date: 2017-01-30
url: https://drewdevault.com/2017/01/30/Lessons-to-learn-from-C.html
slug: Lessons-to-learn-from-C
word_count: 777
---

C is my favorite language, though I acknowledge that it has its warts. I’ve
tried looking at languages people hope will replace C (Rust, Go, etc), and
though they’ve improved on some things they won’t be supplanting C in my life
any time soon. I’ll share with you what makes C a great language to me. Take
some of these things as inspiration for the next C replacement you write.

First of all, it’s important to note that I’m talking about the language, not
its standard library. The C standard library isn’t  *awful* , but it certainly
leaves a lot to be desired. I also want to place a few limitations on the kind
of C we’re talking about - you can write bad code in any language, and C is no
different. For the purpose of argument, let’s assume the following:

* C99 minimum
* Absolutely no code in headers - just type definitions and function prototypes
* Minimal use of typedefs
* No macros
* No compiler extensions

I hold myself to these guidelines when writing C, and it is from this basis that
I compare other languages with C. It’s not useful to compare bad C to another
language, because I wouldn’t want to write bad C either.

Much of what I like about C boils down to this:  **C is simple** . The ultimate
goal of any system should be to attain the simplest solution for the problems it
faces. C prefers to be conservative with new features. The lifetime of a feature
in Rust, for example, from proposal to shipping is generally 0 to 6 months. The
same process in C can take up to 10 years. C is a venerable language, and has
already long since finished adding core features. It is stable, simple, and
reliable.

To this end, language features map closely to behaviors common to most CPUs. C
strikes a nearly perfect balance of usability versus simplicity, which
results in a small set of features that are easy to reason about. A C expert
could roughly predict the assembly code produced by their compiler (assuming
 `-O0` ) for any given C function. It follows that C compilers are easy to write
and reason about.

The same person would also be able to give you a rough idea of the
performance characteristics of that function, pointing out things like cache
misses and memory accesses that are draining on speed, or giving you a precise
understanding of how the function handles memory. If I look at a function in
other languages, it’s much more difficult to discern these things with any
degree of precision without actually compiling the code and looking at the
output.

The compiler also integrates very comfortably with the other tools near it, like
the assembler and linker. Symbols in C map 1:1 to symbols in the object files,
which means linking objects together is simple and easily reasoned about. It
also makes interop with other languages and tools straightforward - there’s a
reason every language has a means of writing C bindings, but not generally C++
bindings. The use of headers to declare external symbols and types is also nicer
than some would have you believe, since it gives you an opportunity to organize
and document your API.

C is also the most portable programming language in the world. Every operating
system on every architecture has a C compiler, and they weren’t really
considered a viable platform until it did. Once you have a C compiler you
generally have everything else, because everything else was either written in C
or was written in a language that was implemented in C. I can write C programs
on/for Linux, Windows, BSD, Minix, plan9, and a dozen other niche operating
systems, or even no operating system, on pretty much any CPU architecture I
want. No other language supports nearly as many platforms as C does.

With these benefits acknowledged, there are some things C could do better. The
standard library is one of them, but we can talk about that some other time.
Another is generics; using void* all the time isn’t good. Some features from
other languages would be nice - I would take something similar to Rust’s match
keyword. Of course, the fragility of memory management in C is a concern that
other languages are wise to address. Undefined behavior is awful.

Even for all of these warts, however, the basic simplicity and elegance of C
keeps me there. I would love to see a language that fixes these problems without
trying to be the kitchen sink, too.

In short, I like C because  **C is simple** .
