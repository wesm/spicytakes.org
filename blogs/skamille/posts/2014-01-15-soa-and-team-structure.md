---
title: "SOA and team structure"
date: 2014-01-15
url: https://www.elidedbranches.com/2014/01/soa-and-team-structure.html
word_count: 496
---

This week I sat on a panel to discuss my experiences moving to a
[service-oriented architecture (SOA)](http://en.wikipedia.org/wiki/Service-oriented_architecture)
at Rent the Runway. Many of the topics were pretty standard: when to do such a thing, best practices, gotchas. Towards the end there was an interesting question. It was phrased roughly like this:

> What do you do when you need to create a new feature, and it crosses all sorts of different services? How do you wrangle all the different teams so that you can easily create new features?

I think this is a great question, and illustrates one of the common misperceptions, and common failure modes, of going to a service-oriented architecture.
Let me be clear: SOA is not designed to separate your developers from each other. In my team, developers may work across many different services in order to accomplish their tasks, and we try to make it clear that the systems are "internal open source". You may not be the expert in that system, but when a feature is needed, it's expected that the team creating the feature will roll up their sleeves and get coding.
At big companies SOA is sometimes done in order to create areas of ownership and development. At my previous company, SOA was (among other things) a better way to expose data in an ad-hoc, but monitored, manner, without having to send messages or allow access to databases. The teams owning the services may be in a totally different area of the company from their clients. To access new data, you needed to coordinate with the owning team to expose new endpoints. It created overhead, but data ownership and quality of the services themselves was an important standard and losing velocity to maintain these standards was an acceptable tradeoff.
That is not the way a small startup should approach SOA, but if you don't anticipate this it may become an unintended outcome. When your SOA is architected as mine is, with a different language powering the services than that which powers the client experience (Java on the backend, Ruby on the frontend), you start to segregate your team into backend and frontend developers. We address this separation by working in business-focused teams that have both backend and frontend developers. Other SOA-based companies approach the challenge of separation by creating microservices that only do enough to support a single feature, so that a new feature doesn't always require touching existing functionality. Some companies do SOA with the same framework (say, Ruby on Rails) that powers their user-facing code, so there's no language or framework barrier to overcome when crossing service boundaries.
SOA is a powerful model for creating scalable software, but many developers are reluctant to adopt it because of this separation myth. There are many ways to approach SOA that work around this downside. Acknowledging the risk here and architecting your teams with an eye to avoiding it is important in successfully adopting this model in an agile environment.