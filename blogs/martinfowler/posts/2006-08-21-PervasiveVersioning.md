---
title: "Pervasive Versioning"
description: "Recently Apple announced theTime Machine, which is the ability 	to go back in time and see all the alterations to your files, 	including finding deleted files. For some of us intense geeks, this 	is n"
date: 2006-08-21T00:00:00
tags: ["version control"]
url: https://martinfowler.com/bliki/PervasiveVersioning.html
slug: PervasiveVersioning
word_count: 399
---


Recently Apple announced the [Time Machine](http://www.apple.com/macosx/leopard/timemachine.html), which is the ability
	to go back in time and see all the alterations to your files,
	including finding deleted files. For some of us intense geeks, this
	is not a new feature. Like others, I put my entire working directory
	under version control, originally CVS now [Subversion](https://martinfowler.com/bliki/Subversion.html), and
	have thus had the ability to easily look at all the changes to
	everything I work on. It's such a useful feature that I've wondered
	before about what it would be like to have [MoreVersionControl](https://martinfowler.com/bliki/MoreVersionControl.html), and
	perhaps Time Machine is a step in that direction.


Time Machine is seen as an automated backup system, so it doesn't
	seem to support the notion of thoughtful commits that a versioning
	system has. I think this is the best way to go, at least initially,
	so that people get used to the idea of this sort of system. The
	time-based browser looks interesting, versioning systems need some
	rethinking of user-interface - and who better than Apple to do this?


I think the more important step is that making this capability
	more widely available will give a kick to application developers. In
	[MoreVersionControl](https://martinfowler.com/bliki/MoreVersionControl.html) I said that not enough applications
	know how to diff and merge. Perhaps Time Machine will start getting
	people to think about that and start building these capabilities
	into applications, this would make versioning much more handy.


Versioning is handy on a single desktop, but as anyone who has
	used it knows, the *real* benefit is in collaboration. Software
	projects see an enormous benefit from using a version control system
	as a collaboration tool. Other efforts can as well - presentations,
	white papers, excel models can all benefit for versioned
	collaboration tools. (Again the lack of intelligent diff and merge
	is a big barrier to this.) Even lonely me benefits hugely with my
	[MultipleDesktops](https://martinfowler.com/bliki/MultipleDesktops.html).


So my hope that is that Time Machine will spur development of
	applications that are aware of versioning and can take advantage of
	it, which will in turn shift to more effective collaboration. But in
	any case, I'd strongly urge you to try doing it now. Subversion is
	free and easy to set up, and even though applications don't diff and
	merge well there are worthwhile benefits in collaborating with
	others using a shared versioned repository. It's much better than
	keeping track of emailed documents or using an unversioned shared drive.
