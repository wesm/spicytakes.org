---
title: "How to design a new programming language from scratch"
date: 2020-12-25
url: https://drewdevault.com/2020/12/25/How-to-design-a-new-programming-language.html
slug: How-to-design-a-new-programming-language
word_count: 832
---

There is a long, difficult road from vague, pie-in-the-sky ideas about what
would be cool to have in a new programming language, to a robust,
self-consistent, practical implementation of those ideas. Designing and
implementing a new programming language from scratch is one of the most
challenging tasks a programmer can undertake.

Note: this post is targeted at motivated programmers who want to make a
serious attempt at designing a useful programming language. If you just want to
make a language as a fun side project, then you can totally just wing it. Taking
on an unserious project of that nature is also a good way to develop some
expertise which will be useful for a serious project later on.

Let’s set the scene. You already know a few programming languages, and you know
what you like and dislike about them — these are your influences. You have
some cool novel language design ideas as well. A good first step from here is to
dream up some pseudocode, putting some of your ideas to paper, so you can get an
idea of what it would actually feel like to write or read code in this
hypothetical language. Perhaps a short write-up or a list of goals and ideas is
also in order. Circulate these among your confidants for discussion and
feedback.

Ideas need to be proven in the forge of implementations, and the next step is to
write a compiler (or interpreter — everything in this article applies
equally to them). We’ll call this the sacrificial implementation, because you
should be prepared to throw it away later. Its purpose is to prove that your
design ideas work and can be implemented efficiently, but  *not*  to be the
production-ready implementation of your new language. It’s a tool to help you
refine your language design.

To this end, I would suggest using a parser generator like yacc to create your
parser, even if you’d prefer to ultimately use a different design (e.g.
recursive descent). The ability to quickly make changes to your grammar, and the
side-effect of having a formal grammar written as you work, are both valuable to
have at this stage of development. Being prepared to throw out the rest of the
compiler is helpful because, due to the inherent difficulty of designing and
implementing a programming language at the same time, your first implementation
will probably be shit. You don’t know what the language will look like, you’ll
make assumptions that you have to undo later, and it’ll undergo dozens of
refactorings. It’s gonna suck.

However, shit as it may be, it will have done important work in validating your
ideas and refining your design. I would recommend that your next step is to
start working on a formal specification of the language (something that I
believe all languages should have). You’ve proven what works, and writing it up
formally is a good way to finalize the ideas and address the edge cases. Gather
a group of interested early adopters, contributors, and subject matter experts
(e.g. compiler experts who work with similar languages), and hold discussions on
the specification as you work.

This is also a good time to start working on your second implementation. At this
point, you will have a good grasp on the overall compiler design, the flaws from
your original implementation, and better skills as a compiler programmer.
Working on your second compiler and your specification at the same time can help
as both endeavours inform the others — a particularly difficult detail to
implement could lead to a simplification in the spec, and an under-specified
detail getting shored up could lead to a more robust implementation.

Don’t get carried away — keep this new compiler simple and small. Don’t go
crazy on nice-to-have features like linters and formatters, an exhaustive test
suite, detailed error messages, a sophisticated optimizer, and so on. You want
it to implement the specification as simply as possible, so that you can use it
for the next step: the hosted compiler. You need to write a third
implementation, using your own language to compile itself.

The second compiler, which I hope you wrote in C, is now the bootstrap compiler.
I recommend keeping it up-to-date with the specification and maintaining it
perpetually as a convenient path to bootstrap your toolchain from scratch
(looking at you, Rust). But it’s not going to be the final implementation: any
self-respecting general-purpose programming language is implemented in itself.
The next, and final step, is to implement your language for a third time.

At this point, you will have refined and proven your language design. You will
have developed and applied compiler programming skills. You will have a robust
implementation for a complete and self-consistent programming language,
developed carefully and with the benefit of hindsight. Your future community
will thank you for the care and time you put into this work, as your language
design and implementation sets the ceiling on the quality of programs written in
it.
