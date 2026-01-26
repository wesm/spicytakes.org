---
title: "Presentation Domain Separation"
description: "One of the most useful design principles that I've found and followed is that of keeping a good separation between the presentation aspects of a program (the user interface) and the rest of the functi"
date: 2003-10-09T00:00:00
tags: ["application architecture", "front-end"]
url: https://martinfowler.com/bliki/PresentationDomainSeparation.html
slug: PresentationDomainSeparation
word_count: 274
---


One of the most useful design principles that I've found and
followed is that of keeping a good separation between the presentation
aspects of a program (the user interface) and the rest of the
functionality. Over the years where I've seen this done, I've seen
plenty of benefits:

- Presentation logic and domain logic are easier to understand
when separate.
- You can support multiple presentations on the same base
program without duplicating code.
- User interfaces are hard to test, separation keeps more logic
in more testable places.
- You can easily add a programmatic API for scripting or exposed
as services (I actually see these as alternative presentations).
- Presentation code requires different skills and knowledge to
domain code.


Despite these many advantages, I often see this principle
violated. I think this is partly due to lack of knowledge, and partly
due to the fact that many frameworks make it much too easy to intermix
domain logic into the presentation, and make it harder to maintain the
separation.


Don't make the mistake that this is a client/server physical
separation. Even if all your code is running on the same machine, it's
well worth making this logical separation.


This principle is the most prominent part of Model View
Controller (MVC), indeed for many people MVC is how they describe this
separation.


Remember that such things as web services are also presentations,
even though they are used by computer users rather than human users.
So don't intermix domain code with the code required to support a web
service, or indeed any other external API.


(I also wrote about this in an [IEEE Software column](https://martinfowler.com/ieeeSoftware/separation.pdf).)
