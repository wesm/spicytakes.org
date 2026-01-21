---
title: "Database Isolation Is Broken and You Should Care"
subtitle: "The database zeitgeist has decided that ANSI SQL '92 isn't enough. We need something better."
date: 2023-12-22T18:20:11+00:00
url: https://materializedview.io/p/database-isolation-is-broken-you-should-care
slug: database-isolation-is-broken-you-should-care
word_count: 731
---


This month saw several related posts onACID(atomicity,consistency,isolation,durability) database properties.


Tony Solomonikwrites a database usingbashin hisdatabase fundamentalspost. bashdb is a fascinating exercise that demonstrates why databases are so complex (ACID, fsync, B+ trees, LSMs, consensus, replication, and so on). Start here to brush up on the basics.


Next,Gwen Shapira, co-founder ofNile[$], postedTransaction Isolation in Postgres, explained. Though the headline says Postres, the post is mostly about database isolation levels (theIin ACID). She describes the various isolation levels inANSI SQL ‘92and shows the edge cases that break them.


![](https://substackcdn.com/image/fetch/$s_!SXPL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ce5c678-ea0c-4df9-b1d4-20fab2223350_1228x534.png)


Here’s where things get interesting. Gwen’s post says that there are many anomalies that aren’t classified in the ANSI SQL ‘92 spec.


> It turned out that defining a perfect state and then defining some states where certain anomalies can happen has this fundamental problem: There may be anomalies you didn't think of. So, only three years after the SQL92 standard came out, a very impressive team of researchers publishedA Critique of ANSI SQL Isolation Levels (1995). The paper introduced a whole collection of anomalies that weren't specified in the standard, and therefore were technically allowed at the Serializable level.


These new-found anomalies make database isolation ambiguous:


> Different databases support different isolation levels, and the same isolation level can mean different things in different databases.


This leads to the final post I want to call out:Jepsen’s MySQL Analysis. Jepsen is a project run by Kyle Kingsbury’s alter ego,Aphyr. Kyle and his team use Jepsen to break databases. Kyle andPeter Avlaro’s latest post finds anomalies with MySQL and Amazon RDS.


> We revisit Kleppmann’s 2014Hermitageand confirm that MySQL’s Repeatable Read still allows G2-item, G-single, and lost update. Using our transaction consistency checkerElle, we show that MySQL Repeatable Read also violates internal consistency. Furthermore, it violates Monotonic Atomic View: transactions can observe some of another transaction’s effects, then later fail to observe other effects of that same transaction. We demonstrate violations of ANSI SQL’s requirements for Repeatable Read.


Similar to Gwen’s post, they find anomalies and that don’t adhere to the ANSI SQL ‘92 spec. But the behavior they find is much worse than PostgreSQL’s behavior. If you’re using MySQL, I recommend reading the post; they provide suggestions to mitigate some of the issues.


What caught my eye was their plea to the standards bodies:


![](https://substackcdn.com/image/fetch/$s_!u1xr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f8170b4-97c8-4441-8505-e9100af038a6_1590x952.png)


Jepsen’s call for better isolation levels mirror Gwen’s. ANSI ‘92 database isolation levels clearly aren’t cutting it.


I assume you’re not part of the standards body, so your takeaway is that your database might not be behaving as you expect. But do you care?This threadsays you don’t.


![](https://substackcdn.com/image/fetch/$s_!B91L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80eb7675-8db0-4379-8616-b88846c3caac_1372x242.png)


Justin’s point is that we’ve been living with these “broken” databases for a long time and no one noticed.


> that said: it took one of the greatest software minds of a generation to prove that one of the most popular databases of all time was broken. kind of calls into question whether anyone ever cared about that brokenness!


The problem I have with Justin’s argument is that the kinds of anomalies in these posts are hard for developers to complain about. They manifest themselves only very occasionally and are very difficult to detect.


Developers that are bitten by database anomalies often don’t know. Applications exhibit some weird anomaly, which developers can’t reproduce. Engineers throw up their hands, shrug, and move on. They never even know the database was the culprit.


I have seen bugs like these while working on paymentsmy last job. Payments processing is a very precise thing (indeed, it’s the example Gwen uses in her post and is whatdurable execution frameworksalways demonstrate). Our double entry book keeping log would no longer line up, databases would misalign, or some other oddity would occur. Such bugs resulted in hours of fruitless debugging and unhappy customers. These are things that I, and many engineers, most definitely do care about.


Jepsen is doing us a favor by showing us that the almighty OLTP database is in fact fallible. Make sure you understand how your database behaves (as best you can) and act accordingly. Caveat emptor.


---


Share


---


You can support me by purchasingThe Missing README: A Guide for the New Software Engineerfor yourself or gifting it to new software engineers that you know.


Buy Now


---


I occasionally invest in infrastructure startups. Companies that I’ve invested in are marked with a [$] in this newsletter. See myLinkedIn profilefor a complete list.
