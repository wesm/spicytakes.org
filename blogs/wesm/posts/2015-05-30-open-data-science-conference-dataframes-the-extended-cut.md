---
title: "Wes McKinney at ODSC Boston 2015 - DataFrames: The Extended Cut"
summary: "Video at Open Data Science Conference"
date: 2015-05-30T00:00:00
tags: ["video", "transcript"]
slug: open-data-science-conference-dataframes-the-extended-cut
word_count: 7926
source_file: transcripts/2015-05-30-open-data-science-conference-dataframes-the-extended-cut.md
content_type: transcript
event: "Open Data Science Conference"
video_url: "https://www.youtube.com/watch?v=ss5-9TQ0rUI"
---

{{< video https://www.youtube.com/watch?v=ss5-9TQ0rUI >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This talk argues for moving beyond "language wars" to build interoperable infrastructure serving Python, R, Julia, and other ecosystems. I gave a shorter version at the New York R Conference a month earlier; this is the extended cut.

## The Great Decoupling

I see a meta-trend in data systems: "the great decoupling." In the past, data systems were vertically integrated—API, storage, and computation all in one library. This makes code sharing hard: "you start using pandas, or you start using R, or any table library, and you're kind of locked in." If you want to switch tools, you have to rewrite everything.

The decoupling separates storage (letting someone else handle distributed storage problems) from computation (making analytics fast and correct) from user interface. "The language wars... are kind of counterproductive, given that we're all in this together, we're just trying to be better data scientists."

## Composability vs. Usability

Coming from a math background, I think in terms of composability: "I like to write theorems, and improve things, and create lemmas, and then you compose them all together." Well-designed systems build "a pyramid of abstractions that all fit together in a nice way." But purely computer science approaches often sacrifice usability. The key question: "If I switch from this function to that function, do I have to look at the documentation to remember how things work?"

## The Five-Way Coupling Problem

Current data frame libraries couple five things: API (code you write), in-memory representation, serialization, computation implementation, and code evaluation. This coupling fragments the ecosystem. Because "all of these libraries have developed organically, including pandas... there was never any design effort in the community, like the R and the Python people never got together and said, how can we build a better data frame."

## The Benchmark Trap

"For any given set of systems, there is a benchmark such that one of the systems will come out on top." Like statistical multiple testing where you keep running tests until finding p < 0.05, developers can cherry-pick benchmarks. "Whenever you see a benchmark, please ask questions."

## Memory Layout Matters

Columnar layout excels for analytics: "suppose you have a really wide table with a thousand columns, and you're only interested in two or three columns for a particular operation, that's really fast because you can access those two or three columns without having to touch any of the other data." Projections and column additions happen without copying. But single-row access and appending rows suffer.

## The JSON Challenge

Most web data is JSON with nested schemas—structs, lists, maps. But "this kind of data is really hard to work with in a data frame." The typical approach: "you would flatten it out into either one big table or a bunch of tables, and you would duplicate the data." Analytics on nested structures becomes "hard to express and slow."

## The CSV Problem

"It's like CSV or JSON, probably in over 50% of cases." Binary formats like Parquet are better—faster, preserve types—but "there's no consensus on like what is the best binary data format." Library support is weak, so "everyone just defaults to CSV files."

## Missing Data

"One of the big regrets that I have about pandas" is the missing data handling. We tried to match R while working within NumPy's constraints. The best approach: "just have an extra bit or byte that you carry around where you say whether something is null or not null." More memory, but "regardless of the data type" you have consistent null handling.

## Current State

dplyr has "really transformed the R programmer's workflow"—it's "a domain-specific language embedded within the R language" that can target both in-memory data and SQL databases. Spark DataFrames follow similar decoupling principles.

pandas "has been around for years, but certainly not the ultimate data library." The internals are complex: "If you go digging, like what's inside a pandas data frame, you might be surprised." The only major internal redesign was summer 2011, working independently with particular use cases. "If we went and redesigned pandas from the ground up, there would be a lot of things that come out differently."

The Blaze project has "one data expression API, and many different execution backends, including pandas and SQL."

## The Path Forward

"Figuring out how to share code amongst the data science community" is critical. "With all the language wars, it's created division and unnecessary barriers to collaboration." Building DataFrame software usable across Python, R, and Julia—and interoperating with Hadoop and Spark—"is the big challenge for the next five or ten years."

---

## Key Quotes

> "The language wars... are kind of counterproductive, given that we're all in this together, we're just trying to be better data scientists."

> "For any given set of systems, there is a benchmark such that one of the systems will come out on top."

> "You start using pandas, or you start using R, or any table library, and you're kind of locked in... if you want to switch from one tool to another, you have to rewrite your code."

> "One of the big regrets that I have about pandas is the missing data handling."

> "If we went and redesigned pandas from the ground up, there would be a lot of things that come out differently."

> "The R and the Python people never got together and said, how can we build a better data frame, how can we share code, how can we make our data and our implementations more interoperable."

> "Suppose you have a really wide table with a thousand columns, and you're only interested in two or three columns for a particular operation, that's really fast because you can access those two or three columns without having to touch any of the other data."

> "An extraordinary amount of compute cycles are being used right now just transforming data from one format to another, and that seems like a big missed opportunity to me."

---

## Transcript

Thank you, Andy.

Thanks, everyone.

It's early for a Sunday morning, so I'm hoping the caffeine kicks in here.

Working on it.

Working on it.

Well, I gave a version of this talk at the New York R Conference a little over a month ago, and that was only a 20-minute talk.

This is a 40-minute talk.

So there's a little more content here and can go a little deeper into some of these topics.

So yeah, we'll have some time for questions at the end.

So I've spent the last number of years building some version of data frames or tabular data interfaces.

This is a bit of a meta talk about all the data frame interfaces and what we can learn from them, maybe what are some of the problems that still exist.

You would think that in 2015 we wouldn't still be having problems with, you know, infrastructural problems with tabular data, but we do, and so it's worth talking about what those are and what we, the community, can do about them and how we can work better together.

And of course, there's lots of opinions here.

I do work for Cloudera now.

You know, there's a whole story there, but, you know, we're working for a bigger company, so these are my opinions and not necessarily the opinions of Cloudera.

So keep that in mind.

And it's definitely a nuanced discussion, so I haven't really stated anything here as fact.

I think there's definitely, you know, shades of gray with, like, all of these issues, and, you know, I think you should keep that in mind when giving consideration to any particular item.

Probably a lot of you are familiar with my background.

I started working on the library that would become pandas in April 2008.

I was working in quant finance at the time, so I was really interested in doing analytics and doing data analysis in Python, but there really wasn't, it was this chicken and egg problem where no one was doing data analysis in Python.

At least Python was really successful for scientific computing and numerical analysis as, like, a MATLAB replacement, but it hadn't really gotten any traction in statistical computing or, you know, when people say data analysis on the West Coast, it more means, like, structured data manipulation, like tables and SQL queries and all that kind of thing.

So Python really hadn't been used for all that kind of thing, that sort of stuff, like, you know, interacting with SQL databases was just not on the scientific Python community's radar at that point in time.

I spent a few years in finance, took some time off to work on open source, wrote my book, which probably a lot of you own, and, you know, I decided to take a break from earning income to make the Python data ecosystem more viable.

So I don't think we're completely there yet, but it's certainly a lot better than things were looking in 2010.

I started a company with Chang She, who was one of the early pandas contributors, and, you know, was a former colleague of mine.

We worked on that for a couple of years, and we now work at Cloudera as of, you know, October.

Hasn't been all that long.

So a data frame, you know, as you're probably all aware, is what I call a table-like data structure, and it varies a lot from library to library, but you can, data frames are more of a user interface than they are a data structure, so there's plenty of tables that exist in the wild that people don't think of as data frames, or, you know, the way that you interact with them is quite a lot different than, you know, the code that you would see writing in R or writing in pandas.

There's a lot of different ways that people look at these tools, so I'm going to talk quite a bit about the internals of the data structure and how that impacts things, but, you know, there's the API, like how you, like the code that you actually write to interact with the data ends up being one of the most important factors, because, you know, underneath there's just some bytes and some columns, you know, either in memory or on disk, and the thing that sets the libraries apart is, first of all, is it easy to express your computations?

Can you write down in a succinct way, like, what you want to do with the data, whether that's building a model or doing some analytics or doing some data transformation, you know, whatever the task you have at hand, like if you're spending all your time just figuring out how to express, you know, getting from point A to point B with the data, and that is really hard, then that's a problem with the library, but beyond that, there's a lot of just implementation issues of, you know, how fast, you know, how much memory does the library use, the data frame library, how fast are the operations, and those can impact you as well, so it's kind of like, there's like a hierarchy of needs of data analysis, like does the code work, like is it nice to use, is it fast, you know, does it run out of memory, like these are all like really critical matters, can you read the data that you have on disk, you know, really simple things like just being able to read the CSV file that you have in front of you is really important, so the meta trend that I see going on with the general, general data ecosystem is what I've, you know, my term for it is the great, like the decoupling, which is to say that, you know, in the past, you know, data systems were very integrated, so you'd have like all of the things in one place, you'd have a completely like a walled garden kind of implementation where you'd have your API, and you'd have your storage, and your computation all in the same library, and the problem with this is that it makes code sharing hard, and you know, you start using pandas, or you start using R, or any table library, and you're kind of locked in, in a way, because all of your code is very specific to the implementation and the low-level design of that library, and so if you want to switch over from one tool to another, you're a little bit stuck, like you have to rewrite your code, it's, you know, there's a bunch of problems there that I'm going to talk about, but one of the really great things about, you know, this decoupling that I see happening is, you know, the data's getting bigger, so that means that the storage problem, you're not going to want to deal with terabytes and petabytes of data, you want to let somebody else be responsible for that distributed storage problem, and all of the fault tolerance, and high availability, and replication, and all that stuff, the problem of, you know, I have some CSV files on my hard drive, you know, for small and medium data problems, that's completely fine, but if you're dealing with, you know, as they say, you know, big data is largely medium data collected over time, so you might have medium data on any particular day, but if you wait long enough, you're going to have big data, and you don't want to have to deal with that storage problem as a data scientist.

There's the other question of the data's getting bigger, and it's more complex, and, you know, implementing analytics and making it fast and correct is tedious, and it's a lot of work to make a lot of the analytics fast, and so you would like for, you would like for the work that happens to make the code fast, to make it correct, to make it well tested, you would like for as much of that code to be shared amongst the broader as possible, so that we aren't getting into this, you know, I'm going to talk some more about this, but I think one of the symptoms that we see is like the language wars, unfortunately, which really are kind of counterproductive, given that we're like, we're all in this together, we're just trying to be better data scientists at the end of the day.

I think there's a lot of work to do, you know, my prediction is maybe in 10 years, like, you know, life will be better, but there's a lot of work to do to get there.

And over the years, over the years, I've become really opinionated about how to build, how to build data tools, there's different schools of thought, you know, some, some developers who are more, have more computer science, I don't really have a computer science background, I have a math background, so I think about the world in terms of like composability, I think.

I like to write theorems, and improve things, and create lemmas, and then you, you kind of compose them all together, and then you can, you can prove something really interesting by composing a bunch of pieces together, and it's quite a lot like building, building software, and so if you design your systems to be composable, and to fit together nicely, then you can, you can build up something really nice from like this kind of pyramid of abstractions that all fit together in a nice way.

And a lot of computer scientists feel, feel the same way, and, and approaching like a data problem, saying, you know, well, what, you know, what are we doing at a high level, like let's break that down into small components, and then we'll fit them all together, and then that will implement a system that can solve a problem, but what gets lost in that process is often the, the usability aspect of, of not, you know, eating, eating your own dog food nearly as much, and stopping like every, every time you build a thing, and say, well, is this easy to use?

If I switch from this function to that function, do I have to look at the documentation to remember how, how things work?

Are the argument names consistent?

Is the, is the, the way that you write the code from step A to step B internally consistent?

And I think one of the big things that's happened between now, you know, looking at today versus, you know, five, ten years ago, is that I think there's now general consensus in, in the, you know, the R and Python communities that this kind of usability problem is a real problem, and one that merits, you know, thoughtful consideration.

If you look at, you know, all of Hadley Wickham's libraries in the R, in the R ecosystem, they're well implemented, and they're, they're, you know, one of the big, you know, benefits of dplyr is that, the fact that it's fast, but the, the thing that's really special about it is the fact that it's internally cohesive, and it presents like a, like a nice flow to work with the data that's very productive.

So I also think that, you know, you as a discerning data scientist who are evaluating software that somebody else has built, when you pick up a new piece of software, you might ask yourself, well, how do I evaluate this?

How do I know whether or not this is trustworthy, and whether I should be, you know, more or less betting the mortgage on a piece of software?

And I think that, and you can ask people, like there's this social proof thing, where, you know, if you see somebody that you trust using a piece of software, you say, oh, well, so and so is using, you know, such and such company is using this software, and if it were bad software, they wouldn't use it, because that would be irresponsible.

But a thing that you can do that is easy is just to look at the tests, and to see, first of all, like what is the development team, what is their approach to testing?

Is it, you know, a bunch of special cases kind of tossed, you know, into a big file?

Is there a systematic approach to, you know, like how systematic is the approach to testing and ensuring the correctness and performance of the code?

Performance often doesn't get tested, and that's unfortunate, because often performance is tested in production, and you only find out that the code is made slower after you've already cut a major release, and that might require, you know, it'd be nice if with every change that's made to a code base, if you had like a very precise view of like how that impacted the performance of real world, you know, downstream use cases, and I'm sure it's all, it's happened to all of you, that you've, you upgraded the library and found your code gets slower.

There's nothing really more frustrating than that, and diagnosing that is very difficult, can be very difficult.

So the, yes, so as I was saying, you know, the big issue that we have right now is this coupling amongst, you know, I guess, let's call them these five key areas, you know, the API, the code that you write, the, how the data is laid out in memory, so that's the low-level details of the data structure.

So when you have a data frame in R, you know, for data scientists, I would say that these really should not be your problem, and these are the things that you don't want to think about, but I just want to raise your awareness about them.

But the, the way that the data is actually laid out in memory is, is, makes a big, makes a big difference.

It affects everything downstream, how everything is implemented, how fast it is, how much memory it uses, so it's, it's certainly, it's certainly an issue.

One that, a thing that's not talked about as much is how data is, you know, serialized and deserialized.

If you're not familiar with, with the serialization term, serialization just means conversion to and from some other format that can, you know, usually can be read by others, so whenever you read a, read a CSV file, that's, you know, people call that deserialization, and writing a CSV file is serialization, and there's good reasons for writing CSV files, and there's really good reasons to not write CSV files.

There's the question of the actual computation, how is that implemented, and that of course depends on the, you know, prior items, and then kind of a software issue is how the code that you write relates to how it's evaluated, so when you write a statement, is it immediately executed or is there some kind of, is there some, like, optimization system that rewrites your logical, your logical data expressions into a more efficient format, and one of the big issues right now is that code sharing is difficult, and for a number of reasons, and as a result is really not happening, and so I want to talk a little bit about the in-memory data representation issue, that if you write an algorithm against a data frame, there's several things that it relies on, and I listed them out here, so first is, like, how the data actually lives in your computer's RAM, so if you have a column that contains numbers or contains strings, depending on, you know, the library that you're using, the programming language, you might have a column that looks like an array of strings, but those strings may not be next to each other in memory, they might be pointers into some other part of memory, they might be all contiguous, you know, next to each other in memory, you know, it's an important factor, there's the question of the type system, so if you have a string, if you have a number, how is that physically represented in memory, if there's some support for missing data, how is missing data handled between all of the data types, and then how is memory allocated and deallocated, in particular, how much control the developer has over the memory management has a big impact on all of the code that he or she writes, and, you know, because all of these libraries have developed organically, including pandas, and so I have myself to blame for some of the, you know, forward inertia, which is now, like, almost impossible to change, that there was never, like, any design effort in the community, like the R and the Python people never got together and said, how can we build a better data frame, how can we share code, how can we make our data and our implementations more interoperable, and the biggest, you know, downstream symptom that you see is the fact that, you know, you get into a lot of benchmarking, and a lot of, like, published benchmarks about the software that's being built, and even building software with the intent of just creating a better benchmark, which is really unfortunate, and so I think there's, like, a saying in computer science, for any given set of systems, there is a benchmark such that one of the systems will come out on top, and so whenever you see a benchmark published in which, like, a particular system wins, you have to really look at, like, the benchmark.

It's kind of like this, like, you know, with statistics, you have the problem of multiple tests, where it's like you have a hypothesis, and it's like, well, just keep coming up with tests until you find one where the p-value is less than .05, and then publish that one, because that's, you know, not disingenuous or anything.

Same thing applies to benchmarks, so probably if you have three systems, and somebody has, like, and, you know, a developer has the system that they're building, they might have a bunch of test cases, and there might be either inconclusive results or not very favorable results, and they'll pick the benchmark that makes their system look the best.

So whenever you see a benchmark, please ask questions.

It really is a, and I've been guilty myself of publishing benchmarks, and so I've gotten caught up in this as well.

It's really hard.

So, but the things that get tested the most are reading and writing files, and generally, like, reading data into memory, which is kind of unfortunate.

You'd think that that would just be a solved problem by now, like, we can read the data into memory really fast.

But the other kind of analytics that end up being bottlenecks in analysis tend to be the joins and aggregations.

And so, basically, you're getting this smorgasbord of testing all of the, all of the things that's not only the quality of the algorithm, but you're also, can end up bottlenecked on how, on lower-level issues that are maybe outside of the developer's control.

So just to give you an example, this is, like, really, you know, a really simple example, but yet, like, these are the kinds of benchmarks that get published, is simple, you know, a simple group by, where you group by one column and you compute some aggregate function.

Like you, you want to, so I wrote out the SQL to make it super clear, like, we're summing B for each distinct value of A within, within a data frame.

And so, if you, if you break this down into, like, you know, what's actually happening when you run, when you run this code.

So the first thing is that all of the values in A and B are being scanned.

And so when I say scanned, I mean all of the memory that's associated then is being accessed.

And so, that might be that if the data is not all stored in the same part of, you know, your system memory, it might involve a bunch of, like, reads from different parts of your, of your system RAM.

And so this is very impactful in both Python and R, because if you have an array or a column of a data frame that contains strings, those strings are not stored in, generally speaking, in the same place.

And so if you, if you're looking at a string in one slot of a column and you want to look at the next string, those are stored often in different, completely different places in memory.

So the system is having to basically look all around your RAM to, like, pull out those strings and then to compute something with them.

So if you had all the strings kind of stored end-to-end, like dominoes, in a, in a, in a contiguous chunk of memory, it would be a heck of a lot faster.

But that's often something that's just not in your control.

So the values of A, depending on what type they are, the usual way that this kind of algorithm is implemented is, is using a hash table.

So you hash the value of A, you use that to compute a, a category ID, so you're testing how is, how fast is it to hash the values of A, how fast is your hash table implementation.

And then once you compute that categorization for each value of A, you actually have to sum the values in B, which again involves the scanning of the, the data in B.

And then putting all of the data into a result data frame and returning it back.

Data types are also, are also a big thing.

I, I shouldn't need to say, it's kind of an empty statement, but you have all your primitive value types.

And most of us, you know, including Python, you know, Python and R, most of our world is in the primitive value type land.

But if you're dealing with data that's coming off, out of the web, you're, you might be dealing with more complex, more complex data types.

And so I broadly put these, these data types into kind of the list, structs, and maps bucket and explain exactly what those are.

And so, so here's like an example of, you know, a chunk of data, of JSON data, which, you know, might have come from, you know, your favorite web framework.

And you want to, you have a bunch of this data for all of the people that use your website, say.

And you want to do some analytics on this data.

So I wrote out, like, here's what the JSON looks like.

Here's what, and here's what the effective table schema looks like.

So I wrote that the row itself, each row in the table is a struct.

And so struct is just like a dictionary with some fields and types.

So name itself is a struct, where it has a first and last field, which are strings.

Age is an int.

I have some favorite numbers, and that's a list of integers.

And addresses, see, is something more complex, because you have a list of structs that all have a city and state associated with them.

And so any given person in your, in your data set will have lived in multiple addresses, and those are all contained in this addresses list of, list of structs.

I didn't really know what kind of, kind of an interesting map to put here, but I just put one with, you know, some strings as keys and integers as, as values.

And so if you think about, like, a data frame, like, this is a perfectly, perfectly reasonable schema, but in practice, like, this kind of data is really hard to work with in a, in a data frame.

And the way that, if you're in R, you're in, you're in, using pandas or any of the data frame libraries, the first thing that you would do if you had a big file containing data looking like this is that you would flatten it out into either one big table or a bunch of tables, and you would duplicate the data in the addresses table, or you, or, you know, you duplicate the data in, like, the name, age, and numbers columns.

But if you want to do analytics, or you want to count things, going into those, you know, say, if you wanted to, say, compute the number of people for whom two appears in their list of numbers, that becomes, like, a more complex operation that's going to be both hard to express and slow.

Memory layout, I, you know, probably don't need to tell most of you, makes, makes a big difference in performance, and for doing analytics, the, you know, the best in class memory layout is, you know, what's called columnar layout, which is that any column in a table, all of the data is stored together in memory, so in a single stripe.

So, you know, here's a representation of a, a columnar table, you know, each color is a different column, and columnar is nice because it, suppose you have a really wide table with, like, a thousand columns, and you're only interested in two or three columns for a particular operation, that's really fast because you can access those two or three columns without having to touch any of the other data in the table.

So if you're just summing the values within a column, it's going to be super fast.

Another thing that's nice is that projections, which is to say, if you have a thousand column table and you want to select a subset of the columns, like five or ten columns, you can do that without copying any data, and it's really fast.

You can add columns without having to do any copying.

Now the downside of this is that if you have an operation which involves just a single row in the table, that's going to be slow because you're walking all over memory to pick out the values within a single row, and if you want to add rows onto the end of the table, you're also having the same problem of having to walk all over memory to put the values in each, in each column.

So the row, row, row-oriented approach is basically the opposite of all of these things.

It's slow for analytics, projections are expensive, it's easy to add rows, but if you just have an operation that involves a single record, you already have, you've effectively already laid out each row of data alongside each other, and so you can do an operation that involves a single row very quickly.

So we'll talk a little bit about the serialization problem, kind of break this down into text formats and binary formats, and unfortunately in data science, a lot of the, a lot of our data that we're dealing with is CSV files.

I don't really have the statistics on it, but it's either, it's like CSV or JSON, probably in over 50% of cases, which is really unfortunate, but part of the problem there is the fact that binary data formats, there are many of them, there's no consensus on like what is the best binary data format to, you know, to use to, you know, give data from one colleague to another, or one organization to another, and so everyone just defaults to CSV files, or maybe like a database dump, that's also like a popular route, effectively a text format that can insert rows into a MySQL database.

So the problem with text-based formats, well, the good thing is that you can take a CSV file and anybody can read it.

The downside is that they're very expensive to read and write.

If you don't know the schema, finding out the correct schema is both slow and you can get it wrong.

Even if you know the schema, you have to check it when you're reading the data, because values might not parse correctly, so there's no like, there's no guarantee that the file that you've, you've received is well-formed.

It's also true with binary formats, but at least with binary formats, you hope that the person used a library that has been tested and is correct.

And yeah, and I guess I call like, you know, text formats is not like high fidelity, so you can lose data as soon as you write it out, and that includes like with CSV files, the biggest thing is you lose precision, you can lose type information, and if you have like JSON data, you can't put that in a CSV file, you have to store it in JSON, and reading and writing JSON is really expensive.

Binary data formats are nice, however, library support for them is really weak.

So one of the, I work at Cloudera, so I have a horse in this race in that we developed, we developed Parquet format for use in Impala, which is a high-performance SQL engine.

There's another, you know, columnar binary format called Orcfile, which is used by some other Apache projects.

There's some other projects which are, you know, similar to Google's protobuf library like Avro and Thrift, that are not designed for analytics, but also can, can transport well-schemed binary data.

The biggest issue is if you're using R or using Python, you probably don't have a reader or writer for these formats, which is really unfortunate, and the reader and writers are inconsistent from, you know, project to project, and they can often be a little more difficult to work with than just a CSV file, and you just want to write, like, read.csv or read underscore csv.

You know, on the subject of the data representation, if you look at, you know, R and pandas, they're actually quite different, and they're similar but yet different.

And part of the issue is that in R, you're working within the R type system, which is a simplified, you know, primitive value type system.

So you have strings, what are called character arrays, you have numbers, you have integers, and you have floating point numbers, you have booleans.

You have a way to store missing data that's very specific to R, but if you're dealing with data types that go outside of the core, like primitive R types, like if you have JSON data, you know, with nested type schemas, like structs and maps and so forth, it becomes a lot more difficult.

pandas has the exact same problem, so this problem hasn't been solved well in Python either.

And missing data is a big problem as well, which I will talk about.

So both R and Python use special values to handle null or NA values, and the problem with this is that, and it's one of the big regrets that I have about pandas, is that the missing data handling was, it tries to be as similar to R as possible, but there's some rough edges, and it's working within the context of NumPy, so we kind of did the best that we could with the tools that we had at the time, and we were going for compatibility with NumPy, and NumPy has no built-in support, at least at that time had no built-in support for missing data.

I don't know what the status on that is, I haven't really paid attention, but we did the best with what we had.

But databases, and in the most general case, the best way, in my opinion, to deal with missing data is just to have an extra bit or byte that you carry around where you say whether something is null or not null.

You pay a memory use and performance penalty for that extra byte, but in exchange you get a very simple way to track whether something is missing or null, regardless of the data type.

So you don't have any type-specific null handling.

So the big picture is that I'm actively, as in day-to-day, working on addressing some of these infrastructural issues, and if they affect you, or if they're important to you, I encourage you to get involved in the conversation, and it's certainly more than a one-person or a one-company job, and will require a lot of people to get in a room and develop consensus about ways to solve some of these questions so that we can share more code and we can all be more productive.

That being said, things are pretty okay right now.

The R stack, as many of you know, has gotten a lot better.

dplyr and what I call the Hadley stack has really transformed the R programmer's workflow in the last couple of years.

Other great data frame-based libraries.

Not everything's great in R. The things that I see as problematic are the type system, the fact that it's not as easy to reuse memory as it should be, so there's relatively easy things that you can do that will cause a whole data frame to be copied and duplicated in memory.

dplyr is really nice, though, because if you look at it, it's really using the characteristics of the R language to build kind of a new SQL in a way, like it's a domain-specific language embedded within the R language that has an in-memory compute engine that will work on in-memory R data, but you can also take dplyr expressions and run them in SQL databases.

So if you think about kind of talking about that decoupling of like, let's separate the user interface from the compute and storage, dplyr is doing that, and that's pretty great.

Spark is very similar in this regard.

Spark has a data frame interface now and is very much in the same vein of a decoupled user interface that uses the Spark compute and storage engine and gives you a workflow that is more familiar for an R or Python user.

There's some little things, like you look at how data frames are actually implemented.

There's the Spark robust distributed data set abstraction, which is effectively a sharded array of row objects, and I don't believe it's represented in a columnar way, so there's definitely ways in which Spark SQL and Spark data frames could get better performance from columnar data layout.

pandas has been around for years, but certainly not the ultimate data library, but it's a very, very good one, in my humble opinion.

The internals of pandas objects are actually very complex.

If you go digging, like what's inside a pandas data frame, you might be surprised at what you find inside, and there's very good reasons why things ended up that way, but there's also the organic growth issue that I think the only time that we really took serious time to evaluate the internal details of pandas was in the summer of 2011, and I was working very independently at that time and didn't have a lot of people to consult with, and I had a very particular set of use cases that I was interested in optimizing their performance for, and that led to an internal structure, which now in 2015 seems a bit anachronistic, or whatever is the term, dated perhaps.

If we went and redesigned pandas from the ground up, there would be a lot of things that come out differently.

On the other hand, there's good things about pandas that are very different from any of the other data frame libraries, like the hierarchical indexes, which many of you have probably used.

It's a very distinct feature from other packages, and the fact that pandas was developed within a financial setting led to really good time series tools.

It really strikes me as unfortunate that a lot of people are choosing Python and choosing pandas for its time series functionality.

I think that we should have just as good time series functionality in all languages, that it shouldn't be this sort of secret sauce that's only available in pandas.

Things about pandas that aren't as great on this general topic is the fact that storage and memory representation type system were from day one all the domain of NumPy, and that led to some of the rough edges and things that we're still dealing with today, and the fact that some of the complexity of the library, which makes it very powerful, can be a source of some pain for people that just want something that feels like an in-memory database table.

Because the internals are complex, there's no C API, so if you want to write some low-level code that interacts with a pandas data frame, it's actually pretty difficult.

There's some really cool stuff going on in the Python community.

There's a new project called Blaze.

There's some developers from Blaze here at the conference, I think.

It's built by Continuum, Continuum folks are here, and it's very much in the domain of the decoupled future, and Blaze is neat because it has one data expression API, and it has many different execution backends, including pandas and SQL.

It does not have a native backend, so Blaze isn't addressing some of the infrastructural issues that I've been talking about, but it has a richer type system called Datashape, which is a standalone Python component that you can use, so that's great.

I think having a native and full-featured backend for computing expressions on anything that can be expressed with the Datashape protocol would be really great, and I hope that we get there.

There was a project called, I guess I shouldn't talk about it in the past tense, it's still being developed, but it's called Libdyned.

It was kind of a new NumPy project that I don't think is being developed anymore, but was originally intended to be a backend for Blaze, but I think that the things have gone off in a different direction, and it's possible that it could get picked up and become a full-featured backend for Blaze, which would be really interesting, but it does implement that Datashape protocol, so it's one example of a pure C++ library that implements a richer tabular type system.

It's all written in C++.

Another neat project for Python programmers is the BCalls project, which is an outgrowth of both CArray, a compressed array library, and Blask, which is a really nice compression suite that handles bigger tables that can be interacted with as though they were in memory.

I've got to give a shout-out to the Julia project, which has its own DataFrame implementation, a lot more similar to R than Python.

So if you're a Julia programmer and like fast code, you should check out Julia's DataFrames as well.

It's still early on, which means that an individual could get involved in this project and have a pretty big impact building it out into a more full-featured library.

And there's DataFrames in all the languages, and so that's great that I think the general trend has caught on.

One of my former colleagues from AQR, Adam, he hopped from a couple of financial firms in New York and built DataFrames in both Scala and Fsharp, which is pretty cool.

And there's even DataFrames in Haskell and Go and many other, and so forth, other languages.

So I'm running out of time, since I'm sort of speeding through slides, but the big thing I wanted to stress in the talk is that figuring out how to share code amongst the data science community, and I think there's been, with all the language wars, it's created division and unnecessary barriers to collaboration amongst the community, and I think if we can figure out how to build a DataFrame software that can be used amongst all the data science languages, in particular Python, R, and Julia, that, I think, is the big challenge for the next five or ten years, and figuring out how those languages can interoperate with the big data ecosystems that's like Hadoop and Spark.

And that's the essential matters I see for bringing about this kind of decoupled future in which you aren't as tied to a particular programming language, you can interoperate between programming languages and collaborate better as developers and better as data scientists with each other.

And the other big thing is, of course, the fact that most of the data that's being thrown off and warehoused is JSON data, and if you don't have a type system which can accommodate the data that you're collecting, you're going to end up spending most of your time transforming data from nested form to platform in order to do analytics, and an extraordinary amount of compute cycles are being used right now just transforming data from one format to another, and that seems like a big missed opportunity to me.

So that's all I've got, and thank you for coming.