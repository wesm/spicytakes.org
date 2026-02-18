---
title: "Day 19: A few reasons why networking is hard"
date: 2013-10-31
url: https://jvns.ca/blog/2013/10/31/day-19-i-might-understand-why-networking-is-hard/
slug: day-19-i-might-understand-why-networking-is-hard
word_count: 482
---


So I’ve been trying to learn how to do a particular network exploit this week
(hijack my phone’s internet so that it replaces every webpage with a pony),
inspired by Jessica McKellar’s
[How the Internet Works](http://pyvideo.org/video/1677/how-the-internet-works)
talk (skip to the end to see what I’m talking about).


For a long time I’ve had the notion that networking is pretty complicated, but
I didn’t really know why that was. Yesterday I learned a few reasons why! I
spent pretty much the whole day being confused.


I started trying to understand how iptables works, since that was one step in
the pony-hacking explanation.


Some things I looked at

- [This extremely long IPTables tutorial](https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html)
- [IPTablesHowTo](https://help.ubuntu.com/community/IptablesHowTo) from Ubuntu’s community wiki
- [A set of web server benchmarks](http://acme.com/software/thttpd/benchmarks.html), via [@pphaneuf](https://twitter.com/pphaneuf)


It turns out iptables is pretty complicated. The extremely long iptables
tutorial above was actually quite helpful, though – it goes into tons of
detail about how TCP and IP work. It is an avalanche of information and way
too much to actually absorb, but it is very useful to know that there is that
much stuff that exists to know.


A choice quote from [the tutorial](https://www.frozentux.net/iptables-tutorial/iptables-tutorial.html):


> Among other things, bit [6-7] are specified to be set to 0. In the ECN updates
> (RFC 3168, we start using these reserved bits and hence set other values than
> 0 to these bits. But a lot of old firewalls and routers have built in checks
> looking if these bits are set to 1, and if the packets do, the packet is
> discarded. Today, this is clearly a violation of RFC's, but there is not much
> you can do about it, except to complain.


So one part of “networking is complicated” is “The protocols change over time
and sometimes implementations don’t keep up”.


In the [set of web server benchmarks](http://acme.com/software/thttpd/benchmarks.html), many of the web servers take at least 1/5
of a second per client to return a response, but some don’t. The webpage author explains why:


> Turns out the change that made the difference was sending the response headers
> and the first load of data as a single packet, instead of as two separate
> packets. Apparently this avoids triggering TCP's "delayed ACK", a 1/5th second
> wait to see if more packets are coming in. thttpd-2.01 has the single-packet
> change.


So another part of “networking is complicated” is that there are many
different levels (Ethernet, IP, TCP, …), and at higher levels the lower
levels are supposed to be more or less abstracted away. For example, a
webserver “shouldn’t” have to worry about the details of how TCP works. But
then it turns out that the details of how TCP works *do* matter sometimes.


And there are a lot of levels of networking that could be causing problems, so
when you’re doing high-performance networking stuff, well… it’s complicated.
