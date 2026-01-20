---
title: "Data analysis in Python with pandas"
summary: "Tutorial Video at PyCon 2012"
date: 2012-03-07T00:00:00
tags: ["tutorial video", "transcript"]
slug: pycon-2012-tutorial
word_count: 29917
source_file: transcripts/2012-03-07-pycon-2012-tutorial.md
content_type: transcript
event: "PyCon 2012"
video_url: "https://www.youtube.com/watch?v=w26x-z-BdWQ"
---

{{< video https://www.youtube.com/watch?v=w26x-z-BdWQ >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This PyCon tutorial provides an introduction to pandas. I explain that pandas emerged from frustration while working at a hedge fund in 2008, where R felt inadequate and NumPy was too low-level. "NumPy is too low-level a tool," I note. The library provides data manipulations typically done in SQL or R/SAS that were "historically very difficult to do in Python."

After eight months working full-time on the library, the codebase had tripled in size within a year.

## Core Data Structures

A **Series** is a one-dimensional NumPy array with labels called an index, enabling both positional and label-based indexing. The **DataFrame** represents tabular data like a SQL table, where each column can contain different data types.

Automatic data alignment is key: when performing operations between pandas objects with different indexes, the library performs join operations, inserting missing values where labels don't match. "You can switch to Python and forget about isMember," I tell MATLAB users.

## GroupBy Operations

The **split-apply-combine** paradigm in pandas' GroupBy functionality mirrors SQL's GROUP BY but extends to transformations and arbitrary function applications. Users can group by column names, arrays of labels, or Python functions applied to index labels.

## Real-World Data Analysis

The tutorial uses three datasets: baby names spanning 130 years, FEC campaign contributions, and USDA nutritional information. The baby names analysis shows John represented 8.15% of boys in 1880, while by 2008 Jacob held the top spot with only about 1%—demonstrating increasing diversity in naming.

I advocate an "anti-DIY" philosophy: rather than forcing users to write repetitive matplotlib or NumPy code, pandas should provide high-level operations.

## Technical Notes

I mention that `get_value` is "about one and a half microseconds faster" than `.ix`. I discuss the limitation that data must fit in memory, acknowledging interest in larger-than-memory datasets and distributed computation.

## Ecosystem

The tutorial shows pandas' integration with IPython, NumPy, SciPy, and matplotlib. Built-in `.plot()` generates visualizations with minimal code.

My O'Reilly book features a golden-tailed tree shrew rather than the hoped-for giant panda.

## Key Quotes

> "I started building the library in 2008. I was working in a hedge fund. And I was frustrated by the data tools that I had working in R. And I also liked using Python for data munching. And I said, well, there's sort of a missing piece here. And NumPy is too low-level a tool."

> "pandas is a rich data manipulation tool built on top of NumPy. It provides the kinds of data manipulations that you would do in SQL or a database engine, or that you might do in R, or SAS, or a statistical computing environment. And things that have been actually historically very difficult to do in Python."

> "You can switch to Python and forget about isMember."

> "I'm of the opinion that we should be doing more stuff like this. I've sort of lately, I tell people that I'm anti-DIY."

> "The entire goal of the constructors is if you have a list of tuples, you have a list of dicts, you have a numpy array, you have a dict of numpy arrays, you have a dict of series. Anything under the sun, if it's got labeling information or it's array-like, it's designed to be very easy to get that into a data frame structure, which is where all the magic starts to happen."

> "The data that we're working with, it has to fit into memory. It has to be able to fit into a NumPy array. Yes, that is currently the case. There is a lot of interest in making pandas work on memory maps or very large stores of data or basically enabling pandas for distributed computation and for dealing with big data. But currently it's an in-memory data tool."

> "In 1880, 8.15% of boys were named John... only one in 100 boys is named Jacob in 2008. But eight in 100 was named John in 1880. So the diversity of names is going up over time."

> "If you took the top 15 most occurring names in 1880, that was 50% of the babies born in the United States... So people have gotten much more creative over time."

---

## Transcript

Hello, everyone.

Wow, that's a big group of people.

So this is going to be fun.

We'll get to know each other very well.

So anyway, this is the pandas tutorial.

I've got some slides, and so I'm going to talk through

some slides and get your head around some of the basics

before we start diving in and looking at code.

Most of the tutorial is going to be writing code.

So we're going to be using the IPython HTML notebook.

So I think the first part, before we start recording, what

we should probably do is make sure that everyone can get

into the IPython notebook.

You don't need to know how to use it.

If you've never seen this thing before and never used

it, I'm going to give a really brief overview of how it

works, some of the keyboard shortcuts, and basically just

how to navigate the notebook.

How many of you were in the IPython

tutorial this morning?

OK, this is about half of you, so you'll be really bored for

the next 10 minutes.

Can you read?

I can't read this.

Can you read it?

Yeah, I will do that.

Yeah.

Yeah.

OK.

Yeah, wow, what a terrible place to have a.

Is there any way to, I mean, there's no dimming feature of

those blinds?

Yeah.

I must have done something to offend the PyCon gods to get

put in this room.

OK, so anyway, so you all should have downloaded an

archive of files.

Wow, this is going to be fun.

OK.

So what you do is just, if you're doing it in, well, I

guess I'll just do it on the Mac.

But so unzip that directory, and I'm going to run everything

from that directory.

So if something doesn't work, then it won't

work on here either.

OK, so it's the, what's it called?

It's called, it's not in here.

OK.

OK, so if you, I guess I should stop Dropbox.

Let me do that.

So you all should have downloaded a directory, an

archive that has a bunch of files that look like this.

So does anyone not have these files?

OK, so there's a thumb drive that is getting passed around.

Let me bring up a link for you to download it.

I think it's on my Twitter feed, actually.

I'll bring it up for you.

Remember, I'm not supposed to do anything that

relies on Wi-Fi here.

OK, so if you do not have the file, so you can try to, that

is an O on the end there.

And there's also, who has the thumb drive right now?

OK.

Could you guys dim the lights?

I think that's going to, I mean, these overhead lights,

is that possible?

Do we have control over that?

No.

OK, so the goal for the next five to 10 minutes is to unzip

this directory.

I'm going to bring the link back up.

Make this here, this here.

So the goal is going to be to run IPython space notebook

space dash dash PyLab equals inline.

And have that work.

And if all goes well, then your web browser should pop

up the IPython HTML notebook.

If not, you may have to navigate to the URL that's

printed by the end of the notebook server.

So if you cannot do any of these things, I'm going to be

walking around and helping people for the next five to

10, and anyone who knows, if anyone wants to help, help

people that can't get it to work.

Have you seen it yet?

So that enables the feature of the notebook that it will

render inline Matplotlib plots in the notebook.

That you don't have.

AUDIENCE MEMBER 2.

In the earlier tutorial, I can do IPython notebook.

Maybe that was my problem.

I just spelled notebook wrong.

Oh, maybe.

OK, excellent.

Yeah, so navigate to the directory where you expanded

those files.

And so you need to start the notebook in the same directory

where you expanded those files.

Maybe I have those four notebooks.

Yeah, so you should see.

Let me pull up what you should see.

Yeah, so you should see four notebook files, one of which

will not open.

So if you're having trouble, raise your hand, and I can

come help.

What's that?

Oh yeah, so we'll be making some plots.

So if it started up, that's a good sign.

0.7, is 0.0 or higher?

If you don't have, yeah, it was on the list.

then I get a print out the help and then I get this error.

Okay. Maybe I'm missing something.

You have a Python point 10. You need to upgrade iPython.

So if you have a, some,

some people might have an early version of iPython.

That also means that you may not have PI zero MQ.

You may not have tornado.

What's that?

Yeah.

Yes.

How would you recommend getting 0.7 if you've got an APD distribution installed?

Cause no 0.7 doesn't.

Oh, um, PIP or PIP or easy install should do it on. Uh,

if you, yeah, I'll get to, get to that point. Um,

um, the, the food database, the food DB.

So the second goal of this setup process is to open the notebook to import pandas

and press shift enter and have that work.

And hopefully if you type, um, dot double underscore version,

you have a version which is 0.7 or higher. Um,

what version of 0.7 or higher it is doesn't actually matter.

So

Oh gosh. Okay.

That's all right. Don't worry.

Yeah. You did get an email about setup instructions, right?

Uh, there was a bit of a screw up.

All right. Who's, who's, who's still having, having trouble.

If you're having trouble, raise, raise your hand

higher. Raise your hand higher. Okay. If, if you have traveling trouble,

raise your hand high and people who, who, uh,

are familiar with all these tools can, can help. And I will help also. Yeah.

Okay.

You have multiple versions of Python installed. It looks like

it shouldn't

type pandas there.

Okay. That's installed in your dist packages. Okay. And

so import sys and type sys dot path in there.

All right.

You got an email about making sure all this worked beforehand, right?

All right. Import sys and then, and then sys dot path.

So, okay. Is this not, this is not working. This is strange.

Okay. Import says

oops. Yeah. Small shift key and then sys dot path.

Okay.

Okay. So you've got EPD free, so you need to put,

yes, yes. So you need to, well, so first of all, you need to put,

um, this EPD free and then the bin path and your path and then restart your show

and then install pandas. Yeah.

Okay. Who else can I help?

So

it's always a fun part of doing yours works, huh? Okay, good.

Yeah.

Oh, I clicked, uh, clicked a new notebook.

Sorry. Yeah. And then just type, sorry to get to that screen up there.

I clicked a new notebook. Um, so if you type import,

import pandas and then shift enter and then do pandas dot and then double

underscore version at shift enter. Okay,

good.

All right. I know

I budgeted about 20 minutes for this, so yeah.

This light situation is just tragic. You know, this is like, yeah.

What's that? No.

Yeah.

Really? There's nothing to be done about the lights here.

Yeah.

Oh, I see. Gosh,

yeah.

Yeah. Well they, they definitely are not helping. Um, but it's mainly the,

yeah.

Yeah.

Yeah.

Okay. Well they said there, there might be like a passport,

password required to change, to dim the lights. Um,

so it's not my fault. I wouldn't, wouldn't,

would never have held a tutorial in this room.

Okay.

No, that's, that's

all right.

Okay.

Okay. So does anyone,

does anyone still not have the notebook running? You?

Cause he, cause you have to install zero MQ. Um, yeah.

Uh,

and uh,

all right. Are we ready to go? Modulo, you know,

not being able to read the screen. I'll make the,

make the font as big as I can while fitting everything on the screen.

Okay. So, all right, let's, let's get started.

I'm just going to give you a very brief explanation of how the,

how the notebook works, um, which will, which will help later. Um,

and then I'm going to, and then I'm going to switch to slides. So, okay.

So from the, so when you start the notebook server, um, you get a,

you get a URL that you type into your web browser.

I think it's set up to automatically if you, you know,

if you've got Google Chrome or, or Firefox,

it will automatically launch into the notebook. If, if you haven't,

then copy paste it into the URL bar to get to, to get to the notebook.

And there's a button up here, um, which says new notebook. Um, so,

so click on that. Um, now over here on the left,

there's, there's a toolbar. So in the,

in the latest version of iPython this has actually been replaced with a very

nice menu at the top of the screen. Um, but now it's currently,

it's this sidebar. Um,

and we're not actually going to be using the buttons over here very much. Um,

so there's a little bar here, um, which you can click to, to minimize that.

Um, and so, so what's going on here for,

for people who have never seen this before, um, is this,

this is a web application which is talking to, um,

an instance of the iPython interactive shell, uh,

which is running inside, running inside the server. Um,

so I can type arbitrary Python code in here.

I type print five and then press shift enter. And what that does,

I'll make it bigger, big as I can. Um, so I type print five shift enter.

So try that a few times. So shift enter up arrow, shift enter.

Okay.

So what this does is it sends the

So it sends the code to the IPython process.

It executes it.

And then it captures any output.

If there are any plots, so type plot a range 10 into that.

And so if everything is set up on your machine right, you

should see a plot in the browser.

So it's a very nice tool for doing interactive research,

interactive data analysis.

And it's also very good for doing talks and for playing

around with data.

So that's why we're going to use it here.

If you press Control-M is the sort of command shortcut.

If you press Control-M-H, you will get a little window of

keyboard shortcuts.

So if you ever want to know what are the keyboard

shortcuts for the notebook, press Control-M-H.

The main ones that are going to be useful

today are Control-M-B.

So let's go down here.

If I type Control-M-B, that inserts a cell below the cell

that I'm currently in.

So suppose I had something here.

I had said print 5.

And then I was in this cell.

And I want to jump to a new cell.

And suppose I wanted to take all the

code that's in this cell.

I could copy that, Control-M-B, and then paste it.

So it's just a mechanic that it's worth getting used to.

Control-M-A inserts a cell above the cell you're in.

So those are the three things that I do very often.

So Shift-Enter executes the code.

Control-M-B inserts a cell below.

Control-M-A inserts a cell above.

And the last one that you may need to know is Control-M-D,

which deletes cells.

So I think for the purposes of the tutorial, this is really

all you need to know about the notebook.

So everyone still following along so far?

OK, excellent.

So now we go to slides.

So my name is Wes McKinney.

Many of you already know me.

I've been involved in Python for about four years.

This is my second PyCon.

I came to PyCon in 2010 to talk really about Python and

quantitative finance, but also was to talk about pandas.

And that was sort of where I first introduced pandas to the

Python world.

So pandas, many of you have already used.

So who here has not used NumPy, never used NumPy?

OK, I expected to have a few of you.

So I'll give you enough about NumPy so that you can get a

bit of a feel for array processing.

So pandas is a rich data manipulation tool

built on top of NumPy.

It provides the kinds of data manipulations that you would

do in SQL or a database engine, or that you might do

in R, or SAS, or a statistical computing environment.

And things that have been actually historically very

difficult to do in Python.

So most of the library are data structures.

And I'll explain what I mean by data structures.

And really, the goal of the project is to make Python an

attractive tool for doing real-world data analysis and

for building data-centric applications where you're

doing a lot of crunching and grouping data, but also for

doing statistical modeling.

The library is actually, I sort of switched gears about

halfway through last year's.

And I've spent about eight months working

full-time in the library.

So if you used pandas about a year ago and you haven't seen

it, the code base is, it was already a large code base, but

it's about tripled in size in less than a year.

And I have a ton of stuff planned for the next year.

So it's a very active project.

I started building the library in 2008.

I was working in a hedge fund.

And I was frustrated by the data tools that I

had working in R.

And I also liked using Python for data munching.

And I said, well, there's sort of a missing piece here.

And NumPy is too low-level a tool.

So that's what led me to start building pandas.

I've started a new company.

It's called Lambda Foundry.

We're building Python tools for finance.

Not really going to talk about that very much here.

Some other projects I'm involved in, stats models and

a couple of other little projects, a little GPU

library for statistical computing and VBench, which I

think I'm going to do a lightning talk about.

So if you care about performance in your code and

you like monitoring the performance of your code,

that's VBench.

It benchmarks your code across versions.

It's a project I'm very excited about.

I'm writing a book with O'Reilly Media.

So some people haven't heard of O'Reilly, but they're the

animal books.

It's a golden-tailed tree shrew.

I thought maybe if O'Reilly had a sense of humor, they

would have put a giant panda on the cover.

But c'est la vie.

I do think it's a nice-looking animal.

So the tagline up here, you can't see it, but the tagline

is Agile tools for real-world data.

And that's definitely been a theme with the work that I've

been doing.

So the book is intended to give a very concise

introduction to the primary tools of what I would describe

the modern scientific computing ecosystem, IPython,

which many of you have heard about today, maybe you've used

in the past.

And then NumPy and SciPy are the core sort of numerics

projects, Matplotlib for data visualization.

We have a lot planned in the scientific Python community

for building better data visualizations, and

particularly building better linkages between the IPython

HTML notebook and JavaScript visualization library.

So building very rich interactive visualizations,

which are harder to do in Python.

So you use an interactive plot on the web, and then you go

back to Matplotlib, and you feel like, wow, this feels

like I've been transported 20 years into the past.

But you can make attractive publication quality plots in

Matplotlib also.

A lot of the book is going to be about pandas and nuts and

bolts of how do I work with data in Python.

And then the rest is going to be case studies, sort of

taking, here's a data set, and here are some questions that I

want to ask about it, and do some analysis, and show how to

synthesize all these tools together.

And so that's why we're here, is to talk about that last

point, to actually look at some real data.

So the basic pieces in pandas, the two objects that we're

going to be talking about are the series and the data frame.

And I'll explain what those are in the next slide.

Talk about how to create them, getting data from flat files,

from CSV files, or from JSON objects,

into data frames and series.

If we have time, I can show you how to, if you had a SQLite

database and you want to translate the SQLite data, how

to get that, convert that into data frames.

Going to talk about indexing.

So a big part of pandas is it facilitates working with

relational data.

So if you have data which is identified by multiple keys,

it gives you a very consistent means of connecting that

relational information to the data, and then selecting out

subsets of the data using that labeling information.

Let's talk about selecting and filtering data, data

alignment, getting descriptive statistics out of data.

Group by is sort of an umbrella term that I use to

describe doing group operations on data.

So if you have a giant data set and it splits naturally

into groups, you can crunch that down to a

more intelligible form.

We're going to spend a lot of time on that.

Sort of reshaping and pivot tables, which are closely, if

you ever, how many of you have ever created a pivot table in

Microsoft Excel?

That's pretty good.

Well, I'll show you an example of that, but sort of a

convenient way of creating a summary view of a data set

grouped along many different facets.

Show you how you can merge data sets together.

So if you have two connected data sets which are linked by

keys, if you've ever done a join statement in SQL, how

that works.

And if we have time and there's interest, we can talk

about time series.

Really, I'm interested in sort of giving you an overview of

how structured data and working with tabular data in

Python and how that looks using pandas.

And we're going to be using the HTML notebook.

So, I've got three data sets that we're going to play around with.

So the first, and well actually the first we're going to look at is the second one on

the list, which is a database of baby names, the top 1,000 names given to boys by percentage

of babies, of boys and girls over about 130 years.

And we can extract some pretty interesting trends in this data, somewhat humorous trends

in my opinion.

And then I've got a much larger data set, which is the Federal Election Commission disclosure

data, all the campaign contributions to the current U.S. presidential candidates with

this sort of state and zip code and occupation, so we can, we'll get some interesting results

out of that.

And the last is, I've got a big JSON database from the USDA, about 6,600 foods and all of

their nutritional information, so how we can import that data which is in this sort of

nested JSON format, how we can unravel that into a tabular structure, join it together

and then start doing some descriptive statistics on it and get actually extracting, you know

if you wanted to say, well what are the top five foods if you're interested in getting

a lot of zinc in your diet, you can get that information very easily.

So the two main objects in pandas are the series, which is a one-dimensional NumPy array,

so it's a homogeneous one-dimensional array of data, and it has a set of labels attached

to it, and I'll show you a diagram on the next slide.

The data frame is, you can think of as like a SQL table or a spreadsheet or a CSV file,

it's your standard tabular data structure, each of the columns in the data can be a different

type, and so it's a rectangle of data where the columns are different types and you can

refer to the data by its row labeling or its column labeling.

Correct, so a series represents a data frame, a data frame column, so I've got an illustration

of that.

Yep.

So the data frame is named as the data frame R?

Yes, so if you've used R, the data frame, I mean the name came directly from R, so anything

you've done with R data frames can translate into pandas, so I'll explain that.

So the series, I guess this is a mock-up of a series, so you have an array of values which

can be any data that is representable in NumPy arrays, and then you have associated

array of labels which are referred to always as the index.

So whenever I say index, I mean this array of labels.

So whenever I talk about pandas I have to always, it's like you have all this jargon

associated with the library, I have to remind myself to, when I say index I mean these labels.

So the labels don't need to be any order, so this happens to be A through E, but they

could be jumbled up into any other order, so there's no restriction on the order.

There are cases where you can have duplicates, but really it's intended to be a unique, like

a one-to-one mapping, so that you can actually, so if you say give me the element at C, then

you can look things up by label, as well as give me the, this was, it's everything zero

index because we're Python, so this is zero, one, and two, so you could refer to the 12

value either by the string C or by the position two.

Of course you can put any Python object in an index, but the only requirement is that

it be a valid dict key, so if you can use it as a key in a Python dictionary, you can

put it in an index.

So the data frame is the two-dimensional analog of a series, so now you have an index, and

you have some collection of columns, and so you can think of a data frame as being semantically

like a dict of series, where each of them has the same index, they're required to have

the same index, and each of the columns can be referred to by name.

And so the columns is the same object as the index, so it's an array of labels, so it has

exactly the same semantics as the row labels, but the columns in the data frame can all

be different types, so here's, I'll use my pointer, so here's an example where, so here

this column is integers, and this one is strings, this one is floating points, so here there's

a missing value here, I just wrote it here as NA, and then we have a column of Boolean

values, so in NumPy Dtype jargon, this would be a Dtype bool, this would be float32 or

float64, these strings are actually stored as Python objects, so this would be Dtype

object, and this would be int64, int32, whichever NumPy integer Dtype is used there.

So in all the objects, so here the index is meaningful, you have the letters A through

E, there are cases where you might create a series but not actually specify an index,

in which case it would be given the values 0 through N-1, so the equivalent of range

N. So the index may not always be meaningful, but it's important to know that there is always

an index, and the index is used to do lookups, so to look up values, but the key feature

and the reason that the indexes are there is that if you have two different objects

and you want to do an operation between them, the indexes are used to perform join operations,

so if you have two time series or you have two labeled arrays and you want to add them

together but the indexes are different, well, I'm going to come back to this slide, so here's

an example where I have two series, they're labeled slightly different, so one has B-C-D-E,

another one has A-B-C-D, so I can actually add these together even though they're the

same length, which they don't need to be, but the indexes are different, so when I do

that, it actually does a join on the labels and inserts N-A, the missing value, in the

places where there wasn't a match, so here this one had A, this one didn't, so you get

N-A in the result, for E you get an N-A, but on the values where it matched, it actually

lined up those values and added them together, and this is a feature that is not present

in a lot of data analysis libraries where you have to be always thinking, like, is my

data aligned, or sort of aligning things up, if you've ever used MATLAB, there's a function

called isMember, so I like to tell people, you know, you can switch to Python and forget

about isMember, so having this sort of automatic join data alignment functionality is very

important.

There are also, you know, to expand your mind a little bit, there's also the concept of

hierarchical indexes, which we'll see some of, so you can think of a hierarchical index

as having a tuple, so here we've got just a string, but imagine we had a Python tuple,

a tuple of strings, but the idea of a hierarchical index is that you can select out, so I've

sort of written this as, you know, you can think about this group of data right here

as the A group, and this is the B group, and so it gives you a means of selecting out groups

of data without having to write a for loop, so you can imagine if you had an array of

tuples and you wanted to select out the set of tuples that their first element is a certain

value, you can imagine what that Python code would look like, you'd write a list comprehension

or a for loop to get, to generate those tuples, so this gives you, this is a means of, you

know, we'll see in the code, but it gives you a way to kind of do away with that and

have a very natural way of identifying data as belonging to groups and then selecting

out groups of data.

In a lot of cases they have to be unique, yeah, so there are a lot of operations that

require uniqueness.

There are many cases where they don't have to be unique, so we'll see, it's not enforced,

yeah.

It's only, the uniqueness is only checked for whenever it's needed.

So kind of abstracting a little bit from, well sort of taking a step up from the series

where we can do a join, so we can say A plus B.

or x plus y, I guess.

And it does a join on the series indexes.

If I add two data frames together,

I could have data frames that contain different.

So this is like what the console representation of a data frame

looks like.

These happen to be all floating point values.

So we've got some row labels, A through E.

This one's A through G. And then I probably

should have called the column something different other

than letters.

So this one has a C column.

This one doesn't.

And so I can still add these together.

And you can see that it unions together

the indices in both data frames and on the columns as well.

And it lines up the values.

So it puts in missing data markers in the result.

And then once you've done that, you

can decide if you want to clean out the missing data any place

where there wasn't a match, then you

have the choice to do that.

But the default behavior is that it

doesn't discard any information.

So to motivate where this idea comes from

is it's very common to get data that looks like this,

where you have this set of labeling information

for your data.

And you have columns of data.

And this is what it might look like where you've got gaps.

And you might have some columns where

there's some things missing.

And you just want to have a coherent way of saying,

just munge this together into a table.

And then you can see that it's not

munged this together into a table.

And that's what the data frame does for you.

But the axes are more than just arrays of labels.

So they can also have names for the columns.

So here's an example of a data frame

where the columns are years.

But it actually has a year attribute.

So there are places where you can

refer to the columns by name.

And that can make your code very readable.

So here's an example of a hierarchical index.

This is what it would look like in the console, where

everything on the first level is Australia.

So here, you can imagine this is Australia all the way down.

But then you have this age from field.

So you can see there are different ages along the interior

level.

And so it gives you a very natural way

of encapsulating this relational information for this data.

So the next concept that I want to talk about at a high level

before I start firing away code at you

and showing you how to work through playing with data

is this idea of groupby.

So who here has ever done a groupby statement in SQL?

Well, that's good news.

So schematically, groupby looks like this.

So you've got data that's identified by some key.

So you have an identifier.

And you say, OK, I want to group on this.

So this might be a series.

And this is the index.

And so you could say group on these values.

That splits the data naturally into three groups in this case.

And then you can apply a function to those groups.

So in this case, summing up the three groups.

And the result that you get out of it now

is a smaller object, which has the unique set of labels

that were in this original array of labels.

And so now you have a smaller object.

And this is all unique.

And those are the aggregated values.

But if you think about the groupby concept,

there's a lot more that you could

do other than aggregation.

So you can imagine taking these groups.

And instead, you want to subtract the mean values.

So you want to center the values within group.

So groupby gives you a coherent and very

Pythonic way of doing that.

So that would be an example of a transformation

instead of an aggregation.

Or you might have some Python function.

You want to say, well, I don't know.

But I've got this chunk of data.

And I want to pass that to a function that I wrote.

And then whatever the result is, you

want to be able to then glue all those results

together into an object.

And so I'll show you some examples of that

and what that looks like.

So the groupby concept, this split,

so this split, apply, combine, gives you

a very powerful way of grouping data and producing

summary statistics on very large data sets.

So we'll see in the code, but as far as ways

that you can split objects.

So here, if we go back to our data frame mockup,

so a very common case is like in a SQL table

where you have a column that you want to group by.

And so you really want to say, just group on the bar column.

In this case, these values all happen to be unique.

But you can imagine if you had a column containing

a very large column and it had only

a small set of unique values, you

could say group on that column.

And that specifies a way to split up the data.

So you can also pass in other, so an array of labels

that you got from someplace else.

But there's also a very general case,

which is you can pass in Python functions, which

get applied to the applied, now this is sort of going

to melt your brain a little bit, but you

can pass a function which gets applied to the access label.

So imagine you had a data frame that was labeled by years

on the rows and you wanted to group those years

on the rows and you wanted to group those years into buckets.

One, let's say it was every year and you wanted

to create decade buckets.

So one approach is you could create an array

of the decade for each label.

Another approach is you create a Python function

which, given a year, yields the decade that it belongs to

and you pass that in.

So that kind of eliminates a munging step from the process.

You cannot, but that would be a nice improvement.

That would be, it would be very easy to add.

Yeah.

Yeah.

So when you do a group by, a group by,

we're going to be doing a lot of group by in this tutorial,

so that's why I wanted to explain what's going on here.

So you have an, so you have a data frame

and you have this method group by,

which is the entry point to the sort of group by machinery.

And what you do is you pass either a single key

or a list of keys.

And now again, these can be either column names

or they can be functions or they can be arrays.

So it can be any of these three.

You can mash them up however you like.

And the last thing is that you can group along the rows

or you can group along the columns.

So the default is to group along the rows,

but you have, you can imagine a case where, you know,

the columns actually are related to each other

and you want to say group them into groups

and add them together or something like that.

And so, so you have a lot of flexibility to,

to specify how to group the data.

But once you've done this,

this is just kind of the theoretical explanation.

So you'll have more of an idea when we start,

you know, look at codes, like what is,

what is this thing that I've created here?

So the, so the object that you get back from here

is a group by object.

And the only thing that it, that it knows,

it doesn't actually do any work.

All it does is it encapsulates the information

about how to split up the data.

And then from there, I mean,

you can decide what you want to do with it.

So you can, you can aggregate the data,

you can transform it,

you can apply an arbitrary function to the groups.

So these are the reason there, there are three functions

instead of, you know, just a single,

you can imagine in an ideal world,

you might just want just a single apply function.

But the reason that there are multiple functions

is because in the apply case,

where you just say,

I want to apply some arbitrary function

to each of the groups,

that the machinery doesn't know what you're about to do.

And so it has to, it has to do things in full generality,

has to split up and create all these Python data structures,

apply functions to the groups,

and then figure out with those results,

how to glue them back together,

how to put Humpty Dumpty back together.

So, so this is just kind of, you know,

high level picture will make a lot more sense in code,

I promise.

But the reason that there are these specialized

aggregate and transform functions,

because if you, if you know that you're aggregating,

you know that you're transforming, you know,

transformation means that you don't change

the size of the data.

You suppose you just subtracted the mean

from a group.

Yeah?

So when you call one of these functions, it's immediate.

Then the operation is actually carried out.

So the creation of the group by is sort of creating

a deferred, you know, here's how to group the data.

And when I actually call.

aggregator I call apply and then it actually goes and does the work.

So,

um, so that's all the slides I have. Um, does anyone have any,

any pressing questions we're going to, uh, yeah.

Yeah. Okay. We're going to do, we're about to do a lot of that.

So we're about to get very, very comfortable with, with group by, um,

I'll try not to lose my voice. So

yeah, sure.

Okay.

That's right. That's right. Yeah. So there's a, yeah. Okay.

So the question was, sorry about that. So the,

so the question was, um, the, the data that we're working with,

it has to fit into memory. It has to be able to fit into a NumPy array. Yes,

that is current. That is currently the case. Um,

there is a lot of interest in making, um, pandas or, or something,

or yeah, I think it needs to go in pandas, but, um,

making it work on memory maps or very large stores of data or basically

enabling pandas for a distributed computation and for dealing with big data.

But currently it's an in-memory data tool. Um, it's a limitation, but it's,

you know, it's a hard enough, it's hard enough problem. Um,

so anyway, so the, so the rest of the tutorial, uh, when,

when do we have a break just so I can, uh,

do we have a break planned? Okay. No,

we'll take a five minute break in about half an hour then. Um,

so the rest of the tutorial,

so we're going to load up data and you're going to load up data on your machines

and I will walk you through, you know, um, sort of nuts and bolts, like how this,

you know, how these objects work. Um,

and we'll start to ask some interesting questions of the dataset and, and,

and uh, carry through some analysis and I'll ask you to write some,

write a little bit of code and uh, yeah, so it should be,

this should be a lot of fun and I encourage you to, uh, to ask questions.

And if you see, if you, you know,

you might have an interesting idea like about something to do with the data.

And so if you, if you think of something like, Oh, I wonder what, you know,

I have something I'd like to figure out about this data. Just feel free to, uh,

feel free to ask and you know, I, we can do it right here. So,

so let's go back to the, um,

to the iPython notebook and click on the dashboard tab. Um,

and I want to open the, the basics file

and then I, and then minimize the, minimize the sidebar.

Okay.

Oh yeah. So let me go into full screen mode.

Is it pretty good? Yeah. Great. So, um, this,

this last line, the, uh, set print options. Could you, could you guys comment that

out? Um, and then, uh, so basically what's going on here. Um,

so I'm doing from pandas import star. I know pep eight says I'm not supposed to

do that, but pretty much everything we're going to be doing are going to be

pandas functions, um, pandas functions and numpy functions. So, um,

there isn't all that much in the namespace. So just importing pandas in case we,

we need, you know, to actually look at what's inside the module. Um,

and I've got important numpy as NP that's actually in,

this is sort of the standard convention for numpy. Um, it's in here,

but I put it explicitly here just so you know it's there. Um,

and this is just a little utility function that, that, you know,

we use for the notebook. So press shift, enter,

cross our fingers. Did that not work for anyone?

Okay.

Oh really? Did you launch the notebook with dash dash pi lab equals inline?

Okay.

Okay. So

to get that import, Matt potlib dot PI plot as PLT.

Can, when you, when you typed, if you play plot a range 10 to that,

does that insert a plot?

Okay.

My guess would be no.

Yeah.

Oh, nothing was supposed to happen.

It's just supposed to run and not generate an exception.

So if you didn't get a reception, if you did,

if you didn't get an exception, then everything, uh, you know,

so if I put, you know, foo here, then, uh, you'd,

you would see it print out an exception. Yep.

Um, I haven't really settled on one. Um, I, you know, I always, uh,

I always have like, you know, I, I shouldn't say this,

but I always have import star everywhere. But, uh, cause it's, it's,

what's that? Sorry about that. You know, it's, it's, uh, you know, it's,

it's at this point it's like it's set of,

it's a set of tools that I just sort of assume exist at all times. Um,

so, uh, what have I done here?

Something horrible has happened.

Yeah. Okay. All right. So now that that worked, hopefully, um,

if, if it didn't work for somebody, is there anyone,

is there anyone who can help her? Yeah. Okay. So we'll, we'll move on.

So, so scroll down to, you know, the CC section title series.

Um, so this, this first line that we look at, um,

I'm going to create a simple, a simple series from a Python list of,

of strings. So this is just like the one that I showed you in the slides. Um,

I'm going to pass the, I'm going to create a, an array of data.

So let me just show you what this is. So ran down five is a,

is a length five array, a NumPy array of, of normally distributed data.

Um, so I pass that as the first argument to series and I pass the labels to the,

as the index keyword. Um, so there's shift enter again.

Um, so that, so that creates a series and you can see now it,

it looks like a column, but really it's a one dimensional,

a one dimensional guy and it prints out the label associated with, uh,

with each value. Um, so now this, so now this object is,

it's like a, it behaves very much like a, like a, like a dictionary.

So I can say, uh, B and five B and S and it says true.

Um, so the labels, so let me create a cell here,

control M B. If I type S dot index,

you will see that it prints, uh,

it shows you an array of these are the labels that are contained inside the

series. Um, so if I do S sub the string B,

then it looks up the, uh, looks up the value,

looks up the value at, at location B. Um,

look, it's at this list line here, mapping equals, and there's a method on series.

Um, so if you haven't pressed tab yet, um,

so go up to here and you can delete this. And if you type two tab,

you should see a little drop down box of methods.

And so I can select the two dict method, press enter, open, close,

print. And so that just converted the series to, to a dict.

Um, I'm gonna make sure I enunciate today,

um, often slur my speech. And that, you know,

has led to jokes on Twitter. Um,

especially at the last NYC Python meetup. So if you have, so here you can see,

I created the series with an array and an array,

but it's very common to have a dict.

So you can also pass the dict to series

and create the series that way.

So what happens in this case is that there's

no specific ordering in a Python dict.

So it basically takes the set of keys and sorts them

and uses that to create the index.

So here, I could specify some other index.

So suppose that I wanted the values to be like B, E, A, D.

So I pass the list B, E, A, D. And I

don't know if you could guess what it's going to do.

So it creates a series that's B, E, A, D.

And it selected out those values from the dict.

So anything that was keyed on something that wasn't in the index

was thrown away.

So here, the C value isn't in the result.

So you can imagine if you had a set of labels

that you were really interested in, and you have some data found

in a dict, then you can create a series out of it

that exactly matches the labels that you have.

The question is, what happens when you have

a label that's not in there?

So in that case, the F value here

gets marked with not a number, which

is, in the case of floating point data,

the value that's used to mark missing.

So we're not going to get into a discussion about dealing

with missing data in Python.

It's just a rabbit hole that I do not want to go down today.

But the thing to know is that inside pandas,

there are two functions, isNull and notNull.

So in this case, if I call isNull on S,

I get a Boolean array, which tells me a Boolean NumPy array.

It has the same index as the series,

and it has true where it's missing.

So if we wanted to select out the data where it's missing,

we say S sub isNull S, and that gives me

the piece of the data where it's missing.

Also, I could do notNull, which is the opposite of isNull,

and select out the data where it's notNull.

So it's very common to have missing data in practice.

So being able to detect and filter out missing data,

the isNull and notNull functions are the way to do that.

This is so common in operation, there's

actually an instance method, dropNA.

I can call S dropNA, and that does the exact same thing.

Why isNull and not isNan?

Is there a particular reason?

isNan only works on floating point arrays.

So if you've used NumPy before, the series object

works very much like a NumPy array.

So I can do S times 2, which is a vector operation

and multiplies the values by 2, and the labels

stay attached to the data.

If I do slicing, so suppose I had

an array which is randN 5, like before,

when you slice that array, you get a slice of the data.

Same thing with the series, but I get a slice

of the data and the labels.

So you can treat it semantically like an end

array, except that you have this label indexing functionality.

So I passed the list B-E-A-D-F to the series.

Yep.

So hopefully, you've all followed along so far.

So the data frame is a two-dimensional object.

I will get better at repeating questions for the recording.

So the data frame you can think of as a collection of series,

as a dict of series.

And so there are many ways.

Well, there's a list of about six or eight ways

to create a data frame.

But one simple way is to pass a dict of arrays

that are all the same length.

They could be NumPy arrays.

They could be Python lists.

They could be a tuple.

But in this case, if you pass simple arrays or Python data

structures, they all have to be the same length.

So I don't know what version of pandas you guys are using.

But I'm using the development version,

which can emit HTML to the notebook.

So I'm actually just going to turn that off

so everyone sees the same thing.

How do I close that tooltip?

By Python, guys.

Something bad has happened.

What's that?

What's that?

What's that?

What's that?

Yeah, I'm clicking on it.

Sorry?

Yeah, it's a glitch.

Yeah, it is.

It's been resolved in the recent version.

Oh, gosh.

OK, so this is like a known bug.

OK.

OK.

Well, if that happens to you, I am closing that.

And then I'm reopening the notebook.

I'll cross my fingers.

So anyway, so if you ran that cell, you should get,

I just typed df here.

And so what happens is that whenever you type an object

into IPython, it calls its wrapper method

and gives you whatever result is returned.

[1:00:01] And so that happens to give us a string, a representation

[1:00:04] of a data frame.

[1:00:07] So here, you can think of this as like a dictive series.

[1:00:09] So if I do df sub a, I get the column a.

[1:00:12] df sub b, I get the column b.

[1:00:17] So you have a dict-like container of series.

[1:00:21] I can assign values here.

[1:00:22] So suppose I assign, do df sub d, and I say equals range 6.

[1:00:30] That just runs.

[1:00:31] And then I type df again, and you

[1:00:32] can see it's inserted a column d.

[1:00:36] You can also assign scalar values.

[1:00:38] Suppose I wanted to set the d column to the value 5.

[1:00:41] And then that propagates that value to the column.

[1:00:46] So it's not just a trick.

[1:00:47] It's actually creating an array of all fives.

[1:00:51] Yeah?

[1:00:52] So when you did df dot a, you put the column a, right?

[1:00:57] Yeah.

[1:00:58] But if I did df dot 0, I just wanted to see the row.

[1:01:01] OK.

[1:01:02] So does that mean that the columns cannot be numbers?

[1:01:07] The columns can be numbers.

[1:01:08] I'm about to get to that.

[1:01:11] So selecting rows, it does not go through the square brackets.

[1:01:18] Yeah?

[1:01:19] It doesn't have the function for recycling.

[1:01:22] Did you take the wire off of the foo bar?

[1:01:25] Because it doesn't have that function.

[1:01:28] Oh, OK.

[1:01:29] Yeah, so it doesn't try to tile.

[1:01:33] It doesn't try to, yeah.

[1:01:35] So in NumPy, there's a function.

[1:01:37] So if I call an np tile foo bar and comma 3,

[1:01:42] then that repeats the value.

[1:01:44] But it doesn't do that by default. Yeah?

[1:01:47] You can't slice rows with the brackets.

[1:01:49] Yes.

[1:01:50] Yes, you can slice rows with the brackets.

[1:01:51] So it's ambiguous whether you're referring

[1:01:58] to the columns or the rows.

[1:02:00] So I made the decision early on that get item refers

[1:02:05] to the columns.

[1:02:07] If I do colon 3 here, you can slice off the first,

[1:02:12] let's say, n rows of the data frame like that.

[1:02:16] So I do colon 3.

[1:02:18] That's there purely as a convenience.

[1:02:20] So sometimes people get upset.

[1:02:22] They'll be like, oh, well, I can slice.

[1:02:24] Why can't I index the rows like that?

[1:02:25] Well, I mean, this was added purely as a convenience.

[1:02:29] So I can do colon 4, select the first four rows, minus 2 colon,

[1:02:32] the last two rows.

[1:02:34] It's just so common that it's incredibly convenient.

[1:02:38] Well, I guess I can talk about label indexing

[1:02:40] and what that looks like using this small data set.

[1:02:45] So there's a function called xs.

[1:02:48] So if I do call the function xs.

[1:02:50] with 0, that gives me the 0th row, which is returned as a series, and the column

[1:02:57] labels become the index of the series that's returned. This is the exact

[1:03:02] same object, the exact same index object, which is stored in the data frame.

[1:03:08] Now, more generally, there are many ways you can select out subsets of the

[1:03:14] rows, and the most general, and we'll see a bunch of this throughout the

[1:03:18] tutorial, is a special field on data frame. If you do .ix, that actually

[1:03:26] returns... Sorry, do you have a question?

[1:03:32] Yeah, so you do colon 1. So yeah, the question was, can you slice for one row?

[1:03:40] Yeah, so if you do 2, 2, 2 colon 3, that gives you the single row, and it slices

[1:03:46] with Python semantics along the rows.

[1:03:53] So the question was, what if you want row 2 of B? The individual cell.

[1:04:02] So I'm about to tell you. So the .ix operator gives you a label

[1:04:11] index, is the label indexing facility. That's what I refer to it as. So it's a

[1:04:17] special object, which you then do an open square bracket. If I do... Basically what

[1:04:23] it enables you to do is to index the data frame like a NumPy array along...

[1:04:27] So this is axis 0, this is axis 1. So you can pass a tuple of the same kinds of

[1:04:35] things you would pass to a NumPy array to index along its rows and columns,

[1:04:39] except you can also pass labels. So I'm going to give you a bunch of

[1:04:43] examples now. So if I do .ix 0, that gives me the first row. If I do .ix 2,

[1:04:51] that is the second or, well, the number two, the third row. But if you do comma

[1:04:57] here, I can do comma and then the string B, and that gives me the scalar element

[1:05:03] at B. There is also a, there is a, a instance method,

[1:05:10] which if you profile is about, you know, one, one and a half microseconds faster,

[1:05:16] get value, or I can, I'm not joking. Are you interested?

[1:05:22] I mean, let's do time it, time it.

[1:05:24] Um,

[1:05:28] if it ends up being a one and a half. So,

[1:05:30] so get value took 1.53 microseconds and this one takes 2.78.

[1:05:38] So 1.25 microseconds. That was a pretty good guess actually. Um,

[1:05:42] you can tell I've spent far too much thinking about this. Um,

[1:05:47] yeah. What's that? Yes, indeed. Yeah.

[1:05:52] I think, uh, I think the time it, uh,

[1:05:54] the time it magic adds about maybe 25 to 50 nanoseconds of overhead if you're

[1:05:58] interested. Yeah. Um,

[1:06:04] I spend way too much time thinking about these things. Okay. So,

[1:06:08] so this is a way to select scalar elements.

[1:06:10] Suppose that you wanted to select a subset of the rows or so here this,

[1:06:14] this element two that says select the second row, but I could also slice.

[1:06:18] So suppose I want it to slice from position two to position four.

[1:06:22] So I changed that to two colon four and that now gives me a slice of the B

[1:06:26] column. So, um, but suppose that wasn't enough.

[1:06:31] Suppose we wanted a region, like suppose we want to call them B and C.

[1:06:35] We can change B to the list, B comma C.

[1:06:40] And that gives us the chunk of data referred to by,

[1:06:44] so the B and C columns. And then, you know, each of those is slicing. Yes.

[1:06:49] Yes. You, the question was,

[1:06:52] can you also slice by the columns and the answer is yes. Uh,

[1:06:55] so I can do B colon C, um,

[1:07:00] which slices from B to C. Now,

[1:07:03] if I did C colon B,

[1:07:07] I don't know if anyone can guess,

[1:07:08] but this is going to return nothing because C occurs after B. So the,

[1:07:13] so the way that label based slicing works is it, it, you know, it looks at,

[1:07:17] it looks at the, looks at the index.

[1:07:19] It's if both of those are contained in there,

[1:07:21] then it maps those to it maps those to maps those to integers.

[1:07:26] Um, and, uh, and then it, and then it slices with those. So in this case,

[1:07:31] C occurs after B. So if I did, you know, two colon one, that's the same,

[1:07:35] it's the same thing.

[1:07:37] So if you have integers in the columns and you slice with integers, then,

[1:07:41] you know, um, well, we're not going to get into that today. It's a,

[1:07:44] you can have a, an hour long discussion about a label indexing with integers.

[1:07:50] So, but the long story short is that you can slice, you can slice with integers,

[1:07:55] you can slice with labels. You can pass an,

[1:07:58] I hear I can pass an array of columns that I want to select over here.

[1:08:03] I can pass a list of rows. I want to select, I can say zero to four.

[1:08:08] And so that selects out the rows zero to four and the columns BCD.

[1:08:11] So this gives you a very natural way of, of, you know,

[1:08:13] given that you have a data that's indexed,

[1:08:15] you can select out subsets of the data very naturally. Um,

[1:08:19] you can also pass in, um, Boolean arrays.

[1:08:22] So control M a created a cell above.

[1:08:27] So suppose that I wanted to select out the data where the C column is greater

[1:08:33] than zero. So here I do C greater than zero.

[1:08:38] It gives me a Boolean array. And so down here I do DFC

[1:08:43] greater than zero. And that selects out that selects out that data for those

[1:08:48] columns. So I can get rid of that. And then, yeah.

[1:08:53] And then that's everything.

[1:08:55] It also happens to be the case that you can pass a Boolean array to data frame,

[1:08:59] get item. And that also works cause that's also extremely common and unambiguous.

[1:09:07] Okay. So, um, all right, we're going to start, uh,

[1:09:13] we're an hour and 10 minutes in. So we're going to,

[1:09:15] we're going to start to pick up the pace here. So, you know,

[1:09:19] here in this case, the, the, the, the, the index is, is integers.

[1:09:25] Um, so I'm not going to go, we're not talking about time series, but you know,

[1:09:29] in pandas can generate a regular frequency, um, dates.

[1:09:33] So, uh, there's a date range class which generates a date index. So here I,

[1:09:37] I said, um,

[1:09:39] um, I want, I Python 0.13 deaf.

[1:09:43] So I use get master all the time. It doesn't have as many bugs. So, uh,

[1:09:47] so I, so this, this statement generates a date range, six periods long.

[1:09:51] So this was the exact same creation statement before.

[1:09:53] And you can see now that the, the data frame has dates as the dates,

[1:09:57] as the rows. Um,

[1:10:01] similar to the series, uh, series constructor,

[1:10:04] I can pass an explicit list of columns, which specifies the column order. Um,

[1:10:08] so here is a case where I had addictive data. Um,

[1:10:12] and I had a column which didn't exist in that dict and you can see it creates an

[1:10:15] a column that's all in a, uh, so if I did, you know, uh, is no,

[1:10:21] uh, is no DF. And then you can see that that column is all,

[1:10:26] is all N a.

[1:10:29] So, um, so you see this little section here,

[1:10:34] sort of the last bed on a, on creation,

[1:10:38] just so you can get a feel for what's going on, what's the data. Um,

[1:10:42] got a little sort of nested for loop where I create a nested dict of data.

[1:10:45] How many nested dicts have you ever seen in Python? I've seen a lot in my day.

[1:10:49] Um, you can imagine. So, so often you might have a nested dict like the,

[1:10:55] but the keys on the, on the dict on the,

[1:10:58] each of the Python dicts inside is there are different and you might just want to

[1:11:03] say munch those into a table. Um,

[1:11:06] and so you can just pass a nested dicts to data frame and it will create a table

[1:11:10] out of that and sort the, sort the, the outer. So the outer, um,

[1:11:16] keys become the columns because you can imagine, you know,

[1:11:19] because a dict maps onto a series.

[1:11:21] So you can imagine addictive dicts being the same thing as like addictive series.

[1:11:25] And so that munches, um, munches everything into a table.

[1:11:29] But suppose that I, you know, went, uh, here and, um, I said, uh,

[1:11:34] well, uh, if I want to delete a key,

[1:11:38] I'm going to have to do Dell data foo C.

[1:11:45] So there I deleted a value and you can see it's inserted an N a into that

[1:11:49] location where I

[1:11:50] deleted a key from one of the dicts inside.

[1:11:54] So a lot of different ways that we can create data frames.

[1:11:57] Mostly, we're about to load some data from CSV files,

[1:12:00] so you won't get to have the pleasure of creating data

[1:12:03] frames yourself.

[1:12:05] But the entire goal of the constructors

[1:12:08] is if you have a list of tuples, you have a list of dicts,

[1:12:12] you have a numpy array, you have a dict of numpy arrays,

[1:12:14] you have a dict of series.

[1:12:16] Anything under the sun, if it's got labeling information

[1:12:20] or it's array-like, it's designed

[1:12:22] to be very easy to get that into a data frame

[1:12:25] structure, which is where all the magic starts to happen.

[1:12:30] So if we go down to the data alignment section,

[1:12:33] so we'll see our first example of reading in data from a file.

[1:12:38] I'm just going to fly through this section

[1:12:40] to give you an idea of the data alignment feature.

[1:12:42] So call read CSV.

[1:12:45] This is a CSV file.

[1:12:46] If you look at, if I do head-n10, stock,

[1:12:52] IPython completes in the file system,

[1:12:55] which is a nice feature.

[1:12:56] So you can see I'm a big IPython fan.

[1:13:02] So who wouldn't be?

[1:13:05] So you see the CSV file.

[1:13:07] It has some column headers.

[1:13:08] This is just some stock data that I downloaded.

[1:13:11] And I said I want to use the first column, which

[1:13:15] has the dates.

[1:13:15] This didn't print very well, so I've got the image blown up.

[1:13:19] The first, use the zero column, the first column

[1:13:21] as the index, and their dates.

[1:13:23] And so there's a parse dates flag.

[1:13:24] So it's very common to work with time series data and CSV files.

[1:13:27] So that creates a data frame which

[1:13:32] contains some stock price data from 2007 through 2011.

[1:13:37] And the entire purpose of this is I just want to show you,

[1:13:42] so I selected out part of the Apple time series.

[1:13:47] I only have through October 14.

[1:13:48] So the real fun stuff, part of Apple stock

[1:13:51] has been in the last two months.

[1:13:55] But if any of you are Apple shareholders.

[1:13:58] So here we have two time series which are differently indexed.

[1:14:04] And so I just wanted to show you that if I add those together,

[1:14:07] then it just works.

[1:14:08] So I can say series one plus series two.

[1:14:10] It forms the union of the dates.

[1:14:13] You can see that these have different start dates

[1:14:15] and different end dates.

[1:14:16] So it inserts NAs on both ends of the series.

[1:14:20] It forms the union of the indexes.

[1:14:22] And so you could take this and then drop NA on it

[1:14:26] to select out the common set of data

[1:14:28] where I actually added something together.

[1:14:35] Yep.

[1:14:36] Sure.

[1:14:37] Can you configure that to say, for example,

[1:14:42] use zeros in the addition?

[1:14:44] Yes.

[1:14:44] So the question is, can you choose

[1:14:50] to use a zero instead of an NA in the addition?

[1:14:53] And the answer is yes.

[1:14:55] But you have to call a method.

[1:14:56] So I have to say s add s1, s2, s add s2.

[1:15:01] And then I say fill underscore value equals zero.

[1:15:04] And so what that's going to do is any place where one

[1:15:06] of them is NA but the other's not,

[1:15:08] it will use a zero for that location.

[1:15:11] But if there's a label where they're both missing or NA,

[1:15:17] well, the index is not there and the other one's NA,

[1:15:19] then you'll get an NA.

[1:15:21] So it's kind of a, so you can see here, if I did that,

[1:15:24] and now I just get the value that was there

[1:15:26] and those missing, because it's just the same time series

[1:15:29] but sliced slightly differently, it

[1:15:31] becomes double in the overlapping region.

[1:15:34] And then you can see it.

[1:15:35] So it used the zero to fill there.

[1:15:38] So you have a lot of flexible arithmetic methods.

[1:15:40] You can align doing different join methods.

[1:15:43] I just wanted to show that we're not

[1:15:45] going to do a lot of this stuff in the tutorial.

[1:15:47] But so you can, this little side by side function

[1:15:51] just prints two objects alongside each other.

[1:15:54] So just useful for illustration purposes.

[1:15:56] But so there's a reindex function which works.

[1:15:59] I could have called dot, I'm hitting

[1:16:03] my Python bugs like crazy.

[1:16:06] Where's Fernando?

[1:16:07] I could give him a hard time.

[1:16:10] It's all been fixed in the development version.

[1:16:13] So I can call dot, IX instead of the API method reindex.

[1:16:16] And that does the exact same thing.

[1:16:18] It explicitly conformed the series one

[1:16:21] to series two's index.

[1:16:22] So you can see here is the guy, the S2.

[1:16:26] And here was, and I called S1 dot, IX, S2 index.

[1:16:30] And so that conformed S1 to this index

[1:16:34] and inserted NAs in the holes.

[1:16:38] So there's also methods like align.

[1:16:42] So you can say S align, S2 join inner.

[1:16:45] And that does the intersection.

[1:16:46] There's outer right, left, inner outer join.

[1:16:49] So it kind of fits with the language of SQL joins.

[1:16:54] And so if you've used SQL before,

[1:16:57] the semantics are quite similar.

[1:17:00] AUDIENCE MEMBER 1 What about the file type, MATLAB?

[1:17:05] There's nothing in pandas for loading MATLAB files.

[1:17:07] But there are tools in the Scientific Python ecosystem

[1:17:10] for loading MATLAB files.

[1:17:11] I have done it, and it worked.

[1:17:14] I think it's scipy.io.loadmap.

[1:17:16] The question was if it's possible to load MATLAB

[1:17:18] files and other file types.

[1:17:22] So we've already seen that the columns can be anything.

[1:17:28] I just want to make that clear.

[1:17:30] There's a little section on function application here.

[1:17:34] So you can apply arbitrary methods

[1:17:39] to the columns, to the rows.

[1:17:42] So if you wanted to take the mean of the columns or the

[1:17:45] rows, there's also many common statistical methods.

[1:17:49] If I call the mean method, that computes a mean of the columns.

[1:17:53] You can see it's attached the column labels to the result.

[1:18:00] So the default is to take the mean of the columns.

[1:18:02] If I do mean one, I get a mean of the rows.

[1:18:06] It also excludes missing data.

[1:18:08] So if you have NAs in your data, then it all

[1:18:10] gets excluded behind the scenes.

[1:18:13] There is a flag skipNA.

[1:18:15] I could say skipNA false.

[1:18:17] There were no NAs in this data.

[1:18:18] But if you didn't want to exclude NAs,

[1:18:20] you have the option not to.

[1:18:25] So there is an access keyword.

[1:18:34] So I can say, so if I do df mean, well, let's look at it.

[1:18:40] So if I do question mark in IPython,

[1:18:43] you can see this function signature has access,

[1:18:46] access keyword, and then skipNA.

[1:18:48] There's also a level argument, which

[1:18:52] is related to hierarchical indexing.

[1:18:56] So what's cool about having a generic way

[1:18:58] to apply functions to data is that because you've

[1:19:01] got this labeling information, you

[1:19:05] can get really fancy with the methods that you apply.

[1:19:08] So here is a slightly non-trivial example

[1:19:11] where we've got this big data frame of 1,000 periods

[1:19:15] of a time series.

[1:19:16] And suppose you wanted to select the date on which

[1:19:22] the maximum value in one of the columns occurred.

[1:19:27] So the way that you would do that is suppose

[1:19:31] we look at the closing price.

[1:19:35] Oh, so one additional thing I haven't mentioned yet

[1:19:37] is that you can complete the columns.

[1:19:39] So if I do .tab, so here the columns are all uppercase

[1:19:43] and happen to appear in the completer.

[1:19:46] But if I had started typing Apple,

[1:19:51] you can see that the two columns that start with A

[1:19:54] appear in there.

[1:19:55] So it's common you might have a data set where the column names

[1:19:58] are actually pretty long to type.

[1:20:00] And so if you want to say close price bracket

[1:20:03] and then have to type out that string,

[1:20:05] that would be a lot of typing.

[1:20:06] But if you're working in the notebook or in the IPython

[1:20:08] shell, you can just start typing it.

[1:20:10] You tab, and it will show you the columns that

[1:20:13] match what you've typed so far.

[1:20:15] Then I can just press Enter.

[1:20:17] That gives me the Apple price.

[1:20:22] So there are a couple ways that we can get the index

[1:20:24] of the maximum value.

[1:20:26] So there happens to be API methods that do that.

[1:20:29] So IDXmax gives me the index of the maximum value.

[1:20:32] So if I call IDXmax on Apple, that

[1:20:35] gives me the index for its maximum value, which

[1:20:40] happens to have been the last, well, October 14, 2011.

[1:20:43] So I haven't gotten the latest data.

[1:20:46] Another way you could have gotten that is indexing

[1:20:49] into its index with.

[1:20:52] with, if you're NumPy aficionados, you can call the argmax method, and that does the

[1:21:03] same thing.

[1:21:04] So I thought that idxmax was a lot less typing.

[1:21:08] This is a pretty common operation.

[1:21:13] So here, well, you can see this is from an older demo before I implemented idxmax, and

[1:21:18] so I can call series.

[1:21:21] I create a little function called peakDate, I call idxmax here, so I have this little

[1:21:26] peakDate method which takes a series, and then I apply that function to the data frame.

[1:21:32] So it's going to call peakDate on each column, and so what that does is it returns a series

[1:21:39] which is now indexed by the column names of the data frame, and it's extracted the index

[1:21:46] of the maximum value for each column.

[1:21:49] So it gives you a powerful way of, you can access, you can apply functions to the rows,

[1:21:55] apply functions to the columns, you've got the labeling information, so really the world's

[1:21:59] your oyster, you can get as fancy as you want.

[1:22:05] So the last thing is, so there's some plotting integration things we're going to look at

[1:22:12] in these real data sets we're about to start exploring.

[1:22:18] Another shortcut you can use for selecting columns out of a data frame, you can pass

[1:22:22] a list of columns to get item, so you don't have to call use.ix, this is another reasonably

[1:22:30] unambiguous case.

[1:22:33] And so we'll get rid of this dot plot here.

[1:22:37] How many of you have this, you guys have this data in memory, you were able to read it from

[1:22:43] the CSV file I hope?

[1:22:45] Cool, cool, cool.

[1:22:47] So by passing the list of these four tickers to get item, I get a data frame of just those

[1:22:54] four columns, and now if I call dot plot, you can see what that does is it creates a

[1:23:03] matplotlib plot of the four time series, it creates a legend, it passes the index, so

[1:23:10] these are dates in this case, and so you get like a reasonably attractive plot with just

[1:23:15] one command, and so I'm of the opinion that we should be doing more stuff like this.

[1:23:21] I've sort of lately, I tell people that I'm anti-DIY, so it's very common on the mailing

[1:23:30] list and in the community, they'll be like, how do I do this, and I'll be like, oh, what's

[1:23:34] these six, eight lines of matplotlib, or it's these six or eight lines of numpy, but you

[1:23:38] see that happening with the same kinds of things over and over again, and I feel like

[1:23:44] that mentality of like that, it's like, oh, just learn this API and write these eight

[1:23:47] lines of code, I feel like that sort of gets in your way, and if you have to, each time

[1:23:51] you want to create a good-looking plot, if you have to, because there's actually quite

[1:23:56] a lot of code that does this, but it's extremely straightforward.

[1:23:59] You've got the row labels, you've got the column labels, so you have everything you

[1:24:03] need to create the plot, so I would much rather just type dot plot, but that's just me.

[1:24:10] So, suppose, so in a case where, suppose that we had like the last row, so we do dot ix

[1:24:18] minus one, so that gives us the last row of the data, so you can create other kinds of

[1:24:23] plots from a series, so in this case, there's no sense of orderedness in the data, so we

[1:24:29] might want to create a bar plot, so you can call the series plot method, say kind equals

[1:24:34] bar, which is funny because I've been having like foo bar baz stuff all over the place

[1:24:41] here, but this will create a bar plot, and hopefully you will see something that looks

[1:24:46] about like this, so it creates a bar chart, and it sets the index values from that series,

[1:24:54] so close px dot ix minus one, so it attaches those to the chart, so there's quite a bit

[1:25:06] of plotting code, it's something I definitely want to do more, so if you use pandas and

[1:25:10] you want to get involved, one great way to get involved is to create awesome plotting

[1:25:15] functions in matplotlibs, especially if you create a visualization yourself that seems

[1:25:19] sufficiently common that it's like, oh, I don't want somebody else to have to write

[1:25:24] this code again for doing this common sort of plot, those are the kinds of things that

[1:25:27] I want to put in here, especially with doing grouped plots where data is split into groups,

[1:25:33] you might want to create a scatter plot matrix, or like a grid of histograms, the amount of

[1:25:40] code that you would have to write to do that by hand is quite large, so I've been trying

[1:25:44] to sort of put a lot of that into the library.

[1:25:49] So okay, I'm not going to melt your brain with hierarchical indexing quite yet. So let's

[1:25:58] take five minutes, and I'm going to sip some water, and let's open a new notebook, and

[1:26:06] then we're going to look at baby name data. Does anyone have any questions right now?

[1:26:14] Great. Okay. Wow, this is so good. Okay. All right. So what I'm going to do is I'm

[1:26:44] going to, so has everyone created a new notebook? Wonderful. All right. So up here, let's just,

[1:26:54] you can change this name to something like baby names, so if you want to come back and

[1:27:00] click rename, and if you want to come back to this file later after we do some fun stuff

[1:27:05] with it. So let's load in the baby names data set. So do names equals read CSV. Well, from

[1:27:14] pandas import star. Okay. That's the first thing we need. And then names equals read

[1:27:21] CSV, baby names dot CSV. You can tab complete that. So if all goes well, it should load

[1:27:30] in in about a second or two.

[1:27:37] And so if you type in names here, you can see that we've got a data frame which contains,

[1:27:42] well, so it's big. So it's 258,000 rows and five columns. So I'm going to call the data

[1:27:48] frame head. I need to turn off the, I'm going to turn off the HTML here. If you don't see

[1:27:59] HTML output, then don't worry about this part. Okay. So you should see something like that.

[1:28:07] So the idea is that we have a data set which contains, it has year, it has a name, it has

[1:28:14] a proportion of that sex that was given that name. This is in the United States. Then there's

[1:28:22] this sound code which basically gives you a way to group names together that sound similar.

[1:28:28] I don't think we're actually going to do anything with this column because I didn't actually

[1:28:31] look at it to figure out what it means.

[1:28:37] So but the basic story is that we have for each year the top 1,000 baby names. So suppose

[1:28:42] we wanted to select out all of the names for the year 1880. So inside data frame, we could

[1:28:49] do names dot year equals equals 1880. So if you've never seen NumPy before, so when you

[1:28:56] do names dot year, that's a series. That's a column from the data frame. When I say equals

[1:29:01] equals equals, a scalar that does a vector operation, it produces a Boolean array, and

[1:29:05] I can pass that to data frame. I get item which gives me, let's see, up here I'm going

[1:29:12] to do set print options. You can do this yourself if you want. I'm going to call it max rows.

[1:29:19] Max underscore rows equals like 5,000 or something. Feel free to do this if you wish.

[1:29:27] So I do that, and that prints out a big, well, I don't have scroll bars because I'm in full

[1:29:34] screen mode, so pardon me. What happened to my scroll bars, iPython people? Is that some

[1:29:43] feature or bug of the full screen mode, that my scroll bars disappeared? What's that? Yeah,

[1:29:50] That's also quite possible.

[1:29:53] Well, pardon me.

[1:29:54] I'm just going to close this and open it back up.

[1:29:58] If you reload the dashboard, you'll

[1:30:01] see notebooks that you've created.

[1:30:03] OK, now I've got crap.

[1:30:11] I think it's a Chrome bug.

[1:30:12] Can you delete the sound?

[1:30:14] Can you go to the resize your browser?

[1:30:16] Yeah, that might do it.

[1:30:20] What's the name of the sound?

[1:30:23] Yeah, but I mean, that doesn't solve my problem.

[1:30:33] Good point, yeah.

[1:30:34] It's a real problem.

[1:30:49] OK, great.

[1:30:51] Thanks, Apple.

[1:30:56] So if we select out all of the baby names for 1880, we get a

[1:31:01] subset of the data frame.

[1:31:05] So I'm going to go back up here and set max rows to like 500

[1:31:11] again, just so we can get a summary view.

[1:31:15] Names to year equals equals 1880.

[1:31:18] OK, so you can see here for 1880, we have 1,000 values for

[1:31:22] boys, 1,000 values for girls.

[1:31:24] A simple way to get the top five rows is the head

[1:31:27] function, so you can call head.

[1:31:30] Tail gives you the last five rows.

[1:31:32] You can see we've got boys and girls names.

[1:31:35] So for purposes of the next little bit of time, so let's

[1:31:40] separate the data into boys and girls names, because we're

[1:31:43] going to analyze them separately.

[1:31:44] So we'll say boys equals names, names.sex, sex equals

[1:31:50] equals boy, and then girls, same thing, but name sex

[1:31:59] equals equals girl.

[1:32:02] Yeah, go ahead.

[1:32:03] AUDIENCE MEMBER 2.

[1:32:04] Could you go back?

[1:32:05] We can't get the names.year equals 1880.

[1:32:07] Because I'll miss out on that.

[1:32:09] What version of pandas are you on?

[1:32:11] Must be on less than 0.7.

[1:32:12] AUDIENCE MEMBER 2.

[1:32:13] I just installed it today.

[1:32:14] Oh, really?

[1:32:17] Well, you should be able to, almost everything that I'm

[1:32:24] doing here works in an earlier version, but some things like

[1:32:28] maybe the .attribute does not.

[1:32:31] So you could also do that.

[1:32:33] Maybe try, well you might just see what

[1:32:36] version that you're using.

[1:32:38] AUDIENCE MEMBER 2.

[1:32:39] How do I get to that version?

[1:32:40] Import pandas, pandas.magicversion.

[1:32:46] That's strange.

[1:32:47] So when you do names.year, that doesn't work.

[1:32:50] So if you do names.year, so we do equals equals 1880, and

[1:33:10] then you do names sub 1880.

[1:33:13] Now I get this class pandas.

[1:33:15] That's where I print that data frame.

[1:33:17] Uh-huh.

[1:33:17] Yep.

[1:33:18] That's right.

[1:33:20] Yeah, well, that's because I said, it basically has a

[1:33:23] threshold after which it prints a summary view versus

[1:33:25] printing everything.

[1:33:26] So you imagine if you print a really large object, then

[1:33:29] something with a million rows, and then it's like you're

[1:33:31] stuck waiting for your terminal to buffer the input,

[1:33:34] the output.

[1:33:34] It's happened to me a million times.

[1:33:37] OK, so anyway, so we segment the data into boys and girls

[1:33:42] names, so hopefully you can get this working.

[1:33:45] So we have two data frames now, boys and boys and girls.

[1:33:54] And so now, I don't know if you thought much about baby names

[1:33:58] data, but there's a number of things that you might be

[1:34:01] interested in asking about the data set.

[1:34:02] So basically, what are the most popular five or 10 names

[1:34:07] per year?

[1:34:10] Given a particular name, what's the rank of that name?

[1:34:13] Or how many people were named that name over time in each

[1:34:19] year, and how has that changed over time?

[1:34:21] So a lot of fun and interesting trends in naming.

[1:34:24] How has the diversity of baby names changed over time?

[1:34:29] So anyway, I'll show you.

[1:34:30] These are some of the questions that we're going to

[1:34:32] be able to answer right now.

[1:34:36] So just to give you sort of a gentle introduction to the

[1:34:40] GroupBy facility in pandas, so let's just look at the boys

[1:34:45] data frame.

[1:34:49] So it's got a year column.

[1:34:50] So suppose that we want to do something by year.

[1:34:54] So to do that, we do dot, and we use the GroupBy method, and

[1:35:01] then we're going to pass the string year.

[1:35:03] And so if you call that, you should get a string which

[1:35:05] looks about like this, which it returns this data frame

[1:35:09] GroupBy object.

[1:35:10] Can you scroll up a little bit?

[1:35:11] Uh-huh.

[1:35:13] No, no.

[1:35:13] Oh, sorry.

[1:35:14] I meant the other way.

[1:35:15] The other way.

[1:35:17] Your pen is moving the light for those guys.

[1:35:20] Oh.

[1:35:21] OK.

[1:35:22] All right.

[1:35:23] That's good to know.

[1:35:24] Here, if you could go up another one.

[1:35:29] I wonder if I can go into full screen mode here.

[1:35:32] Do I attempt to fade?

[1:35:34] Does Apple do that?

[1:35:39] I hate technology.

[1:35:43] I could move the lectern a little bit.

[1:35:45] I'm going to get myself in trouble if I do that.

[1:35:49] What's that?

[1:35:50] AUDIENCE MEMBER 2.

[1:35:51] That row's at the bottom.

[1:35:52] Yeah.

[1:35:53] I can't scroll down anymore.

[1:35:59] I'll do that, right?

[1:35:59] OK.

[1:36:00] That great?

[1:36:00] All right.

[1:36:01] I'll keep that in mind.

[1:36:03] OK.

[1:36:05] What's that?

[1:36:10] View, Hide Toolbar, and then is there anything else that I

[1:36:17] can do, Hide Bookmarks Bar?

[1:36:18] OK.

[1:36:22] Only in the dev version.

[1:36:25] Yeah.

[1:36:26] You'd probably get a menu, too, and a more attractive

[1:36:29] looking sort of thing.

[1:36:31] This has the sidebar.

[1:36:32] Yours doesn't.

[1:36:33] I bet.

[1:36:35] OK.

[1:36:35] So when you call Group By, you get this object back.

[1:36:39] And what's nice about it is that there's lots of things

[1:36:44] that you can do with it.

[1:36:48] So the first thing we might want to do is it has a size

[1:36:51] method, so if you call it size method, that's a method that

[1:36:55] happens to be implemented on DataFrame.

[1:36:57] And what it does is it gives you the number of records that

[1:37:00] are found within each unique value of the year column.

[1:37:03] So you can see that, I wasn't lying to you, that we've got

[1:37:06] 1,000 records per year.

[1:37:13] But you can pass multiple, you can pass more than a single

[1:37:19] column to Group By.

[1:37:20] So in the case of the names database, suppose we did

[1:37:24] Group By, and then we pass the list, sex, and then year.

[1:37:30] Now this groups by two columns.

[1:37:31] And if we call size, then the thing that we, let's actually,

[1:37:35] I'm going to change the order to be sex, comma, year.

[1:37:40] And then the thing that we get back, and let me try to

[1:37:43] explain what we're looking at here.

[1:37:45] So what this does is it says, OK, we grouped on two fields,

[1:37:50] on two columns of the DataFrame.

[1:37:52] The size method tells us the number of records, the number

[1:37:55] of rows in the DataFrame, which are found in each key

[1:38:00] combination.

[1:38:00] So in 1880 for boy, there's 1,000 records.

[1:38:02] For 1880 for girl, there's 1,000 records.

[1:38:05] So it puts empty space here, just to make this more

[1:38:08] readable.

[1:38:08] But you can imagine here, it's 1880, 1880, 1881, 1881.

[1:38:13] And so this is the first example that I've shown you

[1:38:15] of what I generally call a hierarchical index.

[1:38:20] And basically, this object is still a series.

[1:38:24] So it's just like all the objects we've been seeing.

[1:38:27] So if we'll do type, you see it's a series.

[1:38:31] But the index now has multiple levels.

[1:38:36] So suppose that I wanted to select out the group for

[1:38:40] 2000.

[1:38:42] I use the label indexing operator, .ix.

[1:38:45] I do .ix 2000.

[1:38:47] And that selects out a subgroup.

[1:38:50] group of the data.

[1:38:52] So here, I mean, they're all the same because there's 1,000

[1:38:54] records for everything.

[1:38:56] But you can see that it's selected out that little slice

[1:39:00] of data that was labeled by 2000.

[1:39:03] And now I just get a simple series, which is labeled by

[1:39:06] the inner level, which was the sex.

[1:39:09] So it gives you kind of a natural way of referring to

[1:39:12] groups of data.

[1:39:13] So if you got in the outermost level, we have years.

[1:39:17] So you can select out 2001, 2002.

[1:39:21] So the levels don't have to be the same size.

[1:39:24] I mean, it's extremely flexible.

[1:39:26] So just imagine a tree of labels and a means of

[1:39:29] selecting out subsets of the data.

[1:39:31] And you're going to see a lot more of this over the next

[1:39:35] hour and a half.

[1:39:36] So this really isn't all that interesting.

[1:39:41] OK, we've got 1,000 records per group.

[1:39:45] But now, we might want to, say, compute the most popular

[1:39:52] boy's name for each year.

[1:39:55] So what would that look like?

[1:40:02] So I'll kind of work through what this looks like.

[1:40:04] So to take the boy's data for a particular year, this is how

[1:40:09] I usually write code.

[1:40:11] So if we look at year equals equals, let's say, 2000.

[1:40:15] So these are the boy names for 2000.

[1:40:20] So if we take the prop column, which is the proportion of

[1:40:28] names that were given to a particular boy, so these

[1:40:33] happen to be sorted in descending order.

[1:40:35] So if I looked at the first five rows, you can kind of

[1:40:39] already give it away that it's actually Jacob was the most

[1:40:43] popular boy's name in 2000.

[1:40:45] But if we wanted to sort of tease that out of the data

[1:40:47] without looking at it and knowing what order that it's

[1:40:50] in, so we can take the prop column.

[1:40:53] And then, we have a couple of options here.

[1:40:55] So I would just call that IDX max method that I showed you,

[1:41:01] which gives me the index of the maximum value.

[1:41:08] And then, if you wanted to get the whole row for that, you

[1:41:12] could pass that to boys.ix.

[1:41:14] And so that gives you the record of, I guess, the

[1:41:19] maximum proportion for that data set, for that year.

[1:41:24] Excuse me.

[1:41:26] So now, you're like, OK, well, this is sort of generic code.

[1:41:31] And let's do this for each year.

[1:41:34] So I'm going to put this into a little function.

[1:41:38] So get max record.

[1:41:42] Let's call it group.

[1:41:44] And I'm going to change this boys to group.

[1:41:51] Oh, gosh, I have to change it on a lot of places.

[1:41:55] OK, well, that's a mouthful now.

[1:41:59] So this is a function which takes a group of the data.

[1:42:03] It says, oh, this is now I've got to do.

[1:42:05] So the group of data is actually, OK, excuse me.

[1:42:15] So we've got the group of data.

[1:42:18] For each year's worth of data, we take the prop column.

[1:42:22] We get the index of its maximum value.

[1:42:24] And then, we use the indexing facility to retrieve the

[1:42:27] record for that index.

[1:42:30] So if we applied this function to the whole data set.

[1:42:41] So this would be the most popular.

[1:42:46] So this would be the record for which there was a boy's

[1:42:50] name that was the highest proportion for that year

[1:42:52] across the entirety of time, across the whole

[1:42:55] data set, anyway.

[1:42:56] So if we've just passed boys there, you can see that in

[1:43:00] 1880, 8.15% of boys were named John.

[1:43:08] And so the thing is, you might want to do

[1:43:09] this once per year.

[1:43:11] So we do boys group by.

[1:43:16] And then, we pass year.

[1:43:18] And then, now, we call the function apply.

[1:43:20] And we pass getMaxRecord.

[1:43:22] And so now, what this is going to do in the background is it

[1:43:25] splits up the data by year.

[1:43:27] It applies this little function to each one to

[1:43:30] retrieve that row of the boy's name and the proportion that

[1:43:35] was the most popular name that year.

[1:43:37] And then, it's going to take all those.

[1:43:39] And it's going to stack them into a result data frame.

[1:43:41] So you would expect to get a data frame that has one record

[1:43:48] per year.

[1:43:53] So we do that.

[1:43:55] And hopefully, it works.

[1:43:59] And so now, we get a data frame where you can see that

[1:44:02] it's taken each record.

[1:44:03] And it's glued things together.

[1:44:04] And it's now indexed by year.

[1:44:07] And so you can see that John was just super popular.

[1:44:10] And you can see the popularity goes down over time.

[1:44:12] And then, it becomes Robert and James and Michael.

[1:44:15] And it becomes Jacob at the end.

[1:44:18] Jacob is super popular.

[1:44:21] But it's interesting.

[1:44:22] You can see that the percentage is going down over

[1:44:25] time, so only one in 100 boys is named Jacob in 2008.

[1:44:31] But eight in 100 was named John in 1880.

[1:44:35] So the diversity of names is going up over time.

[1:44:38] So that's one thing to notice.

[1:44:42] So you might take this result.

[1:44:44] So let's save this into result variable.

[1:44:48] Call this result.

[1:44:52] Save that into result.

[1:44:56] And so we could take the prop column and just plot it if you

[1:45:01] want it.

[1:45:02] So you can see that this is the graph of the proportion

[1:45:07] for the most popular name over time.

[1:45:10] So you can see that people are getting more and more

[1:45:15] creative.

[1:45:16] And then, I guess, in the Great Depression, people became

[1:45:19] a little less creative, and then more creative, and then

[1:45:22] less creative.

[1:45:23] And now, they're just getting really, really creative, or

[1:45:25] something like that.

[1:45:27] So we're going to figure out maybe a little more of what's

[1:45:29] going on there.

[1:45:31] So that's one sort of thing.

[1:45:41] So we'll think about group by a little

[1:45:45] more here in a second.

[1:45:46] So let's go back to the original Boies database.

[1:45:48] And so here, the records, the data in this data frame, each

[1:45:54] record is uniquely identified by a year and a name.

[1:45:57] So no two-year name combinations occur twice.

[1:46:03] Because within each year, a name only appears once in the

[1:46:05] data set.

[1:46:07] So if you wanted to be able to have a fast way, because

[1:46:12] remember, suppose we want to, you guys know Travis Oliphant,

[1:46:16] the author of NumPy.

[1:46:17] So he'll be around at the conference.

[1:46:19] You should say hello, thank him for making NumPy happen,

[1:46:25] among other things.

[1:46:26] So suppose we wanted to select all the records for Travis.

[1:46:29] You see how popular is the name Travis over time.

[1:46:32] So we select out those records.

[1:46:38] And so we get a data frame.

[1:46:40] You can see here's the percentage of boys named

[1:46:46] Travis over time.

[1:46:50] But the thing is, you've got to remember, whenever we do

[1:46:53] this, that this operation right here, when I say boys.name

[1:46:56] equals equals Travis, that's having to do a comparison for

[1:47:01] every element in the name column.

[1:47:03] So if that was a really long array, in this case it's

[1:47:09] 129,000, and you wanted to do some processing for each name

[1:47:13] in the data set, then you could imagine that that would

[1:47:21] add up to take a long time.

[1:47:22] I'm not going to do it.

[1:47:25] So one way you can get around this is you can just index the

[1:47:27] data frame by name and year.

[1:47:31] Let's just show you exactly what I mean by that.

[1:47:33] So there's a function set index.

[1:47:35] So here I can say index by name and year.

[1:47:44] And we'll save this into, I'm going to call it IDF, so it's

[1:47:47] an indexed data frame.

[1:47:49] Create a cell, Control-MB.

[1:47:54] And so now, well, it gives us a summary view because it's really big, but let's look at

[1:47:58] the first, like the last 50 elements, so open square bracket minus 50 colon.

[1:48:10] And so you can see here that what's happened here is that the name and the year column

[1:48:15] have been pulled out of the data set and they're now part of the index.

[1:48:19] So you can see that there's an empty space here, and then the name and year column have

[1:48:24] been moved into the row index.

[1:48:27] And so now, what's nice about this is that we can use the label indexing.

[1:48:30] We can say .ix Travis, oh gosh, that didn't work.

[1:48:36] Oh, there's no Travises in the last 50 elements of the data set.

[1:48:43] So if we do .ix Travis, you can see that that gives us the slice of data, basically

[1:48:48] all of the Travis proportions across the whole data set.

[1:48:54] So if you wanted to see a plot of the popularity of Travis over time, relative to the whole,

[1:49:00] the proportion of boys named Travis, you just do .prop, gives me the proportion column,

[1:49:04] and then I plot that.

[1:49:06] And you can see that people really got excited about Travis around 1980, and then it sort

[1:49:12] of trailed off after that.

[1:49:13] But I mean, this actually doesn't tell the whole story, because you saw from the last

[1:49:17] plot that the diversity of names has gone up over time.

[1:49:20] So it's not the full story.

[1:49:22] Yeah?

[1:49:23] Can you actually show the number of unique names over time?

[1:49:29] No.

[1:49:30] Well, in this data set, no, because it only has the top 1,000.

[1:49:35] So actually, what I'm going to show is how many I'm going to show in a couple minutes

[1:49:39] is how to get the number of names, if you sort by the most popular names, the number

[1:49:47] of names that make up the first half of the population, and what that number is.

[1:49:53] And that's actually kind of the diversity number.

[1:49:56] That's pretty interesting.

[1:50:00] So anyway, so the point of this is that you can, given a data set, if you've got columns

[1:50:05] that uniquely identify the data, you can, using the set index function, you can add

[1:50:10] those as an index.

[1:50:12] You can see now the index contains elements that look like tuples, you know, John 1980,

[1:50:17] URM 2008.

[1:50:19] And so, you know, you could say, you know, I want the entry for John 1880.

[1:50:24] Well, that didn't quite work like I expected.

[1:50:32] So I did.

[1:50:34] Okay, so here we can, you know, just select out a single record, or if we just pass part

[1:50:42] of the, just part of the tuple, then we can select out that data set, that slice of the

[1:50:47] data.

[1:50:48] And so that's, you know, in many cases, extremely convenient.

[1:50:53] So as far as this diversity number, so one thing that you might want to do is suppose

[1:51:03] that we group by name.

[1:51:08] So the group by object, if you index into the group by object, so like you index into

[1:51:13] it like a dict.

[1:51:14] So suppose we do sub prop.

[1:51:17] So I want to explain what just happened here.

[1:51:19] So when you do sub prop, so when you create the group by, so it encapsulates, you know,

[1:51:25] say we want to group by the name column, and we do sub prop, internally it creates a new

[1:51:31] object which says we've just selected the prop column.

[1:51:34] And so when we do an operation, we're only interested in operating on that column.

[1:51:39] And so what's cool now is that we can group by name, and then we can call a function like

[1:51:43] mean, which gives the, now the mean value by name, the mean proportion by name across

[1:51:53] the data set.

[1:51:55] So this goes all the way down.

[1:51:58] So it's, again, sorted, you know, Zygmunt is in the data set.

[1:52:03] I haven't met anyone named Zachariah in a while.

[1:52:08] So you could, but then, you know, you've got this series object, and you've got methods

[1:52:11] like order.

[1:52:12] So order orders the data by the values.

[1:52:16] So you can see that the name with the highest mean proportion over the whole data set is

[1:52:22] John, and here, you know, John, James, William, Robert, Charles, et cetera.

[1:52:31] And so the idea is, you know, so you group, you select a column, you apply an aggregation

[1:52:37] operation here, dot mean, and then we can call a method like order, which is a series

[1:52:45] method that orders by values.

[1:52:50] Now there are other methods you could call.

[1:52:51] I mean, you could call median, or suppose you wanted to get like a set of summary statistics

[1:52:58] for each name.

[1:52:59] So series has a method called describe.

[1:53:04] If you call describe, then I should probably save this in two variables.

[1:53:10] I'll explain what happens.

[1:53:12] So describe isn't actually a method that is implemented on group by.

[1:53:17] It's actually a series method.

[1:53:18] So if we do boys sub prop describe, if you have SciPy installed.

[1:53:25] If you don't have SciPy installed, this probably did not work.

[1:53:31] So boys sub prop describe takes the entire array of, let me scroll up, okay, so it takes

[1:53:39] the entire array of proportions, and the describe function gives us a simple summary output

[1:53:45] of that column, gives us the mean standard deviation, and then the min, and the interquartile

[1:53:49] region, and the maximum value.

[1:53:51] So you can imagine if you wanted to call that function on each of those groups of data,

[1:53:58] even though describe isn't a method on group by, internally, whenever you call describe,

[1:54:03] it says, okay, I don't have a method called describe, but the things that I'm aggregating

[1:54:07] do.

[1:54:08] So series has a method describe, so it has a simple mechanism to invoke that method on

[1:54:14] each of the subgroups, and then glue everything together.

[1:54:17] So the result that you get out of it now is a data frame which is indexed by the unique

[1:54:22] names, and then the columns are exactly the keys that you see here.

[1:54:27] So you actually get a table output of the summary statistics for each name.

[1:54:33] So this gives you a very concise way of applying a function to groups of the data, and so you

[1:54:38] can render summary statistics like this in a very natural way.

[1:54:43] So I just did result equals, and this expression here, and now I'm just going to get the first,

[1:54:50] let's say, 50, 50, oops, I actually got to run the code, it's thinking, it's thinking,

[1:54:59] make it a little smaller, okay.

[1:55:01] And so now you can see that you've got a table, it's indexed by names here, and so this is

[1:55:09] a very concise way of getting a grouped set of summary statistics for that column grouped

[1:55:15] by some field.

[1:55:16] Of course, you could go crazy here, and you could change this to year, and then now I

[1:55:23] switch to a different grouping field, and I've got now a set of summaries by year, across

[1:55:36] the dataset grouped by year.

[1:55:38] So these numbers, so the count, so the count is the number of non-null values in the group,

[1:55:48] so the mean of the, so this is the proportion of baby names, so this is the mean, the standard

[1:55:53] deviation min, the 25% quantile, the median, the 50% quantile, 75% and max.

[1:56:01] Yeah.

[1:56:02] Mm-hmm.

[1:56:03] When you do group by, I noticed that the data frame loses columns as attributes, so I can't

[1:56:12] go group by year.proc?

[1:56:15] That's correct, yeah.

[1:56:18] I think, so the properties, the fields as attributes is, you get that, well, you get

[1:56:26] the completion in IPython, you have to inform IPython about how to complete fields on an

[1:56:31] object, so I think that's something you could definitely add.

[1:56:37] So the fields as attributes is, you just have to add, you have to add something to the get,

[1:56:43] you have to overload the get attr method, so I just haven't done it yet, but that would

[1:56:48] be, I should make...

[1:56:49] make a note of that.

[1:56:50] You'll remind me later.

[1:56:52] So the question was fields as attributes versus compare it

[1:56:56] with group by versus data frame.

[1:56:57] So you couldn't do .prop here.

[1:56:59] It'd be nice to be able to.

[1:57:03] It'd also be nice to get IPython

[1:57:04] completion help with it.

[1:57:06] So I'll make a note about that.

[1:57:10] OK, so now let's do something a little less trivial.

[1:57:15] So I was talking about the diversity of names.

[1:57:22] So let's take a single year worth of data.

[1:57:26] So let's do boys, boys, sex.

[1:57:33] Let's see, year.

[1:57:35] Boys, sex is all boy.

[1:57:37] Year equals, equals 2008.

[1:57:41] So we've got this data.

[1:57:42] So let's call this like, I'll call this df.

[1:57:48] And now what I want to do is I want to sort the data in

[1:57:52] descending order by the proportion column.

[1:57:55] And then I want to take the cumulative

[1:57:57] sum of that column.

[1:58:00] And thank you.

[1:58:02] I think Chris just told me to remind me to do that in

[1:58:06] pandas, and I will try to.

[1:58:10] So OK, so we do this, and we get the prop column.

[1:58:13] So these are all the proportions.

[1:58:16] They happen to be in descending order already, but

[1:58:19] suppose that they were not.

[1:58:21] So the method to do that is sort index by equals prop.

[1:58:27] And then ascending, the default is ascending order, so we say

[1:58:30] ascending false.

[1:58:33] So we selected out the 2008 data.

[1:58:36] And then we're saying, reorder the data

[1:58:39] frame by the prop column.

[1:58:41] And then ascending equals false means do it in

[1:58:44] descending order.

[1:58:47] So here it's in descending order already.

[1:58:48] If I'd done ascending equals true, then you can see it's

[1:58:52] now in ascending order and the maximum values at the bottom.

[1:59:00] OK, ascending.

[1:59:04] Gosh.

[1:59:07] OK, ascending false.

[1:59:10] OK, prop.

[1:59:11] Now, here's where we can see if you've been

[1:59:16] practicing NumPy.

[1:59:17] I'm going to take the cumulative sum.

[1:59:24] So the cumulative sum, it accumulates the values.

[1:59:32] And so you can see that in 2008, the top 1,000 names

[1:59:36] only represent 80%, 79.5% of the total

[1:59:41] population of babies born.

[1:59:44] And now, so we might want to say, well, how many babies, if

[1:59:50] you take the top n names, how many babies did it take if you

[1:59:55] sort in descending order?

[1:59:56] If you sort in from highest proportion to lowest

[1:59:59] proportion, how many did it take until you reached 50%?

[2:00:04] So to get that using NumPy, you call the search sorted

[2:00:07] method, and you pass 0.5.

[2:00:10] So that gives us a number, 127.

[2:00:13] And so that means that if we look at df prop cumSum, and we

[2:00:21] look at, let's say, colon 130, so the first 130 values, you

[2:00:28] can see that it crosses over into 50% at 127.

[2:00:35] So that's kind of like a measure.

[2:00:39] I'll call it a measure of diversity.

[2:00:43] Now, 0.5, so we get 127.

[2:00:47] The question is, what was that number in 1880?

[2:00:49] So how creative were people feeling in 1880?

[2:00:54] So we changed that to 1880, only 15.

[2:00:56] So if you took the top 15 most occurring names in 1880, and

[2:01:01] that was 50% of the babies born in the United States.

[2:01:04] So it'd be like, hi, John.

[2:01:06] I'm John, and you're Mike.

[2:01:08] Well, I don't know what the next top name is.

[2:01:10] We've got a room full of Roberts, and Johns, and

[2:01:13] Charles, and Georges.

[2:01:14] So people have gotten much more creative over time.

[2:01:17] But you might want to see, well, how has that creativity

[2:01:20] changed over time?

[2:01:22] So let's do that for every year.

[2:01:26] So let's package up this little function.

[2:01:29] So this is selecting out the group of data.

[2:01:31] So I'm going to call that group.

[2:01:34] And we'll do def get num.

[2:01:39] Let's see.

[2:01:40] Let's call it get quantile count.

[2:01:47] How about that?

[2:01:48] Group quantile 0.5, colon, indents, and oops, indents.

[2:01:57] Return this number.

[2:01:59] Let's change 0.5 to quantile so we can play with that

[2:02:02] number a little bit.

[2:02:05] So now, if you have that, it makes sense, right?

[2:02:09] Now we say boys group by year.

[2:02:16] And then select the prop column.

[2:02:20] No.

[2:02:21] Now all we need to do is apply get quantile count.

[2:02:31] OK, so if all goes well, I'll give you a second to type this

[2:02:37] in and get it to work.

[2:02:39] I'll have to get a sip of water.

[2:02:40] OK.

[2:02:47] So the first thing you might do here is

[2:03:10] plot this number over time.

[2:03:16] So anyway, so something interesting

[2:03:21] happened around after 1980.

[2:03:23] People, I guess, decided that my child is special and

[2:03:30] deserves a unique name.

[2:03:31] So I was born slightly after 1980.

[2:03:39] Sorry?

[2:03:40] People now don't remember how to spell.

[2:03:42] Oh, yes.

[2:03:44] That might be the case.

[2:03:47] I should probably group by the sounds like.

[2:03:51] Yes.

[2:03:52] OK.

[2:03:53] I guess I can.

[2:03:57] Let me do that.

[2:03:58] Let's have a little fun, huh?

[2:03:59] So let's do.

[2:04:09] Let's see, group.

[2:04:10] I'm going to do inside here.

[2:04:12] I'm going to group by sound x sum.

[2:04:16] OK.

[2:04:21] Yeah.

[2:04:21] Well, it's a smaller number of names, but yeah.

[2:04:24] What's that?

[2:04:28] Yeah, well, I assume that it gathers together all the

[2:04:31] different spellings of Catherine and I don't know

[2:04:34] what are names that are spelled, started to be

[2:04:38] spelled slightly different.

[2:04:39] But you can see that there's generally a trend of names,

[2:04:44] things people got more diverse until 1920.

[2:04:49] And I guess the war happened, became less diverse, and the

[2:04:52] Great Depression, and then another war.

[2:04:54] And anyway, so yeah, you can come up with a fun story for

[2:04:57] what's going on here.

[2:04:59] Really interesting is, so let's call this the boy count.

[2:05:08] I'm going to get rid of the plot.

[2:05:11] It's no fun for the boys to get all the love here, so

[2:05:14] let's do the girl count, too.

[2:05:16] Girl count.

[2:05:21] So boys, girls.

[2:05:30] So now we can do boy count dot plot.

[2:05:34] Girl count plot.

[2:05:36] And so when I put two plots like this, these are both

[2:05:38] going to go on the same matplotlib subplot.

[2:05:45] So we get a plot.

[2:05:47] We don't know which is which.

[2:05:48] So, um, I'm going to do label equals boys,

[2:05:54] boy label equals girl. Okay.

[2:06:00] I've got a call. Um, Matt pot libs, PLT dot legend.

[2:06:05] I think it's, I think I, because we were in pilot mode, we can just do legend.

[2:06:09] Yeah. Okay. Loke equals best.

[2:06:13] Okay.

[2:06:15] Got to love Matt potlib. Anyway, so this is an interesting plot.

[2:06:20] So you can see that, you know, uh, girls have always been scroll up.

[2:06:24] Sorry about that. Yeah. Yeah. Give you guys a chance to get it,

[2:06:28] get it running. Give you a second here so you can get this working in your book.

[2:06:33] I was here for strata and the, these rooms are just freezing. Um, it's,

[2:06:38] it's, it's better than, well, it's, we've got sunlight,

[2:06:40] so it's a little warmer here. But, um, the, uh, you know,

[2:06:44] the sunlight lists, uh, conference rooms are really cold. So bring your parkas.

[2:06:50] Um, just, just, uh, you know, you'll thank me later.

[2:06:57] The question was how would you pass a different value for quantile? Um,

[2:07:02] and so,

[2:07:04] so what we would do here is what I would do is say create F because I have not

[2:07:09] very creative. I would have been more down here. Um,

[2:07:14] so I'll just create a little Lambda. So Lambda, uh,

[2:07:19] group.

[2:07:25] Yeah, you could use functuals dot partial. Um, I like writing a little Lambda,

[2:07:29] so I'm just going to say, you know, get, get quantile count Lambda, uh,

[2:07:33] to get Lambda group, get, let's call it X, get quantile group,

[2:07:37] get quantile count X, and then like a different quantile, like 0.1.

[2:07:45] Oh, that's a good point. Actually. Thanks.

[2:07:48] Quantile equals Q and I'll define Q so you can pass additional arguments and

[2:07:54] keyword arguments to apply. So if we wanted to just look at the top,

[2:07:59] you know, 25%, um,

[2:08:02] um, you can see it's a, it's a more,

[2:08:05] it's a more jagged plot because you know, it's the same number over,

[2:08:09] over time. But, uh, yeah.

[2:08:16] So, so that's an interesting little study. Um,

[2:08:19] so the last thing that I want to do, um,

[2:08:24] one of the last things that I want to do is, uh,

[2:08:26] well two things I want to do before we move on to the next data set.

[2:08:29] Okay. How are we doing on time? Oh, we've got an hour,

[2:08:33] more than an hour left. Wonderful.

[2:08:37] So, so this is one, one way to look at, you know, sort of to look at diversity.

[2:08:42] Um, another question might be, you know, given that,

[2:08:45] given that names are becoming more and more diverse,

[2:08:47] you might want to say given a particular name like your own name, um,

[2:08:51] just want to know what's the rank of your name in every year.

[2:08:55] That's kind of like, you know, uh, a different sort of measure.

[2:08:58] It's like I'm, you know, I'm the 50 most, uh,

[2:09:01] my name Wes is not very popular, so I do appear in the list many years,

[2:09:05] but it's definitely not, not very high. Um, but you know,

[2:09:09] actually getting that number, like what's, you know,

[2:09:11] my number through one in a thousand, um, at least in the United States,

[2:09:16] most among the most popular names. So I'll show you how we can do,

[2:09:19] we could carry out that analysis and that you'd get to see,

[2:09:21] get to learn a new function on series. So, so again,

[2:09:25] let's look at boys, uh,

[2:09:29] year equals equals 2008 and let's look at the prop column.

[2:09:36] Okay. So, so series has a method rank.

[2:09:43] Um, so if you call rank on a series,

[2:09:46] it gives you a number from a well one to a thousand,

[2:09:51] but it's a, whenever there's a tie,

[2:09:54] it assigns the, um,

[2:09:57] the number that it gives is the mean of the, the ranks among that group.

[2:10:01] So I don't know, I can look back at the proportion here with the,

[2:10:05] what those values actually were. So you can see the,

[2:10:08] the last four values were, you know, some minuscule, you know,

[2:10:12] 0.00089 and so they all got assigned the same, the same rank value.

[2:10:17] Um, so there are many different, you know, tie breaking schemes you can do,

[2:10:21] you can use when, when ranking, ranking values, but here it just does the mean,

[2:10:25] the mean rank, um, by default. Um, so,

[2:10:31] so what we might want to do is take, take the, so take the data set.

[2:10:35] So we've got, um, we've got names,

[2:10:38] we've got years and we want to rank the proportions within each year.

[2:10:44] And so then once we do that,

[2:10:46] we can select out any subset of the names that we want and look at their,

[2:10:50] their rank over time. So show you what that might look like.

[2:10:57] So again, so let's group by

[2:11:04] group by year

[2:11:07] and then let's select prop and then let's just call its rank function.

[2:11:16] Okay. Oh gosh, that didn't do quite what I expected.

[2:11:23] Uh,

[2:11:27] you can tell I haven't done this before actually.

[2:11:33] Okay. So, oops.

[2:11:44] Why is this lying to me?

[2:11:47] Okay. Group by year.

[2:11:51] I'm going to do two things and I'm going to explain what I did before and why it

[2:11:54] didn't do the thing that I expected. Um, so here let's,

[2:12:00] so we select the, select the prop field from, you know, we're grouped by years.

[2:12:05] Oh, prop is not going to work. It will work after I,

[2:12:09] after I roll up my sleeves later tonight. Um, so we select out, um,

[2:12:14] the prop column and now we want to,

[2:12:17] to transform each group of the data. Uh,

[2:12:21] and I'm going to hope that this works and I'm going to pass the series rank

[2:12:24] function. So, um, so the difference between, uh,

[2:12:29] transform and apply in this case is that transform is extremely rigid.

[2:12:35] Um, so it, it, it's going to, you know, look at a subgroup of the data,

[2:12:39] call the function on it,

[2:12:40] but it requires that the result be the exact same size as the thing that it,

[2:12:45] that it, that it took. So in the case of, of ranking, if we take, you know,

[2:12:49] just the proportions for that year, we call rank on it. If it was,

[2:12:52] it was a length 1000 before the ranks, you get back as length 1000.

[2:12:56] So it's going to plug those new values into the, into the result.

[2:13:02] And so you can see now you get a one dimensional array

[2:13:06] right?

[2:13:08] Which has now the same labels as the, as the boys data frame,

[2:13:13] which were not, not all that interesting. They're just integers.

[2:13:16] So now we can take this transformed results.

[2:13:19] We've now taken the ranks within year of the proportions and we can assign that

[2:13:26] to the, uh, to the data frame.

[2:13:30] Let's call it your rank.

[2:13:37] Okay.

[2:13:39] Oh, not equals, equals, equals. Okay.

[2:13:43] And so now we have, so you've transformed the data,

[2:13:47] taken the ranks within groups, and now we've got an additional column which has,

[2:13:53] uh, which has the, the ranks of each name within, within each year.

[2:13:58] And so now, I mean, you know, pretty much, uh, you can do,

[2:14:02] you can pretty much do whatever you want. So, you know,

[2:14:05] we could select out, uh, let me do,

[2:14:14] well, let's just select out a single name.

[2:14:15] So let's look at the rank of Wes over time. So let's do year, uh,

[2:14:20] name.

[2:14:26] So Nate boys name equals Wesley.

[2:14:32] Pretty sure it's Wesley and not Wes. That's my real name.

[2:14:37] And then we can, uh, oops.

[2:14:45] So let's plot the, select out the Wesley data,

[2:14:48] plot the year rank column.

[2:14:53] So it looks like Wesley was never very popular.

[2:14:59] These are ranks, so it's a, well, the x-axis doesn't have

[2:15:05] the date, so I was just going to mention that.

[2:15:07] So in these other plots that we've seen, we had the result

[2:15:11] of the group by actually set the index to be the unique

[2:15:16] groups, which happened to be the years in most of these

[2:15:19] examples.

[2:15:23] So in this case, if we wanted to do this, let's do something

[2:15:27] a little different.

[2:15:28] Let's go back.

[2:15:28] Remember our setIndex function?

[2:15:31] So let's do setIndex, and let's do name year.

[2:15:39] And so, oops, let's call this cursor failing.

[2:15:51] So if we do setIndex, so we set the index of the data

[2:15:54] frame to be name and year.

[2:15:57] So now we get entries again, like name, comma, year.

[2:16:01] I can then do .ix, select out the Wesley group, and now I

[2:16:05] get something that's indexed by year.

[2:16:07] And I can select out the year rank column and plot that.

[2:16:13] So now we get the years on the plot.

[2:16:16] So if you didn't want to set the index, what you could do

[2:16:19] is you could just use the matplotlib plot function and

[2:16:22] explicitly pass the array of years and the array of values.

[2:16:28] But it's convenient to be able to do it all just

[2:16:32] using the dot plot.

[2:16:36] And so I think that these ranks are in ascending order.

[2:16:38] So this just means that Wesley got really less popular

[2:16:42] around the time that I was named that, and then it's

[2:16:44] become a slightly more popular.

[2:16:46] But rank 820 out of 1,000 is nothing to write home about.

[2:17:01] Wesley?

[2:17:03] Wesley.

[2:17:03] Did you explain why transform by series rank resulted in

[2:17:10] something of length 149,000 rather than 129?

[2:17:13] It seems like when you group it, it's less intuitive.

[2:17:19] Yeah, so the question is, why is the result of transform

[2:17:25] length 129,000 versus length 129?

[2:17:29] Basically, why didn't it change the

[2:17:32] size of the data set?

[2:17:35] And so the idea is that transform is a function which

[2:17:38] is intended to mutate the values within a group.

[2:17:42] So suppose that we did transform and we passed lambda

[2:17:46] x, where x is now a group of data, and we did x times 2.

[2:17:51] So we wanted to multiply the values within a group by 2.

[2:17:56] That's very trivial, because you could just do

[2:17:59] that column times 2.

[2:18:00] Suppose we wanted to subtract the mean value within group to

[2:18:06] center each group.

[2:18:07] So then we could do lambda x, x minus x dot mean.

[2:18:11] And so that has the effect of centering the values around

[2:18:15] the mean within each group.

[2:18:18] And so you could use either transform or apply to do that.

[2:18:26] But transform is higher performance.

[2:18:29] And it's just very rigid.

[2:18:31] If you were to pass, so I could do this.

[2:18:35] And you can see that it computes.

[2:18:38] I could prove that it actually works by doing result group by

[2:18:43] year mean.

[2:18:45] And so we should see that.

[2:18:57] Oh, well, it's a series as a result.

[2:19:01] Because see, I selected out the prop column.

[2:19:04] And then when I transformed it, I get a series out.

[2:19:07] And so I tried to group by year.

[2:19:08] And it's no longer a data frame.

[2:19:10] So if I did boys dot, if I grouped by boys dot year here,

[2:19:14] actually passed the array of values and mean, you can see

[2:19:17] the group means are all now 0.

[2:19:19] So that's what happened in the transform.

[2:19:23] I could also have done apply.

[2:19:29] And the result is exactly the same in apply.

[2:19:32] But apply is, if you look at the implementation,

[2:19:35] is very general.

[2:19:37] And we could, I'm morbidly curious in what's the

[2:19:41] difference in run time.

[2:19:42] So if you don't mind me sort of figuring out, if I do

[2:19:49] percent time it on the apply version.

[2:19:52] And I don't know if you guys have figured out yet that I

[2:19:56] spend a lot of time thinking about performance.

[2:20:07] Why didn't that copy?

[2:20:14] Sorry, fellas.

[2:20:15] What's up?

[2:20:18] Chrome, Chrome betrayed me.

[2:20:19] It got rid of my scroll bars right in

[2:20:21] the middle of a demo.

[2:20:25] This is the wrong thing.

[2:20:25] I'm supposed to do transform here.

[2:20:28] My bet is that transform is about five times faster.

[2:20:37] Slower.

[2:20:38] Oh, boo, boo, boo, boo.

[2:20:43] What's that?

[2:20:44] Wrong way around.

[2:20:45] Yeah, it's actually three times slower.

[2:20:47] So the transform method actually, does it end up

[2:20:50] ultimately duplicating the data and memory?

[2:20:52] Or is it just reading through the indexes?

[2:20:54] So the question is, does transform duplicate

[2:21:01] the data and memory?

[2:21:03] So what it does is it allocates a new array.

[2:21:07] And it takes each subgroup.

[2:21:08] And it assigns into that the transformed values.

[2:21:12] And then it returns that to you.

[2:21:14] Yeah.

[2:21:15] AUDIENCE MEMBER 2 Do you have any optimizations of the

[2:21:16] sparseness in that?

[2:21:19] You have like a fairly sparse figure.

[2:21:23] I don't.

[2:21:23] I mean, I'd be interested in that sort of thing, though.

[2:21:26] Yeah.

[2:21:29] OK, so one last thing let's do before we switch gears to the

[2:21:37] election data, which is pretty fun and we'll do some fun

[2:21:39] stuff with, is that let's do read CSV.

[2:21:43] And I also gave you a file called births.csv, which

[2:21:48] contains the number of boy births and

[2:21:52] girl births by year.

[2:21:58] So save that into a variable births.

[2:22:02] Let me make some empty cells so I can scroll this up so you

[2:22:06] can see.

[2:22:08] So if we looked at this data set, and we go back to the

[2:22:19] names data set, you can see that we have the proportion of

[2:22:26] names in that year, but not the actual number of people.

[2:22:30] So if you wanted to know the total number of Johns born

[2:22:32] since 1880, then you wouldn't be able to figure that out.

[2:22:36] Because there are a lot more people now

[2:22:38] than there used to be.

[2:22:40] So first example of doing a join operation.

[2:22:44] So the pandas function for doing joins is called merge.

[2:22:48] So if you've used R, then this will be

[2:22:51] somewhat familiar to you.

[2:22:52] So it has, I can't make this bigger.

[2:22:55] I can't move this up.

[2:22:58] Move it up here.

[2:22:59] OK, great.

[2:23:02] You guys over there can see it.

[2:23:04] So merge takes a lot of options.

[2:23:06] So the idea is that merge can do any of the joins that you

[2:23:10] would do in a SQL database.

[2:23:12] So you pass two data frames.

[2:23:14] You say the join style that you want to do, whether an

[2:23:16] inner, which is going to intersect the keys, outer,

[2:23:19] which unions the keys, left or right, which takes the keys in

[2:23:22] the left or the right data frames.

[2:23:24] You can pass a list of columns to join on.

[2:23:27] If you pass a list of columns to join on, they have to be

[2:23:29] common to the data frames.

[2:23:32] If you have different columns that you want to join on,

[2:23:34] there's left on and right on fields.

[2:23:36] You can also join on the indexes.

[2:23:38] So I can show you an example of that if you're interested.

[2:23:43] So you have a lot of options.

[2:23:43] But it's basically just to span the gamut of merging

[2:23:47] routines that you'd want to perform.

[2:23:48] form on data frames.

[2:23:50] It happens to be, in this case, that the merge that we

[2:23:53] want to do is extremely simple because we

[2:23:57] just have year and sex.

[2:24:01] And that's going to be the join key.

[2:24:03] So we've got that field year and sex in both data frames.

[2:24:08] So to join them together, we say merge names comma births.

[2:24:16] And then we say on year and sex.

[2:24:22] And so that's it, actually.

[2:24:25] So if you run that, then it did a merge operation.

[2:24:30] It aligned.

[2:24:32] This can do many-to-many, many-to-one, one-to-one

[2:24:34] merges.

[2:24:35] So if you've done SQL, the full gamut, turns out that

[2:24:40] many people who use SQL don't understand

[2:24:42] many-to-many joins.

[2:24:43] So it does them.

[2:24:45] And use at your own risk.

[2:24:48] So many-to-many joins actually compute the Cartesian product

[2:24:53] of the duplicated keys.

[2:24:55] So I actually didn't know that for a long time, to make a

[2:24:58] full admission.

[2:25:02] So anyway, so we merged this.

[2:25:04] Hopefully this worked for you.

[2:25:06] It happens to be, in this case, that if you don't specify

[2:25:10] the merge keys, that it uses the intersection of the

[2:25:14] columns as the merge key.

[2:25:16] So in this special case, we could have

[2:25:18] omitted year and sex.

[2:25:20] And it would merge on the common set of columns and give

[2:25:24] you the exact same result, which is kind of nice.

[2:25:27] So I'll leave it there for now.

[2:25:29] And let's call this merged.

[2:25:31] And so now we can, if we wanted to get the total number

[2:25:37] of people named each name, it's just like before.

[2:25:40] Well, we've got to actually add the number of persons.

[2:25:42] So let's do merged persons equals merged prop times

[2:25:51] merged births.

[2:25:56] And then call numpy floor on it, because it's

[2:25:59] going to be a decimal number.

[2:26:03] So just to truncate off the decimal part of it.

[2:26:06] So let's take a look at what this looks like, merged.head.

[2:26:13] So we took proportion times births.

[2:26:14] We floored it, which just basically moves it down to the

[2:26:18] nearest integer less than or equal to the

[2:26:20] number that you get.

[2:26:22] And so then we get approximately the number of

[2:26:24] people named each name.

[2:26:26] Approximately the number of people who were born.

[2:26:29] There were 9,600 Johns born in 1880.

[2:26:35] And so now you can kind of slice and dice the way that

[2:26:39] you want to.

[2:26:40] So if you want to group by name and sex, and then take

[2:26:53] the sum of the persons.

[2:26:57] Not dot.

[2:26:58] You can see my fingers want to type dot, but I can't.

[2:27:03] So we group by name and sex, because there are Wesleys who

[2:27:10] are girls, I think.

[2:27:13] I don't know how popular a name that is.

[2:27:14] There are many boy girl names.

[2:27:16] I think Leslie at one point was a boy's name, then became a

[2:27:20] girl's name.

[2:27:22] Same is also true of Hadley.

[2:27:23] See if any of you know Hadley Wickham of R package fame.

[2:27:28] I got this data set from him, and he told me he was a bit

[2:27:30] saddened to find that Hadley has become a girl's name.

[2:27:36] Anyway, so we group by name, sex, persons, and sum.

[2:27:42] And this gives us, at least within the context of the

[2:27:45] data set, for each name, sex combination, the

[2:27:48] total number of births.

[2:27:53] AUDIENCE MEMBER 3.

[2:27:54] The number of births in 1965.

[2:27:57] Which one?

[2:27:59] It's a hierarchical label.

[2:28:00] It's a hierarchical labeling.

[2:28:01] So this means that there are, so this is Aaron, and this is

[2:28:06] also Aaron.

[2:28:08] And so this is, I guess, there are a certain number of girls

[2:28:10] named Aaron.

[2:28:13] And so then we could order this to get the most popular

[2:28:23] names in the whole sample.

[2:28:25] So you can see that actually, James edged out John by an

[2:28:30] inch, only 5,000 people.

[2:28:33] And that the most popular girl's name over the whole

[2:28:35] sample is Mary.

[2:28:37] So.

[2:28:41] OK, so that's all I have for this data set.

[2:28:43] And if you find fun things to do with it, I'll be happy to

[2:28:46] hear from you.

[2:28:46] Do any of you have any questions or things about this

[2:28:49] particular data or things that we've looked at?

[2:28:53] Sure.

[2:28:53] AUDIENCE MEMBER 4.

[2:28:54] When you do merge the key person, do you get just to

[2:28:58] retribute persons to sign the thing that didn't exist

[2:29:01] before?

[2:29:03] Sorry, could you say that again?

[2:29:04] AUDIENCE MEMBER 4.

[2:29:05] When you made that merge to dot persons.

[2:29:08] Well, if I change this to merge dot persons.

[2:29:10] AUDIENCE MEMBER 4.

[2:29:11] Right.

[2:29:11] If it didn't exist before, you can do that?

[2:29:14] You actually can't.

[2:29:15] So yeah, that's actually one thing I've thought about.

[2:29:18] But selecting columns by attributes is there, but

[2:29:25] setting is not.

[2:29:30] It's another feature that I've debated.

[2:29:32] The question was whether you can assign by attribute.

[2:29:37] And the answer is that you cannot at the moment.

[2:29:39] AUDIENCE MEMBER 5.

[2:29:39] But if it's already there?

[2:29:41] No, you cannot.

[2:29:42] You cannot assign if it's in any case, which may cause a

[2:29:47] bit of cognitive dissonance.

[2:29:50] My inference principle is if it's there, I would think

[2:29:52] that you should be able to assign to it.

[2:29:53] But there are cases where people do assign attributes to

[2:29:56] a data frame, and they don't.

[2:29:59] So if you implement that, you would no longer be able to

[2:30:06] attach new attributes to the object.

[2:30:09] So I think that's the reason why I haven't done it yet.

[2:30:21] So save this.

[2:30:30] And we'll go back to the dashboard.

[2:30:35] And I need to use the restroom.

[2:30:37] So you get a two-minute break while I do that.

[2:30:44] Anyone come up with any questions while I was on my

[2:30:47] short break?

[2:30:49] Yes?

[2:30:51] So a graph, how many people had a particular name?

[2:30:56] So the number of people rather than the percentage.

[2:30:59] So the number of people who had a particular name?

[2:31:03] Rather than a certain per year.

[2:31:06] Yeah, OK.

[2:31:08] Well, so you've got the merged data frame.

[2:31:14] So I guess probably the easiest way is so you would

[2:31:17] just index this by.

[2:31:21] OK, let me do something a little less trivial, so

[2:31:26] something I haven't showed you yet.

[2:31:28] So we've got this merged data frame.

[2:31:30] We created a column that is the number of

[2:31:33] people born on each year.

[2:31:35] So I'm going to index this by year and name.

[2:31:45] So I call setIndex yearName.

[2:31:47] That takes the year and the name columns, and it moves

[2:31:49] them into the index in a new object.

[2:31:53] Let's call this IDF.

[2:31:56] And then I'm only really interested in

[2:31:57] the persons column.

[2:31:59] Let's do .persons.

[2:32:01] It's tidier, I guess.

[2:32:05] Oh, that's lovely.

[2:32:09] It appears that I need, I only care about the boys for now.

[2:32:14] So I'm going to do mBoys equals merge boys births join.

[2:32:27] It's interjoined by default.

[2:32:28] So I'm going to merge the boys with the births data.

[2:32:33] And then I'm going to call setIndex, because the problem

[2:32:35] is there are names that are shared between sexes.

[2:32:39] So then I'm going to call mBoys setIndex and index it by

[2:32:44] year and name, and then select the number of.

[2:32:47] Persons. Looks like it didn't like that. Oh, cause I haven't added a birth.

[2:32:51] So emboys, persons,

[2:32:56] floor, numpy floor,

[2:32:58] emboys prop times emboys births.

[2:33:04] Okay. Sweet.

[2:33:08] Uh, persons. Okay.

[2:33:12] Okay.

[2:33:14] Make some cells. Okay.

[2:33:17] So, so now this, this thing that I've got here,

[2:33:21] so I've created an index of year and name.

[2:33:24] So that creates a hierarchical index on the rows of the data frame.

[2:33:28] And then I selected out the person's column.

[2:33:30] So the object that I get back is a series. Uh, so it's one dimensional.

[2:33:36] It has a hierarchical index.

[2:33:38] And now I'm interested in, in having, you know,

[2:33:43] being able to, so I could use, I could use the, uh, you know,

[2:33:46] the IX feature here.

[2:33:47] So suppose that I wanted to select out all of the people named Christopher like

[2:33:52] Mr. Chris Withers here. Um,

[2:33:54] so I could do dot IX colon comma Christopher and then select out sort of data

[2:34:00] from the inner group. So the number of, uh,

[2:34:03] so this is the number of people, uh, you know,

[2:34:08] so I could just do plot kind equals bar.

[2:34:12] Well, this is going to be a really crowded map.

[2:34:13] Paul had a plot, uh, wrote 90. Um,

[2:34:19] well, it's very crowded because Matt Paula just does not a handle, you know,

[2:34:22] 130, uh, axis X ticks, but you can see, you get a little bit of a graph,

[2:34:27] you know, tons of Chris's and then fewer Chris's nowadays.

[2:34:31] So I guess they got tired of you.

[2:34:33] Yeah.

[2:34:39] So this is actually a lot of typing and it might be that you want to do more

[2:34:43] analysis by name by name on the number of persons group by year.

[2:34:49] So whenever you have something that is hierarchically indexed like this,

[2:34:52] so a method that I haven't shown you yet is so you can imagine that this one

[2:34:57] dimensional object is really a representation of a two dimensional object.

[2:35:01] Imagine you had a data frame which had one column per name and the index are

[2:35:06] the years. So you can actually get that very easily from here. Uh,

[2:35:11] and the method to do that is called unstack. So you say unstack and then you pass,

[2:35:16] you pass name. And so, you know, in your, in your,

[2:35:21] in your head,

[2:35:21] what you can think about is that you selecting this name column and you're sort

[2:35:25] of pivoting it up into the columns.

[2:35:27] And so it's going to take the union of all the names that it sees in the column

[2:35:32] in the, in this level of the index.

[2:35:34] And it's going to create a data frame whose columns are those unique values.

[2:35:39] And then the, the year index that you would expect on the data frame,

[2:35:43] the row labels would be the unique years. So,

[2:35:49] um,

[2:35:50] it's actually a rather big object because of the number of unique names

[2:35:55] observed. And so you can see it does exactly that.

[2:35:57] And it gives us a summary view of the data frame. It says the year,

[2:36:00] the index is now goes from 1880 through 2008 and we've got a column for each a

[2:36:06] unique name observed in the data set. So if you wanted to see like,

[2:36:12] uh, I'm going to go down to the next cell result equals underscore.

[2:36:19] So underscore and I Python is the,

[2:36:21] the output of the last statement that you entered cause I don't want to compute

[2:36:24] that thing again.

[2:36:26] Okay. So, um,

[2:36:31] we can look at that thing and suppose we selected out Wesley,

[2:36:35] like the number of Wesley's by year. And so now we, you know, very simple,

[2:36:38] select out a column, the Wesley's by year. Uh,

[2:36:41] we can plot that and you can, again, you get the number of people that,

[2:36:45] you know, there's just a really gangbuster, uh, Wesley year and like 1978 or

[2:36:50] something. So, yeah. Um, anyway, so that's,

[2:36:54] so that's one way to get at that. Okay. So, uh,

[2:36:58] I have about 33 minutes left to melt your faces off. So, uh, so let's,

[2:37:03] let's go onward to the, uh, click, go back to the, I Python dashboard and,

[2:37:08] um, and click on the election data, uh,

[2:37:12] the election data file, uh, notebook

[2:37:17] and you should see something that looks about like this.

[2:37:19] I'm going to make it a little bigger. Okay.

[2:37:25] Okay. Everyone, everyone good to go. Cool. Okay.

[2:37:30] Um, so I'm about to,

[2:37:31] I'm going to close keynote because I'm about to use a lot of memory. Um,

[2:37:35] so there might be some people in the room that won't be able to load this data

[2:37:37] set because of all the other processes that you have running on your machine.

[2:37:40] I think it takes about half a gigabyte. So, um,

[2:37:43] I probably should have down sampled it to like something a little tidier,

[2:37:46] but with any luck, um, you know,

[2:37:50] you try it out on a, on, on bigger iron or if you can't get it to load,

[2:37:54] then, um, so anyway, so what I've got here, I've just, I've got some imports. Um,

[2:37:58] I've got a little months dictionary because the data requires a little bit of

[2:38:01] cleaning. Um, and then I've got addictive party affiliations for,

[2:38:08] uh, for each of the Republican Democrat. Uh, I think there's,

[2:38:12] I think Gary Johnson was running as a liberal Republican and now he's running as

[2:38:16] libertarian. So I put libertarian. Um,

[2:38:20] okay. So the data set, if you can download this from the,

[2:38:23] the US government, uh, federal election commission, it extracts to this giant,

[2:38:28] uh, CSV file P I don't know why they named it.

[2:38:32] This is P zero zero zero all Ted dot text. Um,

[2:38:37] so run this, throw in this top cell and then we'll run the, uh,

[2:38:43] read CSV on that guy and you cross your fingers that your machine doesn't blow

[2:38:47] up. Okay.

[2:38:52] Okay. So with any luck, how many of you know,

[2:38:56] how many of you were able to load this data set? All right, sweet. Excellent.

[2:39:01] Okay. So, so let me explain what's in this data set and make this a little

[2:39:04] bigger. Okay. So, so this is the summary view of the data frame.

[2:39:08] So it tells us, you know, the number of columns of each type.

[2:39:11] So most of these are string columns which go through as object, uh,

[2:39:15] object D type columns in, in, uh, in the data frame.

[2:39:19] And so we've got the things that we really care about are the candidate name,

[2:39:23] um, the contributor state, the zip code.

[2:39:26] Maybe I was thinking it'd be cool to make like a,

[2:39:28] if anyone wants to make like a, you know, sprint day,

[2:39:30] put together like an interactive viz of you could get like a map.

[2:39:34] You can imagine having like an interactive map where it gives you like big

[2:39:37] dots,

[2:39:37] like where the money was coming from and you could drill down into states and

[2:39:40] that would be really cool. And you could do that with this data set. Um,

[2:39:44] probably see something you would see on like New York times.

[2:39:46] Use like D three or one of those cool plotting toolkits.

[2:39:50] So you've got the zip codes, employer occupation.

[2:39:54] The receipt amount is the amount that they contributed and the date, um,

[2:39:58] in which they contributed it.

[2:39:59] And then there's some extra metadata that we don't really care about. Um, so,

[2:40:05] so the first thing that I, uh, that I noticed here is there's no party column.

[2:40:08] So if you want it to aggregate by, you know,

[2:40:10] how much money is going into Republican versus Democrats. I mean, Democrats,

[2:40:13] it's all Barack Obama, but, uh, you know, we've got all these, you know,

[2:40:18] just motley crew of Republican candidates. Um, I'm from Ohio. And, uh,

[2:40:23] so yesterday kind of made me ashamed to be in Ohio and, but, uh,

[2:40:28] I don't want this to get all political. Um, pardon me for going there.

[2:40:33] I'm sorry.

[2:40:44] Okay. So, um,

[2:40:49] so the, so the candidate name column. Okay. So we get, uh,

[2:40:54] it gives us a, an array of, of candidate names, you know,

[2:40:57] Michelle Bachman through Rick Perry. And separately we've got, I've got,

[2:41:01] I've given you a control ma inserts above, um,

[2:41:05] giving you a dict of parties. So, you know,

[2:41:09] it's pretty clear what needs to happen here.

[2:41:10] So you've got an array of values and you've got an array of core, you know,

[2:41:14] I've got a correspondence between names and parties.

[2:41:17] So what you really want to do is, you know,

[2:41:20] the first step that you might do is to call, is to say, you know, do,

[2:41:24] just write a, um, a list comprehension like parties X for X in candidate name.

[2:41:32] And that's, there's nothing wrong with that. And, you know,

[2:41:35] I fully advocate writing code that looks just like that. So,

[2:41:39] but if you want to be, if you want to be extra fancy, um,

[2:41:43] series has a method called map and I can pass.

[2:41:47] the party's dict to the map.

[2:41:49] And what's cool about map is it can be a dict,

[2:41:51] it can be a function, it can be another series.

[2:41:53] So anything in Python which describes

[2:41:56] like a correspondence between values.

[2:41:59] And so you call that map function

[2:42:00] and now you get an array of party affiliations.

[2:42:03] So let's go ahead and set that

[2:42:06] into our friendly data frame, party.

[2:42:11] So fec party equals fec can't name dot map.

[2:42:18] I was about to make a joke about feckless politicians

[2:42:23] but I won't do it.

[2:42:25] Wait, I did, sorry.

[2:42:28] So this, so now we've got a party, a party column.

[2:42:36] So suppose, so this data frame contains a donation record.

[2:42:39] So if you look at, let's say we do dot IX zero.

[2:42:43] A single record you can look at,

[2:42:46] just do dot IX zero, that gives us the first row.

[2:42:48] So you can see a single record has the person,

[2:42:51] where they are, what their occupation is,

[2:42:54] the date that they made it,

[2:42:55] and the party and the party affiliation.

[2:42:57] So one useful summary statistic,

[2:43:01] easy summary statistic on data like this

[2:43:04] is if we take the party column,

[2:43:06] it's a series now and it has a method called value counts

[2:43:10] which gives you a histogram of a series.

[2:43:14] So you can actually see here

[2:43:15] the number of donation records by political party.

[2:43:21] So, you know, so you get, you know,

[2:43:24] Barack Obama's had the most, you know,

[2:43:26] individual number of contributions

[2:43:27] and so the Republicans and all that.

[2:43:30] And so this by default sorts in descending order.

[2:43:32] So it's been, you know, like I wrote this method

[2:43:36] and then I was like, wait, wait, wait,

[2:43:37] how many times have people needed to do this

[2:43:39] using NumPy arrays?

[2:43:40] And, you know, just think about the code

[2:43:43] that you might write to compute this in NumPy.

[2:43:46] And it would probably be slow

[2:43:51] because you would first have to call unique on,

[2:43:54] I mean, you could do it.

[2:43:55] You could call, you know, unique on fec party.

[2:44:00] And then you could iterate

[2:44:01] through each of those unique values,

[2:44:03] select out the subset of the data

[2:44:04] and then compute the length.

[2:44:06] But it's nice being able to have like a high level way

[2:44:08] to do that.

[2:44:10] So we can go from there and then, you know,

[2:44:14] it's of course very easy, you know,

[2:44:16] given what I've already showed you to do things like,

[2:44:19] you know, group by, you know, group by party

[2:44:21] and then you can select the, well,

[2:44:24] it sure made these fields easy to type.

[2:44:27] Contributor receipt amount, you know, sum.

[2:44:30] So you can get the total amount contributed to,

[2:44:37] contributed to each of the parties

[2:44:39] over the whole sample.

[2:44:40] So you can see the Republicans have raised more money

[2:44:42] and Barack Obama is not really all that shocking.

[2:44:46] But suppose that we wanted to get a graph

[2:44:49] of the donations over time.

[2:44:51] So we augment the group by to do group by party

[2:44:55] and oh gosh, what is it called?

[2:45:00] Contribute receipt DT.

[2:45:03] Okay, so we group by party and date

[2:45:14] and then we take the, we want to aggregate the amount.

[2:45:16] We call it sum method and so that gives us

[2:45:19] a aggregated amount but we see, oh no,

[2:45:24] this is actually is not a Python date time object.

[2:45:26] So if you try to plot this, like it's gonna look awful.

[2:45:28] Don't even try.

[2:45:30] So, all right, so let's go up here and fix that

[2:45:35] right there, right then and there.

[2:45:37] So if we look at contributor receipt date,

[2:45:41] you can see that each of these is a Python string, okay?

[2:45:50] And we'll see if you're all still awake.

[2:45:53] So I gave you a dict of months, print months.

[2:45:59] So maybe take two minutes and write a function

[2:46:04] that converts a date that looks like this

[2:46:06] into a Python date time and then we'll apply that

[2:46:11] to the column and convert it.

[2:46:12] I'm not gonna spoil it for you.

[2:46:17] I did say this was an experienced tutorial, right?

[2:46:30] You could just use date util parser

[2:46:34] but that would be no fun.

[2:46:59] What's that?

[2:47:13] Yeah.

[2:47:30] You don't need to, you only need to do it

[2:47:34] for a single date.

[2:47:36] So you don't need to fix the column yet.

[2:47:45] I'll give you one more minute.

[2:48:59] Yeah.

[2:49:17] Yeah, I could use date.

[2:49:18] I'll just use date time in this case.

[2:49:21] Yeah, it doesn't matter that much.

[2:49:24] I don't have date imported, I only have date time imported.

[2:49:27] Okay, so, what's that?

[2:49:36] What's Y3K?

[2:49:41] Oh, yeah, well I hope they, the question is,

[2:49:46] being Y3K compliant and concatenating two zero on here.

[2:49:52] Hopefully by then the election committee

[2:49:53] will put the full.

[2:49:57] Be like, gosh, we should have, you know,

[2:49:58] if only we thought, you know, 900 years in the past,

[2:50:02] gosh, you know, it's all this data, you know,

[2:50:04] it's gonna be digitized for forever and ever

[2:50:06] and we're gonna come back to it

[2:50:07] and somebody somewhere is gonna be like,

[2:50:09] getting the, you know, forget to that

[2:50:11] it's actually the wrong millennium, so.

[2:50:14] Anyway, okay, so hopefully you have something like this.

[2:50:19] So if you do the contribute receipt date,

[2:50:27] so now we get this array of strings

[2:50:29] and we can just map this convert date function onto it

[2:50:33] and so you can see that that now produces

[2:50:37] a series with the same index of date times

[2:50:41] and so we can just assign contribute receipt date.

[2:50:46] And I wish.

[2:50:47] That was a dot, and I could tab complete it.

[2:50:49] That would make me so much happier.

[2:50:57] So we do that, and hopefully that worked.

[2:51:00] If not, no big deal.

[2:51:02] So now we've got amounts by date.

[2:51:06] And let me save this into by date.

[2:51:17] So by date.

[2:51:19] And now we might want to get a cumulative sum over time.

[2:51:23] But you can see now, see I did group by with two keys, so I

[2:51:27] get a series that is indexed by the unique values of the two

[2:51:30] keys in a hierarchical index.

[2:51:32] So what I'm going to do is unstack the party, which now

[2:51:36] gives me, pivots up the party level into the

[2:51:42] columns of the data frame.

[2:51:43] So now I get a data frame of dates and indexed by, the

[2:51:51] index is dates, the columns are political parties.

[2:51:55] And I can do something like cum sum.

[2:51:58] So to give you the cumulative sum contributed to each

[2:52:01] political party over time, and then plot that.

[2:52:04] So then we get a, make this a little smaller I guess.

[2:52:10] And so now you can see that here, I guess, the blue line,

[2:52:16] the darker blue line is Democrats with Barack Obama.

[2:52:19] You can see around summer of last year, I guess,

[2:52:23] Republican donations really picked up.

[2:52:25] And you see how, of course, the other parties are just a

[2:52:28] little smidgen.

[2:52:29] But yeah, that's cool.

[2:52:31] So you get this nice summary of the data without doing a

[2:52:37] great deal of work.

[2:52:38] Now there's lots of other interesting things that we

[2:52:40] might want to do with this data.

[2:52:41] Suppose that we wanted to get.

[2:52:42] AUDIENCE MEMBER 2 Can you scroll up just for 15 seconds?

[2:52:46] Sorry about that.

[2:52:54] Can you repeat what unstacking does?

[2:52:56] Yeah, so unstacking, let me, well as soon as it's been 15

[2:53:03] seconds I will.

[2:53:04] Yeah, OK, so unstacking, let me take this, by date, OK,

[2:53:21] so let me do, OK.

[2:53:26] So here's like a little tiny chunk of the data.

[2:53:29] Let me make this a little bigger.

[2:53:30] OK, let's call this S.

[2:53:34] I'm actually going to, pardon me for a second, don't worry

[2:53:57] too much about what I typed there.

[2:53:59] I'm just trying to, oh, jeez.

[2:54:05] What have I done?

[2:54:19] OK, let me make this a little bigger, a little bigger, a

[2:54:24] little smaller, OK.

[2:54:26] OK, so we have data that looks, this is just to

[2:54:30] illustrate what's going on with stacking and unstacking.

[2:54:33] So you have data that looks like this.

[2:54:35] And it's really, it's one dimensional.

[2:54:37] So here we've got, for this date, we've got three.

[2:54:43] So you can imagine this label is propagated down for all

[2:54:47] three of these observations.

[2:54:48] And we've got, so the top level of indexing says this is

[2:54:52] January 31st.

[2:54:53] And then the inner level of indexing, we've got the three

[2:54:56] political parties.

[2:54:59] And these happen to all be balanced in this case.

[2:55:02] But there might be some dates here where there was no reform

[2:55:05] donation or there was no democratic donation.

[2:55:10] And so what unstack does is it takes this party column.

[2:55:16] And you can imagine it rotates the data from a one

[2:55:19] dimensional object into a two dimensional object.

[2:55:23] So you can imagine what's gone on is that, the reason it's

[2:55:26] called stack and unstack is that if you took each of the

[2:55:28] independent columns of the data frame and then stacked

[2:55:31] them on top of each other, and then fixed the labels so

[2:55:34] that the data are properly identified, then this is the

[2:55:37] object that you would get.

[2:55:41] So that's exactly what's gone on.

[2:55:42] So if I call unstack, I've got the HTML thing on again.

[2:55:47] OK.

[2:55:56] So there you can see that I've gone from the 1D hierarchical

[2:56:01] format to a 2D data frame format.

[2:56:06] AUDIENCE MEMBER 2 What did it use to unstack the party?

[2:56:11] So the default behavior is to use the inner level.

[2:56:14] So I could have explicitly said party, and that would do

[2:56:19] the same thing.

[2:56:19] But I could have said contributor, receipt, date, and

[2:56:23] that would unstack the other way.

[2:56:29] So you have complete control over it.

[2:56:35] So you can have a data frame that, so let's call this, oh

[2:56:43] gosh, you guys are going to kill me.

[2:56:47] OK.

[2:56:48] So suppose we have a data frame that, let me make this a

[2:56:51] little bigger, blah, blah, blah, looks like this.

[2:56:53] OK.

[2:56:54] So it's a function I haven't showed you, and don't worry

[2:56:59] too much, called concat.

[2:57:00] You can read about it in the documentation.

[2:57:02] So I could take two copies of this data frame and join them

[2:57:06] together along the columns, and do it, and so long axis

[2:57:10] equals 1, and do it with some keys.

[2:57:13] So keys equals capital A, capital B. OK.

[2:57:18] Make this a little smaller.

[2:57:19] And so you can see what it's done is it's taken two copies

[2:57:23] of the data, and it's glued them together, and it's added

[2:57:26] an extra level of indexing along the columns, so that I

[2:57:29] can select out the B group or the A group.

[2:57:35] Ah, crap.

[2:57:37] Fail.

[2:57:40] Or the A group.

[2:57:42] I mean, that's just standard hierarchical indexing stuff.

[2:57:46] But now, you see if I stack here, I stack party, then that

[2:57:54] now rotates down the party labels.

[2:57:57] And so I get a data frame now, which has two columns, and

[2:58:02] then the row index has two levels of indexing.

[2:58:07] And so it's a nice way to be able to rearrange and reshape

[2:58:13] the data.

[2:58:14] Of course, I could have also moved down the top level, so

[2:58:17] stack 0, so stack the top level, and now I get

[2:58:20] something that is now labeled by party up here, and then the

[2:58:24] date, and then that top level that I created

[2:58:27] didn't have a name.

[2:58:28] So it's just none.

[2:58:30] So that's what's going on.

[2:58:34] Takes a little bit of time to wrap your mind around, but

[2:58:38] it's sort of a powerful way of describing, and reshaping,

[2:58:40] and manipulating data.

[2:58:42] And it's a concept that actually is unique to pandas.

[2:58:46] If you go to R, this doesn't exist.

[2:58:49] And it's extraordinarily powerful in my

[2:58:54] uses of it so far.

[2:59:01] So I think we're just going to play with this data for a few

[2:59:03] more minutes, and then I will set you free.

[2:59:06] But the last thing I wanted to do with this data is to look

[2:59:10] at the top, for each candidate, the top

[2:59:15] contributors by occupation.

[2:59:17] So I don't know if any of you've seen infographics of

[2:59:20] this data, so it's kind of interesting to see what kind

[2:59:22] of people donate to Barack Obama, who donates to Mitt

[2:59:29] Romney, and Rick Santorum, and all those fun characters.

[2:59:33] And actually, you should go play with this data, and try

[2:59:35] to find out interesting observations.

[2:59:36] And then we can put those someplace, like a little

[2:59:39] pandas cookbook, like here is a fun analysis of the Federal

[2:59:43] Election Commission data done using this.

[2:59:45] using pandas. So if we look back at the FEC data, so if we group by, now we can do candidate

[3:00:00] name and then, they make it really easy to spell, CONTBR occupation. So let's sum this

[3:00:19] data. Well, we need to select the, I don't know why it's TB in one and TBR in the other

[3:00:29] receipt amount. So, sorry? Yeah, that's, yeah. Okay. Yeah, that's right. Yeah, thanks. Makes

[3:00:45] total sense. So it's the contributor versus a contribution. Yeah. Okay. So, so we aggregate

[3:00:52] by candidate and occupation, call that result. Okay. So hopefully, hopefully you guys have

[3:01:02] got that. Sorry, I got a comment. Oh, so, so I had discovered while, while doing work

[3:01:25] playing with this data set that there is an, somebody had reported their occupation as

[3:01:28] a zombie slayer and he donated to Ron Paul in the amount of $1,556. So it's right there

[3:01:40] in the data. Oh boy. Okay. All right. So, all right. Next, gosh. Okay. So, so the result comes

[3:02:05] out of this, this group by operation with a hierarchical index. And I actually want to get

[3:02:09] rid of the hierarchical index. And the way to do that is there's a reset index function. It is the

[3:02:13] opposite of set index. So let's call result equals result. Oh gosh, actually you're going to hate me

[3:02:23] again. So let's, I need actually need to put this series into a data frame. So let's, let's pass,

[3:02:31] not call results set index. So let's, let's call result equals and then pass a simple dict saying

[3:02:38] total. And well, actually, okay. So up here, if we, so one, one thing that I didn't mention, right,

[3:02:51] is when you do this aggregation, we don't really need to select that column. And, and what it

[3:02:57] actually does is you can see that there were a lot of columns that weren't possible to sum. And

[3:03:04] it actually, the code actually tries to sum them all. And whenever it fails, it just sort of

[3:03:09] silently drops them out. I refer to them as nuisance columns. So if that makes, makes any

[3:03:15] sense, I don't know a better name for them. And now we get a, so now the result is a data frame

[3:03:22] instead of a series because we aggregated a whole data frame instead of a single column. And I'm

[3:03:27] going to call the reset index function, which takes those, the candidate name, a contributor

[3:03:32] occupation and, and sets those back to be columns in the data frame again. So then the index is just

[3:03:38] a simple integer index. Okay. And, and now I want to group by candidate name and apply, well, I'm

[3:03:54] going to unwrap this into a function. So like top donors, top, top five donors group. Okay.

[3:04:05] So within each group, we want to sort index by contributor, contribute, contribution, receipt,

[3:04:17] receipt, amount. And then I want to slice off the last five rows. So, so what's going on here

[3:04:26] is that this, this, so this additional group buys, we've now aggregated the total amount

[3:04:30] donated to each political candidate by occupation. And then we're going to split that up again by

[3:04:36] candidate, sort in ascending order by the total amount donated by occupation and take the top

[3:04:43] five, which are the last, the last five rows. And so, so if we do that, it's going to return that.

[3:04:54] And so you can see if I call top five donors on the whole, oops,

[3:05:10] minus five colon. Yeah. Okay. And so you can see that

[3:05:16] a candidate name. So that the top five occupation candidate name combination. So the most,

[3:05:26] the largest single group of people that's donated to any candidate is retired people who've given

[3:05:32] $15 million to Barack Obama. So but we want to do that by candidate and we want to, so we'll,

[3:05:40] so what we want to do is, so let's do this result guy grouped by candidate and apply the top, top

[3:05:46] five donors function. I'm going to turn on the HTML because it make this a little easier to read on

[3:06:01] here. I, yeah, I just don't have much screen real estate to work with here. So if you don't have

[3:06:05] the you probably don't have this feature. It actually is in pandas 0.71. So so if you do set,

[3:06:15] if you do set print options, notebook wrapper, underscore wrapper, underscore HTML equals true,

[3:06:20] you should get a nice HTML output. And so you can see that, you know, let's see, let's look at like

[3:06:29] I'm really only, only interested in,

[3:06:38] oh gosh, come on Mac, help me. So I guess among, you know, Rick Santorum, let's see,

[3:06:47] retired people and then homemaker information requested best efforts. I don't know what that

[3:06:52] means. I guess they didn't report their occupation and you know, Mitt Romney, let's see.

[3:06:58] But yeah, and Barack Obama after retired people, attorneys and physicians. So

[3:07:08] so we could actually go back to this data set and you know, if we wanted to,

[3:07:13] I don't know how really to slice and dice.

[3:07:23] Just going to select out the, oh gosh, I didn't like me, must have misspelled this.

[3:07:31] Oh, it's because I did reset index and assigned it and it signed in place. And so it can't call

[3:07:35] that again. Okay. So move this one down here.

[3:07:48] So I'm just thinking of a good way to display this.

[3:07:53] a contributor occupation.

[3:08:07] okay.

[3:08:13] Okay. And so get the contributor occupations and

[3:08:18] let's see.

[3:08:22] Well, I'm going to stop that approach.

[3:08:26] Well, anyway, so you can, you know, you take a look at this,

[3:08:28] look at this data and, uh, I mean, one interesting thing

[3:08:30] about this data set, I think to really get a good

[3:08:32] visualization of it, you've got to go through and, uh,

[3:08:34] and get a mapping of the data.

[3:08:36] So, uh, I'm going to show you a couple of examples

[3:08:38] of this data set.

[3:08:42] So, uh, this is a, uh, a, a, a, a, a, a, a, a, a, a, a, a, a,

[3:08:44] a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a,

[3:08:46] of all the sort of similar occupations.

[3:08:48] If you look at it, you'll see that a lot of people

[3:08:50] have reported their occupation as being CEO,

[3:08:52] and then some will be president and CEO,

[3:08:54] some will be president,

[3:08:55] and you really wanna lump all of those into...

[3:08:59] Yeah, yeah, yeah.

[3:09:00] So to really get like a clean view of this data,

[3:09:02] because all of these occupations are self-reported,

[3:09:05] so you would need to go through

[3:09:06] and have an energetic intern or something

[3:09:10] and map all these occupations

[3:09:13] to like their sort of larger buckets.

[3:09:16] And then you could get a pretty interesting idea of,

[3:09:20] is big business contributing to this candidate,

[3:09:22] or is it mom and pops or retired people?

[3:09:27] Yeah, so it'd be...

[3:09:29] So anyway, I feel like I've sort of equipped you

[3:09:31] with a set of tools that you could go about

[3:09:33] working with this data a little bit.

[3:09:34] Yep.

[3:09:40] Yes, I will post these notebooks,

[3:09:44] and I'm actually planning to make some screencast,

[3:09:48] condensed screencasts of running through this stuff.

[3:09:51] And now that I've promised it to you,

[3:09:53] I will actually do it.

[3:09:54] I think I've made a lot of...

[3:09:57] Yeah, I think Titus Brown

[3:09:59] is going to make some screencasts too.

[3:10:01] And I think generally interested in improving

[3:10:04] the quality of education around pandas.

[3:10:07] I mean, the documentation is good,

[3:10:08] but it's more like showing you

[3:10:10] how to apply all of the functionality.

[3:10:13] Here, I'm only able to...

[3:10:15] It's a big library.

[3:10:16] It's like if you look at instance methods on series,

[3:10:20] there's like 50 to 100 instance methods

[3:10:22] on series and data frame.

[3:10:23] And really every manner of data manipulation

[3:10:26] that you might want is found someplace in the library.

[3:10:29] And if not, I'm very avid to add features

[3:10:34] and kind of make it the ultimate data tool

[3:10:38] and sort of right the wrongs

[3:10:39] of the other popular data analysis environments out there.

[3:10:43] So, yeah, does anyone have any questions?

[3:10:47] I wish we had time to do more,

[3:10:48] but hopefully this gives you a little bit of a flavor

[3:10:50] of the kind of stuff you can do.

[3:10:52] Yeah.

[3:10:53] Yeah.

[3:10:54] I have one.

[3:10:54] I would like to use pandas

[3:10:55] a lot more for scientific data.

[3:10:57] Yep.

[3:10:58] And there, you would want to be able to do more

[3:11:01] than three years of what's the status

[3:11:05] in your vision or your will for that.

[3:11:08] Yeah, so the basic story is that there's...

[3:11:12] I don't have anything against doing that.

[3:11:16] The internal data structure that backs data frame

[3:11:20] is this, I shouldn't even show this to you,

[3:11:22] but there's an internal data manager class inside

[3:11:26] which is n-dimensional and is part of what enables

[3:11:32] column insertion and deletion to be cheap

[3:11:35] in data frames and panels.

[3:11:37] There's also a three-dimensional object in pandas.

[3:11:39] So, having hierarchical indexing mitigates

[3:11:44] a lot of the need for higher dimensional objects

[3:11:50] because in many cases,

[3:11:51] those higher dimensional objects are very sparse,

[3:11:54] but at the same time, I do appreciate the need for them.

[3:11:57] So, it's something I do want to do.

[3:11:58] And I actually, I wrote a blog post last July.

[3:12:02] I think I called it a roadmap

[3:12:04] for rich statistical data structures in Python

[3:12:07] and sort of, I really wanted to create like an ND frame

[3:12:11] and with N axes and with the same kinds

[3:12:15] of rich semantics.

[3:12:17] And so, I think there's room for that

[3:12:19] and it's more like just, I need more hackers on the project.

[3:12:23] And so, yeah, let's do that.

[3:12:27] Yep.

[3:12:32] So, we're having an open space.

[3:12:38] We've scheduled an open space on the website.

[3:12:39] I'm not sure what day or time it is.

[3:12:42] Like during the conference, it's listed as PyData.

[3:12:46] So, I think definitely gonna put our minds together

[3:12:50] and think about that problem.

[3:12:52] I spoke with Francesco Ted recently,

[3:12:54] who is the author of PyTables

[3:12:56] and has done a lot of work with HDF5 files

[3:12:59] and working with larger than data sets

[3:13:01] that don't fit into memory.

[3:13:03] And I think a way forward,

[3:13:04] we'd be building a version of data frame

[3:13:06] that has a memory map as its underlying source of data

[3:13:11] or an HDF5 file, or it was designed,

[3:13:14] I mean, the reason that there is this special object inside

[3:13:16] was in order to separate the user interface,

[3:13:19] like how you interact with the data

[3:13:21] and how the data is stored in memory, in or out of memory.

[3:13:24] So, there's nothing that says you can't have a data frame

[3:13:26] that's backed by a memory map.

[3:13:28] The only problem is a lot of the code is written

[3:13:34] and the data algorithms are written

[3:13:36] assuming that the data is all in memory

[3:13:37] and I can pass an entire NumPy array of data

[3:13:40] to a Cython function or a Python function

[3:13:43] or really or what have you.

[3:13:45] So, I think it's that when you,

[3:13:47] so if you write like a group by expression

[3:13:49] on a terabyte of data,

[3:13:50] the way that you implement that

[3:13:51] is going to be very different.

[3:13:53] So, it's on the roadmap.

[3:13:56] It's just, can only type so fast.

[3:14:01] So, yeah.

[3:14:03] Yeah.

[3:14:10] The timeframe is extremely soon

[3:14:12] and if that's of interest to you,

[3:14:15] we should speak more about that.

[3:14:17] There's a date time branch on GitHub

[3:14:21] in which the date time,

[3:14:24] all the date time handling

[3:14:25] is moving to the new NumPy data type.

[3:14:26] So, NumPy has added a 64-bit integer

[3:14:29] date time representation.

[3:14:31] It's very fast.

[3:14:33] It's very space efficient.

[3:14:34] So, all the speed things like alignment

[3:14:37] and all that will go,

[3:14:38] joins will become much faster.

[3:14:41] And but we're currently in the midst of,

[3:14:44] me and the guys I work with on this,

[3:14:46] in the midst of incorporating the ideas

[3:14:48] and logic in Scikit's time series

[3:14:50] but also sort of lifting the best time series ideas

[3:14:53] from other open source packages.

[3:14:56] Because it really is,

[3:14:57] it's the weak area of the library

[3:14:59] because I've been working a lot on elsewhere

[3:15:02] and I really haven't touched time series much until now.

[3:15:04] And we've spent the last like month or so

[3:15:06] working on that.

[3:15:07] So, it's so and you know,

[3:15:09] I think the 0.8 release is going to have

[3:15:12] significant new time series functionality

[3:15:14] and will be an area of focus going forward

[3:15:18] because I'm back working in the financial domain

[3:15:21] where time series,

[3:15:22] having good time series is really important.

[3:15:26] Question was, you know,

[3:15:27] yeah, like people in the video will figure out

[3:15:29] and the question was,

[3:15:30] plans for improving time series support.

[3:15:37] Yeah, any other questions?

[3:15:43] Okay, well, thank you.

[3:15:44] Thank you guys.

[3:15:45] Thank you.

[3:15:46] Thank you.

[3:15:47] Thank you.

[3:15:48] Thank you.

[3:15:49] Thank you.

[3:15:50] Thank you.

[3:15:50] Thank you.

[3:15:51] Thank you.