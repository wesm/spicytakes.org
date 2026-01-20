---
title: "Building Data Science Tools in an AI-Native World"
summary: "talk at Earl UK 2025"
date: 2025-10-16T00:00:00
tags: ["talk", "transcript"]
slug: earl-uk-keynote
word_count: 8764
source_file: transcripts/2025-10-16-earl-uk-keynote.md
content_type: transcript
event: "Earl UK 2025"
---

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this keynote, I reflect on nearly 20 years of building data science infrastructure, from creating pandas to co-founding Apache Arrow. I discuss my evolution from builder to architect to catalyst, and my current work at Posit on the Positron IDE, including the Data Explorer component. I trace the history of Arrow and the "composable data stack" vision—modular, interoperable data infrastructure built on open standards—and discuss projects like DuckDB and Polars that have realized this vision.

The second half addresses AI's impact on software development and open source sustainability. I share my journey from AI skeptic to Claude Code user, while raising concerns about AI companies using open source code for training data without contributing back to maintenance. I frame AI as "the new literacy" that everyone should learn, noting that data science work—requiring human judgment and nuance—is more resistant to full automation than other knowledge work. I conclude with advice for the AI era: spend more time reading code than writing it, learn to recognize good architecture, and embrace AI as augmentation rather than replacement.

## Key Quotes

> "We think that the more human judgment and nuance is involved with a certain type of work activity, the more important it is for humans to be closely in the loop and to be very involved with the analysis."

> "I think this is actually a really good thing for open source projects to be able to start and to be able to thrive and to outlive project creators' direct involvement. So I see this as a real success story for open source."

> "Having a culture that is welcoming where people are respectful to others even when they disagree, that people don't make ad hominem attacks... how you design the community, I think it's important to design it in such a way that you're making the tent bigger, you're bringing people in, you're increasing diversity."

> "Your choice of language becomes part of your tribal identity, like I'm an R person, I'm a Python person."

> "We essentially all got tricked into creating a massive corpus of training data for these LLMs."

> "OpenAI generates a ton of pandas code, but OpenAI, as far as I know, is not contributing in a meaningful way to pandas development. So I certainly, if there was a dividend check, it got lost in the mail."

> "The AI ecosystem has been, over the last few years, essentially strip mining all of the open source intellectual property that's been created. So the snake eating its tail, right? So what happens when the snake runs out of tail to eat?"

> "AI is turning into the new literacy and every person needs to learn how to use AI tools and when is the best time, and also when is not the best time to use them in your work."

> "One of the big shifts in computer science education is going to be less writing code, and more reading code, thinking about code, understanding its architecture, studying design patterns, and learning to recognize what good code looks like."

> "When you're having a chicken and egg problem, the best thing you can do is be the chicken."

## Transcript

**Wes McKinney:** We don't have any recording devices in here, right? Okay. Okay, it's me. I'm from that alternate universe with that slide with all those tools on there, so I felt very seen by all of that.

All right, so Laura introduced me a little bit. I'm gonna take you, before I start talking, give a little more detail about AI tools and what I think about them. I'll take you on a tour through my career over coming up on 20 years, starting to build pandas initially for myself, turning into an open-source project, and then pulling on the thread until it turned into a lot of other projects that I've gotten myself involved with.

And really, the way I thought about my career is that I've moved through different modes of work. And initially, I was a builder. I started projects. I worked on them largely alone for a long period of time until I started recruiting people to work with me. And initially, I didn't know that much about building open-source software and open-source communities, and so I had this idea that, like, well, I can just lock myself in a room and work on the projects, essentially what we call skunkworks in the United States. I don't know if you still call them, those projects like that here in the UK.

But at a certain point, I recognized that, after building pandas, that I needed to look at lower-level layers of the stack and how projects like pandas were created so that we can create better infrastructure to build faster, more efficient, more interoperable data science libraries, and also to build bridges between ecosystems. And that's what got me interested in building bridges between the R and Python community and lots of other language and data infrastructure ecosystems.

So this transitioned to more of an architect, like, infrastructure-type thinker in the mid-2010s with the Apache Arrow projects and file formats like Parquet. And more recently, I've shifted, in addition to continuing to do building and thinking about architecture, to more of like a catalyst role of advising and investing in startups, helping identify and grow open-source contributors, basically how to make the tent bigger, bring more people into it, get people thinking about open-source software, open-source infrastructure, and building communities to create lasting and sustainable contributions in the world.

So more recently, the last two years, I work at Posit. That's my main full-time job, where I'm a software architect. So I've been working on the Positron IDE, as well as—Posit used to be RStudio, as you well know. So I'm sure a lot of you use RStudio. And Posit builds, in addition to about half of the business building open-source software for R and Python, also builds enterprise products to make open-source data science work in the enterprise.

So as part of adding Python support to all of Posit's enterprise products, it made sense to rebrand the company to build a new identity around being a polyglot data science platform company. I also founded a company called Voltron Data, working on GPU-accelerated computing for analytics, where I'm the chief scientist. And I have a small investing business called Composed Ventures, where I've been quietly investing in a lot of data companies. I'll talk a little bit more about that later.

But so many of you, if you're familiar with Posit, but part of the reason why people ask me, like, Wes, why are you at Posit? Well, firstly, it's a company whose mission I feel very aligned with, the mission of creating open, free and open-source software for the public good to create a sustainable business that has sufficient revenue to be able to fund and support open-source contributors to work on innovative new projects and to create this virtuous cycle where the open-source side of the business creates demand for the enterprise products because people want to make open-source work in enterprise. And then the money that's generated from the enterprise part of the business flows back to support the open-source contributors.

The company's been going for as long as I've been doing open-source software. I met JJ and Joe, the first two people at RStudio when I was just starting out with pandas about 15 years ago and found that I really identified with their values and wanted to be a part of the mission. And they also were one of the first people, first companies really stepping up to the plate to put serious funds behind Arrow development. And so Posit and Two Sigma in New York were really the two major sources of funding that I received for building Arrow.

If you have not used Positron yet, who's used Positron? All right, I know about most of you. So if you're using Positron, I have done direct work on this recently, especially the data explorer component, which I will show you briefly. It is a next-generation data science IDE. It brings that classic RStudio-like four-pane data science layout as a thick layer built on the VS Code open-source platform. So it is really designed for that code-first data science.

It does have AI features, but as I will discuss throughout this talk, data science is one of those subtle and nuanced areas where human judgment is really important. And we think that the more human judgment and nuance is involved with a certain type of work activity, the more important it is for humans to be closely in the loop and to be very involved with the analysis. So AI may assist you in your work and help you work faster, but we are not trying to replace data scientists or cut data scientists out of the loop because we think that data science is one of the areas that is most resistant to AI automation.

We have been building a couple of AI tools. That being said, the first thing within Positron that you'll find is something called Positron Assistant, which is essentially like Copilot plus an additional layer of context and information that it collects from the Positron environment to provide you with better suggestions, better generated code, as well as better information about what's going on with your data and how to write the code that you need for your analysis. You can plug in your existing Copilot subscription or other model providers that we support.

Of course, if you've ever worked on an AI tool, I think a few people in the audience have worked on building AI systems, but there's a lot of prompt engineering that's associated with specific models, and so adding new models is actually not so easy. So for each model you add, you have to do a bunch of prompt engineering to make sure that the behavior of the assistant is still good.

Another thing that we've been building relatively recently, we released relatively recently, is called DataBot. It's more of an automated, but user-directed data exploration tool. And so the idea is that it is to help, sort of, not completely autonomously, but help explore data sets while giving you a set of, being able to make a set of decisions, like what aspects of the data set do you want to explore, but it handles generating all the code, generating lots of plots, and helping you look at the analysis drive and then drive the decision about where to go next. So it's not trying to automate data science, but really to help you to understand data sets better.

So the Data Explorer, so if you use Positron, this is the part that I've worked on most directly. It is a fast data viewer, so if you use the data viewer in RStudio, I'll go here to Positron, and I'll just load up from a parquet file in Python. So I loaded a data frame into memory, so if you click the little table icon here in the variables pane, that opens the Data Explorer, and so this is a highly custom table grid component, so it's not using a lot of off-the-shelf open-source technology. It has sorting and filtering built in. These statistical plots are all rendered from the data.

One of the cool things about the Data Explorer is you see in my workspace, I have all of these data files, and so here I loaded a parquet file from Python, but here I can just click on a parquet file, and it just magically opens in the Data Explorer. One of my favorite party tricks, actually, is that I set up an association with Positron in my... oh, it opened in Numbers. I'll fix it later, but if I open with Positron, it opens the file in Positron. The same works with CSV files, and that actually is all powered by DuckDB, so it's good that we just had to talk about DuckDB, and so the magic of that feature is actually powered by an embedded DuckDB that ships with Positron, so very familiar with DuckDB and why it is so awesome.

Okay, here we go. Great, but this Data Explorer, again, is about supporting code-first data science, supporting human exploration, helping you see more of your data and get to answers more quickly so you can move forward with your data science work.

All right, nine minutes in. I think I'm doing pretty good.

### My Journey Through Open Source

So I've had a long and pretty winding journey that's included open-source software, entrepreneurship, investing. I've worked for a lot of different companies, but I'm gonna stay focused on the technology mostly and the things that I've been trying to build and the open-source communities that I've been involved with.

So I started building pandas in 2008. I was 23 at the time, so I'm 40 now, so the time has passed. Four years later, in 2012, published the first edition of Python for Data Analysis. 2016, we co-created Apache Arrow. That was a group of open-source developers who got together. We recognized there was an opportunity to build this new data infrastructure layer to help bring interoperability and better performance. 2018, founded Ursa Labs with Posit to support and fund Arrow development. 2021, founded Voltron Data, accelerated computing company based on Apache Arrow. 2023, I rejoined Posit, and in the last two years, I started a venture capital firm, a small one just for my investing in startups, and just this year, I rejoined Voltron Data as its, in a part-time capacity as its chief scientist.

So, these dates and things, not too important, but just kind of a little bit of a backdrop, like where some of the things from this talk will fit into the timeline.

### The pandas Community

But I know a lot of you are familiar with pandas, so I'd like to talk about the pandas community and where my involvement in it and where it has come in the last 15 years since pandas has been an open-source project. But a lot of people are surprised to learn that I haven't been actively contributing to pandas in 12 years.

And initially, it was a personal project, and then I started recruiting some of my colleagues from AQR, a financial firm where I worked in Greenwich, Connecticut, just outside of New York City. And our goal was to try to see if we could make data analysis and data science work happen in Python. Python was not at all a mainstream language. Even using Python in that type of context, like finance, investments, making decisions about money, people thought I was crazy. They're like, no, clearly you must use a compiled language, must be Java or C++, basically. So even convincing people that Python was an okay, safe language to use was not at all easy.

At a certain point in around 2012, 2013, working with the scientific Python community, projects like Jupyter, NumPy, SciPy, Scikit-learn, there started to develop a critical mass of people feeling like Python is a language that's worth learning, worth adopting for this work. It was shortly thereafter that the major machine learning research labs at Facebook, Google, Microsoft, all decided to build their AI frameworks in Python. I guess all of the rest is history at that point.

But in 2013, I transitioned into entrepreneurship, I started a company, and there was a need to hand off the pandas project to the community. And I'm happy to say that this was a very successful transition because the project had built a small and passionate core team, and I think the culture that we created in the project made me feel like it was okay for me to step away from the project and allow it to grow and thrive without my heavy involvement day-to-day.

And so over the last 12 years, the project has scaled to thousands of contributors, and all the while, while Python has become more popular than ever. So I don't know the exact number of unique contributors to pandas, but it's well over 3,000, probably upwards 5,000 at this point. I was surprised to see on PyPI stats that it's being downloaded or installed from the Python package index almost half a billion times a month. So that's pretty crazy.

But I think this is actually a really good thing for open source projects to be able to start and to be able to thrive and to outlive project creators' direct involvement. So I see this as a real success story for open source.

Of course, having the book, Python for Data Analysis, it's now in its third edition. Of course, there's a lot of other pandas books. Matt Harrison's Effective pandas. There's probably 10 or 20 really solid books that treat pandas out there. Mine was the first out. I had a little bit of a head start because I was building the library while writing the book. And so writing the book actually helped me finish the unfinished parts of pandas. And the third edition came out in 2022. Starting to talk to O'Reilly about a fourth edition. So maybe next year, a fourth edition, or maybe 2027, we will see.

But this has been a foundation for people learning, getting oriented in the Python ecosystem. It's been a resource in university classes. So definitely I've been humbled by the popularity of the book and that it's been as useful as it has to so many people. On my shelf at home, I've got basically a big stack of all the translations. I think it's been translated into 10 languages or something like that.

### Open Source Community Architecture

One of the things that wasn't apparent to me when I was starting out in open source is how important this idea of open source community architecture is. That building a healthy open source project isn't just about folks meeting and working their nights and weekends to write the code and push it up to GitHub. But actually how a project communicates, how people work together, how they communicate with the outside world has a big impact on how that community develops, thrives, attracts new contributors.

And so not every open source project is like this. These are things that are important to me, but having a culture that is welcoming where people are respectful to others even when they disagree, that people don't make ad hominem attacks. And there are certainly open source communities like, I don't know, the Linux community where the project creator routinely makes ad hominem attacks on other contributors. And personally, I don't think that that is okay.

And so all open source communities are different, but how you develop, how you design the community, I think it's important to design it in such a way that you're making the tent bigger, you're bringing people in, you're increasing diversity, not only diversity of people's backgrounds, but also the way that they think. You invite disagreement, constructive criticism, differences of opinion, how things should move forward. And then you conduct all of that discussion and dialogue out in the open and public in a respectful manner. And I think that that lends itself to creating a lot healthier community.

So you wanna be able to, a project like pandas has been around in the open for 15 years. You wanna be able to produce a great project that's healthy, that makes releases, that fixes bugs over a long period of time. You wanna be able to attract and retain contributors. And if people decide to move on and work on something else, the project should be okay, should be able to survive in that scenario.

One thing that's been really influential to me has been getting involved in the ASF, the Apache Software Foundation. It is an open source foundation which provides legal copyright protections and other infrastructure to support open source projects, especially ones that have a lot of corporate contributors that are concerned about governance issues and corporate takeovers of open source projects. It developed in the late 90s and now has, I don't know how many ASF projects there are, but there are quite a lot.

But we decided to do Arrow in the ASF in part because we had a lot of companies that were involved in the project that were direct competitors with each other. And so having that level playing field where you would wear your individual hat—I'm contributing to this project as an individual, not as a representative of this company. And so you represent your ideas and your merit as your contributions to the project, but without bringing the authority of, "I'm this company that's worth this many billions of dollars and we're gonna do it this way because I said so." So the ASF is very much not like that.

But one of the things that is really great for collaboration is the fact that everything is required to take place in the open. And this means that decisions don't take place in private discussions, in face-to-face meetings or in private rooms. All discussion, reasoning and dialogue must take place in public channels, especially allowing people to work and collaborate over language boundaries, time zone boundaries. And so this I think has worked really well for this project.

### The Arrow Vision

All right, so all that being said, let me speed a little bit through this and talk about Arrow. And so about a year into Arrow, I gave a talk at JupyterCon New York called "Data Science Without Borders." You can look up the talk on YouTube and watch the whole talk, it's like 18 minutes.

And so the problem that I described in the talk was this idea that the language communities have developed these silos of technology where everybody is solving the same problems over and over again, but without much collaboration. And so we get into these kind of silly disputes about who's got the fastest CSV reader and who can do data frame operations the fastest. This created a lot of consternation and conflict. Conflict maybe is a strong word, but flame wars, internet flame wars between the R and Python community, for example, especially as Python started to get more popular.

And so the idea was what if we had the ability to share code and share infrastructure and have better interoperability between these ecosystems. And so the way I described it back then is your choice of language becomes part of your tribal identity, like I'm an R person, I'm a Python person.

And so the idea that I had at the time was that if we had a way to deal with data frames and deal with data in memory in a portable way, and we could share data efficiently between computing engines and programming languages, and we had lots of really fast data connectors that we all worked together to maintain and make really fast so we can get our data, we can use it consistently between R and Python, all the places, and we need computing engines to be able to process it efficiently. And ideally, we could share this technology so that if we make improvements to the computation engines, those benefits would roll out to everyone all at the same time.

Sounds great. So when I was starting Arrow, this is what I had in mind. I was like, somehow, how do we do this, right? Sounds like total vaporware, but that's actually what I said eight years ago. But I believe that it was a vision worth striving for, and to think about things incrementally, like how could we build towards these goals of shared infrastructure and interoperable, reusable data systems in an incremental fashion and maybe get there in 10 or 15 years.

So the initial approach to this project, Arrow, that we built, the idea was that it was a language-agnostic universal data frame, tabular data representation that's optimized for processing, so for analytics, data transformations. So it's all language-independent, so you can use it in any programming language. You can move it around between environments with very little overhead, maybe some little memory copying, but no reorganizing of the way the data's arranged in memory. So the idea is we wanted to have a representation that's fast to process and can be moved around with minimal overhead.

And so the way you can think about it is, before Arrow, you would have two systems that wanna talk to each other. They'd have to decide on an intermediate format to communicate, like some kind of protocol. Classic thing is like you query a Postgres database, Postgres has a wire protocol that it sends the data to you, you get the data, and you have to convert from that wire protocol into your data frame. So there's a lot of waste and conversion involved. And so the idea is that two systems, system A could produce Arrow, system B can consume Arrow, there's none of that copying, conversion stuff in the middle.

So that's very brief on Arrow. Question is, did it work? It's been eight years, well, it's been almost 10 years since we started Arrow. I think the answer is yes, it did work. It took a really long time, but Arrow's been broadly adopted across all of these domains. You can use it in all of the data science languages. It's used in database systems for acceleration. It's used in machine learning for faster IO connectivity. It's used in data warehouses. Yeah, so we have broad adoption across all of these domains.

We just heard a lot about DuckDB. I think DuckDB is not Arrow native exactly, but it's very Arrow-like internally. And I identified, I met Hannes and Mark from DuckDB very early on, and I recognized the potential of the project and the vision for this SQLite for analytics. And I was like, sign me up. Let's make it work with Arrow. Let's get this thing everywhere. And I'm happy that that was a good bet, and that now we have DuckDB, and it's amazing, and it's realized this vision of putting a fast columnar database literally everywhere. You can run it on your phone, you can run it in the web browser. It's everywhere. Not as ubiquitous as SQLite, but it's getting there.

We also have Polars in Python, which initially with Arrow, I had the aspiration of building a next-generation pandas based on Arrow from the ground up. But turns out, I didn't have to build it. Ritchie Vink started building it in Rust, and at a certain point, I was like, wow, I think he's, you know, Ritchie and the Polars community have got this. Like, I don't need to solve this problem. So Polars has also become really popular alongside pandas. It was built Arrow-native from the ground up, and I think it's an amazing project.

pandas is obviously not going anywhere, but I'm recommending to Python developers to learn both Polars and pandas. And, you know, for smaller datasets, pandas is still great. If you've got larger datasets, data that doesn't fit into memory, Polars is amazing, so definitely use it.

Out of the Arrow ecosystem, there's a project you may not have heard of called DataFusion, which developed out of the Rust ecosystem, which is a little bit similar to DuckDB in some ways, in the sense that it is an embeddable query engine, but it's, rather than being a full-stack system that's a little bit closed and monolithic, DataFusion is a library that is open and designed to be configurable and customizable for particular use cases. And you can see the evident success of the project by the fact that there's, I don't know how many, but there's a very large number of companies that are building new production query engines based on DataFusion. And essentially what's happened is that DataFusion has gotten so good that there's almost no motivation for somebody to start building a new database system in Rust when they could build a database system with DataFusion as the foundation.

### The Evolution of Computing Hardware

Another thing that's been going on that Arrow was also a part of was this evolution in computing hardware. So maybe some of you have seen the original MapReduce paper. So MapReduce, Google MapReduce, this was the original big data paper that set off Hadoop and the big data revolution about 20 years ago.

But does anyone know how many, in 2004, how many CPU cores do you think was standard in a server, in a data center at that time, like that Jeff Dean and the people at Google were using? The answer's one. So, which is surprising, it actually surprised me. I thought there were more. I thought it might have been four or something.

Today, you can rent a server in AWS with 192 physical cores, dual AMD, or you can rent an NVIDIA Blackwell GPU with 18,000 CUDA cores. At the same time, storage has gotten 100 to 1,000 times faster, networking has gotten 1,000 times faster. What was big data in 2004 is now doable on this MacBook Air, so that's interesting. So, our approach to building systems should also change a great deal, and so that's something that's really been in the background of all this.

### The Composable Data Stack

So, as time moved on with Arrow and the uptake, especially among major tech companies around the world, started to happen, we started coming up with this general idea of what we now call the composable data stack or composable data management. And so, it's this idea of rebuilding all of our data infrastructure and AI infrastructure around technologies like Arrow that lend themselves to interchangeability, modularity, and system reuse.

And so, rather than having these monolithic, vertically integrated systems with lots of duplication of effort, every system rebuilding the same things over and over and over again, we would spend more effort, of course, upfront to build reusable components that we can mix and match to build different types of data processing systems.

So, what a composable stack would look like is you have a composable query layer using dplyr in R, dplyr-type syntax, or if you use Ibis in Python, or you could use SQL. There's many different execution engines that you could use for processing. In the foundation, we have storage formats, Arrow, Parquet, there's a lot of new file formats that are in development, Data Lake systems, Iceberg, things like that.

Ibis was a project that I started around the same time as Arrow, seeing this composable future as like a hypothetical. And I was like, well, we should build something in Python that would help unlock this if it happens one day. And so, the idea was to create a portable Python DataFrame API that could support lots of different backends. And so now, if you use Ibis now, it has first-class support for DuckDB, as well as, most likely, any other SQL or data warehouse that you're using, as well as things like pandas and Polars. So, I definitely don't have too much time to go into detail in this talk, but I encourage you to check it out.

Another thing that's been going on is the DuckDB authors, before they created DuckDB, they wrote this paper in 2017. You can see a lot of stuff was going on in the mid-2010s, called "Don't Hold My Data Hostage." And so, it was this idea that a lot of modern data storage systems are bottlenecked when it comes to exporting data from the database. And so, the idea was that the query might run fast, but then there's all this conversion and serializing the data to be able to return the results to the consuming application.

And so, a thing that we've done in Arrow, so you've probably had the problem of, you run a query and it's like, why does it take so long to get the data into pandas or the data into R out of my SQL database? It seems like it shouldn't take that long. But the idea is that, traditionally, a database would produce the result, they convert it to an intermediate format, send it over the network, and then you have to convert from that intermediate format into your data frame. So, this is kind of like the Arrow problem.

And so, what ADBC is, is Arrow Database Connectivity. And so, this is, I think, the latest and, I think, best solution to this problem now that we have Arrow, and Arrow's been widely adopted. Back in 2017, with this paper, there was really nothing of the sort, but it was identifying the problem and showing, definitively, that this is a problem and it's causing applications to be much slower than they could be.

Anyway, so, I've helped nudge this along through funding DuckDB, through the DuckDB Foundation, and there's a new company, Rill Data, that's helping drive this work forward. So, keep an eye out for that.

### Why Did This Take So Long?

All right. So, before I shift over to talk about my excitement and concerns about AI, I think, in general, one of the questions that people often ask me about Arrow is, like, why did it take so long to get here? And, why did it take 10 years to build? Why did nobody start working on this until 2015, 2016? Couldn't we have done this in the 1990s?

And, it's complicated. But, really, if you think about the development of the internet and the whole, the way that big data has arisen, initially, everyone was very concerned with simply data scale. How do we store it? How do we process it? We don't care if it's inefficient. We don't care about this modularity, composability. We just have lots of data, we have to process it because pointy-haired bosses are expecting me to store and process all of this data.

So, once people had dealt with the scale problem, they could start to think about speed and efficiency. So, speed, first, efficiency, second. And so, this whole composability idea is much more of a, very up the data systems Maslow hierarchy, and so that's part of why I think that it's taken so long to get here because we really had to move up the stack of solving these problems incrementally before there was a collective realization that we needed to put our minds together and think through these ideas of interoperability and composability.

So, if you're using Python, it is now possible to build multi-engine architectures with libraries like Ibis so that you can write your code once and then you can work with small data in pandas. You can transition easily to DuckDB or Polars if you need to run something on a Spark cluster or in BigQuery or something like that. You can do that with very little code changes, which is great.

### AI: Excitement and Concerns

All right. So, right now is one of the most interesting and concerning and exciting times, I think, in my career. I don't think anyone is really ready for ChatGPT and LLMs and all the stuff that's happened in the last couple of years, but I've been grappling with it and I have a lot of thoughts about it that I'd like to share with you.

So, first of all, I am not an AI skeptic. I started out, actually, as an AI skeptic, and throughout 2024, I used ChatGPT a little bit, and beyond using ChatGPT to write recipes and translate from one foreign language to another, or write little snippets of Python code, I didn't really use it for that much. I certainly wasn't using it for software development.

And it really wasn't until, I would say, like February or March of this year that I learned about Claude Code, and I tried it, and I'd used Cursor, I'd used Windsurf, I'd used Copilot. Like, nothing really clicked, and somehow, I don't know what it was about Claude Code, but it suddenly clicked.

And so, I'm now completely obsessed with Claude Code. I use it almost every day. I have a max plan. I frequently max out my max plan. And it's been a little bit mind-blowing. It's simultaneously scary to be writing and generating all this code, that I do spend a lot of time reading it, giving feedback, but I have a lot of experience reading code and thinking about software and giving feedback, and one of the challenges is that not everyone has all that experience and the ability to give the kind of feedback that I'm able to give the agent, and that does create challenges.

So, I'm writing a lot more code with AI assistance, writing a lot less code by hand, which is interesting and scary. I did use Claude Code to make my slides, no joke.

And so, anyway, pandas was open sourced 15 years ago, and GitHub got started also around 15 years ago, and so we've spent the last decade and a half creating the entirety of humanity, creating enormous amounts of code and intellectual property and publishing it for free on the internet.

So, we essentially all got tricked into creating a massive corpus of training data for these LLMs, and it shouldn't surprise no one that ChatGPT and Claude and the LLMs are incredibly proficient at producing pandas code, and very good pandas code, idiomatic pandas code. And this shouldn't surprise anyone because of the just enormous amounts of training data that exist in the wild. I don't know how many repositories there are on GitHub that use pandas. It's gotta be hundreds of thousands at this point. The amount of Stack Overflow answers that have been written, the amount of Stack Overflow answers I have written, the amount of tutorials that people have created, like, it's just, there's just an insane amount of data related to projects like pandas on the internet.

And, yeah, and not only that, but people who couldn't do pandas before, either they lacked programming skills, lacked technical skills. I knew something was up when my brother, who is an accountant, started asking me about pandas. Like, Wes, tell me about pandas. So, yeah, to have this sudden surge of everyone in the world being able to use pandas to do stuff, it creates a lot of sustainability questions about the broader open source ecosystem.

### Open Source Sustainability Crisis

OpenAI generates a ton of pandas code, but OpenAI, as far as I know, is not contributing in a meaningful way to pandas development. So I certainly, if there was a dividend check, it got lost in the mail. So they're not maintaining the library, they're not fixing bugs, they're not writing documentation, they're not paying developers. It's not just pandas, it's really any open source project.

So it's essentially, you know, the AI ecosystem has been, over the last few years, essentially has been strip mining all of the open source intellectual property that's been created. So the snake, you know, eating its tail, right? So what happens when the snake runs out of tail to eat? And some people think that maybe the AI tools, you know, talk about AGI and super intelligence, and maybe the AI tools have become so good that they can write the whole next generation of open source software, and so maybe humans are not needed, but I don't know that I quite believe that yet.

So it's an extractive, not a symbiotic relationship. And, you know, if you think about the amount of money that is being put into delivering ChatGPT and all the LLMs on your phone and on every product that you use and every IDE and everything, there's literally, you know, trillions of dollars in CapEx that has been allocated and budgeted to build data centers and buy graphics cards and to train models.

And, you know, there's also the question of whether or not those trillions of dollars in investment is gonna be sustainable or whether people are gonna be, companies and people are gonna be willing to pay enough for AI products to recover that investment. That's what this talk is about.

I don't know exactly how much money is spent on open-source patronage, basically supporting, paying open-source developers to develop and maintain open-source projects. But my guess is that it's at least like one one-thousandth, probably less than one one-thousandth of the amount of money that's being put into building and delivering AI. So that, you know, that really does raise questions.

And we were already in a maintainer crisis. I think even before AI in the mid-2010s, late 2010s, there was a lot of discussion about, you know, there was the Heartbleed bug, OpenSSL. Open-source maintainers are overworked and underpaid, often unpaid, often volunteers. And that creates, you know, I've worked for many years to make open-source sustainable, to raise money, to create business cases for companies to pay money to do Arrow development, for example. And even that, you know, to have a team of 10 people over a long period of time has been very difficult and has required me to make a lot of personal career financial sacrifices to make that possible.

### AI Agents Are Coming

You know, but at the same time, you know, like AI agents are coming no matter what we do. They work differently from humans. Humans are annoying. They gotta eat, they have to go to sleep, you know, gotta take bathroom breaks. Like sometimes you have to stop and think. Collaboration takes time. Like talking to your fellow co-workers, you know, weekends. You can't work seven days a week.

But agents, they can work 24 hours a day, you know, seven days a week, never tire, think constantly, make decisions continuously, constantly rerun analysis. You have a question or if something changes, it sends you an instant report, you know, in the moment rather than having to like send an email to somebody asking them to run an analysis.

So, you know, I think we are no matter what going to see a wave of AI agents doing data science work and running, you know, tons of queries, querying data, working with it, reasoning about it, and repeat. So, but that also creates this like infrastructure challenge where, you know, if you extrapolate like AI agents are gonna end up doing, you know, 99% or, you know, maybe more fraction of the computing on data. A lot of the work may be like repetitive or like mundane, but still like you think about like the carbon footprint and just the amount of like, you know, computers that they're gonna be kept busy by all this work. And it's clear that like the work is shifting from humans to, is going to shift from humans to AI agents. So this creates like cost problems, power consumption problems, and so forth.

### GPU-Accelerated Computing

And, you know, GPUs are being used to, you know, GPUs are being used to train and deliver AI models. But, you know, we, so we started a company a few years ago, Voltron Data, and, you know, the idea was that GPUs and accelerated hardware can deliver, can solve, you know, certainly do AI at a tiny fraction of the cost that you could do it on CPUs, for example. And so GPUs became very popular for good reason for AI training and AI inference.

And so if we could move more of those workloads into, onto GPUs and into the same data centers where the AI models are running, that we could also drive down the cost of running more heterogeneous data workloads so that entire, you know, data querying, data analysis pipelines could be run at much lower cost than they are, you know, currently run. So this is one of the things that, you know, that we've been doing last, you know, four and a half years at Voltron Data.

We built a GPU accelerated data processing engine that supports NVIDIA and AMD GPUs. Can run in the same data centers as the AI models and the goal is to deliver, and what we, you know, think in the benchmarks we have achieved, data processing at a 10 to 100x of the cost reduction. It may not be enough to satisfy the hunger of the AI agents, but I think it is definitely, definitely helping, but this is a problem that I do think, I do think a lot about.

I do think the composable data stack is also going to be important for providing a simpler and, you know, narrower surface area for the AI agents to do their work, especially to have, to be able to use SQL or APIs like Ibis to generate descriptions of what computation they want to run and then to handle, to have the execution and everything else be handled by composable frameworks where you can delegate the work to the most efficient engine for the work that the agent needs.

So it might be DuckDB, it might be, you know, it might be Spark, it might be Theseus. Like, in the future I expect that we'll have custom hardware for data analytics. I'm not sure how long that'll take, but, you know, 10 years, 20 years, like it's coming eventually.

### AI as the New Literacy

So anyway, starting to wrap up here, but shared a lot of concerns about AI, but I am really bullish on it as a technology, especially in terms of augmenting human cognition, making your intellectual labor, your judgment more productive, enabling you to work faster and more productively.

I think I heard this in a podcast, but I do agree with this, that I think that AI is turning into the new literacy and that every person needs to learn how to use AI tools and when is the best time, and also when is not the best time to use them in your work. And learning the difference does take time, and I'm still finding myself, you know, day-to-day finding scenarios where, you know, Claude Code worked great over here, didn't work great over here, and learning to recognize the difference helps me save time, but to spend two or three hours with an agent and to end up with a pile of stuff that I have to delete is not very fun, and that has happened to me.

I think I'm less concerned about people getting replaced by AI. I think people who do not learn how to use AI, I think their jobs will be increasingly at risk, and so my recommendation to everyone is, you know, learn AI, learn when to use AI, and learn how to use coding agents, and so if you've not used Claude Code, run, don't walk. Like, it really is amazing, and I was skeptical until I started using it to build stuff, and a lot of the work that I've done recently in Positron on the Data Explorer, for example, has been done by Claude Code.

So on the spectrum of tasks, so I heard this framework that I thought was useful, so tasks that are highly predictable, you know, without a lot of need for human judgment, I think are increasingly going to be automated by AI, but data science work, you know, does need a human in the loop, and so AI can make you more productive, but there's always a need for you, so I think that the data scientist's jobs are a lot more safe than a lot of other knowledge workers, and so that does make me optimistic, you know, for the future.

Another thing that I've noticed, and so if you haven't, you know, used coding agents to build a ton of stuff, is that communication often is the bottleneck, and your ability to communicate and articulate exactly what you want, and so I think, and I've been saying to people here in the conference, that I think one of the big shifts in computer science education is going to be less writing code, and more reading code, thinking about code, understanding its architecture, studying design patterns, and learning to recognize what good code looks like, what bad code looks like, and how to articulate those ideas in a way that is actionable for the agent.

And so it used to be that, you know, when I was in school, I learned Java, and then I learned Python, and I took an algorithms class and some things like that, but I think that the learning, you know, I don't even remember the syntax for print hello world in Java anymore, right, but learning kind of how to do those things manually is going to be less and less of a focus, and more like, you know, being able to look at a large amount of code and to instantly recognize, like, oh, this code is factored wrong, like, this has got code duplication, or, like, some other type of, you know, code or architectural smell, so that you can articulate that to the agent and ask it to fix it.

I don't think that, at the moment, and I don't know for how long, but AI is not currently able to build all of its own data and data processing infrastructure, and so in that sense, technologies like Arrow I would describe as an AI-resistant technology, which is kind of cool. Maybe that will change, but we're a long way from that, in my opinion.

Things like dplyr and Ibis that enable you to switch backends without changing your code are really powerful in this new world of heterogeneous hardware. And AI has to use all of our tools, too, so how we access data, how we process it. You know, none of that's going away. MCP is not an efficient way to access and deal with data, and so I see a lot of what's happening in the AI world as largely orthogonal to, like, the more mundane work of data systems and data science tools.

### Closing Thoughts

So, anyway, our new AI overlords, perhaps, but I believe we'll be, at minimum, be working together, hopefully productively, for a long period of time. I'm concerned a lot about the sustainability problems of continuing to build and build new open-source projects, especially when more and more of the code is gonna be written by LLMs.

I do think that we're starting to see discussion and talk about what it means to create data systems that are built for AI agents first and not humans, so that's interesting. Yeah, I'm gonna continue to be laboring for open-source sustainability, and hopefully some of the things I said, like, stoked your curiosity about how the projects that you use every day will continue to function when the AI companies are increasingly the only way that people are interacting with and consuming these projects.

And I do believe that augmenting humans and enhancing your judgment with better productivity from AI is the way to go, and not replacing you. So, anyway, that's pretty much the end, but I was talking a little bit about computer science education, so if there's young people in your life who are concerned about the new world that they are entering, I think spending more time reading code, less time writing code, reading books about design patterns and all that will help you a lot, and learn how to use AI to build stuff, because it's super fun. I've been having fun, at least.

But I'll close this with a quote from my JupyterCon 2017 talk when I said, when you're having a chicken and egg problem, the best thing you can do is be the chicken. So I encourage you all to join me in being the chicken, and to navigate this crazy world that we are entering.

Thank you.