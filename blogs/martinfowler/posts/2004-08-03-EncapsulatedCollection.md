---
title: "Encapsulated Collection"
description: "If you learn about object-oriented design, you quickly learn that 	it's important to encapsulate your data. The simplest form of 	encapsulation is to use accessors (getting and setting methods) or 	pr"
date: 2004-08-03T00:00:00
tags: ["encapsulation"]
url: https://martinfowler.com/bliki/EncapsulatedCollection.html
slug: EncapsulatedCollection
word_count: 336
---


If you learn about object-oriented design, you quickly learn that
	it's important to encapsulate your data. The simplest form of
	encapsulation is to use accessors (getting and setting methods) or
	properties - if your language supports it.  (Some even do
	this within the class - [SelfEncapsulation](https://martinfowler.com/bliki/SelfEncapsulation.html)


While the get and set convention works for single values, it
	doesn't do well for multi-valued fields - fields that are
	collections of values. In this case you need a different accessor
	scheme. The key point with this is that you don't want to give
	clients direct access to the collection data structure itself - for
	if you do it allows clients to alter the supplier's data without the
	supplier being able to intervene. The whole point of encapsulation
	is that an object controls access to its data.


To modify a collection field, you usually see specific methods to
add an element to a collection, or remove an element to the
collection. So if we have a Company class with a collection of
employees - we might expect methods `addEmployee` and
`removeEmployee`. Occasionally you might see a
`setEmployees` method that takes a collection, but usually
it is easier to have add and remove methods.


Usually the trickiest area is in the getting side. You don't want
to return the actual collection used to store the objects - otherwise
people can add and remove the items without using the encapsulating
add and remove methods. So what do you return? The best option is a
read-only view on the underlying collection. Java's collections
library makes this easy with their unmodifiable collection wrappers.
Another option, if available, is an iterator that can't update the
underlying collection.


If neither of these is available the usual response is to return
a copy of the underlying collection. That way if a client modifies it,
it has no effect on the real collection. There is a little time
overhead in copying the collection, but since this is just a bunch of
object references it's hardly ever significant.
