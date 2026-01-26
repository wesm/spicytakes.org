---
title: "Observed Requirement"
description: "Requirements are the 	things that you should discover before starting to build your 	product. Discovering the requirements during construction, or worse, 	when you client starts using your product, is"
date: 2008-09-16T00:00:00
tags: ["requirements analysis"]
url: https://martinfowler.com/bliki/ObservedRequirement.html
slug: ObservedRequirement
word_count: 473
---


Here's one of my favorite software development quotes:


> Requirements are the
> 	things that you should discover before starting to build your
> 	product. Discovering the requirements during construction, or worse,
> 	when you client starts using your product, is so expensive and so
> 	inefficient, that we will assume that no right-thinking person would
> 	do it, and will not mention it again.
> -- Suzanne and James Robertson


It's the opening paragraph of the first edition of their book
	âMastering the Requirements Processâ. As regular readers might
	guess, my liking isn't connected to agreement. I like this quote
	because it sums up the waterfall value system to requirements
	(indeed the word 'requirement' is inherently waterfallish).


Agile methods violate this underlying assumption by intending to
	discover the 'requirements' during construction and after 
	delivery. But even this cavalier disregard of the above sage advice is nothing
	compared to what many leading web sites do these days. These sites explore
	requirements by observing what the users do on their sites and using
	that information to generate ideas for new features along the
	following lines:

- Look at what
	people are trying to do with the site and provide easier ways for
	them to do it.
- Look at where people are abandoning doing something, and look for
	ways to fix whatever was frustrating them.
- Build a new feature and see if people use it.
- Build an experimental feature and make it available to a subset
	of the user base. Not just can you see if they like it, you can also
	assess how much load it puts on your servers.


To support this kind of analysis, you need to add user logging
	behavior into the application and build some tools to analyze these
	logs. Much logging appears for free in web applications, which I
	suspect was  major impetus for people starting to do this. But the
	logging, and analysis, can go further as it's added to the application.


I haven't found much advice out there on the web on how to do
	this, and I don't hear much discussion about doing this in
	practice. Like many things it requires a concentrated effort to
	spend the time to build monitoring capability and then to use
	it to probe how to improve the software. Furthermore it's a mighty
	step away from how the traditional software process, even for
	agile projects.


But there is a huge potential here. Everyone knows how big the
	difference is between what people say they want and what people
	actually need and use. By watching what people actually do with your
	application, you can find out what actually happens with the
	software - which can give you much more direct information than
	other sources. As a result I think more teams should consider
	adding this approach to their toolkit.
