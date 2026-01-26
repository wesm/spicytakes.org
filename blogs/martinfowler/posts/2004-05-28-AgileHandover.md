---
title: "Agile Handover"
description: "One of the most common questions I see about agile projects is how they deal with handover to another team. If you have a development team that leaves and hands over support to a support team, how do "
date: 2004-05-28T00:00:00
tags: ["agile", "continuous delivery"]
url: https://martinfowler.com/bliki/AgileHandover.html
slug: AgileHandover
word_count: 455
---


One of the most common questions I see about agile projects is
how they deal with handover to another team. If you have a development
team that leaves and hands over support to a support team, how do they
cope when agile projects tend to produce much less documentation than
plan-driven processes?


One thing to consider is to ask yourself how much useful
documentation gets produced by an alternative process. I've noticed
that processes that produce mandatory documentation often produce
stuff that isn't very helpful, and under the pressure of deadlines
tends not to be kept up to date. In many ways the agile approach is a
preference for a smaller amount of higher quality documentation.


Agile projects prefer face-to-face communication, so a common
approach I've come across is to bring in members of a
support/maintenance team to work with the development team for a while
before they depart. By spending some time with both teams present, the
development team could teach the system to the maintenance team as
they are working the system. I've come across a number of variations
on this theme.

- One team rotated one or two people in each iteration,
completely replacing the team in two or three months gradually.
- When we've [transferred
projects to India](https://martinfowler.com/articles/agileOffshore.html) we've ensured that an onshore developer spends
at least a couple of months offshore to work with the new team
- One team brought a support person onto the team for the last
month of the development.


The last example came from a colleague of mine, Jonathan
Rasmusson, who pointed out that another benefit of bringing in some
support team people at the end of the development was that it allowed
relationships to form that made it much easier to deploy the new
system. Communications between development and operations are often
strained; frequently the needs of operations are ignored by
developers. Having someone from operations be part of the team for a
while helps communications in both directions.


Which brings me back to documentation. One of the things Jonathan
mentioned was that they had the support member act as the customer for
the documentation of the system. As a result they produced much more
better documentation than they usually see.


Jonathan got to eat his own dog food later on when he came back
with a completely new team to do some enhancements. They found the
documentation very helpful because it was written on demand rather
than according to a process. Quality triumphed over the usual
quantity. The other big help in learning about the system was XP's
huge body of automated tests which - as XPers never tire of pointing
out - is an important form of documentation in its own right.
