---
title: "Platform Building"
description: "Can you use refactoring to build a platform?"
date: 2003-05-18T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/PlatformBuilding.html
slug: PlatformBuilding
word_count: 277
---


**Can you use refactoring to build a platform?**


It's a common question, and the short answer is that yes,
refactoring is very useful when building a platform. But the issues
involved depend on the state of life of the platform, and
particularly in the approach you use to building a platform.


The common issue in the mind of someone who has this question is
that users of a platform need a stable interface to work against. Any
changes to an interface can have severe ripple effects. In my
terminology, a platform usually has a [Published
Interface](https://martinfowler.com/articles/published.pdf). Published interfaces are usually a pain for refactoring
because any refactoring that changes a published interface is made
much more difficult.


One reason this is less of an issue is because many refactoring that
you might do to a platform don't affect the published
interface. Within the non-published boundary, you can refactor
freely. Sadly languages usually don't allow you to mark published
interfaces very cleanly, so you'll usually have to do some extra work
to set up a properly published section to your interface.


## Styles of Platform


The role of refactoring has a lot to do with how you build your
platforms. Many people have the notion of a
[FoundationPlatform](https://martinfowler.com/bliki/FoundationPlatform.html). In this case you have to fix and
publish your API as soon as possible, which means that refactoring is
less useful due the limits I mentioned above.


But a [FoundationPlatform](https://martinfowler.com/bliki/FoundationPlatform.html) isn't
necessarily the best way to go. I've seen a lot of failures in
building platforms that way. I think
[HarvestedPlatform](https://martinfowler.com/bliki/HarvestedPlatform.html) is a much better way to go,
and refactoring is *extremely* useful when you are building a
[HarvestedPlatform](https://martinfowler.com/bliki/HarvestedPlatform.html).
