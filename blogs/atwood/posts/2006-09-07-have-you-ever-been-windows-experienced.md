---
title: "Have You Ever Been Windows Experienced?"
date: 2006-09-07
url: https://blog.codinghorror.com/have-you-ever-been-windows-experienced/
slug: have-you-ever-been-windows-experienced
word_count: 600
---

Now that [Windows Vista Release Candidate 1](https://web.archive.org/web/20060908233751/http://download.windowsvista.com/preview/rc1/en/download.htm) is sorta-kinda available to everyone, let’s see what it takes to run it. Here's a comparison of the Vista hardware requirements with the hardware requirements of Windows XP:

kg-card-begin: html


|  | **Windows XP** (2001) | **Windows Vista** (2007) |
| CPU | 233 MHz | 800 MHz
(1 GHz recommended) |
| RAM | 64 MB
(128 MB recommended) | 512 MB
(1 GB recommended) |
| Video | Super VGA (800 x 600) display | DirectX9 video card
(128 MB video RAM recommended) |
| HDD | 1.5 GB | 15 GB |


kg-card-end: html

**Vista requires 10x the drive space, 8x the memory, and 4x the CPU power.** It also substantially raises the bar for video; most integrated video solutions are no longer acceptable. The increase in minimum spec is not unreasonable, considering it’s been *6 long years* since the last release of a mainstream desktop operating from Microsoft.


Still, Vista-capable PCs can be had on the cheap. Even a basic $449 eMachines box exceeds these requirements. Granted, you might need to spend a bit of extra money to upgrade the memory from the default 512 megabytes, but even then you could buy a cheap 512 megabyte USB key and [use it as ReadyBoost cache](https://web.archive.org/web/20061107203342/http://blogs.msdn.com/tomarcher/archive/2006/06/02/615199.aspx).


To deal with Vista’s increased system requirements, **Microsoft baked in a system benchmarking tool known as the Windows Experience Index.** At first boot, your system is profiled, and features are enabled or disabled based on your machine’s Windows Experience Index score. Here’s what my home PC scored:


![](https://blog.codinghorror.com/content/images/2025/05/image-347.png)


Unlike some of the [new Microsoft Vista features](http://en.wikipedia.org/wiki/Features_new_to_Windows_Vista), this one is remarkably well thought out. For one thing, it expresses the total score as the lowest subscore. This is an incredibly intuitive way to highlight that **your PC’s performance is only as good as the slowest subsystem**. You know immediately which part of your system will give you the most bang for the buck when upgrading.*


Clicking the **View and Print Details** button results in a great detailed system summary as well. Here’s the Windows Experience Index summary page for my [Asus W3J laptop](https://blog.codinghorror.com/asus-w3j-laptop-review/):


![](https://blog.codinghorror.com/content/images/2025/05/image-348.png)


It’s a nice, balanced set of results, exactly what I was shooting for with this laptop. I also planned to upgrade the laptop’s hard drive later in its life to boost its performance, so this confirms that choice as well. But what exactly is being measured here?


If you browse to **c:windowsperformancewinsat** and look in the datastore folder, you’ll find an XML file that describes the test results in detail. Here’s the relevant Metrics section:

kg-card-begin: html

<Metrics>

  <CPUMetrics>

    <CompressionMetric units="MB/s">43.83377</CompressionMetric>

    <EncryptionMetric units="MB/s">23.30456</EncryptionMetric>

    <Compression2Metric units="MB/s">138.22060</Compression2Metric>

    <Encryption2Metric units="MB/s">178.69444</Encryption2Metric>

    <DshowEncodeTime units="s">19.18101</DshowEncodeTime>

  </CPUMetrics>

  <MemoryMetrics>

    <Bandwidth units="MB/s">3316.58691</Bandwidth>

  </MemoryMetrics>

  <GamingMetrics>

    <AlphaFps units="F/s">49.85000</AlphaFps>

    <ALUFps units="F/s">40.82000</ALUFps>

    <TexFps units="F/s">45.64000</TexFps>

  </GamingMetrics>

  <GraphicsMetrics>

    <DWMFps units="F/s">88.73640</DWMFps>

    <VideoMemBandwidth units="MB/s">4695.65000</VideoMemBandwidth>

    <MFVideoDecodeDur units="s">2.93202</MFVideoDecodeDur>

  </GraphicsMetrics>

  <DiskMetrics>

    <AvgThroughput units="MB/s">31.75583</AvgThroughput>

  </DiskMetrics>

</Metrics>

kg-card-end: html

I can see the **Windows Experience Index base score** becoming a standard tool for bragging rights amongst OEM PC builders. And because Microsoft used a balanced set of benchmarks with a logical scoring mechanism based on the weakest link in the system, the WEI score is more meaningful than a third party synthetic benchmark: when these scores improve, *users win*.


Just kidding. My WEI is bigger than yours.


*There is one caveat here: gaming. A low-ish ~2 video card rating will be plenty for Aero and WPF apps. A higher video rating will only really matter for users that play games, so it might be unfair to reduce the entire system’s score to the video card score.

[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[hardware requirements](https://blog.codinghorror.com/tag/hardware-requirements/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
[software development.](https://blog.codinghorror.com/tag/software-development-3/)
