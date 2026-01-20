---
title: "The metadata money corporation"
subtitle: "The only enduring standard is greed."
date: 2022-01-14T17:14:00+00:00
url: https://benn.substack.com/p/metadata-money-corporation
slug: metadata-money-corporation
word_count: 1787
---


![](https://substackcdn.com/image/fetch/$s_!qJ8_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9b6c32d4-2ae6-4dc5-8f02-76aef3c35a58_1200x800.png)


There are a few mandatory slides in every data startup’s fundraising deck. You need a two-by-two matrix, with your company's logo in the upper right, preferably larger and in more vibrant colors than your competitors’ logos. You need a slide with a single number, in enormous font and sourced from a paywalled Gartner report that you didn’t read but found a reference to in a competitor’s press release about their inclusion in it, claiming your total addressable market is worth tens or hundreds of billions of dollars. You need to extrapolate six months of paid trials, sold to friends and previous coworkers, into a five-year revenue projection that exceeds $100 million. You need at least one quote about how data scientists spend80 percentof their time cleaning data, or how we’ve created90 percentof all the world’s data in the last two years. And you need to show how your solution will create a new standard for some messy data practice, finally consolidating disparate approaches into a unifying consensus. If you’re feeling particularly bold, you’ll call it a protocol.


This last ambition—to create a new open standard—is the "network effects" of modern data companies. For a time, consumer startups (and some enterprise ones) sold their ideas to investors on the promise that growth begets more growth. As more people use the product, network effects make it more valuable, drawing more people to the product and making it more valuable still.


This phenomenon is real and powerful—for many social apps like Facebook and Twitter, it’s both their growth engine and competitive moat. But it’s also rare. Most companies create very weak network effects,1and attempts to build around them are often dangerous distractions from focusing on product and marketing fundamentals. Network effects often make for better funding pitches than actual flywheels.2


For data companies, there's a tempting parallel: The open standard. The data ecosystem is messy and fractured, and lots of tools solve similar problems in inconsistent ways. To bring order to this chaos, we’re constantly rolling out new standards tounite the factions, the one ring to rule them all. Superficially, the reasoning makes sense:Standardized marketscan be very efficient for everyone—and very profitable for whoever owns the standard. More subtly, much like network effects, selling the potential to be a standard lets companies spin stories about how their growth curves can go vertical.


To this end, we’ve builtvariouslibrariesfor logging data; there aremultiplestandardsfor data ingestion; we’ve createdlotsofdifferentformatsfor data storage;transformationandmetricgovernanceare defined in different paradigms; we’veopen-sourcedanalyticalpackages;orchestrationand“DataOps” are configured in different ways; there areseveralcompetingmodelsfor metadata management; and we have visualization frameworkscomingoutofourears.


Sometimes, the new productblows up on Hacker Newsand turns into a $3 billion exit. Other times, it gets a handful of stars on Github, and few signups for its community Slack, and fades into oblivion. But in nearly every case, the idea lives or dies on its own merits. And—as wouldn’t be the case if they truly created durable standards—past performance doesn’t guarantee future success. Stitch pioneered the idea of an open standard for ingestion; Airbyte, a two-year old startup, recently raised $150 million to replace it. Looker built a popular new way of modeling data with code; three months ago, one of Looker's founderslaunched an overlapping idea. Standards that are only standards until a better idea comes along aren’t really standards at all.


Instead, the story of most companies’ success is pretty dull: They built useful products and beloved brands, in markets with lots of willing buyers. The rest is fable and folklore, the conflation of social proof and a high NPS with somethingmuch more mythical.


# Squaring up


The data industry is running headlong into this reality. For years, as the space has been exploding outwards, companies have been able to operate in the breach. Silicon Valley, which calls competition eitherscaryorstupid, taught us that this is the winning strategy: elbow out space for yourself; carve a niche that you can own; be a category creator; define a new standard. This tendency has been further encouraged by today’s community-defined modern data market, in which most companies are more comfortable building brands around open platforms than overtly hawking a corporate product for cash.


But the landscape is getting crowded, and its unincorporated territories are becoming too small to represent new categories in the eyes of the customer. Buyers don’t spend nearly as much time studying the distinctions between vendors as the vendors themselves do, and what can seem like category-defining differences from the inside are minor details to everyone else.


![](https://substackcdn.com/image/fetch/$s_!XuwV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F97fe2652-ac65-4074-a957-ea76942155be_990x666.png)

*Themodern data stack, to customers.*


In light of this, there's something refreshing—and foreboding—about the ongoing fight betweenCensusandHightouch, and theperformance warsbetween Snowflake and Databricks. In both cases, nobody’s making bones about where they stand: toe-to-toe, in direct competition. Rather than trying to out-maneuver one another with bank shots aboutcoopetitionand open-source standards, they’re squaring up. And ironically enough, everyone probably ends up winning: consumers get better products; companies get more focus.3Because there are so few actual “standards” and therefore, so few actual winner-take-all markets, multiple vendors can—and in the case of all four of these companies, I believe, will—build very valuable businesses.


There’s a lesson to be learned in this. As much as we all want to be the$3 trillion platform and marketplace, there’s plenty of money in the apps built on top. And for now, as others are jockeying for position in an unwinnable race to standardization, it’s easier money too, just as it was in the early days of the App Store. Eventually, though, the space will tighten, the gold rush will get crowded, and we’ll turn our picks and shovels on one other.


# Privatizing metadata


One area where this philosophy could be immediately applicable is in metadata management. Today’s data stack is quickly fracturing into smaller and more specialized pieces, and we need something thatbinds it all together.


There are a few projects and products that fill this space,includingopen-sourceframeworksthat aspire to be the new “open standard for metadata.”  These platforms offer bold visions not just for glueing everything together, but also for establishing a canonical axle around which the entire stack spins.


But, could the solution be…smaller? The stack isn’t missing another hub or aspirational standard; it’s missing plumbing.


More specifically, speaking as a representative of a vendor, I’d love to surface information about what’s happening across the data stack directly in Mode.4To people writing a query or looking at a dashboard, the statuses of Stitch pipelines, dbt jobs, Redshift queues, and Monte Carlo tests all provide important context. That context, however, is hidden in other tools, out of reach and out of mind. While Mode could integrate directly with these products, it’s impractical for us to build and maintain integrations with even a fraction of the tools in a landscape as expansive and dynamic as the data industry. Open standards could solve this problem,ifeveryone consolidated around that standard. A snowball’s chance, as they say.


Two of the modern data stack’s biggest successes pioneered a better way forward. Segment, staring down the barrels of hundreds of third-party APIs, made no attempt to standardize them; they simply did the hard work for us, giving its customers a single API to write to all of them. Fivetran did the same in reverse, creating one tool to read from scores of disparate APIs.


The data stack could use a similar switchboard. Connect to all of the APIs of various data tools; present all of that information back through a single set of endpoints; let people turn connections on and off just as they can in Segment. To get information from every tool in the rest of the stack, vendors would only need to integrate with a single API, no new standards necessary. Just cold, hard product, sold for cold, hard cash.


This sort of tool may not make for the most compelling investor pitch or community launch. There wouldn’t be many slides painting grand visions of virtuous growth cycles; the company’s addressable market, limited to “modern data stack vendors,” wouldn’t be the sort of number you put in 200-point font. (Although, if the data market is worth $1 trillion, scraping off one percent of one percent of that still gets you your path to $100 million.)


But, slides are just stories. It’s what happens after you raise the moneywhen the real work starts. And in the case of wiring together the modern data stack—and, I believe, in building the next generation of data tools—more than standards to be built, there’smoney to be made.


---


# Are entities standards?


Regular readers may be wondering…what? Didn’t you just propose some nonsense aboutentity standardizationlast week? Isn’t that a standard?


In a way, it is. Which, if nothing else, shows how strong the pull of standards is. Even for a hater like me, it’s hard not to be drawn to their potential.


But, the entity layer proposal is a proposal for a standard architecture, not a standard library. For better or for worse, we’ve had more luck agreeing to the former—ELT over ETL, centralized data warehouses, in-database transformations, and so on—than to the latter. I think that’s because architectural standards rely much less on (always elusive) network effects. They can work in a vacuum: My life is made better by choosing the “right” data architecture regardless of what you choose, and defaults emerge because what’s good for you is probably good for me. By contrast, for libraries for logging events or data structures for modeling metadata to be valuable as standards, we both have to choose the same thing. And data people aren’t exactly known for beingagreeable.

[1](https://benn.substack.com/p/metadata-money-corporation#footnote-anchor-1-47120080)

Some people claim that Zoom, for example,grew because of its network effects. Zoom is viral—my Zoom link exposes you to the product—but there are no meaningful network effects. My usage of Zoom doesn’t improve your experience on Zoom, nor does it degrade your experience on Google Meet.

[2](https://benn.substack.com/p/metadata-money-corporation#footnote-anchor-2-47120080)

In recent years, the network effect moat fad has been replaced by the data moat fad. This claim says that growth is a virtuous cycle because more usage creates more data, which creates more accurate models and better in-product features (e.g., improved recommendations on Netflix), which creates more growth. This, too, is mostly fiction.

[3](https://benn.substack.com/p/metadata-money-corporation#footnote-anchor-3-47120080)

And the blogging peanut gallery gets a show worthy of NBA Twitter. Databricks claims to set aworld recordin database performance;Snowflake saysit’s a “marketing stunt lacking integrity;”Databricks callsthe response “sour grapes.” Census launched under the banner ofoperational analytics, andnow embracesReverse ETL (and started their ownperformance wars); Hightouchintroduces themselvesas “the very first company to coin the term ‘Reverse ETL’” on a blog called theOperational Analytics Blog; Census says the term waspopularized in 2019; Hightouch claims theycame up with itin December of 2020. Inject it all straight into my veins.

[4](https://benn.substack.com/p/metadata-money-corporation#footnote-anchor-4-47120080)

Making Mode, I suppose, adata appfor data people.
