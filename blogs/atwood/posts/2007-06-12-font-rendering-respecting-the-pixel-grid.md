---
title: "Font Rendering: Respecting The Pixel Grid"
date: 2007-06-12
url: https://blog.codinghorror.com/font-rendering-respecting-the-pixel-grid/
slug: font-rendering-respecting-the-pixel-grid
word_count: 673
---

I’ve finally determined [What’s Wrong With Apple’s Font Rendering](https://blog.codinghorror.com/whats-wrong-with-apples-font-rendering/). As it turns out, there actually *wasn’t* anything wrong with Apple’s font rendering, per se. Apple simply chose a different font rendering philosophy, [as Joel Spolsky explains](http://www.joelonsoftware.com/items/2007/06/12.html):


> **Apple** generally believes that the goal of the algorithm should be to preserve the design of the typeface as much as possible, even at the cost of a little bit of blurriness.
> **Microsoft** generally believes that the shape of each letter should be hammered into pixel boundaries to prevent blur and improve readability, even at the cost of not being true to the typeface.


So we answer the question with another question. **What do you respect more: the pixel grid, or the font designer?** It’s not surprising that Apple would side with the font designer, because [Steve Jobs thinks Microsoft has no taste](https://blog.codinghorror.com/there-are-no-design-leaders-in-the-pc-world/). But me, I’m a pragmatist. Given the ubiquity of relatively low DPI displays, [I’m with Dave Shea](https://web.archive.org/web/20070614162218/http://mezzoblue.com/archives/2007/06/12/a_subpixel_s/). I side with the pixel grid.


> Joel talks about the pixel grid, and how Microsoft’s type rendering pays more attention to it. Speaking as someone who [thinks a lot](https://web.archive.org/web/20070614162218/http://www.mezzoblue.com/icons/chalkwork/) about [the pixel grid](https://web.archive.org/web/20070614162218/http://mezzoblue.com/archives/2007/02/21/icon_design/), I have to say I think I’m coming around to the idea that Microsoft’s ClearType simply works better.
> Alright, I’d better qualify that quickly. Think about it this way – as a designer, you don’t just set type in Photoshop and let it go, right? You tweak. You kern. You attempt to [match the letters to the pixel grid](https://web.archive.org/web/20070614162218/http://www.mezzoblue.com/archives/2004/01/18/type_the_ex/) as closely as possible to reduce the blurriness. Sometimes spacing suffers, and you have to choose between a slightly blurry letter with perfect spacing, or a more precise fit within the pixel grid with just slightly off spacing. I can’t be the only one that leans toward the latter most times.
> And that’s the difference here. ClearType is a closer match to what I do manually already. Yes, I prefer the way type on OS X looks; ClearType seems too sharp and overly blocky, the subtleties of the curves are lost and it’s overly chunky. But, for the medium in which it’s being rendered, it seems like a more ideal solution.


Dave’s opinion carries a lot of weight here, not just because he’s [a well-known designer](https://web.archive.org/web/20070613110616/http://mezzoblue.com/), but because the three citations he provides demonstrate just how common it is for designers to do exactly the kind of manual, per-pixel tweaks that ClearType does for us automatically. And it’s not just an aesthetic choice, either – there’s plenty of hard data to support the assertion that snapping fonts to the pixel grid improves reading accuracy.


A fascinating greyscale-only variant of this rendering technique, [FontFocus](http://web.archive.org/web/20070706034446/http://artofcode.com/fontfocus/), illustrates beautifully how subtle tweaks can “snap” fonts to the pixel grid for better readability:


![imagination, 9ppem Helvetica, FontFocus on](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d971d970b-pi.png)


![imagination, 9ppem Helvetica, FontFocus off](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d972f970b-pi.png)


Typography, if you haven’t figured this out by now, is really complicated. It’s one of the few areas of “computer science” that actually [justifies the title](http://www.microsoft.com/typography/ctfonts/WordRecognition.aspx). I highly recommend reading [the entire FontFocus article](http://web.archive.org/web/20070706034446/http://artofcode.com/fontfocus/), as it's very instructive.


Dave Shea thinks **the pixel grid will be moot once high resolution displays become ubiquitous**. I wholeheartedly agree, although I’m unsure when exactly that will be. The history of display resolution increases have been quite modest so far. Ten years ago I was using a single 17" 1024x768 display; now I’m using three 20" 1600x1200 displays. So you’ll forgive me if I’m not overly optimistic about this theoretical jump from 100 DPI to 200 DPI.


I don’t understand why Apple is asking us to sacrifice the present at the altar of the future. **Can’t we have hinting at low resolutions, and accuracy at high resolutions, too?** Snapping fonts to a pixel grid may very well be irrelevant when everyone is luxuriating in the glow of their 200 DPI monitors. Until that glorious day arrives, respecting the pixel grid certainly makes text a lot more readable for those of us stuck in the here and now.

[font rendering](https://blog.codinghorror.com/tag/font-rendering/)
[fonts](https://blog.codinghorror.com/tag/fonts/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[typography](https://blog.codinghorror.com/tag/typography/)
