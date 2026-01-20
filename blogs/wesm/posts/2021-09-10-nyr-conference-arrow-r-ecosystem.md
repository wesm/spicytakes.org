---
title: "Apache Arrow and the R Ecosystem"
summary: "Talk at New York R Conference"
date: 2021-09-10T00:00:00
tags: ["talk", "transcript"]
slug: nyr-conference-arrow-r-ecosystem
word_count: 4375
source_file: transcripts/2021-09-10-nyr-conference-arrow-r-ecosystem.md
content_type: transcript
event: "New York R Conference"
video_url: "https://www.youtube.com/watch?v=u7DecbDw3QE"
---

{{< video https://www.youtube.com/watch?v=u7DecbDw3QE >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I provide an update on Apache Arrow's progress and its growing integration with the R ecosystem. I discuss the formation of Voltron Data (merging Ursa Labs with GPU computing work from RAPIDS and Blazing SQL), the Arrow R package development with dplyr integration, and the semantic versioning approach adopted since Arrow 1.0. I share benchmarks showing Arrow-powered dplyr queries outperforming base R by 3x on single files, and the ability to query 40GB datasets in just over a second through smart file pruning. I also cover Arrow Flight for high-performance data transport, DuckDB integration for SQL functionality, and the emerging Substrait project for creating a common compute representation that can bridge different query frontends (SQL, dplyr, Ibis) with various backend engines.

## Key Quotes

> "The Arrow project was conceived to provide a language independent foundation for analytical computing focused on data frames and tabular data."

> "Arrow has become one of the de facto, if not the de facto standard technology for connecting external data sources to the data science world."

> "Rather than having to serialize data every time you move data between a different environment, we have a common data representation that can be shared without any copying or conversion between Java and C++ or Rust and Go or Python or R and JavaScript."

> "We analyze these expressions and use them to prune files from having to be scanned or to do filtering within the files to limit the amount of data that we have to decode into Arrow format."

> "We're able to evaluate this dplyr expression on a 40 gigabyte data set in a little over one second."

> "If you're familiar with ODBC or JDBC, we want to replace those more inefficient transfer protocols, interfaces to database systems with one that is Arrow-based."

> "We are working with a bunch of open source developers to define and specify an intermediate compute representation which can bridge the gap between these different frontend interfaces."

> "You can choose the API that suits you best, and you can drive as many different compute engines as you have available to you without having to significantly rewrite your code."

## Transcript

**Jared Lander:** He is one of only two people besides me to speak at every single New York R conference. Him and Dan Chen have spoken at every single one of them, which is all the more remarkable because the next one is probably most famous for Python. Actually, now I realize Dan Chen wrote a Python book, but Dan Chen does both languages and now our next speaker does, too.

I used to have a lot of fun trolling him at these conferences. It doesn't feel the same when we're not in person, but also he's contributed so much to the R community now, it doesn't feel right to troll him. Don't get me wrong. As soon as we're back in person, I will start trolling him again. I will absolutely have a fun time doing this, just because that's what you do to a good friend. You troll them when they're in enemy territory.

But he's not really enemy territory anymore because he's contributed so much to the R community now that we can't just make fun of him for being Mr. Python. So I want to sing his praise a little bit more, and I joke about Python, but he is the reason Python became a data science language. Without Wes, I don't think that would happen.

So the data science community owes him gratitude for that, but he's since moved on to doing even more stuff that's also been transformative of the data science community. So he's had at least two transformations of an entire field of work. So sorry if that was too much praise and not enough trolling. Everyone please welcome Wes.

**Wes McKinney:** Thank you, Jared. Thank you. All right. I'm live. All right. You can see me. All right. Let me fix my slides here.

I regret that we cannot be together in person, but I hope to see everyone at a future in person New York R conference. I'll keep my fingers crossed for 2022. It's been interesting to be here every year and to be speaking about very similar topics, but it's good in that each year passes by and we have more and more interesting things to talk about and definitely a lot more work that is bringing value to the R community and increasing the kinds of things that the increasing the computational capabilities that are available for our programmers.

So as Jared says, I've become more of a polyglot as time has gone on, but that was always the intention with the Arrow project. So I'll share with you some of the new things that have been going on and some of the things to expect over the coming year and beyond that you can use now and things that you can get excited about.

So for those who are not aware, the Arrow project was conceived to provide a language independent foundation for analytical computing focused on data frames and tabular data. It wasn't just created for the data science ecosystem, but was also intended to bring better interoperability to database systems, big data systems, but also to provide an efficient bridge between the big data and database systems world and the data science world.

And since then, we've been working on doing development in the project seemingly, it feels like a long time now, but it has been a little over five years of active development. We had maybe another six months of active planning before that. So I've been working on the project for a little over six years now, but it's grown to encompass many programming languages.

And happily for data science users, it has become one of the de facto, if not the de facto standard technology for connecting external data sources to the data science world and for getting data out of traditional database systems, data warehouses, being able to load data more quickly so that we can work more efficiently and get more work done in languages that we love like Python and R.

I knew that starting out that Arrow was going to be a large project that required a lot of people. I started out the project with a large group of open source collaborators. I was at Cloudera working with folks on projects like Impala and Kudu at Cloudera. I moved to New York in 2016 to join Two Sigma because Two Sigma was really excited about Arrow and was offering a lot of sponsorship and support for my work.

But in 2018, it became apparent that Arrow was an important part of the future growth of the data science and database ecosystem. And there were many companies, including hardware companies, other financial firms that wanted to support Arrow development. And also, RStudio said, hey, what about R?

And so we came up with the idea to create this cross kind of multi, this industry consortium model to fund Arrow development for a multi-year period that was, most of the funding came from RStudio. RStudio also provided the administrative support for Ursa Labs, but we were able to get funding from a wide variety of sources and that enabled us to operate a team of full-time developers building out the Arrow project, building out integrations with the data science languages.

So I would say that Ursa Labs was really successful and enabled us to grow the project to where it is today. We realized last year that to enable Arrow to reach its next stage of growth, that large companies, in order to adopt Arrow more wholeheartedly in their systems, that there needs to be larger, software companies with a larger scope that can build products and services to support enterprise adoption of Arrow.

So we saw a lot of interest in adoption of Arrow, use of Arrow, and other software products, but the absence of a software vendor that could support enterprises through their adoption of Arrow was holding back the ecosystem. So we pivoted from Ursa Labs to Ursa Computing. We raised some venture capital from our friends at GV to fund our growth. So that occurred late last, early fall in 2020, and we were able to continue to grow the team throughout 2020 and early 2021.

The thing that kept me very busy this year, we saw an opportunity to bring together a number of forces from the Arrow ecosystem who had been building accelerated computational technology for Apache Arrow, in particular, computing pioneers from the GPU computing world. So folks from the Rapids project, as well as Blazing SQL, which is a distributed SQL engine built on top of Rapids.

And so we said to ourselves, we could have disparate efforts to create computing systems to bring accelerated computing for Arrow users, or we could bring all of these forces under a common umbrella to create unified technologies, unified systems to make it easier for people to use Arrow everywhere.

And so we have called this new company kind of reflecting the joining together of forces. We've called this company Voltron Data, and we are working, we are growing a large team. We have around 50 people, and we are working for the benefit of the Apache Arrow ecosystem, the growth and adoption of the project, as well as creating optimized algorithms and computing technologies across programming languages and hardware, and everything is based on Apache Arrow.

Reflecting the change in name and the change in our expanded scope of our mission, Ursa Labs lives on as Voltron Labs, and we will continue to grow and develop our open source team and our relationship with other open source projects and take on sponsorship and funding for our open source work in the Arrow project, as well as the greater, you know, the Arrow cinematic universe as it is now turning into.

So back to Arrow. So when we started out building Arrow, we developed a language-independent universal columnar data format for data frames and other tabular data, and the idea was to standardize the memory representation so that data could be shared portably across programming languages, and that we could also share algorithms between different computing environments.

So rather than having to serialize data every time you move data between a different environment, we have a common data representation that can be shared without any copying or conversion between Java and C++ or Rust and Go or Python or R and JavaScript, and so that might be sharing data within process or moving data from process to process, and we've developed protocols and interfaces to enable seamless interoperability at those language and system boundaries.

And the growth, you know, the growth in the community, we now have a dozen programming languages represented, you know, some of the recent additions to the ecosystem include MATLAB and Julia, so we're very excited about that, and we expect that things will continue to grow rapidly there.

In addition to the data format and libraries that we've built for getting data into that format, so many R users are familiar with our Arrow has unlocked the ability to read Parquet files, and so we read data into Arrow format from Parquet, and then we load it into R from there.

But Arrow has spawned a number of additional subprojects, and one that we're really excited about that I've spoken about at this conference in the past is Arrow Flight, which is designed to be a new network data transfer protocol to replace old and slower interfaces for moving data between systems.

So, for example, if you're familiar with ODBC or JDBC, we want to replace those more inefficient transfer protocols, interfaces to database systems with one that is Arrow-based. So, firstly, if you have two systems that if you have a system that consumes Arrow, and you have a system that can send Arrow using Arrow Flight, then you don't have to do any conversions when you receive the data.

And so we would like to see as many data storage systems and data warehouse systems adopt Arrow as their adopt Arrow Flight and being able to deliver Arrow data natively to Arrow users, including people working in Python and R. So when you pip install PyArrow in Python, you get a flight client so you can connect to flight servers.

We've developed a prototype interface to flight in R as well, and we think this will be a major source of growth to make it to expand the number of data sources that Arrow users have access to natively.

I would be remiss to mention that one of the things that we are actively working on in the open source project right now is developing a standard for connecting to SQL databases with Flight. Flight is a low-level protocol, and does not contain any notions of SQL like user sessions, shared statements, and the other things that you would find if you were using Postgres or SQLite.

So by creating a standard SQL database middleware, we can simplify the process not only of database vendors implementing Flight, but also as users that you have a standard SQL middleware for connecting to, for example, Postgres or another SQL database system, and you get the results of your queries back to you in Arrow format.

So, the Arrow R package wraps the C++ API using CPP11. You can install it from CRAN like you would any other R package. We've laboured very hard to make this possible and seamless, but if you're interested in following the upstream development, we also have nightly package builds that you can install and get access to the latest features.

And we are always interested. These are not production releases, but we are always interested in having folks from the R community engaged in the development process, giving us feedback on what's broken, like what's not working well, what's slow, like what sorts of features they would like to see.

And the major releases, as I'm about to mention, or about to tell you about, are a little bit slower, a little bit more conservative, so using the nightly builds for developers, you can give us a faster feedback if you're comfortable being on the bleeding edge and seeing your R interpreter crash occasionally.

All right, so, releases of Arrow, we started the project in 2016, and we there were 17 major releases up until our 1.0 release at which point we declared the Arrow format stable, and we moved to semantic versioning. So you maybe have seen that the version numbers are starting to go up more aggressively, and that's because we've moved to a semantic versioning model.

So we do coordinated releases of most of the language libraries and bindings, that includes the R package, so when you see the 5.0 version of PyArrow and the 5.0 version of the R package, we intend for the versions to roughly correspond to each other. And so, while there are some new changes, and non-backwards compatible changes that occur at the API level, at the Arrow format level, things remain stable.

0.14 in 2019 was the first CRAN release, and over time, we've steadily been adding new features to the R library, which I will show you some of the new features that we have, and we've worked to make the installation process more seamless while bringing you as much out-of-the-box functionality as we can without you having to get into the details of how to build and attain the growing number of dependencies that the Arrow package has in R.

So, one of the major growth areas and focuses of the R package development is that we want to provide really seamless integration with dplyr and the tidyverse. This hasn't come all at once, so we've had to implement dplyr verbs on a bit-by-bit basis, and that's because we're working to implement this computational functionality in the R package itself.

So, in the 0.16 release, we released the very preliminary support for the select and filter commands in dplyr. In the 2.0 release, we brought Amazon S3 support, so if you have data that lives in parquet format in an S3 bucket, you can directly access that data using the Arrow package and query that data with the dplyr API using that support.

In the 4.0 release earlier this year, we dropped support for mutate and arrange. We're, of course, working to add as much feature coverage in terms of what you can do inside of these functions. So that we have provide mapping between, because we're executing R expressions natively on Arrow data format which is not the same as R's data frame format.

And so, whenever you have, because these are all non-standard expressions in R, so, when you write an R expression, we have to map the R function onto the corresponding Arrow function, and if you use an R function that we don't support, you may get an error, and then you can open a bug report, or a feature request, maybe a better way to put it, and we can implement that function and provide the mapping in the R library, so you get seamless dplyr querying capability.

Since 4.0 and 5.0, we've rapidly expanded the functions that are supported from within the dplyr verbs to now more than 250 functions. That number continues to expand, continues to expand rapidly, and very excitingly for people who are, who want to crunch very large data sets in the 6.0 release which is coming up later this fall, we will finally have support for Summarize and Group By which will unlock a lot of interesting workloads on very large data sets.

So, to give you a sense of like how all of this works and how the pieces fit together, so this is the baseline, this example shows you the baseline performance of dplyr on an R data frame. So here we're using the Arrow read parquet function to read a single parquet file, the as data frame argument asks Arrow to turn the Arrow data into an R data frame, and then everything from after this point, everything from after this point is using dplyr on R data frames to crunch, to crunch the file.

So we have a 10 million row parquet file, 250 megabytes, this uses a lot of the major dplyr verbs and this runs in about 1.6, 1.6 seconds.

So, if you set as data frame false when you read the parquet file, then the data is read into memory as an Arrow table instead, which is a more memory, it's a more compact and memory efficient representation of the data in many cases, and the Arrow format is really optimized for processing numeric data as well as string data, so you see a lot of efficiency benefits when processing a lot of, a lot of string data.

But here we use all of the same dplyr verbs as we did in the, the R data frame example, and at the very end when you call collect, it's at that point that the Arrow data that's output from the, the last dplyr verb is converted to an R data frame.

And so changing just from the R data frame format to the Arrow, Arrow format, we go from 1.6 seconds to 0.6 seconds on the same, on the same data file, so we get a lot, so we get a lot more efficient processing as well as a lot less memory use. So if you look at the memory footprint of this operation, the Arrow version uses significantly less memory.

Now, let's ratchet up, you know, ratchet up the data set size, so suppose you have not just one parquet file but a ton, like a hundred, or here I have 125 parquet files, so now we're not talking 250 megabytes, it's 40 gigabytes of parquet files spread across 125 files, 2 billion rows.

And so Arrow has this special open data set function which allows you to address partitioned directories of parquet files or CSV files, and then you can query a collection of these files using the same dplyr interface exactly as you would a single R data frame or a single Arrow table.

And what's exciting about this is that we analyze these expressions and use them to, to prune files from having to be scanned or to do filtering within the files to limit the amount of data that we have to decode into, into Arrow format.

And so that enables us to do direct querying on these extremely large data sets while pulling very little data into memory, and so we're able to evaluate this dplyr expression on a 40 gigabyte data set in a little over one second.

And this is partly fast because Arrow is fast, but it's also taking advantage of this static analysis of these dplyr expressions to not scan more data than we need to, so very exciting.

Some new functionality that's dropping, I know I'm running out of time, so I'll go quickly through this, but if you've heard of the DuckDB project, another very exciting analytic, analytic database process, analytic database project, you can seamlessly transfer data into, into DuckDB and use DuckDB for querying.

So here when you use the toDuckDB function, it returns a dbplyr object, and so subsequent dplyr expressions are getting translated into SQL by dplyr and then allowing DuckDB to, to process, to process the data.

And DuckDB has very comprehensive SQL functionality and supports a lot of query, query processing that Arrow does not yet support yet, and so this can help you, help you in your work, and the cool thing here is that it, it composes very naturally with all of the other Arrow machinery, including the Arrow dataset machinery, so you get to reap the benefits of both worlds.

So we're working, you know, very actively to bring comprehensive querying capability natively within the Arrow C++ libraries, which will be made available to our programmers through the dplyr, dplyr interface, so you can see, you'll, you can expect to see more of these coming in subsequent releases.

So I expect we'll have a lot more to talk about a year from now, and I look forward to sharing all of those improvements with, with you.

Since, you know, some of you use Python in R, so you might say, well, where's all, you know, when did the Python programmers get to, to join in on all of the fun, and some of you may be familiar with a project called Ibis, which I would describe as a kind of dplyr-like project for, for Python, and so we are working to enable the same kind of dplyr-like querying ability using the, the Ibis project, which enables the same kind of static analysis of expressions that we have in dplyr from, from Python.

So, so this being said, there, you know, there are, you know, many query engines in development that know how to process Arrow, the Data Fusion project is written in Rust, and so that's another Arrow query engine project you can, you can take a look into.

My team, you know, our team at Voltron is very focused on the C++ project and its interfaces in Python and R, but we are working to deliver fluent computing interfaces in, you know, in multiple programming languages, so we will expand beyond Python and R in the future.

So a kind of, to last, last item to leave you with before I, I leave, since I've, I've overstayed my welcome, but one of the problems we're working actively right now to address is the problem of fragmented user interfaces to different backend computing engines.

So some engines speak SQL, some, some systems have their own interfaces like dplyr and Ibis, and that creates this, like, you know, pair to, point to point problem of, like, how do these query frontends communicate with all of these different query backends, and that, and that creates a lot of headache for users because you have to think, like, okay, what API do I want to use to communicate with this compute backend?

So we are working, you know, with a, a bunch of, a bunch of open source developers to define and, and, and specify an intermediate compute representation which can bridge the gap between these different frontend interfaces, whether data frame interfaces, dplyr, and, and backends so that you can choose the API that suits you best, and you can drive as many different compute engines as you have available to you without having to significantly rewrite your code.

This will obviously take a long time to deliver, but something we're, we're very, we're very excited about. So we're, in the Arrow community, we're actively discussing this, we've getting, begun to collaborate with folks outside of the Arrow community to create a common compute representation to bridge frontends to backends, and so we expect that this will be an important kind of element of the future growth of the ecosystem.

So if you're interested in this, there's a new open source initiative called Substrait, you know, we're involved in this, and we hope to enlist more folks from the community in making this a reality.

So thanks again for, for, for having me, and I look forward to seeing you hopefully in person next year, but otherwise, you know, we, we love to hear from you in the Arrow, Arrow community, and we look forward to continuing to power up data science in R. So thanks, thanks again.

**Jared Lander:** So you heard it, Wes is already confirmed for next year. So good, he'll be in eight years in a row, so you got to make sure Dan Chen is there as well, and ready to do that.