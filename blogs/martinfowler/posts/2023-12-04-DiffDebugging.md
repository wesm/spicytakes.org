---
title: "Diff Debugging"
description: "Regression bugs are newly appeared bugs in features of the software that have been around   for a while. When hunting them, it usually valuable to figure out which change   in the software caused them"
date: 2023-12-04T00:00:00
tags: ["continuous delivery", "version control"]
url: https://martinfowler.com/bliki/DiffDebugging.html
slug: DiffDebugging
word_count: 432
---


Regression bugs are newly appeared bugs in features of the software that have been around
  for a while. When hunting them, it usually valuable to figure out which change
  in the software caused them to appear. Looking at that change can give
  invaluable clues about where the bug is and how to squash it. There isn't a
  well-known term for this form of investigation, but I call it Diff Debugging.


Diff debugging only works if we have our code in version control, but
  fortunately these days that's the norm. But there are some more things that
  are needed to make it work effectively. We need [Reproducible Builds](https://martinfowler.com/bliki/ReproducibleBuild.html), so that we can run old versions of
  the software easily. It helps greatly to have small commits, due to [high-frequency
  integration](https://martinfowler.com/articles/branching-patterns.html#integration-frequency). That way when we find the guilty commit, we can more easily
  narrow down what happened.


To find the commit that bred the bug, we begin by finding any past version
  without the bug. Mark this as a *last-good* version and the current
  version as the *earliest-bad*. Then find the commit half-way between the
  two and see if the bug is there. If so then this commit becomes the earliest-bad,
  otherwise it becomes the last-good. Repeat the process (which is a
  “half-interval” or “binary” search) until we've got the guilty commit.


If we use git, then the [git
  bisect](https://git-scm.com/docs/git-bisect/) command will automate much of this for us. If we can write a test
  that will show the presence of the bug, then git bisect can use that too,
  automating the whole process of finding the guilty commit.


I often find diff debugging to be useful within a programming session. If I
  have slow tests that take a few minutes to run, I might program for
  half-an-hour running only a subset of the most relevant tests. As long as I
  commit after every green test run, I can use diff debugging should one of
  those slower tests fail. Such is the value of committing extremely frequently,
  even if they are so small that I feel its best to squash them for the long-term
  history. Some IDEs make this easier by keeping a local history automatically
  that is finer-grained than the commits to version control.


## Revisions


I originally posted this page on 2004-06-01. In its original form it was
    more of a casual experience report. I rewrote it on 2023-12-04 to make it
    more like a definition of the term. Diff debugging isn't a term that's
    caught on much in the industry, but I haven't seen a another term generally
    used to describe it.
