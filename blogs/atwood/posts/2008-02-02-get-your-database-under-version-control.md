---
title: "Get Your Database Under Version Control"
date: 2008-02-02
url: https://blog.codinghorror.com/get-your-database-under-version-control/
slug: get-your-database-under-version-control
word_count: 343
---

A little over a year ago, I wrote about the importance of [version control for databases](https://blog.codinghorror.com/is-your-database-under-version-control/).


> When I ask development teams whether their database is under version control, I usually get blank stares.
> The database is a critical part of your application. If you deploy version 2.0 of your application against version 1.0 of your database, what do you get? A broken application, that’s what. That’s why **your database should always be under source control, right next to your application code**. You deploy the app, and you deploy the database. Like peanut butter and chocolate, they are two great tastes that taste great together.


![](https://blog.codinghorror.com/content/images/2025/03/image-447.png)


When it comes to version control, the database is often a second or even third-class citizen. From what I’ve seen, teams that would *never* think of writing code without version control in a million years – and rightly so – can somehow be completely oblivious to the need for version control around the critical databases their applications rely on. I don’t know how you can call yourself a software engineer and maintain a straight face when your database isn’t under *exactly* the same rigorous level of source control as the rest of your code. Don’t let this happen to you. **Get your database under version control**.


I was thinking about this again because my friend [and co-author](https://blog.codinghorror.com/do-not-buy-this-book/) K. Scott Allen just wrote a brilliant five part series on the philosophy and practice of database version control:

1. [Three rules for database work](http://odetocode.com/Blogs/scott/archive/2008/01/30/11702.aspx)
2. [The Baseline](http://odetocode.com/Blogs/scott/archive/2008/01/31/11710.aspx)
3. [Change Scripts](http://odetocode.com/Blogs/scott/archive/2008/02/02/11721.aspx)
4. [Views, Stored Procedures and the Like](http://odetocode.com/Blogs/scott/archive/2008/02/02/11737.aspx)
5. [Branching and Merging](http://odetocode.com/Blogs/scott/archive/2008/02/03/11746.aspx)


K is one of the smartest software developers I know. Read it all; even if you currently have your database under version control (and bully for you if you do), there is much food for peanut buttery chocolatey thought here. It **doesn’t matter what tools you use –** per the [agile manifesto](http://agilemanifesto.org/), *individuals and interactions are more important than processes and tools*. Just get your database under version control already.

[database management](https://blog.codinghorror.com/tag/database-management/)
[version control](https://blog.codinghorror.com/tag/version-control/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
