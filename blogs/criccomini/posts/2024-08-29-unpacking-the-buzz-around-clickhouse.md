---
title: "Unpacking the Buzz around ClickHouse"
subtitle: "A look at the excitement around ClickHouse. I break down what makes it great and the challenges ahead."
date: 2024-08-29T19:58:20+00:00
url: https://materializedview.io/p/unpacking-the-buzz-around-clickhouse
slug: unpacking-the-buzz-around-clickhouse
word_count: 1195
---


I have some exciting news! I’m helpingMartin Kleppmannwith the second edition of his popular book,Designing Data-Intensive Applications. Martin and I first met at LinkedIn, where we worked together onApache Samza. I’m very excited to contribute in a small way to such an important and popular book. An early release of the first three chapters are now available toO’Reilly Learningsubscribers, with more to come. SeeMartin’s postfor more details.


I also had a very pleasant conversation in the inaugural episode ofTech on the Rocks. We discussed stream processing,Rust,SlateDB, and more. Give it a listen here:


---


My two previous posts, 15 Years of Realtime OLAP (part 1,part 2), documented my experience with home-grown realtime OLAP systems,Apache Druid, and Apache Pinot. I also discussed the use cases I had for these systems: user facing product analytics and fraud detection. My intent was to lay the foundation for this post, where I investigate the buzz aroundClickHouse.


ClickHouse has been appearing a lot in some of my recent interactions.Tinybird, a user-facing analytics product, uses ClickHouse as its database. Several startups I’ve talked to are working on ClickHouse-related products. My Twitter feed has a lot of ClickHouse mentions, too.


What’s more, much of the feedback about ClickHouse appears to be quite positive, too. This caught my eye—we engineers tend to be a critical bunch. Moreover, when I looked at ClickHouse, I saw another realtime OLAP system like Druid or Pinot. Why all the attention?


![](https://substackcdn.com/image/fetch/$s_!E6p2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2059d00-09b7-4da4-9ff1-a52810f3fa01_692x190.png)

*View Post*


The responses to this post were interesting. The feedback seems to boil down to three things: speed, ease of install, and ease of operations.


![](https://substackcdn.com/image/fetch/$s_!I_bz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F58080b42-1995-40cd-a8ee-fe440381000f_689x96.png)

*Ovais Tariq, founder of TigrisData,View Post*


## Speed


ClickHouse is indeed very fast. A friend told me, “They have the mentality of a team on a budget. Like they didn’t have 1000s of machines to throw at the problem. They had to make it work on what they had.” This might or might not be true—ClickHousecomes from Yandex—but the software definitely has this vibe.


As proof, ClickHouse runs abenchmark project. Database vendors may submit their databases to see how they fair. ClickHouse has been dominating its competition (at least until 6 months ago whenUmbrashowed up). One can quibble over the workloads tested, but ClickHouse is clearly a very fast database.


## Installation


Though speed is nice, it’snot as importantas it used to be. Where ClickHouse really shines is its installation experience. Realtime OLAP systems are notoriously annoying to get running. Apache Druid and Apache Pinot both use bash scripts that spawn multiple local JVM-based services to get the system up and running. Either that or you’ve got to run Docker and use Helm charts, as isthe case with StarRocks.


ClickHouse, by contrast, is a single cURL command toclickhouse.com. The server is smart enough that it recognizes the lack of user-agent in the HTTP request and automatically gives you a bash script to install a native binary for your host. It just works.


![](https://substackcdn.com/image/fetch/$s_!f7Xc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26bd2512-c92f-4420-b280-729504045814_719x301.png)

*ClickHouse Quick Install*


They’ve occupied a really nice spot between embedded OLAP systems likeDuckDBand distributed realtime OLAP systems like Apache Pinot and Apache Druid. It’s surprising to me that there aren’t more single-process realtime OLAP systems out there; it seems obvious in hindsight. ClickHouse seems unique in this regard, aside from recentPostgreSQLOLAP developments (more on this later).


Another way of phrasing all this is that the developer experience (DX) is really nice. And a great developer experience leads to a lot of rave reviews on Twitter. I suspect this is where a lot of the buzz is coming from.


## Operations


A great DX is nice and all, but does it scale and is it easy to operate? Here too, the feedback is positive, but more mixed. ClickHouse’s speed and efficiency mean it can scale up quite nicely—you can continue to run it on one big machine for quite a while.


![](https://substackcdn.com/image/fetch/$s_!cIKQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69358cd5-847f-4622-8aa0-9acdfbca2268_689x135.png)

*Alasdair Brown, Product Marketer at Tinybird (View Post)*


Once you’re ready to move beyond one machine, you’ll need to introduce another ClickHouse service:ClickHouse Keeper. Here, too, the developer experience is excellent. ClickHouse used to rely on ZooKeeper to coordinate its nodes in a distributed environment. Running ZooKeeper is tough, so ClickHouse wrote their own drop-in replacement, which they bundlebundle into their binary.


![](https://substackcdn.com/image/fetch/$s_!4l1t!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F276edddc-0402-4385-b892-a356493946f7_683x164.png)


The operational flexibility to scale up or out without adding a bunch of services is really valuable. And it’s run on some very large workloads. Tinybird has some customersdoing 300K-600K events per second.Uberadopted ClickHouse for theirlog analytics platform(more on this later, too). And I assume Yandex’s usage is still fairly large.


Of course, there will always be operational challenges.Javi Santana, Tinybird’s co-founder, says it’s,“super hard to run at scale.”I also noticed some discussion aboutdisk usage and imbalances. And its XML configuration files are clunky.


## Challenges


As nice as ClickHouse appears to be, I see a few challenges. The first and most significant is cost. Remember Uber’s ClickHouse log system I mentioned above? They’re moving off ClickHouse.Yupeng Fupresented an excellent talk atStarTree’s﹩RTA Summit 2024calledEvolution of OLAP at Uber. The talk discusses how Uber is replacing several pieces of infrastructure, including ClickHouse, with Apache Pinot.


![](https://substackcdn.com/image/fetch/$s_!-Fsj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49b503da-09ca-4407-b578-e48b7c3205fe_2334x1323.png)


Yupeng says that Uber’slog analytics platformmigration in 2020 resulted in 50% cost savings when compared to their previous ELK-based log analytics system. But ELK is very expensive to run on large datasets. A 50% gain isn’t really that much. Since the migration, the team has hit cost and performance challenges. Stories like these are somewhat alarming for large-scale enterprises.


Another more subtle (and perhaps more minor) challenge with ClickHouse is its behavior with materialized views. Materialized views are important for many realtime analytics use cases. By updating aggregates when a write occurs, reads become very fast. Entire systems likeMaterializeandFelderaare built around this concept. ClickHouse supports materialized views, but updates are only triggered when the “main” table—the first table in a join—is written to. For many queries, especially those without joins, this is perfectly acceptable. But for more sophisticated use cases, it simply isn’t good enough.


![](https://substackcdn.com/image/fetch/$s_!CZqk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e165275-2403-4f95-8092-205f0dafe027_698x272.png)

*Frank McSherry, Co-founder and Chief Scientist at Materialized (View Post)*


And finally, the elephant in the room: PostgreSQL is becoming an OLAP system.Hydrarecently publishedpg_duckdbwith backing fromMotherDuck,Microsoft,Neon, and others. Hydra’s extension integrates DuckDB (an evenmorebuzzy project than ClickHouse) with PostgresSQL. AndParadeDBhas seen a lot of adoption with itspg_lakehouse,pg_analytics, andpg_searchPostgreSQL extensions.


As PostgreSQL’s OLAP extensions mature, it will be a great solution for the exact space that ClickHouse shines: single-node scale-up realtime OLAP with a great DX. If PostgreSQL takes ClickHouse’s single-node and small-scale usage, and systems like Pinot and Druid take its large-scale market, there’s not much left. This is the biggest long-term threat that I see for ClickHouse.


Still, as things stand now, ClickHouse is a robust system, and a reasonable solution for many use cases. I look forward to seeing how things shake out; I have a real soft spot for realtime analytics.


---


Share


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
