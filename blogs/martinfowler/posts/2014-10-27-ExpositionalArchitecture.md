---
title: "Expositional Architecture"
description: "Morrisons OrderPad is a tablet web-application that helps staff in supermarkets       place orders for new stock as they walk around the store. The       resulting application makes a goodexpositional"
date: 2014-10-27T00:00:00
tags: ["application architecture", "writing", "expositional architectures"]
url: https://martinfowler.com/bliki/ExpositionalArchitecture.html
slug: ExpositionalArchitecture
word_count: 706
---


One of the problems with growing our understanding of software
  systems is that we don't see enough examples. In many professional
  disciplines, people learn by looking at what's already been done.
  Examples serve as inspiration, a source of good ideas, and warnings
  of difficulties. For a long time it's been much harder to learn
  about software this way.


I've always enjoyed taking a look at how systems are put
  together. I hope to get more time to do this and also
  to share some of the more interesting architectures that I see. I
  think of these architectures as expositional architectures because
  they are like show homes or gardens. While they might not be exactly
  what you would want for your own purpose, they contain aspects that
  you may want to copy.


For a list of articles of this form, see the
 [expositional architectures tag](https://martinfowler.com/tags/expositional%20architectures.html).


I usually avoid the A-word (architecture) because it's such a
 slippery term. In this case I'll be following [my preferred definition of
 architecture](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf) - â*the important stuff (whatever that is)*â - 
  from Ralph Johnson. This means I'll talk about what I
 think is interesting about the system's design, based both on my
 judgement and on the judgement of the team that's been involved in
 its development.


I use the term âexpositionalâ to emphasize the fact that these
  architectures are a source of interesting ideas, and they are not
  intended to be some kind of âbest practiceâ. For a start, I'm very
  wary of architectures that are set up as some kind of standard,
  because there are so many variables to pay attention to when
  building a concrete system. For example, many people stress the
  importance of a scalable architecture (by which they usually mean the
  ability to handle large amounts of load). Yet many useful systems
  are internal systems that never have a high load, so should be
  designed to support a different set of drivers.


It's often useful to highlight factors that haven't been
  successful. We don't just learn by
  looking at things that worked well, things that have been
  unsuccessful can often be a good guide for avoiding a tempting path.
  And it's common for some architectural feature to be really liked by
  some team members and hated by others. By understanding what drives
  the affection and dislike, you can get an impression on whether it
  would fit in with your architectural aesthetic.


I won't be making expositional architecture posts very
  frequently, since they do take a lot of time and effort to write. It
  takes a while to understand a system well enough to get a feel for
  how it works and where the interesting bits are. It also requires
  time and effort from the development team to explain things and
  verify I haven't got any sticks by the wrong end.


I expect most of the architecture that I'll be describing will
  come from Thoughtworks projects, as they are easier for me to get
  to. However this isn't an absolute rule and I'll happily talk about
  non-TW projects should something catch my eye when I have the time
  to work on it 1.


1: 
      Indeed the first expositional architecture I've written about was
      LMAX - which wasn't a Thoughtworks effort. (Although it was an
      ex-ThoughtWorker working on it who was my point of contact.)


Any expositional architecture I write about will be based on at
 least one real system. I prefer something that's been in production
 for a year or so, because many things that look good in development
 turn out differently once you've been live for a while. But that is a
 preference rather than an absolute rule.


When describing the architecture I'll give the architecture a name
 to act as a reference, but usually this name will be one made up for
 my description, since system names are otherwise too tied to the
 client's context. Similarly I describe systems using a vocabulary
 consistent with the rest of what I write about here, which may not be
 the actual terms used by the development team.


## Notes


1: 
      Indeed the first expositional architecture I've written about was
      LMAX - which wasn't a Thoughtworks effort. (Although it was an
      ex-ThoughtWorker working on it who was my point of contact.)
