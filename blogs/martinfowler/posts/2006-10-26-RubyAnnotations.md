---
title: "Ruby Annotations"
description: "One of Ruby's most popular features is its support formetaprogramming, that is features that act like they change the 	language itself - introducing things like new keywords."
date: 2006-10-26T00:00:00
tags: ["language feature", "domain specific language", "ruby"]
url: https://martinfowler.com/bliki/RubyAnnotations.html
slug: RubyAnnotations
word_count: 629
---


One of Ruby's most popular features is its support for
	[metaprogramming](http://ola-bini.blogspot.com/2006/09/ruby-metaprogramming-techniques.html), that is features that act like they change the
	language itself - introducing things like new keywords.


Although the mainstream curly-brace languages have less support
	for metaprogramming in general, one useful feature they do have is
	[Annotation](https://martinfowler.com/bliki/Annotation.html)s. Annotations are an important capability for
	the language enhancement [InternalDslStyle](https://martinfowler.com/bliki/InternalDslStyle.html). At first
	glance Ruby doesn't support annotations, but if tilt your head
	you'll find it does.


With annotations you tag a language element (class, method, field
	etc) with a marker - essentially metadata about that element. You
	can then use that metadata at runtime or compile time.


A good example of this is marking of tests that was pioneered by NUnit2.


```
[Test] public void SomeTestMethod() {...
```


At run time the NUnit framework looks at classes, finds the
	methods annotated with `[Test]` and runs them.


Annotations can take parameters. So if you have a hankering for
	the subranges of Pascal, which allow you to indicate a valid range
	for a variable, you define them with something like this


```
  
@ValidRange(lower = 1, upper = 1000)
  private int weight; // in lb
  @ValidRange(lower = 1, upper = 120)
  private int height; // in inches

```


This isn't quite the same as the Pascal subrange idea, this only
	defines the valid range, you still have to build the mechanism to
	check the value, such as calling an `isValid` method on
	your object (I agree that's not much of a
	[ContextualValidation](https://martinfowler.com/bliki/ContextualValidation.html)). But the key here is that you have
	defined your own declarative statement about that variable.


So how do you do this in Ruby? Something like this:


```

	validate_range :@height, :with => 1..120
	validate_range :@weight, :with => 1..1000

```


In terms of syntax, the big difference is that with Java (or
	.NET) annotations you place the annotation immediately before the
	element you're annotating. In ruby you name the element you're
	annotating in the annotation. Although this adds some typing (a rare
	statement for Ruby) it does give you the freedom to place your
	annotations anywhere in your class. It also makes it easier to
	construct annotations that reference more than one language element.


A deeper difference between the two styles is how they get
	implemented. Curly Brace annotations are a special language
	construct that attach special objects as metadata to language
	elements. These annotation objects can be queried and processed
	either at compile time (with Java's apt) or at runtime.


Ruby's annotations, on the other hand, are class methods usually
defined in a superclass or included module. By writing them directly
in the class definition they are executed when the class is loaded. As
a result they aren't a particular language feature, more of a way of
using class methods. You don't have to create metadata objects
(although you could if you wanted to), more likely you'll just build
the objects to carry out the task you want them to.


Due to Ruby's dynamic nature, you can do a lot more interesting
	things with annotations. In particular you can do code
	generation. The most obvious example of this is things like
	`attr_accessor :height` which will generate get and set
	methods for the field, effectively modifying the class itself. With
	apt Java can do some similar things, but you can't modify the class
	itself. With build scripts and partial classes you probably could do
	something like this in C#, but this kind of run-time code generation
	is certainly more natural in Ruby, it's one of its Lispish elements.


Rubyists don't call these things
	annotations. One of the things I like doing is to find common
	techniques that cross languages, for me this is a common technique
	and 'annotation' seems like a good generic word for it. I don't know
	if Rubyists will agree.
