---
title: "Annotation"
description: "An annotation on a program element (commonly a class, method, or field) is a piece of meta-data added to that program element which can be used to embellish that element with extra code."
date: 2005-08-12T00:00:00
tags: ["language feature"]
url: https://martinfowler.com/bliki/Annotation.html
slug: Annotation
word_count: 181
---


An annotation on a program element (commonly a class, method, or
field) is a piece of meta-data added to that program element which can
be used to embellish that element with extra code.


In **Java** this is called an **annotation**, in **C#**
	this is called an **attribute**. C# has had them since its first
	release, in Java they appeared with version 1.5.


A good example of an attribute is the [Obsolete] attribute in C#
	to mark elements that are going out of service (the same as
	deprecated in Java). The Obsolete attribute can take arguments to
	print messages and to indicate if using the element is an error or a
	warning. The language platform comes with many
	annotations defined, but allows you to add your own annotations.


When writing about programming, I prefer to use 'annotation' as the
	general term. Although .NET was first, the word 'attribute' is
	just too widely used for different things.


Languages may provide annotations in ways that don't reflect the syntax of the
  language, for example [RubyAnnotations](https://martinfowler.com/bliki/RubyAnnotations.html) are very common - but done with class
  methods.
