---
title: "Your VP Is Doing a Rogue Analysis in Cursor Right Now — with Nell Thomas"
summary: "Podcast at The Test Set (Posit)"
date: 2026-03-26T00:00:00
tags: ["podcast", "transcript"]
slug: test-set-nell-thomas
word_count: 12501
source_file: transcripts/2026-03-26-test-set-nell-thomas.md
content_type: transcript
event: "The Test Set (Posit)"
video_url: "https://www.youtube.com/watch?v=wxHz9nTFIY8"
---

{{< video https://www.youtube.com/watch?v=wxHz9nTFIY8 >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this episode of The Test Set, Michael Chow and I sit down with Nell Thomas, VP of Data at Shopify, in Times Square. Nell leads a team of over 400 people spanning data infrastructure, data engineering, data science, and analytics.

Nell walks through her career path from cognitive neuroscience and psychology through equity research, Etsy, Facebook, the DNC (where she was CTO), Hillary for America, and now Shopify. Her entry into data work was unplanned — she moved to New York after college, and her stats skills from running psychology experiments landed her a research analyst job doing large-scale data analysis to predict stock movements. SQL was her first data tool; Python came much later.

We lay out the modern data stack role by role: production engineers generating instrumentation, data infrastructure engineers handling ingestion and processing, analytics engineers modeling data for downstream use (typically in tools like BigQuery with dbt and Airflow), and then data scientists and analysts consuming it. Nell draws a distinction between batch analytics work (where 8-24 hour data freshness is acceptable) and production/operational use cases (like bot detection or real-time recommendations) that require low-latency data processing. Her key point is that the further left you go on that spectrum, the more unified the infrastructure should be — forking too early leads to duplicated data, wasted costs, and lost context.

On AI and agents, Nell describes how Shopify CEO Toby Lütke's internal memo mandating AI adoption as a baseline expectation removed a lot of the noise around whether to adopt AI. Her team built an MCP for their data warehouse by February 2025, months ahead of most companies. She notes that agents can put stress on data platforms in ways that resemble DDoS attacks — replacing the natural rate-limiting of human query patterns with automated loops. She's seeing non-data-scientists (including fellow VPs) doing "rogue analyses" in Cursor and sharing screenshots, which raises questions about data source trust and query correctness.

Nell calls the semantic layer her "greatest failure as a leader" — competing needs across her team (executive insights vs. product-embedded teams), debates over homegrown vs. third-party tooling (dbt-based vs. Looker/LookML vs. internal solutions), and technical limitations with BigQuery made it difficult to converge on a single approach. She's re-interrogating those choices now.

On the broader question of navigating uncertainty, Nell draws on her background in history of science and technology: new technologies are typically co-evolved by their creators, users, and regulators, and the "founder myth" of a single inventor who knew exactly how the tool should be used rarely matches reality. She sees AI as fitting that pattern — a deeply collaborative moment with no single right answer yet.

## Key Quotes

> "I love one of my fellow VPs at the company, but he loves to do a rogue analysis and send me a screenshot and be like, 'I found the number.' And my first question is always, what data sources are you using?" -- Nell Thomas

> "In organizations where people aren't actually paying attention to the data work, it's very hard for it to be amazing." -- Nell Thomas

> "I would say semantic layer decisions have been my greatest failure as a leader." -- Nell Thomas

> "If you can get the right culture and the right people, you can make a lot of mistakes and it's going to be okay because you can switch them out." -- Nell Thomas

> "The simple narrative of the emergence of technologies is usually the founder myth — this one person invented X and they knew exactly how it should be used. But in many, many cases, the technologies get fundamentally altered by the people who use them." -- Nell Thomas

> "Demystifying the idea that there is a right way to do anything right now is important because no one knows. The next Claude model is around the corner." -- Nell Thomas

> "People often ask me, what advice would you give to someone earlier in their data career? And I'm like, watch the movie Sneakers." -- Nell Thomas

## Transcript

*[Podcast intro]*

Welcome to The Test Set. Here we talk with some of the brightest thinkers and tinkerers in statistical analysis, scientific computing, and machine learning, digging into what makes them tick, plus the insights, experiments, and OMG moments that shape the field. On this episode we sit down with Nell Thomas, who has led data teams at Etsy, Facebook, and the Democratic National Committee. And now she's VP of Data at Shopify, which has mandated that AI usage is a baseline expectation for every employee. She leads a team of over 400, and she'll be the first to tell you nobody knows the right way to do any of this yet with AI. We talk about the modern data stack, building trust in data organizations, and why the smartest move right now might be resisting the urge to lock anything in with AI, but embracing exploration and discovery. We also, as a bonus, talk a little bit about the movie Sneakers.

**Michael Chow:** All right, Nell, welcome on to The Test Set. So I should say, you're Nell Thomas, and Vice President of Data at Shopify. But I also have to admit, I'm totally enchanted by your career record choices.

**Nell Thomas:** It sounds so official when you say Vice President. I'm so sorry. I didn't know. It's like when you meet a dignitary.

**Michael Chow:** Yeah. So I just get on one knee. And before that, you were CTO of the DNC, Democratic National Convention.

**Nell Thomas:** Committee.

**Michael Chow:** Committee. I'm so sorry.

**Nell Thomas:** No worries. We got this. We're good. We're good.

**Michael Chow:** And before that, you were at Facebook.

**Nell Thomas:** Yep. Yeah. Before it was Meta.

**Michael Chow:** Nice. Before it was cool.

**Nell Thomas:** Exactly. Or when it was cool. I don't know. Was it ever cool? One of those. We'll figure it out.

**Michael Chow:** And then Hillary for America. And Etsy. So I know it's a long...

**Nell Thomas:** I know. And there's like even, you know, time for that. It's nice to be saying I've had a long career. Lots of interesting choices. So I'm excited to talk about them. I'm excited to be here with you guys.

**Wes McKinney:** Yeah. Thanks for coming on.

**Michael Chow:** That's all to say I'm enchanted by your weaving between sort of like political impact and industry work. So maybe just by way of introduction, I'm Michael Chow and joined by my co-host, Wes McKinney, principal architect at Posit. And we're in Times Square. So there's a very large glowing billboard just rocking behind us.

**Nell Thomas:** It's a little complicated for you to get distracted. It means I have to up my game so that I can compete with the Times Square billboard.

**Michael Chow:** Yeah. You're competing with some kind of ad for something. But thanks for coming out. I'm so excited to talk a little bit about your career and this really interesting path that you've woven. And also about your work as a leader of a data team and a data group. And I think in 2026, that often involves the emergence of AI and what that looks like for folks. But maybe to start, maybe you could just tell us a little bit about yourself.

**Nell Thomas:** Yeah. And yeah, I'm very excited to be chatting with you both. So thanks for having me on. I've been working in data now for two decades, which is a crazy amount of time. And I probably could start the conversation at any point of that journey. But let's say to start at the most important thing, I love working with data. It's always been something that's motivated me. I love finding interesting, hard problems. And I think I've been very lucky to have this opportunity to sort of haphazardly make my way through a series of different choices.

But before we get to the career stuff, I'm also human. I live in New York. I'm a mom of two little girls, which is an important part of my story right now because they are relatively young and take up a huge amount of energy and time, which is exciting and awesome, but also real.

And at Shopify, I run a team right now, it's a little bit over 400. It's data infrastructure, data engineering, data science, some analytics in there. And it's a really fascinating place to be working, especially, you know, I joined three years ago and really been following the arc of the advent of LLMs and AI and how that is rapidly evolving and thinking about how I run and manage a large team. So, yeah, happy to go back on the career in more detail.

**Wes McKinney:** Well, I think what's interesting is that you've been working as a data leader over essentially many eras of big companies figuring out how to do analytics and data science in a way that's sustainable and scalable with good best practices and an engineering mindset. I remember when I first got involved in the data ecosystem in the early 2010s, that's when people were starting to talk about big data. We heard about large data orgs and data problems at companies like Google and Yahoo and Facebook. But then all the rest of the companies in the world were like, OK, we need data teams too. How does that work? What software should we be using? Who should we be hiring? What is a data scientist? What does it mean to do analytics and to build analytics teams?

So I think you've had a front row seat to doing that inside both really interesting e-commerce businesses as well as tech and politics. And so I think you have a pretty interesting perspective on how that understanding of how to build an effective data organization has evolved. And I'm sure, with each passing year, especially now, it's changing rapidly.

**Nell Thomas:** It is funny because it's a weird combination of things changing rapidly and still the same problems at the heart of things, right? Like the quality of your data is always the number one problem. And now maybe more so than ever. But yeah, it is this interesting two different lanes of things. Some things are just consistent backbone of core issues while we're seeing the tooling and the skills rapidly move.

When I graduated college in 2005, before the word data science was even officially coined as a thing, I'll just take a very brief note here. I graduated with a degree in cognitive neuroscience and psychology, and I worked in psychology labs running experiments on humans. And that involves obviously learning a lot of stats and doing a lot of work with and analyzing the data that comes from those experiments.

When I graduated from college, all I wanted to do was move to New York City. And so I took basically the first job that hired me and the thing I had that was marketable was my stats skills. And so I took a job in equity research in finance where I was doing large-scale data analysis to predict the movement of stocks, basically.

**Michael Chow:** And what was the job called? What were they called?

**Nell Thomas:** Yeah, it was called a research analyst.

**Michael Chow:** Nice. Yeah.

**Nell Thomas:** But, you know, as an undergrad, I used SPSS and Stata. And basically when I started at this job, they handed me a book on — this is how old it was — the book, like, SQL for the Workplace. And that was my first job, was learning SQL. Python came much later in my life. But it was very much on-the-job learning. This is what it means to extract value from large datasets and make it meaningful for some outcome. And that was way before — in essence, is a lot of still what happens and what the goal is — but way before we had some of the terminology we have now. And right before big data kind of became this craze and you had this emergence of the crazy data industry that propped up within four or five years. But it set the ball rolling in this sort of unexpected way where I actually found something that I loved to do unexpectedly. And it took me a few curves to get to the rest of the journey, but I never would have anticipated it when I was an undergrad.

**Michael Chow:** So not to try to go too deep into it, but I'm really curious about when you did social psychology and neuroscience. Were you planning on becoming a research analyst?

**Nell Thomas:** Absolutely not. I mean, I studied those topics undergrad because they were just really interesting to me. I think in my head, I always assumed I would go back to grad school. And so I was like, out of college, I just want to get a job and be out in the real world and live in New York. And I wasn't too fixated on the topic as much as I was just getting out and experiencing working. And so it wasn't premeditated, I'll say that. But what's funny is the through line now in retrospect is I've always been really interested in human behavior, understanding it, using data to understand it, which is honestly at the core of a lot of psychological experimentation work.

**Michael Chow:** I mean, I imagine running a 400-person team is maybe very psychological in a lot of ways.

**Nell Thomas:** A hundred percent. I mean, management and leadership is obviously a lot of dealing with humans, at least right now. There's a lot of understanding how to help people do their best work. Now, I think a lot about my job right now is creating scale and leverage. So how do I create systems that enable people to do phenomenal work? And that means making sure that no one is limited in what they can get done, but that we're also holding a really strong quality bar for everyone at the same time.

It's actually a little bit, when you think about it from a data perspective, like law of large numbers. How do you make sure that you keep raising the standards while not putting caps on that would reduce quality for anyone? A lot of where I spend my time is also just making sure that people feel like they are energized, they're motivated, they have the tools they need, they have the context they need, and that there is good scrutiny on the work. Because actually I think that's the number one thing I've noticed — in organizations where people aren't actually paying attention to the data work, it's very hard for it to be amazing.

**Michael Chow:** Oh, interesting. Because you need like a great audience to appreciate it?

**Nell Thomas:** Yeah. And ask questions and push it and deepen it and challenge you. And so that's another thing that I always want to make sure is happening.

**Michael Chow:** I feel like the idea of scrutiny is such an interesting one. Like, in an org, what does scrutiny look like? It's also kind of a bad word, right? Like, you hear the word scrutiny or surveillance. It feels...

**Nell Thomas:** Yeah, it's like, check my work, but don't look too closely. Exactly. And no one wants to feel like their work is constantly being questioned, right? That's not a good feeling either, because it suggests a lack of trust. People who have amazing skills and are curious and great problem solvers, they don't want to feel like someone's coming in and being like, but did you add those things together correctly?

So it's not that type of scrutiny. It's more like people who can appreciate it. Maybe thinking about having a really great audience for a play — doing a play with no one there watching it, are you going to do your best work? But it's not just people clapping. It's also people engaging with the material and being receptive to it and contributing back to it in a way that makes someone feel like they want to do better and better work. And they want to keep staying in that conversation. So I think it may be scrutiny — I should think about a better word — but I think it's about attention.

When you ask me what it looks like, I would say it's making sure that there are the right forums or rituals, could be meetings, could be async things, but where people's work can be reviewed and discussed and debated and is part of the conversation.

**Wes McKinney:** I think part of what's so interesting about modern data teams is how essential data has become to every aspect of the business. I remember 15 years ago at conferences, there was this discussion about every company needing to become a data company. And I think today, the companies that are left are all effectively data companies.

Using data, making data — both collecting the right data and then processing and organizing it and making it accessible in ways where it can be available to all the people who need it and get the results, the analytics, the insights from that data in a way that is timely and actionable so that it can influence decision making, can be a part of product development and all the decisions that get made in the business. It's probably never been a time greater than now that businesses have been more dependent on their data teams to be able to function.

But that also creates this tension where the entire organization is like, our data team — they don't have something they need, they're not able to get the answers they need fast enough. Something doesn't work quite right. The tools that they're using to analyze the data — the dashboards or the query interfaces or whatever tools they're using — if they're not working in the way that they need to, that does make the business run worse. And so that puts a lot of pressure on the data organization to deliver and to continue to innovate and do better and better to ultimately make the business operate better. So I'm curious how you see that playing out and how you manage the expectations of the rest of the organization on what your team is building.

**Nell Thomas:** I mean, that was incredibly well said. And I thousand percent agree that fundamentally, most great companies right now are data companies and how well they leverage that data and the systems they build around it are one of the things that differentiates. So I completely agree.

I like to think about the value chain of data work from raw data creation all the way through to how that data is being used. And one of the nice things about my current role is that especially leading the data infrastructure team, I get to be pretty far left on that spectrum — from raw data creation to how that data is ingested, how it's processed, how we make sure that it is prepared for downstream users, both for analytical purposes or data science purposes and for production purposes. So for building ML models or any LLM use cases.

Being really far left on that spectrum is a place of immense leverage because the better we can — A, make sure we're collecting the right data, which is always a fun little problem, again, one of those age-old problems that's been true for my entire career. And making sure that it's captured in a clear way and making sure that we're actually being cost efficient. That's increasingly an issue now that we see how quickly costs can increase during LLM usage. All of that creates this ability for the whole company to operate better, whether that's the ML models being built or the analytics that are being pulled out of it.

In terms of managing the appetite for that, which I think is a harder question, I see that as an incredibly exciting challenge. I'd always rather be working in that environment than trying to convince people why data matters, right? Which at various points in my career has also been part of the job. I think right now we're in a moment where I don't need to convince anyone that they need to care about that spectrum of data. I think it's more managing the reality of what is possible, managing the expectations around how quickly we can get what we need, and making sure that we have the strength in our foundations on that left side of the spectrum so that we can trust the outputs.

Because increasingly, as you see, it's very easy to work on the right side of the spectrum with vibe coding and lots of ways that you can very quickly do an analysis. Underlying data quality, underlying foundations make everything. It's only positive benefits downstream from that.

I'm really orienting myself and my team around making sure that is where we have the trustworthy work so that we can make it self-service, we can make it accessible. We have an MCP for our data warehouse, so anyone can very easily access that data, making sure we have the right privacy and security controls in place to make sure that's all guarded in the right ways. Those are where I'm really passionate right now because I think it does manage a lot of those things naturally when you focus on trust and quality and systems.

**Michael Chow:** Are you saying — it sounds like your side of things is very data-engineer-heavy? And analytics-engineer-heavy?

**Nell Thomas:** Yeah, all of the above. We have a relatively sizable analytics engineering team that has traditionally focused on the pipelines that we use for all of our data science work and business analytics reporting work, dashboarding, etc. We also have data engineering problems that are much more about using that data for some of our production use cases.

And again, that's the fun thing about being a company that's at the scale of Shopify, is that you have great use cases on all sides of this, whether it's how we're using data that we're getting to predict the likelihood that a visit is a bot and whether we're using that either for routing that traffic on the edge or whether we're using that on how we're counting visits. Those are a very wide spectrum of use cases. One is for infrastructure purposes and one is for business reporting purposes, but it's actually the same data. It's the same model. You don't want to duplicate all that, right?

And so that's where having that holistic view of the data journey and the types of data work happening creates a lot of value. And I've always felt like data is a very ambiguous term. People say, I'm a data scientist. What does that mean? What part of the data stack do you work on? And so I'm more and more seeing there is a lot of differentiation in that spectrum, but I think people who are really good can kind of run that spectrum in their head at least. And they can see the connection between, hey, this is the raw signal that we have over here and here are the myriad use cases. And they can create unified solutions that help enable all of them. And so it's one of the things I definitely look for when I'm looking for new additions to the team — can they see that? Play it through.

**Wes McKinney:** I think one of the problems I've been thinking a lot about lately — and I just want to stay on this platform/architecture problem a little bit — is data teams do all this work to build, to engineer this whole pipeline of data collection, curation, ETL, data cleaning, data quality, and then engineering the data warehouse, designing the storage, the databases, the data access layers, and then the metrics engineering, semantic modeling. So you get further and further up the value chain. And eventually you start reaching the users and you can start thinking about how they're querying the data. What do their dashboards look like? Are they using Tableau? Are they using some other business intelligence tool? Are they using Python? Are they using R? What's their interface?

And so right now what's really interesting is we're seeing AI pop up and people using LLMs in all of those different parts of the value chain. And it also creates a lot of opportunity, but also in every place there's an opportunity for agents gone wild a little bit.

And so I can imagine there are going to be instances where the end user — one thing that people are talking a lot about these days is this concept of headless BI. So who says I have to use Tableau's UI? Just give me the endpoints and I'll use Claude Code or I'll use ChatGPT to vibe code my own custom dashboard. And not knowing that what's inside might be some very large SQL queries that the person building their personalized dashboard — they can't read the SQL or they can't judge whether this hairball of vibe-coded SQL has errors. And so they get a dashboard, they're like, oh, it looks right. It actually contains errors.

And so it's kind of a disruption of the more heavily curated approach — actually having an analytics engineer or somebody with data science experience building the dashboard and writing the SQL by hand and making sure that what you're seeing is the reality of counting things correctly.

**Nell Thomas:** Yes, I agree. But I'm also going to challenge that a little bit because I think — I mean, I've observed at a lot of companies a lot of overly complicated verbose SQL with business logic embedded at that last mile delivery of a data dashboard as well. I'm not naming names, but it's very easy for a lot of these tools for you to actually push your — instead of doing your semantic modeling in the right place and doing it in a way that's code-controlled and doing it in a place that you can really audit, they're putting it basically for the presentation layer. And that becomes very inscrutable. It also creates a common problem at a company — we have a thousand definitions for this core metric. And you actually have to ask the person who knows the right SQL query to write to get the correct value.

Again, with best practices, you're handling all that. But a lot of companies like that — there's slow creep. And all of a sudden you have, which is the right dashboard to use for X? And this person gave me this number and that person gave me that number. So I don't think the problem that you described of can you trust the dashboard is new with the emergence of AI. That's totally fair.

**Wes McKinney:** BI tools can get very creative with the SQL they generate.

**Nell Thomas:** Yeah. And I think it's a not uncommon but suboptimal value prop that sometimes the data scientists have, which is, I know this table the best. It's not even knowing the code — it's like, I know the nuances of this particular table in a way that's arcane. And I'm the only one who can properly write the WHERE clause that suppresses the types of things that shouldn't be counted. And I think that's not ideal because then you're encoding a lot of really important information in one person, as opposed to making it something that a whole team can benefit from.

So I think everything you described about how to make sure that you have really great ETL, really great data pipeline orchestration, really strong modeling, semantic layers, the right tests to ensure all those things are running well — so important. I think that humans and LLMs might be almost just as likely to have some challenges making sure that you have consistently trustworthy presentation. Not that I trust LLMs more than humans, but it's a common trap that everyone falls into.

**Michael Chow:** I almost wonder if at this point it'd be useful because we've talked a bit about data engineers, analytics engineers, a little taste of BI and this big stack. Would you be up for almost trying to lay out who's involved in this stack as you see it?

**Nell Thomas:** Yeah, sure. So I think all the way on the left, you really have your production engineers who are writing the code that hopefully generates the instrumentation that gathers the data you need, right? Whether that's writing to a database or firing an event that's sent off to some sort of log.

Then you have your data infrastructure engineers that are ensuring you're ingesting that data correctly. So whether that's how the events are being fired into whatever Kafka topics, or whether you're replicating data from a database, and then doing the work and building the data platform of processing that through a whole bunch of storage and compute layers that are doing some sort of modeling of that data.

Usually at some point you're handing it over from what is more of a data platform engineer — of creating the house — to the analytics engineer, who is then ensuring that the raw ingested data becomes modeled data that is hopefully some sort of canonical data asset that then the data scientist can query and manipulate.

**Michael Chow:** Just to check — at that point, once it hits the analytics engineer, you're in something like BigQuery or...

**Nell Thomas:** dbt, you're writing SQL or a dbt model, maybe you're using Airflow. I mean, that's the stack we currently use, but yes, that's very common. Maybe you're using Snowflake instead of BigQuery, but obviously flavors vary.

But I think those big buckets are pretty universal. You have the team that's responsible for maintaining the data house, and then those people are working inside the house, as I like to say.

And then obviously at the very end you have your presentation layers, whether that's Looker Studio or Looker or whatever flavor. They all have their limitations, in my opinion.

The other use case here that I mentioned in the beginning is also the diversion of some of that data out of the data science use case into more of the production modeling use case. So like, hey, we're going to model this data to use it for recommendations, for search, for some sort of prediction. And in those cases, usually the handoff isn't to an analytics engineer. It might be to a data engineer or to a machine learning engineer — the path of coding for the machines, as opposed to coding for human input, which is where I think usually most data science and analytics work ends up. It's something that a human looks at to review and make a decision about, as opposed to a machine is taking it in to decide about how to rank something or how to display it.

**Michael Chow:** Are you saying the analytics engineer is modeling the data for an analyst or people downstream to pull it, but once you get into special cases of modeling where it requires domain expertise...

**Nell Thomas:** Yeah, I think the differentiation there is a little bit about latency. So analytics engineers are often working in batch — it might be totally acceptable to have an 8-hour, 12-hour, 24-hour delay in your data being fresh because you're counting things to do an experiment analysis or do a user behavior analysis of usage of a product or feature changes over time, but usually on a longer scale.

Some of the production or operational use cases I'm talking about, you might have very low latency requirements. Like, I want to be able to process data very quickly because I want to see what a buyer is doing on this site to be able to change what I'm showing them on the site. And so that has different requirements for the data infrastructure than you would for the analytics use case.

One of my points here is that the further left you go on that spectrum, the more unified it should be. And then it kind of starts to fork over time, but you don't want it forked the whole time because you end up with a bunch of data replicated, a lot of costs involved, and probably a lot of lost knowledge and context and value because you're not getting great reusable learnings between those two streams.

**Michael Chow:** It's so helpful to lay out the people. But the other thing I'm really curious about — we just talked with Tristan Handy from dbt Labs recently who tried to break down why people use dbt to someone like Hadley Wickham who's thinking a lot about data analysis with R. Sometimes it's worth asking the question, why are we using this tool again?

**Nell Thomas:** It's always usually good to ask that question. And people are afraid to ask it because they're like, I'm cool. I get it.

**Michael Chow:** But I know dbt's relatively recent, like in the last seven, eight years. I'm really curious how you've seen that shift. Like, I'd imagine a place like Etsy was pre-dbt.

**Nell Thomas:** Pre-dbt, very much so. Etsy is an important part of my evolution as a human, but also specifically as a data person because it's where I learned to be a manager and grow a team. So it holds a very special place in my heart.

Also, very quickly on laying people out — my number one recommendation to any person who's new to a company is to get your hands on an end-to-end data flow diagram. What are the technologies being used at every step and who owns them? I think having that holistic view really helps connect things up. It's kind of like a food chain. What are you eating?

**Michael Chow:** Are you saying people should Google the term "modern data stack" or something?

**Nell Thomas:** No, I think you should ask someone internally. Like, do you have this? I bet half the time people don't have it. But if they do, or they only have part of it — they're like, okay, well, the data's in BigQuery, and then we use this. And you're like, well, how did the data get in BigQuery? And then it's kind of asking that infinite set of questions. Where did that come from? And where did that come from? Tracing every data point from somebody clicking on a website to how it ends up in this dashboard.

I just think it's a really interesting way to make tangible some of these things we talk about that are super abstract.

**Wes McKinney:** A closely related question is how you've seen teams navigating technology choice. I feel like as time goes by, it gets harder and harder. The landscape — the modern data stack, you need a microscope to look around at all the different thousands of technologies. There's open source projects, companies, products. I remember there was a famous blog post years ago — "choose boring technology" — and that's probably the right answer most of the time. But often engineers are enthusiastic about some new open source project and using that thing, and adopting new technology carries risk and maintenance and institutional knowledge. So it's a big topic. Curious how you see it.

**Nell Thomas:** It's a huge topic. There's the classic build-versus-buy part of this. There's the deprecation of legacy tools, which is really important and often doesn't happen. And there's the fragmentation of technologies people are using internally and how much do you encourage and permit versus how much do you clamp down on that?

I mean, I remember when I was at Meta, people used all sorts of different personal data stacks. I mean, the data sources were the same, but then some people were using Tableau, some people were using Mode — it was kind of a wild west.

I'm going to attempt to answer your question by connecting it back to the question about Etsy. When I was at Etsy, it was very big on do-it-yourself. Kind of per Etsy's vision as a company — it was founded by a carpenter, very much about craftsmanship. Our databases were all on-prem. It was very much build-your-own-stack. So that was true of our data as well, and our data folks were writing Scalding.

**Wes McKinney:** I haven't heard that name in a long time.

**Nell Thomas:** Nope, you haven't. It had a moment though. We had a Vertica cluster. This is where we did our... which is also an old technology. Weirdly, I've done two Vertica migrations in my life, one at Etsy and one at DNC.

So it was a lot more homegrown tooling. It was a little bit deeper in the stack, which I actually don't mind, because I think when you have less sanitized data as a data scientist, you're going to be getting your hands a little dirtier. I think you're going to learn a lot.

Obviously, pre-dbt, people were writing a lot of SQL, some R, some Python. But a lot of the challenges we had there were not that dissimilar from what I see now in terms of — where is the data for X, and is this the right data? And I think with LLMs, those are still the same questions. Can I trust what the LLM is generating? Can I interrogate what data source they're using, and are they handling it correctly?

There's still a lot of art in using your dataset correctly because you understand the nuances and arcane details. I think it's an interesting evolution of the challenge for us to figure out how to make sure we interrogate the way LLMs are using data, and create visibility on the choices an agentic data scientist is making, make it more transparent, more testable, and quantify errors.

**Wes McKinney:** One of the things I'm seeing discussed a lot lately is agents putting a lot more load and stress on data platforms. It used to be that you'd write a SQL query, run it, look at the result. The human in the loop kind of created a natural rate limiter in terms of the number of queries. But now you can have a bunch of agents interrogating a data platform. And in a way, it's almost not differentiable from a DDoS attack in some cases, where it's just running SQL queries over and over. I imagine that's going to change the way data platforms are designed, with guardrails to help agents not DDoS the data platform. Also, LLMs are not good at looking at large amounts of data, so you can't give them very much data at any given time.

**Nell Thomas:** Again, I think this is where some of the best practices that the industry has been talking about for decades are still the most important. Work out in the open. When you're a data scientist and you're writing code, first of all, write code. Don't do your analysis in Excel. Write code, check it into GitHub, make it observable by others, have it code reviewed, store the output of your analyses in a notebook. Have it all be visible and accessible so someone can walk through your chain of logic — what data was used, what assumptions were made, how was the data changed or manipulated to reach some conclusion.

I think we need LLMs to be able to follow that same path so we can follow their reasoning just as much. I do get shared screenshots of Cursor outputs all the time, mostly by non-data scientists. I love one of my fellow VPs at the company, but he loves to do a rogue analysis and send me a screenshot and be like, "I found the number." And my first question is always, what data sources are you using?

I think the more we can get people on workflows and have their agentic toolkit include some of those best practices that we all know and love, the more we can trust the output.

**Michael Chow:** It's interesting you made a point earlier about the value of an audience, and it sounds like you're also talking about the value of putting your work out so people see it.

**Nell Thomas:** Yeah, I mean, it really builds a lot of trust. When you can show — I mean, to the point you made earlier, Wes, that I kind of challenged you on — there are a lot of people who will just produce an answer, like, oh, we ran the experiment and here is the result, and you get a slide in a deck, and then you're forced to just trust that this human is doing everything right.

But hey, actually, if we can build a system and a set of tools where it makes all of that experiment work really easily auditable, and you can see it and interrogate it — that inherently builds trust in the platform, and it also allows the data person to do higher-order thinking. When transparency in your work is the default, it automatically breeds trust in the results of that work, and it frees people up from that loop of questioning what assumptions you made or what time period you used.

It bypasses all that so you can actually have a conversation about what to do with it. Like, okay, now what do we do now that we have this answer? And so I find that part of best practices really compelling, because it's not just governance for governance's sake, but it actually speeds up the rate of idea to answer and getting us to insight faster.

**Michael Chow:** Do you find people are pretty quick and willing to be transparent, or is there some resistance? What do you see in people?

**Nell Thomas:** First thing I'll say is I have a huge amount of selection bias in what I know about. It's one of the hardest things about being in a more senior role — people don't always want to tell you the truth because they feel like they should be managing up. And I also talk to people who work for me directly the most, and talk to the average entry-level data scientist the least. So I'm always careful about how I answer a question like that, because I'd much rather you had someone from my team here to talk about how they think about it, as opposed to what I think they think about it.

I think in terms of how to encourage a culture where people feel comfortable sharing and working transparently, the number one rule is making sure that when people share their work, the dialogue is healthy and productive. Even if there's an element of critical review, it's from a place of good human interaction. People don't want to work with people who are jerks. They don't want to work with people who are tough or demeaning or being critical of work just to be critical. They want to do it if it's making their work better, and it's craft.

I think probably the most important thing is that to be vulnerable in sharing your work openly, you have to trust that it's going to be received with good intent.

**Michael Chow:** I can see that being a huge factor.

**Nell Thomas:** And I mean, it's easy for me to say that. It's hard for that to happen at scale. But that is definitely one of my corporate beliefs — you want that radical candor where people can be honest and say the hard thing, but also do it from a place of good human trust.

**Wes McKinney:** To me, it seems like the challenge for leadership is creating psychological safety where people feel comfortable — if they see a problem, if something's not working well, that they can share critical feedback without it being punitive. Ultimately the goal is how do we have a successful organization? How do we do better? It's not about pointing fingers or blaming people.

Sometimes there's retrospective looking at past work and saying, it worked then, it's not working today. And sometimes people feel like that is a negative judgment on the work that was done before. If you allow anyone who makes anyone feel that way in an organization, I think that's bad. Because teams have to continuously improve. Whenever something was good then and not good now, let's figure out something better. And not be too attached to sweeping things under the rug.

I've seen companies and teams allow things to rot and fester — code that bit-rots or systems that outgrew their usability or that start to become liabilities and don't get torn out and replaced because it's going to hurt somebody's feelings.

**Nell Thomas:** You said a couple things that really resonated. One, psychological safety — it's a well-worn term, but I think it is the core of the question.

Also, sometimes people get really precious. Things become precious. You start having these tools that no one can touch, or decisions. And one thing I really appreciate about Shopify is that our CEO founder, Toby, is very focused on first principles. That means every tool and technology and choice is always up for discussion. There's no sunk cost fallacy of, we can't talk about that because we've already invested X amount of time.

So much of organizations is always dealing with the years that came before you. Organizational design is always a product of past choices that often are unintentional. You get into weird patterns of — why does this team report over here? Well, four years ago, someone was reporting to someone and they got into a fight and then moved. There's always these weird historical accidents in organizations and in systems. The more you can de-risk re-interrogating those, the better.

**Michael Chow:** Have you seen big differences? Since you've worked at really different organizations — what's that willingness to interrogate and switch up been like in different contexts?

**Nell Thomas:** As a technology leader, you spend a lot of your time thinking about the tools you choose to use. But that cultural vibe is actually almost as important because you're going to make a lot of wrong tooling choices. But if you can get the right culture and the right people, you can make a lot of mistakes and it's going to be okay because you can switch them out.

I think I've worked in a lot of interesting cultures. I think there have been places where there's more freedom to interrogate and there's less. One thing Etsy did very well in terms of psychological safety was they were very big on blameless postmortems. That idea of, we're going to do a retro and make a point of going overboard about never having this be about an individual failure. It's always a system failure and how did a person get caught up in that system failure? That spread around the company as a way of just thinking about mistakes generally.

Right now at Shopify, Toby's investment in hiring people who are super high agency, who have high curiosity, a willingness to learn and treating learning like a muscle — not something you do once but something you do every single day — that creates a culture where it's like, we're not here because we're experts in Rust or Python. We're here because we're smart people who can solve hard problems and use all the tools at our disposal.

**Michael Chow:** I heard on a podcast one really interesting thing about the DNC — this challenge of almost the opposite problem of political campaigns where they make a lot of creative use of technology and then they wind it all down overnight and throw it away, which seems like the opposite side of this problem. Innovation just gets thrown in the garbage.

**Nell Thomas:** Oh my goodness. It's a huge issue in political technology. Campaigns are these ephemeral moments. You have a campaign, it gets spun up, it lives as an organization and as a set of tooling choices for maybe at best 18 months if it's a presidential campaign that makes it through the primary, but more often it might be three months, maybe nine months.

It can be a lot of throwaway work and throwaway org structures. And that is really hard on the overall goal of wanting to learn continuously and leverage those learnings cycle after cycle so the next campaign can be better at talking to voters than the prior one.

That's one of the things that organizations like the DNC try to address — creating consistency across those cycles. Making an investment in technology and infrastructure that creates a strong foundation that campaigns can build upon. Ideally, we take the best of the campaigns and build them into the foundation and create a positive feedback loop.

**Michael Chow:** That's so interesting because you talked about sunk cost and being willing to investigate sunk cost, and then this, where you're sinking.

**Nell Thomas:** Exactly. That's the problem. And the problems in political data, I think, are much harder than a lot of the online data companies, whether it's online shopping or online advertising or social media. It's a different problem space, and the margin of error in terms of lost learnings is different.

**Michael Chow:** Do you feel like you're bringing in the same kind of playbook into those situations as a data worker?

**Nell Thomas:** As a data leader, for sure. People are people, and they fundamentally need a few things — they need to have a good flow state, a bare minimum of good tools, they need to feel respected and have psychological safety, they need to feel connected to something greater than them. Those are usually the core things that people get motivated by, and that's true whether you're working in tech industry or on a political campaign. Obviously on a political campaign, you probably have a higher likelihood to be super connected to the mission.

On the data side, there are obviously a lot of similarities — you need strong data quality foundations. The biggest difference is scarcity of data. In political campaigns, mostly the outcomes you care about are getting people to vote. Voting is an offline behavior. It's also a very sporadic behavior. Maybe once a year if you're lucky, or once every four years, or maybe not at all.

Someone might say, well, just connect them to all of their online behavior. But connecting those things is really hard. Most people don't spend that much time being politically engaged. Usually the people you most want to reach are the people who are least likely to be politically engaged. They're buying Ugg boots, clicking on an ad, watching a dog video. That gives me very little information about how to convince them to like some candidate.

In comparison, being at Etsy or Meta or Shopify — I'm spoiled by data. You get so much data about every little thing someone's doing. Creates different challenges. How do you manage all that data? How do you sift the junk from the good stuff? But the feedback loops are much faster. It's a different beast.

**Michael Chow:** I also realize this might be a good chance to explain a little bit about what Shopify is.

**Nell Thomas:** A hundred percent.

**Michael Chow:** Just roughly — what data? What company?

**Nell Thomas:** Great question. Shopify is a platform for merchants, or a platform for businesses. Primarily selling goods online or in real life — we also have a retail offering. It has millions of merchants using the platform to reach customers and consumers. There are some very big brands that everyone would recognize — Skims, Alo Yoga, Allbirds. But there are millions more amazing long-tail merchants that might be in your local neighborhood. My local yoga studio is a Shopify merchant. They have an amazing little store. As well as subscriptions and things like that.

It's really the infrastructure — the pipes underneath. It's how stores can build a storefront but also manage their inventory. They can email and talk to their customers. Right now there's a whole bunch of work to make all this agentically really easy. You can basically — if you're an entrepreneur building a business, you're passionate about what you're building, you're probably not passionate about writing the code to run a website. Shopify takes that off the plate so the entrepreneur can do their best work.

The data we have is a lot of online shopping data. Millions of buyers making purchases from merchants around the world. It's an amazing view into online commerce. It's one of the major engines of online commerce.

**Michael Chow:** And I love — it sounds like you do data infrastructure for the companies that is infrastructure for shopping. So it's infrastructure all the way.

**Nell Thomas:** It is. Absolutely.

**Michael Chow:** Just out of morbid curiosity, were you Python or R or what?

**Nell Thomas:** Python more than R. But neither really that well, honestly. I mean, I would say my coding skills were never my strongest technical skills.

**Michael Chow:** I'm sure you were a contender.

**Nell Thomas:** I'd like to say my very first language was VBA, which really dates me.

**Wes McKinney:** *[Horrified look]*

**Nell Thomas:** Oh, yeah. A little too much VBA in my past, unfortunately. Terrible memories.

**Wes McKinney:** The way I always describe Shopify to people is, part of the reason Amazon got so popular so fast is that people didn't like typing in their credit card information and their addresses into slightly different forms on every website. And now, whenever I shop from an online merchant that uses Shopify, I don't have to type in all my stuff. It just remembers my credit card information, has my addresses. It makes the whole experience better — especially makes me feel better about not giving all my money to Jeff Bezos.

But speaking of agents — Shopify was in the news from its founder Toby publishing an internal memo around adoption of incorporating AI into everything that the company does. I think we find ourselves in this really interesting moment. I feel like last March was this inflection point with the release of Claude Code and the first coding agents. But something has happened in the last 60 days which has triggered an even bigger acceleration. It's not even a hockey stick — it's just a straight line up.

I'm really curious — navigating overall what it means to incorporate AI into all the different ways that a team like yours works, but now with engineers going into overdrive using coding agents. I can imagine that could create a lot of chaos with a million agentically engineered side projects. People wanting to reevaluate every piece of technology and whether they could replace it with something more bespoke. It's completely upended the buy-versus-build calculus for certain kinds of things.

**Nell Thomas:** It was a pretty big shift when Toby wrote that memo. It was released internally and then it found its way outside of Shopify. I would say I feel very lucky that I was at Shopify at this moment in time because that mandate created a lot of clarity. It took away a lot of the noise of should one or shouldn't one? Is this a direct assault to one's craft and discipline? What does this mean for the future of work? It kind of just said, the future is here, figure out how to use it. And that's actually fun.

When you shift from the fear-based mentality of how is this encroaching on my job to this is another tool and how do I use it to its fullest potential to do my work — it really shifted the feelings around it. And I've seen such incredible work happening internally. I'm continually humbled by how smart and creative people I work with are.

One thing I was incredibly proud of — I think Anthropic announced the Model Context Protocol for MCPs in November 2024. And my team had built one by February. We had an MCP for our data warehouse. Very quickly, people could start doing all the fun analysis. I think that was a good six months before a lot of other companies were doing something like that.

And so that's an example where I think it's creating a lot of flywheel. I know it's scary, and it feels uncertain, and we don't know where it's going, but it's also fun. And it's creating a lot of opportunities to just try different things out, and that is sometimes rare.

**Wes McKinney:** I'm having a lot of fun with agentic coding. I was just watching Peter Steinberger, the creator of the now viral CloudBot — he gave a talk late last year titled, "You Can Just Do Things." And I wrote a blog post called "Why Not?" And that was kind of my new motto — you want to build a thing? Why not? Try, build something, it doesn't work, it's not good, throw it away.

Code now has much less value. It used to be that code artifacts were the product of human labor, and you could attach a cost to this. The code-counting tools like SLOC and CLOC would be like, oh, this codebase would cost $3 million in three years to build. I built it today with my agent.

Part of what's fun is just not knowing the right and proper way to do things, and encouraging that experimentation and creativity. For me, what's happening right now gives me the same feeling that I got when I started to do Python in the late 2000s — I can just write code and do things. Almost 20 years later, it's that same feeling again of, we can just do things.

But also, I can imagine in a company setting, trying to channel that enthusiasm towards productive ends — you know, let engineers enjoy their tokens, try to understand what was a good idea and what wasn't. Maybe three to six months from now, some of the fervor will dissipate and people will be like, okay, this is the best way to use agents to build stuff.

**Nell Thomas:** Yeah, I mean, most of the best things in life get more interesting the more you engage with them. And I think that's true of AI and LLMs right now. The first couple times you do something, you're like, oh, this is magical. But then the more you use them, the more magical they feel. That part is really exciting because it kind of makes you want to keep going down the rabbit holes and pulling those threads.

Which, again, to your point, can be a little bit distracting if you also need to do your job and have tickets waiting. But I think those two things can go hand in hand. Shopify is a pretty fast-paced company with a rigorous set of milestones to hit. People are mostly doing all that creativity for the purposes of impactful work. I don't worry too much about it being a bunch of side quests right now.

But I do think it's uncertain. If six months ago we locked in and said, all right, this is the way to AI, we would have made a bunch of bad decisions. So I think it's probably premature to say here's the right way. A lot of people are still figuring it out. Demystifying the idea that there is a right way to do anything right now is important because no one knows. The next Claude model is around the corner. You never know what's going to emerge in two months that's going to change how we thought about things.

**Michael Chow:** It reminds me — Charlie Marsh also mentioned this sense of uncertainty as a leader. How would you describe how much uncertainty there is? Is this a level you've seen before, or is it one of one?

**Nell Thomas:** For me, this is the most uncertainty I've felt about how a technology might evolve. I was post-internet — people compare it to early internet days, which I didn't quite experience. So for where I am in my career, this is the moment of the most uncertainty.

But a fun fact — I studied the history of science and technology, and there certainly are moments throughout history where there was immense uncertainty about emerging technologies. I don't think this is one of one in the history of how humans have used tools. I think it's a very big one, and certainly the biggest in my lifetime. But it's a pretty common pattern when a new technology emerges — whether it's the car, or the fax machine — there's a period of misuse usually, where the technology is changed by the users.

**Michael Chow:** We can make this whole thing about history of technology. That's a crazy credential to drop.

**Nell Thomas:** That was one of my side quests.

The simple narrative of the emergence of technologies is usually the founder myth — this one person invented X and they knew exactly how it should be and how it's supposed to be used. But in many, many cases, the technologies get fundamentally altered by the people who use them. That usage changes the trajectory in unexpected ways. It's very much a co-evolution once technology has emerged between the technical practitioners, the users, and often regulation. Those governing bodies start to play into how the technology can or can't be used.

We're at that moment right now where all of those things are a little bit up in the air. And what's very cool is AI is something that is so clearly not a founder myth. It's not like there's one person who's like, and now you all can benefit from my great tool. It is such a collaborative moment between all the different ways people are sharing what they're doing and being able to inspire each other. That part is very exciting — the co-evolution of this technology.

**Michael Chow:** It's so inspiring to hear from that perspective — versus a force that threatens to crush you, the co-designing, the exploration. And it's a really interesting point that so many people are sharing what they're building right now.

**Nell Thomas:** It is. There's a lot that is scary. I don't want to gloss over that. Obviously, there's massive existential questions at play. But purely thinking about it in the bubble of how do we use this to do better data work, there's a lot of fun.

**Wes McKinney:** In the past, you would say, well, we can't justify staffing a team to build internal tools for, like, certain types of platform observability or internal systems. Now, that cost equation has changed. There might only be a small audience of people that benefit from creating some new tool. But if it saves them an hour a day, they might spend a day building the tool. If it saves them an hour a day going forward, that's material savings that can be directed toward something else.

**Nell Thomas:** Yeah. Actually, if it's useful to give one more concrete example — a very common data science problem is, why did that metric go up or down? The answers are usually one, seasonality not being properly controlled for; two, a data pipeline issue; three, there's actually some meaningful movement here that we need to understand.

There are so many ways that automation and AI can really help run through the initial hypotheses and jumpstart the investigation into the interesting problem space. There's a playbook most data scientists use — can you get those initial reps in faster, in a less costly way, using some automation, using some AI, and allow you to get faster to the point of interesting work?

We're doing a lot of work right now to put better best practices and governance in place around defining metrics — basically semantic layer stuff — defining metrics, reusable segmentations or dimensions, making sure everyone's cutting by the same things, building better benchmarking tools, and then building alerting and automation on top of that. So there's this interconnected set of things from how you define the metric in code to how you get to understanding how that metric is moving in the most meaningful way.

**Michael Chow:** So you're saying when a metric changes, a data scientist has a list they can go through, and AI can be pretty good at taking a pass at it?

**Nell Thomas:** At least taking a pass. Usually it's going to be — is it moving in all regions or just a couple? Okay, it looks like it's mostly moving in the U.S. Is it based on the age of the cohort? It looks like it's primarily coming from this segment, or no, it's widespread. Those permutations — you can use automation to do that. You don't want to automate all exploratory analysis away, but can you help jumpstart? Think of it like a metal detector — get to the area where the interesting nugget is so you're not doing the macro map.

And a lot of times people don't think to cut by some dimension, and that's actually where the interesting nugget was. But again, data modeling is still the most important problem in that, because you can't do any of that fun automated analysis if you don't have the data modeled properly.

**Michael Chow:** You mentioned the semantic layer, and that's been a hot topic at various times. I wonder if it's worth just saying briefly what a semantic layer is to you.

**Nell Thomas:** Yeah, I mean, also we probably shouldn't use this bit, but I would say semantic layer decisions have been my greatest failure as a leader. But yes — what is a semantic layer? Basically, it's a way to translate between a defined metric, or defined business logic, and the modeled data that you have, and it's reusable across the company, so that you can always reference the same thing.

Looker has a semantic layer built into it — LookML — that's the magic sauce stitching together the datasets and the business units on the other side. Many companies use different versions. It's something I've been grappling with internally. I had a lot of conflicting input from my team, and I had a really hard time navigating it. It's something we're re-interrogating.

**Michael Chow:** It's so helpful to hear. If you're grappling with it, I'm sure everybody else in the world is grappling with it too.

**Nell Thomas:** Yeah. And it's also a good example where sometimes different components of my team have different needs out of it. I have a team that does what we call executive insights — looking at cross-company trends. And I have other teams that are deeply embedded in a product area — just working specifically on our storefronts, or checkout, or our Shop app. Their use cases might be different, and people get attached to what they've been doing. They're like, don't give me some new thing, I have my semantic layer I like.

And so unification is really important of getting everyone on the same thing, but it also comes at the cost of people migrating, which is never fun. And that's where some of my job is to make the hard decisions — yep, we're all doing this. And yes, I'm sorry, you have to do it. When I don't have clarity on what the right tooling choice is, it's the hardest, because then I'm not confident that the juice is worth the squeeze.

**Michael Chow:** Is there any way you can describe the difference between some of these tools? Like, different semantic layer flavors?

**Nell Thomas:** Some of it is how homegrown you are versus not. There were versions that were more dbt-reliant versus not. Whether to go all-in on Looker was another decision. It was about how much dependency do you want on a third-party tool, and how much investment do you want to make in your own tool?

We were also hitting limitations with some BigQuery changes in datasets over time. So we were hitting technical limitations, debating the future of our commitment to Looker, which we are not really committed to, and also debating whether to get people who were on separate systems onto the same one. We have an internal tool that uses a different one, but it's not a huge investment. It's more that the users had different perspectives on their most important priorities.

**Wes McKinney:** Looker is probably the most successful semantic layer company. Essentially it's a semantic layer company that looks like a business intelligence company. The creator of LookML, Lloyd Tabb, has a new semantic layer called Malloy that I've been following quite actively. But then there's other companies like Cube and others. It seems important to have the team invested in whatever you're using. I can imagine there's also the need for good telemetry about what's actually being used, because you could have blind spots where part of the semantic layer is being maintained really well and we have good confidence, but then there might be dark corners where it's drifted because of underlying changes in the data warehouse.

**Nell Thomas:** We've invested a lot in data quality metrics for the data warehouse. The analytics engineering team is responsible for this and we have a monorepo basically for our data warehouse — Shopify is also very big on monorepos, so it's a monolithic development environment.

That team is really focused on the ergonomics of working in the data warehouse and the quality of the data. You have to meet quality standards to be in the data warehouse. We've had a big effort around measuring documentation completeness, measuring freshness and timeliness, measuring usage, and a bunch of tests about completeness of data. That's an age-old problem that you always have to be investing in.

**Michael Chow:** I feel like we've talked about so much — from data cultures to you kindly laying out the whole stack, which feels like a Herculean task. And I think attempting to tackle a semantic layer is a special form of courage. I do think this conversation would be complete, though, with the fact that you mentioned your last podcast was to talk about the movie Sneakers.

**Nell Thomas:** That's right. I have a very specific movie knowledge of one movie from the 90s. I do love the movie Sneakers. I am not an expert, but I am a lover and champion. If anyone has not watched it — it's incredible. People often ask me, what advice would you give to someone earlier in their data career? And I'm like, watch the movie Sneakers. It will teach you nothing about data, but it's just a good time. It'll give you a good laugh. It'll make your day better.

**Michael Chow:** Is that — do you tell people getting into data work they should watch Sneakers because that's the right answer? Because that's your answer to everything?

**Nell Thomas:** That's the data scientist in me. What's this model doing? It's a good movie.

**Wes McKinney:** I only saw it in the last 12 months, and it holds up. It's definitely got some 1990s charm. But for me, the 1990s movie I've seen the most is Groundhog Day. I have very good knowledge of that movie. But I would co-endorse Sneakers.

**Michael Chow:** I haven't seen it. Groundhog Day is kind of a data science movie too, because it's about what happens with repeated...

**Wes McKinney:** Yeah, that is true.

**Nell Thomas:** There's apparently a whole cult following of Groundhog Day with alternate theories about what the movie is really about.

**Michael Chow:** I love those corners of the internet. When they're positive — where people are having fun going as deep as they can into the mythology of a particular movie. That's people at their best.

I do feel like it's closely related to the activity of trying to connect cinematic universes. What if Groundhog Day and Sneakers occurred in the same — they were released very close together.

**Wes McKinney:** Right. Coincidence?

**Michael Chow:** So, great movie taste. I feel like now that we know you're a cool person, maybe we just wind down. How do you like to unwind?

**Nell Thomas:** Well, I mentioned at the top that I have two little kids. So I wouldn't say that's unwinding, but — fulfilling. My recent unlock with them, my youngest just turned three, is that I've introduced them to Mario Kart. I'm an enthusiast, not an expert. But it's so fun to play with them. The three-year-old just holds the remote and it auto-drives. My five-year-old tries really hard.

**Michael Chow:** As you're blasting them with shells, is that...

**Nell Thomas:** Well, weirdly, she usually comes in eighth, and my sweet five-year-old who's trying really hard always comes in 12th. But that's been very fun to introduce them to a little nostalgic throwback and just have some silly fun. It's underrated, just fun.

**Michael Chow:** That's so sweet. I really appreciate you coming on. It's so inspiring to see how you've woven between different jobs and balanced impact and industry work. Really appreciate you weighing in on the modern data stack and AI, and I think you helped me wrap my mind around what it means to lead a group of 400 people, which I'll still have to spend some time marinating on.

**Nell Thomas:** I'm still marinating on it. I'm three years in. We're all still figuring this out. That's my biggest thing — it's all always a little bit haphazard how we make our way through these choices.

**Wes McKinney:** Really appreciate having you. Thanks a lot.

**Nell Thomas:** Thank you. This is fun. This is really fun.

*[Podcast outro]*

The Test Set is a production of Posit PBC, an open-source and enterprise tooling data science software company. This episode was produced in collaboration with creative studio Agi. For more episodes, visit thetestset.co or find us on your favorite podcast platform.