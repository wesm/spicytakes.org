---
title: "Deadlocked!"
date: 2008-08-24
url: https://blog.codinghorror.com/deadlocked/
slug: deadlocked
word_count: 1485
---

You may have noticed that my posting frequency has declined over the last three weeks. That’s because I’ve been busy building [that Stack Overflow thing](https://blog.codinghorror.com/introducing-stackoverflow-com/) we talked about.


It’s going well so far. Joel Spolsky also seems to think [it’s going well](http://www.joelonsoftware.com/items/2008/08/21.html), but he’s one of the founders so he’s *clearly* biased. For what it’s worth, Robert Scoble was [enthused about Stack Overflow](http://scobleizer.com/2008/08/11/pr-less-launch-kicks-off-a-stack-overflow-of-praise/), though it did not [make him cry](http://scobleizer.com/2008/02/27/what-made-me-cry-microsofts-world-wide-telescope/). Still, I was humbled by the way Robert picked this up so enthusiastically through the community. I hadn’t contacted him in any way; I myself only found out about his reaction third hand.


That’s not to say everything has been copacetic. One major surprise in the development of Stack Overflow was this recurring and unpredictable gem:


> Transaction (Process ID 54) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction.


[Deadlocks](http://en.wikipedia.org/wiki/Deadlock) are a classic computer science problem, often taught to computer science students as [the Dining Philosophers puzzle](https://blog.codinghorror.com/classic-computer-science-puzzles/).


![](https://blog.codinghorror.com/content/images/2025/04/image-197.png)


> Five philosophers sit around a circular table. In front of each philosopher is a large plate of rice. The philosophers alternate their time between eating and thinking. There is one chopstick between each philosopher, to their immediate right and left. In order to eat, a given philosopher needs to use both chopsticks. How can you ensure all the philosophers can eat reliably without starving to death?


Point being, you have two processes that both need access to scarce resources that the other controls, so some sort of locking is in order. Do it wrong, and you have a **deadlock** – everyone starves to death. There are lots of scarce resources in a PC or server, but *this* deadlock is coming from our database, SQL Server 2005.


You can attach the profiler to [catch the deadlock event](https://web.archive.org/web/20080824064922/http://www.simple-talk.com/sql/learn-sql-server/how-to-track-down-deadlocks-using-sql-server-2005-profiler/) and see the actual commands that are deadlocking. I did that, and found there was *always* one particular SQL command involved:

kg-card-begin: html

```

UPDATE [Posts]
SET [AnswerCount] = @p1, [LastActivityDate] = @p2, [LastActivityUserId] = @p3
WHERE [Id] = @p0

```

kg-card-end: html

If it detects a deadlock, SQL Server forces one of the deadlocking commands to lose – specifically the one that uses the least resources. The statement on the losing side varied, but in our case **the losing deadlock statement was always a really innocuous database read**, like so:

kg-card-begin: html

```

SELECT *
FROM [Posts]
WHERE [ParentId] = @p0

```

kg-card-end: html

(Disclaimer: above SQL is simplified for the purpose of this post). This deadlock perplexed me, on a couple levels.

1. **How can a read be blocked by a write?** What possible contention could there be from merely *reading* the data? It’s as if one of the dining philosophers happened to glance over at another philosopher’s plate, and the other philosopher, seeing this, screamed “meal viewing deadlock!” and quickly covered his plate with his hands. Yes, it’s ridiculous. I don’t want to eat your food – I just want to look at it.
2. **We aren’t doing that many writes**. Like most web apps, we’re *insanely  *read-heavy. The particular SQL statement you see above only occurs when someone answers a question. As much as I want to believe Stack Overflow will be this massive, rip-roaring success, there just *cannot* be that many answers flowing through the system in beta. We went through our code with a fine tooth comb, and yep, we’re barely writing anywhere except when users ask a question, edit something, or answer a question.
3. **What about retries?** I find it hard to believe that little write would take so incredibly long that a read would have to wait more than a few milliseconds at most.


If you aren’t *eating* – modifying data – then how can trivial super-fast reads be blocked on rare writes? We’ve had good results with SQL Server so far, but I found this behavior terribly disappointing. Although these deadlocks were somewhat rare, they still occurred a few times a day, and I’m deeply uncomfortable with errors I don’t fully understand. This is the kind of stuff that quite literally keeps me up at night.


I’ll freely admit this could be due to some peculiarities in our code (translated: we suck), and reading through some sample SQL [traces of subtle deadlock conditions](https://web.archive.org/web/20080831122722/http://www.code-magazine.com/article.aspx?quickid=0309101&page=2), it’s certainly possible. We racked our brains and our code, and couldn’t come up with any obvious boneheaded mistakes. While our database *is* somewhat denormalized, all of our write conditions are relatively rare and hand-optimized to be small and fast. In all honesty, our app is just not all that complex. It ain’t rocket surgery.


If you ever have to troubleshoot database deadlocks, you’ll inevitably discover the `NOLOCK` statement. It works like this:

kg-card-begin: html

```

SELECT *
FROM [Posts] with (nolock)
WHERE [ParentId] = @p0

```

kg-card-end: html

It isn’t just a SQL Server command – it also applies to Oracle and MySQL. This sets the transaction isolation level to `read uncommitted`, also known as “dirty reads.” It tells the query to use the lowest possible levels of locking.


**But is nolock dangerous?** Could you end up reading invalid data with read uncommitted on? Yes, in theory. You’ll find no shortage of database architecture astronauts who start [dropping ACID science on you](http://en.wikipedia.org/wiki/ACID) and all but pull the building fire alarm when you tell them you want to try nolock. It’s true: the theory is scary. But here’s what I think:


> In theory there is no difference between theory and practice. In practice there is.


I would never recommend using nolock as a general “good for what ails you” snake oil fix for any database deadlocking problems you may have. You should try to diagnose the source of the problem first.


But *in practice* **adding nolock to queries that you absolutely know are simple, straightforward read-only affairs *never seems to lead to problems***. I asked around, and I got advice from a number of people whose opinions and experience I greatly trust and they, to a (wo)man, all told me the same thing: they’ve *never* seen any adverse reaction when using nolock. As long as you know what you’re doing. One related a story of working with a DBA who told him to add nolock to every query he wrote!


With nolock / read uncommitted / dirty reads, data may be out of date at the time you read it, but it’s never wrong or garbled or corrupted in a way that will crash you. And honestly, most of the time, *who cares?* If your user profile page is a few seconds out of date, how could that possibly matter?


Adding nolock to every single one of our queries wasn’t really an option. We added it to all the ones that seemed safe, but our use of LINQ to SQL made it difficult to [apply the hint selectively](http://www.hanselman.com/blog/GettingLINQToSQLAndLINQToEntitiesToUseNOLOCK.aspx).


I’m no DBA, but it seems to me the root of our problem is that the default SQL Server locking strategy is incredibly [pessimistic out of the box](https://web.archive.org/web/20080908073842/http://www.databasejournal.com/features/mssql/article.php/3560451):


> The database philosophically expects there will be many data conflicts; with multiple sessions all trying to change the same data at the same time and corruption will result. To avoid this, Locks are put in place to guard data integrity... **there are a few instances though, when this pessimistic heavy lock design is more of a negative than a positive benefit, such as applications that have very heavy read activity with light writes**.


Wow, very heavy read activity with light writes. What does that remind me of? Hmm. Oh yes, *that damn website we’re building.* Fortunately, there is a mode in SQL Server 2005 designed for exactly this scenario: [read committed snapshot](https://web.archive.org/web/20080908073821/http://www.databasejournal.com/features/mssql/article.php/3566746):


> Snapshots rely on an entirely new data change tracking method... more than just a slight logical change, it requires the server to handle the data physically differently. Once this new data change tracking method is enabled, it creates a copy, or snapshot of every data change. By reading these snapshots rather than live data at times of contention, Shared Locks are no longer needed on reads, and overall database performance may increase.


I’m a little disappointed that SQL Server treats our silly little web app like it’s a banking application. I think it’s incredibly telling that a Google search for [SQL Server dead locks](https://www.google.com/search?q=SQL+Server+deadlocks)  returns nearly twice the results of a query for [MySql deadlocks](http://www.google.com/search?q=mysql+deadlocks). I’m guessing that MySQL, which grew up on web apps, is much less pessimistic out of the box than SQL Server.


I find that deadlocks are difficult to understand and even more difficult to troubleshoot. Fortunately, it’s easy enough to fix by setting `read committed snapshot` on the database for our particular workload. But I can’t help thinking our particular database vendor just isn’t as *optimistic* as they perhaps should be.

[multi-threading](https://blog.codinghorror.com/tag/multi-threading/)
[deadlock detection](https://blog.codinghorror.com/tag/deadlock-detection/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
