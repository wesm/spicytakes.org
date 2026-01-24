---
title: "The Promise and Peril of Jumbo Frames"
date: 2009-03-01
url: https://blog.codinghorror.com/the-promise-and-peril-of-jumbo-frames/
slug: the-promise-and-peril-of-jumbo-frames
word_count: 889
---

We sit at the intersection of two trends:

1. Most home networking gear, including routers, has safely **transitioned to gigabit ethernet**.
2. The generation, storage, and transmission of large high definition video files is [becoming commonplace](https://blog.codinghorror.com/easy-efficient-hi-def-video-playback/).


If that sounds like you, or someone you know, there’s one tweak you should know about that can potentially improve your local network throughput quite a bit – enabling [Jumbo Frames](http://en.wikipedia.org/wiki/Jumbo_frame).


The typical UDP packet looks something like this:


![](https://blog.codinghorror.com/content/images/2025/04/image-316.png)


But the default size of that data payload was established years ago. In the context of gigabit ethernet and the amount of data we transfer today, it does seem a bit.. anemic.


> The original 1,518-byte MTU for Ethernet was chosen because of the high error rates and low speed of communications. If a corrupted packet is sent, only 1,518 bytes must be re-sent to correct the error. However, each frame requires that the network hardware and software process it. If the frame size is increased, the same amount of data can be transferred with less effort. This reduces CPU utilization (mostly due to interrupt reduction) and increases throughput by allowing the system to concentrate on the data in the frames, instead of the frames around the data.


I use my beloved energy efficient [home theater PC](https://blog.codinghorror.com/building-your-own-home-theater-pc/) as an always-on media server, and I’m constantly transferring gigabytes of video, music, and photos to it. Let’s try enabling jumbo frames for my little network.


The first thing you’ll need to do is **update your network hardware drivers to the latest versions**. I [learned this the hard way](http://blog.stackoverflow.com/2009/02/server-speed-tests/), but if you want to play with advanced networking features like Jumbo Frames, you need the latest and greatest network hardware drivers. What was included with the OS is unlikely to cut it. Check on the network chipset manufacturer’s website.


Once you’ve got those drivers up to date, look for **the Jumbo Frames setting in the advanced properties of the network card**. Here’s what it looks like on two different ethernet chipsets:


![](https://blog.codinghorror.com/content/images/2025/04/image-315.png)


![](https://blog.codinghorror.com/content/images/2025/04/image-314.png)


That’s my computer, and the HTPC, respectively. I was a little disturbed to notice that neither driver recognizes exactly the same data payload size. It’s named “Jumbo Frame” with 2KB - 9KB settings in 1KB increments on the Realtek, and “Jumbo Packet” with 4088 or 9014 settings on the Marvell. I know that **technically, for jumbo frames to work, all the networking devices on the subnet have to agree on the data payload size**. I couldn’t tell quite *what* to do, so I set them as you see above.


(I didn’t change anything on my router / switch, which at the moment is the [D-Link DGL-4500](https://blog.codinghorror.com/gifts-for-geeks-2007-edition/); note that *most* gigabit switches support jumbo frames, but you should always verify with the manufacturer’s website to be sure.)


I then ran a few tests to see if there was any difference. I started with a simple file copy.


**Default network settings**


![](https://blog.codinghorror.com/content/images/2025/04/image-313.png)


**Jumbo Frames enabled**


![](https://blog.codinghorror.com/content/images/2025/04/image-312.png)


My file copy went from 47.6 MB/sec to 60.0 MB/sec. Not too shabby! But this is a very ad hoc sort of testing. Let’s see what the [PassMark Network Benchmark](http://www.passmark.com/products/pt_advnet.htm) has to say.


**Default network settings**


![](https://blog.codinghorror.com/content/images/2025/04/image-311.png)


**Jumbo Frames enabled**


![](https://blog.codinghorror.com/content/images/2025/04/image-310.png)


This confirms what I saw with the file copy. With jumbo frames enabled, we go from **390,638 kilobits/sec to 477,927 kilobits/sec average**. A solid 20% improvement.


Now, jumbo frames aren’t a silver bullet. **There’s a reason jumbo frames are never enabled by default**: some networking equipment can’t deal with the non-standard frame sizes. Like all deviations from default settings, it is absolutely possible to make your networking *worse* by enabling jumbo frames, so proceed with caution. This SmallNetBuilder article [outlines some of the pitfalls](http://www.smallnetbuilder.com/content/view/30201/54/1/2/):


> **1) For a large frame to be transmitted intact from end to end, every component on the path must support that frame size.**
> The switch(es), router(s), and NIC(s) from one end to the other must *all* support the same size of jumbo frame transmission for a successful jumbo frame communication session.
> **2) Switches that don’t support jumbo frames will *drop* jumbo frames.**
> In the event that both ends agree to jumbo frame transmission, there still needs to be end-to-end support for jumbo frames, meaning all the switches and routers must be jumbo frame enabled. At Layer 2, not all gigabit switches support jumbo frames. Those that do will forward the jumbo frames. Those that don’t will drop the frames.
> **3) For a jumbo packet to pass through a router, both the ingress and egress interfaces must support the larger packet size. Otherwise, the packets will be dropped or fragmented.**
> If the size of the data payload can’t be negotiated (this is known as [PMTUD](http://en.wikipedia.org/wiki/Pmtud), packet MTU discovery) due to firewalls, the data will be dropped with no warning, or “blackholed.” And if the MTU isn’t supported, the data will have to be fragmented to a supported size and retransmitted, reducing throughput.


In addition to these issues, large packets can also hurt latency for gaming and voice-over-IP applications. Bigger isn’t always better.


Still, if you regularly transfer large files, jumbo frames are definitely worth looking into. My tests showed a solid 20% gain in throughput, and for the type of activity on my little network, I can’t think of any downside.

[networking](https://blog.codinghorror.com/tag/networking/)
[ethernet](https://blog.codinghorror.com/tag/ethernet/)
[jumbo frames](https://blog.codinghorror.com/tag/jumbo-frames/)
[data transmission](https://blog.codinghorror.com/tag/data-transmission/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
