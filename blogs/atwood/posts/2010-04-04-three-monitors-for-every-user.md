---
title: "Three Monitors For Every User"
date: 2010-04-04
url: https://blog.codinghorror.com/three-monitors-for-every-user/
slug: three-monitors-for-every-user
word_count: 978
---

As far as I’m concerned, you can never be too rich, too thin, or have too much screen space. By “screen,” I mean not just large monitors, but *multiple* large monitors. I’ve been evangelizing multiple monitors since the dark days of [Windows Millennium Edition](http://en.wikipedia.org/wiki/Windows_Me):

- [Multiple Monitors and Productivity](https://blog.codinghorror.com/multiple-monitors-and-productivity/)
- [Multiple LCDs](https://blog.codinghorror.com/multiple-lcds/)
- [Joining the Prestigious Three Monitor Club](https://blog.codinghorror.com/joining-the-prestigious-three-monitor-club/)
- [The Large Display Paradox](https://blog.codinghorror.com/the-large-display-paradox/)
- [LCD Monitor Arms](https://blog.codinghorror.com/lcd-monitor-arms/)


If you’re a long time reader you’re probably sick of hearing about this stuff by now, but something rather wonderful has happened since I last wrote about it:

kg-card-begin: html

> If you’re only using one monitor, you are cheating yourself out of potential productivity. Two monitors is a no-brainer. It’s so fundamental that I included it as a part of the [Programmer’s Bill of Rights](https://blog.codinghorror.com/the-programmers-bill-of-rights/).
> But you can do better.
> **As good as two monitors is, three monitors is even better**. With three monitors, there’s a “center” to focus on. And 50% more display area. While there’s certainly a point of diminishing returns for additional monitors, I think three is the sweet spot. Even Edward Tufte, in the [class I recently attended](https://blog.codinghorror.com/reading-with-edward-tufte/), explicitly mentioned multiple monitors. I don’t care how large a single display can be; you can never have enough desktop space.
> Normally, to achieve three monitors, you have to either:
> Buy an exotic video card that has more than 2 monitor connections.
> Install a second video card.

kg-card-end: html

Fortunately, that is no longer true. I was excited to learn that the latest ATI video cards have gone from two to three video outputs. Which means **you can now achieve triple monitors with a single video card upgrade!** They call this “[eyefinity](https://web.archive.org/web/20100315163458/http://sites.amd.com/US/UNDERGROUND/PRODUCTS/EYEFINITY/WHATISEYEFINITY/Pages/what-is-eyefinity.aspx),” but it’s really just shorthand for “raising the standard from two display outputs to three.”


But, there is a (small) catch. The PC ecosystem is in the middle of shifting display output standards. For evidence of this, you need look no further than the back panel of one of these newfangled triple display capable ATI video cards:


![](https://blog.codinghorror.com/content/images/2025/04/image-469.png)


It contains:

- two DVI outputs
- one HDMI output
- one [DisplayPort](http://en.wikipedia.org/wiki/DisplayPort) output


I suspect part of this odd connector layout is due to space restrictions (DVI is awfully chunky), but I’ve always understood DisplayPort to be the new, improved DVI connector for computer monitors, and HDMI to be the new, improved s-video/component connector for televisions. Of course these worlds are blurring, as modern high-definition TVs make [surprisingly effective computer monitors](https://blog.codinghorror.com/will-your-next-computer-monitor-be-a-hdtv/), too.


Anyway, since all my monitors have only DVI inputs, I wasn’t sure what to do with the other output. So [I asked on Super User](http://superuser.com/questions/118957/converting-displayport-and-or-hdmi-to-dvi-d). The helpful answers led me to discover that, as I suspected, the third output has to be DisplayPort. So to connect my third monitor, I needed to **convert DisplayPort to DVI**, and there are two ways:

1. a [passive, analog DisplayPort to DVI conversion cable](http://www.amazon.com/dp/B0007MWE1Y) for ~$30 that supports up to 1920x1200
2. an [active, digital DisplayPort to DVI converter](http://www.amazon.com/dp/B002ISVI3U) for $110 that supports all resolutions


I ended up going with the active converter, which has mixed reviews, but it’s worked well for me over the last few weeks.


![](https://blog.codinghorror.com/content/images/2025/04/image-468.png)


Note that this adapter requires USB power, and given the spotty results others have had with it, some theorize that it needs quite a bit of juice to work reliably. I plugged it into my system’s nearby rear USB ports which do tend to deliver more power (they’re closer to the power supply, and have short cable paths). Now, I *have* gotten the occasional very momentary black screen with it, but nothing severe enough to be a problem or frequent enough to become a pattern. If you have DisplayPort compatible monitors, of course, this whole conversion conundrum is a complete non-issue. But DisplayPort is fairly new, and even my new-ish LCD monitors don’t support it yet.


The cool thing about this upgrade, besides [feeding my video card addiction](https://blog.codinghorror.com/feeding-my-graphics-card-addiction/), is that **I was able to simplify my hardware configuration**. That’s always good. I went from two video cards to one, which means less power consumption, simpler system configuration, and fewer overall driver oddities. Basically, it makes triple monitors – dare I say it – almost a *mainstream* desktop configuration. How could I not be excited about that?


I was also hoping that Nvidia would follow ATI’s lead here and **make three display outputs the standard for all their new video cards**, too, but sadly that’s not the case. It turns out their new GTX 480 fails in other ways, in that it’s basically [the Pentium 4 of video cards](https://web.archive.org/web/20100409114908/http://www.maximumpc.com/article/features/nvidias_hot_rod_gtx_480_powerful_and_power_hungry?page=0,1) – generating ridiculous amounts of heat for very little performance gain. Based on those two facts, I am comfortable endorsing ATI wholeheartedly at this point. But, do be careful, because not all ATI cards support triple display outputs (aka “eyefinity”). These are the ones that I know do:

- [Radeon HD 5670](http://www.amazon.com/dp/B0033WSDO2) (~$100)
- [Radeon HD 5770](http://www.amazon.com/dp/B002SP113K) (~$150)
- [Radeon HD 5830](http://www.amazon.com/dp/B0039YOMZI) (~$250)
- [Radeon HD 5850](http://www.amazon.com/dp/B002QEBGGA) (~$320)
- [Radeon HD 5870](http://www.amazon.com/dp/B003D0QQJS) (~$450)


Unless you’re a gamer, there’s no reason to care about anything other than the least expensive model here, which will handily *crush* any 2D or 3D desktop GUI acceleration needs you might have. As an addict, of course I bought the high end model and it absolutely did not disappoint – more than doubling my framerates in the excellent game [Battlefield: Bad Company 2](http://www.amazon.com/dp/B002NIP2SM) over the GTX 280 I had before.


I’m excited that a triple monitor setup is now, thanks to ATI, so easily attainable for desktop users – as long as you’re aware of the DisplayPort caveat I discussed above. I’d encourage anyone who is even *remotely* interested in the (many) productivity benefits of a triple monitor setup to seriously consider an ATI video card upgrade.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
