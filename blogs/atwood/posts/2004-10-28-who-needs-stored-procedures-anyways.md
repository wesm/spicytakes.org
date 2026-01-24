---
title: "Who Needs Stored Procedures, Anyways?"
date: 2004-10-28
url: https://blog.codinghorror.com/who-needs-stored-procedures-anyways/
slug: who-needs-stored-procedures-anyways
word_count: 941
---

It’s intended as sarcasm, but I believe this [Daily WTF entry on Stored Procedures](https://web.archive.org/web/20040606043627/http://thedailywtf.com/archive/2004/05/25/153.aspx) should be taken at face value:


> *I’m sure we’ve all heard, over and over, that inline SQL is generally a bad practice, and that we should use Stored Procedures when possible. But let's be realistic for a minute. Who wants to write a stupid stored procedure for every stupid little simple query needed.*


Have you ever worked on a system where someone decreed* that **all database calls must be Stored Procedures, and SQL is strictly verboten?** I have, and this decision leads to incredible development pain:

1. Stored Procedures are written in big iron database “languages” like PL/SQL (Oracle) or T-SQL (Microsoft). These so-called languages are archaic, and full of the crazy, incoherent design choices that always result from the torturous evolution of ten years of backwards compatibility. You really don’t want to be writing a lot of code in this stuff. For context, JavaScript is a giant step up from PL/SQL or T-SQL.
2. Stored Procedures typically cannot be debugged in the same IDE you write your UI. Every time I isolate an exception in the procs, I have to stop what I am doing, bust out my copy of [Toad](http://www.quest.com/toad/), and load up the database packages to see what’s going wrong. Frequently transitioning between two totally different IDEs, with completely different interfaces and languages, is not exactly productive.
3. Stored Procedures don’t provide much feedback when things go wrong. Unless the proc is coded internally with weird T-SQL or PL/SQL exception handling, we get cryptic ‘errors’ returned based on the particular line inside the proc that failed, such as *Table has no rows*. Uh, ok?
4. Stored Procedures can’t pass objects. So, if you’re not careful, you can end up with a zillion parameters. If you have to populate a table row with 20+ fields using a proc, say hello to 20+ parameters. Worst of all, if I pass a bad parameter – either too many, not enough, or bad datatypes – I get a generic “bad call” error. Oracle can’t tell me which parameters are in error! So I have to pore over 20 parameters, by hand, to figure out which one is the culprit.
5. Stored Procedures hide business logic. I have no idea what a proc is doing, or what kind of cursor (DataSet) or values it will return to me. I can’t view the source code to the proc (at least, without resorting to #2 if I have appropriate access) to verify that it is actually doing what I think it is – or what the designer intended it to do. Inline SQL may not be pretty, but at least I can see it in context, alongside the other business logic.


So why use Stored Procedures at all? Conventional wisdom says we do it because:

- Stored procedures generally result in improved performance because the database can optimize the data access plan used by the procedure and cache it for subsequent reuse.
- Stored procedures can be individually secured within the database. A client can be granted permissions to execute a stored procedure without having any permissions on the underlying tables.
- Stored procedures result in easier maintenance because it is generally easier to modify a stored procedure than it is to change a hard-coded SQL statement within a deployed component.
- Stored procedures add an extra level of abstraction from the underlying database schema. The client of the stored procedure is isolated from the implementation details of the stored procedure and from the underlying schema.
- Stored procedures can reduce network traffic, because SQL statements can be executed in batches rather than sending multiple requests from the client.


And many people [buy into this philosophy](https://web.archive.org/web/20051107072329/http://weblogs.asp.net/rhoward/archive/2003/11/17/38095.aspx), lock stock and barrel:


> *At just about every talk I give I always try to make several consistent statements. One of which is: ‘Whenever possible use stored procedures to access your data.’*


However, there’s one small problem: **none of these things are true in practice**. The benefits are marginal, but the pain is substantial. And [I’m not the only person](http://weblogs.asp.net/fbouma/archive/2003/11/18/38178.aspx) that feels this way. [John Lam](https://web.archive.org/web/20041212183234/http://www.iunknown.com/000387.html) also adds:

kg-card-begin: html

> *As a guy who dabbles in low-level bit twiddling stuff from time-to-time, the performance claims are quite interesting to me. The new (as of SQL Server 7.0) cached execution plan optimization in SQL Server looks to me a lot like JIT compilation. If this is, in fact, the case it seems to me that the only overhead that would be associated with dynamic SQL would be:*
> The amount of bandwidth + time it takes to transmit the dynamic SQL text to the database.
> The amount of time it takes to calculate the hash of the dynamic SQL text to look up the cached execution plan.
> I can imagine quite a few scenarios where the above overhead would disappear into the noise of the network roundtrip. What upsets me are the folks who spout forth anecdotal arguments that claim stored procedures have “much better” performance than dynamic SQL.

kg-card-end: html

For modern databases and real world usage scenarios, I believe a Stored Procedure architecture has serious downsides and little practical benefit. **Stored Procedures should be considered database assembly language: for use in only the most performance critical situations**. There are plenty of ways to design a solid, high performing data access layer without resorting to Stored Procedures; you’ll realize a lot of benefits if you stick with parameterized SQL and a single coherent development environment.


*“the man.”

[stored procedures](https://blog.codinghorror.com/tag/stored-procedures/)
[inline sql](https://blog.codinghorror.com/tag/inline-sql/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[database development](https://blog.codinghorror.com/tag/database-development/)
[database management](https://blog.codinghorror.com/tag/database-management/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
