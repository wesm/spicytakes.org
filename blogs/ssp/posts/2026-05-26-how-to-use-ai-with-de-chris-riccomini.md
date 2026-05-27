---
title: "Plan Mode All the Time, Substrait over SQL, and the End of the DE Role ft. Chris Riccomini"
date: 2026-05-26
url: https://www.ssp.sh/blog/how-to-use-ai-with-de-chris-riccomini/
slug: how-to-use-ai-with-de-chris-riccomini
word_count: 4398
---

![Plan Mode All the Time, Substrait over SQL, and the End of the DE Role ft. Chris Riccomini](https://www.ssp.sh/blog/how-to-use-ai-with-de-chris-riccomini/featured-image.png)

Contents
This article was written as part of
[my services](https://www.ssp.sh/services)

This series interviews (see [#1 with Mark Freeman](https://www.ssp.sh/blog/specs-over-vibes-interview-mark-freeman/)) real practitioners to extract the patterns behind how they actually use AI in their data work today. This is the second interview in ‘How to use AI with DE’, and this time we have none other than [Chris Riccomini](https://www.linkedin.com/in/riccomini/).


Chris has seen the data stack evolve over the years. He thinks AI will soon handle the majority of data engineering work, provided with the right tooling and access to CLIs and APIs. He also thinks LLMs might not speak SQL, but a format that represents data transformations. With so much shifting and changing currently in the AI space, new models, new workflows weekly, Chris’s perspective helps you navigate without overreacting, based on a long experience in the domain.


The article is structured in four parts: **(1)** correctness when working with financial data, **(2)** the Ralph Loop and why AI might be better off speaking something other than SQL, **(3)** vulnerabilities and the case for “Okta for Agents,” and **(4)** the future of AI — including why “data engineer” as a distinct role might not survive.


## Introducing the Guest: #2 Chris Riccomini


Chris Riccomini is a Software Engineer, Author, [Investor](https://materializedview.capital/), and Advisor. Previously at WePay, LinkedIn, PayPal, and author of [The Missing README: A Guide for the New Software Engineer](https://www.amazon.com/Missing-README-Guide-Software-Engineer/dp/1718501838) and co-author of 2nd version of the iconic [Designing Data-Intensive Applications](https://www.amazon.com/dp/1098119061) book.


Chris has been working in open source throughout his career. He is the author of [Apache Samza](https://github.com/apache/samza), a distributed stream processing framework. His current project is SlateDB, an embedded key-value store built on object storage. He is also on the [Apache Airflow’s PMC](https://projects.apache.org/committee.html?airflow).


## Correctness of Data in the Financial Sector: How Does This Work with AI?


Chris had worked at financial companies where **data correctness** is essential. My first question was “How do you see using AI in data when financial services, or most other places, must be correct? How do you mitigate the small errors AI still makes in such a situation?” His response:


> It really depends on where in the stack AI is being deployed.


### Use Cases with Different Risk Profiles


**Risk, fraud and compliance**. The bar is model explainability, you need to know *why* the model made the decision it did:


> If AI is involved in decisioning around risk and fraud, compliance and “model explainability” comes into play (why the model made the decision it did). This is one of the reasons we really liked random forest models at WePay: you could explain the actual rules that the model had derived and used in order to make a decision.


The **data engineering context**, compared to a traditional data modeling situation, is interesting:


> If AI is being used in a data engineering context, it seems to me more like a **traditional data modeling situation**. You should be able to define invariants that must always be true for your data. For example, the ledger should always sum up. This is how we managed our data pipelines. If AI is defining data integration pipelines and moving data, the invariants should still hold. Traditional data verification tools will continue to play a role there.


For **data analytics**, this is where most of the fear lives:


> There is a fear that AI will hallucinate and cause a bad decision to be made. **I think this is a reasonable fear, but it’s also a problem we had before AI.** Data in any organization is messy. Semantics aren’t always clear, contracts get broken, and so on.* *Every company I’ve worked for has had this problem. It’s **not uncommon to find an incorrect query** that’s been rolled up into a weekly ops review with the CEO, for example. This was true before AI.


So the question, is whether AI makes this worse or better. Chris own view has shifted recently:


> If you’d asked me two years ago, I would have said it was definitely going to get worse. Now, I think it might actually get better, especially if we **pair AI with a human**. The latest LLMs have gotten really good at spotting bugs, inconsistencies, and so on. My personal experience is that I’m both **more productive and more accurate with an AI**.


I am having a similar experience: for working data engineering projects, if I use it for a not-too-distant future, meaning if the scope is clear and in a framework or rigid structure, it can implement a great solution since last December 2025, when the models got better. With it, it can go a long way, but still, it can’t work autonomously, or do a full project from scratch. It still needs a lot of hand-holding, as it does not understand the business.


So, balancing quantity with quality and keeping up with reviews at the speed of generation is also a challenge, especially since the model usually generates many lines of code. But for my writing process, where my personal voice plays a bigger role, I find that AI can’t help me too much yet in the actual writing process - but on the surrounding tasks (research, brainstorming, though also limited for new topics that are not based on existing ideas).


### LLM Should Speak Substrait, not SQL


Chris [said recently](https://x.com/criccomini/status/1946674377153786327) that: “*Similar to my belief that LLM should speak substrait, not SQL*”. I asked him to explain this quote and he said:


> This is more of an intuition than something I’ve demonstrated to be true. But if you look at the way we use SQL, it’s actually used in two different ways: **by humans and by machines**. I think both can benefit from [Substrait](https://substrait.io/) (or some equivalent).


Chris continues to explain that “***Substrait is a format that represents data transformations**. It has many operations that SQL has, but unlike SQL, which is purely logical, **Substrait lets you define physical operations** as well. In SQL, you say JOIN, but in Substrait you can say how to join: merge join or hash join? For those with a compilers background, Substrait can express both abstract and concrete syntax trees–intermediate representations (IRs).*”


This is valuable for LLMs for two reasons:


> 1. You should be able to **express SQL with fewer tokens** (provided the serialization format for the logical operations is more efficient than english). This should make LLMs slightly cheaper to use, but more importantly it should **keep them from hallucinating quite as much**. (Granted hallucinations are less of a problem than they used to be).
> 2. More importantly, LLMs are pretty smart. They should be able to do query optimization really well. And Substrait **gives them that ability–they can express physical operators** (e.g. merge vs. hash), not just logical ones. This should allow them to do **query optimization on the client side**, and pass a physical query plan directly to the DB for execution (provided they have access to the requisite table statistics).


Substrait, as an emerging standard that provides cross-language serialization for relational algebra, is very interesting and something I want to check out, especially the expressiveness compared to SQL.

Downside of Substrait: LLMs are less familiar

Of course, there is a ton of SQL on the internet, so it’s not clear that LLMs will be as amenable to working with lesser known formats like Substrait. I think it’s worth experimenting with, though.


## Making AI Output More Reliable


What I learned is that the longer something is in the future, the more vague or incorrect or hallucinated the outcome can be. So the more context and code you can provide, the more accurate the result. Which is pretty much in line with Substrait.


But how do we work with the LLMs, what’s the best approach, using `god mode` in OpenClaw or `--dangerously-skip-permissions` in Claude Code with no limits where it can go indefinitely with not much more context? I asked Chris if that’s also what he observed, and if he uses `plan mode` and a declarative approach or pipelines, as it helps for context and collaborating with the AI on a shared output, usually Markdown.


> I was having coffee with a friend of mine, lamenting about this very problem a month or two ago. I was trying to get Codex to do something complex and it just kept falling on its face. My friend told me that you have to live in plan mode all the time. You can’t just ask it to plan the work, then flip to “Implement this plan.” You **need to have the LLM iterate on the plan** for many iterations. Probe its plan, ask it for details, ask it to expand sections, and so on. You need to get to the point where you feel like there’s no possible way the LLM can’t implement the plan incorrectly.

Spec-driven AI work

On the note of “needing to have the LLM iterate on the plan for many iterations”, Mark Freeman suggested in [previous interview](https://www.ssp.sh/blog/specs-over-vibes-interview-mark-freeman/) the spec-driven development (SDD) approach with the open-source GitHub [Spec Kit](https://github.com/github/spec-kit), check it out or read the previous interview for more context.


### The Ralph Loop: And Managing Context


After having a plan at hand, the next step is to keep the LLM’s working memory lean:


> Once you have a good plan, you **need to manage context**. In some cases, you will need to take your plan and start with a fresh context in the LLM. In other cases, you’ll need to clear the context periodically throughout the work. I use a [Ralph Loop](https://ghuntley.com/loop/) for such cases1.


I had the exact same experience when working with smaller code bases: to refresh context, the insights you gain over the iterations are not as effective if you add them bit by bit, compared to if you refresh memory and start over with all the new key insights provided at the very beginning, steering the model to a more tailored direction earlier on.


But with the Ralph Loop, which refers to understanding AI beyond surface-level applications, you get new insights that you can then add to your initial prompt, that you wouldn’t have gained otherwise, by exploring deeper programmable patterns.


The loop is an iterative, autonomous AI development technique where a bash loop (or plugin) repeatedly prompts an AI agent with the same goal, forcing it to persistently iterate until tasks pass external tests. It forces the AI to work, fail, and fix errors until success, rather than relying on the AI to decide it is finished.


On top of that, Chris says “*You also need to impose a lot of quality gates. As with plan mode, you need to overdo it. ‘Quality’ is a bit of a squishy term*’”, and he breaks it into three steps:


> 1. Define what quality is for your use case.
> 2. Measure the quality.
> 3. Enforce thresholds (gates) that your LLM must adhere to.

Example by Chris with the three steps for assessing quality

*For example, part of your definition of quality might be test coverage. So that’s step 1. Then you set up a coverage tool for your codebase–step 2. Then, you put the phrase, “You always run tests before commit and keep test coverage above 90%,” in your [CLAUDE.md](http://CLAUDE.md). Finally, you install a git commit hook that enforces this rule.*


*This is a very rudimentary example, but you get the idea. There are a ton of different things you can measure and monitor for your work. I enumerate many in the post [Code Quality Gates for Vibe-Coded Projects](https://rng.md/posts/code-quality-for-vibe-coded-projects/).*


This essentially means we as the Prompt Engineers need to make sure that the workflow is correct, that we understand what we need to do, and accordingly adapt the workflow to get better code quality.


### What about Functional Data Engineering, and Executing Deterministically?


In related terms, just as AI might hallucinate, it also might generate different outcomes with the same questions and same context. It’s non-deterministic. But data engineering works especially well if it’s done reproducibly, so we can backfill our data pipelines reliably and trust they will fill the same way.


This also ties into functional data engineering, running jobs with reproducibility and idempotent. I asked Chris what he thinks about this dilemma.


> I’m not as worried about this as I used to be. A lot of **tooling** has popped up or evolved to help address this. **Durable execution frameworks** try to address some of this by papering over the non-determinism to keep replays deterministic **by skipping the previously-successful** parts of the flow. Ditto for traditional workflow orchestration systems like Airflow, Prefect, and Dagster. (Disclaimer: I have some Prefect shares.)


### Moving to Incremental-loads for Better Determinism?


What I found interesting was Chris’s next suggestion: moving to smaller data sizes, and therefore to loading incrementally for a more reproducible outcome.


> We can also move from full batch data processing to **incremental batch** data processing to help eschew some non-determinism.


A concrete example, splitting load by day:


> Imagine, you have a bulk load job that always loads a full table from PostgreSQL into Snowflake, and that job does some LLM-based processing. Every time you re-run it, you’re going to get non-deterministic output. But if you convert it to an incremental job that runs daily and always loads the previous day’s data, then a re-run will only introduce non-determinism into the last day’s load. And presumably you’re re-running that day because something went wrong. In such a case, non-determinism is likely acceptable.


This is great thinking and shows it’s all about the use case and the risk appetite. If you have a lot less back reloads daily, compared to a full load, the accepted risk of one day might be acceptable, if you get great insights from the LLM, or something you’d need to do manually and then the alternative would be you either don’t do it at all, or very late when the insight is “less” valuable.


Side note, the engineering implementation of incremental loads might be much higher than a full load, as you need to add clear state management, checking what has run, and manage that state yourself, versus just running all. But this point almost certainly comes up in any case, whether you use AI or not, so we can factor out that fact in this scenario.


## How to Prevent Vulnerabilities, and Work Securely with AI Agents?


Another hot topic with agents is security concerns around vulnerabilities. I asked Chris how he sees that domain in combination with generative AI, and also if we need “Okta for Agents”, as Maxime Beauchemin [called](https://www.linkedin.com/posts/maximebeauchemin_i-finally-got-to-around-to-test-driving-clawdbot-activity-7423272818848550912-FSCn?utm_source=share&utm_medium=member_desktop&rcm=ACoAABkA2pgBYM4xDO0z2ChYuxFhBfu4h7jp4Lo) it.


His view splits cleanly in two:


> On the one hand, it’s a nightmare to manage these agents in the enterprise. On the other hand, they’re phenomenal at detecting compliance violations: leaked credentials, leaked PII, and so on.


He’d been thinking about an Okta-for-agents independently:


> It’s funny you mention Maxime’s “Okta for agents” comment. I didn’t see it, but I’ve been saying the exact same thing. It seems patently obvious to me. What’s unclear is whether Okta is Okta for agents, or whether another company (or companies) will take its place. Innovator’s dilemma and all. Okta’s certainly give it a good try–their homepage is covered in it now.


### Skills, Marketplaces and MCPs


He continues and says that it’s the wild west right now. You can load skills and even arbitrary skills from a marketplace and load any kind of text files without knowing if there’s a vulnerability.


There are examples where hidden [code injection](https://x.com/ZackKorman/status/2018386838101086446) is done in a repo:


[

](https://www.ssp.sh/blog/how-to-use-ai-with-de-chris-riccomini/security-ingection.png)A hidden comment that is commented out below |  [source](https://x.com/ZackKorman/status/2018386838101086446)


Chris continues with not having enough guardrails:


> But yes, we absolutely **need lineage, auditability, RBAC, ABAC, and so on**. It’s the wild west right now (as far as I know, anyway). This is one of the reasons I was so outspoken about MCP when it first came out. I was very **disappointed in their (lack of) security model**. It’s the most important part, and it was completely lacking. It was rather shocking to me given Anthropic’s focus on the enterprise. More recently, they’ve added better support, though, so credit where credit is due.


## Future with AI Agents


When asked about the future of AI, especially when we talk about data engineering, we discussed three interesting topics on what agents are doing well today, the role of data engineering itself and what programming language to use.


### What Agents Already Do Well Today


I asked if we get self-healing data pipelines, so we do not need to get up at night, meaning AI does not only detect errors, but also analyses, debugs, pushes a commit to the repo and re-runs the pipeline autonomously?


> I’ll be frank: I think AI will do the majority of the data engineering work in the future. I think we’re already at a point where it can; the tooling and practices just haven’t yet adapted.


This is an interesting point regarding tooling (and practices) not being adapted yet. Jeff Dean, Chief Scientist at Google DeepMind, [made the point](https://www.youtube.com/watch?v=g8BuAtM3fp4) that Amdahl’s Law still applies, and that we need to re-engineer our tools as they were designed for human speed. If AI agents can run 50x faster, but the tools don’t, then we do not get an overall improvement.


On the other hand, what agents already do well today:


> Agents are already excellent at inspecting failed Github actions, failed workflows, running SQL queries, writing Python–all the things data engineers do. As they get plugged into monitoring systems and begin to auto-remediate, the grunt work of data engineering will get taken over by AI.


And building new pipelines, given the right access:


> Agents are also fully capable of adding new data pipelines, provided they have access to infrastructure to do so. If you stand up a fresh Airflow and add connections for all your systems, I’d wager an Agent can set up as many pipelines as you need on it. And if you define the security and compliance policies it should follow, it’ll do so.


Here, in my opinion, it is key that we use declarative and config-driven stacks, like Kubernetes and React are doing, and most modern tooling.


### Data Engineering Role Going Away, or Unified?


Continuing on the thread of the future of AI, Chris talks about how shifting left is a movement we had for a while, and where this leaves data engineers as a role:


> I’m not sure where that leaves data engineers. The “shift left” movement has been going on for a while. I can imagine a world in **which “data engineer” as a distinct role goes away**, or is folded back into a more generic data role that includes **data engineering, machine learning, data analysis, and so on**.


He’s been pushing this for [quite some time](https://materializedview.io/p/merge-analytics-and-data-engineers):


> We over-specialized the data space. It might have been necessary, but it isn’t now. So perhaps we’ll see “data” be a single role that encompasses not just data engineering, but analysis and machine learning/AI as well. I think that would be healthy.


### Should We Let the AI Agent Choose the Language?


We heard people saying (e.g. Wes McKinney) that they choose programming languages, in this case Go over Python, based on AI, not what the human prefers. He calls it [From Human Ergonomics to Agent Ergonomics](https://wesmckinney.com/blog/agent-ergonomics/). That Wes, the creator of Pandas and author of Python for Data Analysis (stay tuned, he will be the next guest for this interview series), chose Go is interesting, and is because its advantages in fast compile-test cycles and painless software distribution are key. Don’t worry, Python will not go away2.


Or Ladybird is [rewriting](https://ladybird.org/posts/adopting-rust/) part of the browser entirely from scratch in Rust with agents in two weeks. So Chris, do you think that choosing the programming language will depend on the ergonomics of the agents in the future (or now already)?


> In a word: yes. I have been pretty enthralled with the **software factory concept** lately. It’s how I do a lot of my development now. **In that world, I just don’t care about the language** my software is written in.


What he optimises for instead:


> I care more about the characteristics of the output: its **performance, stability, and cost to build** (i.e. tokens). Languages that lend themselves to faster, cheaper, more stable LLM output are going to win.


These are very interesting thoughts, and I did a project fully vibe coded in Go to experience the **cost-as-tokens** as well. The codebase kept being small (apart from the tests), and therefore I could go much further with the given tokens compared to other projects where I used the same Claude Plan Pro and ran out.


Go is a language I don’t usually program in. And it is quite astonishing how far you get, but I also noticed a limitation as Lines of Code and size of the project grew, especially when adding new features that would break working features.

Side note by Chris: No more proofs for a programming language required

I used to think that this would pull us in the direction of languages that have formal methods properties. Proofs, model checkers, and so on. I no longer think that’s the case, though. I think LLMs have gotten good enough at writing code that proofs are no longer required. We can use normal testing strategies. I wrote more about this in [The Waymo Rule for AI-Generated Code](https://rng.md/posts/the-waymo-rule-for-ai-generated-code/).


### Does AI Take away the Learnings?


Last question I asked Chris — the danger of not learning new things, and getting overwhelmed with constant stimulation, and even addicted? In a world where we only prompt, where we don’t experience hitting a wall and then figuring it out, does that prevent us from learning new things? Are we just cruising on auto-pilot?


Chris mentions that it depends on how we use it and brings an example:


> One could argue a calculator makes us learn less math; indeed, I keep an eye on that with my middle school-aged kids. But it’s also a tool that lets us do far more complex math without worrying about carrying the one or shifting the decimal, so to speak.


But you can also learn *with* AI he argues:


> I have had instances where I learn a ton from AI. A concrete example: [SlateDB](https://github.com/slatedb/slatedb)’s language bindings. I built them all from scratch (or rather, AI generated them all from scratch). When I started, I knew nothing about bindings. As I **worked with AI to steer it and iterate on the code, I learned** about cbindgen, UniFFI, foreign function interfaces (FFIs), and so on. It’s a phenomenal tool for picking up something from scratch. I can ask it questions, learn from it, and so on.


Again, did he actually learn as much (from scratch, with AI) as he would have building it himself?


> Almost certainly not, I think **I would have learned a lot more [without AI]. But I also wouldn’t have done the work**. Writing four bindings (Node, Java, Python, and Go) from scratch is just too much work. I don’t have the time for it. Especially since I have never written a line of Go, and I know next to nothing about the Node ecosystem. So in the real world, I think I came out ahead.*


#### Do We Learn Fewer Things?


Let’s finish with a question: Are we learning *fewer* or just *different* things? Something I’ve wrestled with for a while. Chris’s answer is:


> Perhaps the things we are no longer learning don’t really matter anymore. Going back to the calculator example, I couldn’t really tell you in detail how a calculator physically works. If you took it apart and showed me its circuitry, I’d be unable to tell you anything about it, really. Does that matter? I’m not so sure.


I think we all are in this experience together, and nobody can really predict the future. I experienced both sides: when I rely too much on the assistant, I get more lazy and do the *deep thinking* less. While I course-corrected, and only used it for dedicated tasks, I noticed that abilities were improving again, or better, my feel and gut feeling got better again, and I had more confidence in the task at hand. But also, as Chris said, if I know it’s going to be a hard task, I can do much more because I deliberately use AI for certain tasks to actually finish the task. So the future will tell.


## Next Interview


I hope you enjoyed this interview with Chris. Huge thanks to Chris for taking the time to speak with me and for sharing his experience with all of us. Follow him on [LinkedIn](https://www.linkedin.com/in/riccomini/), [X/Twitter](https://x.com/criccomini) or on [Bluesky](https://bsky.app/profile/chris.blue), read [his two amazing books](https://www.amazon.com/s?i=stripbooks&rh=p_27%3AChris%2BRiccomini&s=relevancerank&text=Chris+Riccomini). Follow his amazing newsletter, the new one at [Posts on engineering, venture capital, AI, and more. | rng.md](https://rng.md/), but also his old one [Materialized View](https://materializedview.io/) has a wealth of insights.


There are three more interviews already lined up with great guests, one of them is Wes McKinney as mentioned, so please share feedback, questions you might want to ask or just your experience on how to work with AI in the data space. We’re all in this together, figuring it all out. The more we can learn from each other, what’s important, and maybe also what’s not, the better.


So stay tuned for the next interview.


---


```
Full article published at MotherDuck.com - written as part of my services
```


---

1. Chris hints at some of his recent [Wiggum Loop](https://rng.md/posts/wiggum-loop/) post. ↩︎
2. From [https://wesmckinney.com/blog/agent-ergonomics/](https://wesmckinney.com/blog/agent-ergonomics/): Python will remain essential as an exploratory computing layer for humans and agents to collaborate on data analysis, research, and data visualization. Notebook layers (Jupyter, Marimo, and so forth) and hybrid IDEs (like Positron, where I’ve been contributing in the last couple of years) will increasingly focus on catering to the human-in-the-loop data scientist or ML engineer, even though the “Python part” may become thinner and thinner as the lower layers of the stack are re-engineered for performance and agentic engineering productivity. ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/how-to-use-ai-with-de-chris-riccomini/)
|
[Artifical Intelligence](https://www.ssp.sh/tags/artifical-intelligence/)
[Agentic](https://www.ssp.sh/tags/agentic/)
[Data Pipelines](https://www.ssp.sh/tags/data-pipelines/)
[Python](https://www.ssp.sh/tags/python/)
[Dataengineer](https://www.ssp.sh/tags/dataengineer/)
[Orchestration](https://www.ssp.sh/tags/orchestration/)
[ETL](https://www.ssp.sh/tags/etl/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Open-Source](https://www.ssp.sh/tags/open-source/)
[Motherduck](https://www.ssp.sh/tags/motherduck/)
[Services](https://www.ssp.sh/tags/services/)
