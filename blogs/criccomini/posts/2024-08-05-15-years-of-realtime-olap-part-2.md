---
title: "15 Years of Realtime OLAP (Part 2)"
subtitle: "Realtime OLAP for fraud detection, observability, and more."
date: 2024-08-05T10:20:04+00:00
url: https://materializedview.io/p/15-years-of-realtime-olap-part-2
slug: 15-years-of-realtime-olap-part-2
word_count: 975
---


Myprevious postcovered my first foray into user-facing analytics products atLinkedIn. In this post, I want to talk about the realtimeonline analytical processing(OLAP) use cases I found after leaving LinkedIn in 2015 to joinWePay. Each new use case expanded my understanding of the space.


WePay is (was?) a software as a service (SaaS) payments provider. Applications could integrate WePay into their software to process payments. When I joined the company, several customers were growing rapidly, which strained our monolithic database. We began exploring how to spread the load. The two primary query patterns were transferring money and detecting fraudulent transactions. Both of these had realtime OLAP characteristics, but fraud detection seemed easier to start with.


Our fraud system had two main parts: the model and the data. In an offline environment, the model was periodically retrained against data warehouse data. Afterward, the model was pushed to production. The model serving layer in production queried the data that the model was trained on, except it read from our OLTP database (MySQL) instead of our data warehouse.


Model serving needs a lot of data. Both the account and the specific transaction have metadata: logins, transactions, balance, and so on. Each of these data points is aggregated across different dimensions: time (year, month, day, hour, minute), geography, IP block, and so on. Thus, the queries looked like, “logins in the past hour”, “non-US payment volume in the last week”, “credit cards added to the account in last month”, and so on.


The fraud data (referred to as “fraud signals”) were essentially SELECT COUNT(*)/SUM(*) FROM … GROUP BY. This felt familiar to me from my WVMP days. But the model serving layer had a number of important characteristics that were different from WVMP’s:

1. Users were not pivoting on the data in realtime. We knew each dimension and aggregation we needed beforehand.
2. Query responses needed to be very fast (single digit milliseconds)
3. Data needed to be very fresh (less than a minute, ideally less than 10 seconds)


Unlike the WVMP use case, the query pattern from the model was predictable. It asked for the same aggregations for every transaction. But unlike a human waiting on a dashboard to refresh, the fraud models needed to be very fast. We had a tight bound on the number of milliseconds that a transaction would wait for a fraud response. If the window passed, we had to decide whether to reject the transaction outright or risk allowing fraudulent transactions through. The signal data also needed to be very fresh. Fraudsters act quickly and often use scripts. We needed activity data to be available to the model on the order of seconds so we could detect fraudulent behavior as it was occurring.


We did a lot of digging to try and avoid building our own system. Around this time,Fangjin Yangand his co-founders startedImply. We discussed our requirements with them. They told usDruidmight work, but it would require a lot of machines to get the latency we wanted. Even then, it might not be fast enough. Druid was built for dynamic queries and pivots—more like theWVMP use case in part 1.


Ultimately, we went back to what I’d learned at LinkedIn. Webuilt a batch and stream processing pipelineon top ofApache Kafka,Google Cloud BigQuery, andGoogle Cloud Dataflow. The pipeline aggregated data and pushed the results into aGoogle Cloud Bigtableinstance. This largely mirrored theHadoop/Voldemortpipeline we built at LinkedIn.


My work with our fraud signals team helped me recognize that different realtime OLAP use cases have different requirements. Some need flexibility while others need low latency responses. I started calling the former “human interaction” and the latter “machine interaction”. I associated human interaction OLAP with realtime slice-and-dice dashboards. Response times could take a few hundred milliseconds while the chart updated. Machine interaction, by contrast, had pre-defined queries but required much faster response times.


I started to see realtime OLAP everywhere. We were running theElasticsearch,Kibana, andLogstash(ELK) stack at WePay. The Kibana dashboards looked an awful lot like business analytics chart’n’graph dashboards to me. The data was just machine instances, CPUs, and disks. It seemed odd to power these graphs using a search engine; systems likeInfluxDBandPrometheusmade more sense. At LinkedIn, we usedrrdtoolformetric dashboards. And the logs that were funneled into Elasticsearch looked a lot likefaceted search—more GROUP BY and WHERE clauses.


For each of these use cases, there are a different but overlapping set of requirements. Each needs different query latency, data freshness, data correctness, and query throughput. StarTree’s﹩  blog post,How To Pick A Real-Time OLAP Platform, has a fairly comprehensive breakdown:


![Real-time analytics use case requirement summary](https://substackcdn.com/image/fetch/$s_!f68H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F146a8bfc-b7e1-431a-8d6f-5ac800decbfa_1536x858.png)

*How To Pick A Real-Time OLAP Platform*


This is how I see the realtime OLAP space now. Pinot and Druid started with user-facing analytics use cases. InfluxDB and Prometheus are coming from metrics. Elasticsearch started with log analytics (at least, for its realtime OLAP use cases). Traditional data warehouses have dominated the visualization and dash-boarding categories. Even stream processing systems likeMaterializeandFlink’srecentmaterialized tablessatisfy many the use cases in the image above. Indeed, one of Materialize’s marquee customers,Ramp, is using it forfraud detection.


These systems are converging for many use cases. Data warehouses like BigQuery now haverealtime ingest, Pinotnow supports JOINslike a data warehouse, and so on. Data warehouses, real-time OLAP systems,time series databases(TSDBs), and search engines might all converge.


This is the context I carry with me as I look at ClickHouse. In my next post, I’ll try and understand ClickHouse’s history, which uses cases it’s good for, why it’s so popular, and more. Stay tuned.


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
