---
title: "The Popularity Tax"
date: 2004-08-08
url: https://blog.codinghorror.com/the-popularity-tax/
slug: the-popularity-tax
word_count: 740
---

I’m sure everyone reading this is familiar with [the slashdot effect](https://web.archive.org/web/20041122010801/http://slashdot.org/faq/slashmeta.shtml):


> When Slashdot links a site, often a lot of readers will hit the link to read the story or see the purty pictures. This can easily throw thousands of hits at the site in minutes. Most of the time, large professional websites have no problem with this, but often a site we link will be a smaller site, used to getting only a few thousand hits a day. When all those Slashdot readers start crashing the party, it can saturate the site completely, causing the site to buckle under the strain. When this happens, the site is said to be “Slashdotted.” Recently, the terms “Slashdot Effect” and “Slashdotted” have been used more generally to refer to any short-term traffic jam at a website.


The slashdot effect is an interesting illustration of what I call **the popularity tax: the more popular the content is, the more it costs the content owner**. This is unique to the world of bits (e.g., the internet). In the world of atoms (e.g., the real world), it’s the exact opposite: mere popularity doesn’t cost the content owner a dime. If you have something people want, they have to pay to physically get to it, one way or another. Compare a book or a movie to, say, that Bush/Kerry flash movie. Who is footing the massive bandwidth bill for the tens of thousands of people downloading that file?


At the very root of this discussion is, of course, **the cost of bandwidth**. Computer hardware may get cheaper every day and free open source software seems to be flourishing, but bandwidth shows no sign of following the same trends. There’s an interesting Microsoft Research Paper on this topic: Jim Gray’s [Distributed Computing Economics](https://web.archive.org/web/20070103194914/http://dslab.epfl.ch/courses/pods/winter06-07/readings/gray-economics.html).


> Computing economics are changing. Today there is rough price parity between (1) one database access, (2) ten bytes of network traffic, (3) 100,000 instructions, (4) 10 bytes of disk storage, and (5) a megabyte of disk bandwidth. This has implications for how one structures Internet-scale distributed computing: **one puts computing as close to the data as possible in order to avoid expensive network traffic.**


In other words, bandwidth is hellaciously expensive relative to almost anything else, other than perhaps labor costs (and thus software?)


> From this we conclude that one dollar equates to:

kg-card-begin: html


| $1= | 1GB sent over the WAN10Tops tera-CPU instructions8hours of cpu time1GB disk space10M database accesses10TB of disk bandwidth | 1 | GB sent over the WAN | 10 | Tops tera-CPU instructions | 8 | hours of cpu time | 1 | GB disk space | 10 | M database accesses | 10 | TB of disk bandwidth |
| 1 | GB sent over the WAN |
| 10 | Tops tera-CPU instructions |
| 8 | hours of cpu time |
| 1 | GB disk space |
| 10 | M database accesses |
| 10 | TB of disk bandwidth |


kg-card-end: html

So, we have this weird situation on the internet where popularity is a curse, instead of the blessing it should be. This is a terrible state of affairs, a major disincentive to build anything that a lot of people will consume. Right now, unless you are leveraging your popularity to sell something, you are generating a substantial net loss through bandwidth costs. This has always been my [argument for micropayments](http://www.useit.com/alertbox/980125.html), which lets the popularity equal income, but there are a lot of heavyweight barriers to this ever happening, such as the current banking industry’s inability to deal with any volume of tiny transactions.


Micropayments are one answer, but [micropayments have problems](https://web.archive.org/web/20040929073721/http://shirky.com/writings/fame_vs_fortune.html) of their own. I don’t really have any good answers to the bandwidth cost issue. It is a serious, complex problem with no easy resolution. In a worst case scenario, **highly asymmetric upload/download ratios can be an indirect way for big corporations to enforce copyright restrictions on consumers**. The typical cable modem can download data at 300kb/sec but can only upload at a measly 30kb/sec (or less!). Can’t shut down Kazaa or Napster through legislation? The next best thing is to remove people’s ability to upload, thus crippling p2p at its very source. This creates a digital ghetto: 99% of users are locked into the role of ravenous consumers, with massive download capacities but a mere trickle of upload.

[scalability](https://blog.codinghorror.com/tag/scalability/)
[website traffic](https://blog.codinghorror.com/tag/website-traffic/)
[performance optimization](https://blog.codinghorror.com/tag/performance-optimization/)
[internet infrastructure](https://blog.codinghorror.com/tag/internet-infrastructure/)
