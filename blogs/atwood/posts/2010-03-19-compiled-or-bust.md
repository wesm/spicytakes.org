---
title: "Compiled or Bust?"
date: 2010-03-19
url: https://blog.codinghorror.com/compiled-or-bust/
slug: compiled-or-bust
word_count: 1295
---

While I may have mixed emotions [toward LINQ to SQL](https://blog.codinghorror.com/all-abstractions-are-failed-abstractions/), we’ve had great success with it on Stack Overflow. That’s why I was [surprised to read the following](http://weblogs.asp.net/omarzabir/archive/2008/10/28/solving-common-problems-with-compiled-queries-in-linq-to-sql-for-high-demand-asp-net-websites.aspx):

kg-card-begin: html

> If you are building an ASP.NET web application that’s going to get thousands of hits per hour, the execution overhead of Linq queries is going to consume too much CPU and make your site slow. There’s a runtime cost associated with each and every Linq Query you write. The queries are parsed and converted to a nice SQL Statement on *every* hit. It’s not done at compile time because there’s no way to figure out what you might be sending as the parameters in the queries during runtime.
> So, if you have common Linq to Sql statements like the following one...
> var query = from widget in dc.Widgets
> where widget.ID == id && widget.PageID == pageId
> select widget;
> var widget = query.SingleOrDefault();
> ...  throughout your growing web application, you are soon going to have scalability nightmares.

kg-card-end: html

J.D. Conley [goes further](https://web.archive.org/web/20100324044721/http://www.jdconley.com/blog/archive/2007/11/28/linq-to-sql-surprise-performance-hit.aspx):


> So I dug into the call graph a bit and found out the code causing by far the most damage was the creation of the LINQ query object for every call! The actual round trip to the database paled in comparison.


I must admit, these results seem... unbelievable. Querying the database is so slow (relative to typical code execution) that if you have to ask how long it will take, *you can’t afford it*. I have a very hard time accepting the idea that **dynamically parsing a Linq query would take longer than round-tripping to the database.** Pretend I’m from Missouri: show me. Because I am unconvinced.


All of this is very curious, because Stack Overflow uses naïve, uncompiled Linq queries on every page, and we are a top 1,000 website on the public internet by most accounts these days. We get a considerable amount of traffic; the last time I checked it was about 1.5 million pageviews per day. We go to great pains to make sure everything is as fast as we can. We’re not as fast as we’d like to be yet, but I think we’re doing a reasonable job so far. The journey is still very much underway – we realize that [overnight success takes years](https://blog.codinghorror.com/overnight-success-it-takes-years/).


Anyway, **Stack Overflow has dozens to hundreds of plain vanilla uncompiled Linq to SQL queries on every page**. What we *don’t* have is “scalability nightmares.” CPU usage has been one of our least relevant constraints over the last two years as the site has grown. We’ve also heard from other development teams, multiple times, that Linq to SQL is “slow.” But we’ve never been able to reproduce this even when armed with a profiler.


Quite the mystery.


Now, it’s absolutely true that Linq to SQL has the performance peculiarity both posters are describing. We know that’s true because [Rico tells us so](https://web.archive.org/web/20100323013036/http://blogs.msdn.com/ricom/archive/2008/01/14/performance-quiz-13-linq-to-sql-compiled-query-cost-solution.aspx), and Rico... well, Rico’s *the man*.


> In short the problem is that **the basic Linq construction (we don’t really have to reach for a complex query to illustrate) results in repeated evaluations of the query if you ran the query more than once.**
> Each execution builds the expression tree, and then builds the required SQL. In many cases all that will be different from one invocation to another is a single integer filtering parameter. Furthermore, any databinding code that we must emit via lightweight reflection will have to be jitted each time the query runs. Implicit caching of these objects seems problematic because we could never know what good policy is for such a cache – only the user has the necessary knowledge.


It’s fascinating stuff; you should [read the whole series](https://web.archive.org/web/20100330060801/http://blogs.msdn.com/ricom/archive/2007/06/22/dlinq-linq-to-sql-performance-part-1.aspx).


What’s unfortunate about Linq in this scenario is that you’re intentionally sacrificing something that any [old and busted SQL database](https://web.archive.org/web/20100324000745/http://www.yafla.com/dforbes/Getting_Real_about_NoSQL_and_the_SQL_Isnt_Scalable_Lie/) gives you for free. When you send a garden variety parameterized SQL query through to a traditional SQL database, it’s hashed, then matched against existing cached query plans. The computational cost of pre-processing a given query is only paid the first time the database sees the new query. All subsequent runs of that same query use the cached query plan and skip the query evaluation. Not so in Linq to SQL. As Rico said, **every single run of the Linq query is fully parsed every time it happens**.


Now, there *is* a way to compile your Linq queries, but I personally find the syntax kind of... ugly and contorted. You tell me:

kg-card-begin: html

```

Func<Northwinds, IQueryable<Orders>, int> q =
CompiledQuery.Compile<Northwinds, int, IQueryable<Orders>>
((Northwinds nw, int orderid) =>
from o in nw.Orders
where o.OrderId == orderid
select o );
Northwinds nw = new Northwinds(conn);
foreach (Orders o in q(nw, orderid))
{
}

```

kg-card-end: html

Anyway, that’s neither here nor there; we can confirm the performance penalty of failing to compile our queries ourselves. We recently wrote a one time conversion job against a simple 3 column table containing about 500,000 records. The meat of it looked like this:

kg-card-begin: html

```

db.PostTags.Where(t => t.PostId == this.Id).ToList();

```

kg-card-end: html

Then we compared it with the SQL variant; note that this is also being auto-cast down to the handy `PostTag` object as well, so the only difference is whether or not the query itself is SQL.

kg-card-begin: html

```

db.ExecuteQuery(
“select * from PostTags where PostId={0}”, this.Id).ToList();

```

kg-card-end: html

On an Intel Core 2 Quad running at 2.83 GHz, the former took **422 seconds** while the latter took **275 seconds**.


The penalty for failing to compile this query, across 500k iterations, was 147 seconds. Wow! That’s 1.5 times slower! Man, only a *BASIC programmer* would be dumb enough to skip compiling all their Linq queries. But wait a second, no, wait 147 seconds. Let’s do the math, even though I suck at it. Each uncompiled run of the query took less than ***one third of a millisecond*** longer.


At first I was worried that every Stack Overflow page was 1.5 times slower than it should be. But then I realized it’s probably more realistic to make sure that any page we generate isn’t doing **500 freakin’ thousand queries!** Have we found ourselves in [the sad tragedy of micro-optimization theater](https://blog.codinghorror.com/the-sad-tragedy-of-micro-optimization-theater/)... again? I think we might have. Now I’m just depressed.


While it’s arguably correct to say that every compiled Linq query (or for that matter, any compiled anything) will be faster, your decisions should be a bit more nuanced than **compiled or bust**. How much benefit you get out of compilation depends how many times you’re doing it. Rico would be the first to point this out, and in fact he already has:

kg-card-begin: html

```

Testing 1 batches of 5000 selects

uncompiled  543.48 selects/sec
compiled    925.75 selects/sec

Testing 5000 batches of 1 selects

uncompiled  546.03 selects/sec
compiled    461.89 selects/sec

```

kg-card-end: html

Have I mentioned that Rico is the man? Do you see the inversion here? Either you’re doing 1 batch of 5000 queries, or 5000 batches of 1 query. One is dramatically faster when compiled; the other is actually a big honking net negative if you consider the developer time spent converting all those beautifully, wonderfully simple Linq queries to the contorted syntax necessary for compilation. Not to mention the implied code maintenance.


I’m a big fan of compiled languages. Even Facebook will tell you that PHP is about as half as fast [as it should be](https://web.archive.org/web/20100320014228/http://developers.facebook.com/news.php?story=358&blog=1) on a good day with a tailwind. But compilation alone is not the entire performance story. Not even close. If you’re compiling something – whether it’s PHP, a regular expression, or a Linq query, don’t expect [a silver bullet](http://en.wikipedia.org/wiki/No_Silver_Bullet), or you may end up disappointed.

[linq](https://blog.codinghorror.com/tag/linq/)
[sql](https://blog.codinghorror.com/tag/sql/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[performance](https://blog.codinghorror.com/tag/performance/)
[scalability](https://blog.codinghorror.com/tag/scalability/)
