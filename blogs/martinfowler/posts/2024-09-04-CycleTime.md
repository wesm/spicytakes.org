---
title: "Cycle Time"
description: "Cycle Time is a measure of how long it takes to get a new feature in a   software system from idea to running in production. In Agile circles, we try   to minimize cycle time. We do this by defining a"
date: 2024-09-04T00:00:00
tags: ["continuous delivery", "metrics", "process theory", "project planning"]
url: https://martinfowler.com/bliki/CycleTime.html
slug: CycleTime
word_count: 835
---


Cycle Time is a measure of how long it takes to get a new feature in a
  software system from idea to running in production. In Agile circles, we try
  to minimize cycle time. We do this by defining and implementing very small
  features and minimizing delays in the development process. Although the rough
  notion of cycle time, and the importance of reducing it, is common, there is a
  lot of variations on how cycle time is measured.


![](images/cycle-time/sketch.svg)


A key characteristic of agile software development is a shift from a
  [Waterfall Process](https://martinfowler.com/bliki/WaterfallProcess.html), where work is decomposed based on
  activity (analysis, coding, testing) to an Iterative Process where work is
  based on a subset of functionality (simple pricing, bulk discount,
  valued-customer discount). Doing this generates a feedback loop where we can learn
  from putting small features in front of users. This learning allows us to
  improve our development process and allows us to better understand where the
  software product can provide value for our customers. 1


1: It also avoids work being stuck in late
    activities such as testing and integration, which were notoriously difficult
    to estimate.


This feedback is a core benefit of an iterative approach, and like most
  such feedback loops, the quicker I get the feedback, the happier I am. Thus
  agile folks put a lot of emphasis on how fast we can get a feature through the
  entire workflow and into production. The phrase *cycle time* is a measure of that.


But here we run into difficulties. When do we start and stop the clock on
  cycle time?


The stopping time is the easiest, most glibly it's when the feature is put
  into production and helping its users. But there are circumstances where this
  can get muddy. If a team is using a [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html), should it
  be when used by the first cohort, or only when released to the full
  population? Do we count only when the app store has approved its release, thus
  adding an unpredictable delay that's mostly outside the control of the
  development team?.


The start time has even more variations. A common marker is when a
  developer makes a first commit to that feature, but that ignores any time
  spent in preparatory analysis. Many people would go further back and say:
  âwhen the customer first has the idea for a featureâ. This is all very well
  for a high priority feature, but how about something that isn't that urgent,
  and thus sits in a triage area for a few weeks before being ready to enter
  development. Do we start the clock when the team first places the feature on
  the card wall
  and we start to seriously work on it?


I also run into the phase **lead time**, sometimes instead of
  âcycle timeâ, but often together - where people make a distinction between the
  two, often based on a different start time. However there isn't any
  consistency between how people distinguish between them. So in general, I
  treat âlead timeâ as a synonym to âcycle timeâ, and if someone is using both,
  I make sure I understand how that individual is making the distinction.


The different bands of cycle time all have their advantages, and it's often
  handy to use different bands in the same situation, to highlight differences.
  In that situation, I'd use a distinguishing adjective (e.g. âfirst-commit cycle
  timeâ vs âidea cycle timeâ) to tell them apart. There's no generally accepted
  terms for such adjectives, but I think they are better than trying to
  create a distinction between âcycle timeâ and âlead timeâ.


What these questions tell us is that cycle time, while a useful concept, is
  inherently slippery. We should be wary of comparing cycle times between teams,
  unless we can be confident we have consistent notions of their stop and start times.


But despite this, thinking in terms of cycle time, and trying to minimize
  it, is a useful activity. It's usually worthwhile to build a value stream map
  that shows every step from idea to production, identifying the steps in the
  work flow, how much time is spent on them, and how much waiting between them.
  Understanding this flow of work allows us to find ways to reduce the cycle
  time. Two commonly effective interventions are to reduce the size of features
  and (counter-intuitively) increase [Slack](https://martinfowler.com/bliki/Slack.html). Doing the work to
  understand flow to improve it is worthwhile because
  the faster we get ideas into production, the more
  rapidly we gain the benefits of the new features, and get the feedback to
  learn and improve our ways of working.


## Further Reading


The best grounding on understanding cycle time and how to reduce it is
    [The Principles of Product Development Flow](https://www.amazon.com/gp/product/1935401009/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1935401009&linkCode=as2&tag=martinfowlerc-20)


## Notes


1: It also avoids work being stuck in late
    activities such as testing and integration, which were notoriously difficult
    to estimate.


## Acknowledgements

Andrew Harmel-Law, Chris Ford, James Lewis, JosÃ© Pinar, Kief Morris, Manoj Kumar M, Matteo
    Vaccari, and Rafael Ferreira discussed this post
    on our internal mailing list