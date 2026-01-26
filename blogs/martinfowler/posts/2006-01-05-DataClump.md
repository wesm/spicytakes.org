---
title: "Data Clump"
description: "Whenever two or three values are gathered together - turn them into a $%#$%^ object."
date: 2006-01-05T00:00:00
tags: ["bad things", "programming style", "refactoring"]
url: https://martinfowler.com/bliki/DataClump.html
slug: DataClump
word_count: 127
---


> Whenever two or three values are gathered together - turn them
> into a $%#$%^ object.
> -- Me (it was funnier with the voices)


This is one of my favorite [CodeSmell](https://martinfowler.com/bliki/CodeSmell.html)s from the refactoring
book. You spot it when you constantly see the same few data items
passed around together. start and end are a good example of a data
clump wanting to be a [range](https://martinfowler.com/eaaDev/Range.html). Often data
clumps are primitive values that nobody thinks to turn into an
object.


The first step is to replace data clumps with objects and use the
objects whenever you see them. An immediate benefit is that you'll
shrink some parameter lists. The interesting stuff happens as you
begin to look for behavior to move into the new objects.
