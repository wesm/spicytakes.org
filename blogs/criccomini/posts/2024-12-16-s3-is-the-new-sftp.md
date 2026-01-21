---
title: "S3 Is the New SFTP"
subtitle: "Customers want their data. A customer data lake is a great way to give it to them."
date: 2024-12-16T12:03:01+00:00
url: https://materializedview.io/p/s3-is-the-new-sftp
slug: s3-is-the-new-sftp
word_count: 1397
---


I’ve come to realize that payment providers have a comparatively diverse set of  data processing patterns. Fintech startups have transactional workflows that lend themselves todurable execution; they have low-latency processing requirements that benefit from stream processing;theyhaveesoteric double-entry book-keeping systems with strongACIDguarantees; and they have fraud detection use cases that require machine learning (ML) and specialized graph, search, and data warehouse systems.


One of the less glamorous data processing tasks payment providers do is shuffle files between their vendors and partners. Such shuffling usually involvesSecure File Transfer Protocol(SFTP). Simply put, SFTP allows you to securely upload or download a file from a server. Much of the US banking system still runs on SFTP servers. Banks and credit card processors exchange files over SFTP to signal when fund transfers complete, when accounts close, and so on. These files are often written in CSV, XML, orfixed-lengthfile formats.How ACH works: A developer perspectiveis a good read for those that are interested.


When I joined WePay, the company was running as a PHP monolith. One of the first microservices that I built was responsible for reliably syncing files to and from our bank and credit card processors SFTP servers. The service proved very useful, and was in heavy use when I left the company seven years later.


Separately, another of my teams was responsible for WePay’s data pipeline. We used Airflow to extract data from our production databases and load it into our data warehouse. We also used Kafka and Kafka Connect to stream changes from production databases into Kafka and other downstream systems.


One day, our business analytics team approached me to ask for aBigQuerydataset that could be shared with one of our larger customers. The sales team was trying to close a deal, and the customer wanted data access included in the contract. The team’s plan was to writeAirflowjobs that would output customer-specific data to the tables to a BigQuery dataset and grant the customers access to query it.


I hit the roof: our data pipeline (and team) wasn’t built for this. The pipeline was stable enough to be used for internal reporting, debugging, and modeling use cases, but it was not reliable enough to expose to end customers. Our pipelines would break when upstream developers changed their schema, when Kafka Connect decided to rebalance, or when our single Airflow machine failed. We did not have enough SREs and on-call engineers to provide a pipeline suitable for end-users to depend on.


SFTP never came up when talking with the business analytics team about their use case, yet the pattern is similar. We were trying to share data with an external integration partner (our customer, in this case).


The customer data sharing use case stuck with me. It was not an unreasonable request. I started to notice this pattern everywhere. We received many such data requests. The fascinating thing was that different customers requested their data in different forms. Some wanted periodic batch data dumps (like the SFTP integrations our payments team worked on). Others wanted a realtime HTTP/JSON API. Still others simply wanted a button on the website that would generate and email a PDF or CSV file. Data usage varied, too: financial reconciliation, reporting, user-facing dashboards, data products, monitoring, and so on.


Despite all this demand, “reporting”, as we called it, was rarely invested in. It was a rather murky area—the reporting data was owned by the payments product managers, yet the reporting team was part of our frontend group. And of course, my team actually managed the data pipeline. There was no real owner. WePay’s reporting and data export features languished.


I spent several weeks investigating vendor solutions for this mess. I wanted awhite-labeldata platform that we could send our data to. The ideal product would then expose this data as a WebSocket API, HTTP/JSON API, data warehouse, CSV, SFTP, dashboard, or whatever other whacky format our customers wanted. To my dismay, I found nothing that met our needs.


I’ve never given up on this vision, and I continue to see use cases for such a platform everywhere.Stripe Sigma,Stripe Data Pipeline,Nango,Snowflake Data Cleanrooms, everyreverse ETLplatform,Quill﹩; these are all parts of a whole. Customers want data from their SaaS vendors. Yet, for the past decade (longer, really), SaaS vendors have been left to roll their own solutions. That is, until now.


![](https://substackcdn.com/image/fetch/$s_!ZnTe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea04e92b-69f5-407f-834c-d84393b7644a_1180x198.png)

*View Post*


Several startups, includingPrequel,Bobsled, andGeneral Foldersnow seem to be taking this use case seriously. The one I’m most excited about isPrequel. They call themselves a, “data export platform.” The product marketing on their website looks rather reverse ETL-ish, except that the destination’s connections are meant to be an external organization rather than internal tools such as Salesforce or Zendesk (as is usually the case with reverse ETL). But when I spoke to Prequel, they were quite focused on one particular pattern: exporting data to S3 in Parquet files.


The idea is actually fairly straightforward: modern data processing is centralizing around data lakehouses usingS3,Apache Iceberg,Apache Parquet, and data lake query engines such asDuckDBandTrino. SaaS vendors can upload Parquet files to a shared S3 bucket managed by an Iceberg catalog. Customers can then query the files simply by adding an external table to their existing data warehouse or by querying the data directly using a data lake query engine.


Offering customers data in a data lake format maintains some of the benefits that SFTP has historically provided: data transfers are very fast, access can be managed centrally in the catalog, and files can be atomically exposed to customers (no partial uploads). This architecture comes with some additional benefits, too. Centralizing around a strongly typed, columnar format like Parquet and table format like Iceberg makes managing data models much easier. And query engines already support this format, so users can query their data directly without having to ETL it.


Schema evolution challenges still remain. Application engineers might decide to drop a field that customers are using. This problem has existedfor a long time, but it becomes a critical outage when it impacts customers. Fortunately,data contractsare getting attention.Gable.ai﹩and its founder,Chad Sanderson, have been doing a lot of evangelism in this area, which helps. But much like the reverse ETL companies, data contract companies seem to be focused on internal use cases. So when I recently spoke toVakamo, the creators ofLakekeeper, I was very heartened to hear that they’re thinking about data contracts for data catalogs. They directly called out customer data integration as a use case for this feature.


I’m cognizant that a customer data lake doesn’t address all the use cases I enumerated above. Data is loaded in batch, rather than streamed on web sockets or polled through HTTP APIs. You can have any data format you want, so long as it’s Parquet. SaaS vendors are still left to roll their own visualization features if they’re needed. But maybe this is OK. I suspect a data lakehouse with periodic batch loads might be enough.


Customer data lakes might actually end up being a driving force for lakehouse adoption. Many companies are still in the, “What is this, why do I need it, and how do I use it,” phase of lakehouse adoption. These same companies are very motivated to get access to their SaaS data.


![](https://substackcdn.com/image/fetch/$s_!Kwvr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0757b029-5aaa-4cc8-b58c-29780c48defc_1168x378.png)

*View Poster*


Giving a customer’s analysts DuckDB and pointing them at an S3 bucket is pretty compelling. It could drive a land-and-expand transition for lakehouse architectures as companies initially adopt lakehouse query engines to get access to their SaaS data, then realize the benefits for their own data over time.


These lakehouses could also give analytics engineers something to do—something that drives revenue. Irecently lamentedthat the role didn’t drive enough revenue to justify its existence. But someone’s going to need to curate these customer data lakehouse data models and make sure the files are loaded on time. Seems like a good fit.


It’s still early days for all of this, but I see a lot of tailwinds. Customers want their data, lakehouses seem like a good fit, and we have analytics engineers that are eager to help.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
