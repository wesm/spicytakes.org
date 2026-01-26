---
title: "More Version Control"
description: "Recently Apple announced theTime Machine, which is the ability 	to go back in time and see all the alterations to your files, 	including finding deleted files. For some of us intense geeks, this 	is n"
date: 2006-08-21T00:00:00
tags: ["version control", "writing"]
url: https://martinfowler.com/bliki/MoreVersionControl.html
slug: MoreVersionControl
word_count: 284
---


As someone who uses version control all the time, I think it's
	something that can grow into more areas of computer use. Other than
	software developers, few computer users use version control. Yet
	as software developers know, version control is a great mechanism
	for collaborative work, allowing multiple people to work together on
	a single software system. What would be the benefits of version
	control being more widely used?


We've reached a point where it's practical for everyone to use
version control systems in their work. Subversion is a freely
available system that supports binary formats easily and removes many
of the limitations of CVS. Disk space is cheap enough that you can put
people's entire working directory under version control.


At the moment the big limitation is that not enough applications
	and tools are aware of version control. Word has had some change
	tracking capability for a long time, but it's not written with
	version control in mind. What would version control facilities, with
	diff and merge, look like for common applications that people
	use. How could these kinds of applications make use of these ideas?


I do schematic drawings with tools like Visio. It would be nice
	to be able to diff drawings to see what changes have made between
	versions and to see what changes someone else made to my diagram.To
	really get the value of this kind of things we may need tools that
	support a [SemanticDiff](https://martinfowler.com/bliki/SemanticDiff.html).


This might be a real opportunity for the open source community
	to take conventional applications and move them in this
	direction, building on the fact that everyone can easily obtain and
	use [subversion](http://subversion.tigris.org/). Some good ideas around here could really enhance
	collaborative work.
