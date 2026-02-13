---
title: "The “WiFi At Conferences” Problem"
date: 2009-10-08
url: https://www.joelonsoftware.com/2009/10/08/the-wifi-at-conferences-problem/
word_count: 733
---


Why does WiFi work so poorly at tech conferences?


Marcus GriepI assume that WiFi wasn’t really designed to handle a big ballroom with 2000 people, all trying to connect with their laptops and cell phones at the same time. Sometimes I feel like I’m lucky if it works in my apartment. So I never thought it was even possible to get it to work at a large, technically-savvy conference. At Stack Overflow DevDays, yesterday in Boston, the bandwidth seemed OK but the DHCP server ran out of addresses. This didn’t seem to be something that anyone could fix. The conference organizers (er, me and Greg) were incredibly busy trying to, you know, organize the conference, so spending time tracking down the mysterious ISP and making them fix their router was impossible.


It’s almost getting boring to read the conference reports [complaining](http://www.techcrunch.com/2008/12/13/swisscomm-tries-to-deflect-criticism-of-le-web-internet-failure/) about this. Almost every conference, even the ones put on by fancy tech companies, has trouble. I never assume WiFi is going to work whenever I’m in a room with that many techies.


At the smaller conferences, the ones with, say, 300-1000 people, the trouble is that internet access is something of a black box. If you’re a conference organizer, your first priority is finding a space—*any* space—because there usually aren’t a lot of options. For example if you want to put on an event for 500 people in Seattle, there are probably 20 hotels that can accomodate you and maybe 10 other non-hotel venues. For the date you want, 3/4s of them are booked. You end up choosing between three options, if you’re really lucky. The venue with the best Internet access would be nice, but there are so many other considerations that you don’t really think about this when you’re booking the space. Besides, all the venues tell you they have fantastic, soo-perb A-number-1 internet access. When you try to ask complicated questions and explain that your conference has a lot of techies, they say, yes, we understand, we have A-number-1 internet access, no problem very good. When you say, “Yeah, but have you configured your DHCP server so that it has more than the default 254 IP addresses available to hand out,” they have no idea what on earth you’re talking about, and of course it turns out that they had some vendor, a company you’ve never heard of, provide their internet access. And half the time, that vendor installed a DSL line from the local telco and hooked it up to a LinkSys WRT54g they got at Costco, then installed some kind of crappola welcome-screen software just to make it even worse, and then disappeared.


Marcus GriepThere are steps that can be taken. Here’s an interesting study [PDF] done by Intel about [making WiFi work at large conferences](http://www.google.com/url?sa=t&source=web&ct=res&cd=1&url=http%3A%2F%2Fwww.intel.com%2Fit%2Fpdf%2Fconference-wifi.pdf&ei=BZTOSpG5NcG5lAeQzbmpCg&usg=AFQjCNGbX8ISITxs5tvXlOuqcW-VBbx_YA&sig2=2ILRY9y3UYY2z82850mwug). The best idea I got from that was that there should be as many hardwired network access points as possible, to get the heavy users off the air, because ethernet has way more bandwidth. There are companies that specialize in making WiFi systems that will support large conferences: one that I found is called [Meraki](http://meraki.com/); I don’t know much about them but their website sure makes it seem like they understand the issues at least.


At the very least, though, a venue should be able to tell you how many access points they actually have (if it’s just one, you’ve got problems), whether they are managed access points or not, whether dedicated ports with higher priority can be provided for the speakers and for journalists that do not share bandwidth with the audience, how many IP addresses the DHCP server can provide, the total number of people that can be online at once, and the amount of bandwidth available to the entire site. If you can’t get good answers to these questions before the conference begins, you have to assume that they’ll be running a single, consumer router connected to a DSL line and that’s about all you get.


What are some of the best practices for conference organizers? What questions should they ask the conference venue or ISP to know, in advance, if the WiFi is going to work? What are the most common causes of crappy WiFi at conferences? Are they avoidable, or is WiFi simply not an adequate technology for large conferences? I thought I’d ask on ServerFault, so if you have any ideas, [have at it](http://serverfault.com/questions/72767/why-is-internet-access-and-wifi-always-so-terrible-at-large-tech-conferences)!
