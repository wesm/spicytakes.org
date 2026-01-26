---
title: "Multiple Canonical Models"
description: "Scratch any large enterprise and you'll usually find some kind 	of group focused on enterprise-wide conceptual modeling. Most 	commonly this will be a data management group, occasionally they may 	be "
date: 2003-07-21T00:00:00
tags: ["application integration"]
url: https://martinfowler.com/bliki/MultipleCanonicalModels.html
slug: MultipleCanonicalModels
word_count: 486
---


Scratch any large enterprise and you'll usually find some kind
	of group focused on enterprise-wide conceptual modeling. Most
	commonly this will be a data management group, occasionally they may
	be involved in defining enterprise-wide services. They are
	enterprise-wide because rather than focusing on the efforts of a
	single application they concentrate on integrating multiple applications.


Most such groups tend to focus on creating a single comprehensive
	enterprise model. The idea is that if all applications operate based
	on this single model, then it will be much easier to integrate data
	across the whole enterprise - thus avoiding stovepipe
	applications. Much of this thinking follows the shared database
	approach to enterprise integration - where integration occurs
	through applications sharing a single logical enterprise-wide database.


A single conceptual model is a tricky beast to work with. For a
	start it's very hard to do one well - I've run into few people who
	can build these things. Even when you've built one, it's hard for
	others to understand. Many times I've run into the complaint that
	while a model is really good - hardly anyone understands it. This
	is, I believe, an essential problem. Any large enterprise needs a
	model that is either very large, or abstract, or both. And largeness
	and abstractness both imply comprehension difficulties.


These days many integration groups question the shared database
	approach, instead preferring a messaging based approach to
	integration. I tend to agree with this view, on the basis that while
	it's not the best approach in theory, it better recognizes the
	practical problems of integration - especially the political problems.


One of the interesting consequences of a messaging based approach
	to integration is that there is no longer a need for a single
	conceptual model to underpin the integration effort. Talking with my
	colleague Bill Hegerty I realized that

- You can have several canonical models rather than just
		one.
- These models may overlap
- Overlaps between models need not share the same structure,
although there should be a translation between the parts of models
that overlap
- The models need not cover everything that can be represented,
		they only need to cover everything that needs to be communicated
		between applications.
- These models can be built through harvesting, rather than
		planned up-front. As multiple applications communicate pair-wise, you can
		introduce a canonical model to replace n * n translation paths
		with n paths translating to the canonical hub.


The result breaks down the modeling problem, and I believe
	simplifies it both technically and politically.


So far, however, it seems that the data modeling community is
	only beginning to catch on to this new world. This is sad because
	data modelers have a tremendous amount to offer to people building
	canonical messaging models. Not just are skills not taking part,
	many also resist this approach because they assert that a single
	enterprise-wide model is the only proper foundation for integration.
