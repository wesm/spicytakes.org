---
title: "Announcing FogBugz On Demand"
date: 2007-07-09
url: https://www.joelonsoftware.com/2007/07/09/announcing-fogbugz-on-demand/
word_count: 1066
---


I’m happy to announce that [FogBugz On Demand](http://www.fogcreek.com/FogBugz/index.html) is now available. This is a professionally-hosted version of FogBugz 5.0, previously only available as a download.


Selling web software has always been a slightly strange aspect of the way Fog Creek operates. Since FogBugz is a web-based project management tool, why should customers have to download it and install it on their own servers?


In the past, we did it that way because we’re a small company. With just a handful of full time employees, we didn’t really have the resources to be a reliable service provider that customers could trust with their mission-critical data.


To prepare for FogBugz On Demand, we’ve done a lot of hard work over the past year.


First, we hired a professional system administrator. He has pored over every inch of our hosting infrastructure, patching and testing and improving reliability everywhere. He upgraded all the NetBSD servers to Linux, installed a bunch of new hardware, and added lots and lots of automated monitoring.


In general, we decided to use high-end components for our hosting architecture: Dell PowerEdge 2950 Servers with SCSI RAID, Windows Server 2003, and SQL Server 2005. Yep, that’s an expensive way to do it. Since FogBugz runs fine on LAMP (Linux / Apache / MySQL / PHP), we could have gotten a bunch of cheap boxes, used all free software, and saved some money in exchange for some level of headaches. Indeed, most hosted services really should be built on LAMP. In our case, though, the cost of those Microsoft licenses and those extremely reliable Dell servers can be spread out over quite a few paying customers, so for us the cost difference *per customer* is really inconsequential. And we’ve been running IIS and Microsoft SQL Server here for six years without data loss, so that’s what we know and trust. But to be honest, if we ever get to the point where we’re racking up 10 new servers at a time, we’ll almost certainly switch to LAMP. I’m still gonna buy Dell servers and SCSI hard drives, because frankly, the small extra cost over cheapo white boxes is well worth it in reliability.


We made changes to the FogBugz code base itself to make it work better in a multi-hosted environment. The biggest surprise was how much work it took so that every user sees things in their own time zone. We also put a lot of work into the accounting and billing system (FogBugz On Demand is $21 a month, with no commitment). We implemented a database-backed DNS system so that each On Demand customer gets their own domain (*you*.fogbugz.com).


The biggest change was bringing up a second data center. I can’t tell you how scary it is to be responsible for our customers’ mission-critical data, so I didn’t want to have any single point of failure, no matter how fortified it is.


Our first data center has been with [Peer 1 Network](https://www.joelonsoftware.com/articles/Peer1.html) in New York’s financial district. Peer 1 is a Canadian backbone provider where we’ve been since the beginning of 2003. To take advantage of their backbone, we put our second data center in their new Los Angeles facility. This new data center is pretty much an exact replica of what we have in New York.


To some extent, by using Peer 1 for our second facility we are, technically, putting all our eggs on one backbone. But it’s a pretty darn reliable backbone and an excellent company. We actually investigated a couple of other colo providers and even went so far as to build out a facility in Chicago (with an unnamed provider). But shortly before we launched, they had a six hour outage, and in the aftermath of that, we discovered that their network connectivity was inadequate and their concept of building reliable systems did not use the same definition of “reliable” as we do. So we gave up on them, shipped all the servers from Chicago to LA, and went with the tried and true Peer 1.


Rather than setting up Los Angeles as a mere *backup*, we decided it would be completely live. Half our customers will be hosted from Los Angeles, and half from New York. That way we know at any time that both data centers are working and set up correctly, and we don’t have to wait until a massive failure to discover the problems with the backup data center.


Copies of the database backups are maintained in both cities, and each city serves as a warm backup for the other. If the New York data center goes completely south, we’ll wait a while to make sure it’s not coming back up, and then we’ll start changing the DNS records and start bringing up our customers on the warm backup in Los Angeles. It’s not an instantaneous failover, since customers will have to wait for two things: we’ll have to decide that a data center is really gone, not just temporarily offline, and they’ll have to wait up to 15 minutes for the DNS changes to propagate. Still, this is for the once-in-a-lifetime case of an entire data center blowing up, not just for occasional outages: each data center already has incredible backbone connectivity, UPSs, backup diesel generators, and so forth ([Peer 1 survived that huge blackout](https://www.joelonsoftware.com/items/2003/08/21.html) during the summer of 2003 while many of their competitors were winking out).


To implement this warm backup feature, I wrote a SQL mirroring application that implements [transaction log shipping](http://www.sql-server-performance.com/sql_server_log_shipping.asp): basically, it does an incremental backup in one city, compresses that backup, ships it to the other city, uncompresses it, and applies it to the warm backup database. Right now, we’re log shipping twice a day, so you might lose a day of work if an entire city blew up, but in a couple of weeks, we’ll implement a system that does more continuous backups, and we expect that the warm backups will never get more than 15 minutes behind.


FogBugz On Demand has actually been in beta since April, and in fact we have been hosting FogBugz trials on line since 2000, without ever losing anyone’s data. (The first FogBugz 1.0 trial server, believe it or not, was a Thinkpad laptop with a broken screen plugged into our office T1!) So I’m pretty confident now that our little company can do a pretty good job of [hosting FogBugz](http://www.fogcreek.com/FogBugz/index.html) for you.
