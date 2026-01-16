---
title: "BI by another name"
subtitle: "Taking stock of the new semantic layers."
date: 2023-05-05T15:48:01+00:00
url: https://benn.substack.com/p/bi-by-another-name
slug: bi-by-another-name
word_count: 2622
---


![Comcast Xfinity Opens WiFi for Free to Connect Low-Income Families &  Students | Moody on the Market](https://substackcdn.com/image/fetch/$s_!7nNH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d04a872-605b-4220-b77f-e09f6778dfff_6000x3375.jpeg)

*Xfinity: StillComcast.*


There are two important parts to a universal semantic layer. The first is the semantic part: The layer needs to define various business concepts likerevenue, accounts, users, andnet income per home minus fake stock-based expenses. Most companies have a bunch of raw data that needs to be cleaned, joined, and aggregated before it can be used in meaningful ways; semantic layers are, roughly speaking, giant computational formulas that do that cleaning, joining, and aggregating.


When we talk about universal semantic layers—aswe have been recently, following somesignificant updatesfrom dbt Labs,LookML’s secessionfrom Looker, the community’scontinued curiosity about Malloy, andafrenzyofpredictionsaboutLLMs—this is the part we tend to focus on. We question if these new semantic layers can handle the logical complexity of our businesses. We ask if they should be created by humans or AI. We debate new configuration specs. We talk about how semantic layers should be developed, deployed, updated, and versioned.


Important as these things are, they’re only half of a universal semantic layer. In addition to encoding semantics, universal semantic layers also need to be universally accessible.1So far, most semantic layers meet this requirement by being queryable by generic APIs. You define your net retention rate inMetricFlow; you can now request various pivots of it via a Python library. You specify how to count daily active users in some YAML file in your dbt repo; you can now query that metric via a dbt Labs’ JDBC driver and a SQL-like language. You make up a rule for calculatingcommunity-adjusted EBITDA before growth investmentsin Cube; you can now commit securities fraud through Delphi’s conversational interface in Slack.


This approach means that data teams can choose whatever combination of BI tools and semantic layers they want. Want to stay in the Google ecosystem but like Cube? Use Mode and are intrigued by dbt’s acquisition of Transform? Want to migrate from PowerBI to Tableau without replacing AtScale? Today’s universal semantic layers support this kind of mix-and-match modularity.


For a while, I’ve assumed—along with everyone else, it seems—that this fulfills universal semantic layers’ universal requirement. ButCarlin Eng has concerns:


> Analytical freedom is severely limited. Since data from the metrics API is already aggregated, there’s no way to drill into specific records, or create on-the-fly dimensions and measures to slice the data in a way that might reveal new insight. You can request other dimensions from the metrics layer, but what if the dimension you’re interested in doesn’t exist yet?


Put differently, the interface into today’s semantic layers are all more or less the same: Ask it for a metric; specify some filters, dimensions, and secondary calculations like a ratio or rolling average; it gives you a table with those results. Different semantic layers have different query syntaxes (including natural languages), but structurally, most of them are fundamentally about extracting a metric or dataset.


As I’ve argued before, this type ofmetric Mad Libsis great for self-serve becauseit’s an easy way to understand data. But, quoting Carlin again, it “falls flat when the analyst needs to do critical work like debugging misbehaving metrics, or more creative data work such as exploratory deep-dives.”


Presenting data in this way—in a tidy, consumable, andconstrainedformat that’s accessible to everyone—is typically what BI tools are for. In other words, today’s independent semantic layersaren’tuniversally accessible encodings of business logic that can be used by any downstream analytical application; they’re BI tools, without charts.2


Which makes sense! That’s exactly how we created this generation of semantic layers—BIwithout a head; LookMLwithout Looker; the logic boxremoved from the BI box. But, it’s hard to see how this type of semantic layer gets adopted that widely. For a lot of customers, moving away from their BI-based semantic layer is a major undertaking. What’s the point of doing that work if the primary benefit is…to connect your new semantic layer to the same BI tool? Whyinvest in an general solutionif it’s only going to work for one application?


To be clear, even in its current form, I’m still in favor of the move towards universal semantic layers—companies often have multiple BI tools, and building them on top of a shared OLAP cube is better than building each one having their own.3I think it’d be beneficial for companies to migrate to this architectural paradigm, and Mode is invested in doing its part to make that possible. But we also have to acknowledge the obstacles that get in the way of that effort. And I’m starting to think that this is the biggest—that today’s semantic layers are mostly applications for metric extraction that might make our BI tools better, but they don’t make our entire data platforms better.


An ideal semantic layer would go a lot further. It would support more than reporting and self-serve analysis; it would even support more than the analytical work that Carlin referenced that’s done outside of traditional BI tools. Done right—and, fair warning for what’s coming,I don’t know how to do this—it would also provide a means of governance for entirely new ways to interact with and reason about data.


# Universal need, individual preference


If you ask people what their favorite app is that nobody else would say, everyone says their to-do list of choice.4Someone will say Apple Notes, because it's so gracefully simple. Someone will say Notion, because it’s the perfect combination of functionality, ease, and millennial minimalism.5There are the Evernote holdouts, Todoist zealots, and overachievers who built their owncustom-designed, one-of-a-kind bespoke app. And someone will be an actual contrarian and say TextEdit.


People choose this class of app as their favorite—but invariably choose different ones—because the problem they solve is universal, but the solution is personal. Everyone thinks in different ways; their notes and task lists need to reflect that.


Some people think in a “robust latticeworks of mental models” and need avector database of Markdown docsto organize the contents of their galaxy brains. Some of us are one-track luddites who can only think linearly, and can’t handle anything more complicated than a single list of uncategorized tasks. Some are synesthetes who want to color-code everything. Some are theinbox zero addicts, and some are quantified selves whotrack and measure their to-dos’ pipeline velocity; some are hoarders who need to save every task and others are obsessive-compulsives who live for the hit that comes with backspacing through a completed task. Some people choose beauty and useBear; some people choose spartan simplicity and use a mono-spaced code editor; and some lunatics choose chaos and useStickies.


Because of these differences, the market never settles. It’s winner-take-very-little, for the same reason that the fashion and car markets are: People use to-do lists to do different things, and have different personal preferences about what they like.


The same, I believe, applies to data consumption tools. Lower in the stack, in ETL products, in data warehouses, and in emerging applications like data contracts, data tools mostly interface with each other. In these systems, there’s an incentive to coordinate. If we can agree on standard protocols, everyone’s life gets easier. Tools can coalesce around emerging defaults, the best pairings reinforce each other, and the market consolidates. A reverse ETL tool’s “preference” for the kind of database it reads from is whatever kind of database most people use.


The front end, by contrast, is the interface between technology and humans—and people won’t ever agree on the best way to do anything. Some analysts will always like code; some will prefer pivot tables. Some people squint atdecks of time series; some want dedicated tools for analyzing A/B test results; some like funnels and Sankey diagrams; and others will want tododge regulatory oversight by rigging regulatory modelsin spreadsheets. As is the case with to-do list apps, these inconsistencies don’t reflect the thrash of an immature market; they’re real and permanent differences of opinion and preference.6


There is, however, one very tricky distinction between data consumption tools and to-do lists: Data tools need to sit on a shared source of truth. People may want to interact with data in different ways, but they want the data they’re interacting with to be the same.I may want to play with a table of users in Excel, you may want to build a user retention model in Python, a marketer may want to walk throughuser journeys in Amplitude, and a product manager may want to useMotifto find patterns in how users behave. But all of us want our users to be the same.


In theory, this is exactly what a standalone semantic layer is for: Consistent business logic, universally accessible.But today’s semantic layers probably can’t do this.A time series of a metric can’t be pivoted into a funnel, no matter what dimensions you add to it. A free-form spreadsheet is incompatible with the structured tables in a relational database. A domain specific language like Motif, which provides a shorthand for analyzing sequences of events, can’t get passed throughMalloy, a relational modeling language. Our tooling preferences reflect fundamentally different models for interacting with data, and they can’t all be shoehorned into a framework of dimensions and measures.


This is what a semantic layers would ideally be—a place that creates organizational structures and computational shortcuts that can be consumed by any type of data tool. It could power the A/B tests in Eppo, the forecasts in Anaplan, and the user flows in Mixpanel. It could sit underneath Malloy and Motif so that people who learn and like those languages could use them without needing to recreate another semantic model in each tool. It could work in spreadsheets.


Unfortunately, I genuinely don’t know how to do this. How do you add governance to a spreadsheet? How do you ensure that experimental languages use the same computational logic when calculating a metric? It all seems very hard. But there are two success stories that might hint at a couple possible solutions.


The first is dbt Core (i.e., the open source dbt Labs product that creates tables in databases). You can put dbt Core in front of every tool that sits on top of a database because dbt Core defines the data that’s in the database. The logic in dbt Core is automatically picked up by Malloy, Motif, and every spreadsheet with a JDBC connection because, if you’re using data, you’re using dbt Core. In this sense, it is a universal semantic layer; it’s just one that can encode entities but not computation.


The second hint comes from SQL itself, which is actually the inverse of dbt Core. It encodes computation, but not entities. It’s also universal—you can’t get to the data in a database without going through a SQL query first.


An aspirational semantic layer would retain both of these properties. Is that SQL, with semantic functions? Is it a new type of database that supports computationalDDL? Is this already supported by mixing MetricFlow with raw SQL? Is it justMalloy? Is this DAX? Do these questions even make sense?7


Honestly, I’m not sure. But I’d guess that this will be the next challenge for universal semantic layers. So long as they operate as applications for governing metric extraction, they’ll only be able to serve products that primarily need to extract metrics. Other tools—those that need computational flexibility, and that want to create new ways to interact with data—will likely ignore the semantic layer, or create some version of their own.


# The pedantic layer


At this point, some of you may be thinking, “Didn’t you propose exactly the thing you’re saying is incomplete? Wasn’t this whole metric thingyour idea in the first place?”


First, who can say how we got here;we’re all trying to find the guy who did this. Second, something somethingfacts change. And third, there’s some nuance here that’s worth calling out.


As it was originally conceived, a metrics layer was really just a collection of formulas. It was, as the name suggests, a tool for encoding metrics. If you need a metric, write a query with some special syntax; the metrics layer, which could be a SQL proxy or some library of stored procedures, gets you that metric.


I think the problem emerges when this tool gets promoted into a semantic layer. To me, semantic layers are meant to encode everything—relationships, metrics, entities, and so on. This often means that you are either querying through the semantic layer, or not at all.8If this is the expected behavior—which I'd argue the name encourages—a limited semantic layer isn’t that useful, because any analytical work that the semantic layer can’t handle will have to bypass it.


And that’s ultimately the point of this entire post. If we’re going to build universal semantic layers, they have to be flexible enough—like SQL itself—to work with tools that present data in a range of different ways. Otherwise, we’re not building semantic layers; we’re building BI tools by another name.

[1](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-1-119475953)

I realize I’m making the bold claim here that universal semantic layers need to be universal and have semantics. Next week, a post about how large language models need to be large and have languages.

[2](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-2-119475953)

Suppose that, in 2013, you were cursed by an evil sorceress andfell into a deep sleep for ten years. When you woke up and asked what you missed, your (very unfortunate) true love told you that people don’t use MicroStrategy for BI anymore, and instead a thing called the dbt semantic layer with a thing called Mode sitting on top. Which of those two tools would you say is the new BI tool? Is BI’s essential element governance, or exploration? If you ignore the two tools’ paths to their current spot in the stack, I’m not sure the answer is very clear.

[3](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-3-119475953)

Here’s a fun example. I once heard that, among three of the largest BI tools, vendor A’s biggest customer is Walmart. And Vendor B’s biggest customer is Walmart. And vendor C’s biggest customer is Walmart.

[4](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-4-119475953)

There has to be a world for this, right? What do you call a seemingly contrarian take that everyone agrees with?


On a related note, please take thisvery important survey.

[5](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-5-119475953)

Thirty-somethings love software with gentle san serif fonts, off-whites and dark grays, and buttons that fade in on hover.

[6](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-6-119475953)

In some cases, I’d argue that it goes even further than this, and the tools you use affect how you conceptualize what datais. Academics who grew up using R or Pandas think in arrays and data frames, in variables and functions. I've spent most of my career in SQL, which encourages me to think on rows, columns, tables, and joins. When I'm asked a question, I reason about it through that structure: What intermediate tables do I need to create, and what aggregations and joins will help me create them? My thoughts are shaped by the English words that I use to describe what I'm feeling; my analytical reasoning is shaped by the linguistic concepts I use to describe data.

[7](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-7-119475953)

Am I asking for things that already exist?I have no frame of reference here;I’m like a child who’s wandering into the middle of a movie.

[8](https://benn.substack.com/p/bi-by-another-name#footnote-anchor-8-119475953)

For example, in Looker, you either use LookML or write a query; there’s no blended option. Most semantic layer APIs function the same way. You don’t compose a query with a metric inside of it; you just request an object that’s defined in the semantic layer. (I have a similar concern about Malloy as well. Because it replaces SQL rather than decorating it, there aren’t really ways to gradually adopt Malloy or ease up its learning curve. Even if it technically solves the problems described in this post, that’s only half the battle. You also have to get people to use it.)
