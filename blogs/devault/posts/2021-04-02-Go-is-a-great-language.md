---
title: "Go is a great programming language"
date: 2021-04-02
url: https://drewdevault.com/2021/04/02/Go-is-a-great-language.html
slug: Go-is-a-great-language
word_count: 964
---

No software is perfect, and thus even for software I find very pleasant, I can
usually identify some problems in it — often using my blog to do so. Even
my all-time favorite software project, Plan 9, has some painful flaws! For some
projects, it may be my fondness for them that drives me to criticise them even
more, in the hope that they’ll live up to the level of respect I feel for them.

One such project is the Go programming language. I have had many criticisms,
often shared on this blog and elsewhere, but for the most part, my praises have
been aired mainly in private. I’d like to share some of those praises today,
because despite my criticisms of it, Go remains one of the best programming
languages I’ve ever used, and I have a great deal of respect for it.

Perhaps the matter I most appreciate Go for is its long-term commitment to
simplicity, stability, and robustness. I prize these traits more strongly than
any other object of software design. The Go team works with an ethos of
careful restraint, with each feature given deliberate consideration towards
identifying the simplest and most complete solution, and they carefully
constrain the scope of their implementations to closely fit those solutions.
The areas where Go has failed in this regard are frightfully scarce.

The benefits of their discipline are numerous. The most impressive
accomplishment that I attribute to this approach is the quality of the Go
ecosystem at large. In the first place, it is a great accomplishment to produce
a language and standard library with the excellence in design and implementation
that Go offers, but it’s a truly profound achievement to have produced a design
which the community  *at large*  utilizes to make similarly excellent designs as a
basic consequence of the language’s simple elegance.  Very few other languages
enjoy a similar level of consistency and quality in the ecosystem.

Go is also notable for essentially inventing its own niche, and then helping
that niche grow around it into an entirely new class of software design. I
consider Go not to be a systems programming language — a title much better
earned by languages like C and Rust. Rather, Go is the best-in-class for a new
breed of software: an Internet programming language. 1  The wealth of network
protocols implemented efficiently, concisely, and correctly in its standard
library, combined with its clever mixed cooperative/pre-emptive multitasking
model, make it very easy to write scalable internet-facing software. A few other
languages — Elixir comes to mind — also occupy this niche, but they
haven’t enjoyed the runaway success that Go has.

The Go team has also earned my respect for their professionalism. The close
degree to which Go is tied to Google comes with its own set of trade-offs, but
the centralization of project leadership caused by this relationship is
beneficial for the project. Some members of the Go community have noticed the
apparent disadvantages of this structure, as Go is infamous for being slow to
respond to the wants of its community. This insulation, I would argue, is in
fact advantageous for the conservative language design that Go embraces, and
may actually be essential to its value-add as a project. If Go listened to the
community as much as they want, it would become a kitchen sink, and cease to be
interesting to me.

Rather than being closely tied to its community’s wants, Go generally does a
much better job of being closely tied to its community’s  *needs* . If you have
correctly identified a problem in Go, when you bring it to their attention, you
will be taken seriously. Many projects struggle to separate their egos from the
software, and when mistakes are found, they take it personally. Go does an
excellent job of treating it like an engineer — a matter-of-fact analysis
of the problem, deliberation on the solution, and shipping of a fix. 2  Go has
a reputation for plain old good engineering.

In short, I admire Go very much, despite my frequent criticisms. I recognize Go
as one of the best programming languages ever made. Go has attained an elusive
status in the programming canon as a robust engineering tool that can be
expected to work, and work well, in its applications for decades to come. Its
because of this respect that I hold Go to such a high standard, and I hope that
it continues to impress me going forward.

1. It took me a while to understand this. It was a mistake for Go to be marketed as a systems language. Any systems programmer would rightfully tell you that a language with a garbage collector and magic cooperative/pre-emptive threads is a non-starter for systems programming. But, what Go was really designed for, and is mainly used for, is not exactly systems programming. Internet-facing code has straddled the line between systems programming and high-level programming for a while: high-performance systems software would often be written in, say, C — which is definitely a systems programming language — but the vastness of the Internet’s problem space also affords for a large number of programs for which a higher-level programming languages are a better fit, such as Java, C#, etc — and these are definitely not systems programming languages. Go is probably the first language to specifically target this space in-between with this degree of success, and it kind of makes a new domain for itself in so doing: it is the first widely successful “Internet programming language”. ↩︎
2. Sometimes, this has not been the case, and this was the cause of some of my harshest criticisms of Go. Many of Go’s advantages stem from, and even *require*, this dispassionate, matter-of-fact engineering ethos that I appreciate from Go. ↩︎
