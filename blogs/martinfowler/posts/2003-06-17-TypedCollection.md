---
title: "Typed Collection"
description: "When people are starting to work with objects, particularly in a 	strongly typed language, a common question is whether they should 	have specific collection classes for different domain types. So if "
date: 2003-06-17T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/TypedCollection.html
slug: TypedCollection
word_count: 212
---


When people are starting to work with objects, particularly in a
	strongly typed language, a common question is whether they should
	have specific collection classes for different domain types. So if
	you have a company class which stores a collection of employees,
	should you use a regular collection class from your libraries, or
	should you create a specific `EmployeeList` class - a
	typed collection.


(Of course if you have generics, then you would just use a
	parameterized class here - but I'll assume you are using something
	like Java or C# which don't yet have this feature.)


The main argument in favor of using a typed collection is that it
	promotes type-safety. You can ensure that only employees are added to
	the class, and you can also ensure that any elements you get from
	the collection are properly typed - thus avoiding a smelly downcast.


On the whole, however, it isn't worth the trouble. If you're
using a collection you should be making it an
[EncapsulatedCollection](https://martinfowler.com/bliki/EncapsulatedCollection.html), so that protects the type safety on
updates. Handling the downcasting on access is a nice idea, but
involves a *lot* of boilerplate code. You can reduce the pain of
this with code generation - but my take is that it's more trouble than
it's worth.
