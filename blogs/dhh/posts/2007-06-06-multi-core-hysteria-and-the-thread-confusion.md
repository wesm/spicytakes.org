---
title: "Multi-core hysteria and the thread confusion"
date: 2007-06-06
url: https://dhh.dk/posts/7-multi-core-hysteria-and-the-thread-confusion
slug: multi-core-hysteria-and-the-thread-confusion
word_count: 204
---


New CPUs are growing in cores and not in GHz. That's a tough problem for applications that have been traditionally single-threaded, like games. They have to learn all new techniques and rework their thinking to get the most out of the next-generation platforms.


But the fear of that transition has bled into places where it's largely not relevant, like web-application development. Which has caused quite a few folks to pontificate that the sky is falling for Rails because we're not big on using threads. It isn't.


Multiple cores are laughably easy to utilize for web applications because our problems are rarely in the speed of serving 1 request. The problem is in serving thousands or tens or hundreds of thousands of requests. Preferably per second.


Threads are not the only way to do that. Processes do the job nearly as well with a drop of the complexity. And that's exactly how Rails is scaling to use all the cores you can throw at it.


The 37signals suite is currently using some ~25 cores for the application servers that all the applications have dips on. We'd welcome a 64-core chip any day.


Read more: [A good summary of a discussion on multi-core programming in general](http://radar.oreilly.com/archives/2007/06/googles_folding.html).

