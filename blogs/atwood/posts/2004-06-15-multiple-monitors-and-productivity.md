---
title: "Multiple Monitors and Productivity"
date: 2004-06-15
url: https://blog.codinghorror.com/multiple-monitors-and-productivity/
slug: multiple-monitors-and-productivity
word_count: 598
---

I found an interesting blog post about a small, informal [multiple monitor productivity study](https://web.archive.org/web/20040611180359/http://dotnetjunkies.com/WebLog/darrell.norton/archive/2003/11/11/3432.aspx). A number of developers, with some nudging from me, have gravitated to multiple monitor setups over the last year. Based on that experience, I wholeheartedly agree with the study survey results:

- On average, people would much rather have 2 smaller monitors than 1 larger monitor. Nobody answered that they preferred 1 monitor over 2 even a little bit.
- Multiple monitors were most useful when the application had palettes or when 2 or 3 windows needed to be open, such as for programming/debugging.
- The biggest complaint was desk space, since all of our monitors were CRTs (no LCDs).


![](https://blog.codinghorror.com/content/images/2025/06/image-58.png)


**This is really a no-brainer for any developer who values his or her time.** Now more than ever, since:

1. Most mainstream, inexpensive video cards tend to come with two VGA ports (aka “dual head”) standard.
2. The price of less bulky 17″ and 19″ LCDs are quite reasonable.
3. Windows XP has mature multiple monitor support; it’s been a standard out of box win32 feature since Windows 98.


Two monitors is pretty much plug and play with a modern “dual head” video card, but going to **three monitors **is less common – and more work.


I recently went from two to three panels, and I think the transition is worth the effort. All the “extra stuff” I couldn’t fit on the primary or secondary panels finally found a home on the third one. The increase isn’t as noticeable as going from a single monitor was, though. I think the rule of diminishing returns will definitely kick in for more than three. I’m also wondering whether I could physically see four monitors without moving my head around a bunch more than I normally do.


If you’re interested in moving to three displays, you’ll need a second PCI video card installed in addition to your primary AGP video card. Although this generally works, don’t assume it will. Having two different video drivers installed (from two different vendors, on two different hardware busses) can be problematic.


I recommend visiting the excellent [Multiple Monitor Resources](http://www.realtimesoft.com/multimon/faq.asp) website – they pioneered this topic way back in, er, 1999 – and checking their [compatibility database](http://www.realtimesoft.com/multimon/db.asp). I had a dual-output nVidia 5200 video card, so I opted to stick with the same chipset by installing a PCI nVidia 5200 video card. That way, I only had to install one video driver, and I get the benefit of configuring all three panels using the same display properties applet.


[ATI](http://www.ati.com/support/driver.html) and [nVidia](http://www.nvidia.com/content/drivers/drivers.asp) both have good support for multiple monitors in the default drivers, though nVidia’s support is significantly better at this point. So if you’re on the fence, or don’t have a preference, I’d go with a nVidia video chipset where possible. If you get serious about multiple monitors, you’ll also want a copy of [RealTimeSoft’s UltraMon utility](http://www.realtimesoft.com/ultramon/overview/), which has a bunch of legitimately helpful multiple monitor features, and one *absolutely killer* feature:


> *UltraMon adds an additional taskbar for each secondary monitor, and each taskbar only shows tasks from the monitor it is on. This makes managing lots of open applications much easier, and when activating an application, you’ll know on which monitor it will appear.*


I had no idea how significant this feature was until I tried it. It’s huge! The taskbar becomes far more useful when it isn’t crowded by the dozens of windows you’re bound to have open, and each taskbar only shows the windows on that particular display. Strongly recommended.

[productivity](https://blog.codinghorror.com/tag/productivity/)
[multiple monitors](https://blog.codinghorror.com/tag/multiple-monitors/)
[developer](https://blog.codinghorror.com/tag/developer/)
[programming](https://blog.codinghorror.com/tag/programming/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
