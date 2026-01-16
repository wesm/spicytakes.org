---
title: "Microsoft builds the bomb"
subtitle: "What Fabric is, and what I want it to be."
date: 2023-05-26T16:27:34+00:00
url: https://benn.substack.com/p/microsoft-builds-the-bomb
slug: microsoft-builds-the-bomb
word_count: 1994
---


![Oppenheimer' Poster: Doomsday Approaches for Cillian Murphy](https://substackcdn.com/image/fetch/$s_!bIyl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33949711-494c-4b6e-87e1-855c9de2164a_1400x700.jpeg)


---


It is a mistake to think that you can solve any major problems just with potatoes.


– Douglas Adams


---


The modern data stack was always an ambitious project. The technology alone was complicated enough—collectively, we needed to pick up a dozen major enterprise applications, launch them into the cloud, and make them all work at a staggering new scale for a fraction of the cost. But in hindsight, this was the easy part. The much more audacious dream was remaking how this technology is built and sold. Historically, data products had been designed to meet the needs of enterpriseRFPchecklists; they were built by massive development teams in Oracle and SAP office parks; they’d packaged as suites with mandatory professional services upcharges; and they were sold to IT executives on golf courses and in box seats at Warriors’ games.


The modern data stack promised something different: Products built for the people in the trenches, designed by people who came from the trenches,1and demoed, trialed, bought, and championed from the trenches. Analysts and data engineers shouldn’t have to use aging tools imposed on them because a CIO was cross-sold IBM® ILOG® CPLEX® Optimization Studio2over a $400 closing dinner at Ruth’s Chris; they should get to choose whatever products are best for them.


Modularity—interconnected tools, each of which excels at their own specialty—became the means to this end. In theory, it’s a great idea. Businesses want to do thousands of different things with data, and often have contradictory needs—banks, for example, care about scale and security while startups care about speed and cost. People have their ownirreconcilable and idiosyncratic preferences. Titanic monolithscan’t solve all of these problems, nor can they respond quickly to market shifts. Ideally, rather than having to buy some generic all-in-one product, data teams should be able to mix and match pieces to create the perfect potato head,subbing one thing out for another when their needs change.


But this plan has always had one big problem: There is no potato.


The modern data stack has never had a platform. There’s never been an operating system on which everything could sit. There’s no central service that handles user identity and authentication, or data connectivity, or access management, or content organization.3When people have new ideas for improving how we all work with data, there’s no central platform to plug the technology into. To launch a feature, you have to build a product.


Though this problem affects the entire industry, it’s painfully apparent in the BI market. Nearly every product in the space first sold itself undera more specialized bannerthan BI. But over time, with no central platform to lean on, the narrow products couldn’t stand on their own. Customers asked for visualizations, then dashboards of visualizations, then self-serve explorations of dashboards of visualizations—until customers just asked for BI.4


This isn’t a failing of any one vendor; it’s a failing of the market. It’s a failing that potentially powerful innovations—like advancedvisualizationengines, insight-inferringAImodels, clevernewlanguages, andreimaginednotebooks—have to be watered down by redundant BI features before they can widely be brought to market.


Ten years in,this the legacyof the modern data stack: Dozens of creative and delightful features, often buried inside of overlapping and overweight products, all clumsily bumping into each other in a soup of startups and data services.


---


They won't fear it until they understand it. And they won't understand it until they've used it.


–Oppenheimer


---


This week, Microsoft decided that it’d seen enough.To roughly paraphrase their statement to the press, there’s gold in them modern data stack hills, but the prospectors are too disorganized to mine it:


> “Over the last five to 10 years, there has been a pretty massive level of innovation — which is great and that’s awesome because there’s lots of new technologies out there — but it’s also caused a lot of fragmentation of the modern data stack,” Arun Ulag, Microsoft’s corporate VP for Azure Data, told me. “There’s literally hundreds — if not thousands — of products and open source technologies and solutions that customers have to make sense of.” He also noted that a lot of the data and analytics products tend to keep their data in silos. “When I talk to customers, one of the messages I hear consistently is that they’re tired of paying this integration tax,” he said.


Microsoft unveiled its solution—to nuke the entire modern data stack off the face of the earth. EnterFabric:


> “There’s a unified compute infrastructure; there’s a unified data lake. There’s a unified product experience for all your data professionals, so that they can really collaborate deeply. [There’s] unified governance so that IT can manage this and create sources of truth that everybody can trust, and really a unified platform that both IT and business share — and the unified business model. There’s literally just one thing to buy, and it allows customers to save a lot of costs, which, especially in today’s environment, is really important,” said Ulag.


Fabric’s feature list is impressively comprehensive. It included data integration services, SQL workspaces, notebooks, observability and threshold-based reverse ETL capabilities, data exploration and reporting provided by PowerBI, and an omnipresent OpenAI chatbot calledClippyCopilot. Most of the modern data stack’s various categories are represented, built forEdgeand typeset inSegoe.5


Ultimately, however, the most notable thing about Fabric isn’t its features, but—as its name implies—the knitting between them. Fabric isn’t a suite of loosely connected services; it’s asingle applicationthat has one login experience, one user interface, one storage layer, one permission model, and one monthly bill.6Whereas each feature has a counterpart elsewhere, this connectivity is unique.


Of course, none of this is a surprise. Microsoft has run this play before; a year ago, I said they’d probablyrun it again, and “consolidate everything under one branded, proprietary banner, make it all work together, and send out an army of sales reps to steamroll the rest of us with it.” The question now, I suppose, is do we actually get steamrolled?


The first answer seems like no? Microsoft products are anathema to a lot of teams, and some überMicrosoft leviathan of Synapse andOneDriveprobably isn’t going to change that. To the extent that some customers’ problem with Microsoft is that it’s Microsoft, Fabric is a step in the wrong direction.7


Still, write Microsoft off at your own risk. One segment of customer for whom Microsoftisn’ttoxic, and is often preferred, is the enterprise—i.e., the segment with most of the money. As Isaid in the last year’s post, “consolidation and convenience—especially for enterprise buyers—sells better than a delightful product.” Microsoft knows this, and is alreadyon message: “Ulag noted that he personally demoed Fabric to 100 of the Fortune 500 over the course of the last year and that many enterprises are excited about it because it greatly simplifies their data infrastructure.” In this regard, the modern data stack may not get steamrolled, but stunted, frozen out of the top of the market by a Microsoft sales team that already has a standing tee time with every enterprise CIO.


Moreover, even if Microsoft’s execution isn’t perfect, Fabric still presents one new danger to the modern data stack: It gives buyers an integrated alternative. To this point, the only unified data platforms have been legacy ones, and the only modern data platforms have been fragmented. We haven't seen just how much—or how little!—data teams are frustrated by that fragmentation, since it's been part and parcel of products that are SaaS-based, cloud-first, and at least gesture towards a consumer-grade user experience. Fabric changes that. The choice is no longer legacy versus modern, but all-in-one versus best-of-breed. Place your bets, I suppose.


---


Let's kill the dreamer…and see what becomes of the dream.


–Genesis 37:19-20


---


Or—Fabric is an overstep. After all, the dream of a modularandintegrated modern stack isn’t impossible; it just needs,with all due respect to Douglas Adams, a potato. In Fabric, Microsoft built a potato and a bunch of facial features. That may be appealing relative to what else is available—monolithic legacy tools, or disjointed modern ones—but it’s probably not ideal. Fabric’s attachments—the pipeline tools, the SQL and Python workbooks, the AI integrations—will fall behind other vendors. Customers will preferhow other products’ facial features look. Some hot new thing will come out, and Microsoftwon’t be able buy special rights to it.


In this way, Fabric could level the modern data stack, butmake its promise more powerful. Imagine, after all, if we had something like Fabric with more choice on top? What if Microsoft’s launch announcement ended onthis slide, promising to build a platform that would handle the messy administrative needs that today’s data products have to all reproduce? What if Microsoft made its goal to enable small teams of developers to build data components—true components, like abetter experimentation dashboard, or acode-free tool for managing metrics, ora new way to analyze funnels—without having to rebuild half of Tableau in the process? What if Microsoft built a potato?


Or, perhaps the more interesting question is, what ifAWSbuilt a potato? Microsoft just committed to building the whole stack; Google seems to behaphazardly workingtheir way in the same direction. Amazon, by contrast, has always been more comfortable building developer platforms than SaaS applications. Plus,after pioneering the data industry’s move to the cloud, AWS has since faded from the lead. Snowflake, Databricks, and BigQuery are outmaneuvering Redshift and Athena; Microsoft and Google are dominating the AI arms race.


That race doesn’t need another bomb. Makeloveunified administrative service layers for enterprise data storage and compute applications, not war.

[1](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-1-123990165)

Mode's original tagline was "by analysts, for analysts." Flavors of this construct—we were you; we get you; we built this because we wish someone had built it for us—is all over modern data stack marketing materials.

[2](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-2-123990165)

This is theactual name, registered trademark symbols and all. (Also, IBM has a“certified pre-owned” program?? Like, I get it; it’s hardware; makes sense. But imagine if software vendors did this. Buy a certified pre-owned dbt project! It’s never been through a major rewrite, only has a couple thousand runs on it, and our licensed professionals have verified that the Salesforce models are still good for a couple thousand more.

[3](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-3-123990165)

Databaseskindado this. But, because warehouses don’t directly connect other products to each other—a BI tool, for example, can only infer what an ETL tool is doing by looking at the data the latter leaves behind—they’re more centralized gathering points than proper development platforms.

[4](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-4-123990165)

Back in Mode’s early days, I insisted that we call ourselves an advanced analytics platform; today, we’reModern BI. Transform wanted to be a metrics store and a semantic layer; theybecame a dashboarding tool. Narrator started as anew standard for data modeling; it now sells a self-serve data platform. Hextook down a blog postthat said Hex should complement rather than replace BI tools. dbt Labs has toperiodically remind peoplethat BI isn’t on their roadmap. And the same fate awaits the new Slack chatbots and AI integrations that—so far—also insist this time will be different.

[5](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-5-123990165)

In a humble homage toWolmania’s excellent weekly lists, the cloud provider fonts, ranked: 1.Ember(Amazon); 2.Roboto(Google); 3.Segoe(Microsoft).

[6](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-6-123990165)

Or at least, that’s the pitch. When these big integrated amalgamations are cobbled together from existing applications, there tend to be a lot of seams between services. I have no idea if that’s the case here or not, though given how much they said it wasn’t, I’m inclined to believe they’ve put a lot of work into the transitions.

[7](https://benn.substack.com/p/microsoft-builds-the-bomb#footnote-anchor-7-123990165)

More importantly, the default answer to the question, “Will this new product change everything?” is always, “No, it will struggle to get traction, people will keep doing what they’re already doing, the product will chase adoption by replicating the features that people use in existing products, andit will eventually start to look like everything else, until it fades off into the distance.” But that makes for a boring blog post; much better to melodramatically speculate about extreme outcomes with Bible verses and Christopher Nolan quotes.
