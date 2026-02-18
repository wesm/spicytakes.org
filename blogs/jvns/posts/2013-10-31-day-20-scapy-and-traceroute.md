---
title: "Day 20: Traceroute in 15 lines of code using Scapy"
date: 2013-10-31
url: https://jvns.ca/blog/2013/10/31/day-20-scapy-and-traceroute/
slug: day-20-scapy-and-traceroute
word_count: 399
---


Today Jari and Brian explained a whole bunch of things to me about networks!
It was fantastic. It’s amazing to have people with so much experience to ask
questions.


At the end they mentioned that I should look up how `traceroute` works and
that it’s a pretty popular networking-job-interview question. And I’d just
discovered this super cool Python networking library called
[Scapy](http://www.secdev.org/projects/scapy/) which lets you construct
packets really easily. So I thought I’d implement traceroute using scapy!


I thought it would take a long time, but turns out that (a basic version) is
really easy.


So using scapy, you can create IP and UDP packets like this:


```
from scapy.all import *
ip_packet = IP(dst="hackerschool.com", ttl=10)
udp_packet = UDP(dport=40000)
full_packet = IP(dst="hackerschool.com", ttl=10) / UDP(dport=40000)

```


Then you can send a packet like this:


```
send(full_packet)

```


So IP packets have a `ttl` attribute, which stands for “Time-To-Live”. Every
time a machine receives an IP packet, it decreases the `ttl` by 1 and passes
it on. Basically this is a super smart way to make sure that packets don’t get
into infinite loops.


If a packet’s `ttl` runs out before it replies, the last machine sends back an
ICMP packet saying “sorry, failed!”.


To implement traceroute, we send out a UDP packet with `ttl=i` for `i = 1,2,3,...`. Then we look at the reply packet and see if it’s a “Time ran out”
or “That port doesn’t exist” error message. In the first case, we keep going,
and in the second case we’re done.


Here’s the code! It’s 16 lines including comments and everything.


```
from scapy.all import *
hostname = "google.com"
for i in range(1, 28):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print "Done!", reply.src
        break
    else:
        # We're in the middle somewhere
        print "%d hops away: " % i , reply.src

```


The output looks like:


```


1 hops away:  192.168.1.1
2 hops away:  24.103.20.129
3 hops away:  184.152.112.73
4 hops away:  184.152.112.73
5 hops away:  107.14.19.22
...


```


So it turns out traceroute is kind of easy! Apparently the difference between
traceroute on Windows and Unix is that Unix generally sends UDP packets and
Windows sends ICMP packets.


There’s also `tcptraceroute` which, well, sends TCP packets.
