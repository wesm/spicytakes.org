---
title: "Timeboxed Iterations"
description: "A common approach withTimeboxed Iterationsis to   allocate as manyUserStoriesas possible to   each iteration in order to maximize the utilization of the staff involved.   Slack is the policy of delibe"
date: 2023-04-04T00:00:00
tags: ["agile", "process theory", "project planning"]
url: https://martinfowler.com/bliki/TimeboxedIterations.html
slug: TimeboxedIterations
word_count: 536
---


Timeboxed Iterations are a way to divide and schedule up the work on a
  project, particularly associated with agile software projects. The team breaks
  down the visible features of the software into [User
  Stories](https://martinfowler.com/bliki/UserStory.html), and breaks down time into fixed periods (e.g.
  one week), called iterations. They then schedule the stories by
  allocating them to the iterations. Stories are roughly estimated so that the
  team can figure out how many stories fit in an iteration.


Iterations are time-boxed, in that there is no mechanism to slip the end
  date of an iteration in order to complete any stories. If a story isn't
  completed within the next iteration, it is considered as not-done and the team
  creates a new story for the work remaining to complete it.


A good way to figure out the capacity of an iteration is to use [Yesterdays Weather](https://martinfowler.com/bliki/YesterdaysWeather.html). We set the capacity of future iterations to the
  amount of stories we completed in the last one. In practice it's wise to
  consider the last few iterations to smooth changes to the capacity number. The
  most obvious way to do that is to take the average of the last few iterations,
  but a better course is to use the *minimum* to provide valuable [Slack](https://martinfowler.com/bliki/Slack.html). This mechanism is a feedback loop that naturally
  self-calibrates.


An alternative approach to Timeboxed Iterations is [Continuous Flow](https://martinfowler.com/bliki/ContinuousFlow.html). Here there are no iterations, when a story is
  complete the team simply picks the next story from a prioritized list. Many
  people prefer this as it eliminates the effort needed to assign stories to
  iterations - you just pick the next one. But iterations provide a regular
  cadence that people find valuable in setting a rhythm for their work.


Iterations are most valuable due to their ability to make problems visible.
  The end of an iteration is a natural stopping function that provides a check
  against serious overrun, setting up a feedback loop for the quality of
  estimates. If a team regularly runs out of time to complete stories, or
  usually sees fraught rushes of work at iteration end - these are signals of
  snags in the team's way of working. This problem-signaling mechanism is
  especially valuable for teams that are struggling with good
  engineering practices. The best cure for these problems is to
  add more slack to work on the underlying issues, a cure that is sadly undervalued.


## Further Reading


Many books have been written on agile planning over the years, most of
    which are based on timeboxed iterations. My current recommendation is [The Art of Agile Development](https://www.amazon.com/gp/product/1492080691/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1492080691&linkCode=as2&tag=martinfowlerc-20) which goes into detail on choosing iteration
    length, figuring out capacity, tracking, and handling urgent requests. The
    relevant chapter on [task planning](https://www.jamesshore.com/v2/books/aoad2/task_planning) is available on his site.


I might also mention my own book on [Planning Extreme
    Programming](https://martinfowler.com/books/pxp.html) which I co-wrote with Kent Beck early this century.
    Although I'd like to think the soaring elegance of our Anglo-West-Coast prose
    is never to be surpassed in the genre, these days I would turn to [The Art of Agile Development](https://www.amazon.com/gp/product/1492080691/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1492080691&linkCode=as2&tag=martinfowlerc-20) instead.


## Acknowledgements


Alexander Steinhart, Ana Lallena, Andrew Thal, David Jetter, Ian
    Cartwright, James Shore, John Hearn, Kennedy Collins, Kief
    Morris, and Premanand Chandrasekaran discussed this post on our internal mailing list
