---
title: "Humane Registry"
description: "One of the features of the new world of services that SOA-gushers   promoted was the notion of registries. Often this was described in   terms of automated systems that would allow systems to automati"
date: 2008-12-01T00:00:00
tags: ["application integration"]
url: https://martinfowler.com/bliki/HumaneRegistry.html
slug: HumaneRegistry
word_count: 568
---


One of the features of the new world of services that SOA-gushers
  promoted was the notion of registries. Often this was described in
  terms of automated systems that would allow systems to automatically
  look up useful services in a registry and bind and consume those
  services all by themselves.


Well computers may look clever occasionally, but I didn't
  particularly buy that idea. While there might the be odd edge case
  for automated service lookup, I reckon twenty-two times out of
  twenty it'll be a human programmer who is doing the looking up.


I was chatting recently to my colleague Erik Dörnenburg about a
  project he did with Halvard Skogsrud to build a service registry
  that was designed for humans to use and maintain. The organization
  was already using [ServiceCustodians](https://martinfowler.com/bliki/ServiceCustodian.html) to manage the
  development on the project, so the registry needed to work in that
  context. This led to the following principles:

- People develop and use services, so orient it around people
    (sorry UDDI, thank you for playing).
- Don't expect people to enter stuff to keep it up to date,
    people are busy enough as it is.
- Make it easy for people to read and contribute.


The heart of the registry is a wiki that allows people to easily
  enter information on a particular service. Not just the builders of
  the service, but also people who've used it. After all users'
  opinions are often more useful than providers (I'm guessing product
  review sites get more traffic than the vendors' sites).


A wiki makes it easy for people to describe the service, but that
  relies on people having time to contribute. A wiki helps make that
  easy as you can just click and go, but there's still time
  involved. So they backed up the human entry with some useful
  information gathered automatically.

- A tool that interrogates the source code control systems and
  displays who has committed to a service, when, and how much. This
  helps human readers find out who are the other humans who they
  should talk to. Someone who did most of the commits, even if a while
  ago, probably knows a lot about the core design and purpose of the
  service. People who made a few recent commits might know more about
  the recent usage and quirks.
- RSS feeds from CI servers and source code control systems.
- Task and bug information from issue tracking systems.
- Traffic data from the message bus indicating how much the
   service is used, and when. Also the message bus gives some clues
   about the consumers of the service.
- Interceptors in the EJB container that captured consumer
   application names - again to get a sense of who is consuming the
   service. These were on the consumer side to capture consumer
   application names, and on the service to get a sense of the usage
   patterns.
- Information from the Ivy dependencies.


The point of a registry like this is that it does a lot of
  automated work to get information, but presents it in a way that
  expects a human reader. Furthermore it understands that the
  most important questions the human reader has are about the humans
  who have worked on the project: who are they, when did they work on
  this, who should I email, and where do I go for a really good
  caipirinha?


## Acknowledgements

Much of this functionality was inspired by ohloh.net