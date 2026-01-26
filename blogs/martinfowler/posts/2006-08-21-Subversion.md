---
title: "Subversion"
description: "Recently Apple announced theTime Machine, which is the ability 	to go back in time and see all the alterations to your files, 	including finding deleted files. For some of us intense geeks, this 	is n"
date: 2006-08-21T00:00:00
tags: ["version control"]
url: https://martinfowler.com/bliki/Subversion.html
slug: Subversion
word_count: 300
---


Subversion is the an open-source version control system - in
essence a successor to CVS. It fixes the biggest issues with CVS,
introducing such things as atomic commits and support for file and
directory renaming. I've been using it for a couple of years and have
found it very solid.


My colleague Mike Mason has written the [Pragmatic
Programmer Book on Subversion](http://www.pragmaticprogrammer.com/titles/svn/). While you can get a [detailed book online](http://svnbook.red-bean.com/), Mike's book
gives you an excellent introduction to subversion and how to use it.
Buy lots of copies and we won't have to give him a pay raise.


One of the big ways I use subversion is to handle
[MultipleDesktops](https://martinfowler.com/bliki/MultipleDesktops.html). I keep all my working files in Subversion
and use updates and commits to keep everything in sync.


On the basis of my informal conversations with my colleagues,
Subversion (abbreviated to SVN) is a better system than all the
commercial tools except Perforce. So if you're using something else,
you may want to consider a switch.


As someone who uses version control all the time, I think it's
something that can grow into more areas of computer use. Other than
software developers, few computer users use version control. Yet as
software developers know, version control is a great mechanism for
collaborative work, allowing multiple people to work together on a
single software system. What would be the benefits of version control
being more widely used? Most applications that people use have little
capabilities to do diffs and merges. If applications were more aware
of version control then I think we would see more interesting things
being done with it. I hope that a solid, usable, open source tool will
spread the usage of version control to a wider audience - after all we
are no longer short of disk space.
