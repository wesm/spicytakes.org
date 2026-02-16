---
title: "ORDER BY Oracle vs. Microsoft SQL"
date: 2015-09-19
url: https://www.ssp.sh/blog/order-by-oracle-vs-microsoft-sql/
slug: order-by-oracle-vs-microsoft-sql
word_count: 86
---

![ORDER BY Oracle vs. Microsoft SQL](https://www.ssp.sh/blog/order-by-oracle-vs-microsoft-sql/images/Capture2.png)

Contents

Like you would think ORDER BY is the same in Oracle as in the Microsoft environment, it isn’t. It depends on the Collation of the database. In the following example you see, that two manually added text in Oracle and Microsoft don’t order the same. After I added the Collation for SQL_Latin1_General_CP850_BIN2, it ordered the same.


`ORDER BY` Oracle:


`ORDER BY` Microsoft - normal and with collation:

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/order-by-oracle-vs-microsoft-sql/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Microsoft](https://www.ssp.sh/tags/microsoft/)
[MSSQL](https://www.ssp.sh/tags/mssql/)
[Oracle](https://www.ssp.sh/tags/oracle/)
