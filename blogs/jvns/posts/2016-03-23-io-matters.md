---
title: "I/O matters."
date: 2016-03-23
url: https://jvns.ca/blog/2016/03/23/io-matters/
slug: io-matters
word_count: 343
---


Here’s another missive from the series “what Julia learned today at work”.


Today I was running a Redshift query, and it was slow. Redshift is this database-as-a-service from Amazon and so far my experience with it is that it is MAGICAL and AMAZING. You can do huge joins & aggregations between huge tables and it’s fast and it works.


But not this query! This query was slow. I’d been querying this table, for months and it had been slow for months. Finally I was like “well, there has to be a reason why it’s slow”. I asked my awesome coworker Jeff what was up.


Now, Redshift is a columnar database (unlike sqlite/mysql/postgres). This means that it stores the data from each column together on disk, so if you have a 900GB table, but the column you want is only 1GB of data, then you only need to read 1GB. This is amazing when you have wide tables that you only want to query a few columns from, which is the situation I’m in most of the time.


So, back to my table. I was querying a string column. That string column, on disk, was taking up ~100GB of space. This means that every time I queried, it had to read 100GB from disk (modulo disk caches). That’s a lot! Jeff turned on compression and told Redshift that the column was a `varchar(255)` instead of a `varchar(65536)`. My queries got way faster.


### i/o doesn’t go away because you’re in The Cloud


With these Magical Cloud Services it can sometimes be hard to remember that your data is just living on real computers somewhere, with real disks, and you’re still bound by the normal limits of I/O. Having less data on disk will mean you have to do less I/O, and make your queries faster! That’s how disks work =D


This is one of these super obvious things (of *course* Magical Cloud Things are just computers and are bound by the normal laws of computers!), but I’m happy every time I’m reminded of it.
