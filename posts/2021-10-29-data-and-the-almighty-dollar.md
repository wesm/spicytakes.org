---
title: "Data and the almighty dollar"
subtitle: "The data ecosystem is booming. The data economy has some things to figure out."
date: 2021-10-29T16:55:15+00:00
url: https://benn.substack.com/p/data-and-the-almighty-dollar
slug: data-and-the-almighty-dollar
word_count: 2475
---


![](https://substackcdn.com/image/fetch/$s_!tAf2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F115226c3-8076-4517-8d7d-e5efc9a09a41_800x491.jpeg)

*The modern data stack is an Alexander Calder mobile: Complex, delicately balanced, and expensive. Source:The McNay Art Museum.*


Halloween, I’ve heard, is the second most important night of Uber’s year. If this Halloween is likethat of years past, Uber engineers and operations leaders will be huddled around monitors and dashboards, tracking ride requests and active drivers, making sure some imbalance doesn’t sendfares through the roof. Metrics that people typically follow on a daily or hourly basis suddenly need to be updated every few minutes.


Though most of us haven't been in war rooms tracking the minute-by-minutemovements of an entire city, many analysts are familiar with lighter versions of this experience. We’ve had product managers who want to follow how a feature is adopted on the day of a big launch, CMOs who need hourly reporting on Black Friday sales, and operations directors who need frequent updates on the number of new orders coming in during the days leading up to Christmas. In these moments, the typical, casual latency of our dashboards isn’t enough.


In one sense, the modern data stack makes solving this problem easy. Update how often Fivetran extracts data from source systems, schedule a couple more dbt runs, refresh the Tableau dashboard or Mode report more frequently, and each system magically scales itself up to support the necessary load. It’s clicks and configuration updates; no hard work required.


In another sense, these changes are major headaches. Fragmented pipelines, spread across different vendors and tools, have to be kept in sync. Without a way to orchestrate them—whether that’s through adata OSor aconfiguration standard like Terraform—updates are disorganized and brittle. Fortunately, this fragmented user experience, and the need fora better one, is now a problem that’sgettingmoreattention.


But there’s a third—and largely unexamined—sense in which these changes can be problematic. Given the variety of tools wired underneath situation room dashboards, lowering their latency can lead to a cascading set of confusing and interconnected charges.


Refreshing a dashboard more often in Looker, for instance, will push more queries down to your warehouse. If you’re using a database that meters usage, like Snowflake, BigQuery, or Databricks, these extra queries add to your bill. Moreover, some BI tools, like Amazon’s Quicksight,collect their own feeswhen people log into them more often.


Of course, for dashboard updates to be useful, you also have to refresh the data behind them more often. If you’re using dbt, this requires running more dbt jobs, again adding load to the database. If you’re using a metrics layer with its own cache, you likely have to run queries to extract fresh data, and pay the metrics vendor for marginal additions to their cache. And you need to pull data from source systems more regularly, adding even more queries to the database’s queue and spinning the data throughput meters on Fivetran, Stitch, and Segment a little faster.


Lowering pipeline latency can have other indirect effects. Data observability platforms will run more tests; reverse ETL tools will fire more often. Both categories of tools typically bill for this extra usage themselves and, yet again, push more queries down to the database.


Every company’s particular tangle of charges and fees will vary, depending on the collection of tools they’re using and how exactly they’re configured. But some version of this story exists inside of every modern data stack. In its normal operation, costs are intertwined and opaque. And bigger updates and changes—whether it’s scheduling dashboards to update more often, adding a new data source, or onboarding a new department of users—rotate a face of Rubik’s cube, which rings half a dozen cash registers as it turns.


# The danger of the engineering analogy


Over the last few years, the heat in the data market has beenattracting hundreds of new companies, each looking to cut their slice out of a ballooning pie. Some of these products will inevitably fail, but many have already found useful wedges that cleave off a new corner of the market. In an effort to differentiate themselves andelbow others out of their part of the dance floor, companies are now looking for ways to define themselves as a new and necessary part of the modern data stack. So far, according to thepeople who catalog such things, we’ve fractured it into 28 distinct pieces.


Each category makes the data stack more technically robust—and more economically tenuous.


In our current ecosystem, most data products are still expensive to build. They require architectingnew frameworks, developingsmarter AIs, designingcomplex visualization systems, or reinventing howdata gets processed. Work like this isn’t cheap, and companies can only fund it if they promise to make real money on the other side. This sets a high floor for the price of data products.1


Furthermore, while high prices are a constant, data companies’ business models are not. Some products charge usage-based compute fees, some for user licenses, some for feature tiers, and some blend different mechanics. Some products are still searching for the best way to sell. And some, which bury their prices behind a handful of sales calls, don’t tell us what they charge for.


Data companies also sell to a variety of buyers. There are products that are marketed to data engineers and devops teams, to analytics engineers and analysts, to data scientists, to IT departments, to lines of business, and to uncertain mixes of different buyers. The “data” bill has no owner.


You could make the argument that this complexity is just a reflection of the growing importance and ubiquity of data. It is, in other words, the price of success.


Maybe so—but that doesn’t apply to other functions. In what other departments do companies need to buy a wide collection of expensive tools, bought by different people and priced in different ways, to solve a single set of problems? Equivalent scenarios border on the absurd. Imagine needing to build a CRM for a nascent sales team, and having to buy a tool for logging phone calls, a tool for logging emails, a tool that stores these logs, a tool that helps sales reps see the status of their opportunities, a tool that helps sales leaders keep track of their team’s performance, and a tool to alert you when other tools break. While products like these may get hung off of Salesforce at some point, they’re bought by growing sales teams, not integral legs to an eight-legged stool.


The more common comparison is that data products (anddata teams) are tracing the same path as web development stacks, which are also interconnected mobiles of tools delicately balanced against one another. In time, it's implied, our stacks will find the same equilibrium.


But the analogy is fatally flawed. Software stacks are built by engineers, who are comfortable wiring together closer-to-the-metaltechnologies. Many data practitioners are unwilling or unable to do the same. They want to buy hostedservices. If we were generally comfortable managing Spark ourselves, Databricks wouldn’t be worth nearly $40 billion.


A services-oriented industry appears likely to keep prices high relative to a technology-oriented one for two reasons. First, in addition to building core technologies, which are hard enough to develop on their own, companies have to build administrative chrome—user management, security infrastructure, web interfaces, customer onboarding, support and success services—in their products. Second, open-source standards have a harder time taking hold. While LookML could’ve become a standard for semantic modeling, Looker had little incentive to open it up because most people wouldn’t want or be able to run it themselves. An open-source LookML is a gift to Looker’s competitors, not to the community.2


And so, here we are. The ecosystem is creating category after category, throwing out product after product. Thus far, the market has absorbed them—but the dynamic is unstable. With few dominant players and fewer agreed-upon categorical standards, customers are choosing from a large inventory of small companies, offering dozens of startups enough of a foothold to reasonably claim that they provide more value than they cost. Furthermore, because of the variance in buyers and business models, the true cost of the stack is amortized across different teams and obfuscated by irregular billing logistics.3


But data teams and IT departments have budgets. Even if every product is worth it on its own, the collective cost eventually becomes too much to bear.4Something has to give.


# Bigger planets, better orbits


There are two simple ways out.


One is that nothing happens. Data becomes so valuable that none of this matters. We allbecome data companiesand, just as we don’t blink at our AWS bills (until we do), we accept the high price of data tooling as the necessary cost of doing business.


The second is a bloodbath. A few dominant players colonize most of the landscape, and small companies—and potentially entire categories—get squeezed out. The modern data stack becomes a cemetery of once-promising tools, and one of the surviving behemoths dances on everyone’s graves bygoing public with “MDS” as their ticker.


In a consolidated world, the stack’s economics start to make more sense. Everything collapses under one billing system, making purchasing easier to manage. And while different services may get broken out into their own line items, not every product has to run an independent profit. As long as the entire stack is worth its aggregate bill, customers and vendors both come out ahead.5


These aren’t the inevitable poles, though. There are potentially other, less severe ways to balance the economic equation.


Middle men could insert themselves between today’s vendors and buyers, offering everything from shopping catalogs of data tools6to a layer of software to manage those tools. Anumberofconsultanciesalready do this manually; thenext wave of companieswill do it automatically.


Whether or not they’re people or software, these administrative layers make modern data tooling more accessible and easier to operate. To lower a dashboard’s latency, you only have to turn one dial, not six. But it’s not clear how they lower the overall cost of the stack, short of making decisions for you about which tools to include and which to exclude.


Vendors themselves could also take steps to simplify the buying process as well. On the extreme end, companies could merge into large conglomerates, forming a suite of products akin to Atlassian (orMatch Group). Or there could be a rise in soft M&A, in which companies white-label themselves behind other vendors and through revenue sharing agreements. These arrangements would probably be beneficial to the market, but are surely a nightmare to work out.


There are also more complex solutions. Within each major category of the stack, a few key vendors (orplanets, if you will) could serve as platforms—in a real sense—for smaller services to build on. Salesforce, Slack, Stripe, and Shopify7show how this can play out: Companies offer platforms for other people to build on; this enriches the market bymaking it cheaperfor everyone to build new products; those products simultaneously fill the platform’s gapsandreinforce the platform’s dominance.


Forced to choose, I’d bet on the market consolidating into ten or so planets, with dozens of moons orbiting around each. This doesn’t necessarily imply, however, that the market is frothy, or that today’s startups aren’t worth the heady figures on their cap tables. The demand for these tools is there, and more is coming.8The problem is the composition of the supply, which is currently broken apart into hundreds of asteroids with no clear orbits, haphazardly bouncing into one another. To make this whole thing work, we don’t need less mass in the solar system; we just need more organization.


---


# Saving our battery


According to thehistorians of the modern data stack, Redshift’s launch catalyzed the entire movement. Prior to Redshift, we had to be careful with our warehouses; they were slow, expensive, or fragile. Redshift and its successors changed that. They became bulletproof, capable of handling anything we pile into them.


And pile on we have. Across the stack, tools now lazily lean on warehouses, hammering them with query after indiscriminate query. Need to tweak a filter on a dashboard? Run a query. Need to update a table in a database? Run a query. Need to re-sync your entire users table? Run a query. Need to validate your data against a test? Run a query. Need to push an email list to Salesforce? Run a query. Need an alert when a metric crosses a threshold? Run queries constantly.


Today’s warehouses can handle it—happily. Our debits are their credits.


I have no idea how many of these queries are extraneous, but it could easily be a significant number. At some point, when costs come into focus and we start taking a harder look at our receipts, we’ll want to do a better job of coordinating query load across tools. At a minimum, we could reduce load during down hours; more advanced solutions could recognize when a dbt model doesn’t need to update because Fivetran hasn’t run, or when an observability test can be ignored because the underlying data hasn’t changed.


![](https://substackcdn.com/image/fetch/$s_!ukML!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F89ec6d4a-0d4d-4695-878a-8541d71eb904_853x187.jpeg)


To extend the mobile operating system analogy, this could be another job of the data OS—offer a “battery saving mode” that allocates compute in intelligent ways. If nothing else, it’s an easy product to sell: It’s one thing to sell a tool that costs $10,000 with the promise of $20,000 of nebulous value on the other end; it’s something else entirely to charge $10,000 for $20,000 in Snowflake credits.

[1](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-1-43282170)

This dynamic is particularly apparent if you talk to very early-stage data companies. Nearly every company, including those built on an open-source ethos or with community ambitions, has a plan for “moving into the enterprise.”

[2](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-2-43282170)

dbt is an interesting exception here, which I partially attribute to dbt’s simplicity. In its earliest iterations, dbt didn’t need to be hosted; it just needed to be run. There’s a big difference between running a script on a schedule (though the first version of dbt Cloud proved that many data teams didn’t even want to do that) and managing a service like Airflow or running a database like Spark.

[3](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-3-43282170)

Imagine, for example, if every tool charged a per-user fee. We’d be much more sensitive to overlapping charges, and procurement departments would put more pressure on data teams to consolidate costs. With every bill accruing in a different way—a user fee here, a usage-based monthly charge there, a flat annual fee somewhere else—the total cost of the stack is harder to tally.

[4](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-4-43282170)

Is every Billie Eilish show worth more to me than the price of the ticket? Yes it is. Can I afford to go to all of them? Sadly, I cannot.

[5](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-5-43282170)

Selling software suites also makes for bizarre accounting gymnastics. In 2012, Microsoft SharePoint was simultaneously a$2 billion businessand a product even people working at Microsoft didn’t understand.

[6](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-6-43282170)

The modern data mall.

[7](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-7-43282170)

Very clever of Snowflake to start their name with an S.

[8](https://benn.substack.com/p/data-and-the-almighty-dollar#footnote-anchor-8-43282170)

Prove it, you may reasonably say. Fine—but later.
