---
title: "The OSI model doesn't map well to TCP/IP"
date: 2021-05-11
url: https://jvns.ca/blog/2021/05/11/what-s-the-osi-model-/
slug: what-s-the-osi-model-
word_count: 930
---


[TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite) is the set of networking protocols that we use on the modern internet –
TCP, UDP, IP, ARP, ICMP, DNS, etc. When I talk about “networking”, I’m
basically always talking about TCP/IP.


Many explanations of TCP/IP start with something called the “OSI model”. I
don’t use the OSI model when explaining networking because when I first
started learning about internet networking I found all of the OSI model
explanations really confusing – it wasn’t clear to me at all how the OSI
model corresponded to TCP/IP.


So if you’re just starting to learn about networking and you’re confused about
the OSI model, here’s an explanation of how it corresponds to TCP/IP, how
it doesn’t, and why it’s safe to mostly just ignore it if you don’t find it helpful.


### the OSI model has 7 layers


Let’s very briefly discuss what the OSI model is: it’s an abstract model for
how networking works with 7 numbered layers:

- Layer 1: physical layer
- Layer 2: data link
- Layer 3: network
- Layer 4: transport
- Layer 5: session
- Layer 6: presentation
- Layer 7: application


I won’t say more about what each of those is supposed to mean, there are a
thousand explanations of it online.


### how the OSI model corresponds to TCP/IP


Some parts of the OSI model do correspond to TCP/IP. Basically for any TCP or
UDP packet you can split up the packet into different sections and give each
section a layer number.

- Layer 2 corresponds to Ethernet
- Layer 3 corresponds to IP
- Layer 4 corresponds to TCP or UDP (or ICMP etc)
- Layer 7 corresponds to whatever is inside the TCP or UDP packet (for example a DNS query)


Here’s a diagram from my [Networking! ACK!](https://wizardzines.com/zines/networking/) zine showing how you can
assign layers to different parts of a packet.


![](https://jvns.ca/images/networking-layers.png)


Now that we’ve talked about how the OSI model does correspond to TCP/IP, let’s
talk about how it doesn’t!


### people refer to layers 2, 3, 4, and 7 all the time


It’s important to know about the OSI model because the terms “layer 2”, “layer
3”, “layer 4” and “layer 7” are used a LOT. You’ll hear about “layer 2
routing”, “layer 7 load balancers”, “layer 4 load balancers”, etc.


So even thought I don’t really use those terms myself when talking about
networking, I need to understand them to be able to read documentation and
understand what people are saying.


### there’s no layer 5 or 6 in TCP/IP


I’ve heard a few different interpretations of what layers 5 or 6 could mean in
TCP/IP, including:

- TLS is layer 6
- TCP is actually layers 5 + 6 + 7 smushed together


But layers 5 and 6 definitely don’t have a clear correspondence like “every
layer has a corresponding header in the TCP packet” the way layers 2, 3, and 4
do.


And I’ve never seen anyone actually refer to layer 5 or 6 in practice when
talking about TCP/IP, even though people talk about layers 2, 3, 4, and 7 all
the time.


### what layer is an ARP packet?


Also, some parts of TCP/IP don’t fit well into the OSI model even around
layers 2-4 – for example, what layer is an ARP packet?


ARP is a protocol for discovering what MAC address corresponds to an IP
address: when a machine wants to know who has a certain IP address, it sends
out an ARP message saying “help! who is 192.168.1.1?” and it’ll get a response
from the owner of the IP saying “it’s me! I’m 192.168.1.1”


ARP packets contain IP addresses and IP addresses are layer 3, but when people
talk about “layer 3” packets they usually mean a packet which have an IP header, and
ARP packets don’t have an IP header, they just have an Ethernet header and
then some data on top of that which contains an IP.


### the OSI model is a literal description of some obsolete protocols


So, if the OSI model doesn’t literally describe TCP/IP, where did it come
from?


Some very brief research on Wikipedia says that in addition to an abstract
description of 7 layers, the OSI model also contained a [bunch of specific
protocols implementing those
layers](https://en.wikipedia.org/wiki/OSI_protocols). Apparently this happened
during the [Protocol Wars](https://en.wikipedia.org/wiki/Protocol_Wars) in the
70s and 80s, where the OSI model lost and TCP/IP won.


This explains why the OSI model doesn’t really correspond that well to TCP/IP,
since if the OSI protocols had “won” then the OSI model *would* correspond
exactly to how internet networking actually works.


### you can talk about specific network protocols instead of using layer numbers


When talking about networking, instead of using numbered layers I like to
instead just talk about specific networking protocols I mean. Like
instead of “layer 2” I’ll use something like “Ethernet” or “MAC address”. I’ve
written many blog posts talking about MAC addresses and zero posts talking
about “layer 2”.


As another example, when talking about load balancers usually I say “HTTP load
balancer” instead of “layer 7 load balancer”. Basically every layer 7 load
balancer I’ve used has been a HTTP load balancer, and if it’s not using HTTP
then I’d rather know which other protocol it’s using!


### that’s all!


Hopefully this will help clear things up for somebody!  I wish someone had
told me when I started learning networking that I could just learn
approximately how layers 2, 3, 4, and 7 of the OSI model relate to TCP/IP and
then ignore everything else about it.
