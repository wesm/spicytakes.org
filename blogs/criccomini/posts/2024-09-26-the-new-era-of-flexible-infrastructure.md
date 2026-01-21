---
title: "The New Era of Flexible Infrastructure Deployment"
subtitle: "Flexible deployment is now table stakes. Infrastructure must run embedded, client-side, single-node, clustered, as SaaS, BYOC, and self-hosted."
date: 2024-09-26T18:19:49+00:00
url: https://materializedview.io/p/the-new-era-of-flexible-infrastructure
slug: the-new-era-of-flexible-infrastructure
word_count: 537
---


Confluent’srecentWarpStream﹩acquisitioncame as a surprise to me. Why buy WarpStream four months after announcingFreight Clusters, a direct competitor to WarpStream? Confluent says WarpStream will enable bring your own cloud (BYOC) deployment for its customers.


I was a bit skeptical of Confluent’s messaging at first—acquisition motivation and communication are rarely the same. But I’m coming around to the idea. Freight can’t support BYOC deployment because it’s built onKora, the proprietary system confluent built for its SaaS offering. Kora is not easily deployed in a customer’s environment, whereas WarpStream is.


Confluent can now offer self-hosted, BYOC, and cloud versions of their product. I suspect their customers were asking for BYOC, a trend I expect to increase (seeBring Your Own Cloud, Nuon﹩, and Hosted SaaS Challenges With Jon Morehouse). Confluent’s product offering is indicative of what customers want: flexible deployment options. There’s no one-size-fits-all deployment offering.


But Confluent is now running (and supporting) three different versions of Kafka: self-managed open-source Kafka, Confluent Cloud with Kora, and WarpStream. If Confluent were starting from scratch now, I don’t think they would have built things this way. While there’s no one-size-fits-all deployment offering, I suspect we can still build a single system that can accommodate flexible deployment. Doing so would provide a much better user (and vendor) experience.


ClickHouseis an example of such a system. I really didn’t understand why everyone was so excited about ClickHouse until I dug into it in my recent post,Unpacking the Buzz around ClickHouse. Then it clicked: you can run ClickHouse as a single node. In hindsight, it’s a comically obvious gap in the realtime online analytical processing (OLAP) space.


ClickHouse is more than a single-node binary, though. It can also be runin a cluster, or embedded as an in-process library withchDB. The company also offers aSaaS cloud, andBYOCdeployment products. This is an incredible amount of flexibility for one system. It scales from a single in-process library all the way to a distributed cluster. And it can be deployed as a self-managed service, BYOC, or as SaaS. Its highly efficient single-node binary can also scale up nicely, too. This is the future.


Once this clicked, I started seeing the trend everywhere. PostgreSQL now haspglite.devfor client-side and edge deployment.Neonhas added an object storage tier (granted, it’s a fork when I last checked).MotherDuckis trying to stretchDuckDBfrom analyst laptops to the cloud.Daft﹩’s next-generation query engine is going after not onlySpark-scale workloads, but DuckDB as well.


![](https://substackcdn.com/image/fetch/$s_!n5_h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72655317-26f2-4d70-a748-5bb69bbb6294_688x511.png)

*View Post*


There are many reasons for this shift. On the product side of the fence, we’re finally understanding what infrastructure customers want: flexible deployment. On the tech side, new trends such as zero-disk architecture, Rust and C++ adoption,composable data systems, andWebAssembly’s(Wasm)slow but continued growthhave enabled us to actually build such systems.


Infrastructure vendors need to ask themselves: does our system deploy self-managed, BYOC, and as a SaaS cloud? Can we support in-process embedded, single-node, and clustered execution? If not, you’re cooked.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a ﹩ in this newsletter. See myLinkedIn profilefor a complete list.
