---
title: "Operations for software developers for beginners"
date: 2016-10-15
url: https://jvns.ca/blog/2016/10/15/operations-for-software-developers-for-beginners/
slug: operations-for-software-developers-for-beginners
word_count: 1243
---


I work as a software developer. A few years ago I had no idea what “operations” was. I had
never met anybody whose job it was to operate software. What does that even mean? Now I
know a tiny bit more about it so I want to write down what I’ve figured out.


### operations: what even is it?


I made up these 3 stages of operating software. These are stages of understanding about operations I am going through.


**Stage 1: your software just works. It’s fine.**


You’re a software developer. You are running software on computers. When you write your software, it generally works okay – you write tests, you make sure it works on localhost, you push it to production, everything is fine. You’re a good programmer!


Sometimes you push code with bugs to production. Someone tells you about the bugs, you fix
them, it’s not a big deal.


I used to work on projects which hardly anyone used. It wasn’t a big deal if there was a
small bug! I had no idea what operations was and it didn’t matter too much.


**Stage 2: omg anything can break at any time this is impossible**


You’re running a site with a lot of traffic. One day, you decide to upgrade your database over the weekend. [You have a bad weekend](https://blog.clevertap.com/sleepless-nights-with-mongodb-wiredtiger-and-our-return-to-mmapv1/). Charity writes a blog post saying [you should have spent more than 3 days on a database upgrade](https://charity.wtf/2016/10/02/the-accidental-dba/).


I think if in my “what even is operations” state somebody had told me “julia!! your site needs to be up 99.95% of the time” I would have just have hid under the bed.


Like, how can you make sure your site is up 99.95% of the time? ANYTHING CAN HAPPEN. You could have spikes in traffic, or some random piece of critical software you use could just stop working one day, or your database could catch fire. And what if I need to upgrade my database? How do I even do that safely? HELP.


I definitely went from “operations is trivial, whatever, how hard can keeping a site up be?” to “OMG THIS IS IMPOSSIBLE HOW DOES ANYONE EVER DO THIS”.


**Stage 2.5: learn to be scared**


I think learning to be scared is a really important skill – you **should** be worried
about upgrading a database safely, or about upgrading the version of Ruby you’re using in
production. These are dangerous changes!


But you can’t just [stop at being scared](https://jvns.ca/blog/2014/12/21/fear-makes-you-a-worse-programmer/) – you need to learn to have a healthy concern about complex parts of your system, and then learn how to take the appropriate precautionary steps and then confidently make the upgrade or deploy the big change of whatever the thing you are appropriately scared of is.


If you stop here then you just end up using a super-old Ruby version for 4 years
because you were too scared to upgrade it. That is no good either!


**Stage 3: keeping your site up is possible**


So, it turns out that there is a huge body of knowledge about keeping your site up!


There are people who, when you show them a large complicated software system
running on thousands or tens of thousands of computers, and tell them “hey, this needs to
be up 99.9% of the time”, they’re like “yep, that is a normal problem I have worked on! Here’s the first step we can take!”


These people sometimes have the job title “operations engineer” or “SRE” or “devops engineer” or “software engineer” or “system administrator”. Like all things, it’s a skillset that you can learn, not a magical innate quality.


Charity is one of these people! That blog post ("[The Accidental
DBA](https://charity.wtf/2016/10/02/the-accidental-dba/)")) I linked to before has a bunch
of extremely practical advice about how to upgrade a database safely. If you’re running a
database and you’re scared – you’re right! But you can learn about how to upgrade it from
someone like Charity and then it will go a lot better.


### getting started with operations


So, we’ve convinced ourselves that operations is important.


Last year I was on a team that had some software. It mostly ran okay, but infrequently it
would stop working or get super slow. There were a bunch of different reasons it had
problems! And it wasn’t a disaster, but it also wasn’t as awesome as we wanted it to be.


For me this was a really cool way to get a little bit better at operations! I worked on
making the service faster and more reliable. And it worked! I made a couple of good
improvements, and I was happy.


Some stuff that helped:

- work on a dashboard for the service that clearly shows its current state (this is surprisingly hard!)
- move some complicated code that did a lot of database operations into a separate webservice so we could easily time it out if something went wrong
- do some profiling and remove some unnecessarily slow code


The most cool part of this, though, is that a much more experienced SRE later came in to
work with the team on making the same service operate better, and I got to see what he did
and what his process for improving things looked like!


It’s really helped me to realize that you don’t turn into a Magical Operations Person overnight. Instead, I can take whatever I’m working on right now, and make small improvements to make it operate better! That makes me a better programmer.


### you can make operations part of your job


As an industry, we used to have “software development” teams who wrote code and threw it over the wall to “operations teams” who ran that code. I feel like we’ve collectively decided that we want a different model (“devops”) – that we should have teams who both write code and know how to operate it. And there are a lot of details of how that works exactly (do you have “SRE"s?)


But as an individual software engineer, what does that mean for you? I thiiink it means that you get to LEARN COOL STUFF. You can learn about how to deploy changes safely, and observe what your code is doing. And then when something has gone wrong in production, you’ll both understand what the code is doing (because you wrote it!!) and you’ll have the skills to figure it out and systematically prevent it in the future (because you are better at operations!).


I have a lot more to say about this (how I really love being a generalist, how doing some operations work has been an awesome way to improve my debugging skills and my ability to reason about complex systems and plan how to build complicated software). And I need to write in the future about super useful Ideas For Operating Software Safely I’ve learned about (like dark reads and circuit breakers). But I’m going to stop here for now. If you want more reading [The Ops Identity Crisis](http://www.susanjfowler.com/blog/2016/10/13/the-ops-identity-crisis) is a good post about software developers doing operations, from the point of view of an ops person.


This is my favorite paragraph from Charity’s “[WTF is operations?](https://charity.wtf/2016/05/31/wtf-is-operations-serverless/)” blog post (which you should just go read instead of reading me):


> The best software engineers I know are the ones who consistently value the impact and lifecycle of the code they ship, and value deployment and instrumentation and observability.  In other words, **they rock at ops stuff**.
