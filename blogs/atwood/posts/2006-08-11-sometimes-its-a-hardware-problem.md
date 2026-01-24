---
title: "Sometimes It’s a Hardware Problem"
date: 2006-08-11
url: https://blog.codinghorror.com/sometimes-its-a-hardware-problem/
slug: sometimes-its-a-hardware-problem
word_count: 791
---

One of our best servers at work was inherited from a previous engagement for x64 testing: it’s a dual Opteron 250 with 8 gigabytes of RAM. Even after a year of service, those are still decent specs. And it has a nice upgrade path, too: the [Tyan Thunder K8W](https://web.archive.org/web/20070321005012/http://www.gamepc.com/labs/view_content.asp?id=thunderk8w&page=1&cookie%5Ftest=1&MSCSProfile=95385A1F52DEA1A229D5B3754205446402496A28E3B52E54DC9A59A4DC12BEB0C41A332C9707E68B88D5DDB902A616740C6F8C2366185B615564AE36EA6239794BD4AFABCF64AC97BD4F75406EF0E472DC57BD14446CE9443284B9F45986A3CB855BEE6BD4BDF30B0E2FB8AC06ACE056DF38BB534F4CF09C11BC23B2F3F7F2A124547D14F60E1721) motherboard it’s based on supports up to 16 gigabytes of memory, and the latest dual core Opterons.


Anyway, we have it set up for Virtual Server 2005 R2 duties, running Windows Server 2003 x64. However, there was some anomalous behavior:

- Virtual Server reported weird error messages: “Some nodes of this machine do not have local memory. This can cause virtual machines to run with degraded performance.”
- The machine spontaneously rebooted during the day and overnight.


We’ve used this server for over a year and never experienced anything problematic with it. The weirdness only started with the server’s new role.


The first thing we did was **update the BIOS to the latest version, and make sure we had all the latest x64 chipset and platform drivers installed. **This is always a good first troubleshooting step – it’s the hardware equivalent of taking two Aspirins and calling in the morning. This resolved the “some nodes of this machine do not have local memory” error. However, the machine still spontaneously rebooted overnight, even with the latest BIOS and drivers.


At this point I began to suspect a hardware problem. Troubleshooting hardware stability can be difficult. But **you can troubleshoot hardware stability quite effectively with the right software: **[**Memtest86+**](http://www.memtest.org/)** and **[**Prime95**](http://www.mersenne.org/freesoft.htm).

1. **Testing CPU stability with Prime95**
Prime95 is my single favorite PC stability testing tool. If your PC can't pass an overnight Prime95 run, it absolutely, positively has a hardware problem.* Although Prime95 is primarily a CPU test, it can also be a pretty good memory test, too. After downloading it, go to the Options menu and select Torture Test.
If you have a Dual (or Quad) CPU machine, you must run multiple instances of Prime95 to load each CPU. The easiest way to do this is to copy the Prime95 folder and run multiple executables, each one from a unique folder. You may want to set CPU affinity on the executables with Task Manager, but the scheduler will take care of loading all the CPUs just fine by itself.
A bit of warning, though: when Prime95 says “lots of RAM tested,” they *mean* it. We tried running two instances of “Blend” with only 4 gigabytes of memory installed on the server and we nearly crushed the pagefile; both instances allocated nearly 6 gigabytes!


![](https://blog.codinghorror.com/content/images/2025/04/image-750.png)


In my experience, Prime95 will error out almost immediately if your CPUs or memory are unstable. This is great for troubleshooting because you know quickly if there’s a problem or not. If you can run Prime95 “small FFTs” for an hour, it’s highly likely that the CPU isn’t your problem. And if you can run the same test overnight, CPU problems can be definitively ruled out.

1. **Testing memory stability with Memtest86+**
We started with Memtest86+ because we already suspected the memory. Memtest86+ isn’t the only memory testing diagnostic out there, but it’s probably the most well-known. Microsoft also offers their Windows Memory Diagnostic utility, which works exactly the same way. Memtest86+ is [available in several forms](http://www.memtest.org/#downiso) from the Memtest86+ web site. We chose the ISO image, which we burned to CD. Boot from the Memtest86 CD, and it’ll kick off the test run.


![](https://blog.codinghorror.com/content/images/2025/04/image-751.png)


It took about 30-45 minutes to test 4 gigabytes of memory. The progress bar at the top right gives you an indication of how long the test has to run; there are 8 total tests in the standard test run. Beware, because it’ll start repeating at test #1 after the first pass!


In the case of our wayward server, Memtest86+ showed us rare, intermittent memory problems. But Prime95 consistently failed almost immediately when running the “blend” test. When we switched Prime95 to “small FFTs,” it ran two instances for an hour just fine. Clearly a memory issue! Using a combination of Memtest86+ and Prime95, we found that **our server was totally stable with 4 gigabytes of memory installed**; the minute we put in all 8 gigabytes, we couldn’t pass one or both tests.


Since 8 gigabytes of memory is essential for a VM server, removing memory wasn’t an option. On a hunch, I switched the memory speed from 200 MHz to 166 MHz in the BIOS. Now both Prime95 blend and Memtest86+ pass without incident.


Although software is notoriously unreliable, we can’t always blame the software. **Sometimes you really do have a hardware problem**.


*CPUs are almost never defective; it’s usually a heat or power supply related failure.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[server](https://blog.codinghorror.com/tag/server/)
[troubleshooting](https://blog.codinghorror.com/tag/troubleshooting/)
[bios](https://blog.codinghorror.com/tag/bios/)
[virtualization](https://blog.codinghorror.com/tag/virtualization/)
