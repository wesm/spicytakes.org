---
title: "Keeping Time on the PC"
date: 2007-01-02
url: https://blog.codinghorror.com/keeping-time-on-the-pc/
slug: keeping-time-on-the-pc
word_count: 1268
---

I have something of a clock fetish. My latest acquisition is a [nixie tube](http://en.wikipedia.org/wiki/Nixie) clock from my wife, as a Christmas gift.


![](https://blog.codinghorror.com/content/images/2025/03/image-396.png)


My computers aren’t just [giant calculators](https://blog.codinghorror.com/my-giant-calculator/), they’re also clocks. Unfortunately, my nixie clock is a much more reliable timekeeper than any of my PCs are.


There’s a clever PC time drift graph on [this webpage](https://web.archive.org/web/20070308113444/http://vancouver-webpages.com/time/) derived from the difference between JavaScript time on the client, and the server time the webpage was sent to the client. It’s not super accurate, because the resolution is only 1 second, and the time required to send the page to the client is a variable. But it’s plenty good enough to illustrate my point:


![](https://blog.codinghorror.com/content/images/2025/03/image-397.png)


**PCs aren’t very accurate timekeepers.** The distribution of times reported here is a little disturbing, as are the giant peaks on the extreme left and right of the graph. The PCs with wildly inaccurate clocks outnumber those with accurate clocks about 2:1.

kg-card-begin: html


| PCs with correct time (+/-5 sec) | ~3000 |
| PCs whose internal clocks are more than 8 minutes off | ~7000 |


kg-card-end: html

You certainly won’t mistake PCs for [atomic clocks](http://en.wikipedia.org/wiki/Atomic_clock) any time soon. I’ve noticed that my Media Center PC in the living room is losing a lot of time. It’s frequently a minute or more off, even with internet time synchronization turned on in the Windows control panel.


![](https://blog.codinghorror.com/content/images/2025/03/image-398.png)


Right now it’s fairly accurate, but Windows just performed its internet time sync. Normally you may not care if your PC’s clock is off by 5 seconds or even a few minutes. But clock accuracy is important for a PC designed to record television shows that start and stop at specific times.


One way to “fix” a skewed PC clock, at least one that’s connected to the internet, is to have it synchronize often with a reliable internet time source. Unfortunately, there’s no visible UI in Vista or XP to change the synchronization schedule. MSKB article [Q223184](http://support.microsoft.com/kb/223184) appears to have a frequency setting, but this only applies to computers on a domain. On a domain, clients time sync with the domain controller – a dedicated server. Of course, servers are still PCs, so their clocks aren’t any more accurate than the one inside your desktop. **However, servers tend to be synchronized much more aggressively with authoritative time sources.** Compare this graph of observed webserver times to the one I presented earlier:


![Time drift for webservers, in seconds](https://blog.codinghorror.com/content/images/uploads/2007/01/6a0120a85dcdae970b0128776fee0f970c-pi.png)


My computer isn’t on a domain. Browsing around the registry keys, I found a `SpecialPollInterval` setting under the `W32TimeTimeProvidersNtpClient` key which looked promising. I did a web search and found this [worldtimeserver.com page](http://www.worldtimeserver.com/atomic-clock/) which confirms my finding. I changed the setting, stopped and started the w32time service, and it worked. The same page also describes how to add more [NTP time server sources](http://en.wikipedia.org/wiki/Network_Time_Protocol) through the registry or at the command line. So my clock drift problem is solved, for the moment.


But this fix only addresses the symptom, not the problem itself. **Why are PC clocks so inaccurate?** Part of it is by design. An extremely accurate [real-time clock](http://en.wikipedia.org/wiki/Real-time_clock) isn’t necessary for your PC to function, and adding one would probably add cost that OEMs like Dell, HP, and Apple don’t want to bear. Most manufacturers opt for [the “good enough” solution](http://www.greyware.com/software/domaintime/technical/accuracy/pcclocks.asp):


> The real-time clock (RTC) built into most machines is far from reliable. Unless its battery dies or it encounters a Y2K problem, it does a fairly good job of remembering the time while the computer’s power is turned off – as long as you don’t leave the computer off more than several hours, and don’t care if the clock is wrong by a minute or two... or three... or more. The resolution of most PC real-time clocks is one full second, and most RTCs drift considerably over time. It is not unusual for an RTC to gain or lose several seconds or even minutes a day, and some of them – while still considered to be operating correctly by the manufacturer – can be off by an hour or more after a week or two without correction.


To be fair to the manufacturers, the real-time clock inside your PC is good enough for most purposes. One research study (pdf) corroborated this conclusion:


> A typical accuracy of 35ms with respect to the UTC scale is attainable from almost any PC connected to the internet. This performance can be considered adequate for the vast majority of real-time data acquisitions, even in professional applications.


PC clocks should typically be accurate to within a few seconds per day. If you’re experiencing massive clock drift – on the order of minutes per day – **the first thing to check is your source of AC power.** I’ve personally observed systems with a UPS plugged into another UPS (this is a no-no, by the way) that gained minutes per day. Removing the unnecessary UPS from the chain fixed the time problem. I am no hardware engineer, but I’m guessing that some timing signal in the power is used by the real-time clock chip on the motherboard.


**There is an entire class of software problems, bugs, and exploits involving the system clock.** Whether it’s set to the wrong time, or it’s drifting too quickly or slowly, the results can be unexpected or possibly painful. Here are a few I can think of offhand:

- You can’t sync your clock with a NTP source if the clock is already too far out of date. How ironic.
- Some versions of Windows will fail during the setup phase with a cryptic error if the clock is set to a very old date.
- Kernel hacks can speed up or slow down the clock to facilitate cheating in online games, as related in [this article](https://web.archive.org/web/20070127202835/http://www.playnoevil.com/serendipity/index.php?/archives/1000-AhnLab-gets-anti-cheating-patent-for-speed-hack-detector.html). I remember this exact hack happening in the original Counter-Strike; there was suddenly a player on the map running around at breakneck speeds, gunning everyone down before they could respond.
- Some encryption techniques and login mechanisms (Kerberos) will fail if the system clock is too far out of sync.
- A recent Vista activation hack involved setting your system’s date back in the BIOS prior to install.
- It’s theoretically possible to attack servers by measuring their clock skew. I’m extremely skeptical of this particular attack, but [clock skew](http://www.theinternetpatrol.com/track-any-computer-on-the-internet-using-its-clock-skew-fingerprint) is an interesting fingerprint.


I haven’t even touched on the tricky issue of synchronizing events between PCs, each of which will have their own idea of what time it is, and how fast time is advancing. This can lead to some problems, as noted in the NIST document [Configuring Windows 2000 and Windows XP to use NIST TIme Servers](http://tf.nist.gov/service/pdf/win2000xp.pdf) (pdf):


> The time clock in the computer is used to keep track of when documents (files) are created and last changed, when electronic mail messages are sent and received, and when other time-sensitive events and transactions happen. In order to accurately compare files, messages, and other records residing on different computers, their time clocks must be set from a common standard. It is particularly important that computers that are networked together use a common standard of time.


We tend to think of time as an absolute, a universal interval that is the same everywhere. But inside the PC, time is a malleable material. We can go forward into the future, back into the past, or even change the rate of time’s passage. This is something that’s easy to forget when you’re developing software, and it can definitely come back and bite you.

[timekeeping](https://blog.codinghorror.com/tag/timekeeping/)
[pc clocks](https://blog.codinghorror.com/tag/pc-clocks/)
[clock accuracy](https://blog.codinghorror.com/tag/clock-accuracy/)
[javascript](https://blog.codinghorror.com/tag/javascript/)
[client-server time synchronization](https://blog.codinghorror.com/tag/client-server-time-synchronization/)
