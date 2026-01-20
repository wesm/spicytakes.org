---
title: "Has SQL gone too far?"
subtitle: "The case for better business models."
date: 2022-04-15T16:41:38+00:00
url: https://benn.substack.com/p/has-sql-gone-too-far
slug: has-sql-gone-too-far
word_count: 2268
---


![](https://substackcdn.com/image/fetch/$s_!-aAU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6cb6d63-ae28-4bde-b241-0bc2f4d9719e_1480x833.jpeg)

*Hang on a minute…*


Death, taxes, and SQL.


Amid all of the growth, upheaval, and reinvention in the data industry over the last decade, the only durable consensus has been our appreciation of SQL. Every time we flirt with some NoSQL alternative, we end up rebounding back to SQL. Every time someone puts out a new proprietary rewrite—JQL,NRQL,Juttle—the community responds with the same pleading reaction:Please stop doing this.


Remarkably, our attachment to a half-century old technology isn’t inspired by some Churchillian acceptance of our lowly lot in life—“SQL is the worst way to interact with data, except for all the others that have been tried.” No, it’s an active advocacy, in which we don’t want to just protect SQL’s current beachhead as the dominant way to extract and manipulate data, but also want to expand its reach further: SQL forAI; SQL forreal-time applications;1SQL fordata pipelines.


Of course, few people would claim that SQL is the best language for everything. I haven’t seen anyone argue that we should use SQL to describe a data visualization, or to create complex statistical forecasts. No matter how deep our affection for SQL runs, we know—obviously and uncontroversially—SQL has limits.2


As a technical luddite who still can’t make conceptual heads or tails of how to do anything with a Pandas dataframe, I’ve long been an advocate of pushing those limits.3I’ve worked almost exclusively in SQL for much of my career; just asEnglish defines how I see the world, my understanding of data has been rewired around relational notions of tables and joins.Some people think in sentences, some in non-verbal thoughts—and data people, it seems, think in SQL. The more we can do in our native language, I’ve long thought, the easier our jobs will be.


In recent weeks, however, my faith has started to waver. Perhaps,perhaps, we’ve overreached. Perhaps, to nail a disputation on the church door,4one of the core responsibilities of a data team—modeling a business, and defining a semantic layer—is best done in another language.


# Business models aren’t relational models


After years oflanguishing in the backend of BI tools, semantic models—the set of definitions and specifications that inject raw data with meaning, like a formula that determines how to compute revenue from a list of credit card transitions—are having a moment. In the last twelve months alone,Looker branded themselvesas a “universal semantic model;”dbt declaredthat a semantic layer is the next layer of the modern data stack; AtScale said that the universal semantic layer ismore important than ever; andmultiplecompanieslaunched dedicated semantic layer products. To cap it off, not only has anew roleemerged to maintain the semantic model; it was proposedas the world’s sexiest job.


The recent trendiness of the semantic layer runs parallel to that of SQL. dbt championed the idea ofmodeling data in SQL; dbt’s popularity galvanized the creation of a transformation layer; the importance of that layer gave rise to analytics engineering; all of these things together coalesced into a universal semantic layer. As a result, today’s semantic layers are inseparable from SQL itself.


More concretely, in this modern, dbt-inspired construction of a semantic model, a user is defined by the hand-written query that creates a users table; revenue is defined by the similarly manual query that computes it. This structure has two big benefits: It’s accessible, and it’s fast. Anyone who writes SQL can both understand and extend it. Moreover, business concepts are rendered as tables, whichare conceptually easy to understand.


This type of semantic layer has its problems, though. Most notably, there is notruemodel. Queries are related to one another through a simple lineage graph, not through any sort of semantic definition. If you change the segments that you sell to, you have to update every query that uses the outdated segmentation.5


In other words, defining a semantic layer in pure SQL is like animating a movie by hand. Lots of people can make a simple flipbook, and make it quickly. But to add a new character to an existing scene, you have to redraw every frame. The more intricate the scene, the more tedious that work, and the easier it is to draw the new frames inconsistently.


A different approach is to create a Pixar movie. Pixar’s animators don’t have to draw Woody into every shot; instead, they define each scene with an underlying model, which renders every frame consistently. It’s more work up front, but—if you know how to writePresto6—it’s more reliable to maintain.


Most BI tools, fromMicrostrategytoLooker, follow this pattern, as do some metrics layer vendors likeTransform. In all of these products, analysts construct a semantic model by defining how tables in a database are related, and how those tables should get aggregated into metrics. When people interact with these tools, the semantic model translates requests for a metric or dataset into a SQL query. If segments need to be redefined in this framework, they can be updated in the model, and every subsequent translation would use the new definition.


At their core, however, these tools are just thin recipes for SQL queries. In LookML, for instance, you can almost seethe SQL query peeking through. Joins between tables are defined explicitly; metrics are slightly doctored snippets of SQL syntax. In this regard, these semantic layers are little different than dbt—they both rely, wholly and completely, on us telling the layer what SQL to run.


But lots of business concepts aren’t easily defined this way.Consider, for instance, a sales funnel in which prospects move through a series of stages, like “In trial,” “Contract negotiation,” and “Under legal review.” These stages often have a expected order, but not a strict one. Some prospects skip stages, some proceed through them in a different sequence, some stages happen concurrently, and sometimes, if a sale cycle goes sideways, steps get repeated.


How do you model this funnel in SQL? How do you write a query that computes how long legal teams typically take to review a contract? How do you express the semantic nuances of this business process in LookML?


For most companies, the answer, I suspect, is you don’t. Rather than writing a web of queries that handle all of the possible intricacies and edge cases, you model a simplified sales funnel that you know isn’t real, and accept that some prospects, like those who repeat stages or proceed through them in an unconventional order, will get miscounted. Metrics come with a caveat—”This assumes every closed account entered a trial prior to purchasing.”


In some cases, these approximations are probably fine; the only perfect map of the territory is the territory itself. But, given the increasing importance of semantic layers, especially their aspirations to be the universal arbiter of the capital-T Truth, these fudges—rooted in the limitations of SQL—could become very problematic.


Which leads us to the heretical conclusion: Just as SQL can, but shouldn’t, be used to define complex statistical analysis, perhaps SQL can, but probably shouldn’t, be used to model the complex operations of a business.


# BusinessML


Two tools offer a glimpse of a different path forward. The first is actually dbt. Though most code in dbt is SQL, it’s not just SQL—there’s a lot of Jinja too.


In the dbt projects I’ve seen, Jinja is most often used as a kind of programmatic shortcut to generate queries that people would otherwise write by hand. For instance, instead of writing five repetitive lines of SQL to parse each individual UTM parameter from a URL, dbt developers will write a Jinja loop that does it in a single line. It’s not,as Tristan says, that you couldn’t write the same query without Jinja; it would just be painful to do it. But it’s easy to imagine this going much further, where dbt developers stop thinking in queries and instead think in Jinja.


Consider the sales funnel again. To model this funnel in dbt today, I (and I assume others) would first think about how to model it in SQL. If there were repetitive steps, like a bunch of joins of thesalesforce_stagestable onto itself, I’d simplify those with a Jinja loop. The logic behind this model, though, would be expressed in SQL, and my ability to model it would go only as far as the cleverness of what I could do in a query.


Could Jinja, or some forked version of it specifically designed for expressing business logic in dbt, help me go further? Could I define this sales funnel in this language—these are the stages, these are how prospects progress through them, these are the steps that can be skipped—and rely on dbt to figure out how to turn these nested relationships into SQL for me? With marcos and metrics already tilting in this direction, it certainly seems conceivable that our dbt projects become less and less SQL and more and more Jinja, just our web applications are less and less HTML and more and more React and Rails.7


The second tool exploring this idea is Malloy, an open source project led by LookML creator Lloyd Tabb. Whereas LookML is built on join relationships and SQL snippets, Malloy is built on direct expressions of business logic.


This has two big potential benefits over LookML. First, because these logical expressions can be layered on top of each other like functions, Malloy is much more composable than LookML. To extend the Pixar analogy, in LookML, you can model a car into a scene, and that car will appear consistently in every frame of that scene. Malloy goes further—it lets you define the concept of a car, which you can then add to any scene in the entire movie.


Second, just as a heavily Jinja-ified dbt could write more complex queries than we’re able to as people, Malloy writes SQL that better retains the realities of the business logic it’s meant to represent, which is often SQL that an analyst would never write themselves. For example, nested relationships between entities—this city is part of this state, this state is part of this region—aremaintained as nested relationshipsin the results Malloy returns. This provides a path for solving the sales funnel problem: The funnel could be defined as a logical expression in Malloy, and Malloy figures out how to write the ugly, recursive query that is necessary to describe that funnel accurately.


We could actually go one step further though. While Malloy and an evolved dbt would both create, in effect, a new language for modeling business logic, they’re still rooted in SQL. The logic they can express is constrained by the SQL they can write. On the edges, there are surely business concepts that can’t be expressed in SQL at all, no matter how many clever window functions and self-joins we use. Or, there are processes that can be defined in this way, but can’t be queried performantly.8


This opens up yet another type of semantic layer: One that doesn’t render to SQL at all.


Admittedly, this an ambitious endeavor, as it requires creating a new database that can be queried via a language other than SQL. But if you can pull it off—and companies likeRelationalAIare attempting to do exactly that—it allows for much more complex (and performant) expressions of business logic.


Though this may seem like a marginal improvement, consider it in the context ofGeorge’s recent Twitter thread about Lyft. As George tells it, Lyft turned major parts of their business around by building a growth model of their operations, and leaning on that model to make decisions. We would all benefit from these sorts of models, but we often don’t build them—and rarely create them into the semantic layers that are supposed to underpin every decision we make—because they’re nearly impossible to express in SQL. If they exist at all,they usually exist in Excel.


The promise of something like RelationalAI is the ability to create that model more easily and to embed it directly into the semantic layer. It is to pull out the logic that’s buried in load-bearing Excel files—the weekly forecasting sheet, the master marketing funnel workbook, the global growth model—and make them accessible to every analyst and data application in a business.


Of course, none of these ideas are entirely new.9Semantic modeling languages have come at the king for decades, andthey’ve all missed—SQL still sits on its throne.


Every once in a while, though, that which is supposed to be certain, isn't. A year ago today,it was taxes. This weekend,it's death. And next year, it may well be SQL.

[1](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-1-52282421)

I’m apersonal investorin Decodable.

[2](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-2-52282421)

…get it?

[3](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-3-52282421)

I’m also a purveyor of aSQL-based product, so I’m not exactly unbiased here.

[4](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-4-52282421)

Quick, while he’s gone, question everything!

[5](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-5-52282421)

You could, in theory, architect a dbt project such that every bit of segmentation logic cascades from a single model. That’s very hard to do though, and it’s nearly impossible to do, simultaneously, for every one of the dozens of other business concepts that you’d want to cascade down in the same way. In practice, a few core concepts will get defined at the beginning of the lineage graph, while others will get scattered across it.

[6](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-6-52282421)

Wait, what?

[7](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-7-52282421)

For what it’s worth, I’d argue there are very big downsides to doing this in today’s Jinja, which isn’t really designed for this. But Jinja could change.

[8](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-8-52282421)

A third of the time I write a self-join it works, a third of the time I completely butcher the logic, and a third of the time I forget some join condition, fan an event table out into whatever a trillion times a trillion is, and bring down the database.

[9](https://benn.substack.com/p/has-sql-gone-too-far#footnote-anchor-9-52282421)

In particular, Microsoft hasdone it all before.
