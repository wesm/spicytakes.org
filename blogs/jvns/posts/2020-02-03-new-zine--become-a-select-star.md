---
title: "New zine: Become a SELECT Star!"
date: 2020-02-03
url: https://jvns.ca/blog/2020/02/03/new-zine--become-a-select-star/
slug: new-zine--become-a-select-star
word_count: 460
---


On Friday I published a zine about SQL called “Become a SELECT Star!”


You can get it for $12 at [https://wizardzines.com/zines/sql](https://wizardzines.com/zines/sql). If you buy it, you’ll get a PDF that you can
either read on your computer or print out. You can also get a pack of [all 7 zines](https://wizardzines.com/zines/all-the-zines/) so far.


Here’s the cover and table of contents:


### why SQL?


I got excited about writing a zine about SQL because at my old job I
wrote a ton of SQL queries (mostly related to machine learning) and by doing that I learned there are a lot of weird
things about SQL! For example – [SQL queries don’t actually start with
SELECT](https://jvns.ca/blog/2019/10/03/sql-queries-don-t-start-with-select/).
And the way [NULL behaves isn’t really intuitive at
first](https://tweets.jvns.ca/b0rk/status/1195184321818243083).


It’s been really fun to go back and try to explain the basics of SQL from the
beginning. (what’s the difference between WHERE and HAVING? what’s the basic
idea with indexes actually? how do you write a join?)


I think SQL is a really nice thing to know because there are SO MANY SQL
databases out there, and some of them are super powerful! (like BigQuery and
Redshift). So if you know SQL and have access to one of these big data
warehouses you can write queries that crunch like 10 billion rows of data
really quickly.


### lots of examples


I ended up spending a lot of time on the examples in this zine, more than in
any previous zine. My friend [Anton](http://www.cat-bus.com/) helped me come up with a fun way to
illustrate them, where you can clearly see the query, the table it’s running
on, and what the query outputs. Like this:


![](https://jvns.ca/images/sql-diagram.png)


### experiment: include a SQL playground


All the examples in the zine are real queries that you can run. So I thought:
why not provide a simple environment where people can actually run those
queries (and variations on those queries) to try things out?


So I built a small [playground where you can run queries on the example
tables in the zine](https://sql-playground.wizardzines.com). It uses SQLite
compiled to web assembly, so all the queries run in your browser. It wasn’t too
complicated to build – I just used my minimal Javascript/CSS skills and vue.js.


I’d love to hear any feedback about whether this is helpful or not – the
example tables in the zine are really small (you can only print out small SQL
tables!), so the biggest table in the example set has 9 rows or something.


### what’s next: probably containers


I think that next up is going to be a zine on containers, which is more of a
normal systems-y topic for me. (for example: [namespaces](https://tweets.jvns.ca/b0rk/status/1195725346970181632), [cgroups](https://tweets.jvns.ca/b0rk/status/1214341831049252870), [why containers?](https://tweets.jvns.ca/b0rk/status/1224500774450929664))


Here’s a link to where to [get the zine](https://wizardzines.com/zines/sql) again :)
