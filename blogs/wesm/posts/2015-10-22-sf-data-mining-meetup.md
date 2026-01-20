---
title: "McKinney SF DM talk"
summary: "Video at SF Data Mining Meetup"
date: 2015-10-22T00:00:00
tags: ["video", "transcript"]
slug: sf-data-mining-meetup
word_count: 8393
source_file: transcripts/2015-10-22-sf-data-mining-meetup.md
content_type: transcript
event: "SF Data Mining Meetup"
video_url: "https://www.youtube.com/watch?v=5sdzxNQ97CI"
---

{{< video https://www.youtube.com/watch?v=5sdzxNQ97CI >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This talk presents Ibis, a project to bring Python's data science capabilities to big data systems.

## Python's Evolution

Python has gone from a questionable choice for production systems to "safe choice" for data work, due to maturing tooling and successful teams with track records. "Back in 2006, 2007, there wasn't that track record. It was a chicken and egg problem"—choosing Python for data problems "made you seem a little bit weird at the time."

However, Python struggles beyond "medium data"—datasets fitting on a single machine. Even with two terabytes of RAM available, big data forces workarounds: sampling or aggregating until manageable. "The larger the data, the less sophisticated the analysis"—often just counting at scale.

## The Architecture Problem

Tools historically fall into two categories: scientific computing (NumPy, SciPy) for numerical analysis, and big data systems (Hadoop, Spark) for structured data like JSON and CSV. Python excels at scientific computing but has limited presence in big data architectures.

Decoupled storage and compute (S3, HDFS) creates opportunities, but user interface quality comes last in "Maslow's hierarchy of needs for big data"—after solving scalability and performance, user experience becomes an afterthought.

## Ibis

Developed at Cloudera, Ibis "hides away as much of the complexity as possible of the storage and compute problems." Two components: a DSL that looks like pandas but compiles to SQL, and tools for extending analytic SQL systems with Python functions.

The design goal: "anyone can take their gnarliest, craziest SQL 100, 200 line queries and break it apart into composable, reusable Python statements."

## Performance

Bottlenecks: serialization overhead, vectorized vs scalar operations, and inter-process communication. Moving from scalar to vector operations yields 50-150x speedups. "If you're extending a big data system with Python, you'd better have a way to do vector operations if you want your Python code to run fast."

## Shared Memory

My solution: shared memory representation for tabular data that handles JSON-like structures, handing data to Python "with as little conversion or modification as possible." This departs from external language protocols that suffer from row-at-a-time processing and expensive IPC.

## Vision

"Solve big data without leaving the IPython notebook" while leveraging the existing Python ecosystem—pandas, Scikit-learn, domain-specific libraries—without fundamental workflow changes.

Ibis initially targets Impala, with plans for Redshift, Presto, and Hive support.

## Key Quotes

> "Back in 2006, 2007, there wasn't that track record. It was a chicken and egg problem where there were no successful teams that had multi-year stints of doing Python data stuff... if you were choosing to solve those kinds of problems with Python, it made you seem a little bit weird at the time."

> "I think a general trend that you see is the larger the data, the less sophisticated the analysis. Largely just counting things when the data gets really big."

> "In terms of Maslow's hierarchy of needs for big data, in a sense, user interface and the quality of the user experience interacting with the data is the part that comes at the tail end of the equation after you've fully addressed the scalability and performance problems."

> "A question that I get from people a lot is, Wes, I want to keep using pandas, I just want it to work with big data, and it's a complicated, that's a very complicated problem."

> "The design goal out the gate was to look at the SQL programming language. And let's make sure that anyone can take their gnarliest, craziest SQL 100, 200 line queries and break it apart into composable, reusable Python statements."

> "If you're extending a big data system with Python, you'd better have a way to do vector operations if you want your Python code to run fast."

> "So that's my goal, being able to solve big data without leaving the IPython notebook or whatever Python development environment you prefer."

> "Python is a really great tool. And the fact that you have a really accessible community of developers and tools and a learning curve that is not too steep, that building software in Python makes a lot of sense to reach a really broad audience of people who can now tackle data problems that they couldn't have five, 10 years ago."

---

## Transcript

Thanks for coming, I know taking time out of your evening is always a trade-off, but

I appreciate you being here and for using Python to solve problems.

So my abbreviated bio is I've spent the majority of my career working on data tools.

I think people often call me a data scientist, but really I've spent most of my time making

tools for the data scientists and have spent comparatively little time actually doing data

science.

Although I secretly want to be doing more modeling and modeling and data science, but

I find myself gravitating toward the tool making.

I did several years ago make an honest effort to go back to grad school and get a PhD in

statistics, but I dropped out in favor of working on tools.

So I guess as context for this new project, during the first part of my career when I

was at AQR, which is where I got interested in data tool making in the first place, I

found myself in QuantFinance basically writing SQL and using Microsoft Excel and looking

for solutions for that, not only for building production code that can be run every day,

but also doing interactive research and just ad hoc analytics.

So Canvas was kind of a solution to both of those problems to be able to build software

effectively, but also move work out of the SQL and Excel workflow that I found myself

in the middle of.

So we all love Python and the world is a lot different than it was seven or eight years

ago when I started out programming in Python.

It used to be that you had to have all these arguments about, you know, can we trust Python

in production?

Is it a serious programming language?

Maybe we should be doing Java or C++?

And thankfully we're not having as many of those kinds of arguments anymore, in part

because the tooling and the software development tools, the data tools have become a lot more

mature and so big companies find it a safer choice because there is a mature ecosystem

of tools.

There's also a community of supportive developers.

There's resources for learning how to program in Python.

And generally there's also teams of data people that have track records now of using Python

for a period of years that have been successful.

So back in 2006, 2007, there wasn't that track record.

It was a chicken and egg problem where there were no successful teams that had multi-year

stints of doing Python data stuff.

People were just starting out to do it and so if you were choosing to solve those kinds

of problems with Python, it made you seem a little bit weird at the time.

But now it's viewed as a safe choice and for lots of good reasons.

Python has definitely struggled to move beyond the medium data types of problems which fit.

So I describe medium data as data that fits on one machine.

I guess you could also call data that fits on one machine small data.

But I think of small data as data that you don't have to be that careful about the size.

So nowadays you can get machines with two terabytes of RAM.

You can get nodes on EC2 with two terabytes of RAM.

And so the problems that now are medium data are quite large.

Whereas even having 10 or 20 gigabytes of data used to feel like big data because you

need many machines to solve it.

But if you do have properly big data, using Python is still problematic.

And the way that data scientists usually get around the problem is by using another system

to sample or aggregate the data and get it into a size where it can fit on one machine.

So if you have a problem where you need to analyze the full fidelity data set, maybe

you have many terabytes or a petabyte of data.

Maybe the things that you're doing with the data are not very complicated.

I think a general trend that you see is the larger the data, the less sophisticated the analysis.

Largely just counting things when the data gets really big.

But still it would be nice to be able to use Python in a full featured way regardless of

the size of the data.

And some of the reasons for that, and I kind of generalized the world a little bit into

these two categories of tools.

And so there's been a chicken and egg problem in the Python community that the class of

tools tend to fall into these two categories.

On one hand, scientific computing tools.

And people have been doing scientific computing in Python since the mid-1990s.

And part of the reason that we have nice things in Python is because there were a lot of grad

students who were procrastinating on their PhDs and wanted to have an alternative to

MATLAB.

And so they invested heavily in creating and wrapping up all the legacy scientific libraries,

creating really good interfaces to high-performance computing tools, linear algebra, and all that

stuff.

Starting with Sci-Fi in 1999, 2000, that era.

NumPy itself is going to have its 10th birthday early next year, I believe.

I don't know the exact date, but it's getting up around 10 years old.

But people have been doing multidimensional array computing in Python for many years.

But if you look at when people say big data in Silicon Valley, and it might be that big

data is different depending on who you talk to, largely they mean data that's falling

on the left side of this page, which is more heterogeneous, structured data that could

be written in a CSV file or in some form of application log file.

Increasingly, it's JSON.

And in a sense, work that's happened elsewhere, like outside of the Python community, has

encouraged this, because application developers who are Ruby programmers or Python programmers

or Node.js programmers, or they're in the Java ecosystem, they're all putting their

application data, often through the same pipe it's landing, and some distributed storage

in data that's, you know, let's just store the raw data in JSON and we'll figure it

out later.

And so the tools have rised to the occasion in the Duke ecosystem with MapReduce, and

now it's more and more Spark.

You have really good tools for analyzing such data with SQL code.

And in general, you know, this is how things have shaped out, or shooken out, and, you

know, Python's great stuff over here, less stuff on the left side.

It is changing, though.

So if you look at pandas, pandas was an effort to build an industry analytics toolkit using

Python's scientific computing stack.

And if you look at pandas as a library, part of the reason that it's grown so large is

because it had to mind all of its own concerns.

It had to build its own in-memory analytics engine, all of its own relational algebra

and joints.

It has its own CSP reader, it has its own interface

with SQL databases, it implements its own data types

because there's data types that occur in the wild

which are not found amongst NumPy's data types.

It has to handle its own missing data

because NumPy doesn't have a built-in notion

of missing data, and a lot of the reason

that people stick with it is because of its API,

and so the pandas code that you write,

it is true that every time you execute a statement

with pandas, it's immediately executing that operation,

but you can also look at the pandas code

that you write holistically as a domain-specific language

for describing your data transformations,

your analytics, and all of your data work,

and so, in a sense, a question that I get

from people a lot is, Wes, I want to keep using pandas,

I just want it to work with big data,

and it's a complicated, that's a very complicated problem,

and in a sense, the work that I'm doing now

is to address that need.

Now, meanwhile, there's lots of SQL engines,

and the SQL engines often are created

for some problem domain, whether you're Facebook,

I mean, you can have an engineering team

build an interactive SQL database,

some of them have originated in vendors,

some of them are open source, some are closed source,

and these systems have generalized to meet the needs

of industry analytics in a lot of different ways,

I'm sure you're aware of,

and so, the big trend that I see,

and will be the theme of this talk,

is that in big data in general,

one of the novel things with things like Amazon S3,

and HDFS, Hadoop's distributed file system,

is that it's decoupled the storage part of the problem

from the other systems that are part of the equation,

so you can use MapReduce with HDFS,

but it used to be when people said Hadoop,

they really meant HDFS and Hadoop MapReduce,

whereas now you have a whole smorgasbord

of computing tools which know how to read and write data

to HDFS, they can also read and write data

to Amazon H3, to HBase, to other storage engines,

that are all open source,

and so, it used to be you would buy a system

that is vertically integrated,

your user interface is probably SQL,

it has its own built-in compute engine,

its own storage engine,

so when you buy Amazon Redshift,

you're paying for it as a service,

but really you're buying into a vertically integrated stack

of UI compute and storage,

but in open source, these things are decoupling,

so if you have your data,

you can put your data wherever you want,

you can bring your own compute,

whether that's Spark, or MapReduce, or a SQL engine,

and so hence the rise of SQL on Hadoop,

but that leaves the user interface being the area

where there's been comparatively little invested,

and a major reason for this is that the storage

and compute is hard enough,

and so in terms of Maslow's hierarchy of needs

for big data, in a sense, user interface

and the quality of the user experience

interacting with the data is the part that comes

at the tail end of the equation

after you've fully addressed the scalability

and performance problems of the compute and storage systems,

and so if you think about big data architecture,

so how appropriate that we're at LinkedIn,

and I can have a big data architecture which uses Kafka,

which we've created at LinkedIn,

but you see more and more systems like this

where you have a lot of real-time data

that's being ingested, landed in raw form,

usually in JSON or some other flat format,

you write an ETL job to convert the raw data,

to clean it, to pull out the stuff

that you're interested in,

store it in a more efficient format,

which is increasingly something like Apache Parquet,

columnar, compressed columnar format,

and then you consume that ETL data in some compute system,

so I just put an analytic SQL engine here as an example,

but if you think about these architectures,

there's relatively little Python happening in them,

and to choose Python in any stage of this architecture

would come at the cost of performance or usability,

and so usually what you see is that Python

is happening down in this area,

where a lot of the work has already been done,

you write a SQL query, you get the data back

into a pandas data frame,

and then you do your modeling, analytics,

data visualization, you know, whatever.

So the cool thing about the SQL and Hadoop systems

that are being created is that their ability to address,

they're getting better at dealing with more complex data,

so it used to be, if you look at, you know,

your big data architecture,

that half of the work that's happening in your ETL jobs

is taking data that isn't necessarily flat

and normalizing it into a set of tables

that can fit into a flat relational database structure,

and with the addition of nested and nested

or complex type support to analytic SQL systems

is that you can analyze JSON data directly in place

without having to go through that flattening,

you know, kind of unraveling normalization step.

You still have, you know, there's still some work to do,

you have to infer schemas,

that's a pretty hard problem by itself,

but assuming that you can write down a schema for your data

and your SQL system knows how,

has that schema support given your data,

you can write queries that are very expressive

that can analyze that data in place,

and so Google BigQuery is a,

my understanding is a SaaSification

of Google's Dremel system,

which was published about in 2010,

which means that Google was doing analytic SQL

on JSON-like data back in 2003 or so,

and so there's a long history,

and it's been shown to be a pretty good way

of working with this kind of data.

So the project I'm building, Ibis,

which I started when I joined Cloudera a year ago,

is a user interface layer,

well, it's a little more than user interface,

and I'll explain, but really,

it's intended to be the user interface layer

for Python programmers doing industry analytics

that hides away as much of the complexity

as possible of the storage and compute problems,

and enables you to do your Python work with big data

without having to leave Python,

or leaving Python as little as possible.

So, you know, that solves, you know,

I think that I didn't really have experience

with big data systems starting a year ago,

like I was really a small and medium data kind of person,

and so I looked at this and said,

well, it's unfortunate that when you go

from small and medium data to big data,

you have to learn a whole use of tools,

you have to climb a bunch of additional learning curves

and learn a whole bunch of new systems,

whereas what you're actually doing with the data

in a lot of cases isn't that complex,

it just happens to be that Python isn't very good

at talking to those systems and integrating with them.

And so I sat down with various teams around Cloudera

and said, well, how can we build a better synergy between,

I didn't use the word synergy, but I'm using it now,

how can we connect Python to big data systems

in a cleaner, more efficient way

to deliver the kind of experience

that you'd like to see within the next few years?

And so for the purpose of this talk,

I'm gonna talk about two areas.

of concrete things that we're doing with the project.

And the first is to move SQL programming out

of the SQL programming language and into Python

and in a way that looks and feels a lot like Canvas.

And so the other part of the problem, which

is conveniently cut by the screen divider,

is extending analytic SQL systems with Python code.

Not just analytic SQL, but analytic SQL

happens to be the target.

But extending these big data compute systems

with Python code in a way that doesn't trade away

an unacceptable amount of performance or usability.

So I'm going to talk about the Ibis DSL, which

is the deliberately Canvas-like expression layer, which

the design goal out the gate was to look at the SQL programming

language.

And let's make sure that anyone can

take their gnarliest, craziest SQL 100, 200 line queries

and break it apart into composable, reusable Python

statements so that anything you're doing in SQL

can be fully ported to Python.

So if you look on the website, there's

actually a new document, which I wrote last month,

called Ibis for SQL Programmers that

goes through every granular SQL relational concept

and shows how you can map those SQL concepts

onto the equivalent Ibis calls.

So part of what I did there is I looked

at not only real-world customer workloads, queries,

like I said, this crazy 200 line query,

and you see what people are actually doing with the data.

There's also benchmark suites to evaluate

the completeness of SQL engines that you

can use things like TPC-H and TPC-DS,

if your database junkies in the room,

that you can use to really stress your ability

to generate complex SQL.

It did target Apollo, and we're focused

on developing tools that will work well with Apollo

for a couple of reasons that I'll explain.

But the general SQL generation tool chain

inside Ibis is for a general purpose.

And so I'm looking for collaborators,

which might be people in the room,

to build support for other analytic SQL backends.

So high on the list of wants in Ibis

are Redshift, Presto, Vertica, Postgres, which is not really

analytic SQL, but if you do some Postgres and some Redshift,

they kind of help each other because you're all

coming off of basically a common SQL dialect.

And so the way that the project works, if you write Python code,

it hides as much as possible of what happens down

in the compute layer.

We are working on tools to extend analytic SQL

systems with user-defined Python functions.

And that will be in the second half of the talk.

Now I'm going to go into a demo and show you

what the DSL looks like a little bit in about five.

I need to come up with a three or five minute demo for talks.

But if you look at the Ibis for SQL programmers,

it's broken down.

And so even weird stuff exists, subqueries and things

like that.

All that stuff is in here, which is the equivalent Python code.

And so the intent is to be very, very pandas-like.

So while I can't promise to exactly port the pandas

API to an expression language that compiles to big data

systems, the idea is to get as close as possible,

or at least to take every API and concept

from composable R or pandas-like tools

and make them available, executing

on a different back end.

So API and all that stuff there.

So let me try to record the screen for a couple of minutes.

So I'm also operating a blog, which I haven't posted on,

I know, since mid-September.

They've been traveling.

But it's both a developer blog, as well as

use cases and examples of using the project.

So I'm going to use the SQLite Ibis interface.

So I have a data set containing, which you can

download from the blog, it's linked to from the blog,

containing the CrunchBase data set.

Slightly updated, but that's because they won't give me

access to the latest one.

I don't know why.

Maybe if you know anyone at CrunchBase,

you can tell them Wes wants the data.

If he wants the data, he's going to write about it,

about it, popularize CrunchBase.

I think it's a great data set.

And so if you look inside it, it has a set of tables.

And the idea with the project is you grab,

let's look at the rounds table.

So a table in Ibis speak is like a pandas data frame,

except the data is not on your computer.

And so any time you build an operation, let's say,

rounds colon five, which is like the equivalent pandas

operation, whenever you try to examine the expression you

create, Ibis takes that expression,

compiles it to whatever back-end target, runs the query,

and returns the results in a pandas data frame.

So effectively, what you're doing,

you can also call the .execute method,

which returns a data frame.

And so any operation you perform returns

the appropriate pandas object.

So if you have a table expression, you get a table.

If you say, let's see, if you look at rounds raised amount

USD dot sum, it shows you this is the total amount that's

represented in the data set.

And these are all expression objects that you can reuse.

So here, when I call raised amount USD dot sum,

I get a double scalar expression.

And so the fact that if you look inside the object

and you're developing, there's a little expression tree

which shows all of the operations

that you've performed on the data.

So here's the column from this table, which

has this schema, the sum operation, which

produces just a single number.

And so you can take this expression and say, well,

really, I want to maybe group by rounds funded quarter,

and then maybe aggregate with that expression.

Let's call that, I'm not going to give it a name.

So any aggregate expression you can put here,

any grouping expressions you can put here,

and when you look at this guy, you just

get a total amount raised by quarter.

And so you see here, suppose you wanted

to group by quarter name, you'd have to actually transform

the data set a little bit.

So we can just do that right now.

If we look at funded quarter, let's

call strip on it, because it's a string.

And now let's do write to, I actually haven't tried this,

so we're going to see.

OK.

So we strip it, do write to, which gives you

the write to characters.

So we can take this guy.

So let's call this quarter, and then I'll give it a name quarter, now group by quarter.

And so now you get Q1 through Q4.

You can pass a list of grouping expressions just like in Canvas.

You can put a list of metrics here, like suppose I wanted to also get the number of rows, so rounds.count.

So there are some nulls in the data set.

So if you wanted to do some cleaning, you can continue composing and adding operations.

So I can say fill in A, maybe I'll fill in A after doing the data loading.

Fill in A, unknown, quarter.

So we'll get on to something slightly more complex.

So I have friends who started Node Analytics and worked there.

And so they have this query where they compute the most successful investors based on whether or not they've had exits.

So like the number of investments that they've made divided by the number of those investments that led to either an IQ or an acquisition.

So you can go on and look at this example on the blog.

You see there's some munging here where you define what is an exit.

You do a count distinct on that.

You do a count distinct on the company permalink, which is how companies are identified.

And that's after doing a join of investments on companies.

And then finally you have an inline view and you compute the acquisition rate by investor.

And so what's nice about the Ibis version of this is that you take this nested SQL curve with a bunch of embedded expressions

and you can break it down into a set of reusable expressions.

So here's just to walk you through what this looks like.

So there's some cleaning that you do on the investor names.

You fill in A's.

You give the name investor name.

You compute your two metrics of interest.

So the number of unique companies for each investor.

Their statuses.

So either if they're IPO or acquired.

So you use the isn't function just like Panda's.

Do a Boolean if else.

So null out ones that are not IPO or acquired.

Call count distinct on that, which is the end unique function.

Then do your join.

The joins are all reusable.

And then you group, aggregate, and then use the mutate function inspired by dplyr to add the acquisition rate column to the aggregated table.

So you run that.

And you get for each investor an acquisition rate.

And you continue going and say, well, I think I called that stats two.

So then you can take, you know, forget about all that other stuff you did now.

Say I want to filter down to only investors that made over 100 investments.

Sort by acquisition rate and descending order.

And then you get your top 20 most successful investors.

And so with Ron Conway just leading the pack by a significant margin.

So anyway, SQL.

So we're feature complete with SQL.

And that was the first major part of the project.

So if you do use the library and you find something you can't do in SQL, please make a book for it.

That's my attitude toward it.

All right.

So I did the demo already.

So there's some interesting stuff going on in Apollo that we're, you know, Ibis is helping steer development in Apollo.

And the main thing that's happening there, and it's going to take some time, is how do you extend a distributed computing system with Python and achieve good performance.

So if you think about the problem schematically, you want to take Python code, which is at the UI layer, and move that Python code into the compute layer.

And have it run as is without need for some translation or compilation stuff.

And there are a lot of, you know, compilation tools for Python, but they're limited.

And if you have libraries that you've built up over the period of years which are written in Python, there's no chance of translating them or compiling them.

They have all of your domain-specific logic that you want to run in a distributed environment.

You'd like to be able to just move that code there and have a way to extend those systems in an efficient way.

This is extremely hard, though, which I'm sure many in the room are aware of this, that extending any distributed computing system usually involves implementing user-defined functionality.

So let's say you're using Presto, and there is a way to extend Presto with your own code, but you have to write it in Java.

There may be a way to write Python functions or extend Presto.

You can now extend Redshift with Python functions, but they're extremely limited.

So what I call the extension with a language that is not the implementation language of a compute system, I call that the external language protocol.

Usually, sometimes you can have an external language protocol which is embedded in the system.

And so you've seen in big data, I know in LinkedIn, JRuby and any of the Java implementations of dynamic languages got really popular because you could write UDFs not in Java.

If the processes that execute the code live outside of the host system, usually you're dealing with a pretty serious performance bottleneck.

And so if you write UDFs in Redshift, you're basically making inter-process calls between the Redshift master process and an external Python process.

And usually you're operating on a one-row-at-a-time data model, which I'll talk a little more about.

The same issue is true of Spark.

So if you're using Python with Spark and you write anything that can't be expressed as a DataFrame API call, you're dealing with pretty significant performance overhead.

There's a lot of things you can do through your UDF interface beyond simple data transformations.

You can also express a large class of statistical machine learning models as aggregate functions in SQL-type systems.

And so the reason that UDFs are slow, and there may be other reasons, but typically it falls into these three categories of problems.

So the first and the biggest issue in practice is how the data moves between the host system and the external language.

So if you're Redshift, if you're Impala, if you're Presto, if you're Postgres, how do you actually get the data that's flowing around this distributed runtime?

How do you get it into Python?

So that's what I call serialization overhead.

There's also the computation model.

And so with Python, it's generally accepted knowledge that you don't want to operate on one value at a time in Python.

You want to operate on one array at a time.

And the array should be as large as possible so that you can effectively be orchestrating very fast C or C++ code with Python function calls.

There's also the question of how you call out into an external process.

And indeed, you know, inner process can be...

or remote procedure calls can introduce significant overhead

into any external UDF.

So just looking at vectorization as one place

where a lot of performance gets eaten up.

So here's a SQL statement with a Boolean condition selecting

one value for the true branch, x plus y for the false branch.

And if you want to implement this in Python,

I'll explain this diagram.

I don't know how many of you read it.

So the x-axis is the size of the array that is being operated on.

So this line right here is arrays that have 1,000 elements.

And this is 5,000 over here.

The green line is the one line.

So that's the pure Python implementation

of this sum with a Boolean condition.

And so the blue line, so this speedup line right here

is 50x speedup.

This is 100x speedup, 150x.

And the blue line is a naive implementation

using NumPy vector function calls with temporary variables

and everything.

So the simplest thing you could do

is use all vector operations.

And you end up with around 50x speedup of large arrays.

And so if you avoid temporary arrays

and you use Cython to generate C code,

you get up to the red line is the simplest Cython

implementation I can write.

And then I use Cython tricks to eek out another 50x speedup.

But these kinds of speedups, going from scalar

to vector operations in Python are very, very common.

And so if you're extending a big data system with Python,

you'd better have a way to do vector operations

if you want your Python code to run fast.

And so what we're doing to deal with this,

not only the scalar versus vector operations,

but the larger general problem of how

data moves efficiently between systems,

in particular tabular data in analytical systems,

is we are creating a shared memory representation

for tabular data that can address JSON-like data

in an analytic SQL system.

So basically, you can hand off a blob of data,

so a table or an array of data, to a Python process

with as little conversion or modification as possible.

Our goal is to be able to hand off the data with no serialized

or deserialized stuff.

So it's going to be as fast as you

would get out of a map copy through a shared memory region.

Part of the reason why we're focused on Impala

to do that, first of all, being among SQL on Duke engines,

one of the best of the bunch.

It's also written in C++, which is nice,

as far as native performance, being

able to do runtime code generation to accelerate

the management and moving around the data within the runtime.

In particular, when you know that you have a Python UDF

function call coming up.

So there's a lot that you can do there

to achieve native performance in that C++ LLVM framework.

Another reason is that if we improve,

and we do at some point plan to improve the LLVM compilation

toolchain in Python to address more and more complex data,

so there will be an interesting class of Python functions

that can be compiled to LLVM.

And those can be inserted directly into the runtime

without a need for any external data movement.

So there's prior art on having a standard memory

representation for, at least, analytic SQL systems.

The Apache Drill Project, if you're familiar with that,

is another SQL on Hadoop.

Not just SQL on Hadoop, but you can read from many systems

that are initially designed for Hadoop use cases.

It has a standard memory representation

for Hadoop use cases.

It has a standard columnar in-memory representation,

tabular data that can address a substantial subset of JSON.

The same is planned for Apollo.

We're hoping that we can create a format that

can be used amongst all of these systems.

There's already been a standard way, at least in open source,

of storing, an increasingly standard way

of storing compressed columnar data.

That's the Parquet project.

But the thing you have to realize about,

I don't know how much you all studied Parquet or columnar

formats, is that there's an explicit trade-off in systems

like Parquet, or tools like Parquet,

to maximize the throughput that you're getting out

of distributed storage.

So if you're on HDFS, or you're on S3,

the bottleneck in doing analytics

on data that cannot be all memory resident,

or all in RAM cache, is the slowest thing

is going to be the spinning disk hard drives.

It's more and more flash, and so the trade-offs

will change over time as increasingly everything

is solid-state disks everywhere.

But with these serialization formats,

they're designed for that trade-off

between IO and CPU throughput.

So compress and encode the data as compact as possible,

while also being able to blow it up

into fully materialized in-memory form

as you stream through the data to do analytics.

Another problem with this columnar serialization formats

is that there's not a standard data structure

to put the data into.

So if you look at the Parquet Java implementation,

and I actually have not, so I'm not an authority on the matter,

but basically data is being serialized

into native Java data structures.

If you're in C++, well, there's not even a standard C++

implementation of Parquet.

And so if you were in Python and wanted

to interact with data in Parquet to have an efficient data

structure to exchange among systems

that know about compressed, nested columnar data,

like Parquet, you'd be having a bit of a bad time.

So this is a major initiative that I'm working on right now

to create a standard data structure for in-memory data

coming out of things like Parquet,

but can be friendly for Python and used

to move data around amongst these analytical systems

with minimal serialization overhead.

Actually, as of the last week or so,

I have an implementation underway

that will all be open source.

We're trying to come up with a name for the project.

So as soon as there is a name, there

will be a GitHub repo with a specification for the data

structures and reference implementations

as soon as I'm not that embarrassed to show

my messy C++ kit to the world.

But basically, building it up to be able to create Python

bindings, to be able to interoperate

with systems that can emit, send, and receive data

according to that data structure.

So highly technical, but the grand goal

of writing more and more Python.

I think some people think of me as being ideological about,

it must be Python or it's crap.

But I don't really feel that way.

I think Python is a really great tool.

And the fact that you have a really accessible community

of developers and tools and a learning curve

that is not too steep.

that building software in Python makes a lot of sense

to reach a really broad audience of people

who can now tackle data problems that they couldn't have

five, 10 years ago.

So I like other programming languages as well,

but I think that Python is a really great place to invest

and to have as a primary language for data teams.

So anything that is blocking using Python

to solve certain classes of problems strikes me.

That's a real issue.

And so you need to be able to extend these systems

with Python code and to do it without trading away

major performance.

So having these common data structures

is a key part of solving that problem.

So that's my goal, being able to solve big data

without leaving the IPython notebook

or whatever Python development environment you prefer.

You want to be able to bring the software

that you build in Python with you

without having to throw it out completely.

So that means being able to use the existing Python data

ecosystem tools like pandas, Scikit-learn,

and so forth.

You'd like to be able to use them in a big data environment

without having to completely modify your workflow.

Obviously, you do have to write your algorithms in a way

that is amenable to the distributed computation model,

but all the software that's been created

for working at partitions of data locally on one node

should be able to use that software without hesitation

in a scalable big data environment.

So that's all the slides I have, but I

imagine there are some questions,

and so I can answer questions for five or 10 minutes,

and we'll stick around for a little while after the talk.

And if anyone has more detailed questions about the project

or wants to get involved, I'd be happy to talk.

Thank you.

Thank you.

Thank you.

Should we have some mics if there are questions?

Oh, yeah.

Can you repeat the questions?

I'll repeat the questions.

Yeah.

Hi.

Do you think when it's too late to get your time?

Yes.

I'm not sure what the timeline will be, but if that's personally important to you, I would love some help.

Just to give you a background, I've been using MacBook for a long time, and lately I've been doing a lot of complex stuff with live streaming using Python.

And that's a piece of pain to configure, but you can pretty much do whatever you want.

But if you add the level of specificity that you have, it will be a great thing.

Yeah, definitely.

I don't know what the timeline will be.

I guess it's a function of how much help I have, but I'm really keen to get basically a lot of the work in the project for adding SQL support

is mapping SQL built-in functions onto the Ibis operation classes.

And so the idea is every SQL dialect is a little bit different.

And so if Hive has an approximate median that uses count-min-sketch, you can map that function name onto the CMSMedian class, all the string functions, things like that.

So that's the main work.

It's a lot of legwork to wrap all the built-ins, but adding Hive support wouldn't be too terribly much work.

So it's wrapping built-ins, adding test coverage, and then also adding support for it.

Because Hive, I imagine a lot of Hive use is for ETL, so a big use case for Ibis is ETL workflows.

And so, yes, analytics, big data, interactive analytics, but also to be able to create complex ETL workflows that are all with Hive or Impala or some SQL dialect.

That's also to not have to orchestrate hand-generated SQLs is a big win.

Yeah?

It looks like you had the peak separation at about 2,000 for the erase on it, is that right?

Yeah, I was going to say something about that.

I think it's an issue with my methodology, and I think that what's happening around here is that garbage collection overhead, or there's some kind of memory throughput issue in my benchmarking methodology that's causing a problem.

And maybe right around here, you've got arrays that nicely fit, and L2 cache, and everything's fine.

I don't know, I'm not an expert there, but I need to publish the benchmarking code, and somebody will, I'm sure, sort that out for me.

So, in that example you showed for converting the large SQL query into multiple Ibis commands, is it all the intermediate steps being passed back to the memory in a local machine, or is it like lately, badly, like when it happens in Spark?

Yeah, so all the expressions are, oh, repeat the question, yeah.

So the question is, in the SQL example, breaking down complex SQL into multiple statements, everything you create is an expression, so it doesn't evaluate the expressions until you actually go to execute one of them.

So everything is deferred, so it's the same type of model as Spark or other DSL type systems, that you build, effectively, computation graphs, and then those get compiled.

So, I think that building Spark support into Ibis is also something that would be really interesting.

So I think that the Ibis DSL maps nicely onto Spark data frame operations, and so you can think of Ibis as sitting one layer above API access to the Spark computation model.

Okay, so was it possible that you could have done this what Cascade did?

Something at a SQL layer that other people also could leverage, and not just Python, but the general community, where you're at a distributed layer above the SQL, the JDBCs would pull in, and then you get access to it.

Do I need to repeat that?

So the question is, is it possible to create a layer that can be taken advantage of by other languages or other environments?

I'm not quite sure. I guess I would need to see what that looks like exactly.

So one major artifact that will come out of this work is Python.

having a well-defined, efficient, external way

to extend systems with other code.

So I'm focused on, let's make this work with Python,

but for it to work with R and Julia or arbitrary code

that you write that knows how to read and write

the same tabular data format.

So that's definitely something that is in scope.

I also want to see the same tabular data format

make its way into Spark.

And so we can get faster UDFs in PySpark.

So as far as the SQL generation DSL,

it's very coupled to the Python API.

So hypothetically, if you wanted to generate SQL,

you could generate Python code, which generates the SQL.

And that might be easier to generate than SQL itself.

So I don't see any problem with that.

But I guess it's turtles all the way down.

SQL's not going anywhere.

So generating SQL's a pretty good bet.

Have you looked at the data frame

that adapts how it contributes to Spark?

I have looked at it.

The question is, have I looked at the Dotto data frame

library?

I have.

And it's a very nice piece of software.

It's about 150,000 lines of C++11.

There's a lot of Python, too.

It is definitely a large code base.

It is definitely tailored for machine learning,

in both a good and a bad way.

I don't know what the bad is.

But if you look at it, it's like, yes, this

is designed to maximize usefulness

for machine learning.

So I'm happy to see better, scalable, in-memory,

out-of-the-port data frame libraries.

I've encouraged them to look at interoperability

with the analytics SQL systems for Dotto's S frame.

Would there be any practical limits

in terms of the size of the data?

And also, what do you estimate is the performance?

The performance and scalability is

limited by the underlying compute.

So in a sense, as Spark and Pala,

big data compute systems get faster and more scalable,

then tools like Ibis benefit directly from that.

In the UDF case, where you're extending the system

with Python, there will be overhead.

I don't have an estimate of what the slowdown would

be over hand-coded C++ or hand-coded Java.

But the goal will be to bring them as close together

as possible.

I think that in benchmarks of by-code versus hand-coded C,

it's often able to get within a factor of two, three.

So that would be our target, I think.

So how about latency from the perspective of the UI?

Yeah.

So I know that so Analytics SQL, latency

between 100 milliseconds and a second

tends to not be that much of a priority.

Between one second and 10 seconds

is where a lot of the optimization and latency

query throughput is taken into consideration.

So systems like Apollo, you have code gen that takes place.

So if you're operating on 100 terabytes of data,

then the code gen time of generating

LLVM specializations for a query is relatively trivial,

because the query might take tens of seconds or minutes.

But again, it depends on the data.

It depends on what you're doing with it

and underlying how the data is stored,

whether it's how it's partitioned.

How is it stored?

Is it Afro?

Is it Parquet?

Is it S3?

Is it HDFS?

How's your HDFS tuned?

There's a lot of factors.

I also have one more question.

So would machine learning be a use case,

or is that not a use case?

It is definitely.

And I think, in general, to the extent

that machine learning models can be rewritten or designed

in a way that's amenable to the distributed model,

CS systems like Matlib, which are kind of in-database

machine learning, Spark MLlib, same thing.

Machine learning models are rebuilt for the Hadoop type

architecture in mind.

And so being able to access machine learning

[1:00:01] models from a system like this, because you'd

[1:00:04] like to be able to do your ETL, feature engineering

[1:00:07] analytics, and then machine learning

[1:00:09] within the same cohesive workflow

[1:00:12] without having to step outside the workflow whenever you need

[1:00:17] to do more advanced analytics.

[1:00:28] Are there any more questions?

[1:00:29] Should we wrap up?

[1:00:33] Well, let's thank our speaker.

[1:00:35] Thank you.

[1:00:36] Thank you.