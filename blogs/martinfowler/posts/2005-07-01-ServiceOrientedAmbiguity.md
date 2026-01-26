---
title: "Service Oriented Ambiguity"
description: "Whenever Thoughtworks rashly lets me out in front of a client, 	one question I'm bound to be asked is âwhat do you think of SOA 	(Service Oriented Architecture)?â It's a question that's pretty muc"
date: 2005-07-01T00:00:00
tags: ["application integration", "enterprise architecture"]
url: https://martinfowler.com/bliki/ServiceOrientedAmbiguity.html
slug: ServiceOrientedAmbiguity
word_count: 426
---


Whenever Thoughtworks rashly lets me out in front of a client,
	one question I'm bound to be asked is âwhat do you think of SOA
	(Service Oriented Architecture)?â It's a question that's pretty much
	impossible to answer because SOA means so many different things to
	different people.

- For some SOA is about exposing software through web
	services. This crowd further sub-divides into those that expect the
	various WS-* standards and those that will accept any form of XML
	over http (and maybe not even XML).
- For some SOA implies an architecture where applications
	disappear. Instead you have core services that supply business
	functionality and data separated by UI aggregators that apply
	presentations that aggregate together the stuff that core services
	provide.
- For some SOA is about allowing systems to communicate over
	some form of standard structure (usually XML based) with other
	applications. In it's worse form this is âCORBA with angle
	bracketsâ. In more sophisticated forms this involves coming up with
	some form of standard backbone for an organization and getting
	applications to work with this. This backbone may or may not involve
	http.
- For some SOA is all about using (mostly) asynchronous messaging to
	transfer documents between different systems. Essentially this is
	EAI without all the expensive EAI vendors locking you in.


I've heard people say the nice thing about SOA is that it
	separates data from process, that it combines data and process, that
	it uses web standards, that it's independent of web standards, that
	it's asynchronous, that it's synchronous, that the synchronicity
	doesn't matter....


I was at Microsoft PDC a couple of years ago. I sat through a
day's worth of presentations on SOA - at the end I was on the SOA
panel. I played it for laughs by asking if anyone else understood what
on earth SOA was. Afterwards someone made the comment that this
ambiguity was also something that happened with Object Orientation.
There's some truth in that, there were (and are) some divergent views
on what OO means. But there's far less Object Ambiguity than the there
is Service Oriented Ambiguity.


So what do we do? For a start we have to remember all the time
about how many different (and mostly incompatible) ideas fall under
the SOA camp. These do need to be properly described (and named)
independently of SOA. I think SOA has turned into a semantics-free
concept that can join 'components' and 'architecture'. It's beyond
saving - so the concrete ideas that do have some substance need to get
an independent life.
