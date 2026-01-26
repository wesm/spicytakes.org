---
title: "Code Examples"
description: "I write about design, and it's my view that even when you are 	discussing somewhat abstract design patterns it's useful to provide 	source code examples. Of course this can lead to people thinking 	th"
date: 2004-03-11T00:00:00
tags: ["writing"]
url: https://martinfowler.com/bliki/CodeExamples.html
slug: CodeExamples
word_count: 633
---


I write about design, and it's my view that even when you are
	discussing somewhat abstract design patterns it's useful to provide
	source code examples. Of course this can lead to people thinking
	that the code example is the pattern, but I think that risk is
	outweighed by the precision that code provides. Several times I'm
	not quite sure about an idea but a code example helps to clarify it
	for me. So in my writing on design I always try to provide code examples.


There are several ways of doing code examples. Many readers like
complete examples that show how multiple ideas interconnect. I take a
different route. I prefer very small focused examples that show only
one idea at a time.


The problem with realistic examples that show multiple concepts
	is that they are hard to understand because you have understand all
	the concepts to get the example. With a focused example you can
	concentrate on one thing only. However with a focused example you
	don't see how the concepts fit together. Ideally you should provide
	both focused examples for the pieces and interconnected examples to
	show how they fit together. I confess I don't have the energy to do
	both, so I only show the focused examples. I reason that people have
	an easier job of fitting together examples once they have the basic
	patterns down. Also other authors can build on my stuff and provide
	interconnected examples. (Interconnected examples are a step harder
	due to the fact that I like show alternative patterns, so that leads
	to more interconnection combinations to show in a larger example.)


One of the tricks of the focused examples is to keep attention on
	the point of the example. So one of the things I do is to keep
	everything else simple and out of the way, which means I avoid using
	other patterns if they are likely to cloud understanding of the core
	issue, even if you'd use those patterns in a real system. An example
	of this is in the object-relational mapping patterns in [P of EAA](https://martinfowler.com/books/eaa.html). I
	show a lot of mapping patterns (such as Foreign Key Mapping) where I
	hard code the data transfer between objects and database. But in
	many realistic systems (and certainly in OR tools) you would not
	hard-code those transfers, instead you would use Metadata
	Mapping. I show them as hard coded transfers because I think that
	makes it easier to understand what's going on, and also allows you
	to understand Foreign Key Mapping without having to understand
	Metadata Mapping.


Another consequence of keeping things simple is ignoring edge
  cases which ought to have error handling in real code. I feel
  slightly awkward about this, there's a tension here between keeping
  example code simple and ensuring that example code shows good
  habits.


This relates to why I don't provide code samples for download.
I avoid downloads because the code examples I use
contain lots of string and duct tape in the areas outside the pattern.
Such things as generating ids for inserts from a static field - which
you must *never* do in a real system. I do it because it easier
for my simple examples, and I don't show people the scaffolding in the
book.


It's also true that downloading the code
	misses the point. The point of the code examples is the ideas that
	the code expresses not the code itself. You have to read it to
	understand, you can't just throw it into an application of your own.
	One advantage of a code download is that you can step through it to
	help understand how it works. That's a valid point, but the duct
	tape rather spoils this effect. I think downloaded examples work
	better for an interconnected example than for focused examples.
