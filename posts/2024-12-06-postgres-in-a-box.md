---
title: "Postgres in a box"
subtitle: "The next big thing."
date: 2024-12-06T18:17:36+00:00
url: https://benn.substack.com/p/postgres-in-a-box
slug: postgres-in-a-box
word_count: 3550
---


![](https://substackcdn.com/image/fetch/$s_!cS_v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaa7f23d-76db-459c-812a-f1408660f808_612x367.png)


Sometime between now and, I don’t know, 2027, someone is going to go on stage at aY Combinator demo dayand pitch a company that sells copies of Postgres in a box.


I mean, no, they won't literally pitch that. Postgres is an open-source database; it is 28 years old; it is free. And nobody sells software in little cardboard boxes anymore, unless you're doing amarketing stuntforgeriatric millennials.


Because weusedto sell software in boxes. In 1998, if you wanted the new version ofStarCraft—or, like,Microsoft Access 97, but I did not want that when I was 12—you went to CompUSA and bought a seemingly empty cereal box for $49.99.1Then you went home, spent a couple hours trying to install the game on your Gateway 2000 cow computer, and played it until thecomputer imploded, or until IGN told you that there was anew expansion packthat you had to have. In the second case, you then went back to CompUSA; you bought another almost empty cardboard box for another $49.99, spent another three fraught hours installing the game, and then played the new version, until you got frustrated about losing,2or your parents told you that you were out of computer time, or whatever.


Companies did the exact same thing, but instead of buyingStarCraft, they boughtOracle 8i databases, paid $100,000 for them, andspent 13 yearsinstalling them. And if the upgrades broke, they didn’t lose their progress in a game; they lost their customers and their money and their jobs and sometimesgo to jail.3It was much more fraught, for them.


But the internet—the information superhighway, back then—started to change all that. Rather than buying their Oracle 8i databases from a software store, companies could buy alicensefor their databases. They would download the database from the internet; no CDs or boxes required. You still had to buy a new database whenOracle 9icame out though, and upgrades were still slow and difficult.


And then came the cloud and SaaS software.4Instead of buying a program, downloading it on your own computer, andrunning it into oblivion, you buy a subscription to use someone else’s computer. They run and update the software, and you pay them a recurring fee. Don’t install Excel; go to google dot sheets dot com,5and Google will run it Excel-ish for you.


By 2012, you could do the same thing for your database. That year, Amazonreleased Redshift, the first major SaaS database. You bought a subscription to Redshift, paid a monthly fee based on database specs you wanted, and Amazon would run it for you, on their computers, on your behalf. And when Amazon released a new version of Redshift, they would give you the upgrade automatically, without you having to do or pay anything.


This was much better than CompUSA! Not only was it much less of a hassle to manage, it was also ostensibly cheaper. You didn’t have to buy a bunch of IBM servers to run it on. You didn’t have to pay a big upfront fee for new database versions. You just paid a flat monthly rate, and you got a ticket to an all-you-can-eat buffet at Amazon’s database bar.6


But this introduced some new problems. Back then, databases typically had two interlocking components—a big bucket that they stored data in, and a calculator that would perform computations on that data. Though running that calculator was expensive, storage was cheap (for example, you could buy a two-terabyte hard drive for about $100in 2012). However, when you rented a database from Amazon, the two were bundled; your bills were determined by how much data youput inyour database. If you had small data, you could rent a small Redshift database, and pay a small fee. But if you had Big Data—andwhat were you even doingif you didn’t have Big Data—you had to rent a Big Database, and pay a Big Fee. Wouldn’t it be better, we all thought, if you could store your data in one place, and then only pay for thesmall amounts of datathat youuse? That way, you could size each component separately: You could buy a big bucket for your big data, and a small calculator for your small calculations.


So that’s what databases did. They split themselves in half; they “separated storage from compute,” as the catchphrase goes. With databases like Snowflake, BigQuery, and Databricks, customers paid two fees: one (typically low) rate for how much data was in the database, and a metered charge for how many computations they asked the database to do on that data.


And thenallthedatabaseswent towar. The database market is a big one—Larry Ellison became thethird-richest person in the worldselling them—and everyone wanted their companies to become Oracle, so that they could become Larry Ellison. To make their database better than everyone else’s database, database vendors built a bunch of bells and whistles on top of their fancy calculators. Databricks could run Python. Snowflake uses AI.DuckDB is chillaboutcommas.7


Which created yet another new problem: What if a customer wantedmultiplecalculators? What if I want to use Python today, AI tomorrow, and be loose with commas on Friday nights? Though different vendors separate how they bill for storage and compute, you still have to buy them as a bundle. You can’t put your data in one place, and bring your favorite calculator to it.


Or, you couldn’t—but now that is changing too. Earlier this year, Databricksbought Tabular. Tabular was founded by the creators of Iceberg, which is an open-source standard for turning data in buckets into tables for calculators. The deal,according to Databricks, was about promoting “data interoperability:”


> This acquisition highlights our commitment to open formats and open source data in the cloud, helping ensure that companies are in control of their data and free from the lock-in created by proprietary vendor-owned formats.


In other words, if you store your data in a particular way—in this case, using Iceberg—you can put it in whatever bucket you want, and Databricks’ big calculator can read from it.8And two days ago,Amazon announcedthey would support the inverse: If you put your data in S3—a generic bucket for stuff, almost literally—they will automatically store it for you in the particular way that Databricks wants it:


> Amazon S3 Tables deliver the first cloud object store with built-in Apache Iceberg support, and the easiest way to store tabular data at scale. S3 Tables are specifically optimized for analytics workloads, resulting in up to 3x faster query throughput and up to 10x higher transactions per second compared to self-managed tables. With S3 Tables support for the Apache Iceberg standard, your tabular data can be easily queried by popular AWS and third-party query engines.


Which is, for Big Data, aBig Deal:


> Open data formats and data lakes have been all the rage over the past year. Many companies want to keep their data in their Cloud Storage provider [ like Amazon ] and make it accessible to multiple services/query engines [ like Databricks ].AWS coming out and adding first class support for Parquet/Iceberg will lay down the foundations for this trend to accelerate.


But why stop there? Tristan Handy, CEO of dbt Labs,says the stool needs more legs:


> Low-friction workload portability doesn’t happen automatically just because you have an open file format, table format, and metastore. From what I can tell, in order to make this a reality, you need:An ability to transpile workloads between execution engines’ dialects / environments with accuracy guarantees.An ability to route workloads automatically between multiple execution engines.An ability to decision which engine is best suited to execute a given workload.The platforms themselves have to have a minimum shared level of support for the various table formats and metastores, with appropriate performance characteristics.


That is—sure, while all of this Iceberg stuff is great, it’s not enough. The ideal database would not only separate buckets and calculators, but it would alsoseparate the calculators from the programs that people want to run on them.


Because, today, in order to use multiple calculators, you have to write programs in multiple languages. Every database engine has different APIs and uses a different variants of SQL, and all the queries and pipelines and applications built on that engine need to use that variant.9You can’t simply point a query that was originally written for Databricks at a Snowflake or a DuckDB engine, because there areverystupiddifferencesbetween allthreeof them.10Even if the calculators are interoperable with the buckets, the programs are not interoperable with the calculators.


So that seems like what’s next—dbt directly on top of S3, more or less. You write queries in one language, likedbt SQLorSDF SQL, and it gets rewritten in whatever version of SQL a specific execution engine prefers. The programs and pipelines people write would then be agnostic to the calculators underneath them—which would then, as Tristan proposes, make it possible for people to choose the right engine for the right job.


And then,then, we would have the ideal database.


Which, yes! Except:

1. It’s complicated? You have to have S3, for storage. You have to set up a half-dozen different database engines. You have to configure a compilation layer, like dbt orSDF. And you have to glue all these things together, and make sure nothing falls in between the cracks.
2. It’s hard to use? Not only do you have to manage a bunch of services, but they’re alsocloser to the metal. You can “install” databases like Redshift by mindlessly mashing “Next” on asetup wizard. To run this ideal database, you need to install homebrew; update homebrew; uninstall homebrew; reinstall homebrew; fix your Python environment; add your Github SSH keys to your ssh-agent; Google how to add your Github SSH keys to your ssh-agent; configure your AWS security groups to allow access from the right subnets; etc; etc; etc.
3. It’s expensive? Though you might save costs on individual services—you can optimize your queries to run on the cheapest engine—running a query now rings six cash registers rather than one. You pay S3 for storage, and somecryptic Amazon serviceto move data in and out of it; you pay Databricks to run Python and Snowflake to run an LLM; you pay dbt to compile a query. Your one database becomes a modern data stack of databases, in the worst way:A knot of intertwined and opaque costs.


For all of the nice things that this build-a-bear database can do, there’s a lot to sell against here. And if there’s something people don’t want, then there’s something elsepeople want, and an inevitable pitch to YC:


> Hi, I’m Taylor, and I’m the CEO of Databox, the all-in-one database platform. The modern enterprise needs data more than ever, but usingdata has never been harder. My founders and I have seen this problem firsthand—at Waterloo, where we both majored inSystem Design Engineering, and then when we worked on data engineering teams at Google, and Brex. We created Databox to build the database we always wanted: One where you can just upload your data to one platform, and it stores it for you, without you having to worry about which S3 bucket it’s in, or how to reformat your CSVs in Parquet. We abstract away all of that tedious complexity, and let our customers think about everything in Databox as “tables”—an intuitive new format of easily readable rows and columns that we open-sourced two weeks ago, and already has 400 stars on GitHub.Once your data is in Databox, you can interact with it using one unified language, which we call the Proprietary Operating System Transpiler, which Generalizes Really Every Single Query Language, or PostgreSQL. Databox will automatically optimize your PostgreSQL queries by choosing the best engine for each of them, without you having to configure anything.Finally, the only thing harder than using today’s databases is figuring out how much they cost. Which is why we are launching with a revolutionary billing plan: We bill you once, for a perpetual lifetime license, and you can use Databox as much as you want, for as long as you want. No variable costs; no surprise charges. The only time we’ll ever ask for more money is if you want to upgrade your Databox account to include our latest features.I’m Taylor, and we’re reinventing the database. And this…is Databox.


I mean, ok, it’s not Postgres in a box. But isn’t it?


---


# Postgres in a Box


Speaking of, this week, Aaron Levie launched Postgres in a Box, butcalled it Box AI:


> The vast majority of an enterprise’s data is unstructured data, with enterprise content being the most significant portion of this. Some of the world’s most important IP lives inside of this content — our contracts, financial documents, digital assets, movie scripts, R&D files, product specs, HR documents, and more. …However, the majority of this content has tremendous amounts of untapped value for most organizations. For all of our *structured* data that lives inside of a database, we can query this information easily, summarize it, analyze it, pull out insights, and more. But for all of our unstructured data, this has been nearly impossible. In fact, in many cases the more content we have the harder it is to work with and less valuable it becomes.In this new era of AI, this all is reversed. What if you could ask all your content any question you want, or automate any of the workflow instantly. All new ways of working with information become possible: “What’s our best performing product line?”, “How many contracts have risky terms in them?”, “Which clients do we have promotional rights to?”, “Show me all my open invoices”. All of a sudden, the more information we have the more valuable it becomes. We can innovate more and accelerate progress.Now, enterprises are still in the earliest stages of beginning to leverage AI on their unstructured data, but with Box AI we’re building the platform to make this easy, secure, and scalable for any use-case. And we’re doing so with an open approach, to bring the power of any AI model into Box AI so customers can leverage whatever works best. That’s the power of intelligent content management from Box.


We’vetalkedaboutthisalot: When we think about the difference between structured spreadsheets of numbers and loose PDFs of sales call transcripts, we often act as though the former has inherently more validity than the latter. It is math; it is science; it is “statistically significant.” Interviews and conversations and product specs are anecdotes, corrupted by emotions and biases.


As Levie implies, that might not be the right distinction to make. Data is still downstream of emotions and biases; a quantitative survey of 10,000 people isno less corruptiblethan a qualitative interview panel of 10 people. The difference between the two is that, when the data is numbers, “we can query this information easily, summarize it, analyze it, pull out insights, and more.” We can’t average words, or put a where clause on agiant file of traffic camera photos.11But if we could query and aggregate words and images the way we can aggregate numbers—if we could put a calculator on top of a bucket of text files—we might find that unstructured data is both more valuable and easier to analyze than our venerated spreadsheets. From this blog,last year:


> Though the raw material in that Dropbox file is probably more valuable than the raw material in your Databricks database, we can’t easily mine or manipulate it; we can only sample it. That’s why we instinctively dismiss this sort of information as untrustworthy or biased: Not because it’s wrong, but because there’s no way to look at all of it at once.


That is where all this is going, I suppose: Box puts an LLM query engine on top of their files, and Box (and Dropbox, and Google Drive) become three more components in the ideal database for the modern enterprise. And then, in 2029, someone pitches OneBox, to disrupt Databox, by putting Postgres and Box in a box.


---


# Pink Pilates Princess Hollywood Pop


What is the point of hiring an analytics team? There are at least two answers:

1. To make only as many reports and dashboards as necessary, and then gosearching for insights—those invaluable nuggets of wisdom and unexpected truth thatchange companies,make careers, andredefine industries.
2. To make dashboards, forever.


The first one sounds nice, but the second one isprobably what people want:


> [ People ] aren’t looking for complicated and fancy analyses; they usually just want to know what’s happening. The value a data team provides is making that information available. We rarely need to figure anything else out, or obscure these basic facts behind aDaily Readiness Score. More often than not, this isn’t insight; it’s distortion.


Anyway, this week was Spotify Wrapped week—“‘All of my friends say it is like my Super Bowl,’ said Ms. Brown, 23”—andthe youths are upset:


> Ms. Brown is part of a vocal cohort of Spotify’s 640 million users who typically share their Wrapped results proudly, but this year she and many others found that new features generated by artificial intelligence — such as a podcast about their listening habits and word-salad-like summaries of their favorite genres — fell flat. …A new feature of Spotify Wrapped this year is Your Musical Evolution, which aims to reveal up to three musical phases that Spotify says “uniquely defined your year.”Users received phases with largely confounding names, including “Pink Pilates Princess Roller Skating Pop,” “After Hours Football Rap” and “Cinnamon Softcore Art Deco,” paired with the artists whose music had inspired those terms.The feature was widely mocked on social media, with one Reddit user commenting that the titles were “random words tossed together.”


What did she want instead? Just to know what’s happening:


> She also questioned the accuracy of users’ top songs lists.Some other social media users lamented the loss of information such as a user’s top genre for the year, as well as the Sound Towns that sought to geolocate a user’s music tastes.


Yes, right, if you are Spotify, it is tempting to create fancy new insights, like “Your favorite genre of music in June isPink Pilates Princess Hollywood Pop,”12because there’s no way something as simple a 80-character SQL query—SELECT genre, COUNT(*) FROM plays WHERE user_id = 'me' GROUP BY 1 ORDER BY 2 DESC—will go viral. But thatreally is all we want.

[1](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-1-152669011)

There was a CD in the box, and some bits of paper that you did not read. Though at some point, it became a literal empty box, and all that was inside was a code that let you download the game from the internet. And by then, it cost $59.99.

[2](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-2-152669011)

Of course, the best way to playStarCraftwas to plant yourself in a corner andbuild up and build upuntil you had 50 siege tanks thatslowly inched into your enemy’s base. This was obviously a dope strategy, it obviously never worked, and it was probably why I got frustrated about losing all the time.

[3](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-3-152669011)

This is a joke; it’s a civil suit; nobody from CrowdStrike is going to jail. But they are getting sued for securities fraud because of abad software update. And man, it is bad when your software outage not only has itsown Wikipedia page, but that page also has an “Impact” section with separate subsections for air transport, finance, government, ground transport, healthcare, media and communications, and retail.

[4](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-4-152669011)

I still don’t know how tosay this. Just SaaS? SaaS software? Software-as-a-service software? What?

[5](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-5-152669011)

Not a real website, unfortunately. What a missed opportunity forsheets.com.

[6](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-6-152669011)

Technically, this isn’t quite true. Redshift launched withtwo options: A flat annual rate, and a per-hour rate. But the per-hour rate was like a hotel bill. You paid for how long you wanted to reserve the database, not for how much you used the database—that is, you booked a room, and the hotel didn’t charge you more or less based on how much time you spent in it. Since databases are typically long-lived applications, most people did not spin databases up and down all the time.

[7](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-7-152669011)

No, I kid, all of them run Python and use AI and do a bunch of other things. There are genuine differences between databases, but they are technical and esoteric, and probably matter less thanbeing chill about code formattinglike commas.

[8](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-8-152669011)

Is it strange for Databricks to show its commitment to getting rid of proprietary vendor-owned formats bybuying a quarter of the committeethat’s building the leading alternative to proprietary vendor-owned formats? Wemust own itto protect it, as it reaches “new levels of growth and innovation,” I guess.

[9](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-9-152669011)

It would be more fun if we called them varietals. I prefer a 2017 SQL to a 2023 SQL. I prefer a California SQL. I prefer a full-bodied SQL. I prefer my SQL from acardboard box.

[10](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-10-152669011)

To recap: Snowflake usesdatediff, which takes three inputs: A time duration, like day or month, a start date, and an end date. DuckDB’s equivalent function takes the same inputs, but is calleddate_diff. And Databricks usesdatedifflike Snowflake, but their version can only compute how many days separate the two dates, and the function expects the end datefirst, and the start date second. Outstanding.

[11](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-11-152669011)

Me, every time I seesomeone on a Citi Bike now.

[12](https://benn.substack.com/p/postgres-in-a-box#footnote-anchor-12-152669011)

Which is apparently different from Pink Pilates Princess Roller Skating Pop? BecauseBeyoncé and Sabrinia Carpenterare roller skaters, andOlivia Rodrigo and Billie Eilishare Hollywood?
