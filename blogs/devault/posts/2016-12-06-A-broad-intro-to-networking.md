---
title: "A broad intro to networking"
date: 2016-12-06
url: https://drewdevault.com/2016/12/06/A-broad-intro-to-networking.html
slug: A-broad-intro-to-networking
word_count: 2159
---

Disclaimer: I am not a network engineer. That’s the point of this blog post,
though - I want to share with non-networking people enough information about
networking to get by. Hopefully by the end of this post you’ll know enough about
networking to keep up with a conversation on networking, or know what to search
for when something breaks, or know what tech to research more in-depth when you
are putting together something new.

## Layers

The  **OSI model**  is the standard model we describe networks with. There are 7
 **layers** :

Layer 1, the physical layer, is the electrical engineering stuff.

Layer 2, the link layer, is how devices talk to each other.

Layer 3, the network layer, is what they talk about.

Layer 4, the transport layer, is where things like TCP and UDP live.

Layers 5 and 6 aren’t very important.

Layer 7, the application layer, is where Minecraft lives.

When you hear some security guy talking about a “layer 7 attack”, he’s
talking about a attack that focuses on flaws in the application layer. In
practice that means i.e. flooding the server with HTTP requests.

## 1: Physical Layer

*Generally implemented by matter*

Layer 1 is the hardware of a network. Commonly you’ll find things here like your
computer’s  **NIC**  (network interface controller), aka the network interface or
just the interface, which is the bit of silicon in your PC that you plug network
cables or WiFi signals into.

On Linux, network interfaces are assigned names like  *eth0*  or  *eno1* . eth0 is
the traditional name for the 0th wired network interface. eno1 is the newer
“consistent network device naming” format popularized by tools like udev (which
manages hardware on many Linux systems) - this is a deterministic name based on
your network hardware, and won’t change if you add more interfaces. You can
manage your interfaces with the  *ip*  command ( `man 8 ip` ), or the now-deprecated
 *ifconfig*  command. Some non-Linux Unix systems have not deprecated ifconfig.

This layer also has ownership over  **MAC addresses** , in theory. A MAC address
is an allegedly unique identifier for a network device. In practice, software
at higher layers can use whatever MAC address they want. You can change your MAC
address with the ip command, which is often useful for dealing with annoying
public WiFi resource limits or for frustrating someone else on the network.

Other things you find at layer 1 include  **switches** , which do network
multiplexing (they generally can be thought of as networking’s version of a
power strip - they turn one Ethernet port into many). Also common are
 **routers** , whose behaviors are better explained in other layers. You also have
hardware like  **firewalls** , which filter network traffic, and  **load
balancers** , which distribute a load among several nodes. Both firewalls and
load balancers can be done in software, depending on your needs.

## 2: Data link layer

*Generally implemented by network hardware*

At this layer you have protocols that cover how nodes talk to one another. Here
the  **ethernet**  protocol is almost certainly the most common - the protocol
that goes over your network cables. Said network cables are probably  **Cat 5** 
cables, or “category 5” cables.

Other protocols here include tunnels, which allow you to indirectly access a
network. A common example is a  **VPN** , or virtual private network, which allows
you to participate in another network remotely. Tunnels can also be useful for
getting around firewalls, or for setting up a secure means to access resources
on another network.

## 3: Network layer

*Generally implemented by the kernel*

As a software guy, this is where the fun really starts. The other layers are how
computers talk to each other - this layer is what they talk about. Computers are
often connected via a  **LAN** , or local area network - a  *local*  network of
computers. Computers are also often connected to a  **WAN** , or wide area
network - the internet is one such network.

The most common protocol at this layer is IP, or Internet Protocol. There are
two versions that matter: IPv4, and IPv6. Both of them use  **IP addresses**  to
identify nodes on their networks, and they carry  **packets**  between them. The
major difference between IPv4 and IPv6 is the size of their respective  **address
spaces** . IPv4 uses 32 bit addresses, supporting a total of 4.3 billion possible
addresses, which on the public internet are quickly becoming a sparse resource.
IPv6 uses 128-bit addresses, which allows for a zillion unique addresses.

Ranges of IP addresses can be described with a  **subnet mask** . Such a range of
IP addresses constitutes a  **subnetwork** , or subnet. Though you’re probably
used to seeing an IPv4 address encoded like  `10.20.30.40` , remember that it can
also just be represented as one 32-bit number - in this case 169090600, or
0xA141E28, and you can do bitwise math against these numbers. You generally
represent a subnet with CIDR notation, such as  `192.168.1.0/24` . In this case, the
first 24 bits are meaningful, and all possible values for the remaining 8 bits
constitute the range of addresses represented by this mask.

IPv4 has several subnets reserved for this and that. Some important ones are:

* `0.0.0.0/8`  - current network. On many systems, you can treat  `0.0.0.0`  as all
IP addresses assigned to your device
* `127.0.0.0/8`  - loopback network. These addresses refer to yourself.
* `10.0.0.0/8` ,  `172.16.0.0/12` , and  `192.168.0.0/16`  are reserved for private
networks - you can allocate these addresses on a LAN.

An IPv4 packet includes, among other things: a  **time to live** , or TTL, which
limits how long the packet can live for; the  **protocol** , such as TCP; the
 **source**  and  **destination**  addresses; a header checksum; and the
 **payload** , which is specific to the higher level protocol in use.

Given the limited size of the IPv4 space, most networks are designed with an
isolated LAN that uses  **NAT** , or network address translation, to translate IP
addresses from the WAN. Basically, a router or similar component will translate
internal IP addresses (allocated from the private subnets) to its own external
IP address, and vice versa, when passing communications along to the WAN. With
IPv6 there are so many IP addresses that you don’t need to use NAT. If you’re
wondering whether or not we’ll ever run out of IPv6 addresses - leave that to
someone else to solve tens of millions of years from now.

IPv6 addresses are 128-bits long and are described with strings like
 `2001:0db8:0000:0000:0000:ff00:0042:8329` . Luckily the people who designed it
were kind enough to realize people don’t want to write that, so it can be
shortened to  `2001:db8::ff00:42:8329`  by removing leading zeros and removing
sections entirely composed of zeros. Where colons are reserved for another
purpose, you’ll typically add brackets around the IPv6 address, such as
 `http://[2607:f8b0:400d:c03::64]` . The IPv6 loopback address (localhost) is
 `::1` , and IPv6 subnets are written the same way as in IPv4. Given how many
IPv6 addresses there are, it’s common to be allocated lots of them in cases when
you might have expected to only receive one IPv4 address. Typically these blocks
will be anywhere from /48 to /56 - which contains more addresses than the entire
IPv4 space.

IP addresses are often  **static** , which means the node connecting to the
network already knows its IP address and starts using it right away. They may
also be  **dynamic** , and are allocated by some computer on the network with the
 **DHCP**  protocol.

IPsec also lives in layer 3.

## 4: Transport Layer

*Generally implemented by the kernel*

The transport layer is where you have higher level protocols, through which much
of the work gets done. Protocols here include TCP, UDP, ICMP (used for ping),
and others. These protocols are used to power application-layer protocols.

**TCP** , or the transmission control protocol, is probably the most popular
transport layer protocol out there. It turns the unreliable internet protocol
into a reliable byte stream. TCP (tries to) make four major guarantees: data
will arrive, will arrive exactly once, will arrive in the correct order, and
will be the correct data.

TCP takes a stream of bytes and breaks it up into  **segments** . Each segment is
then stuck into an IP packet and sent on its way. A TCP segment includes the
source and destination  **ports** , which are used to distinguish between
different application-layer protocols in use and to distinguish between
different applications using the protocol on the same host; a  **sequence
number** , which is used to order the packet; an  **ACK number** , which is used to
inform the other end that it has received some packet and it can stop retrying;
a checksum; and the data itself. The protocol also includes a handshake process
and other housekeeping processes that the application needn’t be aware of.
Generally speaking, the overhead of TCP is significant for real-time
applications.

Most TCP servers will  **bind**  to a certain port to  **listen**  for incoming
connections, via the operating system’s  **socket**  implementation. Many TCP
 **clients**  can connect to one server.

Ports are a 16 bit unsigned integer. Most applications have a default port
they’re known to use, such as 80 for HTTP. Originally these numbers were
allocated by the internet police, but this has fallen out of practice. On most
systems, ports less than 1024 require elevated permissions to listen to.

**UDP** , or the user datagram protocol, is the second most popular transport
layer protocol, and is the lighter of the two. UDP is a paper thin layer on top
of IP. A UDP packet contains a source port, destination port, checksum, and a
payload. This protocol is fast and lightweight, but makes none of the promises
TCP makes - UDP “ **datagrams** ” may arrive multiple or zero times, in a
different order than they were sent, and possibly with data errors. Many people
who use UDP will implement these guarantees themselves in a some lighter-weight
fashion than TCP. Importantly, UDP source IPs can be spoofed and the destination
has no means of knowing where it really came from - TCP avoids this by doing a
handshake before exchanging any data.

UDP can also issue broadcasts, which are datagrams that are sent to every node
on the network. Such datagrams should be addressed to  `255.255.255.255` . There’s
also multicast, which specifies a subset of all nodes to send the datagram to.
Note that both of these have limited support in real-world networks.

## 5 & 6: Session and presentation

Think of these as extensions of layer 7, the application layer. Technically
things like SSL, compression, etc are done here, but in practice it doesn’t
have any important technical implications.

## 7: Application layer

*Generally implemented by end-user software*

The application layer is the uppermost layer of the network and it’s what all
the other layers are there for. At this layer you have all of the hundreds of
thousands of application-specific protocols out there.

**DNS** , or the domain name system, is a protocol for mapping domain names (i.e.
google.com) to IP addresses (i.e. 209.85.201.100), among other features. DNS
servers keep track of DNS records, which associate names with records of various
types. Common records include A, which maps a name to an IPv4 address, AAAA for
IPv6, CNAME for aliases, and MX for email records. The most popular DNS server
is bind, which you can run on your own network to operate a private name system.

Some other UDP protocols: NTP, the network time protocol; DHCP, which assigns
dynamic IP addresses on networks; and nearly all real-time video and audio
streaming protocols (like VoIP). Many video games also use UDP for their
multiplayer networking.

TCP is more popular than UDP and powers many, many, many applications, due
largely to the fact that it simplifies the complex intricacies of networking.
You’re probably familiar with HTTP, which is used by web browsers use to fetch
resources. Email applications often communicate over TCP with IMAP to retrieve
the contents of your inbox, and SMTP to send emails to other servers. SSH (the
secure shell), FTP (file transfer protocol), IRC (internet relay chat), and
countless other protocols also use TCP.

Hopefully this article helps you gain a general understanding of how computers
talk to each other. In my own experience, I’ve used a broad understanding of the
entire stack and a deep understanding of levels 3 and up. I expect most
programmers today need a broad understanding of the entire stack and a deep
understanding of level 7, and I hope that most programmers would seek a deep
understanding of level 4 as well.

Please leave some feedback if you appreciated this article - I may do more
similar articles in the future, giving a broad introduction to other topics. The
next topics I have in mind are security and encryption (as separate posts).
