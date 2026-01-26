---
title: "Uml Sketching Tools"
description: "I draw a lot of UML diagrams, but I don't use CASE tools. The reason is that I'm interested inUmlAsSketch, not in all the repository stuff. So far my regular choice has been Visio. Although Visio come"
date: 2004-06-16T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/UmlSketchingTools.html
slug: UmlSketchingTools
word_count: 579
---


I draw a lot of UML diagrams, but I don't use CASE tools. The
reason is that I'm interested in [UmlAsSketch](https://martinfowler.com/bliki/UmlAsSketch.html), not in all
the repository stuff. So far my regular choice has been Visio.
Although Visio comes with UML templates I don't use the built in ones
- I prefer those of [Pavel Hruby](http://www.phruby.com/).


Visio has worked very well for me, and it's still my first
choice. But I'll admit to a wandering eye. Visio only works on Windows
- and I also use Macs and Unixen, so it would be nice to have a tool
that worked on all (or actually a common data format). I like to
collaborate with others, so something open source would allow them to
draw diagrams if they don't have access to Visio.


I've played a little with OmniGraffle on my Mac, not enough to
really evaluate its capabilities - although it does produce lovely
looking anti-aliased output. [UMLet](http://www.umlet.com) is
an interesting looking project too.


The biggest thing I would like however is to specify my UML
diagrams as text. That may sound strange - after all UML diagrams are
diagrams, so why use text? Text has some advantages. Much of diagram
layout is tedious to fiddle with in diagrammatic form, and would be
much easier to do textually - using the diagrams as a visualization
rather than an editing mechanism. Also text formats allow you to
easily track changes over time with cvs and diff.


As a result I was intrigued by [UmlGraph](http://www.spinellis.gr/sw/umlgraph/). The part of
this that most grabs me is the sequence diagram editor which uses the
venerable pic program. [This
page](http://www.spinellis.gr/sw/umlgraph/doc/uml-appa.html) shows show the pic macros create a nice textual
representation of a sequence diagram. Of course there are some
limitations of what you can do in a pic macro and I can imagine a textual
representation that's even more compact and clear.


```

objects 
  thread, t:thread
  tool, :Toolkit
  peer, p:Peer, unborn

trace 
  found: a1:run(3) -> 
    thread: 
      run() -> 
        tool: 
           callbackLoop() -> self
           create -> peer
           handleExpose() -> 
             peer: 
               return      
           delete -> peer

```


That's just off the top of my head. I don't know how well that
	would really work in practice. In any case I intend to experiment
	with UmlGraph as it stands to see how it would work for me. The pic
	program is so small I could easily tweak it if I wanted some changes.


UmlGraph's class diagram generator is nice in that it can produce
	stuff from Java source files. However for just a diagram syntax it
	looks rather awkward - and I would like some control over placement
	of classes. Enough to say Customer is to the left of Order. So
	perhaps represent [this
	diagram](http://www.spinellis.gr/sw/umlgraph/doc/ceg-adv.html) with something like this:


```

layout
  row: Controller, EmbeddedAgent, URLStreamHandler, ChannelIterator
  SetTopController below: URLStreamHandler
  PowerManager below: SetTopController

interface URLStreamHander 
  operations 
    OpenConnection()
    parseURL()
    setURL()
    toExternalForm()

class SetTopController
  specializes
    Controller
    EmbeddedAgent
  implements
    URLStreamHandler
  attributes
    authorizationLevel
  operations
    startUp()
    shutDown()
    connect()
  associations
    -> PowerManager

class ChannelIterator
  dependencies
    -> SetTopController keyword:friend

```


Again this is just off the top of my head. The important thing is
	that I'm glad to see someone going in this direction - and would
	like to see more.


Here's some similar sketch-like tools that people have told me
	about

- [MetaUml](http://metauml.sourceforge.net)
- [TWiki
		Draw Plugin](http://twiki.org/cgi-bin/view/Plugins/TWikiDrawPlugin)
- [Sequence](http://www.zanthan.com/itymbi/archives/cat_sequence.html)
- [Agent UML Tool](http://www.winikoff.net/auml)
- [yUML](http://yuml.me/): draws class and use case
    diagrams in a web page from text spec embedded in an img tag. Has a scruffy
                style.
- [PlantUML](http://plantuml.com)
