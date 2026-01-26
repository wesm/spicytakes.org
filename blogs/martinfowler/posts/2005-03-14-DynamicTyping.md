---
title: "Dynamic Typing"
description: "I've long been loath to write any contributions on the debate 	between static and dynamic typing in programming languages. This is 	one of those emotive topics where people seem driven to debate 	rath"
date: 2005-03-14T00:00:00
tags: ["language feature", "ruby"]
url: https://martinfowler.com/bliki/DynamicTyping.html
slug: DynamicTyping
word_count: 703
---


I've long been loath to write any contributions on the debate
	between static and dynamic typing in programming languages. This is
	one of those emotive topics where people seem driven to debate
	rather than listen. But since I've been asked a few times about it,
	I will contribute my personal experiences. I'm not trying to
	convince anyone of anything, but I hope someone finds some food for
	thought in them.


When I first conscious of the distinction I was quickly convinced
	by the advantages of static typing. My early experiences of
	programming were in Basic and Fortran IV - where the typing was
	limited. I then moved to Pascal and that quickly became a language I
	enjoyed programming in.


When I got into objects I worked in both C++ and Smalltalk. For
	quite a while I saw Smalltalk's dynamic typing as a disadvantage - a
	small
	price to pay for the otherwise wonderful productivity of the platform.


I really began to question this when I got involved with some
	moderately sized Smalltalk projects. The general argument for static
	types is that it catches bugs that are otherwise hard to find. But I
	discovered that in the presence of [SelfTestingCode](https://martinfowler.com/bliki/SelfTestingCode.html), most bugs that
	static types would have were found just as easily by the
	tests. Since the tests found much more than type errors, you needed
	them in either a static or dynamically typed language, so having the
	static typing gave you little gain.


It's been interesting to see others follow this line of
	discovery. Both Robert Martin and Bruce Eckel have found the same
	thing coming from C++ to Python.


However catching bugs isn't the only benefit to static typing,
	and it's some of the others that I find more noticeable these days.


One day I found myself trying to follow some well-written Ruby
	code. I found the lack of type information on parameters made life
	difficult - I kept saying to myself 'what exactly do I have here?' I
	didn't find this so much of an issue in Smalltalk for two reasons:
	the excellent environment makes it easy to fire up a debugger and
	see what you have, and secondly the common convention is to name the
	arguments after the type. (This makes sense because Smalltalk has
	keyword parameters rather than positional parameters, so the keyword
	explains the role the parameter plays.)


Another area where static typing is useful is that it allows
	programming environments to be much more helpful. The revelation
	here (as in so many things) was IntelliJ. With an IDE like this I
	really felt the type system was helping me. Even simple things like
	auto-completion are greatly helped by static types, and leading IDEs
	can do much more than that.


Despite this, there's still something particularly satisfying
	about programming in languages like Smalltalk and Ruby - and I think
	it has a great deal to do with the dynamic typing. Chatting at Camp
	4 Coffee with Bruce Eckel we both agreed that one of the most
	frustrating things about the static/dynamic typing debate is that
	it's very hard to put into words the advantages of working in a
	dynamically typed language. Somehow things just seem to flow better
	when you're programming in that environment, even when I'm doing my
	Ruby in emacs instead of IntelliJ. (Smalltalk, of course, has both
	the language and a lovely programming environment.)


I suspect part of this is that the conciseness of the language
	allows such things as doing a [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html) in
	the language. Working with languages such as Java and C# I always
	feel the need to skip over text in order to understand what's going
	on.


Whatever the reason, this better flow leads to more fun
	programming - even with an inferior environment. This may not seem
	to matter much, who cares if programmers have fun? But I do care
	because I really enjoy programming. I enjoy doing things quickly
	without having to futz around on guff that gets between my thinking
	and running code. For me that's the pleasure of Smalltalk and Ruby
	and why I reach for these on any personal projects. And there's
	business value in fun - after all motivation is a major
	factor in programmer productivity.
