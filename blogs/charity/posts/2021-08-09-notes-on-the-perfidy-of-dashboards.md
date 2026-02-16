---
title: "Notes on the Perfidy of Dashboards"
date: 2021-08-09
url: https://charity.wtf/2021/08/09/notes-on-the-perfidy-of-dashboards/
word_count: 1282
---


The other day I said this on twitter —


> every dashboard is a sunk cost
> every dashboard is an answer to some long-forgotten question
> every dashboard is an invitation to pattern-match the past instead of interrogate the present
> every dashboard gives the illusion of correlation
> every dashboard dampens your thinking [https://t.co/OIEowa1COa](https://t.co/OIEowa1COa)
> — Charity Majors (@mipsytipsy) [July 19, 2021](https://twitter.com/mipsytipsy/status/1417168483662503952?ref_src=twsrc%5Etfw)


… which stirred up some Feelings for many people. 🙃  So I would like to explain my opinions in more detail.


### Static vs dynamic dashboards


First, let’s define the term. When I say “dashboard”, I mean STATIC dashboards, i.e. collections of metrics-based graphs that you cannot click on to dive deeper or break down or pivot. If your dashboard supports this sort of responsive querying and exploration, where you can click on any graph to drill down and slice and dice the data arbitrarily, then breathe easy — that’s not what I’m talking about. Those are great. (I don’t really consider them dashboards, but I have heard a few people refer to them as “dynamic dashboards”.)


Actually, I’m not even “against” static dashboards. Every company has them, including Honeycomb. They’re great for getting a high level sense of system functioning, and tracking important stats over long intervals. They are a good starting point for investigations. Every company should have a small, tractable number of these which are easily accessible and shared by everyone.


### Debugging with dashboards: it’s a trap


What dashboards are NOT good at is debugging, or understanding or describing novel system states.


I can hear some of you now: “But I’ve debugged countless super-hard unknown problems using only static dashboards!” Yes, I’m sure you have. If all you have is a hammer, you CAN use it to drive screws into the wall, but that doesn’t mean it’s the best tool. And It takes an extraordinary amount of knowledge and experience to be able to piece together a narrative that translates low-level system statistics into bugs in your software and back. Most software engineers don’t have that kind of systems experience or intuition…and they shouldn’t have to.


Why are dashboards bad for debugging? Think of it this way: every dashboard is an answer to a question someone asked at some point. Your monitoring system is probably littered with dashboards, thousands and thousands of them, most of whose questions have been long forgotten and many of whose source data streams have long since gone silent.


So you come along trying to investigate something, and what do you do? You start skimming through dashboards, eyes scanning furiously, looking for visual patterns — e.g. any spikes that happened around the same time as your incident. **That’s not debugging, that’s pattern-matching.** That’s … eyeball racing.


### if we did math like we do dashboards


Imagine you’re in a math competition, and you get handed a problem to solve. But instead of pulling out your pencil and solving the equation, step by step, you start hollering out guesses.


“27!”

“19992.41!”

“1/4325!”


That’s what flipping through dashboards feels like to me. You’re riffling through a bunch of graphs that were relevant to some long-ago situation, without context or history, without showing their work. Sometimes you’ll spot the exact scenario, and — huzzah! — the number you shout is correct! But when it comes to *unknown* scenarios, the odds are not in your favor.


Debugging looks and feels very different from flipping through answers. You ask a question, examine the answer, and ask another question based on the result. (“Which endpoints were erroring? Are all of the requests erroring, or only some? What did they have in common?”, etc.)


You methodically put one foot in front of the other, following the trail of bread crumbs, until the data itself leads you to the answer.


### The limitations of metrics and dashboards


Unfortunately, you cannot do that with metrics-based dashboards, because you stripped away the connective tissue of the event back when you wrote the metrics out to disk.


If you happened to notice while skimming through dashboards that your 404 errors spiked at 14:03, and your /payment and /import endpoints started erroring at 14.03, and your database started returning a bunch of mysql errors shortly after 14:00, you’ll probably assume that they’re all related and leap to find more evidence that confirms it.


But you *cannot actually confirm* that those events are the same ones, not with your metrics dashboards. You cannot drill down from errors to endpoints to error strings; for that, you’d need a wide structured data blob per request. Those might in fact be two or three separate outages or anomalies happening at the same time, or just the tip of the iceberg of a much larger event, and your hasty assumptions might extend the outage for much longer than was necessary.


**With metrics, you tend to find what you’re looking for**. You have no way to correlate attributes between requests or ask “what are all of the dimensions these requests have in common?”, or to flip back and forth and look at the request as a trace. Dashboards can be fairly effective at surfacing the causes of problems you’ve seen before (raise your hand if you’ve ever been in an incident review where one of the follow up tasks was, “create a dashboard that will help us find this next time”), but they’re all but useless for novel problems, your unknown-unknowns.


### Other complaints about dashboards:


They tend to have percentiles like 95th, 99th, 99.9th, 99.99th, etc. Which can cover over a multitude of sins. You really want a tool that allows you to see MAX and MIN, and heatmap distributions.


A lot of dashboards end up getting created that are overly specific to the incident you just had — naming specific hosts, etc — which just creates clutter and toil. This is how your dashboards become that graveyard of past outages.


The most useful approach to dashboards is to maintain a small set of them; cull regularly, and think of them as a list of starter queries for your investigations.


[Fred Hebert](http://twitter.com/mononcqc) has this analogy, which I like:


> “I like to compare the dashboards to the big display in a hospital room: heartbeat, pressure, oxygenation, etc. Those can tell you when a thing is wrong, but the *context* around the patient chart (and the patient themselves) is what allows interpretation to be effective. If all we have is the display but none of the rest, we’re not getting anywhere close to an accurate picture. The risk with the dashboard is having the metrics but not seeing or knowing about the rest changing.”


### In conclusion


Dashboards aren’t universally awful. The overuse of them just encourages sloppy thinking, and static ones make it impossible for you to follow the plot of an outage, or validate your hypotheses. 🤒  There’s too many of them, and not enough shared consensus. (It would help if, like, new dashboards expired within a month if nobody looked at them again.)


If what you have is “nothing”, even shitty dashboards are far better than no dashboards. But shitty dashboards have been the only game in town for far too long. We need more vendors to think about building for queryability, explorability, and the ability to follow a trail of breadcrumbs. Modern systems are going to demand more and more of this approach.


### Nothing < Dashboards < a Queryable, Exploratory Interface


If [everyone out there who slaps “observability”](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/) on their web page also felt the responsibility to add an observability-enabling interface to their tool, one that would let users explore and identify unknown-unknowns, we would all be in a far better place. 🙂
