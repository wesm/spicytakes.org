---
title: "Harvested Platform"
description: "To build a platform by harvesting, you start by not trying to build a platform, but by building an application. While you build the application you don't try to develop generic code, but you do work h"
date: 2003-06-03T00:00:00
tags: ["api design", "platforms"]
url: https://martinfowler.com/bliki/HarvestedPlatform.html
slug: HarvestedPlatform
word_count: 196
---


To build a platform by harvesting, you start by not trying to build a
platform, but by building an application. While you build the
application you don't try to develop generic code, but you do work
hard to build a well-factored and well designed application.


With one application built you then build another application which
has at least some similar needs to the first one. While you do this
you pay attention to any duplication between the second and first
application. As you find duplication you factor out into a common
area, this common area is the proto-platform.


As you develop further applications each one further refines the
platform area of the code. During the first couple of applications
you'd keep everything in a single code base. After a few rounds of
this the platform should begin to stabilize and you can separate out
the code bases.


While this sounds harder and less efficient than
[FoundationPlatform](https://martinfowler.com/bliki/FoundationPlatform.html) it seems to work better in
  practice.


I originally published this entry under the name HarvestedFramework, but
    our vocabulary has evolved and we're now using the word âplatformâ where we
    did use âframeworkâ. The core thinking, however, remains the same.
