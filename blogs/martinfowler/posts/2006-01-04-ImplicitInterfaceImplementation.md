---
title: "Implicit Interface Implementation"
description: "Both Java and C# share the same model of pure interface 	types. You declare a pure interface by goinginterface 	Mailable, then you can declare you implement it withclass Customer implements Mailable(i"
date: 2006-01-04T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/ImplicitInterfaceImplementation.html
slug: ImplicitInterfaceImplementation
word_count: 826
---


Both Java and C# share the same model of pure interface
	types. You declare a pure interface by going `interface
	Mailable`, then you can declare you implement it with
	`class Customer implements Mailable` (in Java). A class
	may implement any number of pure interfaces. One of the things this
	model ignores is that you have *implicit* interfaces whenever
	you have a class.


The public implicit interface
	Customer is all the public members declared on
	Customer. (This implicit interface is present in every OO language
	I've seen.) One thing that neither Java nor C# allow you to do is
	to implement an implicit interface - that is you cannot write `class
	ValuedCustomer implements Customer`


What would it mean to implement an implicit interface?
	Essentially it would tell the type system that the ValuedCustomer
	class implements all the methods declared in the public interface of
	Customer but does not take any of its implementation, that is its
	public method bodies, and non public methods or data. In other
	words we have interface-inheritance but not implementation-inheritance.


It would be equivalent to changing Customer into an interface
	that contains all the public methods of customer, and then having a
	CustomerImpl class that implements this interface.


Why might this be useful? One case I remember from the past was
	in the old days of Java, before the current collections
	framework. We wanted to replace the Vector class with an
	implementation of our own, but couldn't because Vector was a class
	and we could only subclass it. From time to time you run into cases
	like this when libraries don't provide interfaces to allow free
	substitution, without this feature we're stuck.


This particularly comes up these days with testing. There are
lots of times when you want to stub out stuff, but it's difficult or
impossible unless you have an interface. It also leads to defining
pure interface types when the only reason to do it is to support
substitution for testing. While using an
[InterfaceImplementationPair](https://martinfowler.com/bliki/InterfaceImplementationPair.html) is a common approach it's one
that many of us don't favor. Implicit Interface Implementation would
be a much cleaner approach.


So why don't languages allow this? I don't really know - but then I'm not
	a language designer. I once had the chance to ask Anders Heljsberg
	about this and his reply was much along the same lines as his preference to
	only have overriding if you explicitly declare members as
	virtual. Essentially it's a concern about subclasses (or
	implementers in this case) breaking the superclass, something which
	touches on a much broader topic how to use subclassing. However
	this was only a brief conversation over dinner so I'm not convinced
	we really fleshed out the discussion.


After writing this my old colleague Mike Rettig pointed out that
	one of the problems with this is that classes actually define
	multiple implicit interfaces. In Java, for example, the customer
	class actually defines four implicit interfaces: public, protected,
	package, and private. If an object collaborates with a Customer it
	might use any of these interfaces (another instance of customer can
	use private features.) If we want to implement an implicit interface
	we either have to implement everything, or we to define how far we
	are going. I don't know how hard it would be for the type system to
	keep track of that.


Of course the examples I've given mostly work fine with just
	public implicit interfaces, so in practice that might be enough.


[Ian

Griffiths](http://www.interact-sw.co.uk/iangblog/2006/01/05/implicitinterfaces) pointed out that the issue is possibly about mixing
classes and interfaces. Microsoft's COM technology actually had a
sharp separation between the two: âif you want to use an object in COM
you have to do so via an interface. So you're always able to make your
own implementation.â This was made pretty transparent in VB 6 
where COM interfaces could be generated behind the scenes.


This issue doesn't come up with dynamically typed languages. If
you want to implement another class's interface all you need to do is
implement the same methods and just use the object where you need it.
You don't need to implement every method, just the ones that are being
used in the particular interaction you're focused on. It's a scheme
that works very nicely for testing - Smalltalkers referred to it for a
while as the Imposter pattern. It's also quite common to use dynamic
proxies to do this kind of thing in Java, although I feel that
implicit interface implementation would be more communicative.


Does any of this matter? Mostly it seems to be an issue for
	testing, it's much harder to insert [TestDouble](https://martinfowler.com/bliki/TestDouble.html)s if you
	can't use a reimplementation - and often subclassing won't do the
	trick if the superclass wants a real connection to the
	database. It may well only be an issue for testing - Robert Conley
	told me that he uses VB6's ability to do reimplementation a lot for
	testing, but never found a need for it in production code.
