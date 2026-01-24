---
title: "Why Can’t Database Tables Index Themselves?"
date: 2006-07-18
url: https://blog.codinghorror.com/why-cant-database-tables-index-themselves/
slug: why-cant-database-tables-index-themselves
word_count: 365
---

Here’s a thought question for today: **why can’t database tables index themselves?**


Obviously, indexes are a central concept to databases and database performance. But horror tales still abound of naïve developers who “forget” to index their tables, and encounter massive performance and scalability problems down the road as their tables grow. I’ve run into it personally, and I’ve read plenty of other sad tales of woe from other developers who have, too. I’ve also forgotten to build indexes myself on non primary key columns many times. Why aren’t databases smart enough to automatically protect themselves from this?


It always struck me as absurd that I had to go in and manually mark fields in a table to be indexed. Perhaps in the bad old file-based days of FoxPro, DBase, and Access, that might have been a necessary evil. But in a modern client-server database, the server should be aware of all the queries flowing through the system, and how much each of those queries cost. **Who better to decide what needs to be indexed than the database itself?**


Why can’t you enable an automatic indexing mode on your database server that follows some basic rules, such as...

1. Does this query result in a table scan?
2. If so, determine which field(s) could be indexed, for that particular query, to remove the need for a table scan.
3. Store the potential index in a list. If the potential index already exists in the list, bump its priority.
4. After (some configurable threshold), build the most commonly needed potential index on the target table.


Of course, for database gurus who are uncomfortable with this, the feature could be disabled. And you could certainly add more rules to make it more robust. But for most database users, it should be enabled by default; **an auto-indexing feature would make most database installations almost completely self-tuning** with no work at all on their part.


I did some cursory web searches and I didn’t see any features like this for any commercial database server. What am I missing here? Why does this seem so obvious, and yet it’s not out there?

[indexes](https://blog.codinghorror.com/tag/indexes/)
[database performance](https://blog.codinghorror.com/tag/database-performance/)
[database management](https://blog.codinghorror.com/tag/database-management/)
[database optimization](https://blog.codinghorror.com/tag/database-optimization/)
[database indexing](https://blog.codinghorror.com/tag/database-indexing/)
