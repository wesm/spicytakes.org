---
title: "Day 25: ACK all the things"
date: 2013-11-12
url: https://jvns.ca/blog/2013/11/12/day-25-ack-all-the-things/
slug: day-25-ack-all-the-things
word_count: 286
---


Today I worked some more on my TCP stack! I read a bit of Stevens’
[TCP/IP Illustrated](http://www.amazon.com/TCP-Illustrated-Vol-Addison-Wesley-Professional/dp/0201633469),
where I obtained exactly one insight: every TCP packet I send (except
for the initial SYN) can have the ACK flag set.


This simplified my packet-sending code a lot – I realized I can construct
basically every packet the same way, except for the flags and the payload. Now
I can write


```
def _send_syn(self):
    self._send(flags="S")
    self.state = "SYN-SENT"

```


instead of


```
def send_syn(self):
    syn_pkt = self.ip_header / TCP(dport=self.dest_port, sport=self.src_port, flags="S", seq=self.seq)
    self.listener.send(syn_pkt)
    self.state = "SYN-SENT"

```


Right now the way I’m handling ACKs is basically to send an ACK for every
packet I receive. This isn’t really efficient (because if I’m receiving tons of
packets really fast it would make sense to acknowledge less often). But it is
not incorrect, which is all that I’m going for.


I also decided that I want to be able to be a TCP server as well as a TCP
client. So I started writing `bind()`. Here it is so far:


```
def bind(self):
    pass

```


Seriously I did not ever think about how `bind()` works before. It has to
manage multiple connections! And keep a queue! What am I supposed to do when
people send me packets all at once? Just ignore them until I have time? I don’t
get it.


Testing is fantastic. I love testing. I refactored pretty much all the code today in
[this commit](https://github.com/jvns/teeceepee/commit/aa8ff0a027e8e23388ab922951a7524467b429e7).
The code still works, because tests. =D


However writing tests kind of sucks because it takes forever. Next up: writing
tests for

- receiving packets out of order
- receiving duplicate packets
- being on the server side of the TCP handshake
