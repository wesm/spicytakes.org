---
title: "Derived Information"
description: "How do you represent derived information in the UML?"
date: 2003-12-25T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/DerivedInformation.html
slug: DerivedInformation
word_count: 420
---


**How do you represent derived information in the UML?**


Consider a simple example, you have a class that represents a
rectangle and you want to know its height, width, and area. How do you
show that the area is derivable from the height and width?


A common way is to show the height and width as attributes and
the area as an operation. People do this because that's how they would
implement it; fields for the height and width, and a method to
calculate the area.


UML also has a notation for derived properties, you prefix the
name with a '/'. So you could use this for the area.


Both of these approaches are reasonable and different teams do
different things. Some only use attributes for fields; such teams
don't use derived notation, or only do it when derivable information
is cached in a field. Others use derived markers when they follow the
same naming standard for derived values that they do for fields, such
as a `getArea(`) operation or using properties in languages
like C# or Ruby.


My preference is to think about this slightly differently. One of
the key properties of an object is that they are encapsulated. If I'm
the user of the rectangle class I actually should not know or care
that the circumference is calculated. The implementor might store the
height and circumference and calculate the width - I shouldn't be able
to tell. So that would leads me to use an identical
naming convention for fields and for derived information on the
implementation, and to represent them all as properties on the class
diagram.


Does that mean I wouldn't use the derived marker? Actually no.
I'm happy to mark the circumference as derived, but it indicates that
there's a constraint between the three values, it doesn't specify what
is calculated and what is stored. So in a similar argument I would say
that if you have three side properties for a triangle it's reasonable
to mark one of them as derived.


In fact it matters less which approach you take than it does that
you follow a consistent style within your team. It's also important to
remember that different people do different things, so this is
something you'll need to figure out when looking at a foreign diagram.
(I use derivation less than I would in my books because of this
inconsistency of interpretation.) It's one of the many cases where the
UML is less rigorous than it would like to think it is.
