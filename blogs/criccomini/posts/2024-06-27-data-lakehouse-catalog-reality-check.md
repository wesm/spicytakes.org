---
title: "Data Lakehouse Catalog Reality Check"
subtitle: "Databricks and Snowflake are talking a big game. So far, they've given us empty Github repositories and rewrites."
date: 2024-06-27T19:16:36+00:00
url: https://materializedview.io/p/data-lakehouse-catalog-reality-check
slug: data-lakehouse-catalog-reality-check
word_count: 538
---


Ibegan my serieson data lakehouse catalogs just last week and the newskeeps rolling in. This week, Fivetran announced theirmanaged data lake service, and Onehouseannounced$35 million in series B funding.


In this post, I want to take a look atUnityandPolaris, the open source catalogs thatDatabricksandSnowflakerecently announced. Both vendors launched their catalogs to great fanfare. Unfortunately, the marketing doesn’t yet seem to live up to reality.


Before continuing, readers should know that I owned Tabular shares. I don’t have any particular visibility into Databricks or Tabular’s product strategy, and I’ve tried to be as fair as possible in this post.


Snowflake has produced a greatproduct landingpage andblog post. I naively assumed that the project was, in fact, released—they link to a Github repo. A friend recently asked me, “Yes, but have you looked at the code?” This isthe code.


![](https://substackcdn.com/image/fetch/$s_!3Rm_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4c3f7ab-0cc1-4949-a8ab-af6ace170605_904x207.png)


On further inspection, Snowflake’s blog post does mention that developers should watch the Github repository to be notified when the code is released. I missed this. But I expected a bit more here, especially given the amount of marketing copy they’ve invested in.


Very quickly afterwards, Databricks announced Unity. Again, I was quite excited.


![](https://substackcdn.com/image/fetch/$s_!Qtvo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07b6291a-710e-465d-8da2-978bbf821ab5_693x467.png)


My excitement has waned.As it turns out,Unityis notUnity. Databricks open sourced anAPI-compatible rewrite of their product. And it sounds like it’s missing quite a bit.Sem Sinchenkobreaks down the features inUnitycatalog: the first look:


> At the time of this writing, Unitycatalog looks more like a proof of concept or MVP than a production-ready solution. There are no audit capabilities, no external RDBMS persistent storage support. All ML/AI governance features are currently missing. Big questions were raised about the lack of support for hive-style partitioning.


Shortly after all of this,I came acrossunity-rs. Yes, we’ve now gotanotherUnity rewrite, this time in Rust. The projectexplains why it needs to exist. I don’t have a strong position on their points, but theirserver codecaught my eye.


![](https://substackcdn.com/image/fetch/$s_!XNNr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5aadd92-476c-43a1-a225-e0c9306438b0_1240x259.png)


Deja vu. Out of all of these announcements, all this marketing, and all this noise, we’ve gotten one partial re-write, one empty Github project, and one hello world Rust file.


All of thisbothers me a lot less than it used to. Ibelieveunity-rs will get written, that Polaris will be released, and that Databricks will invest in Unity. In Databricks’s defense, it’soften hardto extricate internal projects. A rewrite is often the right move.


But it’s pretty strange to watch all of this play out. It appears the vendors have gotten ahead of themselves. I’m not even sure they all understand why they’re open sourcing these projects. I’d love to see someone write down their data lakehouse strategy, or at least do a better job of communicating what the end state of all this is. Right now it looks like flailing.


Other posts in this series are available here:

[Begun, The Catalog Wars HaveChris Riccomini·June 20, 2024Read full story](https://materializedview.io/p/begun-the-catalog-wars-have)
[Make Lakehouse Catalogs Boring AgainChris Riccomini·July 3, 2024Read full story](https://materializedview.io/p/make-lakehouse-catalogs-boring-again)

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
