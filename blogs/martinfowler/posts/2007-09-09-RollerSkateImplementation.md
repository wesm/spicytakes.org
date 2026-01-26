---
title: "Roller Skate Implementation"
description: "A key property of agile development is figuring out how to make a 	system go live with a small subset of features. We build software 	for the business value it offers, the quicker we go live, the fast"
date: 2007-09-09T00:00:00
tags: ["experience reports", "requirements analysis", "project planning"]
url: https://martinfowler.com/bliki/RollerSkateImplementation.html
slug: RollerSkateImplementation
word_count: 309
---


A key property of agile development is figuring out how to make a
	system go live with a small subset of features. We build software
	for the business value it offers, the quicker we go live, the faster
	we get at least some of that business value.


My colleague Dave Leigh-Fellows told me one of my favorite
	examples of this kind of thinking. It came when we has working for a
	brokerage firm. They had a new kind of product that they wanted to
	get into the market. The full software support for this was a web
	page that the customer filled in that generated the necessary
	transactions against the back-end system. But Dave came up with a
	way to get the product into the market faster than that.

- Version 1 was a static web page that described the product and
provided a telephone number to call. Some temporary staff then spoke
to the customer and entered the information into the back end
system.
- Version 2 was a web form that captured the data the customer
filled in. However this version didn't load that data into to the back
end system. Instead the web form generated a fax. They hired some more
temps to get the orders from the fax machine to the people that keyed
the information into the back end system. Since the fax machines were
a bit of a distance away, this is where the roller-skates came
in.
- Version 3 hooked the web form into the back-end system directly.


The first two versions may not have been the most elegant
	solutions ever conceived, but they did get the product into the
	market much more quickly. I've not come across any other examples of
	iterative development that use roller-skates, but that may be
	more due to lack of imagination rather than lack of need.
