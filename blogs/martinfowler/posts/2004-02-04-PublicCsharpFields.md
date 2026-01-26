---
title: "Public Csharp Fields"
description: "When I first came across C# I liked the notion of properties right from the start. The getX and setX conventions of C++/Java always seems rather silly to me, it's much more natural to writeobj.X = oth"
date: 2004-02-04T00:00:00
tags: ["encapsulation", "language feature"]
url: https://martinfowler.com/bliki/PublicCsharpFields.html
slug: PublicCsharpFields
word_count: 198
---


When I first came across C# I liked the notion of properties
right from the start. The getX and setX conventions of C++/Java always
seems rather silly to me, it's much more natural to write `obj.X
= other.X`. Providing a property with get and set methods turns
a common convention into a naturally supported feature of the
language.


Another thing about it I liked is that, from a language point of
view, properties and fields look the same. So if I have a field x
which I can just read and write to, I can just declare it as a field.
I don't worry about this violating encapsulation, because should I
wish to do something more fancy I can just replace it with a property later. It
all saves a lot of typing of stupid accessor functions.


Alas, all is not so simple. Fields and properties do have the
same access in terms of program text, but they are represented
differently by reflection. As a result various tools that use
reflection will be broken if you switch between fields and
properties.


So now I have to write stupid accessor functions for accessible
data values. Sigh. (Or use Ruby.)
