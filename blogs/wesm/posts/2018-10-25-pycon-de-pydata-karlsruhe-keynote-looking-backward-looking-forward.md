---
title: "PyCon.DE 2018: Keynote - Wes McKinney"
summary: "Video at PyCon DE / PyData Karlsruhe"
date: 2018-10-25T00:00:00
tags: ["video", "transcript"]
slug: pycon-de-pydata-karlsruhe-keynote-looking-backward-looking-forward
word_count: 9293
source_file: transcripts/2018-10-25-pycon-de-pydata-karlsruhe-keynote-looking-backward-looking-forward.md
content_type: transcript
event: "PyCon DE / PyData Karlsruhe"
video_url: "https://www.youtube.com/watch?v=uETG3bn4kow"
---

{{< video https://www.youtube.com/watch?v=uETG3bn4kow >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

This keynote reflects on a decade of open source data science work.

## Philosophy

Using Maslow's hierarchy, I position open source collaboration as a higher-order need, possible only after basic necessities are secured. My guiding questions: "How can I make myself more productive? How can I make people I work with more productive? How can I make strangers on the internet more productive?"

A key insight: "the technical side of open source, the engineering, the code that you write, is probably the easy part... collaborating with people, understanding other people's motivations and communicating at a level where you're able to create a productive collaboration, that is very difficult."

## pandas Genesis

In 2007, I spent three years convincing a single organization to adopt Python for data analysis. The catalyst: discovering an unmaintained implementation of R's statistical models in Python. The name "pandas" emerged from econometricians discussing "panel data," combined with "Python data analysis."

When released on PyPI in December 2009, pandas was 10,000 lines of code. The breakthrough: "if you look back at seven or eight years ago, reading CSV files wasn't reliable... if there is a killer app for pandas, it's pandas read CSV."

## Existential Crises

I characterize my career as "jumping from one existential crisis to another." In 2010-2011: would Python matter for data analysis? By 2018, with Python dominant: "how do we continue to produce the software that nobody wants to pay for?"

My 2011 blog post warned "fragmentation is killing us," worried about hundreds of incompatible data frame libraries proliferating.

## Limits of Vertical Integration

Building Datapad, an interactive data exploration platform, revealed pandas' architectural limitations. The need for sub-300-millisecond query responses led to my 2013 talk "10 Things I Hate About pandas."

pandas' self-contained approach enabled rapid development but resulted in over 200,000 lines of code. "When you own all of this code, and often with a small team, the code can go out of date pretty quickly, and bit rot is an issue."

## Apache Arrow

At Cloudera in 2014, I found "the Python ecosystem was very much on an island, and that this whole ecosystem of big data tools had been created by mostly Java developers, and so they weren't really thinking about the needs of Python programmers very much."

Arrow aims to create language-independent data frames bridging data science, databases, and big data. "My goal with this project ultimately is to put an embedded analytic database at your fingertips."

Cross-community collaboration proved challenging: "Getting these three communities to collaborate on a technology like this is very difficult. It continues to be very difficult." Arrow now supports 11 programming languages.

## Sustainability

I was candid: "for a lot of days I'm very tired because you do open source development for this long of a time, and you feel like you're carrying the weight of the world on your shoulders."

My solution: Ursa Labs, designed to attract corporate funding for Arrow development. "When you're describing something really ambitious that may take many, many years to build... the longer the horizon of building the thing that you want, the harder it becomes to get funding and support."

## Looking Forward

"I think the future is very bright, and I think as things become less fragmented and we see more collaboration happening beyond the world of Python and across these different communities of people that are doing data processing, we're going to see some very interesting new technology emerge."

---

## Key Quotes

> "How can I make myself more productive? How can I make people I work with more productive? How can I make strangers on the internet more productive?"

> "The technical side of open source, the engineering, the code that you write, is probably the easy part... collaborating with people, understanding other people's motivations and communicating at a level where you're able to create a productive collaboration, that is very difficult."

> "I've been sort of jumping from one existential crisis to another."

> "Fragmentation is killing us."

> "If there is a killer app for pandas, it's pandas read CSV."

> "When you own all of this code, and often with a small team, the code can go out of date pretty quickly, and bit rot is an issue."

> "The Python ecosystem was very much on an island, and this whole ecosystem of big data tools had been created by mostly Java developers, and so they weren't really thinking about the needs of Python programmers very much."

> "My goal with this project ultimately is to put an embedded analytic database at your fingertips."

> "For a lot of days I'm very tired because you do open source development for this long of a time, and you feel like you're carrying the weight of the world on your shoulders."

> "The longer the horizon of building the thing that you want, the harder it becomes to get funding and support."

## Transcript

Well, thanks for having me.

This is my second talk in Germany.

I spoke at PyData Berlin, I think it was last year or maybe it might be two or three years

ago.

I've lost track, but I'm glad to be here.

I've spent a lot of time in Germany over the years, so it kind of feels like it's nice

to be back.

So this talk is, I give a lot of very technical talks, because a lot of them are development

updates, like what have we been building in the last three months, six months.

There's a little bit of, there's a small amount of that in here, but I wanted to give maybe

some high-level context about maybe what I'm all about and why I work on open source projects

and what kinds of things I'm hoping to accomplish in my career.

And I think it's helpful, given I've been working on the Python projects for a little

over 10 years now, and so it's useful to look at the past and say, well, what can we learn

from the past?

How did we get here?

And what would we like to accomplish in the future?

Because things are very different now than they were 10 years ago.

And so I will speak a little bit about that and what has changed and what might continue

to change as we venture into the future.

So if you're an open-source developer or a prospective open-source developer, it is

useful to look at your motivations, like what would motivate you to build free software

and give it away for free on the internet?

I grew up in an American family, and there's kind of the American ideal of capitalism.

You learn things, you get a good education, and then you go out and make lots of money.

And so this idea of building something, taking all of your education and building something

and then giving it away for free on the internet, it doesn't exactly fit with kind of the American

ideal of capitalism.

So I end up having to explain this to my family a lot.

But you're probably all familiar with this idea of the hierarchy of needs, Maslow's hierarchy

of needs.

So we all have our, at least we're very fortunate in that we have, for the most part, food,

water, and shelter pretty well under control.

And when I was growing up, the idea was, okay, well, you have food, water, and shelter, you're

not having to worry about starving.

You're able to go to school and get educated.

Now you should get a good job, and you should make money, and then maybe buy a house, maybe

have some, buy a car, have some kids.

And then you keep going up that sort of hierarchy.

Maybe now you're a computer programmer and you work for a company, and this whole idea

of being able to collaborate with other companies and build software and work with people outside

of the people that are in the office together with you, that's pretty far up the hierarchy

of needs.

You don't really need that necessarily, but it's nice that we do have it.

And so this idea that we can sort of make our way of working better than it is now,

we need a lot of assumptions in order to be able to do that.

So we're very fortunate that we're in a time that we're able to do what we're doing right

now.

So for me, there's a number of questions that guide my work, and I have to remind myself

of these sometimes because open source development can be very frustrating.

So when I started out, I was a mathematician, so I studied, I have a degree in pure mathematics,

so I mostly wrote proofs when I was a university student.

And I started working with the intent of doing some applied mathematics and then maybe going

back and getting a doctorate in the future, but I found that working with data was a lot

more difficult than I expected.

And so I started out with the premise, you know, how can we make data analysis easier

or at least more accessible?

That's kind of very closely related to the amount of leverage that you have as an individual,

and so I started out with how can I make myself more productive?

If I build better tools for myself, I'm able to express the ideas that I have in code,

that code works, that code is fast, that code is reliable.

How can I make other people that I work with, people that I know personally, how can I make

them more productive?

And then eventually it's how can I make strangers on the internet more productive?

I worry about some of the implications of that because I don't always know what people

on the internet are going to do with software, and they will do good things, they will do

bad things, and I've learned over the years that they do a lot of both.

Beyond that, I think there's kind of the bigger picture of how to create and make possible

more productive and more fruitful open source collaborations, and I see a lot of open source

developers, they're very productive as individuals, but maybe aren't so good at building relationships

and building collaborations with other engineers, and one of the biggest things I've learned

is that the technical side of open source, the engineering, the code that you write,

is probably the easy part, and honestly, collaborating with people, sort of understanding other people's

motivations and communicating at a level where you're able to create a productive collaboration,

that is very difficult, and I certainly have not mastered the art of successful collaborations,

but it's something that's very important to me, so if you can work with someone and

both achieve your goals, maybe in less time, or maybe with a more interesting outcome,

I think that's more exciting to me.

Maybe unrelated, these are maybe high-level things, let's make the world a better place,

but there is another thing, which is that we have all of this really great hardware,

you consider how much better in our lifetimes computers have gotten, and I believe that

we should be working to maximize what is possible with the hardware that we have, and if you

look objectively at where we are in terms of hardware utilization, we have a long way

to go, I think we really have just barely scratched the surface of what's, I think the

rate of hardware development and improvements in computer hardware has significantly exceeded

the software that we have to run on it, and part of what's difficult about catching up

in terms of the software is that it's hard to build software, it's hard to have people

with the skills to build the software, it's hard to have the financial support to support

those individuals so that they can build the software, so it's bigger than just like

let's have two or fewer CPU cycles, there's all of these kind of things that are involved

with being able to, if you're utilizing the hardware better, it means that you've solved

a whole bunch of other problems which are enabling you to build better software to run

on the hardware.

So one of the things that pains me a great deal is I look at the way that things are,

the status quo, and maybe it's just a personality flaw, but I tend to find, I appreciate the

things that are good about the status quo, but I also see all the things that are not

good, and sometimes it's good to just ignore the things that aren't good, but it's good

to be aware of them, like if you spot an inefficiency or some negative pattern, something

that feels like it's not the worst thing in the world, but maybe it's something that could

be better, maybe it doesn't keep you up at night, but at least you make a list of all

of the things you think maybe could be better or you would like to see change, and then

maybe start to prioritize those and use that to help steer your efforts.

And I've found that people's feelings about the status quo vary a great deal, so a lot

of people, I've found, are...

generally fine with the way that things are, and so if there's something that

maybe doesn't work so well, or something that's inefficient, or maybe it's hard for them to

get something done, but they're still able to get it done, they say, well, this is just the way that things are,

and so a lot of people are mostly fine with the way that things are,

and personally, I've never, apparently, I guess just given the data, I'm not

fine with the way that things are mostly, and I'm generally looking to, like, how can we do better,

you know, how can we disrupt the status quo, is there anything that we can do

to, you know, make, you know, essentially make humans more productive and

more efficient, but as, you know,

as fine of an idea as it is to disrupt the status quo,

and to change things, is the fact that change is difficult, and people

tend to be resistant to change, so just, you know, just to give you an idea,

you know, when I started my career, it was in 2007,

and back then, there was, there were Python libraries for doing

scientific computing, there weren't a lot of statistical libraries, but

people were doing a lot of data analysis, a lot of them used MATLAB, or they used SAS,

they used products that you pay for, and people were really comfortable with the idea

of paying for software for doing, you know, for doing data analysis,

and so even the idea of using open source or free software

to do data analysis, you know, was considered radical by,

you know, by a lot of people, and there's multiple layers of, you know,

people's resistance to change, like even changing from one function call or one API to another

can be like, well, this is the code that I've written every day for the last five years, and like, why should I have to write a

different line of code, like I already know how this works, like learning new things is work,

and so I'm able to get my job done, so why would I do, why would I do anything differently,

you know, so small changes can be hard, maybe changing from one library to another

can be difficult, and we see this a lot in open source where maybe, you know, I still

use Matplotlib a lot because, you know, I know how to use Matplotlib, I'm comfortable with Matplotlib,

but we have all these new kind of, you know, more interactive,

more web-friendly visualization tools, and if I were doing more data visualization

at some point, I might be motivated to become more of an expert in these other

visualization projects, you know, and kind of, and friction,

you know, so beyond APIs and libraries, changing a programming language is difficult,

so getting people to change from R or Matlab to Python

is, you know, is very difficult because the learning curve in a new programming language is hard,

and going from paying for software to not paying for software, so all of a sudden you have to learn

a new programming language and you have to learn new libraries and new lines of code to write and port all of your ideas,

but you also have to get, you know, sort of get comfortable with the idea

that there's, you know, there's no longer a company that is responsible for the correctness

and the, you know, essentially fixing bugs in that software,

but this is, you know, this has created a lot of other problems now

because now no one wants to pay for software, and so

now we have questions about, you know, how is that software produced or how do we continue

to produce high-quality software.

So for me, I kind of think about this in that I've been sort of jumping from one

existential crisis to another, so, you know,

I think 9 or 10, you know, let's see, what is it, 2018,

so in, you know, 2010, 2011, the existential crisis

was does Python matter at all in doing data analysis,

and this was, you know, we weren't sure. I'll tell you a little bit more about the details of that,

but now, you know, more time has passed, and now we have, you know,

everyone uses, not everyone, but a lot of large percentage, maybe the plurality of people

are using Python for data analysis. You have, you know, a lot of the major tech companies,

you know, Google and Facebook and Microsoft and folks building, you know,

machine learning libraries, and, you know, they're accelerating the adoption of Python,

because now if you want to do cutting-edge machine learning, like we have to,

you have to use Python, so that's bringing a lot more Python developers

into the ecosystem, and so now kind of the new existential crisis is, you know, how do we continue

to produce the software that nobody wants to pay for?

So everyone wants it, they want it to be high-quality, but, you know,

how the sausage gets made, you know, where the money comes from to support people,

you know, they don't want to think about that, or a lot of people just are happy to ignore

that part of the problem. So I want to go back in time

just a little bit to give you an idea of, like, how I got here,

maybe how we got here a little bit. So I started my career,

I worked for a quantitative investment manager

just outside of New York City, and there I spent

about three years essentially working to get a single organization

to adopt Python for doing data analysis

and for building systems that process data and

eventually built financial models that were used for trading.

So I got to experience a lot of the, kind of, all these sort of social problems

around, you know, fighting the status quo, instigating change

in an organization, getting people to learn new things, challenging people's ideas

about, you know, what kind of software will make, you know,

essentially will make a team of people doing statistics the most productive.

But it was not easy and I think, you know, I sort of,

it kind of felt like boiling the ocean because we didn't have data frame libraries

really, we had numerical computing tools, we had Cython, which was a fork of Pyrex

at that time, I can't remember, I mean Stefan Benno I'm sure knows the history of Cython

a lot better, but, you know, I was a very bleeding edge Cython user back in the day

and so we've definitely run into a fair number of Cython bugs over the years, but there was a lot of,

I was able to stand on the shoulders of giants in terms of NumPy and Cython, SciPy, Matplotlib,

IPython, in terms of building, starting to build pandas and build a rudimentary

stack of statistical computing tools in Python. For me the key,

like the catalyst for using Python at all was the fact that a statistics professor

at Stanford, Jonathan Taylor, had re-implemented some of R's statistical models

not in mainline SciPy, it was actually in like a branch of SciPy,

I don't even know how I found it, I think it was on a mailing list somewhere, but there was this

unmaintained, it was crazy in retrospect, but there was this unmaintained implementation

of some of the models in the MASS package in R's, including robust linear models

and some other things that I needed, because I was working with really messy data

and so I needed robust linear models, like normal linear models

didn't work for the data that I was working with, and so this was the catalyst

for being able to actually try to do things

in Python, and I spent the next two years or so

building tools around that to create a sane workflow

for myself and my colleagues. So I was able to convince

a financial firm to release the data manipulation code that I'd been working on,

which we had to dig around and find a name,

so I was working with a lot of econometricians, and so they were talking about

panel data all day long, so all I was hearing about is panel data this,

panel data that, and I was also trying to find a name that somehow related to

the words Python data analysis, so I was rearranging words and there was all these econometricians

talking about panel data, and so we have pandas.

You can look back on PyPI and find the first version of the project, which I think

posted to PyPI on December 31st, 2009, and compared to the

pandas that you use today, it's a tiny,

It's a tiny project, maybe 10,000 lines of code.

A lot of the functionality that you have now in the library just didn't exist back then.

And so it's no surprise that it wasn't something that kind of rocketed off and became a smashing success from day one.

It needed a lot of work from the first version to be something that was generally useful.

So I left the financial industry and I did, in fairness to myself, go back to grad school to start a Ph.D.

And so around May of 2011, a lot of the, I guess we didn't have the term PyData back then,

but what we now think of as the PyData core developers, at least people in the U.S.,

people like Travis Oliphant, Peter Wang, Fernando Perez, Brian Granger, I'm sure people that you've heard of.

We all got together in Austin, Texas, in May of this year,

to essentially talk about the ecosystem of tools that was developing at that time.

So that included pandas and there were a number of other projects similar to pandas.

There was something called Data Array that Fernando and others had worked on.

There was a project called Larry.

So there were a number of these sort of data frame-ish libraries that were developing.

And so we got together to discuss, like, you know, can we synthesize ideas?

Can we work together to build something that will, you know, can help grow the ecosystem?

And also at this time, like, I'd been hearing from a lot of people who were,

a lot of people who were interested in using Python,

but they found that when they started looking at the open source libraries that they were of,

at least for doing data analysis, that they were of fairly low quality.

And so I was starting to see people building their own kind of internal pandas libraries,

and that worried me. That worried me a lot.

I was like, oh, no, people are going to use Python,

but everyone's going to have an incompatible kind of half implementation of the pandas-type concept.

So we'll have, you know, hundreds of data frame libraries proliferating in every Python user.

And so that worried me a great deal.

So my pitch, and I went back to the slide deck that I showed people in this meeting a little over seven years ago,

and so my pitch was that we need tools that are robust and something you can use to build systems,

but is also good for interactive research and can be used by normal people.

And so this being useful for normal people, so people who are not software engineers,

was not something that everyone felt was of value.

And so if you look at the scientific Python ecosystem back then,

you had a lot of computer scientists, physicists, neuroscientists, people working on supercomputers.

So it was a very engineering and computer science heavy group of people.

And so this idea that we needed to build tools that could be accessible to maybe somebody who mostly used Excel,

so the idea of, like, getting people out of Excel and getting them writing Python code

was not something that everyone agreed on.

And so this was kind of an idea that I was trying to convince people of.

So also we need to fix packaging.

So this is pre-Conda and pre-ManyLinux Linux 1.

And so I don't know if anyone was doing Python in 2011, but if you're doing Python on Windows,

because I had done Python on Windows for three years, it was not fun.

Yeah, no.

I think I've got post-traumatic stress disorder from this.

I mean, things are legitimately a lot better.

I mean, you know, we complain about packaging,

but I think we have to sort of step back and appreciate how much better things are than they were back then.

So thankfully the call to arms around packaging.

It was helpful that we met.

We had the first PyData meeting.

I think it was in March 2012.

Guido van Rossum was there, and we kind of explained the packaging crisis to Guido.

And I can't remember his exact quote was, you know,

don't look to us for help, you should just solve your own problems.

So that was kind of the genesis of Conda back then.

But, you know, we'd had these conversations,

and we were beginning to have discussions and ideas about what to do for Python data tools,

and I was really worried that we were going to end up with this just fragmented mess,

and that nothing was going to work well together,

and that basically the ecosystem was going to, you know,

that we were kind of titanic headed for the iceberg, and we're not doing anything about it.

And so I wrote a blog post in July 2011,

and essentially I said, you know, the current maybe is a bit dramatic, overly dramatic,

but, you know, the current state of affairs has me rather anxious.

You know, we're beginning to build these high-level accessible data science tools.

We didn't have data science back then, but we have these data manipulation tools.

Data manipulation is very important to growing the ecosystem,

but, you know, there's too many of them.

Like, we need to kind of consolidate, synthesize ideas, and then begin to build integration.

Because at the end of the day, if I can't read a CSV file,

join it with another CSV file, do some basic data preparation,

and then fit a linear model, like, you know, what are we doing here?

Like, if we can't solve these really basic workflows,

and have it just work, you know, 90, 95% of the time,

like, you know, why are we bothering with this at all?

So, and I kind of call it, you know, it's funny thinking about, like,

commitment anxiety in the context of open source,

but I do find that when you introduce new technology,

there's a period of time where there is anxiety about, like,

oh, there's this new thing, like, is this still going to be around in a few years?

Like, are people going to support this?

Like, you know, maybe the people that developed it are going to abandon it,

and then we're going to be stuck maintaining it.

So I completely understand the resistance to committing to, you know,

using or integrating with new technology.

So I don't think that necessarily, you know,

the community's position in mid-2011 was wrong, per se.

But, you know, at that time, I was like, okay, I've got to, you know,

rearrange my life so that I can help sort of make people feel secure about using,

essentially, pandas or some version of pandas as their primary data manipulation tool.

I kind of summarized this in my blog post, is fragmentation is killing us.

And I still feel this way a lot, that there is a lot of fragmentation in open source.

And I think that people don't always recognize the costs.

You know, to solve fragmentation can be difficult,

because it requires sometimes collaborations with people that have different priorities.

It could mean, you know, somebody created a project,

another person created another project.

It might be that the right way is for, you know,

one person to stop working on their project and to work on the other project,

or maybe to merge projects.

Like, there's a lot of social issues that go along with, you know,

making things less fragmented that I'll talk a little bit about.

But, you know, the way I looked at it in 2011 is that the killer app,

or at least the really thing that we have to solve,

is that we have to be able to read CSV files.

And if you think about, like, is there a killer app for pandas,

like it's pandas read CSV.

It's like everyone's, like, most beloved and most hated function,

because it has, at this point, you know, like, what, 70 or 80 arguments.

And so, you know, the most common question is,

why does read CSV have so many arguments?

And, you know, it's because CSV files are pretty horrible.

And so really we should stop creating CSV files, but, you know, it is what it is.

But, you know, if you look back at, you know, seven or eight years ago,

reading CSV files wasn't reliable, wasn't something that you could do.

Very easily in Python, and I would point people to R and say,

okay, look at read.csv or read.table in R.

That will just work most of the time,

and people are successful reading their data with those functions.

But if you try to use, you know, np.loadtext or npgenfromtext,

or there were some other functions, like they, you know,

they require a computer science mindset.

like you've got to kind of set a bunch of parameters,

like there's not very much, they don't infer types,

you've got to write down the types,

like there was a lot of rough edges

that were preventing people from like,

you know, from step one in the data analysis,

which is reading CSV files.

And I think that kind of this experience of,

you know, kind of this bottom-up thinking of like,

okay, we've got to make sure we're solving

the really basic problems.

I think even today, like it's great to have

all these big designs, but if we aren't solving

like the really basic problems effectively,

like we have, you know, we have a problem.

So all of this work in 2011, 2012,

like culminated with writing a book,

I put the, we're in Germany, so I put the,

thanks to Christian Tismer and Christian Rotar

for translating the book.

I think there's a second edition coming out,

so thanks very much for that.

I didn't expect the book to be so successful,

but, you know, I think it kind of coincided

with the growth of the Python ecosystem

and helps people to learn, to learn all these tools.

But I think also the experience of actually writing

the book helped kind of, you know,

identify rough edges in pandas

and other parts of the data stack.

So to kind of, you know, sort of go through the experience

of like, okay, how do we learn to use all of these tools

and do something productive with them

from the mindset of somebody who's just starting out

and make sure that, you know, everything is there,

like all of the tools that you need and that things work.

And so I would get to sections and chapters

and be like, oh, well, the next natural thing

in this chapter is a section about, you know,

dollar sign foo, but dollar sign foo

does not exist in pandas yet, so I better get busy

and build that so that I can write about it.

And so if you really want to make a good quality piece

of software, I recommend that you write a book

while you're doing it.

It's a lot of work, but it's a very valuable process.

So I took a bit of a detour.

So I'd spent, you know, by 2012,

I'd been working on essentially pandas

for a little over four years.

So I took a detour to start a company called Datapad.

So we built, this is what Datapad looked like,

probably looks like a lot of BI,

kind of business analytics tools that you've used.

And I think this sort of, this concept of like

cross-filtering kind of data exploration

has become fairly ubiquitous nowadays, so that's great.

But everything that we built in Datapad

in the back end was all built in Python,

so we used the Python data stack.

We had to do quite a bit of custom development.

And one of my objectives in starting a company

was to be able to invest a lot of the core technology

back in the open-source ecosystem.

But as things go with startups,

you have these goals of doing open-source development

and all that, but you end up kind of prioritizing

around what will help the company survive.

So the key things that influenced me

kind of while I was building this sort of

interactive data exploration product,

so you would use Datapad on an iPad or in a web browser,

but all of the query processing,

the analytics was happening on the server.

So any interaction with a web application

would trigger through a web socket, a query,

which would go into AWS, and then it would perform

some computations on a data set,

and then it would update the web UI.

And so if you want to have a really interactive experience,

you've got to be somewhere in the 200 to 300 millisecond

threshold, which is a pretty tight constraint

when you consider that there's kind of network traffic

and you've got to deal with the end-to-end,

send query, perform query, send results back to browser,

update UI.

We were also processing queries

in a multi-tenant environment,

and so the amount of resources that we were using

for each user obviously translated directly to dollars.

And so resource utilization was really important.

But really, there were a lot of problems

with pandas performance, and we ended up essentially

building a highly customized version of pandas

with about 10 to 20% of the functionality,

but was focused on better memory use,

better serialization performance,

had support for memory mapping,

and kind of things that pandas doesn't do very well

to address the kind of interactivity requirements

of the application.

So that project was called Badger,

and is talked about in one of my talks,

so a number of my talks.

So I gave this talk at the end of 2013

that was kind of a result of the challenges

that we were having building a performant kind of backend

for Datapad, and the subtitle of the talk

was 10 Things I Hate About pandas.

And I would summarize the talk as being

that pandas internally is not designed

like a database engine.

And a lot of people do use kind of pandas

as Airsoft's database,

but there's a lot of issues around that,

so everything's eagerly evaluated,

you can't memory map files,

there's a lot of performance costs

associated with loading data,

so this idea that the data's either all on disk

or it's all in memory,

that creates a lot of problems.

Strings are all Python objects,

so that's, we didn't have categorical back then,

so categorical's been used to kind of address

kind of the string problem in part.

So you can read the talk

and see all of the points in particular.

But at a high level, I think the key problem

that this led me to contemplate over the last few years

is this idea of vertical integration.

So if you look at pandas,

pandas is this whole world unto itself,

like it does depend on NumPy,

but as time has gone on,

we've become increasingly less dependent on NumPy,

so we have all of our own missing data,

where algorithms for aggregations and array functions,

and there's good things about building

a vertically integrated system,

so you have all of this control,

so you can make all of your own decisions,

you don't have to negotiate with anyone,

you don't have to do pull requests

into some other code base,

you have a single code base,

you can do whatever you like.

Vertical integration can make you more productive,

so because there's less coordination with other projects,

you can cut corners to meet deadlines,

and so when you're collaborating with people,

sometimes they won't be happy if you're cutting corners.

You can make releases whenever you want,

so you don't have to worry about coordinating releases

with other projects.

There's of course some bad things

about vertical integration,

so I think the biggest thing that's hurt pandas

over the years is the amount of code

that the pandas project owns is extraordinary,

so there's over 200,000 lines of code,

there's a lot of C extensions,

the number of distinct components in the project

for data ingest, for data manipulation,

data visualization, data presentation,

Jupyter notebook integration,

the front end API, which is of course sprawling

and very complex.

You're not reusing code, so that's both good and bad,

it means that you have to write code

that you might not have to write

if you were reusing code.

When you own all of this code,

and often with a small team,

the code can go out of date pretty quickly,

and so bit rot is an issue,

and there's probably some other issues

with vertical integration.

So, good things, bad things, not perfect.

But, so this all kind of came to a head

when I, so myself and the Datapad team,

we landed at Cloudera at the end of 2014,

and my job there was, how can we make Python

a proper first class citizen in the big data world?

And I found, unfortunately, that the Python ecosystem

was very much on an island,

and that this whole ecosystem of big data tools

had been created by mostly Java developers,

and so they weren't really thinking about

the needs of Python programmers very much.

So the big issues that I ran into right away

was, oh, there's all of these file formats that we can't read or we can't read very well.

Interoperability with the JVM, getting access to data that's in the Java virtual machine

is difficult or impossible. And a lot of the, when you do are able to extend systems with

Python or with arbitrary programming languages, the interface for injecting custom code is

often not array oriented. And so you might be running, and this is the case with Spark

at the time, that you'd be running one Python function call for each value in a data set.

And so we all know that the difference between a for loop and a NumPy array call can be 100

times or 300 times or more. And so all these things are really not working very well in

our favor. And so to me, the big sort of evil in the ecosystem that was causing me a lot

of problems in sort of thinking about how to integrate Python better with the ecosystem

is the data itself is very fragmented. So the data is in many different formats, many

different files. It's represented differently in each runtime system. If you want to reuse

code, you really can't because code, the algorithms and data serialization is highly

specific to the context in which it's used. So everyone has many implementations of the

same thing. So we have many different CSV readers, many different Avro file readers,

many different implementations of summing data. So we've got to do something about this

fragmentation. So throughout 2015, I sort of went down the rabbit hole of how can we

build some technology to solve this problem. This is what led me to get involved with the

Apache Arrow project, which from the data science perspective, the idea is to have a

language-independent data frame. So depending on where you're coming from, you may or may

not think about data frames, you may not care about data frames. But from an ecosystem

perspective, the three communities that I wanted to pull together are the data science

ecosystem, the database community, and the Java big data world. And so getting these three

communities to collaborate on a technology like this is very difficult. It continues to be

very difficult. So I think the two big picture items is to be able to reuse algorithms. This

is beginning to happen. And so Uwe Korn from Blue Yonder is giving a talk about Arrow later

today, so you can see some deeper internals of how we're doing JVM interop without copying

memory. But we want to be able to access data in memory without copying it that might be

owned by a different library or even a different programming language, and we want to be able

to move data between processes as efficiently as possible. So that might be through moving

data through a socket or through shared memory. And I want to be able to reuse algorithms

and to have common libraries that implement a lot of the stuff that's inside pandas or

that's inside databases without having to keep re-implementing the same thing over and

over again. And preferably, we could also take advantage of a lot of the work and the

research that's happened in analytic databases in the last 10 to 15 years or 20 years. And

honestly, there's been so much innovation that's happened in the database world, and

almost none of that innovation has made its way into the hands of data scientists. So

my goal with this project ultimately is to put an embedded analytic database at your

fingertips. And I think without a technology like Arrow to tie the room together, it's

very difficult to get people in the database world collaborating with people in the data

science world. So this has been a labor of love over the last three years, and finally

the pieces are falling into place and the communities are working together, but it's been

very, very difficult. So we're just about to take on support for our 11th programming

language. They're not all supported equally well, but we're getting there. And the 11th

programming language is csharp.net. So hopefully we'll merge that pull request later today

or tomorrow. I think one thing to appreciate about this project is the diversity of the

community and the number of different applications that people are working on. So I've

mostly worked with Python programmers in the past, and so to be working with somebody

building a SQL database or SQL query engine is really exciting. It's not something that

I've experienced with before, but that was the goal of the project.

There's kind of an aside to my experience getting involved in this project, which is

that building ambitious new open source projects is very difficult. I think everyone likes

the idea of you pitch people on, here's the vision for the kind of world that we want

to build in the future, how we would like to see things change, here's my plan to get

there. And the reaction that I get from a lot of people is, oh, that sounds amazing.

I can imagine early explorers would be like, oh, we're going to sail west and eventually

we'll get to India. And that didn't quite work out, they arrived someplace else. But

I think with software development, if you're describing something really ambitious that

may take many, many years to build, I think the longer the horizon of building the thing

that you want, the harder it becomes to get funding and support for that project. And

so with Arrow, I told people from the early days, look, this is not going to take a year

or 18 months, this is going to take five years, seven years, or more. And we're three years

into it now, and I think that that's very much the case with this project.

And so how we get support for the project, very difficult. I could give a whole keynote

just about that topic. So I decided to rearrange my life yet again to make it easier to get

funding for Arrow development. So earlier this year, I started an organization called

Ursa Labs, which has the mission of building data science tools powered by Apache Arrow.

I was working for Two Sigma the last two years, and it was clear that having a single financial

institution funding all of Arrow development was not fair to Two Sigma or practical in that

there are lots of organizations that are interested in the project and want to fund it. And so

I've been working on bringing more corporate partners into the ecosystem, getting them

to put real money on the table so that I can hire open source developers.

There's other organizations that are involved in Arrow just by having employees internally

who contribute. So folks here in Germany, the Blue Yonder folks have done a lot of really

key work in the project. So very grateful for all of the organizations that have contributed

to the project. One key thing about Ursa Labs is that I wanted to partner with the R ecosystem

to make sure that the R programmers are fully committed in being a first-class citizen in

the new world that is based on Arrow. So I talk with Hadley Wickham from the R community

every couple of weeks, and folks from his team who work on the Tidyverse are actively

involved right now in building R integration with the Arrow ecosystem.

So it's a long story, and I'm excited for the next five to ten years, but hopefully

this gives you some idea of things that I think about. I will say that for a lot of

days I'm very tired because you do open source development for this long of a time, and you

feel like you're carrying the weight of the world on your shoulders. And I think we are

in a sense. You consider the ratio of open source users to open source developers, it's

really pretty crazy when you think about the actual number of people maintaining and building

these projects. So I am hopeful that things do get easier for open source maintainers

in the future, and we have a bigger community.

of developers and corporations will spend more money to fund people.

But things are the way they are, so we've got to make lemonade out of lemons, as we say.

So I think the future is very bright, and I think as things become less fragmented

and we see more collaboration happening beyond the world of Python and across

these different communities of people that are doing data processing,

we're going to see some very interesting new technology emerge

and really help advance our ability to take advantage of modern hardware,

have less CPU cycles, maybe it will help with climate change, who knows.

But we have a lot of work to do, and so as much as we can appreciate the work

that's happened in the last ten years, I think the hardest work is yet ahead of us.

So thanks for listening, and I'll be around the conference today and tomorrow,

so I look forward to talking with everyone, and thanks to everyone who's contributed

to open source projects, we've come a long way, we have a long way yet to go.

Thank you.

So, thank you, maybe stay here. I think there are some questions.

How much time do we have for questions?

We have five minutes, perhaps?

Okay, five minutes. So, questions.

Hi, great talk, thank you. What do you think about open source projects

which come from big companies like Google or Facebook, like TensorFlow, Android,

I mean, I guess they have a different background and different motivation

than the more traditional open source community projects?

Right, yeah, I mean, so Google wouldn't be spending, I don't know what it is,

tens of millions of dollars for how much money they've spent on TensorFlow

at this point if they didn't have an agenda.

So when it's a big company starting a project at that scale,

there's obviously an agenda involved.

So, on one hand, it's great to have Google or Facebook or whoever

spending that much money in building a project like TensorFlow.

But on the other, I think the downside is that I think for community-based

open source projects, so Arrows, a community-based project,

pandas, a community-based project,

it's difficult because we can't muster the kind of resources that Google has

and so there is a risk that community-based projects die out

and that basically the only surviving open source projects

are the ones that are built by major tech companies.

And so it will be kind of closed source software all over again.

The code will be open source, but the process and kind of the engine

that is producing the software will be controlled by multinational corporations.

So there's risks involved.

I mean, it's good to have them involved and it's making the Python ecosystem richer,

but it's coming with risks associated for the open source world.

Okay, so question over there.

Hi, I work in database research and I also teach data science,

and of course we teach pandas, which is great.

But there's one, and I really appreciate what you said about bringing these two worlds

closer together, analytical databases and Python,

but there's one hassle and one suggestion how that could be improved,

and that is the interface to pandas.

So I would really suggest having an interface to pandas

that looks more like relational algebra,

because relational algebra is at the heart of any database system.

And if you had that, things would get easier,

and actually all the optimization things you can do in databases

would become so much easier.

It's just a suggestion.

Oh, my screen is not up.

Let me put my screen up there.

So I've got this Ibis project. Have you seen this?

So this is basically relational algebra in Python,

but trying to be as close to this pandas API as possible.

So this was almost a four-year-old project,

so I would take a look at that project.

Firstly, thank you very much.

I've spent most of my life getting rid of Excel sheets,

and you've personally and collectively made my life a hell of a lot easier.

I just wondered if you can share some wisdom with regards to

how you managed to convince in the early days

your company to open source the primary nature of development on a tool.

Yeah, it was difficult.

I mean, I think probably ultimately what convinced them

was so that I would shut up about it.

Let's get back to work.

But no, I think that my pitch was really that

releasing the software would help just create progress

around that problem in the Python ecosystem.

This was the biggest leap of kind of stretch of imagination at that time,

because I think people were really skeptical that other people would contribute

to the library or that other people would use it.

And so I believed that at some point,

somebody was going to need a project like pandas,

and so if we could make it the project that people used,

now people are like, ah, pandas has all these things that I hate about it.

But it is good that people have a basic toolkit that they can use.

And so the reasons that we ultimately open sourced it

are essentially what has happened,

that now we have a community and people develop and improve the project.

But I think there was a wide degree of skepticism

about whether or not that would actually happen.

And it didn't happen for a long time.

It was maybe two years until pandas had meaningful contributors

after we open sourced it.

And so that kind of like the horizon of thinking around an open source project,

like people want to see results in six months, results in three months,

and you have to change your time horizon

in terms of what does success look like in open source,

because it can take many years for the work that you're doing today to really pay off.

Maybe I have a question.

That my integer column gets afloat as soon as there's something missing.

Any comment on that?

I think there's an integer in a extension type now,

so this is being worked on actively.

We can learn a lot more about extension arrays in Uwe Korn's talk later.

So finally we're doing something about that.

Maybe a very last short question over there.

And I take the time, so please volunteer for the video thing,

and session chairs and registry,

so the conference just lives with your help.

Hello, thank you for your great talk.

It's a quick question about visualization.

I always try to find an equivalent of Shiny when I finish my pandas and analysis.

Do you have anything to... I haven't found anything on the ecosystem.

Do you have anything?

Yeah, I've been asking that for a number of years myself.

I would say that you can do a lot with Bokeh nowadays,

but I think that the kind of end user experience of Shiny,

I don't think we... like Jupyter widgets,

but I don't know that we have anything with the...

There was a project, I can't remember the name of it,

it's escaping me, made by Eli Brussard.

It was essentially kind of a Shiny-alike built at Stitch Fix.

But yeah, I mean, so we need a champion of that problem

to build kind of the true Shiny-alike for Python.

I think it would be useful for people.

Okay, so let's thank Wes.

I think it was a really great talk.