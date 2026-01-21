---
title: "Networking woes in Java"
date: 2012-02-22
url: https://www.elidedbranches.com/2012/02/networking-woes-in-java.html
word_count: 728
---

The only major CS subject I never took a class in was networking. It's kind of ridiculous, looking back, that I took as many systems classes as I did but always eschewed networking. I do own a copy of
[UNIX Network Programming: Networking APIs: Sockets and XTI; Volume 1](http://www.amazon.com/gp/product/013490012X/ref=as_li_ss_tl?ie=UTF8&tag=elidebranc-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=013490012X)

![](http://www.assoc-amazon.com/e/ir?t=elidebranc-20&l=as2&o=1&a=013490012X)

, bought at some point in the past when I knew I was going to be doing some distributed systems work and figured it would be a useful reference. But I can't say it's been my constant companion. For I have learned one thing in my years of Java systems coding:
*Networking code is HARD.*
Here's exhibit A:
[ZooKeeper monitoring misuses sockets](https://issues.apache.org/jira/browse/ZOOKEEPER-1197)
. I spent a good chunk of time desperately trying to figure out why my monitoring commands were crapping out halfway through when run from NY to LN. Turns out, you can't safely expect to just close half a socket, leave the other half open, push some data to it and then close it while seeing all the data through to the other side. Not without a final handshake indicating the client has gotten all the data.
Or at least, I think that's the case.
The thing is, this will work well enough over a very fast network connection or with very little data. The guarantees around so_linger etc change kernel to kernel and my reading at the time led me to think that in fact the standard linux kernel behavior in this case may well have changed over the years that ZooKeeper has been around. So we need to completely rip out and redo the monitoring code if we want to have any hope of this working right for other big, global deployments in the future.
Exhibit B is my current debugging nightmare. Part of our release last week involved a new backend Play service that itself connects to a different backend Play service to prepare results for our storefront. We noticed, several hours after launch, that the service started to throw exceptions that were ultimately
c
aused by java.io.IOException: Too many open files. I know enough about Java to know that running out of file descriptors is often a Bad Thing.
So we're leaking sockets. Why? To date, we don't know.
The underlying libraries are async-http-client and netty, but there's very little to indicate what is going on.
The sockets show up in netstat/lsof as
ESTABLISHED
TCP connections to the various storefront servers. But the storefront servers do not have most of these sockets open on their end. How are they
ESTABLISHED
with no partner? It's an ongoing mystery, one that we haven't been able to reproduce on any other machine (the current theory is bad network hardware/software at the lowest levels, but honestly that's just a shot in the dark and one that we can't verify without taking down a production service).
So, while I keep debugging, what are the takeaways here?
1) You shouldn't write your own socket handling code in Java. Really, no. Don't do it. Use
[Netty](http://www.jboss.org/netty)
. It's very good. Of all the things not to reinvent yourself, I would put networking at the top of the list with a bullet. It's hard, and requires the kind of deep expertise that you can't fake. And, when you fake it, you may end up with something like our ZooKeeper monitoring, that seems to work for years while hiding small but significant bugs.
2) If you're a system architect writing any kind of web services/distributed system architecture, you should know your unix socket monitoring commands.
[lsof](http://www.ibm.com/developerworks/aix/library/au-lsof.html)
is obtuse but powerful.
[netstat](http://www.faqs.org/docs/linux_network/x-087-2-iface.netstat.html)
is simpler and still quite useful.
[This article has a few others, like ss and iftop](http://www.cyberciti.biz/faq/check-network-connection-linux/)
. Know how to up the ulimits for your processes in case you find yourself with a slow socket leak that you need time to debug.
Have an idea what my bug is? I'd love to hear it! Leave me a comment or hit me up on
[twitter](https://twitter.com/#%21/skamille)
!
Edit 2/27: Looks like our bug was indeed on the cloud vendor side; possibly a misconfigured firewall. Moving to a new box and rebuilding the box we were on solved it.
Thank God Play is at least using good networking libraries, because the last time I tested ZooKeeper, when it runs out of sockets the service hard fails with almost no indication of what happened.