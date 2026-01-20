---
title: "Python for Quantitative Finance"
summary: "Video at PyCon 2010"
date: 2010-02-19T00:00:00
tags: ["video", "transcript"]
slug: pycon-2010-python-for-quantitative-finance
word_count: 4929
source_file: transcripts/2010-02-19-pycon-2010-python-for-quantitative-finance.md
content_type: transcript
event: "PyCon 2010"
video_url: "https://archive.org/details/pyvideo_305___python-in-quantitative-finance-158"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this PyCon talk, I introduce pandas, a library I had been developing for two years at AQR Capital Management.

## The Problem Domain

I define quantitative finance as applying mathematics, statistics, and econometrics to model market phenomena and build trading strategies. My firm focused on daily and monthly analysis rather than high-frequency trading, working with time series and cross-sectional data. The core challenges: data manipulation of unreliable financial data, statistical modeling, risk measurement, and strategy development.

A key pain point was the fragmented workflow common in quantitative finance: "often you do research in one language and you implement it in another." Teams would prototype in MATLAB or R, then reimplement everything in C++ or Java for production.

## Python's Emerging Ecosystem

I positioned Python as suited to solve this research-to-production problem, citing NumPy, SciPy, IPython, and Matplotlib. I noted Python's advantage as "a really great language for building systems" compared to R and MATLAB, enabling teams to "research and implement in the same language."

I acknowledged gaps in Python's statistical capabilities, particularly the lack of econometrics libraries that were abundant in R, and highlighted the emerging scikit-stats-model project.

## Introducing pandas

The core insight behind pandas: "link the labels to NumPy arrays and provide a lot of convenience methods for reshaping the data and indexing the data." This addressed the problem that most tools "assume that your data is very clean, which is, again, most often not the case."

pandas introduced two data structures: the Series (one-dimensional labeled data) and the DataFrame (called "data matrix" in early versions). These combined NumPy array performance with label-based indexing, automatic alignment of mismatched data, and handling of missing values.

## Live Demonstration

The demo showed pandas automatically aligning data from different sources, handling missing values, and providing methods for data manipulation. One example analyzed Apple stock returns by day of the week using group-by operations, showing "it's highest on Friday and lowest on Tuesday" due to weekend effects.

The demo progressed to multi-asset analysis with correlation calculations and visualization, then demonstrated running 1,000 rolling regressions in about a second to show how statistical relationships between stocks evolved over time.

## Vision

My stated goal: "build better tools that people can use for finance and for building statistical models so that you can really focus on doing research and not necessarily on worrying about unclean data." I aimed to create "an R-like statistical environment in Python that integrates with all your other system code."

## Key Quotes

> "Often you do research in one language and you implement it in another."

> "Python is just a really great language for building systems, in particular compared with R and MATLAB, which are sort of scientific research environments, and they aren't really system languages."

> "One interesting thing about maybe using Python is you can research and implement in the same language."

> "Financial data, you know, can really never be trusted."

> "A lot of tools assume that your data is very clean, which is, again, most often not the case."

> "The approach that I took to the problem was to link the labels to NumPy arrays and to provide a lot of convenience methods for reshaping the data and indexing the data."

> "You can have an R-like statistical environment in Python that integrates with all your other system code. So you don't really have to switch environments."

> "The goal of it is to build better tools that people can use for finance and for building statistical models so that you can really focus on doing research and not necessarily on worrying about unclean data."

---

## Transcript

Hi, my name is Moshe Zadka, welcome to the late afternoon session here in PyCon, I hope

everyone's having fun, our next talk is Python in quantitative finance by Wes McKinney.

Thank you very much for coming, so in this talk I'm going to talk a little bit about

the work that I've been doing for the last few years in the financial industry, but really

I'm here to talk about Python, being PyCon and all, to talk about how Python can be useful

in doing financial work and also kind of talk a little bit about where Python has been successful

in terms of building tools that people can use to do financial research and to solve

financial research problems.

So give you kind of just an overview of the talk, so talk a little bit about the problem

domain that I've encountered, talk a little bit about me and the company that I work for,

and talk a little bit about sort of common research tools, you know, languages and programming

environments that people use to do finance.

Secondly, talk about Python and kind of tools that are available in Python and for people

who would choose to build research systems and build production systems for both research

and for implementation and trading, what's available to the Python programmer.

The second major portion of the talk is to talk about a library that I've built over

the last couple of years called pandas, which is very helpful for doing finance work, so

talk, you know, kind of give a little bit of background on the library and spend about

ten minutes doing an interactive demo, so do some stuff in the console, you know, kind

of show you how things work and talk about some related projects.

So when we say quantitative finance, just kind of want to clarify what I'm talking about,

so this is the area that we're applying mathematics to model market phenomena, you know, this

is through the use of statistics and econometrics and stochastic calculus and lots of things

that you probably, you know, if you're not in the finance industry, you've probably read

about them or, you know, seen articles or, you know, seen them in school.

I guess in my work, one of the big focuses in using statistics to try to find relationships

between data sets, and secondly, you know, once you've done all those things, you know,

we want to build strategies that we can trade and, you know, hopefully make money.

And of course, you know, in the last, you know, ten, fifteen years, there's been kind

of a huge explosion of quantitative finance roles and people, you know, sort of going

into the field, you know, particularly with the availability of, you know, computing power

and so you have lots of, you know, mathematicians and physicists and computer scientists that

are taking skills they would have otherwise applied in academia and using them to try

to, you know, to build models that make money.

So a little bit about me.

So I have a math background originally and I've been in the industry for about three

years.

The name of my company is AQR Capital Management, stands for Applied Quantitative Research.

So it was founded about a little over ten years ago, in 1998, around the time that,

you know, you may have heard of a little hedge fund called Long-Term Capital Management that

blew up in 1998, so we started around then.

So we have hedge funds and we have long-only products.

And kind of on the last point, a lot of our stuff is looking at things on sort of a daily

basis or a monthly basis and we're not doing sort of the sorts of high-frequency trading

that you might read about, you know, sort of these days it's been kind of vilified in

the media, you know, sort of high-frequency trading is responsible for the financial crisis

and is sort of destroying, you know, destroying the common man.

So the sorts of problems that we're solving, I'm just going to touch briefly.

A is sort of the data manipulation problem, financial data, you know, can really never

be trusted, you know, if you write a function, data comes in, you really can't make very

many assumptions about the data, it could be missing observations, it could be different

frequency, lots of different, you know, problems that you have to kind of always worry about

when you're working with a new piece of data.

Once you sort of have the capability to work with the data, you know, we're interested

in using statistics techniques to, you know, to fit models on the data, you know, sort

of using standard econometrics, you know, linear regression, other sorts of models.

And also we'd like to, you know, kind of measure in a systematic way, you know, how risky are

assets that we might be interested in trading.

You know, at least in the last, you know, two, three years, you know, people have been

very concerned about this whole field of, you know, sort of measuring and forecasting

risk, you know, it's, you know, really we didn't do a very good job of it, we being

sort of the finance industry, you know, prior to 2007, I think we sort of learned a very

hard lesson.

And lastly, of course, is sort of the area of, you know, we fit some models, we can deal

with the data, and we want to actually, you know, build strategies and, you know, decide

what's a profitable strategy that we can implement.

So the basic units of financial data that I'm going to talk about are the time series,

which you're all familiar with.

I'm just showing you some stock prices for Apple and Google, you know, very, you know,

a very common thing you encounter.

And the second is the cross-section, so you have a number of pieces of data at one single

point in time.

So the tools that people commonly use, you know, things you're probably familiar with,

like MATLAB and things that are a little more statistics-oriented like Stata and eViews

and R. And I'll speak a little bit about R because it's a language which is very widely

used in statistics and econometrics and also, you know, for the same reason in finance.

It has a very vibrant community and has, you know, tons of open-source packages available

on CRAN.

And, you know, one big thing is that R has been available to Python programmers.

People would like to use the R functionality through the RPy interface, which is still being

actively developed.

So for many years, you know, things in R have been out there and, you know, are callable

through Python.

One problem that I've encountered with using these languages is that, you know, often you do

research in one language and you implement it in another.

And, you know, there's a lot of work that goes into basically replicating models and

re-implementing things in another language once the research has been done in MATLAB,

say.

So you have a lot of people, you know, rewriting things in C++ or in Java.

So one interesting thing about maybe using Python is you can research and implement in

the same language.

So Python, you know, many of you are probably familiar with some of the efforts that the

Python sort of scientific community has undertaken over the last ten years or so.

You know, in particular, sort of the NumPy and SciPy libraries have become very mature

and offer a lot of flexibility and really robust tools for, you know, for implementing

algorithms and for writing, you know, very stable and fast code.

Two other projects which are very interesting and which, you know, certainly help a lot

are IPython and Matplotlib, which I'll show in the demo.

IPython's, you know, a really wonderful interactive console developed by, you know,

Fernando Perez out at UC Berkeley and a number of other people and has really sort of grown

into a really excellent development environment in addition to being useful for scientific work.

And, of course, Matplotlib for both interactive plotting and sort of a, you know,

automatic API for generating plots.

And of course, there's always sort of the speed question

in using Python, and there are sort of lots of recourses

available to speed up your code using C and Fortran,

and particularly the Cython project has seen a lot of work

in the last few years to bring it closer to NumPy,

so you can write very fast extensions very easily

that run right against the NumPy C API,

and that used to be a lot more work to do,

having to write C code and deal with reference counting

and everything, but Cython takes care of a lot of that

for you.

Of course, as we all know, Python is just a really great

language for building systems, in particular compared

with R and MATLAB, which are sort of scientific research

environments, and they aren't really system languages.

So with Python, we can bring some of that to the table

in terms of being able to build robust and stable systems.

Some of the weaknesses that are still there in Python,

I guess, sort of has to do with a chicken and egg problem

with who's using Python and who's using the other languages

in that there are not a lot of statistics

and econometrics libraries, which are the tools

that we use all the time.

Lots of people are implementing in R and MATLAB

and releasing their code, but not as much in Python,

and that's starting to change.

One library that is making a lot of headway

toward implementing econometrics tools in Python

is scikit-stats-model, so it's really been in the last year

that that's been actively developed,

and I encourage you to check it out if you're interested

in doing more advanced statistical models in Python.

Another problem, of course, is that a lot of tools

assume that your data is very clean,

which is, again, most often not the case.

So my goal, I guess, in this talk and with the library

I built is to try to build tools that make Python

a better choice for finance work

and for building statistical models,

and I'll show you a little bit of that

in what I'm talking about in the demo.

So the pandas project, I'll tell you very briefly,

just so I have enough time,

but it's been actively developed

for the last two years at AQR.

So the idea is that I want data structures

which really understand time series data

and cross-sectional data that can be used

in interactive console, but can also be used

in building production applications

that have various performance needs and robustness needs.

So the approach that I took to the problem

was to link the labels to NumPy arrays

and to provide a lot of convenience methods

for reshaping the data and indexing the data.

So basically gluing together data sets

and working with these sort of messy financial data

can be quite a lot easier.

And the name itself comes from panel data,

which is a very standard term in econometrics

and now in 2010, this library's gonna become

a really very important part of the work

that is happening at AQR and the systems

that we're building.

So kind of what's in the library?

I guess there's data structures,

which are based on NumPy, which are mainly intended

for handling one, two, and three-dimensional data.

A number of people have asked me

why don't I just make an n-dimensional object

that has all this functionality,

but really you don't really encounter

four-dimensional or higher-dimensional data sets.

So I think as soon as I do,

or as soon as a lot of people are running

into those sorts of problems, then we can talk.

There's a lot of built-in statistical functionality

for standard time series methods.

You wanna compute moving averages,

moving or expanding standard deviations,

really standard stuff that you are interested

in being able to compute very efficiently,

and all that is there.

And also what we're doing with the library

is we're building econometrics tools,

which use the same data structure.

So you can have an R-like statistical environment

in Python that integrates with all your other system code.

So you don't really have to switch environments.

If you need to run a regression in R and use RPy,

you don't have to do that anymore.

You can do it all in Python with no conversion

and no messy interface code.

How am I doing on time?

All right.

All right, is that fairly legible?

Okay, so one of the,

just import, I'm sure everything's imported here.

So one of the, I guess, very basic data structures

that you work with is the time series.

So you have, and this is one of the core objects in pandas,

which is the series, and the labels here

don't necessarily have to be dates.

They could be strings or stock tickers or really anything,

but it's a vector plus labels.

So here our index happens to contain Python date time.

And we can sort of treat this vector like a dictionary.

So if we want to grab a value for a date,

then we can get it just like a dictionary.

But at the same time, it's a vector.

It's a NumPy subclass, in fact.

So vectorize operation, scalar multiplication,

multiply two time series together,

and it goes very fast using

kind of the built-in NumPy functionality.

But a very common situation is you have a vector like this

and another one that you got from some other source of data

and they aren't labeled the same.

And this is a big problem because you have to

sort of make them the same shape

and you don't want to add two vectors together

and sort of mismatch the data.

So this library, when you add two of these objects together

it matches the labels in places where

one is missing these dates.

For example, you get a not a number.

So they all have the built-in not a number handling.

So your standard NumPy statistical operators,

things like mean and standard deviation,

we all have as a count function,

are all kind of know that you have these missing data points

and when you request the mean

you don't want to get a not a number

and you don't want to have to worry about the fact

that you have data missing and it just excludes them

and computes the mean or standard deviation

without the missing values.

Of course, we can take a look at this vector

and we can explicitly reconform it

to the larger time series index.

So you have that built-in functionality

so that the thing that you input is any sequence of labels

and it reconforms the vector

to that set of dates here, for example.

So going back to this guy that has these missing values,

you might have gotten this data from somewhere

and let's say you want to take this 404 value

from December 2030 and you want to propagate it

through the end of the year.

Then you can use the fill method and it fills that.

value in, so you can very easily fill in holes in your dataset using various methods.

Or for example, you might want to just drop all the missing observations, so you call

the valid method and they're gone.

So I'll move to a slightly longer time series.

This is a history of prices of Apple.

So I'll plot it on a graph.

So this is Apple's stock price since 2000.

This is just a Matplotlib window.

So these are prices, and in finance we're most often interested in the returns.

So take this guy, divide it by itself, shifted by one, so price divided by previous price

minus one, call this returns.

And so now let's say we were interested in finding out when the returns are most volatile

by day of the week.

So we can use the group by function, say pass in a lambda, x.weekday, so that's going

to be called on all the dates, basically all the data is going to be bucketed by the unique

values of this function that you pass in, and then we're going to aggregate using the

series STD function.

So we get a series result, and then I plot it, and so we can see this is basically return

volatility of Apple by day of the week, so you can see it's highest on Friday and lowest

on Tuesday, so I don't know really the reason for this, but there tends to be more volatility

on Friday, and people don't want to hold stocks over the weekend, so you see a lot more price

movement on Friday, but it's kind of an interesting analysis.

So we're not always interested in dealing with just one time series, often we have multiple

time series, and we want to do the same sort of operation on many time series at once.

So the object for this is the data matrix, which is kind of the analogue to the series

in that it has a lot of the same built-in functionality, except that when you combine

two of these data structures, you're also matching on the column labels in addition

to the row labels.

So if we had a smaller data matrix, which has sort of a smaller data set, and we add

them together, then we get basically something that's the union of all of the labels here,

the places where the data matched up, you have the addition, and everywhere else you

have not a number.

Similar to the series, this object is also kind of like a dictionary, so if we go back

to this guy, if we just want the data for Apple, we just index it like a dictionary,

and we get a time series out of it.

We could also put a column in, so I'll put in the West column of zeros, and you see it's

added in there on the end, and then I can delete it.

And of course, standard scalar addition or multiplication works just like you'd expect.

You can also add time series to data matrix.

So if you wanted to add a time series to each column of this guy, you can do that,

and it basically vectorizes and propagates to all the columns, so I don't know what the

significance of adding Apple prices to Google prices is, but you can do it.

Similar kind of looking at our statistical operators, if we call standard deviation on

this, we get the standard deviation by column, and we don't have any values for Yahoo, so

we have not a number there, but we have otherwise the standard deviation, excluding the missing

data for all of the others, but here we can also pass in an axis number, so the first

axis is over the rows, and so you get the cross-sectional standard deviation at each

point in time.

So now I'll go to sort of a slightly larger data set, so we have all the prices for these

guys since the beginning of 2000, and convert them to returns using exactly the same method

as before, and so here, now that we have multiple time series, we might be interested in the

correlation between them.

We call the core function, and we get a correlation matrix, also represented as a data matrix,

so you can see that Apple and Google are 47% correlated since 2000.

We can also plot this guy, have the nice Matplotlib integration, and you see all of these prices

are plotted on the same graph, and of course, Google starts in 2004 at its IPO, so you don't

have that data prior to that.

So I'm running low on time, so I just wanted to show you a couple quick things.

Sort of inside the library, I mentioned there's sort of the start of building an econometrics

toolbox, so if we look at these returns, let's say we wanted to fit some kind of a regression

model to try to see what do Google and Microsoft and Yahoo tell us about Apple returns.

So what we'll do is we'll pop Apple returns out of this data matrix, so it's no longer

in there, and so then we'll call OLS and we'll say Y is Y, which happens to be our Apple

returns and X is returns, so it's everybody else.

And we get kind of a nice regression output, which gives us sort of the estimated coefficients

for Google, Microsoft, and Yahoo, and sort of your statistical significance and R squared

and all your fun stuff.

Now if we were interested in running some kind of a predictive regression, let's say

what does Google returns and Microsoft returns tell us about Apple returns tomorrow, then

we could just shift Y by one, and now let's run a rolling regression.

So we want to run a regression at each point in time and see how the relationship changes

over time.

So let's say window type rolling, window 250, so about a one-year regression.

And so if we say model.beta, now we get a data matrix of regression coefficients over

time and see now it ran 1,000 regressions and that took only about a second, so that's

very, very speedy.

And so now we can plot these, and we see some kind of a statistical relationship

that there's a positive loading on Google and a negative loading on Microsoft.

No idea what the significance of that is, but it happens to be what the regression shows.

So anyway, there are lots of other neat things in this package, and I certainly encourage

you to check it out, and kind of the goal of it is to build better tools that people

can use for finance and for building statistical models so that you can really focus on doing

research and not necessarily on worrying about unclean data, so it tries to sort of

solve that problem.

So a couple related projects, you can look in the slides and sort of look up these projects,

there's been a lot of sort of related work in this area, and of course lots of ideas

for future things to do with the library and in finance with Python.

Alright, I'm out of time, so thanks very much.

I didn't get to cover quite as much as I wanted in the demo, so anyone who's...

I talked to Enthought, who does a lot of finance consulting work, and Visual Numerics, who

also work with financial firms, and so we're going to do some open spaces that are related

to this.

I'll do an open space for this, so if people are interested, we can sit and I can show

you some stuff you can do with the library, and we can talk about other things.

I've got to go put it on the board, but yeah.

I guess this thing isn't on either, but what do you use to store the data?

You showed us a lot about manipulating the data, but how do you guys store it?

Okay, so the question is how do we store the data?

So there are many approaches.

We store a lot of data in SQL databases, which isn't the most ideal solution, just because

SQL isn't really designed for time series data, but I personally have had a lot of luck

using PyTables and HDF5 to store data, which I highly recommend.

And what's that?

HDF5.

HDF5.

Sorry.

HDF5 is the PyTables storage format, so PyTables is a really fantastic project.

I didn't mention it in the talk, but ... Maybe it is on, is it?

So you're using floating point values to do all your calculations, but you're using financial

data.

Are there any sort of pitfalls to that approach?

So are there any pitfalls to using floating point data?

So we're using 64-bit floating point numbers.

I haven't run into too many problems.

Your precision is about 1e to the minus 13, or 1e minus 15, and that tends to work out

pretty well.

Hey, Wes.

Very impressive.

I like it.

Just two quick questions.

First, how do you handle, or do you handle holiday calendars, like exchange holidays,

different countries, being able to apply it to the data?

And the second question, and I'll go sit down, is in terms of if you want to see the data,

let's say weekly or monthly, changing the periodicity, how's he manipulating it?

The library doesn't have built-in handling of holidays and open and closed times and

that sort of thing, just because typically you have to pay for that data, I guess, information

about exchanges and countries' holidays.

There is the PyTZ library, which has a built-in historical time zone database and tools for

converting to and from local time zones and to and from UTC.

And it also, I think it has holidays, but I could be wrong.

And sort of going back to this, this is daily data that we're looking at.

I didn't really have enough time to show you, but it does have the ability to convert to

monthly frequency and back and that sort of thing.

So I'm out of time, so I'll organize an open space and if you saw something you like, then

come by and we can talk some more.

Thank you very much.

Thank you.

Thank you.