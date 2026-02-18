---
title: "Java isn't slow"
date: 2016-01-03
url: https://jvns.ca/blog/2016/01/03/java-isnt-slow/
slug: java-isnt-slow
word_count: 535
---


This is probably obvious to many of you, but I wanted to write it down just in case.


I used to write Java at work, and my Java programs were really slow. I thought
(and people sometimes told me) that this was because Java is a slow programming
language.


This just isn’t true. This article describes the architecture of the [LMAX Disruptor](http://martinfowler.com/articles/lmax.html), a messaging library that they use to process 6 million events per second on a single machine. That article is also SUPER FASCINATING and really worth reading. Java is fast like C is fast (really fast). People write databases ([Cassandra](http://cassandra.apache.org/)) in Java!


By “Java is fast”, I mean something pretty specific – that you can comfortably do millions of things a second in Java. This isn’t true for languages like Python or Ruby – in the [computers-are-fast game I made](http://computers-are-fast.github.io/), you can see that a pure-python HTTP request parser can parse 25,000 requests a second. I’d expect an optimized Java program to do dramatically better than that.


So if your Java code is doing something easier than processing 6 million events a second, and it’s slow, you can maybe make it faster! Processing 6 million events per second is actually extremely difficult, but I find it inspiring to think about when I’m having trouble processing like.. 10 things per second :)


My Java code was probably slow because I was creating like a bajillion objects all the time, and destroying them, and doing a bajillion allocations takes time, and also it puts pressure on the garbage collector, and… Well, you get the idea. But code like that is not the whole world!


There’s a culture of building high-performance Java code out there. I asked on [twitter](https://twitter.com/b0rk/status/683623665800474624) and got linked to [this interesting-looking data structures library](https://github.com/real-logic/Agrona) and this [Java concurrency tools](https://github.com/JCTools/JCTools) repo. And to Netty! Netty is a networking framework (to build webservers, and other things!) in Java. The [Netty testimonials page](http://netty.io/testimonials) says that trading firms (who we all know care a lot about performance!!) use Netty.


There’s this high performance [database connection pool](https://github.com/brettwooldridge/HikariCP) and a [page explaining how they made it fast](https://github.com/brettwooldridge/HikariCP/wiki/Down-the-Rabbit-Hole). [Chronicle](http://chronicle.software/products/chronicle-map/) is a key-value store in Java. And all that’s just what I got in 10 minutes from reading a few tweets!


### How to make your Java (or Scala, or Clojure) code fast


This is a super small thing, but some people I talked to didn’t know this!


Did you know the JVM ships with a free profiler that can tell you which part of your code is the slowest? It’s called [VisualVM](https://visualvm.java.net). It’s very easy to use and it’s an AWESOME first step to take. Here’s a screenshot of VisualVM profiling VisualVM. It’s spending most of its time on `org.netbeans.swing.tabcontrol.TabbedContainer.paint`. So it’s mostly working on drawing the screen to show me the results of profiling itself!


([YourKit](https://www.yourkit.com/) is better, but VisualVM is free)


It won’t get you to LMAX disruptor speed (that’s much more serious wizardry), but it is a good first step!


I had some [slow JVM code](http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/) at work a while ago. We made it fast. I used VisualVM! So can you :) [Computers](http://computers-are-fast.github.io/) are [fast](http://jvns.ca/blog/2014/05/12/computers-are-fast/), and you should expect a lot out of your computer programs.
