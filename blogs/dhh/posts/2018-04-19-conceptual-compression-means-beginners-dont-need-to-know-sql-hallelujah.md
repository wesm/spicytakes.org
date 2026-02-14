---
title: "Conceptual compression means beginners don’t need to know SQL — hallelujah!"
date: 2018-04-19
url: https://signalvnoise.com/svn3/conceptual-compression-means-beginners-dont-need-to-know-sql-hallelujah/
slug: conceptual-compression-means-beginners-dont-need-to-know-sql-hallelujah
word_count: 1086
---


![](https://signalvnoise.com/assets/svn3/images/2018/04/1vfeuUBcGeQMi_KPDXPJmsA.png)


It used to be a fundamental requirement that you learned an extensive amount of SQL before you were able to start working on database-backed applications. It was taken as self-evident that you needed to speak the native language of the database before you were qualified to use it. And better yet, you really ought to understand and care about your particular brand of database engine.


This is no longer so. That fact has snuck up upon us, but it’s none the less true — and that’s amazing.


Through advances in leaky abstractions, we’ve managed to compress the conceptual overhead of the database so much that it needn’t feature in the introduction material for making database-backed applications. In Rails, we call that abstraction [Active Record](http://guides.rubyonrails.org/active_record_basics.html), and it falls into the category of object-relational mappers (ORM).


The ORM was long derided by programmers as an unreliable, even harmful, aid of the lazy or the weak. Something Real Programmers shouldn’t expect to lean on, as it was likely to break down if not immediately, then certainly soon thereafter. And then you’d better know all your relational theory!


That’s the past.


Basecamp 3 has about 42,000 lines of code, and not a single fully formed SQL statement as part of application logic! It serves millions of people. It not only leans on the ORM abstraction, it hardly even thinks about it the vast majority of the time.


Do you know what else application programmers rarely need to think about any more either? Memory management and garbage collection. It used to be just as foundational to know your pointers, your destructors, your mallocs, and all the other conceptual overhead needed to deal with manually managing memory. Now it isn’t.


Our abstraction of SQL isn’t quite yet to the point of our abstraction of memory management, and certain frameworks and environments are further ahead than others, but it’s getting closer. The first version of Basecamp had a bunch of [#find_by_sql](http://api.rubyonrails.org/classes/ActiveRecord/Querying.html#method-i-find_by_sql) calls, the latest have none. That’s progress.


It’s not that knowledge of SQL isn’t nice to have. It’s good to know a lot of things. Just like it’s helpful to have a strong conceptual model of how computers deal with memory management. It’s just that you no longer need to know these things to start making applications, and that’s a wonderful thing.


SQL, like memory management, is a concept you can unpack when you need to. Further down the line of your career. Then after you learn it, you can compress it back down again and spend more of your mental capacity on other things most of the time. I used to write SQL statements every day. Now maybe I do so once a month? Less? And that’s against a major application that’s reached a scale that most beginner apps never will.


Some programmers will scoff at this notion instinctively. That it’s simply *irresponsible* for programmers to start writing code until they know these historical fundamentals. I suppose it’s natural to think that all the hard work you spent learning the basic concepts — that indeed were required when you got started — should still be taught to all on day one. This is one of the key pitfalls of experience. Falling in love with the trials and tribulations you had to suffer, rather than rejoicing in the fact that the next generation doesn’t have to endure them.


The relational database is a glorious invention, but for most programmers it doesn’t need to be more than an appliance. Sure, take the time to learn how the drying tumbler machine works, it may well save you a service call to a specialized technician one day. But it’s hardly a requirement for living with such a device and getting your clothes dry.


The relegation to “appliance status” isn’t a dig, but an honor. It means we’ve finally made the technology and the abstraction so good that many, if not most, programmers don’t even have to think about it on a daily basis.


It also means it’s become a commodity. At Basecamp we happen to use MySQL, but to be honest, it’s basically only for historical and operational reasons. We could switch to PostgreSQL tomorrow, and I wouldn’t really give a damn. We have nothing in the application that relies on a particular brand of the database appliance.


Building stuff with computers means building on top of abstractions. CPUs, 1s and 0s, assembler, C compilers, database drivers, memory management, and a million other concepts are required to make our applications work. But as we progress as an industry, fewer people need to know all of them, and thank heavens for that.


It takes hard work to improve the conceptual compression algorithms that alleviate application programmers from having to worry about the underpinnings most of the time, but it’s incredibly rewarding work. The more effectively we compress the concepts of yesterday, the lower the barriers to entry become. And we need low barriers if we are to get more people started making applications.


SQL is perhaps the brightest example of conceptual compression over the past decade or so, but application work is full of other examples. And we need such conceptual compression more than ever to starve off specialization, and to preserve the power of individual generalists to make complete applications.


We’re currently living through an explosion of conceptual expansion and experimentation on the client-side in the web application world. That’s really exciting! Lots of new ideas and approaches churning rapidly. But it’s also needlessly intimidating in many ways. We don’t all need to spend hours or days learning how to configure build pipelines. Some day our leaky abstractions will be good enough that the conceptual compression will relegate such tooling to appliance status as well. That will be a good day.


You can’t learn everything. You can’t hold every concept fully expanded in your head. And moreover, you shouldn’t. As we compress formerly fundamental concepts, we make room for new, grander abstractions. These are the leaps of progress it’ll take to continue to make us more efficient and ultimately more effective.


But I get that it’s hard to break habits. Like the stereotype of an old person complaining about the price of gas or a gallon of milk because their frame of reference is anchored in a time past. Broad-based progress sometimes need that generational churn to really happen (and that’s not about your physical age, rather the years of experience).


Don’t be a fogey. Don’t fight the conceptual compression. Help make it happen.

