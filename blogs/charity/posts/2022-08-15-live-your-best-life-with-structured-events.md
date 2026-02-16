---
title: "Live Your Best Life With Structured Events"
date: 2022-08-15
url: https://charity.wtf/2022/08/15/live-your-best-life-with-structured-events/
word_count: 2860
---


If you’re like most of us, you learned to debug as a baby engineer by way of printf(3). By the time you were shipping code to production you had probably learned to instrument your code with a real metrics library. Maybe a tenth of us learned to use gdb and still step through functions on the regular. (I said *maybe*.)


Printing stuff to stdout is still the Swiss Army knife of tools. Always there when you reach for it, usually helps more than it does harm. (I said *usually.*)


And then! In case you’ve been living under a rock, we recently went and blew up ye aulde monolythe, and in the process we … lost most of our single-process tools and techniques for debugging. Forget gdb; even *printf* doesn’t work when you’re hopping the network between functions.


If your tool set no longer works for you, friend, it’s time to go all in. Maybe what you *wanted* was a faster horse, but it’s time for a car, and the sooner you turn in your oats for gas cans and a spare tire, the better.


## Exercising Good Technical Judgment (When You Don’t Have Any)


If you’re stuck trying to debug modern problems with pre-modern tooling, the first thing to do is stop digging the hole. Stop pushing good data after bad into formats and stores that aren’t going to help you answer the right questions.


In brief: if you aren’t rolling out a solution based on **arbitrarily wide, structured raw events that are unique and ordered and trace-aware **and without any aggregation at write time, you are going to regret it. (If you aren’t using OpenTelemetry, you are going to regret that, too.)


So just make the leap as soon as possible.


But let’s rewind a bit.  Let’s start with observability.


## Observability: an introduction


Observability is not a new word or concept, but the definition of observability as a specific technical term applied to software engineering is relatively new — about four years old. Before that, if you heard the term in softwareland it was only as a generic synonym for telemetry (“there are three pillars of observability”, in one annoying formulation) or team names (twitter, for example, has long had an “observability team”).


The term itself originates with [control theory:](https://en.wikipedia.org/wiki/Observability)


“In control theory, observability is a measure of how well internal states of a system can be inferred from knowledge of its external outputs. The observability and controllability of a system are mathematical duals. The concept of observability was introduced by Hungarian-American engineer Rudolf E. Kálmán for linear dynamic systems.[1][2]”


But when applied to a software context, observability refers to how well you can understand and reason about your systems, just by interrogating them and inspecting their outputs with your tools. How well can you understand the *inside* of the system from the *outside*?


Achieving this relies your ability to ask brand new questions, questions you have never encountered and never anticipated — ***without shipping new code**. *Shipping new code is cheating, because it means that you knew in advance what the problem was in order to instrument it.


### But what about monitoring?


Monitoring has a long and robust history, but it has always been about watching your systems for failures you can define and expect. Monitoring is for known-unknowns, and setting thresholds and running checks against the system. **Observability is about the unknown-unknowns.** Which requires a fundamentally different mindset and toolchain.


“Monitoring is the action of observing and checking the behavior and outputs of a system and its components over time.” — @grepory, in his talk “[Monitoring is Dead](https://speakerdeck.com/grepory/monitoring-is-dead)“.


**Monitoring is a third-person perspective on your software**. It’s not software explaining itself from the inside out, it’s one piece of software checking up on another.


### Observability is for understanding complex, ephemeral, dynamic systems (not for debugging code)


You don’t use observability for stepping through functions; it’s not a debugger.  Observability is for swiftly identifying where in your system the error or problem is coming from, so you can debug it — by reproducing it, or seeing what it has in common with other erroring requests.  You can think of observability as being like B.I. (business intelligence) tooling for software applications, in the way you engage in a lot of exploratory, open-ended data sifting to detect novel patterns and behaviors.


Observability is often about swiftly isolating or tracking down the problem in your large, sprawling, far-flung, dynamic system. Because the hard part of distributed systems is rarely debugging the code, **it’s figuring out where the code you need to debug is**.


The need for observability is often associated with microservices adoption, because they are prohibitively difficult to debug without service-level event oriented tooling — the kind you can get from Honeycomb and Lightstep.. and soon, I hope, many other vendors.


## Events are the building blocks of observability


Ergh, another overloaded data term. What even is an “event”?


An observability “event” is a hop in the lifecycle of an end-to-end request. If a request executes code on three services separated by network hops before returning to the user, that request generated three observability “events”, each packed with context and details about that code running in that environment. These are also sometimes called “[canonical log lines](https://stripe.com/blog/canonical-log-lines)“. If you implemented tracing, each event may be a span in your trace.


If request ID #A897BEDC hits your edge, then your API service, then four more internal services, and twice connects to a db and runs a query, then request ID #A897BEDC generated 8 observability events … assuming you are in fact gathering observability data from the edge, the API, the internal services and the databases.


This is an important caveat. **We only gather observability events from services that we can and do introspect**. If it’s a black box to us, that hop cannot generate an observability event. So if request ID #A897BEDC also performed 20 cache lookups and called out to 8 external HTTP services and 2 managed databases, those 30 hops do *not* generate observability events (assuming you haven’t instrumented the memcache service and have no instrumentation from those external services/dbs). Each request generates one event per request per service hop.**


(I also wrote about [logs vs structured events here](https://charity.wtf/2019/02/05/logs-vs-structured-events/).)


## **Observability is a first-person narrative**.


We care primarily about self-reported status from the code as it executes the request path.


Instrumentation is your eyes and ears, explaining the software and its environment from the perspective of your code. Monitoring, on the other hand, is traditionally a third-person narrative — it’s one piece of software checking up on another piece of software, with no internal knowledge of its hopes and dreams.


First-person narrative reports have the best potential for telling a reliable narrative.  And more importantly, they **map directly to user experience** in a way that third-party monitoring does not and cannot.


### Events … must be structured.


First, **structure your goddamn data**.  You’re a computer scientist, you’ve got no business using text search to plow through terabytes of text.


### Events …  are not just structured logs.


Now, part of the reason people seem to think structured data is cost-prohibitive is that **they’re doing it wrong**.  They’re still thinking about these like log lines.  And while you *can* look at events like they’re just really wide structured log lines that aren’t flushed to disk, here’s why you shouldn’t: logs have decades of abhorrent associations and absolutely ghastly practices.


Instead of bundling up and passing along one neat little pile of context, they’re spewing log lines inside loops in their code and DDoS’ing their own logging clusters.They’re shitting out “log lines” with hardly any dimensions so they’re information-sparse and just straight up wasting the writes. And then to compensate for the sparseness and repetitiveness they just start logging the same exact nouns tens or hundreds of times over the course of the request, just so they can correlate or reconstruct some lousy request that they never should have blown up in the first place!


But they keep hearing they should be structuring their logs, so they pile structure on to their horrendous little strings, which pads every log line by a few bytes, so their bill goes up but they aren’t getting any benefit! just paying more! What the hell, structuring is bull shit!


Kittens. You need a fundamentally different approach to reap the considerable benefits of structuring your data.


But the difference between strings and structured data is ~basically the difference between grep and all of computer science. 😛


### Events … must be arbitrarily wide and dense with context.


So the most effective way to structure your instrumentation, to get the absolute most bang for your buck, is to emit a single arbitrarily wide event per request per service hop. At Honeycomb, the maturely instrumented datasets that we see are often 200-500 dimensions wide.  Here’s an event that’s just 20 dimensions wide:


```
{ 

   "timestamp":"2018-11-20 19:11:56.910",
   "az":"us-west-1",
   "build_id":"3150",
   "customer_id":"2310",
   "durationMs":167,
   "endpoint":"/api/v2/search",
   "endpoint_shape":"/api/v2/search",
   "fraud_dur":131,
   "hostname":"app14",
   "id":"f46691dfeda9ede4",
   "mysql_dur":"",
   "name":"/api/v2/search",
   "parent_id":"",
   "platform":"android",
   "query":"",
   "serviceName":"api",
   "status_code":200,
   "traceId":"f46691dfeda9ede4",
   "user_id":"344310",
   "error_rate":0,
   "is_root":"true"
}
```


So a well-instrumented service should have hundreds of these dimensions, all bundled around the context of each request. And yet — and here’s why events blow the pants off of metrics — even with hundreds of dimensions, it’s still *just one write*. **Adding more dimensions to your event is effectively free,** it’s still one write plus a few more bits.


Compare this to a metric-based systems, where you are often in the position of trying to predict whether a metric will be valuable enough to justify the extra write, because every single metric or tag you add contributes linearly to write amplification. Ever gotten billed tens of thousands of dollars for your custom metrics, or had to prune your list of useful custom metrics down to something affordable? (“BUT THOSE ARE THE ONLY USEFUL ONES!”, as every ops team wails)


### Events … must pass along the blob of context as the request executes


As you can imagine, it can be a pain in the ass to keep passing this blob of information along the life of the request as it hits many services and databases. So at Honeycomb we do all the annoying parts for you with our integrations. You just install the go pkg or ruby gem or whatever, and under the hood we:

1. initialize an empty debug event when the request enters that service
2. prepopulate the empty debug event with any and all interesting information that we already know or can guess.  language type, version, environment, etc.
3. create a framework so you can just stuff any other details in there as easily as if you were printing it out to stdout
4. pass the event along and maintain its state until you are ready to error or exit
5. write the extremely wide event out to honeycomb


Easy!


(Check out this killer talk from [@lyddonb](http://twitter.com/lyddonb) on … well everything you need to know about life, love and distributed systems is in here, but around the 12:00 mark he describes why this approach is mandatory. WATCH IT. [https://www.youtube.com/watch?v=xy3w2hGijhE&feature=youtu.be](https://www.youtube.com/watch?v=xy3w2hGijhE&feature=youtu.be))


### Events … should collect context like sticky buns collect dust


Other stuff you’ll want to track in these structured blobs includes:

1. Metadata like src, dst headers
2. The timing stats and contents of every network call (our beelines wrap all outgoing http calls and db queries automatically)
3. Every raw db query, normalized query family, execution time etc
4. Infra details like AZ, instance type, provider
5. Language/environment context like $lang version, build flags, $ENV variables
6. Any and all unique identifying bits you can get your grubby little paws on — request ID, shopping cart ID, user ID, request ID, transaction ID, any other ID … **these are always the highest value data** for debugging.
7. Any other useful application context.  Service name, build id, ordering info, error rates, cache hit rate, counters, whatever.
8. Possibly the system resource state at this point in time.  e.g. values from /proc/net/ipv4 stats


Capture all of it. Anything that ever occurs to you *(“this MIGHT be handy someday”) — *don’t even hesitate, just throw it on the pile. Collect it up in one rich fat structured blob.


### Events … must be unique, ordered, and traceable


You need a unique request ID, and you need to propagate it through your stack in some way that preserves sequence. Once you have that, traces are just a beautiful visualization layer on top of your shiny event data.


### Events … must be stored raw.


Because observability means you need to be able to ask any arbitrary new question of your system without shipping new code, and aggregation is a one-way trip. Once you have aggregated your data and discarded the raw requests, you have destroyed your ability to ask new questions of that data forever. For Ever.


**Aggregation is a one-way trip**.  You can always, always derive your pretty metrics and dashboards and aggregates from structured events, and you can never go in reverse. Same for traces, same for logs. The structured event is the gold standard. Invest in it now, save your ass in the future.


It’s only observability if you can ask new questions. And that means storing raw events.


### Events…are richer than metrics


There’s always tradeoffs when it comes to data. Metrics choose to sacrifice context and connective tissue, and sometimes high cardinality support, which you need to correlate anomalies or track down outliers. They have a very small, efficient data format, but they sacrifice everything else by discarding all but the counter, gauge, etc.


A metric looks like this, by the way.


```
{ metric: "db.query.time", value: 0.502, tags: Array(), type: set }
```


That’s it. It’s just a name, a number and maybe some tags. You can’t dig into the event and see what else was happening when that query was strangely slow. You can never get that information back after discarding it at write time.


But because they’re so cheap, you can keep every metric for every request! Maybe. (Sometimes.) More often, what happens is they aggregate at write time. So you never actually get a value written out for an individual event, it smushes everything together that happens in the 1 second interval and calculates some aggregate values to write out. And that’s all you can ever get back to.


With events, and their relative explosion of richness, we sacrifice our ability to store every single observability event about every request. At FB, every request generated hundreds of observability events as it made its way through the stack. Nobody, NOBODY is going to pay for an o11y stack that is hundreds of times as large as production. The solution to that problem is sampling.


### Events…should be sampled.


But not dumb, blunt sampling at server side. Control it on the client side.


Then sample heavily for events that are known to be common and useless, but keep the events that have interesting signal. For example: health checks that return 200 OK usually represent a significant chunk of your traffic and are basically useless, while 500s are almost always interesting. So are all requests to /login or /payment endpoints, so keep all of them. For database traffic: SELECTs for health checks are useless, DELETEs and all other mutations are rare but you should keep all of them. Etc.


You don’t need to treat your observability metadata with the same care as you treat your billing data. That’s just dumb.


## … To be continued.


I hope it’s now blazingly obvious why observability requires — REQUIRES — that you have access to raw structured events with no pre-aggregation or write-time rollups. Metrics don’t count. Just traces don’t count. Unstructured logs sure as fuck don’t count.


Structured, arbitrarily wide events, with dynamic sampling of the boring parts to control costs. There is no substitute.


For more about the technical requirements for observability, read [this](https://www.honeycomb.io/blog/so-you-want-to-build-an-observability-tool/), [this](https://thenewstack.io/observability-a-3-year-retrospective/), or [this](https://thenewstack.io/observability-the-5-year-retrospective/).


![IMG_4619](https://i0.wp.com/charity.wtf/wp-content/uploads/2018/08/img_4619.jpg?resize=195%2C260&ssl=1)

***The deep fine print: it’s one observability event per request per service hop … because we gather observability detail organized by request id.  Databases may be different.  For example, with MongoDB or MySQL, we can’t instrument them to talk to honeycomb directly, so we gather information about its internal perspective by 1) tailing the slow query log (and turning it up to log all queries if perf allows), 2) streaming tcp over the wire and reconstructing transactions, 3) connecting to the mysql port as root every couple seconds from cron, then dumping all mysql stats and streaming them in to honeycomb as an event.  SO.  Database traffic is not organized around connection length or unique request id, it is organized around transaction id or query id.  Therefore it generates one observability event per query or transaction.*
*In other words: if your request hit the edge, API, four internal services, two databases … but ran 1 query on one db and 10 queries on the second db … you would generate a total of *19 observability events* for this request.*
For more on observability for databases and other black boxes, try
[this blog post](https://www.honeycomb.io/blog/add-observability-to-databases/)
.