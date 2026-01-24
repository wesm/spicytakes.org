---
title: "Did YouTube Cut the Gordian Knot of Video Codecs?"
date: 2006-12-27
url: https://blog.codinghorror.com/did-youtube-cut-the-gordian-knot-of-video-codecs/
slug: did-youtube-cut-the-gordian-knot-of-video-codecs
word_count: 602
---

Playing video on a computer has always been a crapshoot. You must have the correct video codec installed, the same video codec that the clip was encoded with. If you don’t, the video won’t play. You’ll have to find, download, and install the proper codec first. It’s even more of a problem on the web, where users can run any combination of operating system and browser. Just take a look at all the choices in Yahoo’s web-based Media Helper:


![](https://blog.codinghorror.com/content/images/2025/05/image-458.png)


As the old saying goes, we love standards: that’s why we have [so many of them](http://en.wikipedia.org/wiki/List_of_codecs#Video_codecs). Here are a few of the more popular video codecs you’re likely to encounter out in the wild:

- Windows Media Video
- QuickTime
- MPEG-1
- MPEG-2
- MPEG-4
- x264


It doesn’t seem like such a large list, until you consider that there are **dozens of variants for each codec**. What version of QuickTime? What version of Windows Media? Which MPEG-4 implementation? And this is only a partial list of the *popular* codecs. Imagine a poor user trying to view a RealVideo clip in this day and age.


That’s why we call it [codec hell](https://web.archive.org/web/20070104221620/http://btfaq.com/serve/cache/69.html). It makes the current format war between Blu-Ray and HD-DVD look like a walk in the park.


In this hostile environment, it’s no wonder that **YouTube elected to cut the Gordian knot of video codecs: they chose Flash Video, which “just works” on most computers**. Even if Flash isn’t present on your computer, it’s an easy in-place browser download, unlike, say, a QuickTime install. It’s the same reason Google Video switched to Flash in September 2005, long before Google purchased YouTube. Tinic Uro explains:


> [The .FLV file format](http://en.wikipedia.org/wiki/FLV) uses the KISS (keep it simple stupid) approach. It offers neither the high fidelity or the flexibility of file formats like QuickTime or Windows Media. But it does what it does well: playing back simple video streams with some meta information.


The availability of a common, simple video playback format across all browsers and platforms has ushered in a new era of video sharing on the web. And that’s a very good thing.


But we’ve paid an extraordinarily heavy price for this universality: **Flash Video quality is, in a word, *hideous***. Let’s compare the Transformers Movie trailer, which is available in a variety of different video formats.


[YouTube](http://www.youtube.com/watch?v=mwyzSNk8Fu8) version:


![](https://blog.codinghorror.com/content/images/2025/05/image-459.png)


Windows Media Video streaming version:


![](https://blog.codinghorror.com/content/images/2025/05/image-460.png)


QuickTime streaming version:


![](https://blog.codinghorror.com/content/images/2025/05/image-461.png)


QuickTime 480p version:


![](https://blog.codinghorror.com/content/images/2025/05/image-462.png)


The Flash Video version of the Transformers movie trailer is a bottom of the barrel, least common denominator experience. It is painfully bad. But I’d also argue that **quality is largely irrelevant for *most* video content on the web**. Having video you can embed, play, and link everywhere – without worrying about whether the video will play back properly on someone’s computer – is far more important than quality alone. Flash Video “just works,” and it’s never more than one click away from 98% of the web browsers on the planet. It’ll never win any quality awards, but it’s still recognizable as video. Therefore it wins by default.


The codec wars are over, at least for web clips. **Flash Video is the new internet video standard.** Sometimes [worse really is better](https://blog.codinghorror.com/worse-is-better/).


That said, I do wish we hadn’t cut out ten years of video codec progress to get to this point. When watching YouTube clips, I sometimes feel like I’m watching ancient [Video for Windows](http://en.wikipedia.org/wiki/Video_for_Windows) clips circa 1993. Here’s hoping the Flash developers can incorporate more modern, higher quality codecs without re-introducing codec hell along the way.

[video codecs](https://blog.codinghorror.com/tag/video-codecs/)
[multimedia](https://blog.codinghorror.com/tag/multimedia/)
[media formats](https://blog.codinghorror.com/tag/media-formats/)
[web video](https://blog.codinghorror.com/tag/web-video/)
[codec compatibility](https://blog.codinghorror.com/tag/codec-compatibility/)
