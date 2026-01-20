---
title: "Improving the Data Stack & Composable Systems"
summary: "Podcast at Real Python Podcast"
date: 2024-02-23T00:00:00
tags: ["podcast", "transcript"]
slug: real-python-podcast-improving-data-stack-composable-systems
word_count: 11058
source_file: transcripts/2024-02-23-real-python-podcast-improving-data-stack-composable-systems.md
content_type: transcript
event: "Real Python Podcast"
video_url: "https://realpython.com/podcasts/rpp/193/"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of the Real Python Podcast, host Christopher Bailey talks with Wes McKinney about Apache Arrow, composable data systems, the evolution of pandas, and Ibis. The conversation spans 16 years of data science tool development.

### From pandas to Arrow

Wes reflects on starting pandas in 2008 when Python barely had basic data tools. Early concerns were just "making Python a language where you could succeed at doing really basic data work." Now, higher-order concerns like interoperability, scalability, and performance are finally addressable. He handed off pandas leadership in 2013 to focus on entrepreneurship, trusting Jeff Reback and Philip Cloud to manage the community.

### The Modularity Revolution

At Cloudera, Wes was exposed to Hadoop's philosophy of decoupling storage and computation. This influenced his thinking about data systems: rather than vertically integrated monoliths, the future should have "fewer components, less code to maintain, more collaboration, more investment in shared systems." By 2015, multiple projects were hitting the same interoperability walls, leading to the collaborative creation of Apache Arrow.

### What Arrow Solves

Arrow eliminates data serialization and conversion overhead. A modern full-stack web application can send Arrow data from a backend to DuckDB in WebAssembly in the browser—zero conversion needed. Arrow was also designed for efficient single-system use: fast processing on CPUs and GPUs using columnar memory layouts from database research.

### pandas 2.0 and Arrow Integration

The extension array system in pandas now supports Arrow strings and other Arrow types, bringing nullability to integers and Booleans. Arrow strings provide much better memory use and faster processing than Python object-based strings. However, migrating pandas to be fully Arrow-native requires a "delicate and deliberative approach" to avoid backward compatibility issues.

### Ibis: dplyr for Python

Ibis provides a portable data frame API that generates SQL or other execution plans for 20+ backends—BigQuery, PostgreSQL, DuckDB, Snowflake, Spark, and more. "If you can do it in SQL, there should be a way to express the same thing in Ibis." The goal: turn SQL into "the assembly language of databases"—machine generated, but humans don't have to interact with it directly.

### Open Source Community Building

"The hard problems in open source projects are not necessarily technical problems, they're actually social problems." Wes emphasizes building long-term relationships and finding the right collaborators. He worked with Jacques Nadeau on Arrow for nine years. "That initial collaboration... has led to almost a decade long partnership."

### Ending the Language Wars

Rather than Python vs. R competition, Wes and Hadley Wickham recognized early that "we stand to gain more from working together and sharing ideas." Their first collaboration—the Feather format in 2016—demonstrated the potential of cross-language technology sharing. "The struggle is not R versus Python. It's open source versus closed source."

### Current Role at Posit

As a software architect at Posit (formerly RStudio), Wes provides product feedback, design work, and helps orient the company's Python strategy. He appreciates having bandwidth for open source while also getting exposure to enterprise data science problems—"the struggle is not R versus Python, it's open source versus closed source."

---

## Key Quotes

> "At that time, I was really concerned with just making Python a language where you could succeed at doing really basic data work." — Wes McKinney

> "It's natural for people to build vertically integrated systems because ultimately collaboration is hard. Organizing people to collaborate and cooperate on building shared solutions takes a lot of work and a lot of time." — Wes McKinney

> "Clearly the future should look like we have fewer components, we have a lot more data, but the data is being processed by a lot less code. So there's fewer components, less code to maintain, more collaboration, more investment in these shared systems." — Wes McKinney

> "Often, that's the hardest part of building the software projects—the social side. The technical problems by comparison are much easier. But getting people to get on the same page and be on the same wavelength and collaborate with each other is really hard." — Wes McKinney

> "The hard problems in open source projects are not necessarily technical problems—they're actually social problems—building relationships with people, especially long term relationships, trying to find the right people to collaborate with." — Wes McKinney

> "If you can do it in SQL, there should be a way to express the same thing in Ibis." — Wes McKinney

> "Honestly, SQL is not going anywhere. And I think the best thing that we can do is turn SQL into basically the assembly language of databases. A thing that is machine generated, but humans don't have to interact with." — Wes McKinney

> "We stand to gain more from working together and sharing ideas and if possible, sharing code and solutions to problems than competing with each other." — Wes McKinney

> "The struggle is not R versus Python. It's open source versus closed source." — Wes McKinney

## Transcript

**Christopher Bailey:** Welcome to the Real Python Podcast. This is episode 193. How do you avoid the bottlenecks of data processing systems? Is it possible to build tools that decouple storage and computation? This week on the show, creator of the pandas library, Wes McKinney is here to discuss Apache Arrow, composable data systems, and community collaboration.

Wes briefly describes the humble beginnings of the pandas project in 2008 and moving the project to open source in 2011. Since then, he's been thinking about improvements across the data processing ecosystem. Wes collaborated with members of the broader data science community to build the in-memory analytics infrastructure of Apache Arrow. Arrow avoids the bottlenecks of repeated data serialization and format conversion. He shares examples of Arrow's use across the spectrum in tools like Polars and DuckDB.

Wes advocates moving from vertically integrated tools toward composable data systems. We discuss his work on Ibis, a portable data frame API for data manipulation and exploration in Python. Ibis supports multiple backends by decoupling the API from the execution engine.

This episode is brought to you by Posit Connect. Posit is dedicated to open source data science tools, and Connect helps teams manage all their data science publishing. Learn more at pos.it/realPython.

All right, let's get started. The Real Python podcast is a weekly conversation about using Python in the real world. My name is Christopher Bailey, your host. Each week we feature interviews with experts in the community and discussions about the topics, articles, and courses found at realpython.com. After the podcast, join us and learn real world Python skills with a community of experts at realpython.com.

Hey, Wes, welcome to the show.

**Wes McKinney:** Thanks for having me.

**Christopher Bailey:** Yeah, I'm very excited to talk to you. There's just a variety of things I'd like to talk about. One of the major ones is going back to this theme that I see in a lot of the talks that you do about how when you created pandas back in 2008, that you kind of were dealing with the state of the industry at the time, the state of the hardware that people had at the time, and what data maybe looked like at the time.

Maybe we could talk about what were some of the limitations you were facing back then when you originally started the project and why it's led to you having to really think about what we're doing today and where things need to go?

**Wes McKinney:** Sure. Yeah, happy to talk all about that. It's been almost 16 years now. And so obviously a lot has changed, not only in the world of computer programming, data science—there was barely—we called it statistics and statistical computing and just data analysis back then.

But I think at that time, I was really concerned with just making Python a language where you could succeed at doing really basic data work. And so a lot of the themes of the recent decade have been around how do we make it interoperable, scalable, performant?

If you go back 16 years ago, well, those things like performance and scalability and interoperability—those were kind of pipe dreams at that point in time, just things that we might've dreamt about. But getting to the point where we could read CSV files and do basic stuff that you might do in Excel or that you could do in R in Python and with a reasonable API—that was already a lot of work.

So it's taken a long time to get to the point where we can start thinking about some of these higher order concerns. But yeah, it's been a very interesting process to not only build the software, but then build the open source communities around the software and basically scale the community around these projects.

It's been an incremental thing, but already the passion of my career. I've really enjoyed the work and it's given me a lot of satisfaction to have the opportunity to be involved in these projects and to do things that have impact in the open source world.

**Christopher Bailey:** Yeah. So you led the project until 2013 and then turned it over to the open source community. What was some of your thinking behind that or maybe what factored into your decision there?

**Wes McKinney:** Yeah, I've definitely spoken about my history with the pandas project and how I was working for a quant hedge fund, AQR, and I convinced them to let me open source it at the end of 2009. Then I started giving talks in the Python community and I dropped out of grad school to work on pandas in 2011 and I wrote my book, Python for Data Analysis.

Then in late 2012, I teamed up with my colleague from AQR Chang to found Datapad and we raised some venture capital and moved to San Francisco to build a startup. We intended to use pandas and the early Python data stack to build a visual analytics tool with Python programmability. It was a very fun project, but I realized that I wasn't going to have time to be a full-time open source maintainer on pandas.

At that time, Jeff Reback and Philip Cloud had really stepped up and started doing a lot of development work in the project. These were people that I'd met in person and felt like represented the values of the project—people that I trusted to manage the community. And they were really eager to do that work. So I felt really comfortable handing over the reins of the project to them.

It was pretty natural—a pretty natural transition. At some point, we did create a governance document for pandas and established me as the "benevolent dictator for life," similar to how Guido van Rossum was the benevolent dictator for life for Python up until recently.

But in practice, I rarely had to exercise the role of the BDFL, like breaking up impasses or disagreements in the project. I think as far as open source communities go, it's been a really healthy community and has grown—thousands of developers over the last 10 or 11 years, since I haven't really been actively involved over that period of time.

**Christopher Bailey:** Yeah, definitely. I think about it and it's just the tool that is always mentioned in data science as far as the Python side, and it has such momentum. As far as the team that's heading it currently looks at adding features, it's like this massive bus that's traveling down a one lane road. And if it's going to make any turns, it's going to take some effort.

So I wonder about that—adding features and modifying things. Has that been your experience as far as trying to make changes?

**Wes McKinney:** Yeah, from what I've observed from the outside, it's been hard to change things in pandas. Firstly, I think one of the reasons that pandas is both loved and reviled is that it takes responsibility for so many different things in one really large code base.

That has led to these massive monolithic releases where everything—including plotting and value formatting, formatting tables in the console, and all the stuff that pandas does—are part of this gigantic monolithic code base.

But there's also the internal API surface area of all the things you can do with pandas data frames. If I could self deprecate or criticize my decisions 12 or 14 years ago, I think that in some ways pandas data frames do too much.

Or there are some things that they do—like multi indexes and multi level row indexes—that's one example where you can do all these cool pivot table things and you can reshape these massive multidimensional data sets with data frames. Part of me feels like if you look at what Polars is doing, they said, no, we're not going to do row indexes at all. Row indexes make things too complicated. We want Polars to be simpler and focus on performance and scalability and not do all that row indexing craziness that pandas does.

Honestly, I feel like that might be the right—in retrospect, that's probably the right approach. It would have been the right approach to put all that pivot table reshaping stuff into a separate data structure that's concerned with making pivot tables and data presentation and things like that. It just wasn't obvious at the time, and so it's only with hindsight that you can really say that.

I think another thing I would have liked to have been able to do—that I think wasn't feasible early in the project—is that pandas should probably be broken up into six or eight or 10 sub packages that are each released independently.

So you could have some of the components of the project that can move with a higher velocity. For example, if you make a change to how values are formatted in the console or in the IPython or Jupyter notebook, that part of the project could be released a lot more frequently. Whereas code that affects the internals of the library and how data is managed and some of the algorithms and core computations—that would be a little bit more slow moving and would have maybe quarterly releases or release twice a year or something like that.

But it's worked for the project. It's over 15 years old and still growing like crazy and it's being used by tons of people. It isn't trying to be the fastest or the most scalable library out there, but it's become a Swiss army knife.

You don't use a Swiss army knife to cut down trees. But you can use a Swiss army knife to do a lot of different things. And pandas is a lot like that. The fact that it's become this kind of multi-tool that everybody can learn how to use and they can solve all kinds of different data problems with it—it can be a great unifier across data teams. Everybody knows how to use pandas.

And if you've got larger data sets or you need to do something more scalable, you can use Polars or you can use DuckDB or you can use your SQL data warehouse. That was kind of one of the motivations for creating Ibis—to bridge the world of data warehouses and SQL based systems and pandas.

It's only in the more recent years that that project has started to take off as data warehouses and SQL based systems have seen a renewed surge of adoption and kind of taking over the enterprise.

**Christopher Bailey:** I got like three or four points there. I was literally going to ask you about how would you have changed things if you were able to start the project now? And you addressed many of those thoughts already with what you just said.

I also want to address the idea of this multi-tool. And that's how Python is thought of in so many ways as a programming language—the goofy joke that people sometimes say is that Python's the second best programming language at everything. It may not be specialized into one or two different areas, but you can kind of use it for whatever you need to be able to do. And I definitely feel like pandas kind of is in the same ballpark. And Excel in the same way—it's this sort of tool where you can just go to it and people know it and get going with it.

But then I got really excited about you mentioning Ibis right away. You seem to have a passion for this idea of decoupling tools in some ways, and maybe that comes from the background of what you just said.

You mentioned—I think in this other talk—about removing lock-in. Do you want to talk a little bit about the idea of decoupling these tools and how that relates to Ibis? Is it Ibis or Ibis?

**Wes McKinney:** We say Ibis. There's also the hotel brand—I don't know whether it's Ibis styles or Ibis styles. You see those Ibis hotels around the world.

**Christopher Bailey:** Okay, yeah.

**Wes McKinney:** International hotel brand. Yeah, there's a lot to unpack there.

To go back to the late 2000s or early 2010s, I think the whole Hadoop ecosystem—the first wave of open source big data systems—was driven by this idea of decoupling storage and computation. The idea was that you would put all your data in a large distributed file system that's hosted on commodity hardware, and then you would build these computing engines that would execute jobs on the data in that distributed file system.

We had the Hadoop file system and the original Hadoop MapReduce and Hive, which executed SQL using Hadoop MapReduce, and a whole ecosystem of projects which were largely written in Java that ran on top of the Hadoop file system. These were all inspired by similar work that Google had done with their GFS distributed file system and Google MapReduce and the original MapReduce paper.

So you already had this idea of moving from the old school world of the 90s and the 2000s of the vertically integrated data warehouse—where you'd have the storage layer, the transactional layer, the query engine, the query optimizer, query planner, query front end as a vertically integrated system with SQL on one end and storage systems at the other.

The idea of starting to break these systems apart so that you can say, okay, let's let the storage be its own system and let's have multiple different computing engines. And you can use SQL to talk to these systems or you could write Java code or Python code or Ruby code to write jobs.

I was at Cloudera for a couple of years—they bought my company, Datapad, in 2014. So I got to work closely with many of the key people in the Hadoop ecosystem. I was exposed to these ideas of modularity and composability and disaggregating storage and computing.

I'd also been deeply affected by the fact that we had to build all of these systems and libraries ourselves for use in pandas. We were completely on our own. We had to build a whole query engine—the internals of pandas that does all of its computations. We had to build all of our own data interfaces to read data into Python, to read CSV files and read data out of SQL databases and do all of this stuff.

I was really attracted to the idea of being able to reuse software and code and systems between different projects. What I really wanted was—if you go back to my talks in the 2015 era—I was talking about wouldn't it be awesome to have a really high performance C or C++ data frame library that we could use in every programming language that could execute these analytics workloads that we had built ourselves in pandas, but could be done portably, used in all the programming languages.

It just didn't occur to me that a few years later, I would be talking about what we now call DuckDB or Data Fusion or—now there's a number of projects, Velox from Meta. So now we have these reusable execution engines.

That's what I really wanted back in 2015. I was like, I don't want to have to keep building this stuff myself. I want to work with other developers.

**Christopher Bailey:** Yeah, yeah.

**Wes McKinney:** I want to create these reusable software components so that we can focus on building one reusable piece of really high quality data processing software that can keep getting faster and faster, can take advantage of hardware acceleration, use GPUs, all that fun stuff.

I'd used GPUs in my PhD. I started a PhD in statistics and we were using in 2011 NVIDIA GPUs to accelerate Bayesian inference—basically Markov chain Monte Carlo workloads using GPUs. So I'd already seen the potential of using GPUs for accelerating statistical computing workloads.

It just made sense to me that clearly the future should look like we have fewer components, we have a lot more data, but the data is being processed by a lot less code. So there's fewer components, less code to maintain, more collaboration, more investment in these shared systems.

**Christopher Bailey:** It seems like there's a lot of repeatability there, what I mean by that is that everybody was creating—a lot of people at the early days in this field were creating tools that were not unlike pandas that did kind of everything because they felt like they had to be the one stop shop that had all the solutions.

It's kind of a bit of a wake up to this idea that no, we can specialize, we can have GPUs doing this part of it and this doing that part of it. So I kind of like that idea—again, the decoupling.

**Wes McKinney:** Yeah, I mean, I think it's natural for people to build vertically integrated systems because ultimately collaboration is hard. Organizing people to collaborate and cooperate on building shared solutions takes a lot of work and a lot of time.

If you're under a time constraint and you need to deliver a working solution—and this is especially true if you're a business. Imagine you're building a database or some other data processing company. You can't afford to spend an extra six months or an extra 18 months investing in some external joint venture or open source collaboration in order to ship your product.

You say, okay, in the interest of expediency and getting a product to market, solving a customer's problem, we have to build these things ourselves and get them in a customer's or user's hands as quickly as possible.

But what happened is that by the mid 2010s, we'd already been through multiple eras of that way of working. What we found was that many different open source projects were running into the same classes of interoperability, modularity, composability problems.

In order to basically level up and achieve the next plateau of performance and scalability, we were forced to stop and collaborate with each other to build open standards that would facilitate that collaboration.

The Apache Arrow project was one concrete thing that came out of that need to establish open source standards for computing engines. In order to build modular, reusable computing engines, we needed to have an interoperable data format that was language agnostic and could represent large tabular data sets for these SQL workloads or data frame operations.

**Christopher Bailey:** Yeah.

**Wes McKinney:** People asked at the time, they were like, well, why didn't we do this in the 1990s or the 1980s? Why are we doing this in 2015?

The ecosystem—the commercial ecosystem and the open source ecosystem—was able to move quickly and make progress and deliver solutions that were essential without needing to solve those problems. Or at least—again, in the hierarchy of needs, kind of what I was talking about earlier—early days of Python and data analysis in Python, the concerns that we were dealing with at that time were so mundane that these more higher order concerns of like, okay, how do we have a super fast interoperability format for plugging Python into all of these other data systems and computing engines—that was just so far down the road that we couldn't even begin to think about it, because it would be like solving a problem that doesn't even exist yet.

What I've seen is that often these problems—people arrive at these problems independently. It was fortunate that I was in a position where I had a lot of social connections, work connections with many open source developers who all knew each other.

We were able to bootstrap some of these open source collaborations very efficiently. All the right people who worked for major tech companies were able to get together, have high bandwidth conversations about what problems we were seeing in our respective systems, and whether we thought that there was a basis for collaborating and building something together.

There was enough history—track record of working together, goodwill, history of good collaboration, communication—that we were able to solve the hard social problem of getting new open source collaborations going.

Because often, that's the hardest part of building the software projects—the social side. The technical problems by comparison are much easier. But getting people to get on the same page and be on the same wavelength and collaborate with each other is really hard.

Bootstrapping that initial collaboration with somebody you've never worked with before is taking a great leap of faith that you're going to be able to sustain a collaboration for a period of many years.

I'm going on working with Jacques Nadeau on Arrow and other open source initiatives. I didn't know Jacques very well when we started working on Arrow together, but I had a good feeling and he had worked with other people in the community. So there was a good degree of social validation that Jacques was somebody that I could trust.

I got a good feeling initially working together. And nine years later, that was a good bet. We've been able to build a lot of really important stuff together.

**Christopher Bailey:** Taking that back a little bit, I'm fascinated with Apache Arrow. I think that project is really interesting and I feel like a lot of people are maybe a little confused with what it is and how it kind of fits into this world of databases and this way of working with stuff.

I've tried to describe it myself—this idea that it's an in memory format for your data. In a lot of ways, it's trying to get past some of the bottlenecks of having to push something into a database and pull it back out and all that conversion overhead that ends up just really spinning cycles and so forth.

In some ways, if we could just keep this representation of data in memory, it could just save so much effort. I don't know if I'm explaining that well or not.

**Wes McKinney:** Yeah. Arrow solves a number of problems, but yeah, one of the big ones is avoiding data serialization and data conversion.

Nowadays you can build a full stack web application with advanced low latency analytics, querying, filtering, aggregation using DuckDB compiled to WebAssembly in the browser, combined with processing on the backend—which could be anything that speaks Arrow. It could be something written in R and Python and C++. It could be a database engine that has Arrow compatibility.

Now you can take an Arrow dataset from the backend of your full stack web application, send it to the browser in Arrow format—no need to convert to some intermediate representation to send over a web socket—and then immediately hand that blob of data off to DuckDB in WebAssembly to process because DuckDB speaks Arrow natively.

If you went back in time without Arrow, you would need to invent some intermediate data format at each of those stages. Say, well, how am I going to send data to the JavaScript layer of the web application? How would I expose the data from the JavaScript side to the DuckDB compiled to WebAssembly?

If DuckDB, your web application and your backend services all used different data formats or had no standard for talking to each other, if you needed to move a large dataset, that would start to become meaningful latency in your application. You could just spend hundreds of milliseconds or full seconds just doing conversions between these different components in your system.

When you use Arrow, all that conversion and latency killing interoperability overhead completely goes away.

We also—I mean, we designed Arrow to be efficient just used by itself within the context of a single system. So we knew we needed to have something where we could move massive amounts of data from component to component. But also there would be benefits to adopting Arrow within a system in that it's designed for fast processing.

You can use it efficiently on modern CPUs, on GPUs. We used our knowledge of—we learned from the database literature, a lot of the research that had been published in high-performance computing about the benefits of the columnar memory layout and how we could design the Arrow format to achieve a high-performance way of representing data.

That's been almost 10 years that we've been working on the project. People are pretty happy with its existence.

**Christopher Bailey:** That's great. It's pretty amazing. And you mentioned DuckDB. We also talked briefly about Polars in there and pandas 2.0 and lots of these platforms and data tools are now using Apache Arrow. Is that right?

**Wes McKinney:** Yeah, that's right. And so I guess we can just go start with those in order.

DuckDB—you can think of it as like SQLite for analytics. An embeddable engine, SQL database.

**Christopher Bailey:** Does it save as a single file the same way?

**Wes McKinney:** Yeah. They have an amalgamation, a single file DuckDB.cpp that you can embed in your application. So they designed it for portability, zero dependency. You can just drop it into your application and get a full high-performance database engine.

It's a columnar database system. It's built off of the ideas and the research around columnar database, columnar execution engines at CWI in the Netherlands, which has been a powerhouse of database research over the last 30 years.

They really wanted to solve this embeddable high-performance columnar database problem. We connected early on with DuckDB—maybe only two years into the project—and said, hey, we want DuckDB to work really well with Arrow.

My company, Ursa Computing at the time (which became Voltron Data), we became sponsors of the DuckDB Foundation and we established a working relationship with DuckDB Labs, which is the consulting company that the DuckDB developers established to support DuckDB.

We put real money behind building the Arrow integration into DuckDB so that Arrow would become a native interchange format in lots of different applications for DuckDB.

**Christopher Bailey:** Are there limitations to the sizes of what a DuckDB database can have?

**Wes McKinney:** DuckDB is really good for—if the data can fit on your hard disk, DuckDB can probably do whatever you want with it. It's really good at memory-constrained query execution—something that DataFrame users, pandas or Polars users probably experience the pain of running out of memory in some intermediate operation.

But you can tell DuckDB, I want you to use no more than eight gigabytes of RAM and it will respect your wishes. And you could be running on a 300 gigabyte data set that lives on your hard disk. So that's super cool.

We've also extended and made modifications to Arrow to bring the memory format of Arrow closer together with some of the extensions and ideas that have been built into DuckDB, developed in the database literature.

Polars—new DataFrame library for Python. It's written in Rust, led by Richie Vink. There's a new company for Polars now, and it's fully Arrow-based. It's written in Rust. It's a really cool project, very fast.

The API surface area of Polars is a lot smaller than pandas, which I think is a good thing in terms of focusing on performance and scalability and bringing a full lazy expression system to DataFrames.

**Christopher Bailey:** There was a third project in there that you mentioned, and I forgot about it already.

**Wes McKinney:** I was just talking about pandas going to 2.0 and adding Apache Arrow to it.

**Christopher Bailey:** Yeah.

**Wes McKinney:** So one of the focus areas in pandas development in recent years has been the extension array subsystem, which allows you to—so initially, pandas was based on NumPy arrays.

We built this whole complicated data management framework in the internals of DataFrames that would merge columns of the same type together. One of the motivations was that we wanted to make transposing operations and pseudo pivot tables and other linear algebra type operations in pandas a lot faster.

That introduced a lot of complexity, but we did it. We had reasons at the time.

**Christopher Bailey:** I was wondering if there were financial reasons—like that's your background of working in that world. And I think pivot tables and things like that could have been related.

**Wes McKinney:** Yeah, there were some specific workloads that we saw over and over in the financial analytics world that definitely influenced my thinking there.

After I left AQR to go to grad school, I continued to do some consulting work for them. So that did influence some directions in the project.

But the extension arrays allow you to have custom array types. So pandas has introduced arrow strings and other arrow types, which has brought new features like nullability to integers and Boolean data types, which has been a pain area for pandas users. And arrow strings provide a lot better memory use and a lot faster string processing because string arrays in pandas are pretty bloated. They use Python objects. There's a lot of overhead associated with large string arrays.

Using the arrow string representation makes the string arrays, string columns a lot more compact and a lot faster for processing. That was a big focus for the pandas 2.0 release.

Again, it's because it's hard to change things in pandas because we don't want to break people's legacy code—or at least not break it too often.

I think early on, I had the hope that we might be able to forge a path for pandas to become more arrow native more quickly. But the development team found that it was not going to be easy to migrate to using arrow backed pandas data frames without introducing too many subtle edge cases and backward compatibility issues.

It's required a more delicate and sort of deliberative approach to introduce the arrow based functionality into pandas. I think initially it's like an opt in. Now, I think there's some limited cases where if PyArrow is installed, you will get arrow data types out.

**Christopher Bailey:** Yeah, I think of what NumPy are doing with their version 2 and again, changing these core data types and having to kind of look forward and potentially breaking lots of people's code and having to be aware that, hey, you're not going to just be able to simply upgrade to NumPy 2. You're going to need to really look at your code and make sure that these specific types are going to be the same and work inside of it. So that is always a challenge.

**Wes McKinney:** Yeah. Another big chronic problem in pandas is the memory doubling issue—pandas really wants to own its own memory and copy the data that you give it.

Part of that is defensive copying, because for historical reasons, there were scenarios where you would create a pandas data frame and then modify that data frame and that would modify some other arrays that you used to create the series of the data frame.

So there's a lot of places where we introduced defensive copying so that the user would not mistakenly bork some other data that they had. But as a result, it's become pretty difficult to create a data frame that references some other memory that you have.

You can accidentally have 10 gigabytes of data in memory or five gigabytes of data in memory and you convert it into a pandas object. And so all of a sudden you have double the amount of data in memory because of memory copying.

One of the motivations with the extension array work is to make it easier to do zero copy construction of pandas data frames so you can avoid that memory doubling issue.

**Christopher Bailey:** I wonder about the Apache name that's attached to Arrow, and I don't know if there's some background there.

**Wes McKinney:** Yeah, I can speak to that. The Apache Software Foundation came about in the 1990s. I think it was one of the, if not the first open source foundations—501 C3 nonprofit organization that was created to provide legal protections and other infrastructure in support of open source projects in the 1990s.

If you go back and look at the conversations in the 90s, there was a lot of concern about attacks or legal actions from Oracle or from IBM or other companies who felt threatened by open source.

The project that led to the creation of the foundation was the Apache web server. The name actually was a pun. It came from the idea that it was "a patchy" web server—like it had a lot of bugs. So it required a bunch of software patches.

**Christopher Bailey:** Okay.

**Wes McKinney:** People had heard the Apache name and so there was a pun there. That was how the name of the web server came about. Because of the name of the web server, that was the name you initially used for the foundation.

Of course, over the last 30 years, culture has shifted. I think people have justifiable concerns about cultural appropriation and use of Native American language and imagery and associations in these projects.

Something that's brought up repeatedly has been also a concern in the Arrow project. Many cultures—almost all cultures in the world—have invented and used arrows. But putting Apache and Arrow together creates the unfortunate imagery of this kind of Native American connotation that, if it were up to us, we want the benefits that the foundation offers us.

For Arrow, we would like to not have the concern of the cultural appropriation. We would be in support of a name change for the foundation and for everyone to create an inclusive community where everyone feels welcome.

It does concern me that those with Native American heritage might feel that because of this, that the community is not as inclusive as it could be. But it is something that comes up on a frequent basis.

The big data community Apache Hadoop—because of the legal protections, infrastructure provided by the ASF and the fact that the ASF and the Apache Software Foundation has become a trusted brand for corporate contributors to open source—they know when they're contributing to an Apache project that they're getting not only the legal protections, the trademark and copyright handling, that the IP is all clean and is being looked after, but also that there's a governance model in place that is based on openness and transparency.

All communications—all project communications aside from certain private votes about who to give commit access to on projects, those are private—but aside from that, all of the governance of projects is fully open.

For a corporate contributor looking to get involved in open source, they don't want to come into some open source project that is controlled by some other company that's having private discussions. One of the mandates in an Apache project is that all communications have to be public.

That creates this kind of safe space where everyone is playing with their cards up on the table. We call it the Apache way and that model has produced these really healthy and thriving communities.

I don't have a huge horse in the race over the Apache name, but I want to create inclusive, healthy, open source communities and to bring everyone under a happy umbrella where we can collaborate and build great software together.

**Christopher Bailey:** Yeah. I feel like over these years, since you started all these different projects, I wonder if you feel like you've become more of an organizer, a manager. Are you doing as much coding as you would like to do?

**Wes McKinney:** While I was working on my recent company—Ursa Labs, which became Ursa Computing and then Voltron Data—as we built a 130 person company in three years, I didn't have too much time for coding during that time.

In my new role at Posit, I'm getting back to doing more development and working on some new open source initiatives. It's been ebb and flow as far as how much time I have for coding.

You're absolutely right that I have been kind of a community organizer. I recognized early that because the hard problems in open source projects are not necessarily technical problems—they're actually social problems—building relationships with people, especially long term relationships, trying to find the right people to collaborate with, spending a lot of time to make sure that you understand each other, that you're communicating well, that you're on the same wavelength in terms of what you're trying to accomplish.

I found that influencing other people and recruiting other people to a common shared understanding of what we're trying to build and getting on the same page—that pays great dividends.

Finding and recruiting people to work with me—I view that as arguably more important than the code that I produce. Obviously, I love writing code and doing development work. I've had periods where I've been enormously productive and churned out tons of code and tons of pull requests.

But the community development work—it yields a lot greater benefits over time, because if you find the right people to work with, they also recruit other people to work with them.

If you just look at the pandas project—Jeff Reback and Joris Van den Bossche and Phil Cloud and Mark Garcia—they've all been just amazing in terms of community development. I tip my hat to them. pandas wouldn't be anything like it is now without their contributions to building that community.

Community organization work, it's—yeah, I think in open source, it's everything. From the outside, often people think, oh, it's these lone wolf hackers in their attic writing code late at night and on weekends.

There is a lot of privilege attached with doing open source development, because many professional software engineers can't afford to do open source work on their nights and weekends because they have families or they have other jobs or they have other responsibilities or they're too tired.

I've had many days where I'm like, I work on GitHub issues, but I'm too tired today. And not everyone can get permission from their jobs or the space at work to be able to contribute to open source.

Naturally, there's diversity problems in open source. For a long time, it's been a really privileged activity to be in a place where you can do open source development.

**Christopher Bailey:** Yeah. And so I think about that a lot. In my time—I started the podcast almost exactly four years ago, right at the start of the pandemic—just trying to get people to come on the show to talk, the amount of bandwidth that these people had to be able to show up and do something like this, to talk about their projects, to talk about what they're doing and watching organizers of conferences kind of go through the same thing.

And what you're talking about with these different projects—you have to be in a really special spot to be able to contribute. And it's fantastic if you can. But trying to get more people involved is hard. What are the benefits that they're going to get out of it and how much can they invest into it? But I definitely appreciate everything that you've been working on and being a champion for.

Do you want to talk a little bit about Ibis a little deeper? Because we kind of touched on it off and on, and I'm very fascinated.

I mentioned lots of times on the show about being an R programmer for a little bit and what fascinated me about it and I loved about it was definitely the tidyverse stuff and dplyr. And so when I saw Ibis, I was like, oh, this looks really cool and has a lot of the same kind of stuff.

Just a note—I wonder about projects like this sometimes that I feel like have been a little bit under the radar. I feel like it's not something that I hear a lot about. I'm not traveling in a lot of data science circles lately. I try to get more guests involved, but I wonder about not only getting a project started like this, but also promoting it, which goes back to the whole open source thing.

But anyway, maybe we could talk about what it is and then we could talk about the project itself.

**Wes McKinney:** Sure. Yeah, so Ibis is a Python library. It provides an API for data frame operations like building lazy data frame expressions, table expressions, basically interacting with a wide spectrum of database engines and other data processing systems.

The idea of the project was to create a portable query layer similar to what dplyr and dbplyr in R has become, enabling you to write a data frame expression in R, a data frame expression with Ibis in Python. Then based on what execution engine you're using, it will generate the appropriate SQL query or translate it to the appropriate pandas or Polars function calls to execute that operation.

The project started in late 2014 when I was at Cloudera, and the idea was that I was looking to build Python interfaces to these big data systems and I didn't want to build these one off APIs for a single execution engine.

I wanted to have a common API that was data frame like or pandas like, but that had really robust support for SQL because I had written a lot of SQL early in my career. I'd seen the horrors of maintaining large thousand line or hundred line SQL queries.

I wanted to have the ability to write complex SQL a lot more easily—to have reusability and the features of a modern programming language like Python when I'm writing complex SQL queries. But I also wanted to have this bridge between the data frame world and the SQL and big data analytics world.

The project started late 2014, initially had support for Impala because I was working with the Impala SQL engine team at Cloudera. It was a bit of a sleeper project when we launched it.

Philip Cloud, who I had worked with for several years on pandas—one of the key pandas core team developers—was at Facebook in that era. He was also suffering from massive HiveQL and other SQL data warehouse stuff at Facebook.

He got interested in Ibis because it was solving similar problems that he was seeing—SQL maintainability, scalability problems at Facebook. He jumped in and added Postgres support. Somebody at some point contributed BigQuery support and ClickHouse support.

Then some folks at the Google Cloud team picked up Ibis and started using it to build some internal tools and data quality tools for BigQuery. For a period of several years, there were not a lot of users of Ibis and we continued to add features and refine its internals. It was this kind of project flying under the radar.

But then in 2017, 2018, we started using Ibis to build a pretty serious system at Two Sigma, where Philip and I then worked. That brought a bunch of new development energy into the project.

There was some development from—used to be called MapD, then OmniSci, now Heavy AI. That was a GPU database system. So they contributed some development. Google continued to contribute for a period of several years.

Then fast forward to 2021. We started Voltron Data and really started making big investments in making the whole data stack more modular and composable. It was clear that the query layer—how we interact with all these different systems and provide for modularity at the user interface level of writing queries and writing these analytical operations—we needed a solution for that.

We made an early commitment at Voltron Data to make a big investment in Ibis and to build a team around it. The project—if you look at its GitHub history—there's a big spike in 2021 where we hired Philip and he leads a growing team there, which has made an enormous investment in modernizing Ibis.

It now supports 20 different execution backends. It can do real time SQL processing with Flink and it can run against all the different data warehouses—Snowflake and BigQuery and Redshift—and it can generate Spark SQL. It's grown into a quite large project, but still, I think it's a little bit unknown in many areas of the Python community.

Philip and his team have been doing a lot of work on creating content, live streams on YouTube and blog posts. If you go to the ibis-project.org website, there's a lot of really cool blog posts where you can see the things that they've been building more recently.

Actually, the emergence of DuckDB—DuckDB becoming this amazing, ubiquitous data processing tool—has made Ibis a lot more useful. Now you've got a high performance database engine that historically would have been squirreled away inside a cloud data warehouse or a commercial database that you can pip install and use on your laptop to work with massive data sets.

Ibis gives you a really powerful Python API for generating complex DuckDB queries and really nice integration with DuckDB. That gives you a pretty powerful toolkit right at your fingertips.

**Christopher Bailey:** When you think about the workflow there—again, we were talking about pandas earlier with this idea of having to write read CSV and having to move data into this other data frame kind of working relationship.

This allows it to just be literally a much friendlier query type language going right against the database as opposed to it having to be brought into data frames and having these other representations of the data in memory. Am I thinking of that right?

**Wes McKinney:** Yeah. The way you can think about it is that we designed Ibis for a high degree of SQL compatibility. The idea was that if you can do it in SQL, there should be a way to express the same thing in Ibis.

We wanted there to be no loss of functionality going from SQL to doing the same work in Ibis. But because we built Ibis in Python, we could build in a layer of type checking and validation and code reuse.

If you think about the stuff that people are currently doing with DBT, for example, where they're writing SQL queries and then inserting Jinja templates into their SQL queries to generate these complex SQL strings. You can actually do the same stuff in Ibis, but you are writing all Python functions and building things using modern Python programming techniques.

You get type validation and type checking all throughout the process. If you ever make an error, you get a nice error message right away telling you exactly what you did wrong and why the expression doesn't work.

Rather than—I'm sure people have been frustrated working with some large SQL string where you make a mistake and there's some parse error in the SQL string or some type error.

We wanted to create a lot more productive and more pleasant experience for doing industrial SQL. Things that are a lot more complicated than SELECT star.

**Christopher Bailey:** Nice. Yeah. And it has a similar sort of—I don't want to call it piping—but it has the idea of the dot notation to be able to chain multiple things together, which reminds me of working in R and the tidyverse kind of stuff.

**Wes McKinney:** That's right. Yeah, you can think of it as being like dplyr for Python. It has a much larger scope and aspires to be a lot more SQL compatible than dplyr. That's a design difference.

But yeah, Ibis and Polars have converged on a pretty similar way of working in that it's expression based. Everything is lazy. You build these expressions and then you have the control over when it's executed.

Honestly, SQL is not going anywhere. And I think the best thing that we can do is turn SQL into basically the assembly language of databases. A thing that is machine generated, but humans don't have to interact with.

**Christopher Bailey:** Very much.

**Wes McKinney:** One of the things that I thought was interesting in that same talk you were talking about was the ending the language wars. I feel like that's such a common thing that happens. People get involved in these flame wars over what we should be using. I wonder who are the casualties of these wars when you think about it?

**Christopher Bailey:** Yeah, I feel like the language wars, for example, between Python and R have led to a lot of bad feelings and grumpiness and—hostility would be a strong word—but generally just unfriendliness between developers in these communities.

I think Hadley Wickham and I recognized early on that the language wars were kind of stupid. We're all solving the same problems. Yes, we've made different technology decisions in how we solve these problems. But we stand to gain more from working together and sharing ideas and if possible, sharing code and solutions to problems than competing with each other.

When I was just helping start Arrow, I got together with Hadley and said, what can we do with this to make the language wars get better? And so we created the Feather format. It was a quick two week project to create a file format based on Arrow.

That was hugely useful to show the benefits of sharing technology between the R and Python community. That initial collaboration in 2016 has led to almost a decade long partnership between me and RStudio, now Posit.

They helped me create Ursa Labs and put huge amounts of funding into Arrow development. They helped me incubate Ursa Computing. They're a shareholder in Voltron Data.

If I'd adopted the language war posture of, I'm not going to work with anybody in the R community, then that whole collaboration would never have happened. Who knows where I'd be now.

But I'm glad that I embraced building bridges and not walls and working for the benefit of building the shared data science runtime and these reusable components that can be the rising tide that lifts all boats.

**Christopher Bailey:** Yeah. Do you want to talk a little bit about your role at Posit and the kinds of things that you're working on there?

**Wes McKinney:** Posit is around a 300 person company that was formerly known as RStudio and was founded in 2009. Initially they built the RStudio IDE and over the course of many years the company has grown.

They've built a whole enterprise product suite that supports open source data science teams. Initially R focused to start, but since have evolved to be a polyglot, language agnostic computing data science company.

They rebranded the company to reflect their growing into a polyglot computing company, have been adding support for Python-based teams to their enterprise products, been making some investments in open source Python development—for example, porting the Shiny framework for R to Python for building reactive and scalable web applications.

They've funded Arrow development, which has helped with modularity interoperability between the R and Python ecosystem, built the reticulate package, which helps with building hybrid R Python applications.

So I'm doing a few things there. I'm a software architect, so I'm providing product feedback, design and development work across numerous products in Posit's umbrella, helping with the roadmap and feature set and helping boost the Python support and orient the company's Python strategy to benefit data science teams.

They've also afforded me a lot of bandwidth to work on, continue to work on open source projects, which I greatly appreciate.

I think Posit has one of the largest fully open source software development teams. They have a large team there that does nothing but build open source. I'm able—one of the reasons why I wanted to rejoin Posit—to have that platform to be able to dedicate a large fraction of my time to open source development, but also to have the exposure to the enterprise data science problem so that I could see what's going on inside large companies, large data science teams.

To understand what we need to build on the open source side to really empower data scientists to be more successful in the enterprise, because really the struggle is not R versus Python. It's open source versus closed source.

The vision that I share with JJ Allaire, the founder of Posit, and folks like Hadley Wickham and Joe Cheng is that we really want the world to be built on open source software and open standards.

I believe that Posit is a place where I can do my best work. I'm excited to spend the next, potentially the rest of my career there. It's a place that I believe can be a hundred year company and aspires to be a hundred year company, and a place where I have resources and really smart people to work with.

My work in building open source is aligned with the mission and values of the company. I'm very excited for this next leg of my career. I will try to be as useful as I can and continue to build open source and help the open source data science mission succeed.

**Christopher Bailey:** Yeah, that's awesome. Wes, I have these questions I like to ask everybody who comes on the show. The first one is, what's something that you're excited about that's happening in the world of Python?

**Wes McKinney:** I'm pretty excited about the Rustification of Python. I think there's two really cool companies that are building tools for making Python development better.

Astral, which builds the Ruff linter, and Prefix.dev, which is started by Wolf Vollprecht, who created Mamba, a faster conda. They're all working in Rust.

Combining the ideas that have percolated the Rust community and bringing that kind of ethos and developer productivity mindset to Python, I think, can only lead to good things.

I recently configured Ruff and LSP and all the fun things in my Emacs environment. So now I have all these fancy new development aids that I didn't have in the past. And I already feel more productive.

I think obviously that plus the use of generative AI, Copilot and things in the development workflow—I think we're headed to really good places as far as developer productivity and a more pleasant and productive day to day working environment.

**Christopher Bailey:** I had a listener send in a question. He was wondering, is it hype that Rust is so popular? What's going on with it? We spent a discussion section of the last show on that. All I can say is that the people that I speak to on the show that are developers out there working in the community, they're excited about it. I don't know if you would call it hype. It's definitely one of these things that it's a tool and you don't necessarily need to learn it to get everything you want out of it. There's lots of benefits of people using it. And it's just a modern language in so many ways. So I don't know how you feel about that.

**Wes McKinney:** Yeah, I think there is a learning curve to developing in Rust. But once you climb that initial learning curve, what I've seen is that development teams and developers are happier and more productive.

My former co-founder, Chang She, has a new company, Lance DB, building a file format for vector databases and a software as a service vector database solution. They started out building Lance in C++. Over the holidays, they said, well, what if we do this in Rust?

They found that they really loved Rust and all of the friction that you experience with C++ development environments around packaging and tool chain and compilation—a lot of that friction goes away.

To have a modern systems language with a really nice development environment, tool chain and tooling like the LSP, the feedback that you get in development, the IDE support in Rust is really good.

Ultimately, I think it's about building good system software and having productive development teams. And Rust has done a really good job of that. So I think the hype is justified.

I've only written a smidgen of Rust code, so I don't feel like I've used Rust enough to really render a judgment. But just seeing other people around me and how happy they are to be developing in Rust, I think it's more than just hype.

**Christopher Bailey:** Yeah, I think that's an immeasurable thing that you can't ignore—happiness of your developers.

So what's something that you want to learn next? This doesn't have to be about programming.

**Wes McKinney:** I've always been a lifelong foreign language learner. Lately, I've been learning French and Italian.

**Christopher Bailey:** Okay. Are you using any specific tools for that?

**Wes McKinney:** I find tutors on italki. Maybe some listeners have heard of italki. It's like a language tutor marketplace. I've had a good experience with that studying. Since I've been studying languages since I was a teenager, being able to have a Skype call or a Google Meet call with a foreign language tutor, I've found a good way to learn. It does require you to do your homework and consume media and read and get exposed to the language you're trying to learn. But that's fun.

**Christopher Bailey:** There's a commitment there that if there's a person waiting for you to show up.

**Wes McKinney:** Exactly.

**Christopher Bailey:** I always think about that with guitar lessons and piano lessons or things like that. They'll know right away if you've practiced.

**Wes McKinney:** Yeah. And I'm learning—outside of programming things, I'm interested in learning Rust and learning TypeScript, finally. And I'm tinkering with DuckDB Wasm.

**Christopher Bailey:** Okay.

**Wes McKinney:** Which is kind of the WebAssembly version of DuckDB. And so that's hence the TypeScript. Yeah, I'm having a good time doing that.

**Christopher Bailey:** How can people follow the work that you do online?

**Wes McKinney:** You can follow me on—I have my website, wesmckinney.com. And I still post things occasionally on the website formerly known as Twitter. Can't say I approve of Twitter's new management, but it's sad that Twitter is not what it once was, but I don't know what is going to replace it. And so I hope that something does replace it and there is again a public forum where we can share things and stay in touch with each other.

LinkedIn is also great. I think a lot of people have stopped using Twitter and have been using LinkedIn a lot more. So I do try to post things on LinkedIn as well.

So feel free to reach me on those platforms. Outside of that, I do podcasts and I'm going to be speaking at more conferences as part of my role at Posit. Look forward to seeing people in person.

**Christopher Bailey:** I learned that you are a fan of video games. And so I thought I'd just throw this one in there. What video game are you currently playing?

**Wes McKinney:** I would say I'm in between games. I'm about halfway through playing Alan Wake 2, which is great, but it can only be consumed in small doses because it's hard to play right before going to bed.

**Christopher Bailey:** Yeah. It's a little intense.

**Wes McKinney:** I love retro video games. I often like to revisit classic games. I really enjoyed replaying the remaster of Metroid Prime, which came out when I was 17. To replay it at 38 on my Switch, all that has been super fun.

So I don't have as much time for video games as I used to, but for me, it's a way of unwinding and it's a stress relieving kind of thing.

**Christopher Bailey:** Takes your brain to a different place, which is always kind of good.

**Wes McKinney:** Yeah. Except for playing intense games before bedtime.

**Christopher Bailey:** Cool. Well, Wes, thanks so much for coming on the show. It's been fantastic to talk to you.

**Wes McKinney:** Yeah. Thanks for having me.

**Christopher Bailey:** And thanks again to Posit. Posit Connect helps make deployment the easiest step in your analytics workflows. Learn more about Posit Connect and try it for free for three months at pos.it/realPython.

I want to thank Wes McKinney for coming on the show this week. And I want to thank you for listening to The Real Python Podcast.

Make sure that you click that follow button in your podcast player. And if you see a subscribe button somewhere, remember that The Real Python Podcast is free. If you like the show, please leave us a review.

You can find show notes with links to all the topics we spoke about inside your podcast player or at realpython.com/podcast. And while you're there, you can leave us a question or a topic idea.

I've been your host, Christopher Bailey. I look forward to talking to you soon.