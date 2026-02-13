---
title: "New Server at Peer 1 Network"
date: 2003-02-03
url: https://www.joelonsoftware.com/2003/02/03/new-server-at-peer-1-network/
word_count: 1844
---


I’ve moved *Joel on Software* to a new server, at a colocation facility operated by [Peer 1 Network](http://www.peer1.net/). In the process of finding a new home and getting it up and running I’ve learned quite a bit about how web hosting works, so I thought I’d describe a bit of it here and in the process provide a glimpse Behind The Scenes.


The Fog Creek office is connected to the Internet via a single T1, which provides 1.5 Mbps of bandwidth. That’s 1.5 megabits per second, the equivalent of 24 phone lines.


The T1 was provided by Savvis. The cost fluctuates depending on usage but it generally costs us something just over $1000 a month.


We had originally decided to use a T1 instead of the much cheaper alternatives (like DSL or cable modems) because T1 lines had a reputation for reliability. We ran all our servers ([Fog Creek](http://www.fogcreek.com/), [Joel on Software](http://joelonsoftware.com/), [TechInterview.org](http://www.techinterview.org/)) from the office because we needed a fast Internet connection to the office anyway*,* so why pay again for hosting? That was the theory, at least.


But the T1 turned out to be not as reliable as we thought. We had a lot of short outages, from seconds to an hour, and twice in the last year we had outages of a day or more. In both cases, the ISP did not fix them nearly as quickly as we thought they should have been able to. Although our ISP was Savvis Communications, the segment of T1 from our office to the nearest Savvis location (called the “local loop”) was actually provided by Worldcom. And in fact Worldcom didn’t actually provide it, they just resold a Verizon T1 under their own name. So when something went wrong with the Verizon line, we had to convince Savvis to convince Worldcom to convince Verizon to fix it. Somehow this was like pushing on a string. Outsourcing is problematic that way: when everything works perfectly, you don’t notice, but when things go wrong, it’s much harder to get them fixed.


You may be wondering if a single server connected to a T1 was enough for all the traffic this site gets, about 100,000 hits a day, more like 500,000 when I write a new article or get mentioned on slashdot. The short answer is, it was fine. Since I publish the site using [CityDesk](http://www.fogcreek.com/CityDesk) which simply generates a bunch of plain HTML files, the server doesn’t have to do anything tricky like generate each page from a database on the fly.


Anyway, we’re about to move to a new office, so a decision had to be made about whether to take the T1 with us, or do something else. The long outages convinced me we needed a real colocation facility. “Colocation” means that you pay someone with a room with extremely high speed Internet access, usually redundant, to let you put your own computer on a shelf in that room. A good colocation facility, or “colo” as they’re called, also has great air conditioning, a big generator to provide power if the lights go out, and huge batteries to keep the whole thing running during the few minutes it takes to get the generator started up. It also has a lot better security than average, all kinds of exciting fire extinguishing equipment, and locked cages to keep one company’s servers from being tampered with by another company that uses the same colo.


“Colocation” is not the same as “web hosting.” Typically a web host will host your web site on their own servers. They administer the servers; you just put your files up and they serve them. Whereas colo means you buy and install and administer your own server hardware. We chose colocation for a number of reasons, but primarily because it gives us the flexibility to run any software we want.


If you’re in the market for colocation, especially in a major metropolitan area, you probably have quite a few choices. By the way, there’s no reason you have to get colocation in the same city where you’re located — you can just build a server and then ship it to the colo. The colo’s engineers put it on the rack for you, plug it into power and the net, and turn it on.


A quick google search came up with a list of about eight companies that offered colocation in New York, so I called them all for price quotes. For the most part, the quote is based on how much space you need, how much bandwidth you need, and possibly how much power you need. There may be some other charges for things like IP addresses, but those are nickels ‘n’ dimes. Space is measured in racks. A single rack is about 6 or 7 feet high and always exactly 19 inches wide. You might rent a half rack or quarter rack if you have less equipment. If you only have one or two machines,  you’ll see things quoted in U’s. One U is about 1.75 inches and represents the vertical distance from one set of screw holes to the next set on a rack; virtually all equipment that is intended to be mounted on a rack is a round multiple of 1U in height. The thinnest servers are 1U pizza-boxes. Our new server, a Dell 2650, is 2U in height; I chose this model because it had room for 5 hot-swappable hard drives. Hot swappable means you can plug them in and pull them out while the computer is running, so we can add some more storage without turning off the server and messing around with screwdrivers.


There are different schemes for paying for bandwidth. The most common, called* capped bandwidth, *is simply to pay for the bandwidth that’s available. For example, you might get 1 Mbps of bandwidth capped, and you can use all of it or none of it and pay the same amount. The network administrator will program the router to cap your usage at that amount.


Another common system is where they set you up with a ton of bandwidth, but you only pay for the 95% percentile of the actual bandwidth used. That means that they sample how much bandwidth you’re using every ten minutes over the course of a month. At the end of the month, they throw away the top 5% of all the samples, and charge you based on the maximum bandwidth you used during the other 95% of the time. This method means if you have a really big spurt in usage for a few minutes you won’t have to pay for it. This is what’s called “burstable bandwidth.”


Anyway, I’ve been running this server for a while, so I had a pretty good idea of how much bandwidth it was going to need, and I had picked out a nice 2U server, so I took this info to the eight colocation providers I found for quotes. What I found clustered into three groups:

- high end snobs, who told me they never do less than full racks, and I couldn’t afford their services. These were usually companies from the Dot Com days that built ridiculously fancy offices and have marble bathrooms in their colos and named gigantic sports stadiums after themselves, and are now in bankrupcy court. When they would quote me a price, it was in the range of $1000 to $1500 a month.
reasonable small companies who had grown slowly and carefully, with slightly grimy colo facilities because they didn’t waste money on trivial stuff that doesn’t contribute to the bottom line like sweeping the floors or being polite to potential customers. They usually wanted $400 or $500. But luckily there was a third group, consisting of,
[Peer 1 Network](http://www.peer1.net/), a super friendly Canadian company that took one look at *Joel on Software* and said, “hey, nice site, we’ll host it for free for ya.” OK, I like free.


I liked just about everything I saw about Peer 1. They have just built a spiffy new facility in New York which connects to their [cross-Canadian backbone](http://www.peer1.net/network_map.asp). A Google search convinced me that their customers were all happy campers. And if you ever get a choice of whether to deal with Canadians or New Yorkers, I know it’s unpatriotic of me to say this, but, go with the Canadians. Peer 1 is a small enough company that they care about your business, something which the giant bankrupt telcos don’t. And they had a really smart network engineer working out of the New York colo who took the time to teach me a lot of the things I would know if I were a real network administrator as opposed to a software developer pretending to be a network administrator.


I got the Dell delivered straight to Peer 1’s facility which is down the block from the New York Stock Exchange. When it arrived, Michael and I grabbed the Win2K CD-ROM and took the subway downtown to set it up. Most servers run “headless,” that is, without a keyboard or monitor, so Peer 1 had a keyboard, monitor, and mouse on a rolling trolley available for our use so we could set up the system. (You can see the temporary wires in the picture at right.) We installed Windows 2000 and got it completely up to date with patches before connecting it to the live Internet. The server has two separate power supplies and two power cables in case one fails or falls out. The dual power cables also means that if you need to move the server or plug it in somewhere else, you can do this using extension cords *without ever turning the machine off*.


It had three separate ethernet jacks: you use one of them for remote administration. The remote administration jack is really quite neat. This is a little computer with its own network jack which lives inside the big computer. Even if the main computer is off or hung, I can connect to the administration computer over the Internet using a web browser and tell it to reboot or turn on the main computer. Slick!


Peer 1 only gave us a single Internet drop in our cage — just a regular Cat 5 ethernet cable — so I ran out to J&R Computer World and bought a $35 [Linksys 5 port switch](http://www.amazon.com/exec/obidos/ASIN/B00003006E/ref=nosim/joelonsoftware) so we could hook up all three network jacks.


One last step before connecting to the Internet: we turned on packet filters to block all incoming connections except for traffic from the Fog Creek office.


Once we got the computer on the net, we tried [www.google.com](http://www.google.com/), which redirected immediately to [www.google.ca](http://www.google.ca/). Cool! They think we’re in Canada! Our work done, we locked up the cage and came back to the Fog Creek office. Since then, everything we need to do with this machine can be done over the net, using Windows’ built-in Terminal Services. This feels exactly like sitting at the machine. With any luck, it will be years until I visit this computer again.
