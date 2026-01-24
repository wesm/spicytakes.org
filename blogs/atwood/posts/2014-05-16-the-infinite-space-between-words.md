---
title: "The Infinite Space Between Words"
date: 2014-05-16
url: https://blog.codinghorror.com/the-infinite-space-between-words/
slug: the-infinite-space-between-words
word_count: 694
---

Computer performance is a [bit of a shell game](https://blog.codinghorror.com/the-computer-performance-shell-game/). You’re always waiting for one of four things:

- Disk
- CPU
- Memory
- Network


But which one? How long will you wait? And what will you do while you’re waiting?


Did you see [the movie “Her”](http://www.imdb.com/title/tt1798709)? If not, you should. It’s great. One of my favorite scenes is the AI describing just how difficult it becomes to communicate with humans:


> It’s like I’m reading a book… and it’s a book I deeply love. But I’m reading it slowly now. So the words are really far apart and the spaces between the words are almost infinite. I can still feel you… and the words of our story… but it’s in this endless space between the words that I’m finding myself now. It’s a place that’s not of the physical world. It’s where everything else is that I didn’t even know existed. I love you so much. But this is where I am now. And this who I am now. And I need you to let me go. As much as I want to, I can’t live your book any more.


I have some serious reservations about the work environment pictured in Her where everyone’s spending all day creepily whispering to their computers, but there is deep fundamental truth in that one pivotal scene. That infinite space “between” what we humans feel as time is where computers spend *all* their time. It’s an entirely different timescale.


The book, [Systems Performance: Enterprise and the Cloud](http://www.amazon.com/dp/0133390098/), has a great table that illustrates just how enormous these time differentials are. Just translate computer time into arbitrary seconds:

kg-card-begin: html


| 1 CPU cycle | 0.3 ns | 1 s |
| Level 1 cache access | 0.9 ns | 3 s |
| Level 2 cache access | 2.8 ns | 9 s |
| Level 3 cache access | 12.9 ns | 43 s |
| Main memory access | 120 ns | 6 min |
| Solid-state disk I/O | 50-150 μs | 2-6 days |
| Rotational disk I/O | 1-10 ms | 1-12 months |
| Internet: SF to NYC | 40 ms | 4 years |
| Internet: SF to UK | 81 ms | 8 years |
| Internet: SF to Australia | 183 ms | 19 years |
| OS virtualization reboot | 4 s | 423 years |
| SCSI command time-out | 30 s | 3000 years |
| Hardware virtualization reboot | 40 s | 4000 years |
| Physical system reboot | 5 m | 32 millenia |


kg-card-end: html

The above Internet times are kind of optimistic. If you look at the AT&T real time [US internet latency chart](http://ipnetwork.bgtmo.ip.att.net/pws/network_delay.html), the time from SF to NYC is more like 70ms. So I’d double the Internet numbers in that chart.


![](https://blog.codinghorror.com/content/images/2025/02/image-130.png)


Latency is one thing, but it’s also worth considering [the cost of that bandwidth](https://blog.codinghorror.com/the-economics-of-bandwidth/).


Speaking of the late, great [Jim Gray](http://en.wikipedia.org/wiki/Jim_Gray_(computer_scientist)), he also had an interesting way of explaining this. If the CPU registers are how long it takes you to fetch data from your brain, then **going to disk is the equivalent of fetching data from Pluto.**


![](https://blog.codinghorror.com/content/images/2025/02/image-129.png)


He was probably referring to traditional spinning rust hard drives, so let’s adjust that extreme endpoint for today:

- Distance to Pluto: 4.67 billion miles.
- Latest fastest spinning HDD performance ([49.7](http://www.anandtech.com/show/5729/western-digital-velociraptor-1tb-wd1000dhtz-review/3)) versus latest fastest PCI Express SSD ([506.8](http://anandtech.com/show/8006/samsung-ssd-xp941-review-the-pcie-era-is-here/6)). That’s an improvement of 10x.
- New distance: 467 million miles.
- Distance to Jupiter: 500 million miles.


So instead of travelling to Pluto to get our data from disk in 1999, **today we only need to travel to… Jupiter**.


![](https://blog.codinghorror.com/content/images/2025/02/image-131.png)


That’s disk performance over the last decade. How much faster did CPUs, memory, and networks get in the same time frame? Would a 10x or 100x improvement really make a dent in these vast infinite spaces in time that computers deal with?


To computers, we humans work on a completely different time scale, practically [geologic time](http://en.wikipedia.org/wiki/Timeline_of_the_far_future). Which is completely mind-bending. The faster computers get, the bigger this time disparity grows.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
