---
title: "Day 34b: Writing curl using my TCP stack"
date: 2013-11-27
url: https://jvns.ca/blog/2013/11/27/day-34b-wrapping-up-the-tcp-stack/
slug: day-34b-wrapping-up-the-tcp-stack
word_count: 424
---


Today I spent a bunch of time writing READMEs for the projects I’ve
been working on at Hacker School, and putting together a
[project page](http://jvns.ca/projects/) with screenshots and
explanations.


While doing that, I discovered that it was impossible to explain my
[TCP fun](http://github.com/jvns/teeceepee) project because it was,
er, mostly not working. So I fixed it up and wrote a finicky and
unreliable version of `curl` using it, which made me happy.


The `curl` example is quite finicky – it uses ARP spoofing to bypass
the kernel’s TCP stack, which sometimes results in it just Not
Working. Running it a few times sometimes fixes this problem. I found
that if I ran it 5 times then it would work. Mostly.


I ran it using


```
$ git clone http://github.com/jvns/teeceepee
$ cd teeceepee
$ sudo python examples/curl.py 10.0.4.4 example.com

```


You’ll notice that I’m supplying an extra local IP address, which
seems like a weird thing to give `curl`. The reason for this is that
it needs to bypass the kernel, since normally the TCP one has there
will intercept any incoming packets and reset the connection. So we
listen on a fake IP address and send gratuitous ARPs to the router.


This IP address needs to be in my subnet and should not belong to
anyone else, because it would do bad things to them.


### Features

- Can connect to hosts, send packets, and reassemble the replies in
the correct order
- Will ignore out-of-order packets


### Missing features

- Breaking up sent data into more than one packet.
- Resending packets that haven’t been ACKed
- Handling more than one incoming connection at once
- `bind()` hasn’t been tested in the wild at all, just unit tested. So
it probably doesn’t work.
- Basically it is a marginally acceptable client and a totally
ineffective server


### Difficulties

- It needs to run as root because it needs to use raw sockets.
- TCP stacks aren’t really *supposed* to start and stop. In
principle this should really run as a daemon, but it doesn’t.
- It needs to do ARP spoofing in order to receive any packets at all,
as I explained earlier
- It’s slow, because Python. If you watch it in Wireshark, it does a
hilarious thing where it gets backed up sending ACKs and then sends
a load of ACKs at the end and takes forever to close the connection.
- Sometimes the ARP spoofing and packet sniffing doesn’t quite work.
Usually if I run it 5 times it will work.
