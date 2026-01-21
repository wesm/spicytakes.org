---
title: "Java console monitoring basics: The 'j' series"
date: 2012-03-22
url: https://www.elidedbranches.com/2012/03/java-console-monitoring-basics-j-series.html
word_count: 821
---

Think fast: It's 10pm, you have a production java application on a box you can only ssh into, and it's in distress. This is the third time this month it's happened. You didn't write the code, and the joker who did didn't bother to put in any
[metrics](http://metrics.codahale.com/)
for you to grab. What do you do? After cursing, but before giving up, restarting the process, and promising to debug it in the morning, you might want to go a round with the Java command-line monitoring tools.
Perhaps you are already familiar with these tools, but I've found that despite their incredible usefulness many seasoned Java developers have never heard of this tool stack. They hide away in the jdk bin directory, but they can be your best friend when you are stuck with nothing but a console and a prayer.
First we have the lowly
[jps](http://docs.oracle.com/javase/1.5.0/docs/tooldocs/share/jps.html)
. It does what you would expect: shows you java processes running as that user (or all users, if you're root).
Moving up the stack, we have
[jinfo](http://docs.oracle.com/javase/1.5.0/docs/tooldocs/share/jinfo.html)
. Show me the vm version, jars, and all the flags this process is running with, or the value of a particular flag. You may have this information elsewhere, but it's nice to have a shortcut.
More useful is
[jstack](http://docs.oracle.com/javase/1.5.0/docs/tooldocs/share/jstack.html)
. Yeah, I'm sure you know how to kill -QUIT but this is a nice way to teach the newbie how to get a stack trace without the risk that they'll accidentally kill the process. If you should be so lucky as to have an obvious deadlock, jstack will kindly point that out to you so you can go fix it. Stack traces are the bread and butter of figuring out what's wrong with a process. Take several, see how they change, or don't, and you'll come closer to finding your problem code.
My personal all-time favorite is
[jstat](http://docs.oracle.com/javase/1.5.0/docs/tooldocs/share/jstat.html)
. More specifically, jstat -gc 3s. That is, jstat of the garbage collector printing new results every 3 seconds. Back in the days when I wrangled gigantic VMs, this tool was invaluable for spot-checking garbage collection. The output is admittedly hideous. For example:
S0C    S1C    S0U    S1U      EC       EU        OC         OU       PC     PU    YGC     YGCT    FGC    FGCT     GCT
37568.0 41984.0 6592.0  0.0   74816.0  38651.6   70272.0    39290.5   63616.0 55956.0     38    1.608   4      1.441    3.049
Yes, that unformatted barf is what you will see on a screen console output for jstat -gc. But that barf tells you a lot. First things first, the most useful stuff is at the very end. See that "4" followed by "1.441"? That shows the stop-the-world GC collections, and the total time they have taken. If your application is running particularly slow, or is frequently unresponsive, the FGC count will quite possibly be high, and the time related to it will be very high. Remember, your app is essentially dead when FGC is running, so a high number of FGCs is a bad sign.
This also shows you the various used and total sizes of the generations. I'm not going to go into details of Java Garbage Collection but it is useful to be able to see them broken out and growing or shrinking. One pattern of GC to watch out for is the case when you don't have enough survivor/eden space to handle all of the transient data you need to do a big chunk of work, and not enough old capacity to take it all, but just enough freeable state to keep slowly moving forward with your computation. The result will be neverending full-gcs while your process moves slightly forward, does a full GC, moves forward again, does a full GC, and moves forward again. This looks in jstat like an ever-increasing series of FGC where each one finishes but only causes a small amount of space to be freed in OU, while EU and the survivor spaces are constantly near-full. The details of the actual GC behavior may change with versions of the JVM (and the flags that you are using), but the ability to monitor the behavior easily in real-time is always useful.
Finally, for the tools I usually use, there's
[jmap](http://docs.oracle.com/javase/1.5.0/docs/tooldocs/share/jmap.html)
. jmap -heap is a nice way to get a pretty-print of the heap info. jmap -histo and jmap -dump are heavier commands that you might want to hold off on doing until you're ready to restart your process anyway, because sometimes running them will result in bad results for the process. If you're producing a ton of garbage and you don't know why, jmap can show you where the memory is going. jmap -dump will product a file that you can push into something like
[MAT](http://www.eclipse.org/mat/)
for analysis.
None of these tools are an answer for proper monitoring of your JVM, but they're great for a quick and dirty debug before you restart a troubled process, and something to make sure your whole team has in their toolbox.