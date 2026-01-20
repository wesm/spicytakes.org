---
title: "Data science without borders - Wes McKinney (Two Sigma Investments)"
summary: "Video at JupyterCon"
date: 2017-08-24T00:00:00
tags: ["video", "transcript"]
slug: jupytercon-keynote-data-science-without-borders
word_count: 3703
source_file: transcripts/2017-08-24-jupytercon-keynote-data-science-without-borders.md
content_type: transcript
event: "JupyterCon"
video_url: "https://www.youtube.com/watch?v=wdmf1msbtVs"
---

{{< video https://www.youtube.com/watch?v=wdmf1msbtVs >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This talk addresses fragmentation across programming language ecosystems in data science.

## Open Source

I recall explaining to bosses that the Python ecosystem was built by "grad students"—often physicists and scientists "procrastinating on their PhDs." John Hunter started matplotlib out of frustration with MATLAB's licensing. Cloud computing accelerated this transition—traditional licensing doesn't scale when spinning up thousands of machines.

I note hearing from people worldwide, particularly in economically disadvantaged regions, learning these tools to analyze data. The viral growth of Jupyter notebooks, which I first saw in 2011, shows how ideas spread when they solve real problems.

## Coming Challenges

The "AI arms race" drives demand for faster machine learning, but "no matter how sophisticated the AI algorithms get, we're still going to need all of the tools that we've developed for all the work that happens before you're fitting your models."

Hardware has evolved dramatically—from 2-4GB RAM and single cores to terabytes of memory, 16-core processors, and SSDs 10x faster. But current data science tools haven't scaled to take advantage of modern hardware.

## The Tribalism Problem

Despite surface similarities between Python pandas and R dplyr code, implementations are incompatible. Each ecosystem maintains its own data access layers, memory formats, compute engines, and analytics toolkits. For pandas alone, "we've written our own CSV readers and many other data access layers, we have a half-baked implementation of an in-memory SQL database"—infrastructure inaccessible to non-Python users.

Programming languages serve as user interfaces, hiding complexity below the surface. But this leads to duplication across communities that could be collaborating.

## Apache Arrow

Apache Arrow aims to create a "shared data science runtime": portable data frames with consistent in-memory formats across languages, zero-copy data interchange, optimized data connectors, and a computation engine embeddable in existing systems.

Collaboration with R's Hadley Wickham created an interoperable file format between R and Python. This approach lets developers "own less of the infrastructure" while building better tools.

## Collaboration

I acknowledge the "chicken and egg problem" in building pandas. My advice: "when you have a chicken and egg problem, sometimes the best thing you can do is be the chicken."

## Key Quotes

> "No one ever got fired for buying MATLAB."

> "A lot of them are grad students... no, a lot of them are physicists and scientists who are just trying to, who are procrastinating on their PhDs."

> "John Hunter... started Matplotlib because he got frustrated with MATLAB's licensing policy when he was generating plots on different servers."

> "I've been really humbled to hear from people all over the world, especially in very poor places who... are working really hard to learn these tools so that they can analyze data and use that to improve their lives."

> "No matter how sophisticated the AI algorithms get, we're still going to need all of the tools that we've developed for all the work that happens before you're fitting your models."

> "I'm a Python person, I'm an R person, and that becomes a part of your identity."

> "We've written our own CSV readers and many other data access layers, we have a half-baked implementation of an in-memory SQL database."

> "We would like to own less of the infrastructure that enables projects like pandas to exist."

> "Programming languages are user interfaces for describing computation."

> "When you have a chicken and egg problem, sometimes the best thing you can do is be the chicken."

---

## Transcript

So my topic today is very important to me.

Many of you know me from my open source work and my writing.

In the last couple of years, I've been very excited to get involved in a couple of projects

in the Apache software foundation, and we don't have a lot of Python programmers working

in the ASF, and I will say about that, that as open source grows bigger and more popular

and even more commingled with commercial interests, that it's very important to have organizations

like the ASF to put the community first and to protect the intellectual property rights

of open source developers.

So I'd like to reflect for a moment on everything that's happened over the last ten years, and

certainly it goes way, way beyond that.

There's work that we're depending on in the Python world, which happened a long time before

2007, but it was this month, ten years ago, when I personally started thinking about data

analysis, and it's been really amazing to see all of the progress that we've made, and

I spent a lot of this time personally working on the chicken and egg problem of statistical

computing and data analysis in Python.

We didn't call it data science back then, I guess now we can call it data science, but

I was really concerned about we had this great programming language with a scientific computing

ecosystem that was a really great platform to build on, but it was still hard to do what

we now call data science.

One of the biggest trends over this time period is the trend from closed source software to

open source software, and so many of you maybe have painful memories of what things

used to be like, when if you wanted to do statistics or data analysis, usually it meant

writing a check, because no one ever got fired for buying MATLAB, and you can understand

the skepticism in using open source software for these problems, and I remember talking

with my bosses at the time about Python, and they would ask, well, who built this software,

can we trust it, and I would say, well, a lot of them are grad students, and they say,

well, are they computer science grad students, and I'd say, no, a lot of them are physicists

and scientists who are just trying to, who are procrastinating on their PhDs and just

trying to, you know, I think John, you know, John Hunter, who passed away this August five

years ago, started Matplotlib because he got frustrated with MATLAB's licensing policy

when he was generating plots on different servers, and there have been many factors

that have driven the growth and adoption of open source, you know, certainly the maturity

of the libraries has been a big factor, the cloud has been a huge deal, because there

are some days where you want to run a job on one machine, sometimes a hundred or a thousand,

if you needed to, you know, the licensing model for closed source software is not very

compatible with that, and certainly open source has driven the democratization of data science,

and over the years, I've been really humbled to hear from people all over the world, especially

in very poor places who, you know, have a copy of my book or are learning from the Internet

and are working really hard to learn these tools so that they can analyze data and use

that to improve their lives. The Jupyter, the growth of the Jupyter community

has also been a really amazing thing, I saw the first incarnation of the iPython notebook

in summer of 2011, and I was just blown away, now, I used Mathematica, and so was familiar

with the notebook concept, but to see that vision realized in such a natural way that

fit in with the rest of the Python ecosystem was really, you know, was really something,

I started showing it to everyone around me, and I think that viral quality to the notebook

has been a big factor in its success, but I think, you know, the iPython developers,

as they collaborated with the Julia community and others realized that the Jupyter problem

is much bigger than Python, and it concerns the general problem of interactive computing

and reproducible research, and so it's been, you know, just amazing to see this community

grow and to see so much collaboration across these different programming language ecosystems.

But I'd like to think a little bit about the future, and I spent a lot of time thinking

and worrying about the future, mostly because I wanted to get here faster, because we would

all like that, and I don't know that we would have been able to predict accurately the last

ten years, so who knows where we'll be in 2027, maybe we'll all be programming in JavaScript,

I mean, it's entirely likely, but I think there's, you know, there's some things that

we can be doing now to lay the foundation for a better future, and I'd like to talk

about some of those things.

So one of the major themes right now, and I expect this to continue for many years,

is what I call the AI arms race, faster, more scalable, more cost effective machine learning.

So I was in a talk by Michael I. Jordan, a machine learning researcher, and he quipped

that AI is really machine learning, which is pattern recognition, and that's definitely

true, and you have all of these cutting edge new machine learning technologies being developed,

but to use machine learning models, you still need to load and access data and clean and

manipulate it, explore it, find features, and then do all of that in a reproducible

way so that whenever new data comes in, you can update your model.

So no matter how sophisticated the AI algorithms get, we're still going to need all of the

tools that we've developed for all the work that happens before you're fitting your models.

The hardware landscape has also changed a great deal, and continues to change.

So you know, a decade ago, seven years ago, when I was starting out building pandas, most

computers didn't have that much RAM, we were dealing with maybe 2GB or 4GB or 8GB, processors

generally had one or two cores, disks were pretty slow, spinning rust, as some people

call them, and so we've seen disks get 10 times or more faster, you can buy a desktop

processor from AMD with 16 cores, you can get a machine with a terabyte or two terabytes

of RAM, and the data sizes that we're working with have also increased as we were collecting

more and more data, but if you look at the tools that we are using, they have not scaled

so gracefully to be able to take advantage of modern hardware, and to be able to use

this hardware to its maximum capacity is going to be a lot harder and require a lot more

engineering than it took to build the software that we use today.

So one problem that I think a lot about is the fact that when you go beyond the front

end, tools like Jupyter, and you go down into the Python ecosystem, the R ecosystem, and

the other areas where people do data science, there isn't a great deal of collaboration,

I would even go so far as to call these communities tribal, you know, I'm a Python person, I'm

an R person, and that becomes a part of your identity, and it's very rare that you see

software being developed that can be used across silos.

There's tools for calling Python code from Julia, you can call R from Python, but as

a way to build software in general, that's not the predominant method.

There's many different things that are in the silos, so you need to access data.

When you access data, you need to put it someplace, so those are your data structures and what

I call memory formats, things like data frames.

You need compute engines to manipulate those data structures to run, to do exploratory

analytics to engineer features, and then you need analytics toolkits to fit statistical

models and machine learning models, and if you look from left to right, it's a funnel,

so if you have a problem earlier on in the process, if you can't read a file, if you

can't find the right data manipulation, if you can't compute the right thing, you aren't

going to get to the model development stage, you're going to fall off and have a bad time.

And so if you just look in the Python ecosystem and some of the tools, this is not a comprehensive

list, by any means, there's a consistent theme here in that just looking at the pandas project,

that we've had to develop software in many different domains.

We've written our own CSV readers and many other data access layers, we have a half-baked

implementation of an in-memory SQL database, we have developed our own data frame, data

structures, so that's something I think about, the fact that we own all of the software,

we built it all, and it's not accessible if you're not a Python programmer and you don't

use pandas.

So I started thinking more critically about this at the end of 2015, and I think my thoughts

had gone back a pretty long time, at the end of 2013, I gave a talk whose subtitle

was ten things I hate about pandas.

And people thought that was funny, they were like, you built it, you know, shouldn't you

really love it?

But I knew about all of its flaws, and at the end of 2015, we started talking about

ways that we could make the project better, and one of the things that's come out of that

discussion is the fact that we would like to own less of the infrastructure that enables

projects like pandas to exist, so that's, you know, to think about how much time we've

spent writing CSV readers, but we've spent all that time because it is so important.

And so my hypothesis is what if we could make the silos quote smaller and have some kind

of software that we share across ecosystems, and it would make it easier in the future

to build projects like pandas, to build projects like dplyr for R.

When you think about what are programming languages, programming languages are user

interfaces for describing computation, and we choose our programming languages for many

reasons, some of them it's because the people that we work with use that language, but one

of the reasons that Python and R and other data science languages have become so successful

is because the programming languages are maximized for your productivity so that you can get

a lot of work done in a short amount of time, and I use the iceberg metaphor in talking

about programming languages and data science systems, because the amount, the portion of

the software that you see is a fairly small part of the code base, you see the user API

that the engineers have created, like this is how you interact with this piece of software,

but there's a huge body of code that you don't see, and that frankly you don't want

to see, there's parts of pandas that if we showed you'd be like oh my goodness, I never

want to see this again, but this is great, because as engineers this allows us to hide

all this complexity from you, and show you only the parts of the library that you need

to get your work done. So if we look at some R and Python examples,

again the code looks very similar, so here we have an R example using dplyr reading a

CSV file, and the Python code for that looks almost the same, but it uses a different implementation

under the hood. So my hypothesis is what if, and here's the big what if, we could create

what I call a shared data science run time that could be responsible for some of these

tasks which are common to all of the frameworks. Now this might sound like total vapor ware,

so I'm going to give you an idea of what I think needs to go in that shared run time,

and how we might go about building it together as a community.

So the first part, and here's where we have to take a leap of faith, we have data frames

in most languages, Python has a pandas data frame, R has a data frame, we call them data

frames, but in reality our data frames are very different when you look inside. So that's

a problem, because when I write an algorithm that manipulates a pandas data frame, that's

not some code that you can take and use to process the data that is inside an R data

frame, and vice versa. So if we want to build algorithms that can be shared between environments,

we have to have a data frame in memory format which is portable across environments.

A second part of the problem is that we need to be able to share data between environments

without incurring any overhead, so if you have a data frame in Python and then you want

to run some R code on it, if you have to pay this huge cost to move that data from Python

to R, you might be incentivised not to do it at all and just figure out a way to do

it in Python, so if we could make these transitions between ecosystems, including things happening

in the Java world, that would be really powerful and would help make our tools a lot more composable.

Third part of the problem is it's not enough to have a portable data frame, we need to

be able to get data into it, so we need to create optimised data connectors to all of

the formats that we use in practice. So this would be really great, because me as a pandas

user, that means that I could stop maintaining a lot of pandas.read CSV, if you're an R user,

the code that implements R read CSV could also, the burden of developing that could

be shifted to a much larger group of developers. A last part of this, and maybe the hardest

part, is building a computation engine that is able to compute things, to perform computations

natively on portable data frames. And this is a big topic, and I could give a whole hour

long or three hour long discourse on all of my ideas about what we could build in this

type of engine, but the key things are that you need to be able to embed it in existing

systems, so it needs to be embeddable in an R application, embeddable in a Julia application

or a Python application, you need to be able to extend it with functions which are written

in the host language, so if you write a new function to extend the computation engine

in Python, that it can exist as a first class citizen, and you don't pay a performance penalty

when you evaluate that code. And if you look at systems like Apache Spark, which have Python

and R APIs, this has been one of the largest pain points that when you want to extend Spark

with user defined functions, you pay a heavy penalty.

Also, another slightly esoteric point is that if you describe a sequence of operations using

this library, you would like to create a representation of that computation that could be carried

over to another environment and evaluated in a portable way.

So a couple of years ago, I started thinking, you know, I can't do this alone, and I tried

to find a group of people who were like minded and wanted to work on this problem together.

We decided to create a project in the Apache software foundation which we are calling Arrow,

and it doesn't solve all four of these problems, but we have been most focused on building

portable data frames and zero copy interchange between environments, so this is what I have

been spending a lot of the last two years working on, so if you see me being very busy

on GitHub, a lot of it is building the Arrow format, because that means I can build algorithms

against a data frame that is the same across languages.

And so in thinking about how we are approaching the Arrow problem, we need our data frame

to be a superset of the things that you can do in R, in pandas, but also SQL engines,

in particular columnar SQL engines.

It needs to be optimized for processing performance, so that it's efficient on CPUs, and we are

also seeing Arrow used on GPUs and other hardware as well, and another part of the problem is

that it needs to be done in a way where the project is owned by the community and not

by an individual or a corporation, and so we have done it as an Apache project so that

our development process is open and transparent and that the Arrow project is owned by you,

the community.

So many of you might have seen that Hadley Wickham and I got together at the beginning

of last year, I told him about Arrow, and one of the first things that we did is we

said, let's pare down Arrow to just the bare essentials for Python and R and make a file

format that's interoperable between R and Python, so we are really excited to ship that

and to socialize the idea of interoperable data and being able to transition efficiently

between environments.

So I'm happy to report that there's been quite a bit of adoption of Arrow amongst a

variety of open source projects which I'll allow you to explore on your own as I'm running

out of time, but this is a big problem, but seeing what we've accomplished in the last

ten years, I believe this is something that we can all build together and the more we

collaborate the faster we can bring about this future, and as I like to say, when you

have a chicken and egg problem, sometimes the best thing you can do is be the chicken,

so please, be the chicken.

Thank you.