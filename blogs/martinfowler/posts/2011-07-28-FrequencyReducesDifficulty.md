---
title: "Frequency Reduces Difficulty"
description: "One of my favorite soundbites is:if it hurts, do it more often. It has the happy property of seeming nonsensical on the surface, but yielding some valuable meaning when you dig deeper"
date: 2011-07-28T00:00:00
tags: ["agile", "continuous delivery", "productivity", "process theory"]
url: https://martinfowler.com/bliki/FrequencyReducesDifficulty.html
slug: FrequencyReducesDifficulty
word_count: 547
---


One of my favorite soundbites is: **if it hurts, do it more
often**. It has the happy property of seeming nonsensical on the
surface, but yielding some valuable meaning when you dig deeper


An example context for this is integration. Most programmers learn
early on that integrating their work with others is a frustrating and
painful experience. The natural human response, therefore, is to put
off doing it for as long as possible.


The rub, however, is that if we were able to plot pain versus time
between integrations, we'd see a graph like this


![](images/frequency-reduces-difficulty/graph.png)


If you have this kind of exponential relationship, then if you do
it more frequently, you can drastically reduce the pain. And this is
what happens with [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) - by integrating every day,
the pain of integration almost vanishes. It did hurt, so you did it more
often, and now it no longer hurts.


This idea of doing painful things more frequently crops up a lot in
agile thinking. Testing, refactoring, database migration,
conversations with customers, planning, releasing - all sorts of
activities are done more frequently.


What is it that causes this effect? I think there are three broad
reasons. Firstly most of these tasks become much more difficult as the
amount to do increases, but when broken up into smaller chunks they
compose easily. Database migrations are a great example of this.
Specifying a large database migration involving multiple tables is
hard and error prone. But if you take it one small change at a time
it's much easier to get each one correct. Furthermore you can string
small migrations together easily into a sequence. Thus when you
decompose a large migration into a sequence of little ones, it all
becomes much easier to handle. This is the essence of [database refactoring](../books/refactoringDatabases.html).


Feedback is a second reason. Much of agile
thinking is about setting up feedback loops so that we can learn more
quickly. Feedback was an explicit value of Extreme Programming, and at
the heart of [Ken Schwaber's discussion](https://www.amazon.com/gp/product/0130676349/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0130676349&linkCode=as2&tag=martinfowlerc-20)
of the difference between defined and empirical process control. In a
complex process, like software development, you have to frequently
check where you are and make course corrections. To do this you must
look for every opportunity to add feedback loops and increase the
frequency with which you get feedback so you can adjust more quickly.


A third reason is practice. With any activity, we improve as we do
it more often. It's often said that the key to getting good surgery
is to find a surgeon who does the procedure frequently. Practice helps
you iron out the kinks in your process, and makes you more familiar
with signs of something going awry. If you reflect on what you are
doing, you also come up with ways to improve your practice. With
software there's also the potential for automation. Once you've done
something a few times, it's both easier to see how to automate it, and
you are more motivated to automate it. Automation is especially
helpful because it can increase speed and reduce the chance for error.


So whenever you're faced with a painful activity, ask yourself if
these forces apply. If so increasing the frequency can make you more
effective and remove a source of stress.
