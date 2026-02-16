---
title: "There Is Only One Key Difference Between Observability 1.0 and 2.0"
date: 2024-11-19
url: https://charity.wtf/2024/11/19/there-is-only-one-key-difference-between-observability-1-0-and-2-0/
word_count: 1933
---


[*Originally posted on the Honeycomb blog on November 19th, 2024*](https://www.honeycomb.io/blog/one-key-difference-observability1dot0-2dot0)


We’ve been [talking about observability 2.0](https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes) a lot lately; what it means for telemetry and instrumentation, its practices and sociotechnical implications, and the dramatically different shape of its [cost model](https://www.honeycomb.io/blog/cost-crisis-observability-tooling). With all of these details swimming about, I’m afraid we’re already starting to lose sight of what matters.


The distinction between observability 1.0 and observability 2.0 is *not* a [laundry list](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool), it’s *not* marketing speak, and it’s *not that complicated* or hard to understand. The distinction is a technical one, and it’s actually quite simple:

1. Observability 1.0 has three pillars and **many sources of truth**, scattered across disparate tools and formats.
2. Observability 2.0 has **one source of truth**, [wide structured log events](https://www.honeycomb.io/blog/structured-events-basis-observability), from which you can *derive* all the other data types.


That’s it. That’s what defines each generation, respectively. Everything else is a consequence that flows from this distinction.


## Multiple “pillars” are an observability 1.0 phenomenon


We’ve all heard the slogan, “metrics, logs, and traces are the three pillars of observability.” Right?


Well, that’s half true; it’s true of observability 1.0 tools. You might even say that **pillars define the observability 1.0 generation**. For every request that enters your system, you write logs, increment counters, and maybe trace spans; then you store telemetry in many places. You probably use some subset (or superset) of tools including APM, RUM, unstructured logs, structured logs, infra metrics, tracing tools, profiling tools, product analytics, marketing analytics, dashboards, SLO tools, and more. Under the hood, these are stored in various metrics formats: unstructured logs (strings), structured logs, time-series databases, [columnar databases](https://www.honeycomb.io/blog/why-observability-requires-distributed-column-store), and other proprietary storage systems.


Observability 1.0 tools force you to make a ton of decisions *at write time* about how you and your team would use the data in the future. They silo off different types of data and different kinds of questions into entirely different tools, as many different tools as you have use cases.


Many pillars, many tools.


An observability 2.0 tool does *not* have pillars.


## Your observability 2.0 tool has one unified source of truth


Your observability 2.0 tool stores the telemetry for each request in one place, in one format: arbitrarily-wide structured log events.


These log events are not fired off willy-nilly as the request executes. They are specifically composed to describe all of the context accompanying a unit of work. Some common patterns include [canonical logs](https://baselime.io/blog/canonical-log-lines), organized around each hop of the request; [traces and spans](https://www.honeycomb.io/blog/observability-is-about-confidence), organized around application logic; or traces emitted as pulses for long-running jobs, queues, CI/CD pipelines, etc.


Structuring your data in this way preserves as much context and connective tissue as possible about the work being done. Once your data is gathered up this way, you can:

- Derive metrics from your log events
- Visualize them over time, as a trace
- Zoom into individual requests, zoom out to long-term trends
- Derive SLOs and aggregates
- Collect system, application, product, and business telemetry *together*
- Slice and dice and explore your data in an open-ended way
- Swiftly compute outliers and identify correlations
- Capture and preserve as much [high-cardinality](https://docs.honeycomb.io/get-started/basics/observability/concepts/high-cardinality/) data as you want


The beauty of observability 2.0 is that it lets you collect your telemetry and store it—*once*—in a way that preserves all that rich context and relational data, and make decisions *at read time* about how you want to query and use the data. Store it once, and use it for everything.


## Everything else is a consequence of this differentiator


Yeah, there’s a lot more to observability 2.0 than whether your data is stored in one place or many. Of course there is. **But everything else is unlocked and enabled by this *****one core difference*****.**


Here are some of the other aspects of observability 2.0, many of which have gotten picked up and discussed elsewhere in recent weeks:

- Observability 1.0 is how you operate your code; observability 2.0 is about how you *develop* your code

- Observability 1.0 has historically been infra-centric, and often makes do with logs and metrics software already emits, or that can be extracted with third-party tools
- Observability 2.0 is oriented around your application code, the software at the core of your business

- Observability 1.0 is traditionally focused on MTTR, MTTD, errors, crashes, and downtime
- Observability 2.0 includes those things, but it’s about holistically understanding your software and your users—not just when things are broken

- To control observability 1.0 costs, you typically focus on limiting the cardinality of your data, reducing your log levels, and [reducing the cost multiplier by eliminating tools](https://www.honeycomb.io/resources/cost-crisis-metrics-tooling).
- To control observability 2.0 costs, you typically reach for tail-based or head-based sampling
- Observability 2.0 complements and supercharges the effectiveness of other modern development best practices like feature flags, progressive deployments, and chaos engineering.


The *reason* observability 2.0 is so much more effective at enabling and accelerating the entire [software development lifecycle](https://www.honeycomb.io/blog/honeycomb-fit-software-development-lifecycle) is because the single source of truth and wide, dense, cardinality-rich data allow you do things you can’t in an observability 1.0 world: slice and dice on arbitrary high-cardinality dimensions like `build_id`, feature flags, `user_id`, etc. to see precisely what is happening as people use your code in production.


In the same way that whether a database is a document store, a relational database, or a columnar database has an enormous impact on the kinds of workloads it can do, what it excels at and which teams end up using it, the difference between observability 1.0 and 2.0 is a technical distinction that has enduring consequences for how people use it.


These are not hard boundaries; data is data, telemetry is telemetry, and there will always be a certain amount of overlap. You can adopt some of these observability 2.0-ish behaviors (like feature flags) using 1.0 tools, to some extent—and you should try!—but the best you can do with metrics-backed tools will always be** percentile aggregates and random exemplars**. You need precision tools to unlock the full potential of observability 2.0.


Observability 1.0 is a dinner knife; 2.0 is a scalpel.


## Why now? What changed?


If observability 2.0 is so much better, faster, cheaper, simpler, and more powerful, then why has it taken this long to emerge on the landscape?


Observability 2.0-shaped tools (high cardinality, high dimensionality, explorable interfaces, etc.) have actually been *de rigeur* on the business side of the house for years. You can’t run a business without them! It was close to 20 years ago that columnar stores like Vertica came on the scene for data warehouses. But those tools weren’t built for software engineers, and they were prohibitively expensive at production scale.


FAANG companies have also been using tools like this internally for a very long time. [Facebook’s Scuba was famously the inspiration for Honeycomb](https://isburmistrov.substack.com/p/all-you-need-is-wide-events-not-metrics)—however, Scuba ran on giant RAM disks as recently as 2015, which means it was quite an expensive service to run. The falling cost of storage, bandwidth, and compute has made these technologies viable as commodity SaaS platforms, at the same time as the skyrocketing complexity of systems due to microservices, decoupled architecture patterns has made them mandatory.


## Three big reasons the rise of observability 2.0 is inevitable


**Number one**: our systems are exploding in complexity along with power and capabilities. The idea that developing your code and operating your code are two different practices that can be done by two different people is no longer tenable. You can’t operate your code as a black box, you have to instrument it. You also can’t predict how things are going to behave or break, and one of the defining characteristics of observability 1.0 was that you had to make those predictions up front, at write time.


**Number two**: the cost model of observability 1.0 is brutally unsustainable. Instead of paying to store your data once, you pay to store it again and again and again, in as many different pillars or formats or tools as you have use cases. The post-ZIRP era has cast a harsh focus on a lot of teams’ observability bills—not only the outrageous costs, but also the reality that as costs go up, [the value you get out of them is going down](https://www.honeycomb.io/blog/cost-crisis-observability-tooling).


Yet the cost multiplier angle is in some ways the easiest to fix: you bite the bullet and sacrifice some of your tools. Cardinality is even more costly, and harder to mitigate. You go to bed Friday night with a $150k Datadog bill and wake up Monday morning with a million dollar bill, without changing a single line of code. Many observability engineering teams spend an outright majority of their time just trying to manage the cardinality threshold—enough detail to understand their systems and solve users’ problems, not so much detail that they go bankrupt.


And that is the most expensive part of all: engineering cycles. The cost of the time engineers spend laboring below the value line—trying to understand their code, their telemetry, their user behaviors—is *astronomical*. **Poor observability is the dark matter of engineering teams.** It’s why everything we do feels so incredibly, grindingly slow, for no apparent reason. Good observability empowers teams to ship swiftly, consistently, and with confidence.


**Number three**: a critical mass of developers have seen what observability 2.0 can do. Once you’ve tried developing with observability 2.0, you can’t go back. That was what drove Christine and me to start Honeycomb, after we experienced this at Facebook. It’s hard to describe the difference in words, but once you’ve built software with fast feedback loops and real-time, interactive visibility into what your code is doing, you simply won’t go back.


---


## It’s not just Honeycomb; observability 2.0 tools are going mainstream


We’re starting to see a wave of early startups building tools based on these principles. You’re seeing places like Shopify build tools in-house using something like Clickhouse as a backing store. DuckDB is now available in the open-source realm. I expect to see a blossoming of composable solutions in the next year or two, in the vein of ELK stacks for o11y 2.0.


Jeremy Morrell recently published the [comprehensive guide to observability 2.0 instrumentation](https://jeremymorrell.dev/blog/a-practitioners-guide-to-wide-events/), and it includes a vendor-neutral overview of your options in the space.


There are still valid reasons to go with a 1.0 vendor. Those tools are more mature, fully featured, and most importantly, they have a more familiar look and feel to engineers who have been working with metrics and logs their whole career. But engineers who have tried observability 2.0 are rarely willing to go back.


## Beware observability 2.0 marketing claims


You do have to be a little bit wary here. There are lots of observability 1.0 vendors who talk about having a “unified observability platform” or having all your data in one place. But what they actually mean is that you can pay for all your tools in *one unified bill*, or present all the different data sources in *one unified visualization*.


The best of these vendors have built a bunch of elaborate bridges between their different tools and storage systems, so you can predefine connection points between e.g. a particular metric and your logging tool or your tracing tool. This is a massive improvement over having *no* connection points between datasets, no doubt. But a unified presentation layer is *not the same thing* as a unified data source.


So if you’re trying to clear a path through all the sales collateral and marketing technobabble, you only need to ask one question: how many times is your data going to be stored?


Is there *one* source of truth, or many?
