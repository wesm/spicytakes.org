---
title: "Xp Velocity"
description: "Story points are a common name for sizing stories in agile   projects. Combined withXpVelocitythey provide a   technique to aid planning by providing a forecast of when stories   can be completed."
date: 2013-07-16T00:00:00
tags: ["extreme programming", "project planning", "estimation"]
url: https://martinfowler.com/bliki/XpVelocity.html
slug: XpVelocity
word_count: 395
---


Velocity is a notion that helps
  calibrate a plan by tying broad statements of effort into elapsed
  time. Velocity is a statement of how much stuff a team (or a person
  if it's personal velocity) gets done in a time period. You should
  usually determine velocity by measuring how much got done in past
  periods, following the principle of [YesterdaysWeather](https://martinfowler.com/bliki/YesterdaysWeather.html). A
  typical approach is to average the velocity the past three time
  periods to determine velocity for future time periods. Velocity was
  originally formed as part [ExtremeProgramming](https://martinfowler.com/bliki/ExtremeProgramming.html) but has since
  spread  and is now used widely in [agile software development](https://martinfowler.com/agile.html) 
  of all flavors.


For example, a team is working in two week iterations and
  estimates effort for stories using [StoryPoints](https://martinfowler.com/bliki/StoryPoint.html). In its first three
  iterations its velocity was 22, 30, and 27. We would then say the
  velocity of the team is 26. To use this for future forecasting, we
  might add up all the stories we hope to complete for the first
  release, let's say that's 330. We can then say we forecast that,
  given the current plan, we will be able to release in 26 weeks time.
  (330 / 27 => 13 iterations).


Velocity is a tool for calibrating estimations for
  [YesterdaysWeather](https://martinfowler.com/bliki/YesterdaysWeather.html), it is not a measure of productivity.
  Different teams will use different baselines for their velocity
  units, so it's stupid to compare teams based on their velocities:
  there's no such thing as [StandardStoryPoints](https://martinfowler.com/bliki/StandardStoryPoints.html). Similarly
  velocity is a team measure, not an individual measure. [Using
  velocity as a productivity measure kills agility.](http://jimhighsmith.com/velocity-is-killing-agility/)


Velocity is commonly used with fixed iterations, but you can use
  the same idea with Kanban based planning. The amount of effort you
  get done in the last few weeks can be extrapolated the same way to
  come up with a forecast for future effort.


Velocity is a useful tool for estimation, one that's considerably
  less complicated to use than techniques I observed in the 80s.
  However, as with any estimation technique, it can be misused - you
  must always think about the [PurposeOfEstimation](https://martinfowler.com/bliki/PurposeOfEstimation.html).


I wrote a first version of this bliki entry in 2004-05-10.


## Further Reading


Most books on agile development will talk about planning and
    thus mention velocity. The [tasteful green book](https://martinfowler.com/books/pxp.html) has an early,
    in-depth descrption of velocity from Kent and me. You can still find our [initial
explanation of XP planning terminology](http://c2.com/cgi/wiki?XpPlanningTerminology) on the wiki.
