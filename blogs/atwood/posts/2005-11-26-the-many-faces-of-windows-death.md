---
title: "The Many Faces of (Windows) Death"
date: 2005-11-26
url: https://blog.codinghorror.com/the-many-faces-of-windows-death/
slug: the-many-faces-of-windows-death
word_count: 578
---

As I recall, the [Blue Screen of Death](http://en.wikipedia.org/wiki/Blue_screen_of_death) was introduced with Windows NT 3.1 circa 1993:


> **A blue screen of death occurs when the kernel, or a driver running in kernel mode, encounters an error from which it cannot recover. This is usually caused by a [hardware] driver that throws an unhandled exception or performs an illegal operation.** The only action the user can take in this situation is to restart the computer, which results in possible data loss due to Windows not properly shutting down.
> Blue screens are known as “Stop errors” in the Windows NT/2000/XP documentation, and are also sometimes referred to as “bugchecks”
> The “Stop” message contains the error code and its symbolic name (e.g. 0x0000001E, KMODE_EXCEPTION_NOT_HANDLED) along with four error-dependent values in parentheses. Depending on the error code, it may display the address where the problem occurred, along with the driver which is loaded at that address. Under Windows NT and 2000, the second and third sections of the screen contain information on all loaded drivers and a stack dump, respectively. The driver information is in three columns; the first lists the base address of the driver, the second lists the driver’s creation date (as a Unix timestamp), and the third lists the name of the driver.


The BSoD is analogous to a [Kernel Panic](http://en.wikipedia.org/wiki/Kernel_panic) in the UNIX world, and it became a standard fixture in all subsequent versions of Windows. Here’s a chronological pictorial, starting with Win9x and going up to WinXP:

kg-card-begin: html


|  |  |
|  |  |
|  |


kg-card-end: html

Microsoft catches a lot of flak for the Blue Screen of Death, but as frequently noted throughout the BSoD documentation, most BSoDs are due to [faulty third-party hardware drivers](https://blog.codinghorror.com/are-your-exceptions-silent/).


If you’re a glutton for punishment, you can attempt to decipher all that technical jibba-jabba on the BSoD or [perform BSoD troubleshooting](https://web.archive.org/web/20051124110053/http://aumha.org/win5/kbestop.htm). If you’re like most of us, you just cross your fingers and reboot. You may not see the BSoD much in Windows XP or Windows Server 2003 because the latest versions of Windows are configured to reboot automatically after a BSoD is encountered. Why wasn’t it always this way – after all, **what the heck else are you going to do after getting a BSoD?** Have a party?


After rebooting, you could celebrate by buying a BSoD T-Shirt:


![](https://blog.codinghorror.com/content/images/2025/03/image-357.png)


And for a few laughs, you can install the [BSoD screensaver](https://web.archive.org/web/20061122170510/http://www.microsoft.com/technet/sysinternals/miscellaneous/bluescreen.mspx) on a coworker’s computer when they’re not around. This thing is highly authentic – it even simulates a reboot – and quite scary when you’re not expecting it. In other words, it’s hilarious.


**The bluescreen is so well known now that it has become a “(color) Screen Of Death” meme**. Sometimes it’s used correctly, in the case of the Xbox 360 Black Screen of Death – which appears to be related to overheating.* Sometimes it’s expanded incorrectly to include things that have little to do with deep Kernel-level failures, such as the Yellow Screen of Death in ASP.NET:


![](https://blog.codinghorror.com/content/images/2025/03/image-358.png)


It’s only partially yellow, and only partially a screen o’ death. If you see it, your web app may be unavailable, but your server certainly isn’t bluescreening.


*See the [massive internal Xbox 360 heatsink](http://www.anandtech.com/systems/showdoc.aspx?i=2610&p=6) to see why I think this is the case. It’s a common problem with consoles when they’re placed on carpet or in restricted areas with limited airflow. My Nintendo 64 used to overheat!

[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[windows](https://blog.codinghorror.com/tag/windows/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
