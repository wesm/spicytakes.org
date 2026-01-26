---
title: "Refactoring Boundary"
description: "There was some recent discussion on therefactoring mailing listabout what is or isn't a refactoring. As with these discussions, 	there's always a danger of debating how many angels fit on a pin, 	but "
date: 2004-09-01T00:00:00
tags: ["refactoring boundary"]
url: https://martinfowler.com/bliki/RefactoringBoundary.html
slug: RefactoringBoundary
word_count: 221
---


There was some recent discussion on the [refactoring mailing list](http://groups.yahoo.com/group/refactoring)
	about what is or isn't a refactoring. As with these discussions,
	there's always a danger of debating how many angels fit on a pin,
	but thinking about the boundaries does have some useful purpose.


The [DefinitionOfRefactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html) in my book was intentionally
	informal. The informality rests on a couple of phrases that are
	distinctly open to interpretation:

- *without changing its observable behavior:* which begs
		the question what is observable behavior? Essentially it means
		that the software still does what it did before - but
		there's lots of ways you could interpret that.
- *to make it easier to understand and cheaper to modify:*
		this gets at the purpose of refactoring. There are many changes we
		can make to our programs, but in my view refactoring is all about
		making it easier to understand and change. The same changes made
		with a different purpose aren't refactoring as I see it.


The essence of refactoring is that of the sequence of small
	behavior-preserving changes. Despite the fact that refactoring isn't
	something that can be formally defined, it's still a pretty precise
		terms - and I do want to avoid
		[RefactoringMalapropism](https://martinfowler.com/bliki/RefactoringMalapropism.html). But I think it's worth thinking
		about some of these cases, which I'm putting in different bliki
		entries: [IsChangingInterfacesRefactoring](https://martinfowler.com/bliki/IsChangingInterfacesRefactoring.html), [IsFixingAnUnknownBugRefactoring](https://martinfowler.com/bliki/IsFixingAnUnknownBugRefactoring.html),
		[IsOptimizationRefactoring](https://martinfowler.com/bliki/IsOptimizationRefactoring.html), and [IsDeclarationOrderingRefactoring](https://martinfowler.com/bliki/IsDeclarationOrderingRefactoring.html).
