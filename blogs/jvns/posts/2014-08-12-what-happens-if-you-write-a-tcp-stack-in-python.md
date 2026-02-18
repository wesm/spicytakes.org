---
title: "What happens if you write a TCP stack in Python?"
date: 2014-08-12
url: https://jvns.ca/blog/2014/08/12/what-happens-if-you-write-a-tcp-stack-in-python/
slug: what-happens-if-you-write-a-tcp-stack-in-python
word_count: 1070
---


During Hacker School, I wanted to understand networking better, and I
decided to write a miniature TCP stack as part of that. I was much
more comfortable with Python than C and I’d recently discovered the
[scapy](http://www.secdev.org/projects/scapy/) networking library
which made sending packets
[really easy](http://jvns.ca/blog/2013/10/31/day-20-scapy-and-traceroute/).


So I started writing [teeceepee](https://github.com/jvns/teeceepee)!


The basic idea was

1. open a raw network socket that lets me send TCP packets
2. send a HTTP request to `GET` google.com
3. get and parse a response
4. celebrate!


I didn’t care much about proper error handling or anything; I just
wanted to get one webpage and declare victory :)


## Step 1: the TCP handshake


I started out by doing a TCP handshake with Google! (this won’t
necessarily run correctly, but illustrates the principles). I’ve
commented each line.


The way a TCP handshake works is:

- me: SYN
- google: SYNACK!
- me: ACK!!!


Pretty simple, right? Let’s put it in code.


```
# My local network IP
src_ip = "192.168.0.11"
# Google's IP
dest_ip = "96.127.250.29"
# IP header: this is coming from me, and going to Google
ip_header = IP(dst=dest_ip, src=src_ip)
# Specify a large random port number for myself (59333),
# and port 80 for Google The "S" flag means this is
# a SYN packet
syn = TCP(dport=80, sport=59333, 
          ack=0, flags="S")
# Send the SYN packet to Google
# scapy uses '/' to combine packets with headers
response = srp(ip_header / syn)
# Add the sequence number 
ack = TCP(dport=80, sport=self.src_port, 
          ack=response.seq, flags="A") 
# Reply with the ACK
srp(ip_header / ack)

```


### Wait, sequence numbers?


What’s all this about sequence numbers? The whole point of TCP is to
make sure you can resend packets if some of them go missing. Sequence
numbers are a way to check if you’ve missed packets. So let’s say that
Google sends me 4 packets, size 110, 120, 200, and 500 bytes. Let’s
pretend the initial sequence number is 0. Then those packets will have
sequence numbers 0, 110, 230, and 430.


So if I suddenly got a 100-byte packet with a sequence number of 2000,
that would mean I missed a packet! The next sequence number should be
930!


How can Google know that I missed the packet? Every time I receive a
packet from Google, I need to send an ACK (“I got the packet with
sequence number 230, thanks!”). If the Google server notices I haven’t
ACKed a packet, then it can resend it!


The TCP protocol is extremely complicated and has all kinds of rate
limiting logic in it, but we’re not going to talk about any of that.
This is all you’ll need to know about TCP for this post!


For a more in-depth explanation, including how SYN
packets affect sequence numbers, I found
[Understanding TCP sequence numbers](http://packetlife.net/blog/2010/jun/7/understanding-tcp-sequence-acknowledgment-numbers/)
very clear.


## Step 2: OH NO I already have a TCP stack


So I ran the code above, and I had a problem. IT DIDN’T WORK.


But in a kind of funny way! I just didn’t get any responses. I looked
in Wireshark (a wonderful tool for spying on your packets) and it
looked like this:


```
me: SYN
google: SYNACK
me: RST

```


Wait, what? I never sent a `RST` packet?! `RST` means STOP THE
CONNECTION IT’S OVER. That is not in my code at all!


This is when I remembered that I *already* have a TCP stack on my
computer, in my kernel. So what was actually happening was:


```
my Python program: SYN
google: SYNACK
my kernel: lol wtf I never asked for this! RST!
my Python program: ... :(

```


So how do we bypass the kernel? I talked to the delightful
[Jari Takkala](https://github.com/jtakkala) about this, and he
suggested using
[ARP spoofing](http://jvns.ca/blog/2013/10/29/day-18-in-ur-connection/)
to pretend I had a different IP address (like `192.168.0.129`).


The new exchange was like this:


```
me: hey router! send packets for 192.168.0.129 to my MAC address
router: (does it silently)
my Python program: SYN (from 192.168.0.129)
google: SYNACK
kernel: this isn't my IP address! <ignore>
my Python program: ACK YAY

```


And it worked! Okay, awesome, we can now send packets AND GET
RESPONSES without my kernel interfering! AWESOME.


## Step 3: get a webpage!


There is an intervening step here where I fix tons of irritating bugs
preventing Google from sending me the HTML for [http://google.com](http://google.com). I
eventually fixed all of these, and emerge victorious!


I needed to

- put together a packet containing a HTTP GET request
- make sure I can listen for *lots* of packets in response, not just
one
- spend a lot of time fixing bugs with sequence numbers
- try to close the connection properly


## Step 4: realize Python is slow


Once I had everything working, I used Wireshark again to look at what
packets were being sent back and forth. It looked something like this:


```
me/google: <tcp handshake>
me: GET google.com
google: 100 packets
me: 3 ACKs
google: <starts resending packets>
me: a few more ACKs
google: <reset connection>

```


The sequences of packets from Google and ACKs from me looked something
like: P P P A P P P P P A P P A P P P P A. Google was sending me
packets *way* faster than my program could keep up and send ACKs.
Then, hilariously, Google’s server would assume that there were
network problems causing me to not ACK its packets.


And it would eventually reset the connection because it would decide
there were connection problems.


But the connection was fine! My program was totally responding! It was
just that my Python program was way too slow to respond to packets in
the millisecond times it expected.


(edit: this diagnosis seems to be incorrect :) you can
[read some discussion](https://news.ycombinator.com/item?id=8167546)
about what may be actually going on here)


## life lessons


If you’re actually writing a production TCP stack, don’t use Python.
(surprise!) Also, the TCP spec is really complicated, but you can get
servers to reply to you even if your implementation is extremely sketchy.


I was really happy that it actually worked, though! The ARP spoofing
was extremely finicky, but I wrote a version of `curl` using it which
worked about 25% of the time. You can see all the absurd code at
[https://github.com/jvns/teeceepee/](https://github.com/jvns/teeceepee/).


I think this was actually way more fun and instructive than trying to
write a TCP stack in an appropriate language like C :)
