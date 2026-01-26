---
title: "Estimated Interest"
description: "TechnicalDebtis a very useful concept, but it raises   the question of how do you measure it? Sadly technical debt isn't   like financial debt, so it's not easy to tell how far you are in   hock (alth"
date: 2008-12-10T00:00:00
tags: ["metrics", "technical debt", "project planning"]
url: https://martinfowler.com/bliki/EstimatedInterest.html
slug: EstimatedInterest
word_count: 420
---


[TechnicalDebt](https://martinfowler.com/bliki/TechnicalDebt.html) is a very useful concept, but it raises
  the question of how do you measure it? Sadly technical debt isn't
  like financial debt, so it's not easy to tell how far you are in
  hock (although we seem to have had some trouble with measuring the
  financial kind recently).


Here's one idea to consider. When a team completes a feature ask
  them to tell you how long it took them (the actual effort) and how
  long they think it would have taken if the system were properly
  clean. The difference between the two is the interest of the
  technical debt. (So if it actually took them 5 days but they think
  it would have taken them 3 days with a clean system, then you paid 2
  days of effort as interest on your technical debt.)


There are certainly some serious flaws with this technique. The
  statement of how long it would have taken on a clean system is an
  estimate based on an imaginary state - so is difficult to make
  objective. There's the effort in capturing this information, which
  is easy to get out of hand. But the result may help project a
  picture of the state of the code-base in a way that's visible to
  non-technical staff.


Furthermore it may also help with decisions about whether to pay
  the principal. Some teams like to add technical debt stories to
  their product backlog - with estimates on how long it would take to
  remove them. Such technical debt stories are also estimates, but
  also provide a picture of how much debt has built up. You could get
  a bit more clever with the estimated interest payments by
  apportioning them to these debt stories (I spent an extra day on
  this feature because of the bad state of the flipper
  module). Comparing interest payments with the principal may help
  inform a decision about whether to pay off the principal.


I ran into someone recently who tried something a little like
  this and found it handy, but it's not something I've run into a
  lot. Certainly there are flaws with doing it - but it may be worth a
  try for a few iterations.


**Update: **A recent discussion surfaced another way to
  capture the estimated interest.  During a retrospective (which wise
  teams do at the end of each iteration) capture an estimate of
  interest paid against each of the problem areas of the system. Doing
  this estimate against recent completed work may be easier than
  forward estimates against future stories.
