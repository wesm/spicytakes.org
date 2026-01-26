---
title: "Language Workbench"
description: "Language Workbench is a term I coined in 2005 to describe a new   class of software development tool, designed to build software   through a rich environment of multiple, integrated,DomainSpecificLang"
date: 2008-09-09T00:00:00
tags: ["domain specific language", "language workbench"]
url: https://martinfowler.com/bliki/LanguageWorkbench.html
slug: LanguageWorkbench
word_count: 372
---


Language Workbench is a term I coined in 2005 to describe a new
  class of software development tool, designed to build software
  through a rich environment of multiple, integrated,
  [DomainSpecificLanguages](https://martinfowler.com/bliki/DomainSpecificLanguage.html).  These tools are still quite a way
  away from being mainstream, but development on them continues and
  continues to be interesting. They are one of the few things I feel
  could significantly change the programming landscape.


Language workbenches support the idea of Language-Oriented
  Programming, which is the notion of building a sofware system by
  identifying the various areas of the system and using (perhaps
  building) a Domain Specific Language for each area. The workbench
  both supports the definition of these languages and also integrating
  them together into a coherent whole.


To define the DSLs the workbench supports:

- Defining the schema for a Semantic Model for the language
- Defining one or more rich editing environments for the language
- Defining the behaviorial semantics for the language, through
    some mix of interpretation and code generation.


The editing environments are what makes these tools stand
  out. People have been making external DSLs for decades, but you edit
  these in a text editor. language workbenches look to take this much
  further, approaching the level of modern [PostIntelliJ](https://martinfowler.com/bliki/PostIntelliJ.html) IDEs, or even
  beyond. Some language workbenches support editing in regular text,
  others use projectional editors that support structured text that
  needs no parsing, or diagrams, or both.


A particularly powerful style of editing is an environment that weaves example
  execution into the editor, a style that I like to call
  [IllustrativeProgramming](https://martinfowler.com/bliki/IllustrativeProgramming.html). The most common example of this is a spreadsheet.
  When you edit a spreadsheet, the primary thing you see isn't the formulae that
  represents the behavioral definition, instead you see numbers that are calculated from
  the formulae. The program and example data are woven together so as you edit the program
  you see the consequences immediately. This style of editing is startlingly different
  from our usual notions of a programming language, and could well be crucial to better
  engaging domain experts in sofware development.


In 2005 I wrote a  [set of
  papers](https://martinfowler.com/articles/languageWorkbench.html) on Language Workbenches. Some of these thoughts need to
  be revised, but for the moment they are the best deeper discussion
  on them.
