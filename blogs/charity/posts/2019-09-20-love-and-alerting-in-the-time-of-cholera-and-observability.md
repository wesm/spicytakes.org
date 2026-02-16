---
title: "Love (and Alerting) in the Time of Cholera (and Observability)"
date: 2019-09-20
url: https://charity.wtf/2019/09/20/love-and-alerting-in-the-time-of-cholera-and-observability/
word_count: 1424
---


I made a vow this year to post one blog post a month, then I didn’t post anything at all from May to September.  I have some catching up to do.  😑   I’ve also been meaning to transcribe some of the twitter rants that I end up linking back to into blog posts, so if there’s anything you especially want me to write about, tell me now while I’m in repentance mode.


This is one request I happened to make a note of because I can’t believe I haven’t already written it up!  I’ve been saying the same thing over and over in talks and on twitter for years, but apparently never a blog post.


The question is: what is the proper role of alerting in the modern era of distributed systems?  Has it changed?  What are the updated best practices for alerting?


> [@mipsytipsy](https://twitter.com/mipsytipsy?ref_src=twsrc%5Etfw) I've seen your thoughts on dashboards vs searching but haven't seen many thoughts from you on Alerting. Let me know if I've missed a blog somewhere on that! 🙂
> — katy allred (@themindfulmommy) [August 26, 2019](https://twitter.com/themindfulmommy/status/1166034982059397120?ref_src=twsrc%5Etfw)


It’s a great question.  I want to wax philosophically about some stuff, but first let me briefly outline the way to modernize your alerting best practices:

1. implement observability
2. implement SLOs and/or end-to-end checks that traverse key code paths and correlate to user-impacting events
3. create a secondary channel (tasks, ticketing system, whatever) for “things that on call should look at soon, but are not impacting users yet” which does not page anyone, but which on call is expected to look at (at least) first thing in the morning, last thing in the evening, and midday
4. move as many paging alerts as possible to the secondary channel, by engineering your services to auto-remediate or run in degraded mode until they can be patched up
5. wake people up only for SLOs and health checks that correlate to user-impacting events


Or, in an even shorter formulation: **delete all your paging alerts, then page only on e2e alerts that mean users are in pain.  **Rely on debugging tools for debugging, and paging only when users are in pain.


To understand why I advocate deleting all your paging alerts, and when it’s safe to delete them, first we need to understand *why* have we accumulated so many crappy paging alerts over the years.


### Monoliths, LAMP stacks, and death by pagebomb


Here, let’s crib a couple of slides from one of my talks on observability.  Here are the characteristics of older monolithic LAMP-stack style systems, and best practices for running them:


The sad truth is, that when all you have is time series aggregates and traditional monitoring dashboards, you aren’t really debugging with science so much as you are relying on your gut and a handful of dashboards, using intuition and scraps of data to try and reconstruct an impossibly complex system state.


This works ok, as long as you have a relatively limited set of failure scenarios that happen over and over again.  You can just pattern match from past failures to current data, and most of the time your intuition can bridge the gap correctly.  Every time there’s an outage, you post mortem the incident, figure out what happened, build a dashboard “to help us find the problem immediately next time”, create a detailed runbook for how to respond to it, and (often) configure a paging alert to detect that scenario.


Over time you build up a rich library of these responses.  So most of the time when you get paged you get a cluster of pages that actually serves to help you debug what’s happening.  For example, at Parse, if the error graph had a particular shape I immediately knew it was a redis outage.  Or, if I got paged about a high % of app servers all timing out in a short period of time, I could be almost certain the problem was due to mysql connections.  And so forth.


### Things fall apart; the pagebomb cannot stand


However, this model falls apart fast with distributed systems.  There are just too many failures.  Failure is constant, continuous, eternal.  [Failure stops being interesting](https://www.infoq.com/news/2019/07/netflix-learn-from-incidents/).  It *has* to stop being interesting, or you will die.


Instead of a limited set of recurring error conditions, you have an infinitely long list of things that almost never happen …. except that one time they do.  If you invest your time into runbooks and monitoring checks, it’s wasted time if that edge case never happens again.


Frankly, any time you get paged about a distributed system, it should be a genuinely new failure that requires your full creative attention.  You shouldn’t just be checking your phone, going “oh THAT again”, and flipping through a runbook.  Every time you get paged it should be genuinely new and interesting.


> Oh damn this talk looks baller.  😍 "Failure is important, but it is no longer interesting" — [@this_hits_home](https://twitter.com/this_hits_home?ref_src=twsrc%5Etfw)… Netflix once again shining the light on where the rest of us need to get to over the next 3-5 years.  🙌🏅🎬 [https://t.co/OY40Y0BTSa](https://t.co/OY40Y0BTSa)
> — Charity Majors (@mipsytipsy) [July 7, 2019](https://twitter.com/mipsytipsy/status/1147692918339076097?ref_src=twsrc%5Etfw)


And thus you should actually have **drastically fewer paging alerts** than you used to.


### A better way: observability and SLOs.


Instead of paging alerts for every specific failure scenario, the technically correct answer is to define your SLOs (service level objectives) and page only on those, i.e. when you are going to run out of budget ahead of schedule.  But most people aren’t yet operating at this level of sophistication.  (SLOs sound easy, but are unbelievably challenging to do well; many great teams have tried and failed.  This is why we have built an SLO feature into Honeycomb that does the heavy lifting for you.  Currently alpha testing with users.)


If you haven’t yet caught the SLO religion, the alternate answer is that “you should only page on high level end-to-end alerts, the ones which traverse the code paths that make you money and correspond to user pain”.  Alert on the three golden signals: request rate, latency, and errors, and make sure to traverse every shard and/or storage type in your critical path.


That’s it.  Don’t alert on the state of individual storage instances, or replication, or anything that isn’t user-visible.


(To be clear: by “alert” I mean “paging humans at any time of day or night”.  You might reasonably choose to page people during normal work hours, but during sleepy hours most errors should be routed to a non-paging address.  Only wake people up for actual user-visible problems.)


Here’s the thing.  The reason we had all those paging alerts was because we depended on them to understand our systems.


[Once you make the shift to observability](https://thenewstack.io/observability-a-3-year-retrospective/), once you have rich instrumentation and the ability to swiftly zoom in from high level “there might be a problem” to identifying specifically what the errors have in common, or the source of the problem — you no longer need to lean on that scattershot bunch of pagebombs to understand your systems.  You should be able to confidently ask any question of your systems, understand any system state — even if you have never encountered it before.


With observability, you debug by systematically following the trail of crumbs back to their source, whatever that is.  Those paging alerts were a crutch, and now you don’t need them anymore.


### Everyone is on call && on call doesn’t suck.


I often talk about how modern systems require software ownership.  The person who is writing the software, who has the original intent in their head, needs to shepherd that code out into production and watch real users use it.  You can’t chop that up into multiple roles, dev and ops.  You just can’t.  Software engineers working on highly available systems need to be on call for their code.


But the flip side of this responsibility belongs to management.  If you’re asking everyone to be on call, it is your sworn duty to make sure that *on call does not suck*.  People shouldn’t have to plan their lives around being on call.  People shouldn’t have to expect to be woken up on a regular basis.  Every paging alert out of hours should be as serious as a heart attack, and this means allocating real engineering resources to keeping tech debt down and noise levels low.


And the way you get there is first invest in observability, then delete all your paging alerts and start over from scratch.


It works.  It really does. 🌈
