---
title: "Pending Head"
description: "I'm a big fan ofContinuous Integration, it's an relatively simple   practice that can make a huge difference to most development   teams. However like most practices it has its flaws^H^H^H^H^H   oppor"
date: 2007-04-26T00:00:00
tags: ["continuous delivery", "version control"]
url: https://martinfowler.com/bliki/PendingHead.html
slug: PendingHead
word_count: 506
---


I'm a big fan of [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html), it's an relatively simple
  practice that can make a huge difference to most development
  teams. However like most practices it has its flaws^H^H^H^H^H
  opportunities for improvement. [Paul Duvall](http://www.testearly.com/category/duvall/), author of the
  [soon-to-be-standard book](https://martinfowler.com/books/duvall.html) on the subject, [pointed out](http://www.testearly.com/2007/04/25/the-future-of-continuous-integration/) one of these
  recently. If the commit build breaks, the whole team is affected and
  potentially slowed until it's fixed.


When we first started doing Continuous Integration at
  Thoughtworks, this one of the of the things that worried me about
  the way we were doing it. It worried me because there was an
  important difference between between the Thoughtworks 2000 style and
  the style we'd used at [C3](https://martinfowler.com/bliki/C3.html).


The Thoughtworks 2000 style is pretty much the canonical style of
  CI used today. Once you are happy with your work you commit it to
  the repository, and then build it on the build machine (either manually or
  with a CI server like CruiseControl). The problem lies if your
  commit is bad, anyone who updates will get failing code until you
  fix it.


In the C3 way of doing it we didn't commit to the head of
  repository directly. C3 was a Smalltalk project and used Envy, a
  Smalltalk-oriented repository system. Envy had some different
  concepts to mainstream repositories. Since it's ages since I used it
  my memory on exactly how it worked has gone all fuzzy, but the basic
  idea was that when you were working on your feature you committed to
  editions. An edition was like a private branch, visible to everyone
  but not blessed. Only when you had a successful build on the build
  machine would you upgrade your edition into a release, which was the
  equivalent to the mainline. This way you never got broken code into the
  mainline of the project.


Envy made it easy to work this way, the version control systems
we mostly use now make it more tricky. Ideally you want to create a
working copy that updates from the true head (to keep you in sync) but commits
to a different pending-head branch. Only a successful integration build can
actually commit to the true project head. A continuous integration
server would check out from the pending head and, if successful,
commit to the true head.


How difficult is it to set something like this up yourself? I'm
not sure, I haven't chatted with a team that's done it. However a
number of team oriented tools are providing this kind of capability.
For example JetBrains's [TeamCity](http://www.jetbrains.com/teamcity/) does it under
the name âdelayed commitâ. Paul also mentions  Borland's Gauntlet.


The other question is how much it matters. Despite my worries we
  didn't get enough pain from broken builds to want to install a
  pending head in 2000. If you get a lot of broken integration builds
  there are other ways to fix it. Often the main problem is that
  people aren't doing a private build before they commit. As usual the
  people-issue is often a more important issue to deal with before
  introducing more complicated technology.
