---
title: "Pretty Powerful pandas: Interview with Wes McKinney"
summary: "Interview at Pretty Powerful pandas"
date: 2025-09-02T00:00:00
tags: ["interview", "transcript"]
slug: pretty-powerful-pandas-interview
word_count: 4745
source_file: transcripts/2025-09-02-pretty-powerful-pandas-interview.md
content_type: transcript
event: "Pretty Powerful pandas"
video_url: "https://www.youtube.com/watch?v=XYHf5oFt1zA"
---

{{< video https://www.youtube.com/watch?v=XYHf5oFt1zA >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this interview with Laura Mawer for the "Pretty Powerful pandas" series, I reflect on the 17-year journey of pandas from its origins in 2008 to its current role in the data science ecosystem. I discuss the early design decisions around NumPy integration, the challenges of maintaining backwards compatibility while evolving the library, and the recent transition from BDFL governance to a steering council model. I explore pandas' position in the modern data ecosystem alongside tools like Polars, DuckDB, and Arrow, noting that pandas remains useful for small-to-medium data work. I also discuss my work on the Positron IDE and the data explorer component, and highlight pandas' time series capabilities.

## Key Quotes

> "I see it as more of this ever expanding Swiss army knife of data... I think it's always gonna be there as this Swiss army knife of small to medium data." — Wes McKinney

> "The burden of backwards compatibility and not wanting to change the behavior in a way that would break people's legacy code has made it difficult to make large changes in the project. You could understand why there would be a desire for some developers to start fresh and build new DataFrame projects." — Wes McKinney

> "Whenever people adopt an open source project, they're putting their trust in the developers of the project to think of their best interests... you're thinking about harm minimization at all times." — Wes McKinney

> "I've never really believed in one tool to rule them all. I don't view the success and growth of Polars as necessarily meaning that pandas is getting phased out or is going to get replaced. The reality is that it's not going anywhere." — Wes McKinney

> "People know how to use it. LLMs are really, really good at writing pandas code. So especially as long as we have AI copilots helping us write pandas code and our data sets are not hundreds of gigabytes or terabytes, it's a perfectly capable tool that will serve us well for many years to come." — Wes McKinney

> "It would be pedantic to say that everyone needs to use a scalable data analysis tool... a tyranny of people that are working with terabyte scale data sets to say, well, even for small data sets, you need to use this tool." — Wes McKinney

> "A lot of people know, but pandas in part because it was originally created in the financial world, it's actually very good at working with time series data... if you find yourself working with temporal data, any kind of financial data, maybe you're just analyzing your personal finances, pandas' tools for that are really nice." — Wes McKinney

> "In retrospect, probably a lot more complexity than we bargained for in the internals of pandas." — Wes McKinney, on early NumPy integration decisions

## Transcript

**Laura Mawer:** Hi, I'm Laura. Welcome to Pretty Powerful pandas, a mini-series where I'll walk you through the most useful, elegant lines of code in pandas, whether you're just starting out or you want to level up your data game. So welcome to today's episode of Pretty Powerful pandas. We've got a very special guest as Wes McKinney is joining us today. So welcome, Wes McKinney.

**Wes McKinney:** Hi, thanks for having me.

**Laura Mawer:** And thank you for joining us. So as you know, our series is all about kind of sharing the loveliness of pandas and who best to talk to but the creator itself. So I'm very, very excited to have you on. If you wouldn't mind, just in case some of our viewers don't know who you are, if you could just share who you are and your background and, yeah, get started, please.

**Wes McKinney:** Yeah, so again, I'm Wes McKinney. I'm the original creator of pandas about 17 years ago in 2008 and was heavily involved in building it in the initial open-source community for its first five years. It started out as a closed-source project then became an open-source project. It became a fully community-owned project in 2013. And so I graduated to a more of a ceremonial, benevolent dictator for life role. And that freed me up to pursue a combination of new open-source projects in the domain of data science tools and systems and also some startups and other entrepreneurial activities.

So I worked on the Apache Arrow project, was a co-creator there, the Ibis project, which is another Python project. And I've been involved in a number of other projects related to big data and data infrastructure, things like Apache Parquet, so data storage, and, yeah, lots of other stuff. So I've kept busy, but my career started with pandas, and so it's still the thing that I'm best known for.

**Laura Mawer:** Of course, and that title has got to be the best title I've ever heard.

**Wes McKinney:** Yeah, although, yeah, recently pandas just adopted a new governance model. There's now a steering committee, and so there's no longer a benevolent dictator for life. So in the spirit of the project evolving and becoming more mature and developing a more formalized steering council, we decided to retire the BDFL sort of title, similar to Python. Python no longer has a BDFL. So it used to be Guido van Rossum for many years, and now pandas has a similar type of steering council to the Python programming language.

**Laura Mawer:** So much for life then. But, oh, well, at least you held it, and it forever shall be in your heart, I am sure.

**Wes McKinney:** Thank you so much.

**Laura Mawer:** So, yeah, if you don't mind, I'll ask you some questions. So what first sparked the idea of pandas? Where did it come from? And did you ever think it would grow into what it is today?

**Wes McKinney:** I didn't think it would get quite as popular and widespread as like a fundamental tool of data access and data manipulation, and especially in the business setting. But I was really interested in, I had learned about the Python programming language and really liked programming in it, simple scripts, data munging, data wrangling. But I had had a little bit of exposure to the R programming language, and I wanted to have something similar to the DataFrame concept, to be able to manipulate whole tables of data, to have a spreadsheet-like interface.

And I was also, I was working in a financial firm where I was interacting with all these different data storage systems, a lot of SQL systems, pulling datasets from all over the place. And so I found myself just really struggling with basic data manipulation, data cleaning, data integration. And so I wanted to, so the initial stuff that I built in pandas was driven by my own needs, the things that were right in front of me, where I was trying to build, do research and do data analysis and eventually build production systems.

I wanted to do it in Python. And yeah, so I was building the things that I needed. And eventually, once I started working with more people outside of my company where I was working, AQR, and in the broader open source world, the project expanded and so that it could be used in different kinds of circumstances.

**Laura Mawer:** Well, we are very glad that you did because I must say I use it every day. I'm very pleased.

**Wes McKinney:** Yeah, I use it about every day too, even still.

**Laura Mawer:** Excellent. Thank you. When you were building pandas, did you have some like design decisions or principles that you held really important?

**Wes McKinney:** Well, initially it was built in really, with a really close relationship with NumPy. So at the time, so NumPy is the numerical array, multi-dimensional array library for Python. And at that time, back in 2008, 2009, NumPy was kind of the center of the universe if you were working with datasets in Python.

And so the idea was that you wanted to be able to go back and forth between NumPy arrays and pandas data frames with little cost. You didn't wanna have a high conversion overhead or you wanna be able to say, take data out of a data frame and into a NumPy array pretty easily and inexpensively. So that was a major design decision early on.

There were some other things like if you were working with data frames that had all numeric columns, for example, you wanted to be able to get a matrix out without any further copying. Inexpensively, like I was saying.

And so this led to, in retrospect, probably a lot more complexity than we bargained for in the internals of pandas. And so now as time has gone by, it both created a lot of complexity in the implementation of the library, but also once new things, new ways of representing data that address some of the shortcomings of NumPy, things like Arrow specifically, which brought first-class missing data handling as well as better array types for strings and for non-scalar data. So like lists and arrays and dictionaries as values in data frame columns.

So we've had to do a lot of work in pandas, or rather the pandas community has had to do a lot of work to generalize pandas to support other kinds of backing data structures aside from just NumPy arrays. Fortunately, most pandas users don't need to think about that so much, but another design decision that we made early on was to use the NumPy not a number value as the representation of missing data. And that's still something that creates sharp edges and that we're trying to migrate to a more uniform like pandas.na type that works consistently across all the data types.

And there's been some progress on that, but it's tough because when a project like pandas has millions and millions of users across so many different types of use cases, people have a lot of different expectations of the library. Some people want a very slim library with not a lot of dependencies. Some users are happy with maybe they're doing AI. And so they're already working with a ton of third-party dependencies libraries that they have to install. They might be installing hundreds of megabytes or gigabytes worth of libraries in their Python environments.

And so they're okay with pandas dragging along a bunch of dependencies, but we've had to support these two people, the more maximalist users of pandas and the more minimalist users of pandas and make a lot of the optional. So pandas now has a ton of optional dependencies because there's things that we wanna provide integrated support in the library for, but without forcing people to install dependencies that they may not need.

**Laura Mawer:** Nice, and that's a great way to kind of fit for everyone. Fabulous.

What's been your most challenging problem that you've had to solve while working on pandas?

**Wes McKinney:** Well, it's going back in time quite a long time since I haven't been doing active development on pandas for about a decade. But thinking back on pandas' growing pains and the, call it the 2012 turned 2013 timeframes, that's when pandas started to become really popular. Like my book, Python for Data Analysis was first published in 2012. And that was the start of definitely a hockey stick kind of up into the right, massive growth for the project.

Python became a lot more popular for data science and business use. And so suddenly we went from, I don't know, tens of thousands of users to hundreds of thousands or millions of users really quickly. And we found that people would bump into the rough edges of the project, the inconsistencies.

And I think one of the really difficult things that we struggled with for many years is how to control pandas' memory use and to prevent, to make the library safe for people to use without shooting their toes off. But also to have predictable memory use.

And so for many years now, there was a long multi-year discussion that I was partly involved in about introducing the concept of copy on write to pandas where basically pandas would move to a model where it tries to only copy data whenever you actually go to modify something in place. And so that would make it, there have fewer circumstances. If you never modify a pandas data frame in place, you're not accidentally overwriting data that's referenced by some other data frame.

So that's the kind of problem that would really aggravate people. They would modify one data frame and they would see the changes reflected in a data set that they thought that they had copied. And so as a result, pandas grew all of this, had all this code where it would defensively copy data just to prevent that like accidentally modifying a view.

But how to introduce that feature into pandas without disrupting people, because there was lots of subtle corner cases where people expected to be able to modify, expected that they were modifying a view of data, especially like chained assignments is one of the like areas where people would often have trouble. Like where you have data frame and then bracket and then a selection or with .loc or .iloc and you would select a subset of the data frame and then you would immediately assign to that selection.

And so there came a point where the community decided to always produce a copy whenever you would do that selection, because people were expecting to be able to assign directly. And at some point there started being this like setting, assigning data to a copy warning, to warn people that they were doing something that was no longer supported.

So they would know that like, because you could imagine if you were running your, you had a script that you wrote and you didn't write any unit tests for it. And there was some code that you wrote and the behavior changed. And then maybe a year passed, you upgrade pandas in your project. And then you run the script again and the results change. And you're like, gosh, like why did the results change?

And so that's the kind of thing where just managing user expectations and trying to make the project faster, more efficient, like more predictable, but doing so without like trying to minimize the amount of unintentional backwards incompatibilities and breakages that would affect people's code.

And I know that in many ways, like the burden of backwards compatibility and not wanting to change the behavior in a way that would break people's legacy code has made it difficult to make large changes in the project. And in many ways, like you could understand why there would be a desire for some developers to start fresh and build new DataFrame projects, which is why you now have projects like Polars or there's Daft and there's a couple of other new DataFrame projects, which have decided for any number of reasons to rebuild the DataFrame concept from the ground off without having to worry about backwards incompatibilities and API changes and all of those sorts of things, because pandas just has such a large and diverse user base that it's difficult to make changes.

**Laura Mawer:** I can just imagine that every little thing would have to be thought about in such detail as well for so many use cases.

**Wes McKinney:** Yeah. And some of the changes are incredibly subtle and I have to really heap loads of credit on the core developers. They've Jeff Reback and Brock Mandel and Joris van den Bosch and Tom Augsburger and all of the core team. I think over the years they've been, because this is the group of people, folks that I, many of them I met in the early days of the project and we decided we liked working together. They liked working on pandas.

And at a certain point I was comfortable essentially handing over the keys to the project, the keys to the kingdom, so to speak, because I got busy with new projects and the pandas still needed to be developed and maintained. And I think the core team has been incredibly thoughtful about evolving the project in a responsible way and always thinking about the users and not wanting to disrupt people, especially because whenever people adopt an open source project, they're putting their trust in the developers of the project to think of their best interests and to not, whenever you're making design decisions or you're changing things, that you're thinking about harm minimization at all times.

And so sometimes it's inevitable that you do have to break something, but that as much as possible you try to communicate ahead of time, we're going to make this change. We're sorry about it, but here are the reasons why that we have to do it. It's gonna be a little bit disruptive for 1% of users or half a percent of users, but it's for the better of the project.

And I think that the team has done a really amazing job of that over time. And just the continued growth of the project and usage is a testament to the users having a lot of trust and just faith that the project is headed in a good direction and that people are comfortable upgrading pandas and feeling like their code is gonna continue to work.

**Laura Mawer:** Yeah, definitely. Oh, well done the team then. That's brilliant.

So you've mentioned you are working on some other projects. Do you see pandas kind of fitting into a modern data stack today? Or do you think, as you said, it's kind of evolving into other things and people are kind of standing on your shoulders to go a bit further?

**Wes McKinney:** I mean, it's still probably the most used tool in the data science, like the most used data manipulation, data loading, data access tool in the data science, machine learning and AI landscape. So it's definitely not going anywhere, but I see it as more of this like ever expanding Swiss army knife of data that pandas went in this direction.

And I definitely pushed it in this direction and in the spirit of trying to build the biggest tent possible and invite people into the pandas tent by rather than saying like pandas will have a narrow feature set and we won't add like tons of sprawling features, but that instead pandas would have lots of sprawling features to be as useful as possible to as many people as possible.

That's made the project more complex. It's made it difficult, challenging to maintain a lot of work for a very large developer community, but I think it's always gonna be there as like this Swiss army knife of like small to medium data. It wasn't designed for working with very large data sets.

And one of the things that, one of the other projects that I've spent many years working on, the Arrow project was created in part to provide a better computational and memory foundation for data frame libraries. And so what's happened is that in the course of the last 10 years is that simultaneously pandas has incrementally enabled Arrow to be used as a way to represent data in pandas, which gives it much faster string processing, like better memory efficiencies, more consistent missing data handling, a bunch of nice features.

And at the same time, there's a crop of new data frame libraries and tools that have been created that are Arrow native or Arrow compatible. So Polars, for example, is Arrow native. Daft is Arrow native. DuckDB is not Arrow native exactly, but is highly Arrow compatible. And so you can go pipe data in and out of DuckDB very efficiently.

And DuckDB internally has some further optimizations and additions beyond what Arrow does that are specific to DuckDB. But I think because Arrow has emerged as this universal way of representing data and interchanging data between pandas and Polars and DuckDB. So it's served, it's helped create this like interoperable ecosystem of tools.

So if you have one part of your code base, which is heavily using pandas, that's totally fine. And then maybe there's a part where you're processing really large data sets. You're okay with a narrower feature set and you want to use Polars and that's fine too. And maybe there's an area where you have, you want to write SQL queries or you're interacting with database systems and you want to use DuckDB.

And all of these different layers of your system can work well together and they can communicate using the Arrow format or through data files, like Parquet files. And so I think that's really great.

So I've never really believed in like one tool to rule them all. And so I don't view like the success and growth of Polars as necessarily meaning that like pandas is getting phased out or is going to get replaced. Like the reality is that it's not going anywhere. People know how to use it. LLMs are really, really good at writing pandas code.

So especially as long as we have AI copilots helping us write pandas code and our data sets are not hundreds of gigabytes or terabytes, it's a perfectly capable tool that will serve us well for many years to come.

**Laura Mawer:** Definitely. I think, as you say, it covers all the basics and the majority of people just need to get on and do the work and it really does help. A lot of people, yeah.

**Wes McKinney:** I mean, some people have big data, but a lot of people don't. And so I think it would be pedantic to say that everyone needs to use a, call it a scalable data analysis tool, that it'd be this sort of almost like a tyranny of people that are working with terabyte scale data sets to say, well, even for small data sets, you need to use this tool so that it's just everybody's using the same tool.

I mean, maybe in 10 years, maybe we'll all migrate to be using polars. I mean, who knows? But for the time being, I think there's no particular reason to be prescriptive about what tool to use or to say, well, pandas does not scale well beyond a certain size of data set and so we should stop using it.

**Laura Mawer:** Definitely. Brilliant.

So that's kind of looking back. We're gonna have a looking forward question, but before that, is there something that pandas can do that most people don't know and you'd like them to know about?

**Wes McKinney:** That's a good question. I think, I mean, a lot of people know, but I mean, pandas in part because it was originally created in the financial world, like it's actually, it's very good at working with time series data. And so there's many people who use pandas that never interact directly with its time series capabilities.

Like they often look at it as they squint at it and say, well, this is basically an alternative to our data frames or to using or to writing SQL. But actually in many of the other tools outside of the Python world, doing some of these time series type manipulations like binning and bucketing data based on time increments and things like that, the kind of stuff that you would need to do if you were working with high frequency time series data, it's rather difficult to express in many environments.

And I think it's great. Polars has really leaned into this functionality and is also has really robust time series support similar to pandas' time series support. But if you find yourself working with temporal data, any kind of financial data, maybe you're just analyzing your personal finances, pandas' tools for that are really nice.

**Laura Mawer:** Awesome, that's great.

So what is next for you? What's your future hold? What are you looking forward to most?

**Wes McKinney:** Well, I'm a software architect nowadays at Posit, formerly RStudio. So I'm really excited about helping grow and build open source projects and tools at Posit, which has evolved to be not just a company focused on R, but to being a polyglot data science platform company that supports the Python ecosystem as well as the R ecosystem.

And in the future can support other programming languages as they become more popular for data science. If anyone's heard of Mojo, it's like a new programming language from Chris Latner who created Swift. And of course there's Julia, which I know a lot of people are excited about.

But over the last year and a half, I've been pretty involved in the Positron IDE project, which is a new data science IDE from Posit. It's a fork of VS Code. So it's built on the VS Code platform, but it essentially is a re-imagining of the RStudio for classic four-pane data science IDE experience, but built from the ground up to be polyglot. So it works equally well in Python as an R, and you can use it with all of your interactive app development frameworks like Streamlit and Shiny.

The part that I worked on is the data explorer, the data viewer component. If you have a data frame in memory and you click on it in the variables pane and it pops up in this nice window with summary plots and an infinitely scrollable table view of data sets. So I worked on that and I'm continuing to develop on it to build it into a tool that I want to use every day.

So yeah, I'm just really passionate about continuing to support and grow the data science ecosystem. I think I'm at the perfect place to do that and also to be exposed to the problems that people are facing in the business world when it comes to building and maintaining data science platforms over time.

And I maintain a lot of relationships in the open source community, so I'm also looking to continue helping and growing the broader open source ecosystem that connects not just data science tools, but also some of the database systems and data infrastructure that needs to play nicely with the data science ecosystem.

So that keeps me busy, but yeah, I'm not gonna run out of work to do anytime soon.

**Laura Mawer:** No, you are not, definitely not. And Positron, the new IDE is very exciting because our team, I work in Python, but the rest of the team all work in R, so it'd be quite nice to be able to get involved with each other's work and help each other all within one place. So that is very exciting, which brings us nicely back to Earl.

Earl is obviously all about R and Python and all of data science. And we're very much, as I say, looking forward to having you keynote for us in October. Is there anything you're looking forward to seeing at Earl?

**Wes McKinney:** I mean, given how omnipresent LLMs and AI tools have become in making us more productive, I'm interested to see some of the talks related to that. Just for me, like catching up on the latest in what people are thinking about is always just really mind expanding in terms of thinking about new collaborations and new directions for the open source ecosystem.

And the fact that, yeah, I think at Earl, that there will be, yeah, kind of a mixture of programming languages and folks from different backgrounds. It should be a really great conference and I'm excited to be there and to be able to give a keynote.

**Laura Mawer:** Fabulous. Well, thank you ever so much for your time today. It was great talking to you and hearing all about the history of pandas and everything. And we look forward to seeing you at Earl 2025.

**Wes McKinney:** Great. Thanks for seeing everybody there.