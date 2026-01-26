---
title: "Threshold Test"
description: "A threshold test is a test inserted into aDeploymentPipelinethat monitors some measurable   phenomenon by comparing the value in the current build against a   threshold value. Should the current build"
date: 2013-09-12T00:00:00
tags: ["test categories"]
url: https://martinfowler.com/bliki/ThresholdTest.html
slug: ThresholdTest
word_count: 357
---


A threshold test is a test inserted into a
  [DeploymentPipeline](https://martinfowler.com/bliki/DeploymentPipeline.html) that monitors some measurable
  phenomenon by comparing the value in the current build against a
  threshold value. Should the current build's value pass the
  threshold, the test fails, failing the build.


![](images/thresholdTest/sketch.png)


A common example use of threshold tests are in performance. The
  team takes a representative set of operations and times them. They
  then set a threshold test to fail should these operations take some
  significant amount of time greater than this current value.
  Thresholds like this are handy for spotting cases where a commit
  introduces a performance degradation. In data-intensive applications
  these often occur due to badly written queries or poor use of
  indexing.


By having a threshold test you can spot this kind of problem when it's
  first introduced. This makes it easier to fix, since you know it's
  this commit which caused the failure - which cuts down where you
  have to search for the problem. Furthermore maintaining a threshold test
  prevents these kinds of problems building up in the code base. If
  you have many of these poor queries, then it's easier for more to
  creep in since their effects are obscured by the ones already present.


Threshold tests can be used with [ratcheting](https://martinfowler.com/articles/useOfMetrics.html#MetricsAsARatchet),
  where you steadily tighten the threshold over time to improve the
  value. So each time you add a commit that improves performance,
  you'd lower the threshold. This should help gradually improve
  performance over time. Using threshold tests with ratcheting is
  particularly helpful when you begin in a poor place and starting a
  program of improvement.


There are times when a threshold test will fail and the team
  decides the threshold is too aggressive and relaxes the threshold.
  Depending on the circumstances that may be the right thing to do -
 the threshold test helps here by making this decision a conscious one.


## Further Reading


Threshold tests are a way to follow the principles of âFavor
   tracking trends over absolute numbersâ and âUse shorter tracking
   periodsâ from [An Appropriate
   Use of Metrics](https://martinfowler.com/articles/useOfMetrics.html)


For general advice on testing cross-functional requirements,
   take a look at [Chapter 9
   of Continuous Delivery](https://martinfowler.com/books/continuousDelivery.html).
