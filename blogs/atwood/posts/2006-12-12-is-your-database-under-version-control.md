---
title: "Is Your Database Under Version Control?"
date: 2006-12-12
url: https://blog.codinghorror.com/is-your-database-under-version-control/
slug: is-your-database-under-version-control
word_count: 591
---

When I ask development teams whether their database is under version control, I usually get blank stares.


The database is a critical part of your application. If you deploy version 2.0 of your application against version 1.0 of your database, what do you get? A broken application. And that’s why **your database should always be under source control right next to your application code**. You deploy the app, and you deploy the database. Like peanut butter and chocolate, they are two great tastes that taste great together.


At Vertigo, we rolled our own tool to reverse engineer the database into a set of files, which we then check into source control. I’ve visited other customers that did the same thing. But why write what you can buy? Leon Bambrick lists [a number of great tools](http://secretgeek.net/dbcontrol.asp) you can purchase to help you in get your database under version control where it belongs. Unfortunately, he omitted one of the best tools: Microsoft’s new [Team Edition for Database Professionals](https://web.archive.org/web/20061216094550/http://msdn2.microsoft.com/en-us/teamsystem/aa718807.aspx).


![](https://blog.codinghorror.com/content/images/2025/05/image-443.png)


Team Edition for Database Professionals goes far beyond mere reverse engineering of the database into files. You get an industrial-strength database project that you can add to your solution, along with a few other goodies:

- **Create test data.** A blank database schema isn’t particularly useful to develop against. Now you can distribute your database schema along with one-click synthetic data generation plans. With flexible synthetic data generators, you can avoid dumping production data to developers, or, God forbid, letting developers fend for themselves by creating their own test data. And you can generate 1,000 rows or 100,000 rows. I wish I had a dollar every time an application I’ve worked on began to have performance problems because none of the developers had the foresight to test the app with more than a few rows of crappy, manually entered test data. Data generation is a *huge* increase in development quality.
- **Schema comparison**. If we can compare two files in source control, why can’t we compare two tables? A robust schema comparison tool is essential. Not sure why staging is different than production? Run a quick schema compare on ’em. Did I mention it also creates a real-time update script every time you do a comparison... which it can execute with one additional click?
- **Data comparison**. If your testers are complaining because they entered test data that causes your application to crash, run the data compare tool to determine exactly how their data differs from yours.
- **Database unit testing**. If you make a change to the database schema, how do you know if you’ve broken any applications that rely on that database? You know because you’ve written unit tests that validate the database. Right? *Right?*
- **Refactoring**. You can rename entities in the database (columns, tables, procs, etc.) and have the rename automatically cascade throughout the database.
- **Integrated T-SQL editor**. T-SQL is now a first class language construct in the IDE, just like C# and VB.NET. Run queries and view execution plans and stats, all without leaving the cozy confines of good old Visual Studio.


It’s a great tool... if you’re a Microsoft shop, and you're using SQL Server. I highly recommend downloading the trial edition. But the specifics of the tool aren’t important; **get your database under version control by any means necessary**. Making your database a first-class citizen in source control seems totally obvious in retrospect. Now if only we could convince more developers to actually do it.

[database management](https://blog.codinghorror.com/tag/database-management/)
[version control](https://blog.codinghorror.com/tag/version-control/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[database tools](https://blog.codinghorror.com/tag/database-tools/)
[microsoft technologies](https://blog.codinghorror.com/tag/microsoft-technologies/)
