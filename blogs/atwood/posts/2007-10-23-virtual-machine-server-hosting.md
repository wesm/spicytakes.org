---
title: "Virtual Machine Server Hosting"
date: 2007-10-23
url: https://blog.codinghorror.com/virtual-machine-server-hosting/
slug: virtual-machine-server-hosting
word_count: 981
---

My employer, Vertigo Software, graciously hosted this blog for the last year. But as blog traffic has grown, it has put a noticeable and increasing strain on our bandwidth. Even on an average day, blog traffic consumes a solid 30 percent of our internet connection– and much more if [something happens to be popular](https://blog.codinghorror.com/why-cant-programmers-program/). And that’s *after* factoring in all the [bandwidth-reducing tricks](https://blog.codinghorror.com/reducing-your-websites-bandwidth-usage/) I could think of.


While I greatly appreciate my employer’s generosity, I don’t like causing all my coworkers’ internet connections to slow to a crawl. So when my friend and [co-author](https://blog.codinghorror.com/do-not-buy-this-book/) Phil Haack mentioned that we could share a dedicated server through a contact of his, I jumped at the chance.


I’m a [big believer in virtualization](https://blog.codinghorror.com/our-virtual-machine-future/), so I wanted a beefy physical server that could handle running at least four virtual servers. And I wanted it to run a 64-bit host operating system, as [64-bit offers huge performance benefits](https://blog.codinghorror.com/64-bit-desktop-vs-64-bit-server/) for servers. Nobody in their right mind should build up a 32-bit server today.


The contact he was referring to works at [CrystalTech](https://web.archive.org/web/20071218012706/http://crystaltech.com/dedicated-windows.aspx?uid=101). And boy, did CrystalTech *ever* hook us up:

- Windows Server 2003 R2 x64
- Quad-core Xeon X3210 @ 2.13 Ghz
- 4 GB RAM
- 300 GB RAID-5 array


Not too shabby. It is, of course, an obscene amount of power for our relatively modest needs. Have I mentioned how much I like my new friends at CrystalTech? Or what great deals they have on hosting?


![](https://blog.codinghorror.com/content/images/2025/05/image-534.png)


But in all seriousness, it’s effectively a new sponsor for this blog, so welcome aboard.


I was already hosting this server as a VM, so here’s what I did to switch over to completely new hardware:

1. shut down my VM
2. compacted and compressed it
3. transferred it to the new server
4. booted it up again


All I had to do was change the IP address in the VM and I was up and running as if nothing had changed. That’s the easiest server migration I’ve ever experienced, all thanks to virtualization.


Phil and I are both Windows ecosystem developers, so we went with what we knew. But virtualization provides total flexibility. I could spin up a new Linux server at a moment’s notice if I decided to switch this blog over to the LAMP stack. Or I could play with the latest release candidate of Windows Server 2008. And they can all run in parallel, assuming we have enough memory. That’s what I love most about virtualization – the freedom.


Although Phil and I share admin access to the host machine, we have our own private playgrounds in our virtual servers. We’re completely isolated from each other’s peculiarities and weirdnesses: nothing we do (well, *almost* nothing) can affect the other person’s virtual machine. Reboot? No problem. Install some stupid software I can’t stand? Go for it. Format the drive and start over? Don’t care. It’s your machine. Do whatever.


The only downside to virtual machine server hosting is that **it can be difficult to share IPs between virtual machines**. CrystalTech has provided us with a block of 6 public IP addresses, so fortunately we don’t have to worry about this. One IP is occupied by the host, but that still leaves five IPs for virtual machines of our creation. That’s plenty.


But let’s say we only had two public IP addresses – or we wanted to run lots and lots of virtual machines with a small pool of public IP addresses. What then? How could [codinghorror.com](https://blog.codinghorror.com/) and [haacked.com](http://haacked.com/) share the same IP address (and port 80), when they’re on two different virtual machines? They clearly can’t occupy the same IP.

kg-card-begin: html

```

codinghorror.com   10.0.0.1:80
haacked.com        10.0.0.1:80

```

kg-card-end: html

On a single physical server, the answer is easy – [virtual hosting](https://web.archive.org/web/20071203213753/http://httpd.apache.org/docs/1.3/vhosts/), or [host header routing](https://web.archive.org/web/20071224175012/http://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/288bd8ef-c12d-43bc-9b66-264bc572c87a.mspx?mfr=true). But that requires our websites to live side by side on the same server. Phil and I don’t share our wives, so why would we share a server? No offense intended to either of our wives – or our respective servers – but sharing is an unacceptable solution. I like you, Phil... but not *that* much.


If you want two different machines (physical or virtual) to share an IP, it takes some clever trickery. In the Windows ecosystem, that clever trickery often comes in the form of Microsoft’s [ISA Server](https://web.archive.org/web/20071223003634/http://www.microsoft.com/isaserver/default.mspx). (I’m not sure what the open source equivalent is, but I’m confident it’s out there.)


ISA Server acts as our public interface to the world, talking through a public IP address. All DNS entries, and thus HTTP traffic, would be directed to that single public IP address. As our gatekeeper, ISA Server is in a unique position to do lots of cool stuff for us, like firewalling, caching, and so on. But we only care about one particular feature right now: the ability to share an IP address between multiple machines. This is known as a “web rule” in ISA parlance. With appropriate web rules in effect for both of our sites, ISA Server will shuttle the HTTP requests back and forth to the correct private IP addresses based on the host headers. It basically extends the host header routing concepts we saw in Apache and IIS outside the confines of a particular machine.

kg-card-begin: html

```

ISA Server         10.0.0.1:80
codinghorror.com   192.168.0.1:80
haacked.com        192.168.0.2:80

```

kg-card-end: html

That’s one way you can host fifty websites, all running on fifty different machines, with a single public IP address. It’s a very clever trick indeed. Unfortunately, ISA Server isn’t the simplest of products to configure and administer. I’m glad we have enough public IPs that we don’t have to worry about sharing them between multiple machines. But it’s definitely something you should be aware of, as virtual servers become increasingly commonplace... and the pool of available IP addresses [continues to dwindle](https://web.archive.org/web/20071226181730/http://www.networkworld.com/news/2007/062807-ipv6-deadline.html).

[virtualization](https://blog.codinghorror.com/tag/virtualization/)
[server hosting](https://blog.codinghorror.com/tag/server-hosting/)
[virtual machines](https://blog.codinghorror.com/tag/virtual-machines/)
[bandwidth management](https://blog.codinghorror.com/tag/bandwidth-management/)
[internet connections](https://blog.codinghorror.com/tag/internet-connections/)
