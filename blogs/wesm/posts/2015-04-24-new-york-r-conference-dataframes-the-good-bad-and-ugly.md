---
title: "DataFrames: The Good, Bad, and Ugly"
summary: "Video at New York R Conference"
date: 2015-04-24T00:00:00
tags: ["video", "transcript"]
slug: new-york-r-conference-dataframes-the-good-bad-and-ugly
word_count: 4560
source_file: transcripts/2015-04-24-new-york-r-conference-dataframes-the-good-bad-and-ugly.md
content_type: transcript
event: "New York R Conference"
video_url: "https://www.youtube.com/watch?v=stlxbC7uIzM"
---

{{< video https://www.youtube.com/watch?v=stlxbC7uIzM >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This 2015 talk presents a vision for "the great decoupling" of data science infrastructure. I spoke at an R conference while a PyData conference ran simultaneously in Dallas.

## The Great Decoupling

By 2025, three core components should separate: data storage, computation engines, and user interfaces. Rather than comparing benchmarks between data.table, dplyr, and pandas, "why aren't these all using the same code base?" Decoupling would let the community share performance improvements regardless of language, eliminating redundant implementations across tools.

Dplyr is "a really great example of what the decoupled future looks like"—built with multiple backends, users write identical code whether data resides in memory or databases.

## User Interface Philosophy

The best interfaces emerge from real-world frustration. I was "really frustrated with R" while working at AQR Capital Management.

"Any time you add or you improve user interface, you make something more composable, you make an API more consistent, you make your own life better and the lives of the people around you better." Small inconsistencies create productivity burdens through constant context switching and documentation lookups.

## Honest Assessment of pandas

pandas has grown into a 200,000-line codebase approaching 10,000 GitHub issues and pull requests. This "walled garden" approach brings both benefits and drawbacks. The library's financial origins made it strong for time series analysis, and "hierarchical axis labeling" provides power unavailable in R—but creates complexity that can overwhelm users expecting simpler structures.

The NumPy dependency creates "rigidity" in the type system, complicating string handling and missing data. I state: "next-gen pandas for Python programmers is certainly something that is needed."

## JSON and Semi-Structured Data

Future DataFrame systems must embrace semi-structured data to handle "the data of the web." Tabular structures need nested types—fields containing sequences, maps, or structs rather than just numbers or strings.

## Community Standards

I call for "a community standard DataFrame library that we all use, rather than having parallel implementations of all the same things." This requires compromises and extensive design work but is essential to the decoupling vision.

## Key Quotes

> "It would be really nice if rather than kind of comparing benchmarks between data table, dplyr, and pandas, we say, well, why aren't these all using the same code base?"

> "Any time you add or you improve user interface, you make something more composable, you make an API more consistent, you make your own life better and the lives of the people around you better."

> "I was really frustrated with R, and I was excited about Python. I'm like, look, there's no data frames here, there's really not any good data wrangling tools."

> "I think that the best quality and the most useful user interfaces come from what I call the fire of battle."

> "The fact that pandas is also built with NumPy compatibility in mind has led to rigidity in that the data is stored in NumPy arrays. That means we don't have complete control over the type system."

> "The next-gen pandas for Python programmers is certainly something that is needed."

> "I think dplyr is a really great example of what like the decoupled future looks like. And that dplyr was built with multiple backends in mind."

> "I think it would be really great if we could put our heads together, we, the people of the world, and build a community standard DataFrame library that we all use, rather than having parallel implementations of all the same things."

> "The future is JSON-like. It is semi-structured and not structured."

---

## Transcript

Thanks a lot, Jared, and thanks for having me.

It turns out there's actually a PyData conference going on right now in Dallas.

So I don't know what that says about me, but the last time I was at an R conference, I

wasn't speaking, but it was the R and finance conference.

And I've got to say that after about half the conference, I started to feel really self-conscious

about not being German.

If you've ever been the R and finance, I mean, you'll understand.

So necessary disclaimer that, you know, this is what I think.

So now that I work for a bigger company, I got to make sure, you know, sort of to disclaim

when I'm expressing strong opinions, which I very frequently do.

So the goal of this talk, and it's a lot for 20 minutes, but I wanted to talk generally

about data frame interfaces as they, you know, which are one of the primary tools that we

use, present some strong opinions, some of which are perhaps not as well-formed as they

ought to be, just to sort of share some of my thoughts and experiences from building

data frames over the last seven years or so.

I will point out that it is a very nuanced discussion and it's far too nuanced for 20

minutes.

So some of the, I won't necessarily present some of these things as fact or, you know,

fully, you know, finalized conclusion.

So, you know, these are things that we could debate for hours and hours and hours, but

just some food for thought.

What have I been doing with myself the last, you know, number of years?

I started working on pandas.

I worked for AQR up in Greenwich, Connecticut for about three years.

I was really frustrated with R, and I started, and I was excited about Python.

I'm like, look, there's no data frames here, there's not, there's really not any good data

wrangling tools.

Oh, yeah.

We've got a book there.

So I started on this journey at the beginning of 2008, building pandas, and that led me

to get involved in the open source community and write a book and, you know, do lots of

things, and now it's suddenly 2015.

I took a few years off from honest employment, went back to grad school, dropped out of grad

school, came back here, did a lot of open source, wrote a book, you know, things happen,

I guess, in your career.

So I guess the question for this talk is, what's in a data frame?

A table with some rows by any other name would analyze as sweet, or putting it a different

way perhaps is, you know, if you've got a table, why not put a data frame interface

on it?

So, you know, when I talk about data frames, I don't need to tell you being our programmers

that, you know, you have a table and a data frame is just sort of a concept of some kind

of interface for working with tabular data, and unfortunately, it goes pretty far beyond

the data structure itself and has a lot to do with the API and how you think about expressing

computation on the data and has all the hooks into your, you know, modeling frameworks,

how you do run linear regressions, how you describe essentially how you build models.

So, you know, when you talk about data frames, you've got to sort of focus the discussion

on like what aspects of the data frame.

Is it the data structure itself?

Is it the sort of data tidying, data wrangling interfaces?

Is it the modeling interface?

Is it the relational algebra?

Is it its, you know, how you're reading data from CSV files or dealing with databases?

So unfortunately, that's why like the data frame discussion ends up devolving into like

this fixation on one topic or another, and there's lots of different ways that you can

compare them to each other, and I made this kind of like non-exhaustive list of like all

the things that you can find in any particular, you know, suite of data frame tools, and like

the list goes on down to the floor, all the ways that you can, you know, run benchmarks

so you can compare APIs and be like, well, look, it's easier to do this one, you know,

this one weird trick here than it is to do over here, and this code runs faster here

versus here, and it kind of gets into this little shooting match, and it's like, well,

you know, what is the point?

Like why do we care?

And there's kind of a macro trend that I see going on, and it's 2015, and I spend a lot

of time thinking about what's going to happen in 10 years, like, so, you know, you look

10 years ago, like what were we doing 10 years ago?

We didn't have very nice IDs, we didn't have very good libraries, like most of like, you

know, the stuff that Hadley Wickham has built didn't exist in 2005.

There was still R, there was still Python, but it was a very different time, and so if

you look 10 years into the future, like what is that going to look like?

And my hypothesis, and we'll see if this ends up actually being true, so I guess, you know,

the trick to sort of looking really smart is to make a lot of predictions, and some

of them will end up being true, and you just talk about those.

So I've already seen what I described here happening, which is that the, how we're storing

data, how we're performing computations on it, and then how we're sort of thinking about

those computations, and kind of the user interface, which, you know, user interface means a lot

of things to different people, but like the API and like the code that you're writing,

that's your user interface as a programmer, is that I think in 10 years that these are

all going to become decoupled, and we're going to have really great distributed data

storage systems, really fast, interactive, scalable computation engines, and for us as

programmers, whether it's R, Python, kind of whatever data science language, the challenge

is going to be can we build really great user interfaces, and, you know, there's a lot of

reasons why you want other people to assume kind of the storage and execution problem.

It would be really nice if rather than kind of comparing benchmarks between, you know,

data table, dplyr, and pandas, we say, well, why aren't these all using the same code base?

Why should there be multiple implementations of joins and filters and aggregations and

all of that, all of that data munging stuff?

There's ways that we can work together better to kind of, you know, so that effort to improve

the performance of these data structures ends up benefiting the entire community regardless

of the programming language that you're using.

So I see this already happening, and I hope, I think that more of it is going to happen.

On the subject of user interfaces, this is where a lot of opinion comes in here.

So my view, and this is very kind of an egocentric viewpoint, is that I think that the best quality

and the most useful user interfaces come from, you know, what I call the fire of battle.

So you're there, and you've got an itch, and you've got this data, and you've got your

boss who wants that, you know, that data wrangled, that data modeled, you know, wants the plot,

wants the answer, you know, and you've got a deadline, and you find yourself struggling

with the tools that you're using.

Either they're too slow or they're too difficult to use, or you forgot to set strings as factors

equals false, and like, you know.

So little things happen, and all of those little paper cuts add up while you're trying

to get work done, and over time, you know, you suffer from all that, and if you start

actually taking action, say, well, let's improve the tools, let's examine like, you know, rather

than kind of, you know, just suffer from it, and say, well, this is the best that we've

got, and we've got to get the job done with these tools, just start improving the tools,

and if you have the feedback cycle of you're directly impacted by the tools that you're

creating, any time that you add or you improve user interface, you make something more composable,

you make an API more consistent, any time you do that, you make your own life better

and the lives of the people around you better, and if you look at work that Hadley has done

improving the R, you know, the, his, you know, R libraries and kind of creating this ecosystem

of packages, if you talk to Hadley, like, one of his biggest things is consistency,

and that consistency comes in when you're writing code, and you know, you're sort of

moving around, you're making context switches, and just like the number of times that you

have to pull up documentation for functions really impacts you in a material way, and

so if you have inconsistencies, even small ones, in your program or user interface, then

that adds up to a productivity burden over time. So you need real use cases, you can't

be designing in a bubble, and you know, certainly seeing people succeed with tools, that social

proof is really critical, particularly when you're trying to convince your boss to use

a new tool, it's like, well, can we trust this thing, and be like, well, there's all

this social proof that we can accept that, and you know, even ten years ago, R didn't

have quite as much social proof as it does now.

Now it's like, well, of course, use R.

Same with Python.

10 years ago, it was even worse conversation with Python.

It's like, can we even trust interpreted languages?

It doesn't, if it's not compiled, clearly it's not safe.

And people will use that like, it doesn't compile

as like an excuse for not writing tests.

And so now I think we know that that is really

not the right way to think about it.

So you gotta eat that dog food, as I like to say.

And you can learn a lot about a package,

and when you're evaluating software that people have built,

if you aren't looking at the test suites for software

that you're using, you really should,

because that's where all the dirty laundry is

in a lot of cases.

And so if you open up a test suite and you find that

the person building the package hasn't had,

you know, we were just hearing from the carrot folks

and how rigorous and intense their unit testing

and sort of regression testing process is.

And when you're building software like this,

like it's absolutely critical,

not only to validate the correctness

and like build trust around the project,

but also to have the freedom to be able to make changes

and improve the quality of the user interface

without worrying about whether you're breaking the code.

So, well now let's get specific,

talk about a few things, and of course,

highly simplified, you know, details about data frames.

But, you know, the way I think about our data frames

is that, you know, if you've looked internally,

our data frames are basically a pretty simple data structure

built on top of our lists.

You have some column names and you have some vectors.

You can also have, you know, assign the row names variable

and then you have, you could have dates along the rows

or you could have some other symbol

that flows through selections and other computations.

But, you know, when you say our data frames,

what you're talking about is actually a very simple concept.

You have the R type system, you know, you have R arrays,

it's just a table.

And all the value in that table comes from

the ecosystem of packages which are built on top of it,

which can be, which can vary a lot.

So if you're just using base R,

you really don't have a lot of stuff.

I mean, you can read and write files.

There's a lot of reshaping and, you know,

different kind of analytics functions,

but to really get a lot of value out of our data frames,

you've got to go digging into the CRAN library.

So all the value comes from there.

Now, of course, there is a lot of great stuff.

You know, what I call, you know,

a lot of people call the Hadley stack.

It's funny thinking of Plyer and Reshape 2 now as legacy.

You know, two years ago, that was, you know,

they weren't legacy and, you know,

a lot can change in two years.

Now, of course, there's DataTable and XTS,

which are, you know, libraries built on top of data frames

that bring domain-specific functionality

like time series, manipulations.

In DataTable, you have an extension of DataFrame

which has indexing and the ability to modify in place

and various tricks which help with working

with larger data sets and getting very,

very fast performance and joins and so forth.

It's not all sunshine and roses,

as I don't need to tell you.

You know, copy-on-write bites a lot of people.

If you don't sort of pick a set of cohesive tools to use,

you can find yourself dealing with the inconsistency

and fragmentation problem, and I think the Hadley approach

is just have a consistent set of tools and just use that.

And so if you stay in kind of Hadley land, so to speak,

then you can have a lot better time.

A rough edge that I've run into over the years

is kind of what I call like the factor-string dichotomy.

It's like having to pick one or the other,

but you have to know, you have to commit to your choice

and then know how that choice affects

all of the other code that you write.

So just make sure you don't join on factors

that have different levels or you're gonna have a bad time.

Unless you're using dplyr, you know,

just don't, not with base merge.

Another thing with R is the fact that

one of the benefits actually is that R's type system

is somewhat simplified as compared with, say, a database.

So you have one integer type and you have one numeric,

you know, floating point type,

but it's not a very extensible system.

And so for kind of thinking about the future,

that's something to think about.

You know, dplyr has been an incredible boon for R

in terms of thinking about user interfaces

and defining that composable table API.

And you can't do everything with dplyr,

but you can do a lot of useful stuff.

So I kind of think of it as like the Trader Joe's

of, you know, data libraries.

Like it doesn't have everything,

but it has pretty much what you need.

And I think it's a really great example

of what like the decoupled future looks like.

And that dplyr was built with multiple backends in mind.

So, you know, remind Francois and Hadley built

an in-memory, you know, RCPP based backend

to evaluate dplyr expressions,

but he designed it with the intent

of having SQL backends as well.

And so if the data is in a database

or the data is in memory, you can write the same code.

And not everything works with the SQL backend,

but a lot of it does.

And I think it's a good model for the future.

As a lot of people know, Spark is now building

a DataFrame API into all of their APIs,

which I think is really great.

And it's a nice, you know, as we've established,

it's a nice way to think about tabular data in Spark land.

You know, one of the big use cases

is the interoperability with Spark SQL.

And when you're building DataFrame expressions with Spark,

you're effectively building query plans

with the Spark SQL query optimizer,

which is actually kind of cool

because you can write code,

which might be really inefficient in R,

but you're leaving it to basically a SQL optimizer

to decide how to best evaluate

those expressions in a fast way.

So in some sense, Spark DataFrames

are part of the decoupling sort of trend that's going on.

Of course, your execution engine is bound to be Spark.

So if you don't want to be tied to Spark,

then you don't want to use Spark DataFrames.

But if you're happy being committed to Spark,

then of course, go ahead.

It's a very new interface,

and so it needs users in the AMP lab,

like Databricks, kind of the Spark developers,

need the R community to be telling them

what they should be building.

Because they're computer scientists,

and they aren't really suffering nearly in the way

that the R and sort of statistical community

has been using DataFrames for years

and has a very good sense of like

how it should look and feel

and what functions are important

and what will create the most value

in a short amount of time.

You know, pandas is the project

that I've worked the most on.

Which is kind of interesting to talk about

in this discussion,

because there is a DataFrame in pandas,

but in some sense, the pandas DataFrame,

within the scope of the rest of the project,

the data structures themselves are not that interesting.

I mean, they're important.

So there's multiple data structures.

The DataFrame is the one that most people use.

But, you know, you look at, okay, it's a table.

It's got columns, it's got arrays inside.

And if you go back to like pandas 0.2 or 0.3,

and maybe there's some people in the room

that used pandas way back then,

it was a much simpler library.

And now, all of a sudden, it's 200,000 lines of code.

And on GitHub, where you know that they number issues

and pull requests in sequential order,

I looked today and it's about to cross into the 10,000s.

So it's like 3,500 pull requests

and nearly 7,000 issues.

So there's more than just data structures there.

And it's kind of, the thing about pandas

is that it wasn't only just the table.

It was the fact that you needed to build

kind of the whole ecosystem of tools.

So if you look at R, you've got a lot of different packages

which implement different functionality

that involves DataFrames.

And so the DataFrames themselves are very simple.

In pandas, it's kind of this like walled garden approach

or batteries included approach

where you have a really sort of fat library

with a lot of stuff, all the IO stuff.

All of the data wrangling,

all of the group by like transformation.

There's even a bunch of plotting things in there.

So it's this really expansive library

which is both a good and a bad thing.

And there's two kind of, so really distinct qualities

is that because it was built in a financial setting,

it's become very successful in financial services

because people view it

as one of the best time series libraries.

And you know, having, if you use pandas,

what I will describe in a very technical way

is hierarchical access labeling

which is something that doesn't really exist in R.

It is very powerful

but also makes the library complex in some ways.

So it's both a good and a bad thing.

So more about that.

I mean, I've got a book that's about 50% about pandas

so you can learn all about that in there.

So.

So, at the power comes some complexity that, you know,

the access labeling stuff in pandas can create

a bad experience sometimes for people coming from R

who are expecting to have, like, a very, kind of,

vanilla table data structure.

The fact that pandas is also built

with NumPy compatibility in mind

also has led to rigidity in that

the data is stored in NumPy arrays.

That means we don't have complete control

over the type system.

There's missing data handling issues as a result.

Strings are an issue.

You know, little things.

If we freed ourselves of dependency on NumPy,

we could go and fix some of these problems.

So, the next-gen pandas for Python programmers

is certainly something that is needed.

Julia has DataFrames.

And I know that there are some Julia developers here.

I saw Harlan Harris. I don't know if he's around here.

But he and some other folks spearheaded DataFrames.jl,

which I see now has had over 60 contributors.

And if you compare Julia's DataFrames

with R and pandas DataFrames,

it's a lot more like R DataFrames.

And that kind of goes in line

with the broader Julia stats initiative

to create a statistical computing environment in Julia.

You know, it's still, you know, as Julia,

as a language has only been, you know,

out there for a few years, you know, DataFrames and Julia

are still our earlier stage library.

So, things like, if you want a SQL interface

to Julia DataFrames,

I don't know if it's found in the library.

It might be elsewhere.

You're dealing with something that's a lot newer,

but there's also a lot of exciting opportunity there

with the broader benefits of the Julia language on your side.

So, there's DataFrames in other languages, of course.

Adam Klein, who's one of my colleagues from AQR,

worked with for several years.

I guess I sort of infected him with the sort of, you know,

pandas sort of, you know, DataFrames, all the things.

And he's jumped from a couple of financial companies

and has been building DataFrames everywhere he goes,

which is great.

So, now we have DataFrames in Scala and in F-sharp.

I also wanted to, you know, throw a shout-out to the GraphLab,

who are now Dotto folks,

who have built a really amazing and scalable DataFrame.

It does have a licensing issue,

which will be interesting to see how that leads

to community development or lack thereof.

But it really is an amazing piece of software engineering.

And there have even been DataFrames built in Haskell

and Go and other languages.

So, I'm running out of time,

but a couple of things that I wanted to say is that

the future is JSON-like.

It is semi-structured and not structured.

So, we need to think about our DataFrames

and how we can augment them to support nested types.

So, to have fields that are not simply numbers or strings,

but could be sequences or maps or structs.

And that would enable an R-like or a DataFrame-like structure

to also account for the data of the web,

which is JSON, with the types, of course.

I think it would be really great

if we could put our heads together,

we, the people of the world,

and build a community standard DataFrame library

that we all use,

rather than having parallel implementations

of all the same things.

That would require some compromises and design work.

But I think it's a greater part of the great decoupling,

which I'm very excited to see happen.

So, that's all I've got.

Thank you.

Thank you.