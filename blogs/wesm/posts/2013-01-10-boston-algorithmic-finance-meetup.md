---
title: "Boston Algorithmic Finance Meetup with Wes McKinney"
summary: "Video at Boston Algorithmic Finance Meetup"
date: 2013-01-10T00:00:00
tags: ["video", "transcript"]
slug: boston-algorithmic-finance-meetup
word_count: 8060
source_file: transcripts/2013-01-10-boston-algorithmic-finance-meetup.md
content_type: transcript
event: "Boston Algorithmic Finance Meetup"
video_url: "https://www.youtube.com/watch?v=6h0IVlp_1l8"
---

{{< video https://www.youtube.com/watch?v=6h0IVlp_1l8 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

At the first algorithmic trading meetup, I demonstrate pandas—then nearly five years in development—applied to high-frequency financial data analysis, using my experience as a former research quant at AQR Capital Management.

## Genesis

I found R useful but limited for general-purpose programming: "I wanted to have a really rich financial data manipulation tool that could also be used as the foundation for building more complex systems especially for asset management and trading." My goal was to make Python-based systems "more maintainable and scalable" than R alternatives.

pandas sits atop NumPy, providing high-level data structures for real-world financial data. On automatic alignment: "If you add together two time series that don't align, it will automatically align them and insert missing data in the result. So, in practice, that makes life a lot more pleasant."

## Live Analysis: Apple Trading Data

Using five years of Apple minute-bar data from Quantopian, I analyzed volume patterns throughout the trading day, showing the surge in the final ten minutes—"People are rushing to get trades in"—due to mutual fund activity and compliance requirements.

I then asked: does end-of-day price action predict next-morning movements? The analysis found a negative correlation: "If there's bad news overnight, stock price goes down and people buy it back and it goes up a little bit in the first half hour."

## Trading Strategies

I built trading strategies from these findings using pandas' OLS regression capabilities, creating rolling three-month models showing how the overnight-morning relationship changed over time: "The relationship between those two returns changed quite a bit over time."

I implemented three strategies: a simple contrarian approach, an extended version holding until 10 AM, and a model-driven strategy with minimum thresholds. Disclaimer: "Don't try this at home."

## Technical Capabilities

Beyond trading examples: hierarchical indexing for multi-dimensional financial data, resampling across time frequencies, and sparse data representation for memory efficiency.

The library has found adoption beyond finance in ad tech, web analytics, and general data processing. Quantopian incorporates pandas into their platform.

## Status

I noted the todo list "goes down to the floor and out the elevator and down to the bottom floor of the building."

## Key Quotes

> "I wanted to have a really rich financial data manipulation tool that could also be used as the foundation for building more complex systems especially for asset management and trading."

> "I found that people do build algorithmic trading systems in R, but R is not very good at general purpose programming. So, I felt that doing things in Python would make all the code that we're building more maintainable and scalable."

> "If you add together two time series that don't align, it will automatically align them and insert missing data in the result. So, in practice, that makes life a lot more pleasant."

> "The purpose of the book was not to sell a lot of books... I was looking to create a resource that would enable people who aren't necessarily expert programmers to pick up the tools in the Scientific Python stack."

> "People are rushing to get trades in. I think a lot of mutual funds don't make trades until the end of the day."

> "If there's bad news overnight, stock price goes down and people buy it back and it goes up a little bit in the first half hour."

> "The relationship between those two returns changed quite a bit over time."

> "Don't try this at home."

> "It's always the risk of coding live. Your ability to think about math completely goes away."

> "There's a list of things to do which goes down to the floor and out the elevator and down to the bottom floor of the building."

---

## Transcript

So, the purpose of this talk was, well,

I guess just to kick off the first algorithmic trading meetup,

and I guess I wanted to talk a little bit

about work that I've done over the last few years,

particularly the pandas project for Python and

how some of the tools that are in it could be useful

for working with higher frequency financial data

and look at some code and data and do some interesting things.

So, my background,

so about six years ago,

I started out as a research quant at AQR,

which is not an algorithmic trading company,

but a quantitative asset manager down in Greenwich, Connecticut.

I worked there for about three years,

and I was managing credit derivative strategies,

helping manage credit derivative strategies.

There's where I got interested in building better data tools,

in particular for Python,

like I used R and there was a lot that I liked about R,

some things that I didn't like.

I wanted to have a really rich financial data manipulation tool

that could also be used as the foundation for building

more complex systems especially for asset management and trading.

So, I found that people do build algorithmic trading systems in R,

but R is not very good at general purchase programming.

So, I felt that doing things in Python

would make all the code that we're building

more maintainable and scalable.

I've been on my own for a couple of years

and working on a new company.

So, if you are interested in what I'm doing,

just stay tuned on Twitter and the blogosphere.

Hope to talk more about that at some point in the future.

Well, I didn't succeed at making this.

The image is bigger.

But I just wrote this book.

So, Python for Data Analysis.

You know, I don't know how much money I make on each book,

but not very much.

But the purpose of the book was not to sell a lot of books.

Well, I guess it was in a way,

but I was looking to create a resource

that would enable people who aren't necessarily expert programmers

to pick up the tools in the Scinavic Python stack.

NumPy, which is the core array processing library.

IPython, which is the computing and development environment.

It's where you actually do your code development

and sort of hacking around with data.

Matplotlib is sort of the main plotting library.

It doesn't make beautiful plots out of the box,

but you can do a lot of really nice things with it with some effort.

You can think of it as kind of like a low-level plotting toolkit

that with some elbow grease can make some pretty good visualizations.

And then pandas, which has been my project for the last almost five years.

And it's the high-level data analysis

and for financial users, time series processing toolkit.

So, I wanted to put everything in one book.

And given that a lot of the stuff in the book didn't exist three years ago,

or even two years ago,

so I felt the time was right to have a book

that would sort of lower the bar for learning these tools

and putting them to some productive use in your work.

So, pandas, if you know much about Python,

it's a set of data tools that's built on top of NumPy.

So, NumPy is the array library for Python.

And, but it's pretty low-level library.

It just gives you essentially what you get,

the kinds of things that you have in MATLAB.

So, you have vectors and matrices and functions for,

you know, that you can apply to vectors and matrices.

So, you know, things like exponent and square root.

And you can do, you know, sum across axis and things like that.

It provides all of the indexing

and sort of low-level data manipulation that you do with arrays.

But it doesn't provide, you know, high-level constructs

for working with some of the data types

that you have in the real world, things like time series

and being able to express, you know,

the kinds of, you know, actual business logic

that you write on time series with different frequencies

and, you know, date offsets and time zones

and all of that, all that stuff.

It also tackles what I would call the data manipulation,

the data alignment problem

in that the financial data is very heterogeneous.

It comes from lots of different sources.

You might have two sets of time series

where one is, you know, has holiday date,

data for the holidays, and the other one doesn't.

And you want to still be able to combine that data together

without having to, you know, stop and realign the matrices.

So, that's just a problem that pandas takes care of under the scenes.

If you add together two time series that don't align,

it will automatically align them

and insert missing data in the result.

So, in practice, that makes life a lot more pleasant.

You still have to deal with the fact that you're missing data,

but it's not constantly barking at you

that the matrices or the vectors aren't the right size.

So, it's become very popular in the financial world,

especially in asset management

where you can run back tests

and build trading signals,

typically just by loading static blocks of data

and then creating signals from math operations on those data

rather than algorithmic trading,

which is typically event-based

where you observe data one time step at a time

and you make sequential decisions based on that.

So, the decision you make at time T

will depend on what decisions that you made prior to that.

So, in a lot of asset management use cases,

that's not, I guess, how the signals are constructed

and having a tool that, I guess, enables matrix processing

without some of the data line in the headache

makes people very happy.

It's being used in a lot of other places,

ad tech and any kind of web analytics

and people processing data on the server side,

backing web applications.

And Quantopian uses pandas in their platform.

But it's not complete.

It's, you know, like all open source packages,

there's a list of things to do

which goes down to the floor and out the elevator

and down to the bottom floor of the building.

And it gets longer, it's seemingly every day.

So, it's a very active project

and one that if you find the kinds of things

you can do with pandas interesting

and you find something that you can't do

and you would like to be able to do,

I would encourage you to engage with the community

and see what's going on.

Anyway, this slide got completely screwed.

All right, so why do we care about using pandas

for algorithmic trading research?

So, I would say that pandas is most useful

for doing analysis of static data sets.

So, if you're building a trading simulation,

you'll generate lots and lots of data

while you're doing your trading simulation.

And you can take all of that data

and then do very easily sort of slice and dice

and do resampling and sort of bin and aggregate,

do all that post simulation analysis

using pandas very efficiently.

And a lot of work in the library

has been invested in vectorized operations on time series.

So, if you have a high frequency time series

and you wanna select the bar,

most recent observed value as of 9.37 in the morning

at each point in time, it will do that,

look up on the time series in one statement.

So, it does a lot of the sort of data selection

and data manipulation conveniences

that you need to do with time series.

It has very nice support for resampling.

So, if you have higher frequency data

and you want to bin it as four hour or one hour

or one day or one month,

you can sort of go from high frequency to low frequency

or low frequency to high frequency

with very simple commands.

So, if you have data at different frequencies,

you can find a common frequency,

resample the time series to that frequency

and then combine them.

Another feature area that I won't have necessarily

that much time to talk about

is that if you have very complex data

that might be four.

or five, or six dimensional.

pandas enables you to represent that data in a hierarchical way

so that things are organized in sort of a tree fashion,

but the data is still contained in a table or a single time

series.

And it gives you a very nice way of sort

of rearranging what could be very high dimensional, very

complex data, where otherwise in other languages

I've seen people work with this kind of data

and you end up with kind of a tangle of spaghetti code

teasing the particular subset of data

that you want out of a four or five dimensional data set.

One thing about high dimensional data sets

is that sometimes people will store that data

in a hypercube, so you have like a five dimensional matrix.

But there are lots of cases where

one or more of the dimensions will

be very sparse in some of the other dimensions.

So there might be one combination

of three dimensions where 99.9% of the values

are missing along the other two dimensions.

So pandas enables you to represent that data

in a dense fashion without running out of memory,

but you can still do express operations

on it in a pretty simple way.

Of course, I go through all of this

in a bit of absurd detail in the book.

Oh.

OK.

Thank you.

So all right.

So the rest of the talk, I'm just,

so Quantopian kindly gave me a little bit of minibar data

to play with, which unfortunately I don't think

that I will be able to give you.

But if you do have minibar data for some of these stocks,

then you can reproduce this analysis.

I'll post the notebook online after the talk.

How do I go full screen in Safari, or can I?

This is OS 10.6.

Maybe I can't.

You go to Windows, Windows Zoom.

The little yellow icon in the top left.

No, that will minimize it.

It's OK.

This is actually not that much screen real estate is lost here.

Let me hide the toolbar.

OK.

There we go.

All right.

So I'm running the, I don't have too much time

to talk about the IPython notebook,

but this is a web application that's

part of the IPython project.

And the idea is that this gives you a,

let me just create some random data and plot it.

My kernel died.

All right.

Let's try this again.

OK.

So this runs in the browser, and the idea

is that it's a, I guess what they call

a computational notebook.

So I have code cells, so very similar to Mathematica,

if you guys have used Mathematica.

So I have cells of code, and when I execute them,

it sends the code to a running Python process and executes it,

and then it comes back with any output from the code.

So if I put print hello world here,

then it shows hello world right there along with the plot.

So that's the basic mechanic of what's going on here.

So I've got minute bar data that's

contained in some CSV files, so let me show you

what this data looks like.

So bang, head, skip the first 10 rows of downloads,

minute bars, apple.

Who doesn't love looking at apple data?

So the minute bar data is just contained in a CSV file,

so we've got volume, high, low, close, price, date, time stamp,

open price.

So if I want to load this data into a pandas that may not,

if you've never used pandas before,

the main data structure is called data frame,

very similar to R. And so if I do pandas.readcsv,

it loads that into a data frame, and now I

get back a data frame that contains

all the data in that CSV file.

And these are just the first five rows.

And now to work with this data a little more efficiently,

notice that the time stamps are contained in the DT column,

and that's not really that useful

because we want to associate those time

stamps with all of the other columns

because they're the time stamps for the actual data.

So what we can do is select the DT column from the data frame,

and we'll go do pandas to date time, which converts.

Those are strings, and so it's converting those

to actual time stamp values.

So if I do select the first value,

now I've got, when I select an element,

I've got a time stamp object instead of a string.

And then I can assign the data frame's index

to be pandas to date time in that string column.

So I'm actually going to change this to pop DT.

So pop is going to return the column

and delete it from the data frame,

convert it to time stamps, and then set it

to be the index of the data frame.

So if all that goes well, then I now

have a data frame that has a date time index, which

is what we're looking for.

And if I look at the first five rows of the data frame,

data frame.head, I now have five columns and then a time stamp

index.

And the reason that that's useful

is now when I select, say, close price,

I get back a single one-dimensional time series

object.

So you can see that it goes from the beginning of 2008

through exactly five years of data up through three days ago.

And so there's some other things that

are interesting with this data.

So it's in eastern coast time, but the data's all

shifted head by five hours.

Maybe you guys can, Quantopian can tell me

why it shifted head by five hours.

But so what we can do is we can take this index,

and I'm going to use the shift method

and shift by one period frequency minus 5h.

So what that's going to do is shift all the time stamps,

subtract five hours from each one.

So I guess I also could have done shift minus 1.

I don't want to chance my luck that it won't work

because it worked earlier.

So now if we look at the data frame,

you can see that on January 7, 2013,

we've got data that goes up until 4 o'clock

in the afternoon.

It's UTC.

It's UTC, yeah.

Well, it looked actually, it looked

like there was no daylight savings times

transitions in the data.

So one thing that's nice about these time series objects,

if you've ever used XTS in R, then you

might be familiar with this kind of syntax.

So suppose that we wanted to select all of the data

just for one single date.

So we can do that in a shortcut way

by passing a string, just the base date.

So suppose I want the data on January 7 of this year.

So if I pass the string 2013-01-07,

it grabs just the data on that date.

And you can see that it goes from 9-31.

So the first bar in the data is the data from 9-30 to 9-31.

And then that goes up through the end of the day,

the data from the last minute of the day, from 3.59 to 4 o'clock.

So I've seen bar conventions in both ways.

I think, I don't know if this is the more common one,

but somebody can correct me if I'm wrong.

So, yeah, I was doing a little bit of analysis here on like the distribution of hours in

the data set to see if there were, you know, if it was, if it had daylight savings time

in it or not.

And I concluded that it didn't.

Is this the environment you usually work in for doing data analysis?

I often, I sometimes use it.

It's like, it's nice when you're sharing an analysis with somebody else and you want to

tell a story about what you did.

Because you have the code at each step and then maybe some output and plots associated

with it.

But when I'm doing, you know, I guess more hardcore development, I'm just using the terminal

version of this and then writing code in Emacs, because I prefer to write the code in Emacs.

And I actually created an Emacs interface to the notebook.

So, if you're like really an Emacs lover, you can, you know, you can use the notebook

without leaving Emacs.

I haven't gotten it working myself, but, yeah, it's pretty wild.

All right, so, so I loaded the data into a slightly different, slightly different format.

I'll explain why later.

But, so I was looking at, so if we look at, so if we look at an individual, just the timestamps

that are associated with the time series.

So here, let me go back to my, my df above, so if I look at the index here, these are

the timestamps for each of those time series.

So I can do things like request the, an array of hours, so you can extract the hour from

each timestamp.

So if I wanted to do some analysis on by, by hour of day, you could say, you know, data

frame group by data frame index hour, and then if I call the size function on group

by, that just gives me a histogram of the, the number, the count, the number of, you

know, of each hour in the data set, but that you could also compute other more complicated

things.

So if I wanted to get some statistics on the closing, you know, some statistics on

the volume at by, you know, by hour of day, you could say dot volume dot describe, and

let's try unstack, all right, and then, so that gives us, let me see, where are we, okay,

and so that gives me a table of a bunch of summary statistics for each hour of the day,

so you can see the number of observations for hour nine, and then the mean volume, standard

deviation, min, and then inter-coronal region, and maximum value, so it gives you kind of

a nice facility to do some, some quick summaries of, here, this is a data set with a, with

a half million rows, and, you know, doing all these computations is very, very snappy.

So another nice thing, especially for working with bar data, is a very common computation,

especially if you want to look at sort of event-based studies or, you know, things that

go on around particular times of day, like you might want to look at price actions around,

let's say, news announcements, you know, which often, you know, data will be released at

10 o'clock in the morning or at 8.30 in the morning, and you might want to look at price

changes from 10 o'clock to 10.05, and every, you know, each day, and then you could sort

of link that up with a data source that had the actual data about the announcements and

what the announcements were, and you could look at reactions to, well, the data's fairly,

you know, the data's fairly coarse at the minute bar level, but you can still get some

kind of a picture of what was the market reaction to, you know, to various events during the

day, and you could look, you know, compare, you know, if there were lead or lag relationships,

you know, IBM goes up, and what is that, what impact does that have, either a lead

or a lag relationship on other stock price movements.

So, if we're doing those kinds of computations on this data, so I guess a lot of what I'm

about to show you is going to be based on that, I'll come back to this a little later.

So, from where I loaded the data up here, I've got, I guess, another piece of code,

so I've got 10 stocks here, and I was going to do an analysis on all of them, so if I

have time, I'm going to show you, do what I'm about to show you on all of them, and

see if there's any interesting results, but the idea was to do what I showed you, load

each bar data file, convert the, convert the timestamps, put those in a Python dictionary,

and then, at the end, put them in a Panda's panel object, so a panel is just a three-dimensional

data frame, so we can have stocks by timestamps by data item, so that makes it very easy to

slice out if you just want the closing price, you know, the closing bar prices for all of

the stocks in your universe, you can grab, you can grab that slice out of the data set

in a simple way, so that's the reason why the data is a bit different here, so, so I've

got my panel object, which just has Apple data in it, and so, so as I said, I've got

stocks by timestamps by data item, and now I want to select out, so the closing bar prices,

open bar prices, and volume data into individual variables, so I'm going to grab a cross-section

along the minor axis, so the minor axis here are the data items, so I want the close price,

and volume, there's some other, you know, ways that you can get the data out with different

syntax, but I'll run this, and so if we look at closing price head, you can see that it's

just a data frame with a single column, just my Apple stock, and then the first five timestamps

there, and now one thing that's, that's nice about, the thing I was mentioning about looking

at data at particular points in time during the day, so here I have this time series which

goes over the course of about five years, suppose that I want to grab the closing bar

price at, at ten o'clock, at ten o'clock in the morning every day, so what I can do is,

the time series has a method at time, and if I do that and pass in a Python time object,

so I'll pass in the time ten o'clock, that returns a new time series which selects out

the data points at, at ten o'clock every day, so while I was on the train today, I was thinking

that it would be nice to have a method that would do an, do an as of computation, so that

if there's no data at, right, right at ten o'clock, that it would grab the most recent

bar, I don't have a function to do that, but if somebody gets really energetic and writes

it for me, I'll be happy to add it to the library. So something I was, I was thinking

a little bit about, and you know, people give me a really hard time because I, you know,

I do, you know, being an ex-quant, like I do a bunch of trading on the side, but like

I don't really do anything quantitative, and people get like, people really tease me about

it, that I, I don't have a system, that it's more like, you know, I like Apple, kind of

thing, but that was working out really great for me, so pretty recently, so. So another

thing that we can do similar to add time is that we can select, so let's just take a look

at the, the volume data, so I've got a big, so I've got a data frame that has all of just

the volume data for only Apple, I guess maybe I, you know, I'll go back and change it to

more stocks later. So as I was interested in looking at, you know, sort of, the distribution

of volume throughout the day, you'll probably guess, you know, what, you know, maybe, probably

know what that distribution looks like. But if I use the between time method, I can pass

two time objects to say, I want to get data from 931 in the morning through until 10,

10, 10 o'clock, so I just pass two time objects now, and then that gives me back a new, a

new data frame that just has data between those two times.

for each day.

So then what you can do is, suppose

you wanted to compare, split up the day into, say,

three buckets.

I called them morning, afternoon,

and the last 10 minutes of the day.

So I said, I'd make sure I didn't make a mistake here.

So from 9.31 to 12.30, I called that the morning.

We could debate about where we decided the morning is.

Maybe at noon, we could change that.

And then from 12.31 to 3.50, and then from 3.51 to 4 o'clock.

So I select those out, stored them in three variables.

And then, for each of them, what is this here?

OK, that's not what I wanted to show you.

So for each of them now, what I'm going to do

is, so those are minute bar data.

So I want to aggregate those for each day,

put them all into a single table, and then make a plot.

So I can see how that will take the morning data.

And I call the resample method.

I pass the target frequency, which I'm going to call it

daily, change it to something else, monthly.

And I want to compute, for each day, the mean volume.

Because the number of minutes in each bucket is different.

So I want the mean amount for each day.

So when I do that, I get back a new data frame

that contains time series that's now daily frequency.

So it went from having the morning data,

it went from having 200,000 observations to 1,800.

So I'm going to do that for each of those buckets.

So I made a little function to aggregate them,

put those in a data frame with columns morning, afternoon,

and last 10 minutes of the day.

And then I wanted to make a very simple plot.

So I'm going to take a further mean of those daily means

and plot that stuff.

And so I get a plot that looks about like this.

And so we can see that the last 10 minutes of the day

is very exciting.

People are rushing to get trades in.

I think a lot of mutual funds don't make trades

until the end of the day.

If you work for a financial institution,

you may have compliance checks where

you request trades in the morning

and then you can't trade until 345.

I used to not be able to trade until 345 every day.

Yeah, so I know lots of explanations

why people are really heavily trading in the last 10

minutes of the day.

So I just looked at this data and said, OK, well,

maybe does the price action at the end of the day

tell us anything about what's going

to happen to the stock price the next day?

So we can go a bit crazy here with the analysis.

So I thought, OK, let's look at the change in stock price

in the last 10 minutes of the day

and then the stock price overnight and then

the stock price in the first 30 minutes of the next trade

session.

So this is getting at this, I guess,

fairly sophisticated analysis.

And you have to be very, very careful

because you have the open price at each bar

and the closed price at each bar.

So you have to make sure that none of your data overlaps.

So what I did here is, let me make this bigger,

is while I computed times, I guess,

my open bar, my 10 AM bar, the start

of the last 10 minutes of the day and the closing time.

And I selected the open prices at the beginning of each day.

The closing price in the 10 AM bar,

so that's going to be the last print at 9.59, 29.99.

And then I guess the open price at the beginning

of the last 10 minutes of the day

and the last print at the end of the day.

Hopefully I got all that right.

And then I wrote this little helper function normalize.

So there's a function in Canvas that

lets you strip the time information from the timestamps

in the time series because we want all this data to line up.

So we want to throw away the, because this

is going to be 9.31, 10 o'clock, 3.51, and 4 o'clock.

So we want to throw away the time information

so everything lines up.

So I do that.

And so now if I look at the open prices,

now I have just a time series where everything is,

whenever it's midnight, it throws away the time

because nobody wants to see an array of all timestamps

at midnight.

So these are the first print of the day, open price,

first bar of the day for Apple.

And then what I can do is I can compute the very nice syntax,

compute the overnight returns and the returns.

I guess I should also compute the last 10 minutes

or the day returns.

So the overnight returns, we want

to take the price at the beginning of the day,

that's the price open, and take the price

at the end of the day from yesterday.

So I take price close, shift 1.

So that says, OK, price open today,

the last price yesterday, shift 1.

So that's yesterday's price.

Divide those and subtract 1 to get percent returns.

And I'll do the same thing to get the morning returns,

take the 10 AM price divided by the open price minus 1.

So I get the 9.30 to 10 o'clock returns.

We could also throw in here, so here's the returns from the,

you guys are all quants, so you will probably

spot a horrible error in my analysis here.

So also compute the returns in the last 10 minutes of the day.

And so you might be interested to say, OK, well,

what's the correlation of the overnight returns

with the morning returns?

So I spoiled it for you.

So I take the overnight returns.

And I actually don't want shift 1, why is this here?

OK, wait, wait, yeah, OK, so you see

that there's a little bit of negative correlation

between the overnight returns and the morning returns.

So if there's, I guess, bad news overnight,

stock price goes down and people buy it back

and it goes up a little bit in the first half hour.

Or it went up overnight and then people

don't feel as good once they start trading.

The sort of overnight gains, all that,

I mean, you can come up with a lot of stories

about what went on.

But we could measure this a little more quantitatively

and do something more sophisticated

than correlation with our favorite tool,

linear regression.

And you can compute a simple linear regression

using pandas' OLS function, which

is just like a simple linear regression,

but it also does data alignment and missing data handling.

So it gets rid of any missing data

and make sure that everything lines up.

So I want to try to predict Apple's price

movement in the morning using the overnight return.

So I say my y variable is morning returns

and the explanatory variable is the overnight returns.

And so we get a negative coefficient, not a very high

square, but a very significant negative relationship.

So the question I had, well, OK, I

wonder if there's even more negative reaction to, let's

say, the stock rallying at the end of the day

or selling off at the end of the day.

And then maybe it rebounds the next morning.

So we might as well throw in the price movement

at the end of the day.

We could change this.

So notice this is a full sample regression.

So I haven't visualized it for you at all.

It was a coefficient of minus 0.13.

So we might want to do a dynamic regression

and see how this relationship changed over time.

So if we modify this to have a window of 60 periods,

so about three months of data at a time.

And I also put in this min periods parameter.

So the idea is that if the amount of data in the window

falls below 60 and you don't have min periods,

then it won't run the regression at that point in time.

So that kind of gives you a little bit of flexibility

in your data quality.

Sometimes you want all of the data to be there

and to not run a regression if it's not there.

So if I do that, and then I plot the regression coefficient,

you can see that the relationship between those two

returns changed quite a bit over time.

So it happens to be that lately, there's

continuation, at least statistically.

I don't know.

I should probably add significance levels here.

But there appears to be continuation recently,

whereas at the end of 2011, there

was a lot of reversal, at least in this model.

So we can also.

Initially, OLS, just by default, was doing the normal,

just a regular one.

And that one parameter is doing a running one over time.

Oh, that's right.

Yeah.

So you say, OK, let's throw in, as another explanatory

variable, the returns from the last 10 minutes

of yesterday's trading session.

Now, I'm not being completely careful

because I don't have holiday data hooked in here.

So to really do this properly, you

would need a full trade calendar to, I guess,

build a fully faithful backtest out of this.

So I'm adding last 10 minute returns.

Shift by one because I want the returns yesterday.

And running a three-month rolling regression.

Do plot the regression coefficients.

So it turns out that the effect of the last 10 minutes

of the day is more significant, at least

in terms of the regression coefficient,

than the overnight return.

So that's interesting.

So I said, OK, well, I'll put our money where our mouth is.

Let's come up with a few trading strategies.

And I'm just going to go say, don't try this at home.

So I'll hear from you and be like,

Wes told us about this awesome trading strategy that

made lots of money.

And I went and did it.

And then I lost money.

And I'm going to sue him for all of his work.

So I thought there were a few fun strategies we could do.

So you could, well, you talk about position sizing

and all kinds of fun stuff.

Maybe we want to get a trade in at the end of the day,

either buy or short, depending on if it's sold off

in the last 10 minutes of the day.

You might buy at $3.59, $3.59.

Or if it had rallied, you might short right

at the end of the day and hold it to the morning

and then either sell or cover at the open of the next day.

Or you might, I was thinking, I'll call this $3.50.

Initially, I was doing $3.45, and then $3.50

was more interesting, which is what you're not supposed to do.

So this is just about illustrating tools.

So you might look at the return in the last 10 minutes

of the day, which is what I was just saying,

and make a decision based on that.

Or you might, to be even more sophisticated,

you might take our rolling regression,

take the last 10 minute return, the overnight return,

and use the predicted return based on the regression.

So this would be like a statistical arbitrage.

And use that predicted value as the signal.

So if it meets some threshold, you'll make a trade.

And then hold it for half an hour and make or lose money,

you get rid of it.

So you don't hold the trade more than 30 minutes.

So I've got a little function that computes sharp ratios.

I don't want to use that for later.

So for my simple strategy where I look at,

so I'm taking the returns in the last 10 minutes of the day,

shift 1, because my position today

depends on the values yesterday.

So I'm just going to take the sign of that and flip it.

So I'm going to take the opposite view of what

happened in the last 10 minutes of the day

and make the simplifying assumption

that I can actually get a trade in before 4 o'clock.

And so the position, the price that I buy it at

is price closed, shift 1.

So that's yesterday's last price.

I'm going to buy 100 shares and then either buy or sell,

depending on this indicator.

And then to compute a very, very simple backtest,

I take my position, which is just a cash number now,

and overnight return, which is a percent return.

But it's time stamped with today's date.

So all I need to do is take position times overnight

returns.

I put sum 1 here in case we change this to multiple step

time to change it to multiple stocks, which we may not.

And then I plot that.

Let's see if we made money.

All right, so we made a little bit of money.

Let's see here.

Looks like it.

Of course, you're all going to try foul,

because it made a lot of money in 2008

when Apple's stock price was really low.

So we could fix that.

Let's see what the Sharpe ratio of the graph for this guy.

So the information ratio of the strategy is 0.4.

We could further break it down if we wanted.

Suppose that we want to group by the year of the P&L

and then aggregate with the Sharpe function.

So we can get a breakdown by year,

make this a little bigger here.

So it did really awesome in 2008.

And then it had a few middle, well, pretty good 2009,

some middling years.

And then we better sort of get fired up

and start trading this.

I don't think we can draw a conclusion off

of like five data points.

Let's see.

Sharpe was sweet.

So yeah.

And so I looked at another variant of this same strategy

where instead of selling right at the beginning of the day,

we hold it until 10 o'clock.

So maybe like some of the price, sort of the reversals

realized over the first half an hour of the trading session.

So to do that, the position is the same.

And I said, OK, overnight returns plus morning returns.

And I'm pretty sure that these aren't overlapping.

So I can just add these together.

Well, no, I really should compound these.

But please forget my technically incorrect math.

But it's good enough to see that the strategy doesn't really

work.

Well, it worked OK for a while.

And then it's losing money lately.

All right, so more interesting model

is building a model based on the rolling regression that we ran.

So I was looking at the last 15 minutes, the last 10 minutes

now.

So we can take, I already computed this.

So it's our same regression from before.

We get overnight returns, yesterday's, end of day

returns.

We run the regression.

Let's start with six.

You can always data mine the window when we're done.

And so we run a three-month regression.

And now we ask the model for the predicted y value.

So we'll do model.ypredict.

That's just the one period.

It had forecasts of taking the regression coefficients

from yesterday and the current x values

and computing the predicted y value.

So the value that we get from that is a time series.

And then is that being pre-computed?

Or because it's not a function call, right?

It's an attribute, but it gets computed and cached.

Yeah, it's like a cache.

It's a property.

It's a Python property.

It's only calculated once, actually.

Yeah, it's computed on demand.

So we have our predicted y values.

That's sort of the basis of our signals,

what the regression is predicting

for the next period.

We can set some arbitrary threshold.

So if, let's say, if the model thinks

Apple is going to move more than 25 basis points

over the morning session, then we

put the set of that as the threshold.

So if the absolute value of the predicted value

exceeds the threshold, then we take either a plus 1

or minus 1 view based on the sign of the prediction.

And then we'll trade 100 shares.

And we're going to assume that we

can get in at the beginning of the day

and get the open price from the first bar, which

is not realistic, but we'll hope so.

And compute the returns again.

And we get a pretty good strategy that

doesn't trade all the time.

So you can see that there's long stretches

where it never decides to trade.

But then we can, so then you've got like,

that one's got like a 9-sharp ratio of 2013.

That might just mean that it traded on one day

and made money.

So the standard deviation is really, really small.

I guess we could look and see what it is.

But then you can tweak and play with things here.

We want to increase the window to six months.

And then change the threshold to be a little less.

So we get different back tests that we can look at.

You might want to set a maximum amount of cash to risk.

Suppose we only want to trade like $50,000 in Apple.

So then here, our position size is really cash

divided by price open Apple shares.

So let's use NumPy's round function.

I could just do floor divide, right?

So I can't buy any more than $50,000 in Apple.

So that's my number of shares.

So I put shares here.

Does that look right to everyone?

Yeah.

All right.

It's always the risk of coding live.

Your ability to think about math completely goes away.

Number of shares times price.

All right.

So we get, well, OK, we made like $30,000 in 2008,

and then a little more in 2009.

And since then, it hasn't been doing all that much,

probably because the trades become smaller and smaller

as Apple's stock price goes up.

But still, I guess, the Sharpe ratio in 2013 is 12.

Should probably check that and see what's going on.

On the where function, is that Np is one of the variables?

Yeah, so I guess I glossed over that at the beginning.

So Np is NumPy.

That's the base array library.

So in R, this would be if-else.

In MATLAB, it would just be where.

So in R, where you do an index and you

pass a logical time series, or a logical array,

is that what that would be?

Yeah, so here, if we wanted to say, let's find days,

well, days where we may either lost 2% or more.

I don't know what the magnitudes are like in this data.

So if we could do, if we say, take absolute value greater

than 0.02, and then, yeah, so that

returns a logical time series.

And then you can index.

OK, so it's the same way.

Indexing too with that, yeah.

OK.

Oops, so these are in dollars.

So let's say, let's try days that we

made more than $1,000.

OK, so 2008, there were a lot of very positive days.

And then, OK, so that's about all I had.

I was going to do more stocks.

And I'll