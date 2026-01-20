---
title: "Ursa Labs and Apache Arrow in 2019"
summary: "Talk at PyData Miami"
date: 2019-01-11T00:00:00
tags: ["talk", "transcript"]
slug: pydata-miami-ursa-labs-arrow
word_count: 10263
source_file: transcripts/2019-01-11-pydata-miami-ursa-labs-arrow.md
content_type: transcript
event: "PyData Miami"
video_url: "https://www.youtube.com/watch?v=7HiwzHWiF20"
---

{{< video https://www.youtube.com/watch?v=7HiwzHWiF20 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I announce the formation of Ursa Labs, a non-profit open source development group focused on building Apache Arrow and shared infrastructure for data science. Partnering with RStudio and Hadley Wickham, Ursa Labs aims to create language-independent computational foundations that can benefit Python, R, and other programming communities. I discuss how pandas was built on 2007-era technology and the need to modernize computational foundations for multi-core processing, GPUs, and larger-than-memory datasets. I explain Arrow's goal of creating a standard in-memory columnar format that enables zero-copy data sharing between systems, addressing the "10 Things I Hate About pandas" problems like inefficient string representation. Key technical topics include the Arrow Flight RPC framework achieving 3GB/s throughput, Gandiva LLVM-based expression compiler, and the GPU Data Frame (cuDF) project using Arrow on GPUs.

## Key Quotes

> "It's getting harder and harder to build open source software sustainably."

> "We kind of want to get away from this world where we're having to do all of this conversion between point A and point B all the time and at least have some kind of a way of representing data at the memory level."

> "When I get together with people from the R community, yeah, we're writing different code in different programming languages, but these days a lot of us are writing C and C++ code. A lot of us are solving the exact same problems, but we're delivering solutions to different communities."

> "The reason why we haven't had to address these problems so much in the past is precisely because of Moore's Law. And we've been able to say, well, you know, things aren't great, but we'll just wait a couple of years and things will just magically become faster."

> "Even an empty string in Python 3 takes up 48 bytes. There's just, you know, it's blank zero, 48 bytes, there's no way around it."

> "If the data is an immutable standard, then if you have two algorithms which know how to interact with arrow memory, then they don't have to be rewritten."

> "It's kind of always been the dream, and my dream, to be able to have zero-copy data sharing of complex data sets between the JVM and the native code world."

> "I think it is sort of sad that pandas wasn't really designed for working with massive data sets, and so to have five or ten gigabytes of data and be unable to perform joins in memory and have to write a Hadoop job or write a Spark job, it makes me sad."

> "As a data scientist, data scientists are overwhelmed with all of the complexity and things that people have to worry about just to deal with, I want to read a data set, I want to perform some simple analytics and feature engineering and then use TensorFlow."

## Transcript

**Wes McKinney:** Thanks. It's nice to be here. It's nice to be here in Miami. It's good to see a Python community down here. I've actually spent a lot of my life in South Florida. Not a lot of people know that. But between family and so forth. So I've probably spent a couple of years over the last 25 or 30 years down here. So it's nice to be back in the sun. I just moved to Nashville, Tennessee. And it doesn't get cold there. And it got cold just as I was leaving. So perfect.

So last year, for a variety of reasons, I founded a non-profit open source development group. And this is not the kind of thing that you hear about happening very often. Usually when people want to work on an open source project, it's something that they're working on as their hobby. Like they work on it on nights and weekends. And they push code to GitHub.

Unfortunately, recently we've seen some major security breaches in the Node package manager. And in some of those cases, it was like, hey, I was just having fun building this software. And somebody came along and wanted to maintain this module. And I said, sure. And they didn't bother verifying their identity. And there were certain protocols that were not followed.

But I think a lot of people do open source because it's fun. And if it weren't fun, well, probably a lot less of us would do it. People do open source for many other reasons. Often it's because they're solving a problem that they have at work. And they, for whatever reason, they want to give the work that they're doing either, you know, send the contributions upstream into another open source project. Or they feel like, you know, they've built something that's interesting and it's filling a gap that exists in the world. And so they decide to open source it.

And, you know, pandas, which I understand that many people use, started out as a closed source library. And I made the pitch. This was like early 2009. It's like, hey, it would be really great if we had, you know, a nice library that a lot of people used or, you know, that a lot of people used and made data easy to work with. You know, you can read data files. You can manipulate it. You can do analytics. You know, it'll be great.

So I think, you know, at that time there was sort of skepticism like, oh, well, you know, are people even going to want to do this work in Python at all? And that, you know, now at least people, you know, nobody asks that question anymore.

But there's other, you know, people build up open source projects in other ways. Sometimes they start companies. And so lately, you know, you've probably seen a lot of articles. Everyone's sort of wringing their hands because it's very difficult for open source projects to have successful business models when Amazon Web Services or, you know, another, you know, software company that doesn't do a lot of open source can take the software, build a software as a service offering, and then not give any code back to the project.

And so, you know, we've seen many high profile open source projects like Redis, Apache Kafka, well, not Kafka itself, but Confluent, the company that, one of the companies started by the founders of Kafka. So companies have been changing their licenses essentially to try to make it harder for AWS and friends to take from the open source world and not give back.

And so it's getting harder and harder to build open source software sustainably. And so, you know, as I've been working on the Arrow project for a little over three years and, you know, I decided I didn't like really, I didn't like any of the models for funding the work that I saw, particularly given how much the project is an infrastructure project. It's not a product. It's not like a service that you set up and run. It's not a database. It's not something that could be turned into an Amazon service offering. Maybe some part of it could, but, you know, I wanted to really, you know, have a group of engineers who are focused on, you know, building high quality software that the world can depend on and help the ecosystem, you know, the data science ecosystem, but also many other programming communities evolve their computational foundations into the future.

So I've been doing that and that's kept me pretty busy, you know, over the last year or so. I mean, thankfully we have a number of gracious sponsors who are funding the work. We're growing a team. So things are going well.

So as part of this, I wanted to partner with the R community. And so the first time people on the internet found out that Hadley Wickham and I are friends, it sort of produced all this like, what? Like R and Python people can be friends with each other? Like, isn't that, it's like not allowed, right? It's like, you know, cats and dogs, like, you know, Montagues and Capulets, you know, that kind of thing.

And, you know, it's like when I get together with people from the R community, yeah, we're writing different code in different programming languages, but these days a lot of us are writing C and C++ code. A lot of us are solving the exact same problems, but we're delivering solutions to different communities. The R community happens to be more skewed towards the academic statistics world and certain, you know, and so in data journalism and communities where the Python hasn't historically had as much penetration, you know, Python has more machine learning and, you know, kind of computer science in different communities. So it's great for us to be working together.

We are now five full-time engineers, so I'm very happy to be having, putting five people to work full-time just doing open source software and nothing else. We're also working with some folks from the RStudio Tidyverse team, people you may see out in the wild contributing to Apache Arrow or other projects. And my shameless plug is that we are still hiring, and so if you or anyone you know would like a remote software engineering position in a large open source project, you know, please let me know.

So we have a number of sponsors. So from the get-go, I partnered with RStudio to make the business of growing a team of, you know, employees and engineers easier for me so that I can spend more time focused on building software, less time on running a business. And I have run a business in the past. Like, I founded a startup called Datapad six years ago, and so I've had the experience of, you know, doing all of the accounting and business stuff, and so I wanted to do less of that and more software.

Before this, I spent two years working with Two Sigma, who, you know, have been great sponsors of the Arrow project. NVIDIA, who are out in force here at this conference, are sponsoring the work. We just received sponsorship from the Open Data Science Conference, and you might think it's weird. I've got to put this on Twitter. I haven't done it yet. I'm just in the process of updating the website, but you might think it's interesting for a conference to sponsor an open source software development group, but, I mean, you think about the relationship that conferences have with open source software. Conferences are growing and have revenue because the open source software is popular, so it's not, you know, it's not that strange, and I hope that we see more conference organizers giving money back to open source.

So there's other ways that sponsors can help. So NVIDIA just donated these two big workstations, which are now keeping my apartment really toasty. So I just don't even need to turn the heat on anymore, and, you know, well, not that toasty because, you know, cryptocurrency mining is not really profitable right now, so we are only running CUDA for Arrow development, and I'm probably not supposed to joke about that. It is a joke, after all.

So, but it's great to have, you know, other kinds of support because, you know, software development requires tools. You know, we need tools like these to be able to make sure that we are, you know, building software that can run on this kind of high-end equipment, which gets used in many different environments.

So anyway, so with all of that out of the way, I'm going to get to the technical stuff. So I'm going to make some broad generalizations, and so please, you know, don't nitpick the details too much, although nitpicking the details is important.

But, you know, after, you know, after I started working on the pandas project in 2008, and after five or six years, you know, we had built, you know, we had built the project, you know, myself and the other pandas developers had built the project based on the technology that was available essentially in 2007, 2008. So that was NumPy, SciPy, Matplotlib, IPython, you know, CPython itself.

And if you think about, if you think about NumPy and the scientific computing libraries, they in turn are providing a Python API to do array computing, matrix operations, linear algebra using techniques and software that was available in the mid-90s and even before that. So there's like a lot of Fortran code for linear algebra that was available in the 80s and 90s and even the 1970s.

And so there's kind of this huge legacy of computational software that is powering modern data science. And some of it has scaled well to, you know, current hardware, and, you know, some of it has not. Some of it also has to, the problems have to do with just, you know, the software development.

So pandas was built so that every operation, every line of code, every function call is immediately evaluated. And so that works well when your data is a megabyte, but it doesn't work that well when your data is a terabyte. So just things like the way that code is evaluated has to change when you want to think about working with larger, larger data sets.

When you're working with a lot larger data sets, the way that you manage memory and the way that you access data has to change in order to be more scalable.

Another problem that I experienced, and this is partly in interacting with the R community and other, you know, open source communities, is the fact that even though we're solving many of the same problems, we're, you know, we're kind of working independently. Like, we don't collaborate very much. You know, we don't share code very often. If we all have data frames, and we say the word data frame, but if you go under the hood, our data frames look different. And so, you know, I couldn't help but think, like, well, what if we could try to address some of these problems and also make it easier for the different communities to collaborate?

And so, in an ideal world, you know, there's not really any rocket science. It turns out that there's, you know, a rich literature of computational techniques for large-scale data processing. You know, the analytic database world has been solving large-scale data processing problems since the 80s and 90s. There's a rich literature that can be mined for techniques for working with a lot larger data sets and tools like pandas.

So, ideally, you know, we would build everything to be multi-core native. Now we have GPUs. So, you know, even though Moore's Law is sort of over for CPUs, like, the scalability curve is, like, still going and going and going for GPUs. So, we have to take advantage of that if we want to keep scaling into the future.

We have all these fancy runtime compiler tools. So, gone are the days of having to hand-generate x86. Like, we can use LLVM to generate code, efficient code at runtime. We can think about how we can share, you know, now that systems have become a lot more heterogeneous, we can think about sharing data more efficiently between systems.

So, there's a lot of stuff we can do. And one point that I often make is that the reason why we haven't had to address these problems so much in the past is precisely because of Moore's Law. And we've been able to say, well, you know, things aren't great, but we'll just wait a couple of years and things will just, you know, magically become faster because processors get faster because of Moore's Law. Also, the RAM will get bigger, so, you know, more data fits in memory, so we can kind of just punt on solving, on thinking about these problems.

So, the Arrow Project was conceived in 2015 kind of serendipitously as a group of, you know, 20, 25 open source developers that I had connected with mostly out on the West Coast who were key people in various big data projects. And I had just started working at Cloudera and I wanted to somehow mind meld the data science world with folks in the big data and the database community because traditionally, like, I started telling them about pandas and about data science and, you know, I'm dealing with a bunch of people with PhDs in database systems and they have never, you know, they don't know anything about R or Python. They've never really experienced this world. And so, there's just this kind of, like, non, there's no, has historically been no collaboration happening.

And so, what I would like to see is to enable these communities to collaborate and for the data science world to be able to benefit from all of the research and ideas that have been generated in the analytic database community in the last 30 years.

So, when we started the project, the single problem that we wanted to solve was to define an open standard for representing tabular data in memory. And so, pandas has its own way of representing data. R has its own way of representing data. Every SQL database engine has its own internal runtime format.

So, you know, we can't be all things to all people, but, you know, it would be nice to have some kind of a reasonable open standard that could be used to power analytical applications.

So, thankfully, three years have passed or almost four years have passed since we started even talking about the project. And so, it turns out that a lot of people agree that it is a problem. And so, you know, what we would like to see, and I understand that Clement from NVIDIA also spoke about this, but we kind of want to get away from this world where we're having to do all of this conversion between point A and point B all the time and at least have some kind of a way of representing data at the memory level.

So, in RAM or in shared memory, like memory maps, where assuming that two systems know about Arrow, that they have the option of sharing data with each other using Arrow.

Let's see, is this thing working? I'll use the keyboard.

So, now that time has passed, we started out with Java and C++. We're now up to 11 programming languages. So, we most recently added C Sharp and MATLAB to the mix. So, I think other languages that we don't have that would be really interesting, I'd like to see Swift. People are talking about Swift. So, you know any Swift programmers, like this could be a project to work on. We have Rust. A lot of people are programming in Rust.

So, but in terms of the work that we're doing in the project, I, and this is my opinionated view. So, we're focused in a few key areas. So, the first is that we want systems to be able to share data and share code.

So, if you want to share code, you need the data representation to be the same. Otherwise, you say, well, you know, this table looks a little bit different from the, you know, what my code expects. So, I have to convert it to my expectation and then run my code.

So, if the data is an immutable standard, then if you have two algorithms which know how to interact with arrow memory, then they don't have to be rewritten.

Because it's, arrow is a brand new data representation, we have to implement connectors into storage systems and file formats. And so, we've been spending a lot of time doing that. We want to enable systems to share data with each other through different protocols.

So, whether that's through shared memory and memory maps or through, on a network. So, if a system says, hey, you know, rather than going through ODBC or JDBC or some other kind of database protocol, say, here's my port which exposes arrow data natively. And so, we can, you know, move data around a network without having to convert to some intermediate representation.

So, it's a, so as you can imagine, this is very ambitious and it's been a difficult project to work on. And we're working kind of with two kind of high level goals. So, the first is that we want the platform of libraries and all these programming languages to be a suitable development platform, like a foundation for new systems to be built.

So, if you are building a new database, you're building a new data frame library, you know, maybe you're building like a data micro service, like, you know, this, you want to have a service that can receive a table, apply like a small operation to it and then send the data onward to some other service. We want to make those things easy to build.

And we also want to be able to retrofit existing systems with kind of algorithms and tools that are coming out of this, out of this ecosystem. So, that would be like, you know, like the pandas ecosystem, for example. We'd like existing data frame, like data science projects to be able to benefit from this.

All right. Let me use the keyboard.

So, it's kind of like the mnemonic for, you know, thinking about system architecture. I didn't intend to become a computer scientist. I was a mathematician. It just, you know.

Anyway, so, you know, traditionally you build a system and you build this kind of vertically integrated thing where you've got to make your own data structures, you've got to build data connectors, you write your own algorithms, maybe you design your own file formats. If you need to move data around in a distributed system, you define a wire format for moving data around.

So, we'd like to develop standards to kind of solve, address all of these problems at the same time. So, we have standard data structures. We don't have to serialize. We have reusable algorithms, reusable file formats, and we can move data in a distributed system in a standard way.

So, if you ever look at the architecture of a database system, usually in a database you just interact through the front end. The front end is often SQL queries. And, you know, the other parts of the system you don't really see. So, there's an in-memory, like a way that data is managed in memory. There's the query engine that does, you know, select, join, group by, where, and so forth. And then there's back-end storage.

And, you know, there's, you know, I think one of the things that the Hadoop ecosystem did over the last 10 years was decouple the storage, like the file persistent storage, from the database system. So, this idea of, like, bring your own database and, like, all the data is in the Hadoop file system. And now cloud storage, like S3 and Google Cloud Storage, has taken the role of this as well.

So, what we would like to do is kind of decouple all of these components and give them a public API. So, if you need to store and serialize data, we can do that. If we need to compute queries, traditionally databases would not expose the details of their query engines to library users.

But the thing is, the front-end, that's kind of opinionated. Like, maybe some people like SQL, some people like code that looks like pandas. I don't want to dictate what the user API looks like, so that if somebody wants to build something that's eagerly evaluated, they can do that. Something that's lazy, something that's SQL, we can have many different ways of interacting with these components that don't require an opinionated interface, or even an opinionated programming language.

So, you wouldn't be required to use Python or use R. And, in fact, like, it's been really exciting that we're working with folks in the Ruby community in Japan who, you know, we write something in C++ and within a few weeks we have ways to interact with that code in R, Ruby, and Python. So, it's sort of, it's kind of a brave new world. Like, I've never, you know, worked on a project like that before.

So, just kind of rehashing the things that I was just saying. I said them out loud. So, I kind of want to rewind or, like, at least take one step back a little bit into the practical domain of the, of the pandas user.

You say, okay, Wes, like, this all sounds great. You know, we're going to make new systems really fast. We're going to make systems more interoperable. We're going to have all these libraries and all these programming languages. Sounds great. How is that relevant to me? Because every day I go into work and I write import pandas as pd, pd.read.csv, and then I'm off, off to the races.

So, I wrote, I did a, I gave a presentation a little over five years ago, and the title of the presentation was 10 Things I Hate About pandas. And a lot of people thought that was funny, and, but it was really kind of constructive criticism about the internal implementation problems of, you know, kind of how pandas is implemented, like, how it's designed and, like, why those are causing issues.

And it was not to say that, you know, some of these things are fixable, and so this was before we had categorical in pandas, and so that's resolved some of the problems with strings.

But in general, like, if you have really big data that doesn't fit into memory, and you, you know, ideally you could memory map that. Very difficult to do with pandas. So, people have been tackling, have been tackling the out-of-core, very large data problem with other tools like Dask, and Dask has, you know, been a great tool for helping scale, scale pandas.

The way that pandas represent strings is really inefficient. So, they use a ton of memory, and there's basically no way for computational code to process them efficiently, because they're all in the Python object heap.

And so if you've never really thought about this, like, and this is a, from, from my collaborator Uwe Korn's slide deck. So, if you have a pandas series, like a data frame column that has strings, it's representing those strings in a NumPy array that contains Python objects. And so each Python object has a pointer into various objects all over the, you know, wherever Python allocates strings.

So, not only is, not only is the memory that represents the string all over, all over the process heap, but the, the struct, like the C struct for the Python string is large. Like, it actually, from Python 2 to Python 3, it got bigger. So, if you're using strings in Python 3, like, I know we're all really happy to, like, only be using Python 3 now, but, right? Like, it's 2020, it's almost here. Yeah, it's like, this is more serious than Y2K, really, I mean.

Yeah, so, you know, if you, even if you have a string, even an empty string, like, an empty string in Python 3 takes up 48 bytes. Like, there's just, you know, it's blank zero, 48 bytes, like, there's no way around it.

So, but, so one thing that, that, so Uwe, who's one of the Arrow developers, has been able to do is use extension arrays in pandas to extend, extend, I already set this up for myself, to extend pandas with, with Arrow string vectors, which have kind of, like, a packed, kind of contiguous memory representation. They use a fraction the amount of memory that Python strings do, at least the overhead is like, is 4 bytes instead of 48 per string. And all the data's contiguous, so just by having a more efficient representation, you use a lot less memory, you can process the strings a lot, a lot faster, so.

So, there's some other things, like, you know, like, allowing data to be non-contiguous, like, having data frames composed in multiple chunks. We don't really have tools for dealing with nested types, so, I don't know if you've ever run into that problem where you're processing JSON and you need to kind of, like, unravel the whole data structure before you can do anything.

So, my view is, like, we should have operators to just process the data in place and do so efficiently. So, we, so, these are problems that, that we're, that we're tackling in, in Arrow land.

So, I've been talking a lot, so I don't want to run out of time, but I'm going to tell you about a few things that we've been doing that are cool, where, you know, the benefits of this work are, are playing out.

So, one thing we did with my colleagues from, from Two Sigma and also worked with folks, Brian Cutler from IBM, some other folks and, and folks in the Spark community have been involved at all, is that we made custom Python functions on Spark run a lot faster.

So, now, if you're using Spark, I think, 2.3 and higher, there's now, like, a special pandas UDF where you can write extensions to Spark SQL that use pandas operations and have, you know, can have, like, up to 100 times better performance.

And so, it's a bit crazy that the performance is so much better when you consider how much work is actually happening. So, when Spark SQL is evaluating these, these pandas UDFs, it's actually performing four separate conversions to and from the Arrow memory layout.

So, Spark SQL has its own internal representation of tabular data inside Spark SQL, Spark DataFrames, depending on what part of Spark you're using, they could either be Spark DataFrames or just general Spark SQL. But Spark SQL does, its data is not resident in shared memory, so you can't do true zero-copy sharing between processes, so if you wanted to make a large data set available to a Python process, maybe this is changing, but at least as far as, you know, with my up-to-date knowledge, I don't think it's possible.

But the way that it works is that Spark SQL serializes data to the arrow columnar format that is streamed to the PySpark worker process, it's converted again to pandas, but then we built a layer to evaluate native pandas code against data, like chunks of data that are coming from Spark, and then this is streamed back to Spark via the arrow format.

And you might say to yourself, well this is crazy, like we have four serialization steps, like we have to convert from Spark's internal format to arrow format, then to pandas, then run some pandas code, then convert back to arrow, you know, to arrow and then from arrow, so we have four serialization steps, so that can't possibly be efficient.

But you have to remember, like where did we start, and so there was already a multi-step serialization process that was happening, but that serialization format was particular to the Spark PySpark bridge, and even with all of this serialization going on, the efficiency, you know, with the efficiency of the arrow format, these are some sample user-defined functions that are pandas-based, you know, in some cases we're able to get more than a 100x speedup in evaluating custom Python code.

So if you see here on the left, suppose that you wanted to run, you know, compute the cumulative probability function for a normal distribution inside Spark SQL, you can write that using SciPy stats, and when you're using Python, all of these functions that you have for analytics are supposed to be, they're intended to be invoked on NumPy arrays, and so you can use them on pandas objects as well, but if you were to, so the ideal mode is to invoke these functions on a thousand rows, on a thousand values at a time, or a million or a billion values at a time, not to run them once for every row in a data set.

So even though we have all of this serialization work to do to move the data to and from Python, the efficiency gains are coming largely from changing the execution model from row-based to vector-based, and so batching the user-defined function evaluations.

So that's cool. Another thing we're, another thing we're developing actively right now, in case this is relevant to you, is a, an RPC framework for building data services. So if you have a system and you want to, you want that system to be able to send around large data sets, this is a framework for defining custom data services.

We're using gRPC, which is, you know, kind of become the gold standard open-source RPC framework created by Google. The protocol uses protocol buffers, and so if you know about protocol buffers, you might say, well, protocol buffers, you have to parse them, and so how do we avoid that?

Well, we spent some time doing some low-level optimizations in gRPC so that we can receive chunks of data from the server and interpret them as being arrow data sets without having to do any additional parsing.

So let's see here. So I kind of want to make this, this whole thing real to explain kind of how this zero-copy thing works, so I'm just going to, since I don't have a lot of time, I'm just going to skip to the punchline, but all right.

All right. So here on my local disk, I have an 11-gigabyte file, I hope this, I actually haven't tried this demo today, so maybe it doesn't work, because, you know, open-source, but, so 11-gigabyte file, it contains a stream of table chunks that I wrote in one stream to disk.

So we have, like, the notion of streaming data, so which has to be written from start to end. They're also, we also have a way to store data on disk that you can do random access and read a block from the middle of the table.

And so what we can do in Python is memory map that file, open the stream, and then read all of the stream as a table, and so reading that, reading that entire 11-gigabyte file only takes about 10 milliseconds, and now we have a table in memory that has, let's see, 400 million rows, and I can, I can access a column and then access any row in the data set.

So if I want the thousandth row or the 10 millionth row, they happen to all be the same in this case, but, so I can do random access on this giant data set.

And so in the context of, you know, streaming RPC where a table is sending you batches of data, so what you can do is when you receive a chunk of data from the server, you can do whatever you want with it. You can buffer it in memory, you can stream it to a file.

So suppose that a server sends you an unknown amount of data, and possibly more data than you have RAM available, you can put all that data on disk and then memory map it and then proceed with your analysis.

So compared with the way that like pandas handles data, this is like a totally, totally new world.

So if you had, if you had implemented a, the RPC framework is called Flight, and so if you had built a server implementation, there's many different architectures you could do. You could have a planner node which, you know, tells you like which servers to get the whole data set from. It might be distributed across many servers. The planner and the server with the actual data might be the same server.

So there's many different ways you could set it up, but you request info about a data set, which is called a Flight, and then you perform a series of gets to the underlying nodes that contain the data. And so those could be serial or parallel.

And so just in the last month or so, we've created an implementation of this, and in C++ and so in Python, I'm able to move around about three gigabytes per second with a single thread on localhost, and that includes kind of end-to-end, push data through the socket, receive on the other side, and have it ready to go, kind of memory mapped in memory.

So a lot of cool stuff are possible with this.

So if we have any data protocol nerds in the audience, so the way that things work under the hood is when you make a request to the server, a data set get request, it uses a gRPC stream to send a sequence of row batches back to the client, and so each of those row batches might be a thousand rows or a million rows, you know, depending on how you set things up.

And even though the data is transported in a protocol buffer with some additional metadata, we built, we were able to write a custom deserializer for gRPC both in Java and in C++ to be able to receive that payload and avoid doing any extra copying of the memory inside the protocol buffer so that we can interpret it as an arrow data set.

So kind of our goal in building this technology is to create something that is high quality, very general purpose, and that you can take and use it as a library inside existing systems.

So when you're building, so when you're doing RPC, so we sort of said, you know, we don't care about what kinds of commands you execute, you can define custom commands for your clients and servers.

So you could create a custom command that executes a SQL query. So this is a protocol buffer definition that contains a URI for a database and a query. You can send that in a, you know, get info RPC with type command, and then the server, if it understands that command, will send you back instructions how to retrieve the results of that query.

But the kinds of commands you could send, it's really, it's up to you. You can implement whatever you like.

So that's some stuff that's going on in the project, just in recent times. But we've been in development for almost three years now. We have almost 200 unique contributors.

One of the areas that, in terms of, you know, bringing, building a large community of users is that we've been trying to support as many programming languages as possible. There are now up to 10 programming languages. Not all of them are, have a fully complete, you know, set of functionality. So some of them are native implementations.

So we have a native implementation in C++, Java, JavaScript, also in Rust, and Go. And the rest are, the rest are bindings. And so in Python, we interact with the C++ libraries directly. There's folks in Japan, in the Ruby community, who are working on Ruby bindings to this tech, and they're going through a C binding layer.

And but, yeah, so we're kind of essentially adding as many programming languages as we can and making sure that we're giving, you know, we're enabling people to access the data and access the libraries to be able to use those inside their systems.

Another project that's going on, that's pretty interesting, is a expression compiler for creating higher performance analytic functions that evaluate against tables and data frames.

So this came out of the Dremio Corporation, which they're building an open source project called Dremio, which is a kind of federated data access layer. It's SQL-based. It's written in Java. And they wanted to accelerate the evaluation of the expressions that are found in the select part of a SQL query and the where part, so essentially projections and filters.

And even though their system is written in Java, they created a compiler for these expressions that uses LLVM, so it's invoked from C++. And because there's a common memory format in Java and C++, that data can be exposed to the Gandiva compiler runtime through JNI without actually copying the memory because it's just memory addresses that are, you know, coming out of off-heap JVM memory.

So it's kind of always been the dream, and my dream, to be able to have zero-copy data sharing of complex data sets between the JVM and the native code world. I guess it's only taken, you know, it's only taken me ten years to get here, but I'm glad that we're finally getting there.

Some more use cases, but there's another exciting thing that's going on.

So last year, NVIDIA got together a group of companies that are building, a group of companies that are building, doing analytics on the GPU, either building databases that run on, that do interactive analytics on the GPU. Companies like, you might have heard of like MapD, there's another company called Graphistry doing kind of in-browser graph exploration and visualization that's GPU-powered.

And the idea was to create libraries of reusable analytic functions for CUDA to enable, first of all, to enable data to be shared between one GPU-based system and another, and have a standard library of algorithms for performing, doing feature engineering and data frame operations on data on the GPU.

So they've called this the GPU data frame. It's essentially arrow on the GPU.

And the kinds of things that are possible now is that you can run a SQL query in MapD, which is a GPU-based database. You can ask MapD to leave that data, the results of the query on the GPU. That data can be made available to another process using CUDA's built-in inter-process communication, so CUDA IPC.

You can get a handle to that data in Python and then write custom code in Python, compile it with Numba, which is using LLVM, and then run that directly on the data set in the GPU.

And this is the kind of thing that if you didn't have a common data representation, this just would not be, this would not be possible, not be possible at all.

So very cool stuff happening here. As time has gone on, I guess the number of companies and folks who are contributing or using Arrow has expanded.

There's some folks, so one of the components of the project is a system for managing shared memory regions that's used in the Ray machine learning project, which is out of the RISE lab at UC Berkeley.

So we've had folks from Alipay, Ant Financial, contributing to the project, which is really cool since I think the running joke is always somebody from California meets somebody from China and they're like, oh yeah, we have big data, and they say, well, we've got, this is China, we've got probably 10 times as much data as you do.

So I think getting contributions from folks in China is really important for ensuring that these systems are scalable to kind of that level of data sizes.

Sorry, I don't want to overwhelm you with technical detail, but so anyway, as you can tell, this is stuff that I'm very excited about.

A lot of people, let's see how much time I have, like what, five minutes? Yeah, five or ten minutes, yeah.

I'll make some time for some questions, but a lot of people ask me, like Wes, how can I use this software, like how is this relevant to me? And it really depends.

So if you're a data scientist or a data engineer, so my objective over the next, I've been working on this project for about three years, and there's easily three or four more years of work that I want to do on it.

But there's one area which is I would like to deliver a natively Arrow-based kind of next generation data frame library that is a companion project to pandas that's designed for working with very large data sets that has memory mapping built in as its key feature, so you can have, treat data on disk as though it's in memory, so if you have hundreds of gigabytes of data on disk, you can perform meaningful analytics on your laptop without having to spin up a spark cluster.

Okay, I came back, because I think it is sort of sad that, you know, at the level, you know, pandas wasn't really designed for working with massive data sets, and so to have five or ten gigabytes of data and be unable to perform joins in memory and have to, you know, write a Hadoop job or write a spark job, it makes me sad, and I think part of the problem is that data science systems don't, internally are not architected like databases, so they don't have query planners.

If you join two data frames and then want to immediately filter and aggregate, there's no way for pandas to be able to optimize and evaluate that efficiently, that's something that we could build, that's something that we could hypothetically build inside pandas, but, you know, that would be something that, you know, that would be code that's not really reusable outside of the context of pandas.

So, but I'd like to build all of this in a way that is not Python specific, so the R community can take advantage of kind of improved, you know, computational internals for data frames, folks in the Ruby world can use that as well, anyone who wants to build bindings to those libraries can take advantage of them.

I think with the work on like faster RPC and messaging, I think we will see a wave of a lot of systems deprecating their existing data access and RPC layers in favor of natively, natively arrow based messaging. So, you know, to be able to move multiple gigabytes per second through a socket, and that's kind of end to end, you know, you know, traditionally messaging layers might, you might get a few hundred megabytes per second, so to have a 10, 10X, you know, you know, 5 to 10X improvement in throughput improves, you know, resource utilization, you know, it removes a lot of the serialization time that's spent in distributed systems, so it's a clear, clear win in terms of cost savings inside, inside data centers.

And, you know, I honestly envision a world that is built around the notion of data microservices where you have a centralized metadata registry, you can see like here's all of my data services available, I use the exact same client interface to access all of them, and you can push and pull data sets at high, at high speed in a, you know, in a cloud or kind of cluster, cluster environment.

But right now it's, it's difficult because you use different clients to access data, you have to think about how's the data stored, is it a parquet file, is it Avro, is it, you know, is it CSV, like what library do I use, like what settings do I use with that library, like how do I parse the dates, you know, does this have missing data, how is this missing data represented in memory.

So there's like, you know, as a data scientist, you know, data scientists are overwhelmed, personally I'm overwhelmed with like all of the complexity and things that people have to worry about just to deal with like, I want to read a data set, I want to perform some simple analytics and feature engineering and then use TensorFlow.

And there's so many, there's so much, you know, stuff you have to deal with to get to the point of actually doing, you know, like the actual science. So I would like to simplify that as much as possible and just make it about, you know, I request a data set, I get the data set as fast as possible, I don't have to worry so much about all of these details, and I can get on with my, my work as a data engineer or data scientist.

So hopefully that sounds, hopefully that sounds good, but, you know, I think to build technology like this that kind of makes things less fragmented and helps unblock these use cases is a great deal of work. So, you know, people often ask me, how long am I going to have to wait, but, you know, I think the next few years are going to be, you know, pretty impactful in terms of getting the software deployed in many places in production and beginning to make things, you know, faster and simpler.

So, thanks for, thanks for listening, I guess maybe I have five minutes for, for questions.

**Audience Member:** Could you talk about scheme evolution in the format, please?

**Wes McKinney:** Yeah, so the, so the format is, well, so first of all, it's not for, it's not for long-term storage, so it's for ephemeral, ephemeral storage and kind of, you know, for data transport. But I guess the question might be, suppose I have an old server sending data to, you know, sending data to a, a new, a new client, so in the case that you have, well, the case I was talking about is you had that disk on, that file on disk, that arrow file, let's say you have a different schema with several different files.

Yeah, oh, that, I mean, that's, that, that's a temporary file, so that you wouldn't want to, you know, you wouldn't want to store that on HDFS and then come back and read it seven years, seven years later. So in the event that you're, you know, in the event that your schema changes, well, I mean, you can look at, I mean, you can look at the two schemas and project one to the other.

We haven't written the projection code, so, like, hypothetically, you could say, you know, here's the schema I want now and read this file, but conform, you know, when there, if there's a new column that isn't on, on disk, then that column would have shown up as all nulls in the result. But yeah, the schema is, yeah, the schema is stored with the data, so you can look at the schema and decide what you want to do.

**Audience Member:** Hi, thanks for talking to us today. I was just wondering about your, you mentioned Two Sigma as your early collaborator or some sort of, like, contributor. Can you elaborate on that a little bit and maybe talk about specific use cases or applications of error in the hedge fund industry in general? Thank you.

**Wes McKinney:** Yeah, well, yeah, I guess I can't, I can't speak specifically to what Two Sigma is doing with their data, but they, but Two Sigma has a, has a petascale data warehouse and invests a lot of time and money in, in data, you know, in data collection, has acquired companies that specialize in data collection, and I think that they view one of their most valuable sources of intellectual property is their data itself.

Heavy Spark user, a heavy enough Spark user that they actively contribute to Spark and have done significant internal developments to make Spark easier to use in a kind of multi-tenant setting in a lot, in kind of large cloud and on-prem clusters.

But they're also a heavy Python user, and so, you know, the reason that I, the reason that I went to work there is with, is essentially the promise of making Python on Spark a lot better, which we did successfully do. And so, you know, so my colleague, Li Jin at Two Sigma did that work in collaboration with IBM.

And, you know, they, they're also a big Java shop, and so the kind of improved interoperability between the Java JVM ecosystem and the native code world is, is very interesting for companies like Two Sigma that have large, you know, large Java-based systems.

Thank you.

**Audience Member:** First off, I'm super stoked about Arrow. Like, the spec looks really awesome and I'm really excited to use it in a pandas DataFrame. One question that I had about future directions, if there were any, I've read most of the spec and I was really excited to see nullable data in, like, a bit array mask. And I think that was one of your points in your 10 things I hate about pandas talk is, like, how weird null data is in pandas. I didn't mention that here, but it's, I think I should add that to the slide.

**Wes McKinney:** Null data is weird in pandas, and so addressing the, where's that slide? Somewhere up here. Yeah. So, I'll add it to the slide, but, yeah, addressing the kind of weird rough edges and inconsistencies with null data was, yeah, was also a big motivation.

So, in Arrow, you know, there's, so there's a bit for each value. The bit is on if it's non-null and off if it's null. One of the cool things about that is that if you have a batch of data that has no nulls, you can just skip checking for nulls. And, you know, if you have, you can use hardware operations to count really quickly.

So, I wrote, like, a blog post about this recently that, I mean, basically we should stop using sentinel values and use bits instead. Anyway.

**Audience Member:** But by extension, I guess my question was taking nullity to the furthest degree where you have, like, really sparse data. This came up in Richter's talk yesterday. I've tried to use, like, the pandas sparse data frame before and found it to be kind of not, it looked like kind of unloved, like it wasn't being developed really actively. And I was wondering if there were plans to incorporate sparse data into Arrow and then via that pandas later.

**Wes McKinney:** Yeah. I think that, I think that sparse, the sparse objects in pandas are even, are even planned for deprecations and removal. So, sorry to hear that, but I think the way that we would, I think the way that we would address, that we would address sparse data in Arrow is with run length encoding.

And so it's been discussed, but so far there isn't a proposal around, like, how to incorporate it into, into the specification. And so I think there's, it's one thing to say you run length encoded data in memory. A lot of database systems already do this.

But I think the real question is if you want to be able to send run length encoded data from one system to another. And so that's where we would have to do some, some, like, evolve the specification to accommodate that.

There's also kind of the desire to compress data on the wire. And so far we've, we've been concerned with, like, random access memory mappable representation and, and not dealing with compression. But that's also, like, there's a JIRA open about it. But that's something that we eventually have to have in the, in the protocol.

**Audience Member:** So I have, like, two small questions. The first one is do you see any sort of, like, pandas rewrite or ideally in the future it's going to be a rewrite of any of these libraries or it's always going to stay kind of in the fence, in this outer layer as the front end? And the second one is if you can, like, really quickly tell us about the Apache incubation, how that happened, how Arrow got into Apache, and what are the benefits? Just completely out of curiosity.

**Wes McKinney:** Okay. So the, so the first question around rewriting pandas, that seems unlikely. So there's a couple of things. So pandas is an extremely large library. And the way it's, the way it's designed, it's, it's not very amenable to extremely large data sets in the way, just the way that the library works.

And so we've spent a lot of time, like, the pandas core developers and I, like, we all met up last summer in Austin, and this is one of the topics that we, that we discussed.

So I think that the, the consensus is that we want, you know, we want pandas to continue to be, like, a hugely featured, like, super big Swiss army knife of working with data, with a very wide, you know, large collection of APIs, very flexible for working with, you know, low, you know, low gigabytes of data and on down in memory.

Obviously, you know, Dask DataFrame and other projects will continue to use pandas, like, as a black box for doing out of core algorithms. And so that's been going really well.

But I think my, my interest is in building a, essentially companion project might be one way of putting it, but a library that's designed for working with very large data sets and data sets that are large largely on disk, where you need to select, filter, aggregate, join, essentially more like a database, but embedded and in process rather than being a database system that you have to run.

And that, and that's, that will be all be arrow powered and, and something that could be used together with pandas.

In parallel, of course, I think there's some parts of pandas where, like, we have code that we're maintaining, like, that could be retrofitted with stuff that's coming from the arrow libraries. And, you know, that will mean less code to maintain for pandas and, and better performance as well in some cases.

So it's kind of a bit of both, but I think, like, a grand kind of API compatible rewrite of pandas is not in the cards.

The second thing is, so we, we, we decided to do a project in the Apache Software Foundation mainly to head off concerns about kind of, kind of governance and, like, competition amongst vendors.

So, like, a number of the individuals who helped start the project worked for big data companies that are in direct market competition with each other. And one of the ways that the, the ASF helps is by providing, like, a neutral ground for competing vendors, like, the people that work there to still collaborate and say, like, oh, we can't, you know, we can't have one company with a ton of money come in and take over the project. Like, the ASF, like, helps protect the other developers from corporations with lots of money.

So we, yeah, so, so we formed a, we, we split some IP out of the Apache drill project to create a new top level project in 2016. And so we were kind of a top level project from the, from the get go, which, which spared us some of the trials of the incubation process that a lot of projects often have to go through.

**Audience Member:** Do you have any remarks on the new data class feature and is it 3.6 or 3.7 and its usefulness in the pandas workflow, pandas workflows, arrow, or other interesting applications of that new feature?

**Wes McKinney:** I haven't looked, I haven't looked carefully enough to have, I haven't looked carefully enough to have strong opinions about it. I will say that I think it's good that the language moratorium has been lifted and that new features are being added to Python.

I mean, I think if data classes can be used to make, like, nicer ORM-like features, like, I think it, like, there were already, maybe some people in the room are familiar with traits, like, anyone ever use traits before or traitlets?

So this was, like, a long time ago. There was essentially something very similar to data classes where it would do type validation of attributes and if you set a value that was the wrong type, it would error, things like that.

And maybe I think data classes seems maybe like a more, I maybe have the feature set wrong, but it seems like it's, it's a good thing. So, and if it can be made to work well, kind of together with pandas or other tools like this, then, then that's great. So.

**Host:** Thanks again, Wes.

**Wes McKinney:** Yeah. Thank you.

**Host:** So we've got another session of talk starting in here and then tutorial starting at 2.15. Might run a couple minutes late to give you guys more of a break.