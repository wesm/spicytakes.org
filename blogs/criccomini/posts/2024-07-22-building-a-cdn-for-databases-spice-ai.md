---
title: "Building a CDN for Databases With Luke Kim"
subtitle: "Luke Kim, the CEO of Spice AI, talks with me about how to get batch data back into production. Our conversation covers sidecars, Rust, WASM, tiered storage, Arrow Flight, and a lot more..."
date: 2024-07-22T11:06:05+00:00
url: https://materializedview.io/p/building-a-cdn-for-databases-spice-ai
slug: building-a-cdn-for-databases-spice-ai
word_count: 2626
---


I recently wrotea postexploring how best to serve data lake files in production.Luke Kimgot in touch to discuss his startup’s approach. Luke is the CEO ofSpice AI, a startup building an open-source CDN for databases. Spice runs as a series of tiered databases from object storage all the way to the edge. Prior to founding Spice AI, Luke ranMicrosoft Azure’sincubation program, which was responsible for bothDaprandOpen Application Model (OAM).


---


C.R.: I want to start with the work you did at Microsoft running the Azure Incubations team. You were in charge of several projects including Dapr and Open Application Model. Both of these projects tackle the challenges of building and deploying application code in the cloud. How did these projects come to be?


L.K.: Back in 2011, I worked on Visual Studio. As a side project, I also worked withMark Russinovich, then Technical Fellow in Windows, and now CTO of Azure, on his set of advanced system utilities called theWindows Sysinternals Tools.


In April 2019, Mark asked me to join his team directly, whereYaron Schneider, who had helped createKEDA, had put together an early internal prototype called Actions, along with several other projects. I immediately saw how Actions, a unified API and set of application building blocks, could help developers build better microservice applications.


Mark wanted to expand incubations, so I pitched that we create an official Azure Incubations group, which we did. I led the team. Yaron and Mark Fussell, the unofficial Actions PM we had borrowed from Azure Compute, reported to me, and we started hiring a team to incubate the Actions project in earnest. In July, we set an ambitious goal to launch Actions at the Microsoft Ignite conference 4 months later in October, which we did as Dapr.


I also worked with Mark to develop the process of incubations across Azure. During my tenure, we built Azure Incubations from two engineers, to around 25, and worked on incubation projects across open-source, cloud-infra, databases, blockchains, and AI/ML. Many of our projects were focused on helping developers with the challenges of building modern software. We had also recognized the challenges in deploying applications across complex cloud and edge infrastructure, so one of these projects was the Open Application Model (OAM), which eventually evolved intoRadius. Dapr and OAM/Radius are complementary projects. Dapr, a set building-blocks to build distributed applications, and OAM/Radius, an application-deployment model to deploy them.


C.R.: This “building blocks” trend seems to coincide with Kubernetes sidecars. Prior to that, organizations used shared libraries to provide such functionality.


I first came across the library-as-sidecar pattern with Airbnb’sNerveandSynapseprojects. At LinkedIn, I worked on a team that built a software load balancer (REST.li) as a Java library. The drawback of our approach was that it boxed us into the JVM. We couldn’t easily use our load balancer with Javascript, Python, or Ruby—other languages at LinkedIn. The sidecar pattern disentangles you from the language; it’s so much more portable. Airbnb’s projects really influenced how I think about application building blocks.


Dapr seems to go well beyond service meshes. It looks more likeSpring, but as a sidecar rather than a library. Your current project, Spice AI, brands itself as “building blocks for data and AI applications”. It sounds like you’re trying to do for data applications what Dapr does for microservices. Is this a fair characterization? What problems does Spice solve for these applications?


L.K.: The history of the technology industry is a story of turning lower layers of the application stack into commoditized building blocks. For example, we used to rack and stack servers, but now we have a set of cloud infrastructure building blocks we can compose into scalable infrastructure. This process enables value to move up the stack, ultimately to the user, as the developers can focus more and more on business and user value.


Kubernetes (and associated patterns like service meshes) are building blocks for the container layer, which enabled distributed application architectures that were hard to get right manually, including microservices with sidecars.


You're exactly right on the benefit of sidecars. Separation from the language and runtime, enables common functionality to be portable and platform agnostic, while maintaining performance, through a very fast kernel-level local loopback. It also makes them the perfect vehicles for presenting incrementally adoptable building-blocks to almost any application.


Like Dapr, Spice focuses on the application-layer, and so yes, can be characterized as a set of building-blocks specifically for data and AI-applications.


If you consider the layers of intelligent applications, they might roughly be thought of as algorithmic/heuristic at the bottom, then various measures of data and big data driven, to traditional machine learning driven, and now to modern AI driven. As you move up this stack, you want to focus on delivering user value at higher and higher levels, not deal with the lower level data plumbing. Like the cloud infrastructure example, lower level plumbing can be slow to build, expensive, hard to maintain and get right, and often offers little differentiated business value.


Spice focuses on solving three problems to help you move up the intelligent application stack.

1. Access to data wherever it lives.
2. Making that data fast and cost-effective to be useful.
3. Making it easy to use that data with machine learning models and AI.


C.R.: In a recent post, I wrote about a gap that I see in the data lakehouse ecosystem:exposing lakehouse data back to production. That post is actually how we got in touch. All three problems that you listed relate to the gap I’ve been thinking about.


The two most common approaches I’ve seen to serving lakehouse data are to set up an ETL pipeline or to spin up a cache to serve low-latency production use cases. Can  you walk me through Spice AI’s architecture, and some of the design decisions and tradeoffs you made?


L.K.: The data ecosystem has made a ton of progress across writes and transforms, with mature solutions for ETL, ELT, and reverse-ETL available. However, as you've identified, there's still a gap for read and query scenarios, especially specific to those three problems.


In the article, you note"What I want is a cache that sits in front of warehouse data and exposes it through a low-latency API."That's exactly what the Spice runtime is—filling that gap.


Spice is a drop-in caching and materialization solution that sits in front of databases, data warehouses, and data lakes. It provides a single unified SQL API for low-latency, high-concurrency queries. Spice supports both caching and materialization, so to make the distinction between them, you can think of materialization as proactive and caching as reactive.


By enabling materialized acceleration in Spice, data is prefetched and precomputed before it's queried, with the results stored (materialized) using an embedded database, such asDuckDB, in the runtime. This is a proactive, anticipatory approach to serve queries from a fast, local store. In addition, because there is a replica of data stored locally, applications are more resilient as they can query data via either the Spice runtime or the underlying data source.


Contrast materialization to caching, which traditionally involves a cache "miss", then falling back to query the underlying source, caching the result, so that future queries can be served from the cache. Spice also has support for this form of results caching, which can be used together with materialization for complete query coverage.


In terms of architecture, a core principle of Spice is to be application developer centric.


The latest version of Spice, built in Rust, is actually a complete rewrite of ourSpice Firecacheruntime. Firecache was written inGo, also utilized DuckDB, and was serving hundreds of millions of queries a month; however, Firecache was a cloud-only solution. As we focused on developers, and learned from customers, we realized the power and resiliency of a lightweight runtime that sits alongside  applications, often as a sidecar, deployable to the edge or to any cloud.


So we re-architected Spice to be both cloud-scale and just as easily be deployable to anywhere your application runs. You're not setting up bulkyZookeeperclusters, it's a single-node optimized binary/container that's horizontally scalable. Being application focused, Spice differs from federated query architectures like Trino/Presto/Dremio, where there is typically many applications querying a single cluster. Spice inverts the application-data warehouse relationship to be more distributed, and it's typical to have one or more Spice instances serving one application. We've even seen customers elastically scale to having a dedicated Spice instance per application user. And an additional benefit to one Spice instance per application or application tenant is that you can apply scoped security, privacy, and compliance controls to each Spice instance accordingly.


One trade-off of being single-node optimized is of course, the limits of a single node. However, we see the same pattern with our customers thatMotherDucknoted in their "Big Data is Dead" thesis, which is that the working set of data queried day-to-day is normally 2-3 orders of magnitude smaller than the data the applicationcouldquery. If you materialize just an application specific working set on a single node, for most cases it will handle 99% of queries, with always the ability to fallback to the underlying data source in the margins. We've run Spice on horizontally-scalable single-nodes each with 128-cores, 2TB of RAM, and attached NVMe, which handles almost any application use-case.


Being application developer-focused extends to the API. Spice supports connections via JDBC/ODBC/ADBC and Arrow Flight, so there's often minimal, if any, changes required to your application or client to drop it in front of your database. It's easily configurable via its simple spicepod.yml manifest, which is similar to a package.json for a Node.js application.


Finally, one customer-driven design decision we made was to support both OLTP (SQLite,PostgreSQL) and OLAP (Arrow,DuckDB) databases for optimal row/columnar materialization stores at the dataset/table level.


C.R.: I’ve been thinking a lot about tiered storage lately. We’ve had an explosion of layers from memory to NVMe to EBS to object storage. Similarly, we’ve seen databases stretched from the client through local CDNs all the way to regional and multi-region locations.


How does tiering work with Spice? Is Spice stackable? That is, can I deploy it in such a way that every application node has a Spice sidecar, which fronts an application-specific Spice cluster, which then fronts a cloud-based Spice account? Can it be installed client-side via WASM?


L.K.: Yes, that's exactly the idea. Spice was designed to be tier-optimized, or as we like to say, "don't fight physics; minimize data transit." This means co-locating Spice instances with both the underlying data source and the application or client. To do that, Spice is "stackable" or "chain-able", in that Spice instances can be deployed to different tiers, like cloud, on-prem, and edge, and can connect to each other over standard data protocols.


One benefit is you can do as you describe; deploy application-specific Spice instances as sidecars that can take advantage of local storage tiers, such as RAM, local NVMe, or locally attached SAN for a working set of data, and push queries to Spice instances that are colocated with the underlying data source.


For example, in one deployment of Spice, 100s of billions of emails are stored in a data lake in a central region. Spice instances in that region can pull just the data off storage needed and Spice instances in another region can query or be pushed data from the central instance. This makes the entire system much more reliable, as replicas of region specific data are distributed, queries are faster, and data transit minimized.


Long-term, we'd love to extend Spice to client-side WASM, but isn’t yet a priority. There is a trade-off between the number of distributed replicas and minimizing data transit. You could use some of the great DuckDB solutions to connect to Spice instances for in-browser use-cases.


C.R.: How does the stacking actually work in Spice? Is it simply caching identical SQL queries, caching data pages, or something else? And how do you manage consistency as data changes underneath Spice?


L.K.: There are a couple of ways to stack Spice. The first is really just sharding across infrastructure tiers where you're just treating Spice like any other data source.


For example, you could use region-specific (or even end-user specific) Spice instances that connect to central Spice instances that read and materialize partitions of data from Parquet files on a central S3. This minimizes compute on S3 and data transit to each region. Spice supports API-triggered updates, and in many cases applications know when data updates happen (like writing a new Parquet file) so materialization can be triggered analogous to a CDN edge-load.


Another interesting use-case is teams building data APIs for their customers where they provision dedicated Spice instances to serve each customer individually with subsets of data from centralized Spice instances. So in addition to performance and efficiency, you get isolation.


For many scenarios, interval or API-triggered loads across tiers work great. But where strong consistency is required, Change-Data-Capture (CDC) can be employed for distributing changes in real-time. Spice supports CDC through theDebeziumData Connector and our internal implementation, which can be thought of as Debezium overApache Arrow Flightinstead of typicallyApache Kafka. Using this method, Spice instances connect to each other using Arrow Flight and are pushed changes as they happen ensuring consistency and freshness.


And you can combine methods, so in the first example, you might API-trigger Parquet reads on  central Spice instances, which then push filtered data to region-specific instances over Flight. We're still fully developing the Spice-to-Spice Flight DoExchange method and we'd love feedback on the feature.


C.R.: I’m curious about the decision to deploy Spice locally as a sidecar. The pendulum seems to be swinging from sidecars back to embedded libraries. I think this trend coincides with Rust adoption. Rust plays nicely with WASM and is more easily embeddable across languages. Given that Spice is written in Rust, what was the calculus around sidecar versus embedded library in the application?


L.K.: A core principle for Spice is giving users full-control over resource allocation; a separate process allows fine-grain resource control at the container runtime and OS level. One of the issues we saw with bulky, cloud managed products is you only have broad strokes control over resource allocation. If you need more concurrency, you need to provision an entirely new fixed sized cluster, or you need to change VM types.


Running Spice outside the application process allows fine-grain, elastic, application-specific control over how much CPU and memory it has, enabling dynamic scale separate from the application. Additionally, updates to the application can be rolled out without losing in-memory accelerators or caches, so not being tied to the application deployment lifecycle is also a benefit.


Ultimately though, we want users to have the choice how they run Spice, which could be as a library, sidecar, microservice, or cluster. Optionality is a core principle for Spice. We'd love people to reach out if they are interested in running Spice as a library.


C.R.: Speaking of reaching out, this seems like a good place to call the discussion. Thanks so much for taking the time to talk. I’ll give you the final word.


L.K.: Thanks, Chris, this has been a lot of fun!


We’re currently helping a limited number of teams evaluate Spice in production with hands-on proof-of-concept (POC) engagements, so if that sounds interesting to any readers, feel free to reach out to me directly atluke@spice.ai.


And to learn more about Spice, visit the GitHub repo athttps://github.com/spiceai/spiceai.


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
