---
title: "What happened to the data warehouse?"
subtitle: "It's a sandwich, a floppy disk, and an iPhone."
date: 2023-03-03T16:57:11+00:00
url: https://benn.substack.com/p/what-happened-to-the-data-warehouse
slug: what-happened-to-the-data-warehouse
word_count: 2160
---


![the iphone launch](https://substackcdn.com/image/fetch/$s_!dE93!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadde7e64-cb4c-47a6-b845-d66119c75cb1_1280x720.jpeg)

*What could have been.*


Here's amanic idea—let’s run dbt directly on top of S3.


Admittedly, it stresses me out to suggest that, for two reasons. First, I don’t entirely understand what I’m proposing. There’s an outline that makes sense—dbt can nowcompile queries, so why not compile them into something that could be run by a generic Lambda function or an EC2 machine against a bunch of Parquet files in S3?—but I have no idea what technical issues, both big and small, would have to be worked through to make this possible.Computers are above my pay grade.


Second, in the last couple years, the data industry has mostly settled on how to design the lower levels of a data stack. After flirting with a bunch of NoSQL and Hadoop architectures—one of the premier data conferences in 2014, calledHadoop World, had tracks like “Hadoop and Beyond” and “Hardcore Data Science”—we agreed on an orderly peace.1Every data stack needs an ETL tool that spiders its way into various data sources and ingests them into a centralized location; it needs that location, typically a warehouse that both stores the data and provides a means for running queries (orfancier operations) on top of it it; and the stack needs a transformation tool—i.e., dbt—where teams can define business logic that regularly tell the warehouse how to turn its messy raw data into something fit for human consumption. Each of these three territories is well understood and well defined. The borders between them are clear and uncontested.It feels good.


The top layer—how we cooked with our data, once the other toolsput it all in its place—is the only problem left to solve. BI, analytics, AI tools, data apps, data observability systems, data discovery platforms, data catalogs, and a half dozen other categories desperately trying not to be BI2still live in the wilderness, at war, on the other side of the wall. Once we civilize thosebarbarian hordes, we can allmove on from talking about the tools to “doing the work.”3


The alarming truth, I’m realizing, is that the three layers underneath our disorganized outer boundary aren’t actually so stable after all. Specifically, the data warehouse—the anchor, the main beam, the hub around which even ETL and transformation tools spin—has already started to break apart. And an idea like replacing the whole thing with dbt and some CSVs in Azure isn’t actually a deranged dive into some unhinged chaos; it may well be exactly where we’re headed.


# Take us to your warehouse


Supposethe aliensare real,4but weird. They manage to sneak one of their ships through our now-robust balloon popping defenses. Fortunately for us, given how eagerly we shot down their first envoys, they come in peace—they’re pedantic linguists, on a mission to inventory the galaxy into a tidy dictionary that explains how words are commonly understood. “Give us a series of yes or no questions,” they tell us, “that will conclusively tell us if the data community agrees that something is a data warehouse. And we don’t want a textbook definition; we want to know what people think of when someone says warehouse.’”5


If we can give this to them, our sins will be forgiven, and they’ll go on their merry way. But if we can’t, they’ll annihilate the planet, because our indecision and frustrating inexactitude isa blemish on their perfectly arranged universe.


As someone who’s helpedbuild a product that connects to data warehouses, who regularly uses warehouses (and hasplenty of pedantic opinionsof my own about that), and writes a blogaboutwarehousevendors, I should probably be able to give our fussy foreigners an answer. But I can’t. I have no clue how to tell them what a warehouse is. I can name a bunch of examples—Redshift is one; so is Snowflake; Excel is not—but they’re not based on a clean set of rules. It’s classification by feel, by vibe, by Supreme Court Justice Potter Stewart's famous ruling on what defines porn: "I'll know it when I see it."


To define a data warehouse is to define a sandwich: Every attempt has weird and unacceptable exceptions. A sandwich is meat between bread? A PB&J isn’t a sandwich and a hot dog is. A sandwich must havetwo separate pieces of bread? Mostcheesesteaksaren’t sandwiches and tiramisu is. A sandwich is food surrounded by leavened bread? Ice cream sandwiches aren’t sandwiches and soup in a bread bowl is. Bytwopieces of leavened bread? Fine, put on of thoselittle capson the bowl.


Do this for data warehouses, and we tie ourselves in the same impossible knots. Warehouses are where data is physically stored? Consider Snowflake, which can query fromexternal data sourceslike S3 and Google Cloud Storage. If I used this feature, I’d still refer to Snowflake as my warehouse; by creating external tables, the warehouse wouldn’t magically transfer itself from Snowflake to S3.


Are they compute engines? If this were true, it’d force us to conclude that a Python notebook, running Pandas on top of Parquet files, is a warehouse, which definitely doesn’t seem right.


“Sources of truth?" This one is almost laughable, given that most warehouses today are aggregators of data from other places, like software applications and third-party SaaS apps. In this way, warehouses are the map to other sources’ territories.


Perhaps a data warehouse is all of these things—they are,as Oracle says, the storage, the compute engine, and the database management system that knows how the whole thing is organized and accessed. But that’d imply that some stacks, like one that uses Presto’s query engine on top of files in Azure, have warehouses that are split across different vendors. That’s uncomfortable—but not nearly as uncomfortable as this definition also implying that Excel, which stores data, processes it, and provides interfaces for accessing it, is a warehouse. Outside of the inevitable Hacker News food fights about whetherExcelackshuallyis or isn't a database, most analysts would agree—nay,plead—that Excel is neither a database nor a warehouse.6


To make matters even more complicated, our definitions of warehouses are path dependent.Amazon Athena, a standalone query engine that has never stored data itself, is nearly identical to a Snowflake deployment that only queries external tables. But because Athena has always just been the engine, and because Snowflake usually stores data, we’d be more inclined to call the latter a warehouse than the former, even if both are used in the same way. In other words, ifyou start with a ship, you can strip it down to just a few planks and still call it a ship. But if you created the same object by nailing a few planks together, it’s just ashoddy raft.


# The skeuomorphic database


Another definition—the most reasonable one, probably—could be: Who cares? There are no aliens. Why do we need a definition for a warehouse at all?


Mostly, we don’t. Just as 24-hour cable news networks have to fill late-night airtime withsquawking clowns, so too do weekly Substacks. The problem is made up, my manufactured outrage againstXbox’s power saving mode,7for the likes and subscribes and MyPillow advertising dollars.


But, the absence of a definition is, at least for us squawking clowns, an intellectually startling realization. It suggests that the data stacks don’t have to have a traditional warehouse at their center, because today’s warehouse is askeuomorph. It’s an aesthetic echo of a bygone era, and its actual architecture—streaming,serverless,storageless—can be wildly different from what might’ve assumed was required.


Another such wild architecture? dbt on S3.


The rough idea is simple enough. When queries get run through dbt’s SQL proxy (this is the thing that intercepts queries with Jinja and metric references in them, and renders them into pure SQL), it doesn’t hand the query off to an database; it instead compiles the query again into something that can be executed against files in S3. A dbt Server processes the job, by reading data out of S3 and writing the results back out as a new file.8


Josh Wills’DuckDB client for dbtshows what this could look like, and Jacob Matson’smodern data stack in a boxshows how it could be used. As Jacob says, removing the traditional database and running the entire thing on bare compute services could save money and depend only on open-source software. Though his example is more of an experimental prototype than enterprise product, its general pitch could be similar to that of DuckDB itself—huge and complex data platformsare overpoweredfor most of what we need them to do.


It could also be just the beginning. What if thedbt sourcesdidn’t have to point to tables in a database, but could reference any data source, from files in S3 to Google Sheets? What if Transform’s models inside of dbt could be defined across those sources? What if the semantic layer—be it dbt, LookML, Malloy, or any other potentially independent semantic configuration—isn’t just an encoding of join keys and metric formulas on top of a database, but is anorganizational ERDthat describes how entities are related across data sources and apps? What if we modeled our business rather than just our data?


These ideas aren’t exactly novel either;the Modern Data Companyis building something similar with theirDataOS(®), and I might be describing a data mesh in cheaper language.9But whatever you call it, it seems likely that the next decade’s data warehouses—even if they’re still called that—will be as unrecognizable to us asfloppy disks are to teenagers.


# An iPod, a phone, and an internet communicator


The thing is, I don’t think it had to be this way.


In his famous launch announcement of the iPhone, Steve Jobs had a choice. He could’ve decided that the device’s combination of features—an iPod, a phone, and an internet communicator—transcended the traditional telephone. “This is not a phone,” he could have said, “it’s a personal communication platform.”


Instead, he went the other direction. “Today,”he actually said, “Apple is going to reinvent the phone.” Implied in his announcement: A phone isn’t something that just makes calls and sends texts anymore, but does dozens of things, all at once.


It’s always struck me as a little odd that ambitious warehouse vendors took the opposite approach with their flagship products. Snowflake, for instance, has largely moved away from calling itself adatabasein favor of thedata cloud. I get the reasoning; the platform does a lot more than your everyday database. But for Snowflake, I think that’s a missed opportunity. Rather than rebranding themselves, they could’ve rebranded the data warehouse. They could’ve said, as Steve Jobs did, that they reinvented the database. They aren’t a warehouse with lots of extra features; they’re just a warehouse—and for anyone else to be one, they have to have those same features. The only thing better than being a category creator is being the pacesetter in a category that everyone already buys from. (Counterpoint: They’ve got1.938 billion reasonsto keep doing it their way).

[1](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-1-106233151)

It’s not the modern data stack; it’sPax data.(Datum?Datum?Dor?Grammar is above my pay grade too).

[2](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-2-106233151)

“I’m not bi! i’m not bi!!”, i continue to insist as i slowly shrink and transform into bi.

[3](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-3-106233151)

To be clear, once this happens, I’ll be moving on to talk aboutPitbull.

[4](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-4-106233151)

My theory on aliens: Theywereout there, andwill beout there, but they aren’t out there now. There are roughlyone trillion planets(what) in the Milky Way, some of which surely could produce intelligent life. But the Milky Way is also 13 billion years old, so the odds of that our window of galactic availability overlaps with that of some other species—that we are both in between the time we’ve developed technology that can communicate with the cosmos and the time we kill ourselves with it—isn’t that high. Or, as Wikipedia’s entry on theDrake equationput it, under one set of (disputed) assumptions, “we are probably alone in this galaxy, and possibly in the observable universe.” Anyway, back to the important stuff: The future of data warehousing over the next 24 months.

[5](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-5-106233151)

In their dictionary, Frankenstein is the monster, because the aliens are Good.

[6](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-6-106233151)

Troublingly, most blog posts I found aboutwhyExcelisn’tadatabasedon’t answer that question at all, and just explain why Excelshouldn’t bea database. But is it one? Seems like it could well be.

[7](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-7-106233151)

In fairness to myself—and honestly, probably Fox News—I at least proofread these things.

[8](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-8-106233151)

I thinkthis is the same thing as saying dbt could be adata lakehouse, which is, as best I can tell, a query engine that runs on top of files in cloud storage tools like S3. But I don’t really know, because data lakehouses are rarely described in plain language. This has always seemed a little suspicious to me.Good ideas don’t need to be lied about to gain public acceptance; good technology doesn’t need to be exaggerated or obfuscated and dressed up indizzying corporate doublespeakto prove its value. Or maybe this sort of language—”no matter the workload, leverage all your data assets instantly with our new high-concurrency data lakehouse that treats data as code”—is how bank CIOs communicate. If you have to ask someone to explain it,you can’t afford it.

[9](https://benn.substack.com/p/what-happened-to-the-data-warehouse#footnote-anchor-9-106233151)

Ibid.
