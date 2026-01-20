---
title: "Powerful Pythonic Data Analysis Using pandas"
summary: "Video at PyGotham 2011"
date: 2011-09-16T00:00:00
tags: ["video", "transcript"]
slug: pygotham-2011-powerful-pythonic-data-analysis-using-pandas
word_count: 8355
source_file: transcripts/2011-09-16-pygotham-2011-powerful-pythonic-data-analysis-using-pandas.md
content_type: transcript
event: "PyGotham 2011"
video_url: "https://archive.org/details/pyvideo_487___pygotham-2011-powerful-pythonic-data-analysis-using-pandas"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this 2011 presentation, I introduce pandas—then three years in development but still relatively unknown outside scientific Python circles. I had joined a quantitative finance firm one week after the August 2007 "quant equity crisis."

## The Core Problem

I argue pandas should serve as "the foundational layer for doing statistical modeling in Python" while making Python competitive with R and commercial statistics environments. I address the pain point where analysts "use Python, but then they use R for statistics and data analysis, and kind of having to jump back and forth between Python and R can result in a lot of headaches."

The library tackles "relational data" or "labeled data" where each data point is identified by multiple IDs—SQL database exports, log files, student records—providing a unified approach that previously required ad-hoc solutions.

## Automatic Data Alignment

When combining datasets with different labels or timestamps, pandas eliminates manual alignment code: "you can just say add these two data sets together and it will add them together... it will just automatically align them. So it removes the whole data alignment problem from the question so you don't even have to really think about it anymore."

## GroupBy and Reshaping

The GroupBy operations allow aggregation with syntax like `df.groupby('column').mean()`, while stack/unstack methods enable data reshaping. A baseball statistics example demonstrates grouping by year, computing ratios, and visualizing trends.

The hierarchical indexing system allows working with multi-dimensional label structures, enabling operations like selecting all data labeled "foo" regardless of secondary index values.

## Technical Architecture

Built on NumPy, pandas uses a "lazy evaluation scheme" where columns are accumulated and only consolidated into NumPy arrays when performance benefits warrant it. The library separates data types internally—floating point, string, and boolean data stored separately.

## Integration

I emphasize pandas' integration with IPython (the new HTML notebook interface), matplotlib, and Cython. I demonstrate R integration through RPy, loading R datasets directly into pandas DataFrames.

## Future Vision

Even in 2011, I was thinking beyond in-memory processing: "we could say have an object which looks and acts and feels the exact same way, but you're pointed at a large on-disk or distributed store of data, and you could describe an operation and then that would go out until I can perform some kind of map-reduce over a cluster."

I also identified enterprise analytics as an opportunity, suggesting Python tools could compete with SAS in commercial environments.

## Key Quotes

> "I'm trying to make it the foundational layer for doing statistical modeling in Python, trying to make Python a better statistical computing environment."

> "I think there are a lot of people who use Python, but then they use R for statistics and data analysis, and kind of having to jump back and forth between Python and R can result in a lot of headaches. So being able to do everything kind of under one roof is pretty powerful."

> "You can just say add these two data sets together and it will add them together... it will just automatically align them. So it removes the whole data alignment problem from the question so you don't even have to really think about it anymore."

> "We could say have an object which looks and acts and feels the exact same way, but you're pointed at a large on-disk or distributed store of data, and you could describe an operation and then that would go out until I can perform some kind of map-reduce over a cluster."

> "I find people using the library in ways that I never envisioned. So they'll come to me and say, well, I've got this problem, and I'll be like, oh, I've never seen that before."

> "Before there were lots of nice tools, but they weren't well documented, so it's no surprise that not everyone's going to go and read 20,000 lines of Python code to figure out how to use it. So having good documentation I realized was more important than I thought."

> "What Cython does, you can take just a Python module, copy and paste it into a .pyx file and compile it with Cython and it will just become magically, like, twice as fast."

> "I really think it's going to be this amazing, really, teaching tool for the Python community."

---

## Transcript

I don't have a great deal of slides prepared, but I basically just wanted to share what

I've been working on with the pandas library over the last few years.

It's been under construction since the middle of 2008, and more or less continuously, and

especially over the last three or four months, I've spent about three months working full

time on it.

So there's a ton of new features and exciting things that I can tell you about.

So a little bit about me and where I came from.

I started out with a math background.

I was doing pure math, and later in my undergrad, I got interested in doing applied math, and

that's how I ended up getting a job in quant finance.

So I spent a few years.

I had the luck of joining, of going into finance in the middle of 2007, which, as you can imagine,

was just unbelievable timing.

I think, actually, I joined one week after the quant equity crisis on August 6, 2007.

So I joined on the 13th, so I got into work, and everyone was like, man, you missed a hell

of a week last week.

So needless to say, the financial world has changed significantly over the last four years,

and I definitely witnessed a big part of that, but I got involved with the technology of

doing quant finance and building research systems for working with financial data and

building systematic trading strategies, I guess what you might call algorithmic trading,

not high-frequency trading.

High-frequency trading and algorithmic trading are different animals.

Sometimes you read in the media, and algorithmic trading is considered the same thing as high-frequency

trading, but I don't really know anything about high-frequency trading.

So I did that for a few years, and that's where I learned Python and this whole effort

of building out a statistical computing platform.

That's where I became interested in that, and I've been at that for the last few years.

I moved on about a year ago to start a PhD in statistics at Duke, so I spent the last

year there, and a few months ago, I decided to take this year off and dedicate myself

to working on Python and really building out the fundamental tools in this area.

So I'm back in New York.

So the pandas library, it started out as a tool for financial data analysis, and it's

expanded to encompass basically a wide variety of applications, so you can reuse it for pretty

much anything.

The way I describe it to people now used to be like, okay, this is a great tool for working

with time series data, and then people would say, okay, well, it's only for time series

data, but that's not really true at all.

So really, it's a tool for working with relational data.

So if you have data originating from a SQL database or log files or any kind of data

that you need to manipulate or reshape or aggregate or transform, it's a tool for that.

In particular, I guess you say relational data, I think labeled data, so you have a

data point, whether that's a floating point value or a string or some kind of Python object,

and that's identified by a number of IDs.

So those could be, you know, so if you had a list of students in a school, you would

have their first and last name and maybe their student ID number, and then you'd have a bunch

of data for each of those students, and so that would be a labeled data set.

Structured data, sure.

So structured, relational, labeled data, however you want to think about it, whatever that

means to you.

And one of the big parts of the library is I'm trying to make it the foundational layer

for doing statistical modeling in Python, trying to make Python a better statistical

computing environment.

But at the same time, it's not just for statistics.

So I think you can use it to replace a lot of the sort of do-it-yourself data aggregation

and data munching that people do in Python using, of course, you can do it really quick

and everyone knows and understands the built-in Python data structure really well, so you

use dicks and sets and this, and you can grab some data out of a bunch of files, collect

it together, do some munching, compute some results, maybe output some aggregated text

files or feed that into, if you're visualizing something on the web, you could be feeding

that into some JavaScript plotting thing or you could be generating a matplotlib plot

or whatever you're doing with your data, however you're visualizing it and using it.

If you work with data, it's a great tool and you should take a look at it.

But it's largely an in-memory tool, and it's not really designed at the moment for processing

big data, but one of the things that I've been really focused on is trying to figure

out what's the best way to describe these data manipulations.

And so kind of a way forward from here is we've got, well, we've got these great in-memory

data structures, but we could say have an object which looks and acts and feels the

exact same way, but you're pointed at a large on-disk or distributed store of data, and

you could describe an operation and then that would go out until I can perform some kind

of map-reduce over a cluster.

And so you can make it work on big data, and I think the focus has really been trying to

get the right syntax, making it Pythonic, easy to express these sort of complicated

high-level data manipulations.

So the applications I've been mentioning, sort of just general data-munching data manipulation,

I've used the library extensively in financial data analysis and modeling, and there are

a lot of people who have picked it up and have been really successful using it in that

area, working on purely statistical computing in Python, making Python more competitive

with commercial statistics environments and also competitive with, or at least comparable

to R. So I think there are a lot of people who use Python, but then they use R for statistics

and data analysis, and kind of having to jump back and forth between Python and R can result

in a lot of headaches.

So being able to do everything kind of under one roof is pretty powerful.

The area that I haven't done as much in is the whole sort of enterprise and big data

analytics question, basically where SAS, if any of you are familiar with the SAS company,

they're kind of the bread and butter of enterprise analytics, whatever that means.

But just generally I think it's good for the Python community to think more about are there

ways that we can expand into this area and build commercial interests built on this open

source foundation of tools to sort of compete in the enterprise analytics space.

So there was just a new release of pandas on last Monday.

I gather that I'm due for a bug fix release, and it's only been a week.

But the bugs that have been discovered are pretty minor.

There's a lot of new stuff.

Most of it was written over the last three or four months, so I'm going to spend most

of the talk doing a demo, so you'll see some of that.

A lot of the work that I put in was on documentation.

Before there were lots of nice tools, but they weren't well documented, so it's no surprise

that not everyone's going to go and read 20,000 lines of Python code to figure out how to

use it.

So having good documentation I realized was more important than I thought.

And I've got a feature list this long, and it keeps getting longer every time I add a

new feature.

So I'm definitely looking for people to work on the project with me and expand it, definitely

in directions that aren't necessarily related to my primary interest.

So I'm interested in getting more people looking at the code and using it to solve problems

that aren't necessarily statistical in nature, particularly in the web space.

There's tons of data out there, and I find people using the library in ways that I never

envisioned.

So they'll come to me and say, well, I've got this problem, and I'll be like, oh, I've

never seen that before.

And that generates ideas for ways to redesign components of the library or ways to augment

existing features to make them more useful, more expressive.

So, I don't know how many of you know about the, have used much of the Scientific Python

stack.

I don't know, get a show of hands if anyone used NumPy.

Yeah.

All right, actually, it's pretty good.

So, if you go to PyCon, it's usually like 80% of people there use Django and, you know,

15% of them use something other than Django and then maybe you have like 5% of people

who are, who've used the Scientific Python stack.

Of course, all this is built on top of NumPy, which has really only been around since 2005.

People have been doing Scientific Computing and Python since the mid-90s, but there was

sort of a bifurcation.

There were two numerical libraries and they were brought together by Travis Oliphant in

2005.

Travis is now one of the guys who runs Enthought, which is a Scientific Python consulting outfit

out of Austin, Texas.

So, two other projects that you guys are probably familiar with.

One of which is IPython, which I'll talk a little bit about and show you more of, and

Cython.

Cython is this amazing project.

So, if you ever need to make your Python code faster, it should probably be, well, after

you go through the obvious stages of, well, is there a better, you know, pure Python way

to rewrite, you know, am I doing a dumb algorithm, I run cprofile, say, OK, well, this is the

bottleneck.

But sometimes you can't optimize things at the pure Python level.

So what Cython does, you can take just a Python module, copy and paste it into a .pyx file

and compile it with Cython and it will just become magically, like, twice as fast.

Because what it does is it translates the Python code into C code.

So all of the data structures, everything, whenever you make a function call, everything

becomes early bound instead of late bound.

So it skips the interpreter.

That speeds things up quite a bit.

So you can start there, then you can start adding types.

If you have a list, you can say this is a list and whenever you do .append, that's going

to get translated to the appropriate C API call.

So everything kind of magically becomes a lot faster.

And the pain and anguish of building C extensions in Python is largely, well, it's made quite

a lot easier.

You don't have to do reference counting, all that fun stuff.

So the IPython project, you know, when I talk to Python people, often my first question

is, well, do you use IPython?

And if so, why not?

And it's definitely, almost everyone in the scientific Python community uses it because

it has nice integration with the visualization tools like matplotlib.

So when you say plot, plot X, then it pops up a window and it doesn't steal control from

the interpreter, which is what will happen if you use matplotlib within the standard

Python interpreter.

So it's a nice interactive research environment.

But it's this also amazing Python development environment.

So often people ask me, say, okay, what's your Python development environment?

I'm like, well, Emacs and IPython.

And that's kind of like a little bit of a crazy notion to some people, especially those

coming from Java land having an IDE and being able to like visually.

And I admit, it's nice to be able to visually click on a line and set a breakpoint.

But in IPython, you can, well, you can set a breakpoint, but you have to type out the

file, you know, the file name and line number.

So it's a little bit rough around the edges in that way.

But the, it has, you know, kind of, I'll show you a little bit.

So my workflow is typically, I edit a file and then I have a live IPython shell and I'm

basically running that script and I can run it in debug mode, set breakpoints, step through

the code.

Whenever there's an error, I can drop back into the stack trace, step up and down.

It gives me context around each line in the stack trace.

So it's a very nice development experience.

So I do recommend giving it a shot even if you're not a scientific Python programmer.

So a few pretty amazing things that have happened in the last year is there's a new QT-based

console terminal replacement and it can, so you can basically run all your code inside

there.

But when you do plots, there's not a, there's a feature where it will render the plots in

line and you'll see that.

And the next thing, which is the HTML notebook, and, you know, I've been raving about the

HTML notebook for the last week, largely on Twitter, and I'm going to show you exactly

what this is, but it's an interactive Python notebook, I'll show you what I mean by notebook,

but running within a web browser.

So it can be run anywhere, you can connect to a remote Python instance, run code, you

have cells of code that you can edit, plots are rendered in the browser.

So it's, I really think it's going to be this amazing, really, teaching tool for the Python

community.

So rather than having a web page with a bunch of documentation, you can just distribute

a series of IPython notebooks that people can fire up and they can run through and test

the code examples and experiment and edit things and so I really think it's going to

be a big deal and it's extreme, it's extremely new, extremely new.

So skip this slide.

And so some of the features, so back to pandas, some of the features in pandas that I'm going

to show you that are really important.

The first is this data alignment question.

And so often you get data from many different sources and you collect data and they're labeled

slightly different.

So if you have time series data, you might have one data set that has a certain set of

dates and another data set that has another set of dates and you might want to combine

those together, you want to add them together, you want to join those data sets.

And so there's this data alignment problem that happens all the time and oftentimes you

find people write this ad hoc code to say well union together the labels that I care

about and then expand or either take the intersection or the union of the labels and then realign

the data sets and then glue them together.

So pandas completely removes this step.

So you can just say add these two data sets together and it will add them together or

you can say join these two data sets which are labeled differently and it will, based

on how you say how to join, it will just automatically align them.

So it removes the whole data alignment problem from the question so you don't even have to

really think about it anymore.

The second thing is indexing.

So it gets to how you, once you have a data set, you've said okay here are the ID variables,

here are the labels, it's how do I select subsets of the data and how do I select out

portions, either slices along a dimension or collections of data that you care about.

And these last three points, group by, pivoting, reshaping will make sense in the demo, missing

data, I'll explain what that means and then I'll touch a little bit of time series functionality.

So does anyone have any general questions before I start firing away with code demos?

So I'll show you a little bit about the IPython notebook.

So in my terminal I've launched the IPython notebook and I've told it that I wanted to

start it with PyLab inline, I'll explain what that means.

Basically this just starts an HTTP server that I can connect to in the web browser and

when I fire that up it gives me, so this is sort of the welcome screen and it shows

me all of the notebook files that I have living in the directory where I started up the server.

And so I can, so I can then click on one of these and it starts up the notebook interface.

And so you've got all this navigation over here and then on the right side you've got

basically a bunch of cells which can contain Python code.

Here's a cell that contains Markdown, so I can put Markdown in here and it live, and

it live renders.

And I can put in arbitrary Python code.

Put an arbitrary Python code and execute it.

What's happening in the background is there's an IPython, which is the IPython shell.

There's an embedded IPython kernel, is what they call it, in the background.

Whenever I execute a code block, it's executing that code in the IPython namespace.

There's this blob of state where code is executed.

Whenever you do things like plots, what it's going to do is execute the code, capture the

plot, render it, save it to a file, and then load it up right inside the web browser.

It's pretty cool.

I'm going to start to talk about the basics of pandas, and I apologize for those of you

who were at the meetup on Wednesday who've seen some of this.

The idea is that we have arrays of data, and we associate labels with them.

The one-dimensional case here we have, we just generate five random numbers, and I pass

that to the series object, which is the one-dimensional vector, and it generates some arbitrary labels,

just range five for the labels.

If I actually had a set of labels here, ABCDE, and I create the series with the labels, then

you can see now it gives me this array object, which has the labels on the left side.

The labels are stored in the index attribute, and so this object that you have is sort of

dict-like.

I can say b in two, and it says true, and it's b in the index, also true.

If I'd had a dict instead of a series, I could just pass that to the constructor, and it

knows what to do with that, too.

So if you ever have a Python dict, put it into a pandas object, you can just pass it

to the constructor.

What's nice is that whenever you do, because it's also a NumPy array, so you can say s

times two, and it vectorizes that operation to all the elements.

I can call math functions, like take the, raise everything to the e power, or raise

e to each of those power.

But one of the major features that is sort of all throughout the library is this data

alignment concept.

So if I have an object here which has only a, b, c, and then I have another one which

is a, b, c, d, e, I can add them together, and it's going to align the values on label.

So if you had these two arrays of data that came from different places, if one was missing

a set of labels, and you want to add everything together matching a label, and it does it

automatically.

So you just don't have to worry about it.

The 2D analog of the series is DataFrame, and DataFrame is basically the main object

in the library.

And it's this tabular data structure, so you can think of it kind of like a spreadsheet.

So each, so you have columns of data, let me get, I don't know where my scroll bar is

in this browser.

Somehow my scroll bar disappeared in that window.

Mysteries of Google Chrome.

Okay, you guys can all read that.

So you have this tabular data structure, so now you have column labels and row labels.

So you can get the columns, the rows, which is still called the index.

If you ever have a scenario where you build a nested dict of data, so you've got dicts

within a dict, then you can pass that dict of data to the DataFrame constructor and it

will put everything into a table, it will take the union of all the labels and the inner

levels and take all the keys at the outermost level and then put things into a tabular data

structure.

So you can see here in this example, we've got this key column here, which has some strings

in it and then all the other columns have floating point values in them.

So let me run all the code from the beginning here.

This demo is designed to be run in order, so I replaced variables later in the demo,

so it was giving me slightly different data.

So you can access, so you can think of this object as like a dict of the one dimensional

labeled object, so I can say give me the foo column, get item foo, gives me that column.

I can insert columns like a dict, so here I said take foo greater than zero, insert

that and that inserts a Boolean vector.

I can delete columns.

If I insert a column that's shorter than the other ones, then it gets conformed to the

row labels.

I can get the underlying array of data, which is stored in a NumPy array.

If you pass in a dict of series, it's just like a nested dict, so here even though I've

got a dict that contains one that's ABC and one's ABCD, I can pass that into DataFrame

and it knows how to align and basically take the union of everything and align things to

the full set of labels.

You can also say pass in the labels that you care about.

I say I want DBA to be the row labels and it conforms things to that or I can pass in

I only want columns two and three.

Even though that dict that I pass in didn't have a three column, it inserts a three column

and it puts in not a number, which is the missing value marker in that column.

So I can do things like transposing, which is the order of the row and column labels,

so it works very much like...

So if you're familiar with NumPy, you're doing dot capital T transposes an array, so it works

very similarly.

Sorry, I was supposed to tell you a little bit more about data alignment.

Here we have these two series, add them together, it matches the labels.

You can also explicitly align objects to a set of labels.

Here you see I have...

This is S and this is S2 and I could say take S and align it to S2's index.

So the method for that is reindex.

So I say S reindex S2 index and you can see it sets it to be ABC.

I could go the other direction, take S2 and conform it to S1's index and see it inserts

NAs in the missing locations.

Similarly if I have two data frames, here I've got one with ABC and one with ABCD, they've

got different row labels, and I can add them together and that operation works, takes the

union of everything and it inserts NAs in the locations where there wasn't a match.

So other things are nice, so operations between...

I'll explain the syntax later, very briefly, but if I have, let's say, a row from the data

frame and I subtract that from the data frame, it broadcasts down the rows.

So you can see it completely knocked out this five row here, but it broadcasted to all the

other rows.

So you can express operations on data if you wanted to de-mean the...

If you want to subtract the column mean from each of the columns, I could say df.mean which

gives me the mean of all the values in each column.

and then say df minus df.mean.

And that subtracts the mean from all the columns.

So you can see the result now is, well, e minus 17.

So nearly 0, not quite 0.

That's just floating point error.

So another pretty common thing is when you're,

particularly with time series when you're aligning data.

So say I had a time series here going from January 3

through January 12.

And then I had another series, which is some subset

of those dates, so the 3rd, the 6th, and the 11th.

If I, say, take the smaller time series and make it label

the same as the bigger time series, you see it inserts

values into the dates where it matches.

And then there are NAs in the ones where it didn't.

So you might say, well, on January 4, I just want to have

the value from January 3.

So you can re-index with ffill, which then propagates

the values in the whole.

So the value from the 3rd gets propagated to the 4th

and the 5th and whatnot.

So this sort of thing is pretty useful.

You could also take the result of re-index, which has NAs,

and then you could just say fill an A with 0,

and it puts in 0's.

Or I could say fill an A with method ffill.

So if you got some result, and it's got some NAs,

and you want to fill in those holes,

you could just say fill an A with ffill,

and then it propagates the values forward.

And this method, of course, works on non-time series data.

So if you had some kind of ordering on your data,

and it might be some kind of time stamps

or something like that, you could use this method

to clean up a data set.

You have a question?

Yes.

About the labels, are there restrictions on what labels

you can use?

They can be anything.

They just have to be hashable.

So, OK, anything mutable will work?

What's that?

Anything immutable will work?

Yes.

Yeah.

So they could be tuples.

I mean, they could be, yeah.

And what about the data in the data frames?

Does it have to be floats?

No, it could be any type.

So what do you use for NAs, for example?

An int, right?

So that's a whole subtopic.

We should talk about that afterward.

But if NAs get inserted into an array,

it's going to get upcasted to float.

You can store, so non-float, non-numeric data

gets stored in an object array.

And then you can put in NAs.

So, yeah, it's a thorny topic.

They're going to add proper NA support

to NumPy, which will be a very nice thing at some point.

So you're not using, or it's not using master arrays or anything

like that?

No.

Master arrays have performance problems.

Yeah.

Anyway, so some nice things with data frames.

So if you have labels, so there's

a special indexing operator if you want to select out,

let's say, a subset of rows and columns at the same time.

You can pass a list of row labels

and a list of column labels, and that

will select out the portion of the data set that's

labeled like that.

You can mix and match other kinds of indexing.

So if you had a Boolean vector, let's say

you want it everywhere where the foo column is greater than 0,

and you only want the first two, whatever

are the first two columns, you can put in a Boolean vector

here, and then a slice object, and then that

selects out that subset of the data.

It also gives you a nice way, let's say,

just one of the first five rows of the A columns.

You can say colon 5 A, and that will

grab that piece of the data.

You could grab the first five rows, but both the A and C

column, and that gives you exactly that.

So it's a very concise way of selecting out

portions of your data set.

Yeah?

Quick question.

Would the indexing operation create a copy or a reference?

It depends on, it depends.

So if you do a slice, it will create a view on the data.

Yeah, so slices will create a view,

but if you have an arbitrary set of labels,

it will create a copy.

It's just a limitation of NumPy.

You could also set.

So rather than saying, I did get here,

so I could say set equals 0.

And now you can see that those five rows in each of those two

columns have now been set to 0.

So it goes both ways.

So you can do getting and setting.

So if you wanted to, let's say, null out

a portion of a data set, say, I want to ignore this,

then you can.

So one nice thing about these data structures

is that if you do any computations with missing data,

so here I've got some NAs.

Whenever I do, let's say, mean 1,

which says take the mean of each row, it ignores the NAs.

There's a skip NA flag, so I could say skip NA false.

And then you can see that if there are any NAs,

then you get NAs in the result. But the default mean

is to take the column means.

And you can see it also excluded NAs automatically.

So having the built-in missing data handling

is really, really very nice.

So a new thing that I added in the last few months

was hierarchical indexing.

So you could certainly have a tuple

refer to, you could have a tuple as a row label.

But what if you wanted to grab a portion of a data set

where just matching on the first element of the tuples.

So doing that in the past used to be kind of difficult.

So now in this data set where I've

got the first level of FUBAR-BAS quarks,

however you pronounce that, and then the second level,

1, 2, 3, I could say, do the indexing operator to ix

and give me everything labeled foo.

And that will select out that chunk of data.

And then you can see that it dropped off foo there.

I could also do foo comma 1.

And that gives me just a row now.

And so that's very useful.

And I'll show you how the hierarchical indexing integrates

with some pretty sophisticated data reshaping.

So I'm going to kind of skip ahead

to some of that, which is a lot more fun.

So plotting.

So the labels are integrated.

So there's a number of plotting functions.

So if I have a series and you want to generate a bar plot,

you can see I can say plot kind equals bar.

It makes a bar plot with matplotlib

and puts the labels on the axis.

So you can do some pretty quick data visualizations

very easily.

If you've got a time series, you say .plot.

You see it makes the time series plot

and puts dates on the x-axis.

If you have, here I've got some financial data.

But suppose you had a bunch of numerical data

and you wanted to create a histogram of all the columns.

I can just say .hist and it creates a nice matplotlib plot

with histograms of the data.

So it's pretty useful.

So I'll talk about some things that you guys might find

a little more interesting than doing computations

on time series data.

Just generally is this problem of reshaping and aggregating

data.

So it's pretty common to store data,

especially in a SQL database in this,

I guess I call it the stacked format.

So you have a bunch of labels.

These would be like your primary keys.

So here in this data we have a date, a date column,

and then a variable, and a value.

But what you would really like to do is say collect

all of the values for the A variable into a vector

and all of the values for the B variable into a vector.

So I call this essentially a pivot operation.

So I can say, take this data frame,

pivot on date and variable.

And you can see now it reshapes the data.

So now the row labels are the unique values

from the date column, and the column labels

are the unique values from the variable column.

But you can see what it did is because it

takes all of the remaining columns

and it turns that into a hierarchical index

for the columns.

So I can do value here, and so I get all of the data

just for the value column.

If I had multiple columns and I do pivot,

you can see now I've got.

got this chunk of data for the value column and this other chunk of data for value two.

So you could do, here you do value two and so you get the reshaped data for the value

two column. And so with reshaping data, what's going on under the hood is you've got these

column labels and then you have these two special functions stack and unstack. So if

you take this two-dimensional object here with column and row labels, I can say stack.

And what that does is it turns it into 1D. It takes those column labels and it reshapes

the data. So now we have a two-level index on the rows where, you know, here we've got

ABCD for each of these guys. So do something a little more, a little less trivial. So suppose

we had a data frame that looks like, make this a little bigger now. Suppose we had a

data frame that looks like this. Both the rows and columns have hierarchical indexes

now. So I could do df stack and I want to do the second level in the top. And you can

see now it's taken the cat and dog labels and it's reshaped that data into the columns.

So now we've got three labels on the rows and then we've got the remaining. If you look

here, we had AB. This is ABBA. It's now just got A and B as the two unique columns. But

this is really nice. So suppose that you had data that was indexed like this and you wanted

to do some aggregation. Like let's say you wanted to aggregate on this AB level, like

take the mean of the values for each of the groups. So I could do stack to get the data

to look like this, mean one. That's going to take the mean of the rows. So that took

the mean there. And then I could do unstack two. So this is zero, one, two. So unstack

two. And so now it reshapes it back and you've got cat and dog in the columns now. So, I

mean, you could, of course, do any kind of variation you like on this. I could have done

stack zero. So now I've got cat and dog here and I could do mean and that gives me the

mean for cat and dog or, well, you can use your imaginations. But I could do mean one

here and then I could do unstack zero which reshapes things a little bit different way.

So it gives you this kind of like nice expressive way of, you know, you take a data set, you

put all, you can take, you can make it a completely one-dimensional thing where you put all the

labeling sort of your primary key information in the index and then you can use these stack

and unstack methods to kind of reshape the data and then do aggregations and then kind

of munch it in the way that you want. But what's nice about these functions is that

you could have missing observations at a level. So if we take, so if we go here and suppose

we did take every third observation, right? So there's no, so the levels aren't full,

let's say. I'll show you what I mean. So if I then restack, unstack, you can see that

it places where there was no observation for bar one, cat B, it's inserted an NA there.

So you could have incomplete data where things are missing and then all of this stacking,

unstacking, reshaping business works and doesn't throw any errors. And of course, if you do

any arithmetic operations like you now aggregate, if I do mean one, you see now it computes

a valid value. So you can do, you can work with data and have missing data and it's no

problem at all. Kind of related to this is this notion of group by which, you know, you

guys have probably, most of you probably use SQL and have written, you know, select star

from blah, blah, blah with, you know, group by these three fields and whatnot. And so

what I tried to do is build an intuitive group by engine within pandas. So if you've got

data that looks like this and you want to say group by, group by the A column, I can

say DF group by A and that creates this group by object, right? It's this group by object

which you can then do lots of fun things with. I can say mean which is going to then take

the mean of the chunks of data that were labeled bar and bar and foo in the A column. And so

you get a nice data frame output. I could say for key group and grouped. So print key,

print group, right? And so that chops up the data set into the blocks grouped by each of

the keys. Then you could do some arbitrary thing that you want to do with each of those

groups. I could group by multiple keys. So I could pass a list of column names here,

grouped by A and B, same thing. And you can see now the keys are a tuple of each of the

unique grouping keys and then you get the chunks of data associated with each of those

groups. So it's a pretty useful functionality there. So you see here I've got this, let's

see, I've got this returns data set which is, you know, some Apple and Google and Microsoft

Yahoo returns from February 2010 through, well, just about now. And so if I group this

by year, let's say, I could compute, if I do .std which is compute the standard deviation

by year. So what's going on here is group by doesn't have an std method. So when I do

.std, what's happening underneath is that it's creating this wrapper function which

whenever I call it, I can pass arguments to it. You know, you could have some, a method

which takes arguments. So what it's going to do is it's going to take that method, invoke

it on each of the groups and then glue all the results together. So any method that's

implemented on DataFrame, you could, you can group the data set and then you take that

grouped object and call a DataFrame function just like it were there using just a DataFrame

and it's going to dispatch to each of the groups and then glue the results together.

So it's a pretty powerful way to group data and then express these, express these operations.

So I had another fun little data set, some baseball data and I wanted to, so I took baseball,

I grouped this baseball data. Before I run out of time here, demos always take way longer

than I expect. So you can see I've got 22,000 observations across a lot of players and since

1870, I grouped the data by year, I summed it up and then I wanted to see, you know,

how is hit by, I basically took hit by pitch divided by at bats over time. So I did the

total by year and then I took hit by pitch divided by at bats and you can see since

1870 through 2000, you need a relative incidence of being hit by pitch over year. So this is

kind of a really tidy way, say group by year, sum it up, take the ratio and plot it and

you get this kind of nice summarization of data with very few, very few commands. So

of course, you know, the natural way, the place to go from here is start combining this

with statistics and stuff like that. So you could take data and you could run a regression

between a couple of variables but then you could run a regression but grouped by, let's

say, year and month. So I did that here and I said, did this group by statement and it

computes this nice, you know, data frame output of, you know, 20 different linear regression

on a bunch of group data. So you could do arbitrary data munging but, you know, it's

a natural way of kind of expressing statistical operations as well. So anyway, that's about

all I have for you with this. I'm out of time but definitely take your questions and things

you might be interested in.

I have a question about something that's not yet in the stat models.

Okay.

For instance, if you want to work with a pure NumPy array and use some sci-fi function

that is not yet in the library, can I strip all the labels and...

Yeah, so any of these objects, let's say, right, so if I take this guy and then I just

do dot values and I get an umpire array.

So if this were, well, this is mixed type, so the result comes out as an object array,

but if I had just had C and D, all right, so just numeric and I do dot values, then

that comes out as numerical, so you could then just pass that into a function.

But you could also, most NumPy functions, if you just call them on DataFrame, they work.

So if I want to take the square root of the values, then that just works, but if you wanted

to pass this into SciPy Optimize or something like that, then you want to just pass the

array.

All right.

Yeah.

Sure.

Is your DataFrame always backed by a single NumPy array?

No.

There's actually an internal, there's an internal data structure which keeps the types separate,

so all the floating point data will be stored together, all of the string and object data

stored together, Boolean data.

So yeah, there's actually sort of like, there's a lazy evaluation scheme, so if you have a

computation where you insert a bunch of columns into DataFrame, you don't want to keep reallocating

and copying data between NumPy arrays, so what it does is it accumulates the new columns

and then at some point, whenever you do some operation that's going to be faster on a single

NumPy array, it glues everything together.

So you can look at the source, but that's new stuff, that's been looking the last three

months.

Sure.

Are you going to possibly give a longer sort of coldish version?

Do you skip...

Yeah.

That's hard.

Really I'd have to give like a one day class or something, because it's too much material

for an hour, and if you print off the documentation, the documentation's like 100 pages, so it's

just a big library.

Right.

Yeah.

Cool.

Yeah.

You have one more question?

Yeah.

So this R pi that allows you to call the 2R from Python, is there a bridge between the

R DataFrame object and your DataFrame object?

Are they easy to convert?

There is.

So yeah.

If I had more time, which I never do, I have enough time.

So in the Git repository there's an R pi sub-package, and so I can say R pi load data and then tell

it...

So I could say R pi load data and then I could say baseball, that's where I got the baseball

data from, and I could say some R package like Plyer, I think it came from Plyer, and

what that does is it calls R pi and then knows how to translate the data through the bridge.

So it's useful for getting data sets.

I'd like to create some tighter integration between some of the R, there's some nice R

libraries like ggplot2 for data visualization, where you could pass in pandas DataFrame and

it would call the, write R function on it or something like that.

So just a function of spending time.

All right.

Thanks guys.