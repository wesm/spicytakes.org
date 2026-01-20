---
title: "pandas and Beyond with Wes McKinney"
summary: "Episode at Talk Python To Me"
date: 2024-05-15T00:00:00
tags: ["episode", "transcript"]
slug: talk-python-to-me-pandas-and-beyond
word_count: 7334
source_file: transcripts/2024-05-15-talk-python-to-me-pandas-and-beyond.md
content_type: transcript
event: "Talk Python To Me"
video_url: "https://talkpython.fm/episodes/show/462/pandas-and-beyond-with-wes-mckinney"
---

*This transcript was obtained from the official Talk Python To Me website. The summary below is AI-generated.*

## Summary

In this episode of Talk Python To Me, I join Michael Kennedy for a wide-ranging conversation about my journey from creating pandas to my current work at Posit, Apache Arrow, and the future of the Python data science ecosystem.

### Current Work at Posit

I've returned to work full-time at Posit (formerly RStudio) as a software architect to help with their Python strategy. Posit is a certified B Corporation dedicated to open source software for data science and technical communication. The company has built itself to be sustainable over the long term, with enterprise products generating revenue to support open source development.

### pandas Origins and Growth

pandas started as a personal data analysis toolkit I built at AQR in 2007-2008 because working with data felt much harder than it should be. The library became popular due to timing, developer relations (including my book), and a serendipitous open source community. I emphasize how important it is for project creators to make room for others to become owners of the project.

### Apache Arrow

Around 2015, I started thinking about building underlying computing technology that isn't specific to Python or pandas but is really fast and efficient. Arrow defines a standardized data representation that's language-independent, enabling reusable algorithms and zero-copy data sharing between systems. The goal is that future data frame libraries can be built on Arrow components in much less time.

### WebAssembly and the Browser

WebAssembly is opening up exciting possibilities, including running the entire scientific Python stack in the browser without a server. DuckDB compiled to WASM enables high-performance analytics entirely client-side, which is transformative for deployment and application architectures.

### Ibis and the Multi-Engine Future

Ibis provides a portable dataframe API that can compile to different backends like DuckDB, pandas, Polars, Spark SQL, or BigQuery. The goal is enabling "the multi-engine data stack" where you're not locked into one system. You can develop locally with DuckDB but scale to distributed systems when needed.

### SQLglot

SQLglot is a SQL query transpilation framework that understands the quirks of every database dialect and can correctly translate between them. Ibis now uses SQLglot as its underlying engine for generating SQL outputs.

---

## Key Quotes

> "It's really refreshing to work with people who are truly mission focused and want to bring open source data science tools to everyone, sustainably and for the long term." — Wes McKinney

> "I've spoken a lot about how important that is—for open source project creators to make room for others in steering and growing the project so they can become owners as well." — Wes McKinney

> "The mantra in pandas was: how do we make things one line of code? One line of code—it must be easy. Make this as terse, simple, and easy as possible so you can move on and focus on building the interesting parts of your application." — Wes McKinney

> "It turns out that, as is true with many open source software problems, the social problems are harder than the technical problems. If you can solve the people coordination and consensus problems, solving technical issues is much, much easier." — Wes McKinney

> "If you were building pandas now, you could build a pandas-like library based on Arrow components in much less time. It would be fast and efficient and interoperable with the whole ecosystem of other projects that use Arrow." — Wes McKinney

> "One reason I became passionate about building stuff for Python was about giving people superpowers. Peter Wang puts it as enabling people to build things with much less code and time." — Wes McKinney

> "I think one reason pandas has gotten so popular is that it's beneficial to the community to have fewer solutions. It's the Zen of Python—there should be one and preferably only one obvious way to do things." — Wes McKinney

> "There's still a lot to do. We've made a lot of progress in the last 15 plus years, but in some ways it feels like we're just getting started." — Wes McKinney

## Transcript

**Michael Kennedy:** This episode dives into some of the most important data science libraries from the Python space with one of its pioneers, Wes McKinney. He's the creator or co-creator of the pandas, Apache Arrow, and Ibis projects, as well as an entrepreneur in this space. This is Talk Python To Me, episode 462, recorded April 11th, 2024.

**Michael:** Hey, Wes. Welcome to Talk Python To Me.

**Wes McKinney:** Thanks for having me. You know, honestly, I feel like it's been a long time coming having you on the show. You've had such a big impact in the Python space, especially the data science side of that space.

**Wes:** Yeah, it's great to be here. I've had my head down a lot the last N years. I think a lot of my work has been more like data infrastructure and working at an even lower level than Python. So I haven't been as engaging directly with the Python community. But it's been great to get back more involved and catch up on all the things that people have been building. And being at Posit gives me the ability to have more exposure to what's going on and people using Python in the real world.

**Michael:** There's a ton of stuff going on at Posit that's super interesting. And you know, it's sometimes just really fun to build and work with people building things.

**Wes:** For sure.

**Michael:** Well, before we dive into pandas and all the things you've been working on after that, let's hear a quick bit about yourself for folks who don't know you.

**Wes:** Sure. My name is Wes McKinney. I grew up in Akron, Ohio, mostly. I got involved in Python development around 2007, 2008. I was working in quant finance at the time. I started building a personal data analysis toolkit that turned into the pandas project. I open sourced that in 2009, and started getting involved in the Python community.

I spent several years writing my book, Python for Data Analysis, and then working with the broader scientific Python and data science community to help enable Python to become a mainstream programming language for doing data analysis and data science.

In the meantime, I've become an entrepreneur. I've started some companies and have been working to innovate and improve the computing infrastructure that powers data science tools and libraries like pandas. That's led to some other projects like Apache Arrow and Ibis and some other things.

I've been working on a startup, Voltron Data, which is still very much going strong and has a big team. And I've had a long relationship with Posit, formerly RStudio. They were my home for doing Arrow development from 2018 to 2020. They helped me incubate the startup that became Voltron Data. So I've gone back to work full time there as a software architect to help them with their Python strategy.

**Michael:** I didn't realize the connection between Voltron and Posit, but I have had Joe Chung on the show before to talk about Shiny for Python. I've seen him demo some really interesting things about how it integrates with notebooks these days.

**Wes:** On Shiny or on Posit in general?

**Michael:** Yeah, whichever you feel like.

**Wes:** So Posit started out in 2009 as RStudio. It didn't start out intending to be a company. JJ Lair and Joe Chang built a new IDE for R because what was available wasn't great. So they made that into probably one of the best data science IDEs ever built.

It started becoming a company with customers and revenue around 2013. They've built a whole suite of tools to support enterprise data science teams to make open source data science work in the real world.

But the company itself is a certified B Corporation with no plans to go public or IPO. It is dedicated to the mission of open source software for data science and technical communication. It's basically building itself to be a hundred-year company with a revenue-generating enterprise product side and an open source side. The enterprise part generates revenue to support open source development.

The goal is to sustainably support the mission of open source data science hopefully for the rest of our lives. It's an amazing company and one of the most successful companies that dedicates a large fraction of its engineering time to open source software development.

**Michael:** Yes, it's definitely doing cool stuff. Incentives are aligned well, right? It's not private equity or IPO.

**Wes:** Many people know JJ Lair created ColdFusion, the original dynamic web development framework in the 1990s. He and his brother built a company to commercialize it. They built a successful software business that was acquired by Macromedia, which was eventually acquired by Adobe. But they did go public as a company.

Then JJ found himself in his late thirties, around 15 years ago, having been very successful as an entrepreneur with no need to make money and looking for a mission to spend the rest of his career on. He identified data science and statistical computing, particularly open source, as the mission he aligned with.

It's really refreshing to work with people who are truly mission focused and want to bring open source data science tools to everyone, sustainably and for the long term. The goal is to provide an amazing home for top-tier software developers to work on this software, spend their careers, build families, and create a happy and healthy culture.

**Michael:** That sounds excellent. Speaking of history, let's jump in. There's a possibility people listening don't know what pandas is. You would think it's pretty ubiquitous, and I certainly would say it is, especially in data science. But I got a bunch of listeners who say really surprising things. So maybe for that crew, we could introduce what pandas is to them.

**Wes:** Absolutely. It's a data manipulation and analysis toolkit for Python. It's a Python library that enables you to read data files—many different types of data files off of disk, off of remote storage, or read data out of a database or some other remote data storage system.

This is tabular data, structured data like with columns. You can think of it like a spreadsheet or some other tabular data set. It provides you with this DataFrame object, pandas.DataFrame, which is the main tabular data object.

It has a ton of methods for accessing, slicing, grabbing subsets of the data, applying functions that do filtering and subsetting and selection, as well as more analytical operations like things you might do with a database system or SQL. So joins and lookups, as well as analytical functions like summary statistics, grouping by some key and producing summary statistics.

It's basically a Swiss army knife for doing data manipulation, data cleaning, and supporting the data analysis workflow. But it doesn't actually include very much in terms of actual statistics or models. If you're doing something with LLMs or linear regression or machine learning, you have to use another library.

But pandas is the on-ramp for all of the data into your environment in Python. When people are building some application that touches data in Python, pandas is often the initial on-ramp for how data gets into Python, where you clean it up, regularize it, get it ready for analysis, and then feed the clean data into the downstream statistical library or data analysis library you're using.

**Michael:** That whole data wrangling side of things, right?

**Wes:** That's right. And in some history, Python had arrays like matrices and what we call tensors now—multidimensional arrays—going back all the way to 1995, which is pretty early history for Python.

What became NumPy in 2005-2006 started out as Numeric in 1995. It provided numerical computing, multidimensional arrays, matrices—the kind of stuff you might do in MATLAB. But it was mainly focused on numerical computing, not with the type of business data sets you find in database systems, which contain a lot of strings, dates, or non-numeric data.

My initial interest was that I found Python to be a really productive programming language. I really liked writing code in it. But then you had NumPy, which enabled you to work with large numeric arrays. Working with more tabular data—stuff you'd do in Excel or a database—wasn't very easy with NumPy or it wasn't really designed for that.

That's what led to building this higher-level library for tabular data sets: the pandas library, which was originally focused on building with a really close relationship with NumPy. pandas itself was like a thin layer on top of NumPy originally.

**Michael:** I find interesting about pandas is it's almost its own programming environment in the sense that traditional Python involves a lot of loops and attribute dereferencing, function calling. And a lot of what happens in pandas is more functional—more applied to us—it's almost like set operations, right?

**Wes:** Yeah, lots of vector operations. That was behavior inherited from NumPy. NumPy is very array-oriented, vector-oriented. Rather than write a for loop, you would write an array expression, which would operate on whole batches of data in a single function call, which is a lot faster because you can drop down into C code and get good performance.

pandas adopted the NumPy way of array expressions or vector operations. But it's true that's extended to non-numeric data operations in pandas. Like vectorized set lookups where you might say: I have this array of strings and I have this subset of strings. And I want to compute a Boolean array saying whether or not each string is contained in this set of strings.

In pandas, that's the `isin` function. So you would say like `column_a.isin(some_set)` and that produces a whole Boolean array that you can use for subsetting later on.

**Michael:** One of the challenges, maybe you could speak to this a little bit, is that some of these operations aren't super obvious that they exist or that they're discoverable, right? Like instead of just indexing into a column, you can index on an expression that might filter or project columns. How do you recommend people discover what they can do?

**Wes:** There are plenty of great books written about pandas. There's my book, Python for Data Analysis. I think Matt Harrison has written an excellent book, Effective pandas. The pandas documentation provides really detailed information about how different things work.

When I was writing Python for Data Analysis, my goal was to provide a primer or tutorial on how to solve data problems with pandas. I had to introduce some basics of how NumPy works so people could understand array-oriented computing, and basics of Python.

It builds incrementally—as you go through the book, the content gets more advanced. You learn and master an initial set of techniques, and then you can start learning more advanced techniques. It's definitely a pedagogical resource.

**Michael:** That's cool. I didn't realize your book was available just to read on the internet.

**Wes:** Yeah. In the third edition, I was able to negotiate with O'Reilly and add an amendment to my book contract from 2011 to let me release the book for free on my website. It's available at wesmckinney.com/book.

I find a lot of people really like the print book. I thought releasing the online book would affect sales, but no, people just really like having paper books. And it seems even in 2024, people prefer paper.

**Michael:** Even digital books are nice. You got them with you all the time. I think it's about taking notes. Where do I put my highlights and how do I remember it?

**Wes:** That's right. Yeah, stuff like that.

**Michael:** Let's talk about growth and speed of adoption. When you first started working on this and put it out, did you foresee a world where this was so popular and so important?

**Wes:** It was always the aspiration to make Python this mainstream language for statistical computing and data analysis. But I didn't think it would become this popular or that it would become one of the main tools that people use for working with data in a business setting. If that was what I needed to achieve to be satisfied, that would have been completely unreasonable.

I don't know if its popularity is deserved and undeserved. There are many other worthy efforts created over the years that have been really great work. The fact that pandas caught on is a combination of timing. There was a developer relations aspect—content was available. I wrote my book and that made it easier for people to learn. But we also had a serendipitous open source developer community that came together and allowed the project to grow really rapidly in the early 2010s.

I definitely spent a lot of work recruiting people to work on the project and encouraging others to work on it. Sometimes people create projects and it's hard for others to get involved. But I was very keen to bring on others, give them responsibility, and ultimately hand over the reins to others.

I've spoken a lot about how important that is—for open source project creators to make room for others in steering and growing the project so they can become owners as well.

**Michael:** It's tough to make space and bring on folks. Have you heard of the Djangonauts? It's basically like a bootcamp but for taking Django enthusiasts and turning them into actual core contributors. What's your onboarding story for people who want to participate?

**Wes:** I'm embarrassed to say I don't have a comprehensive view of all the different community outreach channels that the pandas project has done. One of the core team members, Mark Garcia, has done an amazing job organizing documentation sprints and other contributor-sourcing events—creating very friendly, accessible events where interested people can meet each other and assist in making their first pull request.

It could be something as simple as making a small improvement to pandas documentation. Given it's such a large project, the documentation is huge—either adding more examples, documenting things that aren't documented, or just making documentation better.

For new contributors, that's more accessible than working on internals or algorithms. Working on a significant performance improvement might be intimidating if you've never worked on the pandas codebase. It's a pretty large codebase because it's been worked on continuously for going on 20 years.

It takes a while to get to a place where you can be productive, and that can be discouraging for new contributors, especially those without open source experience.

**Michael:** That's one of the ironies of challenges with these big projects—they're so finely polished. So many people use them. Every edge case matters to somebody, right?

**Wes:** Yeah. I mean, I think definitely a big thing that helped is allowing people to get paid to work on pandas or contribute as part of their job description. Maybe part of their job is maintaining pandas.

Anaconda was one of the earliest companies who had engineers on staff—Brock Mendel, Tom Augsberger, Jeff Reback—who part of their job was maintaining and developing pandas. That was huge because prior to that, the project was purely based on volunteers. I was a volunteer and everyone was working as a passion project in their free time.

Travis Oliphant, one of the NumPy founders, and Peter Wang founded Anaconda. Travis spun out to create Quansight and has continued to sponsor development around pandas. That's enabled people like Mark to do community building events and for it to not be something totally uncompensated.

**Michael:** Yeah, that's a lot of stuff going on. And I think commercial interest is awesome, right? If there's a different level of problems you could take on—you have this entire week and someone, that's my job, as opposed to I've got two hours and can't take on huge projects.

**Wes:** Yeah. Many people don't know, but I haven't been involved day-to-day in pandas since 2013. That's getting on—a lot of years. I still talk to pandas contributors. We had a core developer meetup here in Nashville pre-COVID, I think in 2019. So I'm still in active contact with developers, but it's been a different team of people leading the project. It's taken on a life of its own, which is amazing.

**Michael:** That's exactly what you want as a project creator—to not be beholden to the project you created. If you look at a lot of the most intensive community development, a lot of it has happened since I moved on to other projects.

Now the project has thousands of contributors. To have thousands of different unique individuals contributing to an open source project is a big deal. I think it says on GitHub around 3,200 contributors, but that's maybe not the full story because sometimes people don't have their email address associated with their GitHub profile. The true number is probably closer to 4,000.

That's a testament to the core team and all the outreach they've done—making the project accessible and easy to contribute to. If people go try to make a pull request and there are many different ways you can fail. Either the project has technical issues with the build system or developer tooling. If you aren't working on it every day, you can't figure out how the tools work.

But there's also the level of accessibility of the core development team. If they aren't there to support you in getting involved, learning how it works, and creating documentation about how to contribute and what's expected, that can be a source of frustration where people leave the project.

Sometimes development teams are unfriendly or unhelpful. They make others feel annoyed or like they're wasting their time. Like "I don't want to look at your pull request and give feedback because I could do it more quickly myself." You see that at open source projects. But they've created a very welcoming environment. Yeah, the contribution numbers speak for themselves.

**Michael:** Definitely do. Maybe the last thing before we move on—the GitHub statistic here is the "used by 1.6 million projects." That's—I don't know if I've ever seen it that high. There's probably some higher, but not many.

**Wes:** Yeah. It's a lot of projects. I think it's interesting—many projects reach a point where they're an essential and assumed part of many people's toolkit. Like the first thing people write at the top of a file is `import pandas as pd` or `import numpy as np`.

I think one reason pandas has gotten so popular is that it's beneficial to the community to have fewer solutions. It's the Zen of Python—there should be one and preferably only one obvious way to do things.

If there were 10 different pandas-like projects, it creates skill portability problems. It's easier if everyone says pandas is the thing we use. You change jobs and can take all your pandas skills with you.

I think that's also one of the reasons Python has become so successful in the business world. You can teach somebody without much programming experience how to use Python and pandas and become productive doing basic work very quickly.

I remember back in the early 2010s there were articles about addressing the data science shortage. My belief was always that we should make it easier to be a data scientist—lower the bar for skills you have to master before you can do productive work.

The fact that there's just pandas and that's the one thing people have to learn has led to people being motivated to make this one thing better. You make improvements to pandas and they benefit millions of projects and people worldwide. It's a steady snowballing effect.

**Michael:** I think doing data science is getting easier. We've got a lot of interesting frameworks and tools.

**Wes:** Yeah. For Python, right? That makes it easier to share and run your code.

**Michael:** Yeah. Shiny for Python, Streamlit, you know, Dash—like these different interactive data application publishing frameworks. So you can go from a few lines of pandas code, loading data and doing analysis and visualization, to publishing as an interactive website without knowing web development frameworks or Node.js.

You can get up and running building a working interactive web application powered by Python pretty quickly. That's a game changer for shortening end-to-end development lifecycles.

**Michael:** What do you think about Jupyter Lite and these PyOdide and basically Jupyter in a browser type of things? Yeah. WebAssembly and all that?

**Wes:** Yeah. So definitely very excited about it. I've been following WebAssembly in general. Some people listening might know about WebAssembly, but basically it's portable machine code that can be compiled and executed within your browser in a sandbox environment. It protects against security issues and prevents the WebAssembly code from doing something malicious on your machine, which is very important.

Won't necessarily stop them from mining cryptocurrency while you have the browser tab open—that's a separate problem. But it's enabled us to run the whole scientific Python stack, including Jupyter, NumPy, and pandas totally in the browser without a client and server and needing to run a container in the cloud.

I think in terms of creating application deployment, being able to deploy an interactive data application like with Shiny without needing a server—that's actually pretty amazing. It simplifies deployment and opens up new application architectures, making things a lot easier. Setting up and running a server creates brittleness, has cost. If the browser is doubling as your server process, that's really cool.

You also have projects like DuckDB, which is a high performance, embeddable analytic SQL engine. With DuckDB compiled to WASM, you can get high performance database running in your browser. You can get low latency interactive queries and dashboards. WebAssembly has opened up this whole new world of possibilities and is transformative, I think.

For Python in particular, you mentioned Pyodide, which is kind of a whole package stack—a framework for building and packaging and managing dependencies. You could create a WebAssembly version of your application for deployment.

The Pyodide main creator went to Anaconda and created PyScript, which is another attempt to make it even easier to use Python to create web applications, interactive web applications.

There's so many cool things here. In the R community, they have WebR—similar to PyScript and Pyodide. There was just an article on Hacker News about figuring out how to trick LLVM into compiling legacy Fortran code to WebAssembly. Because when you're talking about the scientific computing stack, you need the linear algebra and all 40 years of Fortran code supporting scientific applications. You need all that to compile to and run in the browser. Pretty wild to think about, but very useful.

**Michael:** I didn't realize you could use DuckDB as a WebAssembly component. That's pretty cool.

**Wes:** Yeah. There's a company called evidence.dev—it's like a whole open source business intelligence application powered by DuckDB. If you have data that fits in the browser, you can have a whole interactive dashboard or business intelligence fully in the browser with no server needed. It's very, very cool.

I've been following DuckDB since the early days. My company, Voltron Data, became members of the DuckDB Foundation and actively build a relationship with DuckDB Labs to help accelerate progress because I think the impact is so immense. It's hard to predict what people are going to build with all this.

And that was all, going back 15 years to Python—one reason I became passionate about building stuff for Python was about giving people superpowers. Peter Wang puts it as enabling people to build things with much less code and time.

By making things much more accessible and easier to do, the mantra in pandas was: how do we make things one line of code? One line of code—it must be easy. Make this as terse, simple, and easy as possible so you can move on and focus on building the interesting parts of your application rather than struggling with how to read a CSV file or whatever data munging technique you need.

**Michael:** Maybe an interesting mental model for DuckDB is kind of an equivalent to SQLite, but more analytics database for folks in process and that kind of things, right? What do you think?

**Wes:** Yeah. So DuckDB is like SQLite. In fact, it can run the whole SQLite test suite, I believe. So it's a full database, but it's for analytic processing. It's optimized for analytic processing as compared with SQLite, which is not for data processing.

**Michael:** Cool. All right. Well, let's talk about some things you're working on beyond pandas. You talked about Apache Arrow earlier. What are you doing with Arrow and how's it fit in your world?

**Wes:** The backstory was that around the mid-2010s, around 2015, I started working at Cloudera, which was one of the pioneers in the big data ecosystem. I had spent several years—five, six years—working on pandas. I had gone through the experience of building pandas from top to bottom.

It was this full stack system that had its own mini query engine, all its own algorithms and data structures and stuff we had to build from scratch. I started thinking: what if it was possible to build some of the underlying computing technology—data readers, file readers, all the algorithms that power the core components of pandas like group operations, aggregations, filtering, selection—what if there was a general purpose library that isn't specific to Python or pandas, but is really, really fast and efficient?

It has a large community building it so you could take that code and use it to build many different types of libraries—not just dataframe libraries, but also database engines and stream processing engines and all kinds of things. That's what was in my mind when I started getting interested in what turned into Arrow.

One of the problems we realized we needed to solve was that we needed to create a way to represent data that wasn't tied to a specific programming language and could be used for very efficient interchange between components.

The idea is that you would have this immutable, constant data structure which is the same in every programming language. Then you can use that as the basis for writing all your algorithms. As long as it's Arrow, you have these reusable algorithms that process Arrow data.

We started with building the Arrow format and standardizing it. Then we've built a whole ecosystem of components—library components in different programming languages for building applications that use the Arrow format. That includes not only tools for building and interacting with data, but also file readers. You can read CSV files, JSON data, Parquet files, read data out of database systems.

Wherever the data comes from, we want an efficient way to get it into the Arrow format. Then we moved on to building data processing engines native to the Arrow format so that Arrow goes in, data is processed, Arrow goes out.

DuckDB, for example, supports Arrow as a preferred input format. DuckDB is more or less Arrow-like in its internals. It has Arrow format plus a number of DuckDB-specific extensions for better performance within DuckDB.

In numerous communities—the Rust community has built DataFusion, which is an execution engine and SQL engine for Arrow. Yeah, we've kind of looked at different layers of the stack—data access, computing, data transport, everything.

We've built libraries across many different programming languages so you can pick and choose the pieces you need to build your system. Ultimately, the goal was that in the future, which is now, we don't want people to have to reinvent the wheel building something like pandas. They could just pick up these off-the-shelf components.

They can design the developer experience and user experience they want to create, and they can get built. If you were building pandas now, you could build a pandas-like library based on Arrow components in much less time. It would be fast and efficient and interoperable with the whole ecosystem of other projects that use Arrow.

**Michael:** It's very cool. It was really ambitious in some ways, obvious to people. They hear about Arrow and say that sounds obvious—clearly we should have a universal way of transporting data between systems and processing it in memory. Why hasn't this been done in the past?

**Wes:** It turns out that, as is true with many open source software problems, the social problems are harder than the technical problems. If you can solve the people coordination and consensus problems, solving technical issues is much, much easier.

I think we were lucky finding the right group of people. I met Jacques Nadeau at MapR who was working on his startup Dremio. I knew instantly I could work with him. When I met Julien Ledem, who co-created Parquet, I was like, yes, we found the right people. Like we're going to make this happen.

It's been a labor of love and much work and stress. But I've been building kind of satellites and moons and planets circling the Arrow sun over the last eight years. That's kept me pretty busy.

**Michael:** It's only getting more exciting and interesting. It says here it uses efficient analytic operations on modern hardware like CPUs and GPUs. One of the big challenges of Python has been the GIL. What's the story here?

**Wes:** In Arrowland, when we're talking about analytic efficiency, it mainly has to do with how modern CPUs and GPUs work. When data is arranged in column-oriented format, it enables the data to be moved efficiently through CPU cache pipelines. The data is made available efficiently to the CPU cores.

We spent a lot of energy in Arrow making decisions to enable very cache-efficient CPU or GPU cache-efficient analytics on data. We were always breaking ties and making decisions based on what's going to be more efficient for the computer chip.

Modern CPUs have focused on adding single instruction, multiple data intrinsics—built-in operations in the processor where now you can process up to 512 bytes of data in a single CPU instruction. That's like 16 32-bit floats or eight 64-bit integers in a single CPU cycle. There are intrinsic operations—multiply this number by that one, multiply that number to these eight things all at once, something like that.

Or you might say: I have a bit mask and I want to select the one bits set in this mask from this array of integers. There's a gather instruction which allows you to select a subset of SIMD vector of integers using a bit mask. That turns out to be a critical operation in certain data analytic workloads.

We wanted a data format that was essentially future-proofed—ideal for current CPUs. But also, a lot of processing is moving to GPUs and FPGAs and custom silicon. We wanted Arrow usable there as well.

Arrow has been successfully used as the foundation of GPU computing libraries. At Voltron Data, we built a whole accelerator-native, GPU-native, scalable execution engine that's Arrow-based.

The fact that was our aspiration and we've been able to prove that out in real-world workloads, showing efficiency gains using modern computing hardware correctly, is a big deal for making applications faster and reducing carbon footprint of large-scale data workloads.

**Michael:** Yeah. Amazing. All right. What else have I got to talk about? You want to talk Ibis or which one? We got a little time left.

**Wes:** Yeah. Let's talk about Ibis.

**Michael:** Yes. Easy.

**Wes:** I think one of the more interesting areas in recent years has been new dataframe libraries and APIs that transpile or compile to execute on different backends.

Around the time I was helping start Arrow, I created this project called Ibis—basically a portable dataframe API that knows how to generate SQL queries and compile to pandas and polars and different dataframe backends. The goal is to provide a really productive dataframe API that gives you portability across different execution backends.

The goal is enabling what we call the multi-engine data stack. You aren't stuck with using one particular system because all your code is specialized to that system. You have this tool where maybe you could work with DuckDB on your laptop or pandas or polars with Ibis on your laptop. But if you need to run that workload elsewhere—maybe with ClickHouse or BigQuery, or maybe it's too big and you need Spark SQL—you can just ask Ibis to do the same thing on this larger dataset. It has all the logic to generate the correct query representation and run that workload.

It's super useful. There's a whole wave of work enabling people to work in a pandas-like way but get better performance than pandas or work with big data. pandas is a Swiss army knife but isn't a chainsaw. If you were rebuilding pandas, there would be areas that are more bloated or have performance overhead that's hard to get rid of.

That's why Richie Fink started the Polars project—a re-imagining of pandas written in Rust and exposed in Python. Polars is built on Apache Arrow at its core. Building an Arrow-native dataframe library in Rust with all the benefits of building Python extensions in Rust—you avoid the GIL and can manage multi-threading in a systems language.

**Michael:** When you're talking about Arrow and supporting different ways of using it, Polars definitely came to mind. And when you talk about Ibis, I think it's interesting that a lot of dataframe libraries try to base their API to be pandas-like but not identical. But Ibis has the ability to configure and extend it differently, like Dask, which is one of the backends here. But the API doesn't change, right? It just talks to different backends.

**Wes:** Yeah. There's different schools of thought. There's another project called Modin, similar to Ibis in transpilation and supporting different backends dynamically. But Modin sought to closely emulate exact API details—function name, arguments—must be exactly the same as pandas to be a drop-in replacement.

That's one approach—the pandas emulation route. There's a library called Koalas for Spark—a PySpark emulation layer for the pandas API. Then there's other projects like Polars and Ibis and Dask DataFrame that take design cues from pandas in how the API works but made meaningful departures in the interest of doing things better than pandas did in certain parts, making things simpler, and not being beholden to decisions made 15 years ago.

Not to say there's anything bad about the pandas API, but with any API, it's large—very large as evidenced by 2000 pages of documentation. I understand the desire to make things simpler while refining certain things, making certain workloads easier to express.

Polars, for example, is very expression-based. Everything is column expressions and is lazy and not eagerly computed. Whereas pandas is eager execution, like NumPy is. That's how pandas became eagerly executed in the first place.

The mantra with Polars was we don't want to support eager execution by default. We want to build expressions so we can do query optimization and take inefficient code and rewrite it to be more efficient under the hood. You can do that with a query optimizer.

That matters a lot when executing code remotely or in a big data system. You want freedom to take lazy analytic expressions and rewrite them based on—maybe you need to seriously rewrite the expression. In Dask, for example, it has to do planning across a distributed cluster.

Dask DataFrame is very pandas-like but includes explicit details to control how data is partitioned and have knobs to control what's happening on a distributed cluster. The goal is to give the developer more control as opposed to trying to be intelligent and make all decisions on behalf of the developer.

If you know a lot about your dataset, you can make more decisions about scheduling and execution. Dask is building query optimization to start making more decisions on behalf of the user. But Dask has become very popular and impactful making distributed computing easier in Python.

They've gotten a long way without turning into a database. Dask never aspired to be a database engine. A lot of distributed computing isn't database-like—it's distributed array computing or distributed model training, just being able to easily run distributed Python functions on a cluster.

It was amazing how many people were using PySpark in the early days just for the convenience of running Python functions in parallel on a cluster—not exactly what it's designed for.

**Michael:** Right. You probably come across situations where you do a sequence of operations. They're kind of commutative in the end in practice, but computationally, how do I distribute this amongst different servers? Maybe one order matters a lot more performance-wise.

**Wes:** Yeah.

**Michael:** Interesting. All right. One final thing. SQLglot.

**Wes:** Yeah. SQLglot project started by Toby Mao, a Netflix alum and really talented developer who created this SQL query transpilation framework library for Python. It's an underlying core library.

The problem being solved is that SQL, despite being a quote-unquote standard, isn't at all standardized across different database systems. If you want to take SQL queries written for one engine and use them elsewhere, without SQLglot, you'd have to manually rewrite and make sure you get typecasting and coalescing rules correct.

SQLglot understands the intricacies and quirks of every database dialect and knows how to correctly translate from one dialect to another. Ibis now uses SQLglot as its underlying engine for query transpilation and generating SQL outputs.

Originally Ibis had its own kind of bad version of SQLglot—query transpilation powered by SQLAlchemy and custom code. They've been able to delete a lot of code in Ibis by moving to SQLglot.

SQLglot is being used to power kind of new Python-powered products. Toby's company, Tobiko Data, is building a product called SQL Mesh powered by SQLglot. Very cool project—maybe a bit in the weeds—but if you've ever needed to convert a SQL query from one dialect to another, SQLglot is here to save the day.

**Michael:** I would say even simple things like how do you specify a parameter variable for a parameterized query, right? Microsoft SQL Server is like `@parameter_name`, Oracle is `?` or SQLite. I think it's also just question mark. Even those simple things...

**Wes:** It's a pain. Yeah. And without it, you end up with little Bobby tables, which is also not good.

**Michael:** That's true. Yeah, this is really cool. SQLglot—like polyglot, but all the languages of SQL. Nice. And you can say, read DuckDB and write to Hive, or read DuckDB and write to Spark or whatever. It's pretty cool.

**Wes:** Yeah.

**Michael:** All right, Wes, I think we're getting short on time. But you know, I know everybody appreciated hearing from you and hearing what you're up to these days. Anything you want to add before we wrap up?

**Wes:** I don't think so. Yeah. I enjoyed the conversation. There's a lot of stuff going on and still plenty of things to get excited about.

I think often people feel like all the exciting problems in the Python ecosystem have been solved. But there's still a lot to do. We've made a lot of progress in the last 15 plus years, but in some ways it feels like we're just getting started. So we're excited to see where things go next.

**Michael:** Yeah. Every time I think all the problems are solved, you discover all these new things that are so creative. You're like, oh, well, that was a big problem. I didn't even know it was a problem. It's great.

**Wes:** All right. Thank you for being here and taking the time and keep us updated on what you're up to.

**Wes:** All right. Thanks for joining us. Bye-bye.