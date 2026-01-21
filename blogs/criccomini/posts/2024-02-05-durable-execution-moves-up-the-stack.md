---
title: "SQLite’s Tricky Type System, Durable Execution Moves up the Stack, and HikariCP Is Too Fast..."
subtitle: "Everything you need to know about SQLite's type system; Shower thoughts on durable execution, workflows, and their user interfaces; and HikariCP is a giant performance flex."
date: 2024-02-05T11:20:58+00:00
url: https://materializedview.io/p/durable-execution-moves-up-the-stack
slug: durable-execution-moves-up-the-stack
word_count: 906
---


I joinedRyan Blue,Wes McKinney, andPedro Pedreirato talk about composable data systems onThe Data Stack Show. If you enjoyed my last post ondisassembled databases, check outThe Parts, Pieces, and Future of Composable Data Systems.


---


## Demystifying SQLite’s Type System


It’s been a rainy week here in the bay area. I’ve spent much of it working on Recap’sSQLite client and converter. I did some reading on SQLite’s type system while doing so. It has some surprising behavior. Given SQLite’s widespread adoption—especially in tests—I want to highlight some peculiarities.


SQLite’s type system has three important concepts: datatypes, storage classes, and column affinities. SQLite’s datatypes define how data is written to disk (think variable length integers,zigzag encoding, and so on). Its storage classes define how data is stored in memory. There are just five storage classes: NULL, INTEGER, REAL, TEXT, and BLOB.


> A storage class is more general than a datatype. The INTEGER storage class, for example, includes 7 different integer datatypes of different lengths.This makes a difference on disk.But as soon as INTEGER values are read off of disk and into memory for processing, they are converted to the most general datatype (8-byte signed integer). And so for the most part, "storage class" is indistinguishable from "datatype" and the two terms can be used interchangeably.


To understand column affinities—the last concept—you must first know that SQLite ignores column types (unlessSTRICTis used). A value of any type can be written to any column. But rather than ditch column types completely, SQLite uses column affinities to convert data as it’s coming in.


Column affinities govern how data is coerced before it’s written to disk, and to which values and columns the coercion is applied. There are five affinities: TEXT, NUMERIC, INTEGER, REAL, and BLOB (note that these are not the same as the storage classes). Here’s the TEXT affinity’s documentation:


> A column with TEXT affinity stores all data using storage classes NULL, TEXT or BLOB. If numerical data is inserted into a column with TEXT affinity it is converted into text form before being stored.


To determine a column’s affinity, SQLite uses a set of text-matching rules. TEXT affinity is determined as follows:


> If the declared type of the column contains any of the strings "CHAR", "CLOB", or "TEXT" then that column has TEXT affinity. Notice that the type VARCHAR contains the string "CHAR" and is thus assigned TEXT affinity.


SQLite’s column affinity documentation hasa complete list of rules. My favorite is, ‘If the declared type for a column contains any of the strings "REAL", "FLOA", or "DOUB" then the column has REAL affinity.’


This can lead to some funky behavior, but SQLite does surprisingly well in normal use.


![](https://substackcdn.com/image/fetch/$s_!s7jZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a08c5da-ae8f-4ce7-a56c-26110f5a821d_1602x1366.png)


Why go to all this trouble?The Advantages of Flexible Typingclaims the design better suits mixed-type table columns, dynamic programming languages, JSON, cross-compatibility with other databases, and so on.


## Durable Execution as Code, Config, and UI


I spoke recently to bothTemporalCEO,Maxim Fateev, andRestate’s founder,Stephan Ewen. It struck me in both conversations how differentdurable execution,workflow orchestration, andmicroservice orchestrationare when defining work to execute. I seeat least four different waysin which work is defined:

1. Graphical user interfaces (GUIs) (Camunda,Orkes)
2. Config definitions (Camunda,Kestra)
3. Config-as-code definitions (LittleHorse,Airflow,Prefect,Dagster)
4. Code APIs and SDKs (Restate,Temporal)


GUIs seem to be popular withbusiness process model notation(BPMN) systems.  XML is unwieldy, so users ask for a UI.CamundaandOrkesboth offer robust workflow builder GUIs (though I don’t believe Orkes uses BPMN).


Config definitions in YAML, JSON, or XML seem to be most popular with legacy data processing workflow systems likeAzkabanandOozie. Config-as-code has largely replaced config files in the data processing space now.Dagster,Prefect[$], andAirflowall define workflows in code.


Durable execution frameworks prefer APIs and SDKs for their flexibility. Workflows tend to be more rigid—you know the structure of the workflow beforehand. APIs and SDKs work better for dynamic execution with branching and loops.


Systems are starting to adopt more than one of these interfaces.Restatenow hasJSON workflow definitions.LittleHorseplans toadd config and GUI support this year. And people have builthome-grown config systemson Airflow for years.


This trend is unsurprising, but notable. I’ve written about how durable execution needs to move beyond traditional transactional use cases like payment processing:

[Durable Execution: Justifying the BubbleChris Riccomini·November 13, 2023Read full story](https://materializedview.io/p/durable-execution-justifying-the-bubble)

These different models exist because they are well suited for different users and use cases. As durable execution systems move up the stack and workflow systems move down the stack, their addressable market (and competitors) will increase—precisely what I’ve been calling for.


## Project Highlight: HikariCP


HikariCPis an in-processJava Database Connectivity(JDBC)connection pool. Rather than create a new connection for every database request, connection pools keep and reuse them. This removes the overhead of creating a new connection.


We usedc3p0at my previous job, so I wasn’t familiar with HikariCP when I saw Gwen Shapira’s recenttweet.


![](https://substackcdn.com/image/fetch/$s_!IJf6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e18a24a-cee1-44be-85d8-7a8b60a34368_1382x340.png)

*See the post*


This is not hyperbole.HikariCP’s documentationis a gold mine. TheirDown the Rabbit Holepost is a must-read for anyone fixated onGunnar Morling’s1brc challenge.


Gwen’s post also sparkedan interesting questionabout in-process and out-of-process connection pools (likePgBouncer). I don’t have a good answer, but it seems worth answering.Let me knowif you’ve got an answer.


---


Share


---


Support this newsletter by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to someone.


![](https://substackcdn.com/image/fetch/$s_!CI0B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fde442631-41a6-4119-a99a-62957cd53edb_870x978.png)


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
