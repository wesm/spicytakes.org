---
title: "A great alternative is rarely fatter than what it aims to replace"
date: 2021-02-21
url: https://drewdevault.com/2021/02/21/On-the-traits-of-good-replacements.html
slug: On-the-traits-of-good-replacements
word_count: 851
---

This is not always true, but in my experience, it tends to hold up. We often
build or evaluate tools which aim to replace something kludgy^Wvenerable.
Common examples include shells, programming languages, system utilities, and so
on. Rust, Zig, etc, are taking on C in this manner; so too does zsh, fish, and
oil take on bash, which in turn takes on the Bourne shell. There are many
examples.

All of these tools are fine in their own respects, but they have all failed to
completely supplant the software they’re seeking to improve upon. 1  What these
projects have in common is that they  *expand*  on the ideas of their
predecessors, rather than  *refining*  them. A truly great alternative finds the
nugget of truth at the center of the idea, cuts out the cruft, and solves the
same problem with less.

This is one reason I like Alpine Linux, for example. It’s not really aiming to
replace any distro in particular so much as it competes with the Linux ecosystem
as a whole. Alpine does this by being  *simpler*  than the rest: it’s the only
Linux system I can fit more or less entirely in my head. Compare this to the
most common approach: “let’s make a Debian derivative!” It kind of worked for
Ubuntu, less so for everyone else. The C library Alpine ships,  [musl
libc](https://musl.libc.org) , is another example: it aims to replace glibc by
being leaner and meaner,  [and I’ve talked about its success in this respect
before](https://drewdevault.com/2020/09/25/A-story-of-two-libcs.html) .

Go is a programming language which has done relatively well in this respect. It
aimed to fill a bit of a void in the high-performance internet infrastructure
systems programming niche, 2   3  and it is markedly simpler than most of the
other tools in its line of work. It takes the opportunity to add a few
innovations — its big risk is its novel concurrency model — but Go
balances this with a level of simplicity in other respects which is unchallenged
among its contemporaries, 4  and a commitment to that simplicity which has
endured for years. 5

There are many other examples. UTF-8 is a simple, universal approach which
smooths over the idiosyncrasies of the encoding zoo which pre-dates it, and has
more-or-less rendered its alternatives obsolete. JSON has almost completely
replaced XML, and its grammar famously fits on a business card. 6  On the other
hand, when zsh started as a superset of bash, it crippled its ability to compete
on “having less warts than bash”.

Rust is more vague in its inspirations, and does not start as a superset of
anything. It has, however, done a poor job of scope management, and is
significantly more complex than many of the languages it competes with, notably
C and Go. For this reason, it struggles to root out the hold-outs in those
domains, and it suffers for the difficulty in porting it to new platforms, which
limits its penetration into a lot of domains that C is still thriving in.
However, it succeeds in being much simpler than C++, and I expect that it will
render C++ obsolete in the coming years as such. 7

In computing, we make do with a hodge podge of hacks and kludges which, at best,
approximate the solutions to the problems that computing presents us. If you
start with one such hack as the basis of a supposed replacement and build  *more* 
on top of it, you will inherit the warts, and you may find it difficult to rid
yourself of them. If, instead, you question the premise of the software,
interrogate the underlying problem it’s trying to solve, and apply your
insights, plus a healthy dose of hindsight, you may isolate what’s right from
what’s superfluous, and your simplified solution just might end up replacing the
cruft of yore.

1. Some of the listed examples have not given up and would prefer that I say something to the effect of “but the jury is still out” here. ↩︎
2. That’s a lot of adjectives! ↩︎
3. More concisely, I think of Go as an “internet programming language”, distinct from the systems programming languages that inspired it. Its design shines especially in this context, but its value-add is less pronounced for other tasks in the systems programming domain - compilers, operating systems, etc. ↩︎
4. [The Go spec](https://golang.org/ref/spec) is quite concise and has changed very little since Go’s inception. Go is also unique among its contemporaries for (1) writing a spec which (2) supports the development of multiple competing implementations. ↩︎
5. Past tense, unfortunately, now that Go 2 is getting stirred up. ↩︎
6. It is possible that JSON has achieved *too much* success in this respect, as it has found its way into a lot of use-cases for which it is less than ideal. ↩︎
7. Despite my infamous distaste for Rust, long-time readers will know that where I have distaste for Rust, I have passionate scorn for C++. I’m quite glad to see Rust taking it on, and I hope very much that it succeeds in this respect. ↩︎
