---
title: "The State of Solid State Hard Drives"
date: 2009-10-13
url: https://blog.codinghorror.com/the-state-of-solid-state-hard-drives/
slug: the-state-of-solid-state-hard-drives
word_count: 960
---

I’ve seen a lot of people play [The Computer Performance Shell Game](https://blog.codinghorror.com/the-computer-performance-shell-game/) poorly. They overinvest in a fancy CPU, while pairing it with limited memory, a plain jane hard drive, or a generic video card. For most users, that fire-breathing quad-core CPU is sitting around twiddling its virtual thumbs most of the time. Computer performance is typically limited by the *slowest* part in your system. You’d get better overall performance by building a balanced system and removing bottlenecks.


One of those key bottlenecks – and in my experience, the one typical users are most likely to underestimate – is the hard drive. I’ve been a long time advocate of having a small, fast [10,000 RPM boot drive](https://blog.codinghorror.com/you-want-a-10000-rpm-boot-drive/) for your OS and key applications, and a larger, slower secondary drive for storage. The two drive approach is a smart strategy, regardless of your budget.


Hard drives may not be particularly sexy bits of hardware, but we’re on the verge of a **major transition point in storage hardware** – from physical, magnetic platters to solid state memory. I was an early solid state (SSD) drive adopter with [my last laptop purchase](https://blog.codinghorror.com/dell-xps-m1330-review/), and it was a profound disappointment. Those first and second generation SSD drives turned out to be *slower* than their magnetic equivalents, despite the eager promises of vendors. On top of that, they were incredibly expensive, and of limited capacity. Running Windows Vista on an early 32 gigabyte SSD was an exercise in pain and frustration on so many levels. What’s not to love? A lot.


I eventually sold that SSD and replaced it with a traditional hard drive. I had grown deeply disillusioned with SSD drives. That is, until I read Linus Torvalds’ report [on the Intel X-25 SSD](http://torvalds-family.blogspot.com/2008/10/so-i-got-one-of-new-intel-ssds.html):


> I can’t recall the last time that a new tech toy I got made such a dramatic difference in performance and just plain usability of a machine of mine.
> The whole thing just rocks. Everything performs well. You can put that disk in a machine, and suddenly you almost don’t even need to care whether things were in your page cache or not. Firefox starts up pretty much as snappily in the cold-cache case as it does hot-cache. You can do package installation and big untars, and you don’t even notice it, because your desktop doesn’t get laggy or anything.
> So here’s the deal: right now, don’t buy any other SSD than the Intel ones, because as far as I can tell, all the other ones are pretty much inferior to the much cheaper traditional disks, unless you never do any writes at all (and turn off ‘atime’, for that matter).


At that moment, SSD drives came of age. And by that I mean, **they began to justify their hefty price premium at last**. But that was almost a year ago, and even the Intel drives – as great as they were – had [some teething problems](http://hardware.slashdot.org/article.pl?sid=09/02/13/2337258). Not to mention that price and capacity were still ongoing concerns.


But when Intel introduced the [second generation, mainstream X25-M drives](https://web.archive.org/web/20091025102700/http://techreport.com/articles.x/17269/1), that’s when I knew SSDs were poised to go mainstream. Now, those drives are still anything but *cheap*, at **$289 for 80 GB** and **$609 for 160 GB**. But they offer more performance than the original X25-E that Linus reviewed, at about half the price, with hardware fixes to address the fragmentation issue that plagued the original model.


Intel was the only game in town for about a year, but fortunately for us consumers, the competition finally caught up. The new Indilinx controller models, such as this Crucial 128 GB SSD, are just as fast as the X25-M. And, best of all, they’re *cheaper*, while also offering a not-insubstantial bump to 128 GB of storage!


![](https://blog.codinghorror.com/content/images/2025/04/image-431.png)


I picked this model up for **$325** plus tax and shipping. And, frankly, I was **blown away by the performance difference** compared to the 300 GB Velociraptor I had in my system before. That drive is not exactly chopped liver; it’s incredibly fast by magnetic platter drive standards. But it’s *beyond* slow next to the latest SSDs. See for yourself:


![](https://blog.codinghorror.com/content/images/2025/04/image-430.png)


This is just an excerpt, [browse the reviews](http://www.google.com/search?q=crucial+CT128M225+ssd+review) for more detail, but I was astonished how often this drive (based on the Indilinx Barefoot controller) topped the charts. Suffice it to say, **the performance increase is not subtle**. All those little pauses while your system pulls some chunk of data off the hard drive? They simply *cease to exist*.


How much do I like this drive? I like it so very much I bought one for every member of the Stack Overflow team, as a small gesture of thanks for enduring [new feature crunch mode](http://blog.stackoverflow.com/2009/10/introducing-stack-overflow-careers/). I couldn’t sell my old Velociraptor on eBay fast enough.


In my humble opinion, $200 - $300 for a SSD is *easily* **the most cost effective performance increase you can buy** for a computer of anything remotely resembling recent vintage. Whether you prefer the 80 GB X25-M SSD or the 128 GB Crucial SSD, it’s money well invested for people like us who are obsessive about how their computer performs.


Trust me, you *will* feel the performance difference of a modern SSD in day to day computing. That’s **far more than I can say for most of today’s CPU and memory upgrades**. The transition from magnetic storage to solid state storage is nothing less than a breakthrough. It’s already transformative; I can only imagine how fast, cheap, and large these drives are going to be in a few years. So, if you’ve ever wondered what performance would be like if everything was in RAM all the time – well, we just got one giant step closer to that.

[storage](https://blog.codinghorror.com/tag/storage/)
[hard drives](https://blog.codinghorror.com/tag/hard-drives/)
[solid state drives](https://blog.codinghorror.com/tag/solid-state-drives/)
[computer performance](https://blog.codinghorror.com/tag/computer-performance/)
[storage hardware](https://blog.codinghorror.com/tag/storage-hardware/)
