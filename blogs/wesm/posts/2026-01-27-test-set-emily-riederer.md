---
title: "Emily Riederer: Column selectors, data quality, and learning in public"
summary: "Podcast at The Test Set (Posit)"
date: 2026-01-27T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-emily-riederer
word_count: 10186
source_file: transcripts/2026-01-27-test-set-emily-riederer.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=Yjmu18r_j64"
---

{{< video https://www.youtube.com/watch?v=Yjmu18r_j64 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow, Hadley Wickham, and I talk with Emily Riederer, a data science manager at Capital One who works at the intersection of R, Python, and SQL. Emily describes her journey from a theoretical stats background into industry, where she quickly learned about the messiness of real-world data and the central role of SQL in accessing and transforming it.

We spend a good chunk of the conversation on SQL's strengths and limitations. I talk about my long-running effort to reduce the amount of raw SQL humans have to write, noting that while SQL is declarative and accessible for simple queries, complex business logic in SQL becomes brittle and error-prone. Hadley shares that he actually started with databases before R, building Access databases as a teenager, and now works on dbplyr translating R code to SQL. Emily describes how she gravitated from analytical work toward data engineering, motivated by the pain points of writing and maintaining large SQL scripts without functions, tests, or version control.

The conversation moves to dbt and how it addressed many of these SQL pain points. Emily explains how she built dbtplyr, a dbt package that ported tidyverse-style column selectors into SQL. Column selectors let you apply transformations across sets of columns by name pattern or data type rather than typing each column name individually. We trace the origins of selectors through dplyr, Stata, and possibly SAS, and discuss how they've since appeared in Polars, Ibis, DuckDB, and Spark.

We also discuss naming conventions when porting packages across R and Python, how to make tools feel native to each language, and the story behind GT becoming "Great Tables" in Python. Emily talks about imposter syndrome, the value of blogging about "boring" topics, and her approach of writing for the person she was six to twelve months ago. Toward the end, we share what we'd tell our past selves, and both Hadley and I point to adopting Claude Code earlier. Emily is announced as a keynote speaker at the next Posit Conference.

## Key Quotes

> "I was under this whole illusion of data is this ground truth where we can figure things out about the world. And then I entered into this world where data is this kind of source of chaos that you need to control." -- Emily Riederer

> "Write to the person that is struggling with the things you were struggling with six or twelve months ago. And just try to help them know what you need to know." -- Emily Riederer, quoting Emily Robinson

> "If you aren't in rooms with people that you feel like you have a ton to learn from, that's kind of sad. You're probably also in the wrong rooms." -- Emily Riederer

> "We don't actually know what is hard and easy for them. It's so easy to get stuck... you have to see other people do it. And you're like, oh, I just assumed Claude Code could never do that." -- Michael Chow

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field.

On this episode, we're joined by Emily Riederer, who I think has the distinction of living in that sweet, sweet overlap between Python, SQL, and R harder than anyone else I've ever seen, and is a data science manager at Capital One, and apparently listens to The Test Set, but is not planning to listen to this episode.

**Michael Chow:** Welcome to The Test Set. I'm Michael Chow, and I'm joined by my co-hosts, Wes McKinney, who's a principal architect at Posit, and Hadley Wickham, who's a chief scientist at Posit. And I'm so excited to be here with Emily Riederer, who is a data science manager at Capital One, and I think a sort of icon in the R, Python, SQL community for just putting out so much interesting work in this intersection of Python, SQL, and R. Like recently the article "Python Ergonomics" and some talks around that of how to have a workflow that R users love in Python with things like Polars, and dbtplyr, which was a plugin for the SQL framework dbt, which was a really interesting sort of cross-section of ideas. So Emily, thanks for coming on. So happy to have you.

**Emily Riederer:** Oh yeah, thank you so much for having me. I've loved the pod so much so far. I have not missed a single episode.

**Michael Chow:** Oh, I'm so glad. Honestly, the biggest downside of being on a podcast is I was thinking about it and I'm like, ooh, the next one that comes out, I'm not going to want to listen to.

**Emily Riederer:** Yeah, are you going to listen to your own? I feel like you can't break the streak, you know?

**Michael Chow:** Never, never, never, never. So I think people will be really interested to hear sort of your journey through languages like R, Python, SQL, and the things you've put out. But one interesting question I thought might be good to open up with is maybe just on the role of SQL kind of over the years, since I know you started doing a lot of R work and folks here have done a lot of work in SQL, whether it's like dbtplyr, which translates dplyr in R to SQL, or Ibis, which translates Python to SQL. Emily, I'm really curious to hear, what was your journey into SQL like?

**Emily Riederer:** Very abrupt in some ways, because I think if I think about my educational background, I was in a relatively theoretical stats program. So could prove asymptotic convergence of a lot of things, had very little experience with real world data until I get one of my first internships. I'm asked to make a customer profile, I take the average of customer incomes, and I'm like, we're all rich. But we were not rich. I was just averaging in all the 9999 encoded default values. So that was my first introduction both to databases, to SQL, and just the vagaries of real world data. And I think that had been jarring, because I was under this whole illusion of like, oh, data is this ground truth where we can figure things out about the world. And then I entered into this world where data is this kind of source of chaos that you need to control.

But then kind of coming into industry, I think SQL was one of the main tools for the trade, the only way to kind of access your data before you could get in there with something like R or Python. And pulling from just a single brush I'd had in college with database design and data modeling and normal forms, I think just something about that combined with the tidyverse just so clicked in my mind of like, there's actually a real art to how you set this thing up, how you get the data out, that can really just set you up for success.

**Michael Chow:** Yeah, it feels so real that moving into a business, going to work, and hitting SQL and realizing that there's a process to get the data out. I'm curious, your experiences with SQL too, where you both kind of, it seems like ramped up your SQL involvement at some point.

**Wes McKinney:** I will say I've been in an active -- I think calling it a war against SQL is maybe putting it a little bit strongly, but I've definitely engaged heavily, and I think as has Hadley, in building tools so that humans write a lot less SQL. And I've often felt that SQL is, as a language, it's clearly not going anywhere. It's the lingua franca of databases, but it's also a little bit like assembly code or Fortran code. So you have a lot of the modern niceties of a real programming language, you know, like functions, like reusable code, like code that you can refactor and reuse.

And so early on in my career, I was a bit scarred by hundreds and thousands of lines of copy-and-pasted SQL queries that, you know, there's no tests. And so you're dealing with these highly brittle, very complex, hundreds of lines, many pages long, 10-page-long SQL queries. And the reality is SQL is really alluring in the sense that it's declarative, writing simple SQL queries is easy, but complex business logic, especially in a financial setting, ends up being rather subtle and with a lot of complexities. And so I found myself making the same kinds of mistakes over and over again and seeing other people make mistakes. And so I felt like if only we could essentially abstract away the unpleasantness of SQL and make it easier for humans to essentially author SQL indirectly and to avoid many of those common errors, then we would be doing humanity a great service.

**Hadley Wickham:** I guess I actually started with databases. I did SQL before R. So my dad, a lot of his work involved databases. So we had dinner table conversations about relational data and Codd's third normal form. And when I was in high school, I guess starting from age, I don't know, like 15, I made Access databases as my part-time job. I had to write database documentation as a part-time job, which is kind of crazy looking back at it now. I mean, that's really how I learned to program was in Visual Basic for Applications. That was my first real exposure to programming, real exposure to SQL.

And kind of interestingly, I've been working on dbplyr lately, which translates dplyr code into SQL. And people -- dbplyr has an Access backend and people file issues that it doesn't work. And the fact that even in 2025, people are writing R code to connect to a Microsoft Access database and work with that data. I don't know, that's just kind of mind-blowing to me.

**Michael Chow:** Yeah, that's fair. That does feel like the business reality that someone has an Access database somewhere that they need to wrangle and it's surfacing in these tools. Yeah, I'm so curious. Emily, your journey into data science and how you encountered a lot of these things. Could you explain a little bit just how you became a data scientist? What did that journey look like for you?

**Emily Riederer:** I mean, in some ways, I think I have a very boring or traditional data science background. But in a different read, it's kind of funny because at every step of the way, I knew what I wanted to do, but I probably didn't know the right reason why I wanted to do it. So started out in high school, took my first stats class, just had been a math kid figuring out what can I do with math and just had this idea of this being this amazing truth-seeking, applied way to do math in the real world. And then over time, there's all this hype around big data and data science and it seemed like a natural progression into the field.

I mean, definitely going in, I didn't actually know so much of the things that were true about it. That data science is so much more of an art than a science, that it requires so much engineering skills, and you'll never once again in your life feel the certainty of math, which is probably the thing I liked about math in the first place. But I think in some ways, very linear journey, but it's kind of funny to me looking back on how completely on false pretenses.

**Michael Chow:** I think I saw you mention your early work was more around modeling and using R for modeling, is that right?

**Emily Riederer:** In my time at Capital One, my current employer, I've really worn three very different hats, which also maybe mirrors some of the different tools in the data space. Started out working a lot more on problems of measurement, causal inference, understanding the values of different levers you could pull and customer lifetime values. And that's a lot more exploratory type work, a lot more visualization and modeling and just being a lot more intimate with both the data and the business.

Then I probably took a sharp right turn to move upstream and spent a number of years in more of the tools and data stack. So thinking about building out data pipelines or Python tooling for a broader community to use and really just spending a lot more time thinking about how good coding practices, how automation, how good engineering really enable better analytics, before moving back into the core traditional machine learning modeling type space.

**Michael Chow:** I feel like the switch from modeling to data engineering, it's so intriguing. What was that like? What were the sort of tools you switched into and things you used?

**Emily Riederer:** In some ways, I fell into that one pretty organically, even though the actual roles seem on paper very different. I think in part for what we were talking about -- you join a company and suddenly you find out in school the data sets you were working with was penguins, or I'm old enough I'll date myself and say iris, which is some nice little toy data set. But so much of your work, even if you want to do that really exploratory deep analytical work, is around getting the data.

And I think I both had kind of Wes's reaction of like I'm working on this huge, long, multi-page SQL script and there are all these subqueries and nested tables. And I'm trying to draw it out on a board like the Always Sunny in Philadelphia map.

But at the same time, there was something to me that was so interesting about how -- I was feeling all the pain points so closely that I can't focus on the thing I want until we get data right. So starting to get obsessed with column names, data quality checks, how can you actually do testing and macros and all the things Wes called out that aren't native to SQL.

Spending a lot of my time outside of work trying to understand and build out that part, as well as realizing -- truly understanding data, we talk about from a statistics perspective understanding the data generating process, but there's a separate data generating process that's the data pipeline process, which is the number one thing that predicts what the data errors will be, what the failure cases are. So I think I just fell in love, in service of understanding the problem in the last mile, with thinking about the data.

And then at the same time, the thing I was working on, without going into too much detail, I found myself repeating for many different use cases in a way that just felt anathema to how I saw people in Rstats Twitter outside of work building packages, sharing code -- easier to collaborate with someone in Australia than collaborate with someone in the same company sometimes. And I was like, that seems wrong, which is how I started getting into internal package development, tool building. So I just kind of thought I was doing it all in service of the analytical space, but more and more I found my time and energy gravitating towards these upstream problems.

**Michael Chow:** And if you had to break down for yourself, at that time, what a data pipeline is and what the key pieces are, how would you break that down for someone?

**Emily Riederer:** I mean, the most classic go-to paradigm you can think of is something like extract, load, transform. And even probably before an extract, there's a step we don't talk about a lot that's like logging or encoding -- somehow something that happens in the real world has to be turned into some digital signal.

Then extract being someone has to go capturing that signal and getting all of the different data sets into one centralized place in some sort of format. Depending on your field, maybe that's hitting up APIs, maybe that's working with vendors, maybe that's even being a field scientist and doing manual work in a notebook and then punching it into a computer.

But then once that's loaded into a data lake or a data warehouse, you still need to impose some level of organization. At a high level you can think about it as maybe being more like organizing files in your file system. But there are actually different conventions around that. If you're using blob storage like S3, which is more like literally organizing files on your hard drive, or doing it in a database where in some ways there are a lot more rules and constraints. But that helps you get a lot more stuff for free, like discoverability, some level of constraints and checks on internal integrity, all in service of getting your data structured in a format that it's both easy to maintain, meaning easy to add, update, change to reflect the real world, and also easy for your downstream users to understand and use.

**Michael Chow:** And is this the point where you started using dbt more in some of this stuff?

**Emily Riederer:** Down the road. I think dbt was still really in its infancy at the point I started doing a lot of this. But this is definitely the point where I started feeling very acutely on a daily basis the exact sort of pain points that dbt solves for. I could build my own workflows for like, if I want to test some SQL code, maybe set up test cases and unit tests -- not evident to do that. I had some crazy workflows like pulling data down into an R Markdown notebook from my database and doing a lot more round trips than necessary.

Figuring out a big part of data pipelines is orchestration, which I don't think you run into so much in analysis. But if you have a lot of long running things, especially that depend on systems that aren't in your control, thinking about how do you make sure everything happens in the right order. Not a hard problem -- there are a lot of great open source tools for doing that -- but maybe not always ones analysts have at their disposal.

So I just had my elevator pitch for the seven or ten things that were the biggest pain points of SQL. And then one day I was at the gym listening to a data engineering podcast and heard one of the first interviews about dbt, and I was just like, oh wow, these people happen to be interested in solving some of the exact same problems I've been thinking of.

For a certain time, the data space was a weirdly frequent feeling of that sense of serendipity where you'd be working on something or thinking about something and then within a week somebody put out a dbt, put out an R package, asked the exact same question on Stack Overflow. It was definitely serendipitously -- I was having the same problem as a lot of other people.

**Michael Chow:** Yeah, I felt like it took me a while to understand what dbt was. What was it? Why were people so excited about it? Until I kind of realized it's like an IDE for SQL plus the ability to write functions plus the ability to use -- yeah. And I was like, oh wow, that's like -- you didn't have that already for SQL? That's crazy. And obviously people are going to love it because how do you do software engineering without functions and version control?

**Emily Riederer:** Yeah, I feel like for that reason it's a very hard thing to make the elevator pitch for. Because if you turn to somebody that just has a couple of queries they're running and they're like, hey, what if you broke this into 27 queries and added some YAML files in there, and they're like, oh my goodness, that sounds terrible. But once you've lived in the old world, it's super easy to sell. But then people coming into it now, I know there's a lot of talk of dbt versus SQLGlot and anything that you take as the base case, you can see there's still a lot of room for improvement.

**Michael Chow:** Yeah, if you explain the pitch for dbt it might actually sound kind of more complicated. Like it's quite a bit you're asking the person to do. So if the person's already doing a little bit of SQL, it might be kind of a turn off. But to have all these things then bring testing and version control and engineering practices.

**Wes McKinney:** And there's other things like lineage and essentially stuff that provides insights and intelligence into data pipelines. Otherwise you'd be essentially flying without instrumentation. Of course, now it's funny because at one point this whole ecosystem seemed very fragmented. And now it seems that everything is converging. So hopefully, now that many of the folks -- SQLGlot, dbt, SDF -- they were building intelligence for data engineering, and SDF was acquired by dbt. So all the folks are working together. Hopefully that will yield a more integrated stack of tools that play more nicely together. And people are happy to use.

I've met a lot of these folks and they seem like they're all working for the benefit of the actual users and making things better. So I'm hopeful. The other thing I find exciting is trying to see a little bit of innovation in the SQL space. I think dbt has introduced a number of SQL extensions where you're like, oh my God, why has no one done this before? Like everyone has this need. And yet it's taken dbt to be like, hey, we're going to create something that's very SQL-like. We're not going to throw it out and try to create something completely new. But let's just make a few little tweaks here and there to make it a little more logical, a little more useful.

**Emily Riederer:** Yeah. And I think that's the number one weirdest thing of SQL as a language is it's not one thing, but there's a loose standard that everyone adheres to until they don't. I've loved most of the changes they've dropped. And of course, introducing things like column selectors, which I'm a very big fan of largely thanks to dplyr. But at the same time, that is a tough trade-off too. Because every time you deviate from the grain, it's yes, but it's also slightly less interoperable.

**Hadley Wickham:** SQL is really interesting to me because it's sort of this pre-internet technology in many ways. SQL is a spec. It's an ANSI SQL spec, but you cannot actually get the spec without paying for it. So I actually have one of the few books -- I still have SQL 99 Complete Really. This is the only resource I've been able to find that actually explains how SQL is supposed to work, not how some specific database implements it.

And I think that's -- I find that kind of bizarre. I mean, luckily, now I think recently Claude is filling a lot of that gap for me. Claude seems to have this knowledge of SQL that I could never, through Googling, find the right website, but it must be on the internet because Claude seems to understand it now. But it's just really interesting to me as someone who has been writing this translation layer from R to SQL, to try to figure out what is SQL? What's the official way you're supposed to do this? And what databases actually support and what are the databases that are kind of growing up, you just sort of assume whatever database you use the most is the normal database and everything else is weird. But getting out of that mindset, being like, oh, okay, this is what it's supposed to be like, and every database actually does this incorrectly.

**Emily Riederer:** That is fascinating about the spec. I didn't realize that was so not accessible. There's so many fascinating topics in open source governance, but I've never heard of that. Like here's the rules, but you can't see them.

**Hadley Wickham:** I mean, you can get them, but it costs like $3,000 or something. Maybe it's easier, maybe I just never had the right searches, but I found that mystifying. And kind of even just this idea that if I want people to follow something I've written, to me, it's obvious you want to give that away for free. You don't charge people for it. Part of the pit of success you talk about too, of just get your stuff out there.

**Wes McKinney:** And then I think some of the most successful databases, like Oracle and SQL Server, they are the ones that are most distant from the spec.

**Hadley Wickham:** It's interesting too, the spec, because it's so expensive. When I was working on SQL translation, the question I had was, if I bought this spec, would it even -- would it just be a prescription or would it describe databases as they exist? It was almost hard for me to tell -- did databases follow this or is it a prescription that got --

**Wes McKinney:** I think if you read it, it'd be actually extremely difficult to understand because it goes into a very high level of detail. And you actually want something kind of in between. You want the general, what is this supposed to do, but not every single possible little edge case. If you've ever read the HTML5 specification or anything, it's to just lock down every edge case so people can agree on the way to do it. It's so much detail.

I mean, I think there was an aspiration to make it actually a standard, in the sense that C++ has a standard and then compilers agree to implement that standard. So you can say C++ 14, C++ 17, C++ 20. And I think SQL, they tried to do that. But then the reality was that the business needs of database vendors trumped conforming to the standard. And so they would introduce things that went outside the standard, or of course, things like function names weren't standardized. And so every database has different names for functions. And some databases implement division differently, like whether you can divide by zero -- division by zero has a prescribed behavior in the standard. But then some databases will --

Yeah, mind-blowing thing to me is SQL doesn't -- in general, databases don't support proper floating point math. They don't follow, you know, the way you expect modular arithmetic and division and stuff to work in R and Python and every modern language -- SQL is different. You can't represent -- SQL in general doesn't have a notion of positive and negative infinity or not a number. It's just sort of fascinating that this dinosaur technology still lives today.

**Michael Chow:** Yeah. I think just to circle back and flesh out something you brought up, Emily, you mentioned selectors. And I wonder if it'd be useful to explain what a selector is because it has been added recently to a lot of SQL implementations. Maybe you could talk us through what a selector is?

**Emily Riederer:** Absolutely. And I think that tees me up for a question I've always wanted to ask Hadley. So appreciate that.

So if you think about it -- I'll pander to the R crowd here to start out -- a selector is, you have a data frame, you have a bunch of columns. If you have in fact named your columns well in a standardized way, or if you think about data types, there are a lot of different identifying information you could use to grab out and act on a set of variables. So if you want to do some sort of mass data wrangling process, like say in SQL maybe you want to take the average of every Boolean variable you have in your table. If you're doing that in SQL, you're going to be there a while because you're going to be typing average variable A, average variable 2, average variable 3.

But in some of the more modern programming languages with more flexible APIs, you can have these really nice selectors where you might say for all Boolean values, apply the same transformation. Or if you get a little clever with naming columns in a standardized way, for all of my variables related to this entity, apply this operation. So for large-scale wrangling, it can just be a way to write a lot cleaner code, avoid a lot of typos or copy-paste errors by consolidating your business logic and just applying or mapping it over many different variables.

And I know the first place I saw this was in dplyr. I think now Spark has it. Polars has it. A number of different SQL or SQL variants have it. Pandas has it. But Hadley, I've always wondered, to the best of your knowledge, was dplyr the first tool that had implemented those sort of selectors?

**Hadley Wickham:** I don't know. It seems like my recollection of this is vague. I kind of remember around this time learning that one of the problems people have is that they have a data frame with 800 columns and just selecting the correct columns is a pain. My vague recollection, and I did a little Googling that kind of supports this, is I think Stata had some tools for variable selection. And I think that's where I learned about it from, from Stata users.

Looking at the documentation for Stata, it looks like you can say here's a start of the range and here's the end of the range, here's all the variables with a prefix. So I think that's probably -- I have a very vague recollection that maybe SAS has something similar as well. But yeah, I think it came from statistical software, which is kind of surprising because it does feel like this is something you feel the need for in SQL all the time, because you're just typing out --

I was just looking at pandas to see if it has had it. And I don't think it does. I mean, I haven't been super active in pandas in a long time, but it doesn't look like it has selectors quite in the same way that dplyr does or that DuckDB does now, for example.

**Wes McKinney:** I think the Ibis team implemented it. And I guess Polars and Ibis have selectors similar to dplyr now.

**Emily Riedener:** I knew I'd done something similar in Polars or in Python with pandas of just grabbing out the columns and doing some list comprehensions and throwing that back in. But I didn't want to say that was the best way to go. But I'm fascinated if it came from Stata. My main recollection of Stata from college is you can't have two data frames in memory at the same time. So I did not think of these as bastions of user experience.

**Hadley Wickham:** So interestingly, I'm looking at the docs for this on the Stata webpage, and one of the things it mentions -- my kind of favorite selector in dplyr that literally no one uses is called num_range. And so you give it a prefix, you give it a starting number and an ending number, and it will generate. So you can say select me from X1 to X50 really easily. And the Stata docs specifically say that there's no way to do that easily in Stata. So I don't know. I think that's kind of evidence for -- okay, I was like, well, Stata can't do this, I think that's something useful and I'm going to do that.

**Emily Riederer:** You mean, there's like a spite response? Evidence of a response? You're like --

**Hadley Wickham:** But it's also one of those functions I'm like, I think this is cool. I would have thought people would use this and basically no one does.

**Michael Chow:** Yeah, it's so fun. It's such a small, in a way, such a small behavior, but it is so ubiquitous that it does make a big difference. SQL users, when I've had to type SQL manually, this idea that you just type over and over again the same calculation and just change out column names is kind of mind-blowing. So it is funny, selection does seem like a really simple topic, but it is crazy how much it shapes the quality of life.

**Emily Riedener:** And I think even for me personally, I always wish -- I feel like if that existed in databases natively, people would think more as they build their databases about names as something that can do a thing. And then think about those more carefully, like you would think about designing an API.

When you get into industry or production databases, you get into all these things where there are 10 different ways to abbreviate account ID. So you'll end up with 10 different versions of that, mentally accounting which table they're in. But for me, it was just a big aha moment of, oh, my column names can actually do something if I actually think of them as part of the software.

**Michael Chow:** And this, I think this is very much your "column names as contracts" post. Is that right?

**Emily Riedener:** Yeah, indeed.

**Michael Chow:** Nice. And dbtplyr, your dbt plugin, kind of built on that concept. Can you explain a little bit about that?

**Emily Riedener:** Yeah, exactly. So dbt plugins, packages, whatever you want to call them, are the answer to what was called out about SQL not really having a native function interface. Again, that's wildly database-specific. Some do and some don't. But even the ones that do, it's not really great to use them because then you've just loaded code to a database. It's not really version controlled. You can't really see what it does. Can't access it that easily.

But dbt, taking a step back, is essentially a collection of SQL scripts, macros, and other files organized in a very specific way so it can infer the dependency graph and execute, similar to how an R package is maybe just a lot of R files organized in a smart way so the computer knows what to do with that.

So they abstracted that step forward where you can have dbt packages, which are kind of data-agnostic chunks of SQL code that you can then import and call macros. They can be at the function level. They can be at the table level. They can exist at a lot of different levels of granularity.

So dbtplyr was kind of an early-ish dbt package that I put out there that was essentially stealing a number of things I really liked about the tidyverse, but specifically around column selectors, and trying to port that API into SQL to solve this exact problem of how do I grab out a set of columns and how can I then apply transformations on those in bulk?

**Michael Chow:** What was the reception like? Because when I went to dbt's conference Coalesce in 2022 to give a talk, they were kind of surprised that a person from RStudio came through and they were excited. But the one thing I remember is they kept saying Emily is our representative from the R community. And they pointed to dbtplyr a lot as an example of a really interesting cross-pollination of ideas. What was the reception like? What was it like kind of going into that community?

**Emily Riedener:** I think it was interesting because there were people -- going back to the point about it being a simple idea but that has legs -- there were people that got it, that had seen it before. I know there was one dbt Labs engineer at the time that really knew a lot about R, had been part of that community, really latched onto it.

I think the thing I realized in retrospect was probably calling it dbt selectors would have probably been far more useful and informative for discoverability purposes. Since dbtplyr is kind of a shibboleth of pre-limiting yourself to only having the R part of the community have an earthly idea of what you're talking about or what to expect from it.

**Michael Chow:** Yeah. That's a good point. That's a forever debate -- should I name it after the thing it most resembles for me or should I give it a new name for these people over here?

**Emily Riedener:** Yeah. And then in my head, it was like an homage to dbplyr, which I'd also used a lot, gotten a ton of value from. But naming is hard.

**Michael Chow:** That makes me think of a question we've been struggling with. As we're creating more packages where we have an R version and a Python version, what do we name them? Like, do we give them the same name -- with orbital and pins, we're like, okay, we're going to call the R package and the Python package exactly the same thing. Or do we do it like Great Tables? We've got GT on one hand and Great Tables on the other. And I think there's another case where they're totally different names. Do you have any sense of what you think we should do when we're doing the same idea but implemented in two languages?

**Hadley Wickham:** That's a really interesting question.

**Emily Riedener:** Yeah, because I'm sure too, you're also bound by different namespace availability in both languages. On one hand, with orbital, I find it very satisfying -- if I've heard about it in one language, then it's trivially easy for me to be like, oh yeah, I know they have that thing in the other language. But I do think, even with GT versus Great Tables, in a weird way there's a nice mental namespacing to the fact that I know these do not aspire to be at parity. The APIs within them aren't a hundred percent the same. And it kind of fits my expectations that these are aiming at the same goal, but they may not get there in the exact same way.

**Hadley Wickham:** Yeah. That's interesting. Because orbital is a case where probably the API is simple enough that it's basically the same for R and Python. But obviously the more complicated the package, the more it has to diverge. You want a package that feels R-like and you want a package that feels Python-like. You don't want to be like, oh, I'm writing R code in Python or I'm writing Python code in R.

**Emily Riedener:** That's something I've loved about Michael and Rich's work on both Great Tables and Point Blank. And honestly, even PlotNine manages to get that distinctly more Pythonic feel in the Python version. And I think that's something I think a lot about as I switch between languages. I'm all aware -- I definitely write Python code with an R accent. But at the same time, it feels like you're going to get so much further and have a lot less pain if you are leaning into the conventions of the language you're in. So it's been fun from the outside looking in to see where the design decisions are the same and where they do work off.

**Wes McKinney:** I think R has had a lot of impact on Python as well. And if you look at the API of Polars, the API of Ibis, it's a much more pipe-centric, fluent API. And I think a lot of people, myself included, looked enviously from the Python world into the R world. And then we were like, oh, wouldn't it be nice to just be able to refer to column names inside of expressions and not need to index into a data frame to get a reference to that column to do things? Like the nonstandard evaluation that you have in R that comes from its Lisp heritage.

And so I think the people in Python have tried to replicate some of the flavor or the niceties of that, like the underscore operator and stuff like that. But still it's hard to shoehorn that type of API into Python, which is in many ways the opposite of nonstandard evaluation. It's everything must be as explicit and obvious as possible. And so to try to do things magically is considered unpythonic. There's always been a little bit of tension there -- how do we do nice things on behalf of the user but still make it obvious what's going on at any given time?

**Michael Chow:** Yeah, and that feels like the spectrum -- do we give these things the same name is the very first question. And then that reminds me of the deeper questions of how do we even architect it so it feels Pythonic versus having an R sort of smell to it? It seems so tricky to strike that balance on all those fronts.

**Wes McKinney:** I will say for Great Tables, when we started working on Great Tables, which is a port of the library GT in R to Python, it wasn't available on PyPI. So that kicked off right away the need for a new name. But what I appreciate about Rich is he was open to -- what if we just -- nobody, few people knew that GT stood for Grammar of Tables. So I have to hand it to him for being willing to just retroactively rewrite history and pretend the acronym stood for Great Tables.

**Hadley Wickham:** I think actually a few developers would be willing to retroactively change an acronym.

**Emily Riedener:** I'd actually forgotten that. In my head I'd already translated -- yeah, GT, that stands for Great Tables. I'd forgotten it was Grammar of Tables.

**Hadley Wickham:** Yeah. That's perfect.

**Michael Chow:** I didn't know that story. That's cool. Kind of freaky.

**Emily Riedener:** But I do think on the name front, it's challenging because I think when you give something a new name, it's a chance to really speak just to that audience and really force yourself to address them directly.

**Wes McKinney:** I mean, I do think one of the problems with the Python community is that they don't appreciate puns as much as the R community. So I don't know, I think there are a lot of R package names that are just so perfect for R and just would not feel right in Python. I mean, the other big problem with the Python community is not enough hex stickers -- not enough logos. People don't do logos for their packages. I'm like, what is this? This is a serious problem. This is not a trivial problem because I found like, if you go try to give a talk about Python, you're like, I don't know what to put on the slide. You know what I mean? In R it's like, you need a simple slide, you get a hex sticker. But it's a struggle.

**Emily Riedener:** Yeah, I mean, that was Great Tables. I think we used a pentagon specifically to have a logo, but for it not to be a hex, which I know had objections aesthetically. But I don't know, I think there's something perfect about the Python package logo not tessellating the plane. It just feels like Python.

**Wes McKinney:** Yeah, exactly. Like, ah, we're like, let's all fit together, let's all the packages work together.

**Michael Chow:** Yeah. I'm curious, Emily, how do you choose the things you get into? Because I think digging into column names as contracts and addressing the dbt community is so interesting. How do you kind of choose which threads you want to pull?

**Emily Riedener:** I think I've always really gravitated towards things that might otherwise frustrate me, but just had so much curiosity about -- couldn't they be better? Don't we maybe need more internal packages? Surely there must be a better way to write this SQL code. So really being drawn to the little, more paper-cut everyday problems.

And then I think that's coupled with -- I love just learning about new tools, new algorithms, just squirreling away information that doesn't feel like I'll probably ever need, as save it as a nut for winter.

And I think that was so easy, especially early in my career, in the Renaissance of Rstats Twitter, where you could be a fly on the wall for nonstop conversations with people so much smarter than you doing fascinating things. And then just luckily being able to do a lot of that pattern matching of, oh, I have this problem, and then I heard about dbt. Or I'd really love to never copy-paste this again, and I think there's a thing called R Markdown that exists.

I think it's kind of like I'm curious about the things that frustrate me, and then I have all these tools I want to try, and then sometimes I just get lucky pulling the right tool from the toolbox.

**Michael Chow:** Yeah, it's so cool. And I do think it's so interesting where so much of this really shines in your blog, where you're often stitching together tools, multiple tools in really creative ways. And I know something that came up when preparing for this is imposter syndrome, because I know that with blogs or putting stuff out there, that can be a really big challenge. I'm really curious, your take on what that looks like for you, and maybe advice you'd have for people that are blogging or putting tools out that might feel imposter syndrome.

**Emily Riedener:** Absolutely. I mean, even preparing to join this podcast is like, what have I done? I could just be having a nice afternoon. And I'm talking to three luminaries in the field.

But I think in some ways, it's something that you really have to get comfortable with. Because if you aren't in rooms with people that you feel like you have a ton to learn from, that's kind of sad. You're probably also in the wrong rooms. Going back to the last question, the way I learned was just getting to absorb all this amazing content from other people out there. And if you weren't part of the conversation, you weren't going to get to learn and encounter those things.

So I think I've always somehow managed to get myself in a lot of places that I really had no business being. Even switching between the analyst, engineering, more ML hats, and just getting comfortable jumping in and learning as you go. And same with -- obviously I'm not a PhD political scientist or economist, but the more that I could peer over into those spaces and see the different ways they're talking about causal inference -- I think to a large extent it's very good to feel like you aren't the smartest person, because that tells you you're in the right place where you're learning.

Sharing on the internet is always hard and scary. I think it is so much to the great credit of the R community that it never felt that way. I've thought about if I'd come into the field either five years sooner or five years later, both of which was when the internet seems like it was a more hostile place. Would I have felt confident just putting stuff out there?

But I think Emily Robinson really maybe said it best in a conference talk -- just write to the person that is struggling with the things you were struggling with six or twelve months ago. And just try to help them know what you needed to know. Because I think that's a good way to remember there are other people out there working on the same stuff, and that you do genuinely have something to contribute.

**Michael Chow:** Yeah, it's such a neat way to frame it, of just thinking back as both a way to really emphasize your own growth, but also it does feel nice to be able to take that difference and write it down.

**Emily Riedener:** Yeah. And it's the best way to crystallize your own thoughts. I mean, nothing I write will ever be like, hey guys, this is exactly what I did at work today, because I'm pretty sure my employer would prefer I not go sharing IP all over the internet. But thinking about how would I help somebody else do this thing forces you to actually think at the right level of abstraction.

To just take the trivial example of column names -- it's not, oh, it actually works better for this data set if I do this, but almost like it forces you to generate a theory behind things that is in itself a little bit more reusable.

**Michael Chow:** I'm curious if folks have -- this is maybe a tough exercise -- things they would say to themselves from six to twelve months ago? I'm almost curious to hear what people would tell themselves.

**Hadley Wickham:** I mean, I think I would tell myself to try Claude Code earlier. Maybe I was trying to use it six months ago, but I think that is something. It does feel that as you get further along in your career, your growth definitely slows. There is that period when you're first starting your job and there's this firehose of information and everything is amazing, and you look back at code you wrote six months ago and you're like, this is a heap of shit, why would I ever write that?

But it certainly feels like as you get further in your career, you do plateau. I guess that is more my worry now, that I am plateauing. When I look back at my code from a year ago, I'm like, oh, that's pretty good. I don't know, that feels kind of bad. Like, I should be like, oh, that's kind of shitty Hadley, you could do way better now.

**Wes McKinney:** But I think for me, I started using coding agents basically as soon as I learned about Claude Code. I think it was in March. Was it released in February? It was definitely beginning of this year. So there was a little bit of a -- it took a little time for me to find out about it and then start using it.

But I think I for a long time held off for no particularly good reason on building bespoke tools for myself. Essentially identifying things that in the past, five years ago -- I think there's even an XKCD comic about it, the grid of like, is it worth building a coded solution for a problem? How much time per day will it save you? And that tells you whether it's worth it.

And so now with coding agents, that whole chart needs to get completely redone, because the amount of time it takes, especially if it's building something that's not very hard to build but is just for you, and it makes your life just a little bit better, saves you five minutes a day, ten minutes a day, maybe an hour now and then -- I should have been a little bit more -- I've built things in the last three months that I should have done six months ago or a year ago.

And seeing those successes has given me a sense of more boldness or a willingness to dive into things or set an agent to work building something. Maybe it's only going to save me 10 minutes twice a month, but whenever I have those 10 minutes that it saves me, it's going to be super satisfying. So that's definitely changed my whole perspective on how I do work now.

There's no way to really internalize that knowledge without going through the experience. So I don't know if somebody hit me over the head with that -- Wes, build a bunch of custom tools for yourself to automate your life and your development work -- if I would have believed them that it was possible nine months ago, but I certainly believe it now.

**Michael Chow:** Yeah, I mean, I hate to add to the Claude Code pile, but I think I'm similar. I think it was in a podcast with James Blair where I realized I was the only one not using Claude Code, which was a good realization. But now I'm using Claude Code a lot.

But I think the most interesting thing and surprising thing to me has been -- when I watch my friends use Claude Code, I always learn new things. And so I feel like both I would tell myself to use Claude Code sooner, but also watch people use it. Because I feel like with Claude Code, it's so easy to just go on your own and do stuff. But I'm endlessly surprised at how differently people approach things.

That reminds me of this thing -- if you're a data scientist working with a non-technical person, often the things they think are going to be really hard are often really easy, and the things they think are going to be easy are often really hard. And we're kind of in the same state with Claude Code and these tools. We don't actually know what is hard and easy for them. And it's so easy to get stuck in your -- you have to see other people do it. And you're like, oh, I just assumed Claude Code could never do that. It'd be too hard for it. And then it actually turns out to be an easy problem for it, for whatever reasons. It's really fascinating learning this whole new way of working with this alien intelligence.

**Emily Riedener:** I feel like that abstracts to so many things, just the ability to learn from watching other people do things, which is such a hallmark of R and Python. That's something I've thought about a lot, also going back to SQL. There's so much less open source SQL code on the internet because it's mostly probably code people wrote for business applications. And I'm always fascinated by these little spaces where we are less able to learn from one another.

**Hadley Wickham:** It is. Yeah. It's also just hard to share. This is one of the things I remember when trying to teach SQL -- to teach it, you've got to spin up a database. How do you simulate that environment? And that was definitely one of the things that always motivated me in the design of R packages -- how do you get people to experience that time from downloading it to experiencing a win? And if you have to go away and install Postgres on your computer, then that's a multi-day journey that involves a lot of pain and suffering. And by the time you've got that installed, you're not going to follow through some blog post about learning.

**Emily Riedener:** And the way -- I mean, I feel like with R teaching, you always drop people directly into the analysis. I remember the first time I read R for Data Science, I was like, oh, this is cool because this book isn't trying to teach me what a for loop is for the first time. It's fine, I get it. You're just more like, hey, here's the diamonds data set, let's jump between some wrangling and some visualization. That makes sense. That's a good approach.

And that too is just -- I feel like it was the analogous of watching someone over the shoulder do it, which I think can be a real struggle earlier in your career. If you've never actually gotten to see what good looks like, how can you aspire to it?

**Hadley Wickham:** One of the phrases I found super useful was this idea of tacit knowledge, which I learned from Bill Behrman, who taught this amazing data science course at Stanford that I helped out with. And this idea of all of these things that you know to do, but you'd never think to write down. And when you watch someone working, you're like, oh my God, you can do that?

Even within the tidyverse team, we've worked very closely with each other for a long time. Still when someone shares their screen and they do something and you're like, what? You can right-click on the -- in Positron in the dock and it lists your recent projects? Like, mind blown. You'd never think to write that down because it's just something you're like, oh, everyone knows this. And seeing people in the wild do analysis is just really cool.

**Emily Riedener:** Oh yeah. And I think that almost gets us back to the imposter syndrome too, of just anything anybody can put out in the world is that net new aha moment for someone. I've always felt like to the extent that I have a niche, it's just writing about things that were too boring or ordinary or table stakes that no one else ever bothered to think they'd be interesting to put pen to paper on. But it is just really satisfying when you find that tiny little thing that was too unimportant to say, but actually just feels so good.

**Wes McKinney:** Yeah. I mean, I think that ties kind of perfectly back to column selectors, which just feel like this trivial little thing. But you know, people have thousands of columns in their databases and this is actually a really painful problem. And let's just create one boring little helper that just unlocks, gets rid of all this pain.

**Michael Chow:** Oh yeah. I do feel like selectors too, it's the thing you appreciate when you watch someone coding and typing. You're like, this is so fast. You kind of have to see people do it to really get just how powerful it is.

But I think they're kicking us out. We're getting long in the tooth here. Emily, I love -- I appreciate so much you coming on. I feel like it's been so neat to talk about all these things, both how you've spanned communities, but also I appreciate you surfacing the origins of selectors through Stata, and this really important advice for people with imposter syndrome and how to just get into different areas and embrace discomfort. Address yourself from six to twelve months ago.

I'm also -- I had the -- are we allowed to talk about Posit Conf?

**Hadley Wickham:** Yeah, sure, if Emily's okay with it.

**Michael Chow:** I heard a little bird told me you might be the keynote at the next Posit Conf. Is that?

**Emily Riedener:** Yeah, I am both honored -- and I told Jenny when she emailed me, right now I'm still speechless, which is probably not a good trait for a keynote speaker. But no, I'm so excited.

**Hadley Wickham:** Yeah, we're super excited to have you.

**Emily Riedener:** Well, thank you. I'm honored. Going back to imposter syndrome, a little bit horrified. But I'm honored. Yeah, looking forward to the journey, because I feel like I always -- I learn so much just in the process of bubbling my thoughts back down into words. I feel like the process of writing talks, you just learn so much more about whatever it is you thought you were enough of an expert to talk about.

**Michael Chow:** Yeah, a hundred percent. Well, I feel like we're so lucky to have you at Posit Conf and I'm so excited for the talk and really appreciate you coming on.

**Emily Riedener:** No, truly, thank you all. And thanks for the great show. I'm looking forward to being back as a listener next week.

**Michael Chow:** Yeah. Awesome. Thanks.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with Creative Studio Agi. For more episodes, visit thetestset.co or find us on your favorite podcast platform.