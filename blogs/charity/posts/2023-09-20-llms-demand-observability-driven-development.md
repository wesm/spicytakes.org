---
title: "LLMs Demand Observability-Driven Development"
date: 2023-09-20
url: https://charity.wtf/2023/09/20/llms-demand-observability-driven-development/
word_count: 2675
---


[*Originally posted on the Honeycomb blog on September 20th, 2023*](https://www.honeycomb.io/blog/llms-demand-observability-driven-development)


Our industry is in the early days of an explosion in software using LLMs, as well as (separately, but relatedly) a revolution in how engineers write and run code, thanks to generative AI.


Many software engineers are encountering LLMs for the very first time, while many ML engineers are being exposed directly to production systems for the very first time. Both types of engineers are finding themselves plunged into a disorienting new world—one where a particular flavor of production problem they may have encountered occasionally in their careers is now front and center.


Namely, that **LLMs are black boxes that produce [nondeterministic outputs](https://community.openai.com/t/a-question-on-determinism/8185) and cannot be debugged or tested using traditional software engineering techniques.** Hooking these black boxes up to production introduces reliability and predictability problems that can be terrifying. It’s important to understand this, and why.


## 100% debuggable? Maybe not


Software is traditionally assumed to be testable, debuggable, and reproducible, depending on the flexibility and maturity of your tooling and the complexity of your code. **The original genius of computing was one of constraint;** that by radically constraining language and mathematics to a defined set, we could create algorithms that would run over and over and always return the same result. *In theory*, all software is debuggable. However, there are lots of things that can chip away at that beauteous goal and make your software mathematically less than 100% debuggable, like:

- Adding concurrency and parallelism.
- Certain types of bugs.
- Stacking multiple layers of abstractions (e.g., containers).
- Randomness.
- Using JavaScript (HA HA).


There is a much longer list of things that make software less than 100% debuggable in practice. Some of these things are related to cost/benefit tradeoffs, but most are about weak telemetry, instrumentation, and tooling.


If you have only instrumented your software with metrics, for example, you have no way of verifying that a spike in `api_requests` and an identical spike in 503 errors are for the same events (i.e., you are getting a lot of `api_requests` returning 503) or for a disjoint set of events (the spike in `api_requests` is causing general congestion causing a spike in 503s across ALL events). It is mathematically impossible; all you can do is guess. But if you have a log line that emits both the `request_path` and the `error_code`, and a tool that lets you break down and group by arbitrary dimensions, this would be extremely easy to answer. Or if you emit a lot of events or wide log lines but cannot trace them, or determine what order things executed in, there will be lots of other questions you won’t be able to answer.


There is another category of software errors that are logically possible to debug, but prohibitively expensive in practice. Any time you see a report from a big company that tracked down some obscure error in a kernel or an ethernet device, you’re looking at one of the rare entities with 1) enough traffic for these one in a billion errors to be meaningful, and 2) enough raw engineering power to dedicate to something most of us just have to live with.


But software is typically understandable because we have given it structure and constraints.


IF (); THEN (); ELSE () is testable and reproducible. **Natural languages, on the other hand, are infinitely more expressive than programming languages, query languages, or even a UI that users interact with.** The most common and repeated patterns may be fairly predictable, but the long tail your users will create is *very long*, and they expect meaningful results there, as well. For complex reasons that we won’t get into here, LLMs tend to have a lot of randomness in the long tail of possible results.


So with software, if you ask the exact same question, you will always get the exact same answer. With LLMs, you might not.


## LLMs are their own beast


Unit testing involves asserting predictable outputs for defined inputs, but this obviously cannot be done with LLMs. Instead, ML teams typically build evaluation systems to evaluate the effectiveness of the model or prompt. However, to get an effective evaluation system bootstrapped in the first place, you need quality data based on real use of an ML model. **With software, you typically start with tests and graduate to production. With ML, you have to *start* with production to generate your tests.**


Even bootstrapping with early access programs or limited user testing can be problematic. It might be ok for launching a brand new feature, but it’s not good enough for a real production use case.


> Early access programs and user testing often fail to capture the full range of user behavior and potential edge cases that may arise in real-world usage when there are a wide range of users. All these programs do is delay the inevitable failures you’ll encounter when an uncontrolled and unprompted group of end users does things you never expected them to do.


Instead of relying on an elaborate test harness to give you confidence in your software a priori, it’s a better idea to embrace a “ship to learn” mentality and release features earlier, *then* systematically learn from what is shipped and wrap that back into your evaluation system. And once you have a working evaluation set, you also need to figure out how quickly the result set is changing.


Phillip gives this list of things to be aware of when [building with LLMs](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm):

- Failure will happen—it’s a question of *when*, not *if.*
- Users will do things you can’t possibly predict.
- You will ship a “bug fix” that breaks something else.
- You can’t really write unit tests for this (nor practice TDD).
- Latency is often unpredictable.
- Early access programs won’t help you.


Sound at all familiar? 😂


## Observability-driven development is necessary with LLMs


Over the past decade or so, teams have increasingly come to grips with the reality that the only way to write good software at scale is by looping in production via observability—not by test-driven development, but *observability*-driven development. This means shipping sooner, observing the results, and wrapping your observations back into the development process.


Modern applications are dramatically more complex than they were a decade ago. As systems get increasingly more complex, and nondeterministic outputs and emergent properties become the norm, **the only way to understand them is by instrumenting the code and observing it in production.** LLMs are simply on the far end of a spectrum that has become ever more unpredictable and unknowable.


Observability—both as a practice and a set of tools—tames that complexity and allows you to understand and improve your applications. We have written a lot about what differentiates observability from monitoring and logging, but the most important bits are 1) the ability to gather and store telemetry as very wide events, ordered in time as traces, and 2) the ability to break down and group by any arbitrary, [high-cardinality dimension](https://www.honeycomb.io/getting-started/understanding-high-cardinality-role-observability). This allows you to explore your data and group by frequency, input, or result.


In the past, we used to warn developers that their software usage patterns were likely to be unpredictable and change over time; now **we inform you that if you use LLMs, your data set *is going to be* *unpredictable*, and *it will absolutely change* over time, and you *must* have a way of gathering, aggregating, and exploring that data without locking it into predefined data structures.**


With good observability data, you can use that same data to feed back into your evaluation system and iterate on it in production. The first step is to use this data to evaluate the representativity of your production data set, which you can derive from the quantity and diversity of use cases.


You can make a surprising amount of improvements to an LLM based product without even touching any [prompt engineering](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm), simply by examining user interactions, scoring the quality of the response, and acting on the correctable errors (mainly data model mismatches and parsing/validation checks). You can fix or handle for these manually in the code, which will also give you a bunch of test cases that your corrections actually work! These tests will not verify that a particular input always yields a correct final output, but they will verify that a correctable LLM output can indeed be corrected.


You can go a long way in the realm of pure software, without reaching for prompt engineering. But ultimately, **[the only way to improve LLM-based software](https://www.honeycomb.io/blog/improving-llms-production-observability) is by adjusting the prompt, scoring the quality of the responses (or relying on scores provided by end users), and readjusting accordingly. **In other words, improving software that uses LLMs can only be done by observability and experimentation. Tweak the inputs, evaluate the outputs, and every now and again, consider your dataset for representivity drift.


Software engineers who are used to boolean/discrete math and TDD now need to concern themselves with data quality, representivity, and probabilistic systems. ML engineers need to spend more time learning how to develop products and concern themselves with user interactions and business use cases. *Everyone* needs to think more holistically about business goals and product use cases. There’s no such thing as a LLM that gives good answers that don’t serve the business reason it exists, after all.


## So, what do you *need* to get started with LLMs?


Do you need to hire a bunch of ML experts in order to start shipping LLM software? Not necessarily. You cannot (there aren’t enough of them), you should not (this is something everyone needs to learn), and you don’t want to (these are changes that will make software engineers categorically more effective at their jobs). Obviously you will need ML expertise if your goal is to build something complex or ambitious, but entry-level LLM usage is well within the purview of most software engineers. It is definitely easier for software engineers to dabble in using LLMs than it is for ML engineers to dabble in writing production applications.


But learning to write and maintain software in the manner of LLMs is going to transform your engineers and your engineering organizations. And not a minute too soon.


The hardest part of software has *always* been running it, maintaining it, and understanding it—in other words, operating it. But this reality has been obscured for many years by the difficulty and complexity of writing software. We can’t help but notice the upfront cost of writing software, while the cost of operating it gets amortized over many years, people, and teams, which is why we have historically paid and valued software engineers who write code more than those who own and operate it. When people talk about the 10x engineer, everyone automatically assumes it means someone who churns out 10x as many lines of code, not someone who can operate 10x as much software.


But generative AI is about to turn all of these assumptions upside down. All of a sudden, writing software is as easy as sneezing. Anyone can use ChatGPT or other tools to generate reams of code in seconds. But understanding it, owning it, operating it, extending and maintaining it… all of these are more challenging than ever, because **in the past, the way most of us learned to understand software was by *writing* it.**


What can we possibly do to make sure our code makes sense and works, and is extendable and maintainable (and our code base is consistent and comprehensible) when we didn’t go through the process of writing it? Well, we are in the early days of figuring that out, too. 🙃


If you’re an engineer who cares about your craft: do code reviews. Follow coding standards and conventions. Write (or generate) tests for it. But ultimately, the only way you can know for sure whether or not it works is to ship it to production and [watch what happens](https://www.honeycomb.io/blog/testing-in-production).


This has *always* been true, by the way. **It’s just *more* true now.**


If you’re an engineer adjusting to the brave new era: take some of that time you used to spend writing lines of code and reinvest it back into understanding, shipping under controlled circumstances, and observing. This means instrumenting your code with intention, and inspecting its output. This means shipping as soon as possible into the production environment. This means using feature flags to [decouple deploys from releases](https://www.honeycomb.io/blog/deploys-wrong-way-change-user-experience) and gradually roll new functionality out in a controlled fashion. Invest in these—and other—guardrails to make the process of shipping software more safe, fine-grained, and controlled.


Most of all, it means developing the habit of *looking at your code* in production, through the lens of your telemetry, and asking yourself: **does this do what I expected it to do? Does anything else look weird?**


Or maybe I should say “looking at your systems” instead of “looking at your code,” since people might confuse the latter with an admonition to “read the code.” The days when you could predict how your system would behave simply by reading lines of code are long, *long* gone. Software behaves in unpredictable, emergent ways, and the important part is observing your code *as it’s running in production, while users are using it.* Code in a buffer can tell you very little.


## This future is a breath of fresh air


This, for once, is not a future I am afraid of. It’s a future *I cannot wait* to see manifest. For years now, I’ve been giving talks on modern best practices for software engineering—**developers owning their code in production, testing in production, observability-driven development, continuous delivery in a tight feedback loop, separating deploys from releases using feature flags.** No one really disputes that life is better, code is better, and customers are happier when teams adopt these practices. Yet, only 11% of teams can deploy their code in less than a day, according to the DORA report. Only a tiny fraction of teams are operating in the way everybody agrees we all should!


Why? The answers often boil down to organizational roadblocks, absurd security/compliance policies, or lack of buy-in/prioritizing. Saddest of all are the ones who say something like, “our team just isn’t that good” or “our people just aren’t that smart” or “that only works for world-class teams like the Googles of the world.” *Completely false*. Do you know what’s *hard*? Trying to build, run, and maintain software on a two month delivery cycle. Running with a tight feedback loop is *so much easier*.


## Just do the thing


So how do teams get over this hump and prove to themselves that they can have nice things? In my experience, only one thing works: when someone joins the team who has seen it work before, has confidence in the team’s abilities, and is empowered to start making progress against those metrics (which they tend to try to do, because people who have tried writing code the modern way become *extremely unwilling *to go back to the bad old ways).


And why is this relevant?


I hypothesize **that over the course of the next decade, developing with LLMs will stop being anything special, and will simply be one skill set of many**, alongside mobile development, web development, etc. I bet most engineers will be writing code that interacts with an LLM. I bet it will become not *quite* as common as databases, but up there. And while they’re doing that, they will *have* to learn how to develop using short feedback loops, testing in production, observability-driven development, etc. And once they’ve tried it, they too may become *extremely unwilling* to go back.


In other words, LLMs might ultimately be the Trojan Horse that drags software engineering teams into the modern era of development best practices. (We can hope.)


In short, LLMs demand we modify our behavior and tooling in ways that will benefit even ordinary, deterministic software development. Ultimately, these changes are a gift to us all, and the sooner we embrace them the better off we will be.
