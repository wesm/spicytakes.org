---
title: "The bloated world of Managed Code"
date: 2005-04-21
url: https://blog.codinghorror.com/the-bloated-world-of-managed-code/
slug: the-bloated-world-of-managed-code
word_count: 903
---

Mark Russinovich recently posted a blog entry bemoaning the bloated [footprint of managed .NET apps](https://web.archive.org/web/20050608030603/http://www.sysinternals.com/blog/2005/04/coming-net-world-im-scared.html) compared to their unmanaged equivalents. He starts by comparing a trivial managed implementation of Notepad to the one that ships with Windows:


> *First notice the total CPU time consumed by each process. Remember, all I’ve done is launch the programs – I haven’t interacted with either one of them. The managed Notepad has taken twice the CPU time as the native one to start. Granted, a tenth of a second isn’t large in absolute terms, but it represents 200 million cycles on the 2 GHz processor that they are running on. Next notice the memory consumption, which is really where the managed code problem is apparent. The managed Notepad has consumed close to 8 MB of private virtual memory (memory that can’t be shared with other processes) whereas the native version has used less than 1 MB. That’s a 10x difference! And the peak working set, which is the maximum amount of physical memory Windows has assigned a process, is almost 9 MB for the managed version and 3 MB for the unmanaged version, close to a 3x difference.*


While Mark has more coding skill in his pinky finger than I have in my entire body, I think his comparison is misleading at best and specious at worst. He clarifies his position in a [subsequent post](https://web.archive.org/web/20050514082431/http://www.sysinternals.com/blog/2005/04/net-world-follow-up.html):


> *Memory footprint is much more important for a client-side-only application since there can be many such applications running concurrently and clients often have limited memory. Someone stated that by the time that Longhorn ships most new systems will have 1 to 2 GB of memory. In corporate environments clients have at least 3-year life cycles and home users even in prosperous nations might upgrade less often. In developing nations you’ll see system configurations lagging the mainstream by 5 years. That means that most of the world’s computers won’t have 1-2 GB of memory until several years after Longhorn finally ships.
> It’s amazing to me that no matter how much memory we add, how much faster we make our CPUs, and how much faster we make our disks spin and seek, computing doesn’t seem to get faster. If you have a Windows NT 4 system around compare its boot time and common tasks with that of a Windows XP system. Then compare their system specs. Then ask yourself what you really can do on the Windows XP system that you can’t do on the Windows NT 4 system.*


I’m not sure why this trend is currently bothering Mark so much, because it’s been going on for decades. The subset of tasks that *must* be done in (insert favorite low-level language here) for acceptable performance gets smaller and smaller every day as hardware improves over time. This is a perfectly reasonable tradeoff to make; **computers get faster every day, but our brains don’t**. The goal of the .NET runtime is not to squeeze every drop of performance out of the platform – it’s to make software development easier. A talented developer could write several managed .NET apps in the same time it would take to write one unmanaged C++ app. Would you rather have a [single fast native app](http://www.grc.com/smgassembly.htm), or a dozen slower managed apps to choose from?


Mark’s article did get me thinking about the inherent overhead of .NET. **What is the real minimum footprint of a .NET application?**


First, I started a new **Console C# project** in VS.NET, then added a single Console.WriteLine and a Console.ReadLine. I compiled in release mode, closed the IDE, and double-clicked on the release executable. I then used [Mark’s Process Exporer](https://blog.codinghorror.com/task-manager-extreme/) to view the process properties:

kg-card-begin: html


|  | **.NET 1.1** | **.NET 2.0 b2** | **.NET 2.0 final** |
| Private Bytes | 3,912 K | 6,984 K | 7,076 K |
| Working Set | 5,800 K | 3,792 K | 3,872 K |
| Page Faults | 1,484 | 963 | 989 |
| Handles | 67 | 65 | 67 |
| GDI Handles | 11 | 5 | 5 |
| USER Handles | 2 | 0 | 0 |


kg-card-end: html

Next, I started a new **Windows Forms C# project** in VS.NET, then added a single close Button and a label. I compiled in release mode, closed the IDE, and double-clicked on the release executable. I again used process explorer to view the process properties:

kg-card-begin: html


|  | **.NET 1.1** | **.NET 2.0 b2** | **.NET 2.0 final** |
| Private Bytes | 5,760 K | 11,432 K | 11,684 K |
| Working Set | 7,876 K | 7,280 K | 7,072 K |
| Page Faults | 2,140 | 1,876 | 1,817 |
| Handles | 72 | 84 | 76 |
| GDI Handles | 34 | 23 | 25 |
| USER Handles | 15 | 18 | 12 |


kg-card-end: html

(Updated with .NET 2.0 final numbers on 1-12-06. I generated these numbers in a clean Windows XP VM, so they should be accurate.)


The .NET 2.0 beta results were generated on a different machine via Remote Desktop, but I don’t think that should affect memory and handles. Maybe it’s my VB background talking, but **these baseline footprints seem totally reasonable to me**, particularly considering the incredible productivity I get in exchange.

[.net](https://blog.codinghorror.com/tag/net/)
[managed code](https://blog.codinghorror.com/tag/managed-code/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
