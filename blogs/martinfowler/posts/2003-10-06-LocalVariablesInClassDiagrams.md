---
title: "Local Variables In Class Diagrams"
description: "How do you show local variables (parameters, temps etc) on UML class diagrams?"
date: 2003-10-06T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/LocalVariablesInClassDiagrams.html
slug: LocalVariablesInClassDiagrams
word_count: 265
---


**How do you show local variables (parameters, temps etc) on
UML class diagrams?**


The simple answer to this is that you don't. I don't remember a
case where I've seen a need to do this. Where I've seen it done, it
hasn't communicated much that's useful.


If you really, really need to; my recommendation is to use a
dependency with a «keyword» and take a long cold shower
afterward. If one object is storing an instance of another in a local,
that certainly implies some form of dependency. Indeed usually when
such a dependency is worth mentioning, it's only the fact that there's
a dependency that matters, so I wouldn't bother with a keyword.


Some books talk about using a stereotype of association for this;
and indeed the UML 1.3 spec suggests this. The reasons for this are
somewhat involved and to do with problems in the UML meta-model. If
you want to show links between instances in collaboration diagrams,
they need to be represented in the meta model. The way they found to
do this was to make stereotyped associations. They found a better way
to do this in UML 2's meta-model - so in UML these stereotypes are
gone.


My problem with using association notation for this is that I
think there is an important difference between relationships that are
only there within the span of a method invocation, and relationships
that hold for the whole life of a class - and the latter relationships
are far more important. As a result I only like to use associations
for those longer lived relationships.
