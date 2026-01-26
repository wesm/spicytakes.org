---
title: "Is Fixing An Unknown Bug Refactoring"
description: "Here's an interesting conundrum posed by Przemyslaw Pokrywka. One 		of the refactorings in thebookisIntroduce Null Object- a very 		useful refactoring (also discussed inJosh's new 		book.) Przemyslaw'"
date: 2004-09-03T00:00:00
tags: ["refactoring boundary"]
url: https://martinfowler.com/bliki/IsFixingAnUnknownBugRefactoring.html
slug: IsFixingAnUnknownBugRefactoring
word_count: 377
---


Here's an interesting conundrum posed by Przemyslaw Pokrywka. One
		of the refactorings in the [book](https://martinfowler.com/books/refactoring.html)
			is [Introduce Null Object](http://www.refactoring.com/catalog/introduceNullObject.html) - a very
		useful refactoring (also discussed in [Josh's new
		book](https://martinfowler.com/books/r2p.html).) Przemyslaw's point is that this refactoring can alter
		behavior. If you have a method return a null, and you invoke a
		method on that null you'll get a null pointer exception. If you use a
		Null Object you'll get some default behavior.


Now many refactorings do alter behavior, indeed they are intended
	to. If you apply [Form Template Method](http://www.refactoring.com/catalog/formTemplateMethod.html), then the program works
	differently. The key question is whether this is what in my
		[DefinitionOfRefactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) I called *observable*
		behavior. That is does it change what the program essentially
		does? With Introduce Null Object you have to look around the
		program for places that manipulate returned references,
		typically by checking to see if it's null. This is what makes this
		a rather tricky refactoring.


The interesting part of the conundrum is what happens if you miss
	an area where there's a bug. Somewhere in your program you invoke a
	method on a null reference. Before the refactoring you'd get an
	exception, we'll assume here it's one that you don't know about and
	goes all the way up to some top level handler. After the refactoring
	you get the default behavior - which may in fact fix the bug. If you
	fix a bug you don't know about is this still a refactoring?


I'd argue yes, since you didn't know or care (enough) about the
	buggy behavior then I'd say that behavior wasn't
	observable. Even if you knew about the bug, I'd still argue that
	it's okay to call this a refactoring if the bug wasn't behavior
	you cared about preserving.


This is an interesting case, and I could easily imagine myself
	changing my mind or exploring more edge cases.


One of the interesting things it points out is the difference
	between manual and tool driven refactoring. With manual refactoring
	you can make judgement calls like this, tools often have to be much
	more careful. Yet even tools can't always guarantee to preserve
	behavior - even a rename method can be break on refactoring if that
	method is called by reflection with a name that's read from a file.
