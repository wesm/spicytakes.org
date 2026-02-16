---
title: "The Cost Crisis in Observability Tooling"
date: 2024-01-24
url: https://charity.wtf/2024/01/24/the-cost-crisis-in-observability-tooling/
word_count: 2605
---


[*Originally posted on the Honeycomb blog on January 24th, 2024*](https://www.honeycomb.io/blog/cost-crisis-observability-tooling)


The cost of services is on everybody’s mind right now, with interest rates rising, economic growth slowing, and organizational budgets increasingly feeling the pinch. But I hear a special edge in people’s voices when it comes to their observability bill, and I don’t think it’s just about the cost of goods sold. I think it’s because people are beginning to correctly intuit that the value they get out of their tooling has become radically decoupled from the price they are paying.


In the happiest cases, the price you pay for your tools is “merely” rising at a rate several times faster than the value you get out of them. But that’s actually the best case scenario. For an alarming number of people, **the value they get actually *****decreases***** as their bill goes up**.


## Observability 1.0 and the cost multiplier effect


Are you familiar with this chestnut?


> “Observability has three pillars: metrics, logs, and traces.”


This isn’t exactly true, but it’s definitely true of a particular generation of tools—one might even say *definitionally* true of a particular generation of tools. Let’s call it “observability 1.0.”


From an evolutionary perspective, you can see how we got here. Everybody has logs… so we spin up a service for log aggregation. But logs are expensive and everybody wants dashboards… so we buy a metrics tool. Software engineers want to instrument their applications… so we buy an APM tool. We start unbundling the monolith into microservices, and pretty soon we can’t understand anything without traces… so we buy a tracing tool. The front-end engineers point out that they need sessions and browser data… so we buy a RUM tool. On and on it goes.


Logs, metrics, traces, APM, RUM. You’re now paying to store telemetry five different ways, in five different places, for every single request. And a 5x multiplier is on the modest side of the spectrum, given how many companies pay for multiple overlapping tools in the same category. You may also also be collecting:

- Profiling data
- Product analytics
- Business intelligence data
- Database monitoring/query profiling tools
- Mobile app telemetry
- Behavioral analytics
- Crash reporting
- Language-specific profiling data
- Stack traces
- CloudWatch or hosting provider metrics
- …and so on.


So, how many times are *you* paying to store data about your user requests? What’s *your* multiplier? (If you have one consolidated vendor bill, this may require looking at your itemized bill.)


There are many types of tools, each gathering slightly different data for a slightly different use case, but underneath the hood there are really only three basic data types: the metric, unstructured logs, and structured logs. Each of these have their own distinctive trade-offs when it comes to how much they cost and how much value you can get out of them.


### Metrics


Metrics are the great-granddaddy of telemetry formats; tiny, fast, and cheap. A “metric” consists of a single number, often with tags appended. All of the context of the request gets discarded at write time; each individual metric is emitted separately. This means you can never correlate one metric with another from the same request, or select all the metrics for a given request ID, user, or app ID, or ask arbitrary new questions about your metrics data.


Metrics-based tools include vendors like Datadog and open-source projects like Prometheus. RUM tools are built on top of metrics to understand browser user sessions; APM tools are built on top of metrics to understand application performance.


When you set up a metrics tool, it generally comes prepopulated with a bunch of basic metrics, but the useful ones are typically the custom metrics you emit from your application.


Your metrics bill is usually dominated by the cost of these custom metrics. At minimum, **your bill goes up linearly with the number of custom metrics you create**. Which is unfortunate, because to restrain your bill from unbounded growth, you have to regularly audit your metrics, do your best to guess which ones are going to be useful in the future, and prune any you think you can afford to go without. Even in the hands of experts, these tools require significant oversight.


Linear cost growth is the goal, but it’s rarely achieved. The cost of each metric varies wildly depending on how you construct it, what the values are, how often it gets hit, etc. I’ve seen a *single custom metric* cost $30k per month. You probably have dozens of custom metrics per service, and it’s almost impossible to tell how much each of them costs you. Metrics bills tend to be incredibly opaque (possibly by design).


Nobody can understand their software or their systems with a metrics tool alone, because the [metric is extremely limited](https://www.honeycomb.io/blog/ask-miss-o11y-metric-or-trace) in what it can do. No context, no cardinality, no strings… only basic static dashboards. For richer data, we must turn to logs.


### Unstructured logs


You can understand much more about your code with logs than you can with metrics. Logs are typically emitted multiple times throughout the execution of the request, with one or a small number of nouns per log line, plus the request ID. Unstructured logs are still the default, although this is slowly changing.


The cost of unstructured logs is driven by a few things:

- **Write amplification**. If you want to capture lots of rich context about the request, you need to emit a lot of log lines. If you are printing out just 10 log lines per request, per service, and you have half a dozen services, that’s 60 log events for every request.
- **Noisiness**. It’s extremely easy to accidentally blow up your log footprint yet add no value—e.g., by putting a print statement *inside* a loop instead of *outside* the loop. Here, the usefulness of the data goes *down* as the bill shoots up.
- **Constraints on physical resources**. Due to the write amplification of log lines per request, it’s often physically impossible to log everything you want to log for all requests or all users—it would saturate your NIC or disk. Therefore, people tend to use blunt instruments like these to blindly slash the log volume:
  - Log levels
  - Consistent hashes
  - Dumb sample rates


When you emit multiple log lines per request, you end up duplicating a lot of raw data; sometimes over half the bits are consumed by request ID, process ID, timestamp. This can be quite meaningful from a cost perspective.


All of these factors can be annoying. But the worst thing about unstructured logs is that the only thing you can do to query them is full text search. The more data you have, the slower it becomes to search that data, and there’s not much you can do about it.


Searching your logs over any meaningful length of time can take minutes or even hours, which means experimenting and looking around for unknown-unknowns is prohibitively time-consuming. You have to know what to look for in order to find it. Once again, **as your logging bill goes up, the value goes down.**


### Structured logs


Structured logs are gaining adoption across the industry, especially as [OpenTelemetry](https://www.honeycomb.io/resources/the-directors-guide-to-observability) picks up steam. The nice thing about structured logs is that you can actually *do* things with the data other than slow, dumb string searches. If you’ve structured your data properly, you can perform calculations! Compute percentiles! Generate heatmaps!


**Tools built on structured logs are so clearly the future**. But just taking your existing logs and adding structure isn’t quite good enough. If all you do is stuff your existing log lines into key/value pairs, the problems of amplification, noisiness, and physical constraints remain unchanged—you can just search more efficiently and do some math with your data.


There are a number of things you can and should do to your structured logs in order to use them more effectively and efficiently. In order of achievability:

- Instrument your code using the principles of [canonical logs](https://baselime.io/blog/canonical-log-lines), which collects all the vital characteristics of a request into one wide, dense event. It is difficult to overstate the value of doing this, for reasons of usefulness and usability as well as cost control.
- [Add trace IDs and span IDs](https://www.honeycomb.io/blog/observability-is-about-confidence) so you can [trace your code](https://docs.honeycomb.io/concepts/tracing/) using [the same events](https://www.honeycomb.io/blog/ask-miss-o11y-trace-vs-log) instead of having to use an entirely separate tool.
- Feed your data into a [columnar storage engine](https://www.honeycomb.io/blog/why-observability-requires-distributed-column-store) so you don’t have to predefine a schema or indexes to decide which dimensions future you can search or compute based on.
- Use a storage engine that supports [high cardinality](https://docs.honeycomb.io/concepts/high-cardinality/#high-cardinality-and-high-dimensionality-are-critical-for-observability), with an explorable interface.


If you go far enough down this path of enriching your structured events, instrumenting your code with the right data, and displaying it in real time, you will reach an entirely [different set of capabilities](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool), with a cost model so distinct it can only be described as “observability 2.0.” More on that in a second.


## Ballooning costs are baked into observability 1.0


To recap: high costs are baked into the observability 1.0 model. Every pillar has a price.


You have to collect and store your data—and pay to store it—again and again and again, for every single use case. Depending on how many tools you use, **your observability bill may be growing at a rate 3x faster than your traffic is growing, or 5x, or 10x, or even more**.


It gets worse. As your costs go up, the value you get out of your tools goes down.

- Your logs get slower and slower to search.
- You have to know what you’re searching for in order to find it.
- You have to use blunt force sampling technique to keep log volume from blowing up.
- Any time you want to be able to ask a new question, you first have to commit new code and deploy it.
- You have to guess which custom metrics you’ll need and which fields to index in advance.
- As volume goes up, your ability to find a needle in the haystack—any unknown-unknowns—goes down commensurately.


And *[nothing connects any of these tools](https://www.honeycomb.io/blog/cost-crisis-observability-tooling#correction).* You cannot correlate a spike in your metrics dashboard with the same requests in your logs, nor can you trace one of the errors. It’s impossible. If your APM and metrics tools report different error rates, you have no way of resolving this confusion. The only thing connecting any of these tools is the intuition and straight-up guesses made by your most senior engineers. Which means that the cognitive costs are immense, and your bus factor risks are very real. The most important connective data in your system—connecting metrics with logs, and logs with traces—exists only in the heads of a few people.


At the same time, the engineering overhead required to manage all these tools (and their bills) rises inexorably. With metrics, an engineer needs to spend time auditing your metrics, tracking people down to fix poorly constructed metrics, and reaping those that are too expensive or don’t get used. With logs, an engineer needs to spend time monitoring the log volume, watching for spammy or duplicate log lines, pruning or consolidating them, choosing and maintaining indexes.


But all this the time spent wrangling observability 1.0 data types isn’t even the costliest part. **The most expensive part is the unseen costs inflicted on your engineering organization as development slows down and tech debt piles up**, due to low visibility and thus low confidence.


Is there an alternative? Yes.


## The cost model of observability 2.0 is very different


Observability 2.0 has no three pillars; it has a single source of truth. Observability 2.0 tools are built on top of [arbitrarily-wide structured log events](https://www.honeycomb.io/blog/structured-events-basis-observability), also known as spans. From these wide, context-rich structured log events you can *derive* the other data types (metrics, logs, or traces).


Since there is only one data source, you can correlate and cross-correlate to your heart’s content. You can switch fluidly back and forth between slicing and dicing, breaking down or grouping by events, and viewing them as a trace waterfall. You don’t have to worry about cardinality or key space limitations.


You also effectively get *infinite custom metrics*, since you can append as many as you want to the same events. Not only does your cost *not* go up linearly as you add more custom metrics, your telemetry just gets richer and more valuable the more key-value pairs you add! Nor are you limited to numbers; you can add any and all types of data, including valuable high-cardinality fields like “App Id” or “Full Name.”


Observability 2.0 has its own amplification factor to consider. As you instrument your code with more spans per request, the number of events you have to send (and pay for) goes up. However, you have some very powerful tools for dealing with this: you can perform dynamic head-based sampling or even [tail-based sampling](https://www.honeycomb.io/blog/evolution-sampling-refinery), where you decide whether or not to keep the event after it’s finished, allowing you to capture 100% of slow requests and other outliers.


## Engineering time is your most precious resource


But the biggest **difference between observability 1.0 and 2.0 won’t show up on any invoice. The difference shows up in your engineering team’s ability to move quickly, with confidence**.


Modern software engineering is all about hooking up fast feedback loops. And observability 2.0 tooling is what unlocks the kind of fine-grained, exploratory experience you need in order to accelerate those feedback loops.


Where observability 1.0 is about MTTR, MTTD, reliability, and operating software, observability 2.0 is what underpins the entire software development lifecycle, setting the bar for how swiftly you can build and ship software, find problems, and iterate on them. Observability 2.0 is about being in conversation with your code, understanding each user’s experience, and building the right things.


Observability 2.0 isn’t exactly cheap either, although it is often less expensive. But the key difference between o11y 1.0 and o11y 2.0 has never been that either is cheap; it’s that with observability 2.0, when your bill goes up, the value you derive from your telemetry goes up too. **You pay more money, you get more out of your tools.** As you should.


Interested in learning more? We’ve written at length about the [technical prerequisites](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool) for observability with a single source of truth (“observability 2.0” as we’ve called it here). Honeycomb was built to this spec; [ServiceNow (formerly Lightstep)](https://www.servicenow.com/products/observability.html) and [Baselime](https://baselime.io/) are other vendors that qualify. [Click here to get a Honeycomb demo](https://www.honeycomb.io/get-a-demo).


CORRECTION: The original version of this document said that “nothing connects any of these tools.” If you are using a single unified vendor for your metrics, logging, APM, RUM, and tracing tools, this is not strictly true. Vendors like New Relic or Datadog now let you define certain links between your traces and metrics, which allows you to correlate between data types in a few limited, predefined ways. This is better than nothing! But it’s very different from the kind of fluid, open-ended correlation capabilities that we describe with o11y 2.0. With o11y 2.0, you can slice and dice, break down, and group by your complex data sets, then grab a trace that matches any specific set of criteria at any level of granularity. With o11y 1.0, you can define a metric up front, then grab a random exemplar of that metric, and that’s it. All the limitations of metrics still apply; you can’t correlate any metric with any other metric from that request, app, user, etc, and you certainly can’t trace arbitrary criteria. But you’re right, it’s not nothing. 😸
