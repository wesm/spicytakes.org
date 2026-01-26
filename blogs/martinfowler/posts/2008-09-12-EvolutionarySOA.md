---
title: "Evolutionary S O A"
description: "Can SOA be done with an agile approach?"
date: 2008-09-12T00:00:00
tags: ["application integration", "evolutionary design"]
url: https://martinfowler.com/bliki/EvolutionarySOA.html
slug: EvolutionarySOA
word_count: 727
---


**Can SOA be done with an agile approach?**


I don't delve too much into the cluttered world of SOA
  ([ServiceOrientedAmbiguity](https://martinfowler.com/bliki/ServiceOrientedAmbiguity.html)), but I get this question often
  enough (in some form or other) to be worth a pontification.


When I first came across agile software development (in the form
  of Extreme Programming) the most troubling aspect for me was its
  approach to software design. Like many I'd become used to the notion
  that software should be designed before it was programmed, while XP
  seemed to encourage an almost wilful embracing of design
  ignorance. In 2000 I was asked to give the closing keynote at the [first Agile/XP
  conference](https://martinfowler.com/articles/xp2000.html), and in order to gather my thoughts I ended up writing [Is
  Design Dead?](https://martinfowler.com/articles/designDead.html) - an essay that examined the fate of design in an agile
  world.


I'm still quite proud of that essay and I think it's well
  worth reading today - but for this bliki entry I'll summarize. I
  talked about two driving approaches to software design: planned and
  evolutionary. Planned design works out the design of software in one
  phase and builds (programs) it afterwards. In this case changing the
  design is hard once you've begun construction. Evolutionary design
  assumes regular change of the design even once you've done
  significant programming. I concluded that the practices of XP
  provided a disciplined approach to evolutionary design, thus making
  it much more practical than people had realized. This change did not
  remove software design (it is not dead) but did significantly change
  how we think about design.


The argument for planned design in an SOA context is that we are
  building webs of interconnected, loosely coupled systems. In this
  situation each system is making its services available as a
  [PublishedInterface](https://martinfowler.com/bliki/PublishedInterface.html) to the whole enterprise. Published
  interfaces are hard to change, therefore you need planned design to
  get them right so you don't have to change them. Planned design is
  also a reaction to the chaotic system interconnections that people
  see in most organizations. This chaos is the result of poor design,
  so the feeling is that better planned design will prevent this
  happening in future.


Evolutionary design is an essential aspect of agile methods. One
  of the key foundations of agile methods is [the
  desire to handle, indeed welcome, change](https://martinfowler.com/articles/newMethodology.html#PredictiveVersusAdaptive). Planned design assumes
  change is hard, and thus tries to predict where it occurs. If
  changes occur within the predicted boundaries then it's easy, but if
  it falls outside those boundaries you're out of luck. Agile thinking
  assumes unpredictable change is inevitable and tries to enable it in
  a controlled way.


So as I look at SOA, or any other design context, the fundamental
  question I ask is âis change predictable?â Only if change is
  predictable is a planned design approach valid. My sense is that if
  predictability is hard within the context of a single application,
  it's doubly hard across an enterprise. If we use planned design in a
  unpredictable context we find that however good the plans are, they
  will be undermined by the unpredictable changes, leading to the same
  mess we are currently in. Usually, however, the mess is worse
  because a there is significant sunk cost in a planned design, this
  can easily reduce the business value that an SOA effort is intended
  to produce, particularly if time-to-market is important.


As a result I think we have to bite the bullet and figure out how
  to do evolutionary design in this loosely connected context. After
  all the whole of point of loose coupling is to make change
  easier. At the center of this is thinking about contracts in terms
  of change, with such ideas as [Consumer
  Driven Contracts](https://martinfowler.com/articles/consumerDrivenContracts.html).


This direction leads to things like Jim Webber's notion of
  [Guerilla
  SOA](http://www.infoq.com/interviews/jim-webber-qcon-london). This builds up SOA using small steps directed by producing
  business value. Since producing business value is the whole point,
  this offers a path to producing a much better return on
  investment. It's certainly an approach our clients appreciate.


Can evolutionary design scale to SOA sizes? In my view we have an
  existence proof at a much larger scale than even a big SOA effort -
  the web itself. The web is built on very loose coupling and lots of
  unpredictable changes. It is, in many ways, a mess - but it's a mess
  that works, delivering real value to lots of people every day.
