---
title: "Aggregation And Composition"
description: "Few things in the UML cause more consternation than aggregation and composition, in particular how they vary from regular association."
date: 2003-05-17T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/AggregationAndComposition.html
slug: AggregationAndComposition
word_count: 216
---


Few things in the UML cause more consternation than aggregation and
composition, in particular how they vary from regular association.


The full story is muddied by history. In the pre-UML methods there was
a common notion of defining some form of part-whole relationships. The
trouble was that each method defined different semantics for these
relationships (although to be fair, some of these were pretty semantics
free).


So when the time came to standardize, lots of people wanted part-whole
relationships, but they couldn't agree on what they meant. So the UML
definers introduced two relationships.


**aggregation** (*white diamond*) has no semantics beyond that of
		a regular association. It is, as Jim Rumbaugh puts it,
		a modeling placebo. People can, and do, use it - but
		there are no standard meanings for it. So if you see
		it, you should inquire as to what the author means by
		it. I would advise not using it yourself without some
		form of explanation.


**composition** (*black diamond*) does carry semantics. The most
		particular is that an object can only be the part of
		one composition relationship. So even if both windows
		and panels can hold menu-bars, any instance of menu-bar
		must be only held by one whole. This isn't a
		constraint that you can easily express with the
		regular multiplicity markers.
