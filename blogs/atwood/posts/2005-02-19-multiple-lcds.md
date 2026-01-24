---
title: "Multiple LCDs"
date: 2005-02-19
url: https://blog.codinghorror.com/multiple-lcds/
slug: multiple-lcds
word_count: 571
---

In [multiple monitors and productivity](https://blog.codinghorror.com/multiple-monitors-and-productivity/), I proposed **three LCD panels as the standard developer desktop configuration**. The only thing holding us back was price, and the minor inconvenience of obtaining a second video card to drive the third monitor.


I recently upgraded my home system to match my work configuration. I purchased two of these [Rosewill R910 19″ panels](https://web.archive.org/web/20050225093550/http://www.newegg.com/app/ViewProductDesc.asp?description=24-021-003&depa=1), and they live up to all the positive user reviews: they’re dirt cheap and offer excellent image quality.


![](https://blog.codinghorror.com/content/images/2025/05/image-52.png)


I distinctly remember paying around $1000 for a 19″ CRT in 1998, and another $900 for a 21″ CRT in 2000. For about the same price, I can now get three times the display area, less total power consumption, and crisper image quality in 2D applications. Now that’s progress! In my opinion, **price is no longer a valid reason to choose a less-productive single monitor configuration.**


Sure, you could buy a larger single panel, such as this [1920x1200 Dell model](https://web.archive.org/web/20050220052223/http://www.extremetech.com/article2/0,1558,1764466,00.asp), priced at a reasonable $1,200. But **is that really any match for the effective 3840x1024 you’d get with three 19″ Rosewill panels for $200 less? **Buying large LCDs rarely makes sense because of the exponential increase in price as the size goes up. There’s always a price/performance sweet spot, and right now the sweet spot is unquestionably the 19″ LCD panels. Another reason to avoid extremely high resolution single displays: Windows is [trapped in a bitmapped world](https://blog.codinghorror.com/trapped-in-a-bitmapped-world/). The pitiful, wonky “Large Fonts” mode just isn’t cutting it. Until Avalon arrives, with its perfectly scalable PDF-style vector display engine, I can’t recommend suffering through traditional win32 apps on a 1920x1440 display.


Now, if you are making the leap to a third panel, some things to consider:

1. You’ll need a PCI video card, something like this [128mb 5200fx PCI card](https://web.archive.org/web/20050320071613/http://www.newegg.com/app/ViewProductDesc.asp?description=14-140-027&depa=1). I recommend nVidia because of their superior driver support for multimonitor modes. Ideally you would have nVidia cards in both your AGP and PCI slots, so you only need to load one video driver. Running multiple video drivers from different manufacturers *can* work, but can also be a total nightmare.
2. For LCDs, use DVI interfaces whenever possible. I wouldn’t even consider buying a panel that lacked a DVI interface. I have the two Rosewill displays running side by side here, one on DVI and one on analog VGA – nearly an ideal apples-to-apples comparison. The VGA connected panel certainly isn’t chopped liver, but it lacks the perfect per-pixel digital crispness I’ve come to expect from DVI connected panels. It’s not a dealbreaker, but **always choose DVI if you want the best LCD experience.** In particular, try to get dual DVI ports on your primary video card, because I have yet to see a PCI video card with dual DVI ports. This is something PCI Express will fix once it becomes more mainstream.
3. XP has mature support for multiple monitors, but it’s not as good as it could be. I would be remiss if I didn’t mention the outstanding [UltraMon utility](http://www.realtimesoft.com/ultramon/overview/). This adds all the “missing” multiple monitor functionality – it’s essential.


I’m increasingly certain that, sometime in the next few years, **two LCD panels will be a standard configuration for not just developers and power users, but a sizable percentage of mainstream Dell systems**. Why? Well, the same reason that all CPUs will eventually be multi-core – sometimes there’s [nowhere to go but sideways](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/).

[monitor](https://blog.codinghorror.com/tag/monitor/)
[productivity](https://blog.codinghorror.com/tag/productivity/)
[multiple monitors](https://blog.codinghorror.com/tag/multiple-monitors/)
[display setup](https://blog.codinghorror.com/tag/display-setup/)
[lcd panels](https://blog.codinghorror.com/tag/lcd-panels/)
