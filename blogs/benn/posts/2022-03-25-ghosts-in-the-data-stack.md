---
title: "The ghosts in the data stack"
subtitle: "An OLAP cube exorcism."
date: 2022-03-25T17:47:45+00:00
url: https://benn.substack.com/p/ghosts-in-the-data-stack
slug: ghosts-in-the-data-stack
word_count: 2252
---


![](https://substackcdn.com/image/fetch/$s_!3pP6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb875e474-00b1-4b41-9ce2-fb2ba4214782_1400x1050.jpeg)

*Do not make a SQL pun, do not make a SQL pun, do not make a seque-*


Data,Vicki Boykis tells us, is full of ghosts. Teams, organizations, and the analytics industry at large are haunted by implicit knowledge—knowledge that “exists within expert communities but is never written down." What it actually means to clean data, how to navigate the politics of influencing decisions, how to evaluate and purchase software—these are the things data professionals need to know but are never taught. And they’re the things that, once you discover, you forget how you learned.


OLAP cubes are another such ghost. Despite being a foundational piece of data technology, they’re mostly ignored by today’s data community. Despite being frequently referenced in marketing white papers, technical blog posts, and Gartner’s numbing cocktails of buzzwords and acronyms,1OLAP cubes are uncomfortably difficult to define. Wikipedia offers a brief, self-referential definition—an OLAP cube is a multi-dimensional array of data—and refers us to anacademic paperon databases for more information.OLAP.com, a website presumably dedicated to the promotion of OLAP cubes, tells us what they do (“a data structure that allows for fast analysis”) and what they’re not (OLAP isnotOLTP).


Last year, Claire Carroll, motivated by exactly this ghost—she quotes aTwitter userwho says “the ratio of ‘number of articles I have read about OLAP cubes’ to ‘amount of understanding I have of them’ is truly outrageous”—finallygave us a worthwhile definition. OLAP cubes are just tables, but tables structured in a very particular way.


When we think of a table of data, we instinctively think of it as a list of objects. Each row represents some discrete concept: a person, a purchase, a campaign donation, an action taken on a website, a pitch thrown in a baseball game. Not only is it easy to imagine how someone might collect this data—when a person buys something, add that purchase and various details about it to the ledger—but it’s also intuitive to manipulate. To count the number of individuals in a table of people, count the rows; to find purchases of a particular product in a transactions log, search for the entries for that item; to calculate the average donation from a list of campaign contributions, average the “donation amount” column.


![](https://substackcdn.com/image/fetch/$s_!KrXL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9dc0a02d-a88e-4ce6-b8a4-520fc6342414_1600x594.png)

*This is a purchases table, and we all know what it means.*


As sensible as tables like these are, they can also get quite large—large enough that, twenty years ago, performing these simple operations on them was impractically expensive. Just counting the number of items sold in a table of purchases, for example, could take minutes or hours; more complex calculations, like computing median sales prices by state, could take far longer.


OLAP cubes—i.e., tables of a particular structure—were created to solve this problem. Rather than a list of objects, OLAP cubes are a table of metrics, or “measures,” pre-aggregated across nested layers of groupings, or “dimensions.” In the example below, the table of raw purchases is aggregated by month and state. There’s a row for each possible combination (say, January and California, or February and Ohio); each row includes metrics on that pairing, like the number of items sold and the total amount they sold for.


![](https://substackcdn.com/image/fetch/$s_!wVfm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7c82cec5-c107-48bc-a12c-75110fd1eec0_812x558.png)

*An OLAP cube.*


While this table itself isn’t directly useful, people can aggregate it again to produce more traditional reports. If you want to count the total number of purchases, sum the column of items sold. If you want to tally sales in California, filter the table to just the rows where state equals California. And for more complex operations, you can aggregate the data across multiple steps. To find the average number of items sold in a month, first sum the table by month to create a twelve row table of total items sold in each month; then average those totals into a single number.


This is more complicated than working directly on top of the original table, but it has one enormous benefit: It’s fast. No matter how many orders you process, the OLAP cube in the example above can never be more than 600 rows long—fifty states times twelve months. Computers, even those from decades ago, can easily work with tables of this size.2As a result, most legacy BI tools were centered around OLAP cubes. BI administrators would define the cube in the tool, it would get precomputed on a regular cadence, and everyone else would create reports by manipulating and pivoting the data in the cube.


OLAP cubes were also limiting, though. Details get lost when raw data is grouped into pre-calculated aggregates. If you wanted to cut your data by a dimension that wasn’t precomputed, or if you wanted to see a list of the six purchases made in Ohio in January, you couldn’t do it. Compressing data, it turns out, isn’tlossless.


But there’s another, much less discussed downside to OLAP cubes:They’re very difficult to understand.Unlike a standard table, an OLAP cube doesn’t describe a tangible concept. It isn’t a list of objects or reportable metrics; each row, rather than representing a straightforward noun, is a combinatorial abstraction. It’s a middleman, an assemblage of computational scaffolding that can only be understood through its relationships to the raw data underneath it and to the reporting needs above it.


This structural weirdness is obvious in any BI tool that’s built on top of an OLAP cube. The screenshot below shows howMicrostrategy presentstheir cube to its users. Itfeelslike building a pivot table in Excel. But look at the fields: Customer, day, item, metrics, % change units sold, cost per unit, last year’s profit. What underlying table would have all of these fields?


![](https://substackcdn.com/image/fetch/$s_!Jr5T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4a189f21-91c2-4598-8026-6ac3d26f1689_1600x995.png)


No single table, as we typically conceive of one, would. And that’s the problem—OLAP cubes aren’t a normal table. They’re “multi-dimensional arrays of data,” and we can’t intuitively make sense of that.


This, I believe, is what makes OLAP cubes one of Vicki’s ghosts. You can’t look at one and understand it on its own. It has to be defined in context—in the context of the data it describes, and in the context of the technical limitations that necessitate it.


# The OLAP cube is dead, long live the OLAP cube


None of this was supposed to matter anymore. As Claire mentioned in her post, OLAP cubes are no longer popular. Modern databases like Redshift, Snowflake, and BigQuery are large enough to count (and do much more complex operations) on top of very large datasets. People can now compute metrics on top of raw tables nearly as quickly as they can against OLAP cubes.


But, like any good ghost, though they may not exist in the physical form, OLAP cubes are spiritually very much alive.


Consider Looker, for example. Looker was one of the first major BI tools to fully discard the OLAP cube, and run its queries directly against the underlying database. In doing so, however, Looker changed howBI tools interact with data, but they didn’t change how people interact with BI tools.


LookML, the configuration language underneath Looker, is, in effect, a recipe for running a query. It defines how raw tables are related to each other, how they should be aggregated to compute various metrics, and the dimensions by which those metrics can be grouped. In an OLAP infrastructure, this configuration would be used to build an OLAP cube; metrics and reports would then be computed on top of that cube. When people use Looker to create a report, it does both of these steps at once. If you ask Looker for sales by month, it creates a query that extracts this metric directly, with LookML providing the instructions for how to do this.


Despite changing the engine,Looker’s UIis the similar to Microstrategy’s. Just as Microstrategy presents fields as collections of dimensions and measures to be explored, so too does Looker. And just as this presentation makes it hard to understand exactly what underlying object is being manipulated by these fields—it feels like a table, but definitely isn’tjusta table—so too does it in Looker.


![](https://substackcdn.com/image/fetch/$s_!CB4u!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6f8705a2-da50-4020-8219-ed77398a5dc4_1600x1056.png)


The BI landscape is full of interfaces like this.Tableau presents datain this way,as does Power BI.3Even metrics layers like Transform function similarly:Configure how your data is structured, and present those resultsas dimensions and measuresto be explored.4


On one hand, this makes sense. A LookML data model, like an OLAP cube or a Tableau extract, isn’t a simple table of users or customers. It’s a more complex data structure, and the UI reflects that. On the other hand, these data structures are confusing, and BI tools don’t have to create interfaces that mirror the architectures that sit underneath them. Rather than displaying data as we model it, we should display data as we use it.5


# What we think of when we think of data


Early in my career, I worked for a think tank in Washington, D.C., where I helped write a weekly newsletter about the global economy.6The posts were quantitative, and required a fair amount of data analysis. We relied on government data sources, and I, as someone who had never even heard of SQL at the time, relied on those sources’ drag-and-drop web portals to get the data I needed. I was, in other words, the business user to the government’s BI tools.


Two websites easily stood out at the best. The first wasFred, the data platform of the St. Louis Fed. What makes Fred great is its simplicity: It’s just agiant listof economic indicators. I didn’t know what the data sources behind Fred looked like, nor did I ever care. All I had to do was search for a metric.


The second website I liked was theIMF’s World Economic Outlook database.7Unlike Fred, the IMF site didn’t ask you to choose a metric; it helped you build a dataset. You chose the category of economic statistics you wanted to see—you had choices like trade balances, financial indicators, and GDP and output statistics—and picked the countries and regions you wanted to see them for. The website would then generate a big table for you, with one row per country, and one column per indicator.


![](https://substackcdn.com/image/fetch/$s_!POMZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F014e4d97-84f0-4d8b-bee2-3f945913860c_1600x1512.png)


![](https://substackcdn.com/image/fetch/$s_!UW-e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1248678-1b1b-4b54-b49c-2a90b1dab62d_801x450.png)

*Where I spent my early twenties.*


These websites were great because they presented data in the two forms that I understood it: As a metric, or as a table. While I’m sure the data underneath my requests was complicated and intertwined—there may have even been an OLAP cube or two in there—these websites hid all of that from me. Their interfaces matched the way I asked questions: Show me this metric, and help me create that list of countries.


Contrast this with theCensus’s website, the worst government data portal. The Census offers a bunch of topics for you to “explore.” Because data is organized by source (i.e., the survey from which it was collected) and is presented in nested pivot tables, to use the site, you have to have some understanding of how the Census collects its data, and how different topics are related to one another. Even basic numbers, like population statistics by state, are difficult to find.8


![](https://substackcdn.com/image/fetch/$s_!e_Jb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9db69509-9ee8-4c77-b747-bce4d739a592_1600x886.png)

*Nonoperational analytics.*


Most BI tools look like the Census site. They expose data as it’s defined, through a thin GUI around a complex OLAP cube. A better solution would hide the implicit structure of the data behind the tool, and instead speak the language of those who use it. It would replace wide-ranging explorations with simple methods for finding metrics, and for creating flat, intuitive datasets.


This might seem like a step backwards.9It constrains how much you can explore, and splits unified self-serve interfaces like Looker’s into two separate flows. But, our goal as tool builders—either as those who build products, or those who are creating reports and dashboards for our coworkers—should be to rid what we create of Vicki’s demons, and make things that can be understood with as little implicit knowledge as possible. After three decades of trying with OLAP cubes, it’s time to give up the ghost.

[1](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-1-51031696)

The description of thisGartner reportis 208 words long. Thirty-eight are acronyms: SQL, SSAS, OLAP, OLAP, SQL, DBMS, BISM, SSAS, SSAS, SSAS, SSAS, OLAP, OLAP, BI, SSAS, OLAP, SSAS, GUI, SSAS, SSAS, BI, SSAS, OLAP, MOLAP, ROLAP, SSAS, MOLAP, ROLAP, UDM, SSAS, SSAS, SSAS, SSAS, SSAS, UDM, SSAS.

[2](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-2-51031696)

In practice, of course, most OLAP cubes are considerably larger than this. They contain more dimensions, like day of purchase and item purchased, and more metrics, like average sales price and total tax paid. But, contrary to my long-standing assumption that OLAP cubes were a special computational engine or some incomprehensibly complex matrix of numbers and Greek letters, larger OLAP cubes are structurally identical to the one above.

[3](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-3-51031696)

Modeuses a similar languageof dimensions and measures. For better or for worse, however, the data underneath Mode’s Visual Explorer is typically a flat table returned by a query rather than a table structured like an OLAP cube.

[4](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-4-51031696)

Webeheadedthe OLAP cube, and are now haunted by its ghost.

[5](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-5-51031696)

Conway’s corollary: The experience of using any product will be a copy of the product’s data structure.

[6](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-6-51031696)

It’s Tuesday, let’s talk aboutthe regional distribution of foreign exchange reserves.

[7](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-7-51031696)

Sadly, they’ve since replaced it with amuch worse version.

[8](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-8-51031696)

More precisely, with the Census site, it doesn’t feel like you’re finding data as much as you’recreatingdata. And that’s exactly the problem.

[9](https://benn.substack.com/p/ghosts-in-the-data-stack#footnote-anchor-9-51031696)

Not least of all because I’m saying that the most advanced tech companies in the world should take their design cues from a ten-year old “data portal” built by a financial NGO.
