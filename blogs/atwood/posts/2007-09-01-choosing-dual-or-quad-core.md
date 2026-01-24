---
title: "Choosing Dual or Quad Core"
date: 2007-09-01
url: https://blog.codinghorror.com/choosing-dual-or-quad-core/
slug: choosing-dual-or-quad-core
word_count: 895
---

I’m a [big fan of dual-core systems](https://blog.codinghorror.com/multiple-core-cpu-futures/). I think there’s a clear and substantial benefit for all computer users when there are two CPUs waiting to service requests, instead of just one. If nothing else, it lets you gracefully terminate an application that has gone haywire, consuming all available CPU time. It’s like having a backup CPU in reserve, waiting to jump in and assist as necessary. But for most software, **you hit a point of diminishing returns very rapidly after two cores**. In [Quad-Core Desktops and Diminishing Returns](https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/), I questioned how effectively today’s software can really use even *four* CPU cores, much less the inevitable eight and sixteen CPU cores we’ll see a few years from now.


To get a sense of what kind of performance improvement we can expect going from 2 to 4 CPU cores, let’s focus on the Core 2 Duo E6600 and Core 2 Quad Q6600 processors. These 2.4 GHz CPUs are identical in every respect, except for the number of cores they bring to the table. In a [recent review](https://web.archive.org/web/20070908202912/http://www.techreport.com/articles.x/12737/1), Scott Wasson at the always-thorough Tech Report presented a slew of benchmarks that included both of these processors. Here’s a quick visual summary of **how much you can expect performance to improve when upgrading from 2 to 4 CPU cores**:

kg-card-begin: html


| Task Manager CPU Graph |  | Improvement
2 to 4 cores |
|  | The Elder Scrolls IV: Oblivion | None |
|  | Rainbow 6: Vegas | None |
|  | Supreme Commander | None |
|  | Valve Source Engine Particle Simulation | 1.8x |
|  | Valve VRAD Map Compilation | 1.9x |
|  | 3DMark06: Return to Proxycon | None |
|  | 3DMark06: Firefly Forest | None |
|  | 3DMark06: Canyon Flight | None |
|  | 3DMark06: Deep Freeze | None |
|  | 3DMark06: CPU Test 1 | 1.7x |
|  | 3DMark06: CPU Test 2 | 1.6x |


kg-card-end: html

The results seem encouraging, until you take a look at the applications that benefit from quad-core – the ones that aren’t purely synthetic benchmarks are **rendering, encoding, or scientific applications** . It’s the same old story. Beyond encoding and rendering tasks which are naturally amenable to parallelization, the task manager CPU graphs tell the sad tale of software that simply isn’t written to exploit more than two CPUs.


Unfortunately, CPU parallelism is inevitable. Clock speed can’t increase forever; the physics don’t work. Mindlessly ramping clock speed to 10 GHz isn’t an option. CPU vendors are forced to deliver more CPU cores running at nearly the same clock speed, or at very small speed bumps. Increasing the number of CPU cores on a die *should* defeat raw clock speed increases, at least in theory. **In the short term, we have to choose between faster dual-core systems, or slower quad-core systems. Today, a quad-core 2.4 GHz CPU costs about the same as a dual-core 3.0 GHz CPU.** But which one will provide superior performance? A [recent Xbit Labs review](https://web.archive.org/web/20071011010129/http://www.xbitlabs.com/articles/cpu/display/core2quad-q6600.html) performed exactly this comparison:

kg-card-begin: html


|  | **3.0 GHz**
Dual Core | **2.4 GHz**
Quad Core | improvement
2 to 4 cores |
| PCMark05 | 9091 | 8853 | -3% |
| SysMark 2007, E-Learning | 167 | 140 | -16% |
| SysMark 2007, Video Creation | 131 | 151 | 15% |
| SysMark 2007, Productivity | 152 | 138 | -9% |
| SysMark 2007, 3D | 160 | 148 | -8% |
| Quake 4 | 136 | 117 | -15% |
| F.E.A.R. | 123 | 110 | -10% |
| Company of Heroes | 173 | 161 | -7% |
| Lost Planet | 62 | 54 | -12% |
| Lost Planet “Concurrent Operations” | 62 | 81 | 30% |
| DivX 6.6 | 65 | 64 | 0% |
| Xvid 1.2 | 43 | 45 | 5% |
| H.264 QuickTime Pro 7.2 | 189 | 188 | 0% |
| iTunes 7.3 MP3 encoding | 110 | 131 | -16% |
| 3ds Max 9 SP2 | 4.95 | 6.61 | 33% |
| Cinebench 10 | 5861 | 8744 | 49% |
| Excel 2007 | 39.9 | 24.4 | 63% |
| WinRAR 3.7 | 188 | 180 | 5% |
| Photoshop CS3 | 70 | 73 | -4% |
| Microsoft Movie Maker 6.0 | 73 | 80 | -9% |


kg-card-end: html

It’s mostly what I would expect – **only rendering and encoding tasks exploit parallelism enough to overcome the 25% speed deficit between the dual and quad core CPUs**. Outside of that specific niche, performance will actually *suffer* for most general purpose software if you choose a slower quad-core over a faster dual-core.


However, there were some surprises in here, such as Excel 2007, and the Lost Planet “concurrent operations” setting. It’s possible software engineering will eventually advance to the point that clock speed matters less than parallelism. Or eventually it might be irrelevant, if we don’t get to make the choice between faster clock speeds and more CPU cores. But in the meantime, **clock speed wins most of the time**. **More CPU cores isn’t automatically better.** Typical users will be better off with the fastest possible dual-core CPU they can afford.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[cpu cores](https://blog.codinghorror.com/tag/cpu-cores/)
[performance improvement](https://blog.codinghorror.com/tag/performance-improvement/)
[software development](https://blog.codinghorror.com/tag/software-development/)
