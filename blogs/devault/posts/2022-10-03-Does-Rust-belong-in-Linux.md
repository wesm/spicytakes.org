---
title: "Does Rust belong in the Linux kernel?"
date: 2022-10-03
url: https://drewdevault.com/2022/10/03/Does-Rust-belong-in-Linux.html
slug: Does-Rust-belong-in-Linux
word_count: 1692
---

I am known to be a bit of a polemic when it comes to Rust. I will be forthright
with the fact that I don’t particularly care for Rust, and that my public
criticisms of it might set up many readers with a reluctance to endure yet
another Rust Hot Take from my blog. My answer to the question posed in the title
is, of course, “no”. However, let me assuage some of your fears by answering
a different question first: does Hare belong in the Linux kernel?

If I should owe my allegiance to any programming language, it would be
 [Hare](https://harelang.org) . Not only is it a systems programming language that
I designed myself, but I am using it  [to write a kernel](https://git.sr.ht/~sircmpwn/helios) .  [Like
Rust](https://www.redox-os.org/) , Hare is demonstrably useful for writing kernels with. One might
even go so far as to suggest that I consider it superior to C for this purpose,
given that I chose to to write Helios in Hare rather than C, despite my
extensive background in C. But the question remains: does Hare belong in the
Linux kernel?

In my opinion, Hare does not belong in the Linux kernel, and neither does Rust.
Some of the reasoning behind this answer is common to both, and some is unique
to each, but I will be focusing on Rust today because Rust is the language which
is actually making its way towards mainline Linux. I have no illusions about
this blog post changing that, either: I simply find it an interesting case-study
in software engineering decision-making in a major project, and that’s worth
talking about.

Each change in software requires sufficient supporting rationale. What are the
reasons to bring Rust into Linux? A kernel hacker thinks about these questions
differently than a typical developer in userspace. One could espouse the
advantages of Cargo, generics, whatever, but these concerns matter relatively
little to kernel hackers. Kernels operate in a heavily constrained design space
and a language has to fit into that design space. This is the first and foremost
concern, and if it’s awkward to mold a language to fit into these constraints
then it will be a poor fit.

Some common problems that a programming language designed for userspace will run
into when being considered for kernelspace are:

* Strict constraints on memory allocation
* Strict constraints on stack usage
* Strict constraints on recursion
* No use of floating point arithmetic
* Necessary evils, such as unsafe memory use patterns or integer overflow
* The absence of a standard library, runtime, third-party libraries, or other
conveniences typically afforded to userspace

Most languages can overcome these constraints with some work, but their
suitability for kernel use is mainly defined by how well they adapt to them
— there’s a reason that kernels written in Go, C#, Java, Python, etc, are
limited to being research curiosities and are left out of production systems.

As Linus recently put it, “kernel needs trump any Rust needs”. The kernel is
simply not an environment which will bend to accommodate a language; it must go
the other way around. These constraints have posed, and will continue to pose, a
major challenge for Rust in Linux, but on the whole, I think that it will be
able to rise to meet them, though perhaps not with as much grace as I would
like.

If Rust is able to work within these constraints, then it satisfies the ground
rules for playing in ring 0. The question then becomes: what advantages can Rust
bring to the kernel? Based on what I’ve seen, these essentially break down to
two points: 1

1. Memory safety
2. Trendiness

I would prefer not to re-open the memory safety flamewar, so we will simply move
forward with the (dubious) assumptions that memory safety is (1) unconditionally
desirable, (2) compatible with the kernel’s requirements, and (3) sufficiently
provided for by Rust. I will offer this quote from an unnamed kernel hacker,
though:

> There are possibly some well-designed and written parts which have not
> suffered a memory safety issue in many years. It’s insulting to present this
> as an improvement over what was achieved by those doing all this hard work.

Regarding “trendiness”, I admit that this is a somewhat unforgiving turn of
phrase. In this respect I refer to the goal of expanding the kernel’s developer
base from a bunch of aging curmudgeons writing C 2  towards a more
inclusive developer pool from a younger up-and-coming language community like
Rust. C is boring 3  — it hasn’t really excited anyone in decades.
Rust is exciting, and its community enjoys a huge pool of developers building
their brave new world with it. Introducing Rust to the kernel will certainly
appeal to a broader audience of potential contributors.

But there is an underlying assumption to this argument which is worth
questioning: is the supply of Linux developers dwindling, and, if so, is it to
such and extent that it demands radical change?

Well, no. Linux has consistently enjoyed a tremendous amount of attention from
the software development community. This week’s release of Linux 6.0, one of the
largest Linux releases ever, boasted more than 78,000 commits by almost 5,000
different authors since 5.15. Linux has a broad developer base reaching from
many different industry stakeholders and independent contributors working on the
careful development and maintenance of its hundreds of subsystems. The scale of
Linux development is on a level unmatched by any other software project —
free software or otherwise.

Getting Rust working in Linux is certainly an exciting project, and I’m all for
developers having fun. However, it’s not likely to infuse Linux with a
much-needed boost in its contributor base, because Linux has no such need.
What’s more, Linux’s portability requirements prevent Rust from being used in
most of the kernel in the first place. Most work on Rust in Linux is simply
working on getting the systems to cooperate with each other or writing drivers
which are redundant with existing C drivers, but cannot replace them due to
Rust’s limited selection of targets. 4  Few to none of the efforts from the
Rust-in-Linux team are likely to support the kernel’s broader goals for some
time.

We are thus left with memory safety as the main benefit offered by Rust to
Linux, and for the purpose of this article we’re going to take it at face value.
So, with the ground rules set and the advantages enumerated, what are some of
the problems that Rust might face in Linux?

There are a few problems which could be argued over, such as substantial
complexity of Rust compared to C, the inevitable doubling of Linux’s build time,
the significant shift in design sensibilities required to support an idiomatic
Rust design, the fragile interface which will develop on the boundaries between
Rust and C code, or the challenges the kernel’s established base of C developers
will endure when learning and adapting to a new language. To avoid letting this
post become too subjective or lengthy, I’ll refrain from expanding on these.
Instead, allow me to simply illuminate these issues as risk factors.

Linux is, on the whole, a conservative project. It is deployed worldwide in
billions of devices and its reliability is depended on by a majority of Earth’s
population. Risks are carefully evaluated in Linux as such. Every change
presents risks and offers advantages, which must be weighed against each other
to justify the change. Rust is one of the riskiest bets Linux has ever
considered, and, in my opinion, the advantages may not weigh up. I think that
the main reason we’re going to see Rust in the kernel is not due to a careful
balancing of risk and reward, but because the Rust community wants Rust in
Linux, and they’re large and loud enough to not be worth the cost of arguing
with.

I don’t think that changes on this scale are appropriate for most projects. I
prefer to encourage people to write new software to replace established
software, rather than rewriting the established software. Some projects, such as
 [Redox](https://www.redox-os.org/) , are doing just that with Rust. However, operating systems are in
a difficult spot in this respect. Writing an operating system is difficult work
with a huge scope — few projects can hope to challenge Linux on driver
support, for example. The major players have been entrenched for decades, and
any project seeking to displace them will have decades of hard work ahead of
them and will require a considerable amount of luck to succeed. Though I think
that new innovations in kernels are badly overdue, I must acknowledge that
there is some truth to the argument that we’re stuck with Linux. In this
framing, if you want Rust to succeed in a kernel, getting it into Linux is the
best strategy.

But, on the whole, my opinion is that the benefits of Rust in Linux are
negligible and the costs are not. That said, it’s going to happen, and the
impact to me is likely to be, at worst, a nuisance. Though I would have chosen
differently, I wish them the best of luck and hope to see them succeed.

1. There are some other arguable benefits which mainly boil down to
finding Rust to have a superior language design to C or to be more enjoyable
to use. These are subjective and generally are not the most important traits
a kernel hacker has to consider when choosing a language, so I’m leaving them
aside for now. ↩︎
2. A portrayal which, though it may have a grain of truth, is largely false
and offensive to my sensibilities as a 29-year-old kernel hacker. For the
record. ↩︎
3. A trait which, I will briefly note, is actually desirable for a
production kernel implementation. ↩︎
4. Rust in GCC will help with this problem, but it will likely take several
years to materialize and several more years to become stable. Even when this
is addressed, rewriting drivers wholesale will be labor intensive and is
likely to introduce more problems than solutions — rewrites always
introduce bugs. ↩︎
