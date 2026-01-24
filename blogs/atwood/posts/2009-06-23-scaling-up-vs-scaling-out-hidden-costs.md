---
title: "Scaling Up vs. Scaling Out: Hidden Costs"
date: 2009-06-23
url: https://blog.codinghorror.com/scaling-up-vs-scaling-out-hidden-costs/
slug: scaling-up-vs-scaling-out-hidden-costs
word_count: 858
---

In [My Scaling Hero](https://blog.codinghorror.com/my-scaling-hero/), I described the amazing scaling story of plentyoffish.com. It’s impressive by any measure, but also particularly relevant to us because we’re on the Microsoft stack, too. I was intrigued when Markus [posted this recent update](https://web.archive.org/web/20090803041358/http://plentyoffish.wordpress.com/2009/06/14/upgrades-themes-date-night/):


> Last Monday we upgraded our core database server after a power outage knocked the site offline. I haven’t touched this machine since 2005 so it was a major undertaking to do it last minute. We upgraded from a machine with 64 GB of ram and 8 CPUs to **a HP ProLiant DL785 with 512 GB of ram and 32 CPUs**...


The HP ProLiant DL785 G5 *starts* at $16,999 – and that’s barebones, with nothing inside. Fully configured, as Markus describes, it’s [kind of a monster](https://web.archive.org/web/20090803041359/http://h18004.www1.hp.com/products/quickspecs/13046_na/13046_na.html):

- 7U size (a typical server is 2U, and mainstream servers are often 1U)
- 8 CPU sockets
- 64 memory sockets
- 16 drive bays
- 11 expansion slots
- 6 power supplies


It’s unclear if they bought it pre-configured, or added the disks, CPUs, and memory themselves. The most expensive configuration shown on the HP website is $37,398 and that includes only 4 processors, no drives, and a paltry 32 GB memory. When topped out with ultra-expensive 8 GB memory DIMMs, 8 high end Opterons, 10,000 RPM hard drives, and everything else – by my estimates, it probably **cost closer to $100,000**. That might even be a lowball number, considering that the DL785 submitted to [the TPC benchmark website](http://www.tpc.org/results/individual_results/HP/HP_DL785_300G_11-17-2008_ES.pdf) (pdf) had a “system cost” of $186,700. And that machine only had 256 GB of RAM. (But, to be fair, that total included another major storage array, and a bunch of software.)


At any rate, let’s assume $100,000 is a reasonable ballpark for the monster server Markus purchased. It is the very definition of **scaling up** – a seriously big iron single server.


But what if you **scaled out**, instead – [Hadoop](http://hadoop.apache.org/) or [MapReduce](https://web.archive.org/web/20090716181530/http://labs.google.com/papers/mapreduce.html) style, across lots and lots of inexpensive servers? After some initial configuration bumps, I’ve been happy with the inexpensive Lenovo ThinkServer RS110 servers we use. They’re no match for that DL785 – but they aren’t exactly chopped liver, either:

kg-card-begin: html


| Lenovo ThinkServer RS110 barebones | $600 |
| 8 GB RAM | $100 |
| 2 x eBay [drive brackets](https://blog.codinghorror.com/best-or-worst-geek-christmas-ever/) | $50 |
| 2 x 500 GB SATA hard drives, mirrored | $100 |
| Intel Xeon X3360 2.83 GHz quad-core CPU | $300 |


kg-card-end: html

Grand total of **$1,150** per server. Plus another 10 percent for tax, shipping, and so forth. I replace the bundled CPU and memory that the server ships with, and then resell the salvaged parts on eBay for about $100 – so let’s call the total price per server $1,200.


Now, assuming a **fixed spend of $100,000**, we could build **83** of those 1U servers. Let’s compare what we end up with for our money:

kg-card-begin: html


|  | **Scaling Up** | **Scaling Out** |
| CPUs | 32 | 332 |
| RAM | 512 GB | 664 GB |
| Disk | 4 TB | 40.5 TB |


kg-card-end: html

*Now* which approach makes more sense?


(These numbers are a bit skewed because that DL785 is at the absolute extreme end of the big iron spectrum. You pay a hefty premium for fully maxing out. It is possible to build a slightly less powerful server with *far* better bang for the buck.)


But there’s something else to consider: software licensing.

kg-card-begin: html


|  | **Scaling Up** | **Scaling Out** |
| OS | $2,310 | $33,200* |
| SQL | $8,318 | $49,800* |


kg-card-end: html

(If you’re using all open source software, then of course these costs will be very close to zero. We’re assuming a Microsoft shop here, with the necessary licenses for Windows Server 2008 and SQL Server 2008.)


*Now* which approach makes more sense?


What about the power costs? Electricity and rack space isn’t free.

kg-card-begin: html


|  | **Scaling Up** | **Scaling Out** |
| Peak Watts | 1,200w | 16,600w |
| Power Cost / Year | $1,577 | $21,815 |


kg-card-end: html

*Now* which approach makes more sense?


I’m not picking favorites. This is presented as food for thought. There are at least a dozen other factors you’d want to consider depending on the particulars of your situation. Scaling up and scaling out are *both* viable solutions, depending on what problem you’re trying to solve, and what resources (financial, software, and otherwise) you have at hand.


That said, I think it’s fair to conclude that **scaling out is only frictionless when you use open source software**. Otherwise, you’re in a bit of a conundrum: scaling up means paying less for licenses and a lot more for hardware, while scaling out means paying less for the hardware, and a *whole* lot more for licenses.

kg-card-begin: html

*I have *no* idea if these are the right prices for Windows Server 2008 and SQL Server 2008, because [reading about the licensing models](http://www.microsoft.com/Sqlserver/2005/en/us/licensing.aspx) makes my brain hurt. If anything, it could be substantially more.

kg-card-end: html
[scalability](https://blog.codinghorror.com/tag/scalability/)
[server infrastructure](https://blog.codinghorror.com/tag/server-infrastructure/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[database management](https://blog.codinghorror.com/tag/database-management/)
[system upgrade](https://blog.codinghorror.com/tag/system-upgrade/)
