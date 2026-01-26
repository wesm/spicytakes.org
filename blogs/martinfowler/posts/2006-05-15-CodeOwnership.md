---
title: "Code Ownership"
description: "In my recentCodeOwnershippost, I described the way in which I 	think about code ownership issues. Many of my software development 	friends are extreme programmers, and tend to favor collective code 	o"
date: 2006-05-15T00:00:00
tags: ["team organization", "extreme programming", "process theory"]
url: https://martinfowler.com/bliki/CodeOwnership.html
slug: CodeOwnership
word_count: 482
---


There are various schemes of Code Ownership that I've come
	across. I put them into three broad categories:

- **Strong code ownership** breaks a code base up into modules
		(classes, functions, files) and assigns each module to one
		developer. Developers are only allowed to make changes to modules
		they own. If they need a change made to someone else's module they
		need to talk to the module owner and get them to make the
		change. You can accelerate this process by writing a patch for the
		other module and sending that to the module owner.
- **Weak code ownership** is similar in that modules are assigned to
		owners, but different in that developers are allowed to change
		modules owned by other people. Module owners are expected to take
		responsibility for the modules they own and keep an eye on changes
		made by other people. If you want to make a substantial change to
		someone else's module it's polite to talk it over with the module
		owner first.
- **Collective code ownership** abandons any notion of individual
		ownership of modules. The code base is owned by the entire team
		and anyone may make changes anywhere. You can consider this as no
		code ownership, but it's advocate prefer the emphasis on the
		notion of ownership by a team as opposed to an individual. (The
		term collective code ownership comes from [Extreme Programming](https://martinfowler.com/articles/newMethodology.html#xp),
		although in the second edition the practice is called Shared Code.)


Of the three the one I really don't like is strong code
	ownership. There are just too many situations where something you
	need to do needs changes to other people's code. Persuading them to
	make the change and waiting for the change often takes so long that
	it leads to delays and deeper problems, this is particularly galling
	when the change is a simple one.


A good example of a simple change that causes trouble is renaming
	a public method. Modern refactoring tools can do this safely with
	extensively used public methods. But this violates code ownership if
	you cross a module boundary. Essentially you've turned all
	interfaces between developers into [PublishedInterface](https://martinfowler.com/bliki/PublishedInterface.html)s,
	with all the attendant overheads to change.


Even worse is when you want an implementation change, but because
you can't get it quickly enough you make a copy of the foreign code
into your module, call your copy of the code and make the change. Of
course you intend to sort out the mess later.


Weak code ownership is a good way to mitigate these kinds of
	problems. People can make changes freely, the code owner just has to
	keep an eye on things.


The choice between weak and collective ownership has more to do
	with the social dynamics of the team. Both seem to work, and fail,
	equally well. Personally I prefer the dynamics of a collective code
	ownership team - particularly in the context of Extreme Programming.
