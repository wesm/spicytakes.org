---
title: "Fonts don't have to look awful on Windows"
date: 2024-02-29
url: https://world.hey.com/dhh/fonts-don-t-have-to-look-awful-on-windows-564c9d2f
slug: fonts-don-t-have-to-look-awful-on-windows-564c9d2f
word_count: 961
---

I always thought it was a software problem — or at least a difference of aesthetics expressed in software. But it turns out  the reason many Mac owners, including yours truly, so strongly dislike how fonts typically look on Windows is actually a hardware problem!
See, every Mac with a screen has since 2018 shipped with
[a retina-class display](https://en.wikipedia.org/wiki/Retina_display)
. That means a pixel-per-inch count in excess of 218. High enough that you can't see the individual pixels with the naked eye. With a high-resolution display like that, you can run it at 2x or 200%. So a 27" 5K Apple Studio Display (218 PPI) that runs natively at 5120x2880 can run at 2x  and give you the equivalent of a 2560x1440 workspace, but with much nicer rendering. And that's the magic. That 2x/200%. That's why fonts on the Mac look so good out of the box.
If you connect your Windows machine to a screen of similar caliber, you get similar font rendering. I'm typing this on a 32" 6K monitor running at 200% in Windows 11 using
[iA Writer](https://ia.net/writer)
, and it looks amazing. Just as amazing as it does when I write essays in iA Writer on the Mac using the same screen. They're identical!
I did not know this!!
To make matters worse, I just spent last week using a PC on a 27" 4K monitor (163 PPI) where I accidentally committed the other common cardinal sin that make fonts look like shit on any system: Fractional scaling. I had the screen set to 150%. No wonder it looked offensively bad compared to the Mac! You can't split a pixel, so the system has to do all sorts of typographically nasty tricks when doing non-integer scaling, and the end result is awful font rendering.
But none of this is actually Windows' fault, per se. It's all about the hardware. Apple has the power to enforce retina-class displays across its entire lineup, so as a result everyone who looks at a Mac sees beautifully rendered fonts. Windows, on the other hand, runs on everything from rinky-dingy $200 laptops with super low-resolution screens and up to the best computers money can buy. You're quite likely to see a PC with awful fonts because it just doesn't have the hardware to do better.
Although part of the problem is also that many PCs are just optimized for different things than buttery-smooth font rendering. Like playing games. That 27" 4K display I was using last week had an awesome 240hz refresh rate and it was OLED. So colors were super vibrant, and it was excellent for maxing out the frames-per-seconds needed for competitive gaming. Just ace for that, just ugh for reading, writing, and programming.
So it's a trade-off. This lovely 6K Pro Display is great for text, great for photography, great for video, but not so great for gaming, since it tops out at 60hz/60fps. And it's totally fair to prioritize one thing over the other. Apple has famously never prioritized games over anything, and it shows. But they
*have*
prioritized beautiful font rendering, and that shows too.
I just wish I knew about all this before dismissing Windows out of hand as a suitable alternative to macOS on account of font rendering for years. Not that this is somehow secret information, but it doesn't seem widely distributed. As I've been tweeting about comparing Windows and macOS, I've gotten a ton of replies that were essentially "yeah, Windows sucks at fonts". And that's just wrong.
If you want to dive even deeper into the technical specifics of why fractional scaling wrecks font rendering, checkout
[Tonsky's excellent treatise](https://tonsky.me/blog/monitors/)
. He also covers the general problem with low-density displays, and what happens to the fonts when you render them on those.
But the simple conclusion here is that if you want great looking text on Windows, you need to run a high-density display. Nothing crazy. You don't need 8K (unless maybe you're trying to swing a 40" monitor), but you do need retina-style PPI counts.
Apple has set some good rules of thumb here with their 3 desktop displays. The 24" runs 4.5K, the 27" runs 5K, and the 32" runs 6K. That's all right on the money of that 218 PPI retina target. Their 14" MacBook Pro even runs a native resolution of 3024x1964, giving it a very impressive 254 PPI. That's the bar, if you want similar looks.
One final note on beautiful fonts and Windows is worth making, though. And that's the fact that the default system font is the atrocious Segoe UI. Now that's surely a difference of aesthetics, not hardware or software limitations, but I absolutely hate this tinny, thin font. And unless you change the font you're using in apps, that's what you'll see. Ugh!
But Microsoft thankfully has a brand new font that's actually rather nice on the horizon for the new default. It's called
[Aptos](https://microsoft.design/articles/a-change-of-typeface-microsoft-s-new-default-font-has-arrived)
, and they've just rolled it out as the
[new default for Office](https://www.nytimes.com/2024/02/28/technology/microsoft-word-font-aptos.html)
where it replaces Calibri (a font I don't care for at all either!). So fingers crossed that they'll make this font the default on Windows itself soon enough. I think it would go a long way to make the system more appealing to switchers from the Mac. I've already
[downloaded it](https://www.softpedia.com/get/Office-tools/Aptos-Font.shtml)
and made it my default font in Chrome. It's very nice. Not trying to ape Apple, but distinctive Windows, in a good way.
With the font rendering issue identified and fixed, my bigger problem is now that the only thing really holding me back from switching to Windows full-time is my beloved text editor, TextMate. Yep, the pressure is on for finding
[The Last Editor](https://world.hey.com/dhh/finding-the-last-editor-dae701cc)
, and finally liberating any sentimentality about leaving macOS. Exciting!
