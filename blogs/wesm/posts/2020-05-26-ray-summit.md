---
title: "Scalable Python We Can Afford"
summary: "Keynote at Ray Summit"
date: 2020-05-26T00:00:00
tags: ["keynote", "transcript"]
slug: ray-summit
word_count: 2853
source_file: transcripts/2020-05-26-ray-summit.md
content_type: transcript
event: "Ray Summit"
video_url: "https://www.youtube.com/watch?v=TflnJKLRj-M"
---

{{< video https://www.youtube.com/watch?v=TflnJKLRj-M >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this keynote, I discuss the computational challenges involved in scaling Python for distributed computing. I trace my journey from building pandas as a personal toolkit to the broader ecosystem challenges we face today.

I explain that pandas was designed as a "small data" tool, and I was willing to write slow, inefficient code early on if it meant getting something usable out the door. This led to well-known performance and memory problems - I often recommend having 10 times as much RAM as data to avoid running out of memory.

I express concern about approaches being taken to scale pandas for big data. While imperfect scalability is better than none, I reference the 2015 paper "Scalability! But at What COST?" which found that many big data systems require impressive configurations just to outperform a well-implemented single-threaded algorithm. The quote I cite: "You can have a second computer once you've shown you know how to use the first one."

I argue that to reduce the cost of scalability, we need to: reduce the cost of data access, improve single-node performance, and reduce communication overhead. Data science tools like pandas have lagged behind advances in computing hardware, and it's not enough to simply run pandas on a cluster.

I also note that many big data systems weren't designed with Python in mind - Python support was bolted on later. In Hadoop's early days, you could use the streaming interface to write jobs in Python, but it was much slower than Java because it didn't allow vectorized NumPy/SciPy operations.

By 2014, I believed the Python ecosystem would get stuck without a coordinated effort to build a modern computing foundation. To solve the language interoperability problem, we formed the Apache Arrow project in early 2016 with the mission of creating language-independent standards for high-performance in-memory analytics.

I point to NVIDIA's RAPIDS as an example - using Arrow as its foundation, RAPIDS achieved nearly 20x improvement on big data benchmarks with one-third the power consumption. As Paul Dix of InfluxData put it: "When you use Arrow, your data is your API."

I conclude that with Arrow, we have an opportunity to build a modern computing foundation that works across programming languages, providing efficient building blocks for distributed computing libraries like Ray and Dask, and ending the pointless language wars over CSV parsing and Parquet file performance.

## Key Quotes

> "Python just gets out of my way and lets me get my work done."

> "I was willing to write slow, inefficient code if it meant getting something usable out the door that unblocked people's use cases."

> "I often recommend to people that they have 10 times as much RAM as they have data to avoid running out of memory."

> "Pandas was not designed like a database and was not built by individuals with a background in database systems."

> "You can have a second computer once you've shown you know how to use the first one."

> "Along with making it easier to do distributed computing in Python, we must also improve the single-node computational foundation that projects like Dask and Ray are built on. It is not enough to simply use these tools to run pandas on a cluster of machines."

> "Why should choosing Python be a trade-off? That doesn't seem right to me."

> "When you use Arrow, your data is your API."

> "Why should reading a CSV file or crunching a directory of Parquet files perform any differently in Python versus R? It doesn't have to be like that."

## Transcript

**Wes McKinney:** Thank you so much to the Ray community, the Linux Foundation, and Anyscale for giving me the opportunity to speak to you today.

It has been almost 13 years since I took my first steps as a Python programmer and started building a personal data analysis toolkit that would evolve into the Python pandas project. Since then, I've been involved in a number of other projects which superficially may seem loosely related to each other, but which are all part of a larger technology vision about empowering data science practitioners, which I plan to continue to pursue well into the future.

Over the last decade, with the help of an amazing group of maintainers and contributors, pandas has become one of the world's most widely used data tools. I never could have imagined that such a thing was possible when I was 22 years old and fresh out of college, but it has instilled in me a passion for creating open source software to empower people to work better, more effectively with data.

One of the reasons that I fell in love with Python is the feeling of productivity that it gave me. The Python blogger John D. Cook put it this way: "Python just gets out of my way and lets me get my work done." And that's how I've always felt about the language.

The first few years of pandas development for me were really about going from zero to one. That is, can we make Python a viable general purpose data analysis language? And so I was willing to write slow, inefficient code if it meant getting something usable out the door that unblocked people's use cases.

So here you see a picture of me giving the very first public demo of pandas in 2010 at PyCon in Atlanta, ten years ago. In my SciPy conference paper about pandas, I wrote: "We believe that in the coming years there will be a great opportunity to attract users in need of statistical data analysis tools to Python who might have previously chosen R, MATLAB, or another research environment. By designing robust, easy-to-use data structures that cohere with the rest of the scientific Python stack, we can make Python a compelling choice for data analysis applications."

It might seem obvious to everyone in retrospect, but it was an enormous community effort to get to where we are today, and our work is not yet done.

Pandas, of course, was designed first and foremost as a small data tool - which is to say, data that fits on your laptop. While I spent a lot of time optimizing code in the early days, pandas only needed to be "fast enough" or handle "big enough" data. After the scramble to make Python usable for data science, we were left with - let's call it - a healthy accumulation of technical debt.

As a result, pandas has some well-known and well-advertised performance and memory use problems. For example, I often recommend to people that they have 10 times as much RAM as they have data to avoid running out of memory, which often surprises people. But if you've ever read a 10 gigabyte CSV file on your laptop and managed to get it to load into memory, you know exactly what I'm talking about. But the project has become wildly successful anyway, perhaps in part because most of its users' data isn't all that big.

About seven years ago at PyData NYC, I gave a talk provocatively titled "10 Things I Hate About pandas." It was a partial explanation of some of the social and technical reasons why pandas is not as fast or as efficient as it could be. The talk could be summarized essentially that pandas was not designed like a database and was not built by individuals - namely people like myself - with a background in database systems.

There are various shortcomings in pandas that you may be aware of. For example, most of its algorithms are single-threaded and don't make extensive use of modern CPU features like SIMD. Another problem is that pandas requires all of its data to be RAM resident, so that means that when you want to process a data set, you have to load the entire data set into your computer's RAM before it can be processed. And so if your data doesn't fit into memory, you can't do the work.

Another issue is the way that pandas represents non-numeric data, especially strings, is not very efficient - though some work is currently underway to fix that. And one of the reasons it's been difficult to fix some of the issues with non-numeric data is because pandas was designed on purpose with tight coupling to NumPy, which is very focused on numeric data.

With this said, something that has been concerning to me in recent years is the approaches that are being taken to scale pandas or to make pandas work on big data. And so I'm going to be talking about this for much of the rest of the talk.

Indeed, there have been great advances in making distributed computing easier in Python. We've made just about everything else easy in Python, so why should programming a cluster be any different? It's important to note that imperfect scalability is better than no scalability, so if we can scale pandas with the tools that we have, then we absolutely should.

Before getting into the specifics of the concerns that I have, I want to take a step back and emphasize how big data systems work. Since only so much data can be processed on a single machine or a single node in a reasonable amount of time, we have to break up large tasks into smaller tasks that can be performed in parallel across a cluster of machines.

When we turn a single-node problem into a multi-node problem, we don't necessarily obtain one-to-one or linear scalability. In other words, 100 machines won't be able to process 100 units of data in the same amount of time that a single machine can process one unit of data. So if you have 100 machines, you might only be able to process 5 or 10 or 20 times as much data in the same amount of time. Since more computing time usually means more money nowadays, we need to do what we can to reduce the cost - the amount of money we have to spend for each gigabyte, each terabyte, each petabyte that we process.

So perfect or one-to-one scalability, of course, is impossible because distributed computing introduces overhead that isn't present when you're working on a single node. For example, the distributed versions of many algorithms like joins or sorts need to shuffle data between nodes, which has a cost both in data serialization and network transfer. And there's many other sources of overhead in distributed systems.

I'm far from the first person to express concern about this. In 2015, a group of distributed systems researchers at Microsoft Research published a somewhat incendiary paper called "Scalability! But at What COST?" The way that they introduce the paper, they say that the published work on big data systems details their systems' impressive scalability, but few directly evaluate their absolute performance against reasonable benchmarks. To what degree are these systems truly improving performance as opposed to parallelizing overheads that they themselves introduce?

One of the things that they introduce in the paper is an attempt to measure the overhead that a distributed system introduces in order to obtain scalability. So they call this COST, which is the Configuration that Outperforms a Single Thread. They then proceeded to attempt to measure the price of scalability - the scalability cost - in a number of different big data systems. And what they found is that in many cases, it takes quite impressive configurations to outperform a well-implemented single-threaded implementation of many algorithms.

So Paul Barham, who used to be at Microsoft Research and is now at Google, said this quote which is in this paper: "You can have a second computer once you've shown you know how to use the first one."

If we want to reduce the cost of scalability, we have to work on a few different fronts. First of all, maybe this is obvious, but we have to reduce the cost of accessing data. If you can load data into your process faster, then you can process it faster, so your whole application becomes faster and more efficient. Another thing we have to do - because big data problems are composed of many small data problems - we have to improve single-node performance. So if we have algorithms that are not as efficient as they could be, or are not taking advantage as well as they could be of our hardware, we need to do work to get the most out of the hardware that we have. Another thing we need to do is reducing communication overhead, and so in particular that means data serialization and network transfer related issues. So if we can spend fewer CPU cycles converting between data formats in a distributed system, that makes the system run faster.

I bring this up because data science tools like pandas, from a purely computational perspective, have lagged pretty far behind advances in computing hardware in the last decade. Along with making it easier to do distributed computing in Python, we must also improve the single-node computational foundation that projects like Dask and Ray are built on. It is not enough to simply use these tools to run pandas on a cluster of machines.

Another problem we face is that it isn't always practical to write everything in Python. Many of what we think of as today's big data systems weren't really designed with Python in mind, where Python support was bolted on later in life due to popular demand.

Going back in time to the early days of Hadoop, the native way to write MapReduce jobs was to write them in Java. But you could use the Hadoop Streaming interface to write jobs in Python, Ruby, or just about any programming language. This interface didn't even allow you to use Python's vectorized scientific computing libraries like NumPy and SciPy. But people used it anyway, even though it was much slower than Java, because they preferred the productivity benefits that you get by being able to program in a dynamic language like Python or Ruby.

This raises the question: why should choosing Python be a trade-off? That doesn't seem right to me. We might be willing to pay a little bit of extra computing cost to use Python, but it shouldn't be an unacceptable trade-off that causes the price of using Python to be extremely high.

By 2014, I had come to believe that the Python ecosystem would get effectively stuck without a coordinated effort to build a more modern computing foundation for data frame type processing. And in order to solve the language interoperability problem, we would have to build alliances outside of the Python community.

Luckily for me, there were a lot of open source developers who had faced similar computational problems, so we decided to join forces and do something about it. Together we formed the Apache Arrow project in early 2016 with the mission of creating language-independent standards and computing tools for high-performance in-memory analytics and data transport.

Now five years later, Arrow has become the new gold standard for columnar data transport, data access, and in-memory query processing, with massive adoption across the data systems community.

As one example of the successes we've seen, NVIDIA has used Arrow as the foundation for the RAPIDS GPU analytics platform, and they were able to improve on industry-standard big data analytics benchmarks by nearly 20 times measured in time, but with one-third the amount of power consumption. That's on the order of a 60 times improvement in compute efficiency.

For me, one of the things that's so exciting about Arrow is that our computational systems can become less coupled to the programming language that we are using. So Arrow is Arrow whether you're using Python, Java, JavaScript, Rust, or any other programming language - as long as you have a library that supports the Arrow data format.

Paul Dix, who is one of the founders of InfluxData, put it simply: "When you use Arrow, your data is your API." And I find this concept to be really compelling.

With Arrow now in context, we have an amazing opportunity right now to work together - even across language borders - to build a modern computing foundation to power our data science tools that can even be used from any programming language. In doing so, we will provide vastly more efficient computational building blocks that distributed computing libraries like Ray and Dask can use.

As part of this effort, we can also end the pointless language wars. Why should reading a CSV file or crunching a directory of Parquet files perform any differently in Python versus R? It doesn't have to be like that. We can all work together to create high-quality open source Arrow-based computing libraries that we can all use.

I, for one, am optimistic about the future of data science tools and hope to work with you all to make this vision a reality as soon as we can. Thanks again.