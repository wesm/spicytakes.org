---
title: "Copilot 2.0 ships!"
date: 2007-01-26
url: https://www.joelonsoftware.com/2007/01/26/copilot-20-ships/
word_count: 856
---


Hoorah! [Fog Creek Copilot 2.0](https://www.copilot.com/) is now online, with three, no wait, five, no, three new features.


Well, I guess it depends how you count. In a moment I’ll count ‘em. In the meantime, a little background.


Fog Creek Copilot is a remote tech support service that lets one person control another computer remotely, much like VNC or RDC, with the advantage that it requires zero configuration, works through firewalls, and installs nothing.


Two summers ago, we had four interns here who built it, all by themselves, over the course of their 12 week internship. The only thing we gave them was [a spec](https://www.joelonsoftware.com/articles/AardvarkSpec.html), some desks, and computers. They put together the web site, the documentation, all the code for five major components, came up with the marketing plan, did usability testing, and demoed to the public at a trade show. They kept [a blog](http://www.projectaardvark.com/), which you can still read, and someone even made [a documentary movie](http://www.projectaardvark.com/movie/) made about their summer.


(Sidebar: One of the reasons they were able to accomplish so much in one summer is that they used open source software as a starting point. Of course, everything they did, with the exception of our proprietary back end server code, is [available](https://www.copilot.com/faq/#28) under the GPL license.)


OK. New features!


1. Support for Mac! OMG! All versions of Mac OS X from 10.2 on are now supported. I’m fairly confident that our Mac remote desktop implementation is second to none.


Oh, wait. Interruption. You may be wondering, if the interns did the whole thing over a summer, who wrote all this new code?


The answer is that two of the interns accepted full-time jobs at Fog Creek, Tyler and Ben. Tyler extended his summer until December, and then headed off for a leave of absence to finish his Masters degree at Stanford. Ben graduated from Duke last summer and has been cranking away on 2.0 since then. Ben, by the way, is the only person I know who writes code in C, C++, C#, and Objective C all in the same day, while writing a book about Smalltalk at night. We also had a Mac programming guru, [Daniel Jalkut](http://www.red-sweater.com/), get us started with the Mac port.


OK, next new big feature:


2. Direct Connect! We’ve always done everything we can to make sure that Fog Creek Copilot can connect in any networking situation, no matter what firewalls or NATs are in place. To make this happen, both parties make *outbound *connections to our server, which relays traffic on their behalf. Well, in many cases, this isn’t necessary. So version 2.0 does something rather clever: it sets up the initial connection through our servers, so you get connected right away with 100% reliability. But then once you’re all connected, it quietly, in the background, looks for a way to make a direct connection. If it can’t, no big deal: you just keep relaying through our server. If you can make a direct peer-to-peer connection, it silently shifts your data onto the direct connection. You won’t notice anything except, probably, much faster communication.


3. File transfer! An easy-to-use file upload and download feature makes this the PERFECT application for installing Firefox on all your relatives’ computers. It’s especially handy for tech support scenarios. Imagine this: your new software works great everywhere but this *one guy* has a wacky system that makes your software keep crashing. So you use Fog Creek Copilot to take over his system, and then you use the file transfer feature to copy new builds to his computer as you try to fix the problem.


4. Does this count as a feature? We lowered the price for day passes–24 hours of usage—from $10 to no, not $9, not $8, not $7, would you believe it’s only FIVE DOLLARS? That’s right, unlimited usage for 24 hours for five lonely bucks.


I guess I should explain the reasoning behind that. First of all, the direct connect feature (#2) should reduce our bandwidth bills in many situations, so we can pass that savings on.


Second, we don’t want *anyone* to have an excuse not to use Fog Creek Copilot. To avoid paying $10, you might actually be crazy enough to try to just talk your mom into uninstalling Norton Utilities, punching the appropriate holes in the Windows firewall, and setting up appropriate port-forwarding rules on her broadband router… but for $5, why go through the trouble? Or you might be willing to set up your *own* server outside the firewall, with VNC running as a listener, and walk your customers through setting up VNC and connecting back to you, but again, why bother for five bucks?


We think that’s a negligible price to pay to know that all you need to tell your mom, or your customer, is “Go to copilot.com, type in this number, and download and run the program you find there.” And to know that it will Just Work.


We’re betting that the lower price will lead to more users, which will lead to more corporate subscriptions, which will lead to higher total revenues.


So. Congratulations to Tyler and Ben for a fantastic upgrade!
