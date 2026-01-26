---
title: "Abundant Mutation"
description: "Any reader of my writings will know that I'm a big proponent ofevolutionary  design. Despite my enthusiasm for this approach, no technique is perfect and I'm just as happy to report its problems as I "
date: 2005-02-14T00:00:00
tags: ["evolutionary design", "technical leadership"]
url: https://martinfowler.com/bliki/AbundantMutation.html
slug: AbundantMutation
word_count: 503
---


Any reader of my writings will know that I'm a big proponent of
[evolutionary

design](https://martinfowler.com/articles/designDead.html#PlannedAndEvolutionaryDesign). Despite my enthusiasm for this approach, no technique is
perfect and I'm just as happy to report its problems as I am its
successes.


I've come across this problem, although in somewhat different
manifestations, in two projects so far.


Evolutionary Design expects the team to modify the design as the
project proceeds; both to cope with requirements changes and to take
advantage of learning. You can think of this as adding mutations to
the design that react to these changes. This mutation is a good and
necessary thing, but like many good things you can get too much of
it.


The first project was a large project, with around a hundred
developers. In this case the over-mutation occurred because different
sub-teams would tackle a common problem in a different way. This might
be by building different frameworks or by incorporating different
external frameworks.


The second project was a moderate project of a dozen developers,
but with a significant amount of rotation. As newcomers came in they
would look at a previous way of tackling a problem, not understand it
or find it deficient and go in a new direction. The trouble is things
wouldn't complete before new people came in who found this half done
solution had deficiencies... you get the picture.


In both cases the net result was multiple ways of trying to solve
the same problem. Not just was the duplication of effort wasteful, it
also made the software more complex than it needed to be.


I should stress that the overall design health was still pretty
good, compared to other systems in the same organizations. In
particular, the attention to automated testing allowed evolution to be
much safer than the norm and both projects had significantly low
defect rates.


At the risk of abusing [MetaphoricQuestioning](https://martinfowler.com/bliki/MetaphoricQuestioning.html), you
might think of this as a case where the environment hadn't killed off
the weaker mutations. Ideally when a competing design appears it
either dies quickly or kills off the existing design. The problem
here is that neither happened. So the question becomes: how can you
force inferior designs out of the system?


In both cases those I spoke to felt that there was  a lack of
overall design leadership. In the large project this was added through
an architecture team that forged a base approach to these problems and
then kept a close communication about what was being done. The second
team hasn't tackled this issue so far, but it's seen as a need for
some more stable design leadership. So rather than an evolutionary metaphor, you might think of it
	more like a breeder encouraging good traits and discouraging poor
	ones. (This was an inspiration for Darwin.)


Metaphors aside, I think it fundamentally comes down to following the [principle](http://agileManifesto.org) âContinuous attention
to technical excellence and good design enhances agility.â
Evolutionary design requires attention, skill, and leadership. It's
just a [different

sort of leadership](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf) than many commonly think.
