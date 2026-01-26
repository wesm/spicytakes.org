---
title: "Opportunistic Refactoring"
description: "From the very beginning of when I started to talk and write about   refactoring people have asked me how it should be incorporated into   the wider software development process. Should there be refact"
date: 2011-11-01T00:00:00
tags: ["refactoring"]
url: https://martinfowler.com/bliki/OpportunisticRefactoring.html
slug: OpportunisticRefactoring
word_count: 1094
---


From the very beginning of when I started to talk and write about
  refactoring people have asked me how it should be incorporated into
  the wider software development process. Should there be refactoring phases in
  the software development lifecycle, what proportion of an iteration
  should be devoted to refactoring tasks, how should we figure out who
  should be assigned to refactoring duties? Although there are places
  for some scheduled refactoring efforts, I prefer to encourage
  refactoring as an opportunistic activity, done whenever and wherever
  code needs to cleaned up - by whoever.


![](images/opportunisticRefactoring/sketch.png)


What this means is that at any time someone sees some code that
  isn't as clear as it should be, they should take the opportunity to fix it right there and
  then - or at least within a few minutes. This opportunistic
  refactoring is often referred to  as following the camp site rule
  - always leave the code behind in a better state than you found it. 
  If everyone on the team is doing this, they make small regular
  contributions to code base health every day.


This opportunity can come at various parts of implementing some
  new functionality or fixing a bug. One is a preparatory refactoring, where before
  you begin to implement something you see that this task would be
  easier if an existing class's API was structured differently. You
  first refactor it to how it ought to be and then start adding your
  functionality.


As you add the functionality, you realize that some code you're
  adding contains some duplication with some existing code, so you
  need to refactor the existing code to clean things up. This
  continuous attention to the code is important - but do remember that
  you should only refactor when your tests are green.


You may get something working, but realize that it would be
  better if the interaction with existing classes was changed. Take
  that opportunity to do that before you consider yourself done.


Sometimes you see an opportunity when you're in the middle of
  something else. Rather than interrupt your current thought it's
  useful to make a note of it and come back to it when you are ready.
  Don't leave it for long, come back the same day, before you've hit
  that final point of being done.


Some people object to such refactoring as taking time away from
  working on a valuable feature. But the whole point of refactoring is
  that it makes the code base easier to work with, thus allowing the
  team to add value more quickly. If you don't spend time on taking
  your opportunities to refactor, then the code base gradually
  degrades and you're faced with slower progress and difficult
  conversations with sponsors about refactoring iterations.


There is a genuine danger of going down a rabbit hole here, as
  you fix one thing you spot another, and another, and before long
  you're deep in yak hair. Skillful opportunistic refactoring requires
  good judgement, where you decide when to call it a day. You want to
  leave the code better than you found it, but it can also wait for
  another visit to make it the way you'd really like to see it. If you
  always make things a little better, then repeated applications will
  make a big impact that's focused on the areas that are frequently
  visited - which are exactly the areas where clean code is most
  valuable. Like most aspects of programming this decision requires
  thoughtfulness.


One of the features of opportunistic refactoring is that it can
  hit any part of the code base you're working in. You may be doing
  most of your work in one class, but spot problems in a class that's
  in a quite different area of the code. That lack of locality
  shouldn't stop you from making the change now. There's often a
  temptation to leave a change in another part of a code base to
  another day - but another day often doesn't come.


Refactoring does depend on having a good regression suite and
  it's wise to be wary if you think you're about to touch part of an
  application that's weaker on its tests than it should be. In this
  case remember that it's quite reasonable to throw in an extra test
  or two if you can do that without straying too far down the rabbit
  hole. I also find that making a deliberate error to see if a test
  catches it can be a way to get a feel for how good your safety net
  is.


I'm wary of any development practices that cause friction for
  opportunistic refactoring such as strong [CodeOwnership](https://martinfowler.com/bliki/CodeOwnership.html) or
  using a [FeatureBranch](https://martinfowler.com/bliki/FeatureBranch.html). This is actually my primary
  concern with using feature branching . Often when people are working
  with feature branches, they are discouraged from opportunistic
  refactoring because it makes merges more difficult 1 - particularly if the branches live longer than a
  couple of days.


1: 
      Modern tooling helps, but still gets tripped by [SemanticConflicts](https://martinfowler.com/bliki/SemanticConflict.html).


My sense is that most teams don't do enough refactoring, so it's
  important to pay attention to anything that is discouraging people
  from doing it. To help flush this out be aware of any time you feel
  discouraged from doing a small refactoring, one that you're sure
  will only take a minute or two. Any such barrier is a smell that
  should prompt a conversation. So make a note of the discouragement
  and bring it up with the team. At the very least it should be
  discussed during your next retrospective.


From the beginning I've always seen refactoring as something you
  do continuously, as regular and indivisible a part of programming as
  typing if statements. Yet there's a common misconception about
  refactoring in that it's something that needs to be planned out.
  Certainly there is a place for planned efforts at refactoring, even
  setting aside a day or two to attack a gnarly lump of code that's
  been getting in everyone's way for a few months. But a team that's
  using refactoring well should hardly ever need to plan refactoring,
  instead seeing refactoring as a constant stream of small adjustments
  that keep the project on the happy curve of the
  [DesignStaminaHypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html)


## Further Reading


My infodeck on [Workflows of Refactoring](https://martinfowler.com/articles/workflowsOfRefactoring/) talks about different
    ways you can use incorporate refactoring into your work.


Ron Jeffries came up with a [lovely visualization](http://ronjeffries.com/xprog/articles/refactoring-not-on-the-backlog//) to describe
    gradually refactoring through messy code and why you shouldn't
    have refactoring tasks on your backlog.


The metaphor of [TechnicalDebt](https://martinfowler.com/bliki/TechnicalDebt.html) fits in very well with these
    issues.


## Notes


1: 
      Modern tooling helps, but still gets tripped by [SemanticConflicts](https://martinfowler.com/bliki/SemanticConflict.html).
