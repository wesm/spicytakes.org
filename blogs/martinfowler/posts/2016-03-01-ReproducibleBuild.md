---
title: "Reproducible Build"
description: "Infrastructure as code is the approach to defining computing and network   infrastructure through source code that can then be treated just like any software   system. Such code can be kept in source "
date: 2016-03-01T00:00:00
tags: ["continuous delivery", "build scripting", "version control"]
url: https://martinfowler.com/bliki/ReproducibleBuild.html
slug: ReproducibleBuild
word_count: 545
---


One of the prevailing assumptions that fans of [Continuous
  Integration](https://martinfowler.com/articles/continuousIntegration.html) have is that builds should be
  reproducible. By this we mean that at any point you should be able
  to take some older version of the system that you are working on and
  build it from source in exactly the same way as you did then.


This isn't called out as a key practices in the sources I usually
  refer to on the build process. I think that's because it's an
  underlying assumption - one that's considered so obvious there's no
  need to explain it.


One of the driving reasons to have reproducible builds is to
  ensure we can deal with problems in past releases that are still
  used. If we release software to a customer a year ago, and they now
  report a serious bug with it, it's important to be able to recreate
  that software so that we can deliver a fix.


But let's assume a case where you're releasing software every
  week to a hosted environment. Let's also assume you have a solid [Continuous
  Delivery](https://martinfowler.com/books/continuousDelivery.html) process and are thus confident that you promulgate bug
  fix by either waiting until the next release or(if really critical)
  doing an early release. Do you then still need reproducible
  builds?


In a scenario where you: receive a bug report, reproduce the bug
  on head, fix it on head and either wait or immediately release -
  then you don't. But there are cases when it's still very handy to
  have reproducible builds.


What happens when you get a bug report and you can't reproduce
  it. Do you just declare it fixed and move in? I wouldn't be happy
  with that response. Firstly I'd want to be sure I really understood
  the bug - so I'd want to check out the released version of the
  software, build it, and ensure I could then reproduce it. To
  be confident in reproducing the bug, I'd need to reproduce the
  build. Furthermore even if I'm confident that the bug got fixed *en
  passant* during recent development, I'd still argue that there's
  at least one test missing. I'd want to write that test and verify
  that it passes now and fails against the released build.


Another case is a regression. A customer contacts you and says
  there's a bug now that wasn't there before. Such bugs can hide a
  long time before they wake up and wave their feelers at you. Maybe
  it only occurs when the first of the month falls on a Monday. Either
  way you now have software that you think worked two months ago but
  now has a bug.


Here having reproducible builds gives you the ability to use
  [DiffDebugging](https://martinfowler.com/bliki/DiffDebugging.html). Your customer is pretty sure that you
  didn't have this problem two months ago, that was build 20000,
  you're now on build 28000. So you check out build 20000 and look to
  see if the bug is there. It isn't so you try build 24000, not there
  either, so next is 26000. Before long you know the bug first
  appeared with revision 26543 (modern version control systems [have](http://mercurial.selenic.com/wiki/BisectExtension) [features](http://www.kernel.org/pub/software/scm/git/docs/git-bisect.html)
  to help you do this). Now you look at the diffs between revision
  26543 and its parent - often this approach makes it much easier to
  find a bug.
