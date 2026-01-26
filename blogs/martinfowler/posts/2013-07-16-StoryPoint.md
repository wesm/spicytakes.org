---
title: "Story Point"
description: "Story points are a common name for sizing stories in agile   projects. Combined withXpVelocitythey provide a   technique to aid planning by providing a forecast of when stories   can be completed."
date: 2013-07-16T00:00:00
tags: ["estimation"]
url: https://martinfowler.com/bliki/StoryPoint.html
slug: StoryPoint
word_count: 622
---


Story points are a common name for sizing stories in agile
  projects. Combined with [XpVelocity](https://martinfowler.com/bliki/XpVelocity.html) they provide a
  technique to aid planning by providing a forecast of when stories
  can be completed.


When estimating work, a common approach is to estimate in terms
  staff-hours, such as a programmer saying âthis will take me two days
  to doâ. Many people in the early days of agile, especially those in
  the [ExtremeProgramming](https://martinfowler.com/bliki/ExtremeProgramming.html) community, found that teams struggled to
  come up with useful estimates using this approach, even when they
  applied an approach of [IdealTime](https://martinfowler.com/bliki/IdealTime.html). We found the
  most effective way to estimate was to size stories relative to each
  other, and then use past experience to determine how much could be
  done in an iteration. 1


1: 
      âStory Pointsâ is the most common name that I hear these days,
      but various terms have been used over the years, often with
      whimsical names that emphasized their arbitrary nature. I
      particularly like Joseph Pelrine's **gummi bears** and
      Josh Kerievsky's: **NUTs** (Nebulous Units of Time).


To determine the points for a story, we compare rough relative
  sizes. If we are estimating the âfibble the foobarâ story, we look
  for a story of similar size that we've already estimated. We sense
  it's about the same size as âflipping the synergy bitâ. Then we look
  at the story point score for âflipping the synergy bitâ and
  score the âfibble the foobarâ the same amount.


A team using story points uses a small range of story points to
  work with. Common examples might be 1,2,4,8 or 1,2,3,5,8 2.
  Often the top number in the series represents âtoo bigâ and should
  be broken down further. 3


2: 
      This is a Fibonacci sequence


3: 
      Using the top number as too big is saying that a story
  sized at '8' really means '8 or more'. If you do this beware of
  using this top number when making forecasts of things like
  completion time, since '8' can turn into all sorts of numbers when
  it finally gets broken down. It's usually better to explicitly say
  its too big to be estimated rather than use a false marker number.


Allocating story points should be rapid activity. Discussion
  should only break out when people have contrasting views on the
  estimate, in which case its useful to have a discussion as it
  usually means that something about the story isn't clear. Using a
  [ThrownEstimate](https://martinfowler.com/bliki/ThrownEstimate.html) is a good technique to move things along
  quickly.


To form a plan with time, you use [XpVelocity](https://martinfowler.com/bliki/XpVelocity.html).


Some teams don't like using story points, preferring instead to
  use [StoryCounting](https://martinfowler.com/bliki/StoryCounting.html). I don't have a preference between the
  two - both seem to work equally well so it's up to the team to try
  out and go with whichever suits them best.


## Further Reading


Kent and I discussed story points in more depth 
    in the [tasteful green book](https://martinfowler.com/books/pxp.html). Most
    books that talk about planning and estimation in an agile context
    discuss story points in more detail.


## Notes


1: 
      âStory Pointsâ is the most common name that I hear these days,
      but various terms have been used over the years, often with
      whimsical names that emphasized their arbitrary nature. I
      particularly like Joseph Pelrine's **gummi bears** and
      Josh Kerievsky's: **NUTs** (Nebulous Units of Time).


2: 
      This is a Fibonacci sequence


3: 
      Using the top number as too big is saying that a story
  sized at '8' really means '8 or more'. If you do this beware of
  using this top number when making forecasts of things like
  completion time, since '8' can turn into all sorts of numbers when
  it finally gets broken down. It's usually better to explicitly say
  its too big to be estimated rather than use a false marker number.
