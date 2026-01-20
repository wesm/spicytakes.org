---
title: "Down with the DAG"
subtitle: "Reverse the ETL timeline."
date: 2022-08-12T16:15:09+00:00
url: https://benn.substack.com/p/down-with-the-dag
slug: down-with-the-dag
word_count: 2066
---


![](https://substackcdn.com/image/fetch/$s_!8b3a!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9d403c7c-9ac1-4eed-90c4-243c8713b7be_1200x600.png)

*Data pipelines:Nothing makes sense and everything is backwards.*


If a thousand startups have died on the hill of building a better note-taking app, a thousand masochists have died on the hill of building a better calendar.


So naturally, I’m here to say that the data industry needs a better calendar.


Complaining about schedulers is one of the data community’s most consistent hobbies, so I’m not exactly taking some brave stand against a popular hero. To the contrary, Airflow has been a target for years—ofcompetitiveproducts, ofunbundling, and, just last week, ofbreakup notes.


Most of these objections, however, argue that Airflow is structurally outdated. It isn’t designed for managing today’s complex data stacks, and it’s not built for modern development workflows. As data teams, we no longer need a tool for running tasks in ordered steps (aka, the infamous DAG); we now needcontrol planes,coordination planes, and broader, richer systems oforchestration.


Okay, sure. Asingle pane of glasssounds nice. But it’s also a sort of shapeless, all-encompassing leviathan that we can never quite describe. I don’t want to make (yet another) case for that, nor do I want to pile on to Airflow.1Instead, I want to make a narrower point specifically about how we schedule things: We do it backwards.


Nearly every data tool schedules stuff like you arrange dominos. You line up a series of ordered tasks, and configure when to knock over the first one. At that scheduled time—or, when some other external event happens, such as a file getting updated somewhere—the system kicks it down,triggering the entire chain of subsequent tasks.


In simple cases, this paradigm—A causes B, B causes C, left-to-right across a sequence of events—is easy to create and understand. As soon as things get more complicated, however, everything breaks down. Causal chains become impossible to understand and delicate to maintain. And more importantly, they’re defined by what triggers them, not by what they’re meant to create.


# What causes a plane to take off?


To extend every orchestrator’s favorite analogy—theair trafficcontroller—imagine being an airport administrator. To run an airport, you could model the entire operation around the events that matter—when do flights take off and land?—and build forwards and backwards from there. For the flights you want, how many gate agents need to be available to check people in? Can the security line process people fast enough? What baggage claim carousels need to be ready when a new plane arrives? First schedule all the flights, and then figure out what has to happen to support them. To add more flights, stick them in the model, and sequence the rest of the necessary processes around them.


An alternative approach would be to model the airport as a huge DAG, starting with people arriving at the terminal. When a car shows up, tell an airline employee to go to the baggage counter to check their bag. Once a hundred people arrive, begin boarding the plane. When all boarding tasks have been completed, taxi the plane out to the runway. When a plane lands, queue a team ofaircraft marshallersto guide it to a gate. Fifteen minutes after a plane arrives, call twenty cabs.


This approach would be a disaster. Planes wouldn’t actually have scheduled departure times; they’d just take off whenever the preceding tasks were done. It would be impossible to add a new flight to the daily schedule without causing huge disruptions, because you couldn’t add it directly; you’d instead have to figure out which sequence of dominos to push over, and hope that the chain reactions they cause eventually gets a plane in the air. The problem gets even harder as you add more variability, like wanting to schedule some commuter flights to take off six times a day in alawn mower with wings, and others to be weekly long-haul trips in aflying beluga whale.2


Unfortunately, we’ve built most of our data pipelines using the latter model—we want the updated datasets or fresh dashboards at the end of our lineage graph, but define our schedules around what’s at the beginning of it. Like an airport that coordinates everything based on when Ubers drop people off, it’s hard to create, hard to understand, and hard to maintain.


I’m convinced that there’s a better way.


# ReverseETLorchestration


Mode was inspired by an internal query tool that I used—andJosh, one of Mode’s other cofounders, built—at Yammer. In addition to that tool, Josh also created an internal data transformation tool called Integritie,3which was very similar to dbt. As analysts, we committed parameterized SQL statements and YAML configuration files to Integritie, which would use the queries, and the dependencies implied in them, to regularly create and update tables in our warehouse. In May of 2016, a couple years after starting Mode, I built a command-line version of the same thing, which I named Easybake.4


Both Integritie and Easybake were simpler, cruder versions of dbt in nearly every way, except one: Their schedulers. In both tools, there was no explicit dependency graph, and we never scheduled a chain of models to run at specific times (i.e., there was nothing analogous todbt run.). Instead, for each model, analysts set a latency requirement—this table should never have data that’s more than four hours out of date, a day out of date, a week out of date.


The system figured out the rest. It would construct the DAG behind the scenes, and work out when to run all of the models, including upstream ones, to maintain the guarantees. It would then continually orchestrate all the runs, updating models as needed. When jobs failed, it would alert you of the failure and, as downstream delays cascaded through the system, when other tables started exceeding their latency requirements.


It wasn’t perfect. I used some hacky heuristics to estimate how long a model would take to run; it would sometimes update tables unnecessarily; it didn’t make any effort to distribute runs in an intelligent way, which could create bottlenecks if a bunch of tables were about to expire at the same time.


But it worked really well in three ways:


First, because each model was configured independently, we could easily set different requirements for different tables. Important dimension tables often had tight guarantees of an hour or less; computationally expensive tables, like rollup tables that we used for reporting, were rebuilt once a day, or even once a week. This significantly lowered the burden we put on our database—and, had metered cloud databases like Snowflake and BigQuery existed at the time, would’ve lowered our costs.


Second, even differentiated requirements like these were simple to maintain. When adding a new table that we needed to update once a day, we didn’t have to define a procedure for making it so, like choosing which schedule to attach it to or where it should sit in the DAG. We just told the toolwhat we wanted.


Third, latency requirements were a direct way to tell the application what was important to us—fresh data—andto identify when something was broken in a meaningful way. In scheduler-based dependency graphs, we often conflate failed jobs with out-of-date data. But that’s not actually true. A frequently-updating data ingestion task, for example, might periodically fail and self-correct, all within the bounds of a latencySLA. Alerting people about the failed task teaches us to ignore these warnings, and divorces system problems and internal failures from actual problems that affect whether or not data can be trusted.


# On the roadmap


Still, these things being internal tools—and one of them being an internal toolthat I built—they barely scratched the surface of what was possible. Had Josh had more time, or if I had modicum of understanding about how to actually create software,5we could’ve extended this paradigm in all sorts of interesting ways.


We could’ve made it capable of detecting when latency guarantees were inconsistent with upstream dependencies. For example, if I assigned a six-hour requirement to a customer activity table that was derived from an accounts table with a twelve-hour guarantee, the system would update the accounts table more frequently. Instead, it could’ve told me about this mismatch, and let me decide how to handle it.


With a way to identify these conflicting requirements, we could’ve added reverse guarantees that would prevent tables from updating too frequently, protecting ourselves from wasteful jobs and runaway database costs.


We could’ve built smarter ways to distribute load. The system knew the state it wanted to create; it could, like a SQL planner optimizing a query plan, figure out the best way to get there. We could’ve gone even further and told it what to optimize for, like spreading jobs out evenly over time, running them all at once, or minimizing how long they take.


We could’ve supported other temporal guarantees, such as latency requirements fixed to a certain time. These would function like standard schedules, but with bands—make sure this is always updated sometime after midnight and before 8 am. Range requirements would both maintain the guarantee-oriented paradigm over the task-based one, and give the scheduler more flexibility over when to update tables.


We could’ve let people specify layers of guarantees, where the system tries to maintain the strict one, but only alerts us if a looser one gets violated. This could help temper the alarms and notifications—this Fivetran job failed! Stitch ran into Marketo’s API limit! Github is down!—that are now all too easy to disregard.


We could’ve used these guarantees to create tidy indicators of pipeline health, where we track how much time individual jobs and the system as a whole are meeting their latency requirements. As it stands today, concepts likedata downtimeare mostly marketing catchphrases that represent the vague and overinclusive notion of there being errors and anomalies in your data stack. But downtime should mean something more precise: When tables6violate their SLAs. Just as engineers wouldn’t call an application down because it throws a few errors, we shouldn’t call data down because things fail. Instead, we should specify the latency bounds we’re willing to tolerate, and only worry if we step beyond them.


# Isn’t it just…?


People have spent theirentire lives on problems like these, and I’m sure there are enormously difficult challenges with even the simplest parts of this proposal.7I—a technical buffoon with a bachelor’s degree and a blog—won’t pretend to know how to write a program or do the math to build something that does all of this. But as auser, this is the experience I want. As critical as they are to make scheduling systems work, I don’t actually want to think about when to run jobs, how to define DAGs, or to manually orchestrate anything. I just want my data to be fresh—where I can declare what fresh means—and to know when it’s not. Like a passenger wanting to know if their flight isdelayed or departing on time, I don’t care about the intricate and fragile complexities that make it possible for me to safely rocket myself across the planet from major city to tiny remote island in a matter of hours; I just want to knowwhen I can complain.

[1](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-1-68355797)

You gotta give credit to anything that tries to make computers understand time. Time zones don’t make any sense (what time zoneis Arizona in?); doing math with dates is hard (what’s February 29, 2020 plus a year?); time is impossible to format (when is 10/11/12?); we can’t even agree on what words mean (when does a week start?). I can barely set an alarm clock; if you can figure out how to tell a computer how to automatically adjust clocks in Phoenix for daylight saving time during a leap year, you have my eternal respect.

[2](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-2-68355797)

Imagine buildingthis planeand thinking, “Looks great, if only it werebigger.”

[3](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-3-68355797)

As in “integrity,” but ending in -ie. For reasons unknown, that was the naming standard for all internal tools at Yammer (and formost baseball nicknames).

[4](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-4-68355797)

About a year after creating Easybake, we scrapped it in favor of dbt. Prior to that, we briefly considered adding Easybake into Mode, but deemed it a bad business. A dbt-led revolution of data transformation later…oops.

[5](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-5-68355797)

Seriously, what is__init__?

[6](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-6-68355797)

This could be extended to other data assets as well, like dashboards, operational data pipelines, ML models, and so on.

[7](https://benn.substack.com/p/down-with-the-dag#footnote-anchor-7-68355797)

I bet, for instance, that there’s someArrow’s impossibility theoremfor schedulers, where a scheduler can only ever do four of the five things you want it to.
