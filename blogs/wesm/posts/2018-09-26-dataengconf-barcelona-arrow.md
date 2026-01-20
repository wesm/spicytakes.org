---
title: "Apache Arrow: Cross-language Development Platform for In-memory Data"
summary: "Talk at DataEngConf Barcelona"
date: 2018-09-26T00:00:00
tags: ["talk", "transcript"]
slug: dataengconf-barcelona-arrow
word_count: 4274
source_file: transcripts/2018-09-26-dataengconf-barcelona-arrow.md
content_type: transcript
event: "DataEngConf Barcelona"
video_url: "https://www.youtube.com/watch?v=Hqi_Bw_0y8Q"
---

{{< video https://www.youtube.com/watch?v=Hqi_Bw_0y8Q >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I present Apache Arrow as a solution to the fragmentation problem in data systems. I explain how I founded Ursa Labs, a non-profit open source development group partnering with RStudio, to build shared infrastructure for data science across programming languages. The talk covers the challenges of funding open source sustainably, why pandas was built on 2007-era technology, and how Arrow provides a standard in-memory columnar format enabling zero-copy data sharing. I discuss use cases including Spark pandas UDFs (achieving 100x speedups), the Arrow Flight RPC framework, and the "deconstructed database" vision where query engines, storage layers, and user interfaces can be modular and interchangeable. I describe a future of "data microservices" with centralized metadata registries and standardized high-speed data access.

## Key Quotes

> "If you think about open source software as a public good in the sense that we have clean water and roads and sewers, maybe we should take the same approach to essentially individuals, companies and governments funding development of open source infrastructure. It's not such a crazy idea."

> "The two things I'm most interested in is sharing data without having to copy or serialize and sharing code, so being able to take an algorithm that somebody else wrote and being able to run it on my data without having to rewrite the algorithm."

> "If you're a Python programmer, you don't want to be running one Python function call for every row in a billion row dataset, that's going to be ridiculously slow."

> "Open source communities are fragmented by their nature. It's sort of an anarchy. There's no central government making decisions. It's very infrequent that you see developers from different communities come together."

> "I wanted to create the environment that would enable collaboration between the data science world and the database systems world. Where historically, they've been completely separate and there's a lot of really great technology that's in the database world, but very little of that technology has made its way into data science."

> "Our goal is to kind of deconstruct the analytic database to break things into libraries that have public APIs that are reusable and you can pick and choose the components that you want to use to build a data processing system."

> "We don't want to be prescribing the API and the front end, the way that you interact with the data. So if you want it to be SQL, you can make it SQL. If you want it to be pandas-like or R-like, you can create an API that works like data frames in those languages."

> "We really envision a future of data microservices, where you have a centralized metadata registry, and you can see all the data services available, use the exact same client interface to access all of them, and push and pull datasets at high speed."

## Transcript

**Wes McKinney:** I know it's early, at least for me, because I have nine hours of jet lag, but I hope to not bore you to death with this talk and give you some context like why I came to care so much about this project and maybe some ways that you might think about getting involved in infrastructure technology for data science and data engineering or ways that you can support and take advantage of this work.

So a little over ten years I started writing some Python code for myself to wrangle data. I didn't really know much about open source or expected to turn into a very big project, and so the last years have been really interesting. I spent a lot of my time from 2011 and 2012 really focused on building the pandas project, but about five years ago I handed over the reins of the project to the rest of the maintainers, people whose names you may or may not have heard of, people like Jeff Reback and Joris Vanden Bosch, Tom Augsburger, Philip Cloud, folks who've been really building the project out and making the community healthy over the last five years.

But I got busy with some other projects that are closely related to pandas, but not exactly pandas itself. Probably a lot of you have a copy of my, or some of you have a copy of my book, which is almost in its - almost came out six years ago, or six years ago in October.

So as Pete was mentioning, funding open source projects is difficult, and I think lately there's a general feeling in the air around funding maintenance of large established projects. So in the wake of, you know, really major security vulnerabilities and important software, like maybe, you know, a lot of you probably heard about Heartbleed, like it was a major bug in OpenSSL, and after people dug in, they're like, well, who maintains OpenSSL? And it turns out that OpenSSL only had one full-time maintainer, and the other maintainers were working part-time and were all kind of stressed out that, you know, they could have security bugs, but they just don't have enough funding to support the project.

A lot of people have been working on how can we get corporate sponsorship to maintain really critical software, so if you think about open source software as a public good in the sense that, you know, we have clean water and roads and, you know, sewers, like maybe we should take the same approach to, you know, essentially individuals, companies and governments funding development of open source infrastructure. It's not such a crazy idea.

But raising money to - and having money to build brand-new projects is even more difficult because you have to convince people that you can actually build the project and that it will be valuable.

And so I've been building something new the last few years, and so earlier this year I created an organization called Ursa Labs to focus on building the Arrow project with the focus on creating shared infrastructure for data science to accelerate data science and data engineering in Python, R, and kind of across the spectrum of tools that data scientists use.

So to do this, I partnered with RStudio and Hadley Wickham because I wanted the, you know, I guess kind of in the data science world, we're two of the most well-known people in that ecosystem, and I wanted to have the R community, you know, bought in and committed to working together to build, you know, software that we can all use in both programming languages.

But it's certainly not limited to just Python and R, but that's a pretty good place to start. I had been working at Two Sigma for the last couple of years, so they're a financial institution in New York City. They're continuing to kind of sponsor the project, so RStudio is committed to resources, and I expect to be adding some additional logos to this page over the next six months.

So if your company or any companies that you work with would be interested in sponsoring this work, we'd be happy to hear from you. But our goal with what the money that we're raising is to hire people and have them work full-time doing 100% open-source development, so not doing consulting, not building products or any of those things which tend to distract from the core open-source development and doing a good job of building high-quality production software.

So one problem that I've encountered over the years is the fact that data systems are highly fragmented when you look under the hood at the tools that they use to, you know, to implement themselves. So things like how is data stored? How is data deserialized? How is data represented in memory? Who wrote the algorithms to compute things on that data and memory?

And so a lot of systems are black boxes that are very vertically integrated, so pandas is one such system that's highly vertically integrated where we wrote our own CSV parser, our own way to read data from HDF5 files, reading data from databases, we have our own kind of query engine, pandas is kind of its own kind of in-memory database kind of thing. We have our own front end, which - and the front end, the Python code that you write is tightly coupled to the back end.

But it's a complicated thing, and, you know, one of the issues is that we don't have a lot of open standards, so open standards help with making things simpler by using common technology that makes systems interoperable and makes things less fragmented.

And so for me, the two things I'm most interested in is sharing data without having to copy or serialize and sharing code, so being able to take an algorithm that somebody else wrote and being able to run it on my data without having to rewrite the algorithm, and those two things historically are very difficult.

So we have lots of open standards already, you know, if you're in the big data world, you might be familiar with some of the storage formats like Parquet and ORC that have come out of the Hadoop ecosystem, there's things like HDF5 for storing general numeric datasets, we have general structured data serialization tools for RPC, so Avro came out of the Hadoop world, we also have protocol buffers and Thrift, which is - I don't know the history, but I think Thrift was created by ex-Googlers who wanted to have an open source version of protocol buffers and then Google open source protocol buffers, so now we just have lots of incompatible tools.

Some people think of CSV as being an open standard, but it's not, because there's no standard way of - I guess there is, there are some standards for writing down schemas for CSVs, but the amount of variety and different options in parsing CSVs makes them a poor choice for warehousing data.

So given that we have lots of fairly standardized accepted ways of serializing binary data, we don't have a lot of standards for in-memory data, so if you want to share algorithms that execute against in-memory data, you need to have open standards for in-memory.

The main one that we have is the multidimensional array model, which came out of basically APL and Fortran, so when folks built MATLAB and they built NumPy, they already had a memory model for representing multidimensional arrays, like, okay, here's a data pointer, here's shape and strides to instruct the code how to iterate over, interpret a block of memory as being a multidimensional array.

But when you have a standard memory model, that means that two processes can move data through shared memory without any conversions or copying. You can send data through a socket, receive it on the other side without performing any additional conversions outside of the socket send and receive. If somebody writes an algorithm, you can invoke that algorithm in a different context, so that's how we've been able to reuse, you know, decades' worth of linear algebra code written in the 70s and 80s, a lot of it still in Fortran.

If you're in the Java world, you can, you know, you can create bindings to C and C++ code and invoke, assuming all the data is in off-heap memory, you can invoke algorithms that are written in C and C++ on data that was generated by the JVM, so you get lots of good benefits when you standardize in memory.

But when you go beyond multidimensional arrays to, you know, tables and data frames, essentially, so if you're a data scientist, probably use data frames, I guess everything has data frames now. Spark has data frames, you know, pandas has data frames, R has data frames, Julia, you know, every language has a data frame, but when you look under the hood of what's inside the data frame, in almost every case, the internals are different and not compatible.

And this creates a lot of problems, so in the context of a database system, suppose that you want to extend a database system with some custom code that is written in Python or written in R. So because the in-memory format of the database, the way it represents data in its runtime is not public, so there's no public API for the internal data, what they do is they define an intermediate API for writing extensions and then serialize from their internal representation to that intermediate representation and expose that to you as a public API.

That API is often row-based, and so if you're a Python programmer, you don't want to be running one Python function call for every row in a billion row dataset, that's going to be ridiculously slow.

So you know, I arrived in the big data world at the end of 2014 after having a startup. I was at Cloudera. I looked around and said, we've got to make Python and R first class citizens in the big data world. How do we do that? And you know, my feeling after assessing the ecosystem was, well, we have to solve this problem so that we can make data available to the data science world without having to go through a very narrow kind of serialization pipe.

So there's a number of reasons why I think that things are so fragmented and there has not been a prior effort to create standardization. So one thing is just open source communities are fragmented by their nature. It's sort of an anarchy. There's no central government making decisions. It's very infrequent that you see developers from different communities come together.

So I've started spending more time with the R community. The R community historically has not spent much time talking to other communities, the same with Python and others. So you can't really blame communities for focusing on their own needs and developing solutions for the problems that are right in front of them.

I also think that some of the fragmentation is caused because people want to make the front end user API for these projects. They want to make it work exactly in a particular way. So even within R, there's the tidyverse and there's data.table and there's base R. And part of the reason why there's so many different data frame APIs in R is because the user experience of using those libraries is completely different, even though the underlying data is just an R data frame.

And in Python, the pandas API is also a lot different from the R data frame API. But there's a lot of details of the way that pandas is implemented that are visible in the public API. So if we wanted to change, make major changes to the internals, that would cause API breaks that would upset users. And we've just made the decision to try not to upset users very much, although I don't know that we've succeeded at all times.

So kind of in response to this, I spent a lot of 2015 going around the open source big data world. It was a bit Bay Area centric because that's where I was physically at the time and where I could meet with people in person and see if they were interested in working on this effort.

And I was able to assemble a collection of about 25 people who are leaders in different open source data science and big data projects to commit to working together to creating an open standard for in-memory data frames that's column oriented and suitable for analytic computing.

And for me, what's really exciting about this, and I'm going to tell you more about in the next 20 minutes or so, is that I wanted to create the environment that would enable collaboration between the data science world and the database systems world. Where historically, they've been completely separate and there's a lot of really great technology that's in the database world, but very little of that technology has made its way into data science. The only way that data scientists get access to that is by sending SQL queries into a database. And so I would like to see that change.

So to recap our goal, the goal is to go from having non-portable data formats to portable data formats. So that's the Arrow format, which I'm going to tell you more about. And my objective is to create libraries, high quality libraries, that handle the kinds of problems that you solve with pandas and with equivalent libraries and other languages that are reusable and can be ported and built and you can use via binding layers in many different programming languages.

So if you think about this in the context of analytic databases, so traditionally, a database system or a data science library is vertically integrated. So your front end is usually SQL queries. And when the SQL query is parsed, the database creates a logical query plan. It looks at statistics and metadata about how the data is stored and what we know about the data. It creates a physical query plan. That query plan is executed by a computation engine, which might be single node. It might be distributed. That computation executes against data that's in memory, which may be deserialized from disk on the fly or it may be cached in memory. And so that's where the in-memory format comes in. And then we have IO subsystems for interacting with file systems, for reading and writing file formats.

But usually all of this is not visible to external users, so you only see the front end and the internals are deliberately made kind of part of the black box. And so if you wanted to extract code and reuse it, it would be very, very difficult.

So our goal is to kind of deconstruct the analytic database to break things into libraries that have public APIs that are reusable and you can pick and choose the components that you want to use to build a data processing system. So if you just want a fast data access and deserialization layer, you can use that. If you want a way to share memory between processes, like deal with large data sets on disk, you can just use that. If you just want to use the library of algorithms and the memory format, it's sort of up to you.

But the big picture is that we don't want to be prescribing the API and the front end, the way that you interact with the data. So if you want it to be SQL, you can make it SQL. If you want it to be pandas-like or R-like, you can create an API that works like data frames in those languages.

So deconstructed database, deconstructed soup, that's sort of our goal.

So the project, the use cases that we're concerned with, or at least that I'm concerned with, are these three areas. So the first is being able to have very fast access to data, so being able to read and write data in all of the ways that it is stored. So that's dealing with storage formats, like columnar Parquet files. It's being able to read and write data as efficiently as possible to database systems. Because we can't just take all the data out of wherever it's stored and say, okay, we've got a new data format. It's not even a storage format, it's an in-memory format.

So we can't move the data, but we need to get access to the data as quickly as possible from wherever it's stored. If you have data that is in arrow format, we want to be able to move around datasets between processes and nodes as efficiently as possible. So the two areas that we're focused on there are shared memory and RPC, so socket-based communication.

And then it would be kind of useless if you couldn't actually do anything with the data as is, if you just needed to convert it to some other representation all the time. So we're also developing computational libraries that evaluate natively against the arrow format.

So let me see, I need to move. I added some slides and then I, forgive me.

So the arrow format itself is an in-memory table-like format for representing data frames or representing a fragment of a table, like a chunk of a table inside a SQL engine. It's arranged, the way that the data is arranged in memory is optimized for analytical processing. So you wouldn't want to use it to build a mutable row store necessarily, but if you were building a columnar analytic database engine, that's what it's designed for.

So you can represent both flat and nested data, and it works well on both CPUs and GPUs, and we have people actively using the format on both types of hardware.

So when you perform analytic operations, you only, because it's columnar, you only access the data that is relevant for your algorithms, and the access patterns to scan columns are efficient for the processor.

So we've had a couple of things built in the last couple of years to help demonstrate the benefits of using, having more efficient data interchange and data transport.

So in Spark 2.3, Spark 2.3 ships with optional arrow support, which you can use in PySpark, and the idea is that, and I'll go back to the results here, is that Spark SQL has its own internal representation of tabular data inside Spark SQL, Spark DataFrames, depending on what part of Spark you're using, they could either be Spark DataFrames or just general Spark SQL.

But Spark SQL does, its data is not resident in shared memory, so you can't do true zero-copy sharing between processes, so if you wanted to make a large data set available to a Python process, maybe this is changing, but at least as far as, you know, with my up-to-date knowledge, I don't think it's possible.

But the way that it works is that Spark SQL serializes data to the arrow columnar format that is streamed to the PySpark worker process, it's converted again to pandas, but then we built a layer to evaluate native pandas code against data, like chunks of data that are coming from Spark, and then this is streamed back to Spark via the arrow format.

And you might say to yourself, well this is crazy, like we have four serialization steps, like we have to convert from Spark's internal format to arrow format, then to pandas, then run some pandas code, then convert back to arrow, you know, to arrow and then from arrow, so we have four serialization steps, so that can't possibly be efficient.

But you have to remember, like where did we start, and so there was already a multi-step serialization process that was happening, but that serialization format was particular to the Spark PySpark bridge, and even with all of this serialization going on, the efficiency, you know, with the efficiency of the arrow format, these are some sample user-defined functions that are pandas-based, you know, in some cases we're able to get more than a 100x speedup in evaluating custom Python code.

So if you see here on the left, suppose that you wanted to run, you know, compute the cumulative probability function for a normal distribution inside Spark SQL, you can write that using SciPy stats, and when you're using Python, all of these functions that you have for analytics are supposed to be, they're intended to be invoked on NumPy arrays, and so you can use them on pandas objects as well, but if you were to, so the ideal mode is to invoke these functions on a thousand rows, on a thousand values at a time, or a million or a billion values at a time, not to run them once for every row in a data set.

So even though we have all of this serialization work to do to move the data to and from Python, the efficiency gains are coming largely from changing the execution model from row-based to vector-based, and so batching the user-defined function evaluations.

So, I've been talking a lot, I know, but so the key point is that we really envision a future of data microservices, where you have a centralized metadata registry, and you can see all the data services available, use the exact same client interface to access all of them, and push and pull datasets at high speed.

But right now it's difficult because you use different clients to access data, you have to think about how the data is stored, what library to use, what settings, how to parse the dates, missing data, all of this complexity. As a data scientist, I'm overwhelmed with all of these things just to read a dataset, perform some analytics, and use TensorFlow.

I would like to simplify that as much as possible. Just request a dataset, get it as fast as possible, not worry about the details, and get on with my work.

So hopefully that sounds good, but to build technology like this that makes things less fragmented requires a great deal of work. The next few years are going to be pretty impactful in terms of getting the software deployed and making things faster and simpler.

Thanks for listening.