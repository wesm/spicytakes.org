---
title: "Category collapse"
subtitle: "There's no signal in ten million dollars anymore."
date: 2023-09-08T17:14:36+00:00
url: https://benn.substack.com/p/category-collapse
slug: category-collapse
word_count: 2832
---


![](https://substackcdn.com/image/fetch/$s_!fuCn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F983359d2-74e1-4830-a206-c242a862c43e_800x417.jpeg)

*My name isOzymandias, king of a category in the modern data stack.*


“The data industry is going to consolidate” is apretty boring predictionto make these days.1What’s a lot less boring—or at least, a lot less talked about—ishowit’s going to consolidate.


There are options. Most of the startups in the space could get bought by some mega-vendor—sewn intoMicrosoft’s Fabric, rebranded as something inspiring like AWS Pipeline Watch, or have their CEO become atemporarySalesforceexecutive. They could evaporate, and leave behind nothing more than landing page with farewell post, and a $25 million hole on some VC’s balance sheet. Or, they could get absorbed by one another, not only reducing the number of logos onMatt Turck’s dizzying pointillism, but also collapsing the number ofcategories.


The last case is interesting, because there are lots of arrangements that could make sense. The preamble here is well known: The pandemic blew up the economy; interest rates got cut to zero;2startup valuations wenthaywire. Buyers stopped being so anxious about buying cloud data infrastructure; the modern data stack became theNew New Thing; hundreds of new tools chased the hype; the landscape split into somewhere between30and95different categories, with dozens of new startup claiming to be the industry leader inwhatever bit of whitespacethey could triangulate out of the latest market map. TheBig Bangpushed the universe inexorably outwards; gaps opened up between existing products;YC cranked out hundredsof new companies to fill them.


And then, theBig Crunch: Markets fell, interest rates went up, valuations collapsed, and the Fedtook away the punch bowlaround the time theparty turned into a riot.3


This correction,4rather obviously, cooled everything off. Customers, looking to cut costs, bought less stuff. This hasn’t just pushed down spending though; it’s also—predictably, as was predicted by everyone—categorically compressed the market. People stopped looking for specialized tools to solve every problem, and instead started trying to stretch the ones they have across several categories at once. Jacks of all trades may be masters of none, but they are also oftentimes—like, when the Nasdaq isdown thirty percent—better than masters of one.


Big vendors, sensing customers’ interests in consolidating around fewer tools, and sensing their own interest in making more money, have started to become more acquisitive. Databricks, the Lakehouse Platform,bought MosaicML, a generative AI company. dbt Labs, the makers of dbt,bought Transform, the makers of a semantic layer. ThoughtSpot, a BI tool,bought Mode, a different sort of BI tool. Teradata, a data warehouse provider,bought Stemma, a data catalog. Alteryx, an older data prep tool,bought Trifacta, a newer data prep tool.


Though each of these deals makes sense, they aren’t necessarily obvious, nor do they all follow the same structural pattern. Trifacta and Alteryx were direct competitors. Mode and ThoughtSpot were in adjacent boxes—ThoughtSpot as BI and Mode as a “data analyst platform” or a “data workspace.” And Teradata and Stemma were on completely different parts of the map.


If more deals are to come—and surely they are, as valuations are still well below where they were in 2021, and thehype multiplethat data companies got then has moved on to AI—what might the map look like when it stabilizes? Which categories will still exist; which ones will get subsumed; which ones will vanish completely?5


Obviously, I have no idea. And predictions like these—about who’s breaking up and who’s getting together—are probablya bad idea, right?6Whatever, it’s fine.7


## The data warehouses march on


Amid all thediscussions about Snowflake and Databricksrecently, one fact is far more important than the movements of their quarterly consumption trends—they are selling to an enormous marketthat already exists.According to Expert Market Research,8customers spent $60 billion on database management systems in 2022. Combined, Snowflake and Databricks have, one, less than ten percent of that market, and two, popular and easy-to-use products that are built on relatively modern cloud architectures. Pricing, packaging, branding, weird PR statements about customer retention rates—these affect their stock prices, which are built on expected growth rates and forecasted free cash flows. But they don’t really affect the viability of the core business, or their CFOs eventual ability tocount to ten billion. (Or, they start counting a lot more slowly at something like four, the stock market decides that it’d much rather that they count faster, and Microsoft—who has no problem counting to198 billion—buys themselves a database, or Marc Benioff buys himself another temporary exec.)


That said, there are a couple interesting questions about the warehouse market. First, as every database piles on features—data catalogsandLakehouse AI™andapp marketplacesandcollaborative analytics workspacesand100 new features and enhancements that are helping you get business outcomes—will the pendulum ever swing back in the other direction, towards big bare-metal racks that just store numbers and run queries? And second, is there a meaningful market for specialized databases?


My money is on mostly no, to both.9To me, the issue seems like an economic problem. Building warehouse technology is expensive; selling and supporting it is even more expensive. That means these companies will have to sell to enterprise buyers, and enterprise buyers want ecosystems. Plus, there’s so much money in warehousing and compute, any successful small player will immediately become a target—to acquire or copy—for a bigger and better capitalized competitor.


The one major exception to that is for warehouses that are built for application development, and sold to engineers. MongoDB pulled this off, and then some—it’s currently tradingat the highest premiumof any SaaS business in the market.


## Everything becomes BI*


It’s the first law of the data industry:Everything with a chart will become a BI tool.


> Nobody believes it at first.We tell ourselves that this time is different. We’re solving a different problem, for a different audience. We can make something complementary to BI, something narrower, lighter, more focused. We tell ourselves we're more principled than the others; we have more discipline;wewon't cave andbuildpiecharts.Maybe we're right, in theory; maybe it can, eventually, be done. But the market can stay irrationallonger than a startup can stay solvent. And our customers will see our charts and want more of them; they'll want reports, and alerts, and explorable dashboards that can be exported as a PDF. They'll want granular permissions, and to connect to an old version of SQL Server running on aDell Optiplex 3020under Jeff's desk. They'll want exactly what we’re selling, plus just this one feature, and they'll pay us $100,000 if we can build it.


I get the temptation to believe that tools for analysts can stand alone; Ireally, really do. The trap in that belief, I’ve realized, is that there actuallyareenough buyers of these products to support a handful of large vendors. The problem, however, is that these tools can’t be both bigandseparate enough from BI to be seen by buyers as being a distinct thing. As soon as specialized as “advanced analytics platforms” can command big annual contracts, customers start expecting that spend to be offset by reduced spend in BI. Then, no matter how differentiated the product is from BI, it’ll get evaluated through that lens.


Put differently, software categories aren’t defined by Gartner, or VCs, or marketing taglines; they’re defined by buyers. And if you’re selling a product that charges non-trivial amounts of money so that people can answer questions with charts, buyers will see you as a BI tool, compare you to other BI tools, and will call you BI.


My unrelenting belief is that every BI-adjacent product is likely bound for one of three destinations: Be subsumed into some bigger and unabashed BI platform; stall, and become a niche player serving a small market; or get acquired by a major SaaS business that wants to start selling better reporting.


## * Unless it becomes an embedding reporting tool


The real competition to general BI products probably isn’t a bunch of specialized analytics products; it’s internal reporting tools that are built directly on top of systems of record. These products—Adobe, Anaplan, Atlassian, HubSpot, Klaviyo, Salesforce, SAP, ServiceNow, Shopify, Stripe, Workday, and others—already have critical business data; they canquery it live; they don’t need customers to buy ETL or warehousing tools first; and they can build the sorts ofcanned templatesthat have been BI vendors’white whale for years.


True, these sorts of reporting services almost certainly aren’t robust enough to outright replace BI products, especially at larger companies. They’re also limited to reporting on whatever domain they serve and whatever data they have.10But, for these vendors, internal reporting tools are probably compelling enough to customers that they’re worth building—or, more likely, buying on the cheap.


For the visualization tools sitting on a few million in ARR, this is as likely to be a landing spot as within another BI tool. There just aren’t that many BI tools to do the acquiring; plus, BI companies would already have existing pieces of the technologies they’d be buying. Unless there’s a very precise fit, the integration efforts likely aren’t worth the cost, nor is a few million dollars of revenue worth defending. These deals are much more likely to be acquihires—and therefore, priced as such—than product buys.


SaaS vendors, by contrast, may pay a slightly higher premium. They are less likely to have visualization and data infrastructure experts in house already; if they’re revamping their reporting products, they may be planning on building a team to do it already; they’ll also be less sensitive to mismatched technologies or team philosophies.


There’s also already some precedent here:Atlassian bought Chartioin 2021. More are probably coming.


## ELT rebrands as “enterprise data integration”


“Simple” ELT tools that copy data from a SaaS application into a database are not, in fact, simple. SaaS vendors provide data in ways that can’t be directly copied into a database; APIs constantly change or go down. ELT vendors—i.e, Fivetran, we’re mostly talking about Fivetran—have to deal with these problems, across hundreds of integrations, for customers that expect zero mistakes.11That’s not easy, and is unlikely to be replaced by connectors built by bots or poorly maintained open-source ones.


Still, I’m not convinced Fivetran will stay as is. Major SaaS vendors canbuild their own connectors; somealready are. One of the dangers of Fivetran’s usage-based pricing model is that these connectors can get cleanly cleaved off. If Fivetran charged a flat fee, customers would likely want to centralize all of their integration on Fivetran, to get more bang for their buck. But if they’re paying per sync, they have no economic incentive to use Fivetran over another connector that’s either cheaper or better.


Moreover, major database vendors like Snowflake, Databricks, and BigQuery may want to cut out the middleman themselves. ETL and reverse ETL tools are both essentially ports that are charging import and export taxes on top of a warehouse. Surely, databases would rather collect those taxes themselves—or, even more likely, get rid of them entirely, because they make most of their money once the goods get on the mainland. And if buying the port to your warehouse means you own the port into all of your competitors, even better. Tax them and not you; there is no data stackWTO.


So how does that play out? I’ll make two guesses.


First, databases do end up buying their own ports. Probably not Fivetran, but one of the smaller players. (Not a prediction, but Hightouch recently announced a “strategic investment” fromDatabricks Ventures. And there’s a reason these venture arms areoften led by the VP of Corporate Development.) And second, because of all of these factors, Fivetran will worry less about building an impossibly long list of connectors, and to instead focus on the ones that they can charge a lot of money for—like Oracle and SAP HANA. They’ll support fewer startups, and more systems integrators who are paid billions of dollars to figure out how to make IBM talk to NetSuite. And they’ll compete less with Stitch, and more with MuleSoft.


## Die a hero or live long enough to become Alteryx


There are, I believe, four well-defined categories in the data world. The first three are reasonably well understood: Warehouses, for storing the numbers; BI platforms, for graphing the numbers; and integration tools, for going out and getting the numbers.


The fourth category is basically “other.” It’s a giant pileup of somewhat related functions, like data cataloging, governance, lineage, observability, orchestration, transformation, and discovery.


In a booming market, customers might be willing to buy a tool dedicated to each of these problems. In a down market—or within big companies, where procurement people like signing one big check and IT people like managing one big tool—people buy, like, Alteryx.


Ultimately, I think that’s where a lot of the various companies in these spaces are headed. The “data management” space is a lot like BI, in that it does a hundred different things, and every enterprise buyer wants a different combination of twenty of them. There is no killer feature; there is no sharp disruptive wedge. That’s why Alteryx makesalmost a billion dollars a year, despite seeming like aneasy target for startups. The maze of complexity is its defense. Trying to build a simplified Alteryx is how you lose to Alteryx.


And so, the pressure for every company in one of these categories is to become akatamari ball, rolling up related products into a similar web of enterprise services. You see this with Alation and itsData Intelligence Platform; you see this with Collibra and itsData Intelligence Cloud. You see early versions of this taking shape in the growing product catalogs of companies like Atlan and Monte Carlo and Hightouch.


My bet would be that that pattern continues. Standalone data catalogs, discovery tools, and observability applications will end up being products of the times. The individual categories will go away as they all get merged together, or as vendors in one of the other three categories build their own. (This is already happening with catalogs.Tableaualready has one;Teradatajust bought one;Databricksjust built one; Snowflake surely now wants one.12) And a handful of surviving variety shops become the ERP tools of the data world—nobody knows exactly what they do, but the big ones seem to make a lot of money.13


# Inevitably isn’t what it once was


Ten years ago,Jason Lemkin saidthat “inevitability in SaaS comes around $10m in ARR.” In the data world, I don’t think that’s true anymore. The market is big enough, fragmented enough, and disparate enough that getting to $10 million simply doesn’t—or didn’t, at least—have that much signal anymore. There are lots of data tools that can find $10 million worth of buyers that can’t find $100 million.


There’s also not much signal in being a “category leader.” Last year’s categories were potentially just as hyped as last year’s companies. Their kings may run kingdoms, or they may rule overlone and level sands.


So what makes a data company inevitable? Honestly, it’s probably the same as it ever was: Repeatable enterprise sales, solving problems in proven categories.

[1](https://benn.substack.com/p/category-collapse#footnote-anchor-1-136852343)

Things that are embarrassing:When somebody points out the most obvious thing, like, the data industry is going to consolidate, and everyone’s like, oh my goodness, so real, guys, I’ve been saying this the entire time, when it’s like, obviously,obviously.

[2](https://benn.substack.com/p/category-collapse#footnote-anchor-2-136852343)

Ibid.

[3](https://benn.substack.com/p/category-collapse#footnote-anchor-3-136852343)

The last few years haven’t been a bubble; they’ve been Adrian’s Kickback. It started with some people who just wanted to hang out and have a good time; it got popular on the internet; a bunch of money showed up to hype the whole thing; and at some point, thousands of people were there, a lot of them weren’t really sure why or what to do, so we all just lit a bunch of stuff (i.e., money) on fire.

[4](https://benn.substack.com/p/category-collapse#footnote-anchor-4-136852343)

This euphemism has always been funny to me. It’s not a downturn; it’s an opportunity for improvement.

[5](https://benn.substack.com/p/category-collapse#footnote-anchor-5-136852343)

Old habits die hard, apparently.

[6](https://benn.substack.com/p/category-collapse#footnote-anchor-6-136852343)

Yes, I know that we compete, but can't two rivals reconnect?"I only see them as partners, " the biggest lie I ever saidOh, yes, I know that we compete, but can't two rivals reconnect?I only see them as partners, I just tripped and emailed their corp dev.

[7](https://benn.substack.com/p/category-collapse#footnote-anchor-7-136852343)

Why are you reading this?!?GUTSis out! Stop talking about data!!

[8](https://benn.substack.com/p/category-collapse#footnote-anchor-8-136852343)

Sounds legit for sure.

[9](https://benn.substack.com/p/category-collapse#footnote-anchor-9-136852343)

Well, sorta. I’m apersonal investorin MotherDuck, which means my literal money is more on yes.Strong opinions, weakly heldis an ironically awkward investment strategy, I guess.

[10](https://benn.substack.com/p/category-collapse#footnote-anchor-10-136852343)

Unless, of course, they go out andget more.

[11](https://benn.substack.com/p/category-collapse#footnote-anchor-11-136852343)

Which, to be clear, is the point. Data syncing doesn’t really work if you can’t trust the sync.

[12](https://benn.substack.com/p/category-collapse#footnote-anchor-12-136852343)

I look forward to when the fight between Snowflake and Databricks enters itsTravis VanderZanden phase, when we move past disputes aboutperformance specsand into disputes about execs stealing trade secrets. I don’t understand TPC reports or court filings written in lawyerly legalese, but one has bigtables of numbersand the other has screenshots of text messages, and one of those things is way more fun than the other.

[13](https://benn.substack.com/p/category-collapse#footnote-anchor-13-136852343)

Forced to say, I’d probably guess that this is kinda what happens to an independent dbt Labs? They layer on governance and security services, more orchestration features, and a variety of enterprise-y things that compete, in effect, with, like, Alteryx.
