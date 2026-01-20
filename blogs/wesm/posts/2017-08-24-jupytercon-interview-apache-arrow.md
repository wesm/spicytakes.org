---
title: "JupyterCon 2017 Interview: Apache Arrow and Data Science Interoperability"
summary: "Interview at JupyterCon"
date: 2017-08-24T00:00:00
tags: ["interview", "transcript"]
slug: jupytercon-interview-apache-arrow
word_count: 4466
source_file: transcripts/2017-08-24-jupytercon-interview-apache-arrow.md
content_type: transcript
event: "JupyterCon"
video_url: "https://www.youtube.com/watch?v=Q7y9l-L8yiU"
---

{{< video https://www.youtube.com/watch?v=Q7y9l-L8yiU >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this interview with Paco Nathan at JupyterCon 2017, I discuss the motivations behind Apache Arrow and the vision for creating a common in-memory data format that can be shared across programming languages and data systems.

### The Journey to Arrow

Arrow emerged from a decade-long journey that started with building pandas. From 2008 to 2012, I focused on making Python viable for data science—reading data, manipulating it, visualizing it, and preparing it for statistical models. But over time, pandas accumulated technical debt: we built our own CSV readers, our own algorithms, everything from scratch. This created a large burden on a small group of volunteer developers with very little funding.

### The Integration Problem

Plugging pandas and other Python tools into systems like Spark and Hadoop was painful—constantly converting between data representations. At Cloudera, I started looking for others thinking about this problem. Every system had its own "proprietary" data format, even if open source. Jumping between systems meant paying a serialization penalty every time.

### Building Community First

By end of 2015, we had enough people in the room to commit to a community project. The initial Java implementation came from Apache Drill. We deliberately avoided making this "Wes McKinney's special data frame format" or something owned by a single company—we wanted neutral governance and full transparency.

### Composability and the Snowball Effect

Everything in Arrow is composable: if you build two tools that understand Arrow memory, they compose. If you build a data connector returning Arrow data, it works with any Arrow-aware tool. There's a gestalt where the whole exceeds the sum of its parts. The first Spark integration for accelerating Python on Spark was just merged—as more integrations get built, we'll see hockey-stick growth.

### Hardware Evolution

Arrow tracks the evolution of hardware—multi-core, larger memory spaces, non-volatile memory like Intel's 3D crosspoint. The convergence between SSD and DRAM performance means architecting for high-speed non-volatile memory matters. With zero-copy memory formats and fast disk, the old concerns about serialization overhead diminish.

### GPU DataFrames

NVIDIA, Continuum Analytics, MapD, and Graphistry are building open source GPU kernels that process Arrow memory—putting Arrow data on the GPU and invoking operator kernels there. Arrow was designed for CPUs but works just as well on GPUs.

### Be the Chicken

When facing chicken-and-egg problems, be the chicken. It's scary because you don't know if eggs will ever come. Feedback cycles in open source take 6-12 months. You have to pursue the vision for a long time. But there's a snowballing effect—as more integrations get built, Arrow becomes the sensible choice for data ingest and export.

---

## Key Quotes

> "When you don't know what to do in a chicken-egg problem, you should be the chicken. And being the chicken is scary because you don't know if there will ever be any eggs." — Wes McKinney

> "There's a period of time where I didn't have a day job and I was basically burning up all of my savings working on pandas because I felt that it was really important that the Python ecosystem got over that hurdle." — Wes McKinney

> "Everything within pandas is this full-stack system where we've implemented everything ourselves, and that's created over time a large burden on a very small group of volunteer developers. pandas has received very little direct funding over its lifetime." — Wes McKinney

> "The last thing that we would have wanted to do is to have this be kind of Wes McKinney's special data frame format or a format that's created by a startup or a big data company because that could create the perception of governance conflicts." — Wes McKinney

> "All of the technology is composable. So if you build two tools which know about Arrow memory, those tools compose. If you build a data connector which returns Arrow data, that can compose with any other tool that uses Arrow." — Wes McKinney

> "There's this cumulative effect, this kind of gestalt where the whole is greater than the sum of its parts." — Wes McKinney

> "If you profile the runtime of a job and where time is actually being spent, so much of the time is spent, it could be 80% or 90% or more of the time is deserializing, parsing the format from HDFS or wherever the data is stored." — Wes McKinney

> "The feedback cycles take, in my experience, 6 to 12 months... you have to be willing to pursue the vision for a very long time." — Wes McKinney

> "I'm happy for it to take as long as it takes, as long as we're building something that people feel good about and that can sustain an ecosystem of interoperable technology for hopefully many years to come." — Wes McKinney

## Transcript

**Paco Nathan:** Hi, I'm Paco Nathan with O'Reilly Media, and it's a pleasure to be able to talk here now with Wes McKinney, who's currently a software architect at Two Sigma and also, of course, very well known as the creator of pandas in Python and one of our top authors, too, using Python for data analytics. Wes, I really appreciated your keynote this morning. That was fantastic.

**Wes McKinney:** Thank you. Thank you.

**Paco Nathan:** I wanted to get in a conversation a bit more about some of the motivations behind Arrow and how you're talking about kind of a funnel, almost, effect of what you need to build from the data storage out to the data analytics.

**Wes McKinney:** Right, right. Yeah, well, I would say that Arrow is part of a much longer journey that I've been on over the last 10 years or so. When I started out, I didn't know much about doing data analysis or building data systems, and I was attracted to the Python programming language and found this ecosystem of scientific computing tools, and pretty quickly I set about building myself a tool set for statistical analysis and data manipulation and to have some of the kinds of features that are found in R and other statistics-focused programming environments.

And I spent from the middle of 2008 through the end of 2012 really focused on pandas, and there was a period of time where I didn't have a day job and I was basically burning up all of my savings working on pandas because I felt that it was really important that the Python ecosystem got over that hurdle of getting to a place where it's a viable language for doing what we now call data science—that you can read data, you can manipulate it, you can do exploratory analytics, you can visualize it, and then you can hand that clean, prepared data off to statistical models.

And of course during this time we also had to build a body of statistical modeling libraries, so things like statsmodels, things like scikit-learn also got started during that time, and so we needed this kind of convergence of technologies to happen to make the whole ecosystem successful.

But as time went on, in the early days of pandas we built the project using the best of what was available in the Python ecosystem, and that led to an accumulation of technical debt. We found over time that we had developed our own versions of everything. We had our own CSV readers and our own versions of data frame manipulations and algorithms to process those, and we've spent countless cycles optimizing those algorithms to make pandas as fast and scalable as possible.

So there's a couple of issues. The first is that there's a code ownership problem in that everything within pandas is this full-stack system where we've implemented everything ourselves, and that's created over time a large burden on a very small group of volunteer developers. pandas has received very little direct funding over its lifetime.

And we've also found that plugging pandas in, and really most tools in the Python ecosystem, plugging them in to other systems and crossing the boundary between programming languages, between Python and big data technologies like the Spark and the Hadoop ecosystem, there's a lot of pain with that, having to convert between the pandas data frame representation and other kinds of data representations.

So the Arrow project, I didn't come up with on my own, but as I started looking around, this was when I was at Cloudera and I was looking to make Python more of a first-class citizen for working on big data. So I was looking at things like Impala for running Python code inside an analytic SQL engine, looking at Python on Spark and how we can make those integrations stronger.

And one of the things that jumped out was we need a way to exchange data with these systems that's efficient and that is reasonably standardized. And so I started looking around, like, is there anyone else that is thinking about this problem of that every system has their own—they may be open source, but they have quote-unquote proprietary data formats. And so whenever you jump from one system to another, you pay this serialization, this crossing penalty.

And so I spent about six months or so kind of looking around and trying to get as many people in the room as possible to at least talk about the problem and to discuss, like, is this something, is this a common enough problem where we could develop a solution that we could all adopt and grow and develop to meet a broad set of use cases.

So by the end of 2015, we got enough people in the room to say, like, this is something we really believe in and something we want to make a community project and standardize and start building integrations so that the next generation of data systems all can use this common data format.

It took us a little while to come up with the name Arrow, and we had to jump through a few hoops with the Apache Software Foundation to set up the right governance structure and to pull some IP out of other projects. So the initial version of the Java implementation of Arrow came from the Apache Drill Project.

But we felt really strongly about setting up a community-first project where we could develop the format in an open and transparent way and to bring as many people into the process as possible and to make this something that the community owns and that can be really widely adopted.

I think the last thing that we would have wanted to do is to have this be kind of Wes McKinney's special data frame format or a format that's created by a startup or a big data company because that could create the perception of governance conflicts and other issues. So we wanted this to be the community's project and to build it kind of in full view.

And so it's been really exciting and also scary to start from a markdown specification, an incomplete markdown specification of the format, and to build libraries from scratch and to engage with the community to understand how we could best kind of build out the ecosystem from that kind of chicken and egg stage.

And so right now we're looking at how we can use the Arrow technology to more quickly advance the state-of-the-art and what's possible in the Python ecosystem and beyond.

**Paco Nathan:** Well, it's fantastic, the scope and the impact of this, because it's not just working across multiple different popular projects and getting them to work with common storage, but it's across entirely different paradigms. I mean, looking at what people are doing in Python versus what they're doing in Hadoop or Impala, looking at R, it's beyond a scale of integration that I would usually encounter.

**Wes McKinney:** Right. I mean, one of the areas where there's the closest semantic compatibility in terms of what people are doing with the data really is in the data science world. We have pandas data frames in Python, R data frames, Julia has data frames, Apache Spark has data frames. And if you look at their internal data model and the semantics of manipulating those objects, there's a lot of similarity, and even the code has come out looking very similar.

When Spark looked to build an API that looks like data frames for the Spark SQL runtime, they chose to emulate pandas, to emulate R as closely as possible, so that when users were working with data in Spark, that they could use the same knowledge that they'd accumulated as R programmers or as Python programmers to work with data that's part of the Spark runtime.

But the hard part there is that we have so many years and person years of development, creating libraries of algorithms and modeling tools, which are very tightly coupled to data frames in R, data frames in Python. And that is one of the key challenges, is that if we want to be able to share code and infrastructure between the Python world and the R world, for example, we will have to rebuild many of those algorithms to be based on a common memory format that is not particular to R, not particular to Python.

**Paco Nathan:** So I found that chicken and egg problems often drive away contributors because—

**Wes McKinney:** It's too daunting?

**Paco Nathan:** It is very daunting, and by its nature, when you work on a chicken and egg problem, it is often not useful until it reaches a point of critical mass.

**Wes McKinney:** But the interesting part is that in something like this, all of the technology is composable. So if you build two tools which know about Arrow memory, those tools compose. If you build a data connector which returns Arrow data, that can compose with any other tool that uses Arrow. So there's this cumulative effect, this kind of gestalt where the whole is greater than the sum of its parts.

So really what we've been doing over the last year and a half, not only in stabilizing and hardening the Arrow format so that the format isn't changing—and there's lots of fine details dealing with timestamps and decimals and the fringe parts of memory representations, we want to make sure all that's stable—so that we can focus on building libraries of analytics code which can be used very easily between environments.

**Paco Nathan:** One thing you mentioned earlier, which I find is really interesting, is about the serialization. Looking at cluster traces for the early years of Hadoop and large big data jobs that were running, you'd spend so much of your time doing serialization or deserialization. And what strikes me about, if I understand correctly, what strikes me about Arrow is that this is being addressed directly, but even more to the point by using columnar formats. Now you can allow for pushdown predicates and even more sophisticated means of taking a lot of that tech debt off the table.

**Wes McKinney:** Right. That's right. And we aren't reinventing any wheels as far as columnar data formats or even columnar storage. So people talk about, compare Arrow with Parquet or ORC, which are columnar storage formats, but really they're complementary technologies where we read data from those storage formats and then we put it in Arrow in memory.

But you can imagine an I/O pipeline where you deserialize chunks of data from columnar formats into Arrow, and then you apply predicates and filter those chunks of data as they're coming through the pipeline.

You mentioned serialization overhead. This is one of the biggest motivations for the project is the fact that serialization, particularly when you jump between operators within a single system or if you are using two systems as part of solving a bigger problem—and this is certainly true in old school Hadoop MapReduce where so much of, like if you profile the runtime of a job and where time is actually being spent, so much of the time is spent, it could be 80% or 90% or more of the time is deserializing, parsing the format from HDFS or wherever the data is stored, putting that in intermediate data structures, performing the analytics, and then reserializing and writing the results back out to disk.

So particularly as data processing systems are moving to more of an in-memory and shared memory model where data in between operators is not persisted to disk, it may move between processes, but if it moves between processes, it goes through shared memory. So to be able to move data between processes without serialization is very, very powerful.

And so we've invested a lot of time in thinking hard about how that quote-unquote serialization works so that if I have an Arrow data set in a particular process, that I can expose that data to another process or another thread of execution without any serialization. So effectively on the receiver side, it's looking at some metadata and then moving pointers around to be able to access each column in the data set.

**Paco Nathan:** So this evolution of Arrow then, it sounds like it's tracking closely with what's going on in the evolution of hardware, having multi-core, having larger memory spaces, and taking advantage of those as opposed to having a lot of little servers in a cluster.

**Wes McKinney:** Yeah, absolutely. And you see, particularly with what's happening with the non-volatile memory technology, 3D crosspoint from Intel. So we have just absolute throughput to disk. There's this convergence happening in performance and latency between solid-state drives and DRAM.

**Paco Nathan:** Yeah, they're meeting.

**Wes McKinney:** So they're kind of meeting. And so it may not be a full convergence, but architecting the systems with high-speed non-volatile memory in mind, that is kind of how a lot of systems need to evolve in the future.

So it used to be that disk is slow, and so you might be able to get better absolute throughput by serializing and using columnar compression with something like Parquet format. You can make the data really small. And even though your disk is fast, the data store is so small that you can deserialize it much faster in that kind of highly encoded and compressed form.

But when you're dealing with super-fast disk and you have a zero-copy memory format, that concern kind of goes away in a lot of cases.

**Paco Nathan:** It's interesting. So one thing that when I was first looking at this, one thing that I missed was that, as you were saying, Parquet or other kinds of formats for storage—there's the data at rest, there's the data in memory, there are different layers involved here. So you could look at something like Parquet for data at rest, Arrow for the data representation, the data frames that are being used across different processes. It seems like there's another layer beyond that in terms of the DAG of what needs to be computed. And I saw in your talk you were mentioning about that. Forward-looking, is that an extension of the project?

**Wes McKinney:** Absolutely. So the layering of technologies—so the first is the memory format. Then you need a way to manage shared memory, particularly in a multiprocess environment. So one project where, one subproject within Arrow where we've been working on this, came out of the Ray project at UC Berkeley RISE Lab, where they developed a system called Plasma, which is a shared memory object store.

And the idea is that it provides a third party for managing memory lifetime of shared memory. So if you create an object in one process, you would materialize that in the Plasma object store, and then another process can acquire a reference to that data. And so if two processes say, okay, we're both done with this object, then it can be released to the memory pool.

So the way that they're using that in the Ray project is by evaluating task graphs for reinforcement learning and deep learning models, and where you're evaluating this task graph and you have a pool of workers. And so the scheduler can assign work to a worker, and that worker can be in any process. And what it does is the worker will acquire pointers to the data that's stored in the general shared memory store, and it can acquire references to very complex data sets, dictionaries of NumPy arrays and other. It could acquire a reference to a gigabyte or four gigabytes of data for effectively free.

And so that programming model is very powerful in a single machine multiprocess setting and can be even used in a distributed setting. As far as the Arrow project is concerned, I'm very interested in, from the point of the in-memory format, the mechanics of memory sharing. From there, we need to start building a library of operator kernels, which can process primitive Arrow data natively.

So these are things like adding two arrays or computing the square root or counting the distinct values in an array of strings, things like that, stuff that you would find in pandas.

**Paco Nathan:** Composable operators.

**Wes McKinney:** Composable plus. Composable operators, right. So once you have the primitive operator kernels, you need the ability to create operator graphs that can understand dynamic dispatch to the appropriate kernel implementation so that if you can create a deferred graph of effectively data frame operators, and then that can be evaluated against data that is all in shared memory or maybe partially in memory and some of it is in shared memory.

And when you're evaluating that graph, you might choose to materialize the results in shared memory so that the results of computation can be easily accessible to other processes.

So if you look at the architecture of something like TensorFlow or modern deep learning frameworks, they're very much architected in this form where you have deferred operator graphs. Everything works in a graph data flow execution model. So I think that this model would work very well for processing Arrow data, except that the data model for this is tables and columnar data instead of—if you were using TensorFlow, you'd be manipulating tensors, which is just a different data model.

**Paco Nathan:** Are the hardware vendors then engaged in this? You mentioned about Intel, but are there primitives in the works for supporting these kinds of operations in memory?

**Wes McKinney:** Yeah, there are. So I personally have not yet started building an operator kernel library, although it's something I plan to start on soon. But one initiative that's going on right now that's being spearheaded by a group of vendors who build software for graphics cards, GPUs. So NVIDIA, Continuum Analytics is involved, MapD is a GPU database, Graphistry, there are some other players involved.

So they are working together to create open source GPU kernels, which process Arrow memory. So they're calling this GPU DataFrame, and they have a library of GPU kernels which are implemented for the CUDA architecture. And so the idea is that they put Arrow memory on the GPU and then invoke their library of operator kernels on the data in the GPU.

And so this is really exciting because here you have Arrow, which initially was designed for use on the CPU, but there's no reason why you can't put the data on the GPU and then invoke kernels on it.

So I think we'll see more and more of this from specialized use cases, either for specialized hardware, for GPUs, for CPUs. But I'm really interested in, from a community perspective, bringing together as many people as we can inside the Apache Arrow project so that we can develop this software together and solve some of these problems in a way where there's a neutral ground for collaboration and building a body of reusable software.

**Paco Nathan:** Wonderful. Something you mentioned in your keynote also, and you mentioned earlier, is about confronting these chicken and egg problems. And I wanted to close—you had some great advice about that.

**Wes McKinney:** Yeah. What I said in my talk, and I've said this for several years now, is that when you don't know what to do in a chicken-egg problem, you should be the chicken. And being the chicken is scary because you don't know if there will ever be any eggs. And so you have to believe in the vision and be willing to pursue it for a very long time.

And often the feedback cycles are very delayed. So what I found in building open source software for a long time is that you might build something, and to you it seems like it's really great, and you release it, but then the crickets chirping and you're not getting any feedback. And really the feedback cycles take, in my experience, 6 to 12 months.

And so especially when you're working on a new problem or one that requires a lot of investment from a lot of parties, and I think Arrow falls into this category, you have to be willing to pursue the vision for a very long time.

But there's a snowballing effect where as more people build integrations with Arrow—like the first integration with Spark between Arrow and Spark was merged for accelerating Python on Spark. So we're seeing the initial integrations get built, and I think as more and more of them get built, and we start seeing components plugging together that all use Arrow, I think we'll see this kind of hockey-stick growth at some point in the future where it will just be the sensible thing to build Arrow support, either as a primary tool that gets used in a data processing system or at least as an add-on for data ingest and export. So we'll see.

I mean, I'm very optimistic, and I think one of the best parts of doing this as a community project and trying to get as many people to lend their voice and to explain their use cases is that we don't want to leave people out, and we don't want to build this project in the ivory tower.

So I think I'm happy for it to take as long as it takes, as long as we're building something that people feel good about and that can sustain an ecosystem of interoperable technology for hopefully many years to come.

**Paco Nathan:** Wonderful. Thank you, Wes. I wish you all the best on this.

**Wes McKinney:** Yeah. Thank you. Thank you.