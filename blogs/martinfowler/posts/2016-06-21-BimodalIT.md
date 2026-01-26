---
title: "Bimodal IT"
description: "Bimodal IT is the flawed notion that software systems should be divided into these   two distinct categories for management and control."
date: 2016-06-21T00:00:00
tags: ["bad things", "team organization"]
url: https://martinfowler.com/bliki/BimodalIT.html
slug: BimodalIT
word_count: 526
---


Bimodal IT is the flawed notion that software systems should be divided into these
  two distinct categories for management and control.

- Front Office systems (systems of engagement) should be optimized for rapid feature development. These systems
    of engagement need to react rapidly to changing customer needs and business
    opportunities. Defects should be tolerated as the necessary cost for this rapid
    development cycle.
- Back Office systems (systems of record) should be optimized for reliability. As systems of record, it's
    important that you don't get defects that damage the enterprise. Consequently you slow
    down the rate of change.


The term [Bimodal IT](http://www.cio.com/article/2875803/cio-role/what-gartner-s-bimodal-it-model-means-to-enterprise-cios.html) is used by Gartner 1. McKinsey and Co talk about the same basic idea under the name [âTwo Speed ITâ](http://www.mckinsey.com/business-functions/business-technology/our-insights/a-two-speed-it-architecture-for-the-digital-enterprise). (I find it hard to resist calling it âBipolar ITâ.)


1: 
      Sadly all their substantial material is available to subscribers only.


When I first heard about this approach, I was pleased - thinking that these august
  organizations had come to same conclusion that I had with my
  [UtilityVsStrategicDichotomy](https://martinfowler.com/bliki/UtilityVsStrategicDichotomy.html), but as I read further I realized that Bimodal IT
  was a different animal. And worse I think that Bimodal IT is really a path down the
  wrong direction.


My first problem is that the separation is based on software systems rather than
  business activity. If you want to rapidly cycle new ideas, you are going to need to
  modify the back office systems of record just as frequently as the front office systems of
  engagement. You can't come up with clever pricing plans without modifying the systems of
  record that support them.


My second issue is that the bimodal idea is founded on the
  [TradableQualityHypothesis](https://martinfowler.com/bliki/TradableQualityHypothesis.html), the idea that quality is something you trade-off
  for speed. It's a common notion, but a false one. One of the striking things that we
  learned at Thoughtworks when we started using agile approaches for rapid feature
  delivery is that we also saw a dramatic decline in production defects. It's not uncommon
  to see us go live with an order of magnitude fewer defects than is usual for our
  clients, even in their systems of record. The key point is that high quality (and low
  defects) are a crucial enabler for rapid cycle-time. By not paying attention to quality,
  people following a bimodal approach will actually end up slowing down their pace of
  innovation in their âsystems of engagementâ.


So my advice here that it is wise to use different management approaches to different
  kinds of software projects, but don't make this distinction based on the bimodal
  approach. Instead take a [BusinessCapabilityCentric](https://martinfowler.com/bliki/BusinessCapabilityCentric.html) approach, and look at
  whether your business capabilities are utility or strategic.


## Further Reading


Sriram Narayan's book - [Agile IT Organization Design](https://www.amazon.com/gp/product/0133903354/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0133903354&linkCode=as2&tag=martinfowlerc-20)
    - looks at this kind of problem in much more depth.


Jez Humble provides a [worthwhile critique of Bimodal IT](https://continuousdelivery.com/2016/04/the-flaw-at-the-heart-of-bimodal-it/)


Simon Wardley [prefers
    a three-level model](http://blog.gardeviance.org/2015/10/if-you-really-want-bimodal-then-youll.html) of Pioneers, Settlers, and Town Planners.


## Notes


1: 
      Sadly all their substantial material is available to subscribers only.


## Acknowledgements

Brian Oxley, Dave Elliman, Jonny LeRoy, Ken McCormack, Mark Taylor, Patrick Kua, Paulo
Caroli, and Praful J Todkar

discussed drafts of this post on our internal mailing list