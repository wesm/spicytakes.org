---
title: "Data's trillion dollar question mark"
subtitle: "How a data warehouse could become a data platform—and an organizational brain."
date: 2022-01-07T16:58:54+00:00
url: https://benn.substack.com/p/entity-layer
slug: entity-layer
word_count: 1735
---


![](https://substackcdn.com/image/fetch/$s_!VSKC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe266f31c-f01c-4440-bd0d-83d59d0c118b_688x470.jpeg)


“Workday, Salesforce, Adobe—they’re going to be reimplemented as apps on top of the data layer.”


When Martin Casado, a partner at Andresseen Horowitz, was asked why he thought the data industry was a trillion dollar market andwhat bets he’d make[updated link]about where it’s going, this was his response. The answer stuck with me over the last several months, for two reasons. First, why? Why do we need to rebuild Workday, and what, exactly, is better about the tool that replaces it? And second, how? The modern data stack is defined as everything between an architectural diagram1and a state of mind,2but nobody would characterize it as a coherent layer suitable for widespread application development.


I came around on the first question pretty quickly. To borrow an analogyI've used before, we couldn’t have created Yelp by adding stars to listings in the yellow pages. Yelp isn’t valuable because it has reviews; it’s valuable because the entire product is built around them and the data they contain. Restaurants are organized by reviews; results are filterable by them; listings are enriched with details about what they say. It’s an entire experience, with the review at the center.


Similarly, a sidebar in Zendesk that shows a customer’s most recent activity makes Zendesk marginally more useful. But a help desk centered on that activity, one that cataloging tickets into queues based on user behaviors and prioritizes them according to their payment plan or recent sales conversations, could be many times more valuable. Embedding dashboards in Marketo is nice; a marketing automation tool that’s organized entirely around campaign performance data, from the top of the funnel, through product usage metrics, all the way to sales conversions and renewals, is revolutionary.3


Even if Casado’s prediction is a bit too bold, it’s easy to imagine a future full of smaller, more focused data apps.4Surely, even if we don’t all leave Salesforce.com for getsalesforce.ai (YC S22), we’ll at least have dedicated analytical tools for managing remote workforces, for connecting online marketing campaigns with offline retail sales, and for reliably computing SaaS metrics.


Still, Casado’s vision is missing a key piece: The bridge between where we are today, and the platform that’s needed to make these apps possible. The modern data stack—and more specifically, the centralized data warehouse—is a good foundation; data apps are a cool idea. How do we plug the latter into the former? Wehave the underpantsand we want the profit, but what do we do in the middle?


# Reverse ETL, we barely knew ye


Our current answer, such as there is one, is reverse ETL. Reverse ETL tools pull data from warehouses, map it to records and fields in destination apps like Salesforce and Hubspot, and sync the two. In doing so, they do things like create new lead records in Marketo, or update user attributes in Intercom.


In today’s world, these tools work well and are valuable.5If you use Salesforce, you need data in it—and wiring up your own pipelines that make sense of Salesforce’s tedious APIs is what nightmares are made of. So long as Salesforce is useful, reverse ETL products’ syncing function will be useful. But as platforms for backing data apps,6they’re a fudge.


The problem isn’t the reverse ETL tool itself, but how its sources are defined. Most tools simply extract tables, via either aSQL queryor apointer to a dbt modelthat creates a table. This is brittle, at the beginning, in the middle, and at the end. Schema changes can easily break the queries that load data. When creating multiple syncs, it’s easy to define the same concept—say, leads to be synced to Hubspot and Drift—in slightly different ways. And without stronger guarantees about how data will be exposed, you can’t build appson top ofreverse ETL tools; reverse ETL tools are mostly meant to integrate into existing products.


This is not fertile ground for a fledgling ecosystem. Reverse ETL tools, eventhose builton open frameworks, have an incentive to integrate with products that are already serving a lot of customers. Without a clean platform to build on—without a way topulldata, rather than waiting on someone else topushit to you—emerging data apps have to integrate with the warehouse directly. And so they do: Sisuconnects directlyto your warehouse; Narrator asks users towrite queriesin the app to build event streams;smaller, free appsrequire people to define the custom datasets that they depend on. This makes data appsexpensive for companies to buildand expensive for customers to maintain, stressing thealready-questionable economic dynamicsof the modern data stack even further.


Piecemeal architectures like this are also a broken experience for customers. Business concepts like users, customers, transactions, and events are defined in a mix of dbt models, queries in reverse ETL tools, configurations in third-party apps like those above, and the application code of internal tools. This can be, aswas the case for metrics, a mismatched mess.


But metrics—and some recycled ideas from the early 1990s—offer a solution.


# An entity layer


The metrics layer is, at its core, a semantic abstraction. It provides a way for people (and applications) to access business concepts directly, without having to know how to translate those concepts into precise formulas.


This same principle applies to other forms of data. The metrics layer provides a standard API for interacting with a KPI; a generalized “entity layer” could provide the same thing for business objects like customers, products, and users; for activities like web events, downloads, and purchases; and for temporal snapshots like a daily accounting of customers’ subscription types.


The structure of an “entity query” could be identical to a metric query; the only difference is the noun. Both expose properties that are specific to the type of object being requested; both render SQL queries that are directly readable by the warehouse; both push compute down to the warehouse; both can be used as standalone queries or mixed in with raw SQL.


![](https://substackcdn.com/image/fetch/$s_!Youq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6f632cb3-2aa2-45d3-b96e-7407ec328d75_2048x1524.png)

*There are two types of people in the world: Those who admit to having no idea how to format a case statement, and liars.*


At first glance, this doesn't look much different than a table or view. Is the customer entity, for instance, equivalent todim_customers, or the purchases entity the same asfact_purchases?


![](https://substackcdn.com/image/fetch/$s_!NinK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faf2b92ec-83c2-413a-b8a8-f56fd60b12c1_556x500.png)


Potentially—but even if entities are just tables, they’re tables with semantic meaning. To most people,dim_customersis an unremarkable set of rows and columns in a database, a node in a DAG, distinguishable from every other table only by how bold its name is in some data dictionary. It’s an object, with meaning tacked on. Entities are semantic objects first, and tables second. And just as metrics layers encourage teams to canonize one version of a metric, an entity layer could pressure teams to do the same with other semantic concepts.


Moreover, entities could be more complex than flat tables. A customer entity could be best represented through nested relationships, where each customer record contains a list of associated events and user actions.


Isn’t this, then, just a semantic layer with an SQL-like API?


![](https://substackcdn.com/image/fetch/$s_!CnZ9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F85f33bee-1594-4f18-b4cc-ed479a30bac8_556x500.png)


It is. That’sexactlywhat it is. But today’s semantic layers aren’t wrong in concept; they’re just problematic in execution. They’re typically only accessible via the tool they’re embedded in, as LookML is in Looker, for example. They’re also often required in BI tools, which encourages teams to overextend them to model every element of the business.


A better semantic layer would be universally accessible, interoperable with other means of querying the underlying data, and optional. This last point is particularly useful: It promotes discipline in choosing which objects are worthy of semantic definition, and which can exist as regular tables. Even within Looker, calls for this sort of architecture are comingfrom inside the house.


If you squint, Segment’sPersonas productoffers a sketch of what this might look like. As it exists today, Personas is too embedded within Segment to be a general entity, but it points in an interesting direction—what if we had an more API like this, for people, for customers, for purchases, and for other core business concepts, that translated requests into queries that ran directly against the database? This is much more stable ground for app developers to build on than that of custom queries against a warehouse.


# Four steps to the entity


Entity layers, I believe, could serve as the foundation for atrue OSfor the modern data stack. But for the sake of beingeven more concreteabout how we get there—and fortaking some wild swingsto see what ends up on the fairway—here are four guesses about what else might change.


First, metrics layers will expose entities as well as metrics. These concepts are alreadyimplicitly definedin model-based metrics layers, and dbt’smacro-based approachis likely flexible enough to support something similar. Entities, which are essentially an additional form of governance, fit naturally in this space.


Second, reverse ETL tools will incorporate these concepts directly. Census, which integrates withLookerandSegmenttoday, is already gesturing in this direction; entities would just generalize this approach. This also frees up reverse ETL tools to focus on their core competencies—building fast, reliable pipelines to dozens of destinations—rather than worrying about how data is sourced for those pipelines.


Third, an ecosystem of data applications begins to grow on top of entity APIs. While that likely starts with established companies like Sisu and Narrator, it spreads to—and more importantly, encourages—smaller projects like theSaaSGrid.


Finally, entities eventually become writable. Entity APIs, whether or not they’re SQL-like queries or traditional rest APIs, provide ways for updating the data underneath them, enabling the apps that sit on top to be interactiveandtransactional.7And the data warehouse finally evolves from being a dumping ground for organizational data into being its centralized operational brain, the production database for a company.


All it takes is an idea we hadthirty years ago.

[1](https://benn.substack.com/p/entity-layer#footnote-anchor-1-46731656)

That, at this rate, will turn into apointillism paintingby 2023. (small.jpg, lol)

[2](https://benn.substack.com/p/entity-layer#footnote-anchor-2-46731656)

The modern data stack is just, like, your opinion, man.

[3](https://benn.substack.com/p/entity-layer#footnote-anchor-3-46731656)

Is this exact idea revolutionary? I don’t know. But you get the idea.

[4](https://benn.substack.com/p/entity-layer#footnote-anchor-4-46731656)

The term data app issometimes usedto describe interactive reports or notebooks with lots of filters and toggles. To me, these are blinged-out dashboards, not data apps. A data app is a product—a CRM, an applicant tracking system, a design tool, a task management app—for which data is central to the experience of using it.

[5](https://benn.substack.com/p/entity-layer#footnote-anchor-5-46731656)

We use Census at Mode and are happy customers.

[6](https://benn.substack.com/p/entity-layer#footnote-anchor-6-46731656)

Which, in fairness, they don’t really claim to be.

[7](https://benn.substack.com/p/entity-layer#footnote-anchor-7-46731656)

Thereby, reversing reverse ETL.
