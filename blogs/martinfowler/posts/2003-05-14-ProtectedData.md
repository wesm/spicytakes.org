---
title: "Protected Data"
description: "Is it good OO design to have data in my classes with theprotectedAccessModifier?"
date: 2003-05-14T00:00:00
tags: ["encapsulation", "language feature"]
url: https://martinfowler.com/bliki/ProtectedData.html
slug: ProtectedData
word_count: 326
---


**Is it good OO design to have data in my classes with the *protected*
AccessModifier?**


OO designers [differ](http://groups.google.com/groups?threadm=db9bbf31.0303260938.a4bad42%40posting.google.com) about whether you should make all your data
private or whether they allow some to be public.


(Before I dive into this murky pool, I should point out that the
meaning of the protected [AccessModifier](https://martinfowler.com/bliki/AccessModifier.html) varies in subtle but important
ways from language to language.)


I think the reason this topic gets so difficult is because people look
at it either from the angle of in-team or cross-team development, and
it's this point of view that dominates.


On one hand, if I'm writing a subsystem and decide to implement some
behavior through a hierarchy, then I'm quite happy to have the
subclasses have deep access into their superclasses. After all it's
all my code - I'm using the subclasses to provide polymorphic
behavior, not to provide modularity.


On the other, if I'm building a framework and providing hook classes
that I expect to be overridden, I may want to protect data so that I
can make changes in the future without breaking people's
subclasses. Indeed it's more insidious than this because subclasses
can easily break superclasses if you're not careful - this is referred
to as the [fragile base class
problem](http://www.cas.mcmaster.ca/~emil/publications/fragile/).


So I don't think you can say that making data protected is always a
good or bad thing. If you're intending that clients outside your
control will override a certain class, then you should treat your
protected features as part of your published interface, and as a
result take more care. Publishing fields is a bad idea, so I wouldn't
do it in that case.


But if that's not your intention, and it helps you to have access to
data in subclasses you write, then it seems reasonable to me. But I'll
admit my default is to make fields private and I only rarely change it
to protected.


A related question is whether you should use [SelfEncapsulation](https://martinfowler.com/bliki/SelfEncapsulation.html).
