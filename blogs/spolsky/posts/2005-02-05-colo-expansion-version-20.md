---
title: "Colo Expansion Version 2.0"
date: 2005-02-05
url: https://www.joelonsoftware.com/2005/02/05/colo-expansion-version-20/
word_count: 3280
---


(Updated 2/6/05)


It’s been about two years since [we first installed a server](https://www.joelonsoftware.com/articles/Peer1.html) at the Peer 1 colocation facility downtown. That server, a Dell 2650, has patiently handled the load for Joel on Software and Fog Creek gracefully, but there are a few issues that are starting to become more significant as Fog Creek grows and reliability becomes more important. And we need more server horsepower and scalability.


In the past I would have upgraded the system, installed it all, and written an article about it. And then people would have emailed me to suggest better ways to do things, but it would be too late.


So now for the first time ever, I’m going to publish a “live” article here. So far, I haven’t done anything. If you have any better suggestions for how to do things, it’s not too late for me to learn from your experience. As we go along, I might have a few questions for my readers who have experience with this stuff. **Thanks to everyone who has emailed me so far!**


Step one was figuring out what problems we’re trying to solve. Here’s the list:

- Not enough horsepower to handle the large number of [FogBugz online trials](http://try.fogbugz.com/) we’ll be hosting. FogBugz 4.0 is a couple of weeks away from shipping and that should create a flood of people wanting to take advantage of the free online trial. (By the way, if you want to beat the traffic, apply to join [the FogBugz 4,0 beta](https://shop.fogcreek.com/beta/?prod=1).)
- Running an email server on Windows allowed us to save hardware, at the cost of buying a commercial email product, IPswitch IMail. We are very close to using up the maximum number of mailboxes we’re entitled to create, and we’d really like to switch to a Linux mail server running [qmail](http://www.qmail.org/) or [Postfix](http://www.postfix.org/). **The votes seem to be in favor of Postfix.**
- Although we have a standby server, a small Dell 750 we stuck in there last summer, we don’t really have a good story for handling failures. Right now we could recover from most kinds of failures in about 24 hours, and we have to take all the sites down for about 15-30 minutes when we need to apply OS patches or upgrade the server. But Fog Creek’s daily revenue has grown to the point where I’m not happy with that. Our new goal is to have no single point of hardware failure be able to bring down any of our sites, to be able to upgrade OSes without bringing everything down, and to be able to recover from very major problems in 15 minutes. **This goal is fairly absurd. There will always be single points of failure. The ozone layer, for example. A more accurate goal would be “No single hard drive, power supply, or fan failure takes us out of commission for even 1 second. Any other server failure can be recovered from in 15 minutes. Routine Windows Updates will no longer bring our site down. If something happens to the colo facility, its power supply, or the City of New York, well, we go off the air for a while.”**
- And we want to have an architecture in place to be able to scale up our hardware relatively easily to meet new demand.


Step one in this project was finding a good sysadmin to help design and implement this project. One of the great things about Fog Creek in its fifth year is that when we need to do something, we have the money to do it. So instead of me trying to build mission critical server networks using off-the-shelf consumer grade plastic linksys crap, I called up Adam Prato, who I had worked with at Juno, who has years of experience building out these kinds of things. After about an hour briefing he wrote up a very professional plan, sketched out the basic architecture of the new network, and started recommending purchases.


In choosing servers, there’s a lot of benefit to using totally standard, identical parts. It makes it easy to swap things around when you need to scale or when something fails, and things are cheaper by the dozen. In order to avoid going totally broke, we still want reasonably affordable servers, but my requirement of “no single point of failure” means we need servers with dual power supplies, hot-swap RAID, and everything engineered for longetivity. That tends to narrow things down to the Dell PowerEdge 2850, which is the updated version of the 2650 we have now. **I looked into the equivalent HP box. It looks like it costs 2-3 times as much for the equivalent thing.**


The current plan is to get six servers:


1 and 2: web servers running Windows 2003. Two mirrors, each containing every site we host. We’re using Win2003 instead of Win2000 because mirroring is much easier – the IIS 6.0 metabase is just a big XML file so we should be able to mirror the two machines using something as simple as ROBOCOPY. **In fact, I think we can stage all our web sites back at the Fog Creek office and let Robocopy distribute them out to the web servers. **


We will have some rudimentary load balancing by using a different IP address for every site that we host, and we can program each server’s NIC to respond to some subset of IP addresses. That way moving a website from one server to the other is a simple matter of changing what IP addresses each server uses. We can scale up by adding more of these servers as we go along, and in the future we can use round-robin DNS or a real load balancer to distribute the load if necessary. If one server dies, the other one is a mirror so it can take up the whole load. **Many people wrote in to recommend Windows’ built-in Network Load Balancing. I think this may be overkill for the first generation but it sounds like a good idea in the long run.**


3: SQL Server. Because everybody is sharing the same SQL Server, this machine will be *slightly *different than its peers: it will have the fastest available CPU available and it will have more hard drives plugged in. I heard that it’s a good idea to get the transaction logs onto a different physical drive than the data itself, for better performance, so I think this machine will have two RAID 1 mirror sets (4 hard drives). **Most correspondents agreed that this is the best architecture.**


4: Mail and everything else server. Linux.


5: Routing server. Probably NetBSD. This machine will have four ethernet ports and will route between the public internet, the direct connection to the Fog Creek office, the “DMZ” containing our public-facing servers, and a private network segment containing the SQL Server machine. **Many people suggested OpenBSD for better firewall support (“pf”). I’m out of my league here, and will have to trust Adam to use the right technology. Also having different OSes for #4 and #5 doesn’t make sense so we’ll try to pick one OS for both.**


**Other people thought that it might be better to use a solid-state hardware firewall/router rather than build our own on a generic Intel server. The advantages of building our own is a lot more flexibility, and somehow I think that the Dual-everything Dell PowerEdge 2850 is going to be a lot more robust than one of those dinky firewall/routers you get at CompUSA. I’ve already had one of those die on me with no explanation… **


6: Cold backup. Another machine, identical to the first five, sitting around ready to be used for whatever we need it for or to serve as an emergency replacement.


Each machine will contain:

- A Xeon processor, 800 MHz Front Side Bus, with 1 MB Cache
- SCSI RAID with room for 6 drives. All the systems will start with 2x146GB drives installed in RAID 1 (mirroring) formation, except for the SQL machine which will have 4 drives. Every hard drive in the rack will be a Seagate Cheetah, 146GB SCSI U320, at 10000 rpm. Since they’re hot swappable we can move them around at will and we can keep a couple of spares in the cage. **10K is much cheaper than 15K. Some people suggested using 15K for the SQL Server but I’ve actually heard elsewhere that RPMs aren’t such a big deal for SQL Server. And I really don’t want to have two kinds of hard drive.**
- Dual Gigabit NICS. The whole network is going to be gigabit ethernet and we’ll use unmanaged Dell gigabit switches which seem to be priced well below the (NetGear) competition. **The managed gigabit switches are more than 3x the price of unmanaged gigabit switches.**
- 2 GB RAM
- Dell’s DRAC 4/I remote management card (more about that in a minute).


I called up Dell and got a quote for this whole mess. By the way, if you’re ever buying more than one or two machines, it’s worth actually calling Dell. Somehow you always get a lower price than you would have gotten on the website. I’ve also been told that if you call during the last week of Dell’s fiscal quarter, which I just missed, you get great deals as they spaz out trying to make their numbers for Wall Street in a classic display of American public company mismanagement.


I still have a list of open questions that I need to work on this week. If you have any answers, email is appreciated!


**Question 1 – Power Management**


Dell’s built-in management card, the DRAC 4/I, has the ability to turn on and off the machine its plugged into, to resolve “stuck” systems, which is nice. But in two years of operating our current server, we’ve learned that the DRAC card itself (an older model, the DRAC 3) is more likely to freeze up than Windows 2000 itself. And there’s no cure to a frozen DRAC card other than a full power cycle.


To address this, out of desperation, we put an APC MasterSwitch in the rack. This is basically a power strip with a web server. You can connect to it using any web browser to turn on or off anything plugged into the back. The MasterSwitch is awesome. It does one thing, and does it well.


The trouble is, this poor MasterSwitch only has 8 outlets and we have 6 servers with two power supplies each. It looks like there’s a company called Sentry that makes something called the [Dual Feed Power Tower](http://www.servertech.com/products/product.aspx?ProductID=4&GroupID=1), which, if I understand correctly, is designed exactly for these servers with dual feeds. Has anyone ever used such a thing? I can’t find a price on the website which always makes me worry. **It looks like it’s about $1350. For less money I can get a new APC MasterSwitch Plus plus the “expansion pack” giving me 16 power outlets on two separate boxes thus reducing points of failure.**


And another question — according to Dell’s very cool [Rack Advisor](http://support.dell.com/support/downloads/format.aspx?releaseid=R91359), my six PowerEdge’s are going to need about 35 amps of power. Yelps. Is that believeable? From what I remember you’re not even allowed to have more than 20 amps on each circuit. So I’m wondering if a single power tower switcheroo thing can handle the load. And speaking of power, sometime this week I need to track down Joe Cooper of [Peer 1](http://peer1.net/en/index.asp) networks and find out how much it would cost to upgrade from a 1/8th rack to a 1/2 rack. We’ll be going from 3U today to 14U. I’m hoping that Peer 1 has some way of getting me enough amps to run six servers. Or maybe when Dell says that one of their servers consumes over 5 amps, they mean “fully loaded”, and we won’t really be close to fully loaded. **People have told me that Dell is on drugs. Technically the power supplies in these things are 700 watts, but realistically you never draw that much, and so 20 amps should be fine.**


**Question 2 – Rack Management**


As soon as we got the second server, our small backup PowerEdge 750, and put it on top of the old 2650, we had to add RAM to the 2650 (on the bottom), which was a terrible pain in the buttocks. Which made me realize we really need to rack mount all our servers properly. I need to get Peer 1 to tell me what kind of mounting equipment I need to order… Dell gives you a choice of “VersaRails” or “RapidRails.” I’m sure we’ll figure out how to install things, but it would be nice if Dell had a video showing how to rack mount their servers instead of badly written technical documentation with instructions like “Install two 10-32 x 0.5-inch flange-head Phillips screws in the back mounting flange’s top and third-from-top holes to secure the slide assembly to the back vertical rail.” *What? ***VersaRail is for round holes and requires screwing things in. Rapid Rails is for square holes and things just click into place. It’s not that hard, I’m told **


**Question 3 – Remote Control**


We need to decide between a remote KVM-over-IP system and just using Dell’s built-in DRAC 4/I remote control.


The DRAC has two advantages I know of:

1. It has other nice features like power cycling (when it doesn’t freeze) and the ability to boot your server off of a floppy or CD-ROM which is mounted over the network.
2. It’s a lot cheaper; KVM over IP is pretty expensive.


But I’m worried about the DRAC’s KVM capabilities. With version 3, you *could* see the computer screen while it was booting up, but after that the remote control capability disappeared for a while until the operating system came up, after which it seemed to use Windows Terminal Services or something like that to remote control the server. This is a little bit to OS-dependent for comfort. I have heard rumors that the new model DRAC 4/I fixes this problem and lets you remote control the server no matter what state the OS is in. Can anyone confirm this? If so we can probably live without an expensive KVM-over-IP solution. **The bottom line is that we *need* to have the DRAC 4/I, because there’s no other way to *turn on the server remotely*. Power cycling a server that was on will make it come back on, but if you screw up and tell windows to shutdown you can power cycle until next monday and it won’t go on. Given that we have to buy the DRAC 4/Is anyway, I’m hoping that they are good enough and we can live without expensive KVM over IP. If I’m wrong we’ll just add KVM later.**


**Question 4 – SQL Server on its own Machine**


I’ve never tried running SQL Server on a separate physical box than the ASP application that’s using it. I know it works since FogBugz customers do it all the time, and it *seems* like it should improve performance, but then again, I’m worried about the network bottleneck. We’ll have fast gigabit ethernet and the two machines are only one hop away. Do I need to worry about this? **I don’t have to worry about this, it works fine, etc. Many people pointed out that Best Practice is to have a separate network segment/switch for the SQL traffic so it doesn’t compete with  web server traffic. I strongly suspect this best practice arose in the days of 10/100 ethernet, not gigabit ethernet, and that this would be overkill, although if needed it will be easy to retrofit in later since every server has 2 ethernet ports.**


**Question 5 – RAID And *nix**


People tell me that even using Dell-standard RedHat on their own servers with RAID has the problem that there’s no way to find out when a drive has failed, and that the situation is even worse with the BSDs. This could be a major problem. There’s no point in having RAID if you don’t find out when a drive failed. We need to make sure whatever OS we choose for the two Unix boxes supports the Dell Perc Raid Thing.


**FAQ**


Q: Why Windows for the web servers?


A: FogBugz is written for Windows and ported to Unix. Thus the Windows version is usually about 2 months ahead of the Unix version, and we always want to be running the latest daily builds of our own dogfood. Also, a lot of Fog Creek’s existing applications such as the online store are written for ASP or ASP.NET.


Q: Why SQL Server instead of MySQL?


A: Similar historical reasons, the performance is better, and the Unicode support is far better.


Q: Don’t you like Linux/Unix/MacOSX/NetBSD/BeOS?


A: Yes. I love all operating systems equally. If we were building all this software from scratch I *might *have taken a different technical approach, but we didn’t, so get off your OS religion high horse for a minute. We’re going to have a mixed environment for the foreseeable future and 90% of FogBugz customers choose to run it on Windows servers. But we will use Unix for network routing, email, DNS, and a few other small things.


Q: Why Windows 2003 instead of Windows 2000?


A: Because IIS 6.0, the web server in Windows 2003, stores all its configuration information in a XML text-file metabase, and supports “XCOPY deployment,” it means we’ll be able to mirror web servers more trivially simply by mirroring file directories. **And Windows 2003 has lots of improvements to web server performance.**


Q: Why Dell?


A: My experience has been that it’s easier to get a Dell server built and configured exactly the way you want it, and it usually comes out a lot cheaper than the alternatives. **At least 2x cheaper than HP! **And I don’t like buying through resellers who don’t know what they’re selling. Every time I ever made the mistake of buying something from PC Connection I sentenced myself to *weekly* annoying sales calls from a clueless sales person who always dramatically screwed up anything I tried to buy from him. When you call Dell you get a nice, cheerful, competent kid in Austin, Texas who laughs at your jokes, no matter how dumb, and actually has the ability to do sophisticated things like read email that you sent him and then *actually reply to it!*


But that said, Dell has really, really crappy software skills, and their management software sucks big rocks. Every simple application they make is a horrible mess of Shockwave, HTML, Java, *and *Visual Basic with 35 MB of runtimes just to do some basic system administration thing. Today when I downloaded their otherwise cool Rack Advisor, the download was an EXE — a self-extracting EXE. Running the EXE extracted — wait for it — another EXE. This EXE was the single file installer. Really, really, really crappy software skills. Get some programmers, Dell! HP and IBM are reputed to have much better system management software, not that I’ve ever seen it.


Finally, Dell has a neat feature where you can log on to their website and see a list of every computer you’ve ever bought from them, and I love logging on and seeing that list get longer and longer.


Q: Why not a SAN?


A: There seem to be lots of good reasons to use a storage area network, although I don’t think it’s quite cost-effective for our situation. We’re looking at a total bill in the neighborhood of $20K, and SAN solutions tend to start around that price.
