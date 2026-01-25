---
title: "Zero Framework Cognition: A Way to Build Resilient AI Applications"
date: 2025-11-02
url: https://steve-yegge.medium.com/zero-framework-cognition-a-way-to-build-resilient-ai-applications-56b090ed3e69
word_count: 2054
source: medium
---


# Zero Framework Cognition: A Way to Build Resilient AI Applications


--


1


Listen


Share


I’ve built four AI-enabled apps this year, all developer productivity tools. While I was building them, I began to notice a pattern:

- In my code,I always want the AI to make decisions. For instance, checking whether some worker task has completed, or categorizing or ranking some output. My feeling is, if it’s tricky to code, just give it to a model, right?
- The AIs have consistently preferred to write code that employs pattern matching, local heuristics, and nasssty little hackses.


I found myself crying, week in and week out, “No! Bad! When we reach a decision point,send it back to the model.Don’t try to hack this on the client side with regular expression matching!”


And they’d say yeah yeah yeah, and do it, but then they’d forget again. So I started having to encode it into the onboarding instructions. I’d say, “Keep the smarts out of the client side!”


But they would disregard this and still try to put hacks into the client. Example: keyword matching. They’ll say, “Let’s look for ‘finished’, ‘done’, ‘complete’.” They love to do that. And it’s a stupid, stupid thing to do. What if the output isn’t in English? We’d miss the decision completely. Or what if the output instead uses synonyms like ‘ended’, ‘concluded’ or ‘finalized’? Our hack would have missed those too. But AIs will just keep adding keywords to the list, because, with palpable irony,they don’t want to send decisions to a model.


I’m not sure if this is the models exhibiting defeatism, or attempting to save costs, or they’re just ignorant… but it became so prevalent that I finally had The Talk with a model over the summer, probably Claude 3.7 Opus, and asked, wth man, why u always do this.


And that’s how we came up withZFC: Zero Framework Cognition. It was a name suggested by Claude, a name that was significantly snappier than my hours of whining had been, so we agreed to use it going forward.


We wrote up the principles of ZFC into the agent onboarding docs, and they have reduced ZFC violations substantially. But more importantly, since the AI still violates ZFC all the time (I discovered a huge violation while writing this post, even), having ZFC principles in the onboarding docs makes it easier to fix violations when they inevitably occur. Just tell the AI, “ZFC violation!” and they’ll understand and fix it without needing any further explanation.


I’ll start by showing ZFC to you — this is the “what” and “how.” And then we’ll go into the “why,” the “where have we seen this before,” and the “ouch my wallet” sections.


Here’s what we tell agents when they join my projects; it’s straight from myAGENTS.mdfiles:


ZFC (Zero Framework Cognition) Principles


Core Architecture Principle:This application ispure orchestrationthat delegates ALL reasoning to external AI. We build a “thin, safe, deterministic shell” around AI reasoning with strong guardrails and observability.


✅ ZFC-Compliant (Allowed)


Pure Orchestration


IO and Plumbing• Read/write files, list directories, parse JSON, serialize/deserialize • Persist to stores, watch events, index documents


Structural Safety Checks• Schema validation, required fields verification • Path traversal prevention, timeout enforcement, cancellation handling


Policy Enforcement• Budget caps, rate limits, confidence thresholds • “Don’t run without approval” gates


Mechanical Transforms• Parameter substitution (e.g.,${param}replacement) • Compilation • Formatting and rendering AI-provided data


State Management• Lifecycle tracking, progress monitoring • Mission journaling, escalation policy execution


Typed Error Handling• Use SDK-provided error classes (instanceofchecks) • Avoid message parsing


❌ ZFC-Violations (Forbidden)


Local Intelligence/Reasoning


Ranking/Scoring/Selection• Any algorithm that chooses among alternatives based on heuristics or weights


Plan/Composition/Scheduling• Decisions about dependencies, ordering, parallelization, retry policies


Semantic Analysis• Inferring complexity, scope, file dependencies • Determining “what should be done next”


Heuristic Classification• Keyword-based routing • Fallback decision trees • Domain-specific rules


Quality Judgment• Opinionated validation beyond structural safety • Recommendations like “test-first recommended”


🔄 ZFC-Compliant Pattern


The Correct Flow


1. Gather Raw Context(IO only)• User intent, project files, constraints, mission state


2. Call AI for Decisions• Classification, selection, composition • Ordering, validation, next steps


3. Validate Structure• Schema conformance • Safety checks • Policy enforcement


4. Execute Mechanically• Run AI’s decisions without modification


That’s what I put inAGENTS.md. That’s ZFC in a nutshell. I’ve elided some examples, and a bit about compliance checking and enforcement, but that’s the gist of it.


Why ZFC?


Well, for a rich underlying theory that predates GenAI, but certainly foreshadows and anticipates ZFC, we can thank industry legend and superhero Martin Fowler.


A brief but related aside: Martin Fowler became a superhero to me in 1999 with his book,Refactoring, which had a greater impact on me as a programmer than anything I’d ever read before and probably since. Almost nobody read it! IDEs encoded about 5% of the book into hardwired tool menus, and everyone thought that was all there was to it.


But Refactoring was so much more: it was a way of thinking about code that was revolutionary. Martin Fowler pushed us to stop worrying about function-call overhead, and to start writing code for humans. Fowler was encouraging us to embrace exponentials long before Dr. Karpathy coined the lovely phrase. There was so much more to his book than the mechanical stuff you see in IDEs. It’s a timeless masterpiece that applies equally today to writing code for AIs.


Backstory concluded, we return to the main plot. Fifteen years later, in 2014, Martin Fowler and James Lewis laid the groundwork for ZFC with theirSmart Endpoints and Dumb Pipes. This is a microservices architectural principle in whichall the intelligence remains in the endpoints, while the communication infrastructure remains as simple as possible.


ZFC mirrors this with the “dumb framework, smart model” division. The main difference is that microservices deal with decentralizing business logic across services, whereas ZFC deals with outsourcing cognitive reasoning. But architecturally, ZFC conceptually treats an AI model as the smart endpoint.


“Smart endpoints and dump pipes” isn’t the only architectural pattern that creates a division between intelligence and orchestration infrastructure. We have a long, rich history of building systems thatseparate mechanism from policy— famously, Unix. To me, ZFC feels like the AI world’s version of a lot of similar-looking ideas from the past 30–40 years.


Maybe most interestingly, seven years ago, long before GPT-3, Dr. Andrej Karpathy gave us the language–and effectively, the philosophical framework–for talking about replacing code with models inSoftware 2.0.Both that and his more recent Software 3.0 are visions where software is just glue and piping that links models together. In his vision, it’s for gathering training data.


But you can achieve a lot of that vision today, in my opinion, using ZFC to harness AI workers on short leashes, but still letting AI do its thing.


But Whyyyyyyy, You Never Said Why


OK, fair enough.


Why?Because regular expressions suck.Thank you for coming to my TED Talk.


If you want an application that processes work queues 24x7(you do), and you want it to replace human labor(you do, even if it’s your own labor), then you’re going to have to call models many times, and orchestrate them.


You can’t just give one big task to one big model and let it run forever.


When you build your orchestration, connecting AI models together, it will be very tempting to try to have your application wear Big Boy Pants too, asserting itself by making some of its own decisions.


But you arebound to miss edge casesif you’re using any kind of old-fashioned pattern matching, ranking, semantic analysis, fallback rule, heuristics, or any other kind of cognitive treatment–especially when operating on text that isn’t 100% pure code.Double-especiallyif you are trying to look at (a) AI output, (b) human output, or (c) tool output. Do not try parsing these at home anymore, folks, lest ye be the toole.


ZFC violations make your program brittle. It will panic for no reason, have more failures, retry more often, have lower throughput, higher downtime, and will feel like it has developed a serious attitude problem. Your program will suck.


ZFC-compliant apps arenaturally resilient, because AIs can handle a multitude more edge cases. Moreover, you can build them so that any AI worker has a way to respond to any situation with a system orchestration request, rather than actually doing the work. You can let the AI exercise its decision power at any point where it might be needed.


For instance, your worker might size up its task and say, “this task is too big for me, we need to go break it up and resubmit it.” This can all be done with dumb pipes that are sending structured requests around to smart models at the right cognitive tier levels.


For instance, you could route all of your butt-kissing tasks to GPT-4o, which is good at it. From a ZFC perspective, as long as it’s an AI that decides it’s a bum smooch, and not some bum-smooching pattern matcher in your client code, you will be 100% ZFC-compliant.


Building a truly self-healing workflow app is still a surprising amount of work. But I’ve found that ZFC at least gets you going in the right direction as soon as you set out.


I don’t know if ZFC is right for all applications.


On the one hand, all of my AI-enabled apps this year have been dramatically improved by ZFC. On the other hand, they’re all variations on coding agent tools, and primarily deal with code generation, which is its own (highly verifiable) unique space. So maybe I’m just in an area where it works well.


On the other hand, itfeelskinda universal. Because regular expressions suck. Surely you remember my TED Talk?


Last Chapter: Cost Optimizing ZFC


The main problem with ZFC is that it’s expensive, because you are replacing code with model calls. To justify ZFC, you have to be like Fowler and Karpathy, and steer hard into the curves. AIsaregetting smarter, but the dumb models never go away, and they are getting cheaper while remaining incredibly useful, as we saw in our recent butt-smooch example.


AI is evolving into a pyramid of models, smartest at the top. That is convenient, because all knowledge work can be decomposed into pyramids of cognitive tasks, hardest at the top. There will be a place in this world for the likes of Sonnet 3.5 and GPT-4o for all eternity, because they can slog and smooch away at the bottom. Smarter models will give them work, via decomposition.


Even today you can see the separation and how useful it already is: Claude Haiku, Sonnet, and Opus. You delegate the really hard stuff to Opuspensive (Opus’s full name, a little-known factoid.) Delegate as much easy stuff as you can to Haiku. Sonnet gets the rest. It’s a perfect Goldilocks setup. I think it’ll get finer grained, but it doesn’t necessarilyneedto. You already have the knobs you need for cost optimization today.


Perhaps surprisingly, not everyone is using those knobs yet. The poster child offender: coding agents. The problem with coding agents today is that they send all requests to the medium model (or the smart one if you’ve got extended thinking turned on), when probably 50% to 80% of the traffic could have gone to the cheap model.


If you build a ZFC-enabled app, you can cost-optimize by having AI decompose your work into tasks explicitly labeled high-, medium-, or low-tier cognition, and then you delegate each task to the smoochiest-match model class.


That’s it! That’s the pattern, for large classes of applications going forward. You start with some work. An AI decomposes it and sorts it. You file it, someone assigns workers, and then you have a dumb-pipe, ZFC-compliant orchestrator that routes every task to the smallest AI model that can handle it.


Call To Action


Go back to work. We’re done. Thanks for coming. Stop using regular expressions, maybe?


If you’re building an application that is already calling models to do work, I think you’re officially on the slippery slope towards ZFC.


And with that, thank you for coming to my ZFC talk. Let me know what you think. Like, subscribe, and comment. Retweet on MySpace. All that stuff.


P.S. Ourbookcame out today! So exciting. If you enjoyed any of the jokes or insights in this post, there are plenty more like them in the book!

