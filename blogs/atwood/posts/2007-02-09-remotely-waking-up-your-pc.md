---
title: "Remotely Waking Up Your PC"
date: 2007-02-09
url: https://blog.codinghorror.com/remotely-waking-up-your-pc/
slug: remotely-waking-up-your-pc
word_count: 638
---

My home theater PC is set to **automatically enter a low-power sleep mode after 25 minutes of inactivity**. This works well with Vista’s Media Center, which wakes the machine up when it’s scheduled to record. This way I can avoid the additional [electricity cost of a computer](https://blog.codinghorror.com/the-cost-of-leaving-your-pc-on/) turned on around the clock. My HTPC doesn’t use that much power, but even at [a miserly 60 watts idle](https://blog.codinghorror.com/why-estimate-when-you-can-measure/), that still works out to about $80 per year here.


This arrangement works out fine most of the time. I don’t mind waking the machine manually when I want to watch television – after all, I’m in the same room and I’m walking towards the couch anyway. It’s on the way. But **a sleeping PC can be incredibly annoying when I’m sitting at my desk and I need to access that machine remotely**. I use my HTPC as my digital media file server, so I often need to transfer files back and forth. But now I can’t, because the machine is often asleep. Zzzzz. I desperately need it to WAKE UP. This always reminds me of ToeJam & E*arl on the *[*Sega Genesis*](http://en.wikipedia.org/wiki/Sega_Mega_Drive)*. If you left the controller alone for a minute, your character would fall *asleep.


![](https://blog.codinghorror.com/content/images/2025/06/image-116.png)


You had to frantically bash all the controller buttons to wake your character up, which he did only reluctantly. Unfortunately, mashing all the buttons on my keyboard didn’t seem to work. What I need is a way to remotely wake a sleeping computer.


Fortunately, one already exists: it’s called [Wake-on-LAN](http://en.wikipedia.org/wiki/Wake-on-LAN). Most modern motherboards have integrated ethernet ports that support Wake-on-LAN. Here’s how to tell if yours does: **put your computer to sleep, then take a look at the ethernet port and see if the transmit and receive LEDs are still blinking**. If they are, it’s likely you can use Wake-on-LAN. That was true in my case, so I figured it should work.


I downloaded a few Wake-on-LAN tools, but the one I liked most was Vitaly Evseenko’s small, [free command-line utility, mc-wol.exe](https://web.archive.org/web/20070217084720/http://www.matcode.com/wol.htm). These utilities send a specially crafted “magic ethernet packet” to the target PC which initiates the wake-up sequence. Note that **you have to identify the target PC by MAC address, not IP address**. I checked my router’s DHCP tables, which included the following MAC entry for my HTPC:


`00:01:80:5c:d3:24`


Armed with that information, I gave it a shot. But nothing happened. Zzzzz. Darn! I checked the PC’s BIOS settings, but there was nothing relevant. And then I remembered the properties page for the network adapter in Device Manager:


![](https://blog.codinghorror.com/content/images/2025/06/image-117.png)


![](https://blog.codinghorror.com/content/images/2025/06/image-119.png)


Bingo. It’s in two different places under Device Manager, Network Adapters, Properties:

- Advanced tab, Wake from Shutdown property, Value = On
- Power Management tab, Allow this device to wake the computer, check


I’m not sure which one is the “right” one to set. I set both just to be sure. Once did, I was able to wake up the machine remotely exactly as desired:

kg-card-begin: html

C:UsersJeffDesktoptest>mc-wol 00:01:80:5c:d3:24
WakeOnLAN v1.0 Copyright (c)2001, MATCODE Software.
Web: http://www.matcode.com
Author: Vitaly Evseenko, [[email protected]](https://blog.codinghorror.com/cdn-cgi/l/email-protection)
Sending “Magic Packet” to 00:01:80:5c:d3:24 - Success!
C:UsersJeffDesktoptest>ping mce
Pinging mce [192.168.0.110] with 32 bytes of data:
Reply from 192.168.0.110: bytes=32 time<1ms TTL=128
Reply from 192.168.0.110: bytes=32 time<1ms TTL=128
Reply from 192.168.0.110: bytes=32 time<1ms TTL=128
Reply from 192.168.0.110: bytes=32 time<1ms TTL=128
Ping statistics for 192.168.0.110:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 0ms, Maximum = 0ms, Average = 0ms


kg-card-end: html
You know, I think there’s an inspiring moral to this story: **why get out of your chair and walk 20 feet when you can spend two hours figuring out how to do it without moving at all? **It’s a symbolic victory for lazy people everywhere.

[power management](https://blog.codinghorror.com/tag/power-management/)
[remote access](https://blog.codinghorror.com/tag/remote-access/)
[file transfer](https://blog.codinghorror.com/tag/file-transfer/)
[energy saving](https://blog.codinghorror.com/tag/energy-saving/)
[wake-on-lan](https://blog.codinghorror.com/tag/wake-on-lan/)
