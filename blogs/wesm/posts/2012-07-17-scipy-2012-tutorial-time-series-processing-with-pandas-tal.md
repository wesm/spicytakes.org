---
title: "Time Series Manipulation with pandas"
summary: "Talk Video at SciPy 2012"
date: 2012-07-17T00:00:00
tags: ["talk video", "transcript"]
slug: scipy-2012-tutorial-time-series-processing-with-pandas-tal
word_count: 3495
source_file: transcripts/2012-07-17-scipy-2012-tutorial-time-series-processing-with-pandas-tal.md
content_type: transcript
event: "SciPy 2012"
video_url: "https://www.youtube.com/watch?v=bgfLrKpc4jA"
---

{{< video https://www.youtube.com/watch?v=bgfLrKpc4jA >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This SciPy talk provides a development update on pandas, focusing on the time series functionality overhaul in spring 2012.

I explain my transition from R to Python in 2007-2008 revealed a gap in high-level data manipulation tools: "I wasn't willing to stop at where those languages ended, which kind of was where the pandas project came from."

## DateTime64

The major technical enabler was NumPy's new DateTime64 dtype, which I describe as "essentially just an int64" representing timestamps at nanosecond resolution. Only about 600 years can be represented, but "we probably don't care that much about nanoseconds prior to the year 1700." This provides binary compatibility with existing time series databases.

## String-Based Indexing

The new indexing system allows slicing data using simple string representations rather than datetime objects. Inspired by R's XTS package, pandas supports partial indexing: specifying "2001" selects all data for that year, "2001-03" narrows to March 2001. "It really kind of falls off the fingers when you're working interactively."

## Resampling

The resample method addresses one of users' most frequent questions about converting between data frequencies. Built on pandas' groupby framework, it allows conversion from high-frequency to low-frequency data and vice versa.

## Period Logic

Period logic, lifted from the SciKits time series library, represents time intervals rather than timestamps, enabling temporal arithmetic. Users can start with an annual period like 2001, convert to monthly frequency, and chain operations through time hierarchies.

## Time Zones

I admit I contemplated rewriting PyTZ entirely. The solution stores all timestamps internally as UTC, making time zone conversions "free operations" since they only change interpretation, not underlying data.

## Documentation

I announced my upcoming book aimed at "a really solid, coherent introduction" to Python data analysis. I identified documentation fragmentation as a persistent problem: "finding the right information and getting up to speed on all the tools is often a bit bewildering because all the documentation is scattered across many different projects."

## Other Improvements

pandas 0.8 included hierarchical indexing, rebuilt merge and join infrastructure, and enhanced groupby functionality.

## Key Quotes

> "I wanted some of those features in Python, but I wasn't willing to stop at where those languages ended, which kind of was where the pandas project came from."

> "One of the trouble problems with open source is that finding the right information and getting up to speed on all the tools is often a bit bewildering because all the documentation is scattered across many different projects."

> "The DateTime64 Dtype... is essentially just an int64. So it's an 8-byte integer that NumPy can interpret as being of a particular unit."

> "One of the downsides of going to nanoseconds is that you can only represent about 600 years... I guess we probably don't care that much about nanoseconds prior to the year 1700."

> "Pandas is really all about being used interactively at the command line as well as building applications."

> "It makes it very nice and really kind of falls off the fingers when you're working interactively and exploring a data set."

> "I was on Twitter, I think maybe a month or so ago, and I said, my god, I've got to rewrite PyTZ in a fast way. And John Hunter told me to step back from the ledge. Unfortunately, I had to keep going on it."

> "The really nice thing about this is that under the hood, all of the timestamps are represented in UTC. So this is actually a free operation."

---

## Transcript

Well, thanks everyone for coming, and thanks to the SciPri organizers and Nthoth for having

me.

So I'm here to talk a little bit about pandas.

I imagine that some of you are in my tutorial and already are familiar with a lot of what

I'm about to talk about, so I just wanted to give a little bit of a development update

and tell you about what's been going on in the library for the last year, in particular

because there was a really major effort this spring to overhaul the time series functionality

in the library, and to give you some more background on that, tell you what's the story

there and where things are going with the library.

So pandas is a data manipulation, data analysis tool that's built on top of NumPy.

NumPy by itself is a pretty low-level tool, so when I started programming in Python at

the end of 2007, beginning of 2008, I was used to programming in R and other statistical

analysis, data analysis languages where you had a lot more high-level data manipulation

tools, and I wanted some of those features in Python, but I wasn't willing to stop at

where those languages ended, which kind of was where the pandas project came from, and

I've been working very actively to turn it into one of the easiest to use and fastest

and most productive data manipulation tools that you can find anywhere.

So we just had a major release at the end of June, version 0.8.

It's been a really active year since I talked about pandas in a lightning talk last year

at SciPy, and we really kind of manned up on the development, and it's been really hectic

last year, and there's been a huge amount of progress and growth in the user base and

the community, so it's been very, very exciting to see some growth and to see people use the

library to solve their problems.

So anyway, pandas are in good shape.

So some of the major things that have happened in the library, hierarchical indexing, multi-level

indexing got added, the sort of merge and join infrastructure got rebuilt and is now

one of the best merge utility, in-memory merge utilities in any open source project that

I know of.

The group by NGIN got a lot of work and is now similarly, in my opinion, a much better

alternative to having to write out the data to an SQL database in order to do data aggregation

and that sort of thing.

So these other things as well, but I'm here to talk about time series.

I've also got a book coming out, and I hope that if you buy it, that you find it useful.

I wanted to give people a means to get educated in, especially for new Python programmers

who've never used NumPy, IPython, Matplotlib, pandas, that they have a really solid, coherent

introduction to this tool set, especially refugees from other languages like R.

Really, I think one of the trouble problems with open source is that finding the right

information and getting up to speed on all the tools is often a bit bewildering because

all the documentation is scattered across many different projects.

It isn't very well documented, so it's something I hope to solve with this book.

So a little bit of an overview of what's been going on in time series.

The major thing that changed in NumPy that enabled a lot of this work and to make it

all really fast and not use very much memory is the new DateTime64 Dtype, which mThot and

other people have built and added to the library, and is really, you know, really none

of this would be, everything would be a lot more difficult without it.

It enables supporting timestamps and working with data at the nanosecond resolution.

So DateTime objects in Python only support microseconds, so being able to work at a finer

grain resolution is a boon for a lot of users who previously might not have been able to

use Python.

There's a resampling infrastructure, so you can do conversions up and down in frequency

very easily now, and that all builds on pandas' groupby infrastructure.

And now I think pandas is one of the best places to do time zone manipulations.

If you've ever worked a lot with time zones and at some point along the line you've probably

wanted, you know, just, okay, I'll be happy to wake up at, you know, 2 a.m. UTC or something

like that.

And the last thing with this endeavor was that I thought there was a lot of really great

stuff in the SciKits time series library, and I was sorry to see that the library hadn't

seen a lot of active development since 2009.

So I wanted to take the good parts of SciKits time series, move them into pandas, and give

people with legacy code bases that were heavily dependent on SciKits time series a way that

they could upgrade to pandas and sort of participate more actively in ongoing development.

So the DateTime64 Dtype, for those who aren't familiar, is essentially just an int64.

So it's an 8-byte integer that NumPy can interpret as being of a particular unit.

So years, hours, minutes, nanoseconds, it even goes down to a very fine-grained resolution.

Because of the hardware limitations of the datatype, depending on the unit, you can

only represent a certain amount of time.

So one of the downsides of going to nanoseconds is that you can only represent about 600 years.

So I felt it was a worthwhile trade-off.

And I guess we probably don't care that much about, you know, nanoseconds prior to the

year 1700.

There are a number of time series databases that provide nanosecond support.

So having binary compatibility with time series databases in Python is fairly important.

Now, in pandas, there's a...

So all of the axis indexes, like the series and data frame, row and column index, provides

basically a subclass structure for you that you can define new index types.

And the datetime index is an axis index that has datetime 64 values.

The scalar values, so if you select the first element, come out as timestamp objects.

And I'll mention very briefly what that is.

Namely, it's a subclass of datetime.datetime that knows how to deal with nanoseconds and

has better time zone support.

So working with fixed-frequency time series, pandas doesn't force you to be fixed-frequency.

You can have completely irregular data and go about your business and never worry about

what frequency your data is.

But if you do, there's lots of different frequencies which are implemented, and there's

nice string aliases.

So you can say D for daily or 4H for four hours.

So you can combine the base unit along with a multiplier to derive many different frequencies.

You can even do things like 1H 30 min and get one hour 30 minutes like that.

But there's also a date offset.

So there are classes which define the frequencies, which provides a certain amount of extensibility

for plugging in custom date logic, which is important in a number of domains.

So I'm going to show you a little bit in the IPython notebook of what some of these

things look like.

And some of you might already be old hats at this stuff.

But I'm just generating a make this a little bigger.

Good if I actually ran the code.

So here is a standard pandas time series that goes for 1,000 periods.

And it was generated by the function date range, which creates a fixed frequency date

range.

And you can see that the index is now this new class in pandas 0.8, the date time index.

If you look inside, you can see that, well, there's a bug in NumPy 1.6 that affects the

string representation.

But the data type of the array involved is this date time 64 with nanosecond unit.

And if you go back to the index and you select out an element, you can see it's this

timestamp object, which is a new object in pandas.

And inside there is a nanosecond timestamp.

But otherwise, it has all of the same attributes and methods that you would come to expect

in a Python date time object.

So one of the things that I wanted to do is to make indexing and working with time series

data a lot easier.

So in older versions of pandas, you could already do things like select individual values

by using the date time to index into the time series.

And I believe you could also select and slice with dates.

You could say time series sub date and then date time value colon.

And that would select all of the data from that date onward.

So something that I wanted to do was make it so just at the command line.

So pandas is really all about being used interactively at the command line as well as

building applications.

So being able to not have to create a Python date time object to say, oh, what's the value

on September 4 that you can just type in the string and it will cast the value to date

time behind the scenes and look up the right value.

But then, of course, you can do slice operations with that as well.

So just add a colon and then you've sliced the time series up until that point.

So slicing between dates takes much the same syntax.

But there's also partial indexing conveniences.

And this was actually inspired by the XTS package in R, which is a very nice piece of

work by Mr. Jeff Ryan, that you can specify parts of a date and that will select out subsets

of data from the time series that match that criteria.

So if you just wanted all data for the year 2001 in the time series, here you could just

pass the string 2001.

And then it does a binary search and selects out that chunk of data from the time series.

If you add a month, then it just selects out that single month.

So it makes it very nice and really kind of falls off the fingers when you're working

interactively and exploring a data set.

Now, resampling is another area.

And this was something that if you've used pandas in the past, doing resampling, especially

going from high-frequency data to low-frequency data, was not easy at all.

And it was one of the biggest questions I got is, well, I have some irregular data.

I want to compute mean values for every five minutes of data.

So that's what resampling is.

There's also converting from low-frequency data to high-frequency data.

If you have monthly data that you want to combine with some daily data, you might just

propagate forward those monthly values between dates.

And that would be an example of upsampling.

So in pandas now, there's a new method.

So I'm just generating some about half a million minutely data, minutely dates, and a

corresponding time series.

So we get a time series that has, well, heck, I'll make it 5 million.

So we've got a 5 million length time series.

And now there's a new method, resample.

And I can, in here, I can put a, this is minutely data.

So suppose I wanted to compute the mean value for every day.

So I can say resample daily.

And then that computes a new time series that, by default, is the mean of the values in each

group.

But you can also put in custom aggregation functions.

If I just wanted the number of values, I could say how equals len, so the Python length

function.

And that will compute the number, the length of the time series within each group.

It can get more complicated.

You can say, you know, I want the max, the min, and the count, and specify that as a

list.

And that comes back.

Well, it didn't work.

So there goes that.

I'm not sure exactly why.

It was working earlier.

I'll figure out what the problem is later.

It's the risk of running on a development version while giving a talk.

So you have a lot of flexibility there, not only in the aggregation function that you

apply, but also how the bins are formed.

So when you resample, you have to decide which side of the bin is open.

So the default is for the right side of the bin to be closed.

But if you wanted the left side to be closed, you could say closed equals left.

And that will sort of re-bin the data in a slightly different way.

So here's an illustration of resampling, what I mean by being closed on the left and

closed on the right.

This is minutely data that we want to resample to, say, five minutely.

So you have two decisions to make.

Which side of the interval is closed, and what do you want to call the bin?

So you could call it with the left bin edge or the right bin edge.

And you have flexibility to do either of those things.

So one of the main features that got lifted, I'll use, I guess, as far as I can with my

remaining time, one of the features that got lifted from Saiket's time series that

was really useful and one of the things I really wanted to see in pandas is this idea

of period logic.

So what was formerly the Saiket's time series date object.

And so what this is, is, so it's not a timestamp necessarily, but you have an object

which refers to a period of time.

So say the year 2001.

So you have an object that represents that interval time with a particular frequency.

So the year 2001, let me call this P, and it shows us that we're 2001 with frequency

annual ending on December.

And so that I can do arithmetic with.

I can say A plus 2, that becomes 2003.

P minus 1 becomes 2000.

But what's useful, what's really nice, is that I have this sort of ordinal, this pointer

to a period of time.

And then I can convert to other frequencies and move around the time axis in a flexible

way.

So if I have 2001 and I want to convert that to a monthly period, I can say M, which is

monthly.

And then I want the last month in the period.

So how equals end.

And that gives me December 2001, whereas how equals start gives me January 2001.

So that makes it easy to be able to do things like, well, I'm year 2001.

I want next year the first month in the, well, the second month in that year.

And then, say, convert to business day frequency, and I want the third to last day in that month.

So you can see how you can chain these operations together and really efficiently move around

the time axis.

And these operations all apply to whole time series as well.

So the last thing is, the last important item that was a lot of work was time zone

handling.

So I was on Twitter, I think maybe a month or so ago, and I said, my god, I've got to

rewrite PyTZ in a fast way.

And John Hunter told me to step back from the ledge.

Unfortunately, I had to keep going on it.

But so I'm running out of time.

But I guess the main thing is that the time zone handling is built into the scalar timestamp

object and the date time index itself.

So if you generate a date range, let's say some daily data with 20 periods of data, I

can specify that this is central time.

And you get back a localized date time index.

So if I do that, and I will very quickly do, before I run out of time.

So you get back a time zone aware time series, which you can then say if you wanted to see,

well, where were all of these timestamps in Moscow at this particular point in time.

So I can specify TZ convert and then a different time zone.

And that batch converts the whole time series.

But the really nice thing about this is that under the hood, all of the timestamps are

represented in UTC.

So this is actually a free operation.

The way that we interpret the UTC points in time is really only through the lens of what

time zone we're in.

So prior having to do the time zone conversion with PyTZ, you'd be doing all of this work

to convert the values, when really it's always the same point in time.

So I guess the last item, which I unfortunately don't have time to show you, is that the

plotting has been improved quite a bit.

And a lot of this code came from Scikit's time series, another one of the really nice

features in that library.

I'm very excited to see it.

So anyway, I have time for a couple of questions.

Thank you.