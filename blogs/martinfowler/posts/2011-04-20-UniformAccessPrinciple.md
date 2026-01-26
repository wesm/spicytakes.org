---
title: "Uniform Access Principle"
description: "All services offered by a module should be available through a uniform notation, which does not betray whether they are implemented through storage or through computation."
date: 2011-04-20T00:00:00
tags: ["encapsulation", "language feature", "api design", "object collaboration design"]
url: https://martinfowler.com/bliki/UniformAccessPrinciple.html
slug: UniformAccessPrinciple
word_count: 448
---


> All services offered by a module
> should be available through a uniform notation, which does not betray
> whether they are implemented through storage or through
> computation.
> -- Bertrand Meyer


Bertrand Meyer coined this principle in his highly-influential book
[Object-Oriented Software
Construction](https://www.amazon.com/gp/product/0136291554/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0136291554&linkCode=as2&tag=martinfowlerc-20).1


1: 
This formulation of of the principle is from the second edition. In
the first edition he called it the Uniform Reference
Principle  (§2.1.4). He changed it to Uniform Access Principle in the second
edition and supplied the quoted definition.


The essential point of the principle is that if you have a person
object and you ask it for its age, you should use the same notation
whether the age is a stored field of the object or a computed
value. It effectively means that a client of the person should neither
know nor care whether the age is stored or computed.


![](images/uniformAccessPrinciple/sketch.png)


This gives the
person object the flexibility to change between the two easily as well
as removing what is usually an unnecessary concern from the
client. It's an important part of encapsulation - or at least the
data-hiding aspect of encapsulation.


Although it's a fundamental feature of object-oriented programming,
remarkably few OO languages really follow it. (Eiffel is naturally an
exception.) Most languages simulate it by convention, hence the habit
of using accessors such as `getAge` in Java and C++ programs.


Whatever the language does, it's important that programmers don't
violate the principle. Often you'll see conventions that subvert uniform
access. An example of this might be saying that data accessors are
named `getAge` while computed accessors are named
`calcAge`. I make a point of naming my accessors the same
way in either case.


One argument against uniform access is that data access is fast
while computation can be slow - and it's useful to give client
programmers an indication if a method is slow to respond. I prefer to
treat this as a special case - follow the uniform access principle
unless there is a particularly slow computation (and that should be
one that's been measured to be slow, not just expected to be
slow). And in that case there are other options, such as a caching
accessor, that you can also explore.


Uniform access applies to both getters and setters, although often
computed accessors are read-only. Whether a property is read-only or
not is a separate issue as to whether it is stored or computed.


## Notes


1: 
This formulation of of the principle is from the second edition. In
the first edition he called it the Uniform Reference
Principle  (§2.1.4). He changed it to Uniform Access Principle in the second
edition and supplied the quoted definition.
