---
title: "Day 18: ARP cache poisoning (or: In ur connection, sniffing ur packets)"
date: 2013-10-29
url: https://jvns.ca/blog/2013/10/29/day-18-in-ur-connection/
slug: day-18-in-ur-connection
word_count: 589
---


Today I learned how to steal packets on a wireless network! If you want to try
this one at home, you’ll need

- `dsniff` (in the Ubuntu repositories)
- [Wireshark](http://wireshark.org)
- At least 2 devices on a network (like a smartphone and a computer)


This finally pretty much only involved one line of code. Here it is:


```
  $ sudo arpspoof -i wlan0 -t 192.168.0.13 192.168.0.1 
```


Okay, so what does this even mean, right?


`192.168.0.13` is my phone’s IP address on the local network.
`192.168.0.1` is the address of the router.


What this line basically does is “Hey phone! You want to send a packet to the
router? Send that to me instead. Thanks!”


This exploitation technique is called “ARP cache poisoning”. Apparently when
my computer needs to communicate with an IP address (like 192.168.1.68), it
*actually* needs to look up the MAC address for that IP address and send
packets to the MAC address. If it needs to send packets to the outside world
it sends them to its router first, so it needs the router’s MAC address.


Here’s what a normal asking-for-MAC-address exchange looks like, in Wireshark:


That image is a bit small, but you can click on it to enlarge it.


So the conversation goes:

1. **Computer** (to everyone on the network) “Who is 192.168.0.13”
2. **Phone** (to computer) “I am! My MAC address is `38:e7:d8:64:42:b7`”
3. **Phone** (to computer) What is your MAC address?
4. **Computer** (to phone) My MAC address is `60:67:20:eb:7b:bc`


And then the phone and the computer remember which MAC address to use and
communicate with each other that way.


(aside: My ethernet card and wireless card actually have different MAC
addresses, so it’s not exactly a *machine* that has a MAC address, it’s the
NIC. I think.)


So the deal with MAC address spoofing is: it turns out ANYONE can go ahead and tell my phone


“I am! My MAC address is `aa:bb::cc::dd::ee::ff`”


and my phone will just go ahead and believe them. But it gets better! It’s not
*just* that anyone can reply, they can reply *even if the phone didn’t ask for
a MAC address*. So if my phone has the *right* MAC address for my computer,
someone else can go ahead and tell them “The MAC address for `192.168.0.15` is
`aa:bb:cc:dd:ee:ff`”.


And my phone will just think “Sweet. Thanks for the update!”. It’ll eventually
fix itself up, so you have to keep sending it these messages over and over
again to keep the cache poisoned.


So let’s look at what that `arpspoof` command from before is doing in
Wireshark:


You can see that every 2 seconds or so my computer (`IntelCor_eb:7b:bc`) is
telling my phone (`Htc_64:42:b7`) the wrong MAC address for the router
(`10.0.0.1`)


And that’s what `arpspoof` does! It actually tries to do it both ways (so the
router and the phone will both communicate with me instead of each other), but
I think the router doesn’t take as much bullshit so it doesn’t work.


It also doesn’t appear to work on my Linux computer, but it seemed to work on
Kate’s Macbook Pro. If you try to poison your cache on a Unixy machine, you
can find out if it worked by running `arp -na` and seeing if the MAC addresses
are right.


I learned all this stuff from [Hacking: The Art of Exploitation](http://nostarch.com/hacking2.htm).
It is fantastic. You can also download the LiveCD from the website for free
and it has all the tools I mentioned here.


I paired on this with [Kate](https://kate.io/) a lot.
