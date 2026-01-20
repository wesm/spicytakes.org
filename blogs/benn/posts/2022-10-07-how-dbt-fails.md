---
title: "How dbt fails"
subtitle: "For sale: data company, worn out."
date: 2022-10-07T16:40:21+00:00
url: https://benn.substack.com/p/how-dbt-fails
slug: how-dbt-fails
word_count: 2956
---


![Photographs Ernest Hemingway Having Fun Boxing In Cuba Photo Great Writer  Photos Artwork 8x12 Home & Kitchen](https://substackcdn.com/image/fetch/$s_!pwmZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcec73e32-7aad-478e-a130-8c5b1c966230_1000x674.jpeg)


For most startups, the road to hell is paved with predictable problems. They create a product that nobody wants; the market they serve is too small; they chase a vision they can’t fulfill; they waste money running ineffective marketing campaigns and building unused features; they fail to execute, sputter along and flame out, and eventually wind the whole thing down or disappear inside of some disappointing acquisition.


Some companies, however, die more interesting deaths. They beat the usual demons—unrequited product-market love, underwhelming demand, poor product adoption, general mismanagement—and lose their fortunes for more exotic reasons. The productjustmisses the mark; the marketcollapses underneath them; the economicsnever add up; the businessfully detaches itself from reality. These are the startups that build a war chest and a lead in the market, and, because of someunforced errororunforeseen obstacle, end up losing anyway. They’re the companies that were always going to be business school case study; the only question was if they’d be a winner or a warning.


In the data industry, no company is more likely to end up in an HBS classroom than dbt Labs.1


Its unconventional origin story is the stuff of Silicon Vally fan fiction—a startupbegat a consultancy; a consultancy begat an open-source product; an open-source productbegat a software company; a software companybegat a revolution. The rest is charmed history. For those of us in the data community, the dbt Slack has become our watering hole; Coalesce,our pilgrimage; and dbt itself, not only essential, butourproposedsolutionforeverything. Given such a golden run, the only data industry story that would be more captivating than one about dbt Labs’ success would be one about its failure.


Though I don’t think that it’ll happen—just as I don’t thinkSnowflakeorFivetranwill fail—there is somedark timelineout there that ends with a room full of twenty-something MBA students having a snotty debate about how they would’ve saved dbt Labs from its eventual fall from grace. Prior to that discussion, they’ll all read acase studythat chronicles what went wrong.


This is my guess as to what it’ll say.2


---


# No money, no problems


dbt Labs’ first obstacle was to turn a free thing into money—and in their case,a whole lot of money. Popular open-source projects aren’t destined to be commercial successes, and dbt’smost obvious stumbling blockwas that it would end up as something we all use but never pay for.


This wasn’t a major issue, for a few reasons. First, dbt Labs expanded their core offering from an open-source package into something that looksmore like a traditional SaaS service. dbt Labs also preempted the possibility dbt being resold by cloud vendors through itslicensing of dbt Server.3Second, unlike most open-source software, dbt isn’t primarily used by engineering teams, but data teams thatsit in between engineering teams and business departmentslike sales and marketing. These latter groups tend to raise fewer objections about paying for out-of-the-box products than engineering teams (no sales team wants to run an open-source version of Salesforce; no HR team wants to run an open-source version of Workday). Finally, as dbt’s customers evolved from open-source purists andhacker analysts-turned-analytics engineersinto enterprise procurement teams, the more compelling its SaaS offering was over a do-it-yourself framework that has to be managed on its own.


Figuring out whatpeople should payforwas a tougher question. dbt Labs’ original business model was built around selling seats on dbt Cloud, which clearly understated the value that dbt provides. At most companies, everyone who uses data is helped by dbt, but only a handful of people need seats to develop in it.


Though dbt Labs was initiallysuccessfulin selling seats, it didn’t scale with their ambition. If we assume the average revenue per seat is about $125 dollars a month,4or $1,500 dollars a year, dbt Labs would have had to sell more than 300,000 seats to get to $500 million in revenue—the eventual number required to justify their2022  fundraising round.5That’s not an impossible figure, but it would be an awfully steep climb, especially whenother products start offering competitive—and free—development environments.


That left dbt Labs with two choices: Either compel more people to buy seats, or change the business model. The first path is the slow road to BI, which wasoff the table. The other option was to bill customers for something other than user licenses.


Usage-based pricing was the obvious choice, though the optics of this model proved tough. Most metered SaaS products charge seemingly trivial prices for vast amounts of usage—twenty centsper million Lambda invocations;$0.0075per text;five hundred emailsorten thousand synced recordsfor a dollar. For the math to work out for dbt Labs, each invocation ofdbt runwould have to cost about 25 cents.6At that price, customers start to flinch at pushing the run button, especially if they are also paying the database to actually execute those runs.


There were other metering options though, like charging for every call to dbt Server or for every run of every model. Ultimately, dbt Labs settled on the latter option—customers pay each time an individual model gets invoked. This pushed the unit price of each action down to something more psychologically palatable; it scales directly with customer adoption; unlike charging fordbt run, it doesn’t encourage people to create teetering monolithic dbt jobs to save costs; it still makes sense in a world wheredbt runhas less meaning; it meters development and production in a fair way, because small development runs cost a fraction of big production ones.


Sensible as this pricing was, rolling it out caused some angst among a community that was becomingincreasingly cost-conscious, and had grown accustomed to using dbt on the cheap. In the end, though, data teams needed the value dbt provides, dbt Labs had the means to capture it, and most of their enterprise customers didn’t balk at paying for it.


# Live by SQL, die by SQL


The long-time headline on dbt Labs’ homepage—”Transform data, transform teams”—captured what dbt had been for the the first six years of its existence: A tool for data transformation. But dbt expanded beyond that—in late 2022, dbt launched asemantic layer.


As Simon Spätiwisely pointed out, transformation layers and semantic layers are different things (and dbt had beensupportive of this distinction). When data is transformed, it’s typically prepared ahead of when it’s needed, on a schedule, in batch—like, say, a nightly job to clean up a messy transactions table into something usable. Semantic layers, by contrast, are a kind of on-the-fly query compiler: You ask for a particular metric or dataset, and the semantic layer figures out the right joins and aggregations to get you what you need.


On the one hand, dbt expanding into the semantic layer made sense. The line between transformation layers and semantic models, though present, is blurry; as a customer, I’d ideally define both in a single tool where each operation is aware of the other.


On the other hand, it was a fundamentally broken marriage.


When dbt was first released, its promise was simple and elegant: It’s SQL, all the way down. We can build pipelines query by query and table by table, one predefined building block at a time. The downside of this approach is that there’s no true relational model inside of dbt. There is a lineage graph that shows how tables are derived, but not anentity-relationship diagramthat defines how those tables are related to one another. Each is largely independent of the other.


Though dbt’s first semantic element—metrics—could get by without a complete model underneath it, metrics gave dbt’s user base asemantic cookie. Inevitably, people started asking for more. They wanted todefine joins; they wantedmore complex metrics; they wanted the logic within one metricto be accessible in another. To fulfill these asks, dbt had to add more and more semantic complexity.


dbt Labs tried to add these capabilities to their SQL-heavy core, but SQL alonewasn’t able to do it.7Just like every other prior effort to build a semantic model, dbt Labs ended up building acomplexsemanticlanguageof their own.


This put dbt on its heels. Unlike other the modeling languages that came out at the same time—MetricFlow, Cube, Metriql, Malloy—dbt Labs’ language had to be shoehorned around an existing query- and table-based foundation. That forced some awkward product choices, like an initial reliance on Jinja, which slowed development and customer adoption.


Still, dbt Labs won much of the market.8Thousands of companies were already using dbt, wanted to keep using dbt, and were willing to put up with rough edges to keep doing so. But it weakened dbt’s position as the pacesetter in its categorical box. By pioneering the SQL-based transformation layer, dbt Labs sold to customers with few preexisting expectations. Adding a semantic layer cost dbt Labs that luxury—customers had demands, and dbt struggled to meet them.


# The briar patch


dbt’s semantic also added a new problem: It made dbt opaque.


One of the underappreciated elements of dbt is how easy it is to follow what it’s doing, especially compared to other data pipeline products. Within a dbt project, SQL queries are run in a sequence to create tables. Each model is declarative and self-contained; you can read it and check the result it produced. If data at the end of a long pipeline looks weird, you can walk backwards through each step to figure out what happened.


Semantic layers are more of a black box. You configure the layer, and the queries get written for you. This makes incorrect results hard to debug, especially as the layer gets get more complicated.Python modelscompound this problem by addingexternaland potentially cross-model dependencies. As does Jinja, which dbt uses partly as configuration and partly as a programming language—and it’snot great at either.


From the beginning, dbt projects already had the potential to bearchitecturally complex.9The addition of computational complexity on top of that pushed dbt to a breaking point. Done well, a robust transformation layer, connected to a semantic model, augmented by Python, and extendable with something like Jinja would be immensely powerful. But it’s difficult to balance these things correctly. As dbt Labs rolled them out, the initial calibrations were inexact. Customers struggled to manage it, and a lot of dbt projects became briar patches of unparsable Jinja, entangled Python and SQL models, and an incomplete semantic layer. It was then—during countless late nights of analytics engineers debuggingthatnightmare—that the community’s affection for dbt started to fade.


# Blood in the water


The community was always dbt Labs’ true advantage. It’s an unmatched distribution channel; it’s an enormous audience that evangelizes fordbt’s beliefs; it’s a legion of users that provide feedback, build integrations and add-ons, and sometimes contribute directly to dbt itself.


It was also protection that scared off a lot of would-be competitors. For a time, companies that were building products that should’ve competed with dbt bent over backwards to explain why they were actually complimentary.10The dbt community was family, andnobody takes sides against the family.


When things were going well, this, much like an iconic brand, was an unbreachable competitive moat. No matter how good your lipstick is, you’re not going to outsellKylie Jenner.


But brands don’t last forever. As dbt expanded into new areas—new markets, new pricing schemes, semantic layers, Python models—it lost some of its sheen. Part of that came from age and fading novelty, part of it from dbt selling to people who were less online and less eager to adopt new technologies, and part of it came from some of the inevitable missteps that come from building new things.


This decay of the community was a slow but fatal disease. At its core, dbt is a relatively thin piece of technology (and an open-source one at that). Given how valuabledbt’s real estate isin the modern data stack, any sign of blood from dbt Labs—especially if it comes from a souring community, a chink in dbt Labs’ thickest armor—will attract a lot sharks.


Some companies took direct swings at dbt Labs—dbt withsmarter schedulingto save costs; dbt for the enterprise; dbt builtexclusively for Snowflake. dbt Labs was able to deflect most of this competition; no one, after all,was better positionedto build a better dbt than dbt Labs.


The indirect competition did the real damage. Warehouse vendors, in their effort to be thebackend of everything, tried to attract more workloads by building semantic models directly in the database. For example, BigQuery began supporting Malloy natively. Malloy became to SQL whatTypeScript is to JavaScript: Asyntaticsemantic superset to raw queries.


Other companies took on dbt by offering a richer modeling layer. Startups likeModernbuilt products that could create semantic models across a range of data sources (i.e., a multi-database LookML). This technology proved more successful at managing sprawling enterprise data infrastructures than dbt.


Orchestration tools like Dagster11undercut dbt with development environments explicitly built for creating multi-source,multi-destination, and polyglot data pipelines. They were able to copy the beloved parts of dbt Core more quickly than dbt Labs was able to add dynamic scheduling, robust support for Python, and the other elements that people wanted in their transformation layer.


Finally, new startups began to sell against dbt’s complexity. The industry started to debate if it was time for dbt to be unbundled, and if we would be better off separating transformations from semantics, SQL jobs from Python models, and runtimes from schedulers.


The result was a war on multiple fronts. dbt struggled to build competitive products that went beyond its original version; customers grew frustrated as dbt lagged behind their expectations in those new areas; dbt’s star lost its luster, and new companies started to jab at dbt Labs. The community turned its attention to these tools and technologies, emboldened competitors began taking direct swings, and eventually, dbt Labs gotcaught in the corner and died.One generation passeth away, and another generation cometh.


---


# The future


When we see a company that connects with the market as well as dbt Labs has, it’s natural to assume that something must be a mirage. It looks great, butsurelywe’re overlooking something. Surely there is a fault somewhere in their stars.


And so, snarky and cynical people who haveweirdwaysof entertaining themselves cook up indulgent thought experiments to figure out why things might not work out. We concoct exciting and cinematic narratives about failure, and convince ourselves that they’re reasonable.


The actual answer is more obvious: It’s all real. dbt is a beloved product; the industry cherishes it, and will tolerate its flaws and relax hardline feature requirements because dbt makes thousands of people capable of doing things we otherwise couldn’t. Yes, dbt Labs will face its moments of difficulty, but exceptional peaks don’t always come with exceptional valleys. Instead, it will likely have to deal with the same hard things that most growing companies deal with: Rapid expansion causes moments of organizational turmoil; new products don’t always work out; they become an incumbent, and upstarts eat at their edges.


Despite it all, dbt Labs’ unforgettable start probably isn’t a warning, but a precursor to unforgettable future. No matter how many words we write about it, the final story about dbt issuccinct: It’s a damned good product, and it’snot just pretty to think so.

[1](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-1-77057156)

For clarity, when I say dbt Labs, I’m referring tothis company. When I say dbt, I’m referring to any product that dbt Labs produces, including dbt Core and dbt Cloud.

[2](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-2-77057156)

I wrote the rest of this post as though it was written in 2030, describing events that would’ve happened around 2025. How do tenses work if I’m writing that 2022? As you’ll soon find out, I have no idea.

[3](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-3-77057156)

The rebranding of Fishtown Analytics into dbt Labs was also a clever maneuver, because it makes clear to the market who owns—if not literally, but spiritually—dbt’s open-source elements. You can google Kafka without finding Confluent, but you can’t google dbt without finding dbt Labs. (In both cases, though, your first results are aboutanxietyandexistential dread.)

[4](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-4-77057156)

The team seat price isfifty dollars a month. Enterprise seat upcharges are typicallyabout five timeshigher than listed prices. I’d also guess that the average enterprise seat is discounted twenty percent, and that half of all sold seats are on enterprise plans. Given those numbers, dbt Labs would collect, on average, about $125 a month per seat.

[5](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-5-77057156)

Asanais valued at $4.4 billion on a $500 million run rate;Pagerdutyis worth $2 billion on $281 million in revenue;Oktahas a valuation of $8.8 billion on annual revenues of $1.3 billion; acrossall SaaS companies, enterprise valuations are roughly eight times revenue. dbt Labs was most recently valued at $4.2 billion; one-eight of that is $500 million.

[6](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-6-77057156)

dbt Labs invokesdbt runabout400,000 times a year. Given the size of the company and that dbt Labs is probably a heavy user of dbt, I’d guess the economics of metered pricing only add up if a company of that profile pays at least $100,000 a year, or 25 cents per run.

[7](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-7-77057156)

As a present-day aside, it’s certainly possible that dbt Labs actually pulls this one off, and figures out a way to define semantic models in something that feels like native SQL. I can’t quite see what that would look like, but that’s the advantage of having an enthusiastic community contributing to the product. If there’s a way, someone will find it.

[8](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-8-77057156)

There are two big risks to this. One is that isGoogle gets their act togetherand spins LookML out as anindependent layer. The second—and much bigger one—is thatstandalone metrics layerssimplydon’twork.

[9](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-9-77057156)

The road to hell is paved withunstaffed DAGs.

[10](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-10-77057156)

I know at least five examples of this.

[11](https://benn.substack.com/p/how-dbt-fails#footnote-anchor-11-77057156)

I have asmall personal investmentin Dagster. Lest you think that motivates me to say Dagster will beat dbt: If Dagster goesfull Figmaandtakes no more dilution along the way, I’d still have to take a loan tosend a kid to NYU.
