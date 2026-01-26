---
title: "Catastrophic Failover"
description: "One of the oft advertised features of modern application servers is that they provide failover in a cluster. Clustering improves the reliability of your application, if one of your servers goes down, "
date: 2005-03-07T00:00:00
tags: ["continuous delivery", "bad things"]
url: https://martinfowler.com/bliki/CatastrophicFailover.html
slug: CatastrophicFailover
word_count: 258
---


One of the oft advertised features of modern application servers
is that they provide failover in a cluster. Clustering improves the
reliability of your application, if one of your servers goes down, you
have some more up to server your customers. Failover can add even more
reliability, if a server goes down in the middle of a interaction the
cluster can move that interaction to another server.


However this can be a problem.


A request may do something that causes a server to crash, perhaps
by unwittingly exposing a bug in the server software. So when the
failover kicks in, the deadly requests gets moved to another server
which it can then bring down in turn. Get the timing just right and by
the time the first server has rebooted, it will be ready to receive
that request again.


(In case you're wondering, this is a true story.)


So if you see your servers repeatedly going down, an errant
transaction could well be the cause. To prevent this, you need a check
to ensure that you don't migrate a request that's already been in a
couple of failovers. It's good to failover, but you don't want your
farm to do it too often.


**Update: **[Christopher
Baus](http://www.baus.net/catastrophic-failover) pointed out that this problem suggests you should
deliberately use different equipment on your cluster. So if you're
running a Java application, consider using a mix of different app
servers, operating systems, and hardware. A mix is more complex to
manage, of course, but greatly reduces the chance of this problem
happening.
