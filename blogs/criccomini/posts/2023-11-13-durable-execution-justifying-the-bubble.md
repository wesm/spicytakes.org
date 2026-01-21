---
title: "Durable Execution: Justifying the Bubble"
subtitle: "From Temporal to an overflowing market, durable execution is having a moment. The space is too crowded and frameworks are hard to use. What needs to change?"
date: 2023-11-13T11:01:31+00:00
url: https://materializedview.io/p/durable-execution-justifying-the-bubble
slug: durable-execution-justifying-the-bubble
word_count: 1061
---


There’s been a surge in durable execution frameworks over the past 6 to 12 months.Temporalhas been the go-to for a while but many new projects and companies are emerging. Let’s look at why, and what needs to change.


![](https://substackcdn.com/image/fetch/$s_!wu5n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb50e442-db8d-408d-bf1f-ad12ed329767_689x250.png)


## Durable execution explained


Temporal’sBuilding Reliable Distributed Systems in Nodeblog post does a decent job of defining durable execution:


> Durable execution systems run our code in a way that persists each step the code takes. If the process or container running the code dies, the code automatically continues running in another process with all state intact, including call stack and local variables.


Essentially, this is workflow orchestration with transactional state management.


We needed durable execution atWePay, the last company I worked for. WePay did payment processing and had to safely move money between accounts.


A money movement request can be in dozens of different states (like the “pending” state you see when you pay at a gas pump). State changes sometimes happen over long periods of time (weeks or months) and systems sometimes attempt invalid state changes. And state changes must happen transactionally.


Payment processing is a very common durable execution use case. So much so that nearly every durable execution system uses payments (or shopping carts) as their canonical example. Here’s Temporal’sMoneyTransfer(…)example. And here’sRestate’saddTicketToCart. Oh, and here’sOrkes’sdeposit_payment.


## The space is crowded


There are now many durable execution companies:

- Temporal
- Restate
- Orkes
- StealthRocket
- LittleHorse
- Flawless
- Convex
- Rama


I’m sure I’ve missed many more (Azure Durable Functions?), to say nothing of the various open source projects.


The current market can’t sustain this many startups. For even a few big winners, the market has to become much larger. And for the market to become larger—to expand beyond payments and shopping carts—new use cases must be added.


Durable execution can subsume many common tasks such as work queues, batch workflows, stream processing, ETL, and more. Temporal alreadyshowcasesbusiness transaction, business process applications, and infrastructure management use cases.


Yet many application developers don’t pick durable execution frameworks as the first choice for such use cases.


## Frameworks are hard to use


The adoption cost for durable execution is too high because the frameworks are too hard to use. Temporal is probably the pinnacle of usability at the moment, and itsPython courseis daunting. I don’t use these frameworks unless Ihaveto.


![](https://substackcdn.com/image/fetch/$s_!fmMi!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9149462-df08-49b9-bdc6-6b986b0f04b2_689x142.png)


Chris Gillum, the creator ofAzure Durable Functions, summarizes many challenges in his post,Common Pitfalls with Durable Execution Frameworks, like Durable Functions or Temporal. To move beyond the payments-style use cases, Gillum’s issues must be addressed.


The good news is there’s a lot of experimentation happening! I’vealready highlightedLittleHorse’suser tasksthat marry durable execution with traditionalBPMN-style workflows;Camundais coming from the opposite direction, from BPMN toward durable execution;Chris Gillumis working ondurabletask-go;StealthRocketis playing withdurable coroutines; AndRamais just… way, way out there.


## Reconciling with stream processing


Stream processing is the biggest opportunity for experimentation. Many of the common pitfalls that Chris lists inhis postare exactly the same problems that make stream processing hard: non-determinism, idempotency, at-least-once semantics, schema evolution, payload size, dead letter queues, and the list goes on. We dealt with the same problems when buildingApache Samza(LinkedIn’s stream processor) ten years ago.


This week,Responsive’s [$] founder,Apurva Mehta,pointed outthat stream processing can address many durable execution use cases.Maxim Fateev(Temporal’s CEO) responded:


![](https://substackcdn.com/image/fetch/$s_!xY0h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc8c587d5-52c9-408d-9a23-11dc1054d08c_687x167.png)


I agree with Maxim, but stream processorscould beused for these use cases with proper APIs and some Kafka improvements. Three such improvements are two-phase commit (KIP-939), Kafka queues (KIP-932), and optimistic locking on message keys (KAFKA-2260). We actually implemented the last one (locking) inWaltz, which we used to—you guessed it—build a durable execution framework for our payments state machine.


Stream processing also offers solutions to some of the problems that Gillum lists. Versioning, in particular, is something that the Kafka community has spent 15 years thinking about. Gillum even mentions this in his post (emphasis added).


> There are two primary approaches that I’ve seen for dealing with the code versioning challenge. One is to make the code aware of different versions by adding if/else checks against version numbers.It’s not unlike putting schema version numbers in queue messages.… Durable Functions instead proposes deploying code changes into a separate copy of the app… Doing so removes the problem of needing to be careful about code changes but places a burden on the developer to manage multiple versions of their apps running side-by-side.


There’s an opportunity for collaboration and convergence here.


Restate,LittleHorse,Convex, andRamaare companies to look at in this space. They bridge stream processing, serverless functions, and transactional state management. These new frameworks often use a log like Kafka to store state.


> Restate’s core is a distributed Raft log of events and commands, with indexes, the ability to compute over the log (to actualize commands) and to invoke functions/handlers based on events.


Convexdoes the same.Why We Built Restate’s first FAQ question is literally,"Well, isn’t this just like Kakfa plus Temporal?”, and their follow-on blog post isRestate + Kafka. LittleHorse is perhaps the best example; itactually isbuilt on top of Kafka and Kafka Streams. A log-based architecture is standard for durable execution frameworks. Merging compute paradigms and APIs is a logical next step.1


## Moving forward


Right now, we have a collection of first-generation durable execution and stream processing frameworks. No one has really nailed the hard parts and the APIs are clunky. That’s not a dig on any of these teams; these problems are really, really tough. I have the scars to prove it.


My hope is that second-generation frameworks will unify stream processing and durable execution with a more user-friendly API. Such a product would greatly expand the TAM for durable execution (or stream processing, for that matter) and justify the current durable execution bubble.


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.

[1](https://materializedview.io/p/durable-execution-justifying-the-bubble#footnote-anchor-1-138469997)

Andreessen Horowitz writes about durable execution inThe Modern Transactional Stack. The authors coin the term application logic transactional platform (ALTP). While an excellent overview, their framing is wrong. Where a16z sees a database, I see a write-ahead log. And when you have a write-ahead log, stream processing (or event-driven serverless functions) are the natural building block for computation. Thus it’s stream processing and durable execution (ALTPs) that should be reconciled, not workflow-centric and database-centric approaches, as they suggest.
