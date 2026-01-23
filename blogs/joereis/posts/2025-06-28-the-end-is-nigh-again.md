---
title: "The End is Nigh (Again)"
subtitle: "Joe's Nerdy Rants #83 - Weekend reads, podcasts, and other stuff"
date: 2025-06-28T17:55:05+00:00
url: https://joereis.substack.com/p/the-end-is-nigh-again
slug: the-end-is-nigh-again
word_count: 1896
---


![Predictions – After Christ®](https://substackcdn.com/image/fetch/$s_!1zSm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F123f262c-573f-4d64-ae43-ed5d0a998ba9_1200x686.jpeg)

0:00
-16:15

It’s that time again in the zeitgeist where the end is nigh for programming languages and practices. The last couple of months have felt like a coordinated campaign to declare things like SQL, R, data engineering, BI, analytics, and more as dead or obsolete. Why now? Maybe it’s the changing of the seasons. Maybe it’s the uncertainty about what AI does to our field and tools. Or perhaps we’re once again trapped in the echo chamber of a hype cycle, where people start confusing “what’s hot” with “what matters.”


Whether someone is pushing an agenda or simply lacks a sense of history, the outcome is the same. Long-standing tools and roles are suddenly useless in an AI-first world. I’ve seen this before. During the last machine learning and data science craze in the 2010s, I’d constantly hear that data warehousing, BI, SQL, and analytics were dead. Never mind that in 2025, all of these are more popular than ever. The “death of X” arguments are mostly superficial and miss a deeper truth. While technologies and job titles evolve, the fundamentals remain and become increasingly ingrained in our everyday lives.


There are two buckets into which these “death of X” arguments fall: technology and roles. Let’s look at these two buckets of bad takes.


1. The Technology Is Old, Therefore It’s Dead.


This is the classic mistake of confusing “new” with “better,” and “old” with “obsolete.” Here are some examples of things written off as dead that are still very much alive.

- Mainframes continue to run critical systems worldwide, powering many large companies. Sales of mainframes are$2.7 billion in 2024, with total salesgrowingat 6.11% CAGR. The ancient COBOL language still powers many of these mainframes.
- Although data lakehouses are the rage, Hive Metastore still underpins many data stacks.
- SQL interfaces with virtually every data system on earth. SQLite alone claims to have over1 trillion databasesin active use. There are billions of other varieties of RDBMS in active use worldwide. Since SQL is how we interface with these databases, the claim that SQL is dead is preposterous.
- R isn’t irrelevant, and is still one of the best out-of-the-box statistical languages. If I need a “hand calculator for stats”, I’m using R.


The reality is that we often radically underestimate the cost and pain of replacing what already works. The newer something is, the less likely it is to have been battle-tested. Stability isn’t sexy, but it’s sticky. As the saying goes, “Legacy is a condescending term for things that make money.”


2. The Role Is Dead, So the Fundamentals Must Be Too.


This one’s trickier. It assumes that if a role, say, “data engineer”, changes or disappears, then the underlying work must vanish with it. But that’s just not how the world works.


Let’s take a topic near and dear to me - data engineering. When Matt Housley and I wrote the Fundamentals of Data Engineering, we were doing so from a place of dissatisfaction with how data engineering was typically described. The practice of data engineering was often equated with tools, and we’d read malarky like “data engineering is the use of Spark, Pig, and MapReduce”, or “data engineers build pipelines and transform data.” Neither of these explanations describes a field per se, but rather the tools people use and the activities they perform. But don’t confuse tools and activities with the field itself. These are not the same. It’s like saying medicine is about prescribing medications and doing surgery, or carpentry is about swinging a hammer and drilling holes with a DeWalt power drill. Sadly, many people take a superficial view of data engineering and other fields, struggling to tell the difference. Oh well.


The goal of our book was to establish data engineering from first principles. We developed with the data engineering lifecycle and its undercurrents. Data is ingested from source systems, stored and transformed, and served for downstream use cases like ML/AI, analytics, etc. Along the lifecycle sit the undercurrents - security, data management, DataOps, orchestration, architecture, and software engineering. The data engineering lifecycle is tool-agnostic and robust, whether humans or machines operate within this framework. The management of this lifecycle is the heart of data engineering.


As a term, data engineering has been in use for a long time. The term first surfaced (to my knowledge) in 1984 at theIEEE First International Conference on Data Engineering. It appeared in various articles throughout the 1980s to the present, evolving into titles such as ETL developer, BI Engineer, and Big Data Engineer.


Now, AI is helping to automate parts of the data engineering lifecycle. We’ve AI agent workflows, MCP integrations, and more. Who knows what else is coming, but the new crop of AI tools are pretty cool. Regardless of the AI tooling, the data engineering lifecycle and its undercurrents will still exist. Whether a person or AI builds and maintains things, we’ll still need pipelines, models, data quality checks, security, governance, and transformation logic.


Which brings me to the stickiness of fundamentals. My good friend and “big bro” Bill Inmon (who I can strongly argue is one of the godfathers of the modern data industry) once told me that “fundamentals are gravity.” You can try to escape the fundamentals with new tools and hype cycles, but ultimately, they will not change the core principles. Ultimately, everything conforms to the fundamentals.


There’s a concept called theLindy Effect, which states that the longer something has been around, the more likely it is to persist. SQL is Lindy. Data modeling is Lindy. Data engineering is Lindy. AI might reshape how we do those things, but it won’t erase the need for doing them in the first place.


There IS a possible flip side with AI. If AI does build novel architectures for itself, it probably won’t use SQL or columnar data formats or even human-centric tools at all. I imagine it would create some semantic, real-time, graph-based knowledge substrate optimized for non-human consumption. But that’s not our world. That’s AI’s world. And we’re not the users or maintainers of that world. At that point, perhaps things truly change. I’m open to this possibility.


Until then, we’re still the ones writing, shipping, and maintaining the systems that matter for humans.


This won’t be the last time people declare things to be dead. During the next hype cycle (whatever that is), people will get overly excited and put a nail in the coffin of whatever “legacy” tools and practices they choose. SQL will undoubtedly be on the list.


To be clear, I’m not anti-AI. Quite the opposite. Every day, I chat with my AIs and code with them. I’m building my new business with AI. The AI models are awesome and constantly improving. I’m excited for what it can unlock. However, I also have a long memory and have devoted a significant amount of time to understanding the history of our field and craft. I know how long things stick around, how hard they are to replace, and why the fundamentals of our craft will outlast the noise.


The end has been nigh for many decades. Yet somehow, we’re still here.


Please listen to the audio above or onSpotify(or your podcast platform of choice).


Also, I will be publishing this newsletter more sporadically in July through September. It won’t be on a weekly cadence during this time. I’m heads down and finishing my book. Therefore, any writing I do right now needs to be related to the book. You can see the progress atPractical Data Modeling, where I publish drafts of sections and chapters. That said, if I have a rant or a hot take, I’ll publish it here. My podcast will still be published on a regular cadence.


Have a wonderful weekend,


Joe


---


### Is your data stack too complex and expensive?


Stop juggling 10+ tools for extraction, transformation, and storage.Keboolais the all-in-one data operations platform that replaces your entire brittle stack. Connect to 700+ sources, transform with SQL or Python, and load to Snowflake or BigQuery in one place.


Now with the newKeboola MCP Server, their AI assistant can understand your data and build real infrastructure, not just code snippets. It's AI that knows your business, on a platform built for production.Check out Keboola's MCP Server


Thanks toKeboolafor sponsoring this newsletter.


---


# Cool Weekend Reads


Here are some cool articles I read this week. Enjoy!


The Computer-Science Bubble Is Bursting


What If we're overthinking Data Products? - by Ash Smith


AI Beyond The Hype - With Joe Reis@Databricks Data + AI Summit 2025


Nearly Headless BI


The Uncomfortable Truth About Data Engineering Tool Choices (That Vendors Won’t Tell You) | by Sohail Saifi


Build and Host AI-Powered Apps with Claude - No Deployment Needed \ Anthropic


How to Vibe Code as a Senior Engineer


Ticket-Driven Development: The Fastest Way to Go Nowhere


---


Australia (Sydney, Melbourne) - Data Eng Bytes, July 24-30.Register here


US Tour - September TBA


UK - Big Data London, September 24-25.Register here


Fall US and European Tour - TBA


More to be announced soon…


---


# Podcasts


Freestyle Fridays - The End is Nigh (Again) (Spotify)


Definitive Python Polars with Jeroen Janssens and Thijs Nieuwdorp (Spotify,YouTube)


Freestyle Fridays - Small is the New Big, AI Native Data Architectures, and More (Spotify)


Gordon Wong - The Impact of AI on Attention and Expertise, Platform Wars, and More (Spotify,YouTube)


Freestyle Fridays - Next-Generation Data Architectures. Ramblings and Musings (Spotify)


Zhamak Dehghani - Autonomous Data Products, Decentralized Data and AI, and More (Spotify,YouTube)


Matthew Scullion - The Agentic Data Engineering Team  (Spotify,YouTube)


Freestyle Fridays - Platform or Predator? (Spotify)


Svetlana Tarnagurskaja - Building a Boutique Data Consultancy (Spotify,YouTube)


DuckLake w/ Hannes Mühleisen - Practical Data Lunch and Learn. June 4, 2025 (Spotify,YouTube)


Ash Smith - Data Products, Interoperability, Data Teams, and More (Spotify,YouTube)


Freestyle Fridays - So You Want to Work in Data? w/ Gordon Wong (Spotify)


Hamilton Ulmer - Instant SQL with DuckDB/MotherDuck - Practical Data Lunch and Learn (Spotify)


Gaëlle Seret - Change Management in Large Organizations (Spotify)


There are way more episodes over at the Joe Reis Show, available onSpotify,Apple Podcasts, or wherever you get your podcasts. Also available onYouTube.


---


# Thanks! If you want to support this newsletter

- The Data Engineering Professional Certificate is one of the most popular courses on Coursera! Learn practical data engineering with lots of challenging hands-on examples. Shoutout to the fantastic people at Deeplearning.ai and AWS, who helped make this a reality over the last year. Enrollhere.
- Practical Data Modeling. Great discussions about data modeling with data practitioners. This is also where early drafts of my new data modeling book will be published.
- Fundamentals of Data Engineering by Matt Housley and I, available atAmazon,O’Reilly, and wherever you get your books.
- The Data Therapy Session calendar is postedhere. It’s an incredible group where you can share your experiences with data, good and bad, in a judgment-free place with other data professionals. If you’re interested in regularly attending, add it to your calendar.
- My other show is The Joe Reis Show (Spotifyand wherever you get your podcasts). I interview guests on it, and it’s unscripted, always fun, and free of shilling.


Thanks!


Joe Reis


Thanks for reading Joe’s Nerdy Rants! Subscribe for free to receive new posts and support my work.
