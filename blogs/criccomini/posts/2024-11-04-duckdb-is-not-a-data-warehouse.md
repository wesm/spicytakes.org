---
title: "DuckDB Is Not a Data Warehouse"
subtitle: "DuckDB is a tool, not a product."
date: 2024-11-04T12:37:59+00:00
url: https://materializedview.io/p/duckdb-is-not-a-data-warehouse
slug: duckdb-is-not-a-data-warehouse
word_count: 887
---


Before I get to DuckDB, I’ve got three house-cleaning items this week: Bluesky, Materialized View’s one year anniversary, and P99 CONF.


Let’s begin with social media. I’ve moved toBluesky🦋. Follow me@chris.blueif you’ve enjoyed my Twitter posts over the past 15 years. You can crosspost withFedicaorBufferif you like. There are some greatstarter packsto bootstrap your feed, too. Here are a few:

- Infrastructure Engineers(mine)
- Distributed Systems on 🦋
- AI, ML, Data Science, and Security
- ML, Data, & Tech
- Data People Starter Pack
- AI and Data


I don’t know what this means for my Twitter account. All I can say is that I’ve been using Bluesky exclusively for the past week and it’s absolutely buzzing. It feels like the good old days. I haven’t missed Twitter at all.


![](https://substackcdn.com/image/fetch/$s_!HBtw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8043ec6e-08f7-43fb-a1c1-e39ff7f48baa_1182x316.png)

*View Post*


Next, Materialized Viewturned oneon October 31 🎃. It’s been an incredible year for the newsletter. I’ve published50 postsand the newsletter just passed 4,000 subscribers. I’ve also received a lot of positive feedback. Almost everyone I meet mentions Materialized View. Thanks again for all the support and encouragement.


![](https://substackcdn.com/image/fetch/$s_!LnrR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f91c712-e954-4afd-b906-25a0e9a708fb_2312x896.png)


Finally,Rohan Desaiand I presented atP99 CONFand the video is now online. Along with myThe Geek Narratorinterview, our talk is a great starting point to learn aboutSlateDB’sinternals.


---


A consequence of drinking from thedataBSfirehose is that you will get a lot ofDuckDBchatter. For the unfamiliar, DuckDB is essentiallySQLitefor columnar data. It has a number of interesting properties. It’s very portable: it runs locally on your laptop, inside an application, or even in a browser. It’s alsovery fast(though, I’m toldthat’s not enough). Most importantly, it can connect to remote storage to readApache Parquet filesandApache Iceberg tables.


These properties have made DuckDB a favorite among analytics and data engineers. All kinds of creative DuckDB uses have popped up.Oktauses DuckDB to cheaply transform databefore it entersSnowflake. MotherDuck alsoshowcases ETL examples.RillandModehave both adopted DuckDB as their in-memory query engines. PostgreSQL has been overrun with DuckDb extensions such aspg_duckdb,pg_mooncake, andpg_analytics. You can even use DuckDB to queryNew York City taxi datastraight from your laptop (orfrom Modal﹩).


Given that DuckDB is anonline analytical processing (OLAP)database, you might expect to see stories of DuckDB replacingSnowflake,Redshift,BigQuery, orDatabricksas a data warehouse. There aresome, but not many. I’ve always been skeptical of the idea that DuckDB is a viable solution for an enterprise data warehouse.Ananth Packkildurai(ofData Engineering Weeklyfame) posted an observation that resonated with me:


![](https://substackcdn.com/image/fetch/$s_!kO13!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadefdbbd-d2c7-4041-b793-1d04fc4c3bca_1172x700.png)

*View Post*


DuckDB’s deployment model and limited scalability are what I struggle with. If you’re in an enterprise, your data warehouse users are going to include product managers, customer support, risk analysts, business analysts, finance teams, operations teams—virtual everyone at the company. I don’t see how DuckDB can be deployed in such an organization. It’s untenable to install DuckDB on everyone’s laptop, grant everyone access to data lake buckets, and ask them to run queries from the CLI.


Even if a company wanted to use DuckDB as their data warehouse, they couldn’t. DuckDB can’t handle the largest queries an enterprise might wish to run. MotherDuckhas rightly pointed outthatmost queries are small. What they don’t say is that the most valuable queries in an organizationarelarge: financial reconciliation, recommendation systems, advertising, and others. These are the revenue drivers. They might comprise a minority of all the queries an organization runs, but they make the money. DuckDB just can’t handle such queries.


![](https://substackcdn.com/image/fetch/$s_!gWEu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb75cd778-4993-468f-9492-822cc7c4cc87_1384x1064.png)

*View Post*


To be a viable data warehouse, DuckDB needs a centralized deployment model, a better UI, and a way to scale. This is exactly what MotherDuck is building, and it sounds a lot like Snowflake or BigQuery. As much as MotherDuck would like to be the DuckDB vendor, they’re a cloud data warehouse that just happens to use DuckDB.


This begs the question: why should I switch from my current data warehouse to MotherDuck? It seems like the answer right now is cost. Cloud data warehouses are expensive. MotherDuck saves money by running DuckDB on small data sets. But it’s also really expensive to change data warehouses. It’s often easier to cut costs in your existing data warehouse by auditing queries and data retention.


Smaller companies can adopt DuckDB or MotherDuck and scale cheaply as they grow. This is a reasonable story for SMBs, but not for enterprises that already have a warehouse. But SMBs can also adopt the PostgreSQL extensions that I mentioned earlier. If I were tasked with rolling out DuckDB in an organization, that’s probably how I’d do it.


So, on the one hand, MotherDuck has picked a fight with some of the nastiest apex predators out there: Snowflake, BigQuery, and Databricks. On the other, they’re getting squeezed by PostgreSQL extensions and DuckDB on the laptop. This is a tough environment. MotherDuck has raiseda lot of money, so perhaps they can find enough SMB customers and wait for them to scale.


As for DuckDB itself, I thinkPedramand Erik have it right in the Tweet above. It’s amazing middleware, much like SQLite. I don’t see it as a data warehouse, though.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
