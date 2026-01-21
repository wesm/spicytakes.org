---
title: "Quick Wins: Monitoring Request Times in Play with Coda Metrics"
date: 2012-02-09
url: https://www.elidedbranches.com/2012/02/quick-wins-monitoring-request-times-in.html
word_count: 492
---

My twitter feed has been abuzz about
[coda metrics](http://metrics.codahale.com/)
for a while now. I decided to finally bite the bullet and try it out, and the result was a very nice quick win for our code base.
We're still using
[Play](http://www.playframework.org/)
at work, and we have a service about to go into production that we've been monitoring through the oh-so-elegant method of "writing log messages". This is fine, but it doesn't tell you how long various request types are taking on average without doing a bit of log parsing, and I'm not much of a scripter.
Today, I promised that I would provide something slightly better to measure how our various endpoints are doing. Cue coda. I've been looking at it on and off for a couple of days, but kept getting hung up on wanting to do things like use the EhCache metrics gathering (not trivial in Play at first glance). Going back to basics, I decided after some thinking that the
[histograms](http://metrics.codahale.com/getting-started.html#toc_5)
would be the best thing to use. We were already grabbing method execution time for logging purposes, so all I had to do was insert that into a histogram and it would track the running times. Simple enough. But I want to create these histograms for each method type, and ideally, I just want to put it into our superclass controller that is already set up to capture the method timings and log.
Fortunately, Play has lots of nice information floating around in the "request" object of its controllers. Using that object, I can see what Controller subclass this request is destined for, as well as the method that will be called on that class. So I have enough information to create the histogram for each method, like so:

> Histogram histo = Metrics.newHistogram(request.controllerClass, request.actionMethod, "requests");

Great. But I was a little tired, and thought that I needed to keep these around, so I stuck them in a ConcurrentHashMap associated with a unique key based on the controller class and the action method. Turns out though, if you look in the
[MetricsRegistry source code](https://github.com/codahale/metrics/blob/master/metrics-core/src/main/java/com/yammer/metrics/core/MetricsRegistry.java#L486)
, you'll see that in fact you don't really need to do this at all. As long as the "MetricName" that would be generated for your metric is the same, the same metric will be used for the monitoring. Now THAT is the kind of clever code I like to see.
I decided to keep my ConcurrentHashMap around anyway, to save myself the (utterly trivial) overhead of creating the various objects passed in to the registry by newHistogram. The resulting code is embarrassingly simple. So simple, in fact, I wanted to make it more complicated and it took me 3 revisions to realize how little code I actually needed.
[Here is the resulting BaseController, on GitHub](https://github.com/skamille/play-sample-code/blob/master/app/controllers/BaseController.java)
, in a skeleton Play application.
I'm a bit sleep-deprived, so if I missed something, be sure to leave a comment or hit me up on
[twitter](https://twitter.com/#!/skamille)
!