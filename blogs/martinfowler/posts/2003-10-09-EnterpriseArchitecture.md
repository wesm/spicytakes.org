---
title: "Enterprise Architecture"
description: "Just recently I've picked up a couple of bad reviews on Amazon 	forP of EAAbecause there is nothing in the book about enterprise 	architecture. Of course there's a good reason for that - the book is 	"
date: 2003-10-09T00:00:00
tags: ["application integration", "enterprise architecture", "application architecture"]
url: https://martinfowler.com/bliki/EnterpriseArchitecture.html
slug: EnterpriseArchitecture
word_count: 689
---


Just recently I've picked up a couple of bad reviews on Amazon
	for [P of EAA](https://martinfowler.com/books/eaa.html) because there is nothing in the book about enterprise
	architecture. Of course there's a good reason for that - the book is
	about enterprise *application* architecture, that is how to design
	enterprise applications. Enterprise architecture is a different
	topic, how to organize multiple applications in an enterprise into a
	coherent whole.


As it turns out, I can get pretty cynical about enterprise
	architecture. This cynicism comes from what seems to be the common
	life-cycle of enterprise architecture initiatives. Usually they begin
	in a blaze of glory and attention as the IT group launches a major
	initiative that will be bring synergy, reuse, and all the other
	benefits that can come by breaking down the stovepipes of
	application islands (and other suitable analogies). Two or three
	years later, not much has been done and the enterprise architecture
	group isn't getting their phone calls returned. A year or two after
	that and the initiative quietly dies, but soon enough another one
	starts and the boom and bust cycle begins again.


So why does this cycle happen with such regularity? I think that
	most people involved in these initiatives would say the reason they
	fail is primarily due to politics - but what they often miss is that
	those political forces are inevitable. To succeed in these things
	means first recognizing the strength of those political forces.


The problem for central architecture groups is that they are
	driven by IT management, but the applications they are looking to
	organize are driven by business needs. If an application team is
	told to do work that doesn't benefit their application directly, but
	makes it easier to fit in the architecture, there's a natural
	reluctance to do it. Furthermore they have the ace card - the
	business sponsor. If the business sponsor is told the application
	will ship four months late in order to conform to the enterprise
	architectural plans, then they are motivated to back up the
	application team when they say no (spelled âwe'll get around to it laterâ). Since the application is directly
	connected to providing business value, and the central architectural
	team isn't, the application team wins. These wins cause the
	enterprise architecture initiative to bust.


To avoid this the enterprise architecture initiative has to
	recognize and submit to the political realities.

- Understand what the business value of any enterprise
		architectural initiative is.
- Make sure that any work is supported by incremental short term
		gains in business value.
- Minimize costs to the applications


A good way to think about this is that these initiatives should
less about building an overarching plan for applications, and more
about coming up with techniques to integrate applications in whatever
way they are put together. (After all [ApplicationBoundaries](https://martinfowler.com/bliki/ApplicationBoundary.html) are
primarily social constructs and they aren't likely to conform to
anyone's forward plans.)  This integration architecture should work
with the minimum impact to application teams, so that teams can
provide small pieces of functionality as the business value justifies
it. I think you also need to focus on approaches that minimize
coupling between applications, even if such approaches are less
efficient than a more tightly coupled approach might be.


These reasons tend to lead me toward a [messaging approach](http://www.enterpriseintegrationpatterns.com/) to
	integration. While it has its faults, it's something that can be
	applied with minimal impact to existing applications.


By the way, enterprise application architecture can have a big
	impact upon enterprise integration. Applications that are nicely
	layered, particularly with a good [PresentationDomainSeparation](https://martinfowler.com/bliki/PresentationDomainSeparation.html), are
	much easier to stitch together because you can more easily expose
	the applications functionality through services. This isn't a cost
	to the application, because good layering makes the application
	easier to maintain as well. However too few application developers
	understand how to do [PresentationDomainSeparation](https://martinfowler.com/bliki/PresentationDomainSeparation.html). One of the best
	things an integration group can do is to support education and
	training to help them to do this (an approach that's best supported
	if they act like [Architectus Oryzus rather than Architectus Reloadus](https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf)). So in that sense my book has a lot
	to do with enterprise architecture.
