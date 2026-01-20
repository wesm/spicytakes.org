---
title: "Is Minerva the answer?"
subtitle: "A few thoughts on Airbnb’s metrics layer."
date: 2021-05-04T19:30:54+00:00
url: https://benn.substack.com/p/minerva-metrics-layer
slug: minerva-metrics-layer
word_count: 1315
---


![Professor McGonagall, solving data problems.](https://substackcdn.com/image/fetch/$s_!6b4i!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdae05b72-8b2a-4791-8cc1-30b3cb2480ab_953x540.png)

*Accio metric, or some other heinous Harry Potter pun. [source]*


After postingmy proposal for a metrics layertwo weeks ago, a number of folks reached out to share their take on the problem, and a few recommended potential solutions. But the most impressive reaction came from Airbnb’s data team. In response to the post (I assume), they rearchitected their entire data stack around the idea, built a central metrics repository for thousands of metrics, integrated it with all of their other major data tools,andpublished a comprehensive blog postexplaining the whole thing.


It was quite the eight day turnaround. So when several people asked me what I thought about what they’d built, my first answer—”give me a couple weeks to think about it”—felt pretty underwhelming. Though I’m not sure my second answer is any better, I can at least make it longer.1


## What I like about Minerva


Minerva takes on precisely the right problem: It’s really hard to use the same metrics consistently. As the authors’ point out, despite Airbnb having well-maintained “core data” tables—and while they don’t mention it, a famously strong data science team—when execs asked “simple questions like which city had the most bookings in the previous week, Data Science and Finance would sometimes provide diverging answers using slightly different tables, metric definitions, and business logic.” This perfectly highlights the biggest gap in today’s data stack. We have the tools for governing tables, and we have tools for governing dashboards and analysis, but we’re still pretty sloppy about governing the space between the two. Because we don’t manage metrics globally, people define and calculate them in different and often bespoke ways. And the more tools and teams that are involved, the worse the problem gets.


Minerva, as their graphic shows, was built to literally bridge the gap—to add the layer—between tables and consumption. Structurally, this is exactly the piece our puzzle needs.


![Minerva and the metrics layer](https://substackcdn.com/image/fetch/$s_!Ezr5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fddb51d71-97b1-4187-857a-4fff023f7f06_760x653.jpeg)

*Who wore it better?*


The Airbnb team took Minerva a step further than I proposed, integrating it with Dataportal, their data catalog. Though the synergy2between a metrics repository and a data catalog is obvious, Airbnb’s integration unlocks a subtle but profound shift in data discovery.


When we think about documenting data within an organization, we tend to think about documenting tables and the columns within them. On the surface, this makes sense, and not just because tablesaredata; tables are also how analysts model data in their heads. As Fishtown’s Claire Carroll outlined inher insightful postabout writing queries to answer business questions, her first step is to sketch out the table she needs to answer the question, and work backwards from there. This way of thinking is almost required for analysts who work with relational data; do it enough, and it becomes hard to see data problems in any other way. Just asmusicians hear music differently than the rest of us, analysts see structures in data that others don’t.


But most people aren’t analysts. They don’t think of data as a set of tables, columns, and relationships; they think in terms of metrics and charts. Data isn’t a hosts table and a bookings table with a join key; it’s bookings by month, bookings per host, and average booking price.


Backed by Minerva, Airbnb’s Dataportal presents data through this lens—in the language of its consumer, not its creator. Most self-serve tools provide ways for people to manipulate data with drag-and-drop interfaces that are abstractions of a SQL query. Minerva goes further, hiding not only the SQL query from its users, but also the very tables and fields themselves.3Rather than the usual data exploration, it’spure metric extraction. That’s a clever step forward.


## What I’d do differently


My biggest gripe with Minerva is how you “query” it. As best I can tell, metrics are extracted from Minerva via API; from thescreenshots of the Python integration, it looks like the API lets people request metrics over date ranges, with filters, and grouped by different dimensions.


As I mentioned in my initial post, API-based solutions don’t work for analysts working directly in SQL. Though I don’t know how analysts work at Airbnb, in the broader market, most analysts’ work starts in SQL; for many, it also ends there. Unfortunately, Minerva appears to be inaccessible to these workflows. Analysts, when inevitably asked to explain why some KPI is yo-yoing across a Minerva-backed dashboard, will eventually have to recreate that metric, in SQL, on raw data in their warehouse. The more fluid this process, the faster the analyst can answer the question—and just as importantly, the more likely it is that their results match the canonical standard maintained in Minerva.


In fairness, it’s worth noting that the R and Python clients are nodding in this direction. If most analysts work in these languages over SQL—which may be the case at Airbnb; I don’t know—these clients may be all you need. But given the ubiquity of SQL in modern analysis these days, that’s likely more of the exception than the rule.


My other objection to an API-based metrics layer is that it’s harder to adopt. Metrics are useful in lots of tools, including dashboards, data catalogs, A/B testing and ML platforms, and operational tools like marketing automation software. Because Airbnb built most of this infrastructure in-house, they were able to integrate them directly with Minerva’s API. It’s work, but it works. Most of us don’t have that luxury. We buy these tools from different vendors, and can only use a metrics layer if each vendor builds a bilateral integration with it. If Minerva operated through a centralized data warehouse instead, most data consumption tools—which often interact with warehouses more or less directly—will “integrate” with the metrics layer automatically, just as they can “integrate” with dbt.


I have a final question about how metrics are defined. The screenshot of the COVID-19 dashboard configuration is in YAML, so I’d guess that Minerva uses something similar.4Though YAML is an obvious choice, my heart wants something rooted in SQL. SQL is more expressive than YAML; analysts think in tables, and so does SQL; and SQL can also be pulled apart into intermittent steps, making it easier to follow its logic. YAML configurations are harder to trace. That said, I’m not exactly sure how to configure metrics in SQL. But I’d be thrilled if someone figured it out.


In the end, more than any feature or technical detail, Minerva’s adoption is its headline. Over the last decade, companies like Airbnb have been the pioneers for the rest of us, figuring out what problems we’ll run into in a few years and charting paths through them. If Minerva solves as big of a problem at Airbnb as its usage indicates, we’re all likely to need something similar soon. Minerva—and just as importantly, the openness of the Airbnb team to share details about it—put us one big step closer to getting there.

[1](https://benn.substack.com/p/minerva-metrics-layer#footnote-anchor-1-36031621)

See also, “Why don’t you use Twitter instead of Substack?”

[2](https://benn.substack.com/p/minerva-metrics-layer#footnote-anchor-2-36031621)

Synergy! Deliverables! Running point!Read this article!

[3](https://benn.substack.com/p/minerva-metrics-layer#footnote-anchor-3-36031621)

There’s a (very nerdy) debate to be had (among a very small group of people) on how aware people should be of the tables that underlie the data they see. On nearly every website we use, we interact with lots of structured, relational data. Most of us rarely think of it as such—many people probably aren’t even aware of it—and we can all use those apps just fine. But in data applications like self-serve BI tools, we put those tables at the front, so much so that these apps are difficult to usewithoutthinking about those tables. Do we do that because fields and tables are actually important for people to understand, or because the data comes in fields and tables, and we haven’t come up with a more creative way to repackage it? I lean more toward the latter.

[4](https://benn.substack.com/p/minerva-metrics-layer#footnote-anchor-4-36031621)

YAML: Yet another magic language.
