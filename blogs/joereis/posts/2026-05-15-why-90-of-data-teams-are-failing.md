---
title: "Why 90% of Data Teams Are Failing at Data Modeling"
subtitle: "The Weekend Windup #33 - Cool reads, events, links, and more"
date: 2026-05-15T21:53:30+00:00
url: https://joereis.substack.com/p/why-90-of-data-teams-are-failing
slug: why-90-of-data-teams-are-failing
word_count: 1843
---


Earlier this week, I published the results of April’s Data Modeling Pulse Survey. I wrote up the full surveyover at Practical Data Modeling. I also recorded a Freestyle Friday this morning while walking around Salt Lake City, unpacking the data. But I want to spend the weekend post on the thing the data is actually telling us, because it's bigger than data modeling.


---


Sponsored byFivetran: Your pipeline works great for 3 data sources. Will it work with 30?


Manage >750 data sources without rebuilding pipelines. Fivetran delivers analytics-ready data in hours. Fivetran handles: schema changes, API updates, and retries. You handle: strategy, AI, and infrastructure overhauls. Free for 14 days, flexible pricing afterwards.Try Fivetran free.


![](https://substackcdn.com/image/fetch/$s_!lmnH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1a2082a-5cfa-4669-bc7a-3f9cf544a527_425x118.png)


---


Sponsored byRevefi: Are your Snowflake costs going crazy? Most data teams spend months analyzing Snowflake costs. You can reclaim up to 50% of yours in just hours.


Talk to aRevefi experttoday.


![](https://substackcdn.com/image/fetch/$s_!6spe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F57fab78b-d47d-49a2-84c0-1ce903a94c4f_301x101.jpeg)


---


# Data Modeling’s Biggest Pain Points Aren’t a Tooling Story


Here’s the number I can’t get out of my head this week:4.8%.


That’s the percentage of working data practitioners who said “better tooling” would most improve data modeling at their organization. Out of 334 respondents to the April Practical Data Community pulse survey, sixteen of them pointed to tools.


The other 95.2% pointed at training, requirements, time, and ownership.


Let that sit for a second. These numbers are against the backdrop that AI will “solve everything.” The number of AI-powered SQL tools is insane. But schemas and SQL are not data models on their own. And if you’re a vendor selling a modeling tool (or frankly any tool), this is the kind of number that should keep you up at night. If you’re a practitioner, it’s the kind of number you forward to your boss (hopefully they understand). And if you’re a leader, it’s the kind of number that tells you exactly which conversations you’ve probably been punting.


# Three Surveys This Year. Same Answer Every Time.


I’ve done three surveys this year. Each one has a similar theme. January’s State of Data Engineering survey (n=1,101) flagged “lack of clear ownership” as the #2 modeling pain point. I decided to dig deeper with the April pulse survey. The April pulse (n=334) tells you why: half the field works in environments where data modeling has no real owner. 42.5% of respondents said modeling decisions are made by “whoever is building the pipeline.” Another 7.8% said nobody, and “models emerge organically.” Only 19.2% have a dedicated modeler or architect anywhere in the org.


So the picture is this. Data pipelines get built. Models get built as a side effect of pipelines getting built. The person who built them moves on. Six months later, somebody tries to query the resulting mess for a dashboard, an AI feature, or a semantic layer…and the firefighting begins.


One respondent put it cleaner than I could:


> It’s not a modeling problem, it’s an ownership problem.


Another nailed why the ownership keeps falling through:


> One person can build the architecture. One person can’t make a team use it. The ungoverned path has no bottleneck, so that’s where models get built.


This is an organizational design failure, and better tooling might ease the pain a little, but it won’t fundamentally change anything. The survey comments read like a cry for help, and I’ve been there myself. It sucks and the pain is real.


# Standards…Who Needs Them?


Here’s the part of the data I want every leader reading this to look at twice.


Teams with formal, enforced modeling standards report that their models hold up wellroughly five times as often as teams with looseor no standards. Five times.


The cost of standards is a few meetings, some written documents, and clarity. That’s cheaper than firefighting. Or, do what most teams do and avoid standards, raw dog your data modeling and architecture, and do lots of wasted motion on unnecessary heroics. The winning teams invest in standards because somebody decided to care, writes it down, and got everyone else to follow it.


One respondent described what this looks like in practice. I’ll quote it in full because it’s the closest thing to a how-to in the entire dataset:


> Having clear modelling standards from the start of shifting to the cloud a few years ago, a solid conceptual data model as a planning basis for all new models, concerted knowledge sharing of good modelling practices, and documentation side by side with the code (ie. dbt yml files), and decent review process has meant our marts have been really solid and re-usable for many different purposes. Has saved us a ton of time in the long run and is leading to significant increase in trust from the rest of the business.


Standards. Conceptual model. Docs next to code. Review process. Trust.


Nothing in that paragraph requires a new platform or tool. But if this well-oiled machine of a data team invests in tools, I’m willing to bet they’ll execute infinitely better than the sloppy team with the best tools in the world, but winging it as they go along. This is the equivalent of an untrained runner buying fancy sub-2 hour marathon shoes, expecting to be a professional runner. The hard work is the hard work. Period.


# AI Makes You Go Faster. This is Good and Bad.


Here’s where AI comes in, and where I’m going to annoy half my readers.


The January survey found 82% of practitioners use AI tools daily or more often. The cat’s out of the bag. AI is here, and the question of whether to use it is settled. To me, AI is the boring part now.


The question thatisn’tsettled is what happens when you point AI at a broken foundation. But I think we’re starting to understand what happens, and it’s the same old story we’ve seen in past hype cycles.


In my Stockholm talk at Data Innovation Summit last week I put it this way:AI amplifies what you know about and what you’re good at. AI also amplifies what you don’t know about and what you’re bad at.There’s no free lunch. The teams that have done the modeling work, that have an owner, that have standards, AI makes them dramatically faster. The teams that haven’t, AI helps them generate broken systems at a velocity their previous tooling could only dream of.


Speed works if you know how to maneuver. Speed works against you when you don’t know what you’re doing. Speed kills if you’re acting like an amateur. But you’re a professional, right?


The April survey caught both camps on the record. The pessimists:


> Data modelling was being neglected at the best of times. AI will only accelerate that unfortunately.


The optimists:


> We are pitching a data model to staff this week, and our biggest selling point is getting a semantic model for AI tooling.


Both camps are correct. The same forcing function pushing leadership to skip modeling is the one that’s going to make them regret it. Whichever camp wins the argument inside your org over the next twelve months will determine where you’re standing in three years.


# AI is Here. The Hard Parts Remain.


If you’re a leader, the call is simpler than any vendor deck will let it sound.Name an owner. Give them air cover. Fund the standards work. Make the time.That’s the whole playbook. It costs you a meeting and a job description.


If you’re a practitioner, the survey is your permission slip. 334 of your peers said the same thing. The data is public, which you can find in thisthe writeup. Forward it.


If you’re a vendor (and I love you, I really do, several of you sponsor this newsletter) the 4.8% number is going to inform every conversation I have with you this year. If your product genuinely accelerates training, process, or ownership, you have a story to tell that will measurably help data teams. I’m happy to work with vendors to sanity check their product and positioning. Space is very limited, so message me for information.


TL;DR: AI is here and not the interesting story anymore. The interesting story is whether the field decides to invest in the things the data clearly shows are important to make a real impact for data teams: ownership, time, support, and upskilling.


That’s your move.


Have a great weekend,


Joe


---


Here’s this week’s Freestyle Friday podcast. Available on Spotify, Apple, and wherever else you get your podcasts.


Please support the show with a review.It means a lot.


---


# Awesome Upcoming Events


Here are a couple of things I’m up to. Taking the Summer off (might be in Australia), and launching the new business. Stay tuned for lots of announcements around that (and the book).


---


![](https://substackcdn.com/image/fetch/$s_!Jene!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5d6df69-f48c-499c-8332-259705bbccfa_430x90.png)


London! I’ll be at Confluent Current London. See you there!


When: May 19 to 20


Where: Excel London


Register here.


---


Detroit! I’m in town May 21 and 22. Catch me at the Data in the D Meetup. I’m also around for the Movement Music Festival over the weekend.Register here.


---


# Cool Videos and Reads


Are AI agents silently draining your cloud data budget? With the rise of consumption-based pricing and autonomous AI queries, data teams are facing a perfect storm of skyrocketing costs and operational chaos. In this episode, I sit down with Sanjay Agrawal, CEO and Co-founder of Revefi, to discuss the intersection of data engineering, cloud warehouse optimization, and FinOps in the age of AI.We chat about how legacy on-prem habits are bankrupting modern data platforms, why query optimization is more about ROI than just speed, and how AI agents are changing the landscape of data consumption.Sanjay shares his deep expertise from building world-class databases at Microsoft and ThoughtSpot, revealing how to automate cost management and performance tuning for Snowflake, Databricks, and BigQuery.


---


### Here are some things I read this week that you might enjoy.


Im going back to writing code by hand | k10s devlog


April 2026 PDC State of Data Modeling Survey Results Are In!


Three AI principles every exec leader needs to understand


The slop cannons in your engineering orgIC work is the new career flex - by Elena Verna


Amazon workers are under pressure to up their AI usage—so they’re making up extraneous tasks


Reluctantly Influential: Inside Lenny Rachitsky’s Demandingly Chill Life


# Find My Other Content Here


📺YouTube- Interviews, tutorials, product reviews, rants, and more.


🎙️Podcasts- Listen on Spotify or wherever you get your podcasts


📝Practical Data Modeling- This is where I’m writing my upcoming book, Mixed Model Arts, mostly in public. Free and paid content.


If you’re interested in sponsoring my newsletter and podcast, H2 2026 is opening up. Please message me for details.


# The Practical Data Community


The Practical Data Community is a place for candid, vendor-free conversations about all things tech, data, and AI. We host regular events such as book clubs, lunch-and-learns, Data Therapy, and more.


🤖Join on Discord


Thanks for reading! Subscribe for free to receive new posts and support my work.
