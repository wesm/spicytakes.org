---
title: "Because Everyone Needs a Router"
date: 2010-09-25
url: https://blog.codinghorror.com/because-everyone-needs-a-router/
slug: because-everyone-needs-a-router
word_count: 1176
---

Do you remember when a router used to be an exotic bit of network kit?


Those days are long gone. A router is one of those salt-of-the-earth items now; **anyone who pays for an internet connection needs a router**, for:

1. NAT and basic hardware firewall protection from internet evildoers
2. A wired network hub to connect local desktop PCs
3. A wireless hub to connect laptops, phones, consoles, etcetera


Let me put it this way: my mom – and my wife’s mom – both own routers. If that isn’t the definition of *mainstream*, I don’t know what is.


Since my livelihood revolves around being on the internet, and because I’m a bit of a tweaker, I have a fancy-ish router. But it is [of late 2007 vintage](https://blog.codinghorror.com/gifts-for-geeks-2007-edition/):


![](https://blog.codinghorror.com/content/images/2025/04/image-489.png)


Although the [DGL-4500](http://www.amazon.com/exec/obidos/ASIN/B000Z7AKGC) is a nice router, and it has served me well with no real complaints, the last major firmware update for it was a year and a half ago. There have been some desultory minor updates since then, but clearly the vendor has, shall we say, *moved on* to focusing on newer models.


The router is (literally!) the central component in my overall internet experience, and I was growing increasingly uncomfortable with the status quo. Frankly, the prospect of three year old hardware with year old firmware gives me the heebie-jeebies.


So, I asked the pros at [Super User](http://superuser.com/), even going so far as to set up a Recommend Me a Router chat room. (We disallow product recommendation questions as they become uselessly out of date so quickly, but this is a perfect topic for a chat room.) I got some fantastic advice from my fellow Super Users via chat, though much of it was of the far too sane “if it ain’t broke don’t fix it” variety. Well, that’s just [not how I work](https://blog.codinghorror.com/dont-be-afraid-to-break-stuff/). To be fair, the router market is not exactly a hotbed of excitement at the moment; it is both saturated and heavily commoditized, particularly now that the dust has settled from the whole [802.11 A/B/G/N debacle](http://en.wikipedia.org/wiki/IEEE_802.11). There just isn’t much going on.


But in the process of doing my router research, I discovered something important, and maybe even revolutionary in its own quiet little way. **The best router models all run open source firmware!**

- [DD-WRT](http://en.wikipedia.org/wiki/DD-WRT)
- [Tomato](http://en.wikipedia.org/wiki/Tomato_(firmware))


That’s right, the truly great routers [are available in “awesome” edition](https://blog.codinghorror.com/oh-you-wanted-awesome-edition/). (There may be other open source router firmwares out there, but these are the two I saw most frequently.) I learned that these open source firmwares can turn a boring Clark Kent router into Superman. And they are *always* kept updated by the community, in perpetuity.


In my weaker moments, I toyed with the idea of building [a silent mini x86 PC](https://web.archive.org/web/20101224033030/http://techreport.com/articles.x/19227) that could run a routing optimized distribution of Linux, but the reality is that current commodity routers have *more* than enough memory and embedded CPU power – not to mention the necessary wireless and gigabit ethernet hub bits already built in. Dedicating a whole x86 PC to routing is power inefficient, overly complex, and awkward.


Yes, today’s router marketplace is commoditized and standardized and boring – but there are still a few clear hardware standouts. I turned to the experts at [SmallNetBuilder](http://www.smallnetbuilder.com/) for their in-depth technical reviews, and found two consensus recommendations:

kg-card-begin: html

Update: Though these models are still fine choices, particularly if you can find a great deal on them, I have newer recommendations in [Because Everyone (Still) Needs a Router](https://blog.codinghorror.com/because-everyone-still-needs-a-router/).

kg-card-end: html

[Buffalo Nfiniti Wireless-N High Power Router](http://www.smallnetbuilder.com/wireless/wireless-reviews/30889-buffalo-nfiniti-wireless-n-high-power-router-a-access-point-reviewed) ($80)


![](https://blog.codinghorror.com/content/images/2025/04/image-488.png)


[NETGEAR WNDR3700 RangeMax Dual Band Wireless-N](http://www.smallnetbuilder.com/wireless/wireless-reviews/30925-start-your-buying-netgear-wndr3700-reviewed) ($150)


![](https://blog.codinghorror.com/content/images/2025/04/image-487.png)


Both of these models got glowing reviews from the networking experts at SmallNetBuilder, and both are 100% compatible with the [all-important open source dd-wrt firmware](http://www.dd-wrt.com). You can’t go wrong with either, but I chose the less expensive [Buffalo Nfiniti router](http://www.amazon.com/dp/B0028ACYEK). Why?

1. It’s almost half the price, man!
2. The “high power” part is verifiably and benchmarkably true, and I have some [wireless range problems](https://blog.codinghorror.com/extending-your-wireless-network-with-better-antennas/) at my home.
3. I do most of my heavy network lifting through wired gigabit ethernet, so I can’t think of any reason I’d need the higher theoretical wireless throughput of the Netgear model.
4. Although the Netgear has a 680 Mhz embedded CPU and 128mb RAM, the Buffalo’s 400 MHz embedded CPU and 64mb of RAM is not exactly chopped liver, either; it’s plenty for dd-wrt to work with. I’d almost go so far as to say the Netgear is a bit overkill… if you’re into that sort of thing.


I received my Buffalo Nfiniti and immediately installed dd-wrt on it, which was very simple and accomplished through the existing [web UI on the router](http://dd-wrt.com/wiki/index.php/Buffalo_WZR-HP-G300NH). (Buffalo has a history of shipping rebranded dd-wrt distributions in their routers, so the out-of-box firmware is a kissing cousin.)


After rebooting, I was in love. The (more) modern gigabit hardware, CPU, and chipset was noticably snappier everywhere, even just dinking around in the admin web pages. And **dd-wrt scratches *every geek itch I have*** – putting that newer hardware to great use. Just check out the detailed stats I can get, including that pesky wireless signal strength problem. The top number is the Xbox 360 outside, the bottom number is my iPhone from about 10 feet away.


![](https://blog.codinghorror.com/content/images/2025/04/image-486.png)


Worried your router is running low on embedded CPU grunt, or that 64 megabytes of memory is insufficient? Never fear; dd-wrt has you covered. Just check out the detailed, real time memory and cpu load stats.


![](https://blog.codinghorror.com/content/images/2025/04/image-485.png)


Trying to figure out how much WAN/LAN/Wireless bandwidth you’re using? How does a real time SVG graph, right from the router admin pages, grab you?


![](https://blog.codinghorror.com/content/images/2025/04/image-484.png)


It’s just great all around. And I haven’t even covered the proverbial laundry list of [features that dd-wrt offers](http://www.dd-wrt.com/wiki/index.php/What_is_DD-WRT%3F) above and beyond most stock firmware! Suffice it to say that this is one of those times when the “let’s support everything” penchant of open source projects works in our favor. Don’t worry, it’s all (mostly) disabled by default. Those features and tweaks can all safely be ignored; just know that they’re available to you when and if you need them.


This is boring old plain vanilla commodity router hardware, but when combined with an open source firmware, it is a *massive* improvement over my three year old, proprietary high(ish) end router. The magic router formula these days is **a combination of commodity hardware and open-source firmware.** I’m so enamored of this one-two punch combo, in fact, I might even say it represents the future. Not just of the everyday workhorse routers we all need to access the internet – but the future of all commodity hardware.


Routers; we all need ’em, and they are crucial to our internet experience. Pick whichever router you like – as long as it’s compatible with one of the open source firmware packages! Thanks to a wide variety of mature commodity hardware choices, plus infinitely and perpetually updated open source router firmware, I’m happy to report that **now everyone can have a *great* router**.

[networking](https://blog.codinghorror.com/tag/networking/)
[router](https://blog.codinghorror.com/tag/router/)
[security](https://blog.codinghorror.com/tag/security/)
[firmware](https://blog.codinghorror.com/tag/firmware/)
[hardware protection](https://blog.codinghorror.com/tag/hardware-protection/)
