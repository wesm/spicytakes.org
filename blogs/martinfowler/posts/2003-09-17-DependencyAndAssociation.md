---
title: "Dependency And Association"
description: "What is the difference between dependency and 	association?"
date: 2003-09-17T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/DependencyAndAssociation.html
slug: DependencyAndAssociation
word_count: 374
---


**What is the difference between dependency and
	association?**


In general, you use an association to represent something like a
	field in a class. The link is always there, in that you can always
	ask an order for its customer. It need not actually be a field, if
	you are modeling from a more interface perspective, it can just
	indicate the presence of a method that will return the order's
	customer.


To quote from the 3rd edition of [UML Distilled](https://www.amazon.com/gp/product/0321193687/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321193687&linkCode=as2&tag=martinfowlerc-20) (now just out) âa
	dependency exists between two elements if changes to the definition
	of one element (the supplier) may cause changes to the other (the
	client)â. This is a very vague and general relationship, which is
	why the UML has a host of stereotypes for different forms of
	dependency. In code terms, such things as naming a parameter type and
	creating an object in a temporary variable imply a dependency.


You don't want to show every dependency on a UML diagram - there
	are far too many. You need to be very selective and show only those
	that are important to whatever it is you are communicating.


I tend not to use stereotypes on the dependencies very often. I find that
	most of the time the key point I want to show is that a dependency exists,
	and which kind is rather less vital.


Associations also imply dependency, if there is an association
	between two classes, there is also a dependency. But I can't imagine
	a case where you would show that dependency as an extra line on the
	diagram. The association implies it, as does a generalization.


One source of the confusion was the use of transient links
	in UML 1. These appeared due to meta-model problems in UML 1. They
	manifested themselves as stereotypes of association such as parameter. I've always disliked these since I think the
	difference between a permanent slot and a relationship that's only
	present within the context of a method is rather important. As a
	result I would use such stereotypes on a dependency rather than an
	association. In UML 2 this issue no longer arises, since the
	meta-model has a different way of handling method scoped
	relationships, so such stereotypes are no longer valid in UML 2.
