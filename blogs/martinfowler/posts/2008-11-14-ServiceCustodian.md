---
title: "Service Custodian"
description: "Let's imagine a pretty world of SOA-happiness where the computing   needs of an enterprise are split into many small applications that   provide services to each other to allow effective collaboration"
date: 2008-11-14T00:00:00
tags: ["team organization", "application integration"]
url: https://martinfowler.com/bliki/ServiceCustodian.html
slug: ServiceCustodian
word_count: 455
---


Let's imagine a pretty world of SOA-happiness where the computing
  needs of an enterprise are split into many small applications that
  provide services to each other to allow effective collaboration. One
  fine morning a consumer service needs some information from a supplier
  service. The twist is that although the supplier service has the
  necessary data and processing logic to get this information, it
  doesn't yet expose that information through a service interface. The
  supplier has a potential service, but it isn't actually there yet.


In an ideal world the developers of the consumer service just asks
  the supplier service to develop the potential service and all is
  dandy. But life is not ideal - the sticking point here is that the
  developers of the supplier service have other things to do, usually
  things that are more important to their customer and management than
  helping out the consumer service team.


Recently I was chatting with my colleague Erik Dörnenburg and he
  told me about an approach he saw a client use to deal with
  this problem. They took a leaf out of the open source play-book and
  made all their services into internal open source systems. This
  allows consumer service developers write the service themselves.


I'm sure many readers are rolling their eyes at the visions of
  chaos this would cause, but just as open source projects don't allow
  just anyone to edit anything; this client uses open-source-style control
  mechanisms. In particular each service has a couple of custodians -
  people whose responsibility it is to keep the service in a healthy
  state. In the normal course of events the consumer developer wouldn't
  actually commit changes to the supplier source tree directly,
  instead they send a patch to the custodian. Just like an open-source
  maintainer, the custodian receives the patch and reviews it to see
  if it's good enough to commit. If not there's a dialog with the
  consumer developer.


As Erik knows well from [his own open
  source work](http://erik.doernenburg.com/open-source-projects/), reviewing a patch is much less effort than making
  a change yourself. So although the custodian approach doesn't
  entirely eliminate the problem of consumer developers needing to wait
  on supplier developers, it does a lot to reduce the difficulty. And
  again following the open-source model, a consumer developer can be
  made a committer once the custodians are comfortable. This
  still means that commits can get reviewed by the custodians, but avoids
  the custodians becoming a bottleneck.


Related to this was their approach to a service registry. We've
  seen a lot of fancy products being sold to provide service registry
  capabilities so that people can lookup services and see how to use
  them. This client discarded them and used a
  [HumaneRegistry](https://martinfowler.com/bliki/HumaneRegistry.html) instead.


reposted on 24 May 2012
