---
title: "An very obvious deal"
subtitle: "Shopping for the Data Stack Value Realization methodology."
date: 2025-10-24T20:03:26+00:00
url: https://benn.substack.com/p/an-very-obvious-deal
slug: an-very-obvious-deal
word_count: 2963
---


![](https://substackcdn.com/image/fetch/$s_!ApMH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2268c2a7-b67d-4c03-92ac-78a653d54738_2048x1094.png)

*Isn’t it obvious?*


I sometimes wonder if it’s all Slack’s fault.


In 2012, before Slack existed, I worked for awould-be Slack competitor. We sold software in the way that wastrendyat the time: People bought licenses to use it.Pay us $15, and one person can use it for a month. Pay us $30, and two people can. Pay us $15,000, and a thousand people can.1And just as a landlord doesn’t care how much time someone spends in their apartment every month, we didn’t care what people did with our software, or if they even logged into it all.2In both cases, customers buy timed access. What they did with that access was irrelevant.


When Slack launched, they charged their customers in the same way. According to theirfirst pricing page, “adding or removing team members during the term of a subscription will cause a one-time pro-rated credit or charge on your account.” But then, Slack blew up. The product—andthis chart—was suddenly everywhere. And Slack, with their “be kind” brand and CrayolaCore aesthetic, decided thatthis old pricing model was capital-w Wrong:


> Most enterprise software pricing is designed to charge you per user regardless of how many people on your team are actively using the software. If you buy 1,000 seats but only use 100, you still get charged for 1,000. We don’t think that’s fair. And it’s also hard to predict how many seats you’ll need in advance.At Slack, you only get billed for what you use. So you don’t pay for the users that aren’t using Slack. And if someone you’ve already paid for becomes inactive, we’ll even add a pro-rated credit to your account for the unused time. Fair’s fair.


It was a savvy maneuver, for Slack. People were quickly becoming addicted to their product, and it’s unlikely that many of their customers were buying 1,000 licenses and only using 100. Instead, they probably had the opposite problem: More people wanted to use Slack than companies’ IT departments were willing to initially pay for. By charging for only the licenses that people used, Slack could tell those IT departments that they didn’t need to worry about overspending on Slack, because theycouldn’toverspend on Slack. If nobody liked it, then they would stop logging into it and nobody would get charged for anything. And if lots of people liked it and used it all the time, wasn’t that worth a few dollars a month?


It was an ethos that ate the internet. Silicon Valley is an industry of trends, and Slack was our generation’s trendsetter. Shortly after they launched their “Fair Billing Policy,” other startups launched their own imitations. At Mode, our customers, many of whom had recently bought Slack, started to ask for the same thing. “Why should I get billed for something if I didn’t want to use it that month?” people said, for the first time. “That’s not how this should work,” they said of how it always worked.


Software pricing is like that though. When you’re selling virtual ephemera on the internet, there is no obvious way to buy it, and there are no physical or economic laws for how it should work. Instead, it’s almost entirely driven by norms and market expectations:

1. At first, people bought software by paying for a CD-ROM (or worse) in a box, and got to use it as much as they wanted, forever.
2. Then, we began to rent access. Rather than installing software, we paid monthly fees to use a website.
3. Next—in part because of companies like Slack—people started expecting to only pay for the days or hours that they used a product.
4. And now, prices are even more granular, and are defined bywhat you doon a website. Though usage-based pricing models have been around for some time—cloud computing services like AWS charged people for how much traffic they handle; storage apps like Dropbox charged for how big of a hard drive you want to rent; web tracking products like Mixpanel charged more if you wanted to track more events—they’restartingtoshow upinSaaS productstoo.


These trends were especially apparent in data products. Peopleused to buy databasesvia perpetual licenses that they paid for once and could use forever. Then, Amazon launched Redshift, which was offered asa monthly leaseof a dedicated database. Snowflake shortened the term of the lease—instead of renting a database for a month at time,you leased it by the minute.3BigQuery thenbegan charging by query, billing customers for every byte they asked BigQuery to process.


At first glance, these steps seem like a refinement of the former model. Each progression addssmaller intervalsunder the demand curve. Pay for exactly what you use—it is pure; efficient; the markets,clearing.


Which, maybe; I don’t know;sir, this is a Substack, not an NBER paper. But if you spend some time selling all this virtual ephemera on the internet, you’ll probably discover at least one thing: Regardless of the economic theory of each pricing model, there is apsychologicaldiscontinuity between model three and model four. In the first three models, it is hard to reason abouthow muchsome software service should cost. What is the right price for a license to use Slack? What is a Google Docs subscription worth? How do I put a price on Spotify? These are esoteric, almost philosophical questions. What is the value of corporate communication? Of an infinite library of documents? Of listening to Gracie Abrams4on a loop for a month?5


We don’t know, so we price software via dead reckoning: What’s fair today is what was fair yesterday. Outlook cost$12.50 a month, so Yammer cost $15 a month, so Slack cost$12.50 a month.6


But in the fourth model, this breaks down. When you’re selling a single unit of consumption,people seem much less willing to accept an arbitrary price.And they start asking one question in particular: “How much does this thing I’m buying costyou?”


Consider: A customer could say to Slack, “It costs you a few cents to add another person to your user database and to store the thousand messages that they send every month. Why are you charging me $12.50 for that?” Historically, people don’t ask that though—or at least, don’t complain about it too much—because that’s not how the world works. Arbitrary monthly licensing fees might not be an economically precise pricing model, but, when everyone is used to paying them, it’s a psychologically durable one. But if Slack started charging per message sent, people would start talking about the egregious markup. “It costs Slack a fraction of a penny to send a message, and they’re charging a full penny for it!” There would be righteous online riots about price gouging.


There is nuance here though. If Slack charged incremental fees for storing files, there would be probably be protests, but tamer ones. Because, again, we’re used to that. Storage is a thing we long thought of a scarce resource; we’ve stillpay more for computerswith more memory; conceptually, storage feels like a fair expense.


We saw all of these dynamics at Mode. When we charged a monthly licensing fee, our first price was $250 for technical users. People were upset by that—not because of the titanic markup we charged on top of a website that cost pennies to provide to an additional user, but because $250 a month for SaaS software was abnormally high. We eventually changed our prices to about $25 for all users. Then, when we added a fee of a few cents to run an additional query—running a query was our equivalent of sending a message on Slack, and also cost us a fraction of a penny—people were outraged by our brazen margins. But later, when we added computational middleware—“an in-memory compute engine”—that made running queries a plausibly expensive operation for us to perform, people still objected, but most customers were ultimately ok with it.


And that’s the lesson, I’d argue. If you can sell subscriptions to your software, you won’t get asked about margins, but you only have so much flexibility about what you can charge. And if you sell consumption, you better charge for something thatsounds expensive. Storing stuff works. Doing a bunch of hard math works. Generating an AI image works. But rendering a website, or calling an API, or managing a database of files and messages—well, “we don’t think that’s fair.”


---


This is why dbt Labs has always been a fascinating company to me (and why it will be good for that HBS case). Because, stylistically, here is the position that it’s always been in:

1. They provide a service that lots of people want to use. They built a product, the market wants that product, and dbt Labs quite successfully delivered it to them.
2. But how do you charge for it? Even if you put aside thedilemma about open source, there isn’t a clean pricing mechanic. You can charge for seats, but notthatmany people use dbt. You could solve that problem by charging a lot per license, but people start to balk at any seat price that’s more than two figures a month.
3. Or, you can charge for usage—that is the trend, after all, and people use dbt a lot. But that doesn’t really work either, because dbt hasn’t historically done anything that looks like real work. It doesn’t store data; it offloads all the hard computation to a database (which is already charging people for that exact operation). And if you’re not doing the thing that feels like work, people getmadwhen you charge them for it.


It’s a very unique set of rocks and hard places: A popular product, without no obvious way to sell it. And for years,I assumed the way outwas for dbt Labs to attach itself—via acquisition or a series of white-labeled OEM deals—to the databases that had more direct ways to make money from people using dbt:


> Databricks solves the riddle of dbt Labs’ business model. Databricks can offer dbt as a free, unmetered service. It wouldn’t care if you use the open-source version or dbt Cloud, nor would it worry about how many seat licenses you buy. This frees up dbt Labs to focus on what it does best—driving adoption of dbt’s core services.


It’s an obvious solution: if you can’t monetize your own service, find someone who can, and get a shared bank account.


---


Of course, when it happened, people also said that combiningdbt with Fivetranwas obvious. It was peanut butter and jelly. It wasone-thirdandtwo-thirdsof athree-letter acronym. It just made sense.


Spiritually, absolutely; both companies are from the same generation; of the same religion; they went to the same high school. Logistically, as a merger to make a one-stop shop for data services—the Atlassian for Open Data Infrastructure, the Adobe for data people, theBean Counter Cloud—I can see that too. Financially, as a way to combine two IPO-ish scale balance sheets into one; makes sense. Defensively, as a means for creating a business big enough to stand its ground against empire-building companies like Databricks and Snowflake; sure, why not?


But, as a solution to the pricing problem—the core dbt problem—that story seems harder to tell. Fivetran can’t make money off of the queries that dbt generates, nor can dbt transform their popularity into more volume for Fivetran. The two businesses are loosely synergistic: They indirectly help one another by, because Fivetran brings more raw data to dbt and dbt makes Fivetran’s raw data more useful, but that was true when they were independent.


Which doesn’t mean the dealdoesn’tmake sense—those other benefits are there, and it gives both companies one less potential competitor in acompacting industry. Still, it’s not quite 1+1=3, and M&A bankerslove 1+1=3.


There are a couple obvious options though. One is for the combined company to use its weight and position as the data department storeto become the bully in the industry:


> fivetran and dbt, the two largest players outside the data warehouses, are merging to flip the script: move value capture back into business logic. what is business logic? it’s the finite set of if/else statements that define your business. sql pipelines are endless conditionals that say “if customer did x, then calculate y, and route to z.” those transformations, rules, definitions of what revenue means and who counts as an active user and how to segment customers - that’s your actual business encoded in code. …[Snowflake and Databricks convinced everyone] that compute should capture all value, that business logic should be free. … by merging, [Fivetran and dbt Labs are] trying to have more firepower to make compute cheap and commoditized, and move value capture back where it belongs: business logic.


I guess it could work? But, this doesn’t solve the psychological issue: What, exactly, does dbt chargefor? You can’t bill for lines of business logic written. I suppose you could charge for a giant platform license—but that is the way we sold software decades ago. The trend is towards charging for consumption, and databasesfeellike they have more right to charge for that than SaaS applications that use databases.7


A second option is for dbt and Fivetran tofill in the hole in diagram, and become a database. Which, also, could work too? But that’s a big risk. Snowflake and Databricks aren’t huge companies because they figured out that there is money in building a giant enterprise database; everyone has know that for decades. They’re huge because they actually pulled off the very difficult thing of building a giant enterprise database. There is a big difference between a clever idea and ahardidea, and building a database is very much a hard idea.


Still, perhaps there is a third option—stolen, in true Silicon Valley fashion, from our latest trendsetter.


---


Here is one way to think about how Cursor works:

1. They built a very popular app for writing code with AI. Initially, most of the work that Cursor did was actually done by Anthropic (or OpenAI, or Google, or whatever): You told Cursor what code you wanted written, Cursor would wrap some prompts around your request, send it to Anthropic (et al), and Anthropic wrote the code—i.e., it did the thing that sounds expensive.
2. Cursor became very popular. But its strategic position was somewhat unsustainable, because all the money that customers spent to write code went to Anthropic rather than Cursor.
3. In doing this, Cursor noticed a pattern. A lot of the requests they were sending to Anthropic were relatively simple. They could be solved with simple models, and didn’t require giant state-of-the-art LLMs.
4. The opportunity, then, is straightforward enough: Raise abunch of moneyand make amini-modelthat handles the simple stuff. Don’t compete with Anthropic exactly; instead, just use Anthropic for less. Make it about saving customers’ money by choosing more efficient ways to write code, and then charge your customers when they invoke your high-volume, low-cost models.


The analogy is obvious. Cursor is to Anthropic as dbt is to a database. dbt is the interface; the database “does the work.” dbt has people’s attention; the database gets the money.8And—most notably—most of the queries that people run are small, and don’t require giant databases to execute.


So, you know. Put a database underneath dbt Fusion. But a small one; one that’s not aboutcompetingwith Databricks and Snowflake, but about saving customers’ money by choosing more efficient ways to run queries. It’s about doing what’s more efficient. It’s about Fair Pricing.


If only there was a company that was aboutSmall Data.9

[1](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-1-177037878)

Well, no, that’s not quite right. Most SaaS software vendors offer discounts if you buy in bulk, so if you paid us $15,000 a month, you’d probably get something like 1,500 licenses. And if you paid us enough—say, $100,000 a month—we’d probably give you an unlimited number of licenses.

[2](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-2-177037878)

That’s not quite right either. We also cared a lot about how much people used a product, but it wasn’t because we charged for usage; it was because unused licenses were unlikely to get renewed. If we sold 1,000 licenses and only 100 people used it, most customers (though not all! You’d be surprised!) would notice that, and wouldn’t buy 1,000 licenses again next month or year. And theentire economic apparatusof a SaaS business depends on customers buyingmoreservices every year, not less.

[3](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-3-177037878)

Strictly speaking, Snowflake doesn’t charge for consumption. They charge for the amount of time you keep the database active; what you do while it’s active doesn’t matter. It’s similar to Slack in this regard—they refined the terms of the subscription, but didn’t charge for actual activity.

[4](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-4-177037878)

Has everyone always known this????

[5](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-5-177037878)

Duuuu…dun.

[6](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-6-177037878)

How philosophical is SaaS pricing?Slack’s guide to understanding the value of Slackincludes the following phrases:

- “What is value…?”
- “...a value-centric partnership…”
- “...we have a dedicated Value Realization team…”
- “...the Slack Value Realization methodology…”
- “Build a value map”
- “...value stories…”
- “...value strategy…”
- “Start your journey toward becoming a value expert”


And, in a telling coincidence, after all of that, uh, rigorous study, Slack found that the correct price of their revolutionary new communication platform was…exactly the same as as what their older competitors charged.

[7](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-7-177037878)

Making compute a faceless commodity doesn’t really solve this either. All that does is drive the margins out of the database; it’s not clear that it pushes those margins back into the software that’s on top. “We own more of the pie by shrinking everyone else’s slices of pie” is great for customers, but not so great for anyone with pie.

[8](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-8-177037878)

Cursor charged their customers and then paid Anthropic to execute their requests, whereas dbt connects to customers’ databases, who then bill customers directly for dbt’s usage of the database. The result is the same though; the money ends up with Anthropic and the database, not with Cursor or dbt Labs.

[9](https://benn.substack.com/p/an-very-obvious-deal#footnote-anchor-9-177037878)

Anideaand ananalogythatis, also,obvious.
