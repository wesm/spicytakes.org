---
title: "Refactoring Cringely"
description: "A recentpiece by Robert Cringelycaused a small stir in the refactoring community recently, as he criticized refactoring. Phlip summed the response on therefactoring mailing listwith an unusually restr"
date: 2003-06-03T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/RefactoringCringely.html
slug: RefactoringCringely
word_count: 486
---


A recent [piece by
Robert Cringely](http://www.pbs.org/cringely/pulpit/pulpit20030508.html) caused a small stir in the refactoring community
recently, as he criticized refactoring. Phlip summed the response on
the [refactoring
mailing list](http://groups.yahoo.com/group/refactoring) with an unusually restrained '...he sounds like a
âskepticâ who writes reviews of books he has no intention of
reading.'


Certainly it isn't clear how much Cringely understands about
	refactoring, although he certainly understands the key point about
	it being a behavior preserving transformation process. What he does
	do is highlight a number of ways where refactoring is used inappropriately.


One misuse is that of refactoring code that won't change.The
		whole point of refactoring is that it improves the design of
		existing code. The value of well designed code is that it is
		easier to change. Hence you refactor code that you expect to
		change in the future. There's no point refactoring code that's stable.


Another is his example of a refactoring team that goes into the
		code of other teams and refactors it. This is the kind of
		'service' that I would pay to avoid. Programmers should refactor
		their own code only, not go banging around in other stuff. XP
		teams use collective code ownership, which encourages anyone to
		refactor any code in the team's code base, but this applies only
		to that team's code. The idea of one team wandering around
		refactoring other teams' code without telling anyone is certainly
		not something that I would recommend.


Finally he complains about refactoring being used to cover any
		form of code changes. As with the others, I agree with him
		100%. It's long been one of my pet peeves that people use
		refactoring as a synonym for restructuring something. Refactoring
		is a very particular process that uses a series of small
		semantics-preserving transformations to change a code base. It's
		quite a particular and disciplined process. There are other ways
		to restructure code, beneficial or not these are not
		refactoring.


So on the whole it sounds like I agree with a lot of what
	Cringely says. That's true, and it's true of the comments on the
	mailing list. On the whole the annoyance was about a feeling that
	Cringely mischaracterised refactoring in an eagerness to point the
	finger at fads.


Where I certainly do part company with Cringely is his opinion
that 80% of refactoring is a waste of time and software managers
should put a stop to refactoring to save money. The point of
refactoring is that improving the design makes it easier to change
things, therefore refactoring increases productivity. Certainly
programmers need to judge whether the refactoring effort will pay off,
and that's not something you can easily quantify. But time after time
I've seen people waste time working their way around poorly designed
code with patches that only make it worse. Refactoring is a way to get
out of that particular death spiral - which is why I consider it to be
such a valuable technique.
