---
title: "One Language"
description: "Should we strive to only have one language in our 	development efforts?"
date: 2007-07-28T00:00:00
tags: ["programming environments"]
url: https://martinfowler.com/bliki/OneLanguage.html
slug: OneLanguage
word_count: 962
---


**Should we strive to only have one language in our
	development efforts?**


Throughout much of the last decade the fashion in the enterprise
	software world has been to focus on one standard language for
	software development efforts. Many development organizations strive
	to do all their work in Java (or C#/VB).


The rationale for this is that developers find it hard to be
	proficient in more than one language. Sticking to a single language
	lowers the learning burden, particularly when hiring new people.


There's some truth to this, but also much that's missing. The
	programming environment is partly language, but also about languages
	and frameworks. Larger frameworks, Hibernate, Struts, ADO, present
	as much of a challenge to learn as a language even if you program
	them in a single host language. Often the difficulty of expressing
	what you need in the host language is sufficiently awkward that many
	frameworks resort to configuration files, which are effectively
	external [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html)s written in XML - which
	adds a jigger of 80 proof ugliness to them.


For many developers, the one-language notion is a sign of lack of
	professionalism. This is best exemplified by the [Pragmatic
	Programmers'](http://www.pragmaticprogrammer.com/ppbook/index.shtml) advice to learn a new language every year. The point here
	is that programming languages do affect the way you think about
	programming, and learning new languages can do a lot to help you
	think about solving problems in different ways. (It's important to
	learn languages that are quite different in order to get the benefit
	of this. Java and C# are too similar to count.)


I agree with prags' advice here, as in most things. But I also
	sympathize with the overhead of learning a new language. My
	personal scripting is pretty much all done with Ruby and I've been
	loath to any more than play with reasonable alternatives like
	Python, Groovy, or PowerShell. It's not that it's hard to use the
	alternatives, but with Ruby I know too much that I'd have to look up
	with the alternatives.


The important point here is that when I'm writing these scripts
	I'm not manipulating new abstractions. Much of what I do is fiddling
	with text, the file system, and hunks of XML or YAML. If I need to
	take on a sizable new abstraction, the cost of learning it as a
	library isn't really much less than the cost of learning a language
	to manipulate it. If I want to specify a directed graph structure
	for display, learning [Graphviz's](http://www.graphviz.org/) Dot language is hardly more work than
	learning a new Ruby library.


Using a DSL instead of a library can offer us better ways of
	manipulating our abstractions. This makes it easier to see what
	we've written and to reveal our intentions. An API is like declaring
	a vocabulary, a DSL adds a grammar which allows you to write coherent
	sentences.


This argument is strong for DSLs, but does it also apply to
	general purpose languages? If you are working in Java (or soon C#) does it
	make sense to use Ruby now it's available on your platform?


The last decade has seen the rise of memory managed C-based
	languages. People saw that, despite many years of skepticism, memory
	management makes life sufficiently better that it was worth stepping
	away from C and C++ in the enterprise world. A common platform and
	language also pulled people away from proprietary walled gardens like
	Powerbuilder and Delphi.


Now there is a similar question. Are modern scripting languages
	another step forwards? Do we prefer their well-chosen terseness?
	Time and time again I hear experienced Java and C# developers report
	they are more effective in Ruby - which is why I've been encouraging
	 Ruby. It wouldn't surprise me if similar reports appear in the
	next few years about other languages too.


A decade ago I was talking to my old friend Tom Hadfield at
OOPSLA 96. Java's rise was apparent and it was clear that Smalltalk's
future was doomed. Despite my love of Smalltalk I was pretty sanguine.
I felt that Java gave people enough of what they needed; while it
wasn't quite as nice as Smalltalk it was enough of an improvement over
C++, particularly with memory management, for me to be happy with it.
Tom disagreed, he felt there was something fundamentally different
about the expressiveness of Smalltalk, the way you could better
capture the intention of what you were doing directly in your code -
closing the gap between domain knowledge and programming.


In the intervening years I've come to the view that Tom was right
	after all. After several years in curly brace land, Ruby reminded me
	of what I was missing. There's a clarity to reading Ruby code that
	just makes it an easier medium to work with, despite the inferior
	tooling. I'm way more sympathetic to the Smalltalk holdouts than I
	felt then, even though I haven't felt inclined to open an image in anger for a
	long time.


So are we returning to the language cacophony of the late 80's
	and early 90's? I think we will see multiple languages blathering
	away, but there will be an important difference. In the late 80's it
	was hard to get languages to inter-operate closely. These days
	there's a lot of attention to making environments that allow
	different language to co-exist closely. Scripting languages have
	traditionally had an intimate relationship with C. There's much
	effort to inter-operation on the JVM and CLR platforms. Too much has
	been invested in libraries for a language to ignore them.


So my sense is that we will see multiple languages used in
	projects with people choosing a language for what it can do in the
	same way that people choose frameworks now. I agree with Neal that
	we are entering a period of [Polyglot Programming](http://memeagora.blogspot.com/2006/12/polyglot-programming.html).
