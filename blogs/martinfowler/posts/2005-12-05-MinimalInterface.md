---
title: "Minimal Interface"
description: "Hanging around the ruby crowd for a while, I've come across the 	term 'Humane Interface' quite a bit. It describes part of the 	rubyist attitude to writing class interfaces, I think it also sets 	up a"
date: 2005-12-05T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/MinimalInterface.html
slug: MinimalInterface
word_count: 505
---


A minimal interface is a style of API design which I contrast
	here to a [HumaneInterface](https://martinfowler.com/bliki/HumaneInterface.html). The idea behind the minimal
	interface is to design an API that allows the client to do
	everything they need to do, but boils down the capabilities to the
	smallest reasonable set of methods that will do the job. (See
	[HumaneInterface](https://martinfowler.com/bliki/HumaneInterface.html) for a good example of the difference.)


Using the ruby-array/java-list example from
[HumaneInterface](https://martinfowler.com/bliki/HumaneInterface.html), the you would not include a first and last
method on a list class that already has an indexer and a length method
because you can do first and last just using the exising interface. As
a result first and last are convenience methods - minimalists don't
avoid all convenience methods, but convenience methods have a high bar
to cross to get in.


The arguments for [HumaneInterface](https://martinfowler.com/bliki/HumaneInterface.html) are there, here's
the rationale for a minimal interface.


Interfaces take time to learn. A class with a huge interface is
	not likely to be used well and may well be off-putting in the first
	place. By keeping a small, focused set of methods, you make it
	easier for clients to find out what the class is and what it can
	do.


This focus is also important for the class designer. A common
	problem with class design is to make classes do too much. Focusing
	on the essentials helps keep cruft out of the class, allowing it to
	focus on doing one job and doing it well.


If you follow a humane approach, how do you know where
	to stop? If you keep adding methods because someone might want them,
	you'll have no end of methods. So you need some guideline to avoid
	this explosion of methods. The humane guideline (provide what is
	useful) is arbitrary and difficult. The minimalist one is simple -
	if the client can do it with the existing methods, then they don't
	need an extra one.


(Note that this issue of finding what is useful is more of an
	issue for people writing published class libraries than it is for
	application code. With application code you know your uses - it's a
	closed system.)


If you are using statically typed pure interfaces (such as with
	the interface keyword in Java and C#), then another reason
	to keep the method count small is that it reduces the burden on
	implementers. A large number of methods all have to be implemented
	which is a lot of work. (Using an abstract class as a mixin can help
	reduce this burden.)


If you want more functionality on a minimal class you can do it
	by using other classes. For example in Java if you wish to reverse
	or sort a list (operations which are regular methods on Ruby's
	Array) you use the Collections utility class.


When you're working on a library, once you publish it it's very
	hard to take anything out. As a result it's better to start with
	something too small and add things, than to have something too big
	when you can't remove things.
