---
title: "Dsl Exceptionalism"
description: "One of the tricky things about writing about externalDomainSpecificLanguagesis that I'm walking through   territory already heavily tracked by the programming languages   community. Programming langua"
date: 2008-12-22T00:00:00
tags: ["domain specific language"]
url: https://martinfowler.com/bliki/DslExceptionalism.html
slug: DslExceptionalism
word_count: 785
---


One of the tricky things about writing about external
  [DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html) is that I'm walking through
  territory already heavily tracked by the programming languages
  community. Programming language research has always been a popular
  area of academic activity, and I'm the first to admit that I don't
  have anywhere near the depth in this topic as many people who've
  been studying in this space for years. So inevitably the question
  comes up as to why such a noob as me thinks he can write a book in
  this well trodden ground?


The primary reason is that nobody else has written a
  practitioner-oriented book on DSLs. I like topics like this that are
  well-trodden but not well written about. However as I've spent time
  walking these pathways I think there's another factor in the
  works.


There's a lot of work on programming languages out there, but
  almost all of it has concentrated on general purpose programming
  languages. DSLs are seen as a small and simple subset of general
  purpose programming thinking. As a result people think that what's
  true for general purpose languages is also true for DSLs (with the
  implication that DSLs are too small to be worth thinking much about).


I'm increasingly of the opposite conclusion. The rules for DSLs
  are different to the rules for general purpose languages - and this
  applies on multiple dimensions.


The first is in language design. I was talking with a language
  designer who I have a lot of respect for, and he stressed that a key
  feature of languages was the ability to define new
  abstractions. With DSLs I don't think this is the case. In most DSLs
  the DSL chooses the abstraction you work with, if you want different
  abstractions you use a different DSL (or maybe extend the DSL you're
  using). Sometimes there's a role for new abstractions, but those
  cases are the minority and when they do happen the abstractions are
  limited. Indeed I think the lack of ability to define new
  abstractions is one of the things that distinguishes DSLs from
  general purpose languages.


Differences also occur in the approach that you use for
   implementing the tools that go with languages. A constant issue for
   general purpose languages is dealing with large inputs, since
   realistic programs will have thousands or millions of lines of
   code. As a result many tools and techniques for using them involve
   aspects that make parsing harder to follow but support these large
   inputs. DSL scripts tend to be much smaller, so these trade-offs
   work differently.


In my work I've put a lot of emphasis on using a DSL to populate
   a [Semantic
   Model](https://martinfowler.com/dslwip/SemanticModel.html), using that model as the basis for any further
   processing: interpretation, visualization, or code generation. Lots
   of language writing I've seen tend to emphasize code generation,
   often generating code directly from the grammar file. Intermediate
   representations are not talked about much, and when they do appear
   they more in the form of an Abstract Syntax Tree rather than a
   semantic model. Serious compilers do use intermediate
   representations, such as program dependence graphs, but these are
   seen (rightly) as advanced topics. I think Semantic Models are a
   really valuable tool in simplifying the use of a DSL, allowing you
   to separate the parsing from the semantics.


Since DSLs are less expressive, you can
  design a simpler language for them.  Much of the language community's writing
  talks about how to handle the difficulties of a complex general
  purpose language, while the challenge of DSLS is to write a language
  that is readable to the intended audience (which may well include
  non-programmers) and also should be easy to parse (to simplify the
  maintenance of the parser). Not just does this lead to different
  decisions on the design of a language, it also means that you only
  really need a subset of the features of parser generators.


A consequence of this is DSLs are written with the expectation
  that each individual DSL won't solve the whole problem at hand and
  often you need to combine DSLs. Traditional language thinking hasn't
  explored the idea of composable languages that much, but I think
  this topic is very important as DSLs develop. Thinking about
  composable languages should have significant effects on both language
  design and language tools.


So I'm increasingly coming around to the thinking that DSLs
  inspire some seriously different ways of thinking about programming
  languages. It may also lead to developing different kinds of parsing
  tools that are more suited for DSL work - usually tools that are
  simpler. I hope the increased attention that DSLs are getting these
  days will lead to more people treating DSLs as first class subjects
  of study rather than a simplistic form of general purpose languages.
