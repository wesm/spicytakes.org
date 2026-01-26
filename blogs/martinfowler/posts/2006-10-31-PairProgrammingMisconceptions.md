---
title: "Pair Programming Misconceptions"
description: "A bunch of common misconceptions aboutPair Programming."
date: 2006-10-31T00:00:00
tags: ["agile", "productivity", "team organization", "extreme programming", "collaboration"]
url: https://martinfowler.com/bliki/PairProgrammingMisconceptions.html
slug: PairProgrammingMisconceptions
word_count: 617
---


A bunch of common misconceptions about [Pair Programming](https://martinfowler.com/bliki/PairProgramming.html).


**You have to do pair programming if you're doing an agile
	process.**


This is utterly false. 'Agile' is a very broad term defined
	 only in terms of values and principles, most notably in the
	[Manifesto for Agile Software Development](http://agilemanifesto.org/). The manifesto doesn't
	mention pair programming and most agile methods don't make it part
	of their approach.


Since pair programming is a practice of XP it's had a lot of
	influence in the agile community. As a result it's often mentioned
	as an agile practice - meaning a practice that's commonly used by
	people on agile projects. But that's an observation not a prescription.


**Extreme Programming forces you to do Pair-Programming**


This is much more nuanced issue. Pair-Programming is one of the
	practices of XP and has been since its inception. The nuance here is
	whether XP practices are mandatory for a team that claims to be
	doing XP. This is actually a much more tricky question than it may
	seem at first sight. XP, like any agile method, expects a team to
	choose its own process. In Extreme Programming Explained Kent says
	that practices are âthe kind of things you'll see XP teams doing day
-to-dayâ. I would say that pair-programming is usual for XP teams. I
wouldn't say that a team that doesn't do pair-programming thus cannot
call itself an XP team. I should also point out that to most XPers I
know the question of whether a team is XP or not is uninteresting; the
real issue is whether a team is effective.


The closest I'd get to forcing pair programming would be to say
	that if you want to learn how to do XP you should try
	pair-programming and see if it works for you.


**I don't need to try pairing because I know I won't like
	it.**


The problem with this statement is that many people have been
	surprised by pair programming. They gave it a try, expecting to hate
	it, and found they really liked it.


This is further complicated by many people trying out pairing
	badly - which can give a false impression. Hours passively staring over
	someone's shoulder in a corner cube isn't pair programming. Make
	sure you have someone who really knows how coach you, so you
can be sure you're evaluating the real thing.


**Pair-Programming halves the productivity of 
	developers.**


My flippant answer to this one is: âthat would be true if the
	hardest part of programming was typingâ.


Advocates of pair-programming are advocates because they believe
	that a pair is actually more productive that two separate
	developers. This is due to the continuous discussion and review that
	pairing introduces. You come up with better designs, make less
	mistakes, and make more people familiar with the code. All of these
	things offset having less people typing.


Of course, since we [CannotMeasureProductivity](https://martinfowler.com/bliki/CannotMeasureProductivity.html) we can't
know for sure. My view is that you should try it and the team should
reflect on whether they feel they are more effective with pairing that
without. As with any new practice make sure you allow enough time so
you have a good chance of crossing the
[ImprovementRavine](https://martinfowler.com/bliki/ImprovementRavine.html).


**It's only worth pairing on complex code, rote code yields no
	advantage.**


I think there is a point to this - pairing is about improving
	design and minimizing mistakes. Rote code that's simple to write
	yields little opportunities for pairing to make a difference.


Except this: writing boring rote code is a smell. If I'm writing
	boring repetitive code it's usually a sign that I've missed an
	important abstraction, one that will drastically reduce the amount
	of rote code to write. Pairing will help you find that abstraction.
