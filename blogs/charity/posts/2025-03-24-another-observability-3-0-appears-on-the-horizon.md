---
title: "Another observability 3.0 appears on the horizon"
date: 2025-03-24
url: https://charity.wtf/2025/03/24/another-observability-3-0-appears-on-the-horizon/
word_count: 2027
---


Groan. Well, it’s not like I wasn’t warned. When I first started teasing out the differences between the pillars model and the single unified storage model and applying “2.0” to the latter, Christine was like “so what is going to stop the next vendor from slapping 3.0, 4.0, 5.0 on whatever they’re doing?”


Matt Klein dropped a new blog post last week called “[Observability 3.0](https://blog.bitdrift.io/post/observability-3-0)”, in which he argues that bitdrift’s Capture — a ring buffer storage on mobile devices — deserves that title. This builds on his previous blog posts: “[1000x the telemetry at 0.01x the cost](https://blog.bitdrift.io/post/1000-x-the-telemetry)”, “[Why is observability so expensive](https://blog.bitdrift.io/post/observability-cost-crisis)?”, and “[Reality check: Open Telemetry is not going to solve your observability woes](https://blog.bitdrift.dev/post/reality-check-otel)”, wherein he argues that the model of sending your telemetry to a remote aggregator is fundamentally flawed.


I love Matt Klein’s writing — it’s opinionated, passionate, and deeply technical. It’s a joy to read, full of fun, fiery statements about the “logging industrial complex” and backhanded… let’s call them “compliments”… about companies like ours. I’m a fan, truly.


## In retrospect, I semi regret the “o11y 2.0” framing


Yeah, it’s cheap and terribly overdone to use semantic versioning as a marketing technique. (It worked for Tim O’Reilly with “Web 2.0”, but Tim O’Reilly is Tim O’Reilly — the exception that proves the rule.) But that’s not actually why I regret it.


I regret it because a bunch of people — vendors mostly, but not entirely — got really bristly about having “1.0” retroactively applied to describe the multiple pillars model. It reads like a subtle diss, or devaluation of their tools.


One of the principles I live my life by is that you should generally call people, or groups of people, what they want to be called.


That is why, moving forwards, I am going to mostly avoid referring to the multiple pillars model as “o11y 1.0”, and instead I will call it the … multiple pillars model. And I will refer to the unified storage model as the “unified or consolidated storage model, sometimes called ‘o11y 2.0’”.


(For reference, I’ve previously written about [why it’s time to version observability](https://charity.wtf/2024/08/07/is-it-time-to-version-observability-signs-point-to-yes/), what [the key difference is between o11y 1.0 vs 2.0](https://charity.wtf/2024/11/19/there-is-only-one-key-difference-between-observability-1-0-and-2-0/), and had a fun volley back and forth with Hazel Weakly on versioning observabilities: [mine](https://charity.wtf/2024/12/20/on-versioning-observabilities-1-0-2-0-3-0-10-0/), [hers](https://hazelweakly.me/blog/the-future-of-observability-observability-3-0/).)


## Why do we need new language?


It is clearer than ever that a sea change is underway when it comes to how telemetry gets collected and stored. Here is my evidence (if you have evidence to the contrary or would like to challenge me on this, please reach out — first name at honeycomb dot io, email me!!):

- Every single observability startup that was founded *before* 2021, that still exists, was built using the **multiple pillars model** … storing each type of signal in a different location, with limited correlation ability across data sets. (With one exception: [Honeycomb](http://honeycomb.io).)
- Every single observability startup that was founded *after* 2021, that still exists, was built using the **unified storage model**, capturing wide, structured log events, stored in a columnar database. (With one exception: [Chronosphere](http://chronosphere.io).)


The major cost drivers in an o11y 1.0 — oop, sorry, in a “multiple pillars” world, are 1) the number of tools you use, 2) cardinality of your data, and 3) dimensionality of your data — or in other words, the amount of context and detail you store about your data, which is the most valuable part of the data! You get locked in a zero sum game between cost and value.


The major cost drivers in a unified storage world, aka “o11y 2.0”, are 1) your traffic, 2) your architecture, and 3) density of your instrumentation. This is important, because it means your cost growth should roughly align with the growth of your business and the value you get out of your telemetry.


This is a pretty huge shift in the way we think about instrumentation of services and levers of cost control, with a lot of downstream implications. If we just say “everything is observability”, it robs engineers of the language they need to make smart decisions about instrumentation, telemetry and tools choices. Language informs thinking and vice versa, and when our cognitive model changes, we need language to follow suit.


(Technically, we started out by defining observability as differentiated from monitoring, but the market has decided that everything is observability, so … we need to find new language, again. 😉)


## Can we just … *not* send all that data?


My favorite of Matt’s blog posts is “[Why is observability so expensive](https://blog.bitdrift.io/post/observability-cost-crisis)?” wherein he recaps the last 30 years of telemetry, gives some context about his work with Envoy and the separation of control planes / data planes, all leading up to this fiery proposition:


“What if by default we never send any telemetry at all?”


As someone who is always rooting for the contrarian underdog, I salute this. 🫡


As someone who has written and operated a ghastly amount of production services, I am not so sure.


Matt is the cofounder and CTO of Bitdrift, a startup for mobile observability. And in the context of mobile devices and IoT, I think it makes a lot of sense to gather all the data and store it at the origin, and only forward along summary statistics, until or unless that data is requested in fine granularity. Using the ring buffer is a stroke of genius.


Mobile devices are strictly isolated from each other, they are not competing with each other for shared resources, and the debugging model is mostly offline and ad hoc. It happens whenever the mobile developer decides to dig in and start exploring.


It’s less clear to me that this model will ever serve us well in the environment of highly concurrent, massively multi-tenant services, where two of the most important questions are always what is happening right now, and what just changed?


Even the 60-second aggregation window for traditional metrics collectors is a painful amount of lag when the site is down. I can’t imagine waiting to pull all the data in from hundreds or thousands of remote devices just to answer a question. And taking service isolation to such an extreme effectively makes traces impossible.


## The hunger for more cost control levers is real


I think there’s a kernel of truth there, which is that the desire to keep a ton of rich telemetry detail about a fast-expanding footprint of data in a central location is not ultimately compatible with what people are willing or able to pay.


The fatal flaw of the multiple pillars model is that your levers of control consist of deleting your most valuable data: context and detail. The unified storage (o11y 2.0) model advances the state of the art by giving you tools that let you delete your LEAST valuable data, via tail sampling.


In a unified storage model, you should also have to store your data only once, instead of once per tool (Gartner data shows that most of their clients are using 10-20 tools, which is a hell of a cost multiplier.)


But I also think Matt’s right to say that these are only incremental improvements. And the cost levers I see emerging in the market that I’m most excited about are model agnostic.


## Telemetry pipelines, tiered storage, data governance


The o11y 2.0 model (with no aggregation, no time bucketing, no indexing jobs) allows teams to get their telemetry faster than ever… but it does this by pushing all aggregation decisions from write time to read time. Instead of making a bunch of decisions at the instrumentation level about how to aggregate and organize your data… you store raw, wide structured event data, and perform ad hoc aggregations at query time.


Many engineers have argued that this is cost-prohibitive and unsustainable in the long run, and…I think they are probably right. Which is why I am so excited about telemetry pipelines.


Telemetry pipelines are the slider between aggregating metrics at write time (fast, cheap, painfully limited) and shipping all your raw, rich telemetry data off to a vendor, for aggregating at read time.


Sampling, too, has come a long way from its clumsy, kludgey origins. Tail-based sampling is now the norm, where you make decisions about what to retain or not only after the request has completed. The combination of fine-grained sampling + telemetry pipelines + AI is *incredibly* promising.


I’m not going to keep going into detail here because I’m currently editing down a massive piece on levers of cost control, and I don’t want to duplicate all that work (or piss off my editors). Suffice it to say, there’s a lot of truth to what Matt writes… and also he has a way of skipping over all the details that would complicate or contradict his core thesis, in a way I don’t love. This has made me vow to be more careful in how I represent other vendors’ offerings and beliefs.


## Money is not always the most expensive resource


I don’t think we’re going to get to “[1000x the telemetry at 0.01x the cost](https://blog.bitdrift.io/post/1000-x-the-telemetry)”, as Matt put it, unless we are willing to sacrifice or seriously compromise some of the other things we hold dear, like the ability to debug complex systems in real time.


[Gartner recently put out a webinar](https://www.gartner.com/en/webinar/705166/1576691) on controlling observability costs, which I very much appreciated, because it brought some real data to what has been a terribly vibes-based conversation. They pointed out that one of the biggest drivers of o11y costs has been that people get attached to it, and start using it heavily. You can’t claw it back.


I think this is a good thing — a long overdue grappling with the complexity of our systems and the fact that we need to observe it through our tools, not through our mental map or how we remember it looking or behaving, because it is constantly changing out from under us.


I think observability engineering teams are increasingly looking less like ops teams, and more like data governance teams, the purest embodiment of platform engineering goals.


When it comes to developer tooling, cost matters, but it is rarely the most important thing or the most valuable thing. The most important things are workflows and cognitive carrying costs.


## Observability is moving towards a data lake model


Whatever you want to call it, whatever numeric label you want to slap on it, I think the industry is clearly moving in the direction of unified storage — a data lake, if you will, where signals are connected to each other, and particular use cases are mostly derived at read time instead of write time. Where you pay to store each request only one time, and there are no dead ends between signals.


Matt wrote another post about how OpenTelemetry wasn’t going to solve the cost crisis in o11y … but I think that misses the purpose of OTel. The point of OTel is to get rid of vendor lock-in, to make it so that o11y vendors compete for your business based on being awesome, instead of impossible to get rid of.


Getting everyone’s data into a structured, predictable format also opens up lots of possibilities for tooling to feel like “magic”, which is exciting. And opens some entirely different avenues for cost controls!


In my head, the longer term goals for observability involve unifying not just data for engineering, but for product analytics, business forecasting, marketing segmentation… There’s so much waste going on all over the org by storing these in siloed locations. It fragments people’s view of the world and reality. As much as I snarked on it at the time, I think Hazel Weakly’s piece on “[The future of observability is observability 3.0](https://hazelweakly.me/blog/the-future-of-observability-observability-3-0/)” was incredibly on target.


One of my guiding principles is that ✨**data is made valuable by context**.✨ When you store it densely packed together — systems, app, product, marketing, sales — and derive insights from a single source of truth, how much faster might we move? How much value might we unlock?


I think the new few years are going to be pretty exciting.
