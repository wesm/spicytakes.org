---
title: "VM Server Hosting"
date: 2005-05-25
url: https://blog.codinghorror.com/vm-server-hosting/
slug: vm-server-hosting
word_count: 272
---

My friend Josh Carlisle was kind enough to host this website during my move to California. Josh set me up with a Microsoft Virtual Server slice of Windows 2003 Standard on his Xeon 2.8 server. I’m currently running a WIMP (Windows, IIS, MySql, Perl) configuration which I was able to set up remotely without issue.


Although everything is generally running quite well, and the commit charge is well under 256mb in Task Manager, **I am disappointed with VM performance**... [again](https://blog.codinghorror.com/virtual-pc-2004-tips/). Intel’s Xeon 2.8ghz is basically just a rebranded Pentium 4 2.8ghz, but that’s still way more performance than I need. Unfortunately, under actual use, it performs more like a 1.4ghz Pentium 4 – the older version with only 512kb L2 cache! HTTP post operations that used to take under a second take multiple seconds; installs that used to be a minute long take upwards of five minutes, etcetera.


VMs are great for convenience, but the performance cost is quite a bit higher than I expected it to be – on both client and server. Even if you aren’t emulating the x86 processor, the cost of emulating the motherboard hardware is clearly *substantial*. Particularly for disk and video. I found this list of [Virtual Server performance tips](https://web.archive.org/web/20060105045935/http://www.roudybob.net/?p=101), although it’s not very server specific – it’s basically the same advice I’ve seen for Virtual PC. No silver bullet there; get the fastest disks you can afford, dedicate them to VMs, and make sure you have enough memory. Virtual PC guy also has some interesting tips for remote desktop-ing [into a virtual server](https://web.archive.org/web/20051207020714/http://blogs.msdn.com/virtual_pc_guy/archive/2005/05/02/414187.aspx).

[virtualization](https://blog.codinghorror.com/tag/virtualization/)
[server hosting](https://blog.codinghorror.com/tag/server-hosting/)
[vm performance](https://blog.codinghorror.com/tag/vm-performance/)
[microsoft virtual server](https://blog.codinghorror.com/tag/microsoft-virtual-server/)
[windows 2003](https://blog.codinghorror.com/tag/windows-2003/)
[xeon server](https://blog.codinghorror.com/tag/xeon-server/)
