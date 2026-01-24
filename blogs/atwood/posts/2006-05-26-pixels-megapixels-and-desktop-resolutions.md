---
title: "Pixels, Megapixels, and Desktop Resolutions"
date: 2006-05-26
url: https://blog.codinghorror.com/pixels-megapixels-and-desktop-resolutions/
slug: pixels-megapixels-and-desktop-resolutions
word_count: 336
---

I’ve always wondered why digital cameras express their resolutions in terms of **megapixels**, rather than the typical pixel height and width numbers you find on computer displays. Nobody buys a 21" LCD with 1.9 megapixels of resolution; they buy a 21" LCD that can display 1600 x 1200. But they’re technically the same thing: 1600 x 1200 is 1,920,000 pixels, or 1.9 megapixels. It looks like we’re using the old hard drive manufacturer’s trick of [dividing by powers of ten](https://web.archive.org/web/20060614163453/http://blogs.msdn.com/oldnewthing/archive/2003/09/19/55024.aspx).


One problem with using the megapixel designation alone is that you have no idea what the aspect ratio of those pixels are – 16:9? 5:4? 1.33:1? Who knows, maybe that 1.9 megapixel camera is really taking 192 x 10,000 pictures. Pixels are pixels, right?


The Wikipedia entry on [computer display resolutions](http://en.wikipedia.org/wiki/Computer_display_standard) has a great [chart](http://en.wikipedia.org/wiki/Image:Vector_Video_Standards.png) that contrasts the most common monitor resolutions, along with the ratio line that each falls on:


![](https://blog.codinghorror.com/content/images/2025/05/image-295.png)


It’s interesting to note that **the most common monitor resolutions (800x600, 1024x768, etc.) are 4:3**. I didn’t realize how oddball the 1280x1024 ratio was. The widescreen variants are really catching on quickly, too, if the [current LCD monitor selection](https://web.archive.org/web/20060614072148/http://www.newegg.com/ProductSort/SubCategory.asp?SubCategory=20) at Newegg is any indication.


But the [alphabet soup of display designations](https://blog.codinghorror.com/dont-acronymize-your-users/) isn’t doing anyone a favor, either. I’d much rather know that a display is capable of 1600 x 1200 instead of the cryptic designation [UXGA](http://en.wikipedia.org/wiki/UXGA).


You can compare the different resolutions of most common electronic devices (cameras, screens, video, etc.) and many common formats using this nifty [dynamic megapixel overview tool](http://web.forret.com/tools/megapixel_chart.asp). Some of the camera models listed tend to have 4:3 aspect ratios, like PC displays. But not all. The 3:2 ratio is also common. Here are a few samples:

- Canon Powershot Pro 1
3264 x 2448 (8 megapixels, 4:3)
- Canon EOS 5D
4368 x 2912 (12.7 megapixels, 3:2)
- Nikon D70s
3006 x 2000 (6 megapixels, 3:2)


Evidently the 3:2 ratio derives from the native [dimensions of classic 35mm film](https://web.archive.org/web/20060529074012/http://fotogenetic.dearingfilm.com/golden_rectangle.html).

[display resolutions](https://blog.codinghorror.com/tag/display-resolutions/)
[megapixels](https://blog.codinghorror.com/tag/megapixels/)
[pixel aspect ratio](https://blog.codinghorror.com/tag/pixel-aspect-ratio/)
[digital cameras](https://blog.codinghorror.com/tag/digital-cameras/)
[monitor resolutions](https://blog.codinghorror.com/tag/monitor-resolutions/)
