---
title: "Thread Priorities are Evil"
date: 2006-08-29
url: https://blog.codinghorror.com/thread-priorities-are-evil/
slug: thread-priorities-are-evil
word_count: 612
---

Programmers* love to futz around with thread priorities. As if [programming with threads](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/) wasn’t already dangerous enough, we’ve got to get in there and tweak thread priorities to make things run... er... "better.”


![](https://blog.codinghorror.com/content/images/2025/04/image-765.png)


Let’s [fire up Task Manager](https://blog.codinghorror.com/everything-you-always-wanted-to-know-about-task-manager-but-were-afraid-to-ask/) and take a quick survey of process priorities. Out of **38** processes running on my computer right now, I have **0** at low priority, **36** at normal priority, and **2** essential system processes (csrss and winlogon) running at high priority.


I bet **almost every process on your machine is running at a base priority of “Normal,”** too. And there’s a very good reason for this.


Witness K. Scott Allen’s [strange threading experiment](http://odetocode.com/Blogs/scott/archive/2006/08/27/6053.aspx):

kg-card-begin: html

> This program behaves badly on a single processor machine, and pegs the CPU at 100% for over two minutes. On a multi processor machine, the program finishes all the threading work in the blink of an eye - only a brief CPU spike.
> Strangely, if I remove a single line of code:
> t.Priority = ThreadPriority.BelowNormal;
> ... then the program performs just as well on a single processor machine (only a brief spike - comparable to the multi processor scenario).

kg-card-end: html

This little threading demo highlights **one of the reasons a dual-core computer is so desirable – it protects you from poorly written programs.** If a program goes haywire and consumes 100% of CPU time, you still have a “spare” CPU waiting to pick up the slack. Whereas a single processor machine becomes totally unresponsive. That’s why **Task Manager itself runs at High priority **– so you can pre-empt these kind of runaway apps.**


Hardware fixes to software problems [are never pretty](https://blog.codinghorror.com/nasty-software-hacks-and-intels-cpuid/). What’s really going on here? Joe Duffy is something of an expert on the topic of threading and concurrency – he works for Microsoft on CPU-based parallelism in the .NET Common Language Runtime – and he has [this to say](https://web.archive.org/web/20060912112030/http://www.bluebytesoftware.com/blog/PermaLink,guid,1c013d42-c983-4102-9233-ca54b8f3d1a1.aspx):


> **Messing with [thread] priorities is actually a very dangerous practice, and this is only one illustration of what can go wrong.** (Other illustrations are topics for another day.) In summary, plenty of people do it and so reusable libraries need to be somewhat resilient to it; otherwise, we get bugs from customers who have some valid scenario for swapping around priorities, and then we as library developers end up fixing them in service packs. It’s less costly to write the right code in the first place.
> Here’s the problem. If somebody begins the work that will make ‘cond’ true on a lower priority thread (the producer), and then the timing of the program is such that the higher priority thread that issues this spinning (the consumer) gets scheduled, the consumer will starve the producer completely. This is a classic race. And even though there’s an explicit Sleep in there, issuing it doesn’t allow the producer to be scheduled because it’s at a lower priority. The consumer will just spin forever and unless a free CPU opens up, the producer will never produce. Oops!
> The moral of the story? **[Thread] priorities are evil, don’t mess with them.**


Although there are some edge conditions where micromanaging thread priorities can make sense, it’s generally a bad idea. **Set up your threads at normal priority and let the operating system deal with scheduling them.** No matter how brilliant a programmer you may be, I can practically guarantee you won’t be able to outsmart the programmers who wrote the scheduler in your operating system.


*And users who think they’re programmers
**Assuming the runaway app itself isn’t running at High priority, in which case you’re in a world of hurt.

[threads](https://blog.codinghorror.com/tag/threads/)
[thread priorities](https://blog.codinghorror.com/tag/thread-priorities/)
[multi-threading](https://blog.codinghorror.com/tag/multi-threading/)
[cpu optimization](https://blog.codinghorror.com/tag/cpu-optimization/)
