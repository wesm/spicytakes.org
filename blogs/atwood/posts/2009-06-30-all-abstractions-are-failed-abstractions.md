---
title: "All Abstractions Are Failed Abstractions"
date: 2009-06-30
url: https://blog.codinghorror.com/all-abstractions-are-failed-abstractions/
slug: all-abstractions-are-failed-abstractions
word_count: 1320
---

In programming, [abstractions are powerful things](https://web.archive.org/web/20170630005110/http://www.advogato.org/person/Bram/diary.html?start=43):

kg-card-begin: html

> Joel Spolsky has [an article](http://www.joelonsoftware.com/articles/LeakyAbstractions.html) in which he states
> *All non-trivial abstractions, to some degree, are leaky.*
> This is overly dogmatic - for example, bignum classes are exactly the same regardless of the native integer multiplication. Ignoring that, this statement is essentially true, but rather inane and missing the point. Without abstractions, all our code would be completely interdependent and unmaintainable, and abstractions do a remarkable job of cleaning that up. **It is a testament to the power of abstraction and how much we take it for granted that such a statement can be made at all**, as if we always expected to be able to write large pieces of software in a maintainable manner.

kg-card-end: html

But they can cause problems of their own. Let’s consider a particular [LINQ to SQL](http://msdn.microsoft.com/en-us/library/bb425822.aspx) query, designed to retrieve the most recent 48 Stack Overflow questions.

kg-card-begin: html

```

var posts =
(from p in DB.Posts
where
p.PostTypeId == PostTypeId.Question &&
p.DeletionDate == null &&
p.Score >= minscore
orderby p.LastActivityDate descending
select p).
Take(maxposts);

```

kg-card-end: html

The big hook here is that **this is code the compiler actually understands**. You get code completion, compiler errors if you rename a database field or mistype the syntax, and so forth. Perhaps best of all, you get an honest to goodness `post` object as output! So you can turn around and immediately do stuff like this:

kg-card-begin: html

```

foreach (var post in posts.ToList())
{
Render(post.Body);
}

```

kg-card-end: html

Pretty cool, right?


Well, that Linq to SQL query is functionally equivalent to this old-school SQL blob. More than functionally, **it is *literally* identical**, if you examine the SQL string that LINQ generates behind the scenes:

kg-card-begin: html

```

string query =
“select top 48 * from Posts
where
PostTypeId = 1 and
DeletionDate is null and
Score >= -4
order by LastActivityDate desc”;

```

kg-card-end: html

This text blob is of course totally opaque to the compiler. Fat-finger a syntax error in here, and you won’t find out about it until runtime. Even if it does run without a runtime error, processing the output of the query is awkward. It takes row level references and a lot of tedious data conversion to get at the underlying data.

kg-card-begin: html

```

var posts = DB.ExecuteQuery(query);
foreach (var post in posts.ToList());
{
Render(post[“Body”].ToString());
}

```

kg-card-end: html

So, LINQ to SQL is an abstraction – we’re **abstracting away raw SQL and database access in favor of native language constructs and objects**. I’d argue that Linq to SQL is a *good* abstraction. Heck, it’s exactly what I [asked for five years ago](https://blog.codinghorror.com/why-objects-suck/).


But even a good abstraction can break down in unexpected ways.


Consider this optimization, which is trivial in the old-school SQL blob code: instead of pulling down every single field in the post records, why not pull just the id number? Makes sense, if that’s all I need. And it’s faster – much faster!

kg-card-begin: html


|  |
| select top 48 * from Posts | 827 ms |
| select top 48 Id from Posts | 260 ms |


kg-card-end: html

Selecting all columns with the star (*) operator is expensive, and that’s what LINQ to SQL always does by default. Yes, [you can specify lazy loading](https://web.archive.org/web/20090803041357/http://mkdot.net/blogs/thearchitect/archive/2008/04/24/lazy-load-in-linq-to-sql.aspx), but not on a per-query basis. Normally, this is a non-issue, because selecting all columns for simple queries is not all *that* expensive. And you’d think pulling down **48 measly little post records** would be squarely in the “not expensive” category!


So let’s compare apples to apples. What if we got just the id numbers, then retrieved the full data for each row?

kg-card-begin: html


| select top 48 Id from Posts | 260 ms |
| select * from Posts where Id = 12345 | 3 ms |


kg-card-end: html

Now, retrieving 48 individual records one by one is sort of silly, because you could easily construct a single `where Id in (1,2,3..,47,48)` query that would grab all 48 posts in one go. But even if we did it in this naïve way, the total execution time is still a very reasonable (48 * 3 ms) + 260 ms = 404 ms. **That is *half* the time of the standard select-star SQL emitted by LINQ to SQL!**


An extra 400 milliseconds doesn’t sound like much, but [slow pages lose users](https://web.archive.org/web/20091006034220/http://radar.oreilly.com/2009/06/bing-and-google-agree-slow-pag.html). And why in the world would you perform a slow database query on every single page of your website when you don’t have to?


It’s tempting to blame Linq, but is Linq really at fault here? These seem like *identical* database operations to me:


> 1. Give me all columns of data for the top 48 posts.


or


> 1. Give me just the ids for the top 48 posts.
> 2. Retrieve all columns of data for each of those 48 ids.


So why in the wide, wide world of sports would one of these **seemingly identical operations** be twice as slow as the other?


The problem isn’t Linq to SQL. The problem is that **we’re attempting to spackle a nice, clean abstraction over a database that is full of highly irregular and unusual real world behaviors.** Databases that:

- may not have the right indexes
- may misinterpret your query and generate an inefficient query plan
- are trying to perform an operation that doesn’t fit well in available memory
- are paging data from disks which might be busy at that particular moment
- might contain irregularly sized column datatypes


That’s what’s so frustrating. We can’t just pretend all our data is formatted into neat, orderly data structures sitting there in memory, lined up in convenient little queues for us to reach out and casually scoop them up. As I’ve demonstrated, even trivial queries can have bizarre behavior and performance characteristics that are not at all clear.


To its credit, Linq to SQL is quite flexible: we can use strongly typed queries, or we can use SQL blob queries that we cast to the right object type. That flexibility is critical, because **so much of our performance depends on these quirks of the database**. We default to the built-in Linq language constructs, and drop down to hand-tuning ye olde SQL blobs where the performance traces tell us we need to.


Either way, it’s clear that you’ve *got* to know what’s happening in the database every step of the way to even begin understanding the performance of your application, much less troubleshoot it.


I think you could make a fairly solid case that Linq to SQL is, in fact, a leaky and failed abstraction. Exactly the kind of thing Joel was complaining about. But I’d also argue that **virtually *all* good programming abstractions are failed abstractions**. I don’t think I’ve ever used one that didn’t leak like a sieve. But I think that’s an awfully [architecture astronaut](https://blog.codinghorror.com/it-came-from-planet-architecture/) way of looking at things. Instead, let’s ask ourselves a more pragmatic question:


> Does this abstraction make our code at least a *little* easier to write? To understand? To troubleshoot? Are we better off *with* this abstraction than we were without it?


It’s our job as modern programmers not to abandon abstractions due to these deficiencies, but to embrace the useful elements of them, to adapt the working parts and construct ever so slightly *less* leaky and broken abstractions over time. Like desperate citizens manning a dike in a category 5 storm, **we programmers keep piling up these leaky abstractions, shoring up as best we can, desperately attempting to stay ahead of the endlessly rising waters of complexity.**


As much as I may curse Linq to SQL as yet another failed abstraction, I’ll continue to use it. Yes, I may end up soggy and irritable at times. But it sure as *heck* beats drowning.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[abstractions](https://blog.codinghorror.com/tag/abstractions/)
[abstraction leaks](https://blog.codinghorror.com/tag/abstraction-leaks/)
[linq to sql](https://blog.codinghorror.com/tag/linq-to-sql/)
