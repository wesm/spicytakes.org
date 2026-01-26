---
title: "Premature Ramp Up"
description: "One of the good things about software is that people seem to want   it, and want it quickly. It's usual for organizations to ask teams   to speed up production of software and from time to time the   "
date: 2011-11-10T00:00:00
tags: ["bad things", "team organization", "project planning"]
url: https://martinfowler.com/bliki/PrematureRampUp.html
slug: PrematureRampUp
word_count: 1039
---


One of the good things about software is that people seem to want
  it, and want it quickly. It's usual for organizations to ask teams
  to speed up production of software and from time to time the
  organization seeks to help in the way that really shows its
  commitment - by spending money to add more people to the team.


Now there's many an argument that's been had about the true benefit
  of adding people to a software team. It's clear to me that you don't
  get a linear benefit, doubling a team won't double its productivity
  because the communication and coordination costs kick in and blunt
  the increase. My utterly unscientific rule of thumb is that any
  increase in productivity is likely to be proportional to the square
  root of the increase in people, so doubling a team will get you
  roughly a 50% increase in productivity. But in practice this will
  vary a great deal depending on individual factors. There are some
  people I know who are likely to double the productivity of even a
  sizable team just on their own, and we have run into people who will
  reduce a team's productivity.


But the issue I want to highlight here is that of the ramp-up.
  You have a small team that's working well, but you want more
  software and you are prepared to spend the money to get it. You're
  happy to pay quadruple, even sextuple to double your rate of
  progress. An important, yet not well understood factor is the rate
  at which you can safely add people to a team.


More than once, I've come across projects who added too many
  people too quickly. This manifests itself in a breakdown of the
  cohesion of the code base itself. Duplication runs rampant, several
  friends of mine know about the project that had three
  object-relational mapping frameworks within a single application.
  This breakdown occurs because the new people don't understand
  how the code base currently works, so they do something at odds with
  it, like adding a competing framework. If there's too many new
  people around, the team leadership can't keep track of it all and
  the code base sprouts problems. These problems then reinforce each
  other because nobody can find a consistent way to do things, the
  Broken Windows syndrome kicks in and you get a positive feedback
  loop. (And positive feedback loops are usually a bad thing.)


On top of this an overly rapid ramp up leads to a break down of
  the human communication mechanisms. It takes time for people to get
  used to working with each other and a rapid ramp up can  stop a
  large team from forming the relationships it needs to succeed.


So how much ramp up can you safely do? It's difficult to give any
  concrete advice here, because any experienced project manager I ask
  always rightly points out that there are many variables that have to
  be taken into account. I pressed Joe Zenevitch, one of my most
  trusted PM sources, and he indicated that he would never want to
  more than double a team at once. Even doubling would be a risky
  call, with the risk increasing if the exisiting team was already a
  dozen or more people, or had a signficant amount of juniors.


If you do a significant increase in size you shouldn't add yet
  more people until the new folks have settled into the team. It will
  take a few weeks for this to happen. Developers need to get to know
  the code-base and the domain, BAs need to be familiar with the
  domain experts, everyone needs to get to know each other. At
  Thoughtworks we expect people to come up to speed quickly, after all
  we hire bright, high motivated people who are quick learners. But
  even so it still take a week or two. For most teams you should allow
  a good bit longer.


When you add people to a team, you don't get an immediate
  increase in capability. It takes time for people to become
  productive on a new project. Worse still existing staff have to
  spend time helping them get up to speed, so your [velocity](XpVelocity.html) may well drop at first. Joe Z's
  observation for Thoughtworks teams is that there will be no net
  effect for the first couple of weeks as the new people and hit for
  existing people cancel out. 1 Most
  ThoughtWorkers like to point out that pair programming is a big
  enabler to on-boarding people more rapidly. Pat Kua also has some [good
  advice](http://www.infoq.com/articles/pat-kua-onboarding-new) on how to bring new people onto a team effectively.


1: 
      This couple-of-weeks rule is for ThoughtWorkers, so we would
      expect it would take longer for people who don't match our
      hiring standards.


Another thing to watch is to not ramp-up too early in the
  project. One of the firmest bits of advice I've heard from people
  who do large projects (anything over 50 people) is that the project
  should start small, maybe with just a dozen or so developers. They
  should figure out the key design elements and interactions of the
  system by building early parts of it. Only once that design has
  settled down should you think of increasing the team size to its
  full size. As part of that settling down put time into 
  removing any design elements that you don't think should be copied.
  People will naturally copy stuff that's already there, so you should
  ensure that what's there is all going to make a good platform for
  further development. This is a time to err on the side of excessive
  attention to code-cleanliness.


Finally, when thinking of ramping up, think very carefully about
  whether it's worth it. I've rarely come across a large team where
  there isn't a feeling that the team could be significantly cut
  without reducing its productivity. As I once said [âscaling
  agile is the last thing you want to doâ.](https://martinfowler.com/articles/canScaling.html#MartinFowler)


## Further Reading


My colleague [Francisco Trindade talks](http://blog.franktrindade.com/2012/02/23/knowledge-sharing-on-steroids/) about a good experience he
    used for bringing on a few developers at once over a couple of weeks.


## Notes


1: 
      This couple-of-weeks rule is for ThoughtWorkers, so we would
      expect it would take longer for people who don't match our
      hiring standards.
