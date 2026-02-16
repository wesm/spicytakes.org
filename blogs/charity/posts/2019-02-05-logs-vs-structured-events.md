---
title: "Logs vs Structured Events"
date: 2019-02-05
url: https://charity.wtf/2019/02/05/logs-vs-structured-events/
word_count: 1594
---


I got an interesting tweet the other day from [@evntdrvn](https://twitter.com/evntdrvn) in response to [this thread of mine](https://twitter.com/mipsytipsy/status/1086366949682995200). Paraphrasing,


> “So I’ve almost got our group at work up to Step 1 in your observability maturity model, but some of the devs that I work with want to turn OFF our lovely structured logging in prod for informational-level msgs due to their legacy philosophy (‘we only log errors in prod’). The reasons given are mostly philosophical (“I’m a dev and only interested when things error out, I don’t want any other noise in prod logs”, “I don’t want to slow my app down in prod”). Help?!?”


As I was reading this, I was itching to fly out and dive into battle with Eric. I know *exactly* where his opinionated devs are coming from. I used to say the same things! I even wrote a whole [blog post](https://www.honeycomb.io/blog/lies-my-parents-told-me-about-logs/) about it.


These developers have internalized a set of rules and best practices for dealing with output data, in the context of “monolith application development in the early 2000s”.


### Monolithic systems assumptions


Those systems had many common constraints and assumptions, such as:

- We have a monolith service, or a very small number of services. We can model the system in our heads.
- Logging is done to local disk, which can impact performance
- Disks are expensive
- Log lines are spat out inline with execution.  A poorly placed printf can take the whole system down.
- Investigation is rare, and usually means a human reading error logs.
- Logging is of poor utility for understanding internal states or execution paths; you should just read the code or use a debugger.  (There are few or network hops between functions.)
- Logging is mostly useful for detecting certain terminal crash states or connection errors.


### Monolithic logging best practices


Therefore:

- We should be very stingy in what we log
- Debuggers should be used for understanding internal states of the code
- Logs are a last resort and record of crash dumps.  We do not expect to use log data in the course of our daily work.  We assume log-related manual investigation will be infrequent and of limited utility.


These were exactly the right lessons to learn in the era of expensive hardware and monolithic repos/artifacts. Many people *still* work in environments like this, and follow logging best practices like these. God bless, more power to em.


### Distributed systems assumptions


But more and more of us face systems that are very different.

- We have many services, possibly many MANY services. A representative request will have “many” hops across “many” services and routers and proxies and meshes and storage systems.
- We cannot model the system in our heads; it would be a mistake to try. We rely on tooling as the source of truth for those systems.
- You may or may not have access to those services, or the systems your code runs on. There may or may not be a logging facility, or a centralized log aggregator. **Your only view of the system is through the instrumentation of your code.**
- Disks and system resources are cheap, ephemeral, all but disposable.
- Data services are similarly cheap.  We can almost entirely silo application performance off from the cost of writing perf data out.
- Investigation is prohibitively slow and expensive for a human to do by hand. Many of the nodes or processes we need to inspect **may no longer even exist**, but their past states may still be relevant to us in understanding patterns to the present time.
- Investigation should usually be done distributedly, across all instantiations of your code, however many there might be — and in real time
- **Investigation requires computation** — not just string search. We need to ask on the fly involving math and percentiles and breakdowns and group by’s.  And we need access to the raw requests in order to run accurate computations — no pre-aggregates.
- **The hardest part isn’t usually debugging the code**, it’s figuring out where is the code you need to debug. Or what the errors or outliers have in common from the perspective of the code.  Fixing the code itself is often comparatively trivial, once found.
- What even is ‘logging’?
- What even is ‘local disk’?


This isn’t optional: at some point of complexity or scale or distributedness, it becomes necessary if you want to work with these systems.


### Logs can’t help you here.


And you aren’t going to get that kind of explorable data out of loglevel:ERROR, or by chopping up your telemetry into disconnected metrics devoid of context.


You are only going to get this kind of explorable, ad hoc, computation-friendly data if you take a radically new approach to how you output and aggregate telemetry.  You’re going to need to replace your log lines and log levels with a different sort of beast: **arbitrarily wid****e structured events that describe the request and its context, one event per ****request per service**.


If it helps, don’t think of them as log files any more. Think of them as events. Yes, you can stash this stream in a file, but why would you?  on what disk?  will that work for your serverless functions too?  Just stream them over the network to wherever you want to put them.


Log levels are another confusing and unnecessary artifact of yesteryear that you no longer really need. The more you think of structured events as logs, the more tempted you may be to apply the old set of best practices. So just don’t think of them as logs at all.


### How to gather and structure your data


Instead of dribbling little pebbles of log effluvia throughout your code, do this.  (If you’re a honeycomb user, our [beelines do it all automatically](https://github.com/honeycombio/beeline-go) for you *and* pre-propagate the blobs with everything we know of your context.)

1. Initialize an empty blob at the beginning, when the request first enters the service.
2. Stuff any and all interesting detail about the request into that blob throughout the lifetime of the request.
  - Any unique id, any high-cardinality variable, any headers passed in, every full query, normalized query, and query execution time; every http call out to a remote service, every http execution time; any shopping cart id, first and last name, execution time — literally anything interesting, append to blob.
3. Then, when the request is about to exit or error, write the blob off to honeycomb or another service or disk somewhere.


You can see immediately how this method has radically different performance implications and risks than the earlier shotgun spray approach. No more “oops i accidentally put a print line INSIDE a for loop”. The write amplification profile is compressed. Most importantly, **the incremental cost of capturing more detail about the request per service is nearly zero.**


And now you have the kind of structured data that you can feed into something like a columnar store, or honeycomb, and run ad hoc queries to your heart’s delight.


### Distributed systems logging events best practices:


Let’s sum up.  (I’m including links to other past rants on this topic):

- [Emit a rich record from the perspective of the request as it executes the code](https://twitter.com/mipsytipsy/status/1042817542648082432).   Include all the context you can get your paws on.
- [Emit a single event per request per service that it hits](https://github.com/honeycombio/beeline-go).  Write it out just before  the request errors or exits the service.
- Bypass local disk entirely, write to a remote service.
- [Sample](https://docs.honeycomb.io/getting-data-in/sampling/) if needed for cost or resource constraints.  Practice [dynamic sampling](https://www.honeycomb.io/sampling/).
- [Treat this like *operational data*, not transactional data](https://twitter.com/mipsytipsy/status/1032146885375475713).  Be profligate and disposable.
- Feed this data into a columnar store or honeycomb or similar
- **Now use it every day**.  Not just as a last resort.  Get knee deep in production every single day.  Explore.  Ask and answer rich questions about your systems, system quality, system behavior, outliers, error conditions, etc. You will be absolutely amazed how useful it is … and appalled by what you turn up.  🙂


Just think.


*No more doing multi-line regexps trying to look for the same request ID or user ID doing five suspicious things in a row. *


*No more regexps at all, for fuck’s sake.*


*No more bullshit percentiles that were computed at write time by averaging over a bunch of other averages*


*No more having to jump around from dashboards to logs trying to vainly eyeball correlate one spike with another. No more wondering why no two tools can agree if anything even exists or not*


Just gather the detail you need to ask the questions when you need them, and store it in a single source of truth.  It’s that simple.


No need to shame people from learning best practices that worked perfectly well for a long time.  You can either let them learn the hard way that this transformation is non optional, or you can help them learn the easy way that it’s simply much better and easier to invest in this telemetry up front.  You seem like a nice enough chap, which is probably why you chose door 2.  (If you wanted to get tougher about it, have a few reformed folks in to tell their horror stories.  Try some ex-twitter engineers.)


The hardest part seems to be getting people to unlearn all the best practices they once learned for dealing with logs.  So just don’t call it logs anymore, if that helps. Call it “structured events”.


– charity.
