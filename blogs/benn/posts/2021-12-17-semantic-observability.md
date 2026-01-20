---
title: "Fwd: Exec KPIs - Daily"
subtitle: "in board call and revenue looks off, pls advise asap"
date: 2021-12-17T19:13:02+00:00
url: https://benn.substack.com/p/semantic-observability
slug: semantic-observability
word_count: 2121
---


![](https://substackcdn.com/image/fetch/$s_!QZ8-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7b0f8968-0a4f-450d-b359-5acf08dad245_1024x768.jpeg)


The dashboard worked, but it didn’twork.


Somewhere, in the twisted labyrinth of its aging diesel engine, my friend’s forty-year-old Land Cruiser sprung a leak. The jeep would irregularly lose oil, sometimes shedding an entire quart in just a handful of drives. Other times, its pipes held together, and it’d go weeks without losing a drop. To compensate for the problem, my friend built up a variety of habits to make the car safe to drive. Before starting it, check the dipstick. Always store a spare quart in the glove compartment. On long drives, check the oil every time you get gas.


The warning lights on the car's dashboard—the gas meter, the check engine light, the temperature gauge—all worked as intended, and were still useful for the problems they identified. But because the car’s designers didn’t anticipate that, after 200,000 miles and nearly half a century of wear, it’d randomly eject critical fluids, there was no oil alarm. And that omission, impossible to anticipate and potentially isolated to this single jeep, made an otherwise reliable car frustrating and dangerous.


—


The dashboard worked, but it didn’twork.


Somewhere, in the tangle of ETL pipelines, transformation jobs, Jinja templates, SQL queries, and visualization encodings, retention rates started to drift. The complicated process for booking renewals in Salesforce, plagued by the various details necessary to distinguish between an upsell, a multi-year renewal, and a coterminous contract addition, was inconsistently followed. To compensate for the problem, we developed a habit of spot checking every renewal, comparing KPI dashboards with sales directors’ notes to make sure everything always matched.


The warning lights on our data stack—Fivetran alerts, dbt run failure notifications, automated anomaly detection—all worked as intended, and were useful for the problems they identified. But because the dashboard’s designers didn’t anticipate every possible quirk and edge case that would find its way into a two-year step-up upsell with tiered triggers for overages, there was no alarm for catching when the numerator on our retention rate started to double-count several renewals. And that omission, impossible to anticipate and isolated to a few opportunities, made an otherwise reliable metric wrong.


And unlike the story about the Land Cruiser, this one ended in a crash: misreported numbers, bad decisions, and eventually, an embarrassing and painful correction.


Every data team has war stories like these. We all know the panicked feeling when we realize that a key metric has been wrong for three straight board meetings;1we’re familiar with the terror of seeing an error in a CSV that's already been sent to a customer; we go through the same internal debate of asking ourselves if that inflated number in the deck we just presented is worth correcting.2


More than anything, these are the problems—the quiet failures, the lurking mistakes, theunknown unknowns3—that keep us up at night. They're the ticking time bombs that prevent a data team from resting easy, and the anxieties that make no subject line more triggering than “Fwd: Exec KPIs - Daily.”


# Modern data complexity


The modern data stack, unfortunately, makes this stress worse. The simple Salesforce dashboard has been replaced by ELT jobs unloading data from Salesforce, batch loads into a warehouse, overlapping dependencies of templatized SQL queries, YAML files that define measures and metrics, and visualization parameters that configure the final dashboard. It’s a delicate balance of complex operations, each as critical as the next.4


In response to this problem, we did what we do best: created a new category, and built more tools. In the last few years, data observability—the warning lights for our data infrastructure, the dashboards for our dashboards—was born,broke out, and, as is in vogue these days,drowneditselfincash.5


I don’t yet share the same excitement. Observability tools solve a useful problem, but, like the Land Cruiser dashboard that ignores an oil leak, they don’t ease my paranoia about what problems could still be hidden in the engine.


Though each product is different, observability tools generally help companies see the structure of their data pipelines, and what’s actually flowing through them. The first view is a map (or DAG, if you prefer) that draws lines from data sources to dashboards and other analytical assets. It also defines how those pipelines should be shaped—expected schemas, data types, and other structural elements. If something in this diagram finds itself out of place, we’re alerted to this structural anomaly.


The second view monitors what’s happening in those pipes. It records when data is extracted from a source, how many records were updated, how long it took, and if anything went wrong in the process. A second category of alerts are triggered by statistical anomalies, when some data point is outside an expected bound (a user enters their age as 450 years old) or if data volumes deviate from normal ranges (including, especially, if volumes fall to zero).


In other words, data observability tools provide two windows into a data stack: One tells you if your data pipelines are built correctly and if theyshouldwork, and another tells you if they actually did.6


This is all well and good, and certainty catches problems we may not otherwise see. And for massive datasets feeding sensitive models, like a stream of credit card purchases that back a fraud prediction algorithm, this may be all that’s necessary. But for most of us, there’s a third category of anomaly that’s more common than a Segment event stream going haywire, more difficult to track down than a broken Fivetran pipeline, and more insidious than a flatlining dashboard: The semantic anomaly.


Semantically anomalous data is structured correctly—it has the right schema, strings are indeed strings—and is statistically uninteresting—it’s an acceptable number of records, and doesn’t include a row for a transaction of negative eighty trillion dollars—but is still wrong. It’s data that misrepresents the business concept it’s supposed to capture. It’s data that, on the trip from measurement to meaning, got lost in translation.


These anomalies happen when an account manager enters a renewal contract in Salesforce without closing out the existing contract, double-counting the customer’s revenue in a key KPI dashboard. They happen when the operations team adds a new stage in the sales process, and sales cycle lengths are still computed using the old sequence. They happen when a new product release starts logging background events on the latest version of an iPhone app, and these events lead the mobile team to gradually overstate the number of daily active users.


These cases, and the millions of other versions just like them, create results that are just as wrong as those built on top of broken data pipelines. Unlike a broken pipeline, however, they don’t look suspicious and they trigger no warnings, in observability tools or in our manual spot checks. Instead, they often linger undetected, slowly and silently pushing the analytical assets that use them further and further from reality—until, during a board meeting, on a customer call, or in an angry midnight email from the CEO, the bomb goes off.


# Keep talking and nobody explodes


Admittedly, most observability tools aren’t trying to address this problem directly. As an individual vendor, that’s a reasonable choice. Startups have to be focused, and semantic anomalies are different in degreeandkind than structural and statistical ones. Moreover, today’s observability companies aren’t just building status pages for the modern data stack; some are more focused on keeping logging infrastructure clean, or helping teams profile data as they’re updating it.


Still, as a category, data observability can only go so far without addressing semantic anomalies. For people who want to know if they can trust the data they’re seeing—for people who want to know their data is reliable—the distinction between a broken pipeline and a misreported metric is irrelevant.


So how do we defuse the bomb? We acknowledge it, we isolate it, and we talk about it.


Acknowledging the problem requires admitting whatwon’tfix it: More rule-based and statistical tests. Though it’s true that most semantic anomalies could be reduced to assertions like “this field should always have values in this range,” or “the value in this date field should always be earlier than the value in that date field,” it’s impossible to write a rule for every potential problem. Data, like an old Land Cruiser engine, can go wrong in more ways than we can enumerate. Moreover, unlike a car engine, businesses are constantly changing, and no test suite could ever keep pace.


It’s also tempting to monitor the outputs as well as the inputs, and build tests and outlier detection systems on dashboards themselves. But this doesn’t really help either; semantic anomalies are often problematic precisely because they look normal. A handful of incorrectly labeled ad conversions would easily slip through this type of test, even though misattributing this data could lead to millions of dollars being spent on the wrong marketing campaigns.


Instead of generalized tests, we need specialized tools that directly target and isolate semantic anomalies. One version of this could focus on common sources of confusion: duplicated assets,organizational entropy, and data stacks’ general states of disrepair. If we could allprune stale data modelsas efficiently as Good Eggs ordedupe metricsas reliably as Uber, we’d have a much easier time maintaining the assets we keep.7


Another, more ambitious version of this approach would aim to solve semantic problems with semantic solutions. Just as general BI tools know nothing about the meaning of the data they contain (Mode, for instance, knows if fields are numbers or strings, but has no concept of what revenue means), general observability tools have no conceptual awareness of what they’re monitoring. Tools like Amplitude, by contrast, are semantic BI tools. They can more easily figure out when something’s gone wrong in a dashboard—for example, if a user retention rate is more than 100 percent—because their dashboards understand what they represent.


Vertical observability tools (or vertical features in existing observability tools) could follow the same principle. If we know that data comes from Salesforce and that it represents customer contracts, we can create semantic assertions like, “Can a single customer have multiple active contracts?” These sorts of tests are not only easier to maintain and understand, but they can automatically compile the various technical assumptions—the tests in general observability tools—that are implied by each assertion.


Finally—in the inevitable note about people being at thebottom of everything—we all have to keep talking. No observability tool, from the nascent ones in the market today to some future sentient AI, is a substitute for the data team knowing what the marketing team is doing. Relying entirely on automated alerts trains us to put too much trust in something thatisn’t intended to drive entirely on its own.


But, even in the absence of autonomous semantic observability, we could use more assisted semantic observability. While all undetected anomalies are bad, it’s the semantic ones that really sting. A failed pipeline has the feel of an inevitable outage, abuck that can be passed, anact of Godthat’s just part of life with computers. Semantic anomalies are mistakes. They’re human errors, the things we should’ve caught and didn’t. They’re the biggest bombs waiting to be dropped into our inbox, and the ones I’d pay a lot of money to disarm.

[1](https://benn.substack.com/p/semantic-observability#footnote-anchor-1-45650004)

And like dropped toast with jelly, they always fall in the wrong direction.

[2](https://benn.substack.com/p/semantic-observability#footnote-anchor-2-45650004)

“There were lots of numbers in the presentation, will anyone notice if we just change it, no, no way they do, plus, it’s better for the team if I don’t say anything, if I say something people won’t trust us, yeah, this is about the team, definitely, if it were just me I’d say something, of course I would, not saying something is actuallyharder, I’m being brave, for the team, it’s for the team.”

[3](https://benn.substack.com/p/semantic-observability#footnote-anchor-3-45650004)

Betcha thought you were gonna get aDonald Rumsfeldreference there but NOPE THAT’S NOT HOW WE DO IT AT BENN DOT SUBSTACK DOT COM.

[4](https://benn.substack.com/p/semantic-observability#footnote-anchor-4-45650004)

There’s another, softer effect of the complexity too: People are reflexively more skeptical of it. Rightly or wrongly, tools like Google Analytics appear more trustworthy because there are fewer visible moving parts.

[5](https://benn.substack.com/p/semantic-observability#footnote-anchor-5-45650004)

For full disclosure, I’m a small investor in Bigeye.

[6](https://benn.substack.com/p/semantic-observability#footnote-anchor-6-45650004)

Other people who think much more deeply and clearly about these sorts of things (i.e., the makers of data observability tools)describe these categoriesin a more granular and technical way: Observability is about metrics, metadata, lineage, and logs. That works too, and bonus points for the catchy alliteration.

[7](https://benn.substack.com/p/semantic-observability#footnote-anchor-7-45650004)

Does the metrics layer solve this? Yes and no. On one hand, it narrows the problem. The fewer places metrics are represented, the fewer places they can be wrong. On the other hand, it makes the problem harder by adding more layers of abstraction between a data source and the person interpreting it.
