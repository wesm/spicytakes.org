---
title: "Nimble and Lance: The Parquet Killers"
subtitle: "Everything you need to know about the new AI/ML storage formats from Meta and LanceDB."
date: 2024-05-13T17:03:03+00:00
url: https://materializedview.io/p/nimble-and-lance-parquet-killers
slug: nimble-and-lance-parquet-killers
word_count: 1781
---


Apache Parquethas been the de factocolumnar data formatonobject storagefor some time. Nearly every cloud data warehouse and data lake integrates with Parquet. But developers are recognizing its limits. Recently, two new formats were open sourced—one fromMetaand one fromLanceDB. In this post, I’ll dig intoNimbleandLance V2(LV2) and give some thoughts.


## Storage Format Primer


(You can skip this section if you know what a columnar file format is.)


Before I discuss Nimble and LV2, you need to know how a columnar storage format works. Meta’sNimble YouTube videofromVeloxCon 2024does a good job summarizing, so I’ll borrow from it.


Row-based formats write data to disk as a sequence of row bytes. Consider a database table with auser_idandfeaturescolumn. When a new row is written, it’s stored as a sequence of bytes representinguser_idfollowed by a sequence of bytes representingfeatures.


![](https://substackcdn.com/image/fetch/$s_!iCAJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21b2ef27-04c5-46d7-838c-84347c8f06c0_1177x430.png)

*Nimble, A New Columnar File Format - Yoav Helfman, Meta*


Each red block on the right represents one row written to disk. Each row contains bytes for each column, one after the next (represented by green and orange boxes). Columnar file formats invert this sequence. Bytes are grouped by column not row.


![](https://substackcdn.com/image/fetch/$s_!h4Bm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97013aad-9736-4436-8d6e-8a61e9205801_1170x399.png)

*Nimble, A New Columnar File Format - Yoav Helfman, Meta*


Columnar formats are useful for data warehouse-style queries that typically do aggregation on a few columns but a large number of rows (e.g. SELECT state, SUM(price) FROM sales GROUP BY 1). In a row-based format, you’d have to read every row just to use one or two columns. With a column-based format, readers can read only the column bytes they need and take advantage of sequential IO performance gains.


Traditional columnar-based formats require the writer to buffer all data before they can write it. The writer needs to know all of theuser_ids before it can write the red block in the image above—a substantial burden


Parquet (andORC, a similar but less popular file format) solve this problem by introducing the idea ofrow groups(or ORC’s synonymousstripes). Row groups combine the row-based and column-based approach. The idea is to partition the data up into smaller groups of rows so that a writer can store just that set of rows in a columnar format. Because the partitions are relatively small, the writer doesn’t need to buffer the entire data set before writing the columnar data for that row group.


![](https://substackcdn.com/image/fetch/$s_!P9o2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa63acead-dd62-40d9-a48b-1de15615fe74_1174x398.png)

*Nimble, A New Columnar File Format - Yoav Helfman, Meta*


The example above illustrates a table that’s been divided into two row groups (orange and green). Each row group contains a sequence of columns (represented by the blue and red blocks).


Pages are represented as green blocks in the image—chunks of each column. Pages are used so a reader needn’t read all column data for a row group; they can read only a subset of the data if it’s sorted in the same manner as their query. All of these tricks are just ways to partition the table data up to make it friendly for data warehouse-style queries.


## Parquet’s Problems


Parquet is an incredibly well done storage format. It has enabledcomposable database systemsand provided an integration format for data lakes and cloud data warehouses. But it’s begun to show its age. LanceDB’sLance v2 postsummarizes the issues well:

- Point lookups: Reading a single row requires reading an entire page, which is expensive.
- Large values: Columns with large values make the row group size hard to tune. If the row groups are small, only a small number of rows will be included in each page (since the large values will take most of the page). If a row group is large, writes become memory intensive.
- Large schemas: Some datasets have 1000s of columns. Parquet requires readers to load the schema metadata for all columns to read just one—a costly and wasteful operation.
- Limited encodings: There have been an explosion of encoding styles for data of different shapes and sizes. These new encoders do a better job of compacting and compressing data in different scenarios. Parquet provides only a fixed set of dated encoders.
- Limited metadata: Parquet only allows encoders to store metadata—statistics, min, max, nulls, and more—in pages. Some encoders would benefit from storing metadata at the row grow, stripe, or file level.


These problems are particularly acute for machine-learning (ML) and artificial intelligence (AI) style uses. Machine learning data often has columns with a long list of floats, as thefeaturescolumn in the screenshots above illustrates. AI use-cases often need text, images, or video near their feature vectors for training andretrieval-augmented generation(RAG) use cases. Parquet struggles with such use cases. Nimble and LV2 address these issues.


## Nimble and LV2


Nimble takes an incremental approach to Parquet’s problems. The format handles wide schemas usingFlatBuffersrather thanProtobufto decode only the metadata bytes that are actually used. Nimble’s encoding layer is extensible; new formats can be added by the user. Metadata is also made extensible by treating it as part of the encoding payload rather than a rigid schema in the file footer. While stripes (row groups) still exist, their footers have been moved to the end of the file.


![](https://substackcdn.com/image/fetch/$s_!_86W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e0b5740-c91c-4fae-8ad9-73ac9f0aebd1_1088x956.png)

*Nimble, A New Columnar File Format - Yoav Helfman, Meta*


LV2 is far more radical. Parquet’s row groups have been completely removed. LV2 files are simply a collection of data pages, column metadata, and a footer—that’s it. In the name of extensibility, LV2 has no type system and no built-in encodings. Both are pluggable. LV2 is so thin, the whole spec is a mere~200 line Protobuf file.


![](https://substackcdn.com/image/fetch/$s_!HVUm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F976ca889-d1c8-4173-872d-21d4df1bb05b_1310x294.png)


## Extensibility Is a Double Edged Sword


Engineers love to make things extensible. It’s an escape hatch for bad decisions, the promise of flexibility, and an openness to new ideas. But extensibility causes fragmentation.


Each library must implement a wide range of encodings. A library that doesn’t support an encoding will not be able to read or write its data. Users will see read errors. This is a frustrating user experience.


In an enterprise, this is a common pitfall. Team A encodes a column with some fancy new encoding that suits their use case. Team B wants to read the data but can’t because their library (probably written in another language) doesn’t support the encoding.


![](https://substackcdn.com/image/fetch/$s_!SAGE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08a1d9d3-29b3-478f-a2ab-04445d7197a8_1374x380.png)

*View Post*


Meta ispleading with users—please don’t build more implementations. (Emphasis added.)


> More than a specification, Nimble is a product.We strongly discourage developers to (re-)implement Nimble’s spec to prevent environmental fragmentation issues observed with similar projects in the past.We encourage developers to leverage the single unified Nimble library, and create high-quality bindings to other languages as needed.


They’re dreaming. It’s not written in Rust, so that’s going to happen. There will be others, too. Engineers just can’t resist reimplementing specs in their native languages.


Lance ismore laissez-faire:


> If a user tries to read a file written with this encoding, and their reader does not support it, then they will receive a helpful error “this file uses encoding X and the reader has not been configured with a decoder”. They can then figure out how to install the decoder (or implement it if need be). All of this happens without any change to the Lance format itself.


And we’re just talking about encodings. LV2’s choice to ditch both encodingsandtype systems really freaked me out. I spent a bunch of time with type systems when working onRecap. It’s really hard to get types right.


This is hell for data engineers. At least, that was my first reaction. I’ve since realized that LV2 has adopted an unstated philosophy: Arrow will dictate the standard.


LV2 has already implemented Arrow’s types (Schema.fbs) as its first type system. This is an excellent choice. Likewise, the encodings that Arrow supports will dictate what other implementations must adopt. I really like this.


## To Stripe or Not to Stripe


It’s not totally clear to me whether LV2’s decision to ditch stripes is a net win or not. Column I/O is not sequential in LV2. Reads can be scattered across pages all over the file. LanceDB’sWeston Pacehad areasonable responsewhen I asked about this:


> Pages should be large enough that there is no real advantage to having them sequential. E.g. 10 random 4MB reads has same perf as 10 sequential 4MB reads. This should be true for both disk and cloud. Also, LV2 favors larger pages (compression chunk size is independent)


This led to a very interesting exchange between Weston andWarpStream’s [$] co-founder,Ryan Worl. Ryan, too, is worried that non-sequential pages will require more reads.


![](https://substackcdn.com/image/fetch/$s_!0P0H!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2df6dffe-9339-45c1-9050-72bbd78a525f_1396x1616.png)

*View Post*


Both engineers know what they’re talking about. Tradeoffs are always tough. I suspect LV2 has opted for tuning that works better for ML and AI use cases. I’m interested to see how these formats perform against more traditional analytical queries—large scans on a few columns that span many pages.


EDIT: LanceDB’sWeston Pacehas publishedColumnar File Readers in Depth: Parallelism without Row Groups, which further discusses their choice to abandon row groups.


## It’s Early Days


Nimble and Lance are both young. They’ve chosen to focus on ML and AI workloads first. Parquet is weak for these use cases, and there’s a real need for a better format. But the ultimate goal for both formats is to replace Parquet foronline analytical processing(OLAP)-style queries, too.Chang She, LanceDB’s CEO,tells me:


> Don’t want to put words in Nimble’s mouth but Lance has so far been very focused on vectors / images / videos + indexing. Basically OLAP + Search + Training. AFAICT that’s not the stated focus for Nimble.


Nimble’s Github says:


> Nimble is meant to be a replacement for file formats such as Apache Parquet and ORC.


Neither format is close to this yet. Nimble is missing predicate pushdown—a key feature for analytical queries. LV2has only basic encoding support. Theperformance numbers in Meta’s talkshow a machine-learning use case executing twice as fast on Nimble. Given the favorable workload, one wonders how an OLAP workload would look. Probably not great right now. Lance includes some numbers in their (somewhat dated) CMU presentation:


![](https://substackcdn.com/image/fetch/$s_!3S2I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea5c2a80-bb36-4550-a38e-8bf7891c53fd_974x420.png)

*Lance: A Modern Columnar Data Format (Chang She)*


Given all this, it’s obvious that the formats are not ready for prime-time yet. Most analytical use cases are still best suited for Parquet. That’s totally fine—it’s expected. These are young projects. I’m bullish on both, but particularly LV2. It’s a radical shift, but its integration with Arrow and thoughtful design make it really compelling to me.


---


#### Book


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


#### Disclaimer


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
