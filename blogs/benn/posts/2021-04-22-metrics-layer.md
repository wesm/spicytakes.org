---
title: "The missing piece of the modern data stack"
subtitle: "Our cool new house needs one more plank in its foundation."
date: 2021-04-22T18:33:26+00:00
url: https://benn.substack.com/p/metrics-layer
slug: metrics-layer
word_count: 2311
---


![Not the modern data stack](https://substackcdn.com/image/fetch/$s_!6K4B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F48cd5250-94f4-48c7-88bf-5b4ae03f968c_1000x568.jpeg)

*Ok, this is an overdramatization.*


In the evidently tiny professional circles that I run in, the “modern data stack” is having a moment. The concept, which is a new framework to move data around an organization and make it available for people to use and analyze, isinspiring conferences,historical retrospectives,listicles,how-to guides, andcompanies themselves. A decade afterThe Economistwarned us we’d all soon be drowning in data, the modern data stack is emerging as Silicon Valley’s proposed life raft.


![](https://substackcdn.com/image/fetch/$s_!5cQM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F11f02e5c-acc1-4303-b332-a4436ef88171_1600x1271.png)

*In which I write 2,000 words about a topic less popular thanwondering if you’re an elephant.*


While everyone’s definition of the modern data stack differs slightly (i.e., the tool they sell isthehub around which the whole apparatus spins1), there’s little dispute over its general contours. An ingestion tool writes data from a wide variety of sources into a central warehouse; a transformation tool models that data in the warehouse, converting it from raw ores to usable alloys; a BI tool provides direct access to data so that it can be visualized and analyzed. Over the last year, a couple extra complications are becoming popular as well:Reverse ETLtools write data back into source systems, and monitoring tools track the health of the whole system.2


In an ecosystem this dynamic—and, frankly,this overrun with cash—a lot of new companies will be looking to define their niche.3Some tools will claim to be areimagining of legacy tools, or anunbundling of legacy tools, or abundling of legacy tools, or “Superhuman for X,” or “Clubhouse for Y.” And some products will claim to be something entirely new, their own distinct yet critical category in companies’ growing collection of data apps.


Most new products won’t be that. The tools we have are, in fact, pretty good. While there are definitely improvements to be made, we aren’t lacking many foundational elements.


Except for one: a metrics layer.


Though companies use data for a lot of things, one of the most important is also one of the most mundane: basic reporting on business operations. Employees across a company have to make decisions; to make those decisions, they need to know what’s happening. Which products do people like? Which marketing campaigns are attracting new customers? Who on the sales team is hitting their quota? For most companies,data isn’t an AI-powered screenwriter; it’s just a simple narrator, telling people what’s going on.


Companies solve this problem through what’s come to be called self-serve. The idea behind self-serve is that anyone at a company can get the data they need—they can be told what’s happening—without having to ask someone for help.


As I’ve talked about before, self-serve is a misunderstood (or, at least, misrepresented) problem. Because the most common question people have is “How often did this thing happen?,” effective self-serve is less about complex analysis and more about metric extraction. People “want to choose from a list of understood KPIs, apply it to a filtered set of records, and aggregate it by a particular dimension. It's analytical Mad Libs—show meaverage order sizefororders that used gift cardsbymonth.”


Today’s current stack makes it easy to answer this question, but really hard to answer it consistently.The core problem is that there’s no central repository for defining a metric.Without that, metric formulas are scattered across tools, buried in hidden dashboards, and recreated, rewritten, and reused with no oversight or guidance.


To see the problem, consider the journey that data follows to reach that dashboard. After being written into a warehouse (e.g., Snowflake) by an ingestion tool (e.g., Fivetran), data is updated by a transformation tool (e.g., dbt) several times, passing through a couple types of aggregations along the way:

- Cleaned granular data: The first stage creates dimension and fact tables, which maintain the same degree of granularity as raw tables while removing the irregularities and aesthetic irritations that make raw data difficult to work with. In these cleaned tables, malformed rows are excluded, columns are renamed so they’re easier to understand, fields like phone numbers are standardized, and tables for new concepts that don’t exist in raw form, such asdimension_web_sessions, are created. Data is polished at this stage, but not aggregated—if there’s a raw table that has one row per email,dimension_emailswill have one row per email too.
- Rollups: A second stage rolls up granular data into aggregated metrics tables. For example, arollup_active_userstable might include rows for daily, weekly, rolling 7-day, and rolling 28-day active users, signups, returning users, and so on. These tables only include metrics, obscuring which records compose those aggregates. While therollup_active_userstable will tell you that 100 people were active over the seven days prior to April 10th, it won’t tell you who those 100 people were.


To extract metrics from these tables, people have two options: They can pull from pre-aggregated rollups, or they can compute new metrics on the fly from granular dimension tables.


Rollup tables are typically generated by transformation tools like dbt, so the metrics in these tables can be consistently defined and reliably governed. However, because rollup tables are precomputed, there’s a practical limit to how many can be created. As a result, they’re often only built for top-level metrics, like active users or customer NPS.


But self-serve analysis requires another level of depth—daily active usersfor a particular customer segment, or NPSfor a particular type of user. Even with just a handful of metrics and segments, it’s all but impossible to precompute every possible combination.


Without a rollup to draw from, data consumers have to follow the second path: aggregate new metrics directly from dimension tables. That leaves the nature of the aggregation up to the person doing the analysis, and these aggregations are rarely simple. Counting weekly orders in Europe, for example, requires you to define week, order, and Europe. Do weeks start on Sunday or Monday? In which time zone? Do orders include those made with gift cards? What about returns? And are European customers those with billing addresses or shipping addresses in Europe? Are Russian customers European? Are British customers European?45While all of this logic might live in therollup_orderstable, it isn’t necessarily in thedimension_orderstable, meaning someone has to apply it on their own to do their analysis. This makes it incredibly difficult for people, especially people who aren’t analysts and aren’t familiar with the weird nuances that riddle most datasets, to consistently arrive at the same result.


## A shared foundation


BI tools appear to solve this problem by offering ways for people to define on-the-fly computations in reports and dashboards. Through LookML in Looker, calculated fields in Tableau and Mode, and formulas in Sisense, analysts can configure visualizations to aggregate results in specific ways.


But this is a superficial fix, barely better than scattering this logic across Excel spreadsheets. Defining metrics in a BI tool localizes those definitions to that tool—or even worse, to individual charts or elements within that tool. A Tableau calculated field is only accessible in the dashboard that uses it; LookML is only accessible in Looker itself.


Local solutions don’t work because BI tools aren’t the only way companies consume data. Analysts and data scientistsanswer complex questionsin ad hoc tools—work that’s often inspired by a change to a metric in a BI tool but is rarely done in that BI tool. Data engineers build pipelines from data warehouses into marketing automation tools or operational systems, ideally bypassing the BI tool entirely when they do. In both of these cases, LookML or the logic defined in a calculated field is inaccessible. So metrics get recomputed in new tools. In the best case, these calculations drift apart over time; in the worst case, they never match in the first place.


A better architecture would do for metrics what dbt did for transformed data—make them globally accessible to every other tool in the data stack. Rather than each tool defining their own aggregations, the metrics layer is a centralized clearing house for how all metrics are calculated.


![The architecture of the metrics layer](https://substackcdn.com/image/fetch/$s_!Mriu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3c382242-eb8f-4187-a4e1-a9d08801ccaf_760x653.jpeg)

*The smiling database likes it.*


Looker and dbt hint at how this could be done, though neither tool is particularly close to solving the problem themselves. dbt showed us that the best path to make something universally accessible is through the data warehouse. dbt works not because everything connects to it, but because nothing needs to connect to it. It produces tables, and anything that can talk to a data warehouse—i.e., any modern data tool—can make use of what dbt produces. And Looker, and LookML specifically, provides a template for translating a request for a metric into a query that extracts that metric from a database in a consistent and governed way.6


These tools, however, have foundational gaps that prevent them from operating as a metrics layer. dbt doesn’t run on demand, and LookML configures an application, not a globally accessible service.


How might a proper metrics layer close these gaps? Fortunately,the community is sensing this problem, and a few companies—Supergrain,7Transform, andTrace—are already working on a solution. And while I’m not an expert on compilers or the inner workings of a database (I still don’t understandGROUP BY, which is apparently aDSL hash map, so…high speed internet from 2003?), I have my own ideas for what I’d like to see.


First, a metrics layer should be centrally configured, either in a language like LookML or in something that looks more like SQL. I could see the case for both. I’m biased toward SQL-based solutions, but YAML is a more natural configuration language.


Second, the tool should have a simple job: Take metric requests—let’s call them metric queries—as an input, and return SQL queries that extract those metrics as an output.


Third—and most critically—other tools should connect to the metrics layer as though it were a database. The layer could live directly in the warehouse, as some combination of views and stored procedures, or it could act as a proxy that sits in front of a database. In both cases, any tool that connects to the database, either directly or through the proxy, could issue metric queries, which the metric layer would translate into a SQL query that the database runs. (This is why API-based solutions are unlikely to work. If people have to interact with the metrics layer through a REST API, analysts can’t access it in the SQL-based tools that they live in, severely limiting its applicability.) Metrics queries, which might look like the Mad Libs examples above, could go even further, and be combined with raw SQL (as a CTE, say). This would allow analysts to extend centrally-defined metrics by both modifying the SQL they render to, and by incorporating them directly into more complex ad hoc analysis.


![How a metrics query might work](https://substackcdn.com/image/fetch/$s_!T1iy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F69541f8e-b391-4700-9621-0e97fcf7c994_846x580.jpeg)

*Come at me, leading comma people*


A global metrics layer like this would ensure that metrics are consistently calculated across every tool that connects to a database. By calculating metrics on demand, it uncaps the number of possible Mad Lib combinations that people can request. And by rendering directly as SQL, it’s extensible if an analyst needs to use a metrics query as a starting point for deeper, more complex analysis.


Most profoundly, though, it fundamentally redefines how data is consumed, and the role BI plays in that process.


At first glance, the metrics layer doesn’t feel like a BI tool. This is code! BI tools have drag-and-drop interfaces! But that misses the point of those drag-and-drop interfaces, which is to make data accessible. If the query language is simple enough, text-based commands can actually bemoreaccessible than the complex “code-free” UIs of tools like Tableau. We Google, after all, with nothing more than text.


That doesn’t make BI tools obsolete; it just shifts them a different, and potentially more valuable, role. With a metrics layer, analytics tools can worry less about data modeling and governance and focus on creating a great experience for issuing metrics queries, for visualizing their results, and for extending those results with deeper, analyst-led explorations. In this world, BI is a creative workflow that supports analytical development and collaboration—realizing the actual value in data—rather than a piece of infrastructure centered around data governance and reliable reporting.


That, ultimately, is the biggest benefit of a metrics layer: It completes the foundation on which operational BI and exploratory data science both live, bringing these two functions together in ways they can’t be combined today. Without a central metrics repository, these two workflows—metric extraction in one case, and complex strategic research in the other—will remain apart. Even if they share the same database and the same transformed tables, the stories they tell will be inconsistent until they share the same metrics.


Update: Shortly after this post came out, Airbnb published an article about Minerva, their internal metrics layer. My thoughts on it arehere.

[1](https://benn.substack.com/p/metrics-layer#footnote-anchor-1-35493960)

Mode is the tool around which the modern data stack spins.

[2](https://benn.substack.com/p/metrics-layer#footnote-anchor-2-35493960)

This monitoring function, which is still finding its footing, is evolving in curious ways. More on that in a later post, probably.

[3](https://benn.substack.com/p/metrics-layer#footnote-anchor-3-35493960)

And there area lotof new companies. YC alone funded 43 data companies in 2020, up from 11 in 2015.

[4](https://benn.substack.com/p/metrics-layer#footnote-anchor-4-35493960)

lol, a five-year-old Brexit joke.

[5](https://benn.substack.com/p/metrics-layer#footnote-anchor-5-35493960)

omg, Brexit was five years ago.

[6](https://benn.substack.com/p/metrics-layer#footnote-anchor-6-35493960)

As I mentioned in the piece on the problems with self-serve, this isn’t without its challenges. While Looker will compute the same configuration the same way every time, it’s difficult for people to always arrive at the correct configuration if there are a lot of options. People are just as easily overwhelmed by choice as they are technical hurdles.

[7](https://benn.substack.com/p/metrics-layer#footnote-anchor-7-35493960)

After getting interested in this topic, I made a personal investment in Supergrain, so I now have some bias in this area. That said, as someone who’s made an enormous personal investment in Mode, which is somewhere between adjacent to and overlapping with most pieces of the data stack, I’m directly or indirectly biased about nearly every modern data tool.
