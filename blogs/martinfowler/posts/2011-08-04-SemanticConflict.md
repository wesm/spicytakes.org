---
title: "Semantic Conflict"
description: "Those who hear my colleagues and I talk aboutFeatureBranchknow that we're not big fans of that   pattern. An important part of our objection is the observation that   branching is easy, but merging is"
date: 2011-08-04T00:00:00
tags: ["continuous delivery", "bad things", "version control"]
url: https://martinfowler.com/bliki/SemanticConflict.html
slug: SemanticConflict
word_count: 836
---


Those who hear my colleagues and I talk about
  [FeatureBranch](https://martinfowler.com/bliki/FeatureBranch.html) know that we're not big fans of that
  pattern. An important part of our objection is the observation that
  branching is easy, but merging is hard. One argument we hear from
  time to time is that modern [VersionControlTools](https://martinfowler.com/bliki/VersionControlTools.html) make
  merging sufficiently easy that feature branching is worthwhile.


Certainly modern tools do a much better job of merging than in my
  youth. A good example of this power is merge-through-rename
  which can properly merge the situation where I change some of the contents of
  `lorem.rb`, while Jez changes its name to
  `ipsum.rb`.


This is all very well, but it only solves textual conflicts and does
  not help with semantic conflicts. By a semantic conflict I mean a
  situation where Jez and I make changes which can be safely merged on
  a textual level but cause the program to behave differently


The simplest example is that of renaming a function. Say I think
  that the method `clcBl` would be easier to work with if
  it were called
  `calculateBill`. With modern refactoring tools this is
  trivial: just press Shift+F6, type the new name, and the tool then
  changes all the callers. The problem appears, however, if Jez adds
  more calls to this method on his feature branch. When the two get
  merged, the textual merge will work fine, but the program will not
  run the same way.


![](images/semanticConflict/rename.png)


A method rename is a simple example, and is also easy to find in
  a statically typed language as it will fail to compile. But there
  are plenty of subtler semantic conflicts that won't merge so
  cleanly. Let's imagine I'm looking at that
  `calculateBill` method and realize that as well as
  calculating the bill, it also sends off accounting entries to the
  accounting system. I don't like the side effect, so I pull it
  out into a separate `notifyAccounting` method. I can then
  find all the callers of calculateBill and add a call to
  `notifyAccounting`. But Jez doesn't know about that in
  his branch.


So the first point here is that however powerful your tooling is,
  it will only protect you from textual conflicts 1. The particularly
  annoying point is that semantic conflicts are harder to spot and
  harder to fix.


1: 
      And if we change the exact same text, the merge tool usually
      can't help either unless you have something like git rerere.
      But that problem is much smaller than semantic conflicts.


We can't automatically resolve semantic conflicts. Maybe some day
  tools will be able to tackle some of them, but I suspect some gnarly
  ones will always be with us - at least until computers can read our
  mind and automatically deduce our intentions. There are, however, a
  couple of strategies that can significantly help us deal with them


The first of these is [SelfTestingCode](https://martinfowler.com/bliki/SelfTestingCode.html). Tests are
  effectively probing our code to see if their view of the code's
  semantics are consistent with what the code actually does. If Jez is
  expecting certain things to happen with the code he's calling and
  has tests for that, then they will break when he integrates. It's
  not a perfect response, of course. Tests can never be perfect, but
  they catch lots of semantic conflicts in practice. They also don't
  help with fixing the conflict once you've discovered it, but finding
  it is a big part of the battle


The other technique that helps is to merge more often. Jez's
  difficulties are much less if he discovers my change in a few hours
  rather than in a few days. That way he's no longer building a lot of
  code on the old semantics. This is why we are such big fans of [continuous
  integration](https://martinfowler.com/articles/continuousIntegration.html).


There seem to be two groups of people who promote the notion of
  tools make feature branching tolerable. One is purveyors of
  âenterprise gradeâ VCSs. We don't really care about them. The other
  group is fans of DVCSs (Distributed Version Control Systems). I get
  a bit more concerned about the latter group. Often people try to
  justify DVCSs based on how they make feature branching easy. But
  that misses the issues of semantic conflicts 2. There are lots of good
  reasons to use a DVCS, so there's no reason to couple a good tool to
  a problematic technique.


2: 
      If your features are built quickly, within a couple of days,
      then you'll run into less semantic conflicts (and if less than a
      day, then it's in effect the same as CI).  However we don't see
      such short feature branches very often.


## Notes


1: 
      And if we change the exact same text, the merge tool usually
      can't help either unless you have something like git rerere.
      But that problem is much smaller than semantic conflicts.


2: 
      If your features are built quickly, within a couple of days,
      then you'll run into less semantic conflicts (and if less than a
      day, then it's in effect the same as CI).  However we don't see
      such short feature branches very often.
