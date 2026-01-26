---
title: "Software Component"
description: "The notion of changing software development from laboriously   crafting code  to building powerful systems by simple   assembly of components has been a target since I entered our   profession. It's t"
date: 2015-09-13T00:00:00
tags: ["team organization", "encapsulation", "application architecture"]
url: https://martinfowler.com/bliki/SoftwareComponent.html
slug: SoftwareComponent
word_count: 486
---


The notion of changing software development from laboriously
  crafting code  to building powerful systems by simple
  assembly of components has been a target since I entered our
  profession. It's target that is sometimes glimpsed, but never really
  attained - although many technologies have dangled the carrot of industrial reuse.


When we talk about software components, often the hardest step is
  to talk about what they are. My favorite definition is still this
  one


> Components are not a technology. Technology people seem to find
>     this hard to understand. Components are about how customers want
>     to relate to software. They want to be able to buy their software
>     a piece at a time, and to be able to upgrade it just like they can
>     upgrade their stereo. They want new pieces to work seamlessly with
>     their old pieces, and to be able to upgrade on their own schedule,
>     not the manufacturer’s schedule. They want to be able to mix and
>     match pieces from various manufacturers. This is a very reasonable
>     requirement. It is just hard to satisfy
> -- [Ralph Johnson](http://www.c2.com/cgi/wiki?DoComponentsExist)


I summarize this as saying that **software components are things
  that are independently replaceable and upgradeable**.


I look as components today as coming in two guises: libraries and
  services. A library consists of some code that is linked into a
  process at runtime, becoming part of the client process. Examples
  would include Java's jars, C#'s assemblies, Ruby's gems, and
  Javascript's modules. To be a proper component, the library user
  should retain the decision of when and whether to upgrade supplier
  libraries. So if I choose to use a 6 month out-of-date version of
  library, that's up to me.


A service is a component that exists in its own process, 1 clients talk to it over some interprocess communication
  mechanism: RPC, RESTful calls over HTTP, messaging, etc. Services may upgrade
  on their own timetable, without coordinating with clients, but to do this they
  must preserve their existing client contracts, so the client may choose when
  to upgrade their use of the service. For services to be components, you should
  never need to coordinate the upgrade of one service with another service.


1: Services in this context are distinct from Service Objects in the
    [EvansClassification](https://martinfowler.com/bliki/EvansClassification.html)


I consider a component as a particular form of module. I define modules
  as a division of a software system that allows us to modify a system
  by only understanding some well-defined subsets of it - modules
  being those well-defined subsets. Components are a form of module,
  with the additional property of independent replacement.


## Revisions


2020-11-05: I was digging through my files and found this bliki post,
    which I'd finished but never published. So I added it to my bliki while
    with the date on which I wrote it.


## Notes


1: Services in this context are distinct from Service Objects in the
    [EvansClassification](https://martinfowler.com/bliki/EvansClassification.html)
