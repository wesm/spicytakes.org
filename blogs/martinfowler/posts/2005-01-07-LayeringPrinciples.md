---
title: "Layering Principles"
description: "For the last few days I've been attending a workshop on enterprise software in Norway, hosted by Jimmy Nilsson. During the workshop we had a session where we came up and voted on a bunch of design pri"
date: 2005-01-07T00:00:00
tags: ["application architecture"]
url: https://martinfowler.com/bliki/LayeringPrinciples.html
slug: LayeringPrinciples
word_count: 574
---


For the last few days I've been attending a workshop on
enterprise software in Norway, hosted by Jimmy Nilsson. During the
workshop we had a session where we came up and voted on a bunch of
design principles.


The rules were this. Everyone could propose principles for good
layering which were added to a list. There was little discussion of
the principle - only clarification as needed. People could propose
principles they liked or not - the rule was to capture principles that
people had heard in the field.


Once we'd got a list, it was time to vote. We used a variant of
[DotVoting](https://martinfowler.com/bliki/DotVoting.html) where everyone got 10 positive and 10 negative votes.


I've put the results below - principle followed votes in the
format positive/negative.

- Low coupling between layers, high cohesion within them.
10/0
- Separation of concerns. 11/0
- Layers should be agnostic of consumers (a layer shouldn't know
who's on top of it.) 4/4
- Adaptability: be able to change. 2/0
- User interface modules should contain no business logic.
10/0
- Business logic layers contain no user interface and don't
refer to user interface modules. 8/0
- No circular references between layers. 8/0
- There are at least three main layer types: presentation,
domain, and data source. 3/9
- Business layer only uses abstractions of technological
services. 14/0
- Separate development teams by layer. 1/22
- Layers should be testable individual. 12/0
- Prefer layers to interact only with adjacent layers. 4/4
- A layer should be wary of exposing lower layers to upper
layers. 1/0
- Layers should hide lower layers from upper layers.
- Layers should only interact with adjacent layers. 2/3
- Changing a lower level layer interface should not change upper
layer interfaces. 2/5
- Distribute at layer boundaries 0/18
- Layers are a logical artifact that does not imply
distribution between layers. 11/0
- Lower layers should not depend on upper layers. 6/0
- Every layer should have a secret. 3/2
- Layers should be shy about their internals. 8/0
- Layers should be substitutable. 2/0
- Layers can have multiple adjacent upper layers. 2/1
- Always wrap domain logic with a service layer. 4/5
- Rethrow exceptions at layer boundaries. 0/15
- Layers should be independently maintainable and versioned.
2/0
- Layers should have separate deployment units (eg separate jars
or assemblies for each layer). 0/7
- Layers may share infrastructural aspects (eg security)
7/0
- The domain layer should not talk to external systems - the
service layer should do that. 2/3
- Inbound external interface modules (eg web service handlers)
should not contain business logic. 10/0


Obviously you can't read too much into this list. While it was a
good group of people, it was hardly a definitive source of enterprise
development expertise. The principles are also worded somewhat loosely
and there are overlaps and imprecisions that would be cleaned up if
we'd had more than an hour for the exercise. However I suspect the
list might provoke a little thought and discussion.


I asked people if there were things that surprised them. A couple
of people were surprised that principles that they had heard often (and
disliked) were trashed in the voting. (Separate development teams by
layer and Rethrow exceptions at layer boundaries.) Similarly there was
a surprise that âBusiness layer only uses abstractions of technological
servicesâ got such a strong vote even though it's rarely done in
practice.
