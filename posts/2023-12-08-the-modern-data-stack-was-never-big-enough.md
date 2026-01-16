---
title: "The modern data stack was never big enough"
subtitle: "Microsoft moves on."
date: 2023-12-08T17:39:19+00:00
url: https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough
slug: the-modern-data-stack-was-never-big-enough
word_count: 2315
---


![](https://substackcdn.com/image/fetch/$s_!Yymj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc51b7a59-6c30-4504-9430-5c0af14b468e_1500x630.png)

*There’s always a bigger fish.*


Six months ago, the modern data stack hit an important milestone: It was big enough for Microsoft to care about it. Until this year, Microsoft had operated in a different cinematic universe than the classic modern data stack vendors1—in enterprises versus startups, in Houston and Chicago versus Silicon Valley, and in companies that choose software based on its features and cost versus those that choose Notion based on its aesthetic and vibe.2This May, however, Microsoft stopped ignoring the modern data stack, and decided to fight it:


> Microsoft today launched Microsoft Fabric, a new end-to-end data and analytics platform. ... “Over the last five to 10 years, there has been a pretty massive level of innovation—which is great and that’s awesome because there’s lots of new technologies out there—but it’s also caused a lot of fragmentation of the modern data stack,” Arun Ulag, Microsoft’s corporate VP for Azure Data, told me. ... “When I talk to customers, one of the messages I hear consistently is that they’re tired of paying this integration tax,” he said.So Microsoft looked at the core data analytics workloads (data integration, engineering, warehousing, data science, real-time analytics and business intelligence) and looked at how it could build a unified experience around this. … [With Fabric, there’s] “literally just one thing to buy, and it allows customers to save a lot of costs, which, especially in today’s environment, is really important,” said Ulag.


For the modern data stack’s ascendent clique, this was alway the risk. Today’s data tools are famously warehouse-centric; what happens if the warehouse providers decide that they want to build their own versions? Databases make a lot more money than the applications that run on top of them; providers of the latter sell at the pleasure of the former. What if Snowflake gives anative reporting toolaway to all its customers? Or Databricksbuilds(orbuys) dbt, and provides it for no extra charge? Or Microsoft bundles acheaper Fivetranon top of their Azure SQL databases? Despite what theinspirational posterssay, when Microsoft stops ignoring you and starts fighting you,theyusually win.3


When it first came out, I thought this was what Fabric was about—the modern data stackconsolidatingaround the warehouse at itscenter.4The cash cows were taking control of their loss leaders.As I said at the time, even if Microsoft didn’t try to directly poach every Astronomer or Hightouch customer, “the modern data stack may not get steamrolled, but stunted, frozen out of the top of the market by a Microsoft sales team that already has a standing tee time with every enterprise CIO."


That, it turns out, may have been delusionalmain-character energy. For better or for worse,Microsoft’s fight’s not with us,5but for something much bigger.


# The Database in Me


If Redshift were to write amemoir, it would be a weird book. When Amazon launched Redshift in 2012, it was the first affordable cloud-based data warehouse, and an instant success. Practically overnight,an entire ecosystem of data companiesformed around it. Segment’s first destination for writing eventswas Redshift; Fivetran’s first users wanted to combine all of their analytics datain Redshift; people ran their businessesout of Redshift.


And then, at the height of its fame, Amazonsold it out. In the late 2010s, AWS’ sales reps startedgetting paid for selling Snowflake too, so long as it was hosted on AWS. Snowflake grew, Redshift faded, and the modern data stack’s first star became a has-been with an interesting backstory andno future.


A couple years ago,Erik Bernhardsson wonderedwhy Redshift’s parents traded it away. His answer, backed up by research and math and the sort of concrete analysis that this blog prefers not to bother with, was that Amazon probably makes more money—and definitely makeseasiermoney—by selling infrastructure to one big vendor like Snowflake than it does by selling databases to thousands of individual buyers like it had to with Redshift. Customers pay Snowflake, Snowflake pays AWS, and “AWS basically ends up with the same bottom line impact, but effectively ‘outsources’ to Snowflake all the cost of building software and selling it. That seems like a good deal for them!”


In the hierarchy of things you want to sell, databases aren’t actually the cash cow, but themiddle fish—bigger than the apps, but smaller than the cloud. Just as BI tools and ETL companies sell at the pleasure of database vendors, database vendors sell at the pleasure of the cloud providers. Databricks can undercut the data catalog market byoffering one for freeto its customers—but Google can undercut Databricks by offering big BigQuery6discounts to customers who use GCP. Frank Slootmancomes for data companies; Satya Nadellacomes for everyone. If database vendors want to build durable defenses against their larger predators, eating the modern data stack doesn’t help all that much. They need to prioritize ahigher order bit.7


# Blue skynet


Easier said than done, though. If companies could just decide to build an$80-billion-a-year cloud infrastructure business, AWS wouldn’t be an $80-billion-a-year cloud infrastructure business. But what if you could build adifferenthigher order bit, in anew marketthat doesn’t yet have any dominant incumbents? As I said nine months ago, theremight be one out there for the taking:


> In ten years, a new type of cloud—a generative one, a commercial Skynet, a public imagination—will undergird nearly every piece of technology we use. … Just as cloud providers built out hundreds of utilities that are all underpinned by core services like EC2, I'd expect OpenAI to do the same thing on top of GPT and other foundational models. …Public AI providers like OpenAI would become another backbone for the internet. Nearly every piece of technology will rely on their models. Nearly every piece of technology will rely on their models. Outlook will need them to summarize our emails. Github will use them to automate code reviews. DoorDash will need them to help guide you through your order. Delta will depend on them for booking flights. Facebookmight not be able to open doors without them. …The final equilibrium is the same as it for the cloud providers: A few companies win the market, and the rest of us come to accept their bills as the cost of doing business.


Assuming this whole AI thing isn’t overblown,8I think this still holds up, with one major adjustment. In that post, I said the public AI providers would sell inference: Developers would send OpenAI a prompt or some sort of media, and OpenAI would send back a response. “Training and running LLMs is very expensive,” I thought, “like building data centers is expensive.”


The part seems partially wrong. It is expensive, but it’s notthatexpensive. Moreover,lotsoflargecompanieswant to train their own models, both to get better results and to maintain control of their data. And the market for that could be huge: Companies are already spendingmore than a billion dollars a yearwith OpenAI—despite it being a new technology that most people are just experimenting with, OpenAI serving generic models, and companies having to deal with the security problems associated with sharing data with a third party.


The real money in AI, then, may not be in foundational model providers who sell inference via API, but in the services that actually look much more like today’s cloud providers—offering metered infrastructure that’s designed to help companies build custom models, fine-tune open source ones, and run both of them.9Moreover,as those open source models get better, the companies best suited to offer this aren’t necessarily those with the most advanced foundational models or the biggest data centers. They’re the companies with access to customers’ data. And nobody has more data than database vendors.


That’s why Databricks paidsuch a premium for MosaicML, at a time when it could’ve acquired a number of modern data stack startupsat a discount. MosaicML’s core competency isn’t providing LLMs; it’sbuildingthem. MosaicML can nowoffer servicesfor “training custom models either from scratch on an organization's data,” or for “continued pretraining of existing models such as MPT and Llama 2;” Databricks can offer a metered service for running those models. It’s the seed of an AI cloud, if an AI cloud is to be built.


In other words, had Databricks acquired an ETL or BI tool, they’d be a database eating a smaller fish. In MosaicML, they bought what they hope becomes a bigger fish that will one day eat the database.


# The great fish moved silently through the night water


When Microsoft Fabric came out a couple weeks ago, I was confused by the announcement. Thelede of the press releasemade a bunch of bold claims—“prepare your data for AI innovation;” Fabric is the “biggest launch of a data product from Microsoft since the launch of SQL Server”—but the product seemed more like technical glue between existing services (thepotato, if you will). The three customers  that were featured in the announcement didn’t talk about AI, but aboutgovernance and security, anddata integration and centralization.10Onewent even furtherin his understated enthusiasm:


> Fabric is giving us an evolutionary way to improve what we have. It’s an evolution; not a revolution. … Those capabilities were always there in Azure, but they’ve been brought together under one roof in Fabric.


Nothing is wrong with any of this, especially for Microsoft, who sells tosystems integratorsas much as they do to end customers. A unified platform designed to help consultants integrate all the Microsoft services they’re hired to deploy and manage is surely part of what Fabric is about. Still, none of this matches the headline.11


It’s possible that the glitter about AI is just branding,chasing the trends that people are searching for. But I think that’s too cynical. I’d guess Fabric is actually about the same thing that Databricks’ acquisition of MosaicML is about—putting in the studs for what might become the next multi-hundred billion dollar market. Not only does Microsoft already have data in Azure, but they also have access tounstructured datain Office, Outlook, and Teams. The real vision behind Fabric isn’t to be the data platform that sits underneath some charts in PowerBI; it’s to the infrastructure that collects and manages the data that can be fed into anAI model factory.


Of course, Microsoft and Databricks aren’t the only players here. OpenAI—now free to make money with wild abandon—will probablyplay along. Snowflake surely has something in the works. AWS launched Q, which is something between apowerful AI assistant that can solve problems and spark innovation, and a chatbot that isalso confusedby AWS documentation. Google is armed withincredible technology, access to Gmail and Google Docs, and achronic habit of underplaying good hands. IBM and Oracle will probablyshow up.


Though the fight hasn’t started yet—we still have to figure out if AI is useful, after all—the big companies arequietly maneuvering into position. Announcements like Fabric and acquisitions like MosaicML give us a peek of what they’re building. And if it doesn’t want to get passed by—or outright eaten—the modern data stack isgonna need a bigger boat.

[1](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-1-139619217)

What is the “classic” modern data stack? A contradiction, probably, but most people know what I mean?

[2](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-2-139619217)

I’m not saying that trendy and well-designed tools aren’t useful. But I am saying that a lot of people buy trendy and well-designed tools because theywant to be seenas people who use trendy and well-designed tools. Silicon Valley isn’t abovestatus symbols.

[3](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-3-139619217)

Ask Slackhow the attention went.

[4](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-4-139619217)

I don’t understand what this diagram means, but “OneLake” is definitely written in the biggest font.

[5](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-5-139619217)

On one hand, this clip is backwards? If the analogy worked, the modern data stack would be band-of-misfits Johnny Ringo, Microsoft would be living-legend Doc Holliday, andRingowould be trying to fightHolliday. And thenHollidaywould say, “The fight’s not with you, Ringo,” and they would both just walk away. On the other hand, it’s a great scene, so why overthink it?

[6](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-6-139619217)

If you write long and peculiar SQL statements in GCP’s cloud data warehouse to analyze the performance of other long SQL statements in that same warehouse, you get to say “big queer BigQuery queries query big queries.”

[7](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-7-139619217)

This is a good post and you should just read it, but to quickly summarize: “The binary representation of a number is made up of a set of ordered bits. The number 13 would be represented as 1101. The increase in value of flipping a higher-order bit outweighs flipping all the lower-order bits combined. 100 is bigger than 011, 1000 is bigger than 0111, and so on.”


Very,veryroughly, the tech market is made up of three ordered bits—one for cloud computing, one for databases, and one for apps. If you’re a database provider—and therefore represented by 010—building a bunch of apps can bump your number up to 011. That’s a little higher than 010, but much smaller than both 110 and 100. Which is all a very nerdy way of saying no matter how many apps a database vendor builds, they’ll always be a much smaller fish than a cloud provider.

[8](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-8-139619217)

It might be? For comparison, Apple launched the App Store in 2008. Three of themost populariOS-native apps of all time areFacebook Messenger,Instagram, andWhatsApp, which came out in 2011, 2010, and 2009, so it took about two years for people to build transformative applications on top of the platform. We’re about one year into the LLM hype wave, Microsoft Copilotmight be the only truly notable productthat’s been built on one so far.

[9](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-9-139619217)

Importantly, helping people train models with millions of parameters isn’t cool;runningthose models billions of times—and charging for compute every time—is cool.

[10](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-10-139619217)

So thecontentof these customer interviews is a bit underwhelming. But theexistenceof them is why Microsoftis an armyyou can never bet against. According to the launch post—i.e., the post that marks the beginning of Fabric being generally available—“25,000 companies are already using Fabric today, including 67 percent of the Fortune 500.” I’m sure that’s inflated by a bunch of Azure customers automatically having Fabric turned on for them, but still, that is a flex.

[11](https://benn.substack.com/p/the-modern-data-stack-was-never-big-enough#footnote-anchor-11-139619217)

Or the amount of thrill in thiscompanion launch post.
