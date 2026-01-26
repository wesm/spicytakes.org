---
title: "Constructor Initialization"
description: "With setter initialization you construct an empty object and then 	use setter methods to setup various properties as you go. (An   alterative toConstructorInitialization.)"
date: 2006-02-09T00:00:00
tags: ["api design"]
url: https://martinfowler.com/bliki/ConstructorInitialization.html
slug: ConstructorInitialization
word_count: 430
---


Constructor initialization is an approach where you pass in all
	the collaborators that the object needs in the creation method of
	the object. It is an alternative to
	[SetterInitialization](https://martinfowler.com/bliki/SetterInitialization.html).


So to create a person with firstname, lastname, and a
	collection of favorite bars we might see something like


```

# ruby
mf = Person.new('martin', 'fowler', 
                ['Turners Oyster Bar', 'Square and Compass'])

```


By doing this you are always sure you have an object in a
	reasonably well-formed state that's ready to be used. It's also a nicely
	compact approach, allowing you to get the object going in one
	line. If you only want to do one thing with the object, you can also
	assign it or call a method on it in that single line, which means
	you don't need a variable lying around.


Declaring all the necessary collaborators in the constructor
	makes it clear which collaborators are needed, making it easier to
	see how to get the class going. You'll need one constructor method
	for each valid combination of mandatory collaborators. It's usually
	handy to provide constructors that include commonly needed optional
	collaborators too.


This approach makes it easy to see the difference between
	immutable and updatable attributes as immutable attributes don't
	have a setting method, they are just initialized in the construction
	method.


Constructor Initialization is my first choice. There are cases
	when it's difficult to set things up this way and I do occasionally
	prefer setter initialization, but most of the time constructor
	initialization is the best bet.


## Common Issues


*What if there's lots of different legal combinations for a
		new object?* Often people get worried that there will be a
		gazillion constructor methods if you use this approach. Most of
		the time, this isn't an issue - there's only a few. You only
		really need the mandatory collaborators here, and there's hardly
		ever more than a handful of combinations of them.


*What if there's a lot of collaborators to provide in the
constructor?* A large list of construction parameters, like any
large parameter list, is a [CodeSmell](https://martinfowler.com/bliki/CodeSmell.html). Usually when I see these I find that many of the parameters
are [DataClump](https://martinfowler.com/bliki/DataClump.html)s and should be replaced by their own object. Having said that it's not unusual for constructor methods to
have more parameters than other methods - but they are a good place to
spot data clumps.


*How does this square with
		[ContextualValidation](https://martinfowler.com/bliki/ContextualValidation.html)?* The context here is basic
		usage of the object - essentially a minimally useful state. This
		probably won't be valid for various other activities, but it
		should be valid enough to be useful.
