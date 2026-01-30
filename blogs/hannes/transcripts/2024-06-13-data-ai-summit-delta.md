---
title: "Announcing DuckDB Support for Delta Lake and the Unity Catalog"
date: 2024-06-13
event: "Data + AI Summit 2024"
location: "San Francisco"
video_url: "https://www.youtube.com/watch?v=wuP6iEYH11E"
video_type: "Keynote"
transcribed: 2025-01-30
---

*This transcript was AI-generated using Whisper and may contain minor errors.*

## Transcript

Hey, thank you so much. Yes, hello and very good morning. It's wonderful to see all of you here. I have to adjust my eyes a bit to the amount of people. As Shanta said, I'm one of the people behind DuckDB. So for those of you who do not know, DuckDB is a small in-process analytical data management system. It's a very simple system. It's just that the stars on GitHub have doubled within a year to almost 20,000. And in fact, we're so close to 20,000, so if you want to like it today, then maybe we'll beat it.

But what also happened, and just last week, we actually released DuckDB 1.0, and that was a big moment for us. It was the culmination of six years of R&D in data management systems. And what does 1.0 mean? It means that we have now a stable SQL dialect and various APIs. And most importantly, our storage format for DuckDB is going to be backwards compatible from now on out.

But maybe taking a little bit of a step back, how does DuckDB fit into the general ecosystem? If we look at the world's most widely used data tools, Excel, and we look at very capable systems like Spark, there's still a pretty big gap. There's a lot of data sets that are not going to work in Excel, but they are maybe a bit too small to actually throw Spark at them. So DuckDB is really perfect for this last mile of data analysis, where you may not need a whole data center to compute something. So for example, you have already gone through your log files in Spark, and now it's time to do some last mile analysis with DuckDB, doing some plots, what have you. That's where DuckDB fits into this big picture.

But now we have to somehow get the data from Spark to DuckDB. So how are we going to do that? Obviously, we're going to use the best tool for the job available, right? CSV files. Maybe not. So typically, people use Parquet files for this. Obviously, both Spark and DuckDB can read and write Parquet files, so that works really well, but we've all heard about the issues that have appeared with updates and schema evolution, these kind of things, which is why we have lakehouse formats.

So today, we are announcing official DuckDB support for Delta Lake. It's going to be available completely out of the box with zero configuration or anything like that. But we have done a bunch of these integrations, and one thing that's really special about the Delta Lake integration is that we use this delta kernel that Databricks is building with the community, and that's really exciting because it means that we don't have to build this from scratch like we used to, for example, with the Parquet reader, but we can actually delegate a lot of the hard work of reading delta files to the delta kernel, while at the same time keeping our operators within the engine and so on and so forth. So it's really exciting.

We also made an extension for DuckDB that can talk to the Unity Catalog. So with this extension, we can find the Delta Lake tables in the catalog and then actually interact with them from DuckDB itself. So here we can see a script that actually works if you install DuckDB now. You can install this Unity Catalog extension. You can create your secret, which is like credentials, and then you can basically just read these tables as if they were local tables. If you want to hear more about this, there's actually going to be a talk this afternoon at 1:40. Just look for DuckDB in the title.

So the Delta extension joins this growing list of DuckDB extensions. For example, there's others for Iceberg, Vector Search, Spatial, and this sort of thing. But as an open source project and a small team, we're really excited about Tabular and Databricks bringing Delta Lake and Iceberg closer together because for us, it means we don't have to maintain two different things for essentially the same problem. And we're really excited about that. It means less work for us and I think everyone wins.

I just want to plug one sort of small thing that we're actually launching today. I've mentioned extensions to DuckDB. We've seen a lot of uptake in DuckDB extensions. And from now on, actually, we are launching community extensions, which means that everyone can make DuckDB extensions and basically publish them and then installing them is as easy as just typing install into DuckDB near you. So that's all for today. Thank you very much. And I will give back to Shanta.
