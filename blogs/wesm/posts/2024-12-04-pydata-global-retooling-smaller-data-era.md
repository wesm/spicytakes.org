---
title: "Retooling for a Smaller Data Era"
summary: "Talk at PyData Global 2024"
date: 2024-12-04T00:00:00
tags: ["talk", "transcript"]
slug: pydata-global-retooling-smaller-data-era
word_count: 3742
source_file: transcripts/2024-12-04-pydata-global-retooling-smaller-data-era.md
content_type: transcript
event: "PyData Global 2024"
video_url: "https://www.youtube.com/watch?v=w4aYrav8-zE"
---

{{< video https://www.youtube.com/watch?v=w4aYrav8-zE >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I examine how the definition of "big data" has changed over the past 20 years. What once required distributed clusters can now fit on modern laptops thanks to improvements in CPU cores, SSD performance, and networking bandwidth. I discuss the "scalability at what cost" problem highlighted in a 2015 paper, arguing that many big data systems introduced significant overhead while achieving parallelization. I advocate for composable, modular data systems built on open standards like Apache Arrow, open protocols like Arrow Flight, and interchangeable execution engines like DuckDB and Polars. I introduce projects like Ibis (a Python dataframe API that transpiles to 20+ backends), Narwhals, and the emerging vision of a multi-engine data stack where users can choose the right execution engine for their data size.

## Key Quotes

> "What used to be big data can now fit on your laptop."

> "In 2004, all servers and data centers had a single processor core."

> "That in a single server is bigger than many of the big distributed clusters of machines that Google folks were talking about in their MapReduce paper 20 years ago."

> "While many of the big data systems had achieved scalability and the ability to process large data sets, they also introduced a lot of overhead that makes the cost for processing each terabyte or each gigabyte significantly higher than what you could do on smaller scale data sets on a single machine."

> "These systems have achieved impressive scalability, but to what extent are they truly improving performance as opposed to parallelizing the overhead that they introduce into the process."

> "Wouldn't it be amazing if we had a powerful computational runtime that could be shared across programming languages so that it isn't all the Python developers working for themselves to rebuild everything just for Python."

> "DuckDB... has pretty much shut down the cottage industry of people building their own database and data processing engines."

> "Why be locked into a single execution engine, along with a full stack of tools, including storage, and query interface."

## Transcript

**Host:** Hi, everyone. And welcome to PyData Global. We're excited to have you join us. Please feel free to use the chat to connect with fellow attendees and share your thoughts during the session. If you have any questions, please post them in the Q&A tab, and we'll address them at the end of the session. Now, it is my absolute pleasure to introduce the speaker, Wes McKinney. And let's provide him with a warm welcome. Wes McKinney is an open source software developer and entrepreneur focusing on data processing in tools. So, Wes, take it away.

*[Technical difficulties with audio resolved]*

**Wes McKinney:** All right. Is this thing working? It's working. I give talks all the time, and so I've never had this happen. So I don't know what's going on. I've never used AirMeet before, so I've got to kind of blame the platform. All right.

Let me try to get back into my talk here. It's not my day. One second. All right. Can everyone see and hear me? All right.

So with that small, small detour, I'll give a slightly shorter version of my talk, which let's figure out how to control this. All right.

So this talk is about work that's been done in open source ecosystem over the last 10 years, which has had a lot of impact on the PyData ecosystem, but is more broadly about data science, data processing, database, and data science systems and how they work together.

I assume most people in the audience are familiar with me from my work on the pandas project and my book Python for Data Analysis. But I've also, in recent years, have been shifting my effort to some other projects like Apache Arrow, Apache Parquet, as well as the Ibis project. And we'll talk a little bit about those in this talk.

My present day job is that I'm a principal architect at Posit, formerly known as RStudio, data science platform company. I also co-founded Voltron Data, and I'm a part-time investor through my fund, Composed Adventures.

A lot of what I've been involved with at Posit, if you're interested, is doing some work on the new Positron data science IDE. It is a brand new polyglot IDE experience that's been built on top of the open source VS Code platform. We have created the classic four-pane data science layout with the code editor, console, variables pane, and plots pane. I've been building a fast, scalable, interactive data explorer for looking at data frames and database tables. So you can get that through the public betas of the Positron IDE. So check it out.

One of the things that we encounter over and over is that data size is relative. And what we think of as big data or small data has changed a lot over the last 20 years. So what used to be big data can now fit on your laptop.

So we used to think that a gigabyte or 100 gigabytes or a terabyte of data was big data. But now a terabyte of data may compress down to a set of parquet files that are not that big and can easily fit on your laptop and be queried very effectively with many of the tools that we have today.

And so if you go back and think about the original big data paper from Google, the MapReduce paper from 2004, I don't know if anybody knows how many processing cores, CPU cores were standard in top of the line servers in 2004. So the answer is one.

So in 2004, all servers and data centers had a single processor core. So maybe they had hyper-threading in that era so you could run two threads simultaneously. But the processing capabilities 20 years ago were much more modest than they are today.

And if you look at the servers that you can buy and rent now in AWS or in other cloud services, you can get servers that have 96 physical cores. And so if you have hyper-threading, that's 192 concurrent threads of processing on a single CPU socket.

And servers can have two of these or even sometimes more than two sockets. And so you could have a dual socket server in the cloud with 384 simultaneous threads of processing. And so that in a single server is bigger than many of the big distributed clusters of machines that Google folks were talking about in their MapReduce paper 20 years ago. So this is a massive change.

We've also seen similar evolution in hard disk drive performance. So 20 years ago, everything was spinning rust, hard disk drives with high seek latency. We moved on to solid state drives and got massive improvement in seek performance, much higher read and write bandwidth. And then more recently, we've moved on to non-volatile memory and NVMe, which has brought the read and write bandwidth starting to approach 10 gigabytes a second.

And I expect that disk will continue to get faster and faster. And we've seen similar trends in networking performance, networking performance as well. So this chart shows, you know, basically state of the art networking performance over time, it's logarithmic scale. And so we've gone from, you know, gigabit Ethernet to, you know, terabit Ethernet in less than 20 years, which is, which is pretty, pretty impressive.

For a long time, people were talking about how Moore's law is dead. So Moore's law is the idea that every 18 months, the number of the transistor density in CPUs doubles, and effectively, you know, the processing capability of CPUs goes up by a factor of two.

And that started to plateau in CPUs at some point, but we've continued to see core counts go up, especially in GPUs and specialized, specialized silicon, which has enabled us to continue to have that exponential increase in processing capabilities.

But one of the challenges in thinking about the development of big data systems, compared with our nice, friendly Python tools, PyData tools, is that the people thought about the ergonomics, the usability, the user experience of big data systems in a very different way, whereas in Python, we really value our library ergonomics, the code that we write that it should be very easy to read, that it should be easy to type very fluent and natural.

And so you know, that that emphasis on developer productivity, user user productivity was less comparatively less important in the big data ecosystem where it was really all about how do we how do we make it feasible to process terabytes and petabytes of data.

And so then not just the the usability and the ergonomics, but also the overhead and the cost of processing data at scale was also often an afterthought. And so this was highlighted in this famous paper from 2015 by some former Microsoft Research developers who've gone on to have, you know, illustrious careers working on TensorFlow and materialize and other projects.

But they pointed out that while many of the big data systems had achieved scalability and the ability to process large data sets, they also introduced a lot of overhead that makes the cost for processing each terabyte or each gigabyte significantly higher than what you could do on smaller scale data sets on a single machine.

So the way that they described it in the paper is these systems have achieved impressive scalability, but to what extent are they truly improving performance as opposed to parallelizing the overhead that they introduce into the process.

And so to make, you know, to make this, what we're talking about a little bit more complete is think about a SQL query that that aggregates a very large table, maybe we're grouping by one column computing the average of another column, we may very well write similar code in pandas or similar code in R. And these are all, you know, basically doing the same thing.

But under the hood, the architecture of the systems that evaluates this code, depending on the scale of the data and the underlying execution engine is very different. So in pandas and R, we're loading the whole data set into memory, whereas in the SQL engine, it might be some distributed map reduce job that's running on a big cluster of machines if you have a massive data set that can't possibly fit on a single node.

And so this has led to this sort of hierarchy of needs when thinking about building these systems, when looking at things from the big data perspective, where the ability to scale to say I can process a terabyte of data or 10 terabytes, or a petabyte of data, that starts out as being the primary concern.

And only after that point, can you begin to think about, can you begin to think about, okay, how do we make it faster, just wall clock time, we want it to take less time from start to finish, to complete the job.

After you've made it fast, you can start thinking about efficiency, both from a resource, like the amount of hardware you use, but also, increasingly, we're beginning to think about processing efficiency in terms of power utilization. And so how many kilowatt hours, and thus how much money does it cost to execute a particular workload.

And when you're paying for compute time, by the core hour in the cloud, this starts to become a big deal, because the queries that you're running are converting into a bill that you're getting from AWS, or from Google Cloud.

And then beyond these performance and efficiency considerations, as we start building more heterogeneous data systems that are doing raw data processing, feature engineering, as well as AI training, and model serving, we have a system, a set of components that is solving many different problems that can't be achieved within a single system.

And so how those systems fit together, like how they are composed with each other, and how efficient is composing them together, is another concern, which has become brought more to the forefront in recent years, especially with the growth and adoption of AI.

And so when we think about these composable data systems, one of the things that enables us to plug the systems together, and do it in an efficient way, is to develop open standards and protocols for connectivity at the data level, as well as transmitting an understanding of what you want each system to do.

And so, you know, we're beginning to design around these concept of modularity, reuse and interoperability, so that if we adopt an open standard or protocol for plugging systems together, we can greatly reduce the amount of overhead that is present in distributed systems that make use of different processing components.

And if in doing so, we can create a virtuous cycle with the different open source projects that can then work better together to build in more efficient, heterogeneous distributed systems.

And so a lot of this work is broken down into a number of different areas that are common in the world of data processing engines and database systems from the processing engines themselves to the protocols which connect systems together.

Those are generally data protocols like Arrow, but also, there's new things like open lineage, which provides an open standard for metadata. So you can talk about what the system is doing with the data in a standard way. So you can reason about schemas and transformations across different processing components.

Increasingly, how we store our data and doing so in an open standard way has become an important area, we've seen significant investment there and projects, open source projects like iceberg. And in file formats like parquet to make that easier for people.

But this is for me, this is a problem that I've been thinking about for many years, going back to 2015, the same year that the scalability but at what cost paper came out, you can see a lot of people were thinking about this problem in this era, because we had recognized that there was a problem, but we didn't have a lot of great solutions to it.

And so the idea is that we want to facilitate decoupling the query kind of user layer, the programming layer, the code that you write, how you express what you want the systems to do, you want to decouple that from the underlying storage and the execution so that we can enable the respective developers of each layer of the stack to really hyper specialize and make the different pieces as powerful and efficient and composable as possible.

And so when you do this, you're enabling components to be shared across different types of systems, you enable interchangeability. So you can swap out an execution engine or you bring in a new query interface. And we've made significant progress toward this. And so that's been really exciting to see happen and to be a part of.

And the way that I described the problem to the PyData and also the broader data science community in 2017. This was at JupyterCon in 2017 was, you know, wouldn't it be amazing if we had a powerful computational runtime that could be shared across programming languages so that it isn't all the Python developers working for themselves to rebuild everything just for Python and the same with the R ecosystem and the same with the Julia ecosystem, but that we could have a set of shared libraries and components that could be portably reused in a portable way across programming languages so that the programming language becomes an interchangeable front end for the computational backends.

And so we can make improvements to our computational systems and reap the benefits everywhere, not just in Python or not just in R or another language.

So one of the things that we've built to make this easier is Apache Arrow, which has provided a language independent fast interchange layer for data for tabular data, data frames, effectively database tables.

And another component which has helped lead the way and thinking about embeddable and interchangeable execution engines is DuckDB, which you can think about affectionately is like SQLite for analytics. So it's a super fast columnar database engine that can be embedded into existing systems deployed and used everywhere.

And so this has become, you know, a wildly popular project and pretty much has shut down the cottage industry of people building their own database and data processing engines.

So used to be that if you wanted to add some form of querying or SQL capability to a web application or just some other application, you might build some subset of the features that you need just for your application. But now you can pick up DuckDB off the shelf and have something that is state of the art.

And so I'm a huge fan of this project and has been has helped, you know, socialize these ideas of modularity and reuse of systems.

There's some other data processing engines that have been built that are being used, kind of along these, this mantra of modularity and interchangeability, the Data Fusion project, which is similar to DuckDB, it's written in Rust.

Polars, which many of you are probably familiar with a new data frame library, that ultra fast Rust based data frame library for Python, which has become really popular. But there's a number of projects that I'm aware of that are using the Rust execution engine of Polars to build other types of systems. And that's really excited to see.

The folks at Meta have been building a project called Velox, which is a modular execution engine written in C++ that uses Arrow. And so what we're starting to see is these kind of new, fast Arrow based execution engines used to accelerate existing systems like Presto, Presto and Spark.

And so we have projects like Data Fusion Comet, which is being led by developers at Apple, where they're accelerating Spark SQL with Data Fusion. And I expect that we'll continue to see projects like this, as well as new query engine projects being built with these new components from the ground up, rather than retrofitting them into existing systems.

But this kind of begs the question, why be locked into a single execution engine, along with a full stack of tools, including storage, and query interface.

And so, you know, based on the size of your data set, as well as different requirements of your workload, you may want to use one stack of tools that's optimized for smaller data sets, and maybe programming in Python, whereas in another environment, you may have much larger data sets in your programming in SQL.

And so you'd like to have the flexibility, you know, to be able to work in different modalities on top of your storage, which may be all parquet files living in iceberg tables in s3.

And so traditionally, the way that people would approach, you know, working at different scales, and many different engines processing on the same data was you would use, we would use SQL, but SQL was conceived as a standard, but in practice, it is fragmented and being different for every database engine, and choosing which engine to use can also can often be non trivial.

And so there's tools like SQL glot for Python, which helps with transpiling SQL queries from one dialect to another. But we'd also like to be able to, you know, not be stuck using SQL for everything, because we're having SQL strings littered around your Python code base is not ideal.

So one of the I know I'm about to run out of time, but some projects which are helping with this, you know, we've seen also a proliferation of data frame APIs and Python. But there are some projects which are trying to help make things simpler.

There's a new project called narwhals, which is a Polars API transpiler that can use Polars, but also transpile to different SQL dialects, or other query backends.

I've been involved with the Ibis project, which is a data frame API, which transpiles into 20 different backends. There's a modin project, which is another query transpiler that targets the pandas API.

And so if you're interested in this problem at the query layer level, or interested in having a nice data frame API that targets lots of different backends, I encourage you to check out the Ibis project. It's now a nine year old project and has become, you know, pretty mature and easy to use.

You write, you know, data frame like expressions, but everything is an expression and can be composed with each other to build more complicated expressions. And if you want to run things in memory with pandas or with Polars, you can do that. But if you want to run things out of core with DuckDB or BigQuery, you can do that as well.

So the hope of all this is to work towards a future multi engine data stack where we can choose the execution engine that makes most sense for the size of data to get good performance and good efficiency. But with freedom of choice when it comes to the language front end. So if we want to work in Python with something like Ibis, we can do that. But if we want to write SQL from another language, we can do that as well.

So sorry about the AV issues, but I appreciate everybody coming and yeah look forward to engaging with you all in the open source world and see you next time.

**Host:** Yes, thank you so much, Wes, for this presentation. Thank you all for your patience during the tech issues. If you want to continue this conversation and ask some more questions. We do have our discord channel available and the lounge is accessible. But again, thank you, Wes. We're going to go ahead and close out the session, but I hope you all get to join some other ones and have a good day.