---
title: "Ideal Time"
description: "Ideal time was a term used in earlyExtremeProgrammingto help   with estimation of effort. It's been mostly superseded now byStoryPointsorStoryCounting."
date: 2013-07-16T00:00:00
tags: ["estimation"]
url: https://martinfowler.com/bliki/IdealTime.html
slug: IdealTime
word_count: 366
---


Ideal time was a term used in early [ExtremeProgramming](https://martinfowler.com/bliki/ExtremeProgramming.html) to help
  with estimation of effort. It's been mostly superseded now by
  [StoryPoints](https://martinfowler.com/bliki/StoryPoint.html) or [StoryCounting](https://martinfowler.com/bliki/StoryCounting.html).


When estimating effort for a task, it's common to estimate in
  terms of staff-time, such as a team saying âit will take 4 staff
  days to do thisâ, meaning it might take 2 people 2 days or one
  person 4 days.


One of the problems with this form of estimation is that you make
  it when thinking that you are working on the problem in a focused
  way, which ignores many of the other things people have to do as
  part of their job. Attending meetings, carrying out recruitment
  interviews, some customer support - all can reduce the amount of
  time you can focus on your programming tasks in a given day.


With ideal time you specifically estimate in terms of focused
  quality time âif I'm doing nothing else, how long would this take
  meâ. We then map from ideal time to actual time using a **load
  factor**. So if you only got 6 ideal hours of work done in an
  eight hour day, your load factor would be 6/8 (0.75). This way
  people could estimate without worrying about external factors and
  we multiply by the load factor to figure out how long in elapsed
  time a task should take.


This, of course, raises the question of how we determine the load
  factor. Our advice was to measure it by using [XpVelocity](https://martinfowler.com/bliki/XpVelocity.html).
  You'd do this by looking at recent iterations, taking all the
  stories that were delivered, adding up the ideal time, and comparing
  that to the elapsed time to determine the load factor. For example, we looked
  at the stories done last week and added up the ideal time for them to be 23
  hours. The elapsed time was 40 hours, so the load factor was 0.6
  (23/40 to one significant figure).


Using idea time fell out of favor since [StoryPoints](https://martinfowler.com/bliki/StoryPoint.html)
  were easier to calculate, less likely to be abused, and every bit as
  accurate.


## Further Reading


You can find some more information on ideal time in the
    [tasteful green book](https://martinfowler.com/books/pxp.html), although even by then we were preferring
    story points.
