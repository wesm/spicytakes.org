---
title: "Please Sir May I Have a Linker?"
date: 2004-01-28
url: https://www.joelonsoftware.com/2004/01/28/please-sir-may-i-have-a-linker/
word_count: 906
---


For some reason, Microsoft’s brilliant and cutting-edge .NET development environment left out one crucial tool… a tool that has been common in software development environments since, oh, about 1950, and taken so much for granted that it’s incredibly strange that nobody noticed that .NET doesn’t really have one.


The tool in question? **A linker.** Here’s what a linker does. It combines the compiled version of your program with the compiled versions of all the library functions that your program uses. Then, it removes any library functions that your program does not use. Finally, it produces a single executable binary program which people can run on their computers.


Instead, .NET has this idea of a “runtime” … a big 22 MB steaming heap of code that is linked dynamically and which everybody has to have on their computers before they can use .NET applications.


Runtimes are a problem, much like DLLs, because you can get into trouble when application version 1 was designed to work with runtime version 1, and then runtime version 2 comes out, and suddenly application version 1 doesn’t work right for some unpredictable reason. For example right now for some reason our internal company control panel is rounding sales figures to four decimal points, as a result of upgrading from 1.0 to 1.1 of the runtime. Usually the incompatibilities are worse.


In fact .NET includes an extensive technology system called “manifests” which are manifestly complicated and intended to insure that somehow *only* the right runtime will be used with a given application, but nobody I know can figure out how to use them.


This calls for a story. At the Fog Creek New Year’s Eve party, we wanted a bunch of computer screens in the main room to display a countdown until midnight. Michael wrote an application to do this in C# with WinForms in about 60 seconds. It’s a great development environment.


My job was getting countdown.exe to run on three computers. Sounds easy.


Nope. Double click the EXE, and I got a ridiculously user-hostile error message about mscoree.dll or something, followed by a gratuitous dump of my path. No mention of the fact that the problem was simply that the .NET runtime was not installed. Luckily I’m a programmer and I figured that must be the problem.


How do you install the runtime? The “easiest” way is through Windows Update. But Windows Update really wanted me to get all the critical updates *first* before I installed the runtime. That’s reasonable, right? Two of the “critical” updates were a Windows service pack and a new version of Internet Explorer, both of which required a reboot.


All told, for each computer I needed to run this little .NET application on, I had to download something like 70 or 80 MB (good thing we have a fast net connection) and reboot three or four times. And this is at a software company! I know how long it took, because the first time it started downloading, I put [Office Space](http://www.amazon.com/exec/obidos/tg/detail/-/6305508550/ref=nosim/joelonsoftware) on the big screen TV, and by the time the movie was over, the installation process was *almost* finished. Every ten minutes during the movie I had to jump up, go to each computer, and hit OK to some stupid dialog box.


This is frustrating enough for our in-house apps. But think about our product [CityDesk](http://www.fogcreek.com/CityDesk). Almost all of our users download a [free trial version](http://www.fogcreek.com/CityDesk/Starter.html) before buying the product. The download is around 9 MB and has no additional requirements. Almost none of these users has the .NET runtime yet.


If we asked our trial users, usually small organizations and home users, to go through a movie-length installation hell just to try our app, I think we’d probably lose 95% of them. These are not customers *yet*, they’re prospects, and I can’t afford to give up 95% of my prospects just to use a nicer development environment.


“But Joel,” people say, “eventually enough people will have the runtime and this problem will go away.”


I thought that too, then I realized that every six or twelve months Microsoft ships a *new version* of the runtime, and the gradually increasing number of people that have it deflates again to zero. And I’ll be damned if I’m going to struggle to test my app on three different versions of the runtime just so I can get the benefit of the 1.2% of the installed base that has one of the three.


I just want to link everything I need in a single static EXE that runs without any installation prerequisites. I don’t mind if it’s a bit bigger. All I would need is the functions that I actually *use*, the byte code interpreter, and little bit of runtime stuff. I don’t need the entire C# compiler which is a part of the runtime. I promise CityDesk doesn’t need to compile any C# source code. I don’t need all 22 MB. What I need is probably five or six MB, *at most*.


I know of companies that have the technology to do this, but they can’t do it without permission from Microsoft to redistribute bits and pieces of the runtime like the byte code interpreter. So Microsoft, wake up, get us some nice 1950s-era linker technology, and let me make a single EXE that runs on any computer with Win 98 or later and *no other external dependencies*. Otherwise .NET is fatally flawed for consumer, downloaded software.
