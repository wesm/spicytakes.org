---
title: "Microtech’s Crashtacular Zio Driver"
date: 2003-08-07
url: https://daringfireball.net/2003/08/microtechs_crashtacular_zio_driver
slug: microtechs_crashtacular_zio_driver
word_count: 1079
---


Stability-wise, Mac OS X is indisputably much more robust than the old Mac OS: a single application, no matter how buggy, can neither bring down the entire system nor bring down other apps. But that’s not to say Mac OS X can’t be brought down. “Kernel panic” is a fancy term, but the end result is just as disastrous as an old-fashioned system-wide crash — your only option is to reboot, and hope that you didn’t have anything important open with unsaved changes.


Under normal circumstances, individual apps on Mac OS X cannot cause a kernel panic. The reason is that Mac OS X enforces memory protection. The basic idea is that each application gets its own pool of memory (RAM), whereas on Mac OS 9, there was one giant system-wide pool of memory, shared by all applications. Memory-related bugs are fairly common programming errors, especially in system-level languages like C, C++, and Objective-C; hence, a memory error in a single application on Mac OS 9 could bring down the entire system.


The problem is that while *applications* can’t bring down the system on Mac OS X, other kinds of software can. Such as, say, device drivers implemented as kernel extensions. A *device driver* is software that allows the operating system to talk to a piece of hardware. On Mac OS X, drivers are implemented as *kernel extensions*, which unlike applications, are not restricted to their own sandbox. Buggy kernel extensions can cause kernel panics, a.k.a. system crashes.


What happened to me is this. I have a Microtech [Zio USB CompactFlash card reader](http://www.microtechint.com/zio/index.html). I used to use it on a machine running Mac OS 9, and it worked great. Now, however, I’m using Mac OS X full-time, and I wanted to try the Zio.


Just plugging it in to a USB port didn’t work; it needed driver software. So I went to Microtech’s web site and downloaded their latest Zio software for Mac OS X, which they claim works under Mac OS X 10.2. It’s a standard Mac OS X Installer package, and it installed without a hitch. Because it’s a kernel extension, I needed to reboot before using it.


Reboot I did, and it seemed to work just fine. CompactFlash cards mounted on the desktop as volumes, and iPhoto slurped the images off the cards without a hitch. OK so far.


The problem is that once the machine went to sleep, waking it up resulted in a kernel panic. This is 100 percent reproducible — once I mount a CF card through the Zio, whether I leave it in or unmount it, the kernel panics the next time the machine attempts to wake up from sleep.


What’s insidious about it is that it’s not necessarily obvious the Zio driver is causing the kernel panic. The on-screen kernel panic message offers no clue as to the cause; it’s a generic message that simply tells you to hold down the power key to bring the machine back to life. If the kernel panic occurred immediately after inserting or removing a CF card in the Zio, it’d be pretty obvious where things are going wrong. But putting the machine to sleep doesn’t seem to have anything to do with the Zio.


I suspected the Zio immediately, because I know that only certain kinds of software can cause kernel panics, and the Zio driver was the only such software I’d installed recently. Many Mac users, however, are unlikely to make such a connection — especially if they don’t encounter it until days after installing the Zio driver.


This isn’t Apple’s fault (although it would be nice if the system were able to point an accusing finger at the Zio driver in the kernel panic dialog). It’s Microtech’s fault for releasing a buggy driver.


## Out, Out Damn Spot


And so, what to do? I don’t need to use the Zio — I can just connect my camera directly via USB. (In fact, I don’t think I even paid for the Zio; I think I got it free with my camera.)


The obvious solution is just never to plug-in the Zio — like the Groucho Marx bit where a guy goes to the doctor and complains, “Doc, it hurts when I do this,” and the doctor replies, “So don’t do that.”  So long as I don’t plug in the Zio, the driver shouldn’t cause any problems. But of course, that’s not good enough. I want Microtech’s crummy software off my machine, on general principle.


Easier said than done.


The installer was no help, offering neither an Uninstall option nor uninstallation instructions. Nor was there any useful information at Microtech’s web site. I searched my boot disk for file names containing “zio” or “microtech”, but found none.


Time to get nerdy. One of the nice features of Mac OS X’s Installer application is that it creates *receipts*: logs of the files installed by each installer. They’re stored in `/Library/Receipts/`, but to read the log info, you need to view the *bill of materials* (a file with the suffix “.bom”) inside the Installer receipt package. I.e., the receipt is a package which contains a .bom file inside.


Further complicating things is that the .bom format isn’t plain text; you need special software to parse it. Namely, the `lsbom` command-line tool. In the case of the Zio, the .bom file was located at:


```

/Library/Receipts/ZiO! CF Installer.pkg/Contents/Resources/ZiO! CF Installer.bom

```


Using `lsbom`, I was able to determine that the driver software was installed as:


```

/System/Library/Extensions/USBATCF.kext

```


*“USBATCF.kext”?*  That’s so obvious! How did I miss it?


Now that I’d found it, the last problem was actually getting rid it. The entire `/System/` folder is owned by root; thus even a user with administrator privileges can’t just go there using the Finder and trash the extension. You’ve got to either nuke it via the Terminal (more convenient, but very dangerous) or reboot in Mac OS 9 or from another disk (such as a CD).


There is no easy way to get rid of anything inside `/System/`. In general, this is a good thing: it was entirely too easy in the old Mac OS to trash essential system files. But for those who aren’t sufficiently savvy regarding root permissions — which describes the vast majority of Mac users —
something like Microtech’s crummy Zio driver is likely to sit there stinking up the Extensions folder forever.



| **Previous:** | [Crayolas](https://daringfireball.net/2003/08/crayolas) |
| **Next:** | [Panic Room](https://daringfireball.net/2003/08/panic_room) |


PreviousNext