---
title: "High-Definition Video on the PC"
date: 2006-12-15
url: https://blog.codinghorror.com/high-definition-video-on-the-pc/
slug: high-definition-video-on-the-pc
word_count: 886
---

Now that HD-DVD and Blu-Ray are starting to enter the market in earnest, I thought I’d revisit HD video playback on the PC. I’m seriously considering buying one of the $199 [Xbox 360 HD-DVD kits](https://web.archive.org/web/20070320143653/http://www.pcper.com/article.php?aid=325) and retrofitting it into [my Home Theater PC](http://www.hackaday.com/2006/11/13/xbox-hd-dvd-rom-on-mac-and-pc/).


I’ll start by comparing three clips from the Microsoft [Windows Media High Definition Showcase](https://web.archive.org/web/20061217104146/http://www.microsoft.com/windows/windowsmedia/musicandvideo/hdvideo/contentshowcase.aspx) page. It’s a tad out of date now – most of these sample high-definition clips were mastered in late 2003 or early 2004, long before HD-DVD or Blu-Ray. But the bitrates and sizes are still representative.


Most of the clips had similar performance characteristics, so I chose one clip from each category.

kg-card-begin: html


|  | [T2 Promo](https://web.archive.org/web/20080319085418/http://download.microsoft.com/download/1/5/0/15092c6c-5af1-4208-b5e2-54af6f1009a4/T2_720.exe)
**720p** | [T2 Promo](https://web.archive.org/web/20080319085341/http://download.microsoft.com/download/1/5/0/15092c6c-5af1-4208-b5e2-54af6f1009a4/T2_1080.exe)
**1080p** | [Step Into Liquid Promo](https://web.archive.org/web/20080319085724/http://download.microsoft.com/download/e/a/d/eadb9b42-728b-42b0-bfdf-b472fa2a2464/Step_into_Liquid_1080.exe)
**1080p** |
| Resolution | 1280 x 720 | 1440 x 1080 | 1440 x 1080 |
| Bitrate | 6.93 Mbps | 8.44 Mbps | 8.44 Mbps |
| Audio Codec | WMA 9 Pro
5.1 channel
384 Kbps | WMA 9 Pro
5.1 channel
384 Kbps | WMA 9 Pro
2 channel
384 Kbps |
| Video Codec | WMA 9 Pro | WMA 9 Pro | WMA 9 Pro |


kg-card-end: html

Note that I included the [Step Into Liquid](http://www.amazon.com/exec/obidos/ASIN/B0001FGBUC/) promo because it’s the *only* clip on the WMV HD Showcase page that requires an abnormally large amount of CPU power to decode. I’m still not sure exactly why. The resolution is the same, and the bitrate looks comparable. You’ll also note that Microsoft has an odd definition of 1080p. The official television resolutions break down as follows:

kg-card-begin: html


|  |  |  | Pixels per frame |
| **480i** | 704 x 480 | interlaced | 168,960 |
| **480p** | 704 x 480 | progressive | 337,920 |
| ****720p**** | 1280 x 720 | progressive | 921,600 |
| **1080i** | 1920 x 1080 | interlaced | 1,036,800 |
| **1080p** | 1920 x 1080 | progressive | 2,073,600 |


kg-card-end: html

The official definition of **1080p is 1920x1080**, so I’m not sure what Microsoft was thinking there. Interlaced means resolution is effectively halved vertically in time; frames alternate between odd and even lines each cycle.


![](https://blog.codinghorror.com/content/images/2025/05/image-447.png)


[Interlaced video modes](http://en.wikipedia.org/wiki/Interlace) are generally considered inferior to progressive video modes, and should only be used if you have no way to enable progressive modes. Interlacing has a lot of problems and should be avoided whenever possible.


I compared CPU usage in Task Manager during full-screen playback of each clip in Windows Media Player 11 on a few systems I have around the house. Note that [DirectX Video Acceleration](http://en.wikipedia.org/wiki/DXVA) was enabled in each case.

kg-card-begin: html


|  | **Pentium-M 1.75 GHz** | **Athlon 64 1.8 GHz** | **Core Duo 2.0 GHz** |
| T2 Promo
720p | 75% CPU, perfect | 50% CPU, perfect | 25% CPU, perfect |
| T2 Promo
1080p | 85% CPU, perfect | 75% CPU, perfect | 33% CPU, perfect |
| Step Into Liquid Promo
1080p | 100% CPU, unwatchably choppy | 95% CPU, very choppy | 40% CPU, perfect |


kg-card-end: html

I have a sneaking suspicion the reason Microsoft redefined “1080p” as 1440x1080 had to do with performance. I doubt any PC system could play a true 1080p clip at the time these clips were mastered. **It clearly requires a lot of CPU horse power to render high definition video.** Driving 1920x1080 requires a lot of grunt – both in terms of pixel-pushing video bandwidth, and also in terms of CPU power for the advanced encoding used to keep the file size down on these massive resolutions. Dual core does this especially well, although it appears to do so by brute force load sharing rather than any special multiprocessor optimizations in the decoder. **The mainstream PC is only now catching up to the performance required to watch high definition video**.


All the video samples I cited are in Windows Media format. Windows Media, by all accounts, offers a [very good next generation encoder](https://web.archive.org/web/20061219014555/http://www.drunkenblog.com/drunkenblog-archives/000312.html), but it isn’t the only encoder on the block. Both [Blu-Ray and HD-DVD](http://www.engadget.com/2005/09/19/blu-ray-vs-hd-dvd-state-of-the-s-union-s-division/) allow three different encoders:

- [H.264 / MPEG-4 AVC](http://en.wikipedia.org/wiki/H.264)
- [Microsoft Video Codec 1](http://en.wikipedia.org/wiki/VC-1) (aka VC1, WMV HD)
- [MPEG-2](http://en.wikipedia.org/wiki/MPEG-2)


Woe to the poor consumer who buys [a HD-DVD or Blu-Ray disc](http://www.highdefdigest.com/feature_blurayvshddvd_roundtwo.html) encoded with the ancient MPEG-2 encoder. It’ll look awful and take up a lot more room than it should. H.264 and MVC-1, however, are truly next generation encoders. They look better in less space, but they also require a* lot* more CPU power to decode. At least we have a few legitimate uses left for the ridiculous amounts of CPU power we’ve inherited over the years.


If you own a relatively new video card, **it is possible to offload some of the video decoding chores from your CPU to your video card’s GPU**. But the configuration, drivers, and software necessary to achieve this acceleration is daunting. Anandtech found that, when properly configured, the latest video cards can significantly reduce the H.264 decoding burden on the CPU; [ATI reduced it by half](http://www.anandtech.com/video/showdoc.aspx?i=2645&p=2), and [Nvidia reduced it by a fifth](http://www.anandtech.com/video/showdoc.aspx?i=2798&p=3). But good luck getting everything set up in Windows XP. Here’s hoping Windows Vista and DirectX Video Acceleration 2.0 enables hardware accelerated video decoding out of the box.

[video playback](https://blog.codinghorror.com/tag/video-playback/)
[hd-dvd](https://blog.codinghorror.com/tag/hd-dvd/)
[blu-ray](https://blog.codinghorror.com/tag/blu-ray/)
[high-definition](https://blog.codinghorror.com/tag/high-definition/)
[pc](https://blog.codinghorror.com/tag/pc/)
