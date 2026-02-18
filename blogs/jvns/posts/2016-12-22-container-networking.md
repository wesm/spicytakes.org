---
title: "A container networking overview"
date: 2016-12-22
url: https://jvns.ca/blog/2016/12/22/container-networking/
slug: container-networking
word_count: 2462
---


I’ve been talking about container things a bunch on this blog, mostly
because I’ve been looking at them at work.


One of the hardest things to understand about all this newfangled
container stuff is – what is even going *on* with the networking?!


There are a lot of different ways you can network containers together,
and the documentation on the internet about how it works is often pretty bad. I
got really confused about all of this, so I’m going to try to explain what it
all is in laymen’s terms.


(I don’t like to rant here, but I really have been frustrated with the state of
the documentation on this networking stuff.)


### what even is container networking?


When you run a program in a container, you have two main options:

- run the program in the host network namespace. This is normal networking – if you run a program on port 8282, it will run on port 8282 on the computer. No surprises.
- run the program in its *own* network namespace


If you have a program running in its own network namespace (let’s say on port
9382), other programs on other computers need to be able to make
network connections to that program.


At first I thought “how complicated can that be? connecting
programs together is simple, right?” Like, there’s probably only one way to do
it? It turns out that this problem of how to connect two programs in containers
together has a ton of different solutions. Let’s learn what those solutions
are!


### “every container gets an IP”


If you are a container nerd these days, you have probably heard of
[Kubernetes](http://kubernetes.io/). Kubernetes is a system that will take a container and
automatically decide which computer your container should run on. (among
other things)


One of Kubernetes’ core requirements (for you to even start using it) is
that **every** container has to have an IP address, and that any other
program inside you cluster can talk to your container **just using that
IP address**. So this might mean that on one computer you might have
containers with hundreds or thousands of IP addresses (instead of just
one IP address and many ports).


When I first heard of this “every container gets an IP” concept I was
really confused and kind of concerned. How would this even work?! My
computer only has one IP address! This sounds like weird confusing
magic! Luckily it turns out that, as with most computer things, this is
actually totally possible to understand.


This “every container gets an IP” problem is what I’m going to explain
in this blog post. There are other ways to network containers, but it’s
going to take long enough already to just explain this one :)


I’m also going to restrict myself to mostly talking about how to make this work
on **AWS**. If you have your own physical datacenter there are more options.


### Our goal


You have a  computer (AWS instance). That computer has an IP address (like
172.9.9.9).


You want your **container** to also have an IP address (like 10.4.4.4).


We’re going to learn how to get a packet sent to 10.4.4.4 on the computer
172.9.9.9.


On AWS this can actually be super easy – there are these things called
“VPC Route Tables”, and you can just say “send packets for 10.4.4.* to
172.9.9.9 please” and AWS will make it work for you. The catch is you can
only have 50 of these rules, so if you want to have a cluster of more
than 50 instances, you need to go back to being confused about
networking.


### some networking basics: IP addresses, MAC addresses, local networks


In order to understand how you can have hundreds of IP addresses on one
single machine, we need to understand a few basic things about
networking.


I’m going to take for granted that you know:

- In computer networking, programs send **packets** to each other
- Every packet (for the most part) has an **IP address** on it
- On Linux, the kernel is responsible for implementing most networking
protocols
- a little bit about **subnets**: the subnet 10.4.4.0/24 means “every IP
from 10.4.4.0 to 10.4.4.255”. I’ll sometimes write 10.4.4.* to mean this.


I’ll do my best to explain the rest.


**Thing 0: parts of a network packet**


A network packet has a bunch of different parts (often called “layers”). There
are a lot of different kinds of network packets, but let’s just talk about a
normal HTTP request (like `GET /`). The parts are:

1. the MAC address this packet should go to (“Layer 2”)
2. the source IP and destination IP (“Layer 3”)
3. the port and other TCP/UDP information (“Layer 4”)
4. the contents of your HTTP packet  like `GET /` (“Layer 7”)


**Thing 1: local networking vs far-away networking**


When you send a packet **directly** to a computer (on the same local network),
here’s how it works.


Packets are addressed by **MAC address**. My MAC address is
`3c:97:ae:44:b3:7f`; I found it by running `ifconfig`.


```
bork@kiwi~> ifconfig
enp0s25   Link encap:Ethernet  HWaddr 3c:97:ae:44:b3:7f 

```


So to send a packet to me, any computer on my local network can write
`3c:97:ae:44:b3:7f` on it, and it gets to my computer. In AWS, “local network”
basically means “availability zone”. If two instances are in the **same AWS
availability zone**, they can just put the MAC address of the target computer
on it, and then the packet will get to the right place. It doesn’t matter what
IP address is on the packet!


Okay, what if my computer **isn’t** in the same local network / availability
zone as the target computer? What then? Then **routers** in the middle need to
look at the IP address on the packet and get it to the right place.


There is a lot to know about how routers work, and we do not have time to learn
it all right now. Luckily, in AWS you have basically no way to configure the
routers, so it doesn’t matter if we don’t know how they work! To send a
packet to an instance outside your availability zone, you need to put that
instance’s IP address on it. Full stop. Otherwise it ain’t gonna get there.


If you manage your own datacenter, you can do clever stuff to set up your
routers.


So! Here’s what we’ve learned, for AWS:

- if you’re in the same AZ as your target, you can just send a packet with any
random IP address on it, and as long as the MAC address is right it’ll get
there.
- if you are in a different AZ, to send a packet to a computer, it has to have the IP address of that instance on it.


### The route table


You may be wondering “julia, but how can I **control** the MAC address my
packet gets sent to! I have never done that ever! That is very confusing!”


When you send a packet to `172.23.2.1` on your local network, your operating
system (Linux, for our purposes) looks up the MAC address for that IP address
in a table it maintains (called the ARP table). Then it puts that MAC address on the packet and sends it off.


So! What if I had a packet for the container `10.4.4.4` but I actually wanted it
to go to the computer `172.23.1.1`? It turns out this actually easy peasy! You
just add an entry to another table. It’s all tables.


Here’s command you could run to do this manually:


```
sudo ip route add 10.4.4.0/24 via 172.23.1.1 dev eth0

```


`ip route add` adds an entry to the **route table** on your computer. This
route table entry says “Linux, whenever you see a packet for `10.4.4.*`, just
send it to the MAC address for `172.23.2.1`, would ya darling?”


### we can give containers IPs!


It is time celebrate our first victory! We now know
all the basic tools for one main way to route container IP addresses!


The steps are:

1. pick a different subnet for every computer on your network (like 10.4.4.0/24 – that’s 10.4.4.*). That subnet will let you have 256 containers per machine.
2. On every computer, add **routes** for every other computer. So you’d add a route for 10.4.1.0/24, 10.4.2.0/24, 10.4.3.0/24, etc.
3. You’re done! Packets to 10.4.4.4 will now get routed to the right computer. There’s still the question of what they will do when they **get** to that computer, but we’ll get there in a bit.


So our first tool for doing container networking is the **route table**.


### what if the two computers are in different availability zones?


We said earlier that this route table trick will only work if the computers are
connected directly. If the two computers are far apart (in different local
networks) we’ll need to do something more complicated.


We want to send a packet to the container IP 10.4.4.4, and it is on the computer
172.9.9.9. But because the computer is far away, we **have** to address the
packet to the IP address 172.9.9.9. Woe is us! All is lost! Where are we going
to put the IP address 10.4.4.4?


**Encapsulation**


All is not lost. We can do a thing called “encapsulation”. This is where you
take a network packet and put it inside ANOTHER network packet.


So instead of sending


```
IP: 10.4.4.4
TCP stuff
HTTP stuff

```


we will send


```
IP: 172.9.9.9
(extra wrapper stuff)
IP: 10.4.4.4
TCP stuff
HTTP stuff

```


There are at least 2 different ways of doing encapsulation: there’s “ip-in-ip” and “vxlan” encapsulation.


**vxlan** encapsulation takes your whole packet (including the MAC address) and
wraps it inside a UDP packet. That looks like this:


```
MAC address: 11:11:11:11:11:11
IP: 172.9.9.9
UDP port 8472 (the "vxlan port")
MAC address: ab:cd:ef:12:34:56
IP: 10.4.4.4
TCP port 80
HTTP stuff

```


**ip-in-ip** encapsulation just slaps on an extra IP header on top of your old
IP header. This means you don’t get to keep the MAC address you wanted to send
it to but I’m not sure why you would care about that anyway.


```
MAC:  11:11:11:11:11:11
IP: 172.9.9.9
IP: 10.4.4.4
TCP stuff
HTTP stuff

```


**How to set up encapsulation**


Like before, you might be thinking “how can I get my kernel to do this weird
encapsulation thing to my packets”? This turns out to be not all that hard.
Basically all you do is set up a new **network interface** with encapsulation
configured.


On my laptop, I can do this using: (taken from [these instructions](http://www.linux-admins.net/2010/09/tunneling-ipip-and-gre-encapsulation.html))


```
sudo ip tunnel add mytun mode ipip remote 172.9.9.9 local 10.4.4.4 ttl 255
sudo ifconfig mytun 10.42.1.1

```


Then you set up a route table, but you tell Linux to route the packet with your
new magical encapsulation network interface. Here’s what that looks like:


```
sudo route add -net 10.42.2.0/24 dev mytun
sudo route list 

```


I’m mostly giving you these commands to get an idea of the kinds of commands
you can use to create / inspect these tunnels (`ip route list` , `ip tunnel`,
`ifconfig`) – I’ve almost certainly gotten a couple of the specifics wrong,
but this is about how it works.


### How do routes get distributed?


We’ve talked a lot about adding routes to your route table (“10.4.4.4 should go
via 172.9.9.9”), but I haven’t explained at all how those routes should actually
**get** in your route table. Ideally you’d like them to configured automatically.


Every container networking thing to runs **some** kind of daemon program
on every box which is in charge of adding routes to the route table.


There are two main ways they do it:

1. the routes are in an etcd cluster, and the program talks to the etcd cluster to figure out which routes to set
2. use the **BGP** protocol to gossip to each other about routes, and a daemon (`BIRD`) listens for BGP messages on every box


## What happens when packets get to your box?


So, you’re running Docker, and a packet comes in on the IP address 10.4.4.4. How
does that packet actually end up getting to your program?


I’m going to try to explain **bridge networking** here. I’m a bit fuzzy on this
so some of this is probably wrong.


My understanding right now is:

- every packet on your computer goes out through a real interface (like `eth0`)
- Docker will create **fake** (virtual) network interfaces for every single one of your containers. These have IP addresses like 10.4.4.4
- Those virtual network interfaces are **bridged** to your real network interface. This means that the packets get copied (?) to the network interface corresponding to the real network card, and then sent out to the internet


This seems important but I don’t totally get it yet.


## finale: how all these container networking things work


Okay! Now we we have all the fundamental concepts you need to know to navigate
this container networking landscape.


**Flannel**


Flannel supports a few different ways of doing networking:

- **vxlan** (encapsulate all packets)
- **host-gw** (just set route table entries, no encapsulation)


The daemon that sets the routes gets them from an etcd cluster.


**Calico**


Calico supports 2 different ways of doing networking:

- **ip-in-ip** encapsulation
- “regular” mode, (just set route table entries, no encapsulation)


The daemon that sets the routes gets them using BGP messages from other hosts.
There’s still an etcd cluster with Calico but it’s not used for distributing
routes.


The most exciting thing about Calico is that it has the option to not use
encapsulation. If you look carefully though you’ll notice that Flannel also has
an option to not use encapsulation! If you’re on AWS, I can’t actually tell
which of these is better. They have the same limitations: they’ll both only
work between instances in the same availability zone.


Most of these container networking things will set up all these routes and
tunnels and stuff for you, but I think it’s important to understand what’s
going on behind the scenes, so that if something goes wrong I can debug it and
fix it.


### is this software defined networking?


I don’t know what software defined networking. All of this helps you do
networking differently, and it’s all software, so maybe it’s software defined
networking?


### that’s all


That’s all I have for now! Hopefully this was helpful. It turns out this stuff
isn’t so bad, and spending some time with the `ip` command, `ifconfig` and
`tcpdump` can help you understand the basics of what’s going on in your
Kubernetes installation. You don’t need to be an expert network engineer! My
awesome coworker Doug helped me understand a lot of this.


Thanks to Sophie Haskins for encouraging me to publish this :)
