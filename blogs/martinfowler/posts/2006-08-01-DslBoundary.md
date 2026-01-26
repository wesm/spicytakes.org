---
title: "Dsl Boundary"
description: "When the topic ofDomainSpecificLanguagecomes up, one of the 	common puzzles is exactly what is or isn't a DSL. The trouble is 	that there is no precise definition for a DSL and there is a large 	gray "
date: 2006-08-01T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/DslBoundary.html
slug: DslBoundary
word_count: 561
---


When the topic of [DomainSpecificLanguage](https://martinfowler.com/bliki/DomainSpecificLanguage.html) comes up, one of the
	common puzzles is exactly what is or isn't a DSL. The trouble is
	that there is no precise definition for a DSL and there is a large
	gray area between DSLs and other things.


For me, a key element is that DSLs are limited both in scope
	(they refer to a particular domain) and capability (they lack
	features that are basic for general purpose languages). As a result
	good DSLs are usually small and simple: hence terms like 'little
	languages' and 'mini-languages'.


For internal DSLs, the fuzzy boundary is what is an API and what
is a DSL. Fundamentally there is no difference, an internal DSL is
just an API with a fancy name (as the old Bell labs saying goes:
âlibrary design is language designâ). Despite this, however, I think
there is a different feel when you are working with an API that's
written with a DSL feel. Things like a [FluentInterface](https://martinfowler.com/bliki/FluentInterface.html) can
make working with an API a qualitatively different experience. Thinking
in DSL terms makes you think about readability in a different way,
exploiting the syntax of the host language to create something that
seems to stand on its own - [rake](https://martinfowler.com/articles/rake.html) is a
great example of this.


When it comes to external DSLs the question often comes in the
	form of what the difference is between a DSL and a general purpose
	language (GPL). Often a clear sign is when the DSL isn't Turing
	complete or lacks abstraction facilities. Regexps are a fine example
	of this limitation in capability. SQL is a more interesting candidate. It's a complex and capable
	language, yet lacks both Turing completeness and the ability to
	build new abstractions.


Can a language be Turing complete and still be a DSL? [Ploticus's](http://ploticus.sourceforge.net)
	script language is Turing complete, but it's clear focus on
	producing graphs within Ploticus makes it a DSL - at least for
	me. But then what about XSLT? It too has a limited focus on
	transforming XML documents, yet it has gained so many capabilities
	that increasingly people think of it as a GPL.


The example of Ploticus raises the question of whether embedded
	languages are DSLs. Is Excel's macro language a DSL when it's
	virtually the same as Visual Basic? What happens if you embed a general
	scripting language into an application?


As with the internal DSL vs API issue, I think the intention is
	 the key here, both of the language writer and of the
	user. If I use XSLT only to transform an XML document then I'm
	treating it as a DSL - even if I do some fancy call out to embed
	some value in the output document. However if I use it to solve the
	eight queens puzzle I'm using it as a GPL. If the designers of XSLT
	see it as about XML transformations then they are thinking of it as
	a DSL even if clever people do unnatural acts with it.


This is one of those discussions are interesting ones to have in the
	pub but shouldn't detract from the good ideas in using
	DSLs. DSLs should be designed as used to be a limited language
	tightly focused on a single problem. If you go into their design and
	use with that idea foremost, they'll be useful. And after all it's
	usefulness that really counts.
