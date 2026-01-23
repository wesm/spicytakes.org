---
title: "Migrate from Oracle to Microsoft (Views) â Part II09-24"
date: 2016-09-24
url: https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-ii/
slug: migrate-from-oracle-to-microsoft-views-part-ii
word_count: 338
---

![Migrate from Oracle to Microsoft (Views) â Part II](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-ii/images/microsoft-sql-server-vs-oracle.jpg)

Contents

Continued from [Migrate from Oracle to Microsoft (Views) â Part I](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-i/)Â here part II with more focus on the performance part.


## Performance issues recursive queries


When it comes to performance I had one big issue with the built-in functionÂ `SYS_CONNECT_BY_PATH` which is used for rekursiv queries in Oracle. This function is well know by the Oracle optimizer which makes this function unbelievable fast and there is no similar function on SQL Server. Even more complex was, that this queries was used on nested views, so the SQL was quite complex.


I started to translate it to an [CTE view ](https://msdn.microsoft.com/en-us/library/ms175972.aspx)which is the pendant in SQL server and the answer to recursive queries in SQL Server. But I ended up having big performance issues because the queries where to complex. I had good performance measures on an easy simple query but invinitive response with more complex.


So what’s the solution to that?

**[Inline User-Defined Functions](https://msdn.microsoft.com/en-us/library/ms189294.aspx)**. Of course it will rise the complexity to one more level, but in my case it solve the performance issue from not responding to 1-5 second each view. At the mostÂ complex views, IÂ had to create a normal function where I created temp-tables inside to boost the performance even more, for example if there where a recursive query on a complex query, then I stored this complex query to a temp table and queried recursively on this temp-table. With this the complexity for the recursive query disappeared and that made it so fast. At the end I created the view on top of this function. Means there wasn’t any difference to see for the users nor applications.


**Links**:

- [[https://msdn.microsoft.com/en-us/library/ms175972.aspx](https://msdn.microsoft.com/en-us/library/ms175972.aspx)](https://msdn.microsoft.com/en-us/library/ms175972.aspx)
- [[http://stackoverflow.com/questions/12971580/sys-connect-by-path-in-sql-server](http://stackoverflow.com/questions/12971580/sys-connect-by-path-in-sql-server)](http://stackoverflow.com/questions/12971580/sys-connect-by-path-in-sql-server)


Contact me if you want to see this views or just want to know more, I’m happy to help you.


Continue reading about testingÂ in my part III [Migrate from Oracle to Microsoft (Views) â Part III](https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-iii/).

[Discuss on Bluesky](https://bsky.app/search?q=domain%3A%20https://www.ssp.sh/blog/migrate-from-oracle-to-microsoft-views-part-ii/)
|
[Pay what you like](https://ko-fi.com/sspaeti)
|
[Microsoft](https://www.ssp.sh/tags/microsoft/)
[MSSQL](https://www.ssp.sh/tags/mssql/)
[ORA-SQL](https://www.ssp.sh/tags/ora-sql/)
[Oracle](https://www.ssp.sh/tags/oracle/)
