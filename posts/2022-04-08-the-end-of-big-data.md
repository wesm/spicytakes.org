---
title: "The end of Big Data"
subtitle: "Databricks, Snowflake, and the end of an overhyped era."
date: 2022-04-08T16:21:10+00:00
url: https://benn.substack.com/p/the-end-of-big-data
slug: the-end-of-big-data
word_count: 1970
---


![](https://substackcdn.com/image/fetch/$s_!MqVK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8aa9755d-43fc-4c33-b2c8-80fc45db3ffd_1431x591.png)

*Thirty-eight billion dollars isn't cool. You know what's cool? Being boring.*


Databricks is a $38 billion dollar mistake.


As aninth largestprivate tech company in the world,1banking$800 million of revenueper year, it’s a mistake all of us would be lucky to make. But it’s hard not to look at Databricks and see a company selling to a bygone era. And the dizzying success of its competitors—Snowflake is worth $70 billion, even after its stock’sbrutal five-month slide; BigQuery, I’ve heard, books as much as $3 billion a year—suggests that, with a couple pivots, a repositioned Databricks could capture far more potential than it does today.2


I first heard about Databricks in 2014. It was Silicon Valley hype, manifest. Databricks’ founders were brilliant computer scientists turned reluctant entrepreneurs. They were reinventing big data, which itself was reinventing the entire world. Growth rates were straight up, and overloaded sales reps were leaving their phones off the hook.


When I looked it up, my first reaction was that it was built for people smarter than me. Instead of a demo or product screenshots, I found technical papers explaining something I didn’t understand. The case studies talked about real-time enterprise workloads, streaming Spark applications, and distributed, highly-scalable data science model development.


I needed a database. I was, at the time, spinning up a (pre)modern data stack: Segment, Fivetran, Mode, and, at the center of it all, Redshift.3Though Redshift worked reasonably well, it was starting to cause a few headaches. Keeping it up required regularly shuffling a couple large tables between it and S3, and the cluster status page was gradually creeping up my shortcut list on Chrome.


Eventually, after a failed attempt to migrate to Athena and Spectrum, we made the decision to go shopping. BigQuery was our presumptive favorite. It was frighteningly fast; it required no management; and several customers had recently told us about their successful transitions from Impala4to BigQuery. We took a call from Snowflake out of obligation—to see what else is out there; to do the diligence; to request the proposals.


The pitch we heard from Snowflake was both the dumbest and most effective sales pitch I’ve ever heard. We were told that it was the same as Redshift—and really, the same as Postgres—but big, fast, and stable. We didn’t see any glossy slide decks filled with stock images of strikingly handsome business professionals huddled around a conspicuously unbranded computer. We didn’t hear any customer testimonials from bank executives about how their five-year initiatives came in on schedule and under budget. There were no forced mentions of digital transformations, distributed systems, or, God forbid,the blockchain.They never even told us what we could use Snowflake for. We were told to just keep doing what we’d been doing, except if we did it with Snowflake, they’d host the whole thing, back it with bottomless storage, and run our queries faster than ever before—a strictly better,Pareto improvement.5


The pitch (and Snowflake) worked masterfully. As they undoubtedly anticipated, we started using Snowflake the same way we used Redshift, but quickly, after becoming accustomed to its speed and scale, found new things to do with it. Rather than worrying about precisely tuning our incremental loads in dbt, we started doing more full refreshes. We stopped carefully vetting which logs we wrote into our warehouse. We found new waysto share data with customers. We didn’t buy—and wouldn’t have bought—Snowflake for these things, but once they were so accessible, we happily picked them up.


Throughout our entire evaluation, we never considered Databricks.


In hindsight, we should’ve. Databricks is, just like Snowflake, a fast, hosted, almost infinitely scalable database. And, unlike Snowflake, it supports awider range of languagesthat could’ve opened up entire classes of new applications that, once accessible, we would’ve been excited to try. But we never connected these dots during our evaluation because the story Databricks told was buzzwords. Snowflake’s was boring, and all we wanted—at least at first—was boring.


# Data for the middle class


When the history books on the modern data stack get written,6two moments will thus far define its arc. One is dbt Labs stampeding through the ecosystem in 2020 and 2021, and the other is  Snowflake’s IPO.


These moments capture several key features of the era. First, they highlight two companies that at the technological center of what the industry is has been building for the last decade. Second, they validate its commercial success, through anenormous IPOand a two-yearfundraising tear. But most importantly, these moments finally closed the door on the breathless age of Big Data.


For years, data was talked about as if it were a massive stack of technological tarot cards. We’d read about it incryptic special reportsin theEconomistthat said we werehockey-stickingtowards a future governed by digitalMinority Reportmystics. Thepremier eventsin the industry, bankrolled by first-wave big data companies like Cloudera, Hortonworks, and MapR, hyped the same narrative: We have tons of data, and we’re going to change the world with it.


This story has completely changed. Indecipherable technologies have been replaced by boring ones, like a big Postgres database worth north of $50 billion, and open source SQL templates. And the conversation has moved from focusing on rare problems to common ones. Forall that’s been said about Data Council, there’s one way in which it was more firmly anchored to reality than nearly any other data conference before it: The problems people talked about were relatable. In 2014, for example, Strata, the leading data conference at the time,included talks titled​​Information Visualization for Large-Scale Data Workflows, Scaling Charts with Design and GPUs,andGetting a Handle on Hadoop and its Potential to Catalyze a New Information Architecture Model.These aren’t problems most organizations had in 2014 (or ever). At Data Council,many of the topics discussed, while niche, are familiar to any data team: How to track data lineage; how to run an experiment; how to govern your results.


These talks reflect the implicit ethos behind Snowflake and dbt: Our problems aren’t new, we don’t want to reimagine, reinvent, or revolutionize how we work to solve them, and we don’t want to be hit in the face with new innovations. We just want the same tools we’ve always had—a database and some SQL—with some modern new magic quietly tucked behind them.


# The boring industry


Over time, I expect the rest of the industry to follow Snowflake and dbt away from its history of technological hype and up the “slope of enlightenment.”7For most of us, this looks like embracing what we consider pedestrian, talking about problems and not technologies, and listening to awider array of professional voices.


I think there’s a more explicit lesson, however, for Databricks, and for technologies, like real-time and augmented analytics tools, that currently have more promise than widespread practical application.


For Databricks, be boring. There’s a version of Databricks that’s centered around a polished whitepaper about the Data Science Platform™—it’s a company with a website that’s more “Solutions” pages than “Product” pages, that’s defined by what it enables and not what it does, and depicts itself, abstractly, as a serene oasis in middle of the howling chaos of enterprise data management.8


This approach has sold software to CIOs for decades, and it’ll surely work here. But I’d hazard a guess that it wouldn’t sell as well as a simpler pitch: Databricks is a big, fast database that you can write SQL and Python against. Don’t sell Databricks as a new architecture for an all-in-one AI platform; sell it as centralized warehouse—the kind that turned Oracle into a $220 billion dollar company, andmade Microsoft $5 billion a yearin 2014—that’s hosted, has effectively no storage limit, is really fast, and can be queried directly with Python and R. Don’t sell it as a new category; sell it as a replacement to my vanilla analytical warehouse, but bigger, faster, and polyglot. Don’t sell me use cases and testimonials; sell me this diagram. Once I buy it—and I would buy it—I’ll find everything else Databricks can do, just as we did with Snowflake.9


![](https://substackcdn.com/image/fetch/$s_!RPvB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F529a45d1-09e7-48cd-9ec1-318afd87ecce_1932x1162.png)


The same lesson can be applied to a handful of other industry subsegments that are selling emergent technologies that don’t yet have clearly defined applications.


Take real-time products, for example. Most businesses have little use for true real-time experiences. But, all else being equal, real-time data is better than latent data. We all have dashboards that update a little too slowly, or marketing emails we wish we could send a little sooner. While these annoyances don’t justify the effort currently required to build real-time pipelines, they do cause small headaches.


But if someone came along and offered me a streaming Fivetran, or a reactive version of dbt, I’d take it. If the cost of a real-time architecture was low enough, regardless of the shoehorned use-cases, there’d be no reason to turn it down. And just as we came to rely on Snowflake after we chose it as a better Postgres, I’m certain we’d come to rely on streaming pipelines if they replaced our current batch ones. We’d start doing more real-time marketing outreach, or build customer success workflows around live customer behavior.


Over the next five years, I’d guess that real-time data tools follow this exact path: They’ll finally go mainstream, not because we all discover we need them, but because there will be no reason not to have them. And once we do, we’ll find ways to push it to their limits, just as we did withfast internet connections and powerful browsers.


The same could apply to other tools, like augmented analytics platforms and AI applications likeContinual. In Continual’s case, most of us don’t have an immediate need to enrich our data pipelines with ML models. If the barrier to doing so is low enough, however—if we can easily classify leads’ job titles, or add health scores to our customer models, without sacrificing anything about how our existing pipelines already work—many of us would.


Erik Bernhardssonidentified a similar dynamicin software development. People who had little corporate use for software, like a small dentist’s office, built their first websites not because they suddenly had a huge need to do so; they created them because it became cheap to do it. This initial, “there’s no reason not to”-inspired foray into software uncorked a rush of latent demand: If you have a website, why not let people use it to book appointments? Why not build a system to message patients? Why not run a few ads that direct people to the site? If people don’t need something—but recognize that it’s better if they have it—few things can catalyze a market to grow faster than making it easier for people to buy it.


By following the same path, Big Data is finally starting to live up to its potential. It’s getting there, ironically, by giving up many of its hyped promises for a very boring one: lower costs for marginally more useful things. With Snowflake—and hopefully, with Databricks—we don’t get flying cars or predicting the future; we just get a little less headache. But, it turns out, that’s exactly whatus boring peopleneed.

[1](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-1-51867183)

Noweighth!

[2](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-2-51867183)

Warning: This is wild speculation. Read this blog; buy some NFTs; bet everything on black. These are all the same thing.

[3](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-3-51867183)

Ah, simpler times.

[4](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-4-51867183)

Impala is one of those pieces of technology, like Meerkat, or Secret, that precisely dates anyone who knows anything about it.

[5](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-5-51867183)

And, in the one bad thing they didn’t tell us, it willYELL AT YOU EVERY TIME YOU WRITE A QUERY.

[6](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-6-51867183)

Or, if we’re lucky, when the scandalousApple TV docu-seriesgets made.

[7](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-7-51867183)

There’s no waythis pagewasn’t written by someone at Gartner.

[8](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-8-51867183)

No data, no substance, all vibes.

[9](https://benn.substack.com/p/the-end-of-big-data#footnote-anchor-9-51867183)

Of course, I'm not a CIO at a Fortune 500 company, so my opinions on this issue may not matter at all. Like I said, I’m just out here taking cuts.
