---
title: "Gigabit Ethernet and Back of the Envelope Calculations"
date: 2005-07-12
url: https://blog.codinghorror.com/gigabit-ethernet-and-back-of-the-envelope-calculations/
slug: gigabit-ethernet-and-back-of-the-envelope-calculations
word_count: 1014
---

At work today, we had a problem with a particular workstation. Although it was connected to a gigabit ethernet hub, network file transfers were “too slow.” How do you quantify “too slow?”


![](https://blog.codinghorror.com/content/images/2025/05/image-114.png)


I was reminded of chapter seven of [Programming Pearls](http://www.amazon.com/exec/obidos/ASIN/0201657880) – The Back of the Envelope:


> It was in the middle of a fascinating conversation on software engineering that Bob Martin asked me, “How much water flows out of the Mississippi River in a day?” Because I had found his comments up to that point deeply insightful, I politely stifled my true response and said, “Pardon me?” When he asked again I realized that I had no choice but to humor the poor fellow, who had obviously cracked under the pressures of running a large software shop.
> My response went something like this. I figured that near its mouth the river was about a mile wide and maybe twenty feet deep (or about one two-hundred-and-fiftieth of a mile). I guessed that the rate of flow was five miles an hour, or a hundred and twenty miles per day. Multiplying
> 1 mile x 1/250 mile x 120 miles/day ~ 1/2 mile3/day
> showed that the river discharged about half a cubic mile of water per day, to within an order of magnitude. But so what?
> At that point Martin picked up from his desk a proposal for the communication system that his organization was building for the Summer Olympic games, and went through a similar sequence of calculations. He estimated one key parameter as we spoke by measuring the time required to send himself a one-character piece of mail. The rest of his numbers were straight from the proposal and therefore quite precise. His calculations were just as simple as those about the Mississippi River and much more revealing. They showed that, under generous assumptions, the proposed system could work only if there were at least a hundred and twenty seconds in each minute. He had sent the design back to the drawing board the previous day. (The conversation took place about a year before the event, and the final system was used during the Olympics without a hitch.)
> That was Bob Martin’s wonderful (if eccentric) way of introducing the engineering technique of “back-of-the-envelope” calculations. The idea is standard fare in engineering schools and is bread and butter for most practicing engineers. Unfortunately, it is too often neglected in computing.


To diagnose the network throughput issues, I busted out my copy of [pcattcp](https://web.archive.org/web/20050727084029/http://www.pcausa.com/Utilities/pcattcp.htm) and started doing some baseline network speed measurements. It’s a great utility, and quite simple to use; just run one instance on a remote machine using the -R flag, then run another instance on the client with -t (remotename) and you’re off to the races.


But even before that, I started with a loopback test:

kg-card-begin: html

```

C:Program Filesttcp>pcattcp -t -f M localhost
PCAUSA Test TCP Utility V2.01.01.08
TCP Transmit Test
Transmit    : TCP -> 127.0.0.1:5001
Buffer Size : 8192; Alignment: 16384/0
TCP_NODELAY : DISABLED (0)
Connect     : Connected to 127.0.0.1:5001
Send Mode   : Send Pattern; Number of Buffers: 2048
Statistics  : TCP -> 127.0.0.1:5001
16777216 bytes in 0.17 real seconds = 93.02 MB/sec +++
numCalls: 2048; msec/call: 0.09; calls/sec: 11906.98

```

kg-card-end: html

This is helpful because it establishes an absolute upper bound on network performance. Even with an infinitely fast network, **I won’t achieve more than 93 megabytes per second throughput –** at least not on my PC. And this is a completely in-memory test; real world network operations may depend on hard disk reads and writes, which will be far slower.


A good rule of thumb for real-world throughput is:

- 10baseT = 1 megabyte/sec
- 100baseT = 10 megabytes/sec
- 1000baseT = 30 megabytes/sec


All my ttcp testing over the last couple years has confirmed these numbers, plus or minus ten percent. I don’t have as much experience with gigabit throughput, since I just got my [first gigabit router](https://blog.codinghorror.com/blue-led-backlash/), but you definitely shouldn’t expect the perfect scaling we achieved moving from 10baseT to 100baseT. Without any major tweaking, you’ll get only a fraction of the tenfold bandwidth improvement [you might expect](https://web.archive.org/web/20060429183034/http://www.windowsitpro.com/Windows/Articles/ArticleID/24551/pg/5/5.html):


> I noticed a significant improvement in multicast performance, measured by the time required to send a 690MB disk image to 18 multicast clients in one session. The HP NetServer LT6000r served as the multicast server, and the clients were using Fast Ethernet links to the desktop switch. On the Fast Ethernet network, the task took 19 minutes. On the Gigabit Ethernet network, the time was reduced to 9 minutes.
> I measured the transfer of a large (1GB) file between the same hosts over Fast Ethernet and Gigabit Ethernet links with sustained network traffic (streaming media to multiple unicast clients). The file transfer took 230 seconds on Fast Ethernet and 88 seconds on Gigabit Ethernet.
> Overall, my tests showed that Gigabit Ethernet provided a tangible performance improvement, but **bottlenecks elsewhere kept the overall throughput lower than I had hoped**. I was satisfied with Gigabit Ethernet performance relative to Fast Ethernet, and I was particularly impressed that general network responsiveness remained acceptable even during peak network loads. But I was disappointed not to be able to reach much beyond 450Mbps on the Lab’s most capable server.


To be fair, that article is from 2002. A typical new desktop PC probably has more bandwidth and power than the author’s fastest server. Even with those real world caveats, **gigabit ethernet still offers 2 to 3 times the performance of 100baseT**, which isn’t exactly chopped liver, either.


In the end, our issue at work had nothing to do with the “problem” desktop. After a bit of ad-hoc ttcp testing, we found that *nobody* could achieve more than about 11 megabytes per second throughput to the server, even when directly connected to the gigabit switch. [Download pcattcp](https://web.archive.org/web/20051125120649/http://www.pcausa.com/Utilities/ttcpdown1.htm) and try for yourself. Some other interesting experiments you can run with ttcp are UDP (-u) versus TCP/IP, and varying the packet size (-l 4096).

[networking](https://blog.codinghorror.com/tag/networking/)
[gigabit ethernet](https://blog.codinghorror.com/tag/gigabit-ethernet/)
[calculations](https://blog.codinghorror.com/tag/calculations/)
[back of the envelope](https://blog.codinghorror.com/tag/back-of-the-envelope/)
[file transfers](https://blog.codinghorror.com/tag/file-transfers/)
