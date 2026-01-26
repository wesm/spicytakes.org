---
title: "Feature Branch"
description: "A feature branch is a source code branching   pattern where a developer opens a branch when she starts working on a   new feature. She does all the work on the feature on this branch and   integrates "
date: 2020-05-07T00:00:00
tags: ["continuous delivery", "version control"]
url: https://martinfowler.com/bliki/FeatureBranch.html
slug: FeatureBranch
word_count: 348
---


A feature branch is a [source code branching
  pattern](https://martinfowler.com/articles/branching-patterns.html) where a developer opens a branch when she starts working on a
  new feature. She does all the work on the feature on this branch and
  integrates the changes with the rest of the team when the feature is done.


During the work, she may merge in changes confirmed by the rest of the team
  into her branch, in order to reduce her integration once the feature is
  complete, but she doesn't put her changes into the common codebase until that
  point. This has the consequence that two people, working on different feature
  branches, do not integrate their work until the second one merges their work
  into the common codebase.


Feature branches are a popular technique, particularly well-suited to
  open-source development. They allow all the work done on a feature to kept
  away from a teams common codebase until completion, which allows all the risk
  involved in a merge to be deferred until that point. However this isolation
  does prevent early detection of problems. More seriously, it also discourages
  refactoring - and a lack of refactoring often leads to serious deterioration
  in the health of a codebase.


The consequences of using feature branch depend greatly on how long it
  takes to complete features. A team that typically completes features in a day
  or two are able to integrate frequently enough to avoid the problems of
  delayed integration. Teams that take weeks, or months, to complete a feature
  will run into more of these difficulties.


## Further Reading


For more details on feature branching, see my long form article on [Patterns for Managing Source Code Branches](https://martinfowler.com/articles/branching-patterns.html). This sets
    the feature branching pattern into the broader picture of using branching in
    software development, breaks down the workflow of working on a feature
    branch, discusses the trade-offs involved with the frequency of integration,
    and explores the alternative of Continuous Integration.


## Revisions


I published my original post on this URL on 3 Sep 2009. When I published [Patterns for Managing Source Code
    Branches](https://martinfowler.com/articles/branching-patterns.html) I cut this page down to a short summary.
