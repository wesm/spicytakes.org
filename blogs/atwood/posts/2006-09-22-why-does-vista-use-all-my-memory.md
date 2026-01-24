---
title: "Why Does Vista Use All My Memory?"
date: 2006-09-22
url: https://blog.codinghorror.com/why-does-vista-use-all-my-memory/
slug: why-does-vista-use-all-my-memory
word_count: 1199
---

Windows Vista has a **radically different approach to memory management**. Check out the “Physical Memory, Free” column in my Task Manager:


![](https://blog.codinghorror.com/content/images/2025/03/image-362.png)


At the time this screenshot was taken, this machine had a few instances of IE7 running, plus one remote desktop. I’m hardly doing anything at all, yet *I only have 6 megabytes of free physical memory*.


Now compare with this screenshot of Windows XP’s Task Manager under similar low-load conditions:


Under “Physical Memory, Available” I have approximately 1.5 gigabytes of free physical memory, as you’d expect.


So what’s going on here? Why is Vista using so much memory when I’m doing so very little?


To answer that question, you have to consider what your computer’s physical memory (RAM) is *for*. Just as a hypothetical, let’s say you wanted to create a new text file:

1. You double-click on the notepad icon.
2. The Notepad executable loads from disk into memory.
3. Notepad executes.
4. Notepad allocates free memory to store your text document.


So Notepad clearly needs a little memory for itself: enough to execute, and to store the contents of the text document it’s displaying. But that’s maybe a couple megabytes, at most. If even that. What about the other 2,046 megabytes of system memory?


You have to stop thinking of system memory as a resource and start thinking of it as a a cache. Just like the [level 1 and level 2 cache on your CPU](http://en.wikipedia.org/wiki/CPU_cache), system memory is yet another type of high-speed cache that sits between your computer and the disk drive.


And the most important rule of cache design is that **empty cache memory is wasted cache memory.** Empty cache isn’t doing you any good. It’s expensive, high-speed memory sucking down power for zero benefit. The primary mission in the life of every cache is to populate itself as quickly as possible with the data that’s most likely to be needed – and to consistently deliver a high “hit rate” of needed data retrieved from the cache. Otherwise you’re going straight to the hard drive, mister, and **if you have to ask how much going to the hard drive will cost you in performance, you can’t afford it**.


Diomidis Spinellis [published](http://www.spinellis.gr/pubs/trade/2006-login-memhier/html/memhier.html) an excellent breakdown of the cache performance ratios in a typical PC circa January 2006:

kg-card-begin: html


|  | Nominal | Worst case | Sustained |  | Productivity |
| Component | size | latency | throughput | $1 buys | (Bytes read / s / $) |
|  |  |  | (MB/s) |  | Worst case | Best case |
| L1 D cache | 64 KB | 1.4ns | 19022 | 10.7 KB | 7.91Ã‚Â·1012 | 2.19Ã‚Â·1014 |
| L2 cache | 512 KB | 9.7ns | 5519 | 12.8 KB | 1.35Ã‚Â·1012 | 7.61Ã‚Â·1013 |
| DDR RAM | 256 MB | 28.5ns | 2541 | 9.48 MB | 3.48Ã‚Â·1014 | 2.65Ã‚Â·1016 |
| Hard drive | 250 GB | 25.6ms | 67 | 2.91 GB | 1.22Ã‚Â·1011 | 2.17Ã‚Â·1017 |


kg-card-end: html

In summary, here’s how much faster each cache memory type in your computer is than the hard drive:

kg-card-begin: html


| System memory | 37x faster |
| CPU Level 2 cache | 82x faster |
| CPU Level 1 cache | 283x faster |


kg-card-end: html

Those figures explain why I only have 6 megabytes of “free” memory in Windows Vista. **Vista is trying its darndest to pre-emptively populate every byte of system memory with what it thinks I might need next.** It’s running a low-priority background task that harvests previously accessed data from the disk and plops it into unused system memory. They even have a fancy marketing name for it – [SuperFetch](http://www.microsoft.com/windowsvista/features/foreveryone/performance.mspx):


> In previous versions of Windows, system responsiveness could be uneven. You may have experienced sluggish behavior after booting your machine, after performing a fast user switch, or even after lunch. Although too many carbohydrates might slow you down after lunch, your computer slows down for different reasons. When you’re not actively using your computer, background tasks – including automatic backup and antivirus software scans – take this opportunity to run when they will least disturb you. These background tasks can take space in system memory that your applications were using. After you start to use your PC again, it can take some time to reload your data into memory, slowing down performance.
> SuperFetch understands which applications you use most, and preloads these applications into memory, so your system is more responsive. SuperFetch uses an intelligent prioritization scheme that understands which applications you use most often, and can even differentiate which applications you are likely to use at different times (for example, on the weekend versus during the week), so that your computer is ready to do what you want it to do. Windows Vista can also prioritize your applications over background tasks, so that when you return to your machine after leaving it idle, it’s still responsive.


This isn’t a new concept, of course. But **Vista treats system memory like a cache much more aggressively and effectively than any other version of Windows**. As alluded to in the above lunch anecdote – and as you can see from the Task Manager screenshot above – Windows XP has no qualms whatsoever about leaving upwards of a gigabyte of system memory empty. From a caching perspective, this is unfathomable. Vista tries its damndest to fill that empty system memory cache as soon as it can.


Although I am a total believer in the system-memory-as-cache religion, SuperFetch can still have some undesirable side effects. I first noticed that something was up when I fired up Battlefield 2 under Vista and joined a multiplayer game. Battlefield 2 is something of a memory hog; the game regularly uses a gigabyte of memory on large 64-player multiplayer maps. During the first few minutes of gameplay, I noticed that the system was a little sluggish, and the drive was running constantly. This was very unusual and totally unlike the behavior under Windows XP. Once the map is loaded and you join the game, the entire game is in memory. What could possibly be loading from disk at that point? Well, SuperFetch saw a ton of memory freed to make room for the game, and dutifully went about filling the leftover free memory on a low-priority background disk thread. Normally, this would be no big deal, but even a low-priority background disk thread is pretty noticeable when you’re playing a twitch shooter online with 63 other people at a resolution of 1600x1200.


I’m perfectly fine letting SuperFetch have its way with my system memory. **The question shouldn’t be “Why does Vista use all my memory?” but “Why the heck did previous versions of Windows use my memory so ineffectively?”** I don’t know. Maybe the rules were different before 2 gigabytes was a mainstream memory configuration.


The less free memory I have, the better; every byte of memory should be actively working on my behalf at all times. However, I do wish there was a way to tell SuperFetch to ixnay on the oadinglay when I’m gaming.

[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
[windows vista](https://blog.codinghorror.com/tag/windows-vista/)
[task manager](https://blog.codinghorror.com/tag/task-manager/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
