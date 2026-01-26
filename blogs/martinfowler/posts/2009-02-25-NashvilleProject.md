---
title: "Nashville Project"
description: "I spent some time recently with one of my favorite ever   Thoughtworks projects. It's a project that started in 1998, using   then new J2EE technology. Over the years it's had a fascinating   history:"
date: 2009-02-25T00:00:00
tags: ["testing", "experience reports", "legacy modernization"]
url: https://martinfowler.com/bliki/NashvilleProject.html
slug: NashvilleProject
word_count: 501
---


I spent some time recently with one of my favorite ever
  Thoughtworks projects. It's a project that started in 1998, using
  then new J2EE technology. Over the years it's had a fascinating
  history: starting with EJBs, ripping them out, going offshore to
  Bangalore, coming back to Chicago. Many people have moved in and out
  of the project and the project has varied in head-count between 6 and
  60. Overall the project has had over 300 staff-years of effort on
  it and weighs in at around 100 KLOC.


It's a favorite of mine because it exhibits an important property
  of my preferred view of software development: a long term support of
  a business function enabled by a well-designed code-base. The fact
  that they are still adding useful business value after ten years is
  an big dollop of kudos. They are able to rapidly add new features
  when needed so haven't fallen into the typical morass of a legacy app.


On this visit a couple of thoughts grabbed me.


Firstly they've had an interesting evolution in their approach to
  acceptance tests and how they update them as they add new
  features. In their original (and common) world view, each time you
  implement a new [UserStory](https://martinfowler.com/bliki/UserStory.html) you add one or more tests. This leads you to a
  simple tracing structure where each story is verified by one or more
  acceptance tests. But the problem with this approach is that over
  time the tests grow in complexity with much duplication.


In their new world view there is a suite of acceptance tests that
  describe the application behavior in
  [SpecificationByExample](https://martinfowler.com/bliki/SpecificationByExample.html) style. Each time they play a new
  story, they decide how to update this suite to reflect the new
  behavior. This breaks the simple story-to-test relationship, but
  results in a much simpler and coherent suite of tests.


The second interesting aspect of the project is how it continues
  to work at improving the code base. They came up with a good, if
  informal, metric for describing this. A few years
  ago, if they wanted to take on someone new they wanted that person
  committed for at least a year, so they could get contributions that
  would be worthwhile after coming up to speed on the code base. Now
  that time is down to three months. For a ten year old app with that
  many hands on it, that's quite an achievement.


For me the key purpose of good design is that it allows you to
  continue working rapidly with the code (the
  [DesignStaminaHypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html)). Assessing how long it takes a
  developer to be productive with a code base is a good way to sense
  this design quality. The minimum-commitment length metric is another
  spin on this same idea. It's not something we can measure
  objectively, but it is something that a team can consider looking
  at.


I'm hoping we'll get more people from the project talking about
  their experiences. They did do a podcast last year (go to
  [thoughtworks podcasts](http://www.thoughtworks.com/what-we-say/podcasts.html) and look for âKeeping Grey Code Fitâ).
