---
title: "Internal Dsl Style"
description: "An internal DSL (often called an Embedded DSL) is aDomainSpecificLanguagethat is written 	inside an existing host language. It's a common way of thinking in 	a number of programming language communiti"
date: 2006-10-24T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/InternalDslStyle.html
slug: InternalDslStyle
word_count: 345
---


An internal DSL (often called an Embedded DSL) is a [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html) that is written
	inside an existing host language. It's a common way of thinking in
	a number of programming language communities - particularly the Lisp
	community. It's now gaining a lot of attention as DSLs are a common
	way of thinking in the rapidly growing Ruby community.


When people talk about internal DSLs I see two styles: internal
minilanguages and language enhancements.


An internal minilanguage is really using an internal DSL to do
	the same thing as you would with an external DSL. You consciously
	decide to use a subset of the full GPL for a minilanguage section of
	your program. It might look something like this (example from my 
	[Language Workbench](https://martinfowler.com/articles/languageWorkbench.html) paper)


```

mapping('SVCL', ServiceCall) do
  extract 4..18, 'customer_name'
  extract 19..23, 'customer_ID'
  extract 24..27, 'call_type_code'
  extract 28..35, 'date_of_call_string'
end
mapping('USGE', Usage) do
  extract 9..22, 'customer_name'
  extract 4..8, 'customer_ID'
  extract 30..30, 'cycle'
  extract 31..36, 'read_date'
end

```


This is all valid ruby, but its use of a subset of ruby makes it
	seem almost like a custom DSL.


Unlike an external DSL you are limited by the syntax
	and programming model of your host language, but you don't need to
	bother with building a parser. You're also able to use the host
	language features in complicated cases should you need to.


The alternative way of using internal DSLs is quite different to
	anything you might do with an external DSL. This is where you are
	using DSL techniques to enhance the host language. A good example of
	this is many of the facilities of Ruby on Rails. Look at these bits
	of Rails validation


```

validates_numericality_of :age
validates_uniqueness_of :ssn
validates_format_of :length, :with => /^\d+(in|cm)/

```


Reading these bits of Rails's validation, it looks like we've
	given the ruby language new keywords. Of course we haven't modified
	ruby, this is all clever [metaprogramming](http://ola-bini.blogspot.com/2006/09/ruby-metaprogramming-techniques.html). But it feels like we've
	enhanced the ruby language.


These are both very useful techniques. As with any classification
	there's a fuzzy line between them (Rake could be thought of either way.)
