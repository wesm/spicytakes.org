---
title: "Day 24: Unit testing this TCP library"
date: 2013-11-07
url: https://jvns.ca/blog/2013/11/07/day-24-unit-testing-this-tcp-library/
slug: day-24-unit-testing-this-tcp-library
word_count: 183
---


Today in morning checkins I realized I’d been having a lot of trouble
testing this TCP library yesterday, because all of the tests needed to
use the network.


So now I have better unit tests which don’t need to sleep and use the
network! I did this by adding a `MockListener` class which takes
packets.


The actual sending-packets-over-the-network tests no longer pass,
because right now I’m just writing to the mock unit tests. But now the
tests are


a) faster (0.009 seconds instead of 5 or 10), and
b) deterministic (they do the same thing every time)


So this is *much* better. The implemention is still pretty much a
scattered mess. I tried to deal with replies to packets and completely
failed. I’m at the point where I have no idea of how to implement this
TCP state machine.


My plan for fixing this is to read [this tiny implementation](http://dunkels.com/adam/miniweb/)
of TCP – it’s about 1000 lines of C. Right now I have about 100 lines
of Python, *and* I don’t even have to unpack the packets or anything
because scapy does that.
