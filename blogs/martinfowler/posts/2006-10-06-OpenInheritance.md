---
title: "Open Inheritance"
description: "One of the longest running arguments on object-oriented circles 	is the debate betweenOpenInheritanceand 	Designed Inheritance. The principle of Designed Inheritance is 	probably best summed up byJosh"
date: 2006-10-06T00:00:00
tags: ["encapsulation", "api design"]
url: https://martinfowler.com/bliki/OpenInheritance.html
slug: OpenInheritance
word_count: 404
---


This is the opposite attitude to
	[DesignedInheritance](https://martinfowler.com/bliki/DesignedInheritance.html). Advocates of open inheritance do not
	look to disallow inheritance by [Seal](https://martinfowler.com/bliki/Seal.html)ing their classes or
	doing anything else to stop people inheriting classes.


Fans of open inheritance don't disagree with designed inheritance
fans about the dangers of inheritance. Inhertiance is an initmate
relationship with plenty of dangers for the unwary. You can easily
break superclass behavior and you have to be expecially wary of
upgrades since you can be relying on hidden implementation details.
But open inheritors belive that the choice of whether to take on those
risks should be the decision of the users of the library. If they
choose to inherit, then they accept the risks and the
consequences.


A designed approach is in theory better, but the problem is that
it's very hard to figure out all the ways in which someone can
usefully vary an existing class. This leads to two problems:  library
users can't use a library in a way that the designer didn't anticipate
and  library designers  have to take on the  responsibility of trying to
anticipate  extensions.


Designed inhertance assumes that library writers are wiser than their
	users. Often this isn't the case. Library writers make mistakes too,
	if inheritance is open then the user of the class has the
	opportuntity to fix them and still take advantage of the library
	writers hard work.


Designing for inheritance is a very tricky task, particularly as
	you usually don't know what the use cases are. Asking people to
	think through all inheritance cases places a big burden on library
	writers. Open inheritance means they don't have to deal with it
	unless they specfically want to, with the proviso that those that do inherit
	have to be careful about what they are doing.


One area that particularly causes trouble for designed
inheritance is testing. Often with testing you need to use a
[TestDouble](https://martinfowler.com/bliki/TestDouble.html), but are prevented by a sealed class with no
interface that you can use for substitution. These kinds of APIs can
be [Detestable](https://martinfowler.com/bliki/Detestable.html)


Open inheritors often do design classes with intended extension
	points that are safer to use than others. However they usually mark
	these through naming or documentation rather sealing them. That way
	people are pointed to the safe areas but not prevented from
	overriding elsewhere if necessary.


Often design inheritance comes with  a
[DirectingAttitude](https://martinfowler.com/bliki/DirectingAttitude.html), which usually forgets that fools are
ingenious when it comes to messing things up.
