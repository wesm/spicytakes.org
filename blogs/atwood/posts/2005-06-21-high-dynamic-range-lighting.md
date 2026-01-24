---
title: "High Dynamic Range Lighting"
date: 2005-06-21
url: https://blog.codinghorror.com/high-dynamic-range-lighting/
slug: high-dynamic-range-lighting
word_count: 616
---

At the [nVidia 7800 launch event](https://web.archive.org/web/20050626023909/http://blogs.pcworld.com/staffblog/archives/000743.html) today, one of the video rendering technology highlights was high dynamic range lighting. Almost all video cards in use today are limited to 32 bit color values – that’s 8 bits for red, green, and blue, with the “rounded” 8 bits typically thrown away.* 24 bits is enough to represent most of the colors the human eye can see. But **those 8 bits per color also represent intensity**. That means the brightest white is 255, 255, 255 – only 256 times brighter than the blackest black. This vastly underrepresents both the dynamic range of light in the real world (1012 to 1) and the dynamic range of the human eyeball (1000 to 1).


That’s why HDR lighting uses 64-bit values to represent color, which offers both 16 bits of color precision and 16 bits of brightness. As the chief scientist at nVidia points out in a recent Q&A session, don’t underestimate the importance of good old black and white:


> Reader Question: What is your opinion about some of the new graphical features that are being implemented in games? Some are quite beneficial to GPU performance, such as normal-map compression and virtual displacement mapping. But others are very costly to performance, specifically high-dynamic-range lighting. After seeing the extreme over-saturation of light with HDR in Far Cry (even on the lower levels of HDR) and the performance hit it took, I personally am not convinced that HDR is a method that should be pursued any longer. What are your opinions on this subject? – cfee2000
> David Kirk: **I think that High Dynamic Range Lighting is going to be the single most significant change in the visual quality over the next couple of years. It’s almost as big as shading.**
> The reason for this is that games without HDR look flat. They should, since they are only using a range of 256:1 in brightness – a small fraction of what our eyes can see. Consequently, low-dynamic-range imagery looks flat and featureless, no highs, and no detail in the shadows, the lows. If you game using a DFP (LCD display), you probably can’t tell the difference anyway, since most LCD displays only have 5 or 6 bits of brightness resolution – an even narrower 32:1 or 64:1 range of brightness. On a CRT, you can see a lot more detail, and on the newer high-resolution displays, you can see not only the full 8 bits, but even more. There are new HDR displays that can display a full 16-bit dynamic range, and I can tell you that the difference is stunning. When these displays become more affordable in the next year or two, I don’t know how we’ll ever go back to the old way.


Here are some comparative screenshots from Far Cry, which supports HDR lighting as of the 1.3 patch:


![](https://blog.codinghorror.com/content/images/2025/05/image-106.png)


High dynamic range lighting (64-bit color)


![](https://blog.codinghorror.com/content/images/2025/05/image-107.png)


Standard lighting (32-bit color)


The effect is not always obvious, but it’s just as significant as the move from 16-bit color to 32-bit color in my opinion. It’s like going from dial-up to broadband; you don’t really know what you’ve been missing until you’ve seen it in action.


Of course, [TANSTAAFL](http://en.wikipedia.org/wiki/TANSTAAFL): increasing the data payload from 32-bit to 64-bit hurts performance. Although the GeForce 6 supported HDR lighting, the new GeForce 7 is supposedly the first generation of video card that can deliver HDR without significantly impairing performance.


*The data has to be rounded to the nearest power of two for performance. I’m not entirely sure what is done with the “extra” bits in 32-bit and 64-bit color framebuffers.

[video rendering](https://blog.codinghorror.com/tag/video-rendering/)
[high dynamic range lighting](https://blog.codinghorror.com/tag/high-dynamic-range-lighting/)
[nvidia 7800](https://blog.codinghorror.com/tag/nvidia-7800/)
[color depth](https://blog.codinghorror.com/tag/color-depth/)
[hdr lighting](https://blog.codinghorror.com/tag/hdr-lighting/)
