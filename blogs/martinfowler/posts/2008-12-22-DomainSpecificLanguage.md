---
title: "Domain Specific Language"
description: "One of the tricky things about writing about externalDomainSpecificLanguagesis that I'm walking through   territory already heavily tracked by the programming languages   community. Programming langua"
date: 2008-12-22T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/DomainSpecificLanguage.html
slug: DomainSpecificLanguage
word_count: 337
---


The basic idea of a Domain-Specific Language (DSL) is a computer
		language that's targeted to a particular kind of problem, rather
		than a general purpose language that's aimed at any kind of
		software problem. Domain-specific languages have been talked
		about, and used for almost as long as computing has been done.


DSLs are very common in computing: examples include CSS,
	regular expressions, make, rake, ant, SQL, HQL, many bits of Rails,
	expectations in JMock, graphviz's dot language, FIT, strut's
	configuration file....


An important and useful distinction I make is between internal
	and external DSLs. **Internal DSLs** are particular ways of using
	a host language to give the host language the feel of a particular
	language. This approach has recently been popularized by the Ruby
	community although it's had a long heritage in other languages - in
	particular Lisp. Although it's usually easier in low-ceremony
	languages like that, you can do effective internal DSLs in more
	mainstream languages like Java and C#. Internal DSLs are also
	referred to as embedded DSLs or [FluentInterfaces](https://martinfowler.com/bliki/FluentInterface.html)


**External DSLs** have their own custom syntax and you write
	a full parser to process them. There is a very strong tradition of
	doing this in the Unix community. Many XML configurations have ended
	up as external DSLs, although XML's syntax is badly suited to this
	purpose.


The most most common DSLs in the wild today are textual, but you
	can have graphical DSLs too. Graphical DSLs requires a tool along the
	lines of a [Language
	Workbench](https://martinfowler.com/articles/languageWorkbench.html). Language Workbenches are less common but many people
	think they have the potential to profoundly improve the way we do
	programming.


DSLs can be implemented either by interpretation or code
	generation. Interpretation (reading in the DSL script and executing
	it at run time) is usually easiest, but code-generation is sometimes
	essential. Usually the generated code is itself a high level
	language, such as Java or C.


I published [a
	book on DSLs](https://martinfowler.com/books/dsl.html) in late 2010. I have a [guide page](https://martinfowler.com/dsl.html) where I pull
	together my work on DSLs.
