---
title: "Keynote: My Data Journey with Python |SciPy 2015 | Wes McKinney"
summary: "Video at SciPy 2015"
date: 2015-07-09T00:00:00
tags: ["video", "transcript"]
slug: scipy-2015-keynote-my-data-journey-with-python
word_count: 8259
source_file: transcripts/2015-07-09-scipy-2015-keynote-my-data-journey-with-python.md
content_type: transcript
event: "SciPy 2015"
video_url: "https://www.youtube.com/watch?v=kHdkFyGCxiY"
---

{{< video https://www.youtube.com/watch?v=kHdkFyGCxiY >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This SciPy keynote traces my path from mathematics graduate to pandas creator.

## From Finance to Frustration

In 2007 at AQR Capital Management, a $40 billion hedge fund, I encountered data analysis realities. Complex mathematical discussions could be summarized in 30 minutes, but executing the work required months of data munging in Excel and SQL. This gave me "an allergy to anything that harms productivity."

The Python ecosystem in 2008 was different. NumPy, SciPy, and Matplotlib existed but were "bleeding edge stuff" focused on replacing MATLAB in academic research. Critical gaps existed for business analytics: no robust statistical tools, poor missing data handling, no SQL-heavy workflow support. "All of the things that were most relevant at a core...were not core concerns of the community."

## The Proto-pandas Moment

I discovered Jonathan Taylor's experimental port of R's statistical models to Python. Though unreleased, it provided the statistical foundation I needed. But to use it effectively, I required better data structures for time series and relational operations—what became pandas, initially "the AQR time series library."

At AQR, introducing open source tools was risky. I described it as being "short a put option"—if the software failed, blaming open source developers wouldn't save my job.

## The Pivotal Year

After pandas was open sourced in 2009, it remained niche until two events in 2011. Enthought convened developers to address fragmentation in Python's statistical tools. I argued for integrated solutions rather than "a federation of loosely connected components." Consulting work revealed data analysis problems weren't unique to AQR.

Recognizing that "someone has to be the chicken" in the chicken-and-egg problem of tool maturity, I took leave from graduate school and spent my finance savings to work full-time on pandas for a year, willing to "go broke over it." Working with companies like AppNexus, I came home with lists of missing functionality, then coded from 6 PM until 2 AM.

## Community

John Hunter encouraged me to "forge your own path" when others pressured me to work on NumPy instead. The IPython team and Stats Models developers provided collaboration and support.

A train conversation from Seattle to Portland about Python and the IPython notebook turned out to be with Titus Brown, later instrumental in securing IPython's first funding.

## Looking Forward

Now at Cloudera, I focus on scaling Python for big data while fostering collaboration across languages. I argue that "R versus Python versus Julia...language wars" are counterproductive, advocating shared toolkits for common problems.

My technical focus: LLVM and JIT compilation as the future of data processing, hoping for "a no-JVM future" where "LLVM and JVM live in perfect harmony."

## Key Quotes

> "This whole formative experience kind of imbued me with this sort of allergy to anything that harms productivity, or that prevents you from expressing your ideas in a concise way."

> "You're short a put option. So if you use a piece of software, and it ends up causing bugs that are not your fault... blaming the open source developers is not a valid excuse."

> "All of the things that were most relevant at a core, like the things that were going to solve the problems I had, were not core concerns of the community."

> "Someone has to be the chicken, and it might as well be me."

> "I was willing to go broke over it. Like, it was that important to me."

> "I would come home from a day at AppNexus with this long list of, these are all the things that need to get built in pandas. And then it would be like 5 or 6 PM. And then I would work from 6 PM until 1 or 2 in the morning."

> "Forge your own path. If you need to do your own thing, don't worry about it. It'll all sort itself out, and as long as the software that you're building is useful."

> "The R versus Python versus Julia, like the data science language wars is very counterproductive and I think has impeded progress in certain ways."

> "I'm kind of hoping for a no-JVM future. I don't know if we'll ever see it, but LLVM and JVM living in perfect harmony would be really exciting."

---

## Transcript

Thanks Eric for the introduction and thanks to Enthought and all the organisers and sponsors

of the conference.

This is my fifth SciPy, I missed one in the middle.

My first was in 2010 and I have been to all but one since then, so it's great to see the

community grow.

There are a lot more Python programmers and also folks tackling a lot more diverse use

cases than we were five, six years ago, so that's really exciting to see how the language

and the community and the software has grown to be useful in a lot more areas of work.

Thanks also for getting up, I'm on Pacific time so this is early for me, so at this time

yesterday I was sleeping so I promise I'll watch Chris Wiggin's keynote, I think the

video is probably already up but you know how that goes.

So this is a little bit different than my normal talks which are more like focused on

pandas and specific details of pandas versus the rest of the data tools, other programming

languages.

I work at Cloudera now so my life is more about big data than it used to be, but this

is a bit more of a retrospective on my own experiences and maybe some thoughts on where

we've been, where we're going and we can talk more about that, maybe have some questions

at the end.

So I've been up to, well, a lot of things, I guess these things just kind of happen as

time passes that you move from one thing to another, at least I did.

So I've been involved in a number of different Python projects, I've worked in a number of

different places, studied a couple of different places, so we'll talk some more about those

things.

This is really covering 2007 to the present, things that I was up to, talk about how things

have gone well, which is really a testament to the community and talk a little bit in

brief about what I'm personally focused on right now and what I see as some of the opportunities

for the community to continue to grow and flourish.

So whenever you come to one of these conferences, it is useful to look around at the people

at the conference and say, well, what brought you here, how did you end up here?

And I know I often ask myself the same question, the odd sequence of events, kind of the butterfly

effect, if you could trace it back to how could I end up on the stage at a scientific

Python conference back when I knew very little about Python eight years ago.

I think the common thread that brings us all here is Python is helping us solve our problems.

Some folks here are core developers on many of the projects that you use every day, you

know, the pandas core team, a lot of them are here, Jeff Reback, the project leader,

Philip Cloud, Stephen Hoyer, who is building not exactly an offshoot project of pandas

but a reimagining of pandas for climate data and sort of a different set of use cases,

but definitely sort of stemming off of the experience offered by pandas.

There's a lot of the NumPy core team is here, people who built NumPy, people who built SciPy,

so it's really exciting to bring together people from industry who are using Python,

learning more about Python, how to use Python more to solve their problems, along with the

people who are building the software.

It's incredibly important that we bring those two groups of people together so that if you're

just using the Python data stack, the scientific Python stack on a day-to-day basis, that you

can tell the core developers about, you know, what's working well, what's not working well,

what if you ran into a problem where you ended up down a rabbit hole and had to spend three

months building some custom solution to fit your problem, that can often speak to a limitation

in the tool set and telling those stories to the folks who are at least part or full-time

working on the open source software is incredibly useful and none of the software that we have

here would exist if not for those use cases and those real world applications.

So before I started programming in Python in 2007, 2008, I really wasn't much of a programmer.

I got a math degree and I didn't do a lot of programming in college and so people talk

to me now and they're like, Wes, what happened, you were writing proofs in 2006 and now you're

mostly writing Python code.

It was mostly, I think in retrospect, a matter of exposure that I'd never really seen Python

programming, didn't know any Python, didn't really know any Python programmers.

The one anecdote that I had about Python is I was taking the intro algorithms course

at MIT and we had a dynamic programming problem on one of the problem sets and because I'd

taken a Java course and so I wrote the solution in Java and it was like a couple hundred lines

of Java at the end of the day, it wasn't a very complex dynamic programming problem and

a friend of mine said to me, she said, well, I'm going to write the solution in Python

and I bet you it doesn't exceed 30 lines and I just said that's crazy, clearly there's

no way that the solution to the problem can be that short and one of the TAs published

a solution to the problem in Python and I said, wow, this is crazy, it's so short.

This was in 2005, I think and it just didn't really click with me at that point and I continued

onward writing proofs and getting a math degree.

I also had no exposure to any data analysis or analytics really of any kind, so I'd never

written a SQL query, I didn't know what R was, I actually never heard of R until I was

working at AQR.

I was kind of within this very sheltered bubble of technology and science when I was at MIT,

so let's just say that joining industry was a bit of a rude awakening.

I got a job at AQR, which stands for Applied Quantitative Research, so if you follow the

hedge fund industry, AQR was started by Cliff Asness, who was one of Eugene Fama's grad

students at the University of Chicago, so Eugene Fama, I don't know that he's won the

Nobel Prize yet, but he's always on the short list for the Economics Nobel Prize for the

Efficient Market Hypothesis, but I think that the Efficient Market Hypothesis is a bit on

the down these days, since a lot of, I think it's more for political reasons than anything,

but they were at Goldman Sachs, they were running the hedge fund operation at Goldman,

they spun out in 1998, started AQR, eight or nine years later I got a job there because

there were a lot of math folks who had gotten jobs there and I was looking for applications

of math and so I got a job at a quant fund.

But it was an interesting environment, while there was a lot of math and a lot of research

involved with the asset management process, the whole company really at its core ran on

SQL and Excel, and I'd hardly used Excel at that point, so that was also a bit of a trial.

The systems that built the models and ran all of the, computed the buy sell orders were

all written in C++ and Java, there was development in all of the standard compiled programming

languages that we all know.

There were a number of folks who'd come from economics departments who had PhDs, and in

PhD, economics and finance departments, even today, are still very much about MATLAB and

R, and depending on the department, it'll either be more MATLAB or more R. I think that's

beginning to change and you're seeing more Python, but at least at that time, the message

was if you're going to do some research not in C++, then you should use MATLAB.

I had a bunch of projects my first year that involved some of them were more analytics

that were more about summarizing data that was found in, you know, all of our data was

in a Microsoft SQL database.

So you would pull data out of the, you know, your workflow would either be do all of your

data analysis in the SQL database, which you would end up with, you know, 100, 300 line

SQL queries, or you would pull some of the data out, you would write a simpler SQL query,

you would pull the data out and then either analyze it, usually in Excel.

But if you were using MATLAB, and you could, you know, analyze the data in MATLAB.

The group that I was in had had someone who with with our experience, and so that that

team, the credit derivatives team was doing a lot of our programming.

And so I was introduced at that time to this very strange programming language R, which

at that time was quite a quite a lot different than it is now.

Kind of surrounding all this was he was huge amounts of Excel.

So you know, if you didn't sort of mechanically end up with all of the Excel shortcuts and

in your hands, you know, after a year, so you just weren't getting very much done, because

most of your life was moving data around in Excel, you know, copy and pasting special

values and all that sort of thing.

But the thing that really that really jumped out at me is that I, I felt like I was spending

a lot of my time dealing with just data munging, moving data around, cleaning data, normalizing

it, you know, lining up, lining up data and spreadsheets.

And, you know, these were data analysis projects that were that could be discussed, you know,

in a half hour meeting where they weren't, they weren't really very complex and the details

of you know, what data is coming from where and what do we need to do with it?

And what are the deliverables for the project?

They were very easy to talk about, but actually getting them done was a whole lot of work.

And so that was, you know, I think this whole, you know, formative experience kind of imbued

me with this sort of allergy to anything that anything that harms productivity, or that

prevents you from expressing your ideas in a concise way, so that you can, you know,

hopefully your code will keep up with your thought process about the problem as much

as possible.

And that rarely, that rarely occurs, but certainly it should be better than 95.5.

I mean, maybe it should be like 80.20 would be, would be a better, would be a better situation.

And so I had gotten exposed to Python, one of my colleagues had had written a couple

scripts for, you know, for, you know, odd jobs, you know, nothing really, no scientific

Python, like nothing really, nothing heavy duty, but I had gotten introduced to the language

and it was very alluring, because it's like, wow, it's like readable pseudocode, you know,

the same thing that I'm sure brought a lot of people in this room to Python in the first

place.

And I discovered at the beginning of 2008, like, wow, there's this whole numeric and

scientific computing community who are, you know, solving research problems and doing

fast numerics in this interpreted programming language that's really easy to write.

But it was, it was a very different time.

So you know, you look at today, we have very mature tool sets, you know, projects that

have been around for, you know, more than, more than 10 years, NumPy is going to have

its 10th birthday next year, you know, SciPy is getting on, you know, might be about 15

years old or so at this point, you know, Matplotlib's been around since 2002, I think, IPython around

the same time.

You know, all these projects have, you know, they've been around for a long time.

But if you fast forward, or if you go back in time to 2008, you know, these, this was,

this was bleeding edge stuff.

And you know, you have to remember, I was in a financial firm, where, you know, as we

used to say, you know, you're short a put option.

So if you use a piece of software, and it ends up like causing bugs that are not your

fault, it's like, oh, well, there were bugs in this open source software that I was using,

you know, it was pretty clear, like, it wasn't, you know, explicitly said, you're like, I'm

pretty sure I'm gonna get fired.

Because you know, blaming the open source developers is like, not a valid, not not a

valid excuse.

And that was part of what drove the the use of, you know, tools that came from Microsoft

or that came from, you know, the math works, you know, with MATLAB, is that there was this,

you know, and you can understand, like, we were managing built, you know, billions of

dollars, you know, at that point, you know, AQR had $40 billion under management.

Nowadays, it has well over $100 billion under management.

So there's this, you can understand the risk aversion that if you lose your clients money,

like, you know, your heads on the chopping block, quite literally.

And so you can imagine kind of the apprehension that that was experienced when I started telling

my colleagues, like, hey, let's, let's start doing all of our work.

In Python, it will make us all a lot more productive.

I think people worry first about, you know, what's the downside risk here.

The community was also a lot different at that point.

And I don't, you know, this is not really true.

This is not really true anymore.

But at that point, the battle was quite a lot different.

The battle was being waged in scientific research, it's you were doing your PhD, and you're

telling your advisor, I'm going to do this work in with, you know, Python and NumPy and

SciPy.

And I'm instead of instead of MATLAB.

And so a lot of the work in the community was about, and I think, you know, maybe part

of it was that a lot of the core developers were PhD students procrastinating on finishing

their PhDs.

That's, you know, that's, you know, another story.

But you know, but that was really where the focus was.

And when I, you know, came upon the community, you know, I saw that I'm like, oh, this is

amazing, like, clearly, and I because I had MATLAB users at AQR.

So I was like, well, it'd be great.

I didn't want to program in MATLAB.

And so, you know, the prospect of, you know, having an alternative to MATLAB, at least

was was really exciting.

But in my case, you know, very different, very different use cases.

And so all of pretty much all of the things that were most relevant at a core, like the

things that were going to solve the problems I had, were not core concerns of the community.

I hadn't written any SQL, you know, before I got to AQR, suddenly I'm, you know, my whole

world is writing SQL queries, and I'm spending 40% of my day and SQL Server Management Studio.

But you know, if you look at the proceedings of SciPy, you know, the conference talks and

the papers, there really wasn't there weren't a lot of relational databases, not a lot of

SQL was getting written.

And as it was, and that kind of trickled down to all of the other related problems around,

you know, how do you deal with nulls and missing data?

Using Python for statistical use cases, if you looked at statistics departments, at that

time, it was more about statistics departments were fighting to use R instead of Stata and

commercial statistics, you know, really SAS and Stata, using R as an open source alternative

to those tools.

And you had this chicken and egg problem where there were no statistical tools, or very few

statistical tools in Python, very few statistical tools, and as a result, not very many people

were using it for statistical applications.

And then kind of, you know, your downstream use cases, making graphics that are statistical

in nature, you know, machine learning.

So a lot of the things that we kind of take for granted now didn't really exist.

And the work that I was doing, I fell into this last category of more, you know, unfortunately

analytics has this, you know, buzzwordy connotation means all sorts of things, but, you know,

analytics in a lot of business settings means things that you can do with SQL, but you would

like to write Python code instead of SQL.

But that was not really a thing that you could do well at that time.

So and, you know, also taking in context that I was, you know, let's see, beginning of 2008,

so I was almost 23 years old and incredibly stubborn, and I guess I didn't care that much

about getting fired.

I'm like, well, if I get fired over this, it will make a really good story.

And I was doing an R project, and I'd seen that a professor named Jonathan Taylor at

Stanford had ported a select subset of an important R package to Python, and that's

the MASS package.

And so in particular, I needed an algorithm called iteratively reweighted least...

squares, say that three times fast on a podium, also known as robust linear model for doing

the project that I was doing and the thing about SciPy stats models is that it wasn't

even in mainline SciPy, so I found it in the SVN repo, I think it was in a branch, it might

have been in trunk, maybe it was in a branch but it hadn't been shipped in SciPy so this

was like seriously bleeding edge stuff but I said it implements my model, I fitted the

model and it matches the R results, I can maybe use this, I just won't tell anyone that

it's bleeding edge stuff that hasn't been released.

And so that was, if you go back to what was the hook that gave me a reason to really try

this out seriously, it was really that.

And the funny thing is Jonathan Taylor is a statistics professor and he was embedded

in Stanford which was very much MATLAB and R at that time and still is in a lot of ways.

So I think he was drawn to Python as were we all and so if not for that, I don't, it's

like the butterfly, I don't know how things might be different, I think I might still

be programming in R although quite a lot less happy.

So in order to really use that library well, I needed some kind of data structure or data

wrangling toolkit, I had no idea what was going to be the scope of the project, I had

just the problem that was sitting in front of me and I had a whole big bag of frustrations

from using R and working with time series data, dealing with data from many different

tables, doing all that munging, joining, aligning, normalisation, missing value handling, forward

filling, all that stuff was very difficult to do in R at that time, it's gotten easier

in the meantime, but those were the problems I had, it was financial data and so I tried

to port my R code to Python.

So about a month later, the proto pandas, thousand lines of code, as Fernando Perez

would say, just an afternoon hack, had turned into a useful tool for the particular problems

I was working on and the interesting thing that happened at AQR is we had a case where

we needed to implement a statistical model in production and doing it in C++ was going

to take a really long time, because C++, and so we found with a little bit of research

that we could actually embed the Python interpreter and enable users to write analytics or statistical

computations in Python and extend the legacy system with Python instead of with C++, it's

funny to think back on that project and how hackish and horrible it was in some ways,

we just had to get something running as a proof of concept, but it was this amazing

thing where it was like a Trojan horse that we quite literally opened up inside of this

legacy system and then all of a sudden people realised that they can write Python instead

of C++, well you can imagine what happened, everyone wants to write a lot of Python.

Getting Python adopted in a $40 billion asset management business overnight is certainly

not a thing that happens, so a lot of the work that occurred over the next year was

building consensus around can we use Python in a serious way, can we trust it, can we

trust the open source community, who are these people that are building this software, those

are all the discussions that we had and at a certain point and there was a lot of skunk

works porting existing systems to Python as proofs of concepts, getting folks to use

proto pandas, it wasn't called pandas at this point, it had no name actually, it was just

the AQR time series library.

So there was a lot of evangelism around like don't do Ruby, don't do MATLAB, consider Python,

look at this cool time series tool that I'm building.

So long story short, by the beginning of 2009 we decided to make a serious commitment

to Python and see how it goes.

I'm sure there was always an escape hatch, we'll escape to Java if Python doesn't work

out but it did and it was certainly a lot of work and the things that made it easier

and made it possible, one of the big ones is that we didn't have to re-implement or

implement any core system components, so we were able to reuse essentially pick and choose

components of the scientific Python ecosystem, things like Pytables, HTF5, NumPy, SciPy,

Matplotlib, IPython, those formed the foundation of an interactive research environment and

the thing that was missing was the domain specific functionality, the data wrangling,

the time series support, the things that you needed to build quantitative models for trading.

The other big thing was the interoperability and of course that's a big reason why we're

all here is because it would have been a fool's errand in the late 90s to go and re-implement

all of the legacy code bases that were written in C, C++ and Fortran, you can just bring

them with you and script them from Python, build a nice wrapper layer and the fact that

we were both able to embed Python in a legacy system, that was kind of the step one and

also take legacy components as we would sort of cut away parts that had been re-implemented

in Python, we could wrap those C++ components in Python C extensions so that systems that

just didn't make sense to go and re-implement or there was no bandwidth to port those, either

no bandwidth or it might have been a legacy system that was maybe we'll decommission this

in a few years, we could just wrap those in Python just, I mean it was a lot of work but

it was certainly easier than the alternative, having to more or less throw out a trusted

system that had been developed over the course of ten years.

The other big thing was the fact that the user interface was so much more pleasant and

palatable for the users and I think that when new people come to the Python ecosystem that's

often one of the big revelations, you learn the libraries, you learn IPython, the basic

tools, IPython notebook didn't exist back then but I think now when people discover

the IPython notebook they are like wow how did I get on in life without this, it's like

life was so horrible before, it's like you realise you have been sort of walking uphill

both ways and eating dog food and all sorts of things and you've got a motorbike and you've

got Flamin' Yon and life is just really great, you can spend more time reading the internet.

And so I think from that point onward, the approach to problems would be you encounter

a new problem and be like well can we use Python to solve the problem and I think that

our community is very much the same way and you hope in your companies and any software

project that you should have a really good reason to not be using Python and it's great

that this is now considered a popular belief that Python is the first thing that you reach

for, try to solve problems with it first and have a really good reason to be programming

in Java or C++.

So after a period of time and a lot of convincing, so I think Eric alluded to that, financial

institutions don't like to open source code.

a matter of principle, as any IP is considered to be precious.

And I made the argument that open sourcing would

be a really positive thing for the company,

for recruiting, for getting community development

and involvement in the project.

It's interesting how that played out.

And if I have time, maybe I'll talk a little bit about that.

So I looked, I downloaded, it's on PyPI,

and you can download pandas 0.1.

And it's really small.

You think about pandas 0.16.2 now,

which weighs in at a little under 200,000 lines of code.

And the first version of pandas was a really small project.

There was a little bit of Cython for accelerating

certain algorithms.

But it's a really small library.

And it certainly wasn't the package that it is today.

And it was only useful for a certain small set of use cases.

And I was busy with other things.

And so at the time when we open sourced,

we open sourced pandas.

Developing pandas was not our main priority.

It was suitable for our needs.

It had pretty much everything that we needed.

And so spending a lot of time moving pandas forward

wasn't really a priority.

And in 2010 and 2011, there was just

starting to develop the first kind of whispers

of a statistical community in Python.

So Skipper Sebald, who's here, one of the core developers

of the Stats Models project, the first major version

of Stats Models came out of his, he

was a Google Summer of Code student in 2011.

And that was the first version of Stats Models.

But you go back to 2010, and there was no consensus

about if you need to do data wrangling or analytics,

what should you use?

And pandas was this little known thing

that sat there that wasn't, it was useful, but not

as useful as it is today.

I went to grad school.

AQR, I consulted with AQR while I was in grad school,

mostly to fix bugs and add a few new features to pandas.

But the real story of pandas didn't really

get started until the summer of 2011.

And there were two discrete events

that occurred that led me to get really worked up,

for the lack of a better term.

So the first is that I think that among the literati

and the core scientific Python developers,

the perception that there was some lack of consensus

around data structures and data toolkits

for statistical computing in Python,

that was acknowledged that it was an issue

and that we should talk about it and build some consensus

and figure out a way forward.

mThought flew us all in.

We met for a couple of days to talk about this problem

and figure out how we can solve the architectural issues,

low-level issues with NumPy that we're preventing.

NumPy from being used better, more for statistical computing.

What's up with the data structures?

And my big argument at this time was

that rather than having this federation of loosely connected

components, that we needed to build something that

was more integrated and delivered a better user

experience to the end statistical user who's not

a computer scientist that just wants

to be able to import a library and read a CSV file

and compute some statistics about it.

And you have to remember that at that point in time,

even simple things like reading CSV files were still very hard.

And so I'd gotten more interested in the problem.

I was a grad student, didn't have a lot of time

for open source development, but that was a big thing.

And then I went and spent a couple

of weeks working with a hedge fund that was not

AQR in a consulting engagement.

And I spent a couple of weeks with them.

And I realized that the problems that we had at AQR

were not isolated to AQR.

I think at that time, I had invented this fantasy

that every company had built better software than we had.

And it turned out that it was quite the opposite,

that a lot of companies were still

kind of back in the dark ages in a lot of ways.

And that wasn't necessarily true of the particular company

I was working with, but I think I

heard stories about the general financial industry

and hearing about other companies.

And it felt like it was the time for Python data tools,

and we need to do something about this.

But the issue was maturity, and again, the chicken and egg

problem.

And so it was like the end of May 2011,

or I guess I decided that someone has to be the chicken,

and it might as well be me.

And I think when you're building community

and you're building a software, the use cases

and the real world applications are the most important thing.

And you can't build a useful piece of software

unless you're being faced at least in a nearly direct way,

like you have a consulting project

or you're working in some direct way

with somebody who's suffering from a problem

so that you can ship a piece of software

and then say, well, did that solve your problem?

Did that solve your problem?

And if it didn't, then you have this sort

of virtuous cycle of making the software better

until you're really completely solving the use case.

During the latter half of 2011, I

worked with AppNexus in New York.

I don't even know if I'm allowed to say that

in these consulting agreements.

They're like, you may not talk about AppNexus, Big Python

Shop.

And that was a very enlightening time for me

because it was a set of analytics and data challenges

that was pretty far afield of what I'd encountered at AQR.

And I very quickly realized, wow,

we need to make pandas more or less a SQL replacement as much

as possible.

And there was just a heck of a lot of stuff

that was missing from the library.

And I would come home from a day at AppNexus

with this long list of, these are

all the things that need to get built in pandas.

And then it would be like 5 or 6 PM.

And then I would work from 6 PM until 1 or 2 in the morning.

And then I would wake up and do it all over again.

And so the next year and a half pretty much worked like that.

Making pandas better, evangelizing,

building consensus in the community,

building functionality that you really

couldn't find anywhere else that would also attract

users from other communities.

So the time series capabilities in pandas

still are among the very best.

And that was a draw for our folks,

for really any programming language

to say, wow, this is this amazing time series

tool that also can be used for general relational data

operations.

Like, we don't have to put the data in a database

to do an outer join.

So something I will mention is that part of the reason

that this was all possible was that I found myself in,

you know, it was May 2011.

And I got really fired up.

And I went to my advisor at Duke.

And I said, I have to take leave so I can work on software.

And so I took a year off from grad school.

And I moved back to New York.

And the reason that I made, in retrospect,

it seemed it was a little crazy.

Part of the reason I was able to do all this

was that I had been very frugal when I worked in finance.

And I'd saved up just about enough money

where I was like, well, I can work

on open source for about a year.

But then I'm going to have to figure my life out

on how to support this in a sustainable way.

But I was willing to go broke over it.

Like, it was that important to me.

And I was like, well, I saved this money.

And like, what better, you know, I

might as well spend it on this because it

feels like the thing that is needed right now.

I got a book deal with O'Reilly, November 2011.

I hope to talk a little bit more about the back story.

But there's other things I wanted to talk about.

Needless to say, it's been very successful.

I think a lot of you here probably own copies of the book,

and I certainly never expected it to be so successful.

Fernando, Brian, and John had been putting together

different book drafts in the past,

and we talked about working together on a book,

but they were very busy, I had the time,

and I wanted to make a more pandas-focused book,

and I honestly used writing the book as a way to,

it was like the carrot to make me finish parts of pandas.

So I was like, well, here's an empty section of the book.

I wanna put something there,

so I'd better finish the software.

You know, with any project,

it's not just about sitting down

and hacking out a bunch of code.

You really have to have clarity

about what it is that you're building,

what are the problems that you're solving,

and being faced with those real use cases

is the thing that will help you kind of get there

the most quickly.

And I had a lot of support along the way.

I wasn't working in a bubble.

There were constant conversations

with folks in the community on the mailing lists,

at SciPy, it was a lot of discussion and collaboration,

and honestly, the folks on this list,

and this is not the complete list,

but the folks here at Enthought,

Eric and Travis and Peter,

and the IPython folks and the Stats Models folks,

they were all cheering me on,

and so without their support

and without their use cases and their support,

it would have been really hard for me to do all this,

and certainly being that lone wolf

that's kind of in the cave writing the code,

the real world's not like that.

You have to engage with others

and learn about the problems that other people are facing.

So just to relay a little anecdote,

just to show you how small the world is,

and how, I guess, serendipity does, in fact, occur,

I was on a train from Seattle to Portland in November 2011,

and I had just been in Seattle

and had spent at the supercomputing conference

and had spent a few days hanging out with

and talking about data with Peter Wang,

and the guy sitting next to me sees that I'm in Emacs

and says, well, are you a programmer?

I said, well, yes, I'm a Python programmer,

and he says, oh, I do a little bit of Python, too,

and I said, oh, well, have you seen the IPython notebook,

which at this point was very beta software.

So it turns out that I was sitting next to Titus Brown,

who, if you don't know, is a huge Pythonista

and has been at SciPy many times,

is in the PSF, and a huge proponent of Python

and uses Python in his research lab for,

he believes he's at UC Irvine now,

and as fate would have it,

I'm informed that he was very helpful

in helping the IPython team get their first

dedicated funding for IPython in 2012,

and Fernando claims that a part of that was sort of the,

that I think after that conversation with Titus,

he became a huge convert and proponent

of the IPython notebook.

So John Hunter, who's unfortunately not with us,

was also a big part of helping me along the way.

Part of the reason why I'll single out John Hunter

is he was, after Eric Jones,

John was one of the first people

from the Python community that I met,

and the reason was that in January 2010,

I wasn't sure what I was doing with myself.

I was like, maybe I'll go to grad school,

maybe I'll get another job, I don't really know.

I wanted to sort of move on to some new project,

and I saw that Tradeworks in Chicago, where John worked,

was looking for Python developers.

I said, oh, a finance company that, you know,

has been using Python for years,

and so I flew to Chicago and I interviewed at Tradeworks

and I spent quite a long time with John,

and he and I bonded right away,

and I think that maybe John saw me

as like a 17-year-younger sort of version of himself

in a certain way, and when you go back

to the origin story of Matplotlib,

John was very much kind of the lone wolf programmer,

so I'm going to build a plotting replacement

so that my research lab doesn't have to use MATLAB anymore,

and I certainly identified with that,

and John was often a person that I would email

or get on the phone with whenever I sort of needed

to discuss community issues or, you know,

like, oh, this is really hard,

how to make the open-source lifestyle sustainable,

and one of the things that I faced in the Python community

was the pressure to not work on pandas

but to instead work on other components like NumPy

rather than build kind of pandas,

which was viewed at that time

to be kind of working around limitations in NumPy

to just work on NumPy and fix the kind of, you know,

limitations of NumPy rather than building

this sort of, you know, other project,

and so John, I think, was kind of the loudest voice.

It was like, well, forge your own path.

If you need to do your own thing,

like, don't worry about it.

Like, it'll all sort itself out,

and as long as the software that you're building is useful,

and so it was good that I had somebody telling me that,

and, you know, couldn't have been, you know,

a more empathetic person than John,

so for everyone who knows him.

I started a couple of business ventures.

During 2012, while I was writing my book,

we explored building a commercial Python financial toolkit.

It's one of the things I realized during that time

is that selling Python software is hard,

and maybe as a result, I've developed a very strong feeling

that the software needs to be free

and it needs to be open source,

and so, you know, I haven't been as interested

in building commercial scientific software, you know,

as a result, and that was a large reason

that Chong and I started Datapad and said,

well, we're not building software for Python users,

but we're gonna move upstack into the business user,

build a business intelligence tool that solves problems

that exist out there and still exist,

but use the Python stack as our core technology

for building the product.

So starting companies is hard.

I don't need to tell many of you.

We were venture-backed, and we built a product,

built a company, and we had kind of, you know,

I knew the Cloudera founders,

and we'd been talking about the product

for a very long time, and selling to Cloudera customers

would have been one of our go-to-market strategies,

but the back end, like the systems engineering problems

that we were tackling were very similar

to the problems at Cloudera, and last summer,

they said, hey, why don't we join forces

and solve these problems together,

and that is indeed what occurred.

So where I am now and what I'm doing,

Cloudera, I guess you can think of as an open-source company

for big data that builds and supports Hadoop

and projects that are related to Hadoop

and the Hadoop distributed file system,

and for me, kind of thinking about the arc of my life

and wanting to have a way to sustainably work

full-time on open-source, I really couldn't ask

for a better situation and to be working

on data problems at very large scale,

so I'm happy to talk more offline with other folks

about my work there and Cloudera itself,

and if you're looking for a job in big data,

well, I'm sure you can figure out how to contact me.

So it's been seven years of Python development,

and the things that I'm really interested right now

are much the same problems.

I'm still very much a Python person at my core,

but I'm very interested in fostering collaboration

amongst all of the data science programming languages.

I think it's the R versus Python versus Julia.

like the data science language wars is very counterproductive

and I think has impeded progress in certain ways.

And I would like to see collaboration in...

I would like to see collaboration among those groups of people

because we are solving the same problems,

the same machine learning problems,

the same analytics, you know, data serialization,

you know, network database problems.

And if we could build toolkits that we could all use,

particularly for the same kinds of problems that Panda solves,

that would be, you know, a great benefit for the future.

As long as there's a first-class Python interface,

that's the most important thing.

And the other things related to that

is generally making Python, using Python for big data a lot better

because I work at a big data company,

so I'm working on that right now.

And, you know, I think the whole LLVM,

you know, JIT compiling, cogeneration stuff,

I believe that is the future of a lot of what we are doing

and, you know, I'm putting my chips in that pile.

So I'm kind of, you know, hoping for like a no-JVM future.

I don't know if we'll ever see it,

but, you know, I think, you know, LLVM and JVM

living in perfect harmony would be really exciting.

And so the other kind of broad theme of what I'm working on

is that, you know, as the data gets bigger,

invariably the storage and execution,

you know, how the data gets processed and how it gets stored

are going to be, you know, for really big data,

are going to be, you know, standalone systems

for storage and data processing.

And the question then becomes,

how can you build the best user interface?

And I think, and I think a lot of you should think,

that Python is, you know, the best

or one of the best user interfaces

for doing sign-in computing, data processing,

you know, all these problems that we're solving.

So making sure that we can continue to program in Python

and that, you know, Python is viewed

as one of the best environments for getting work done,

that's, you know, that's what I'm working on

and I think I will continue to for quite some time.

So I ran slightly long and I don't think I have any time,

I don't know if I have time for questions,

but thank you very much for having me

and looking forward to what the future holds.

APPLAUSE