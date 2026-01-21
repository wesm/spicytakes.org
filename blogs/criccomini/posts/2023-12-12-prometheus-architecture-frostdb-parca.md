---
title: "The Surprising Simplicity of Prometheus's Architecture, Discover FrostDB's LSM Tree for Observability, and more..."
subtitle: "Why you can't offer Prometheus as a service; I try to find an embeddable metrics database; and I stumble over Parca, an open-source CPU profiler in an eBPF filter."
date: 2023-12-12T11:31:24+00:00
url: https://materializedview.io/p/prometheus-architecture-frostdb-parca
slug: prometheus-architecture-frostdb-parca
word_count: 470
---


## Why Is There No Cloud Hosted Prometheus?


Apurva, CEO ofResponsive[$], recently asked abouttimeseries databases (TSDBs)for Responsive’s observability product.


![](https://substackcdn.com/image/fetch/$s_!C9Nr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c5505cc-4132-469d-a2b1-bd688a2788a7_696x181.png)


The responsesincluded the usual suspects:Clickhouse,TimescaleDB,InfluxDB, andPrometheus.


I wassurprised to findthat there isn’t anyPrometheuscloud hosting. There are only managed offerings fromGCPandAWS, or Prometheus protocol-compatible offerings fromVictoriaMetrics,Grafana Mimir, and so on.


After some digging, I realized I’d been misunderstanding Prometheus’s architecture. Prometheus isintentionally designedwithonly single-node storage:


> Prometheus's local storage is limited to a single node's scalability and durability. Instead of trying to solve clustered storage in Prometheus itself, Prometheus offers a set of interfaces that allow integrating with remote storage systems.


I love this! Getting started is easy because you don’t have to set up a distributed system. Users can defer the scaling decision until later. When it’s time to scale, users get to decide whether to scale up or out. Users that decide to scale out have dozens of remote stores to choose from:


![](https://substackcdn.com/image/fetch/$s_!Akfu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a5cd568-4146-4641-b83b-cb9d7a4ad1e5_693x759.png)


That final note at the bottom—prom-migrator—means even migration is easy. This architecture is all about user choice. Kudos to the Prometheus designers.


## Project Highlight: FrostDB


Prometheus’son-disk layoutdocumentation got me thinking about embedded TSDBs. The last embedded TSDB I used wasRRDtool(c.f.Ganglia, LinkedIn’sInGraphs). RRD has been around for a long time; the repo’sfavicon.icois 18 years old. Surely things have evolved in the last 20 years.


![](https://substackcdn.com/image/fetch/$s_!7wx0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07682928-609f-43a8-911a-6e16c6e104bc_1384x258.png)


It looks like many people are repurposing embeddedOLAPDBs likeDuckDBorClickhouse’s engine. OLAP DBs should work, but I was really looking for something purpose-built for common metric characteristics:

- High writes,  low reads
- Wide and unpredictable data (unstructured, many dimensions/labels, and so on)
- Immutable data


I came across a  project calledfrostdbfromPolarSignals.


![](https://substackcdn.com/image/fetch/$s_!Gcad!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfa7141c-8818-42c8-86e0-c2187f92e0fe_1394x396.png)


From the README:


> FrostDB is similar to many other in-memory columnar databases such asDuckDBorInfluxDB IOx.FrostDB may be a better fit for you if:Are developing a Go programWant to embed a columnar database in your program instead of running a separate database serverHave immutable datasets that don't require updating or deletingYour data contains dynamic columns, where the number of columns in the schema may increase at runtime


The README also has a lovely write-up on frostdb’son-disk structure. It’s built exactly as I’d hoped—alog-structured merge-tree (LSM). The first level storesApache Arrow records. Data is then rewritten into Parquet for subsequent levels.


If you’re looking for a local TSDB that’s built for metrics,frostdbis worth a look!


Bonus: frostdb was built forParca, another cool project. Parca does, “Continuous profiling for analysis of CPU, memory usage over time, and down to the line number.” It’s built as a singleeBPFfilter.


## More Awesome Infrastructure


Keep up with new infrastructure projects as they’re added toawesome-infra. New submissions are welcome!

- No updates for this post.Send me PRs!


---


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
