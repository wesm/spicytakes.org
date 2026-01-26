---
title: "Refactoring Malapropism"
description: "Once a term known to only a few, âRefactoringâ is now commonly tossed 	around the computer industry. I like to think that I'm partly 	responsible for this and hope it's improved some programmers l"
date: 2004-01-03T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/RefactoringMalapropism.html
slug: RefactoringMalapropism
word_count: 247
---


Once a term known to only a few, âRefactoringâ is now commonly tossed
	around the computer industry. I like to think that I'm partly
	responsible for this and hope it's improved some programmers lives
	and some business's bottom lines. (Important point, I'm not the
	father or the inventor of refactoring - just a documenter.)


However the term ârefactoringâ is often used when it's not appropriate. If
	somebody talks about a system being broken for a couple of days
	while they are refactoring, you can be pretty sure they are not
	refactoring. If someone talks about refactoring a document, then
	that's not refactoring. Both of these are restructuring.


I see refactoring as a very specific technique to do the more
	general activity of restructuring. Restructuring is any
	rearrangement of parts of a whole. It's a very general term that
	doesn't imply any particular way of doing the restructuring.


Refactoring is a very specific technique, founded on using small
	behavior-preserving transformations (themselves called
	refactorings). If you are doing refactoring your system should not
	be broken for more than a few minutes at a time, and I don't see how
	you do it on something that doesn't have a well defined behavior.


I realize I may be fighting a losing game here, but I do want to
	preserve the precision of the
	[DefinitionOfRefactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html). There may be other
	good techniques for restructuring, but they are different. I'd like
	us to be clear about what we mean when we use this word.
