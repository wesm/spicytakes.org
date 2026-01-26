---
title: "Embedment Helper"
description: "In recent weeks I've been playing with, and looking at, 	compiler-compiler tools. A common feature of these tools is that 	they have a grammar file whose core is a description of the 	production rules"
date: 2007-03-26T00:00:00
tags: ["web development", "domain specific language"]
url: https://martinfowler.com/bliki/EmbedmentHelper.html
slug: EmbedmentHelper
word_count: 590
---


In recent weeks I've been playing with, and looking at,
	compiler-compiler tools. A common feature of these tools is that
	they have a grammar file whose core is a description of the
	production rules of a grammar for a language. As well as describing
	the grammar, the file also provides information to the parser about
	how to process the language as it recognizes the language
	elements. In most compiler-compiler tools these instructions are
	represented as actions in the grammar - often these actions are
	encoded as as fragments of code in a high level language.


For example in my [HelloAntlr](https://martinfowler.com/bliki/HelloAntlr.html) example you see bits of
	embedded Java to create and populate a configuration from the source
	file. (Embedding Java isn't the only approach, tree walking is another.)


This approach of embedding a General Purpose Language (GPL) inside
	another Domain Specific Language (DSL) is quite common. Most readers
	here will have come across it when creating HTML pages using
	templating systems like Velocity, JSP, ERBs and the like. Again we
	have a different representation (HTML) where we can embed fragments
	of a GPL to provide dynamic data and more complex processing.


When I'm working in an environment like this, I like to minimize
	the amount of Java (or whatever GPL I'm using) in my templates. A
	common technique for this is to create a separate helper class in
	Java and ensure that all the embedded Java in the template does is
	make simple method calls to this helper.


The main reason I like to do this is because I believe that if you
	embed large amounts of a GPL in a DSL, you end up obscuring the flow
	of the DSL. The whole point of using a template language for HTML is
	to concentrate on the HTML, so every bit of Java you stick in there
	gets in the way. This is especially true for grammar files where
	lots of code in actions makes it hard to understand the productions.


A further benefit of using an embedment helper is that it makes
	it easier for tools to do their job. Whether it's just syntax
	highlighting, or the full power of a [PostIntelliJ](https://martinfowler.com/bliki/PostIntelliJ.html) IDE,
	these tools often don't work well with mixed language
	files. AntlrWorks, for example, will highlight and offer completion
	on Antlr's grammar, but embedded Java is just plain text.


When using a helper like this, my normal style is to include code
	early on in the host (DSL) file to set up the helper. Usually this involves declaring a
	field in the host and either constructing a new helper in
	there, or making it so a caller can pass a helper in. (I confess I'm
	happy to use a public field in my Antlr grammar for this.) After
	that all the embedded Java in the host is a simple call on the
	helper. I name these calls from the perspective of the host file,
	to indicate what's wanted from the helper.


The helper and the host files are very tightly coupled together,
	usually with a bi-directional link between them and plenty of back
	and forth. The helper knows all sorts of grubby details about the
	host - I'm happy for an HTML helper to spit out HTML and grammar
	helpers will poke around the parse tree.


Usually I treat the word âhelperâ on a class as a red flag as it
	usually indicates a poorly thought out abstraction. Here I'm happy
	to use the word, since the helper is really only there as a support
	to the host file.
