---
title: "Primary Keys: IDs versus GUIDs"
date: 2007-03-19
url: https://blog.codinghorror.com/primary-keys-ids-versus-guids/
slug: primary-keys-ids-versus-guids
word_count: 285
---

Long-time readers of this blog know that I have [an inordinate fondness for GUIDs](https://blog.codinghorror.com/mastering-guids-with-occams-razor/). Each [globally unique ID](http://en.wikipedia.org/wiki/Globally_Unique_Identifier) is like a beautiful snowflake: every one a unique item waiting to be born.


Perhaps that’s why I read with great interest recent accounts of people switching their database tables from traditional integer primary keys...

kg-card-begin: html

```

ID  Value
--  -----
1   Apple
2   Orange
3   Pear
4   Mango

```

kg-card-end: html

... to GUID keys.

kg-card-begin: html

```

ID                                    Value
------------------------------------  -----
C87FC84A-EE47-47EE-842C-29E969AC5131  Apple
2A734AE4-E0EF-4D77-9F84-51A8365AC5A0  Orange
70E2E8DE-500E-4630-B3CB-166131D35C21  Pear
15ED815C-921C-4011-8667-7158982951EA  Mango

```

kg-card-end: html

I know what you’re thinking. *Using sixteen bytes instead of four bytes for a primary key? Have you lost your mind?* Those additional 12 bytes do come at a cost. But that cost may not be as great as you think:

- [The Cost of GUIDs as Primary Keys](http://www.informit.com/articles/printerfriendly.asp?p=25862&rl=1) (SQL Server 2000)
- [Myths, GUID vs. Autoincrement](http://krow.livejournal.com/497839.html) (MySQL 5)


Using a GUID as a row identity value feels more natural – and certainly more truly unique – than a 32-bit integer. Database guru Joe Celko [seems to agree](http://groups.google.com/group/microsoft.public.sqlserver.programming/msg/6d61dbf80d6f0fb6?hl=en&lr=&ie=UTF-8&oe=UTF-8&rnum=14). GUID primary keys are a natural fit for many development scenarios, such as replication, or when you need to generate primary keys outside the database. But it’s still a question of balancing the tradeoffs between traditional 4-byte integer IDs and 16-byte GUIDs:

kg-card-begin: html


|  |


kg-card-end: html

I’m not proposing that every database switch to GUID primary keys, but I do think it’s important to know the option is out there. If you’re still on the fence, [What should I choose for my primary key?](http://web.archive.org/web/20150511162734/http://databases.aspfaq.com/database/what-should-i-choose-for-my-primary-key.html) has excellent advice and a solid analysis of the tradeoffs.

[uuids](https://blog.codinghorror.com/tag/uuids/)
[primary keys](https://blog.codinghorror.com/tag/primary-keys/)
[database design](https://blog.codinghorror.com/tag/database-design/)
[guids](https://blog.codinghorror.com/tag/guids/)
[sql server](https://blog.codinghorror.com/tag/sql-server/)
