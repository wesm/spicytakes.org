---
title: "Application Boundary"
description: "When I talk about databases and how they relate to applications, I've found it useful to distinguish between two styles of database:ApplicationDatabaseandIntegrationDatabase. The difference between th"
date: 2004-05-24T00:00:00
tags: ["team organization", "enterprise architecture", "application architecture"]
url: https://martinfowler.com/bliki/ApplicationBoundary.html
slug: ApplicationBoundary
word_count: 216
---


One of the undecided problems of software development is deciding
what the boundaries of a piece of software is. (Is a browser part of
an operating system or not?) Many proponents of Service Oriented
Architecture believe that applications are going away - thus future
enterprise software development will be about assembling services
together.


I don't think applications are going away for the same reasons
why application boundaries are so hard to draw. Essentially
  **applications are social constructions**:

- A body of code that's seen by developers as a single unit
- A group of functionality that business customers see as a
single unit
- An initiative that those with the money see as a single
budget


All of these are social things. We can draw application
boundaries in hundred arbitrarily different ways. But it's our nature
to group things together and organize groups of people around these
groups. There's little science in how this works, and in many ways
these boundaries are drawn primarily by human inter-relationships and
politics rather than technical and functional considerations. To think
about this more clearly I think we have to recognize this
uncomfortable fact.


(If you are interesting in thinking further about applications
and how they interrelate, you should take a look at the strategic
design section of [Domain-Driven
Design](https://www.amazon.com/gp/product/0321125215/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321125215&linkCode=as2&tag=martinfowlerc-20))
