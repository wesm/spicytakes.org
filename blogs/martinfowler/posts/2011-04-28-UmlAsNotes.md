---
title: "Uml As Notes"
description: "Yesterday I was poking around a code base, looking at the domain   model part of the code. When exploring a code base, I like to take   notes to help me remember what I'm learning. For some code bases"
date: 2011-04-28T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/UmlAsNotes.html
slug: UmlAsNotes
word_count: 541
---


Yesterday I was poking around a code base, looking at the domain
  model part of the code. When exploring a code base, I like to take
  notes to help me remember what I'm learning. For some code bases, in
  particular domain models, I find it handy to sketch UML class diagrams.


UML has got rather out of fashion it seems. Although this isn't
  good for me financially, I can't say I'm displeased to see a lot of
  rather dodgy UMLisms going away. I continue to find it a useful
  tool, as I did that morning. As I worked my way around the code I
  would jot down classes and relationships, to see how the various
  classes played together.


I don't use âreverse-engineeringâ tools for this. Such tools run
  on your code base and automatically generate the class
  diagram. Although this is quite straight-forward to do technically,
  the result is rather useless. For me the value of a good diagram is
  that it highlights the important stuff, and ignores what's not. So I
  don't draw every class, let alone every relationship and feature. I
  decide to jot down things that I think are important to remember,
  particularly focusing on connections that often don't show up so
  much when you're looking at the code. I also only use a little of
  the endless class diagram syntax, and I'm not afraid of being sloppy
  with it. 1


1: Actually I'm not very sloppy, because I
    know the syntax so well that I'm unconsciously pretty accurate. But
    the point is that people who are less familiar with the syntax
    shouldn't worry about it in this mode of working.


When I'm doing this speed is important. Currently my favorite
  tool for this kind of jotting is [Umlet](http://www.umlet.com/) 2. What I
  like about it is that most of what you capture goes in as text,
  using a wiki-ish markup. As a result I can quickly slap things in
  there, using the mouse just to broadly move things around as
  needed. It's a java program, so it suffers ugliness for
  availability.


2: Yes that home page is littered with
    ads that make it hard to find the useful stuff.


When I'm doing this, I do the diagrams just for me; so I don't
  put effort into making them nice and clear for others. If I were to
  produce diagrams to help explain the code to others, I'd approach
  them differently. With notes I'm creating reminders for myself, with
  explanatory diagrams I'm trying to communicate different things to
  another audience. 3


3: I'd also use a different tool. If I'm going
    to publish a diagram, I use OmniGraffle. I've loved its diffuse
    shadows ever since [DHH](http://www.loudthinking.com/) introduced it to
    me.


## Notes


1: Actually I'm not very sloppy, because I
    know the syntax so well that I'm unconsciously pretty accurate. But
    the point is that people who are less familiar with the syntax
    shouldn't worry about it in this mode of working.


2: Yes that home page is littered with
    ads that make it hard to find the useful stuff.


3: I'd also use a different tool. If I'm going
    to publish a diagram, I use OmniGraffle. I've loved its diffuse
    shadows ever since [DHH](http://www.loudthinking.com/) introduced it to
    me.
