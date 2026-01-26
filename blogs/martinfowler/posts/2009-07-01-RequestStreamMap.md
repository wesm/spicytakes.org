---
title: "Request Stream Map"
description: "Hang around my colleagues at Thoughtworks and you soon get the   impression that the only good Enterprise Service Bus (ESB) is a dead   ESB. Jim Webber refers to them as Erroneous Spaghetti Boxes. So "
date: 2009-07-01T00:00:00
tags: ["application architecture"]
url: https://martinfowler.com/bliki/RequestStreamMap.html
slug: RequestStreamMap
word_count: 309
---


Hang around my colleagues at Thoughtworks and you soon get the
  impression that the only good Enterprise Service Bus (ESB) is a dead
  ESB. Jim Webber refers to them as Erroneous Spaghetti Boxes. So it's
  not uncommon to hear tales of attempts to get them out of systems
  that don't need them.


Battle was joined at one client and it brought to mind my younger
  days playing D&D. Webber swings but misses as the ESB is AC 2,
  Evan gets a hit and rolls 2d8 for 6 damage. Erik finally kills it
  by casting â[Summon Request Stream Map](http://erik.doernenburg.com/2009/07/making-esb-pain-visible/)â.


So what was Erik Dörnenburg's
  decisive spell? Essentially the idea was to take a simple request
  and show how the data for the request and response made their way
  through the layers of the application. Erik printed out all the code
  that you needed to read to understand how this would work - which
  ran to several pages. He also produced this diagram.


![](images/requestStreamMap/low-level-esb-600x533.png)


It's currently fashionable in agile circles to do Value Stream
  Mapping as a way to uncover waste in a software development
  process. I think of this as a request stream map because it similarly
  takes a request and shows how it moves through the layers allowing
  us to visualize what's going on and think about the cost and value of
  the layers.


Layering is an essential tool for building software
  applications. But like most essential things in life, excess can
  be almost as much of a problem as too little. A visualization like
  this (or the multiple pages of code) can help you find where âjust
  enoughâ is.


One hazard, however. If you do need to transform data from one
  form to another, it's usually better to a few little
  transformations than one big transformation. You want to avoid
  unnecessary transformations not compress the ones you need.
