---
title: "Deployment Pipeline"
description: "A threshold test is a test inserted into aDeploymentPipelinethat monitors some measurable   phenomenon by comparing the value in the current build against a   threshold value. Should the current build"
date: 2013-09-12T00:00:00
tags: ["continuous delivery", "build scripting"]
url: https://martinfowler.com/bliki/DeploymentPipeline.html
slug: DeploymentPipeline
word_count: 268
---


One of the challenges of an automated build and test environment
  is you want your build to be fast, so that you can get fast
  feedback, but comprehensive tests take a long time to run. A
  deployment pipeline is a way to deal with this by breaking up your
  build into stages. Each stage provides increasing confidence,
  usually at the cost of extra time. Early stages can find most
  problems yielding faster feedback, while later stages provide slower
  and more through probing. Deployment pipelines are a central part
  of [ContinuousDelivery](https://martinfowler.com/bliki/ContinuousDelivery.html).


Usually the first stage of a deployment pipeline will do any
  compilation and provide binaries for later stages. Later stages may
  include manual checks, such as any tests that can't be automated.
  Stages can be automatic, or require human authorization to proceed,
  they may be parallelized over many machines to speed up the build.
  Deploying into production is usually the final stage in a pipeline.


More broadly the deployment pipeline's job is to detect any
  changes that will lead to problems in production. These can include
  performance, security, or usability issues. A deployment pipeline
  should enable collaboration between the various groups involved in
  delivering software and provide everyone visibility about the flow
  of changes in the system, together with a thorough audit trail.


A good way to introduce continuous delivery is to model your
  current delivery process as a deployment pipeline, then examine this
  for bottlenecks, opportunities for automation, and collaboration points.


For more information see chapter 5 of the [Continuous Delivery book](https://martinfowler.com/books/continuousDelivery.html),
  available as a [free
  download](http://www.informit.com/articles/article.aspx?p=1621865).


## Acknowledgements

[Jez Humble](http://continuousdelivery.com/)
provided detailed help with this page.