---
title: "Foundation Platform"
description: "A Foundation Platform is a that is built prior to any application that are built on top of it. The idea is that you analyze the needs of the various applications that need the platform, then you build"
date: 2003-06-03T00:00:00
tags: ["api design", "platforms"]
url: https://martinfowler.com/bliki/FoundationPlatform.html
slug: FoundationPlatform
word_count: 184
---


A Foundation Platform is a that is
built prior to any application that are built on top of it. The idea
is that you analyze the needs of the various applications that need
the platform, then you build the platform. Once the platform is
complete you then build applications on top of it. The point is that
the platform really needs to have a stable API before you start work
on the applications, otherwise changes to the platform will be hard
to manage due to their knock-on effects with the applications.


While this sounds reasonable in theory, I've always seen this work
badly in practice. The problem is that it's very hard to understand
the real needs of the platform. As a result the platform ends up
with far more capabilities that are really needed. Often its
capabilities don't really match what that the applications really
need.


Contrast this with [HarvestedPlatform](https://martinfowler.com/bliki/HarvestedPlatform.html)


I originally published this entry under the name FoundationFramework, but
    our vocabulary has evolved and we're now using the word âplatformâ where we
    did use âframeworkâ. The core thinking, however, remains the same.
