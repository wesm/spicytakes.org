---
title: "Setter Initialization"
description: "With setter initialization you construct an empty object and then 	use setter methods to setup various properties as you go. (An   alterative toConstructorInitialization.)"
date: 2006-02-09T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/SetterInitialization.html
slug: SetterInitialization
word_count: 183
---


With setter initialization you construct an empty object and then
	use setter methods to setup various properties as you go. (An
  alterative to [ConstructorInitialization](https://martinfowler.com/bliki/ConstructorInitialization.html).)


So create a person with firstname, lastname, and a
	collection of favorite bars we might see something like


```
#ruby
mf = Person.new
mf.firstname = 'Martin'
mf.lastname = 'Fowler'
mf.add_bar âTurner's Oyster Barâ
mf.add_bar âSquare and Compassâ

```


This approach gives you the maximum flexibility in wiring up
	objects, allowing you to provide just the collaborators you need
	for a specific usage.


It frees you from having to set all the
	values at once - which is handy if some objects are only available
	at later times.


Each method call is compact, which avoids the
	problem of long parameter lists to constructors and an array of
	different constructors to choose from.


Marko Schulz reminded me that setter  methods have names that
explain their use for the new object - this is a noticeable advantage
over [ConstructorInitialization](https://martinfowler.com/bliki/ConstructorInitialization.html) in most languages these days
which only have positional parameters. Constructor parameters with
very general types (strings etc) can easily get very cryptic.
