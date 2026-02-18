---
title: "Thoughts on performance & optimization"
date: 2020-02-21
url: https://drewdevault.com/2020/02/21/Thoughts-on-performance.html
slug: Thoughts-on-performance
word_count: 857
---

The idea that programmers ought to or ought not to be called “software
engineers” is a contentious one. How you approach optimization and performance
is one metric which can definitely push my evaluation of a developer towards the
engineering side. Unfortunately, I think that a huge number of software
developers today, even senior ones, are approaching this problem poorly.

Centrally, I believe that you cannot effectively optimize a system which you do
not understand. Say, for example, that you’re searching for a member of a
linked list, which is an O(n) operation. You know this can be improved by
switching from a linked list to a sorted array and using a binary search. So,
you spend a few hours refactoring, commit the implementation, and… the
application is no faster. What you failed to consider is that the lists are
populated from data received over the network, whose latency and bandwidth
constraints make the process much slower than any difference made by the kind of
list you’re using.  If you’re not optimizing your bottleneck, then you’re
wasting your time.

This example seems fairly obvious, and I’m sure you, our esteemed reader, would
not have made this mistake. In practice, however, the situation is usually more
subtle. Thinking about your code really hard, making assumptions, and then
acting on them is not the most effective way to make performance improvements.
Instead, we apply the scientific method: we think really hard,  *form a
hypothesis* , make predictions, test them, and then apply our conclusions.

To implement this process, we need to describe our performance in factual terms.
All software requires a certain amount of resources — CPU time, RAM, disk
space, network utilization, and so on. These can also be described over time,
and evolve as the program takes on different kinds of work. For example, we
could model our program’s memory use as bytes allocated over time, and perhaps
we can correlate this with different stages of work — “when the program
starts task C, the rate of memory allocation increases by 5MiB per second”. We
identify bottlenecks — “this program’s primary bottleneck is disk I/O”.
When we hit performance problems, then we know that we need to upgrade to SSDs,
or predict what reads will be needed later and prep them in advance, cache data
in RAM, etc.

Good optimizations are based on factual evidence that the program is not
operating within its constraints in certain respects, then improving on those
particular problems. You should always conduct this analysis before trying to
solve your problems. I generally recommend conducting this analysis in advance,
so that you can predict performance issues before they occur, and plan for them
accordingly. For example, if you know that your disk utilization grows by 2 GiB
per day, and you’re on a 500 GiB hard drive, you’ve got about 8 months to plan
your next upgrade, and you shouldn’t be surprised by an ENOSPC when the time
comes.

For CPU bound tasks, this is also where a general understanding of the
performance characteristics of various data structures and algorithms is useful.
When you know you’re working on something which  *will become*  the application’s
bottleneck, you would be wise to consider algorithms which can be implemented
efficiently. However, it’s equally important to re-prioritize performance when
you’re not working on your bottlenecks, and instead consider factors like
simplicity and conciseness more seriously.

Much of this will probably seem obvious to many readers. Even so, I think the
general wisdom described here is institutional, so it’s worth writing down. I
also want to call out some specific behaviors that I see in software today which
I think don’t take this well enough into account.

I opened by stating that I believe that you cannot effectively optimize a system
which you do not understand. There are two groups of people I want to speak to
with this in mind: library authors (especially the standard library), and
application programmers. There are some feelings among library authors that
libraries should be fairly opaque, and present high-level abstractions over
their particular choices of algorithms, data structures, and so on. I think this
represents a fundamental lack of trust with the programmer downstream. Rather
than write idiot-proof abstractions, I think it’s better to trust the downstream
programmer, explain to them how your system works, and equip them with the tools
to audit their own applications. After all: your library is only a small
component of  *their*  system, not yours — and you cannot optimize a system
you don’t understand.

And to the application programmer, I urge you to meet your dependencies in the
middle. Your entire system is your responsibility, including your dependencies.
When the bottleneck lies in someone else’s code, you should be prepared to dig
into their code, patch it, and send a fix upstream, or to restructure your code
to route the bottleneck out. Strive to understand how your dependencies, up to
and including the stdlib, compiler, runtime, kernel, and so on, will perform in
your scenario. And again to the standard library programmer: help them out by
making your abstractions thin, and your implementations simple and debuggable.
