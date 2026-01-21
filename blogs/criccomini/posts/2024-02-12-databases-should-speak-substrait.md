---
title: "Databases Should Speak Substrait"
subtitle: "It's silly to have applications generate text-based SQL; they should be allowed to pass query plans to the database."
date: 2024-02-12T11:20:11+00:00
url: https://materializedview.io/p/databases-should-speak-substrait
slug: databases-should-speak-substrait
word_count: 435
---


High winds during the bay area storm last week woke me up at 3am. While drifting back to sleep, I had an idea: databases should acceptsubstraitquery plans directly, rather than forcing users to provide text-based SQL queries.


![](https://substackcdn.com/image/fetch/$s_!Rbm5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6a7107c9-3e4f-4b1d-ba43-93f2730d2f85_688x172.png)

*View Tweet*


Application code currently useobject-relation mappings(ORMs) andfluent query buildersto generate text SQL. The text query is sent to the database over the wire. Databases then parse the text using a language frontend. The frontend converts the query into an intermediate representation (IR).Velox'sintroduction videohas a nice visualization of this:


![](https://substackcdn.com/image/fetch/$s_!sfNI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37fedbf3-6f89-498e-a1e9-f39dd0dcda57_738x332.png)


SQL is built for humans. Machines are much better at generating structured messages. This is (one of) the reasons that developers use ORMs and query builders instead of concatenating text strings. You get type safety, testing, and other niceties.


Under the hood, query builders are all generating text SQL right now. I’ve always found this strange.


![](https://substackcdn.com/image/fetch/$s_!ARAn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe220b068-52a3-4ad8-9e70-5cbde3061750_692x191.png)


ORMs and query builders should be able to go straight to the IR (ORM → IR → wire). This would open up a few new possibilities:

1. Databases could support multiple query languages with different frontends (SQL,PRQL,Malloy,LLM-based plaintext queries, and so on)
2. Text parsing overhead would be eliminated.NOTE: Intuitively, it seems that encoding and parsing the IR should be faster than text parsing. IRs might be a larger payload than text-based SQL, though. It’s hard for me to be certain about performance tradeoffs between parsing and network.
3. Programmatic database access would become a first-class citizen. Fluent queries, ORMs, and DataFrame APIs could all directly interface with the database without having to use text-based SQL queries.


The tools already exist to do this. Substrait defines a standard set of compute operations. Applications can definelogical relationslike joins, filters, and sorts. Databases should accept substrait queries over the wire, and client libraries (ORMs, query builders, and DataFrame APIs) should generate and send substrait queries.


It appears that this is already happening in the data warehousing. Kudusupports adaptersto generate queries.Spark connecttranslates DataFrame API calls directly into logical parse plans.


![Spark Connect communication](https://substackcdn.com/image/fetch/$s_!SWHO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd4f0300-0a6d-41cc-bf58-99e07a5cb3fb_3454x1940.png)


My favorite example is DuckDB, which has asubstrait extensionto interoperate with substrait. You can generate substrait query plans using `generate_substrait`, or you can also pass in query plans using `CALL from_substrait()`.


Surprisingly, I haven’t found any support for substrait in the OLTP space. (TiDBdoes havean open Github issue.) It makes sense to use substrait query plans for DataFrame APIs, but I expected ORMs and fluent queries to be a more natural starting point. Imagine if PostgreSQL had a `from_substrait()` extension. ORMs and fluent query builders likePrismaandHibernatecould generate substrait query plans and send them straight to PostgreSQL. Someone should build this.
