---
title: "We used to build steel mills near cheap power. Now that's where we build datacenters"
date: 2015-05-01
url: https://danluu.com/datacenter-power/
slug: datacenter-power
word_count: 1055
---


Why are people so concerned with hardware power consumption nowadays? Some common answers to this question are thatpower is critically important for phones, tablets, and laptopsand thatwe can put more silicon on a modern chip than we can effectively use. In 2001Patrick Gelsinger observed that if scaling continued at then-current rates, chips would have the power density of a nuclear reactor by 2005, a rocket nozzle by 2010, and the surface of the sun by 2015, implying that power density couldn't continue on its then-current path. Although this was already fairly obvious at the time, now that it's 2015, we can be extra sure that power density didn't continue to grow at unbounded rates. Anyway, the importance of portables and scaling limits are both valid and important reasons, but since they're widely discussed, I'm going to talk about an underrated reason.

People often focus on the portable market because it's cannibalizing desktop market, but that's not the only growth market -- servers are also becoming more important than desktops, and power is really important for servers. To see why power is important for servers, let's look at some calculations about how what it costs to run a datacenter fromHennessy & Patterson.

One of the issues is that you pay for power multiple times. Some power is lost at the substation, although we might not have to pay for that directly. Then we lose more storing energy in a UPS. This figure below states 6%, but smaller scale datacenters can easily lose twice that. After that, we lose more power stepping down the power to a voltage that a server can accept. That's over a 10% loss for a setup that's pretty efficient.

After that, we lose more power in the server's power supply, stepping down the voltage to levels that are useful inside a computer, which is often about another 10% loss (not pictured in the figure below).

And then once we get the power into servers, it gets turned into waste heat. To keep the servers from melting, we have to pay for power to cool them.Barroso and Holzleestimated that 30%-50% of the power drawn by a datacenter is used for chillers, and that an additional 10%-20% is for theCRAC(air circulation). That means for every watt of power used in the server, we pay for another 1-2 watts of support power.

And to actually get all this power, we have to pay for the infrastructure required to get the power into and throughout the datacenter. Hennessy & Patterson estimate that of the $90M cost of an example datacenter (just the facilities -- not the servers), 82% is associated with power and cooling1. The servers in the datacenter are estimated to only cost $70M. It's not fair to compare those numbers directly since servers need to get replaced more often than datacenters; once you take into account the cost over the entire lifetime of the datacenter, the amortized cost of power and cooling comes out to be 33% of the total cost, when servers have a 3 year lifetime and infrastructure has a 10-15 year lifetime.

If we look at all the costs, the breakdown is:

[Table]

| category% | % |
| server machines53 | 53 |
| power & cooling infra20 | 20 |
| power use13 | 13 |
| networking8 | 8 |
| other infra4 | 4 |
| humans2 | 2 |

Power use and people are the cost of operating the datacenter (OPEX), whereas server machines, networking, power & cooling infra, and other infra are capital expenditures that are amortized across the lifetime of the datacenter (CAPEX).

Computation uses a lot of power.We used to build steel mills near cheap sources of power, butnow that's where we build datacenters. As companies start considering the full cost of applications, we're seeing a lot more power optimized solutions2. Unfortunately, this is really hard. On the software side, with the exceptions of toy microbenchmark examples,best practices for writing power efficient code still aren't well understood. On the hardware side, Intel recently released a new generation of chips with significantly improved performance per watt that doesn't have much better absolute performance than the previous generation. On the hardware accelerator front, some large companies are building dedicated power-efficient hardware for specific computations. But with existing tools, hardware accelerators are costly enough that dedicated hardware only makes sense for the largest companies. There isn't an easy answer to this problem.

If you liked this post, you'd probably like chapter 6 ofHennessy & Patterson, which walks through not only the cost of power, but a number of related back of the envelope calculations relating to datacenter performance and cost.

Apologies for the quickly scribbled down post. I jotted this down shortly before signing an NDA for an interview where I expected to learn some related information and I wanted to make sure I had my thoughts written down before there was any possibility of being contaminated with information that's under NDA.

Thanks to Justin Blank for comments/corrections/discussion.

---

1. Although this figure is widely cited, I'm unsure about the original source. This is probably the most suspicious figure in this entire post. Hennessy & Patterson cite “Hamilton 2010”, which appears to be a reference tothis presentation. That presentation doesn't make the source of the number obvious, althoughthis post by Hamilton does cite a reference for that figure, but the citation points tothis post, which seems to be about putting datacenters in tents, not the fraction of infrastructure that's dedicated to power and cooling.Some other works,such as this onecitethis article. However, that article doesn't directly state 82% anywhere, and it makes a number of estimates that the authors acknowledge are very rough, with qualifiers like “While, admittedly, the authors state that there is a large error band around this equation, it is very useful in capturing the magnitude of infrastructure cost.”[return]
2. That being said, power isn't everything -- Reddi et al. looked at replacing conventional chips with low-power chips for a real workload (MS Bing) and found that while they got an improvement in power use per query, tail latency increased significantly, especially when servers were heavily loaded. Since Bing has a mechanism that causes query-related computations to terminate early if latency thresholds are hit, the result is both higher latency and degraded search quality.[return]
