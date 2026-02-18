---
title: "IP addresses & routing"
date: 2018-07-24
url: https://jvns.ca/blog/2018/07/24/ip-addresses-routing/
slug: ip-addresses-routing
word_count: 1428
---


Hello! Tomorrow I’m running a workshop at work about the humble IP address, so here are some notes
about IP addresses and how IP routing on Linux works!


This came up because someone on my team pointed out that there’s actually a LOT going on with IP
addresses even though it seems like a simple concept, and they said they’d like to learn more. Here
goes!


This post is only about IPv4 because I’ve still never used IPv6.


### What’s in the IP header?


Almost every packet your computer sends and receives (with some exceptions like [ARP packets](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)) has an IP header.


There are [14 fields](https://en.wikipedia.org/wiki/IPv4#Header) in the IP header. The only 3
important ones for most people to know about are:

- the source IP address
- the destination IP address
- the TTL (see: [how traceroute works](https://jvns.ca/blog/2013/10/31/day-20-scapy-and-traceroute/))


One thing you’ll notice **isn’t** in the IP header is a port! The TCP and UDP protocols both have
ports, but that lives at a different network layer. (and is why TCP port 8080 and UDP port 8080 are
different ports, and can run different services!)


There’s also a ‘protocol’ field that tells you the protocol (like TCP/UDP).


### What’s a subnet?


IP addresses are often grouped into **subnets**. The main useful thing to know about subnets is to
understand CIDR notation – `168.23.0.0/8` means “all the packets that have the same first 8 bits as
the packet `168.23.0.0`”. In this case that would be `168.*.*.*`, or any packet beginning in 168
(since each of the 4 numbers in an IP address is 8 bits).


## When I create a packet on my computer, what happens to it?


Suppose you create a packet with IP address 1.2.3.4 on it. Where does it go? It turns out that this
isn’t a super simple question – there are at least 3 possible systems that can affect your packet


### System 1: The route table


The most likely system to affect your new packet destined to `1.2.3.4` is the **route table**. On
Linux, you can view your route table with `ip route list table all`. Here’s what the route
table on my laptop looks like:


```
$ ip route list table all
default via 192.168.1.1 dev wlp3s0  proto static  metric 600 
169.254.0.0/16 dev docker0  scope link  metric 1000 linkdown 
172.17.0.0/16 dev docker0  proto kernel  scope link  src 172.17.0.1 linkdown 
192.168.1.0/24 dev wlp3s0  proto kernel  scope link  src 192.168.1.170  metric 600 
broadcast 127.0.0.0 dev lo  table local  proto kernel  scope link  src 127.0.0.1 
local 127.0.0.0/8 dev lo  table local  proto kernel  scope host  src 127.0.0.1 

```


Each of these routes has:

- a **subnet** (127.0.0.0/8, 172.17.0.0/16, etc)
- a **network device** (my wireless card `wlp3s0`, the virtual loopback device `lo`, the virtual
docker device `docker0`, etc)
- possibly something like `via 192.168.1.1` which means “send all packets like this to IP
192.168.1.1’s MAC address, which happens to be Julia’s router”
- a bunch of other stuff which I don’t understand that well (`metric 600`, `scope link`, `proto kernel`, etc). Not understanding what those things mean hasn’t hurt me yet.


The main things to pay attention to are the subnet and the network device. So `192.168.1.0/24 dev wlp3s0` means “send packets in the `192.168.1.0/24` range to the `wlp3s0` network device. That’s not
so complicated!


It’s useful to know a little bit about your Linux computer route table if you’re doing container
networking, because with containers you’ll end up with one or more virtual network devices (like
`docker0`) that packets will end up being sent to.


That’s it for the route table!


### System 2: iptables


Having read the above, you might think that the way packets get routed is:

1. they come into your computer
2. Linux looks at the route table and decides which network device to send to the packet to
3. That’s it


That’s often true, but not always!! There are a bunch of secret in between steps (“prerouting”,
“output”, “postrouting”) where Linux says “hey, iptables, want to make changes to this packet
here?”. When this happens, iptables can change the source or destination IP address on the packet to
be something different.


The two main things I’ve used this for are **DNAT** (“destination NAT”) and **SNAT** (“source NAT”)


**destination NAT**


Let’s start with destination NAT! One place this shows up is in this program called
[kube2iam](https://github.com/jtblin/kube2iam). kube2iam is this program that you run on your host
that pretends to be the AWS metadata endpoint (`169.254.169.254`). Why you might want this isn’t
important right now, but – how can kube2iam pretend to be this other IP address? That would mean
that we need to magically redirect those packets somehow? How?


It turns out that forcing packets destined for 169.254.169.254 to go somewhere else is totally
possible! Here’s the iptables rule that they suggest using:


```
iptables \
  --append PREROUTING \
  --protocol tcp \
  --destination 169.254.169.254 \
  --dport 80 \
  --in-interface docker0 \
  --jump DNAT \
  --table nat \
  --to-destination $YOUR_IP_ADDRESS:8181

```


Usually iptables rules make me want to hide under the couch but in the last year I’ve become a
little less afraid of them. Here’s what’s going on with this one:

- it only applies to tcp packets to 169.254.169.254 port 80 that came from the `docker0` interface (`--protocol tcp`, `--dport 80`, `--destination 169.254.168.254`, `--in-interface docker0`)
- it happens at the PREROUTING stage (before the packet gets assigned a network interface)
- it (`--jump DNAT`, `--table nat`, `--to-destination $YOUR_IP_ADDRESS:8181`)


What’s this DNAT thing? Basically what this means is that Linux won’t just rewrite packets to
169.254.169.254:80 to go to $LOCAL_IP:8081, it’ll also modify the reply packets from $LOCAL_IP:8081
to make them appear as if they came from 169.254.169.254. So from the perspective of the application
receiving the reply, it has no idea that it’s not talking to the IP 169.254.169.254. Lies!!!


To make all this work, Linux needs to keep track of connection state and remember “hey, this reply
packet is part of this DNATed connection so I need to rewrite it”


Phew. Hopefully that made any sense.


**source NAT**


Source NAT is like destination NAT, except instead of rewriting destination IP address,
it rewrites source IP addresses!


The place I’ve used source NAT before is also for container stuff – if you have a bunch of
containers with weird virtual container IP addresses sending packets to the outside world, you
can’t just let them use those IP addresses!! The outside world (like google) has no idea about your
container IPs and will not be able to reply to those packets. So you need to pretend that they come
from your host.


If this is you, you probably want an iptables rule something like this on your host:


```
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

```


`MASQUERADE` is a confusing way of saying “use source NAT and pretend the packet is coming from this
host’s IP address”. What this rule does is rewrite the source IP address on every packet to pretend
to be from the host’s IP.


### System 3: IPsec


I’m not going to go into this much (I wrote about [IPsec the other day](https://jvns.ca/blog/2018/07/11/netdev-day-1--ipsec/)),
but a third way packets can end up going to weird places is if you’re using IPsec. You can see
what’s going on there with the `ip xfrm` command. It turns out `xfrm` stands for “transform”.


### some notes on AWS networking


A lot of these concepts (a route table, NAT, IPSec) have their AWS networking analogs in [Amazon
Virtual Private Cloud (VPC)](https://aws.amazon.com/vpc/) – much like you can control how packets
get routed when they arrive on your Linux computer, you can use these AWS tools to control what
happens when you send packets from an instance in a VPC. I looked at the [VPC FAQ](https://aws.amazon.com/vpc/faqs/) today and it’s pretty good.


here are some very rough mappings

- route table: [VPC route table](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Route_Tables.html), which
controls how packets are routed in your VPC
- iptables/source NAT: [NAT gateway](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-nat-gateway.html) or [Internet Gateway](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Internet_Gateway.html). If you have
an AWS instance with no public IP address, you need to use source NAT (for the same reasons as we
talked about before with containers) to talk to the public internet. The way this works in AWS is you set up a NAT
gateway/internet gateway which will rewrite your packets for you.
- IPsec: [VPC peering](https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/Welcome.html). This
isn’t really the same thing (peering connections are only encrypted for cross-region traffic), but it does give you a way to
set up private connections between two different VPCs and I think it’s useful in some of the same
scenarios.
