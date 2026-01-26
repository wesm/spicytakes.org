---
title: "Don’t start with a monolith"
description: "In the last few months, I’ve heard repeatedly that the only way to get to a successful microservices architecture is by starting with a monolith first. To paraphrase Simon Brown: If you can’t build a "
date: 2015-06-09T00:00:00
tags: ["microservices"]
url: https://martinfowler.com/articles/dont-start-monolith.html
slug: dont-start-monolith
word_count: 1150
---


In the last few months, I’ve heard repeatedly that the only way to
get to a successful microservices architecture is by starting with a
monolith first. [To
paraphrase Simon Brown](http://www.codingthearchitecture.com/2014/07/06/distributed_big_balls_of_mud.html): If you can’t build a well-structured
monolith, what makes you think you can build a well-structured set of
microservices? The most recent – and, as usual, very convincing –
rendering of this argument comes from [Martin Fowler](https://martinfowler.com/bliki/MonolithFirst.html) on this very site. As I had
a chance to comment on an earlier draft, I had some time to think
about this. And I did, especially because I usually find myself in
agreement with him, and some others whose views I typically share
seemed to agree with him, too.


I’m firmly convinced that starting with a monolith is usually exactly the
wrong thing to do.


Starting to build a new system is exactly the time when you should
be thinking about carving it up into pieces. I strongly disagree with
the idea that you can postpone this, as expressed by Sam Newman, again
someone I agree with 95% of the time:


> I remain convinced that it is much easier to partition an existing,
>   âbrownfieldâ system than to do so up front with a new, greenfield
>   system. You have more to work with. You have code you can examine,
>   you can speak to people who use and maintain the system. You also
>   know what 'good' looks like - you have a working system to change,
>   making it easier for you to know when you may have got something
>   wrong or been too aggressive in your decision making process.
> -- [Sam Newman](http://samnewman.io/blog/2015/04/07/microservices-for-greenfield)


In the majority of cases, it will be awfully hard, if not outright
impossible, to cut up an existing monolith this way. (That doesn’t
mean it’s always impossible, but that’s a topic for a future post.)
There is some common ground in that I agree you should know the domain
you’re building a system for very well before trying to partition
it, though: In my view, the ideal scenario is one where you’re building a
*second version* of an existing system.


If you are actually able to build a well-structured monolith, you
probably don’t need microservices in the first place. Which is OK! I
definitely agree with [Martin](https://martinfowler.com/bliki/MicroservicePremium.html): You shouldn’t introduce the
complexity of additional distribution into your system if you don’t
have a very good reason for doing so.


(So what would be a good reason? There are many, but to me the most
important one is to allow for fast, independent delivery of individual parts within a larger
system. Microservices’ main benefit, in my view, is enabling parallel
development by establishing a hard-to-cross boundary between different
parts of your system. By doing this, you make it hard – or at least
harder – to do the wrong thing: Namely, connecting parts that shouldn’t
be connected, and coupling those that need to be connected too
tightly. In theory, you don’t need microservices for this if you
simply have the discipline to follow clear rules and establish clear
boundaries within your monolithic application; in practice, I’ve found
this to be the case only very rarely.)


![](dont-start-monolith/monolith-theory-practice.svg)


You might be tempted to assume there are a number of nicely
  separated microservices hiding in your monolith, just waiting to be
  extracted. In reality, though, it’s extremely hard to avoid creating
  lots of connections, planned and unplanned. In fact the whole point
  of the microservices approach is to make it hard to create something
  like this.


But if you start with a monolith, the parts will become extremely
tightly coupled to each other. *That’s the very definition of a
monolith*. The parts will rely on features of the platform they all
use. They’ll communicate based on abstractions that are shared because
they all use the same libraries. They’ll communicate using means that
are only available when they are hosted in the same process. And these
are only the technical aspects! Far worse than that, the parts will
(almost) freely share domain objects, rely on the same, shared
persistence model, assume database transactions are readily available
so that there’s no need for compensation … Even the very fact that
it’s easy to refactor things and move them around – all in the
convenience of your IDE’s view of a single project – is what makes it
extremely hard to cut things apart again. It’s *extremely* hard to
split up an existing monolith into separate pieces.


I strongly believe – and experience from a number of our recent projects
confirms this – that when you start out, you should think about
the subsystems you build, *and build them as independently of each
other as possible*. Of course you should only do this if you believe
your system is large enough to warrant this. If it’s just you and one
of your co-workers building something over the course of a few weeks,
it’s entirely possible that you don’t.


But starting with an approach where you carve up your system into
smaller parts, and treat each of them as a clearly separated, individual
system with its own development, deployment, and delivery cycle, and (the
possibility of) its own internal architecture, is a very powerful
concept that can help you to deliver a system in the first place.


So is there any actual experience to back this up? Yes, there are a few systems we’ve been
involved with recently that showed this concept to work – provided you
tolerate the fact that what I’m talking about is more likely bigger
than your typical microservice. The most prominent
one is Otto.de, about which I did
[a talk together with their tech lead](http://www.infoq.com/presentations/modular-ecommerce-website)
 (and which you can read about in
 [this nice write-up by one of their lead architects](http://dev.otto.de/2015/09/30/on-monoliths-and-microservices/)).
 But there are quite a few others as well, and I remain convinced it’s
 a good idea to start building a system using this approach –
 given you know the domain you’re building for really, really well.


But there is another lesson to be learned from this discussion, in my
view – and it’s a more general one: Beware of architectural recipes
that are too simple and too obvious. This one – start by carving up
your domain into separate, independent parts – is no
exception. Sometimes a monolith *is* preferable, sometime it’s
not. If you decide to build things using a microservices approach, you
need to be aware that while it will be a lot easier to make localized
decisions in each individual part, it will be much harder to change
the very boundaries that enable this. Refactoring in the small becomes
easier, refactoring in the large becomes much harder.


As is always the case with architecture discussions, there is no way
to get around the fact that you need to make that decision on your
own, in each and every individual case.


---
