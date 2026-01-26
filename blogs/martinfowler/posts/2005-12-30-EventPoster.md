---
title: "Event Poster"
description: "This a style of application I've come across a couple of 	times. The application is primarily a reporting application that 	gives users real time information about the state of something. It 	is an ac"
date: 2005-12-30T00:00:00
tags: ["application architecture", "event architectures"]
url: https://martinfowler.com/bliki/EventPoster.html
slug: EventPoster
word_count: 617
---


This a style of application I've come across a couple of
	times. The application is primarily a reporting application that
	gives users real time information about the state of something. It
	is an active application, in that the users have a lot of control
	about what kinds of things they are looking at they're able to drill
	down in particular areas and generally manipulate their display;
	however it is still, at least primarily a read-only application.


Another characteristic of this kind of application is that is an
[event
sourced](https://martinfowler.com/eaaDev/EventSourcing.html) application, that is all updates to the display state are
made through event objects that can be stored and queued. These events
can be custom made for the application, or they can be an external
message stream. Chris Stevenson told me about an example event poster:
[Inkblot](http://cdn.pols.co.uk/papers/agile-approach-to-legacy-systems.pdf), 
which  used a database table, written for another application, where
rows were inserted as events.


Taking these two characteristics together, and you can see that
there's no need for a database to save the in-memory state of the
display. There is often some initial state to load into the system,
such as the world at the start of the day, after that all the changes
are made through the event stream into the in-memory state of the
event poster. Should the application fail, it just reloads the initial
state and replays all the events in the queue.


Going without persisting the application state leads to two main
advantages: firstly the application is very fast since there's no disk
access involved as people manipulate the system. Marcel Weiher told me
about a news feed application at the BBC where a former version took
several seconds to process a request in production and the replacement
event poster application easily did several hundred a second on his
laptop.


Secondly all the complexities of mapping between in-memory and
database are removed, which allows people to build a good domain model
geared towards the display needs and never worry about persisting it.
(This may not be such a big advantage if the display behavior happens
to match relational behavior, because then SQL is advantage.)


Obviously there are limits to this kind of application. You are
	limited in data by what can fit in memory, although these days main
	memory can hold a hell of a lot, it wasn't that long ago when
	gigabyte databases were considered pretty large. You also run into
	the other limitations of event sourcing.


It's trivially easy to cluster this kind of system. All you have
	to do is ensure events get broadcast to all the copies. If one goes
	down it's easy to replace it with another since the states are
	always going to be pretty much in sync.


I said these applications are read-only, but that isn't strictly
true. To do an update the poster just captures the information and
sends it to the back-end application that is the source of the events.
It doesn't update its own data directly, instead it waits for the
appropriate event to come through the stream from the source
application. This ensures that multiple posters show the same data and
that the source application can do any processing it needs to do on
the changes.


We struggled with a good name for this kind
	of application. There are several characteristics that are important
	that it would be nice if the name evoked: event streams, transient
	data, display only. I thought 'poster' was nice because it made me
	think of message boards that carry the news of the day on a poster
	that are torn down and replaced every morning.


An event poster is a natural choice for a system using [CQRS](https://martinfowler.com/bliki/CQRS.html) with event
  collaboration
