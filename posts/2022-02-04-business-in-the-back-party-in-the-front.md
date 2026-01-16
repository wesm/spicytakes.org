---
title: "Business in the back, party in the front"
subtitle: "Sorting through the chaos in the consumption layer."
date: 2022-02-04T17:04:30+00:00
url: https://benn.substack.com/p/business-in-the-back-party-in-the-front
slug: business-in-the-back-party-in-the-front
word_count: 1707
---


![](https://substackcdn.com/image/fetch/$s_!FL7K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F012c4464-c068-444c-b2e2-794aecd829de_1268x573.jpeg)


The front is falling off.


Or, more accurately, the front is splitting into a thousand tiny pieces, dumping 20,000 tons ofcrude oilinto our corporate environments.


In this case, our enormous faceless frigate is the front of the modern data stack.1Over the last decade, the data industry has been building a giant ship, now worth hundreds of billions of dollars, for ingesting, storing, transforming, and shipping data to every corner of every company in the world. Three-fourths of our boat has taken a clear shape around emerging architectural principles. We scrapped legacy ETL processes and replaced them with ELT; we’ve agreed to centralize our data in cloud warehouses that speak ordinary SQL (and have come to terms with Snowflake taking a tithe on everything we do); we do transformations in the warehouse, in SQL, and arestarting to debateif we should define metrics in similar ways.


Though far from universal, these approaches are at least normal.2If a data leader pitches this design to their CEO, they can find hundreds of analyst reports, blog posts, and customer testimonials to back them up. Nobody gets fired for buying I(ngestion), B(ig cloud data warehouses), and M(odels in SQL).


But the front quarter of the ship—analytics and BI tools for data consumption—the front is a very different story. There are no defaults. There are no generally accepted standards. There’sbarely a shared understandingof what companies should be doing with the data they have, much lesshowthey should do it.


Instead, the front of the data stack is represented by an explosion of tools, all tacking in slightly different directions. There’straditional BI; there’smodern BI; there’sheadless BI; there’sopen-source BI; there’sBitcoin-based BI. There arenotebooks for analysis,notebooks for SQL,notebooks for collaboration,notebooks for apps, andapps for notebooks. There aredata visualization tools,data visualizations for notebooks, andnotebooks for data visualizations. There areSQL editors for teams,SQL editors for people who don’t want to write SQL, andSQL editors for Snowflake customers. There arecollaborative workspaces, andtools that combine lots of things together. There arespreadsheets we can’t get rid ofandspreadsheets replacing the spreadsheets we can’t get rid of; there arerebuilt spreadsheets; there arespreadsheets, but BI. And more of everythingis coming.


All of these tools do ostensibly the same thing; they help people analyze data, and help companies make sense of that analysis.3Which raises two obvious questions: First, do we need so many nuanced options, or will the shape of the front of the ship, much like the rest of the boat behind it, settle on a more narrow consensus? And second, if it does, what will it look like?


# The case for choice


A few years ago, I was talking with a handful of people at a data meetup in San Francisco. One person was sharing their frustrations about their current team. "We hired a couple of data scientists to solve hard problems like building ML models,” he said, “but they've mostly only had time to answer business questions like analysts."


As someone else was quick to point out, his premise was wrong: Helping people use data effectivelyisthe hard problem. Unlike purely technical work, or the work of moving data around the lower levels of the data stack, solving business problems requires that datacross the chasm from computer to person.The fragmentation of the analytics space may simply be a reflection of the boring truth that people are different, we understand things in our own ways, and we’ll never have a standard API into people’s heads.


Moreover, different companies also use data in lots of different ways. The consumption layer is the interface to those use cases, and may need to be as varied as they are.


To continue our long history offood analogies, every business needs to cook different things with their data. Our kitchens are only so big, and don’t have the space or budget for every appliance and piece of cookware from Sur La Table. We’ve got to choose if we want a juicer or an Instapot; if we want a tortilla press or an immersion blender; if we want a conical burr grinder, a digital gram scale, a gooseneck pour-over kettle, and a Chemex carafe, or if we’re happy making coffee with a can of instant Folgers and the hot water from a garden hose that’s been sitting out in the sun.


The best choices aren't universal. We all have different problems, and different aptitudes and preferences for how to solve them. What architecture is best? How should we compose our kitchens? It, as the classic line goes, depends.


Still, kitchens havesomestandards. No matter what we’re cooking, we all need a sharp chef’s knife, a stock pot, and a couple sauce pans. Even if the consumption layers’s details remain stubbornly variable, surely, surely, we’ll eventually agree on a few essentials.


# The choices we face


In fairness, people have been trying to make sense of how we consume data for decades, and these aren’t exactly novel questions. But in fairness to being fair, a lot of the more recent conversations about the consumption layer have been dominated by voices who have a very big stake in which perspective prevails.4


People who are incentivized to say that we shouldn’t consume data through dashboards saywe shouldn’t use dashboards. People who are incentivized to say that analytical applications are different from self-serve BI tools say thatanalytical applications should be different from self-serve BI tools. People who are incentivized to say that collaborative, document-inspired experiences are best say thatcollaborative, document-inspired experiences are best. People who are incentivized to say that legacy BI is deaddeclare legacy BI dead.


It’s not that these arguments are wrong (though they can’t all be right). Nor is there anything wrong with people making them—presumably, we created these incentives for ourselves because we believed them first. But, this makes the conversation about the consumption layer a campaign, and proxies opinions about architectures through specific products. That muddies feature sets with more fundamental questions that haven’t yet been sorted out.


In the spirit oftrying to figure outwhat exactly we’re all doing here—of stepping back from talking about which kitchen appliances we need and not the brands behind them—these questions, however, are still worth asking.


### Specialized, or a suite?


Few people would disagree that different jobs call for different interfaces. Spreadsheets, notebooks, dashboards, exploratory visualizations—they all have their place, just asdocs and slideshave their place in office productivity apps.


The interesting question is about how they fit together. Should analytics tools exist as completely separate products, like the old desktop Office suite? Should they all be under one integrated roof, though remain generally distinct, likeGoogle Apps(I mean Google Apps for Work, I mean G Suite, I mean Google Workspace)? Or should the lines between them be fully blurred, as they are in Notion and Coda?


### For analysts, or for everyone?


No modern analytics tool would dare not be collaborative. But collaborative among which groups of people? Specifically, should analysts and data scientists primarily live in an advanced tool, and the rest of the business live in a BI and reporting tool, with people occasionally interloping between the two? Or should everyone always gather together in one spot, whether they’re there to look at a dashboard of ad spend or to do a strategic investigation of why search ads are suddenly outperforming social ads?5


This question is complicated by domain-specific apps, from traditional tools like Google Analytics to whatever operational toolsthe future cooks up. In a potential world where everyone lives in their functional apps, do we even need a tool for generic dashboards?


### Who’s an analyst, anyway?


Analysts’ and data scientists’ roles are getting compressed from both sides. Analytics engineers are eating into the upstream edge of their work, designing data models and configuring business logic that analysts used to be responsible for. And quantitatively savvy business experts are squeezing the downstream boundary, self-serving (in theory, at least) answers without analysts needing to intervene.


The latter case raises foundational questions about how non-analysts should consume data. Should they work in environments with high walls and protected paths, limited butprecisely governed? Or should people be encouraged to gradually venture off the trail?


Looker and Tableau provide useful examples of this dimension’s two poles. Though both sell to a general, “code-free” business audience, they clearly see that audience differently. Looker emphasizes governance and control; it’s BI with enough padding that nobody can hurt themselves. Tableau has a steeper learning curve and can be more easily misused, but, for the folks who invest in learning it, can stretch much further.


### Separate, interoperable, or embedded?


We can also imagine more extreme reconfigurations of the consumption layer. Rather than every tool building their own cut of a notebook, or visualization engine, or SQL client—not to mention content management systems, admin tools, and application cruft that’s necessary in every modern SaaS product—vendors could simply provide composable pieces that get glued together elsewhere. This consumption layer could look like Wordpress: An open platform where everyone chooses their favorite plugins. Just as it has for other parts of the stack, will there be a day that modularity and interoperability—true interoperability, not just APIs shouting at each other—comes for consumption too?


---


Technology trends are often cyclical, swinging back and forth fromcentralized and decentralized, frombundled and unbundled. In the analytics space, however, thependulum has lost its period.6That’s not necessarily a bad thing; innovation emerges from disorder. But it seems inevitable that the industry will eventually pull itself back in line, potentially corralled by community consensus, or, more harshly, yanked together by aninescapable economic gravity. But either way, someday, our boatwill get its face.

[1](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-1-48216628)

omg you must be soooo surprised

[2](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-2-48216628)

And actually, it turns out, really do have aminimum crew requirement of one.

[3](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-3-48216628)

I forced a bot to read the marketing sites of a thousand data companies and write its own. Here is the first page: Collaboration and team collaboration help data teams collaborate! Announcing Notebook, the democracy for data teams. Stack modern data with AI-powered analytics at the speed of time. We’re humbly backed by $800 million in seed funding to remake the Snowflake data lake. Join our growing Slack community; no credit card required.

[4](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-4-48216628)

Disclaimer: I have avery big stakein which perspective prevails.

[5](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-5-48216628)

Because, hoo boy,are they ever.

[6](https://benn.substack.com/p/business-in-the-back-party-in-the-front#footnote-anchor-6-48216628)

That music, though.
