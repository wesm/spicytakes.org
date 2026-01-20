---
title: "How much for that DAG in the window?"
subtitle: "There's a theoretical price and a real price."
date: 2023-08-25T16:02:10+00:00
url: https://benn.substack.com/p/how-much-for-that-dag-in-the-window
slug: how-much-for-that-dag-in-the-window
word_count: 2649
---


![What Channing Tatum's New Movie 'Dog' Gets Right About Military Working  Canines | Military.com](https://substackcdn.com/image/fetch/$s_!rWZc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F987f6ac0-96cb-4bfc-ac1e-18711da297a5_621x414.jpeg)

*Are dags our best friend? Or will theykill us?*


If you want to know the id of white man in tech, ask him what kind of bar he wants to open.


The men who see themselves as tastemakers will describe a bougie cocktail bar with a curated list of small batch bourbons and gins. The menu will call tequila “agave;” it will specify which drinks are served up and which are neat; there will be no substitutions. They will recommend that their staff follow themenswear guy.


Insecure tech bros will dream of opening a dive bar in Detroit, or Baltimore, or some rusted-out machine shop in Richmond. They’ll talk about servingNatty Bohand Jameson, because aperformative appreciation for cheap beerwill definitely convince the locals that, despite growing up in Alexandria and making four million dollars from the Figma acquisition, they’re not one ofthoserich men.


Self-described entrepreneurs will tell you that their bar will be next to a laundromat, will be a vodka bar because Moscow mules are thehighest margin cocktail, and will be near public tennis courts because studies have shown that recreational tennis players have incomes that are some significant percentage higher than the national median. Everything else will be decided by the market.


Men who wish they were in college will open a sports bar. Men who wish they were in their twenties will open a craft beer bar. And men who wish they were podcasters will tell you that if you’d listened toAndrew Hubermen, you’d never open a bar.


My bar would be Frisco’s, located in Hayes Valley in San Francisco. The outside will be unassuming and understated; the inside will be a gaudy and obnoxious carnival. It will be a celebration of San Francisco, designed by someone who’s never been to San Francisco. There will be bad murals of SF’s proudest landmarks, like the Golden Gate Bridge, the painted ladies, andRice-a-Roni. Some tables will look like cable cars; others will be up several flights of curvy stairs. Some will be under heaters, and some will periodically get cannoned by amisting fan. The menu will be full of horrific—and horrifically named—drinks, like the Mission Margarita, a 32-ounce mix of well tequilas, Sweet’n Low,Mango Madness Snapple, aBud Light Lime-a-Rita, and some liqueur that turns the whole thingroyal blue.1When you walk in, the entire staff will yell, “Welcome to San Fran!”2


Ever the cradle of innovation, Frisco’s won’t simply charge a flat price for their drinks. Instead, you have to pay rent: We charge you for your table, by the hour. Early in the afternoon, prices are affordable—rent is low, and drink prices are set at a discounted rate. Get there early—get in on the ground floor—and you canlock in your rentand rights to lower drink prices for as long as you’re at the bar. As it gets later and more crowded, prices of both will go up. People who show up at peak hours pay steeper rents and a higher dollar-to-drinkmultiple.3Until, late at night,4the hype bursts, people start to leave, and prices crash. And then, tomorrow,we do it all again.


Of course, this probably wouldn’t work, because it is insane. But it’s noteconomicallyinsane. Some people could argue, somewhat reasonably, that traditional, pay-per-drink pricing is unfair, because it lets people idly take up space and enjoy ("enjoy") Frisco's ambiance without paying as much as the steady drinkers. Other people could argue, somewhat reasonably, that they should get a discount for coming early or staying late, when demand for a seat at the bar is much lower. And others could even argue, somewhat less reasonably butplausibly, that the point of coming to a bar is to have a drink, and charging for every single one discourages customers from being successful. If I want eight Muni Martinis,5why should I be punished for wanting to be a thriving customer? Plus, that lastSex on the Ocean Beach6was actuallybadfor me; is it really fair to charge me for something that I didn’t need but was tempted into buying?


Nobody says any of this though, because it issociallyinsane. This is not how bars work. We have standards for these things, and people expect businesses to stick to them—even when the thing they’re buying is marked up500 percent.


Pricing is like that. Even for something as simple as a bar, it’s not as economically fixed as it seems, nor are there natural laws that make some pricing models inherently right or wrong. Lots of pricing structures could make financial sense; each one has tradeoffs that favor some customers over others. We mostly accept pricing as a matter of precedent. If, for the last hundred years, bars charged by the hour and gave us one drink every thirty minutes, we’d probably see it as equitable and just. And when one started charging us for drinks, we’d riot.


# The best, in theory


Two weeks ago, dbt Labs started chargingby the drink:


> Beginning August 8, 2023 we are taking our first step in a journey towards offering more consumption-based pricing for dbt Cloud. After a ton of research—both via customer calls and looking at the data—the metric we’re going to use to measure consumption is the number of model materializations that dbt Cloud has successfully built on your behalf.


To admit my bias here, I have an earnest fascination with dbt pricing, because there is no obvious market precedent for how it should work. dbt is part infrastructure application and part developer tool; it couldconceivablybeextendedinadozenotherways; it’s very popular, but its most popular element is free.As much as I enjoygawking at the hot goss about these sorts of things, in this case, it’s the analyst in me—curious about an economic puzzle—that’s drawn to this problem.


The interesting exercise here to me isn’t to figure out what’s wrong with the new model relative to the old one. For bars and SaaS startups alike, every pricing model has tradeoffs, and has its winners and losers. It’s easy to find fault in a change to these sorts of things, because there’s fault in all of them. Instead, the question I have is what pricing model would be the best—the best!—if dbt Labs were launching today. If it had no customers on its books and no expectations in the market, how should it charge for its products?


I tried to figure this outten months ago, didn’t see a way to make seat-based pricing work, and landed on exactly what dbt Labs did:


> Though dbt Labs was initiallysuccessfulin selling seats, it didn’t scale with their ambition. If we assume the average revenue per seat is about $125 dollars a month, or $1,500 dollars a year, dbt Labs would have had to sell more than 300,000 seats to get to $500 million in revenue—the eventual number required to justify their2022 fundraising round. That’s not an impossible figure, but it would be an awfully steep climb, especially whenother products start offering competitive—and free—development environments.…Usage-based pricing was the obvious choice, though the optics of this model proved tough. Most metered SaaS products charge seemingly trivial prices for vast amounts of usage—twenty centsper million Lambda invocations;$0.0075per text;five hundred emailsorten thousand synced recordsfor a dollar. For the math to work out for dbt Labs, each invocation of dbt run would have to cost about 25 cents. At that price, customers start to flinch at pushing the run button, especially if they are also paying the database to actually execute those runs.There were other metering options though, like charging for every call to dbt Server or for every run of every model. Ultimately, dbt Labs settled on the latter option—customers pay each time an individual model gets invoked. This pushed the unit price of each action down to something more psychologically palatable; it scales directly with customer adoption; unlike charging for dbt run, it doesn’t encourage people to create teetering monolithic dbt jobs to save costs; it still makes sense in a world where dbt runhas less meaning; it meters development and production in a fair way, because small development runs cost a fraction of big production ones.


There are other reasons why this model makes sense to me, if you were starting from scratch. People use dbt to create and update tables in their warehouse; for every model a dbt customer “buys,” they are ostensibly getting something—a new table, a fresher dataset—that they want. It’s also an expense that customers can control relatively well. Reducing the number of models in use, turning down refresh cadences, and turning some materialized tables into views are easier and more precise adjustments to make than, say, optimizing query runtimes or reducing the number of events logged in a tool like Mixpanel.7


This change also discourages “bad” behavior. One complaint that people sometimes have about dbt is that it creates an unwieldy mess of SQL dependencies; another is that itpiles unnecessary compute into metered warehouses. Charging by model aligns customers’ financial incentives with best practices for sustainable use.8


Most tellingly, asking how dbt Labs would launch its pricing model today isn’t an entirely speculative question. Though Dagster9isn’t an identical product to dbt, it’s similar. It orchestrates ETL jobs. It’s open-core. It sells a cloud product. It’s builtin a lab. Free to define a pricing model without the weight of thousands of customers on top of it, Dagster launched one thatcharges for seats and usage. If dbt was just building momentum too, I’d argue it should do the same.


# No plan survives first contact with the enemy


Of course, all of this is somewhat academic—dbt Labs isn’t starting from scratch. While there’s not a clear general precedent for how a product like dbt should be priced, the market has a clear expectation for howdbt specificallyshould be priced. And that, rather obviously andpredictably, is the real tension here. dbt is valuable, people are accustomed to getting to use the open source parts for free and the cloud parts for relatively little money, and dbt Labs is not a charity.


This is no doubt a problem, though I think it’s worth recognizing exactly what the problem is: A social one, about pricingexpectations. It’s the same problem with Frisco’s novel rental scheme—people are used to using and buying dbt Core and Cloud as they were, anddon’t want to use or buy them as they will be.10That’s perfectly reasonable, but it’s a different issue than dbt not being useful at all.


That said, I’m not sure that it’s an easier issue to resolve. If a product isn’t useful, you can make it better, and people will enthusiastically buy it. If your product is already useful but people are used to getting it for free, trying to claim that value is a very delicate line to walk. Even if the final destination is the same in both cases—people getting something they want at a cost that’s tolerable to both buyer and seller—one will earn you accolades for being a good, customer-focused business, and the other will get you accused of exploitation.11


So what do you do? Honestly, I don’t know. But, in this light, dbt’s decision topermanently grandfather existing customers into the old pricing modelcould end up making some rough sense.12One way to work around entrenched pricing expectations is to just charge people how they’re used to being charged. If you expect dbt Cloud to be sold by the seat, you pay by the seat; if you’ve never bought it before and don’t have any specific expectations for how you’ll be charged—which you probably don’t, since there aren’t clear market precedents—you pay for usage. I mean, I dunno; it’s clunky, but it could work.


The other, more elegant way out is probably to build more features, in both dbt Core and Cloud, that specifically appeal to buyers who never had expectations of using dbt for free—i.e., the ever-looming enterprise. If Twitter’s excitement for the modern data stack and its various novelties aren’t representative of the broader market—and it probably isn’t—then Twitter’s willingness to glue together homegrown versions of dbt Cloud withAirflowand GitHub Actions probably isn’t either. Enterprise buyers don’t want headaches. They don’t want rogue AWS services managed by decentralized teams. They want easy administration, SLAs, and professional services attached to their vendor contracts. And if they want dbt Core, that means they probably want dbt Cloud too.


So do they want dbt Core? I have no idea. But I can certainly imagine there being things that could be added to dbt Core to make it more attractive to these buyers. And that’s ultimately the point—to keep growing, dbt Labs may not need to pile features into dbt Cloud; they may need to pile features into either Core or Cloud that appeal to people who won’t use one without the other.


---


If the id of a man is in his bar, the id of a company is in its customers. The people who pay for a product are the people who it gets built for. That’s why every specialized analytics startupbecomes a BI company for the masses, why community projects become commercial platforms, and whyClarence Thomas should be impeached.


I’m sure that dbt Labs wants to build for its longtime fans, and wants to keep serving the customers who made it popular. But if those customers prove too stingy—for rational economic reasons, for social reasons, for reason of chance or dbt Labs’ own making, it doesn't matter why—their ability to keep using dbt will have to be subsidized by some other buyer. And dbt’s id will inevitably come to reflect that.

[1](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-1-136402036)

Officially, the “Mission Margarita™, brought to you by Rakuten.”

[2](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-2-136402036)

The extra ingredient behind Frisco’s incredible popularity will be itsspicy attitude.

[3](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-3-136402036)

Unless, I guess, people who got there early sell their drink rights on a secondary market.

[4](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-4-136402036)

In San Francisco, “late at night” is 9 p.m.

[5](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-5-136402036)

When you order a Muni Martini, we tell you it’ll be ready in three minutes; no, eight minutes; no, forty minutes; no, actually, it’s been canceled and won't be coming tonight.

[6](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-6-136402036)

Peach vodka,Five Alive, topped with mango White Claw. Served on the rocks. No substitutions.

[7](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-7-136402036)

People sometimes say this is unfair, because it “penalizes success” or “discourages customers from using the product.” On one hand, this is true. On the other hand, what pricing model doesn’t, in some way, discourage people from consuming a product?

[8](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-8-136402036)

You could, I suppose, argue that, by charging per run, dbt Labs is encouraging itself to promote these sorts of behaviors. That’s possible, but I’m not sure you can have it both ways? If one pricing model is bad because it monetizes people’s carelessness, I’m not sure that another one can also be bad fornotpenalizing the same carelessness. Moreover, to return to the bar, if the goal is to protect people from alcoholism, it seems like we should be lobbying for bars to charge per drink and not per hour at the bar. Surely, economic incentives have a stronger effect on people’s behavior than public service announcements to drink responsibly.

[9](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-9-136402036)

I’m asmall investorin Dagster.

[10](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-10-136402036)

Case in point: One of the complaints I’ve seen about the new pricing model is that dbt shouldn’t charge for runs because it doesn’t cost them anything material to run them. But dbt Labs’ margins on provisioning a new user are almost certainly higher. Nobody raised that objection for the last several years, though, because all of us expected to pay for users.

[11](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-11-136402036)

dbt is far from the only example here. Elon Musk’s effort to make people pay for Twitter was always going to be a disaster for largely this reason (the other reason beingElon Musk). And just a couple weeks ago, HashiCorpsparked a riotby trying to make more money from Terraform.

[12](https://benn.substack.com/p/how-much-for-that-dag-in-the-window#footnote-anchor-12-136402036)

Obviously, this particular decision didn’t seem to be part of a master plan, but a response to how customers took the initial change.
