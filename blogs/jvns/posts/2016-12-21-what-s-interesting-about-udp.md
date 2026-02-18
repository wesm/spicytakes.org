---
title: "What's interesting about UDP?"
date: 2016-12-21
url: https://jvns.ca/blog/2016/12/21/what-s-interesting-about-udp/
slug: what-s-interesting-about-udp
word_count: 1154
---


I asked on Twitter today “what’s interesting about UDP”? ([this tweet](https://twitter.com/b0rk/status/811403117673742336))
I got a bajillion replies. Here’s a rough summary because there was
some really interesting stuff in there once I made it through all the
UDP jokes and I don’t want to lose it.


First, we should talk about what UDP is for a second: UDP lets you send
network packets. If a UDP packet you send gets dropped, you never find
out about it and nobody will help you retry. Retrying is up to you.


Technically speaking it stands for “user datagram protocol” but I think
“unreliable data protocol” is better because it’s funny and probably
more accurate anyway.


Another fact about UDP is that if you mention UDP there will be 1000
jokes about dropping packets.


So! What is there to know about UDP? Here’s a list.


One interesting thing was that there’s a really common notion “video
streaming/VOIP uses UDP” and “games use UDP” but I think the issues
there are actually kind of subtle and sometimes these things actually
end up using TCP instead. I don’t understand this very well yet but it
doesn’t seem to be totally straightforward.


### DNS uses UDP


This is possibly the most important protocol that works on top of UDP. I
think the *reason* DNS uses UDP is probably that practically all DNS requests and
responses fit into a single IP packet, so retry logic is relatively simple
(you send your request, if you don’t get a response, you just.. try
again.) You don’t need to assemble multiple packets.


When servers need to send a large DNS response, they use TCP instead (I
actually ran into a bug at work recently related to this – in one case
UDP DNS responses were working properly, and TCP responses weren’t).


### statsd uses UDP


[statsd](https://github.com/etsy/statsd)  is a metrics server from Etsy.
The idea here is that statsd uses UDP because metrics reporting should
be as cheap as possible (sending UDP packets is really fast, there is no
connection to manage). Some extra factors.

- the overhead of setting up a TCP connection is pretty high, so they
don’t want to do that for every single statistics request
- Etsy uses PHP, which I think means they can’t have long-lived
persistent TCP connections


Also apparently sometimes people do logging (like syslog) over UDP.
Here’s [an RFC about that](https://tools.ietf.org/html/rfc5426). It’s
not clear to me that this is generally a good idea (it leads with
“Network administrators and architects should be aware of the
significant reliability and security issues of this transport”)


### Packet size limits


The practical packet size limits for UDP are pretty important to
understand.


This seems super important – with TCP you can kind of ignore the fact
that internet packets can only be so big, because TCP will automatically
combine packets for you. With UDP, it gets important
really fast because there’s no automatic combining of packets. You need
to manually split up your data into packets.


For example the reason there are only 13 root DNS servers
is that DNS uses UDP and that is how many fit inside a single UDP packet! (according to
[wikipedia](https://en.wikipedia.org/wiki/Root_name_server#Root_server_addresses))


### WebRTC uses UDP


The chapter in “High Performance Browser Networking” [about WebRTC](https://hpbn.co/webrtc/) is
super interesting and well written and very much worth a read. Also that whole book is
great. Actually you should probably just go read that chapter instead of this
blog post :).


### Some games use UDP


[Your Game Doesn’t Need UDP (Yet)](https://thoughtstreams.io/glyph/your-game-doesnt-need-udp-yet/) is an article about this. Many real-time games use UDP because dropped frames are considered better than delayed frames. I know almost nothing about this.


@caitie summarized the reason some games use UDP pretty clearly:


> UDP is used for video and some games because with TCP you can get huge
> delays for one dropped packet. Imagine you are sending 20 packets via
> TCP, and packet 3 goes missing. Due to network delay you don’t get the
> missing packet 3 msg until you’ve sent all 20 messages so now you have
> to send 3 through 20 again to guarantee in order delivery. So on very
> lossy networks you can waste a lot of bandwidth and cycles resending
> packets.


### video streaming uses UDP, sometimes

- “Most h.264 streams for live cameras and such are UDP as far as I know.” ([here](https://twitter.com/TheTarquin/status/811412243434782720))
- “I worked on the video delivery side more recently, and RTMP, RTSP,
and obviously HLS etc. are all TCP now” ([here](https://twitter.com/sean_a_cassidy/status/811413095817936896))


### probably don’t reimplement TCP on top of UDP


If you actually want reliable message delivery, you should probably just
use TCP and not try to do any fancy UDP tricks. If you really actually
do not care if your packets arrive or not and they are all basically
independent of each other and the order does not matter at all (like
with statsd), maybe that is a good time to use UDP.


It’s possible that, most of the time, the answer to “when should I use
UDP” is “don’t, just use TCP instead, it’ll be easier”.


### Google is maybe trying to reimplement TCP with UDP though


See [QUIC](https://www.chromium.org/quic), [SPDY](https://en.wikipedia.org/wiki/SPDY)


### multicast


Wikipedia says “The most common transport layer protocol to use
multicast addressing is User Datagram Protocol (UDP).” I still don’t
understand what’s up with multicast but many people mentioned it. Here’s
[the wikipedia article](https://en.wikipedia.org/wiki/Multicast).


“udp lets you write stateless protocols. stateless protocols are great
cause you can talk to millions of peers from 1 machine”


### other interesting stuff

- udp checksum is endian independent!
- “how Bittorrent built uTP on top of it is interesting”
- I’ve been confused before that you can still get a “connection
refused” (via icmp) even though UDP is connectionless (this is a
real, weird, thing)
- UDP is used in a bunch of denial of service attacks in various ways
(“you can write someone else’s address as the return address. A lot.
This sucks.”)
- UDP came about when tcp was split into ip and tcp
- “It’s really hard to do load balancing well for UDP, but that can be
really important (eg for server infrastructure for video calls).”
- DHCP uses UDP
- strictly speaking UDP carries “more data” than TCP because TCP headers
take more space (more overhead) than UDP headers
- I think there are some issues with UDP and network address translation
(NAT) because UDP doesn’t have connections. I’m not super clear on
this though.
- It’s easier to spoof IPs for UDP traffic since no handshake is
necessary


### Questions

- Why would you use TCP instead of UDP? Why would you use UDP
instead of TCP?
- Why is UDP considered ’not blocking’?? What is configurable about it?
Sendbuffer / receive buffer size??
- “why would you use this? why is unreliable a better idea sometimes?”
- how lossy is it in practice?
