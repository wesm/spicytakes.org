---
title: "Internal tools make lousy startups"
subtitle: "The inside of a company is a misleading market."
date: 2022-10-14T16:04:58+00:00
url: https://benn.substack.com/p/internal-tools-make-lousy-startups
slug: internal-tools-make-lousy-startups
word_count: 2548
---


![](https://substackcdn.com/image/fetch/$s_!FERj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa07918ad-9a80-49cc-9896-fcd4c61636b8_2308x1242.jpeg)

*We love your bear, but we don't want to buy your bear.*


I'm an aNgEl iNvEsToR.


I started my investing career in public equities—in a grand total of three companies, to be exact. In 2000, as a Christmas present, my grandmother gave me one share of Krispy Kreme right after the company’s IPO. It was a good first investment—the stock rose from $21 to over $50 in three years—but, in some analog version offorgetting my crypto wallet password, I lost the ceremonial certificate that came with it, and had no way to sell it.1Twelve years later, I bought my second stock: Microsoft shares, as part of theiremployee stock purchase plan. Microsoft went to the moon after that, rising from $28 to a high of $343 in ten years. Savvy as ever, I cashed out at $32. In the final move of my day trading career, and ina manic feverof FOMO, Ijoined the Reddit circusand bought six shares of GameStop. Twelve hours and a roller coaster ride later, my diamond hands turned to paper, and I sold all of them. Other than that, all I've ever bought is the S&P 500.Giddy up.


Two years ago, I “diversified”into data startups. My approach to angel investing was as sophisticated as my strategy for stocks: Everything was going up, it was making people rich, and I wanted to be rich too. Needless to say, I'mstill available on the VC draft board.


Proper investors, by contrast, have real theses around what they buy. They have someparticular view of the market; somecontrarian perspective; some differentiating sharp edge. They writecredos, and publishmanifestos. They believe in the cloud, orin AI, orthat founders shouldn’t be older than 32. They don't shotgun cash based on gut or greed; they findpatterns in the numbersthat nobody else sees, and exploit them.2


Fine. If I had to come up with my own manifesto—ifbenn.venturesneeded a new ethos topromote on Twitter—here’s what I'd go with: Beware of companies that are inspired by internal tools.


# Product-coworker fit


The lifecycle of the typical internal data tool seems to go something like this: The data team has a problem, and nothing in the market solves it exactly the way they want. For example, an ETL tool might be missing an important integration, doesn't load data quickly enough, or can’t mask sensitive data in the way that the company needs. Or a BI tool trips over important stored procedures, or can’t make exactly the visualization that the CEO wants.


Someone then steps up and says they can build the solution themselves. Often, their motivation isn’t entirely pure; yes, they want to solve the problem, but they also think it’d be a fun project to take on. Everyone loves a hack day, and creating internal tools can feel like all the good parts of software development without the annoying ones. You start from a blank slate with no debt, you know your product will get used, and you can often shortcut the tedious things—deployment, security, testing—that are required for customer-facing products.


The tool gets built. The tool gets used. It looks like a profound success. Not only did it help the company, but the team found some hole in the public software market and filled it. Its creators start to wonder: did we strike gold? This narrative sounds especially appealing when the new service was created inside of a high-flying startup. Look at the talent of the team that built the tool! Look at the success that the tool helped create!


It’s usually all a mirage.


There are three fallacies that make internal tools look more promising than they actually are. First, the obvious one—they have a customer base of one. It’s easy to find product market-fit when your market is your coworker sitting right next to you, telling you exactly why the other products they’ve tried don’t work.


Second, internal customers often have no alternative. They’re a captive buyer. Even if they don’t like it—if the builder actually misses the market—people are compelled to use it, because they’ve been told they have to, or to be a good sport and support the team that made it.


Finally, the need that inspired the tool in the first place is, almost by definition, a rare edge case. Though that could represent an undiscovered opportunity, it’s more likely that it was unaddressed by other tools because nobody else wants it. Does Uber’shuge investment in mapping technologymean that there’s some latent demand for geospatial analysis out there, just waiting for the right product to tap it? Or does it mean that Uber cares about where people are more than anyone else?3In some cases, internal demand and market demand might even be inversely related. The more a company “couldn’t live without” some tool they couldn’t buy, the further their need likely was from the average customer in the market.


# One size fits one


Still, even this undersells the problem. The value of the tool itself is only half of the illusion. The other half—and the more overlooked issue—is distribution.


Assome VCs will tell you, distribution can make or break a startup.4Companies have to figure out how to get their products in front of buyers, how to show them what it does and why it’s worth paying attention to, and how to deploy it alongside other software and among existing processes, all while navigating theinternal politics of the purchasing organization. This can be a far harder problem than building the technology, especially if the product is part of an interconnected ecosystem of other tools.


Internal tools can often bully their way through these obstacles. Teams don’t need to market the tool to anyone; they walk over to people’s desks and tell them they have to use it. Nor do internal tools need to support a variety of technical integrations; they just need to work with the company’s current database, or with the existing SaaS services. And internal tools don’t have to sell people on different workflows or new ways to run their teams; they either fit into processes that are already in place, or the top-down decision to build the tool and update a process are made together, where each supports the other.


Take, for example, OKR management software. Suppose, hypothetically, that some team inside Figma built an application for administering and tracking OKRs across the company. If they wanted to spin their platform into a new startup—the team behind Figma’s operational excellence! The secret fuel in Figma’s $20 billion execution engine!—VCs would throw cash at them sight unseen.


But consider the problem that team solved inside of Figma compared to the one they’d have to solve outside of it. If Figma used Salesforce for tracking sales goals and Github to record engineering issues, the internal tool could not only integrate directly with these products; it could also make assumptions about exactly how they’re configured and used. More importantly, the OKR tool could also be designed around whatever goal-setting method Figma was using. Presumably, part of the reason for building the tool in the first place was to streamline an existing framework that’s already working for Figma. The tool’s “buyers” didn’t have to be sold on the need to define key results in the way the tool encourages, nor did the team that managed Figma’s objectives have to convince other departments to standardize around their particular flavor of OKRs. All of these were either in place, or were mandated as part of the decision to build the tool.


Outside of Figma's friendly confines, none of this is true. Companies set goals in different ways—OKRs,5V2MOMs,subversive OKRs,messed-up OKRs—if they set them at all. Everyone uses different SaaS products as their systems of record, and they use them in different ways. And OKRs can be a contentious topic between teams, with different departments preferring different structures and approaches. Selling into a market like this requires selling a lot more than a single product; it also requires selling a philosophy, a process, and a bunch of counseling sessions to get everyone to agree.6


# No Snowflake is the same


Because data stacks now have so many components, and because no data team is structured quite the same way, this dynamic exists all over the data ecosystem. Every data product sits at the intersection of a dozen roles, processes, and other technologies. Internal tools are often bespoke bits of tile that fit exactly within the mosaic of each company—a perfect shape for the picture they’re in, but not useful anywhere else.


Airbnb’s Minerva is a good example of this. It’s ametrics platformat the center of Airbnb’s stack, andthe inspiration for Transform, a generalized metrics store. Though Minerva is undoubtedly quite useful to Airbnb, much of its value comes from howtightly coupled it iswith Airbnb’s dashboarding suite, data catalogs, A/B testing and ML platforms, and operational tools. Selling Minerva on its own would be like pulling the engine out of a BMW and offering it to people who drive Toyotas. The engine doesn’t work the same without the rest of the car. Case in point: Transform recentlyadded a BI tool.


This explains, I think, why the community conversations around data contracts and the data mesh have felt so unmoored. Both proposals are also like car engines—you can’t easily remove them from the context in which they operate. Data contracts, for example, are a political entity as much as a technical one. Even if teams don’t have to agree on what’s in the contracts themselves, they at least have to decide how tocreate,enforce, andlitigatethem. A type of data contract thatworks well at one companyis anathema to another because of the political realities within the two organizations. What prospers in one environment might be poisonous in another.


Much like OKRs, both the data mesh and data contracts seem, as a best case, destined to splinter into a hundred different variants, where no company uses them in quite the same way. That makes for very rocky ground forvendors, which all feel like Figma’s fictional OKR spinoff: Based on small, specific, and highly successful but ultimately inimitable examples.7


# A better incubator


Of course, not all in-house tools make for bad companies. There are plenty of successful counterexamples, and there will be plenty more. However, relative to theirperceivedvalue—as measured by how much funding they seem to attract—I think they’re generally overpriced. If there were data on such things, I’d guess that building a popular internal tool at a successful company isn’t the strong signal that it first appears to be.8


Instead of lurking around the data teams of recently acquired unicorns, venture capitalists should look at consultancies and professional services teams. These organizations work with a much wider range of customers, sometimes build technicaljigsto help their clients, and have to work with and not around company politics. Products that help consultants—and even better, products that have been proven to work with consultants’ clients—are likely to have far stronger legs than some glittery tool at a Silicon Valley darling. An Indianapolis-based engineer from Monster Data Solutions, LLC may not have the same pedigree as a Facebook VP, but I’d bet they have more battle-tested ideas. But I’m an index fund guy, so I would say that.


---


# How Mode fails


The challenge of turning an internal tool into a company hits close to home for me for another reason: I’ve walked that road. Mode wasbased on something we built at Yammer and Microsoft, and for years, I saw this as proof that our vision was right. In hindsight, our prior experience acted as blinders that kept us stubbornly on the path that we’d seen work before.


This both helped and hurt us. On one hand, it committed us to building a cloud-only, SQL-based data product before that was the norm, and the market eventually (and luckily) came around to those standards. On the other hand, the first version of Mode was perfectly designed for teams like the one we’d been on, and was an uncomfortable fit for everyone else. Because of the success of the tool we’d been inspired by, it took us too long to come down from that soapbox.


Had Mode failed years ago, this would’ve been its cause of death: We misunderstood the market we were building for, made a thing that wasn’t useful to enough people, and ran out of money before we realized that we needed to step out of the shadow of the internal tool we were trying to emulate. Today, our challenges are different, but stillrelatively mundane: How do we build the right products and attract customers in acrowded, confusing, and ill-defined consumption layer?IfModefails, its headstone will have the same boring epitaph as hundreds of other startups, including many of today’s data companies—the product missed the market, and someone else hit it.


That’s what makes asking aboutSnowflake,Fivetran, anddbtmore interesting. They were bullseyes, hitting their target so squarely that their success now seems inevitable. Thehater’s guide to data toolswas never meant to be a series of product teardowns or company critiques; it was meant to be a paranoid search for things thatmight stop the remarkable musicthat those three companies are dancing to. For the rest of us, we're still hunting that beat.

[1](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-1-78395588)

I did, however, get quarterly shareholder reports for about a decade.

[2](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-2-78395588)

Or so they say. In most cases, these “strategies” are more brand than blueprint. They look good to LPs who want to feel like they’re giving their money to smart people, and they get likes on Twitter. But once a pitch comes across investors’ desks, philosophies go out the window—it’s mostly gut, emotion, and the feelings about “pounding on the table.” If a VC gets excited about something, they’ll find a way to shoehorn their market thesis around their investment memo, just as I could with my “strategy” ofcopying what the rich people do.

[3](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-3-78395588)

Theaggrieved ex-boyfriendscertainly do.

[4](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-4-78395588)

The fun thing is you can complete this sentence—“the key to startup success is ___”—with anything you want, google it, and find some random blog post from a self-proclaimed serial entrepreneur or angel investor that makes the case for you. Is distribution the key to a startup’s success? I have no idea, but my Google search saying it was gave me results saying it was.

[5](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-5-78395588)

The author of this post is “Google.”

[6](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-6-78395588)

It’s telling that a number of startups haveraised a bunch of moneyto do exactly this, and the default OKR tracking software is probably still a spreadsheet.

[7](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-7-78395588)

My guess is that specific implementations are like a baseball player’s swing: each person has to find what works for them. Right now, at this stage of the conversation, we’re all looking at only a handful of examples and wondering if that’s the right form for us. Kevin Youkilis thinks he foundthe secret to being a great hitter. The rest of us think we’d fall down if we tried that. And everyone is right.

[8](https://benn.substack.com/p/internal-tools-make-lousy-startups#footnote-anchor-8-78395588)

There’s another more pointed risk with these companies: Their founders are used to being successful. People who build popular internal tools (or create popular open-source projects, or are just internet famous) are accustomed to running downhill. This can amplify the dangerous feeling of “if I build it, they will come” that’s already present in a lot of companies that are inspired by internal tools.
