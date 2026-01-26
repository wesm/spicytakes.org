---
title: "Interface Implementation Pair"
description: "The practice of taking every class and pairing it with an 	interface. So as a result you see pairs of things - maybe ICustomer 	and Customer or Customer and CustomerImpl. In many ways it echoes 	the C"
date: 2005-12-08T00:00:00
tags: ["api design", "object collaboration design"]
url: https://martinfowler.com/bliki/InterfaceImplementationPair.html
slug: InterfaceImplementationPair
word_count: 213
---


The practice of taking every class and pairing it with an
	interface. So as a result you see pairs of things - maybe ICustomer
	and Customer or Customer and CustomerImpl. In many ways it echoes
	the C/C++ habit of header files for each class, although in this case
	the interfaces and implementations are actually separate types.


The advantage of this approach is that you can completely
	substitute anything at any point by providing another implementation
	of the interface.


This isn't, however, a technique that I've ever much liked. Using
	interfaces when you aren't going to have multiple implementations is
	extra effort to keep everything in sync (although good IDEs
	help). Furthermore it hides the cases where you actually do provide
	multiple implementations.


As often is the case the trade-offs are different depending on
whether you are writing application classes or libraries. In an
application if you ever need an interface where you don't have one you
can just do [Extract Interface](http://www.refactoring.com/catalog/extractInterface.html) and you're done. With published
libraries your users don't get that fast feedback so it's much more
useful to make your published types interfaces. However just mimicking
the implementation classes in your [PublishedInterface](https://martinfowler.com/bliki/PublishedInterface.html)s is rarely the best move.
Interfaces should be designed around your clients' needs, often these
don't match the implementation.
