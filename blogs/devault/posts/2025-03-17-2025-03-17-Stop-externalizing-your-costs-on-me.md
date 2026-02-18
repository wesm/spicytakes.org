---
title: "Please stop externalizing your costs directly into my face"
date: 2025-03-17
url: https://drewdevault.com/2025/03/17/2025-03-17-Stop-externalizing-your-costs-on-me.html
slug: 2025-03-17-Stop-externalizing-your-costs-on-me
word_count: 762
---

*This blog post is expressing personal experiences and opinions and doesn’t
reflect any official policies of SourceHut.*

Over the past few months, instead of working on our priorities at SourceHut, I
have spent anywhere from 20-100% of my time in any given week mitigating
hyper-aggressive LLM crawlers at scale. This isn’t the first time SourceHut has
been at the wrong end of some malicious bullshit or paid someone else’s
externalized costs – every couple of years someone invents a new way of ruining
my day.

Four years ago, we decided to  [require payment to use our CI services](https://man.sr.ht/ops/builds.sr.ht-migration.md) 
because it was being abused to mine cryptocurrency. We alternated between
periods of designing and deploying tools to curb this abuse and periods of
near-complete outage when they adapted to our mitigations and saturated all of
our compute with miners seeking a profit. It was bad enough having to beg my
friends and family to avoid “investing” in the scam without having the scam
break into my business and trash the place every day.

Two years ago, we threatened to  [blacklist the Go module mirror](https://sourcehut.org/blog/2023-01-09-gomodulemirror/)  because for
some reason the Go team thinks that running terabytes of git clones all day,
every day for every Go project on git.sr.ht is cheaper than maintaining any
state or using webhooks or coordinating the work between instances or even just
designing a module system that doesn’t require Google to DoS git forges whose
entire annual budgets are considerably smaller than a single Google engineer’s
salary.

Now it’s LLMs. If you think these crawlers respect robots.txt then you are
several assumptions of good faith removed from reality. These bots crawl
everything they can find, robots.txt be damned, including expensive endpoints
like git blame, every page of every git log, and every commit in every repo, and
they do so using random User-Agents that overlap with end-users and come from
tens of thousands of IP addresses – mostly residential, in unrelated subnets,
each one making no more than one HTTP request over any time period we tried to
measure – actively and maliciously adapting and blending in with end-user
traffic and avoiding attempts to characterize their behavior or block their
traffic.

We are experiencing dozens of brief outages per week, and I have to review our
mitigations several times per day to keep that number from getting any higher.
When I do have time to work on something else, often I have to drop it when all
of our alarms go off because our current set of mitigations stopped working.
Several high-priority tasks at SourceHut have been delayed weeks or even months
because we keep being interrupted to deal with these bots, and many users have
been negatively affected because our mitigations can’t always reliably
distinguish users from bots.

All of my sysadmin friends are dealing with the same problems. I was asking one
of them for feedback on a draft of this article and our discussion was
interrupted to go deal with a new wave of LLM bots on their own server. Every
time I sit down for beers or dinner or to socialize with my sysadmin friends
it’s not long before we’re complaining about the bots and asking if the other
has cracked the code to getting rid of them once and for all. The desperation in
these conversations is palpable.

Whether it’s cryptocurrency scammers mining with FOSS compute resources or
Google engineers too lazy to design their software properly or Silicon Valley
ripping off all the data they can get their hands on at everyone else’s expense…
I am sick and tired of having all of these costs externalized directly into my
fucking face. Do something productive for society or get the hell away from my
servers. Put all of those billions and billions of dollars towards the common
good before sysadmins collectively start a revolution to do it for you.

Please stop legitimizing LLMs or AI image generators or GitHub Copilot or any of
this garbage. I am begging you to stop using them, stop talking about them, stop
making new ones, just  *stop* . If blasting CO 2  into the air and
ruining all of our freshwater and traumatizing cheap laborers and making every
sysadmin you know miserable and ripping off code and books and art at scale and
ruining our fucking democracy isn’t enough for you to leave this shit alone,
what is?

If you personally work on developing LLMs et al, know this: I will never work
with you again, and I will remember which side you picked when the bubble
bursts.
