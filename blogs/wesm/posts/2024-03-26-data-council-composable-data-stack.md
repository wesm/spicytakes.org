---
title: "The Future Roadmap for the Composable Data Stack"
summary: "Talk at Data Council Austin 2024"
date: 2024-03-26T00:00:00
tags: ["talk", "transcript"]
slug: data-council-composable-data-stack
word_count: 6402
source_file: transcripts/2024-03-26-data-council-composable-data-stack.md
content_type: transcript
event: "Data Council Austin 2024"
video_url: "https://www.youtube.com/watch?v=9rOefO341sI"
---

{{< video https://www.youtube.com/watch?v=9rOefO341sI >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I give an overview of the composable data systems movement—what it is, why it's happening now, and where I think things are headed. I lay out a vision for a multi-engine data stack where users can move between execution engines based on their data scale and requirements.

### Background and Current Work

I discuss my various roles and how they connect to the composable data vision:

- **Posit (formerly RStudio)**: I returned as Principal Architect to help them become a polyglot data science company. Posit is a 15-year-old, 300-person B Corporation with no plans to go public or be acquired. Their business model is making open source work in the enterprise through products like Workbench, Connect, and Package Manager.
- **Voltron Data**: I co-founded this company to work on GPU acceleration for large-scale analytics and to support Apache Arrow development.
- **Micro Venture Fund**: I launched a small fund to invest in companies building on composable open source technologies.
- **Posit and RStudio history**: Hadley Wickham and I started collaborating in 2016 on Arrow, leading to Ursa Labs in 2018. Our shared belief is that the R vs. Python "language wars" are counterproductive—we should focus on making humans more productive with data.

### What Are Composable Data Systems?

The core philosophy of composable data systems:

- **Open standards and protocols**: Building on shared interfaces rather than proprietary ones
- **Modularity and reuse**: Designing components that can be mixed and matched across systems
- **Resisting vertical integration**: Avoiding the "homespun" approach where every layer of the stack is bespoke

The tradeoffs are real: composability requires coordination, open source diplomacy, and negotiating shared governance with other developers. But the payoff is that each component becomes better, faster, and more interoperable over time. You end up with more future-proof solutions.

I reference the "Composable Data Management System Manifesto" paper I co-authored with folks at Meta for VLDB 2023. The key insight: by decomposing data management systems into reusable components, we can streamline development of new engines, reduce maintenance costs, and provide more consistent user experiences. Critically, modular systems can more easily adapt to leverage new hardware accelerators as they emerge.

### Why Is This Happening Now? A Historical Perspective

The evolution of big data technology explains why composability wasn't feasible earlier:

- **Mid-2000s (MapReduce Era)**: Google's MapReduce paper popularized disaggregated storage and compute. Hadoop cloned this as HDFS + MapReduce starting in 2006. This created monolithic, vertically integrated systems. Just getting these components to work productively was hard enough—modularization was pie-in-the-sky thinking.
- **2010s (Cloud Shift)**: Large vendors moved from selling proprietary software to delivering cloud services. This drove emergence of open standards like Parquet. Hardware improved dramatically: faster disks, faster networking. Moore's Law slowed for CPUs but continued for GPUs.
- **2020s (Composable Era)**: We're now re-architecting systems on interoperable standards for better performance across heterogeneous workloads (ETL, feature engineering, ML training, AI inference). New systems are built composable from the ground up, while existing systems are being retrofitted with modular components.

### The "Scalability at What Cost" Problem

I revisit a crucial 2015 paper from Microsoft Research called "Scalability at What Cost." The core insight:

- Big data systems showed impressive scalability in benchmarks, but few evaluated absolute performance
- The question: are these systems truly improving performance, or just parallelizing the overheads they introduce?
- The paper introduced the COST metric (Configuration that Outperforms a Single Thread) to measure overhead in distributed systems

One of the central goals of composable systems is building standards and protocols that eliminate these overheads.

### Key Technologies Enabling Composability

**Apache Arrow**: We started this project in the mid-2010s as a cross-language, fast in-memory format for computing and data interchange.
- Enables a "shared data science runtime"—libraries and computational systems usable interchangeably across programming languages
- Performance becomes language-agnostic: doesn't matter if you're using Python, R, or something else

**ADBC and Arrow Flight**: Solving the database connectivity problem.
- Exporting data from databases is like "drinking a thick milkshake through a straw that's too small"
- ADBC provides a standard Arrow-native API shim for database interaction
- Arrow Flight is an Arrow-native wire protocol that databases can adopt directly
- Together they enable dramatically better performance for data export/import

**Modular Execution Engines**: Reusable query engines that work with these new standards.
- **DuckDB**: Super-fast columnar analytical database that runs everywhere—phones, web browsers, anywhere with C++ or WASM
- **Apache DataFusion**: Rust-based modular query engine with optimizer and frontend, also usable as just an execution engine
- **Velox**: C++ engine created at Meta
- **GPU-accelerated engines**: What Voltron Data is building, initially targeting NVIDIA GPUs

**Substrait**: The missing link between frontends and backends.
- An intermediate representation for queries that's not SQL-based or coupled to any particular language frontend
- Language frontends (dataframe APIs, SQL) translate to Substrait plans
- Plans get optimized, then execution engines turn them into physical execution plans
- Decouples the frontend you prefer from the backend you need

### Retrofitting Existing Systems

Several projects are adding modular accelerators to existing query engines:

- **Prmo**: Retrofitting Presto (not Trino) with Velox
- **DataFusion Comet**: Apple donated this to the DataFusion project—accelerates Spark with DataFusion
- **Apache Gluten**: In the Apache Incubator, accelerates Spark with Velox

Eventually we'll have every combination of modular accelerators within existing query engine projects. This raises the fundamental question: why should users be locked into a single full-stack query engine when cost, performance, and latency vary so greatly across systems?

### The Multi-Engine Data Stack Vision

I reference Jordan Tigani's "Big Data is Dead" talk from the previous year's Data Council. My nuanced take:

- A terabyte is no longer big data for many use cases—DuckDB handles this fine
- But truly big data still exists for some organizations
- The challenge is gracefully transitioning from small-scale (laptop with DuckDB) to large-scale (distributed clusters) without pain and suffering

**The SQL Dialect Problem**: A major obstacle to portability.
- SQL is a "standard," but in practice dialects are non-portable
- Database vendors aren't incentivized to fix this—non-portability creates lock-in
- If you have a mountain of existing SQL queries and want to migrate to a different engine, you have to rewrite everything and deal with quirky edge cases (type coercion, etc.)
- Tools like SQLGlot help with transpiling between dialects, but it's still painful

**Microsoft's Magpie Research**: A glimpse of the future.
- Presented at CIDR 2021, approached the problem from the Azure data platform perspective
- Created a unified pandas-like dataframe API
- Compiler and optimizer in the middle, common Arrow-based data layer
- Intelligently delegates to different Azure backends based on workload characteristics (data size, statistics)
- Makes smart choices on behalf of users for performance and total cost of ownership

### Ibis: A Unified Python Interface

I started the Ibis project almost 10 years ago to try to make the multi-engine vision practical:

- Harmonizes the best features of modern SQL with Python's fluent dataframe APIs
- Deliberately departed from the pandas API to fix some of its shortcomings
- Makes complex analytical SQL queries easier to build using programming language features (functions, parameters—things SQL lacks)
- Now supports 20+ backends with a unified API

**The Dev-to-Prod Workflow**: This is the main use case we're targeting.
- Nobody wants to burn Snowflake credits while developing ETL workflows
- Ideal: develop locally on your laptop with DuckDB, then flip a switch to run in Snowflake or Spark
- Ibis enables this without rewriting queries

### GPU Acceleration and the Need for Multi-Engine

I share benchmarks from Voltron Data's GTC presentation the previous week:

- Compared Spark SQL on EMR vs. an 80-GPU on-prem cluster with InfiniBand and NVLink
- At 10TB+ scale, specialized GPU clusters deliver massive speedups
- But it doesn't make sense to run all workloads on expensive GPU hardware
- Large companies don't want their GPU clusters clogged with small-scale queries

This is exactly why the multi-engine data stack matters: use DuckDB or DataFusion for sub-terabyte workloads on your laptop, transition gracefully to Spark or GPU clusters only when you actually need that scale.

### The Future: Portable Language Frontends

As execution components standardize, innovation moves to creating more productive user experiences:

- **Malloy**: A new programming language for analytical queries from Google's ex-Looker team
- **PRQL (Pipeline Relational Query Language)**: Another effort to build a better SQL
- The pattern: as the backend becomes commoditized, the frontend becomes the differentiator

Almost 9 years after we started Arrow, it's becoming a de facto standard for building APIs and connecting systems. This should lead to better performance and interoperability going forward.

## Key Quotes

> "Hadley and I think that the language wars are stupid. All the enmity between the R and Python communities is counterproductive. We are in the business of creating tools to make humans more productive working with data."

> "We are building systems based on open standards and protocols. We're designing for modularity, reuse, interoperability with other systems that share those common interfaces and open standards and protocols. In particular, we're resisting this idea of vertical integration, where every layer of the stack in your system is bespoke and you build it yourself."

> "The hope is that over time, each of the component pieces that we use to build these systems becomes so much better, easier to use, faster, more interoperable, and that you end up creating a solution that is a lot more future-proof and delivers better results over time."

> "To what degree are these systems truly improving performance, as opposed to parallelizing the overheads that they introduce?"

> "If you need to export a lot of data out of a database, you're trying to drink a thick milkshake through a straw that's too small."

> "In many cases, a terabyte is no longer big data, and so for many people, big data is indeed dead. But there still is big data. Big data does exist. I believe that we should be able to gracefully transition from working at the single machine scale to a large, scalable data processing engine without as much pain and suffering."

> "Database vendors are not that incentivized to resolve this problem because if you have a mountain of existing SQL queries and you want to migrate them to use a different data processing engine, you have to rewrite all those queries and deal with all the quirky edge cases of type coercion, conversion, and whatnot."

> "Nobody wants to burn a ton of Snowflake credits while they're developing their ETL workflow. The ideal scenario would be to be able to develop, build your model, do all of your development locally on your laptop with DuckDB, and whenever you're ready to go into prod in Spark SQL or BigQuery or Snowflake, it's about as easy as flipping the switch."

> "It doesn't make sense to run all of your workloads on hardware like this. If it's a pain to work at small scale, but whenever you're working at very large-scale queries you have to work in a completely different way, that's very painful for the user."

## Transcript

So this talk is a little bit of an overview of what some work that's been going on in in the open source ecosystem over the last decade, my thoughts about it, and give you some ideas about where I think things are going. But firstly, I'll tell you a little bit about my background. Most people are familiar with pandas, but I've been working on lots of projects over the last 16 or 17 years. I'll tell you about my new role back at Posit and what I'm doing there, why I work for Posit, why you should pay more attention to Posit as a company. I'll give you an overview of where this whole concept of composable data systems came from, tell you about what's active and what I think is exciting right now, and where I think things are headed, or at least where I'm personally focusing my energy to help things move forward.

So as Sean mentioned, my full-time job is I'm an architect at Posit, formerly RStudio. I co-founded Voltron Data. Voltron Data just had a big week at GTC conference last week, and I'll talk a little bit about that. I just launched a venture fund, which I'll tell you about. Many of you probably have my book, Python for Data Analysis. It's in its third edition. It's now freely available on the internet. If you go to wesmckinney.com/book, you can read it for free. Also very helpful if you need to look something up. And I've been working on a bunch of open source projects. I'm also helping out Lance DB. My former co-founder Chong is here with some folks from Lance DB. Also very excited about what they're doing there.

So the last several years, until very recently, I was 100% focused on Voltron Data. The mission of that company is to unlock the potential of GPU acceleration in large-scale analytics workloads. We also have built a large team to support Apache Arrow development and offer partnership to companies that are building on the Arrow ecosystem. So we've created partnerships with Meta and Snowflake and other companies, raised a lot of money. So very exciting.

I just launched a micro venture fund. Micro refers to the size of the checks. I have some LPs, but I've been investing in data and data infrastructure companies for the last 5 years, and I wanted to be able to do more investing, in particular to invest with a thesis around how we can help accelerate growth in companies that are building on this new stack of composable open source technologies. I'm a speaker here, so I didn't have to pay a VC ticket for this conference. Maybe next year. But I am a part-time VC, not a full-time one. My goal is not to invest as a full-time job, but I do enjoy helping founders and being involved in startups.

So many of you maybe know Posit by its former name, RStudio, which is a 15-year-old company. It's now 300 people. It's a remote-first company. The headquarters is in Boston, but there are people all over the world. Its mission is building open source data science software for code-first developers. They've steered clear of building low-code tools for data science. Also very passionate about technical communication. JJ Allaire, who founded Posit, goes all the way back to ColdFusion. He created ColdFusion in the 1990s. Building tools to help with publishing websites and creating communication for the internet has been a passion for 30 years, and that continues at Posit. It is a certified B Corporation with no plans to go public or to be acquired. It's designing itself for long-term resiliency with the intent to be a 100-year company.

300 people is a lot of mouths to feed, so you might be wondering how Posit makes money with all this open source software. Their main business is making open source work in the enterprise. That comes in a few different products. Firstly, Posit Workbench, used to be known as RStudio Server. They added support for JupyterLab notebooks, VS Code, in addition to the RStudio IDE. That enables you to do development in a hosted environment. Connect allows you to publish Streamlit, Dash, Shiny, all kinds of data applications, publish your Jupyter notebooks, Quarto documents. Very helpful product if you need to get your work in the hands of the people you work with. There's also a package manager product. A lot of stuff going on there.

I've actually been involved with this company for a long time. I knew Hadley Wickham and the RStudio folks well before 2016, but we started working together more actively in 2016 when we started the Arrow project. In 2018, I formally partnered with them to create Ursa Labs to do full-time development on Apache Arrow. They helped me incubate Ursa Computing, which turned into Voltron Data. After several years of working on that, I decided to come back to Posit to help them with their journey to become a polyglot data science and computing company.

Going back to 2018, the way I described the reason why I wanted to work with Posit was that Hadley and I think that the language wars are stupid. All the enmity between the R and Python communities is counterproductive. We are in the business of creating tools to make humans more productive working with data. We share a passion for the long-term vision of empowering data scientists and creating a positive relationship with the open source user communities. So very excited to be involved with this company.

If you followed me back when I was doing Ursa Labs, we also had significant sponsorship from a number of other companies that were essential to making Apache Arrow and this whole composable data stack happen over the last six, seven, eight years.

All right, composable data systems. Last year at VLDB, I collaborated with fine folks at Meta to write this paper called "The Composable Data Management System Manifesto." It's a great paper. I'm going to help you in this talk by presenting some of the key ideas from the paper and why they matter. I do recommend that you check out this paper. I think it's really well written. The Meta folks did most of the writing, but it lays out a really compelling vision for where things are going.

So what is a composable data system? The way I think about this is we are building systems based on open standards and protocols. We're designing for modularity, reuse, interoperability with other systems that share those common interfaces and open standards and protocols. In particular, we're resisting this idea of vertical integration, where every layer of the stack in your system is bespoke and you build it yourself. It's this kind of homespun thing where you've built everything top to bottom.

It does create more work in some ways because you have to deal with coordination and open source diplomacy. You have to think about moving along these different pieces that you share governance and ownership with other developers and people who are working on different layers of the stack. But the hope is that over time, each of the component pieces that we use to build these systems becomes so much better, easier to use, faster, more interoperable, and that you end up creating a solution that is a lot more future-proof and delivers better results over time.

Up front, it's a little bit painful because you have to go through the painful growing pains of creating these new systems and making them all work together, as well as negotiating with all the open source developers that are involved in these projects.

The way it was put in the paper is that we envision, by decomposing data management systems into a more modular stack of reusable components, the development of new engines can be streamlined while reducing maintenance costs and ultimately providing a more consistent user experience. By clearly outlining APIs and encapsulating responsibilities, data management software could more easily be adapted, for example, to leverage novel devices and accelerators as the underlying hardware evolves.

That was one of the reasons why we founded Voltron Data. We observed that it's hard for people to take advantage of GPUs to accelerate their systems. We also saw that there are many new hardware companies creating new types of hardware. So we need to make a corresponding investment in the software layer to make it easier to take advantage of new developments in hardware, whether that's faster computing, faster networking, storage. Ideally, from the standpoint of view as a user, you just want to be able to write Python code, and then as the hardware improves, all your software gets faster and you don't have to think about the messy details like, "How do I take advantage of this bleeding-edge development in computing hardware?"

The hope is that by relying on a modular stack that reuses execution engines and language front ends, the data systems can provide a more consistent experience and semantics to users, from transactional to analytic systems, stream processing to machine learning workloads. This sounds very nice in principle.

One question people have had is, "Why is this happening now? Why is it happening in the 2020s? Why didn't this happen in the 2010s or even earlier?" It helps to go back and think about the generational eras of big data technology, going back to the original Google MapReduce paper in the mid-2000s. Hadoop was started essentially as a clone of Google MapReduce and HDFS (Google File System). The first release of Hadoop from Yahoo was in 2006.

The MapReduce paper popularized this idea of disaggregated storage and compute. You have a big distributed file system, all of your datasets live as files in that file system, and then you have a bunch of compute engines that can process those files. So you process files in these systems and write out back into that distributed file system.

What this created was a collection of monolithic, vertically integrated systems that were part of the Hadoop ecosystem. Just getting these components to the place where they were viable and you could use them productively was hard enough. In terms of a hierarchy of needs, thinking about how we could modularize components of those systems and reuse large pieces of software between those systems—that was pie-in-the-sky thinking back in the late 2000s, early 2010s.

But there was a big shift in the 2010s, where in particular, large software vendors shifted from selling proprietary, vertically integrated software components to delivery of services in a cloud environment. That also led to an emergence of open source standards, file formats like Parquet. There was major progress in computing, networking, and storage. Disk drives got a lot faster, networking got a lot faster. Moore's Law kind of ended for CPUs a little bit, but in GPUs, it's continued to go to the moon as Moore's Law has continued in more specialized processor chips.

Through that period, as open standards began to emerge, we started thinking about how we could create technologies that would help continue to better take advantage of the innovation in the hardware layer. That has led us in this current era to think about re-architecting all of our systems on interoperable standards that will enable us to get much better performance and efficiency across a heterogeneous application stack that's doing a mixture of raw data processing, ETL, feature engineering, machine learning training, and AI inference.

We've had this emergence of new standards for composability, which I'll talk about. We're seeing simultaneously an emergence of new systems which are built to be composable from the ground up, as well as retrofitting existing systems with new components which are created with this new composable mindset.

Back to the paper: we foresee that composability is soon to cause another major disruption to how data management systems are designed. We foresee that monolithic systems will become obsolete and give space to a new composable era for data management.

Personally, this isn't a new idea. I didn't come up with this idea. Back in 2015, I was at Cloudera and working with the Hadoop ecosystem at the time. I was trying to socialize these ideas with the data science community. This was my first talk at New York R Conference in 2015. This year, 2024, will be the 10th in a row that I speak at this conference. Back then, I was trying to cross-pollinate ideas—there wasn't a lot of cross-pollination between the data science world and the big data world. These were ideas from the big data world that we were trying to socialize in the data science community.

Around this time, from Microsoft, there were ex-researchers who wrote this paper called "Scalability at What Cost." The core idea of this paper is that we've made all of this progress in big data systems with impressive scalability, but few of the performance benchmarks evaluate their absolute performance. They just look at scalability without evaluating absolute performance. This paper poses the question: to what degree are these systems truly improving performance, as opposed to parallelizing the overheads that they introduce?

In this paper, they introduce a metric called COST (Configuration that Outperforms a Single Thread) to try to measure the amount of overhead that is introduced into a distributed system by enabling it to scale. One of the core problems that we've tried to address through these new composable systems is building standards and protocols that eliminate these overheads in distributed systems.

Over the last several years, we've focused work in several key areas. Firstly, in protocols—mainly Apache Arrow and things related to Apache Arrow. We have a new collection of modular engines which are helping accelerate systems, either through new systems based on those engines or existing systems that are being retrofitted. We're also seeing a lot of work in query optimization, language interfaces, and storage. There's a lot of other stuff that isn't in this picture—distributed computing, ETL, modeling, workflow and infrastructure orchestration—and I'm sure there are a lot of talks at this conference where you can learn more about those things.

One of my main pieces of involvement in this was helping create the Apache Arrow project. We realized in the mid-2010s that we needed to create a cross-language, fast memory format which could be used for fast in-memory computing as well as fast data interchange across disparate systems.

The way I described the problem to the data science community is that we can start imagining, "What if we had this shared data science runtime, a set of libraries and computational systems that we could use interchangeably across programming languages?" It didn't matter which language front end you're using, what programming language—the performance is the same. We can collaborate on this shared collection of algorithms and data processing tools to make all of the languages faster and more efficient at the same time.

In the database world, there was also gnashing of teeth around the problem of how inefficient it is to import and export data from databases. If you're using just a single database or data warehouse, you're doing fine. But if you need to export a lot of data out of a database, you're trying to drink a thick milkshake through a straw that's too small. If you've ever had that experience...

This was in 2017, right around the same time that we were starting Arrow. What we've done is create technologies to provide an open standard for Arrow-native APIs for interacting with databases, as well as an Arrow-native wire protocol to enable new databases to use a standard wire protocol out of the box rather than using a proprietary or system-specific wire protocol that has to be serialized when you're getting data out.

Our hope is that firstly, with existing systems, they can take advantage of the ADBC API shim to provide a standard for systems interacting with those databases. But at the same time, they can also build support for the new wire protocol directly into the database, so they have their legacy protocol as well as the new open standard protocol. That yields significantly better performance.

Around the same time—you might have recognized those fellows, Hannes Mühleisen and Mark Raasveldt—because they also created DuckDB right around the same time. It's maybe not a surprise that as we're building these new interoperable data formats and protocols, we also need reusable, modular execution engines that can be put everywhere, that work well with these new standards and data formats.

DuckDB is one very successful example of a project which is putting a super-fast columnar analytical database literally everywhere. You can run it on your phone, in a web browser, pretty much anywhere that can run C++ code or WASM.

If we think about the architecture of what new composable systems look like—this is a diagram from the paper—we have, on the bottom tier, a modular execution engine, a runtime which provides for distributed computing and coordination. That could be Spark, it could be Ray, or another distributed runtime that makes use of one of these modular engines like DuckDB or Velox. We have a query optimizer in the middle that is the mediator between the language front end, which may be SQL-based or non-SQL-based, and we create optimized query plans which are handed off into our distributed runtime.

There are now several modular execution engines written in different programming languages with different features and bells and whistles that cater to different types of users. Just yesterday, I was at the Apache DataFusion meetup. It's a Rust-based modular query engine. It has a query optimizer and a front end as well, but can also be used as just an execution engine.

In Rust, we have DuckDB and Velox. Velox is being created at Meta, written in C++. At Voltron Data, we've been creating an accelerator-native distributed execution engine in C++ that initially is targeting NVIDIA GPUs.

One of the things we've developed in this community to make connecting these engines to the language front end easier is to have an intermediate representation for queries that is not SQL-based or not coupled to a particular language front end. We call this project Substrait. The idea is that your language front end, whether that's a data frame API or SQL API, translates that into a Substrait plan. Then we can optimize that Substrait plan, and then the execution engine can take that plan and turn it into a physical execution plan that is sent off to the cluster to be executed.

I mentioned earlier that there have been efforts to retrofit existing popular query engines with these new modular accelerators. Three of them that you can get access to or look at or contribute to right now: one is Prmo, which is retrofitting Presto—I should clarify, not Trino—with Velox. There's DataFusion Comet, which has been donated into the DataFusion project from Apple, which is accelerating Spark with DataFusion. There's also Apache Gluten, part of the Apache Incubator, which is accelerating Spark with Velox.

I guess eventually we'll have DataFusion and Presto and probably every combination of modular accelerators within these existing large query engine projects. All of this begins to pose the question of, as a user, why should I be locked into using a particular full-stack query engine like Spark or Presto? The cost, performance, and latency of these different systems varies greatly.

We can do a lot with DuckDB, and for small problems, in a lot of cases, you should probably just use DuckDB. But when you have an actual big problem that's too big for DuckDB, you want to be able to transition gracefully to using that larger, scalable execution engine.

Now, of course, last year at Data Council, we had Jordan Tigani on the stage in a duck costume talking about how big data is dead. I will say that in many cases, a terabyte is no longer big data, and so for many people, big data is indeed dead. But there still is big data. Big data does exist. I believe that we should be able to gracefully transition from working at the single machine scale—could be a large single machine but the small scale—to a large, scalable data processing engine without as much pain and suffering.

This isn't that easy, though, in part because—I have a ChatGPT-assisted depiction of "gaslighting SQL"—it's advertised as just standard SQL, but because SQL dialects, while SQL is a standard, in practice SQL dialects are non-portable and they feature a wide spectrum of different features.

There's a tool like SQLGlot, which is amazing, which helps with transpiling and converting from one SQL dialect to another. But this does create a problem. In a sense, database vendors are not that incentivized to resolve this problem because if you have a mountain of existing SQL queries and you want to migrate them to use a different data processing engine, you have to rewrite all those queries and deal with all the quirky edge cases of type coercion, conversion, and whatnot.

Knowing which engine to use in every scenario is non-trivial and may not always be obvious. Different systems have orchestration and infrastructure requirements.

A few years ago, in CIDR 2021, folks at Microsoft approached this problem from the standpoint of the Azure data platform. They asked: could we create a unified API for interacting with all these different database engines that we have available in the Azure platform and intelligently choose which one to use based on the type of workload, how big the dataset is, what statistics we have about the data, to make a smart choice on behalf of the user to give them good performance and good total cost of ownership for the query?

They described a research project they did called Magpie, where they created a pandas-like data frame API. They have a compiler and optimizer in the middle, a common data layer based on Arrow that provides for a distributed data fabric to coordinate these different execution engines within the Azure platform. On the back end, they delegate to the different backends that are available in Azure.

I love this idea and would really like to help it become more mainstream, a reality for data engineers everywhere.

A project that I started about nine, almost 10 years ago, and that we've been putting a lot of resources into, is the Ibis project in Python. It's been an effort to harmonize the best features of modern SQL with Python's fluent data frame APIs. We also wanted in Ibis to fix shortcomings in the pandas API and make things that are hard to do with pandas a lot easier to do with Ibis. We made a deliberate choice to depart from the pandas API.

We wanted to make it easy to build complex, large analytical SQL queries by using the benefits of a modern programming language—functions, parameters, things that don't exist in SQL. Over the years, we've been really focused on portability and compatibility across a wide spectrum of engines. We now support over 20 backends to provide a unified API that could be the basis to building a multi-engine data stack.

Ibis code produces a pretty complex SQL query, and everything is based on pipeable sequences of methods that compose with each other to create complex expressions.

One of the workflows where we hear a lot of pain points about—people wanting to work in this ecosystem and create a composable data stack—is how to go from dev to prod. Nobody wants to burn a ton of Snowflake credits while they're developing their ETL workflow. The ideal scenario would be to be able to develop, build your model, do all of your development locally on your laptop with DuckDB, and whenever you're ready to go into prod in Spark SQL or BigQuery or Snowflake, it's about as easy as flipping the switch, saying, "Run this workflow but in Snowflake," and not have to rewrite all of your queries. That's one of the key things that we're trying to facilitate with this project.

One of the reasons why this is so important is because at truly large-scale workloads—these are benchmarks that were just published by Voltron Data last week at GTC—we showed that when you have a specialized cluster of GPUs, comparing Spark SQL and EMR with an 80-node, 80-GPU on-prem cluster with InfiniBand and NVLink and all the bells and whistles—if you have a truly large-scale workload at 10 terabytes and up and you're willing to make an investment in hardware or to rent to work at that scale, you can get some truly amazing performance with the hardware that's available today.

We want to facilitate taking advantage of hardware acceleration in really large-scale workloads. But it doesn't make sense to run all of your workloads on hardware like this. If it's a pain to work at small scale, but whenever you're working at very large-scale queries you have to work in a completely different way, that's very painful for the user. If you're a large company and you have a lot of workloads going into your GPU cluster, which you want to reserve only for your large-scale workloads, you don't want it clogged with a bunch of small-scale queries.

This multi-engine data stack is really important for the future of the ecosystem, and I see all these technologies building up to make that possible.

I really aspire to help us create the reality of a multi-engine data stack, to have execution engines available that are tailored for different data scales, so that when you're below a terabyte, you can use DuckDB, DataFusion, things that run on your laptop, and then at those larger scales you can transition to using Spark or more specialized tools at much larger scale a lot more gracefully, and with a lot more productivity for you as a user.

I'm pretty excited about these new portable language frontend projects. I didn't have time to talk about it in this talk, but the Malloy project at Google from the ex-Looker folks, I think is extremely exciting. It's a whole new programming language for analytical queries that I encourage you to check out. Another project—I think it's called Prql or pql (Pipeline Relational Query Language)—is another effort to build a better SQL.

I think, particularly as these execution components standardize, a lot of the work in data systems is going to be about creating more productive user experiences, making it easier to orchestrate systems, write queries, execute them portably across these different environments.

Now almost eight years into Arrow, almost 9 years since we started conceiving and putting together the project, it's great that Arrow is becoming the de facto standard for how we build APIs and how we connect systems together. I think that bodes well for even better performance and interoperability in the future.

With that, I'm sure you're all hungry and ready for lunch, but I think I have time for a few questions. I appreciate your attention. Thanks.