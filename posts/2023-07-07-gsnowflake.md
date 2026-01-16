---
title: "Gsnowflake"
subtitle: "It’s a database; it’s a data cloud; it’s an informationbase!"
date: 2023-07-07T17:32:07+00:00
url: https://benn.substack.com/p/gsnowflake
slug: gsnowflake
word_count: 2207
---


![](https://substackcdn.com/image/fetch/$s_!X7_k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90d92c49-ab32-4440-9e7b-9f6260c55549_1076x798.png)


Is Google a database?


In some very abstract sense, it definitely is. I query it, it flips through an infinite filing cabinet for the thing I asked for, and brings it back to me. It is an organized collection of structured information, stored electronically in a computer; it is controlled by some data management system that determines which links should be returned for a given search; there are applications, like the search bar on google.com, that are associated with both Google’s data and its data management system. This is, according to Oracle, theexact definition of a database.


Still, I’d imagine most of us would say that Google most certainly isn’t a database. When we think of a database, we usually think of the second paragraph from Oracle’s definition: “Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient….Most databases use structured query language (SQL) for writing and querying data.”


In other words, a database isn’t just a collection of information; it’s a tightly organized catalog of capital-D Data. Data is a CSV; it’s something you can open in Excel; it can be charted on a graph or aggregated in a pivot table; it’s an input to computational operations and mathematical formulas and analytically useful summary statistics. And using data is loosely synonymous with doing math.1


Google’s “database” is none of these things. A proper database can be cataloged, and we can look up where things in the database are, and what they mean. I’m not even sure what “cataloging” Google would even mean. Moreover, Google doesn’t return structured tables or numbers that we analyze; it returns links, ads, a location on a map, or some news widget aboutShohei’s latest tank. This isn’t “data;” it’s information.2


And so, when we talk about databases—and when we makewildclaimsabout the future of databases—we tend to think in Oracle’s terms, not Google’s. There are tables, queries, numbers, results, aggregations, catalogs. We think about how databases couldstore more data, how they perform calculations against itmore efficiently, or how they could provide new methods foringestingormanipulatingorsharingthat data. And at the core of all of these conversations is a rough assumption that a database is still a database, to us and to Oracle: It stores capital-D Data, and it returns capital-D Data.


But the other version of a database—the one that’s not full of data but information; the information database; the informationbase—is awfully valuable too. First, it makes us more informed, and probably much more so than a carefully-organized catalog of data. As I’ve argued before, most people aren’t looking for insight; theyjust want to know what’s going on. Google is a much better resource for that than any analyst with an almanac could ever be. And second, databases of information make a lot of money. The printing press in Mountain View that stamped out $282 billion dollars last year is powered by demand for facts and information, not data.3


# Search on


Snowflake—the Data Cloud formerly known as a cloud data warehouse—launched a bunch of new features last week. Because it’s 2023, the year of our new Large Language Lord, most of the announcementsemphasized their AI bona fides: Host LLMs in Snowflake; use LLMs in Streamlit; use ML functions in SQL; use LLMs to write SQL; extract data from PDFs with LLMs; run LLMs on Nvidia chips.


In most of these updates, the focus makes sense; the AI is the feature. But for one—Document AI, which lets you pull information from PDFs and other files—the LLMburies the lede:


> With new innovations like Document AI (private preview), Snowflake is launching a new large language model (LLM) built from Applica’s pioneering generative AI technology to help customers understand documents and put their unstructured data to work…Over the next five years, over 90 percent of the world’s data will be unstructured in the form of documents, images, video, audio, and more according to IDC. This massive volume of unstructured data is routinely stored by organizations, however gaining valuable insight from it has historically required manual, error-prone processes and limited expert skillsets. Building on Snowflake’s support for unstructured data, Snowflake’s built-in Document AI will make it effortless for organizations to understand and extract value from documents using natural language processing.


There are four ways you could read this announcement. One is that Snowflake is using LLMs! They’re technologists who are up on the latest technology! As a Snowflake customer, you won’t be forced to use a51-year old version of COBOL; you will always be on the bleeding edge. Just look at thatcompleteness of vision.


The second interpretation is that Document AI is meant to be aninputto even more LLMs. Hoover up a bunch of unstructured data with Snowflake; build an LLM in Snowflake; create the enterprise chatbot that a thousand YC startups are already feebly chasing.4


The third interpretation is that Document AI is an ETL pipeline for unstructured data. It’s meant for turning your documents into tables that an analyst can query, just as Fivetran does for objects in Salesforce, or asSnowpipedoes for logs in S3. In this version, the LLM doesn’t matter that much—it’s just a fancy transformation method, little different than ingestion pipeline casting a date that’s a string into a date that’s a date.


The fourth interpretation is much…weirder? Document AI may not be an ETL pipeline, but a web crawler.5It’s a means for Snowflake to index unstructured data, and find the connections between these different pieces of content. It’s the beginning of Snowflake no longer being a repository for data, but a repository forinformation.


It’s both a subtle and profound distinction. The difference between data and information is loose and colloquial—the former is tables and numbers and spreadsheets, and requires some expertise and experience to be valuable. The latter, by contrast, is valuable as is. If I want to find all the contracts that a sales manager closed last quarter, or the release date of a new feature that was mentioned in a recent all-hands, or thelyricsto Olivia Rodrigo’s new (and I’m gonna say it, disappointing) singlevampire, I’m looking for contracts, and a date, and some lyrics; there’s no analysis required.


All of the hype around natural language querying and chatbot-based BI tools is implicitly built on this understanding. We usually want information more than we want data, and the appeal of a chatbot to tell us the answer we want, without having to do the complicated work of retrieving and interpreting the data ourselves. If Snowflake has access to more indexed information, much like Google does, we don’t always need the LLM middleman; a lot of questions could be answered by returning some document or snippet directly. And over time,though AI can make those results better, it’s still fundamentally just search—search for documents, search for records ETL’ed from third-party sources, and search for the connections between the two.


Does this make sense? Maybe (though Databricksseem to think it might?6). Is it real? I have no idea—nobody (still) tells me nothing. But there are a handful of reasons it might be worth an attempt.


# The Information Cloud


The first is pretty obvious: The market for a database full of information is almost certainly bigger than the market for data. As much as we talk about the importance of data democratization and self-serve analytics, it’s still a relatively niche need compared to the operational questions—what’s our team’s budget? Who’s in charge of this account? Where are the talking points for this feature?—that people have all the time.


Moreover,in a post from earlier this year, I said that, “if I had to bet on a race between one company that was broadly uninformed but well-researched on a few key decisions, versus one that was well-read about its business but had to make most of its decisions on that awareness,” I’d take the latter. If that’s true—and I stand by it—it suggests that we should be at least as focused on building automated librarians as we are on buildingautomated analysts, and that an easily-searchable catalog of basic facts could be just as valuable as a rich warehouse that’s full of data that’s primed for analysis.


Which highlights the third benefit: A lot of companies don’t have—and will never have—that warehouse.As Jamin Ball saidin his recap of Snowflake Summit, to make use of AI, “we need organized data in the cloud.” Call me a cynic, but a lot of us will never get there. Data is too complex, the systems that generate it are too brittle, and the experts who can corral it are too expensive and too hard to find. Any technology that makes solving those problems a prerequisite to using it is a technology that’ll be out of reach for most people.


The Snowflake Informationbase®™ would have no such requirements. Dump your documents and emails and Slack messages into it, and FrankRank®™ takes care of the rest. It indexes them, builds a graph of their connections,7and makes them searchable, no complex ETL or data modeling required. Though further enhancements could be added—data itself could be searchable, the whole thing be conversational, and so on—it'd be built around discovery and retrieval rather than computation and analysis.


Admittedly, this seems like a bit of a wild idea, and a potentially big step away from Snowflake's core service—which I would guess, despite its various bells and whistles, is still traditional data warehousing. But it's not completely without precedent. If Snowflake has primarily focused on serving the analytical needs of an organization, these basic questions are a company’s transactional operations—they’re not complex calculations, but simple reads and writes.Snowflake(and others) are already trying to unify analytical and transactional databases into a single platform. Why would a complete data cloud not want to unify analytical and transactional questions as well?


# Occam’s bomb


Matt Levine, the prominent financial blogger for Bloomberg, commonly says that his only vested interest in the newsis that it's funny. “Bumbling idiotadmits torunning a ponzi schemeon a podcast” is far better material for an email newsletter than government announcements about thelatest additions to their spreadsheets, even though the latter might be more important.


Those of us who write blog posts about tech companies’ product releases can also find ourselves looking for stories in otherwise mundane and mechanical news. So, sometimes, when a company releases a new feature to extract information from a document and put it into a table, we try to extrapolate it into some grand narrative about building Google for the enterprise, and not tell the more obvious story that they probably built it because their customers kept asking for a way to extract information from a document and put it into a table.


The fifth, more-likely-but-less-interesting interpretation of Document AI is exactly that—it’s a feature that customers want, and Snowflake wants to make things that people will buy.


Still, even that might be revealing of a larger strategy. A number of Snowflake’s new features are offered by other vendors in the market—Document AI is similar toSnorkel AI;Snowpark MLcould be a simple version ofModelbit;dynamic tableslook a lot like Materialize, andtasksand thedynamic table dependency graphlook a lot like dbt; the teasedtext-to-SQL featurecompetes with forty YC startups building the same thing. Though none of these things are all that surprising, they at least reveal that Snowflake isn’t shy about stepping on potential partners’ toes. So the real conclusion from Summit may be that: Though they’re doing itmore slowly than Microsoft, Snowflake is gradually building a bomb of their own.

[1](https://benn.substack.com/p/gsnowflake#footnote-anchor-1-133717126)

Or it’s JSON! Or some other semi-structured format! My point here isn’t that every database is a relational database full of tables; it’s that we tend to think of databases as storing well-organized and cataloged sets of data, and not, like, a bunch of HTML scraped from the internet.

[2](https://benn.substack.com/p/gsnowflake#footnote-anchor-2-133717126)

Even if Google isn’t a database, it’s definitely powered by a lot of databases. So as an aside, here’s a brain teaser for some Google interview panel: How many rows of data get created or updated around the entire world, across Google and every other internet service, when I run a single search? My guess is…122,000.

[3](https://benn.substack.com/p/gsnowflake#footnote-anchor-3-133717126)

To put that printing press in comparison, between 2010 and 2020, during an era ofunprecedented monetary expansion, or whatever the line now is, the money supply in the United States increased by anaverage of $693 billion a year. So, Google’s printing press is about forty percent as big as that of the actual Fed.

[4](https://benn.substack.com/p/gsnowflake#footnote-anchor-4-133717126)

Ok, “only”forty.

[5](https://benn.substack.com/p/gsnowflake#footnote-anchor-5-133717126)

This blog seems to have two recurring themes: Talking abouthowthingssucceedorfail, and makingweirdanalogiesto describe Snowflake. Since I probably shouldn’t talk about howthis acquisition(hypothetically!Hypothetically!That’s the whole schtick! To be aware of whatcouldgo wrong so itdoesn’tgo wrong!) fails until the deal actually closes, seems like it’s option two.

[6](https://benn.substack.com/p/gsnowflake#footnote-anchor-6-133717126)

I went to Snowflake’s conference but not Databricks’ because I’m not atime turner, so I don’t know any details about how this was actually presented. It seems like it’s more of anatural language query enginethan search, but it kinda looks like search?

[7](https://benn.substack.com/p/gsnowflake#footnote-anchor-7-133717126)

Powered by RelationalAI!InsideSnowflake’s Snowpark Container Services! (Snowflake, y’all, friend to friend,this headline, what is happening, it’s so long and angry, I was looking for a press release and I gotAugie Garrido.)
