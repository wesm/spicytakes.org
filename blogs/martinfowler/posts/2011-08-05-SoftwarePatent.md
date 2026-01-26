---
title: "Software Patent"
description: "I think almost everyone I know in the software development field   has a deep hatred for patents and the way they've been used in our   field. I've had a post on my todo list for ages about this and h"
date: 2011-08-05T00:00:00
tags: ["internet culture", "legal"]
url: https://martinfowler.com/bliki/SoftwarePatent.html
slug: SoftwarePatent
word_count: 1457
---


I think almost everyone I know in the software development field
  has a deep hatred for patents and the way they've been used in our
  field. I've had a post on my todo list for ages about this and have
  finally been moved to write about it after a [particularly
  good piece of investigative journalism](http://www.thisamericanlife.org/radio-archives/episode/441/when-patents-attack) by This American Life.
  The short form of my post is that while patents (even software
  patents) are a good idea in principle, in practice they have turned
  into an unmitigated disaster and would be better scrapped.


To begin, however, I'll say why patents are a good idea in
  principle, indeed they may be one of the most valuable 'inventions'
  in human history.


A good argument for patents playing such a central case in human
  development is made by William Rosen in his book [The Most Powerful
  Idea in the World](https://www.amazon.com/gp/product/1400067057/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1400067057&linkCode=as2&tag=martinfowlerc-20). Rosen's book looks at the Industrial
  Revolution which he characterizes as one of the most important
  events in human history, one that made a step change in human
  wealth.


> A skilled laborer—a weaver, perhaps, or a blacksmith—in
>     seventeenth-century England, France, or China spent roughly the
>     same number of hours a week at his trade, producing about the same
>     number of bolts of cloth, or nails, as his ten-times
>     great-grandfather did during the time of Augustus. He earned the
>     same number of coins and bought the same amount, and variety, of
>     food. His wife, like her ten-times great-grandmother, prepared the
>     food; she might have bought her bread from a village baker, but
>     she made pretty much everything herself. She even made her
>     family’s clothing, which, allowing for the vagaries of weather and
>     fashion, was largely indistinguishable from those of any family
>     for the preceding ten centuries: homespun wool, with some linen if
>     flax were locally available. The laborer and his wife would have
>     perhaps eight or ten live offspring, with a reasonable chance that
>     three might survive to adulthood. If the laborer chose to travel,
>     he would do it on foot or, if he were exceptionally prosperous, by
>     horse-drawn cart or coach, traveling three miles an hour if the
>     former, or seven if the latter—again, the same as his
>     ancestor—which meant that his world was not much larger than the
>     five or six miles surrounding the place he was born.
> And then, for the first time in history, things changed. And
>     they changed at the most basic of levels. A skilled fourth-century
>     weaver in the of Constantinople might earn enough by working three
>     hours to purchase a pound of bread; by 1800, it would cost a
>     weaver working in Nottingham at least two. But by 1900, it took
>     less than fifteen minutes to earn enough to buy the loaf; and by
>     2000, five minutes. It is a cliché, but nonetheless true, to
>     recognize that a middle-class family living in a developed
>     twenty-first-century country enjoys a life filled with luxuries
>     that a king could barely afford two centuries ago.
> -- William Rosen


The change wrought by the Industrial Revolution is almost
 unimaginable. We think our current era is one of constant change, but
 that phrasing captures what we forget. These days we are used to
 change, but before the Industrial Revolution human life changed very
 slowly. The biggest change the Industrial Revolution unleashed was
 change itself.


Thus I think few students of human history doubt the vital
 importance of the Industrial Revolution, but this raises a couple of
 important questions - why did it occur when and where it did? What
 was so special about late 18th century England that set this steam
 train off? Rosen's view is that patents are the key enabler, because
 they provided a financial incentive and platform to support inventors
 and entrepreneurs. Without patents only wealthy people (or those with
 wealthy patrons) could afford to innovate, and there was little
 incentive for them to do so.


I find Rosen's argument  persuasive and thus think that
 patents were not just a Good Thing but one of the Best Things to have
 happened to our species. So why do I loathe software patents so much?


It boils down to the fact that patents generally have become very
 debased from the animal that enabled the Industrial Revolution. The
 primary debasement is that of novelty. The whole point of
 patents is to grant a (limited-term) monopoly to something that is
 new. The [US
 patent law](http://www.uspto.gov/web/offices/pac/mpep/consolidated_laws.pdf) says you can't have a patent if âthe subject matter as
 a whole would have been obvious at the time the invention was made to
 a person having ordinary skill in the art to which said subject
 matter pertains.â This boils back to the English 1623  Statute on
 Monopolies1 which
 started the notion that a patentable invention is something that is
 both novel and useful.


1: 
     I rather like its original name: âAct concerning Monopolies and
     Dispensations with penall Lawes and the Forfeyture thereofâ


The core problem with software patents is that this key principle
 has been tossed aside. Everyone in the software field has seen a
 parade of patents which do nothing but try to claim rights on
 techniques that have already been in use for years, let alone 
 developments that while new, are are still obvious to those of us with ordinary
 skills in programming.


Although this debasement is quite enough to ruin the integrity of
 software patents, there are some other debasements worth mentioning
 too. Patents were originally created with a limited time in mind -
 the 1623 law placed them at fourteen years. This, of course, at a
 period of time when change was much slower than it is now, let alone
 than it is in our field. Proper software patents should hold for a
 shorter period than that. Further debasement occurs in lack of
 specificity - most software patents are ridiculously broad and vague,
 while patents were originally seen as narrow and specific. Narrow
 patents encourage innovation by incenting people to think of
 different ways to solve the same problem, broad patents
 snuff that innovation out.


The result of all this debasement is a world where patents no
 longer incentivize and communicate new inventions, but where they are
 weapons to be used to fight legal battles. For large companies they
 are, at least on the surface, an annoying distraction and cost. But
 the real damage they do is to small outfits, that can't afford the
 time and money to fight a patent lawsuit. Thus we see patents used for
 shakedowns - stifling innovation.


The tragedy is that patents have become a source of reinforcing
 existing powers. A big company may find patents a significant
 inconvenience, but in the end patents are good for perpetuating the
 current power-holders because they can snuff out the smaller ones. This is why
 it's hard to change the system, those with the power have no
 incentive to give it up.


I find it particularly depressing that my fellow programmers are
 complicit in this tragedy. It's not uncommon for programmers to talk
 about patents they've been involved in getting and how they know how
 absurd they are. I know it's easy to get on a high horse here, but I
 do think that any programmer who cooperates in getting a baseless
 patent should be ashamed of themselves. It shows the kind of lack of
 responsibility that undermines any justification we have to be
 treated as professionals.


In theory, I'm not against software patents if we were able to get
 back to the core beneficial principles of patents and apply them
 properly. This would imply developing a process that would ensure
 that patents were only granted for truly novel ideas. But unless such
 a process were properly put together, I'd rather see software patents
 eliminated completely. A world without software patents would be
 better than the mess we're currently in.


## Further Reading


There's a huge amount of material that's been written about
   patents out there. Tim Bray's piece last year on [giving
   up on patents](http://www.tbray.org/ongoing/When/201x/2010/02/22/Patent-Fail) links to a number of good sources. A couple of
   these point to evidence that software patents have reduced innovation.


Planet Money did [a follow up podcast](http://www.npr.org/blogs/money/2011/08/04/138934689/the-tuesday-podcast-the-patent-war) to the one on This American
   Life, with links to the studies they summarize.


âAt a time when our future affluence depends so heavily on
   innovation, we have drifted toward a patent regime that not only
   fails to fulfil its justifying function, to incentivise innovation,
   but actively impedes innovation.â - [W.W. of The Economist](http://www.economist.com/blogs/democracyinamerica/2011/08/intellectual-property)


## Notes


1: 
     I rather like its original name: âAct concerning Monopolies and
     Dispensations with penall Lawes and the Forfeyture thereofâ
