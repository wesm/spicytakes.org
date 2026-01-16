---
title: "The data config"
subtitle: "A humble YAML file, with ambitions for more."
date: 2022-07-15T16:43:22+00:00
url: https://benn.substack.com/p/the-data-config
slug: the-data-config
word_count: 2082
---


![4,459 Organized File Cabinet Stock Photos, Pictures & Royalty-Free Images -  iStock](https://substackcdn.com/image/fetch/$s_!ieE8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef992eb-5d13-43e9-a653-236ef6ff4afc_612x344.jpeg)

*One file is better than thousands.*


This one might be a bad idea.


But it also could be a nifty toy, and in Silicon Valley,toys become the next big thing. So it might be a very good idea. If nothing else, it’s at least a simple idea, so let’s start there.


Nearly every asset that a data team creates—a report, a dashboard, a data model, a predictive forecast, you name it—is riddled with hardcoded bits of business logic. The query that transformspage views into sessionshas a number somewhere that determines if sessions end after30 minutes of inactivity, after an hour, or after some other period of time. Ad attribution reports define how soon an action has to happen after an ad click for that action to be credited to the ad.1Models that group customers into segments often contain fixed case statements that set the thresholds between small businesses, mid-market companies, and enterprises. Dashboards of active users filter out certain background events (like a user getting a push notification) that don’t count as true activity, and discard users with blacklisted email domains. When we classify users into different personas, we often group them with simple heuristics, like people who send at least ten messages in seven days are power users.


Data stacks are full of numbers, lists, and logical snippets that define these concepts. In the worst cases, these configurations are often duplicated across dozens of queries and data models. In the best cases, definitions are centralized in a few core models (e.g., customer segments are defined in a single query early in a dbt DAG), though new versions often leak out in ad hoc analyses.


This pattern creates one glaring problem, and one subtle one.


The obvious problem is consistency. Because it’s so simple to encode logic like this in queries—it’s just an integer in a where clause, or date in a join condition—we often lazily copy and paste them from one script to the next. For example, though we may recognize that we’re better off defining personas in dbt, doing so would require us to redesign a couple core tables, to pass the concept through several downstream models, and to document the whole thing somewhere. If we need to put together a report on personas for a board meeting tomorrow,  there’s no time to rework everything today. We can make it more durable later, we say; for now, let’s just add a case statement to the query and get the analysis done.


Once we do this—which we often do, especially for new concepts that first appear in one-off reports before becoming something we want to canonize—it’s impossible to keep the values of these variables consistent. As a result, specifications drift. One dashboard will put companies with 5,000 employees in the enterprise segment, one will say the cutoff is 2,500, and a third will label companies with 2,500 to 10,000 employees as enterprise, and those with more than 10,000 as strategic.


But there’s another problem with this pattern. Even if we manage to keep everything consistent, nobody outside of the data team can ever know for sure how these concepts are defined.


Take user personas again. When trying to understand why passive users are growing faster than power users, product managers first want to be reminded of the exact criteria that group people in one bucket versus the other. When building targeted email campaigns, marketers need to know if lurkers post no new messages, or just a few. When closing a deal in a fast growing account, sales reps should be aware if new users are those who signed up today, this week, or this month.


The answers to these questions might be centralized in a single user personas model. But they’re only accessible to people who know both SQLandwhich query has the SQL they care about. While data teams can usually figure this out,2very few other people can. So analysts get pestered to look it up.


Some data teams try to deflect these questions through documentation. Documentation is hard to maintain though, and it can almost be self-defeating: As soon as a team defines something like user personas outside of the code itself, there are now two versions of this logic—the query and the documentation—to synchronize. Once any part of the documentation goes stale, as it inevitably will, people stop trusting all of it.


Recognizing that data dictionariesdon’t really work, the industry recently turned its hopes towards fancy data discovery solutions that parse data pipelines and try to smartly surface their contents. These tools might eventually live up to their promise, but in the meantime, I’d propose a simpler (and dumber?) solution: A config file.


# Yet Another Modeling Layer


Instead of hardcoding values into SQL queries, what if we centralize them into a single YAML file,3much like developers do inconfiguration files for software applications? These values could be fixed numbers, like the ad attribution window, or they could be lists, like the array of lead channels that are considered outbound. Analysts could then reference these constants—as, for example,$ad_attribution_window_in_minutesor{var(‘excluded_domains’)}—in SQL queries, saving them from writing the literal values directly.


Structurally, this isn’t a new idea. dbt, which is the most natural place for such a config file to live, already supports a similar concept invariables. However, in my experience,4variables are most commonly used asruntimeparameters that people might want to change from one run to the next. It’s less common for teams to use variables to define fixedlogicalparameters.


I think we should, and I think we should do it a lot.5


Designing data lineage graphs is hard. To keep from repeating ourselves—to make sure user personas are defined in one and only one place—we have to be meticulous in how we construct our DAGs. The popularity of analytics engineering is in part a reflection of this complexity: Maintaining a stable architecture is a full-time job.


A config file takes pressure off of this design. Because models could repeat computations without repeating the variables that underlie them, we don’t have to be as careful about always including important transformations at the top of the lineage graph. We also don’t have to clumsily cascade fields from table to downstream table, and can instead reference variables from the config file as needed, regardless of the model’s position in the DAG.


Moreover, a config file helps remove the tradeoff between speed and durability. Today, it’s often difficult to introduce new concepts into mature graphs that haven’t anticipated where the definition of some concept might live. This forces a choice: Do the slow, upfront work to figure out the best place to define that new concept and how to pass it through the rest of the DAG, or ship it quickly in a one-off query. A config file offers a third alternative. We can simultaneously centralize variables without needing to rethink the architecture of the lineage graph.


# Transform workflows, transform industries


This is all interesting enough, and on its own, might be a marginally better way to use dbt. But the real value doesn’t come from stuffing more variables into dbt project files; it comes from what we could build on top of configuration files if people were to use them in this way.


Most importantly, these files could make logical variables accessible to everyone, regardless of their familiarity with SQL. A service (dbt Cloud or otherwise) could read the config, and create a light interface on top. Values and lists, like which device types are classified as mobile or which industries are considered financial services, wouldn’t be buried in queries; they’d be configured in a single file, and published as live documentation. Changing the configuration would change the logic and the documentation, all at once.


Analysts would benefit from this as well. All too often, analysts create duplicative logic in queries and models simply because they don’t know that someone has done the same thing before somewhere else. Putting variables in a single config file exposes which ones exist, providing a kind of abbreviated summary of what has and hasn’t been done before.


Configuration files could be extended even further. First, the service that hosts the file and creates the interface on top of it could also make the file’s content accessible to other services. Python scripts could call the file and pull in its variables at runtime. BI tools could integrate with it, and let their users reference configuration variables directly in SQL. Update the config file, and all of the assets that reference it—from ingestion pipelines, to transformations, to dashboard queries, to operational models—update with it.


Second, the UI on top of the config file doesn’t have to be read-only; people could alsowriteto the file. If a product team wants to add new email domains to the test account blacklist, they can do it themselves through the configuration file UI. If the marketing team wants to reclassify UTMs into different channels, they can do it directly. If the growth team wants to define new user retention as a user returning in seven days instead of in just one day, they can do it on their own.


Finally, taken to the extreme, the config file could go beyond just variables. It could also define computational logic, like the formula for net revenue retention or the full case statement that determines the billing status of a customer accounts.6


Again, this isn’t entirely novel; much of this already exists in dbt in macros and, eventually, inmetric expressions. But like variables that are hardcoded in queries, these functions aren’t accessible to people who don’t know exactly where to look for them. Providing a means to centralize this logic, to broadcast it to others who don’t work in the dbt project itself, and to make it more broadly editable as individual components could dramatically alter how we use and construct data transformation pipelines.


For example, it would encourage us to design more composable projects that are built around shared functions, instead of burying logic in queries or reports.7Using a config file as a publishing mechanism would also make analytics engineering—the process by which we translate business concepts into formal encodings of our data—amore inclusive practice. Variables and short macros that define business concepts, which are often no harder to read than Excel formulas, are easier toeducate people onthan thousands of lines of SQL across hundreds of queries; an editable config file is an easier hub to collaborate around than a full dbt project.


All of this may seem like a lofty destination for a file or two full of YAML. But dbt itself, especially in its early iterations, could be described as little more than ahandful of SQL templates. It still took off, not because it was built on some profound technological achievement, but because it cracked open the door to a new way of working. A better data configuration file, and the change in workflow that it nudges us towards, might echo the same pattern, even if it, too, initially sounds like atoy you could build on a weekend.

[1](https://benn.substack.com/p/the-data-config#footnote-anchor-1-64173842)

Ad attribution reports nowcome with merch.

[2](https://benn.substack.com/p/the-data-config#footnote-anchor-2-64173842)

Unless, of course, some deranged analyst hid all of this logic in case statements that usethis heinous syntax, in which case we’re all hosed.

[3](https://benn.substack.com/p/the-data-config#footnote-anchor-3-64173842)

YAML as a product.

[4](https://benn.substack.com/p/the-data-config#footnote-anchor-4-64173842)

Is this something everyone already does? Have I just been doing this wrong? Is this a blog post a giant act ofhepeating?

[5](https://benn.substack.com/p/the-data-config#footnote-anchor-5-64173842)

For the rest of this post, I’m going to assume this config file lives in dbt because dbt already has a similar concept, and dbt models would be the most frequent consumers of configuration variables. It could exist in any tool though, or even be a standalone thing.

[6](https://benn.substack.com/p/the-data-config#footnote-anchor-6-64173842)

An actual case statement that defines this logic at Mode. Writing this once is enough; please don’t make me do it again.


```
CASE
     WHEN a.is_ever_closed IS NULL THEN 'pre-sales'
     WHEN l.created_at <  a.first_ever_closed THEN 'pre-sales'
     WHEN l.created_at >= a.first_ever_closed 
        AND l.created_at < NVL(a.first_ever_won,'2030-01-01') 
       THEN 'post-closed-lost'
     WHEN a.churned_account = TRUE THEN 'churned customer'
     WHEN l.created_at <= a.final_end_date THEN 'customer'
     WHEN l.created_at >  a.final_end_date THEN 'churned customer'
     ELSE 'WTF LOL'
 END AS account_status
```

[7](https://benn.substack.com/p/the-data-config#footnote-anchor-7-64173842)

This idea is similar to the core thesis behindMalloy, which is built on computations that are “modular, composable, reusable, and extendable in ways that are consistent with modern programming paradigms.” A logical config file, which moves computation from individual queries into a centralized library of reusable “functions,” tilts dbt in this direction.
