---
title: "A Diary of a Data Engineer"
date: 2026-01-13
url: https://www.ssp.sh/blog/diary-of-a-data-engineer/
slug: diary-of-a-data-engineer
word_count: 2886
---

![A Diary of a Data Engineer](https://www.ssp.sh/blog/diary-of-a-data-engineer/featured-image.jpg)

Contents

You ingest data. You model it. You transform it. You serve it. Someone asks for a change. Everything breaks. You rebuild. This is the loop. It was the loop in 2005 with SSIS and star schemas. It’s the loop in 2025 with dbt and Iceberg, or 2026 with prompting AI agents.


The tools change. The loop doesn’t.


## The Invisible Plumbers


When I started my career in 2003, there was no “data engineering”. There was no big data, no data science. We called it Business Intelligence. Data Warehouse Developer. ETL Developer.


We were the plumbers of the organization. And like plumbers, nobody noticed us until something broke.


Being a data engineer means: you’re building the foundation that everyone stands on, but when the presentation goes well, the data scientist, the app developer, anyone who presents gets the applause. When the executive makes the right decision, the analyst gets the credit. When the dashboard loads in 1 second instead of 20, nobody says anything at all.


But when one number is wrong? When a pipeline is 10 minutes late? When someone asks for “a small change” and you explain it’ll take a day, or a week to fix it?


That’s when everyone notices you. And shares their opinion on how to make it better.


“Why does this take so long? It’s just one column. Why isn’t it real-time?”


They don’t see the 147 downstream dependencies. The three systems that need a fuzzy-logic join. Or the security measures that go through three different subnetworks. The backfill that’ll take 6 hours to run. The schema that hasn’t been touched since 2021 because the last person who understood it left the company long ago.


This is the paradox of data engineering: when you do your job, you’re invisible. When anything goes wrong, you’re under a microscope.


## The Epochs: A 50-Year Journey


To understand where we are today, you need to understand where we came from.


### 1970s: The Beginning


Edgar F. Codd proposed [SQL](https://ssp.sh/brain/sql/) in 1970. A way to abstract the complexities of data storage. By the 1980s, it became the standard. IBM built System R. Oracle launched their RDBMS in 1979.


The foundation was laid. But nobody called it “data engineering” yet.


### 1980s-1990s: The Warehouse Era


[Bill Inmon](https://ssp.sh/brain/bill-inmon/) formalized data warehousing principles in the 1980s. Many call him the father of data warehousing. Then in 1996, Ralph Kimball published “[The Data Warehouse Toolkit](https://ssp.sh/brain/the-data-warehouse-toolkit-ralph-kimball/)” and gifted us with [dimensional modeling](https://ssp.sh/brain/dimensional-modeling/)—star schemas, fact tables, slowly changing dimensions.


These concepts? They’re still relevant today.


### 2000s: When “Big” Changed Everything


The dot-com bubble burst. Tech titans were born such as Google, Amazon, Yahoo, hitting walls their databases couldn’t scale past.


So Google released two [groundbreaking papers](https://ssp.sh/brain/data-engineering-whitepapers/): the Google File System in 2003, MapReduce in 2004. Yahoo responded with Hadoop in 2006. Hardware prices plummeted.


Suddenly, we weren’t just BI engineers anymore. We were “**Big Data Engineers**”. We had to know traditional relational databases AND the new open-source filesystems. The skillset kept expanding—from data modeling to software development to mastering Hive and Spark, all coordinated with R and Python.


The term “big” was everywhere. But how big is “big”? Nobody really knew. We just knew the old ways weren’t working anymore. And Facebook and co showed us the way.


### 2010s: The Cloud Changes the Game


Amazon announced AWS. Google Cloud and Azure followed. Companies no longer needed to own hardware. The flexibility was unprecedented, and we could get any DWH on demand.


Redshift. Snowflake. And then the open-source wave hit:

- Airflow for orchestration (2014)
- Superset for visualization (2015)
- dbt for transformation (2016)


And in 2017, Maxime Beauchemin—after creating both Airflow and Superset—published “[The Rise of the Data Engineer](https://medium.com/free-code-camp/the-rise-of-the-data-engineer-91be18f1e603)”. He defined, for the first time, what data engineering actually meant. He explained the shift from business intelligence to data engineering.


I remember releasing my first viral article in March 2018: “[Data Engineering, the future of Data Warehousing?](https://www.ssp.sh/blog/data-engineering-the-future-of-data-warehousing/)” It got 200 likes. Back then, that was a lot ð.


Since then? New technologies appeared weekly. The [Modern Data Stack](https://ssp.sh/brain/modern-data-stack/) was born.


### 2020s: DevOps Meets Data Engineering


This is where it gets interesting.


Data engineering isn’t just about moving data anymore. It’s about **infrastructure as code**, version control for data, CI/CD pipelines, Kubernetes, Docker, and Terraform.


The skills needed have exploded. You need to know:

- SQL (still the foundation)
- Python or Scala
- Cloud infrastructure (AWS/GCP/Azure)
- Linux and bash scripting
- Git for version control
- Data modeling (the lost art)
- Business logic (the most important)


DevOps principles are now [table stakes](https://ssp.sh/brain/the-state-of-devops-in-data-engineering/). You’re not just building pipelines. You’re building systems that need to self-heal, auto-scale, and deploy without downtime on any environment.


And today? AI agents? They’re the latest chapter. But under all the hype is the same eternal truth: **you need fresh, organized, clean data.**


## The Eternal Loop: Same Problems, New Tools


Here’s the uncomfortable truth: we’ve been solving the same problems for 50 years.


In 2005, we had SSIS and star schemas. “The cube is rebuilding” was the pain point.


In 2015, we had Hadoop and Spark. “The cluster is full” was the nightmare.


In 2025, we have dbt and Snowflake. “The bill is how much?” is the new horror story.


The tools change. The problems don’t.


Last month I analyzed a 200-line dbt model as part of a larger GitHub repository. You know what it was doing? Exactly what we did in 2005 with stored procedures. Same business logic. Different syntax. I laughed. Then I cried a little. (just kidding, I didn’t ð)


An old data warehouse architect from 2003 once drew a star schema on a whiteboard in 40 seconds. It would take my team three sprints to model in Oracle Warehouse Builder (OWB). He said, “We called it just another day at the office”.


We’re not really any smarter than the people before us. We just have better marketing ð.


## What Actually Matters (And What Doesn’t)


Here’s what I’ve learned after 20+ years.


### The Excel File That Saved Me


I was in a coffee meeting with a finance analyst—call her Maria. Fifteen years at the company. She opened her laptop and showed me an Excel file (sometimes it was Microsoft Access DB with a custom UI!).


Forty-seven tabs. Formulas referencing other files on a shared drive. VBA macros from 2012. VLOOKUP nested inside SUMIF.


“This is how we calculate the quarterly forecast”.


From my perspective of making it available to everyone and needing to understand it, I was a little shocked. I’d spent three weeks reverse-engineering the business logic, trying to understand it, trying to recreate it in SQL Server, and adding it to our data warehouse. But the numbers were never the same, close most of the time.


After having multiple such experiences, sometimes Microsoft Access databases with custom UI built in (!!!), I learned something. Though my initial reaction was shock and horror, I learned that **Excel isn’t the enemy**. Excel is the **business telling you what they actually need**.


When someone asks to export to Excel, they’re not rejecting your work. They’re telling you something. Maybe your dashboard is too slow. Maybe they need to add a column you didn’t think of. Maybe they just need to feel in control of their analysis.


Power users will overengineer everything, but ask them for the Excel file and you might get validated business logic and ETL code for free. Win-win.


### The Real-Time Lie


Everyone wants real-time. “We need to see this data instantly”, they say. “For decision-making”.


I always ask: “What decision will you make differently if you see it 10 minutes sooner?”


Most of the time, they can’t answer. There’s a small percentage that needs it: air traffic control, fraud detection, Black Friday e-commerce. But the rest? They just think real-time serves them better.


Real-time adds a much higher complexity. Harder debugging. Harder backfills. Harder historization. The question is, for what? So someone can watch a number update every 30 seconds instead of every hour?


Push back on “real-time”. Start with hourly refreshes. It’s almost always enough.


### The Schema Change: A People Problem


They said it was small. Just renaming `user_id` to `customer_id`.


You trace the lineage. 147 downstream dependencies. Three teams. One undocumented view from 2019 that somehow powers the CEO’s dashboard.


That’s when you realize: **schema changes are usually people problems**, not technology problems. The reason things break is when upstream producers don’t own responsibility for downstream analytics and don’t communicate the changes. There’s no process in place. Just assumptions.


Fix the people process first, then update the code.


## The Lost Art of Data Modeling


Max Beauchemin once [said](https://www.heavybit.com/library/podcasts/data-renegades/ep-3-building-tools-that-shape-data-with-maxime-beauchemin) in an interview: “I like the analysis side. I think I’m a good data modeler. It’s kind of a lost art, so I still do a lot of our data pipelines”.


He’s right.


After years of “just dump it in the data lake”, people are rediscovering that structure matters. Data modeling forces you to think about:

- **[Grain](https://ssp.sh/brain/granularity/)**: What’s the lowest level of detail we need for this data?
- **[Relationships](https://ssp.sh/brain/entity-relationship-diagram-erd/)**: How do these entities connect?
- **[What the business needs](https://ssp.sh/brain/the-goal-of-business-intelligence/)**: What user insights they cannot know today, but lie in the source system provided, or combined with other data sources.


It’s the difference between a data warehouse and a data dump.


But here’s the thing: I believe AI will bring us back to the fundamentals. When AI-generated code breaks and you’re out of context, what then? That’s where the fundamentals save you. Data modeling. Understanding the grain. Knowing SQL deeply, not superficially1.


Someone needs to understand and refactor generated code. Someone needs to simplify. That someone is you.


## The Lost Code We Inherit


You’ll inherit code from someone who left. Everyone does.


I once found a DAG called `final_v3_FIXED_REAL_FINAL.py`. Inside was a comment:



| `1
` | `# Mike: I don't know why this works. Just leave it
` |



Mike was right. I left it.


**The biggest pitfall?** Trying to recreate everything to your taste. Accept the legacy. Adapt or improve one thing at a time. The motto “Don’t touch what works today” really applies to legacy code most often.


Usually, the previous engineer wasn’t naive or stupid. They were solving different problems with different constraints. Your job isn’t to make it beautiful (sometimes it helps!). Your job is to keep it running while slowly making it better over time.


## The Books That Actually Matter


As the cycles come and go, these books helped me throughout the cycle2, and can be applied to this day.


**[Designing Data-Intensive Applications](https://unidel.edu.ng/focelibrary/books/Designing%20Data-Intensive%20Applications%20The%20Big%20Ideas%20Behind%20Reliable,%20Scalable,%20and%20Maintainable%20Systems%20by%20Martin%20Kleppmann%20%28z-lib.org%29.pdf)** by Martin Kleppmann about distributed systems and how to build them. Wait a little, version two is just around the corner.


**[The Data Warehouse Toolkit](https://ssp.sh/brain/the-data-warehouse-toolkit-ralph-kimball/)** by Ralph Kimball. Someone in 2045 will still need to understand fact tables and dimensional tables.


**[Fundamentals of Data Engineering](https://www.amazon.com/Fundamentals-Data-Engineering-Robust-Systems/dp/1098108302)** by Joe Reis and Matt Housley. A great start to know about all the concepts and principles you hear everywhere, including in this article.


**[Data Engineering Design Patterns (DEDP)](https://dedp.online/)** by me. If you want, you can also read my unfinished online book, which starts with the state of the art, the history and key [convergent evolution in data engineering](https://dedp.online/part-1/2-overview-dedp/understanding-convergent-evolution.html), about the ever-returning cycle we talk about here, and explains them with higher-level patterns.


The first two books don’t mention Snowflake, Lakehouse or dbt. They mention problems that existed in 1995 and will exist in 2045. That’s the Lindy Effect, and how you know they’re worth reading.


## What I Know Now That I Wish I Knew Then


If I could go back to 2003 and talk to my younger self, here’s what I might say. Boy:


**1. The tools will change. The fundamentals won’t.**


Stop chasing every new framework. Learn [data modeling](https://ssp.sh/brain/data-modeling/). Learn how data is flowing. Learn SQL deeply, not superficially. Learn how humans make decisions. Everything else is syntax.


In 2026, AI helps us write code faster. But someone still needs to understand the fundamentals, the [Data Engineering Lifecycle](https://ssp.sh/brain/data-engineering-lifecycle/). That someone can be you.


**2. Talk to the business people.**


This is a crucial lesson in my journey. What you’ll learn from them will make you inevitably a better data engineer. Technical skills can be learned, outsourced, automated. Knowledge about the business is much harder.


The best data engineers aren’t the ones who know every new tool. They’re the ones who know *why* the data matters.


**3. You’re building the foundation, not the showcase.**


When the presentation goes well, the data scientist, the AI engineer gets the credits. When the executive makes the right decision, the analyst gets credit. When the dashboard loads fast, nobody says anything.


But when one number is wrong? Everyone sees you.


Accept this. You’re a plumber. Be the **best plumber in the world** and make sure nobody ever thinks about the pipes.


**4. Data quality is learned through pain.**


You can’t understand data quality from a textbook. You need to see bad data. If you start looking, it won’t take long, and you’ll see really bad, production-breaking data. That will teach you what good data looks like.


And you’ll only get faster by talking to the people who use it.


**5. Presentation matters more than you think.**


No matter how fancy your pipeline, how elegant your code, how profound your insights—if the presentation isn’t right or the data quality is terrible, no one cares.


Throughout my career, presenting data understandably has been as important as building the pipeline. That’s why these days, I focus on the [storyline and craft](https://craft.ssp.sh/) extensively.


**6. Set boundaries early.**


This job will take everything you give it. The people who succeed aren’t the ones who work 80-hour weeks. Sure, in the beginning you need it here and there too. But over time, you need to learn to [say no](https://ssp.sh/brain/hell-yeah-or-no/). Document things so you can take vacation. Build systems that don’t require you to be online at 3 AM.


Future you will thank you.


**7. Don’t chase every trend.**


Data engineering is still going strong. Stronger than ever. AI won’t take our jobs any time soon. The opposite is true. There will be more chaos, and people who know how to model data, understand business requirements, and deliver high-quality insights will always be needed.


Plus, every AI solution out there needs data, a lot of data, and probably a plumber to fix the pipeline too. Use the knowledge of past years building data pipelines. We don’t need to rebuild everything every 5 years.


## The Loop Continues


It’s 2026. I’m building a pipeline with DuckDB and Rill. The business wants faster dashboards and better insights. They want to edit data themselves. They want to use an AI chatbot. Or sometimes they just rename a column in the source system without telling anyone.


Here we go again.


But here’s the thing: I still love it. Especially when I can write about the learnings.


I don’t miss the late nights or the schema changes or the never-ending rewrites. I love the moment when you finally get the data right and someone in finance sees something they’ve never seen before. When a dashboard actually changes a decision. When the CEO asks a question and you can answer it with data.


That’s the job. Not the tools. Not the frameworks. Not the buzzwords.


The moment when data helps a human make a better decision.


## The Final Truth


The tools will change. The vendors will rise and fall. Snowflake will be replaced by something else. The latest new shiny tool will become the legacy tomorrow. AI agents will be the next big thing, and then something after that.


But someone, somewhere, will always need to:

- Understand the grain of a business
- Know why the numbers don’t match
- Explain to the CEO that the data they want doesn’t exist yet
- Debug why a pipeline broke at 2 AM
- Figure out why production data looks different from dev data


That someone is you.


You’re the invisible plumber. The unsung engineer. The person who makes sure the foundation doesn’t crumble while everyone else builds on [top of it](https://xkcd.com/2347/).


And honestly? It’s a pretty damn good job if you like to work quietly, helping a large part of the business.


Because 50 years from now, when we’re using tools we can’t even imagine today, someone will still be ingesting data, modeling it, transforming it, serving it. Someone will ask for a change. Something will break.


The loop continues. The problems remain. Only the tools change.


And that’s okay. Isn’t that somehow beautiful? Because beneath all the hype, all the new frameworks, all the promises of “this time it’s different”—there’s you, the data engineer ð. Understanding the data. Knowing the business. Building the foundation.


That’s *[Data Engineering](https://ssp.sh/brain/data-engineering/)*.

Inspiration

*This piece was inspired by the confessional storytelling style of [Diary of a CEO](https://www.youtube.com/@TheDiaryOfACEO). If you enjoyed this format applied to data engineering, let me know—I’d love to hear your own stories from the field.*


---

1. I wrote more at [Will AI Replace Human Thinking](https://ssp.sh/brain/will-ai-replace-humans/) ↩︎
2. I collect [Books of Data Engineering](https://ssp.sh/brain/books-of-data-engineering/) at my data engineering brain, find more interesting once there too. ↩︎

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/diary-of-a-data-engineer/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Dataengineer](https://www.ssp.sh/tags/dataengineer/)
[Data Architecture](https://www.ssp.sh/tags/data-architecture/)
[Data Modeling](https://www.ssp.sh/tags/data-modeling/)
[Career](https://www.ssp.sh/tags/career/)
[Devops](https://www.ssp.sh/tags/devops/)
