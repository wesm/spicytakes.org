---
title: "Make Lakehouse Catalogs Boring Again"
subtitle: "Let's all agree on Iceberg's REST API and let the query engines dictate its evolution. Vendors can compete on enterprise features."
date: 2024-07-03T17:28:06+00:00
url: https://materializedview.io/p/make-lakehouse-catalogs-boring-again
slug: make-lakehouse-catalogs-boring-again
word_count: 616
---


There’s plenty more to write about data lakehouse catalogs, but I’m going to call it with this post. My last write-up, below, explores where I’d like to see lakehouse catalogs go from here.


Before I get to that, there’s a distinction to be made between lakehouse catalog use cases. I’m going to divide the use cases into “core” and “non-core” functionality. Core functionality provides query engines with the metadata they need to execute queries—the information_schema functionality that I talked about inpart 1 of this series. Non-core functionality is everything else that lakehouse catalogs do (or could do): user interfaces, data discovery, lineage, governance, and so on.


I would love to see everyone congregate aroundApache Iceberg’sREST APIfor core lakehouse catalog functionality. In fact, this is already happening.Databricks’sUnityhas (or will have?) Iceberg’s REST API. Nessieannounced in Maythat they, too, will have Iceberg REST endpoints.Snowflake’sPolariswill be an open source implementationof Iceberg’s REST API.ManyotherIcebergREST implementations are popping up, too.Gravitino,which I’m toldwill soon begin incubating in Apache, looks particularly promising.


Adopting Iceberg’s REST API is a great first step in cleaning up this mess. Next, I’d like to see query engines take a more active role in evolving the spec, particularlyApache DataFusionandTrino. The core functionality that Iceberg provides is critical for query engines; they should be the ones dictating how it evolves.


Yes, this means that Databricks’sSpark(andPhoton) query engine will have some say. And yes, Snowflake is also a query engine that should have a say. But reorienting the API evolution around the query engines it serves means more projects can take an active role, thereby reducing the control of one or two vendors.


I don’t know exactly what an “active role” looks likefor these query engines. I would love for Trino and DataFusion to throw down the gauntlet and say, “This is theOpenAPIwe’re working with”. DataFusion already has aCatalogProvidertrait, it’s just in Rust. Pushing one level deeper means query engines like Trinowill be able to deprecateHive Metastore Service(HMS),AWS Gluecatalog, JDBC catalog, Nessie catalog, and Snowflake catalog integration. This will take time, but it’ll be better in the long run.


PuttingApache ArrowandApache DataFusionin the driver’s seat is something thatLanceDBdid withLance V2. Rather than define their own types and encodings, they’re deferring to Arrow—something I wrote about inNimble and Lance: The Parquet Killers. Applying a similar approach in the catalog space seems wise to me.


![](https://substackcdn.com/image/fetch/$s_!S2P_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d9cb7af-9e56-4008-9a69-5b6b133d4d58_693x136.png)

*View Post*


The nice thing about this is it frees vendors like Databricks and Snowflake to focus on the non-core functionality. Don’t mistake “non-core” for not valuable. Much of the functionality in this bucket is extremely valuable, if not required for enterprises. In fact, Databricks’s (non-open source)Unity pagefocuses entirely on such features—discoverability, permission management, governance, monitoring, observability, and so on. This is where the vendors should compete.


From this vantage point, it seems data lakehouse vendors have accidentally stumbled upon the wedge that traditional data catalogs have been struggling to find. Traditional data catalogs have been unable to shift from nice-to-have to must-have in the enterprise; they remain a dusty tool that’s often ignored once installed. Data lakehouse catalogs are must-have for anyone running query engines on a data lake. From there, eating into the customer base ofAlation,Datahub, and others seems natural.


Other posts in this series are available here:

[Begun, The Catalog Wars HaveChris Riccomini·June 20, 2024Read full story](https://materializedview.io/p/begun-the-catalog-wars-have)
[Data Lakehouse Catalog Reality CheckChris Riccomini·June 27, 2024Read full story](https://materializedview.io/p/data-lakehouse-catalog-reality-check)

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
