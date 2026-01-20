---
title: "PyCon SG 2013 Conference Keynote from Wes McKinney"
summary: "Video at PyCon Singapore"
date: 2013-06-14T00:00:00
tags: ["video", "transcript"]
slug: pycon-singapore-keynote
word_count: 9560
source_file: transcripts/2013-06-14-pycon-singapore-keynote.md
content_type: transcript
event: "PyCon Singapore"
video_url: "https://www.youtube.com/watch?v=Jm73dKlYHZw"
---

{{< video https://www.youtube.com/watch?v=Jm73dKlYHZw >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This 2013 talk offers a state-of-the-union assessment of Python's data science ecosystem.

## Scientific Python Maturation

I note how recently the Python data stack came together. NumPy reached its current form in 2005 when Travis Oliphant unified the array library landscape. The IPython notebook, which I call "really game-changing," had emerged just two years prior.

Key libraries driving adoption: Scikit-learn brought machine learning, with its French and German developers being "a model for how open source should work." Stats models provided R-like statistics, and PyCuda made high-performance computing accessible: "if you've ever written Cuda code in C and then gone to PyCuda, it's just really a transformative process."

## Data Preparation

Data cleaning represents 80-90% of analysis time. "Making the data cleaning and data preparation tools easier to use and more productive really overall speeds up the analysis process a great deal."

A key principle: "if your tools are hard to work with, you're less creative." Reducing friction enables faster iteration and more questions.

## Stack Overflow Analysis

A live demo analyzed Stack Overflow data. Django declined from 15% of Python questions in 2010 to lower percentages by 2013, while Flask gained ground. pandas had grown to over 2% of Python questions. Emerging trends: Raspberry Pi, Python 3 adoption, and IPython itself.

## The Web Challenge

"The big challenge for Python over the next four or five years is how to keep Python as an important and relevant language that people want to program in and that they can use to build systems in the way that they need to be built for the future."

Obstacles: JavaScript isn't designed for serious data processing, browsers handle only data subsets, and network latency complicates interactive applications. The solution: build bridges to web technologies, not abandon Python.

## Python-Web Integration

The IPython notebook runs as a JavaScript application executing Python on the backend. RStudio's architecture creates applications running locally or in the cloud seamlessly.

Emerging tools like Vincent (Vega.js integration) and Folium (Leaflet.js mapping) power web visualizations from pandas data.

## JIT Compilation

Numba translates Python code into machine-code performance. Related: PyPy, Julia's LLVM architecture, and Cloudera's Impala using JIT for SQL processing.

## Big Data and SQL

The "SQL everywhere" trend: Facebook's Hive, Berkeley's Shark, Amazon's Redshift. Python has limited success in big data compared to "medium data," but emerging interfaces to Spark looked promising.

## Requirements for Data Tools

Built-in missing data handling, intuitive APIs that don't impede thinking, and core operations for grouping, sorting, and filtering that are both fast and easy to use.

I urged users to document pain points: "The more that the open source development community understands problems that people are experiencing in the real world, that really helps everyone make good design decisions."

## Key Quotes

> "If your tools are hard to work with, you're less creative."

> "Making the data cleaning and data preparation tools easier to use and more productive really overall speeds up the analysis process a great deal."

> "The big challenge for Python over the next four or five years is how to keep Python as an important and relevant language that people want to program in and that they can use to build systems in the way that they need to be built for the future."

> "If you go on GitHub and look at the Scikit-learn project, it's kind of a model for how open source should work."

> "Hopefully, we don't have to give up on Python and just program in JavaScript, because that would make us all very sad."

> "I think in order for Python to really stay relevant, rather than saying, no, I'm not going to program in JavaScript, I think we have to build interfaces to JavaScript and to the web technology so that you can keep your serious work in Python."

> "The more that the open source development community understands problems that people are experiencing in the real world, that really helps everyone make good design decisions."

> "When I started using Python in 2007, people thought I was crazy. They were like, this is not a serious language, you can't build production systems with this."

---

## Transcript

Thanks a lot. Thanks a lot, Calvin, for the introduction. Thanks for having me here. This

is my first time in Singapore, second time in Asia, but it's been a long time since,

I think the last time I was in Asia was in 2005, so it's been a very long time. I'm excited

to, already excited to come back. So, I guess this talk is a little bit high level. I will

have some examples and some things about pandas, but also I wanted to comment a bit generally

about the state of Python for working with data, and if you're not very familiar with

some of the development that's been going on the last five or six years, just to tell

you a bit about that, and at least to tell you from my point of view, what are the interesting

trends right now and where I see things going. So, I've been doing a lot of things the last

few years. Most recently, I just moved to San Francisco from New York. I'm working

on a new analytics company there, which hasn't launched yet, and there will be more information

about that later this year. Went to MIT a long time ago, started the pandas project

not long after I got out of college, mainly because I was very excited about programming

in Python, but I found that there was kind of a missing piece, which was data manipulation

tools. You had great general purpose programming libraries, tools for building systems, unit

testing libraries, array computing with NumPy, very rich scientific Python ecosystem, but

the statistical data analysis tools and data manipulation, data cleaning tools, there really

wasn't very much of that in Python, in large part because Python didn't have a very big

statistics community, so I started pandas essentially in response to that. So, my book

came out in October, and the goal of the book was to have a nice introduction for people

who've never used Python for working with data before. So, it's not a book about data

analysis methods so much as it is a book that shows you how to use the important Python

tools for working with data so that you can do data analysis. So, I wanted to give a nice

introduction to the main scientific Python tools, NumPy for array computing, IPython,

which is the programming environment we've all come, you know, I've been a big fan of,

Matplotlib for data visualization, and then pandas is about, you know, maybe more than

half the book, showing you how to use the library to solve, you know, all of the various

problems you may encounter. So, the last six years have been very interesting for

Python. Well, you know, you have to remember that NumPy, which is the array computing library

for Python, essentially what gives you, you know, matrices and linear algebra and, you

know, MATLAB-like functionality in Python, really only existed in its current form from

about 2005 onward. There were multiple array libraries starting in about 1995, and there

was a bit of a community fragmentation that was going on, and Travis Oliphant really wanted

to unite the Python community under a single array library and merge those two libraries

together, Numeric and NumArray, and created NumPy, and that was only in 2005. And the

NumPy project and SciPy, which is built on top of NumPy, has matured a lot in the last

five years, and that's been very important for businesses who want to adopt Python and

want to feel like they're building on top of a mature and stable tool, that the code

that they write today is going to be robust and not have weird crashes and problems running

in production, but that that code will also be maintainable and will still have a good

chance of working a few years down the road. One of the other really game-changing things

in the Python ecosystem in the last, really just last two years, has been the IPython

notebook. How many of you have used the IPython notebook? So I'll show it to you in the talk,

but it's been a really great tool for creating and sharing data analysis and really any kind

of Python work. It's very easy to take a notebook that you've created on your computer and upload

it on the Internet and share it with people. It's a really great way to collaborate on

Python work. Other libraries that have been really important for bringing more people

into the Python ecosystem outside of pandas have been things like Scikit-learn for machine

learning. So it used to be if you wanted to do machine learning, you had to use R or you

had to use Java or some other library. So a group of primarily, they seem to be mostly

French, but mostly French and German developers have built the Scikit-learn library and now

has a very large and very active community of developers. So if you go on GitHub and

look at the Scikit-learn project, it's kind of a model for how open source should work.

The progress they've made is really incredible. I've been involved in stats models, which

is the statistics and econometrics library for Python. It gives you a lot of the kinds

of regression and statistics tools that you have in R, but in Python. There's now, we

now even have formulas. So if you're, it used to be pretty hard to write down complex regression

models, so now you can write formula strings that describe your linear model and there's

a formula parser that will, that connects with stats models that you can use. Other

things, well the next talk up is about PyCuda, which has certainly brought a lot of people

to Python for doing high performance computing. Tools like PyCuda and PyOpenCL make, you know,

programming on GPUs for very high performance computing applications a lot more accessible.

So if you've ever written Cuda code in C and gone through that, that painful process and

then gone to PyCuda, it's, you know, it's just really a transformative process. So I

wrote some Cuda C before I used PyCuda and I was really upset about all the time I spent

writing C code before I used PyCuda, so really great. Another missing piece of the puzzle,

as I was saying, is pandas, which made Python a good language for working with any kind

of raw data and wrangling it into shape so that you can do analysis on it. So data preparation,

I love this, I love this quote, this happened during the Strata conference last February

in the Bay Area, that in doing data analysis often the data cleaning and data preparation

makes up a lot of the time that you spend doing the analysis. You know, people quote

80%, sometimes it could be 90%, and you spend a lot of time, you know, you prepare your

data, you do a bit of analysis and you might find some problem with your data and you have

to return to the sort of data cleaning, data preparation to sort out issues and bad, you

know, problems in your data. So making the data cleaning and data preparation tools easier

to use and more, you know, faster and more productive really overall speeds up the analysis

process a great deal. And that's what pandas is for. It's primarily a tabular, you know,

spreadsheet style data manipulation tool for Python. It's very fast, so it's much faster

than you would get writing something in pure Python. But one of the main features is that

it has a really nice API, so the functions, all of the methods and functions are intended

to fit really nicely together so you don't have to spend, hopefully you don't have to

spend a lot of time digging around documentation and remembering how functions work. So some

people like to describe it as like our data frames in Python and that's not a completely

accurate characterization, but, you know, you can see, you can think of it, think of

it that way. And it's been growing very, very fast and now has a quite large development

community. As an aside, another project I've been involved with is a little library called

VBench. So if you ever care about performance testing your code and are interested in, you

know, keeping track of how fast your code is, it's a tool. I had to build it in order,

you know, to keep myself sane while developing pandas, monitoring whether things get slow

or not. So you can see in this example, you know, in the middle of 2011, there was an

operation that got slower for a while and then it got faster and faster over time.

time.

So this is a benchmark of a simple panda statement benchmarked at each version of the code base

over time.

So you can see how, keep track of whether the library's getting slower or faster.

So one of the big things that I've learned in working on data tools is if your tools

are hard to work with, you're less creative.

And I found this myself that, because I'm very curious, like I like to ask a lot of

questions and I like to be able to get answers to those questions very quickly.

So each time you ask a question, if you feel like you have to go through a lot of pain

and suffering to be able to get to the point where you can answer that question, sometimes

you may not even do it at all.

So the less impedance and the less friction you have in your tools, the faster you can

sort of iterate and ask different questions and analyze your data.

And this will hopefully lead to more creative work and better insights into your data.

So one interesting analysis, how many of you use the Stack Overflow website?

Most people, yeah.

So Stack Overflow has gotten much more popular over the last few years, and I think primarily

because people find that they can get answers to their questions really quickly, sometimes

in minutes.

The number of people who are actively trolling Stack Overflow and answering questions is

pretty remarkable.

People have an incredible amount of time on their hands.

So I was interested in looking at, you can query all the data from Stack Overflow about

any particular topic.

So I downloaded all of the Python Stack Overflow data for the last, since the beginning of

2009.

And I was interested in looking at, just based on Stack Overflow, what can we see about what's

going on in Python and the whole world.

So let's do that.

So I'm inside the IPython notebook.

So if no one has ever seen this thing before, I'll give you a very brief teaser about it.

So the idea with the, if any of you have ever used Mathematica, this will be very familiar.

I think it was modeled on the Mathematica notebook.

And the idea is to be able to have code cells that you can put Python code in.

So if I put print hello world, I'm using Python 2, so I don't need parentheses.

If I put print hello world, what's going on is I'm inside Google Chrome.

So I'm in a web browser.

And the notebook application is running on my local machine.

And I can put a Python statement here, press Shift-Enter.

It sends that code to a running IPython process, executes it.

If there's any output or plots or anything, it captures those and inserts them in the browser.

So if I had, so if I generate some random data with NumPy, so I just generated some

1,000 normally distributed random numbers, took the cumulative sum to turn it into a

random walk, and then I'm using the matplotlib plot function to make a plot.

And so to have this notebook interface is really nice because you can essentially tell

a story with your Python code.

You can also have cells that have markdown.

So I can put stack overflow analysis here.

And so I can put any markdown statements here.

So you can mix text and writing with your code and analysis and build.

People are starting to use the notebook to write books and papers and blog and do all

kinds of things.

So it's a very, very nice tool ecosystem.

So what I did, I'm not going to take you deeply through the code, but I, so I downloaded all

of the stack overflow data into one big, one big pandas data frame.

So if we look at the, look at the tags column in the data frame, you can see that each,

each post, I'll show you what a post looks like, if I can, okay.

So a post looks like this.

So you have a post ID, the date it was created, the person who, the person who asked the question,

and it's, it's title and also it's tags.

So we're really interested in these tags and that's kind of a proxy for what the, what

the question is about.

So this guy asked about calculating harmonic series.

So it's tagged with math and, and Python.

So let's look at.

So what we want to do is to, to take all of these tags and to do some, some aggregate

the data to get some kind of idea about which tags appear the most over time.

And then maybe we can look at some trends and see how things are, what people are talking

about on stack overflow is changing over time.

So I won't, I won't belabor you, but I, I wrote a little regular expression to split

tags into a list of, list of strings.

So made a, a big table called tag table that now has for each post ID a sub tag associated

with it.

Then I can merge that with the, the post table.

So now if we look at this merged table.

So now we have for each post ID and each sub tag, in each sub tag, we have one row

in the table.

So now this is something that we can, that we can aggregate.

So now I'm going to take this merge table group by sub tag, call the size method and

that gives us the count of number of posts by number of posts by tag, order and descending

order and then take the top 500.

So make this a little bigger, gosh, okay.

So this is since the beginning of 2009, these are the top, the top occurring tags on stack

overflow for the whole, for the whole time span.

So as, as you might expect, well everything's tagged with Python, so that's everything.

But then, you know, Django being definitely the most popular Python library is next up.

You know, Google App Engine, NumPy is also up there, kind of shows you, you know, relative

to Django, you know, how, roughly how popular, you know, scientific Python is relative to

web development, regular expressions, Matplotlib, various things on down here.

If we look at the top, top 25, I think I have to go a bit further down the list to

find pandas.

I think pandas is in the top 50.

Yeah, so, so pandas is down here toward the end of the, end of the top 40.

And so this isn't that interesting because this is just, well it is interesting but it's,

it's over the entire, the entire sample of the dataset.

So if we want to look at trends over time, what we can do, first I need to convert the,

the creation date column, which is strings, into timestamps.

So I do that.

And then I'm going to filter down the dataset to just the top 500 tags, just to make things

a little faster.

And then I'm going to group by tag.

And for each, for each subtag, I want to get a count by month.

So for, you know, September 2009, for each tag we would get a, get the number of posts

that occurred in, in that month.

So this is pretty, pretty standard pandas stuff.

I'll show you what this thing looks like.

Okay.

So we have a, we have a big data frame now.

One column per tag, the index, which are the row labels of the data frame.

are time stamps, so going from January 2009

through June 2013.

If we look at...

the Python tag

and then plot that...

so this shows us, um,

the number of posts per month

over the full sample, so you can see, um,

well, Python is getting more popular, but

Stack Overflow is also getting more popular, um,

and then there's this drop at the end, and that's because

we're in a partial month, so

I'm gonna drop off...

just go up to 2013-5-31

to drop off the June data,

so now we don't have that partial month at the end.

And now there's a few interesting trends in the dataset,

um, particularly, you know, between libraries

that do similar things, so you can see how, you know,

the popularity of things has changed over time, um,

and one thing that we want to do is, because you see that

Python questions are getting more popular in Stack Overflow,

so we might be interested in, to see, you know,

what percentage of, um, Python posts are about Django

over time rather than looking at the absolute number, um,

because we're gonna see an uptrend basically in everything,

depending on this overall trend.

So I'm gonna divide everything by the number of Python posts,

and that gives us a percentage.

And so here you can see this is just the percentage

for pandas, so you can see the library, you know,

taking off, and now, you know,

a little over 2% of Stack Overflow questions, um,

in recent times are about Python

or also about pandas.

You can also look at Django and see that,

you know, back in 2010, you know,

almost 15% of questions were about Django,

and then you see Django becoming, well,

at least less popular based on this metric over time.

Something like Flask, which has been gaining in popularity,

um, you can see, well, it's really only about, you know,

percent and a half, but, you know,

getting quite a lot more popular.

Python 3.

If anyone's using Python 3,

you can see generally people not being as excited

about Python 3 a few years ago,

and more and more people are adopting it.

Matplotlib.

Matplotlib also getting more popular over time.

Regular expressions staying about the same.

I think people generally have problems

with regular expressions all the time.

I know I do.

Other things, maybe like IronPython.

So I think a few years ago people were more excited

about doing Python on .NET,

and there was a lot more activity around IronPython,

but it's sort of declining in popularity.

And then there's other, like, things like Twisted.

I don't know if any of you use Twisted

web stuff, so you can look at, you know,

the popularity of Twisted over time.

You know, it had a very more popular period

and it's become less popular.

And Tornado, which is a new library,

you can see appeared in, you know,

late 2009 and has gotten a bit more popular over time,

but still less than a percent of questions.

So this is fairly interesting.

But we might want to look at, you know,

trending tags,

like things that have experienced the most growth

over the last year,

either growth or decline,

to see kind of what's moving and shaking in Python land.

So I'm going to go back to my data aggregation,

and rather than resampling by month,

I'm going to go by year.

Of course, that doesn't want to work.

Oh, great.

Let's try A.

Okay.

So now we have data

annually.

So now you can see this is...

So we'll just look at this

graphically, make a bar plot of

Python posts.

So here we're looking at...

This is a partial...

This is a partial year.

But we can...

Let's just look at Django.

And now I need to do...

I need to do that normalization thing again

so we can look at percentages.

And feel free to have at the data yourself

so you can find.

So if we look at norms Django...

So here is the Django plot

over time.

This is 2013, 2012.

And if we take just this time series,

there is a method percent change

that gives us the year over year change

on a relative basis for each year.

And so what we want to do is do this

for every tag

and then find the top 10

and the bottom 10 to see what's changing.

So I'm just going to do that.

So we're going to call percent change

on the entire data frame.

I'm selecting the percent changes for 2013.

So let's call this

what's happening 2013.

Order by value.

This doesn't look good.

This might be a bit distorted

because we don't have the counts here

so we might want to...

Well, these are the top 500

so it should be fairly accurate data.

So...

Let's get the downtrends

and then the uptrends.

Okay.

Yeah.

So here's the uptrends.

So this is maybe some things you might expect.

In particular, you know, Raspberry Pi

has gotten super popular.

How many of you own a Raspberry Pi?

Very cool.

You know, Python 3, getting more popular.

pandas getting more popular.

Python, Scikit-learn.

We can see, you know, Flask and Node.js

also getting a lot more popular.

People using Python in a web system.

IPython getting quite a lot more popular.

And in the downtrends...

I don't know if there's anything.

It would also be interesting to look at the counts here

to see how many posts overall there were.

There was a real...

So metaclasses and metaprogramming,

I don't know if you noticed, there was a big...

People just couldn't stop talking about metaclasses

for a couple of years there.

So when I started to look at this data,

somebody said, oh, you should look at, you know,

how much people are talking about metaclasses.

And so you can see that, you know,

the number of Emacs questions down 40%.

So people are not big Emacs fans anymore.

Let's see.

I mean...

Down 20%.

So just people aren't asking about text editors, you know.

Maybe, like, sublime text is in here.

Sublime text 2.

All right, plus 37%.

How many of you use Sublime Text 2?

I don't, but it's a very great text editor.

All right, so as you can see, there are some things

changing, happening in the Python community.

There are, I guess, more general, broader trends in

technology that we can talk more about.

And I just wanted to comment on a few of them.

So generally, with the growth of web technologies getting

better, web browsers getting better, there's more and more

of a push to putting things in browser-based interfaces,

things like the IPython Notebook, putting the

computation in the cloud rather than on

your local desktop.

Essentially being able to do computing anywhere.

Now that there's the Chromebook, being able to

essentially have a computer just be a view on some remote

computation in the cloud and to not have to do anything

locally anymore.

And you can imagine how this would be beneficial.

I'm sure you've all experienced headaches with

deploying, installing software on your computer.

And you could solve that problem by having everything

be handled by somebody else in the cloud and not have to set

up your own machines.

I've suffered a lot from that myself.

One of the things that's also pushed people to do more data

stuff on the web and in the cloud is that web graphics has

gotten a lot better.

So I don't know how many of you do JavaScript.

Anyone use D3 in here?

So I'll show you a couple D3 examples.

So generally, three or four years ago, it was much harder

to do a lot of interactive visualization on the web just

because there's Internet Explorer.

And so you'd write JavaScript code, and it would work in one

browser and not at another.

So with more and more, the web technology becoming more

standardized, you can have more confidence that you can

build something once, and then it will run everywhere.

There's been a lot of talk about, like Calvin was saying,

about big data.

People are also starting to talk about whether big data is

overhyped, which I think is probably true.

But big data is still an important trend and one worth

paying attention to.

I guess the other thing I'll talk about very briefly is

just-in-time compilers, making Python faster, making

languages faster, generally speeding up computation.

And I would say that the big challenge for Python over the

next four or five years, especially with the big push

toward the web and toward the cloud, is how to keep Python

as an important and relevant language that people want to

program in and that they can use to build systems in the

way that they need to be built for the future.

I don't know that I know the best answer to this.

I have some ideas, but I think this is going to be something

that we all have to pay a lot of attention to.

Hopefully, we don't have to give up on Python and just

program in JavaScript, because that would

make us all very sad.

But there is something very alluring about being able to

do all of your data analysis on the web, to be able to

build something in one place, share that with anybody,

access your data and your analysis, and to be able to

ask and answer questions very quickly from any computer in

the sense that sites like Bitbucket and GitHub and nice

sites for software development have really revolutionized

collaboration on software projects.

I'm very hopeful that the same thing will happen

for data analysis.

There's really not that kind of thing.

It's still very much, here's my code on GitHub and maybe a

link to the data, and you can reproduce the

analysis in that way.

So I'm very interested in this problem.

One of the big issues is that implementing all of the data

processing in JavaScript is a pretty tall order.

I've written quite a bit of analytics code in JavaScript,

and it's really just JavaScript is not meant for that.

The other problem is that you're not going to process

all of the data in the browser.

So whenever you're working inside a web browser, you have

to only be looking at small subsets of the data.

And so that really complicates your system.

You have to do data processing on the server side and be

interacting with only a small subset for

visualization.

But on the other hand, your brain can only look at so much

data at once.

So even if you had a whole giant pile of data in the

browser, you wouldn't need all of it in there at once.

The other problem, of course, is building

interactive applications.

You get very used to having a desktop application.

You press Enter, the code runs, the results happen

immediately or as soon as they run on your

laptop or your desktop.

But when you're on the web, you have to think about server

round-trip time and cloud storage and how data moves

between machines.

And it becomes a lot more complicated.

So of course, web graphics has just really had a renaissance.

Well, there really never was a birth before.

So it's really had a fantastic growth of really

nice and compelling visualizations on the web.

The main technologies that are driving that

are SVG and Canvas.

The big SVG library that everyone uses, it's a vector

graphics library for JavaScript, is called D3.

It stands for Data Driven Documents by the venerable

Mike Bostock.

Let's see if I have a couple of examples here that I'll

jump to in a second.

So with regard to JavaScript, I think in order for Python to

really stay relevant, rather than saying, no, I'm not going

to program in JavaScript, I think we have to build

interfaces to JavaScript and to the web technology so that

you can keep your serious work in Python.

But then whenever you need to build a visualization or you

need to send those results of something that's happening in

Python to the web, that you have a nice way to do that.

And that you can enable other people to get their data and

analysis on the web.

And there's been some really great examples of this.

So what I've already showed you, the IPython Notebook,

essentially it runs in the web browser.

It's a big JavaScript application.

And now when you look at the IPython project, it's become

not 50%, but a lot of the code in IPython now is in

JavaScript, which is not something I think the IPython

guys would have predicted a few years ago.

Another great example is the RStudio IDE.

Any RStudio or R users in the room?

All right.

So RStudio, it's been around for about three years and

maybe four years now.

But it's an IDE for R programming.

And so it's got graphics and a shell down here.

So that's R code, so graphics and all this.

But the really amazing thing about this application is that

even though it's running on my Mac and looks just like a

normal application, the folks who build it, JJ Allaire and

Joe Chang and others, they build it entirely using web

technologies.

So this exact same application could be run inside the web

browser, but users of it would never know that they're

looking at a web application.

So it's pretty brilliant.

And I think it's a model for the future of being able to

have applications that can run either locally on the desktop

or can run inside the web browser in the cloud and to

just not know the difference.

So you don't have to make a choice of whether you're going

to be in the browser, in the cloud, or

local on the desktop.

Another thing that can really help is building integrations

between libraries like pandas, like data and analysis tools,

and charting libraries like, well, I'll show you a couple

of examples here.

There's a fellow in Portland named Rob Story who's got some

libraries for integrating pandas with Java.

JavaScript libraries, so here's one example using the

library vega.js, which is a pretty new package.

And making a bar chart, I think, I don't know if this

uses pandas data, but no, this is just using vanilla, sort of

raw Python data.

But this chart is not generated by Matplotlib.

It's rendered in the browser, and this is vector graphics.

And here's an area plot, and here's a line plot.

And I think this is generally a good idea, especially when

you have things like the IPython notebook, which you

run in the browser, makes it a lot easier to incorporate the

cutting edge developments in JavaScript land.

Here's another example, also by Rob Story.

He has another project called Folium, which is as soon as

this loads.

And it integrates pandas with a library called leaflet.js,

which is a mapping library.

So this is some data about the US that's being overlaid on a

map, and the legend up here.

And so I can zoom in on this, and it doesn't

give me tool tips.

So this is interactive JavaScript visualization that's

being fed directly by data from pandas.

There's other libraries like ChartKick.

So it's actually a Ruby library.

There's a Python one now.

And the idea is to have very simple Ruby or Python code

that makes it easy to take data in those languages and

build interactive JavaScript visualizations.

So each of these charts, one line of Ruby.

There's also the equivalent Python interface that gives

you the same thing with one line of Python.

So if you need to get graphics in the browser and you want to

use Python, these are good options to consider.

So I think a lot about generally what makes the

perfect data language.

And as much as I love Python, I'm not completely convinced

that Python is it, but it's pretty good.

And I think it's gone quite far.

And I've been very happy using pandas, and people so seem to

be a lot of other people.

But I think there's still work to do.

And some of the problems have to do with low-level concerns,

things like missing data, so designing all of the data

structures with missing data in mind.

You want to spend most of your brain cycles thinking about

what you're doing with the data rather than how you're

going to do it.

And that often boils down to nice APIs and clean syntax.

So one of the big problems with R is that the syntax and

the language itself often gets in your way.

And that's one of the reasons why I wanted to do Python way

back when, but there's even things that are a bit hard to

express in Python.

And using SQL is nice for certain kinds

of data operations.

But yet there's a lot of things where writing SQL

queries is not a particularly good way to

express what you want.

So I think we haven't quite got there yet.

But I think a lot of what you need, the core built-in

operations of grouping and sorting, doing set logic and

filtering, and all of that, all of that needs to be there

and needs to be fast and really easy to use.

So another important trend, especially on where the

computation is happening, is more and more projects are

being built on top of just-in-time compiler

technology.

So if you're not familiar with what a just-in-time compiler

is, the idea is that you have a framework that can take a

high-level description of an algorithm and generate fast

machine code, assembly code, on the fly.

So that sort of steps around the traditional, if you wrote

C code, you would write that C code, compile it, and then run

it, but if you need to generate a custom function on

the fly that's optimized for a particular specific

application, you wouldn't want to generate all of those.

You could end up with millions of combinations of

specialized functions that you might want to compile.

So having a tool chain like LLVM enables you to build

custom functions and then generate very, very fast code

that's every bit as fast as if you wrote hand-coded C code.

And one of the really great things about these tools is

that you can write, there's a tool called Numba, which came

out in the last two years.

I think last year, really.

And it enables you to write Python code, and then the

Numba tool chain uses LLVM to translate that Python code

into machine code.

Essentially, it's about as fast as if you wrote C code.

Sometimes it's faster.

There's another language called Julia, which is a new

scientific programming language, and it's built

entirely on top of everything you write in the language gets

passed through the LLVM compiler tool chain.

So all of the code is compiled on the fly and is very, very

fast as a result.

Some of you are probably familiar with PyPy, which has

its own just-in-time compiler tool chain.

And that team has really done some amazing work, squeezing

performance out of Python, doing optimizations that

people never thought were possible.

There's other projects.

I put up here a project from Cloudera, which is a big data

company in the Bay Area.

And they built a project called Impala, which is

basically a database engine or a SQL engine

on top of Hadoop.

And part of where it gets its speed is by using LLVM to

take SQL queries and generate really fast, specialized

functions that process the data.

And I think that sort of thing is going to be the model for

the future.

Now, in big data space, the big trend in the last two

years is to do SQL everywhere.

So I brought up SQL a couple of times.

I was going to write up here, on here, SQL all the things.

But this is actually a pretty interesting set of benchmarks

that came out.

I don't know if any of you can read this, but there's a lot

of competing SQL interfaces to big data.

So this was a set of benchmarks that was done

comparing Hive, which is Hive was developed at Facebook.

And it basically takes a SQL query and converts it to a

MapReduce job and runs it on Hadoop.

It works, but it wasn't built for performance.

So it's pretty slow.

So a lot of people have been building

replacements for Hive.

So this was done by the Spark team from Berkeley.

And they have a project called Shark, which is Hive on Spark.

And they were comparing that with Impala and also Redshift,

which is a big data SQL engine that came out about six

months ago, well, within the last year, from Amazon that

runs on Amazon Web Services.

So basically in big data land, there's a big shootout going

on to who can build the fastest SQL engine for big data.

And so it's very interesting to pay attention to.

And a lot of it's just doing pretty simple

group by aggregations.

But it turns out that that represents a lot of business

use cases.

So basic conclusions that I have for data tools and where

things are going, I think we all have to embrace the web.

It's where things are going, the web and the cloud.

The desktop model of computing is really on its way down.

In the future, it's going to be tablets and your phone.

And well, I guess the tablets are shrinking in size.

The phones are increasing in size.

So I guess at some point, we'll just have one device

that we occasionally hold up here.

And sometimes we type.

So device consolidation, the user interfaces, those need

to get worked on, of course.

How do you build a data analysis interface for touch?

I don't know that I really know the answer to that.

with data tools there's still a lot more work to do. I think tools like pandas are a good

step in the right direction and I think have made people a lot more capable and productive

in working with their data. But it's definitely worth examining, especially when you're working

with data yourself and you run into something that is tedious or takes you a long time or

you can't figure out how to do something, write that down and tell people about it and

open an issue on GitHub or write an email to the mailing list to tell people the problem

that you ran into and tell them about your use case and what you see as roadblocks or

problems with the tools for your particular problem. And I think the more that the open

source development community understands problems that people are experiencing in the real world

that really helps everyone make good design decisions and new thinking about the tools

and how to make them better. And of course I think big data is here to stay. The Python

ecosystem is definitely good for medium data. Python really hasn't had mainstream success

in big data. So if we go back to this benchmark page, the same project that the team that

made these benchmarks for Shark, for the Spark project, there's now a Python interface to

Spark so you can write functions in Python that process big data. So to the extent that

we can build bridges to the big data ecosystem so that we can get more people programming

Python and processing big data with it, I think that will also help Python stay relevant

because the data is not shrinking in size. Maybe in two or three years we'll all decide

that all this data, petabytes of data that we're warehousing isn't really worth much

and we should just start throwing it all away. So yeah, that's my talk. I really appreciate

you having me here and I'll have some time for some questions which, you know, happy

to comment further on any of these topics. Thanks. Yeah. Oh, could I have the mic? Yeah.

Thanks for the talk, guys. Once again, you did the Python conference in New York for Finance last month. Can you tell me what is the update in the Finance area?

Sorry, could you repeat the question?

You did the Python conference in New York for Finance. So can you give an update on the

use of Python in Finance? Thanks.

Yeah, so the question is how the use of Python in Finance is changing or doing generally.

So Python has become really, really popular in Finance in short. When I started using

Python in 2007, people thought I was crazy. They were like, this is not a serious language,

you can't build production systems with this, the only real choices are Java and C++.

So now everyone is hiring Python developers as fast as they can for doing financial work

and I think that organizations have seen the productivity benefits both in their system

maintainability, developer happiness, and being able to get more done with fewer people.

And also, because the libraries have gotten a lot better, people are, big financial firms,

even like big investment banks, JP Morgan has, I don't know if any of you work for JP Morgan,

but they're big Python users. Bank of America, I know folks at UBS and Goldman Sachs,

and really all the banks, people have really taken to Python.

Scala, which is a Java JVM language, has gotten a lot more popular in Finance as well,

so I think the two big trends there are in Python and Scala in Finance.

Well, I'm not in Finance anymore, but I'm excited to see Python doing well there.

I was wondering whether you could go into more detail about the collaborative effort.

Right now, these tools like Python, Node.js, they're very cool as a single user kind of thing,

and of course everybody has their GitHub repository, but is there anything on the horizon

that you can see where you can actually make collaborative work with other organizations here?

Yeah, so my friends over at Continuum Analytics,

they've built a hosted IPython notebook environment that,

I think there's a free plan on here, so let's see,

there's a free plan and then there's paid plans that hosts IPython notebooks

and enables you to share notebooks among a group of collaborators.

There's also, and they have a lot of other tools there for like environment management

if you want to build like custom environments and all that kind of thing.

There's the NBViewer site, which is a place to,

you can upload an IPython notebook someplace, like on Gist on GitHub,

and then generate a link on NBViewer and then send that out

and so you can get a static view of an IPython notebook.

So that also helps with collaboration.

There's no multi-user version of the IPython notebook.

I know that the IPython team, they got a big grant,

like a million dollar grant to work on IPython for the next two years,

and so they're pouring a lot of resources into improving the IPython infrastructure

to be able to more easily integrate with JavaScript libraries

and building interactive widgets and things within IPython.

And I think they're also hashing a plan for like a multi-user IPython notebook

because what you really want is something that's kind of like Etherpad

or any of those kind of collaborative text editors on the web

and to be kind of both looking at an IPython notebook

and working, collaborating in real time on a project.

I think within two years we'll have it, but I'm not sure exactly when.

man in audience speaks

Why is Python getting more popular?

Well, I don't have complete information

about why Python is getting more popular,

but I would say that the libraries have gotten better,

both in the analytics, like Scikit-learn for machine learning,

stats models, pandas for just general data work,

and that's brought a lot of people to the Python ecosystem.

Sort of the web development libraries have gotten better,

so more and more people are...

Well, really, I think maybe Ruby has won in web development.

Like, there's a lot more Ruby developers than Python developers,

but generally there's a lot more people doing web development

and building websites with Python.

There's also a lot of refugees from Java and C++

that have maybe some of them in the room.

I programmed in Java before I did Python,

so I think more companies are becoming more comfortable

building software in interpreted languages than they used to be.

Like, people have embraced unit testing and dynamic types,

and people used to be a lot more uncomfortable

with not having static types,

and so more mainstream acceptance of dynamic languages

has definitely made Python more popular.

I'm doing scientific research,

and in my area, most of the people, they use pandas.

And if I introduce Python to all these people,

they will wonder what Python can do,

and I tell them Python can do nearly everything.

But it's not very specific.

It's like with pandas, you can clearly see

any linear things you can solve.

All you need is R.

You can think about statistics.

Don't you think there are too many entities

and too many functions?

So, yeah, I think one of the main things that's holding back a lot more MATLAB users from

moving to Python is mainly the development environment.

People really love, like, the MATLAB IDE, the profiler, the debugger.

You know, the R community has been essentially solved that problem in a lot of ways with

RStudio, and so I would be very interested to see, you know, the equivalent of RStudio

in Python.

I think that would help kind of really, you know, drive the nail in the coffin on MATLAB

a bit more.

But yeah, I think, you know, you can do pretty much all the things you can do in MATLAB and

in Python.

You know, some of the library is a bit rougher around the edges, but I think the benefits

that you get from, you know, better data structures, you know, object-oriented programming, tools

like pandas, which help with data preparation, you know, I think they do bring a lot of benefits.

So maybe if you want to sell more people on switching away from MATLAB, like, look at

their code and find the places where they're kind of having to, like, really hack their

way around limitations in MATLAB and show them a better way.

And I think once people realize that they can be, you know, by switching their technology

they can make themselves, like, more productive and, you know, be able to get more done.

So I think they see, you know, okay, well, if I program in Python, then, you know, I

can get more research done, you know, kind of the benefits become, yeah.

Well, my real question is, like, why there are so many pieces in Python?

I mean, Ruby is quite relevant.

You think of Ruby on the real line, the only free one.

But in Python there are too many choices.

Yeah, there's a lot of fragmentation.

Well, at least it's easier to install now with things like, you know, Anaconda, which

is, like, a free, you know, scientific Python distribution.

So, you know, with a few clicks you can have everything installed.

That used to be the big barrier.

It's like, oh, I've got to install, like, 50 packages before I can, like, make a plot.

So that definitely is easier.

But the library, you know, the multiple library problem, I guess I don't really have a good

solution for that.

I think, you know, with pandas what I've tried to do is to integrate multiple libraries and,

you know, be able to access.

If you want to make plots, you can make plots without knowing anything about Matplotlib.

You can do array computing without knowing deep information about NumPy.

So that, you know, you essentially have to learn one set of integrated tools.

And, you know, I don't know what problem domain you're in.

But I think generally, you know, to build a set of, you know, domain-specific sort of

tools and helper functions and utilities that help kind of, you know, reduce the amount

of, you know, having to use, you know, eight different libraries to solve a problem.

Yeah, I don't know.

It's a problem with open source.

You know, you've got a very highly distributed development community rather than, you know,

kind of the math works in Needham, Massachusetts.

You know, building a tightly integrated development environment.

I guess rather than asking for fewer libraries, I think that's for one more or actually about

one more.

You had some good examples of the web technologies that are sort of in the space of G3 for JavaScript.

And some of those things that basically create SVG Canvas as alternatives to Matplotlib.

So is there, I mean, when I was looking at it, I was thinking, well, not Python, but

wouldn't you want to just, wouldn't the idea be to just overload everything in Matplotlib

with something that generates SVG?

I mean, is there any movement towards that?

So that effectively, once you're in a web framework, you would be generating web graphics

rather than the graphics that are intended for the more traditional web style.

Yeah, so the question is, you know, when you're in, you know, the IPython notebook and in

the browser, like, why not do everything, you know, with web graphics and SVG?

That's definitely the direction that we're going in.

I guess we're just not, we're not there yet.

It's like we need more developers and more people working on that problem.

So, you know, you saw here in, you know, I'm in R and this is made with ggplot2 and doing

these kinds of, you know, faceted statistical graphics, you know, it's very easy to do in R,

but doing this, you know, even with D3 is pretty difficult.

But I think, you know, five years from now, we'll have a set of JavaScript libraries

for statistical graphics that everyone uses.

And we have interfaces to them from R, from Python, from JavaScript.

And, you know, all the graphics is going, is clearly going to the web.

And I think, you know, generating static desktop graphics is going to be

a thing of the past in the long term.

Just it's, yeah, it's just a lot of development effort.

I'm, you know, my company, we're working on a lot of things in that direction

and we'll definitely open source some packages that help with that at some point

once they're ready for people to use.

I have one more question.

There's a problem with Python and the CPython implementation

in GIL. So the question to me is, how does that affect data processing?

Yeah, so the concurrency issues in Python,

if you're doing data processing, that can all be done, you know,

in a multi-threaded way, you know, that releases the GIL and

you just have to kind of design carefully for that.

Like if you're using, I'm a big fan of Cython for writing

numerical codes. And Cython has, you know,

[1:00:00] a version of range, PRange, that will parallelize a for loop.

[1:00:04] And so as long as you're not accessing any Python data structures inside the loop,

[1:00:08] just doing numerical computing, then you can have truly multi-threaded code.

[1:00:12] If you're doing, you know, well, if you're doing

[1:00:16] a lot of IO stuff, then, you know, the GIL is not really an issue

[1:00:20] because the GIL gets released. But there are occasionally things

[1:00:24] where the GIL does get in the way. And it is a long-term liability.

[1:00:28] So it's something I do worry about.

[1:00:32] Yeah, thank you very much.

[1:00:46] Thank you very much.