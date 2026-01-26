---
title: "Parser Fear"
description: "I talk quite a bit with people aboutDomainSpecificLanguagesthese days and a common reaction I get to external DSLs is that it's 	hard to write a parser. Indeed one of the justifications for using 	XML"
date: 2008-05-20T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/ParserFear.html
slug: ParserFear
word_count: 1314
---


I talk quite a bit with people about [DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html)
	these days and a common reaction I get to external DSLs is that it's
	hard to write a parser. Indeed one of the justifications for using
	XML as the carrier syntax for an external DSL is that âyou get the
	parser for freeâ. This doesn't jive with my experience - I think
	parsers are much easier to write than most people think, and they
	aren't really any harder than parsing XML.


I even have evidence. Well it's actually only one case, but I'll
	quote it anyway as it supports my argument. When I wrote the [introductory
	example](https://martinfowler.com/dslwip/Intro.html) for my book I developed multiple external DSLs to
	populate a simple state machine. One of these was using XML (using
	it as a gateway drug) another was a custom syntax which I parsed
	with the help of [Antlr](http://www.antlr.org/). Writing
	the code to fully parse these formats took about the same amount of
	time.


Although you get an XML parser for free (I used Elliotte Rusty Harold's
	excellent [XOM](http://www.xom.nu/) framework) the output of an XML parser is effectively
	a parse tree in the form of an XML DOM. In order to do anything
	useful with that you have to process it
	further. My practice with DSLs to is base them around a clear
	[Semantic
	Model](https://martinfowler.com/dslwip/SemanticModel.html), so the true output of parsing in this case is a populated
	state machine model. In order to do this I have to write code that
	walks its way through the XML DOM. This isn't especially difficult,
	particularly since I can use XPath expressions to pick out the bits
	of the DOM I'm interested in. Indeed I'm not walking the DOM tree at
	all - for each thing I'm interested in I have a method that issues
	an XPath query, iterates through the resulting nodes and populates the
	state machine model.


So the XML processing is easy, but it isn't non existent - around
	a hundred lines of code. It took me a couple of hours. I hadn't used
	XOM in a while, so there was some familiarization required, but
	it's a very easy library to learn and use.


The Antlr processing was remarkably similar. Antlr has a notation
	that allows you to put some simple rules in the grammar file to
	populate an AST. The code to process the AST and populate the
	semantic model was very similar to the XML code - query for the
	right nodes in the tree and then process them. Including the grammar
	file the resulting code is around 250 lines, but took me about the
	same amount of time to write. I was familiar with most of Antlr
	before this, having used it a few times, but I hadn't actually used
	the tree construction stuff before. (If you're interested you can
	find [a description of this example](https://martinfowler.com/dslwip/TreeConstruction.html) in my book's work in progress.)


Although my explorations of parser generators have got me used to
	the fact that they are much easier to write than many people think,
	I was surprised when I realized it was actually no slower than the
	XML case. In a more carefully controlled example, I would still
	expect it to take longer because I did the Antlr example second and as
	any programmer knows, things always go much faster with a second
	implementation. Even so, the difference is much less than what many
	people seem to expect - when the word âparserâ seems to mean âtoo
	complicatedâ.


I can't deny there is certainly a learning curve to get used to
	parser generators. You have to get used to grammar files and how
	they interact with code samples. There's different strategies you
	can use (what I currently refer to as Tree Construction, Embedded
	Translation and Embedded Interpretation). You also have to think
	about the syntax of your custom syntax, which involves more decisions
	than wondering whether to make something an attribute or an element
	in XML. But that curve isn't really that high. Modern tools make it
	much easier. Antlr is my current default choice, it comes with a
	very nice IDE which helps in exploring grammar expressions and
	seeing how they get parsed into an AST. But once you've got used to
	how one parser generator works, it's not hard to pick up others.


So why is there an unreasonable fear of writing parsers for DSLs?
	I think it boils down to two main reasons.

- You didn't do the compiler class at university and therefore
think parsers are scary.
- You *did* do the compiler class at university and are therefore
convinced that parsers are scary.


The first is easy to understand, people are naturally nervous of
things they don't know about. The second reason is the one that's
interesting. What this boils down to is how people come across parsing
in universities. Parsing is usually only taught in a compiler class,
where the context is to parse a full general purpose
language. Parsing a general purpose language is much harder than
parsing a Domain Specific Language, if nothing else because the
grammar will be much bigger and often contain nasty wrinkles which you
can avoid with a DSL.


This problem is compounded by encouraging code that
tangles up parsing with output processing and code generation. For me
the key to keeping things straight is to use a Semantic Model, so that
your parser does no more than populate that model. Most of the time I
can then do what I need by just executing that semantic model like any
other OO framework. Most of the time I don't need to do code
generation, and when I do I base it off the semantic model so it's
independent of the parser. I think that if you've got code generation
statements inside your grammars, things are way too coupled together.


For people to work effectively with external DSLs they have to be
taught about it quite differently to how you'd teach parsing a general
purpose language. The small size of both the language and the scripts
in the language changes many of the concerns that people typically
have with parsing. Avoiding code generation unless you really need it
can remove a big hunk of the complexity. Using a clear semantic model
can separate out the steps into much more tractable chunks.


The problem, of course, is that there isn't much written that
follows these guidelines. (Which is one of the triggers for me to be
spending so much time on it.) You're hard put to find any
documentation out there on parser generator tools. When you do get
some really nice documentation (like Terence Parr's [Antlr book](https://www.amazon.com/gp/product/0978739256/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0978739256&linkCode=as2&tag=martinfowlerc-20)) it's still usually written
with a general purpose language mindset. Don't get me wrong, I find the
Antlr book very helpful (it's a big reason why Antlr is my default
choice of parser generator) but I believe that there's an assumption
there of parsing general purpose languages rather than domain specific
languages that makes it harder to approach than it could be.


The nice thing, however, with all this is that you can still mount
that learning curve. If you haven't tried working with a parser
generator I'd certainly suggest giving it a try. Try writing a simple
DSL of your own. Don't worry about code generation when you start,
just create a domain model as you normally would and get the DSL to
populate it. Start with something really silly (like I did with
[HelloAntlr](https://martinfowler.com/bliki/HelloAntlr.html)) and gradually work it up from there. Poke
around some open source projects that use a DSL and see what they
do.


> What we're trying to do is introduce the tools that are often
> used in compilers but are much more general than that to an audience
> that associates the tools only with compilers, because that's how
> they've always been taught.
> -- Rebecca Parsons
