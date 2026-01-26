---
title: "Utility Vs Strategic Dichotomy"
description: "A common question in IT departments is whether to provide a   capability by building custom software or by buying a package. For longer   than I've been programming the debate has raged about how to m"
date: 2011-07-06T00:00:00
tags: ["agile adoption", "team organization", "process theory"]
url: https://martinfowler.com/bliki/UtilityVsStrategicDichotomy.html
slug: UtilityVsStrategicDichotomy
word_count: 1315
---


One of the steady themes I've seen throughout my career is that
  of the nature and importance of software development. A few years ago a
  prospect told one of our salespeople that âsoftware is like sewage
  pipes, I want it to work reliably and I don't want to know about the
  detailsâ. This is the kind of approach that Nicholas Carr talked
  about in [IT Doesn't
  Matter](http://www.nicholasgcarr.com/articles/matter.html). 1
  On a contrasting note we've done work for many businesses where IT
  has been a clearer strategic enabler to their business, allowing
  them to enter new markets or significantly increase their market
  share. So is IT a utility, like sewage pipes, or a strategic
  asset?


1: 
       This is a well-known paper in Harvard Business Review where he
  questioned whether IT was ever of any great importance to
  business. He followed this up with a [book](https://www.amazon.com/gp/product/1591394449/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1591394449&linkCode=as2&tag=martinfowlerc-20), which is reasonable even if it does
  read like a padded HBR article.


![](images/utilityVsStrategicDichotomy/sketch.png)


I take that the view is that it can be either, depending on the
  system. A classic example of a utility IT effort is payroll,
  everyone needs it, but it's something that most people want to âjust
  workâ.


So what is the distinguishing factor between utility and
  strategic projects? To my mind it's all about whether the *underlying
  business function* is a differentiator or not. If how you do this
  function is a crucial part of what makes you better than the
  competition, then the software that supports this function needs to
  be as good as you can make it.  As Ross Pettit [puts
  it](http://www.rosspettit.com/2010/07/separating-utility-from-value-add.html) âThis is not a separation of IT by the nature of the
  technology, but into what technology does for the host
  businessâ.


The most important point about this dichotomy is to realize that
  there are two kinds of software projects and they need to be treated
  entirely differently. The way you staff, run, and budget a
  strategic effort is entirely different to how you do a utility
  project. Too often people assume that what is good for one is good
  for the other - and trouble inevitably follows.


Another consequence is that only a few projects are
  strategic. The 80/20 rule applies, except it may be more like
  95/5. While certainly it's most common for people to not recognize
  the dichotomy at all, it's also common for people to think that too
  many projects are strategic.


One of the most important ways in which these efforts differ is
  where the risks lie. For utility projects the biggest risk is some
  kind of catastrophic error - you don't want the sewage pipe to
  break, or to miss payroll. So you need enough attention to make sure
  that doesn't happen, but other than that you want costs to be as low
  as possible. However with strategic projects, the biggest risk is
  not doing something before your competitors do. So you need to be
  able to react quickly. Cost is much less of an issue because the
  opportunity cost of not doing something is far greater than costs of
  software development itself.


This is not a static dichotomy. Business
  activities that are strategic can become a utility as time
  passes. Less often, a utility can become strategic if a company
  figures out how to make that activity a differentiator. (Apple did
  something like this with the design of personal computers.)


One way this dichotomy helps is in deciding between building
  custom software and installing a package. Since the definition of
  utility is that there's no differentiator, the obvious thing is to
  go with the package. For a strategic function you don't want the
  same software as your competitors because that would cripple your
  ability to differentiate.


Often people realize this and buy a package for a utility
  function, but then spend huge amounts of money customizing this -
  which is just as wasteful. My view is that for a utility function
  you buy the package and adjust your business process to match the
  software. Usually this is politically infeasible, so the workaround
  is to put a low grade software team to work on it. Provide enough
  care to avoid catastrophe, but otherwise you don't need a high-grade
  team.


Another way the dichotomy makes its influence felt is the role of
  agile methods. Most agilists tend to come from a strategic mindset,
  and the flexibility and rapid time-to-market that characterizes
  agile is crucial for strategic projects. For utility projects,
  however, the advantages of agile don't matter that much. I'm not
  sure whether using an agile approach for a utility function would be
  the wrong choice, but I am sure that it doesn't matter that much.


Like many classifications, there's a lot of grey in between. Yet
  this is one of those rare cases where I think there's a strong
  argument to turn up the contrast and force more binary thinking. As
  Ross commented in a discussion of a draft of this post: â'shades of
  grey' give license to pile things into the wrong category; things
  that are really utility will be given an inflated importance, rather
  than dispositioned as the utilities they really are.â Forcing a
  binary decision, tilted to minimize what's in the strategic bucket,
  would help provide the focus that's often lacking in IT initiatives.


Ross goes so far as to argue that there
  shouldn't be a single IT department that's responsible for both
  utility and strategic work. The mindset and management attitudes
  that are needed for the two are just too different. It's like
  expecting the same people who design warehouses to design an arts
   museum.


## Bimodal IT


Recently some consulting companies have popularized the notion of Bimodal IT (or
     Two Speed IT) 2. At first blush this seems the same
     as the Utility/Strategic dichotomy, but in fact it's quite a different notion.
     Bimodal IT is also a path that heads in the wrong direction.


2: [Bimodal IT](http://www.gartner.com/it-glossary/bimodal) is the term used by Gartner, [Two-Speed IT](http://www.mckinsey.com/business-functions/business-technology/our-insights/a-two-speed-it-architecture-for-the-digital-enterprise) is the term used by McKinsey.
      From my reading they seem to be roughly equivalent.


The first difference is that Bimodal IT is based on separation of IT systems by
     layer rather than the underlying business activity. Bimodal IT separates rapid-moving
     front-end *systems of engagement* from slow-but-reliable backend *systems of record*. But
     if you're trying to innovate rapidly in a strategic business function, you're usually
     going to need rapid change in both the front-end and back-end systems.


My second beef with Bimodal IT is that a driving reason for the separation is the
     notion that rapid-changing systems of engagement are inherently full of defects and
     we tolerate these defects in order to gain speed. However the decade-plus experience
     at Thoughtworks and other leading agile organizations tells us that this
     [TradableQualityHypothesis](https://martinfowler.com/bliki/TradableQualityHypothesis.html) is a false trade-off. Usually we find that when we introduce agile
     approaches with rapid cycle times, we also see an order of magnitude decreases in
     production defects. Indeed without reducing defects like this we wouldn't be able to cycle
     so rapidly: **high quality (and low defects) are a crucial enabler for rapid cycle-time**.


## To explore more...

- [Ross's
    article](http://www.rosspettit.com/2010/07/separating-utility-from-value-add.html) calls for a Glass-Stegall of IT
    departments.
- Marc McNeil talks of projects as [Tractors, nuclear power plants and the bleeding edge](http://www.dancingmango.com/blog/2010/07/14/tractor-bleedingedge/)
- Neal Ford points out that integration efforts, such as SOA,
    [can't be strategic](http://memeagora.blogspot.com/2009/01/tactics-vs-strategy-soa-tarpit-of.html).
- Jez Humble [explains
    three flaws in the  bimodal IT model](http://continuousdelivery.com/2016/04/the-flaw-at-the-heart-of-bimodal-it/)


## Revisions


Originally published on 2010-07-29.


Updated on 2016-04-07 to describe the difference between this and Bimodal IT.


## Notes


1: 
       This is a well-known paper in Harvard Business Review where he
  questioned whether IT was ever of any great importance to
  business. He followed this up with a [book](https://www.amazon.com/gp/product/1591394449/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1591394449&linkCode=as2&tag=martinfowlerc-20), which is reasonable even if it does
  read like a padded HBR article.


2: [Bimodal IT](http://www.gartner.com/it-glossary/bimodal) is the term used by Gartner, [Two-Speed IT](http://www.mckinsey.com/business-functions/business-technology/our-insights/a-two-speed-it-architecture-for-the-digital-enterprise) is the term used by McKinsey.
      From my reading they seem to be roughly equivalent.
