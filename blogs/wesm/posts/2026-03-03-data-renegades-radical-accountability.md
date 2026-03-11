---
title: "Radical Accountability in Software"
summary: "Podcast at Data Renegades (Heavybit)"
date: 2026-03-03T00:00:00
tags: ["podcast", "transcript"]
slug: data-renegades-radical-accountability
word_count: 11056
source_file: transcripts/2026-03-03-data-renegades-radical-accountability.md
content_type: transcript
event: "Data Renegades (Heavybit)"
video_url: "https://www.youtube.com/watch?v=neeROOdM39w"
---

{{< video https://www.youtube.com/watch?v=neeROOdM39w >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this conversation with CL Kao and Dori Wilson on the Data Renegades podcast, I cover the origins of pandas, the state of AI in data infrastructure, and a concept I call "radical accountability" in software.

I recount building pandas at AQR during the 2008 financial crisis, driven by frustration with existing data tools. The project grew through direct feedback loops with users -- watching Excel power users discover what scripted, reproducible workflows could do for them. I wrote the first edition of Python for Data Analysis during the same period, which led to literal "book driven development" where gaps in the book forced me to build missing features in pandas.

I discuss why data engineering and database systems are among the last frontiers of AI-resistant technology. Text-to-SQL still struggles badly with real-world enterprise schemas. Michael Stonebraker presented the Beaver benchmark at CIDR showing that foundation models fail to generate correct SQL against complex institutional databases like MIT's. Semantic modeling languages like Malloy -- Lloyd Tabb's successor to LookML -- can reduce the dimensionality of what LLMs need to reason about by encoding table relationships, join types, and metric definitions.

I describe Spicy Takes, a side project that scrapes and summarizes tech blogs, grades quotes by "spiciness," and currently covers 23 authors and 31,000 quotes -- built entirely through vibe coding sessions for essentially just the cost of my AI subscriptions.

The core thesis: AI has created a wave of "radical accountability" for software creators. The old excuse of not being able to afford the engineering time to do things right no longer holds. The only remaining excuses are not knowing what the right thing to do is, or having bad taste. Software vendors shipping mediocre products will lose their customers to empowered individuals who can build better alternatives with coding agents. I predict 2026 will be about examining everything that is bad or mediocre in the software industry and burning it to the ground.

On startups: the bar for MVPs is higher -- showing up to a pitch without a working prototype is now a red flag. Differentiation will be harder amid a sea of AI-generated project slop. Credibility of the people involved will matter more than feature lists or documentation, because it will be harder to judge software quality from the outside. The data market consolidation (Fivetran acquiring Census, dbt, Tobiko Data; Databricks acquiring broadly) is healthy -- the modern data stack landscape had become too fragmented and was creating buyer fatigue.

I close by encouraging everyone to build personal software. I built Money Flow for personal finance, MSGVault for email archiving, and Roborev for continuous agent code review -- all tools tailored to exactly what I want. The cost of building something that makes your life better has dropped to near zero.

## Key Quotes

> "Data engineering and data processing systems, database systems, are maybe one of the last frontiers of AI resistant technology." -- Wes McKinney

> "Right now you can have exactly what you want. You no longer have to make compromises and not have the thing that you want. And I think that's frankly kind of wonderful." -- Wes McKinney

> "AI in a way is going to create this wave of what I would describe as radical accountability for creators of software projects where you do not have to accept things being mediocre, things being bad anymore." -- Wes McKinney

> "The only excuse is that you don't know what the right thing to do is or you have bad taste. Usually it's some combination of both." -- Wes McKinney

> "2026 is going to be about swatching kind of the software industry, like take a look at everything that is bad, everything that is mediocre, and burning it all to the ground and let a thousand new trees grow fresh." -- Wes McKinney

> "At the earliest stage of a company, if you come to a pitch and you have nothing to demo, that's almost a red flag at this point." -- Wes McKinney

> "People aren't going to be able to look at the product and judge just purely based on the website and the feature list and the documentation whether the product is good or not. It's going to be based on, are the people involved credible?" -- Wes McKinney

> "Pandas wasn't designed like a database. It probably should have been, but I didn't know what I was doing whenever I started the project." -- Wes McKinney

## Transcript

**Dori Wilson:** Hey, I'm Dori Wilson, Head of Data and Growth at Recce.

**CL Kao:** Hi, I'm CL, CEO and founder of Recce. Welcome to Data Renegades. Today our guest is Wes McKinney. Wes McKinney is the author of Pandas, the Python library that fundamentally changed on how the world does data analysis.

He also co-created Apache Arrow, the open standard that powers much of the modern data infrastructure. I think over the years he tackles the important gaps in data infra piece by piece, as a developer, as a founder, and also as an investor. He's currently a principal architect at Posit.

Welcome to the show, Wes.

**Wes McKinney:** Thanks for having me.

**Dori:** Yeah, I just want to add to your Python for Data Analysis is incredible. It's what allowed me to go from economics to data science. I was an R user and so it helped me get a job in the industry. So just, I love that book. Thank you so much.

**Wes:** Yeah, of course. Yeah. I mean, right now I'm having like almost this existential thought of like, maybe people are not going to read books like Python for Data Analysis anymore. I'm actually working on the fourth edition of the book, but there is a part of me that is concerned that like, that whole media might be dead in a year or two years. It's like people are just not going to read books to learn how to do stuff anymore.

So I guess we can talk more about that as we get into the conversation. But it's true that the book did help a lot of people in the past. And I'm happy that it exists and it served a really useful purpose to help people get over the hurdle of beginning to use Python and learning how to use Pandas and growing that ecosystem of software.

So even if people don't read it in the future, I'm still okay. It had a pretty good run. It's been 14 years since the first edition came out, so it's been a pretty good run.

**Dori:** Definitely. I mean, it changed my career.

**CL:** Yeah. We're so thrilled to have you here. You have this massive experience and wisdom about creating Pandas like 20 years ago. Right? And then Arrow, like 10 years ago and all the other projects they're working on nowadays.

**Wes:** Yeah.

I really like to go where I'm needed. I think in 2008, I felt that I was needed to work on what turned into Pandas and that really motivated me. I felt like there was this potential for Python. And so I felt a lot of satisfaction to perceive the need and then fill that gap. And when we started The Arrow Project 10 years ago, this month is actually the 10th birthday of Arrow, I also had that same feeling of like, here's a problem that needs to be solved and I feel like I can contribute here and I feel needed.

And so of course right now, I'm having the same thoughts about agentic software engineering. And so I'm a little bit down that rabbit hole at the moment. But yeah, we'll see where things lead in the future.

**CL:** We'll definitely get in that in a bit.

**Dori:** Yeah. So taking a step back, when you went to full time on Pandas, what made you decide to do that jump? Because that's like an unpaid, open source library.

**Wes:** It was an experiment, I will say. I was fortunate in that I graduated from college without any student loan debt. And so that was one massive enabler and that I could, at 20, let's see-- How old was I? I dropped out of grad school and I worked full time on Pandas. I was 26, so I moved to New York City.

I had some money saved up for my first job, which was in finance, so I had no debt. I had saved about a year's worth of living expenses from my job. I lived very frugally in those days. So basically I figured, well, the worst that could happen is that I spend all my savings and I build a really interesting software project and maybe it goes nowhere, but at least I will have tried.

And so I think in my 26 year old lizard brain, I felt like that was the gamble that I was willing to make. And even if I ended up being wrong and Pandas wasn't that useful, that I just felt like I had to really give it 110%. And so I was living in a mouse infested apartment in the East Village in New York City.

Literally, like there were mice, like I trapped like a bunch of mice. And so I was just like, I would just wake up and write Python code. I'd take a break to eat and go to yoga and then I would work, come back home, like eat dinner and work until the late hours.

And so I was just going from like basically probably 8 o'clock in the morning until midnight or 1 o'clock in the morning pretty much every day, seven days a week for that year or so.

**Dori:** That's founder hours.

**Wes:** Yeah, so I was working founder hours, working on Pandas and that's also the same period that I wrote the first version of Python for Data Analysis. So I was kind of working on writing, building Pandas. And at that point I was working with two of my former colleagues from AQR, the company where I worked when I started the Pandas project, Adam Klein and Chang She. So they were working with me at that point.

And so we were working on Pandas and then I would flip between working on Pandas and writing the book. And then often I would come to empty sections in the book or stuff that I felt like should be in the book and I'm like, well, I guess I have to write that part of Pandas now so that I can write the section in the book to make the whole story complete.

So Pandas in 2011 was essentially, in 2012, was essentially book driven development, quite literally.

**CL:** Yep.

**Wes:** So sometimes projects are like documentation driven development.

**CL:** Or conference driven.

**Wes:** Conference driven development. But this was book driven development.

**Dori:** Well that's the agentic future right there, where you're writing books to help feed the LLMs what they need to build next.

**Wes:** Maybe. I guess the question is like, do the LLMs even need books? Maybe they can generate all of their own content and just reading our code bases and our test suites, they can generate their own. I think the problem is that the LLMs, their knowledge is a little bit too contaminated on all their training data about Pandas.

But you could imagine if you had a brand new project that you built entirely from scratch now and then you pointed LLMs at it and asked them to write a book about this new project, I'm sure they would oblige and write the book. What I don't know is whether the book would be any good. I've created a few new software projects with agents in the last four months and I haven't thought about asking them to write a book about them. But maybe I should. Why not? It seems like they probably would generate a bunch of slop, probably nothing that I could necessarily sell online. But it would be an interesting experiment to see how bad it is relative to an artistically created, human created book.

**CL:** Well, you've been also like collecting Spicy Takes, right? So let the authors of Spicy Takes write those books. Well, in their voices.

**Wes:** Yeah. Well, that's a funny thing because I had this problem where I love reading blogs and have for years probably for, I don't know. I started reading blog posts right when I got out of college. When I was working, we would send around blog posts about software engineering, data science, like the emerging field of data science, like legendary bloggers like Paul Graham, Joel Spolsky, things like that, Martin Fowler.

And so I used to love reading all those. And then now, of course, blogging has become almost like a full time job for some people. Like people are making enough off their Substacks to make a living. Like they're creating media companies just doing like YouTube content and Substacks.

And I had this problem where I would often read a blog post that I really liked and I would send it to a bunch of my data friends, like my engineer friends. And they almost invariably their response would be, "I don't have time to read a 2000 word Substack. Can you tell me what it's about?"

And so of course now with LLMs, I'm like, okay, well I can solve that problem of like, just give me the TLDR on this blog post. Like tell me what it's about. If the writer said anything like spicy or provocative or interesting, show me those five or six things. And that's how spicytakes.org was born, essentially, I think last month, basically.

So just one vibe coding session after another. And now I have a whole website with like 23 blogs and 31,000 spicy quotes from all those blogs. So it's a fun little side project. And of course, if anyone has any ideas for like blogs to contribute, I'm actually working on Joel Spolsky's blog right now.

Like today actually I started scraping and processing the Joel on Software blog, which is like, he has over a thousand posts. And so that's a lot of content to chug through, even with a very hungry Claude Max subscription. But I'll get through it eventually.

**Dori:** What are a couple of the takes you remember most that are top of mind?

**Wes:** Oh, gosh. Well, I have to go to spicytakes.org. There's even like an analytics dashboard, so you can, you know, you don't even have to dig. You can just say like, what's the spiciest stuff that Paul Graham said in like, I don't know, 2020. "Haters are just fanboys with the sign switched. If you believe there's nothing true that you can say, then anyone who gets in trouble for something they say must deserve it."

So you could just click around. It's fun. Yeah, it's totally not for any professional purpose. It's fun. And now, whenever somebody publishes-- I really like Benn Stancil's blog. Like he's founder of Mode, and I read his substack every week. And it's fun to read, but also, again, a lot of people don't have time to read Substacks.

And now like, whenever a new blog post comes out, I go to my terminal tab for Spicy Takes and I asked Claude to add the new Substack post to Ben's Spicy Take site. So anyway, just little things that I'm amusing myself with in this new world of agentic engineering. It's great.

**Dori:** Yeah. And for our listeners, we did an earlier episode with Benn Stancil, so feel free to check that out as well.

**Wes:** Oh, cool.

**CL:** Yeah, I feel this is such an amazing time to reimagine everything. You're literally like doing a RSS reader that is smarter. Right? And then you're building an email archiving thing. And then, we are supposed to talk about data first and then AI.

**Wes:** Well, these are all, in a sense, different kinds of data problems.

I feel like building tools to process and curate knowledge, it is a data problem. But not until now have we had the ability to do this much intelligent data processing and curation and at a cost that is tiny. Like I think basically spicytakes.org was all paid for out of my AI subscriptions. And so the maximum cost was essentially a few hundred dollars more or less. And so to be able to create something like that at such a small cost is frankly like pretty impressive. And so I think it is a big question right now, like, what do we do with this new power that we have?

Like every day I jump out of bed and it's like, you know, I was joking with friends, like there's like the meme of like He-Man with the sword. It's like, "By the power of Grayskull. I have the power."

And I wake up and every day, every morning I'm like, I have the power. Like what do I use the power for? I think data problems, like certainly I expect that we'll make a lot more progress on a lot of understanding of data systems and figuring out what to do next. I also am concerned that LLMs are just not good enough to do, like "build Arrow," for example. We built Arrow 10 years ago.

I think it's the type of problem that is difficult enough and nuanced enough that if you tried to throw LLMs like coding agents at building Apache Arrow from scratch, you would get a much worse product than the one that was like carefully, intricately designed by humans over a long period of time.

Like Arrow is a project that has the intricacy of like a fine Swiss watch. Like there's a lot of very small details that were created like very painstakingly over a long period of time.

Coding agents need time to deliberate and come up with ideas. And I think you would have to be willing to have the agents generate a hundred ideas and maybe you only pick one. And maybe in the future that's what software engineering will look like. Maybe you have the armies of agentic monkeys on keyboards, typing away, coming up with all these different ideas. And then you have some way of using other agents to judge all the ideas and figure out which ones are good. Like you know, try not to accept anything that's over complicated and whatnot.

**CL:** Or maybe not ideas but like pick the implementation that makes sense.

**Wes:** Yeah, I digress. But I'm more than happy to talk more about it. I've been vibing on agentic engineering and all the fun AI stuff that I'm doing these days. But yeah, I think my field is like I'm, you know, a data professional.

I've worked on data science tools and data system software for most of my career and in many ways, data engineering and data processing systems, database systems, are maybe one of the last frontiers of AI resistant technology. And so I think it's still an area where there's still a lot of work to do. Like we still need to build file formats and processing engines and metadata, scalable metadata management and all these things. And I'm less concerned about those things being vibe coded.

**Dori:** Yeah, well actually tell us a little bit more about that because I'll say we speak to a lot of people in the data field. I personally have a wide variety of friends in data and there's definitely this tension about our jobs being gone. You have people that are like one data person can do the job of five. You have the end to end data person. So tell me more about this optimism you have of there's a frontier left if people are wondering where should I be moving to.

**Wes:** I think that while the coding agents and the frontier LLMs have definitely made a lot of progress in Text to SQL, for example, they still struggle to generate correct SQL in complex real world schemas. So in contrived benchmarks they often perform well in text to SQL tasks.

But when you actually go to apply the foundation, frontier foundation models in enterprise resource planning systems and the actual real world database schemas that exist in large institutions that have been building and curating their database schemas over a long period of time, they begin to struggle because there's a lot of subtleties in the relationships between tables and essentially what's necessary to generate semantically correct SQL.

Like I was just at the CIDR Database conference and Michael Stonebraker, you know, one of the godfathers of modern database systems, gave a talk about exactly this, which is that he and some research collaborators developed a new, they call it the Beaver, like the Beaver benchmark for Text to SQL.

Basically it's a very, very difficult eval for text to SQL where they found that, you know, and I think it was this real world schema that's found inside MIT, basically the databases that power the Massachusetts Institute of Technology, like the institution and that the foundation models weren't able to generate correct SQL to do things in the schema that powers the organization.

And so I think that's an area where, I think semantic models are one thing that is important to do there. So I've, there's a number of semantic modeling languages that are being developed right now. There's companies doing semantic modeling. I've been really excited about Malloy, which is Lloyd Tab's like successor to LookML, which was the semantic modeling language that powered Looker, which is like the most successful BI product of the last generation.

And so Malloy is like a next generation version of that. And so there's companies like there's a company called Credible Data, where I'm an investor, full disclosure, that are working on essentially like headless business intelligence and like apply building a platform for people to create agentic data experiences but where the data modeling like semantic layer is managed by Malloy.

And I think that that's going to be really important to like reduce the complexity of the query generation problem. Otherwise like people are just going to be pointing Codex or Claude Code at their production databases and like blowing their feet off basically with a kind of agents generating.

Well the trouble is that a lot of people are going to be generating complex SQL queries and they aren't even going to read the queries. So they're going to look at the dashboard and they're going to be like, "seems okay."

But how do you verify if the SQL queries are correct, like if they execute? Okay, that's one thing. But, Benn Stancil wrote a blog post about this. He called it the Vibe and Verify revolution and how like analytics and data engineering is probably one of the areas that is at present time like most resistant to being fully vibe coded because there's too much subtleness in understanding how the database schemas work and like what are correct measures and correct, you know, how to write the queries correctly.

And maybe you could argue that we should be restructuring our database schemas to be better for agents and we'll probably do that too. But it's clear that like all the reinforcement learning in the world, all the pre and post training in the world has not been good enough yet.

And maybe it just means that OpenAI and Anthropic are going to have to staff a team to do reinforcement learning on this problem to get the quality of the model's output up to a level where they can perform at a 99% level and maybe right now it's like a 70 percent level. I haven't looked at the evals exactly to tell you where it is, but my sense is that it's like not in the 90th percentile. It's much worse than that now in the hard benchmarks.

**CL:** So what I'm hearing is that for an LLM to directly generate SQL, there's two problems, right? You have to generate very complex things that humans cannot comprehend. So you don't have a good way to tell if it's good or bad. And then it's almost like an intermediate abstraction or representation like Malloy will have something that's higher level that human can comprehend, that kind of sits in between human and machine, that you kind of become a communication tool, right? Is that what you're saying?

**Wes:** Right. Yeah. Because the idea is that things like Malloy or other, there's other semantic modeling languages or like frameworks, they serve to reduce the dimensionality of what the LLMs have to reason about. So they provide guardrails for like you have the semantic model which defines the table relationships because that's one of the hardest things is understanding the join relationships. Is it a one to one join? Is it a one to many? Is it a many to many join? And so that's one layer of complexity.

You know there's been a lot of over the years with you know, analytics and BI on the modern data stack, there's been a lot of work on having shared metric systems and be it like to have everyone in the organization like put all their metrics in one place and so that you aren't having like different teams computing different business KPIs in their own custom way which maybe is wrong or you know like is missing some subtlety of like counting wrong or like you know there's all these like details that's involved with like generating correct measures for dashboards.

**Dori:** Which very few companies actually succeed in doing, I feel like. Like it's done.

**Wes:** Right and it is a hard problem but like that that domain is also like littered with the dead and broken bodies of like many startups that have tried and failed to solve this problem. And like I think many of them end up looking like this should just be a feature of like a full stack BI platform and those. It turns out that the full stack BI platforms are the ones that have been been the most successful, like Looker being you know one of the flagship examples of that.

But I am not actually not an expert in this area. Like I, my work has always been a little bit BI adjacent. Like I used Tableau in the late 2000s before it was cool, circa 2007, 2008. It was really cool for me and I did a lot of cool stuff I think with Tableau but seeing some of the advanced business intelligence that people do now. The stuff I was doing was pretty derpy by comparison. But I definitely know more about, my area has been more data frame libraries, file formats.

Like I've done a lot of work on Parquet, had a heavy hand in designing Arrow and the protocol and like the libraries around Arrow and so a little bit more of like where the data meets the metal kind of thing. And so because initially like building Pandas, I didn't know anything about database systems or how to build a data processing engine. And so I think at that time, circa 2008, I was 23, like I had a math background but not a computer science or database systems background.

So I just, there was no way that I was going to be able to like come up with the idea of building a database engine basically. And I started giving talks like once I learned the mistakes that I'd made that Pandas wasn't built like a database, I started giving talks about like, "Pandas isn't designed like a database. It probably should have been, but I didn't know what I was doing whenever I started the project."

Of course the funny thing is like is it didn't need to like it. Pandas was, you know, primarily most people use it on small data and it would have been over engineered to build something like Polars. And so now like people legitimately need something like Polars to do large scale multicore data processing with an API that is, you know, data frame API.

But if I had taken three years longer to get something useful into the market to do things the right way, it would have been too late. So like people in 2010, 2011, people needed solutions right then. They needed to be able to read CSV files, they needed to be able to do basic data wrangling if the data fit into memory. If you know, you couldn't handle many gigabytes of data, like it was fine because most people just had Excel spreadsheets and CSV files that weren't that big.

And so the fact that it was inefficient or didn't scale, it didn't matter because it solved the problems that people had and it was fast enough and it had the features that they needed to be able to get their work done.

**Dori:** Yeah, a good founding lesson.

**Wes:** Yeah, indeed. Yeah, I guess a good lesson to like, don't over engineer. Like if you can get something to market faster that solves a problem that's worth a lot. And often I think founders and system builders are frustrated when like not the best solutions are the ones that are the most popular, the most financially successful and like the only thing that I made money from, from Pandas was book royalties, which are like, you know, just a drop in the bucket compared to the money that people make from successful startups.

But you know, I didn't build Pandas to make money. It was about making Python into a data language that people could adopt and begin to trust in a business setting. And in 2008 Python was not a mainstream language for business data work. It was considered kind of a niche scripting language basically. And it had a small scientific computing community, but it was not considered a safe language to adopt for mission critical work, if that makes sense.

**Dori:** Yeah. So what made you decide to believe so deeply in like that Pandas needed to exist then?

**Wes:** Well, I think fundamentally it was about the human ergonomics of the Python programming language. The language itself, its readability, conciseness, like the fact that there's very little-- There was no types in those days. And actually like I embrace and appreciate typing in Python, but I also I feel like if Python had had typing 20 years ago, it would have been worse because it would have hampered the ergonomics of the language.

Like, part of the beauty of why people really enjoyed Python was that they could express complex ideas and manipulate data in an interpreted language. You could express complex ideas very concisely. Things that might take you 100 lines of Java or C++ code you could do in three or four lines of Python. And so I think initially that benefited people doing scripting, like basically little automations and glue code and doing things that you could do in Perl but with like code that was much nicer to look at and read.

**Dori:** Yeah.

**Wes:** And so the fact that Python was designed as a teaching language it was designed for readability and like ease of writing and ease of reading as well. And so when I started building kind of a little personal data toolkit, I also was using IPython. So there was no Jupyter, it was just the IPython terminal experience before it was even Jupyter.

And so I felt like we have solid bones here. We had NumPy, SciPy, Matplotlib, we had the Python interpreter, Python language, really nice to program in. We had IPython and all that was missing was a data toolkit that could read CSV files, that can read data out of databases, that can assist with like doing stuff that you might do in SQL or you might do with like Unix tools, you know, awk, sed and grep basically, but essentially give you a nice API that would provide what you could do in, you know, you could do an R with data frames.

**Dori:** Yep.

**Wes:** And so it was a definitely just a bet that this was something that people would want and that people would adopt and be happy with. But it was something that I needed for the work that I was doing. And I found that I really enjoyed programming in Python. And so initially it was just a personal data toolkit, but it was really, it was working with other users, like introducing them to Python, people who'd never programmed in Python before, looking at the way that they worked now, especially looking at people who are heavy Excel users.

And then I would show them what it could look like if they were using a programming language to script and automate the stuff that they were doing in Excel, but using early versions of Pandas, so writing Python scripts and running them in IPython, interacting with the data frames. And I found that people really liked it. And so I got pretty quickly got into this feedback loop with users, where I started to see people become really empowered by the combination of Python and Pandas.

And so that was what gave me the belief that, like, there's something here. If this can just become more feature complete, more functionally complete, like serve a broader set of users, make it really well documented, like have a book about it, then it could become really, you know, really big and successful.

But again, like, these were just gut feelings, like, I had no real evidence to support it. It was purely like, you know, just felt like the right thing to do.

**Dori:** I mean, if you're getting people to turn off Excel and learn another language, I mean, that's a pretty strong sign, especially in finance.

**Wes:** Yeah, in finance, yes. But people have a lot of Excel experience. You know, I've seen people that have, like, all the Excel keyboard shortcuts memorized. And so there, you watch them running an Excel spreadsheet, they're like. It's like they're playing an organ, basically. Really impressive. I've seen some really impressive Excel users in my life.

But it's very manual. And any type of automation would end up getting built in Visual Basic, which is like a whole special kind of hell. So I think, like, just, just getting to that breakthrough, aha moment of, like, look at what the Excel workflow looks like, especially when you would want to, like, automate a bunch of, like, similar types of analyses.

And people would, like, manually set up different Excel spreadsheets that would replicate. They would, like, copy this, the sheet and like, tweak it a little bit and that would be the way that they iterate. And so I'm like, well you just get out of the spreadsheet and everything is just Python code and you can mold it and make it reproducible and you can have it generate Excel spreadsheets for you and it, you know, you could even do that in those days.

And so I think getting to that aha moment of like, oh, just recognizing that there's an ability to automate this work that, that was very manual or like tedious in Excel in the past, like that was, I think what was necessary to get people to like cross the chasm, you know, so to speak.

**CL:** Yeah, I think there's nothing more satisfying than like what you're describing, like the early kind of a new open source, finding this user, interacting with them and actually like, wow, this is something I wasn't sure about. But people love it, right?

**Wes:** Yeah, for sure, for sure.

**Dori:** How do you think your experiences building Pandas and Arrow have informed now that you're on the other side of the table, so to speak, as a VC?

**Wes:** As an investor?

**Dori:** Investor, yeah, sorry.

**Wes:** I hesitate to call myself a VC. I do have a small fund, but it's essentially, it's Composed Ventures. It's an outgrowth of the angel investing that I was doing. So I still view it as angel investing but like angel investing with slightly larger checks and investing my own money as well as other people's money.

So I'm not aspiring to become a full time investor, but I think when I talk to companies about investing it's often very relationship based. The investments that have been most rewarding to me, where I've been able to help the most, have been ones where I have some connection to either the underlying technology or I know the founders. I've been investing in a lot of companies that use Arrow, for example. So one of the reasons for setting up Compose was I wanted to explain to the world that I have this investment thesis around Arrow, companies that are all in on using Arrow, using data fusion, basically adopting and leveraging the Arrow ecosystem of technologies.

And so I think the majority of the companies that I've invested in the last three or four years have been companies that are using Arrow in some capacity. Of course you could argue that we're getting to a point where there's fewer companies that aren't using Arrow than are using Arrow. Many people are using Arrow without even realizing it.

**Dori:** Yeah.

**Wes:** Which is I think a good place to be. But generally like what I'm looking for in when talking to founders, and especially if I'm introduced to a company that I've never met before, founders I don't know, maybe a new technology, is that sort of looking for alignment between people's background and experience and the problem that they're solving. Like, is there a reason why you are the right people to solve this problem?

Do you have the right background? Do you have the fundamental motivation why you should solve this problem? And so typically I'm looking to see that articulation of what is it that got you fired up to solve this problem? And sometimes with startups, sometimes the answer is that they feel like it's a way to build a successful company and make money, which is completely valid. But many, many companies do have like this deep down desire to solve a problem that they experienced in the past.

And so I think the running joke is like the next companies that people found are to solve the problems that they experienced, like, you know, unrelated problems from like the last company that they worked on. Like a famous example is that the founders of ksplice, which was a Linux kernel hot live update, they went on to found Zulip, a chat company and Pilot, a bookkeeping company.

**CL:** They experienced that.

**Wes:** Yeah, it's like we weren't happy with the state of bookkeeping and we weren't happy with the state of workplace communications. And so now the founders of ksplice are now doing, you know well they did Zulip, which got acquired by Dropbox, and then now Tim Abbott and some others are doing Zulip as a standalone company and Jessica McKellar and others are doing Pilot.

But you know, these are examples of where, you know, having firsthand experience with the problem that's being solved is, is definitely very helpful. Obviously you have to go out and like, do easier interviews and understand like, is it just you that has this problem or do other people have the problem too?

And then of course, you have to try to quantify like how many people have that problem and what's their willingness to pay for a solution. Like maybe they're willing to pay for a solution, but they don't want to be locked in on a vendor. And so it's gotten even more complex.

And of course now with AI, I feel like the table has been completely flipped where the bar for adopting a third party software vendor is that much higher. Because now not only is it like, am I comfortable buying software from this vendor and being dependent on them. But there's also the calculus of can I just have somebody on my engineering team spend three weeks with Claude Code and build a replacement?

And people are doing that anecdotally. Not at maybe it's quite the scale that's being claimed in the tech media, but it's to a certain extent that is happening.

**Dori:** Oh yeah, I'm doing that personally right now about building out a couple different side projects where yeah, there's tools. Like one of them is I want basically like an LLM document editor, but where I can like at different models and like have conversations and all of this stuff. And CL shared with me, I forget the name of a company that had built something similar, but it wasn't exactly what I wanted. But I'm like me and Claude, we can get exactly what I want and it's just for me.

**CL:** Yeah, personal software.

**Wes:** Right now you can have exactly what you want. You no longer have to make compromises and not have the thing that you want. And I think that's frankly kind of wonderful. But also, I mean think of it this way, it also creates in a sense like I'm planning to write a blog post about this at some point. I've been kicking around this idea in my head is that I think that AI in a way is going to create this wave of what I would describe as radical accountability for creators of software projects where you do not have to accept things being mediocre, things being bad anymore.

Like it is much easier now to reject a solution that is mediocre. And you know, if I interact with somebody that's building a software project, I'm not even gentle about giving the feedback. I'm like, this is bad. Like why haven't you fixed this yet? Like if I was on your engineering team I would have already fixed this. I would have done it like today with Claude Code. Why have you not fixed it yet?

And I think a lot of software vendors as a result are being caught flat footed by their newly empowered customers who are essentially no longer going to put up with their mediocrity. And so I do think that this new radical accountability is going to be a good thing for the software industry because basically any software vendors that continue to ship mediocre software, they're going to lose all their business. People are going to say like what? Like, you know, it used to be the excuse was we can't afford the engineering time to do it the right way. And now the only excuse is that like you don't know what the right thing to do is or you have bad taste. Usually it's like some combination of both. Like, oh, we don't have good ideas or we don't have good taste. Like it's one of the two. Maybe, maybe both.

And you know, personally, like I'm happy to just let all those companies go extinct. Like just out with you. Seriously. No, like I that's again, radical accountability. I'm like, you don't know what's the right thing to do. Like you can't be bothered to sit down and do it the right way to make it better, like in Benn Stancil's words, like, you know, basically out with the garbage.

And I think a lot of these kind of old and crusty kind of incumbent systems that have just stayed bad for so long. Like think of like every expense management system I've ever used. Like, why are they so bad? Like even Expensify. Like I hate to like criticize a tool that I pay for and that I think is like the least bad expense management tool. Like it still doesn't have keyboard navigation. Like why?

Even now, today, like they built some kind of like you know, AI native, you know, new Expensify. And I logged into it and it was terrible. And so I went through their support system and I was like, please, please, like just give me the classic like not AI native Expensify. Because like whatever you have done here is totally awful.

But I think like basically people are going to look at all these tools that they paid for and maybe like, you know, Expensify is maybe not the best example, but if you had a team of people, maybe you have a 30 person company, you might be paying $300 a month for Expensify. Pretty sure you could probably have somebody vibe code a better solution, you know, and maybe one person with a $200 Claude Max plan, like maybe you could vibe code your way out of that problem, maybe with some security holes and bugs and things like that.

But anyway, I'm very excited about where it. I think somebody described what's happening right now as like a great wildfire. Like the world is full of dead wood and dead trees and stuff that basically just needs to be burned to the ground. And so I think that 2026 is going to be about swatching kind of the software industry, like take a look at everything that is bad, everything that is mediocre, and burning it all to the ground and let a thousand new trees grow fresh probably a lot faster than they would have in the past because people can build new solutions a lot more quickly.

But anyway, so that's kind of my soapbox, like, kind of where I think where things are headed. But now, my patience has run out. When I interact with a bad software product, like a bad SaaS product, I'm just like, why? Like, you know, there's no excuse for this anymore. Like radical accountability. I'm just like, burn it, burn it down.

Like, I want better expense management tools. I want email that doesn't suck. Like, why is it so hard to find stuff in Gmail? Like, I don't know. Apparently Gemini has some new like, AI inbox. Like, I looked at it, it doesn't look like what I want, so I don't want that. I just say, yeah, just radical accountability. Let's burn it down. Let's make things good. We can make it good. I believe we can.

**CL:** I look forward to reading that on the Spicy Takes.

**Dori:** Yeah, well, I have two follow ups. So one, since the bar is higher, how do you see that impacting startups? As somebody who is an ex-founder and has a bunch of people that are still living the journey, may they continue, and then just the bar is higher to get to that MVP, I assume. What does that mean for the earliest stage of like, us trying to get going?

**Wes:** Yeah, well, I mean, certainly at the earliest stage of a company, if you come to a pitch and you have nothing to demo, that's almost a red flag at this point. It's like, what, you didn't build a prototype? Like you know, it used to be you could justify not building a prototype because it takes time and you want to get the money raised and everything. But now it's like, you know, show me something that moves.

**Dori:** Yep.

**Wes:** But when companies actually get into building, I think it's difficult for us to extrapolate from where we are, where we stand right now to imagine what things are going to be like in 12 months after everyone has had a chance to run teams of people running 5 parallel Claude Code sessions for a year and see what they produce. I mean, maybe some people will have agent psychosis and will not produce anything of value.

So I think there's going to be a lot of slop and stuff that only makes sense to them and doesn't make sense to anyone else when you go to demo the software like hyper personalized software that just doesn't have good taste.

But I do believe that it is going to be harder and harder to achieve differentiation amid the sea of new project slop. And so basically like, I mean I think even open source, like the role and value of open source in this new world is even debatable because collaboration in the open source world has gotten much harder. The AI generated contributions have created a lot of burden for open source maintainers and so a lot of people are like, I mean Mitchell Hashimoto just this week put out his vouch project to create a system of like credibility amongst open source contributors because of all the overwhelming slop PRs that are coming into Ghostty.

I mean the same problem is going to happen with, with startups where basically people are going to decide like which companies to pay attention to on the basis of how credible the people are involved. And so if you see people you're going to be looking at less, less of like the software they created, you're going to be looking at more at the people involved and asking yourself like, is this somebody that I trust? Is this a person with good taste? Do they have a track record of building solutions that work and building software consistently over a long period of time that, that works?

And I've been building some new stuff with agents but I'm being very heavy handed in how I manage the agents and I keep them on track and make sure that they build the right thing. When I go into work on a project with agents I have a very clear picture in my head of what the software needs to do. And yes, I'm not reading all of the code so you could argue that there's probably some slop hidden in my my agents PRs.

But I'm asking a lot of hard questions about like the testing strategy and like I'm proactively refactoring the tests and doing test driven development and being really rigorous with how I manage the agents. And so I think when people look at a piece of software that I created and like I've released a couple of new open source projects in the last month MSGVault and roborev. So an email archive and search system and roborev is a continuous code review system for agents.

So when people see those projects they say oh Wes built these like they're probably not slop. And they aren't slop because I've put a lot of work into making sure that they aren't slop. And so I think that's going to be like the bar because people aren't going to be able to look at the product and judge just purely based on the website and the feature list and the documentation whether the product is good or not. It's going to be based on like, are the people involved credible?

And even how to like determine that credibility is kind of a fraught question and I'm not quite sure what the solution to that is.

**Dori:** Yeah, the second part, because that's a lot to chew on, the second question I had from going back before that and it still ties in I think here on the credibility, there's been a lot of consolidation in the data market.

**Wes:** Right.

**Dori:** You know, and in one part you're talking about all this credibility, you know, for the young startup founders getting going, you know, or young at heart. They're now competing also not just with the big boys who have that credibility baked in, but are also soaking up so many of these other little startups. And you're like, oh, it's a wildfire. We had like a thousand trees. But that seems, you know, like Fivetran's acquisitions, you know.

**Wes:** Sure, yeah. I mean now like, yeah, Fivetran and Databricks are two of the biggest, the biggest fishes of them all. Databricks has acquired a ton of companies. Fivetran has acquired a bunch of companies. Once upon a time we had Census, Fivetran, dbt and Tobiko Data based, Tobiko Data SQL Mesh, duking it out in the market. Now they're all the same company, so that's already significant consolidation. And I'm sure that Fivetran has made other acquisitions that I'm not aware of.

You know, I'm a holder apparently now of Fivetran stock as the result of like all the mergers and acquisitions that have taken place. Like I have a bunch of stock and Databricks also as a result of, you know, mergers and acquisitions activity. But I think that the consolidation is healthy in the sense that the modern data stack, so to speak and like the modern data stack landscape had got so large and fragmented and confusing that it was creating a weariness amongst the buyer class.

And people that just need to build their data platforms to get things done were kind of just eyes glazing over looking at like, oh, we need to choose one of the 40 products available for solving every problem in our data stack. And Matt Turk is one of the investors that famously created these comprehensive landscapes diagrams of like where you need a microscope to like look up. It's this gigantic, you know, 100 megabyte PDF and you need a microscope to look up the logos and see all the different companies and projects that are in all the quadrants of the modern data stack.

So I think that the consolidation is really healthy. And you know, I think there were a lot of companies that there was speculation that there was going to be like a mass extinction event for startups, especially after the zero interest rate period ended. And so that was like, I think back in 2023, 2024, that was what I was seeing in the tech media and in venture circles was like, when's the startup mass extinction going to take place?

And what happened is that the companies that would have died in the past all pivoted to become AI companies. And so that gave them like a new second wind. But like we have the same problem in that there's like, for any given problem, you know, think about any given application of AI, there's now dozens or hundreds of companies pursuing some kind of solution for that problem and then living basically in existential fear that like any given week Anthropic is going to release an upgrade to Claude Desktop that kills their product.

And there were like already tons of companies that were wiped out by or were forced to pivot by ChatGPT or you know, basically just the innovation that has come, you know, rapidly in the foundation models. So at the same time like I'm really optimistic about there being lots of like mighty small companies, like companies that have outsized impact and influence with really small teams and not just in the sense of like, you know, fastest 100 million ARR.

There's like seemingly a competition right now about like who can go from 0 to 100 million ARR faster. And I feel like every week there's like a new record being set, like the fastest time to 100 million ARR. But it's like, how sticky is that revenue?

Like is Cursor going to be around in two years? I wouldn't bet on it, which is to say, I'm not confident in a lot of these companies, like it's not an equilibrium and it feels very unstable and the future is hard to predict. Certainly a lot of the value will accumulate to the providers of the foundation models now of course, whether what they're doing is even sustainable and whether CoreWeave will still be around or whether OpenAI will still be around in five years. You know, I think there's like a financial bubble around AI that could also burst and have significant collateral damage. And so as a result, like, you know, I'm very bullish on Anthropic, maybe like less bullish on OpenAI. I use all their products, I pay for their subscriptions, but almost certainly, like I'm a token whale.

Like I consume extraordinary amounts of tokens and I am costing these AI companies a lot of money. And so at some point they're going to have to charge me the true cost of the tokens and maybe they'll get the token economics such that like they can like my use of Claude Max or my use of ChatGPT Pro, the 200 a month plans. I use Codex enough. Like just my code review volume is enough to exhaust my $200 a month Codex plan.

And so maybe they'll get the token economics to a point where like they're making money off me at $200 a month. Like tokens have gotten really cheap but still like based on CC usage, you know, I'm burning $6,000 a month in tokens on $400 in subscriptions. And so I just don't, you know, it's unclear like how long that's going to be sustainable. Maybe they're sustainable. Maybe there's like a bunch of people who are not burning that many tokens and so it averages out.

But I just don't know. Every day feels wild and uncertain and it's hard not to feel like you're riding a wave and wondering how long is the wave going to last? Maybe the wave is a tsunami. What happens like at the end of the wave? Are we going to crash into something? Anyway, we're living in a very stimulating time. I find it very interesting what's going on and we're all having a lot of fun right now. It's unclear that the fun is going to last forever, but I hope that it stays fun as long as possible. Let's put it that way.

**Dori:** Yeah, I definitely feel like I've been able to be a lot more creative. Right? Like I would not have been building my own document editor ever, you know, without Claude.

**Wes:** 100%. Yeah. I'm all for, you know, everybody realizing all their small and large ambitions and building all the things that they always dreamed of and never could justify taking the time to do. And you can build the project of your dreams, you know, during and in between meetings that you're on. Like imagine all those Zoom calls that you've been on where you've never said you've maybe spoken for 60 seconds out of an hour.

And I'm not saying that I've ever vibe coded on a Zoom call, but you can turn unproductive times into productive times now. You can work on projects in parallel while you're waiting on Claude to finish something, you can nudge along, you know, a pet project, a side project, and you know, maybe it's something that makes your day to day life 1% better, but that 1%, like it feels good and like the cost of building the thing that makes your life a little bit better.

Like I was frustrated about using personal finance products, and so I was like I'm just going to build a thing that makes managing my personal finances and categorizing my business expenses like a little bit less horrible. Now like I have a project called Money Flow and like now I exclusively manage my personal finance through a terminal UI that I built in October. And I never have to click around a website like mint.com.

I've used all the personal finance products and I think Monarch is probably the best one so far. But I don't like clicking and it's built for a different kind of user than me. Like I want something that I can script and automate and that I can use with AI. And so that's why I'm like, I could just build the thing that does exactly what I want and makes me productive in the way that I want to be productive.

And so I'm encouraging everybody to just go ahead and build stuff. There's nothing stopping you.

**CL:** Yeah, one other question before we hit our lightning round. So we talk a lot about all this ecosystem, the current AI, but what do you think, maybe not five years, but in three years, what's going to be laughably outdated about how we deal with maybe data or anything today?

**Wes:** Well, I think there's different schools of thought on whether IDEs as a class of software are going away or not. I don't think they're going away, but they're definitely going to be disused. And I actually feel somewhat better about my laziness and that I didn't adopt an IDE until the last two years when I started working on an IDE project, Positron, which is a fork of VS Code.

And it's very difficult to work on VS Code itself or a fork of VS Code without the help of VS Code because they've been kind of built, it's been sort of built to be able to develop itself. And so like developing VS Code from the terminal sounds like kind of one of the most miserable things imaginable.

And seeing like the stuff that we built in Positron, like Data Explorer and different things, you know, I think there's, it's clear that for certain types of use, like data science is one example that I think an IDE still has tremendous value. But basically a lot of IDE use in the past was to give you autocomplete and like refactoring and like code based search, like jump to definition, stuff like that.

And that was the stuff where I was just never compelled to like use a Python IDE because you know, I didn't even have LSP like tab complete. Like I just used Emacs and you know, I just knew what file to open. I don't know, I was kind of a, kind of a caveman using Emacs. But I feel like now, now if you look at the vibes on the Internet, like people are just using their Claude Code and a text editor is the way that they're working. So I think that trend will continue.

I don't see like a pendulum swinging the other way towards more visual environments. I think we might see like more visual like canvases for managing and monitoring supervising agents. And so that's maybe something different.

I don't know, maybe even the terminal UI coding agents, like maybe we will have moved past that. Like we adopted them very quickly. Like maybe if there's something better that's created, like maybe we'll be just as eager to give them up. It's hard, really hard to say.

**CL:** Yeah, okay, cool. So this is such a fun conversation. Before we wrap we're going to put you in the data debug run: quickfire questions, short answers. Are you ready?

**Wes:** Sure.

**CL:** So first programming language you loved or hated?

**Wes:** Java. I hate it.

**CL:** Okay, what is your go to data set for testing any data related stuff?

**Wes:** These days, I guess it's pretty boring. Like the New York Taxi data set.

**CL:** Okay. NYC taxi. Classic.

**Wes:** Yeah.

**CL:** What's one lesson outside of tech that influences how you build?

**Wes:** I think authors that I really like, like Kurt Vonnegut. And so I feel like there's sort of an insightful, kind of humanist, empathetic aspect of his writing that I've always enjoyed, as well as his not too serious perspective on things, especially some of the later Vonnegut writings. And so I think it's reminded me to be very empathetic towards all of the humans involved in the software process, while also not taking it too seriously and trying to have fun because life is a little bit weird. And often people do take it too seriously.

**CL:** Yeah, that's great.

**Dori:** Okay, you've already mentioned Kurt Vonnegut, but what's another podcast or book that's not about data that you enjoy?

**Wes:** I like Ursula Le Guin's science fiction novels, so Left Hand of Darkness, books like that. I also really enjoy her kind of reinterpretation of the Tao Te Ching. Her kind of poetic reinterpretation of that I really, I really enjoy.

**Dori:** Yep.

**CL:** We have that book at home.

**Dori:** Final question. Tabs or spaces?

**Wes:** Well, spaces, I guess. But since I'm not writing any code anymore, I'm writing a lot of code in Go, and the agents are using tabs for everything. So I guess maybe I'm a tabs person now, but I'm not sure that I really care anymore. I can set the tab to two spaces or to four spaces, whatever I like.

**Dori:** Whatever the agents want.

**Wes:** Wow. Thank you so much, Wes. Before we end, where can listeners find you and what do you encourage people to do?

**Wes:** Well I have a website, wesmckinney.com where you can follow my blog ramblings, as well as my podcast appearances and conference talks, which now have transcriptions and AI summaries along with spicy takes.

You can go to spicytakes.org and enjoy that. And of course, I'm putting out new software almost every day on GitHub. And so I'm sure that the recent projects MSGVault and Roborev, won't be the last new projects that I create this year. So I'm excited to see what what's in store.

**Dori:** Yeah.

**CL:** Wow, Amazing. Thank you so much.

**Dori:** Thanks, Wes.

**Wes:** Thank you.