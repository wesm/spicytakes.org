---
title: "netdev conference, day 2"
date: 2017-04-07
url: https://jvns.ca/blog/2017/04/07/netdev-conference-day-2/
slug: netdev-conference-day-2
word_count: 1763
---


Hello! Here are notes from the second day of the netdev conference!
[this great tutorial on how to filter packets with XDP/BPF was also today and i wrote it up
separately](https://jvns.ca/blog/2017/04/07/xdp-bpf-tutorial/)


very very rough list of themes:

- lots about BBR, a TCP congestion algorithm from Google
- you can take the linux kernel networking stack and put it in
userspace? and it works??
- `tc` is a cool tool and it can program network cards to do amazing
things
- benchmarking networking algorithms is hard and it’s important to build
benchmarking tools
- even more information about XDP and why it’s fast!


### BBR talks


There were 2 talks about BBR! I was super confused at the beginning
because I came late and didn’t know what BBR was.


Here’s what I know so far.


TCP algorithms today all fundamentally interpret packet loss as
“congestion”. The idea is that – if packets are being lost along the
way, then there must be too much data being sent, so you should slow
down. TCP algorithms scale their “window size” up and down in response
to congestion. The window size is basically the amount of data that’s
you’re allowed to send before it being ACKed.


Today the TCP congestion control algorithm the Linux networking stack
uses is called CUBIC. But there is a new
congestion control algorithm on the block! It is called BBR and here’s
an [article from Google about it from Dec. 2016 in ACM Queue](http://queue.acm.org/detail.cfm?id=3022184).


BBR tries to

- estimate the round-trip time between you and your client
- estimate how much free bandwidth there is between you + your client


I think the idea here is that – if you know how much free bandwidth
there is between you and your client (“100MB/s”) then you should just
send that much data, even if there is some packet loss along the way.


I have no idea how BBR estimates how much bandwidth there is but that’s
a start. I’m planning to read the Google article about it.


The first talk (Driving Linux TCP Congestion Control algorithms around the LTE
network Highway by Jae Won Chung, Feng Li) was about using BBR with LTE (mobile) networks, I think.
I came in late and so I didn’t learn a lot but it sounded positive.


### linux kernel networking, in userspace


by Hajime Tazaki


The next talk was really cool! The idea was – maybe you want to use the
Linux network stack (because it is a mature network stack) but you want
to either

- use it on Linux, but with different options / a newer version
- use it on Windows/FreeBSD/some other operating system.


So basically instead of using Linux, you take all the Linux networking
code and just use it as a library!


This talk used the [linux kernel library project](https://github.com/lkl/linux), specifically to look at BBR performance inside LKL.


The speaker  went through a few different performance
problems he ran into.


The goal was to get the same performance with LKL as you would when
running the same code as Linux kernel code.


**first benchmark**


in their first benchmark, they set up two computers connected with a
10Gbps link, and tested Linux with BBR and LKL with BBR. At the
beginning, Linux was getting 9.4Gbps (good!) and LKL was doing 0.45 Gbps
(very bad!!)


The problem here was that BBR really needs accurate timing, and for some
reason the LKL implementation had really bad resolution (100HZ, so it
could be off by up to 5ms).


Increasing the resolution to 1000Hz (by changing the kernel jiffies
setting) made things way better (LKL got 6Gbps instead of 0.4), and
patching LKL


This seemed to be interesting to people because people **thought** that
BBR was really sensitive to inaccuracies in timing measurements, but
these experiments showed that you really did need to have accurate
timing. Cool!


**second benchmark**


In the second benchmark they added a bunch of latency between the two
systems (using tc!!). At the beginning Linux did 8.6Gbps (good!) and LKL
did 0.18Gbps (very very bad!).


It turned out that this was because the LKL box had a very small socket
buffer. This makes sense, I think! If you have more latency in your system, you’re
going to need more buffer space to store packets. So they had to set the sysctl
that Linux uses to control socket buffer size. This is easy to do in LKL!


### XDP mythbusters


by David Miller


There are basically an infinite number of XDP talks at this conference
:). This one basically listed a bunch of facts & myths about XDP. It was
pretty opinionated and I will reproduce the opinions here :)


**facts**

- XDP runs **when the device driver receives a packet**
- XDP can **modify packet contents**
- XDP **doesn’t do memory allocation** (so things go faster)
- XDP is **stateless** (so things go faster)


**reasons to use XDP**

- DDoS prevention
- load balancing
- collecting statistics about your packets
- sophisticated traffic sampling (with `perf_events`, you can come up
with fancy rules and decide what to sample)
- high frequency trading (“but they won’t tell us what they did, it’s
their secret sauce :)”)


**ebpf myth list**


the idea here is that the answer to all of these questions is “no”

- is XDP just a fad? “no”
- is XDP unsafe because you’re letting user code run in the kernel? “no,
the eBPF verifier checks that the code is safe. if you trust virtual
memory protection / the kernel to protect you from userspace, you
should trust this too!”
- is XDP less flexible than DPDK? (i didn’t understand why the answer is
“no” bc i don’t really understand what DPDK is, but he said you can
access kernel objects which is cool, and there’s “no container story”
for DPDK)
- is XDP a replacement for netfilter/tc? (“no, there’s some overlap, but
XDP has limits because it’s stateless”)


things that are going to be changing with XDP:

- more introspection
- debugging symbols, probably CTF and not DWARF because “DWARF is too
complicated”
- tracing with perf events


He also made a parallel with Arduino development – in arduino you make
some binary code and put it into your Arduino and it’s kind of the same
workflow as XDP. He also said “arduino doesn’t any introspection and
people love it” which is maybe true? Unclear. I love debugging tools a
lot :)


### new TC offloads


chair: Jamal Hadi Salim (who is also the conference chair and did a
really really wonderful job throughout). He told me things about tc at lunch
yesterday!


okay so – apparently TC (the tool that lets you slow your network down)
is actually a big deal and you can do a ton of stuff with it. I am only
slowly learning what all those things are.


One cool thing about TC is:

1. tc can do a lot of things (like delay packets, drop packets at
random, modify packets, do “traffic shaping” stuff)
2. for a lot of the things TC can do, it can also train your hardware
how to do it for you! which is faster! So you can buy a relatively
cheap network card and have it do operations on your packets for you,
that you program


Being able to program your network card to do stuff for you just by
running a thing on the command line seems pretty magical so I think I
understand why there was like 1.5 hours about new capabilities there.


I only used tc for the first time last week so I am still struggling to
understand what’s going on with it but here are some new tc subcommands:

- `pedit munge ip ttl add 255` (this actually *subtracts* 1 from the
TTL, it’s unsigned integer arithmetic)
- `pedit munge eth dst set 11:22:33:44:55:66` changes the destination
MAC address


and those are both things that you can program your network card to do,
if you have the right network card.


**testing**


tc is a userspace program, and it integrates pretty tightly with the
kernel, and it’s always getting new features, so it’s important to make
sure its features stay in sync.


Someone demoed a testing framework for tc where you define tests in
JSON, which seemed really nice!


### lunch (aka PCI bus time)


Yesterday there was a talk about virtualization and about how the PCI
bus is a bottleneck. I didn’t know what a PCI bus was so I asked
someone. He was like “is that a serious question” but he answered me!
Here is what I know so far about the PCI (or PCIe?) bus.

- it goes between your CPU and your network card (and other peripherals)
- but also actually sometimes the network card writes stuff directly
into RAM  through the PCI bus (with DMA?). [here is a blog post](https://geidav.wordpress.com/2014/04/27/an-overview-of-direct-memory-access/).
- its jobs is to send bytes from your network to your CPU, and vice
versa
- it is slower than your CPU
- usually the network card is slower than the PCI bus, so the PCI bus is
not the bottleneck, but sometimes when packets are too small, then
things get inefficient and the PCI bus becomes the bottleneck
- but why is it more inefficient?
- well – I’m still confused, but someone told me that when the network
card sends packets, it does not just send packets. It also sends you
metadata about those packets! So if there are more small packets,
there is more metadata, and that is inefficient.


I’m still pretty vague about all of this but I know more than yesterday
so that’s cool


### netesto


Lawrence Brakmo from Facebook demoed an interesting looking network testing
framework!


This also involved that BBR TCP congestion algorithm from before. He
emphasized that when you do the same networking tests between the same
computers under the same conditions, the results can be really
different! So it’s important to repeat your tests a lot of times.


He gave an example of a test with BBR: he tested having 2 TCP streams
(so you start sending data from A to B, and then 20 seconds in start
sending more data from C to B). He tested this 25 times, and 3 of those
25 times, the results were REALLY BAD. Like the second TCP stream only
got to 100Mbps bandwidth even though there was a lot more available.


He said this tool will appear at [https://github.com/facebook/fbkutils](https://github.com/facebook/fbkutils) by
April 14.


### that’s all!


Tomorrow is the last day, so more tomorrow.
