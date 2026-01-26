---
title: "Published Interface"
description: "Making a change to an interface that impacts all its consumers requires two thinking modes:       implementing the change itself, and then updating all its usages. This can be hard when you       try "
date: 2014-05-13T00:00:00
tags: ["encapsulation", "language feature", "application architecture", "api design"]
url: https://martinfowler.com/bliki/PublishedInterface.html
slug: PublishedInterface
word_count: 129
---


*Published Interface* is a term I used (first in [Refactoring](https://martinfowler.com/books/refactoring.html))
to refer to a class interface that's used outside the code base that
it's defined in. As such it means more than public in Java and indeed
even more than a non-internal public in C#. In my column for IEEE
Software I argued
that [the distinction between published and public is actually more
important than that between public and private.](https://martinfowler.com/ieeeSoftware/published.pdf)


The reason is that with a non-published interface you can change
it and update the calling code since it is all within a single code
base. Such things as renames can be done, and done easily with modern
refactoring tools. But anything published so you can't reach the
calling code needs more complicated treatment.


reposted on 03 May 2012
