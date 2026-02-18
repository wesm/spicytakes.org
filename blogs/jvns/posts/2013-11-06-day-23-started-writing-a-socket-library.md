---
title: "Day 23: Started writing a TCP stack in Python"
date: 2013-11-06
url: https://jvns.ca/blog/2013/11/06/day-23-started-writing-a-socket-library/
slug: day-23-started-writing-a-socket-library
word_count: 353
---


For the last couple of days I’ve been trying to understand how TCP
works, because networking is really fun. Yesterday I realized that I
really hadn’t been writing as much code as I want to be, though.


So I’ve started working on a mini TCP stack! I’m not sure yet how far
this will go, but so far I’m running into tons of problems, so I think
this might be a good choice.


The code so far is at
[https://github.com/jvns/teeceepee](https://github.com/jvns/teeceepee).


Here are the parameters:

- Built on top of [scapy](http://www.secdev.org/projects/scapy/), so I
don’t have to actually know how the bits of a TCP packet are put
together
- I do, however, need to use raw sockets in order to be able to send TCP
packets, so everything has to run as root


So far I have

- A `TCPSocket` class, which manages connections to servers and keeps some
state. Right now my states are `CLOSED`, `SYN-SENT`, and
`ESTABLISHED`. I’m using [this diagram](http://www.tcpipguide.com/free/t_TCPOperationalOverviewandtheTCPFiniteStateMachineF-2.htm)
as a reference.
- A `TCPListener` class, which is responsible for managing all the
sockets that might be open. Basically it has a dictionary that maps
ports to `TCPSocket` instances. I have no idea if this is actually how
socket libraries work.


There’s a thread that listens for packets that are coming in and sends
them off to the appropriate `TCPSocket` instance for handling, using the
`dispatch` method. This is my first time using threads pretty much ever.
Expecting all the problems. The listener thread starts when I import the
`tcp` module and ends when the program importing it ends.


Right now I can

- establish a connection (send a TCP handshake)
- send some data (but not parse the response)


Tomorrow I’m hoping to be able to tear down a connection properly and
assemble the packets I’m receiving into some actual data.


One of the things that is the most challenging so far is that I keep
starting and stopping the library, so there are all kinds of connections
that just die. Also I think the servers I’m interacting with think I’m
unreliable, so sometimes they send me packets slowly.
