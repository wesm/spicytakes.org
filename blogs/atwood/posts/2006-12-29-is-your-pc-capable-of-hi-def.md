---
title: "Is your PC capable of Hi-Def?"
date: 2006-12-29
url: https://blog.codinghorror.com/is-your-pc-capable-of-hi-def/
slug: is-your-pc-capable-of-hi-def
word_count: 631
---

As I recently discovered, playback of [high definition video](https://blog.codinghorror.com/high-definition-video-on-the-pc/) is very demanding. You’ll need a beefy PC to achieve the holy grail of maximum 1080p (1920x1080) resolution playback. Here are the [minimum system requirements](https://web.archive.org/web/20070106030650/http://www.cyberlink.com/english/support/bdhd_support/system_requirement.jsp) according to Cyberlink:

- *Very* fast single core CPU (3.2+ GHz Pentium 4, 2.0+ GHz Pentium-M, 2.4+ GHz Athlon 64), or almost any dual core CPU
- NVIDIA 7600gt or better, or ATI X1600 or better
- 512mb system memory, 256mb video card memory
- for digital [HDMI output](http://en.wikipedia.org/wiki/HDMI), a certified video card with [HDCP](http://en.wikipedia.org/wiki/High-Bandwidth_Digital_Content_Protection) support and a HDMI connector


If you’re wondering how your system stacks up for high-definition video, Cyberlink offers its [BD/HD Advisor software](http://www.cyberlink.com/english/support/bdhd_support/diagnosis.jsp), which runs through the requirements checklist automatically. Here’s how [my current home theater PC](https://blog.codinghorror.com/pentium-m-home-theater-pc/) scored:


![](https://blog.codinghorror.com/content/images/2025/05/image-463.png)


Cyberlink’s tool is helpful, but it’s also a subtle sales pitch for their [PowerDVD Ultra HD playback software](https://web.archive.org/web/20070106053249/http://www.cyberlink.com/multi/products/main_112_ENU.html), which was just released a week or so ago. That’s fine by me; I already use PowerDVD to enable DVD playback through Windows Media Center. It’s the least problematic of all the DVD software I’ve tried, and believe me, I’ve tried all the major players at one point or another.


Most of the system requirements for Hi-Def are reasonable, but **the CPU requirement is off the charts, even by modern *gaming* standards**. Those insanely high CPU requirements are there for a reason. I can personally vouch for that. Although the Pentium-M chip in my home theater PC is overclocked to 1.75 GHz and has a full 2 megabytes of L2 cache, it can’t play 1920x1080 (1080p) content without massive stuttering. It’s possible the GPU could offload some of the work from the CPU, but getting GPU decode acceleration working is a crapshoot at best. Fast dual core CPUs are cheaper and certainly simpler than dealing with the hassle of offloading the decoding to the video card.


For most modern systems, all you’d have to do is...

1. Drop in a new video card, one with HDMI output and HDCP support. There are a number of these on the market now; just look for the certified models with the HDMI connector. You will pay a premium over the standard DVI and VGA models, but it’s not prohibitive. Capable HDMI+HDCP video cards can be found for under $150.
2. Add a HD-DVD or Blu-Ray drive. Internal Blu-Ray drives go for around $699 now. Unfortunately, there are no commercially available internal HD-DVD drives available at the moment, only the (amazingly cheap) external $199 Xbox 360 add-on, which [also works on the PC](https://web.archive.org/web/20070320143653/http://www.pcper.com/article.php?aid=325).
3. Purchase HD playback software, such as Cyberlink’s [PowerDVD Ultra](https://web.archive.org/web/20070106053249/http://www.cyberlink.com/multi/products/main_112_ENU.html). No high-def playback capability is built into any OS that I’m aware of.


My HTPC uses an analog VGA connection, so it neatly bypass any HDCP requirements. I don’t need to buy a new video card unless I want digital output; my old workhorse Radeon 9600 has 256 megabytes of memory and enough muscle to handle very high resolution analog video playback. But then there’s this ominous disclaimer on the Cyberlink page:


> Note: **Some Blu-ray Discs or HD DVD titles may require a digital output instead of analog.** In this case, the digital output requirements listed above must be satisfied in order to play those titles.


Scary stuff. Gotta plug [that pesky analog hole](http://en.wikipedia.org/wiki/Analog_hole) eventually, I suppose.


Most of this is moot to me, as my home theater PC is currently connected to my EDTV plasma, which is only capable of 800 x 480. It’s a perfect resolution for DVDs, but high-def, it ain’t. Still, I like to think that this system would be capable of 720p (1280x720) playback if I had a reasonably cheap HD or Blu-Ray drive to drop into the drive bay.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[system requirements](https://blog.codinghorror.com/tag/system-requirements/)
[high definition video](https://blog.codinghorror.com/tag/high-definition-video-2/)
