---
title: "Uml As Sketch"
description: "I draw a lot of UML diagrams, but I don't use CASE tools. The reason is that I'm interested inUmlAsSketch, not in all the repository stuff. So far my regular choice has been Visio. Although Visio come"
date: 2004-06-16T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/UmlAsSketch.html
slug: UmlAsSketch
word_count: 296
---


In this [UmlMode](https://martinfowler.com/bliki/UmlMode.html) developers use the UML to help communicate some
aspects of a system. As with blueprints you can use sketches a forward
engineering or reverse engineering direction. Forward-engineering
draws a UML diagram before you write code, while reverse-engineering
builds UML from existing code in order to help understand it.


The essence of sketching is selectivity. With forward sketching
you rough out some issues in code you are about to write, usually
discussing them with a group of people with your team. Your aim is to
use the sketches to help communicate ideas and alternatives about what
you're about to do. You don't talk about all the code you are going to
work on, just important issues that you want to run past your
colleagues first, or sections of the design that you want to visualize
before you begin programming. Sessions like this can be very short, a
ten minute session to discuss a few hours of programming or a day to
discuss a two week iteration.


With reverse engineering you use sketches to explain how some
part of a system works. You don't show every class, just those that
are interesting and worth talking about before you dig into the code.


Since sketching is pretty informal and dynamic you need to do
them quickly and collaboratively, so a common medium is a white board.
Sketches are also useful in documents, in which case the focus is
communication rather than completeness. The tools used for sketching
are lightweight drawing tools and often people aren't too particular
about keeping to every strict rule of the UML. Most UML diagrams shown
in books, such as mine, are sketches. Their emphasis is on
selective communication rather than complete specification. Hence my
sound-bite âcomprehensiveness is the enemy of comprehensibilityâ
