---
title: "It's Time to Merge Analytics and Data Engineering (Again)"
subtitle: "Data pipelines are commoditized and analytics engineers don't provide enough value."
date: 2024-11-18T19:37:20+00:00
url: https://materializedview.io/p/merge-analytics-and-data-engineers
slug: merge-analytics-and-data-engineers
word_count: 720
---


Josh Gray, CEO ofArtemis﹩, interviewed me about data stack fragmentation,dbt, cost savings, and more. Josh’s questions really got me thinking, and is the subject of today’s post. Here’s the interview:

[Artemis BlogFragmentation in the Data Stack and cost structure with Chris RiccominiRead morea year ago · 3 likes · Josh Gray](https://artemisdata.substack.com/p/fragmentation-in-the-data-stack-and?utm_source=substack&utm_campaign=post_embed&utm_medium=web)

I also did a podcast interview onThe Joe Reis Show. Joe and I had a leisurely talk about all things data infrastructure. Best enjoyed in a hammock with a beverage of choice.


---


Iposted a Bluesky thread this weekendarguing that analytics engineers and data engineers should be folded back into a single role. I decided to make the argument after coming acrossBenn Stancil’s post,Disband the analytics team. The post wrestles with the struggles that analytics teams face and offers the choice: disband or rebrand.


> In short, my answer is that analytics—not as an industry or as a technology ecosystem, butas a discipline—might not work. The average company may never be able to make better decisions by hiring a team of average analysts. We canmake dashboardsand beoperational accountants. But the fun, exploratory, “valuable” work may always be an indulgent, empty dessert, and never the entrée we want it to be. —Benn Stancil,Disband the analytics team


I’velong heldthat creating the “analytics engineer” role was a mistake.dbtLabs says, “Analytics engineers provide clean data sets to end users, modeling data in a way that empowers end users to answer their own questions.” I don’t believe that this set of activities is enough value to justify a full headcount; it’s is too limited in scope and too far removed from revenue generation.


![](https://substackcdn.com/image/fetch/$s_!aC0w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d063aa6-0fa9-4181-8c7b-d50e0b3894b0_1462x758.png)

*View Post*


Extracting, transforming, and loading (ETL’ing) data used to be handled by one team: the data warehouse team. But several trends have encouraged a schism in warehouse teams. Some—data engineers—now work on data pipelines (extract and load) while others work on data marts (“clean data sets”, as dbtLabs calls them). In short, data engineers do the E and L, and analytics engineers do the T. Many trends contributed to this bifurcation.

- We switched from ETL to ELT when we adopted data lake architectures. Dumping garbage into an object store made it easy for data engineers to ignore transformations and gave analytics engineers something to do.
- Similarly, adopting data integration with Kafka and Kafka Connect greatly expanded the number (and importance) of data pipelines in an organization, which gave the data engineers something to do as well.
- Shift-leftbecame a data philosophy that encouraged everyone to be their own analyst, which left analysts squeezed.
- ZIRPended, which made CFOs take a hard look at the cost of analyst and data teams, which further squeezed analysts.
- dbtLabs,Motherduck, and otherMDS vendorswere all too willing to create a new role to sell their products, which dovetailed nicely with analyst’s desire tobe engineers and get paid more.
- LLMs are replacing analysts in some cases. Screech all you want, but it’s happening. There are dozens of data chatbots now (Cimba.ai﹩,DataChat,Julius.ai), and LLMs write pretty good SQL.


We’re in a new world now, though. ZIRP is gone, most of the connectors that data engineers were working on have now been built, and there aremanyvendorsyoucan pay to run your data pipeline, and chatbots can answer data questions. It’s time to merge data engineers and analytics engineers back into a single data team that’s responsible for E, T, and L.


![](https://substackcdn.com/image/fetch/$s_!4ul5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F009de8c6-2534-47eb-9f80-f31f9e7ff20a_1466x806.png)

*View Post*


I’m happy to see companies and projects showing up to ease this transition. The most notable one isdltHub, which adoptsSDLCbest practices for data pipelines much as dbt did for transformations. Tools such as this should make it easier for analytics engineers to take ownership of data pipelines. I’ve also seen several tools liketabsdata﹩ that merge ETL back into a single tool for analytics and data engineers, rather than having both dltHub and dbt. I expect to see a collapse of data engineering and analytics engineering back to a single team in the next few years.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
