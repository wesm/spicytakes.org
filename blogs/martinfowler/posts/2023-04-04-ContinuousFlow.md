---
title: "Continuous Flow"
description: "Continuous flow is an approach to scheduling work, often associated with   agile software development. The team breaks down the features of the software   intoUser Stories. They then prioritize   thes"
date: 2023-04-04T00:00:00
tags: ["project planning"]
url: https://martinfowler.com/bliki/ContinuousFlow.html
slug: ContinuousFlow
word_count: 332
---


Continuous flow is an approach to scheduling work, often associated with
  agile software development. The team breaks down the features of the software
  into [User Stories](https://martinfowler.com/bliki/UserStory.html). They then prioritize
  these stories into a crude list. The team then takes some of these user
  stories and works on them, when they complete one, they pull the next one off
  the list.


When working with continuous flow, it's useful to set a work-in-progress
  limit (WIP Limit) of how many stories the team can work on. Once they reach
  the WIP limit, they can't start any more stories until they complete one
  already in progress. WIP limits are important because they keep the team
  focused on finishing stories, otherwise it's too easy to build up a pile of
  “nearly done” work.


Continuous flow is well suited for a unpredictable stream of work - such as
  bug fixing and maintenance tasks. But in such cases be careful to keep the
  team large enough to be able to respond promptly to surges, which also means
  that in quieter times the team will have [Slack](https://martinfowler.com/bliki/Slack.html) to use to improve their working
  environment. If a continuous flow team is always busy, that's usually a red
  flag.


Continuous flow is an alternative to [Timeboxed Iterations](https://martinfowler.com/bliki/TimeboxedIterations.html), with the advantage that the team doesn't need to
  go through an exercise of allocating stories to iterations, estimating
  stories, or figuring out the iteration capacity. However such teams often run
  into difficulties because the regular cadence of iterations provide a feedback
  loop that helps a team spot problems such as cruft building up in the code
  base or sinking time into stories that are much larger than expected.
  Consequently continuous flow is effective for skilled teams that want to
  reduce the ceremony in their work, but less experienced teams are better off
  with iterations.


My colleague Kennedy Collins observed that continuous flow
  is good for the unpredictable *arrival* of work, but less so when the
  *nature* of the work is unpredictable or poorly understood.
