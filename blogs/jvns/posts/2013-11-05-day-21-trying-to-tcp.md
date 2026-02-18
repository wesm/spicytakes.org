---
title: "Day 21: Trying to TCP"
date: 2013-11-05
url: https://jvns.ca/blog/2013/11/05/day-21-trying-to-tcp/
slug: day-21-trying-to-tcp
word_count: 400
---


Today I started trying to write a TCP stack. In Python. We will see if
this is a good idea.


I’m using [scapy](http://www.secdev.org/projects/scapy/). I talked
about scapy on
[Thursday](http://jvns.ca/blog/2013/10/31/day-20-scapy-and-traceroute/)
– it’s a great tool for playing with low-level networking stuff in
Python.


So. I’ve gotten a TCP handshake working. The way this goes is you send a
SYN, then get back a SYN-ACK, then send an ACK.


I tried this TCP handshake code first:


```
dest = "google.com"
source_port += 1 # We need to set a different source port every time
ip_header = IP(dst=dest)
ans = sr1(ip_header / TCP(dport=80, flags="S", seq=random.randint(0, 1000))) # Send SYN, receive SYN-ACK
reply = ip_header / TCP(dport=80, seq=ans.ack, ack = ans.seq + 1, flags="A") # ACK
send(reply) # Send ACK

```


This did NOT WORK. Upon inspecting Wireshark, it turned out that *my* machine
was the problem: it was sending out a RST (reset) packet after I got a SYN-ACK
packet back from Google. What’s up with that?


Well, I already have a network stack on my machine, and it was like “what’s
this SYN-ACK packet? I didn’t ask for this!”. So it would just reset the
connection.


Jari (who is amazing) suggested a workaround: set up a fake IP address and
tell the router using ARP
([previously](http://jvns.ca/blog/2013/10/29/day-18-in-ur-connection/)) that
I am the person with that IP address. Here’s the fixed version:


I think I could also use iptables here to tell the kernel to ignore those
packets. But I’m currently afraid of iptables. So. This code worked much
better!


```
# Set port & MAC address
FAKE_IP = "10.0.4.4" # Use something that nobody else is going to have
MAC_ADDR = "60:67:20:eb:7b:bc" # My actual MAC address

# Broadcast our fake IP address
srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(psrc=FAKE_IP, hwsrc=MAC_ADDR))

source_port += 1
ip_header = IP(dst=dest, src=FAKE_IP) # Set the source port to 
ans = sr1(ip_header / TCP(dport=80, sport=source_port,  flags="S", seq=random.randint(0, 1000))) # SYN
# ans is the SYN-ACK
reply = ip_header / TCP(dport=80, sport=source_port, seq=ans.ack, ack = ans.seq + 1, flags="A") # ACK
send(reply) # Send ACK
pkt = ip_header / TCP(dport=80, sport=source_port, seq=reply.seq, flags="AP") / "GET / HTTP/1.1\r\n\r\n" # Send our real packet
send(pkt)

```


That is my small amount of code for the day. I also spend a ton of time reading
[the UDP handling code from the 4.4BSD network stack](https://github.com/denghuancong/4.4BSD-Lite/blob/master/usr/src/sys/netinet/udp_usrreq.c?source=cc).
I do not yet have anything intelligent to say about that, but it’s pretty interesting.
