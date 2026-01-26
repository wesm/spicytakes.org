---
title: "Multiplicity Not Cardinality"
description: "When data modeling methods talk about relationships, they use the 	termcardinalityto indicate how many entities may be linked 	together. So you might have a relationship between order and 	customer an"
date: 2003-08-12T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/MultiplicityNotCardinality.html
slug: MultiplicityNotCardinality
word_count: 201
---


When data modeling methods talk about relationships, they use the
	term *cardinality* to indicate how many entities may be linked
	together. So you might have a relationship between order and
	customer and say that the cardinality of the relationship is
	one-to-many. Or you might hear that the cardinality of customers for
	an order is 0-to-many.


UML avoids the term cardinality preferring to use
	*multiplicity*. Often people with a data modeling background
	are surprised at this since cardinality has been so widely used in
	data modeling circles.


The reason for the change is that the dictionary definition of
	cardinality is *âthe number of elements in a particular set or
	other groupingâ* (OED). According to this the data modeling usage
	is actually wrong. In the excellent [UML Reference Manual](https://www.amazon.com/gp/product/020130998X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=020130998X&linkCode=as2&tag=martinfowlerc-20), Rumbaugh defines
	multiplicity as âA specification of the range of allowable
	cardinality values - the size - that a set may assumeâ. The UML uses
	multiplicity in various places, for a property (association or
	attribute) and also to show the multiplicity of parts in a composite
	structure. It's formally defined as a lower and upper bound. An
	association (the UML equivalent to a relationship in data modeling
	circles) has a multiplicity for each direction.
