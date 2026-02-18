---
title: "Why do UDP packets get dropped?"
date: 2016-08-24
url: https://jvns.ca/blog/2016/08/24/find-out-where-youre-dropping-packets/
slug: find-out-where-youre-dropping-packets
word_count: 744
---


There’s a joke about UDP. it goes like this: “Never mind, you probably
wouldn’t get it.”


The first time I heard this joke I did not understand it because I didn’t
really understand what UDP was. UDP is a network protocol. The deal is: I send
you a network packet. Maybe you get it, maybe you don’t. I have no idea
whether it arrived or not. UDP doesn’t care.


When you’re losing UDP packets, it’s sort of tempting to say “well, whatever,
that’s what happens when you use UDP!” But UDP packets don’t get lost by
magic.


I was pretty confused about some the details of dropping UDP packets (how do
you know how many packets got dropped? what causes a packet to be dropped
**exactly**?) Maggie Zhou (who is the best) explained some new things to me
today! All the parts of this that are right are thanks to her and all the
parts that are wrong are thanks to me.


This is all on Linux, as usual. There are going to be sysctls! It will be the
best.


### lost on the way out


Imagine you’re sending a lot of UDP packets. Really a lot. On every UDP
socket, there’s a **“socket send buffer”** that you put packets into. The Linux
kernel deals with those packets and sends them out as quickly as possible. So
if you have a network card that’s too slow or something, it’s possible that it
will not be able to send the packets as fast as you put them in! So you will
drop packets.


I have no idea how common this is.


### lost in transit


It’s possible that you send a UDP packet in the internet, and it gets lost
along the way for some reason. I am not an expert on what happens on the seas
of the internet, and I am not going to go into this.


### lost on the way in


Okay, so a UDP packet comes into your computer. You have an application that
is listening and waiting for a packet. Awesome! This packet goes into – maybe
you guessed it – a **socket receive buffer**. How big is that buffer? Everything you might want to know about socket send and receive buffer sizes is helpfully explained in [the man page for `socket`](http://man7.org/linux/man-pages/man7/socket.7.html). Here’s the maximum receive buffer size on my computer:


```
# This prints the max OS socket receive buffer size for all types of connections.
$ sudo sysctl net.core.rmem_max
net.core.rmem_max = 212992
$ sudo sysctl net.ipv4.udp_mem 
net.ipv4.udp_mem = 181110	241480	362220

```


`man udp` says that last number from `net.ipv4.udp_mem` (362220) means
“Number of pages allowed for queueing by all UDP sockets.” 362220 pages is
1.7GB? That’s a lot of pages! Weird. Not sure what’s up with that.


Then your application reads packets out of that buffer and handles them. If
the buffer gets full, the packets get dropped. Simple!


You can see how many packets have been dropped on your machine with `netstat -suna`. Mine has dropped 918 packets so far apparently (“918 packet receive
errors”)


```
$ netstat -suna
IcmpMsg:
    InType3: 1072
    OutType3: 522
Udp:
    1828608 packets received
    568 packets to unknown port received.
    918 packet receive errors
    662721 packets sent
    RcvbufErrors: 918
    SndbufErrors: 1031
    IgnoredMulti: 659

```


This is cool! This means that if you have a machine which is trying to drop as
few UDP packets as possible (for instance if you’re running statsd), then you
can monitor the rate at which that machine is dropping packets!


### buffers everywhere


After I published this blog post initially, @gphat and @nelhage very astutely
pointed out that the OS socket send/receive buffers are not the only buffers.


EVERYTHING IS BUFFERS. Your network card has a buffer that can get full! There
are a bunch of intermediate routers between your computer and my computer. All
of those have buffers! Those buffers can get full! My current understanding is
that most packet loss is because of full buffers one way or another.


If you’re interested in learning more details about the Linux networking stack, there is this huge post called [Monitoring and Tuning the Linux Networking Stack: Receiving Data](http://blog.packagecloud.io/eng/2016/06/22/monitoring-tuning-linux-networking-stack-receiving-data/). I have not read it yet but it looks **amazing**.


Also everything here I said about UDP packets applies just as well to any kind
of IP packet – TCP packets can get dropped just as easily, but they’ll get
retried, so you’re not as likely to notice.
