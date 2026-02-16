---
title: "The Truth About “MEH-TRICS”"
date: 2022-04-13
url: https://charity.wtf/2022/04/13/the-truth-about-meh-trics/
word_count: 1270
---


*First published on 2022-04-13 at *[*https://www.honeycomb.io/blog/truth-about-meh-trics-metrics*](https://www.honeycomb.io/blog/truth-about-meh-trics-metrics)


A long time ago, in a galaxy far, far away, I said a lot of inflammatory things about metrics.


“Metrics are[ shit salad](https://twitter.com/mipsytipsy/status/1210757638222311425?s=20&t=Sv2z1R-iJulJYFOIfVOJBA).”


“Metrics are simply[ nerfed dimensions](https://twitter.com/mipsytipsy/status/1186839853335367680?s=20&t=Sv2z1R-iJulJYFOIfVOJBA).”


“Metrics[ suck](https://twitter.com/mipsytipsy/status/1210769987477991425?s=20&t=Sv2z1R-iJulJYFOIfVOJBA),” “metrics are[ legacy](https://twitter.com/mipsytipsy/status/1172294278799929345?s=20&t=Sv2z1R-iJulJYFOIfVOJBA),” “metrics and time series aggregates will[ fucking kneecap you](https://twitter.com/mipsytipsy/status/910631218424700928?s=20&t=3QKB8ImU2D0xHRA2u08zmA).”


I cannot tell a lie; Twitter will testify that I’ve spent the past six years ragging on metrics. So much so that ever since we launched [Honeycomb Metrics](https://www.honeycomb.io/metrics/) last year, our poor solution architects have been encountering skeptics in the field who repeat my quotes back to them and ask, dubiously, whether Honeycomb Metrics are any good or not, and whether we genuinely plan on investing in it or not, given our known anti-metrics sympathies.


That’s a great question. 😊


## **Metrics aren’t worthless; they’re just limited.**


Metrics are a mature technology that’s been around for over 30 years, and they have some real advantages. They’re tiny, fast, and cheap; you can hold a bunch of them in memory as counters, summaries, and gauges. They aggregate well and take up a fixed amount of storage space. The entire monitoring industry is built on top of metrics.


When it comes to workloads like, “How heavy is the write load on my hard drive?” or “What is the temperature or fan status inside my chassis?” or “What is the traffic rate in and out of this interface on my switch?”  metrics are what you should use. **In fact, pretty much any time you want to know the health of a system or component *****in toto*****, metrics are the right tool.**


Because that’s what metrics do best—report statistics in aggregate, from the perspective of any system or component. They can tell you that your Ruby HTTP worker pool is 70% utilized or that your nginx webserver is returning 502s 1% of the time. What they *can’t* tell you is what this means for any one of your users, applications, delivery vehicles, and so forth.


Until recently, metrics-based tools or logs were the only game in town. People were trying to sell us metrics tools for observability use cases, and *that’s* what got my goat so badly. If you simply append “… for observability” to each of my inflammatory statements, then I stand by them completely.


“Metrics are shit salad … *for observability.*”


Yup, rings true.


You’re never going to make a metrics tool like Prometheus or Datadog into an observability tool. You’re just not. Observability is about unknown-unknowns, while metrics are a tool for known-unknowns.


If you need a refresher on the differences between observability and monitoring, I’ll refer you to pieces like [this](https://thenewstack.io/observability-a-3-year-retrospective/), [this](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/), and [this](https://charity.wtf/2020/03/03/observability-is-a-many-splendored-thing/). What I want to talk about here is slightly different. In a post-observability world, what is the true and proper place for metrics tooling?


## **Metrics and observability have different use cases.**


Metrics aren’t completely useless, even if you have a robust observability presence. We still use metrics at Honeycomb to this day for certain workloads—and always will because they’re the right tool for the job.


There are two kinds of workloads, roughly speaking: *your code*—the code you write, review, ship, debug and maintain on a daily basis. And *other people’s code—*the code you have to run and use in order to support your code. Some examples of the latter might be: Linux, Docker, MySql, Amazon RDS, Kafka, AWS Lambda, GCP gateways, memcache, CI/CD pipelines, Kubernetes, etc.


Your code is your crown jewels, the code you need to survive and succeed as a business. It changes constantly—many times per week, if not per day. You are expected to understand its inner workings intimately, and spend lots of time chasing down bugs or understanding and reproducing behavior. You care about the way it performs and interacts with each and every individual user, with changing infrastructure state, and under a variety of different load conditions.


That is why **your** **code demands observability**. In order to understand your software, you must first instrument it, in a way that collects lots of rich context and bundles it up around each event end-to-end. Then you need to stream those events into a tool that lets you slice and dice and trace and explore with support for high-cardinality and high-dimensionality data. That’s the only way you’re going to be able to correlate errors, track down outliers, and reflect each user’s experience.


But what about the rest of the software? You can’t instrument Amazon RDS, and only crazy people would instrument, rebuild, and repackage things like Kafka or Docker or nginx. The whole point of third-party software is that you DON’T USE IT until it’s stable enough to be taken more or less for granted. Sure, you roll updates, but usually on the order of months or years—not every day. You don’t need to be intimately familiar with its inner workings because you aren’t changing it every day. Those aren’t your crown jewels.


You do care about their health though, only differently. You care about whether you need to provision more capacity or not. You care about knowing how hard you’re hammering on the underlying hardware or hypervisor. That’s why **metrics and monitoring are the right tools to use for third-party code**. They don’t let you peer under the hood in the same way, or slice and dice in the same way, but that’s okay. You shouldn’t have to.


**With third-party stuff, you don’t care about the *****code*****, you care about the *****health of the service*****.** In aggregate.


(There are some kinds of in-between software, like databases, where event-level information is super useful for debugging things like slow queries and lock percentages, and you can use various [black box techniques to approximate observability](https://www.honeycomb.io/blog/add-observability-to-databases/) without instrumentation. But in general this model holds up quite well.)


## **In a post-observability world, what are metrics for?**


I’ve often pointed out that observability is built on top of arbitrarily wide structured data blobs, and that metrics, logs, and traces can be derived from those blobs while the reverse is not true—you can’t take a bunch of metrics and reformulate a rich event.


And yes, **people who have observability typically find themselves using metrics and dashboards less and less**. They’re simply not as versatile or useful as events that you can slice and dice and manipulate in infinite ways. And you *can* derive aggregates and trends from the events you have stored.


But metrics will always be useful for understanding third-party software, from the perspective of the service, cluster, or node. They will always be the right tool for the job when it comes to software interfacing with hardware. And they can be *super* complementary when you are investigating your code using events and instrumentation.


If you’re an engineer writing and shipping code, you’re never *not* going to want to know if your change caused memory usage to triple, or CPU utilization to skyrocket, or disk usage or network throughput to saturate. That’s why we built Honeycomb Metrics as an overlay, a way to enhance or validate your understanding of the impact your code changes have had on the underlying system.


**Metrics are also valuable as a bridge to the past**. People have been instrumenting software for metrics for 30 years—they’re never going away completely, and not everything can or should be reinstrumented with events. Lots of people already have robust monitoring systems that slurp in millions of metrics. Nobody wants to have to redo all that work just because they’re moving to a different tool, so people tend to point their metrics firehose at Honeycomb as a way of getting started as they roll observability out into their code.
