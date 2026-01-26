---
title: "Model Driven Architecture"
description: "Some people think thatModel Driven Architecture(MDA) will be biggest shift in software development since the move from assembler to the first high level languages. Others think that it's nothing more "
date: 2004-02-02T00:00:00
tags: ["uml"]
url: https://martinfowler.com/bliki/ModelDrivenArchitecture.html
slug: ModelDrivenArchitecture
word_count: 742
---


Some people think that [Model
Driven Architecture](http://www.omg.org/mda/) (MDA) will be biggest shift in software
development since the move from assembler to the first high level
languages. Others think that it's nothing more than Night of the
Living Case Tools. I'm in the latter camp but feel the need for more
than a slick saying.


Much of what's being said now for MDA was the same things that
the CASE tool community talked about in the 80's. I think CASE tools
failed for a number of reasons, but underlying it all was the fact
that they couldn't come up with a coherent programming environment
that would allow people to build general enterprise applications more
effectively than the alternatives. Certainly CASE tools can help,
often considerably, for particular tasks. I'd rather draw up a
database schema with a graphical schema designer than typing SQL into
TextPad. But too many things were either not possible or much harder
with CASE environments.


So my question is whether MDA alters this. The UML grew out of
notations that are pretty reasonable for sketching to convey design
ideas. I use [UmlAsSketch](https://martinfowler.com/bliki/UmlAsSketch.html) heavily, but the degree of
formality and cohesion that's required to turn UML into the complete
solution that's needed for MDA to work is much tougher. Certainly with
UML 2 many people have worked hard to try to make the UML
computationally complete. But much of this is done on paper, without
clear examples and experience of what a platform using the UML would
be like in practice. Even if the UML is computationally complete, it
has to be a more effective environment for software development than
the alternatives. As one who is familiar with both the UML and the
alternatives, I have to say I don't see this.


As an example, consider behavioral logic. I can't see that drawing
sequence diagrams or activity diagrams is as good, let alone better,
than writing code in a modern language. I find this is true even when
I have to write code to a greater degree of precision than the
diagrams, as I do if I want to execute and test them.


Even if the UML forms an effective programming environment, it
still needs to become a popular one. As an ex-Smalltalker I know only
too well that even the best languages don't always make it into the
mainstream.


Other arguments for the MDA are secondary, but also unconvincing.

- Having an OMG standards stack is certainly something that the
80's CASE tools lacked, but we'll see how well people stick to it. One
thing that's struck me is how many MDA fans seem to see UML as the
[UnwantedModelingLanguage](https://martinfowler.com/bliki/UnwantedModelingLanguage.html).
- MDA proponents talk about platform independence, but I've
already dismissed this as a
[PlatformIndependentMalapropism](https://martinfowler.com/bliki/PlatformIndependentMalapropism.html).
- I've heard about how MDA will simplify development by allowing
automatic generation of patterns. But I don't see a difference between
what you can do in UML and what can be done with good libraries and
frameworks. (As well as the fact that generating pattern
implementations is missing at least half the point of patterns.)
- Much of the boosting of UML seems to be based on the statement
			that pictures are better than text. In cases this is true, but I
			see no evidence for that in general -  anyone who has compared
			flow charts to pseudo code can form their own conclusions.


In many ways I'd love to be wrong about this. I would really like
	to see software development raised by a level of abstraction. (Not
	to mention that the UML's success would be good for me personally.)
	But I don't see that the UML provides this abstraction jump - and
	without it the MDA will not succeed.


Interestingly there is a growing sense that a broader group of
people want to do MDA without the OMG standards. I'm hearing more
about Model Driven Development using tools other than the OMG's MDA stack.


Here's some other thoughtful criticism of the MDA:

- Steve Cook talks about [Microsoft's

views on MDA](http://www.bptrends.com/publicationfiles/01-04%20COL%20Dom%20Spec%20Modeling%20Frankel-Cook.pdf) and the broader issues of Model Driven Development.
Steve was a central contributer to the UML as well as a leader in the
early days of OO in the UK.
- [âBedarraâ Dave
Thomas](http://c2.com/cgi/wiki?DaveThomas) gave a spectacular display of energetic skepticism at the
MDA panel at OOPSLA 2003. Sadly I don't have a video of his
performance, but an older [jot column](http://www.jot.fm/issues/issue_2003_01/column1)
captures some of the depth of his argument.
