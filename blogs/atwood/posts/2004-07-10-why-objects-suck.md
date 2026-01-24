---
title: "Why Objects Suck"
date: 2004-07-10
url: https://blog.codinghorror.com/why-objects-suck/
slug: why-objects-suck
word_count: 514
---

There’s been a lot of discussion recently about the [Object to Relational mapping problem](http://en.wikipedia.org/wiki/Object-relational_mapping), which is a serious one. This [Clemens Vasters blog entry](https://web.archive.org/web/20051219154745/http://staff.newtelligence.net/clemensv/PermaLink.aspx?guid=8a119c62-2fc1-4409-9ae4-0b250fdb785b) summarizes it best:


> Maybe I am too much of a data (read: XML, Messages, SQL) guy by now, but **I just lost faith that objects are any good on the “business logic” abstraction level**. The whole inheritance story is usually refactored away for very pragmatic reasons and the encapsulation story isn’t all that useful either.
> What you end up with are elements and attributes (infoset) for the data that flows across, services that deal with the data that flows, and rows and columns that efficiently store data and let you retrieve it flexibly and quickly. Objects lost (except on the abstract and conceptional analysis level where they are useful to understand a problem space) their place in that picture for me.


A follow-up from [Steve Maine’s blog](https://web.archive.org/web/20051126230310/http://hyperthink.net/blog/PermaLink,guid,22728ae4-a1d4-4fa7-b8fd-757640112d06.aspx) elaborates a bit:


> A typical business problem is the converse of a typical object-oriented problem. Business problems are generally interested in a very limited set of operations (CRUD being the most popular). These operations are only as polymorphic as the data on which they operate. The Customer.Create() operation is really no different behaviorally than Product.Create() (if Product and Customer had the same name, you could reuse the same code modulo stored procedure or table name), however the respective data sets on which they both operate are likely to be vastly different. As collective industry experience has shown, handing polymorphic data with language techniques optimized for polymorphic behavior is tricky at best. Yes, it can be done, but it requires fits of extreme cleverness on the part of the developer. **Often those fits of cleverness turn into fugues of frustration because the programming techniques designed to reduce complexity have actually compounded it.**


All I can say to the above is, I concur. We’ve concluded the same thing in a few projects at work. We started with naive Object implementations, and then scaled back – purely for reasons of simplicity – to passing around raw DataSets. As one of my co-workers said:


> At first you’re like “whee! objects!” and then you realize – hey, this is a lot of tedious, error-prone mapping code I didn’t have to write before...


I’ve always maintained that the IDE should be able to support named dot-style access to the database and tables, which it automatically absorbs from the database schema behind the scenes. I know we have Typed Datasets, but those are not transparent and certainly not automatic. So instead of this syntax, which raises the hackles of SmallTalk fans worldwide:

kg-card-begin: html

```
ds.Tables("Customers").Rows(1).Item("FirstName")
```

kg-card-end: html

We could use this syntax:

kg-card-begin: html

```
ds.Customers.Customer(1).FirstName
```

kg-card-end: html

Again, this is only useful if it is **completely automatic in the IDE, with intellisense support – that is, zero code required from the developer!** It also would force you to have a clean schema design for your DB, which can’t be a bad thing.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
[relational mapping](https://blog.codinghorror.com/tag/relational-mapping/)
[abstraction](https://blog.codinghorror.com/tag/abstraction/)
[data management](https://blog.codinghorror.com/tag/data-management/)
