---
title: "Our Brave New World of 4K Displays"
date: 2015-08-18
url: https://blog.codinghorror.com/our-brave-new-world-of-4k-displays/
slug: our-brave-new-world-of-4k-displays
word_count: 1320
---

It’s been three years since I last upgraded monitors. Those [inexpensive Korean 27″ IPS panels](https://blog.codinghorror.com/the-ips-lcd-revolution/), with a resolution of 2560×1440 – also known as 1440p – have served me well. You have no idea how many people I’ve witnessed being Wrong On The Internet on these babies.


![](https://blog.codinghorror.com/content/images/2015/08/read-what-the-smart-people-are-saying.png)


I recently got the upgrade itch real bad:

- 4K monitors have stabilized as a category, from super bleeding edge “I’m probably going to regret buying this” early adopter stuff, and beginning to approach mainstream maturity.
- Windows 10, with its promise of [better high DPI handling](https://www.thurrott.com/windows/windows-10/4597/windows-10-feature-focus-display-scaling), was released. I know, I know, we’ve been promised reasonable DPI handling in Windows for the last five years, but hope springs eternal. This time will be different!™
- I needed a reason to buy a new high end video card, which I was also itching to upgrade, and simplify from a [dual card config](https://blog.codinghorror.com/multiple-video-cards/) back to a (very powerful) single card config.
- I wanted to rid myself of the monitor power bricks and USB powered DVI to DisplayPort converters that those Korean monitors required. I covet simple, modern DisplayPort connectors. I was beginning to feel like a bad person because I had never even *owned* a display that had a DisplayPort connector. First world problems, man.
- 1440p at 27″ is decent, but it’s also… sort of an awkward no-man’s land. Nowhere near high enough resolution to be retina, but it *is* high enough that you probably want to scale things a bit. After living with this for a few years, I think it’s better to just suck it up and deal with giant pixels (34″ at 1440p, say), or go with something *much* more high resolution and trust that everyone is getting their collective act together by now on software support for high DPI.


Given my great experiences with modern high DPI smartphone and tablet displays (are there any other kind these days?), **I want those same beautiful high resolution displays on my desktop, too.** I’m good enough, I’m smart enough, and [doggone it, people like me](https://www.youtube.com/watch?v=-DIETlxquzY).


I was excited, then, to discover some [strong recommendations](https://pcmonitors.info/reviews/asus-pb279q/) for the [Asus PB279Q](http://www.amazon.com/dp/B00YWCYKQM/).


![](https://blog.codinghorror.com/content/images/2025/02/image-98.png)


The Asus PB279Q is a 27″ panel, same size as my previous cheap Korean IPS monitors, but it is more premium in every regard:

- 3840×2160
- “professional grade” color reproduction
- thinner bezel
- lighter weight
- semi-matte (not super glossy)
- integrated power (no external power brick)
- DisplayPort 1.2 and HDMI 1.4 support built in


It is also a more premium monitor in price, at **around $700**, whereas I got my super-cheap no-frills Korean IPS 1440p monitors for roughly half that price. But when I say no-frills, I mean it – these Korean monitors didn’t even have on-screen controls!


4K is a surprisingly big bump in resolution over 1440p – we go from 3.7 to **8.3 megapixels**.


![](https://blog.codinghorror.com/content/images/2015/08/common-hd-resolutions-compared.png)


But, is it… *retina?*


It depends how you define that term, and from what distance you’re viewing the screen. Per [Is This Retina](https://web.archive.org/web/20151225135226/http://isthisretina.com/):

kg-card-begin: html


| 27" 3840×2160 | 'retina' at a viewing distance of **21"** |
| 27" 2560×1440 | 'retina' at a viewing distance of **32"** |


kg-card-end: html

With [proper computer desk ergonomics](https://blog.codinghorror.com/computer-workstation-ergonomics/) you should be sitting with the top of your monitor at eye level, at about an arm’s length in front of you. I just measured my arm and, fully extended, it’s about 26″. Sitting at [my desk](https://blog.codinghorror.com/the-ideal-computer-desk/), I’m probably about that distance from my monitor or a bit closer, but certainly beyond the 21″ necessary to call this monitor ‘retina’ despite being 163 PPI. It definitely looks that way to my eye.


I have more words to write here, but let’s cut to the chase for the impatient and the TL;DR crowd. **This 4K monitor is totally amazing and you should buy one.** It feels exactly like going from the non-retina iPad 2 to the retina iPad 3 did, except on the desktop. It makes all the text on your screen look beautiful. There is almost no downside.


There are a few caveats, though:

- You will need a beefy video card to drive a 4K monitor. I personally went all out for the [GeForce 980 Ti](http://www.amazon.com/dp/B00YU72IS6/), because I might want to actually game at this native resolution, and the 980 Ti is the undisputed fastest single video card in the world at the moment. If you’re not a gamer, any midrange video card should do fine.
- Display scaling is definitely still a problem at times with a 4K monitor. You *will* run into apps that don’t respect DPI settings and end up magnifying-glass tiny. Scott Hanselman provided [many examples](http://www.hanselman.com/blog/LivingAHighDPIDesktopLifestyleCanBePainful.aspx) in January 2014, and although stuff has improved since then with Windows 10, it’s far from perfect. Browsers scale great, and the OS does too, but if you use any desktop apps built by careless developers, you’ll run into this. The only good long term solution is to spread the gospel of 4K and shame them into submission with me. [Preach it](https://blog.codinghorror.com/are-you-an-evangelist-too/), brothers and sisters!
- **Enable DisplayPort 1.2** in the monitor settings so you can turn on 60Hz. Trust me, you *do not* want to experience a 30Hz LCD display. It is unspeakably bad, enough to put one off computer screens forever. For people who tell you they can’t see the [difference between 30fps and 60fps](https://web.archive.org/web/20151114072216/http://30vs60.com/), just switch their monitors to 30hz and watch them squirm in pain.


Viewing those comparison videos, I begin to understand why gamers want 90Hz, 120Hz or even 144Hz monitors. 60fps / 60 Hz should be the *absolute minimum*, no matter what resolution you’re running. Luckily DisplayPort 1.2 enables 60 Hz at 4K, but only just. You’ll need DisplayPort 1.3+ [to do better than that](http://www.extremetech.com/extreme/199128-vesa-steams-ahead-with-displayport-1-4a-allows-for-8k-scaling).

- Disable the crappy built in monitor speakers. [Headphones or bust](https://blog.codinghorror.com/headphone-snobbery/), baby!
- Turn down the brightness from the standard factory default of [retina scorching 100%](https://blog.codinghorror.com/bias-lighting/) to something saner like 50%. Why do manufacturers do this? Is it because they hate eyeballs? While you’re there, you might mess around with some [basic display calibration](https://blog.codinghorror.com/computer-display-calibration-101/), too.


This Asus PB279Q 4K monitor is the **best thing I’ve upgraded on my computer in years**. Well, actually, thing(s) I’ve upgraded, because [I am not f***ing around](https://web.archive.org/web/20151208060916/http://www.theonion.com/article/coworker-with-two-computer-screens-not-fucking-aro-29151) over here.


![](https://blog.codinghorror.com/content/images/2025/02/image-99.png)


I’m a long time proponent of the [triple monitor lifestyle](https://blog.codinghorror.com/three-monitors-for-every-user/), and the only thing better than a 4K display is *three 4K displays!* That’s 11,520×2,160 pixels to you, or 6,480×3,840 if rotated.


(Good luck attempting to game on this configuration with all three monitors active, though. [You’re gonna need it](http://www.tweaktown.com/tweakipedia/88/nvidia-geforce-gtx-980-ti-4k-surround-6480x3840/index.html). Some newer games are too demanding to run on “High” settings on a *single* 4K monitor, even with the mighty [Nvidia 980 Ti](http://www.amazon.com/dp/B00YU72IS6/).)


I’ve also been experimenting with better LCD monitor arms that properly support my preferred triple monitor configurations. Here’s a picture from the back, where all the action is:


![](https://blog.codinghorror.com/content/images/2025/02/image-100.png)


These are the [Flo Monitor Supports](https://web.archive.org/web/20151217092716/http://www.colebrookbossonsaunders.com/products/monitor-arm-stand/flo), and they free up a ton of desk space in a triple monitor configuration while also looking quite snazzy. I’m fond of putting my keyboard *just* under the center monitor, which isn’t possible with any monitor stand.


![](https://blog.codinghorror.com/content/images/2025/02/image-101.png)


With these Flo arms you can “scale up” your configuration from dual to triple or even quad (!) monitor later.


4K monitors are here, they’re not that expensive, the desktop operating systems and video hardware are in place to properly support them, and in the appropriate size (27″) we can finally have **an amazing retina display experience at typical desktop viewing distances**. Choose the Asus PB279Q 4K monitor, or whatever 4K monitor you prefer, but take the plunge.


In 2007, I asked [Where Are The High Resolution Displays](https://blog.codinghorror.com/where-are-the-high-resolution-displays/), and now, 8 years later, they’ve finally, *finally* arrived on my desktop. Praise the lord and pass the pixels!


![](https://blog.codinghorror.com/content/images/2015/08/common-hd-resolutions-compared-8k.png)


Oh, and gird your loins for 8K one day. It, too, [is coming](https://www.youtube.com/watch?v=sLprVF6d7Ug).

[4k displays](https://blog.codinghorror.com/tag/4k-displays/)
[high dpi](https://blog.codinghorror.com/tag/high-dpi/)
[windows 10](https://blog.codinghorror.com/tag/windows-10/)
[monitor technology](https://blog.codinghorror.com/tag/monitor-technology/)
[video cards](https://blog.codinghorror.com/tag/video-cards/)
