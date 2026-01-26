---
title: "Command Query Separation"
description: "The term 'command query separation' was coined by Bertrand Meyer 	in his book âObject Oriented Software Constructionâ - a book that is 	one of the most influential OO books during the early days o"
date: 2005-12-05T00:00:00
tags: ["api design", "programming style"]
url: https://martinfowler.com/bliki/CommandQuerySeparation.html
slug: CommandQuerySeparation
word_count: 428
---


The term 'command query separation' was coined by Bertrand Meyer
	in his book â[Object Oriented Software Construction](https://www.amazon.com/gp/product/0136291554/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0136291554&linkCode=as2&tag=martinfowlerc-20)â - a book that is
	one of the most influential OO books during the early days of
	OO. (The first edition is the one that had the influence, the second
	edition is good but you'll need several months in a gym before you
	can lift it.)


The fundamental idea is that we should divide an object's methods
	into two sharply separated categories:

- **Queries**: Return a result and do not change the
		observable state of the
		system (are free of side effects).
- **Commands**: Change the state of a system but do not
return a value.


Because the term 'command' is widely used in other contexts I
	prefer to refer to them as **'modifiers'**, you also see the term
	'mutators'.


The really valuable idea in this principle is that it's extremely
	handy if you can clearly separate methods that change state from
	those that don't. This is because you can use queries in many
	situations with much more confidence, introducing them anywhere,
	changing their order. You have to be more careful with modifiers.


The notion in the principle is that the return type is the
give-away for the difference. It's a good convention because most of
the time it works well. Consider the java idiom for iterating through
a collection: the `next` method both gives the next item in
the collection and advances the iterator. Personally I'd much prefer a
style that has separate `advance` and `current`
methods.


Meyer likes to use command-query separation absolutely, but there
	are exceptions. Popping a stack is a good example of a query that
	modifies state. Meyer correctly says that you can avoid having this
	method, but it is a useful idiom. So I prefer to follow this
	principle when I can, but I'm prepared to break it to get my pop.


It would be nice if the language itself would support this
	notion. I could imagine a language that would detect state changing
	methods, or at least allow the programmer to mark them. One reason
	that languages can't detect them automatically is that the rule
	about not changing state really only applies to the [ObservableState](https://martinfowler.com/bliki/ObservableState.html)
	of the system. Using programmer markings seems more reasonable but
	is rare. The only case I've really come across it is the const
	modifier in C++. Since I haven't used C++ for many years it's hard
	for me to assess how useful it is in practice. My sense is that good
	C++ers use const a lot and like it.
