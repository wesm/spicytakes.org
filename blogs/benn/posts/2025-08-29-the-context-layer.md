---
title: "The context layer"
subtitle: "It didn’t work for us before…but it might work for us now."
date: 2025-08-29T16:43:21+00:00
url: https://benn.substack.com/p/the-context-layer
slug: the-context-layer
word_count: 2039
---


![](https://substackcdn.com/image/fetch/$s_!g5Tj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f6dc783-5833-49ea-91d5-f28fb0eb487d_856x480.png)


Let's trythis oneagain, I guess.


That article was one of the first things I posted on this blog. It proposed that the growing ecosystem of data startups—then called the modern data stack; now called the modern data stack (derogatory)—needed one more elemental piece: A metrics layer.


At that time, there werefour generally-accepted layers:

1. An integration or extraction layer that collected data from various sources.
2. A database that stored and processed what had been collected.
3. A transformation layer that defined how to turn messy raw data into clean and tidy tables.
4. An application layer—BI tools, visualization products, notebooks, SQL clients, lol, no, it was just BI tools,it was always just BI tools—that let people do stuff with all their data, which mostly meant making charts and dashboards of metrics.


Though this worked well enough, there was a problem. People wanted all of the charts in the fourth layer to be consistent with one another, but there was “no central repository for defining a metric.” Even if the third layer included some precomputed revenue tables—revenue by quarter; revenue by product line; revenueadjusted to be pleasing to the CEO—people couldn’t calculate new segments without rewriting the formula for “revenue” from scratch. So,metric definitions were often“scattered across tools, buried in hidden dashboards, and recreated, rewritten, and reused with no oversight or guidance.” And because the formulas for computing business metrics are often complicated and nuanced, sometimes people would mess them up. Dashboards wouldn’t match, or a customer would get the wrong marketing email, or the CEO would tell regulators that they had$78 billionthat did not exist.


Hence, the metrics layer: Put the formulas for all of your business’ metrics in a big library, so that people—or BI tools, via programmatic means—could write stuff like this:1


```
GET revenue AND
    paying_customers AND
    community_adjusted_ebitda

 BY quarter AND
    country
```


and know that all that logic that’s implicit in that question—like what revenue includes, what a customer is, and what Adam Neumann finds to be a pleasing definition of EBITDA—would be defined correctly.


Of course, none of this was a new idea; semantic layers have encoded metric definitions like these in BI tools for decades. But this added a new twist: Historically, semantic layers couldn’t be shared across different tools. The hypothesis behind the metrics layer was that a universal logical layer would be better than a bunch of fragmented ones—which was itself simply an extension of one of the foundational ambitions behind the modern data stack itself. From a post evenolder than that metrics layer post:


> [It used to be that] the most popular data tools were responsible for every aspect of the data “supply chain”—collection, storage, analysis, and visualization. If you wanted to analyze a particular type of data, there was a tool specific for that data or business domain. … [For example,] if you want to track how people are using your website, you can do that, soup to nuts, through Google Analytics. …[Now,] one tool is responsible for each layer—each stage of the data supply chain—across the entire business. A single tool handles ingestion, another one is responsible for storage, a third for consumption, and so on. This not only makes it easier to introduce new technologies, but it also ensures that updates to one layer—for example, an update to the logic defined in the transformation tool—automatically propagate to every other layer.


That is: The whole stack wasturning horizontal: “We no longer need to buy a bunch of vertical-specific products to do analytics on specific things; we push data into a warehouse and can then analyze it all together in a common set of tools.” The metrics layer was a proposal for another shared layer.


And:


> It was also a bad idea?I mean, I don’t know that, not for sure, not yet. But the trajectory isn’t great. By the end of 2021, at leastsix companieswere building a product that could reasonably be called a metrics layer.Twopivoted, one gotacquired, and onestalled. Two are still growing—Cube raisedsome moneyin June [of 2024], and dbt still sellstheir semantic layer—but neither have becomeanything closeto a market standard. Google hasgone silentabout their spinoff. In 2022, the industry was chasing the idea; now, after some false starts and disappointing v1’s, it’s slowly backing away from it.


However, to the extent that the idea flopped, the issue probably wasn’t technical or experiential; it was economic.As Fivetran CEO George Fraser predicted, a standalone metrics layer was too hard to sell without a BI tool attached:


> They [Looker] weren’t able to sell their metric store without a built in viz/dashboard/users/permissions layer, and that’s not going to change.


Though centralized horizontal layers sound nice, you have to have something to sell. You can draw a diagram of a great ecosystem of interconnected products, but those products are made by independent companies. And what’s best for the customer—a tight architecture of mutually exclusive and collectively exhaustive parts—may not be what’s best for the businesses making the stuff.


I missed that then, and perhaps deluded myself into thinking auniversal standardwould work for us. But—it might work for us now.


# Glue work


If you squint at semantic layers, they are ways to translate questions into numbers. Companies have a bunch of tables of data over there, and a bunch of people with business questions over here, and semantic layers intermediate between the two. The people creating them first figure out the sorts of questions people might ask, and then they create a catalog of metrics and filters that map to those questions. If they’re able to create a complete-enough library and describe everything with reasonable-enough names, the theory goes, people could find what they need.


If you squint even more, this is similar to the problemeverydatacompanyistryingtosolveright now.2Except, the intermediation happens with AI, through agents that try to translate questions into numbers. Most of these bots try to understand people’s questions by using whatever information the product running the bot has—Tableau uses its data catalog to understand questions; ThoughtSpot uses its internal semantic model and user feedback; Julius remembers previous conversations to guide future ones. But now, products are beginning toreach out to other servicesfor more “context:”3


> But data teams need a way to curate trusted context; relying on LLMs alone comes with too many gotchas! Last week, we launchedsemantic authoring, and next we'll be integrating agentic capabilities with semantic models, so anyone in your organization can ask questions in Hex using governed context straight from the data team.


You can imagine where this might go. To get better at answering questions, analytical bots begin by sourcing information from semantic layers; then, from the MCP servers ofother data tools;4and eventually, from Slack messages, and Google docs, and emails, and thetranscribed recordings of Zoom calls.


In other words, they will probably do what an analyst does. They will get told a bunch of facts directly, like how to define certain metrics and which ones are most important, and will be given instructions on how to figure out the facts they don’t know—check these docs; read the history of this Slack channel; look at the old versions of some canonical deck and make sure it matches that. And then they have some learned set of skills that help them make sense of all of it.


This isn’t simple to do, though. Building integrations5into different sources requires work; explaining how to use each tool requires work; defining the organizational particulars of each tool requires work; writing all the various prompts that start with “you are an expert analyst” requires work. You can’t onboard an analyst by giving them logins to a bunch of tools; you can’t make a good bot by granting it access to the same sources. You have to instruct and train both. You have to teach them how the tools work, and how the business that’s using them works.


In theory, it’d make sense for this to exist in one centralized place, rather than every BI tool doing it. Put this contextual logic—how to access relevant information, how to use it, and how to think analytically about it—in a single repository of integrations and prompts; let other tools use it as a source when they need to understand what someone means when they ask how many new accounts were created this fiscal quarter. It’s Fivetran, for context.6


Or it’s the metrics layer, for fuzzy analytical concepts. And it has the same problem that that idea had: It’d be hard to sell on its own. Every BI tool wants to be the best place to ask questions; they want to make their “AI analyst” the best one; they want to differentiate themselves by having a proprietary agentic loop that can answer questions that nobody else can. And BI tools are unlikely to outsource that, just as they’ve been reluctant to outsource semantic layers to a third party that they can’t control, and that everyone else can use.


# Specialistsina spreadsheet


Still, there is perhaps a broader question here. As software fitfully becomes more “agentic,” you could imagine two architectures emerging:

1. One that combines applications and agents. Every word processing tool has a chatbot that’s told how to be a good writer; every project management app is full of prompts that tell it how to write a good status update; every vibe-coding product is both a hosting platform and virtual engineer; every video conferencing system has a note-taking service; every BI tool sources its own context for its own agentic loops. The AI isinthe software.
2. One thatseparatesapplications and agents. SaaS products build programmatic interfaces that allow bots to manipulate them, but they don’t build the bots themselves. Instead, a new class of software emerges that is just the agent—it’s a sales operations manager that knows all of Salesforce’s peculiarities; it’s a product manager that knows how to consolidate Slack messages and Linear updates into a roadmap deck; it’s an analyst that knows how to translate an ambiguous questions into mixed and matched MCP calls and a bunch of analytical reasoning. It’s not a SaaS app with a specialized bot inside; it’s a specialized bot that can use SaaS apps.


For the same reason that a universal semantic layer seems like it’d be better than a bunch of fragmented ones, the latter arrangement of apps and agents also seems better. Those sorts of bots would be unbounded by the tools they use, could persist across them, and would be purchased (hired?) independently of the software they use. And they could be trained and maintained in a single place, eliminating a bunch of duplication both inside of the companies that use them, and in the market as a whole.


But that also has the same economic and logistic problems as the metrics layer. You can’t sell a meeting notetaker without a tool for hosting meetings; you can’t sell an analyst without some charts. And software is, first and foremost, a thing to be sold.The road to hell is paved with practicalities.


Still, perhaps we willgo somewhere differentthis time. Maybe we try option two. Because no matter how this evolves, it seems like we’ll always have systems of record that are full of important information.7And we’ll likely add "experts" that are imbued with a bunch of domain-specific skills that let them manipulate those systems of record. But will the experts come attached to the app? Will they be more like employees?Will they be human, or will they be vendor?

[1](https://benn.substack.com/p/the-context-layer#footnote-anchor-1-172277867)

If we get bent out of shape abouttrailing or leading commas, imagine what would happen if they were ANDs.

[2](https://benn.substack.com/p/the-context-layer#footnote-anchor-2-172277867)

lol, of course it is, because this is what BI is,it was always just BI.

[3](https://benn.substack.com/p/the-context-layer#footnote-anchor-3-172277867)

“Context” feels like AI’s version of social media’s “content:” A sterile, anesthetized term that flattens everything into a flavorless algorithmic grist.

[4](https://benn.substack.com/p/the-context-layer#footnote-anchor-4-172277867)

From a new startup calledZayer:


> Your data warehouse contains the insights and context that could transform AI performance.


And:


> [With Zayer], easily create Data Experts that know exactly how to turn agents' natural language questions into answers.

[5](https://benn.substack.com/p/the-context-layer#footnote-anchor-5-172277867)

Or, in the parlance of AI, defining the tools an agent has access to.

[6](https://benn.substack.com/p/the-context-layer#footnote-anchor-6-172277867)

Possibly, inevitably, it’s dbt again, anddbt should know about context.

[7](https://benn.substack.com/p/the-context-layer#footnote-anchor-7-172277867)

Which might eventually just be spreadsheets.
