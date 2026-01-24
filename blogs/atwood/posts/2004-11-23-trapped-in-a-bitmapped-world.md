---
title: "Trapped in a Bitmapped World"
date: 2004-11-23
url: https://blog.codinghorror.com/trapped-in-a-bitmapped-world/
slug: trapped-in-a-bitmapped-world
word_count: 504
---

In a [recent blog entry](https://web.archive.org/web/20060901223329/http://www.docuverse.com/blog/donpark/EntryViewPage.aspx?guid=8a1b1e48-8693-4250-8bc2-c140af06d185), Don Park waxed poetic about 1600x1480 15″ LCDs. That’s more of a microfiche reader than an actual screen. High DPI displays, though, aren’t the root of the problem. As Scoble points out, [the real issue is Windows](https://web.archive.org/web/20041124054610/http://radio.weblogs.com/0001011/2004/11/21.html#a8703) itself:


> *Turns out his screen was set to a non-native resolution. This is a common thing I see on LCD screens. Most LCD owners don’t realize that there is only one resolution that their screen should be set to. Unfortunately Windows doesn’t tell you what that resolution is and the tools to let you control your resolution are confusing at best.
> Why is this bad? Well, for one, if you don’t run an LCD screen at the “right” resolution then the ClearType font sharpening technology won’t work (it’ll actually be even worse on a screen that isn’t set to the right resolution).
> So, I asked Dave [Winer] if I could set his screen to the proper resolution. “Sure.”
> After I did, I showed him the screen and he promptly said “I can’t read that, it’s too small.”
> “How old are you?” he asked.
> “Almost 40.”
> “In another 10 years you won’t be able to read that screen either.”
> Unfortunately I didn’t have the right setting for making everything on the screen appear bigger while retaining the sharpness of a well-set screen... **the settings that are built into Windows XP today really are inadequate to deal with high resolution screens.** Even now, some things on my page are way too big and others are way too small.*


The sad truth is that Windows is hard coded to specific pixel sizes. It doesn’t scale because bitmaps don’t scale. Oh sure, you can *pretend* that it scales by flipping on Large Fonts, or modifying the DPI setting in control panel, but these are just hacky workarounds with major side effects. Windows is a bitmapped UI. If you run Windows, like it or not, **you live in a bitmapped world**.


Nothing short of a full-blown UI redesign – something far more radical than the change from Windows 3.1 to Windows 95 – will fix this problem. That’s exactly what the Avalon technology is supposed to do. And thank God Microsoft decided to [port Avalon to XP](https://web.archive.org/web/20041204092626/http://www.sellsbrothers.com/news/showTopic.aspx?ixTopic=1504) and reach a much larger audience with the blessing of backwards compatibility. I seriously doubt we’d ever get to use Avalon if it was tied to a new OS release.


Now, I’m sure this will come as no surprise to Flash developers, who have had vector primitives for nearly ten years. Steve Jobs’ ill-fated [NeXTstep OS](http://en.wikipedia.org/wiki/NeXTSTEP) used Display PostScript to drive its windowing engine – and that was fifteen years ago. Interestingly, the current Mac OS X inherits this choice. **Why is it taking Windows so long to catch up?** It sucks to be trapped in a bitmapped world when vectors are more powerful, more flexible, more elegant: just plain better. Bring on the Avalon!

[display technology](https://blog.codinghorror.com/tag/display-technology/)
[screen resolution](https://blog.codinghorror.com/tag/screen-resolution/)
[dpi](https://blog.codinghorror.com/tag/dpi/)
[lcd screens](https://blog.codinghorror.com/tag/lcd-screens/)
