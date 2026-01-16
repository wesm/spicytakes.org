---
title: "How Fivetran fails"
subtitle: "SaaS giveth, and SaaS can taketh away."
date: 2022-09-16T16:10:12+00:00
url: https://benn.substack.com/p/how-fivetran-fails
slug: how-fivetran-fails
word_count: 2582
---


![7 Big-Bargain Outlet Malls | Visit California](https://substackcdn.com/image/fetch/$s_!2sE9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F77a02ec5-9371-4263-8dfa-76f797f9c5fb_1280x640.jpeg)

*The biggest threat to Fivetran: The outlet mall.*


Sometime in 2014 or 2015, we were trying to figure outour next moveat Mode. At that point, we’d built a query and visualization tool that was asolid frontendfor the modern data stack. The only problem was that the modern data stack didn’t exist yet. Most companies weren't using a cloud database, an ELT provider, and dbt; instead, they had Salesforce, Mixpanel, Stripe, Facebook Ads, and a bunch of building frustrations about the limitations of each product’s embedded reporting tools. They wanted something more flexible that could work directly with raw data, which was exactly what Mode was for—so long as you had a warehouse with data in it. Back then, people had neither.


We had a choice: Do we tell these companies—potential customers, at a time when we only had a few dozen—that we can't work with them until they buy a database and figure out how to load stuff into it? Or do we connect directly to their SaaS services, extract data out of tools like Salesforce, and try solve the entire problem ourselves?


On the roof of a bike shop in SoMa, we decided on the former. Redshift was becoming popular; everyone, we predicted, would have a warehouse soon. And it was getting easier to fill it with data. A small explosion of cloud ETL startups—Fivetran,Alooma,Xplenty,ETLeap, andBlendo1—had launched recently,2and data collection tools likeSegment3andSnowplowwere starting to write directly to Redshift. Our view was two-fold: Data warehousing and ingestion will get solved by other companies, and the ELT market, which we thought provided an undifferentiated syncing service between a handful of SaaS apps and databases, wasn’t a business worth getting into.


Eight years later, we were half right. Other companies certainly solved both of these problems. But we got the size of the ELT market wrong. AsSaaS adoption blew up, so too did demand to pull data from these services into a database. ELT products were no longer extracting data from a few apps; they were extracting data from hundreds.


Now, the success of Fivetran, the modern data stack’s leading ELT provider, seems obviousandinevitable. But, totenth man Fivetran, is it? Surely, there are twists that would take us all down a road on which Fivetran slips from its perch, and its decline seems more guaranteed than its ascent. If we knew that’s where we’re headed—if we assume the result, and try to figure out the cause—what might lead us there?


There are three plausible paths, I think: We no longer need to move data from SaaS apps to warehouses; we still do, but we start moving it in a fundamentally different way; or we need to solve the same problem in the same way, and Fivetran’s no longer the best tool for doing it.


# The problem goes away


Fivetran is, if nothing else, a product of its time. It perfectly married two of the biggest trends in data over the last decade: The explosion of the SaaS industry, and growing desire for a centralized data warehouse.


These waves could dissipate. We might stop buying SaaS products—because ourSaaS debtcatches up to us, or because Microsoft and Salesforce (and Adobe) gofull Borgandassimilaterebundle the entire SaaS ecosystem into a single hulking mothership. We could conclude that the centralized warehouse was a mistake, and move back towardsdata marts.4We could keep our SaaS tools and our databases, and simply decide we don’t need to move things from one to the other.


The first two don't seem very plausible to me. Millennialslove appsandhate acquisitions. And databases have been around long enough that I wouldn’t bet against their durability.5However, the third possibility—we stop wanting to move data—is a bit more intriguing.


Major SaaS vendors like Salesforce, Hubspot, and Intuit have a strong incentive to build their own reporting tools. Companies at this scale make a lot of money from selling new product lines and to new business units; analytics and BI tools offer an opportunity for both. And it’s already happening: Salesforce bought Tableau (to sell as an independent BI product and, I suspect, to improve the native dashboards in Salesforce); Atlassian bought Chartioto upgrade their apps’ internal reporting; Stripe built anembedded query toolto give their customers direct access to data.


These efforts make sense to vendors, who probably see the money analytics companies are making on top of their data and want to take a cut for themselves. And they make sense for some customers, who want reporting—and in this case, precise and purpose-built reporting—without having to buy a database, Fivetran, and a BI tool to get it.


But does this kill Fivetran? Probably not. Most SaaS companies won’t be able todrop $16 billionon a better reporting suite. Moreover, embedded tools only have access to the data created by the product they’re embedded in. No matter how good Stripe’s query tool is, it can’t query what’s in Salesforce, or Zendesk, or that random new ad tech app that someone bought from a Product Hunt promotion three weeks ago. To do that, we still need to centralize everything, and we still need Fivetran.


Unless, of course, we centralize that data in a different way.


# The problem is different


This is where things get interesting.


Though we’ve grown accustomed to seeing Fivetran as the natural line between SaaS apps and the data warehouse, ELT tools are actually a kind of awkward kink in this flow. They often operate as an unofficial middleman, manually mapping themselves to the APIs of the services they source from. It’s brittle—APIs can change without warning—incomplete—some data may not be available via an API—and inefficient—rather than getting told when things change, ELT tools usually have to scrape for updates. Fivetran and others do the hard work of dealing with all of this for us, but it can’t be cheap to support.6As customers, we pay that price somewhere.


We’d all be better off—well, all of us except ELT vendors—if more apps did what Segment does, and wrote data straight to the warehouse themselves.


SaaS vendors could charge for this service, opening a new revenue stream that’s considerably easier to build than an embedded BI tool. If customers are already paying usage fees to Fivetran to sync data to their warehouse, the sale is easy: Pay us instead of them. They could be aggressive about it too, by packaging bulk access to their APIs with the syncing service, which would choke off Fivetran’s ability to run the syncs on their own.


Customers would probably prefer to buy these pipelines directly from the SaaS provider. It’s one less vendor to deal with, and would probably cost less. Most importantly, though, vendors could provide a better service than Fivetran. An native syncing product would be more reliable, because the SaaS app and the data pipeline would be managed by the same people; it’d be faster, because vendors could push data to the warehouse in real time when the app updates; it’d be more efficient—and therefore cheaper—for the warehouse, because it wouldn’t rely on bulk updates.


Warehouses might make efforts to support this as well. For example, Snowflake, which clearlyhas ambitions to be the hub of the data ecosystem, could build simple ingestion APIs for SaaS services to write to. The more apps that create native integrations into Snowflake, the more Snowflake’s gravity builds—if you know you want to centralize your SaaS data, and all your SaaS tools can write to Snowflake, you probably buy Snowflake. And the easier it is to build these syncs, the more SaaS vendors could and would offer them.


Granted, if this happens, Fivetran has at least two defenses. First, I’m probably underappreciating how hard it is to build these sorts of syncing services, and the amount of effort that goes into handling errors, retries, not dropping data, alerting people when something breaks, and so on. Admittedly, I know nothing about this point, or how durable of a defense it is.7


Second, there will always be SaaS apps that don’t want to build a feature like this, or warehouses that vendors don’t write to.8But I doubt this protects Fivetran as much as it might seem. If the biggest SaaS providers start creating their own pipelines, Fivetran has to sell on the tail of popularity distribution. That tail is long—but the money’s in the body.


This, to me, is the biggest structural risk to Fivetran. Apps build outlet stores, and goDTC. SaaS vendors giveth Fivetran its market; SaaS vendors could taketh it away.


# The problem is better solved by someone else


Of course, Fivetran could also lose in the boring way: Another tool takes them head on, andbeats them at their own game.


One version of a better Fivetran is Fivetran plus...much better observability. Or Fivetran plus real-time pipelines. Or Fivetran plus way more integrations. Or Fivetran plus built-in (ugh) Data Contracts™. I can see the value in all of these additions, but if anyone's going to build Fivetran Plus, it’ll probably be Fivetran.


A second version of a better Fivetran is Fivetran minus...the cost. A product that runs on open source connectors could offload the effort of building and maintaining those connectors to the community, while providing a hosted service that runs them. This would presumably lower the cost to customers. Airbyte, for example, claims to beten times cheaperthan other ELT alternatives.


Still, despite Airbyte’s assurances to the contrary, I’m skeptical that this“open core” modelcan compete with Fivetran on quality. Connector maintenance is tedious work, especially across the long tail of infrequently used integrations. Even if people get compensated to maintain them, the four-hundredth most popular SaaS connector is, by definition, not going to make much money. I suspect the only way to fund the development of these integrations—which, unlike open source software packages, have to be vigilantly updated alongside the corresponding SaaS app—is by using the money that’s made from the lucrative ones. That funding model—pay engineers in one part of the business to make features that are subsidized with profits from another part of the business—starts to look a lot like a more traditional software company, and erodes most of the potential cost savings associated with the open source approach.9


Open source tools could also displace Fivetran if people decide it’s cheaper to host them themselves. Like all compute-driven SaaS services, Fivetran surely adds a healthy overhead on top of their own AWS (or GCP, or Azure) bills. As buyers, we could run a service like Airbyte ourselves, and pay those compute fees at cost.


I’m skeptical of this too. The data market is moving aggressively towards hosted services. While there are a lot more conversations about thefinancial implicationsof this migration, our preference is clearly tilting away from self-hosted software. Rising costs might slow that lean, butit won’t reverse it.


A final version of a better Fivetran is Fivetran…a Snowflake Company (or Amazon, or Microsoft, or Databricks Company). For the same reasons I mentioned earlier, database vendors have an obvious incentive to make it easier for customers to load data into their products. It gives them more opportunities to spin their usage meters; it means they don’t have to recommend other vendors to their customers to help them source data.


But, it seems unlikely that any of the major databases will build a true competitor to Fivetran on their own. It’s more plausible for someone to buy Fivetran outright—just as Google did (andsquandered)with Alooma. Given thecurrent prices acquirers are payingfor premier SaaS companies, it’d be hard to characterize this result as anything other than Fivetran succeeding spectacularly.


# The problem is the crystal ball


Putting all of this together, my best guess is that, if Fivetran gets dethroned, it’s a combination of events10that does it. Warehouse providers start building ingestion APIs to encourage more people to write data into them; major SaaS vendors begin selling integrations with those warehouses.11Fivetran loses their most profitable integrations, and has to focus on the long tail of nonessential connections that make less money per dollar spent to develop and maintain. This leads to erosion of Fivetran’s business economics, a long decline in growth, and Fivetran’s eventual reclassification as a fringe tool in the modern data stack.


Is this likely? Probably not. Fivetran is the leading product in space that’s growing on both ends, and my bet is almost always on inertia.12But if my past predictions about the ELT market are any guide, I’m not very good at making bets. And sometimes, the future that looks unreasonable and impractical today ends up looking right and natural tomorrow.


---


# An addendum on Snowflake


I went through this same obnoxious contrarian exercise with Snowflakea couple weeks ago. After reluctantly digesting other people’s criticism,13my views have evolved a bit: The most important determinant of Snowflake’s success will be its marketing.


Right now, Snowflake is a database with a bunch of new features hanging off the side. If they can convince people that it’s actually a single cohesive platform that can’t be separated into its component parts, Snowflake will be extremely hard to unseat. We’ll want to pay for the cohesive experience, not for each feature. We’ll want the full product, and not a bare bones open source database running on our own AWS metal. We’ll wantthe iPhone, and not a disconnectediPod, phone, and internet communication device.


But if they don’t convince us of that—if Snowflake becomes a database, with frilly bells and whistles—people will start to shop for something cheaper. They’ll look for ways to get their core needs met without paying for the unnecessary add-ons and upsells. And they’ll potentially migrate from a database witha hundred small featuresto a database that’s one giantduck.

[1](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-1-73615268)

Stitch wasstill part of RJMetricsat this time.

[2](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-2-73615268)

I stand by the best definition of the modern data stack is data tools that launched on Product Hunt.

[3](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-3-73615268)

In a forgotten bit of esoteric history, Segment originally wrote data to a Redshift databasethat they hosted. White-labeling Redshift like this was briefly a trend—Periscope Data did the same thing—and, though it faded reasonably quickly, it’s interesting to imagine a world where this pattern had stuck.

[4](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-4-73615268)

Or, I guess, move towards data meshes, though I’m gonna be honest—these seem like the same thing.

[5](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-5-73615268)

Relational database, very lindy.

[6](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-6-73615268)

I will say, I respect the simplicity of Fivetran’s business model: Find the tedious work that everyone does but hates doing, and just do it for us. I think more startups could be successful this way. Don’t out-innovate the competition in the sky; outlast them in the salt mines. (Counterpoint:Don’t do that.)

[7](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-7-73615268)

Well, not nothing. I’ve built two syncing services at Mode: Goatherd, and Goatherd Lambda (it’s important to have two goatherds; otherwise they getlonely). Do they work? I can’t be sure, because they don’t have anything for handling errors, retries, not dropping data, alerting people when something breaks, and so on.

[8](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-8-73615268)

IBM’s cloud data platforms—which includes DB2—made elevenbilliondollars in 2020. There’s a decent chance that this is more than every modern data stack vendor combined.

[9](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-9-73615268)

There’s an indirect way that Airbyte (and tools likePortable) could compete on price though. In the process of developing open source frameworks on which the community can create connectors, these companies might uncover ways to make connector creation easy. Easier to build connectors are cheaper connectors, even if all of them are built in-house.

[10](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-10-73615268)

And abloody pen.

[11](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-11-73615268)

Two hours before this got published, this…started happening?

[12](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-12-73615268)

It’s kinda my thing.

[13](https://benn.substack.com/p/how-fivetran-fails#footnote-anchor-13-73615268)

it’s friday, why are people fighting with me?
