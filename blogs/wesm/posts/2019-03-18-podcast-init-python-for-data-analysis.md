---
title: "Wes McKinney's Career in Python for Data Analysis"
summary: "Episode at Podcast.__init__"
date: 2019-03-18T00:00:00
tags: ["episode", "transcript"]
slug: podcast-init-python-for-data-analysis
word_count: 5403
source_file: transcripts/2019-03-18-podcast-init-python-for-data-analysis.md
content_type: transcript
event: "Podcast.__init__"
video_url: "https://www.pythonpodcast.com/wes-mckinney-python-for-data-analysis-episode-203/"
---

*This transcript was obtained from the official Podcast.__init__ website. The summary below is AI-generated.*

## Summary

In this episode of Podcast.__init__, I join host Tobias Macey to discuss my contributions to the Python community, my current projects at Ursa Labs, and the vision for making data analytics easier for everyone.

### Getting Into Python

I first heard of Python as an undergrad at MIT in 2005. A classmate wrote a dynamic programming solution in 20-30 lines of Python compared to my 150 lines of Java. I didn't start programming in Python until 2007-2008 at AQR, when I began rewriting legacy Perl code and building data analysis tools.

### Motivation for Building Data Tools

I was struck by how difficult basic data analysis was. There was a disconnect between what you wanted to do with data and the tools available. SQL felt clumsy for time series data. I got interested in building tools for myself, then expanded to focusing on making others more productive. The process is a virtuous cycle: build tools, get feedback, incorporate improvements.

### Open Source Funding Challenges

I've experienced most standard funding models for open source: corporate sponsorship (AQR paid my salary while I built pandas), academia (PhD at Duke), consulting, and venture-backed startups (Datapad). Each has challenges. Corporate developers may struggle to prioritize work that doesn't directly impact the business. Much of what makes open source successful is unglamorous maintenance work that's hard to justify to a boss.

### Apache Arrow and Ursa Labs

After building pandas, I realized the constraints on user-facing tools lie in the systems domain. In 2015, I gathered developers to define a standardized, language-independent data representation. Arrow provides a common data format that allows collaboration across programming languages with zero-copy data sharing.

I partnered with RStudio and Two Sigma to create Ursa Labs, a nonprofit organization to scale up Arrow development. The mission is developing Arrow as shared computational infrastructure for data science, uniformly accessible from R, Python, Ruby, and other languages.

### Ibis: An Underappreciated Project

Ibis is probably one of the most underappreciated things I've worked on. It's a domain-specific language for interacting with SQL-based systems, very similar to pandas in API but lazy and strongly typed. It brings code reuse to SQL analytics that you can't do in SQL itself. The work on Ibis's expression language is also influencing Arrow's DSL development.

### Looking Forward

I want the future to get here faster. The more open dialogue we have around these problems, the more progress we'll make. We're still in the wild west of data science tooling, with a long way to go toward making things better.

---

## Key Quotes

> "It felt like there was a disconnect between the ability of your mind and brain to think about what you want to do with the data and the actual tools to do it." — Wes McKinney

> "A lot of the work in making open source software projects successful is very unglamorous and falls into this category of things that can be hard to explain to your boss." — Wes McKinney

> "Doing code reviews and fixing esoteric bugs that people report may not, on paper, seem like a high priority, but really is the core stuff that makes open source software projects successful." — Wes McKinney

> "Part of the reason why I'm working on it is because I feel that it is underattended, and it's something that deeply impacts the productivity of the users." — Wes McKinney

> "The reason that having this common data format is so important is that it gives you something to collaborate on." — Wes McKinney

> "I contend that Ibis is probably one of the most underappreciated things that I've worked on because it makes writing really complex SQL a lot more tractable, and it brings a level of code reuse to SQL analytics that you can't really do in SQL." — Wes McKinney

> "The way you reuse code in SQL is by copy and pasting." — Wes McKinney

> "I like to tell people that I want the future to get here faster. I don't want time to pass more quickly, but if we could advance human progress on these kinds of tools by a few years here and there, I think that would be pretty great." — Wes McKinney

> "It still feels like we're a bit in the wild west in terms of the development of systems and tools for doing data science." — Wes McKinney

## Transcript

**Tobias Macey:** Your host as usual is Tobias Macey. And today I'm interviewing Wes McKinney about his contributions to the Python community and his current projects to make data analytics easier for everyone. So, Wes, could you start by introducing yourself?

**Wes McKinney:** Sure. I'm Wes McKinney. Most people know me as the creator of the Python pandas project. So I've been doing development work for data analysis tools for a little over 10 years, and I'm very interested in open source software and funding models for doing more open source software and making data processing systems more powerful and more accessible to normal people.

**Tobias Macey:** And do you remember how you first got introduced to Python?

**Wes McKinney:** I do. The very first time I heard of Python was when I was an undergrad at MIT. I was taking a class on algorithms, a computer science class. I wasn't a computer science major, but we were studying dynamic programming. It was the only part of the course where we actually needed to write code. And I had done a bit of Java, and I wrote my solution to the dynamic programming problem in Java, and it was maybe a 150 lines of code or something.

And a friend of mine, someone named Christine Corbett, told me that she was going to write her solution in Python. She expected it would only be 20 or 30 lines, and I was like, how could that be? How could it be so short?

And she was right. And so that was my first exposure to Python as a programming language. That was in like 2005. But I didn't really start programming in Python until a couple of years later in 2007, when I was working at AQR. And so a colleague of mine named Michael Wong had written some rudimentary distributed computing tools in Python. And I was intrigued by the language from my prior experience with it, and I sort of went down the rabbit hole and started rewriting some legacy Perl code into Python. That was November or December 2007, something like that.

**Tobias Macey:** At this point, you have spent a large portion of your career on building tools and platforms for data science and data analytics, largely in the Python ecosystem. So I'm wondering what your overall motivation is for focusing on that particular problem domain.

**Wes McKinney:** Yeah. Well, I have a mathematics background, so I didn't do a lot of programming in the past. People talk about how they learn to program when they're like 10 or 11 years old or something like that. But I really didn't start programming until much later in life because I realized at some point that I needed to be able to program in order to be useful.

And so I was struck in my first job working at AQR Capital Management up in Greenwich, Connecticut, by how difficult it was to go about very basic data analysis problems. I saw how much time people were spending using Microsoft Excel. I was learning SQL, and I felt that for a lot of basic data wrangling, SQL felt very clumsy. We were working with a lot of time series data, which also felt extremely clumsy. And just in general, it felt like there was a disconnect between the ability of your mind and brain to think about what you want to do with the data and the actual tools to do it.

And so I got really interested in building tools for myself to be more productive, to make the whole process of translating—I have an idea about what I want to do with the data to actually having working code to do that. And as I've expanded, I've been more focused on the needs of other people and looking at how people are working with data and how to make them more productive. And so I find it to be a kind of virtuous cycle where you build tools, you get feedback from people, you see if it makes their work or their lives better, and then you incorporate that feedback into your process.

And as time has gone on, I've gone deeper and deeper into underlying systems problems that are the underpinnings of tools like pandas in general—data analysis tools. Because after spending several years building very user-centric data analysis tools, things that normal people can pick up and use, like somebody that might be a Microsoft Excel user and they want to start writing some Python code instead, I found myself pretty limited in terms of what could be built in those user-facing tools, and the constraints lie in the systems domain. And so some people have asked me, like, why are you working on all these systems problems? It's because they directly impact the kinds of tools that can be built for end users.

**Tobias Macey:** And a large variety of the tools and projects that you've worked on are open source, and at various points, you've worked for different businesses or run your own. And I'm wondering what your experience has been overall in terms of the differences as far as sustainability and levels of sophistication that are possible based on different environments and funding models for the different projects that you've worked on?

**Wes McKinney:** Yeah. So I mean, I've been through pretty much all of the different types of standard funding models for building open source software. So nowadays, if you consider where most of the funding for open source is coming from, it's largely coming from corporations that are allowing their employees to work on open source projects either as their full-time job or maybe they spend anywhere from 20% to 80% of their time working on one or more open source projects. And so in a sense, that was my first exposure. I worked for an investment manager, a financial firm, AQR, from 2007 through 2010. So they effectively were the initial funding for pandas because they paid my salary.

After that, I moved into the next kind of environment where funding comes from academia. I spent a year as a PhD student at Duke University and continued to do some open source development, but I found myself basically split between doing research and doing software development, and I also found that a bit problematic.

I've done consulting, and so sometimes open source gets funded through consulting work. So after I dropped out of grad school, I moved back to New York and did some consulting work with AppNexus, which is an ad tech company, and some other organizations. And basically, I was looking for people that were trying to do more data analysis work in Python, and I used that working with them to kind of influence the development roadmap for pandas.

I also started a company with one of the early pandas developers, Changsha. We started Datapad, which is a venture-backed startup, and we were building a visual analytics tool where all of the back-end technology was the Python data stack, including pandas and a number of other things. And so we ended up shutting down the project in 2014, but part of our objective in starting the company was to direct some of our R&D budget and engineering time back into supporting the underlying open source projects.

So there's challenges with all of those funding models—consulting, academia, startup, single company funding. And just taking you know, working for a company as an example, one of the challenges that open source developers have is that they may run into a conflict of priorities with their parent company where they may feel at liberty to work on problems that are directly relevant to their company's business, but work on maintenance and building features and fixing bugs that do not directly impact the business or don't have, you know, return on investment—they may find it more difficult to prioritize those things.

And a lot of the work in making open source software projects successful is very unglamorous and falls into this category of things that can be hard to explain to your boss, like how you're spending your time. Doing code reviews and fixing esoteric bugs that people report may not, on paper, seem like a high priority, but really is the core stuff that makes open source software projects successful—that grind of taking care of all of the little things and making sure that the project as a whole is healthy and not just your little corner of the project that's immediately relevant to the applications that you're working on.

**Tobias Macey:** And are there any other areas of data science and data analytics that you think are not receiving the attention that they deserve or the support or funding that we should be providing to be able to bring all of our capabilities forward and improve the types of systems that we're able to build, whether in terms of tooling or just general research or awareness?

**Wes McKinney:** Yeah. Well, I guess my answer is a little bit biased. But if you look objectively at where a lot of the money is going and where a lot of the hype and marketing is going, it's really skewed towards machine learning and, quote-unquote, AI. So that's basically machine learning frameworks, deep learning. There's a huge amount of money that's being invested in that. And comparatively, a lot less money and effort and attention is being given to some of the more fundamental problems in data access and kind of interoperability.

So just really basic things like reading data files. You know, if you consider public cloud providers—Google, Amazon, and Microsoft—they support five primary open file formats for data warehousing: CSV, JSON, Avro, Parquet, and ORC. And if you look at the quality of libraries for dealing with those file formats and dealing with those file formats in the context of using a cloud platform, like, the software is really not very good. And it sort of leads you to scratch your head. Like, well, isn't the problem of reading and writing datasets pretty fundamental? And why don't more people work on that? It really perplexes me a lot.

That happens to be what I'm working on in large part, but it's a function of—part of the reason why I'm working on it is because I feel that it is underattended, and it's something that deeply impacts the productivity of the users. And I think when there's a lot of friction in really basic data access and data manipulation, it tends to close off people. They'll choose not to pursue different development approaches to problems because they run into these really basic roadblocks just dealing with the data in a very basic way.

So I'm really interested in having robust and reusable, high-quality solutions to data access and, you know, just dealing with datasets in a multi-language setting. So not just for Python, but for all programming languages.

**Tobias Macey:** And on that front, you've been dedicating a lot of your time and attention to the Arrow project, which I know initially started off as just a way of being able to share data frames in memory between Python and R and has now expanded into the realms that you were discussing—of data access and interoperability with different data formats. So I'm wondering if you can talk a bit about some of the cases where a Python developer would be interested in leveraging Arrow and also being able to use its capability for incorporating capabilities from other runtimes, such as a particular analysis suite in R or something in Julia, versus reimplementing it in Python or finding a different Python library that does some measure of the same things?

**Wes McKinney:** Sure. So the Apache Arrow project—just to give a little bit of history about things, a very brief history about how things got started. I had been building the Datapad company with Changsha and our team in 2013-2014. And we felt like we were boiling the ocean in a number of ways and working on a lot of systems problems around low latency and high-performance analytics in the cloud. And we developed a bunch of columnar analytics tools to be able to power the Datapad application.

We decided to join Cloudera at the end of 2014 to spend more of our time working on systems problems for data science. And my initial appointment when I landed there was to come up with a plan to make Python more of a first-class citizen in the big data world. So that's in the Hadoop and Spark ecosystem. And one of the things that struck me pretty much right out the gate was how fragmented the technology was. And this is just a function of things being open source and there being lots of different corporate players. And so even though hundreds of millions of dollars have been invested in big data projects, the level of interoperability was not very good in terms of sharing data and using multiple computing frameworks in a single application.

It was also very Java-centric, and so a lot of these systems were written in Java, or they were more like black boxes. So I was working with the Apache Impala team. It was still Cloudera Impala back then, but I was interested in plugging Python into Impala and found that really basic issues, like how do we move data between Impala and Python, there was no off-the-shelf technology to do that in a standardized way.

And so I spent a large part of 2015 gathering a group of open source developers to see if there was interest in defining a standardized data representation—basically, a standard data frame that was language-independent. So it could be used in Java, it could be used in Python, C++, R, really used in any language that would be a technology that we could use to essentially tie the room together.

That was the rationale for creating the project. And the reason that having this common data format is so important is that it gives you something to collaborate on. So traditionally, if you consider two systems, they write libraries to read and write datasets. They write algorithms to perform analytics on the datasets. They write messaging layers to move datasets around in a distributed system, around on a network. All of the code and the libraries that people write in general are specialized to the way that the data is represented in memory in the runtime environment.

So by defining this standardized representation, it allows us to create reusable libraries and also to be able to use libraries written in different programming languages in process without any overhead. So now, a few years later, we can use C++ and LLVM to process data that originates in the JVM without any serialization.

And so it's the kind of thing that we always dreamed of, but it's just extremely difficult because you have to define all of these standards and these ways of communicating large datasets in a language-agnostic way.

And so as we've built out the project, our goal has expanded beyond just defining an open standard for tabular datasets—aka data frames—to building essentially a polyglot development platform for building data processing applications.

So if you're working with tabular datasets and you're working in Python or C++, there are building blocks. All of the building blocks that you need to do analytics, to read and write datasets, to send datasets in a distributed system. These are kind of the basic pieces that you could use to build a data frame library like pandas or that you could use to build something more sophisticated like an analytic database.

And so for me, the interest is in partially improving interoperability broadly across the big data world, but I'm also interested in consolidating efforts within the broader data science community. So that's the Python world, the R world. We have a pretty significant contingent of Ruby developers that are really interested in having data science tools for Ruby, and we are building almost all of the core computational system software in C++, and then we build relatively thin bindings to those libraries that we can use in Python and R and Ruby.

And so in other languages, we also have MATLAB kind of bindings to the C++ libraries. So it's really cool that we can implement a feature once and keep improving that implementation, and that code is immediately reusable in all of these places.

And so I believe that as time goes on, we'll start seeing more and more data processing systems that are formed from heterogeneous computational components. So you might see a system that includes some Rust and some C++ and maybe even some Java, and that's possible because we have this unifying technology at the data level.

And so I'm really very excited about that. But as you can imagine, it's one of these, like, frighteningly ambitious projects that hasn't really happened in the past, and part of the reason it hasn't happened is because it's so difficult.

**Tobias Macey:** A lot of your overall sort of recognition in the Python community in particular, but also data science at large, is related to pandas. And most recently, you've been very involved with the Arrow project, but I'm wondering if there are any other achievements that you're particularly proud of that you'd like to call out that people might not necessarily be as familiar with?

**Wes McKinney:** Yeah. So one project that we haven't talked about on this podcast yet is the Ibis project, I-B-I-S. So it's a project that I started when I was at Cloudera, and the idea was to develop a fairly rich DSL—domain-specific language—for interacting with, initially SQL-based systems. And so I wanted to build something that was very similar in its API to pandas and could be adopted by a pandas user, but was lazy and created you would create strongly typed, well-typed expressions, and you could essentially take any SQL query and rewrite it as an Ibis Python expression and write it with Python code.

And, you know, I contend that Ibis is probably one of the most underappreciated things that I've worked on because big fans of it—because it makes writing really complex SQL a lot more tractable, and it brings a level of code reuse to SQL analytics that you can't really do in SQL. So the way you reuse code in SQL is by copy and pasting.

It's something I'm quite proud of, and I think the work in designing the expression language of Ibis is also influencing the work that we're doing in the Arrow project, because we also need to have a DSL for writing down deferred analytical expressions in C++.

And so the fact that I have a fully formed DSL that is a superset of SQL and can express even very complex SQL concepts like correlated subqueries and, you know, things that are traditionally very hard to even think about in pandas—I think it gives us a head start on thinking about how to map declarative SQL analytics onto the imperative, kind of functional approach of Python and essentially composability and function calls.

So I think it's an interesting research project and something I hope that more people take a look at. It's been one of these, like, sleeper projects that has been growing and developing over time and has expanded to support a lot of different SQL systems and now has an in-memory pandas backend.

And Philip Cloud from the pandas project has done a lot of amazing work on that. Christian Suetsch, who is also getting involved in Apache Arrow as a PMC member, has been working with me on that project as well. So he's done a lot of work on Ibis. So it's a cool project.

But I've tended to concentrate my development work in a few areas. So you know, pandas and Ibis and statsmodels or outside of the Arrow project are where most of my development work has gone.

**Tobias Macey:** And it's also worth at least an honorable mention that you wrote the book "Python for Data Analysis." So if anybody hasn't read that, it's probably worth taking a look at that as well as a means of getting introduced to the ecosystem.

**Wes McKinney:** That's true. Yeah. So I wrote my book, "Python for Data Analysis," essentially concurrent with the development of pandas, which was a bit risky thinking back on it. This was, you know, 2012 that I was mostly writing the book, and I did a second edition of the book a couple years ago to update it for Python 3 and for the latest version of pandas. So, you know, if you're learning pandas or you want to learn more about data analysis and Python, the book definitely is a good resource for that.

**Tobias Macey:** And looking forward, what do you have in terms of grand ambitions for the future of the data science community, both inside and outside of the Python ecosystem? And within that, any projects that you are particularly excited to be working on in the near to medium future?

**Wes McKinney:** Yeah. So I helped start the Arrow project while I was at Cloudera in 2015. In 2016, I moved across the country and spent a couple of years working with Two Sigma on systems for data science, and they're really gracious supporters of the Apache Arrow work. And we did, you know, integration between Spark and Arrow to make Python on Spark faster, and we collaborated with IBM on that work. That was really an exciting collaboration to see come together and be successful.

And last year, in order to scale up my work in Apache Arrow, I partnered with RStudio and Two Sigma to create a new organization called Ursa Labs, which is a nonprofit group that enables me to put people to work full time working on the Arrow project. And the mission for Ursa Labs is to develop the Arrow platform as a shared computational infrastructure for data science.

And so my grand ambition for all of this is to have a really powerful computational runtime for data science, for analytics, data access, feature engineering for machine learning and statistical applications that is uniformly accessible from R and Python and Ruby and the different languages that people want to use for data science.

And so it's the kind of thing that hasn't really been possible in the past because of the points of friction that have made it difficult to share code between these programming languages.

And also, part of that ambition is to foster collaboration between the data science world and the database systems community because part of what's missing from data science is the level of computer science and computational systems work that has been done in the analytic database world for the last 20, 25 years. But almost very little of that systems work has made its way into the hands of everyday data scientists.

And so part of the goal of the Arrow project is to create reusable libraries that provide the level of performance and scalability that you have in modern analytic databases, but put those at the fingertips of everyday data scientists and to essentially liberate individuals from being tied to a particular programming language or being able to use multiple programming languages, but not having to be too concerned about whether things are gonna run 10 times slower in one programming language versus the other.

So I think things are on their way toward that goal, and I think setting up the Ursa Labs organization helps provide some scalability in terms of building relationships with more corporations that wish to fund the Arrow work so that we can build a bigger and bigger team as time goes on.

So if anyone listening has interest in funding this work or helping us move faster, you can definitely reach out to me on Twitter or any of the standard communication channels.

**Tobias Macey:** And for anybody who does want to get in touch either for offering funding or support or who are interested in working with you on the Ursa Labs mission, I'll have you add your preferred contact information to the show notes. And to close out the show, is there anything else that we didn't discuss yet that you think we should cover before we close out, or any parting advice that you have for active or aspiring data scientists or any resources that you'd like to recommend?

**Wes McKinney:** I don't think so. But, yeah, it's still a pretty in terms of where we are and on our sort of historical timeline, if you think about maybe what life might be like in 2050 and where are we right now, I think it still feels like we're a bit in the wild west in terms of the development of systems and tools for doing data science. And so I think we have a long way to go.

And you know, I think the more open dialogue we have around these problems and collect ideas and combine and coalesce efforts in building open source software and tools and systems, I think the more progress we'll make.

So you know, I like to tell people that I want the future to get here faster. I don't want time to pass more quickly, but you know, if we could advance human progress on these kinds of tools by a few years here and there, I think that would be pretty great because it means that we'll be able to do more interesting science and, kind of, you know, make things in the world just a little bit better, which you know, I think we can all agree is something we should all be concerned with.

**Tobias Macey:** Well, with that, I'll move us on into the picks. And this week, I'm going to choose the author Roald Dahl. He has written a number of great books for all ages. I have enjoyed them for many years. So if you have never read any of his books, I definitely highly recommend them. The BFG is a great one. James and the Giant Peach. Pretty much anything he's ever written is good fun. So with that, I'll pass it to you, Wes. Do you have any picks this week?

**Wes McKinney:** Well, I just, you know, finally, after being recommended to me several times over the years, I just finished reading "The Soul of a New Machine" by Tracy Kidder. So it's a classic book about engineering or computer engineering from the early 1980s. The book is a bit dated, but still, I think for anyone who's in software or computer engineering, I feel like it's a good read for anyone who's in the field. It helps kind of understand the motivation that drives engineers to build things. So I found it to be a pretty enlightening profile of some people that worked very hard over a very short timeline to build a new computer system. So it gets a high recommendation from me.

**Tobias Macey:** Well, thank you very much for that recommendation. I'll have to take a look at it, and I appreciate you taking the time today to join me and share your experiences working with and building tools for the data science and data analytics communities. I have used the outputs of your labors a number of times. I'm sure a number of other people have as well. So thank you for that, and I hope you enjoy the rest of your day.

**Wes McKinney:** Great. Thank you. Thanks for the conversation.