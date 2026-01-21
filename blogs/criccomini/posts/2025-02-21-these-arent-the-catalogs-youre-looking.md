---
title: "These Aren’t the Catalogs You’re Looking For"
subtitle: "Metadata is useful for data warehouses, streaming systems, humans, and machines. We don't need different catalogs for each use case, though. Catalog convergence is here."
date: 2025-02-21T00:44:24+00:00
url: https://materializedview.io/p/these-arent-the-catalogs-youre-looking
slug: these-arent-the-catalogs-youre-looking
word_count: 668
---


House keeping! First up, Materialized View hit a new landmark while I wasn’t looking. 5000 subscribers! Thanks again for all of your support.


Earlier this month, I joinedThe Infra Podto chat about all things infrastructure. Give it a listen:


Finally, I re-did my personal blog,cnr.sh, as well. I am planning to do some non-infrastructure writing this year. If you’d like to keep up to date, please do follow mynewsletterorRSS feedthere. I just published my first post,Comparing Apache, CNCF, and Commonhaus.


The blog launch led to a couple of fun Python libraries:markupdownandpython-docstring-markdown. Markupdown is the static site generator I’ve always wanted. It acts more like a build system rather than a classical SSG. python-docstring-markdown was just scratching an itch I had: I wanted to generate a simple DOCUMENTATION.md file from Python docstrings in my Python libraries.


---


Recapis a project I started working on a few years ago. It started as atiny data catalog for machinesand morphed into a type system. It provides a single schema definition language (SDL) that can describe database schemas, event schemas such asAvro, and web service schemas such asJSON schemaandProtobuf. The project has now been adopted byGable.ai; they use it as the SDL for their data contracts.


One of Recap’s features was itsclient framework. I implemented readers forBigQuery,Confluent’sschema registry, and a slew of databases and filesystems. I began to realize that these systems were all data catalogs. Some called themselves registries, others wereinformation_schema, and many called themselves catalogs. But they were all handling metadata about your data; they seemed 80% the same. Yet they were being used for different things.


Registries are typically used to store event schemas for streaming systems in Avro, Protocol Buffers, and JSON Schema. Service catalogs such asBackstageandApicuriouserve a similar purpose for web services.information_schema-style metadata is used in bothOLTPandOLAPdatabases. “Traditional” data catalogs such asCollibra,Atlan,Alation,Open Metadata, andDatahubbegan with data discovery use cases.


Each use case has a distinct yet overlapping set of requirements. Registries must be low latency and highly available since realtime infrastructure often queries them in production. They must also track schema compatibility to prevent breaking changes. Similarly, OLTP metadata needs to be very fast since it’s being used by query engines serving production traffic. OLAP metadata, on the other hand, need not be as low latency. Instead, tracking things like lineage, schema evolution, access controls, and sensitive information are important. Service catalogs are concerned with discovery, but also schema compatibility.


I’m not convinced that each of these use cases deserves its own distinct catalog. Each use case has separate requirements, but it seems to me that one system could service them all.


Indeed, I’m beginning to notice a lot of convergence in this space. Backstage, which started as a microservice catalog, now covers data pipelines, machine learning models, and more. Datahub, which began as a data discovery tool,is going to adopt Iceberg’s REST API. Confluent’sTableflownow speaks Iceberg’s REST API and converts schemas for their registry.LakeKeeper, an Iceberg REST-compatible data catalog, has adopteddata contractfeatures similar to those you find in Confluent’s schema registry or Gable’s data contract product. Datahub has also tried toadopt data contracts.


Catalog convergence makes sense. We spent the last 10-15 years doing data integration. Data pipelines aresupply chains now. All of our data (and metadata) flows through OLTP, streaming systems, batch, and data warehouse systems. It no longer makes sense to have a separate catalog for each use case.


The optimist in me hopes the convergence continues; “data catalog” should mean only one thing. If Iceberg’s REST API evolves fast enough, it might become the lingua franca that we need. The realist in me knows that this is unlikely. Instead, we’ll probably end up with catalog gateways or proxies.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profileandMaterialized View Capitalfor a complete list.
