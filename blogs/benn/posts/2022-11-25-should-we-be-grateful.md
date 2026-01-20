---
title: "Should we be grateful for the modern data stack?"
subtitle: "Yes."
date: 2022-11-25T17:52:12+00:00
url: https://benn.substack.com/p/should-we-be-grateful
slug: should-we-be-grateful
word_count: 2258
---


![](https://substackcdn.com/image/fetch/$s_!RY7w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3c311efd-9e13-4c5b-806d-f9d3fc8d9b9c_780x520.png)

*We’re still all trying to find the guy who said we shouldn’t be.*


It’s easy tocomplain. It’s easy tobe skeptical. It’s easy to say it’s alloverhypedandovervalued. It’s easy to look at the rough edges of an unfamiliar tool, andwonder why such obvious problems haven’t been fixed.1


There’s a place for this sort of commentary2—this kind ofcommunity of inquiryis how we stumble forward together. But in only pointing out those flaws, looking at the uneven ground at our feet, it’s also easy to lose track of just how far we’ve traveled. Even in the relatively short amount of time I’ve been working in the data industry—I took my first tech job as an analyst atYammer, a B2B SaaS company, in 2012—the amount of collective progress we’ve made has been dizzying.


In the early 2010s, the data teams atLinkedIn,Facebook, andZyngawere seen as revolutionaries, but inimitable ones: They were funded by massively hyped tech companies, flush with technical experts, and worked with some of the biggest andmost monetizable datasetsin the world. They were blazing trails, but trails that weren’t easily followed.


Yammer’s analytics team—my introduction to the data world—was a pioneer forthe everyman.3Though Yammer was a “high-growth” startup, it was a pedestrian one, no different than dozens of other tech companies of its size. Unlike the data science team at Google, which wasorganizing all the world’s information, our objective as analysts was to use product usage logs and CRM data to help a sales team hawk software to IT departments. Rather than trying to solve new problems or invent new uses of data, our explicit goal was to apply techniques stolen from Facebook and social gaming to sell enterprise software.4To achieve that end—which is more or less the goal of nearly every data organization now—my bosses built a data organization that looksa lot like those of 2022, but without the glossy sheenfrom ten years ofIT consumerization, YC-backed data startups, and trendy thought leadership. In other words, we were a modern data team without the modern data stack.


It’s a team, then, that offers answers to two questions: How did data teams actually work ten years ago? And how would teams have to work without the last decade of growth and innovation?


# Proto-modern


Just as our team wouldn’t look entirely out of place in a startup today, the architectural outlines of our data stack would be pretty familiar too. The modern data stack didn’t exist—this was 2012; Redshift, whicharguably catalyzed the entire movement, hadn’t been released yet; we were still all enamored withthe possibilities of Hadoop—but we ran a proto-version of it: We ingested data from a handful of sources into a centralized warehouse; we transformed it in the warehouse using a DAG of SQL scripts; we pushed that data out through ad hoc analysis, BI reports, and a handful of department-specific tools.5We didn’t recognize any of these patterns by their current brands—ELT, analytics engineering, data apps—but the shapes were the same.


The experience of using it, however, was not.


## The storage layer


Vertica, a columnar-store analytical database, sat at the center of our data stack. Like most databases at the time, we couldn’t buy a hosted version; instead, we bought a license—for about half-million dollars a year6—to run the software in some server rack we leased in a data center in San Jose.7Since we were responsible for its own uptime, Vertica had to be maintained by aDBA, whose job was to monitor the cluster's instruments, and make sure everything was healthy.8


Routinely, it was not. Bad queries had a tendency to sendnodessideways, which would not only clog up the warehouse, but would also require a coordinated set of operations to rehabilitate.  What exactly caused these problems and how exactly were they fixed? I never quite knew. But I knew I had to be delicate, or else I'd send the people staring into the matrix on vertical monitors into furious fits of SSH'ing in and out of remote boxes, while everyone else fielded angry emails from execs about their dashboards being out of date.


After Yammer was acquired by Microsoft, we dabbled in “big data” alternatives to Vertica, eventually settling on Cosmos, Microsoft’s then-internal andnow-public NoSQL warehouse. I remember being told there was useful data in Cosmos, though I never figured out what it was, because accessing it required writing queries in someFrankenstein language that mixed SQL and C#. So I stayed away, and let other people write the 800 lines of .NET-flavored MapReduce that was needed to parse SharePoint’s usage logs into an estimate of daily active users9—and hoped that knowing that number wasn't important to the company.


## The ingestion layer


Our ETL architecture was strikingly modern—but, much like our warehouse, plagued by problems that don’t concern today’s data teams. Nearly all of the data in Vertica came from three sources: The application Postgres database that powered Yammer’s product, an event stream from that same application, and Salesforce. In all three cases, we did very little transformation in flight.


To my knowledge, the application replica and its event stream were reliable and required very little babysitting—less, in fact, than Postgres-to-Snowflake-or-Redshift connectors do today. Salesforce, by contrast, was a nightmare. We had to build our own service for extracting data from its APIs into Vertica, and, despite an engineer working on the problem nearly full-time, it was a perpetual wreck. The Salesforce APIs were brittle. The Salesforce admins on the other side of the office would sometimes change Salesforce schemas, which would require updates to our connector. When something broke, extraction jobs would get backed up, and, like Vertica, require careful handholding to revive.


Because of this ongoing fire—and the cost of containing it—we generally avoided sourcing data from other third-party sources. An effort to get data from Exact Target, a marketing automation tool for sending emails, took several months; an effort to get data from Jobvite never made it past a hack day.


## The transformation layer


Once loaded into Vertica, raw data wasmodeled by Integritie, our homemade transformation tool. It was similar to dbt, minus a bunch of developmental niceties: There was no IDE for it; you couldn’t run models in staging environments; jobs were written in raw SQL, without Jinja or macros.10Instead, we followed a “works on my machine” model of development. Run queries locally, copy them into the Integritie repo, deploy it, and hope production runs as expected. Sometimes it obviously did, and sometimesit obviously didn’t. But most of the time, the query executed correctly, and—without any kind of testing environment or way to see how tables actually changed—our best gauge of how well something worked was if someone complained about it later.


Given how easy it was to overrun Vertica with long-running queries, we spent a lot of time optimizing the jobs in Integritie. Models were almost required to load incrementally; rebuilding large tables was costly, and had to be manually orchestrated. This amplified the challenges of resolving upstream issues like Vertica getting backed up or Salesforce syncs stalling. We couldn’t just unplug it and plug it back in; we had to make sure failed jobs didn’t restart all at once, and nurse the pipeline back to health.


## The consumption layer


All of this effort and expense—which probably totaled a few million dollars a year in software costs and salaries—powered a handful of applications that drove “business value.” The analytics team spent most of their time in abrowser-based SQL editor, with some very basic charts on top. We got questions, wrote queries in the tool, and sent URLs with answers back to whoever was asking. These links were our crude audit trails, and internal communications, Excel files, and Powerpoint speaker notes were littered with them.


The data engineering team also built a few proper data apps for more durable use-cases. There was an executive dashboard that showed our most important KPIs, with a few simple filters; there was an site for profiling customers and aggregating how healthy their accounts were; there were a set of pages that were embedded directly inside the Yammer application so that customers could see a few vanity metrics on how they were using the product. These were applications in the truest sense: They were built in Rails, hosted on their own servers, and ran on top of dedicated databases. As analysts, our only involvement in the development of these tools was to create tables in Integrie that mapped to exactly what each application needed. The app would then retrieve our tables and—assuming we’d formatted everything correctly, which I often didn’t—update the apps.


Most of these tools, however, were feeders into Excel.11The email lists we sent to marketing got exported to Excel, and uploaded into Marketo. Product managers, wanting to tinker with A/B test results, exported reports to Excel. The monthly board deck was built in Powerpoint using charts that were generated by copying query results into “raw” data tabs in a giant Excel workbook. None of it was peer reviewed or versioned, and only some of it was centrally organized. Instead, much of our work—the culmination of all the technology that sat underneath it—was scattered across Dropbox folders of SQL queries and_v3_final.xlxsfiles.


![](https://substackcdn.com/image/fetch/$s_!Z7l8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffabf0bef-0234-46ab-b015-b5fb70fa4218_1576x578.png)

*An actual screenshot of what it was all for.*


# The questions we should be asking


The tools we have today—built and supported by thousands of people across dozens of companies—represent a profound leap forward from what we had then. And their effect extends beyond easing the daily frustrations of existing data scientists; they also made the work we did in 2012 accessible to a far greater range of companies and aspiring analysts and analytics engineers. Nearly part of the industry is breathtakingly easier, faster, more powerful, and more reliable than it was a few short years ago.


Except us.


Because there’s one nagging inconvenience in the comparison between today’s data teams and the one I was on in 2012: Yammer’s data team was as impactful as any that I’ve ever worked with. It was a key part of the product development process; its members were honorary members of the marketing and customer success leadership groups; it was respected, in-demand, and had a voice in the strategic direction of the company. And all this was done on top of technology that was, relative to what’s available today, fragile, narrow, expensive, and powered bynow-archaic computing capacity.12


That’sthe paradox we need to solve. Why has data technology advanced so much further than value a data team provides? Does all of this new tooling actually hurt, by causing us to lose focus on the most important problems (e.g., the data in Salesforce) in favor of the shiny new things that don’t actually matter (e.g., the data in our twenty-fifth SaaS app)? Has the industry’s talent not caught up with the capacity of its tools, and we just need to be patient? Is the problem morefundamental? I’m not sure.13But if our 2032 selves want to be as grateful for 2020s as we should be for the 2010s, those are the next questions we need to answer.

[1](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-1-86811203)

Shoutout to sycophantic egomaniac George Hotz for taking this hubris tobreathtaking new heights, only to immediately change the goal postsandask someone else to kick the ball through them. (Also, how does this guy not only have aWikipedia page, but has one that has more references than the pages forDenzel Washington,Dan Quayle,Diana Taurasi, and theBattle for Fort Sumter? Ashley Feinberg,we need you.)

[2](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-2-86811203)

Right?Friends?

[3](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-3-86811203)

Where the everyman is adrug- and alcohol-fueled VC-backed Silicon Valley startupfor which the typical laws of economics—e.g., you should make more money than you spend—don’t apply.

[4](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-4-86811203)

The theft was almost literal. Yammer’s product was designed to mirror Facebook, and the head of our data team was hired fromPlaydom, a Zynga competitor.

[5](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-5-86811203)

Good god, do not attempt to diagram this sentence.

[6](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-6-86811203)

Or at least, I’m pretty sure it cost this. And this is roughly in line with somerandom person’s answerto a random Quora question about a loosely related topic, so I’m gonna go with it.

[7](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-7-86811203)

The pricing structure was also wonky. Licensing fees were determined by the size of the warehouse (i.e., the number of nodes in your cluster, and the amount of memory in each node) you wanted to run, but you bring your own hardware. There were no fees for using the warehouse though; once licensed, you could pummel it with as many queries as you wanted.

[8](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-8-86811203)

This was fairly normal for the time. For comparison, a few years earlier, Teradata, another major database vendor, released a “low-cost” and “fast-to-deploy” warehouse, which you couldhave up and running in ninety days for $350,000.

[9](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-9-86811203)

Based on a true story.

[10](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-10-86811203)

This may have been a feature and not a bug.

[11](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-11-86811203)

Prior to the Microsoft acquisition, Google Sheets was too immature to replace Excel; after the Microsoft acquisition, Microsoft’s ego was too immature to allow anyone to use Google products.

[12](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-12-86811203)

If you ever want to humble yourself, read about semiconductors and how they’re made. One of many fun facts: They have to use precision mirrors to manufacture semiconductors. What’s a precision mirror, you ask? It’s one that, if blown up to the size of Germany, its biggest bump would beone tenth of a millimeterhigh. Whatever you do,don’t walk on it.

[13](https://benn.substack.com/p/should-we-be-grateful#footnote-anchor-13-86811203)

If you want a BI-centric version of discussion,Mode is hosting a webinarin a couple weeks to talk about how we (we = Mode, I work at Mode) want to solve some of this. On one hand, smart and thoughtful people will be on it. On the other hand,so will I.
