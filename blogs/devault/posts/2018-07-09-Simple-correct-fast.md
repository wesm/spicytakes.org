---
title: "Simple, correct, fast: in that order"
date: 2018-07-09
url: https://drewdevault.com/2018/07/09/Simple-correct-fast.html
slug: Simple-correct-fast
word_count: 445
---

The single most important quality in a piece of software is simplicity. It’s
more important than doing the task you set out to achieve. It’s more important
than performance. The reason is straightforward: if your solution is not simple,
it will not be correct or fast.

Given enough time, you’ll find that all software which solves sufficiently
complex problems is going to (1) have bugs and (2) have performance problems.
Software with bugs is incorrect. Software with performance problems is not fast.
We will face this fact as surely as we will face death and taxes, and we should
prepare ourselves accordingly. Let’s consider correctness first.

Complicated software breaks. Simple software is more easily understood and far
less prone to breaking: there are less moving pieces, less lines of code to keep
in your head, and fewer edge cases. Simple software is more easily tested as
well - after all, fewer code paths to run through. Sure, simple software  *does* 
break, and when it does the cause and appropriate solution are often apparent.

Now let’s consider performance. You may have some suspicions about your
bottlenecks when you set out, and you should consider them in your approach.
However, when the performance bill comes due, you’re more likely to have
overlooked something than not. The only way to find out for sure what’s slow is
to measure. Which is easier to profile: a complicated program, or a simple one?
Anyone who’s looked at a big enough flame graph knows exactly what I’m talking
about.

Perhaps complicated software once solved a problem. That software needs to be
maintained - what is performant and correct today will not be tomorrow. The
workload will increase, or the requirements will change. Software is a living
thing! When you’re stressed out at 2 AM on Tuesday morning because the server
shat itself because your 1,831st new customer pushed the billing system over the
edge, do you think you’re well equipped to find the problem in a complex piece
of code you last saw a year ago?

When you are faced with these problems, you must seek out the simplest way they
can be solved. This may be difficult to do: perhaps the problem is too large, or
perhaps you were actually considering the solution before considering the
problem. Though difficult it may be, it is your most important job. You need to
take problems apart, identify smaller problems within them and ruthlessly remove
scope until you find the basic problem you can apply a basic solution to. The
complex problem comes later, and it’ll be better served by the composition of
simple solutions than with the application of a complex solution.
