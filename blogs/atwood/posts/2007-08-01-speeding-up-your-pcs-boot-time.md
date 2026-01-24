---
title: "Speeding Up Your PC’s Boot Time"
date: 2007-08-01
url: https://blog.codinghorror.com/speeding-up-your-pcs-boot-time/
slug: speeding-up-your-pcs-boot-time
word_count: 1193
---

I frequently hear apocryphal stories about Macs booting much faster than Windows boxes. There’s a great set of [Mac boot time benchmarks](https://web.archive.org/web/20071002174454/http://www.silvermac.com/2006/macmini-core-duo-start-up-time/) on the Silver Mac site that provide solid empirical data to back up those claims:

kg-card-begin: html


|  | Intel iMac | G5 iMac | G5 iMac | Mac Mini |
|  | 10.4.4 | 10.4.4 | 10.4.5 | 10.4.5 |
| Mac sound | 4.5 | 3.5 | 3.6 | 4.0 |
| Apple logo | 6.7 | 15.6 | 15.2 | 10.2 |
| Mac OS X | 31.9 | 34.4 | 34.9 | 22.8 |
| Ready to use | 37.9 | 40.8 | 41.6 | **25.8** |


kg-card-end: html

To be clear, **the standard convention for “boot time” is the time from initial power on to the time we can finally interact with the desktop**. The Silver Mac benchmarks are admirably thorough, as they break out important milestones during boot: the first boot sound, the appearance of the Apple logo on the screen, the OS X loading screen, and finally the ability to interact with the desktop. The intermediate milestones help us see where the real bottlenecks are in the boot process.


For perspective, a 1986 Mac Plus boots to the desktop in *eleven seconds*. The modern PC it is compared to clocks in at just over a minute of boot time. It’s not even remotely a fair comparison for a whole host of reasons, but it’s a fun data point nonetheless. How long does it take for your car to boot? Your MP3 player? Your television? Your cell phone?


For typical PC boot times, I turn to [Ed Bott’s excellent blog](https://web.archive.org/web/20070913074428/http://blogs.zdnet.com/Bott/?p=240).

kg-card-begin: html


|  | 2006 vintage
PC Desktop | 2005 vintage
PC Laptop | 2004 vintage
PC Desktop |
| Windows XP | 1:01 | 1:47 | 0:58 |
| Windows Vista | 1:12 | 1:20 | 1:14 |
| Ubuntu Linux 6.10 |  |  | 1:49 |


kg-card-end: html

Wow, **PC boot times really do suck**, right? Well, maybe. It depends on the PC.


The [“Ultimate Developer Rig”](http://www.hanselman.com/blog/GoneQuadDay0WithTheUltimateDeveloperPC.aspx) I built for Scott Hanselman **boots to a clean install of Vista x64 in 22 seconds**. According to Scott, 10 seconds of that is attributable to the BIOS, and the other 12 is the operating system loading from disk. It’s sobering to consider that almost *half* of the system’s total boot time is spent in the third-party motherboard BIOS – something Microsoft has no control over.


Now, these kinds of speedy PC boot times are only attainable if you have a clean install of the operating system. A clean install is *de rigueur* for Apple, because they’re a single-source vendor. They have the luxury of complete control over the way their operating system is shipped – not to mention the system BIOS itself. Every Apple box should boot consistently quickly as a matter of course. It’d be a crushing disappointment if they didn’t.


On a Windows box, however, you almost never get a clean install. You typically get Microsoft’s operating system plus **a bevy of **[**performance-sapping craplets**](https://blog.codinghorror.com/stop-having-trouble/)** the third-party vendor was paid to install on your system**. Your boot times are already compromised the second you break the seal on the box.


Tweaking the BIOS to improve boot time is usually out of the question. But it is possible to restore most Windows boxes to near-clean-install boot speeds, at least. The process isn’t exactly rocket surgery – just **stop doing so much stuff at startup!** The primary tool for turning off unnecessary startup tasks is conveniently built into both XP and Vista: [MSCONFIG](http://www.netsquirrel.com/msconfig/msconfig_xp.html).


![msconfig utility screenshot](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b0120a86d8f97970b-pi.png)


In my experience, anything that *wants* to runs at boot almost never *needs* to. **It’s generally safe to turn off almost everything in the MSCONFIG startup tab.** If you have any applets that you recognize and want to run on boot, leave those; for everything else, when in doubt, turn it off. This not only speeds up your boot time, it also frees up memory on the PC. If you later decide you made a mistake, reverting is easy enough – just run MSCONFIG again and tick the appropriate checkbox.


It’s also quite common for your boot time to degrade over time as you install certain kinds of software, as [noted by Adrian Kingsley-Hughes](https://web.archive.org/web/20070913075105/http://blogs.zdnet.com/hardware/?p=359):


> Sudden changes in boot times are usually quite noticeable, but what usually happens in that boot times grow slowly over time. You start off with a PC with a fresh install of Windows on it and it feels nice and fast (hopefully – if it doesn’t then you’re in serious trouble and things are only going to get worse, no matter how much you trash your system trying to speed it up). You then install security software and performance takes a hit. Install some big apps like Office and boot times take another nose-dive. I’ve seen boot times increase by over 100% over the course of setting up a new PC. It’s actually quite depressing to watch.


Indeed, and **the vast majority of that boot slowdown is attributable to security and anti-virus software**, [as documented on PC Spy](https://web.archive.org/web/20070814122018/http://www.thepcspy.com/articles/other/what_really_slows_windows_down/5/). That’s why I urge people to pursue other methods of [securing their PCs](https://blog.codinghorror.com/choosing-anti-anti-virus-software/); if you rely on commercial anti-virus, you are literally *crippling* your PC’s performance. [Anti-virus software barely works](http://chuvakin.blogspot.com/2007/04/answer-to-my-antivirus-mystery-question.html) these days anyway, so it’s a raw deal no matter how you slice it.


Of course, the best boot time of all is *no* boot time – as Adrian so aptly points out:


> How many times a day do you boot up your PC? **If you [boot] more than two or three times a day on a regular basis then you’re not making proper use of the features that your PC offers, such as hibernate or sleep.** My systems can go for days, and sometimes weeks, without a reboot, being hibernated/put to sleep at the end of the day or during any big breaks in the work day. In fact, I like the hibernate feature a lot because it lets me shut my systems down yet leave my work open. Next time I restart the system, all my apps and documents are open and waiting for me.
> Even if I did need to reboot my system a few times a day, I don’t think that I’d be all that worried about boot times unless they were really long (+3 minutes) or my system was really unstable and needed rebooting several times a day. In either case, there’s a problem somewhere that needs to be solved. If the system only takes a few seconds or a couple of minutes to boot up then I’m really not worried about the effect that the lost time will have on my productivity.


He’s right. Maybe boot time is ultimately irrelevant; your best bet is to avoid booting altogether. **Make use of those “Sleep” and “Hibernation” options in lieu of powering all the way down**. Support is fairly mature for these modes, even in the wild-and-wooly PC ecosystem – and they’re many times faster than cold booting and loading up all your applications again.

[macos](https://blog.codinghorror.com/tag/macos/)
[boot time](https://blog.codinghorror.com/tag/boot-time/)
[benchmarks](https://blog.codinghorror.com/tag/benchmarks/)
[performance](https://blog.codinghorror.com/tag/performance/)
[mac](https://blog.codinghorror.com/tag/mac/)
