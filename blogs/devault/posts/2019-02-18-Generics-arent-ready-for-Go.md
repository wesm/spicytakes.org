---
title: "Generics aren't ready for Go"
date: 2019-02-18
url: https://drewdevault.com/2019/02/18/Generics-arent-ready-for-Go.html
slug: Generics-arent-ready-for-Go
word_count: 1002
---

In the distance, a gradual roar begins to grow in volume. A dust cloud is
visible over the horizon. As it nears, the shouts of the oncoming angry mob can
be heard. Suddenly, it stops, and a brief silence ensues. Then the air is filled
with the clackings of hundreds of keyboards, angrily typing the owner’s opinion
about generics and Go. The clans of Java, C#, Rust, C++, TypeScript, Haskell,
and more - usually mortal enemies - have combined forces to fight in what may
become one of the greatest flamewars of our time. And none of them read more
than the title of this article before writing their comment.

Have you ever seen someone write something to the effect of “I would use Go, but
I need generics”? Perhaps we can infer from this that many of the people who are
pining after generics in Go are not, in fact, Go users. Many of them are users
of another programming language that  *does*  have generics, and they feel that
generics are a good fit for this language, and therefore a good fit for any
language. The inertia of “what I’m used to” comes to a violent stop when they
try to use Go. People affected by this frustration interpret it as a problem
with Go, that Go is missing some crucial feature - such as generics. But this
lack of features is itself a feature, not a bug.

Go strikes me as one of the most conservative programming languages available
today. It’s small and simple, and every detail is carefully thought out. There
are very few dusty corners of Go - in large part because Go has fewer corners in
general than most programming languages. This is a major factor in Go’s success
to date, in my opinion. Nearly all of Go’s features are bulletproof, and in my
opinion are among the best implementations of their concepts in our entire
industry. Achieving this feat requires having  *fewer*  features in total.
Contrast this to C++, which has too many footguns to count. You  *could*  write a
book called “C++: the good parts”, but consider that such a book about Go would
just be a book about Go. There’s little room for the bad parts in such a spartan
language.

So how should we innovate in Go? Consider the case of dependency management. Go
1.11 shipped with the first version of Go modules, which, in my opinion, is a
game changer. I passionately hate  `$GOPATH` , and I thought dep wasn’t much
better. dep’s problem is that it took the dependency management ideas that other
programming languages have been working with and brought the same ideas to Go.
Instead, Go modules took the idea of dependency management and rethought it from
first principles, then landed on a much more elegant solution that I think other
programming languages will spend the next few years catching up with. I like to
make an analogy to physics: dep is like  [General Relativity](https://en.wikipedia.org/wiki/General_relativity)  or  [the
Standard Model](https://en.wikipedia.org/wiki/Standard_Model) , whereas Go modules are more like the  [Grand Unified
Theory](https://en.wikipedia.org/wiki/Grand_Unified_Theory) . Go doesn’t settle for anything less when adding features. It’s
not a language where liberal experimentation with imperfect ideas is desirable.

I feel that this applies to generics. In my opinion, generics are an imperfect
solution to an unsolved problem in computer science. None of the proposals I’ve
seen (notably  [contracts](https://go.googlesource.com/proposal/+/master/design/go2draft-contracts.md) ) feel  *right*  yet. Some of this is a gut
feeling, but there are tangible problems as well. For example, the space of
problems they solve intersects with other Go features, which weakens the
strength of both features. “Which solution do I use to this problem” is a
question which different people will answer differently, and consequently their
code at best won’t agree on what “idiomatic” means and at worst will be simply
incompatible.  Another problem is that the proposal changes the meaning of
idiomatic Go in the first place - suddenly huge swaths of the Go code, including
the standard library, will become unidiomatic. One of Go’s greatest strengths is
that code written 5 years ago is still idiomatic. It’s almost impossible to
write unidiomatic Go code at all.

I used to sneer at the Go maintainers alongside everyone else whenever they’d
punt on generics. With so many people pining after it, why haven’t they seen
sense yet? How can they know better than all of these people? My tune changed
once I started to use Go more seriously, and now I admire their restraint.  Part
of this is an evolution of my values as a programmer in general: simplicity and
elegance are now the principles I optimize for, even if it means certain classes
of programs are simply not on the table. And I think Go should be comfortable
not being suitable for writing certain classes of programs. I don’t think
programming languages should compete with each other in an attempt to become the
perfect solution to every problem.  This is impossible, and attempts will just
create a messy kitchen sink that solves every problem poorly.

fig. 1: the result of C++'s attempt to solve all problems

The constraints imposed by the lack of generics (and other things Go lacks)
breed creativity.  If you’re fighting Go’s lack of generics trying to do
something Your Way, you might want to step back and consider a solution to the
problem which embraces the limitations of Go instead. Often when I do this the
new solution is a much better design.

So it’s my hope that Go will hold out until the right solution presents itself,
and it hasn’t yet. Rushing into it to appease the unwashed masses is a bad idea.
There are other good programming languages - use them! I personally use a wide
variety of programming languages, and though I love Go dearly, it probably only
comes in 3rd or 4th place in terms of how frequently it appears in my projects.
It’s  *excellent*  in its domain and doesn’t need to awkwardly stumble into
others.
