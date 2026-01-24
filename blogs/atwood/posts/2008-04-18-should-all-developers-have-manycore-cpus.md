---
title: "Should All Developers Have Manycore CPUs?"
date: 2008-04-18
url: https://blog.codinghorror.com/should-all-developers-have-manycore-cpus/
slug: should-all-developers-have-manycore-cpus
word_count: 1718
---

Dual core CPUs are effectively standard today, and for good reason – there are substantial, demonstrable performance improvements to be gained from having a second CPU on standby to fulfill requests that the first CPU is too busy to handle. If nothing else, **dual-core CPUs protect you from badly written software**; if a crashed program consumes all possible CPU time, all it can get is 50% of your CPU. There’s still another CPU available to ensure that the operating system can let you kill CrashyApp 5.80 SP1 Enterprise Edition in a reasonable fashion. It’s the [buddy system](http://en.wikipedia.org/wiki/Buddy_system) in silicon form.


My [previous post](https://blog.codinghorror.com/building-a-pc-part-v-upgrading/) on upgrading the CPU in your PC was more controversial than I intended. Here’s what I wrote:


> In my opinion, quad-core CPUs are still a [waste of electricity](https://blog.codinghorror.com/choosing-dual-or-quad-core/) unless you’re putting them in a server. Four cores on the desktop is great for bragging rights and mathematical superiority (yep, 4 > 2), but those four cores [provide almost no benchmarkable improvement](https://blog.codinghorror.com/quad-core-desktops-and-diminishing-returns/) in the type of applications most people use. Including software development tools.


It’s unfortunate, because this statement overshadowed the rest of the post. All I wanted to do here is **encourage people to make an *informed* decision in selecting a CPU**. Really, pick any CPU you want; the important part of that post is being unafraid to upgrade your PC. Insofar as the above paragraph distracted readers from that goal, I apologize.


However, I do have strong feelings on this topic. All too often I see users seduced by Intel’s marketing department, blindly assuming that if two CPU cores is faster than one CPU core, then, well... four, eight, or sixteen must be *insanely* fast! And out comes their wallet. I fear that many users fall prey to marketing weasels and end up paying a premium for performance that, for them, will never materialize. It’s like the bad old days of the Pentium 4 again, except for absurd megahertz clock speeds, substitute an absurd number of CPU cores.


I want people to understand that **there are only a handful of applications that can truly benefit from more than 2 CPU cores**, and they tend to cluster tightly around certain specialized areas. To me, it’s all about the benchmark data, and the benchmarks just don’t show any compelling reason to go quad-core unless you regularly do one of the following:

- “rip” or encode video
- render 3D scenes professionally
- run scientific simulations


If you frequently do any of the above, there’s *no question* that a quad-core (or octa-core) is the right choice. But this is merely my recommendation based on the benchmark data, not iron-clad fact. It’s your money. Spend it how you like. All I’m proposing is that you spend it knowledgably.


Ah, but then there’s the **multitasking argument**. I implored commenters who felt strongly about the benefits of quad-core to point me to multitasking benchmarks that showed a profound difference in performance between 2 and more-than-2 CPU cores. It’s curious. The web is awash in zillions of hardware review websites, yet you can barely find any multitasking benchmarks on any of them. I think it’s because **the amount of multitasking required to seriously load more than two CPU cores borders on the absurd**, as [Anand points out](http://www.anandtech.com/printarticle.aspx?i=2879):


> When we were trying to think up new multitasking benchmarks to truly stress Kentsfield and Quad FX [quad-core] platforms we kept running into these interesting but fairly out-there scenarios that did a great job of stressing our test beds, but a terrible job and making a case for how you could use quad-core today.


What you will find, however, is this benchmarking refrain repeated again and [again](https://web.archive.org/web/20080420042735/http://www.techreport.com/articles.x/14424/7):


> Like most of the desktop applications out there today, including its component apps, WorldBench doesn’t gain much from more than two CPU cores.


That said, I think I made a mistake in my original statement. **Software developers aren’t typical users**. Indeed, you can make a reasonable case that software developers are almost by definition edge conditions and thus they should *seek out *many-core CPUs, as [Kevin](https://web.archive.org/web/20100926114503/http://brokencoder.com/) said in the comments:


> How would you suggest developers write applications (this is what we are, and what we do, right?) that can actually leverage 4, 8, etc... CPU cores if we are running solo or dual core systems? I put this right up there with having multiple monitors. Developers need them, and not just to improve productivity, but because they won’t under stand just how badly their application runs across multiple monitors unless they actually use it. The same is true with multi-core CPUs.


I have two answers to this. One of them you probably won’t like.


Let’s start with the first one. **I absolutely agree that it is important for software developers to consider multi-core software development**, and owning one on their desktop is a prerequisite. I originally wrote about this way, way back in 2004 in [Threading, Concurrency, and the Most Powerful Psychokinetic Explosive in the Universe](https://blog.codinghorror.com/threading-concurrency-and-the-most-powerful-psychokinetic-explosive-in-the-univ/). In fact, two of the people I quoted in that old article – true leaders in the field of concurrent programming – both posted direct responses to my article yesterday, and they deserve a response.


Rick Brewster, of the [seriously amazing Paint.NET project](https://blog.codinghorror.com/making-donations-easy/), had this to say in a comment:


> Huh? Paint.NET, for one, shows large gains on quad-core versus dual-core systems. There’s even [a benchmark](http://paintdotnet.forumer.com/viewtopic.php?f=16&t=21669). I’d say that qualifies as “applications most people use.”


He’s absolutely right. A quad-core Q6700 @ 2.66 GHz trounces my dual-core E8500 @ 4.0 GHz on this benchmark, to the tune of 26 seconds vs. 31 seconds. But with all due respect to Rick – and seriously, I absolutely adore Paint.NET and his multithreading code is [incredible](http://blog.getpaint.net/2008/03/23/paintnet-just-can%E2%80%99t-satisfy-an-8-core-opteron/) – I feel this benchmark tests specialized (and highly parallelizable) filters more than core functionality. There’s a long history of [Photoshop benchmarking](http://www.barefeats.com/quad11.html) along the same lines; it’s the 3D rendering case minus one dimension. If you spend a significant part of your day in Photoshop, you should absolutely pick the platform that runs it fastest.


But we’re developers, not designers. We spend all our time talking to compilers and interpreters and editors of various sorts. [Herb Sutter](http://en.wikipedia.org/wiki/Herb_Sutter) posted an entire blog entry clarifying that, indeed, software development tools do [take advantage of quad-core CPUs](http://herbsutter.wordpress.com/2008/04/18/quad-core-a-waste-of-electricity/):

kg-card-begin: html

> You must not be using the right tools. :-) For example, here are three I’m familiar with:
> Visual C++ 2008’s [/MP flag](http://msdn2.microsoft.com/en-us/library/bb385193.aspx) tells the compiler to compile files in the same project in parallel.
> Since Visual Studio 2005 we’ve supported [parallel project builds](http://msdn2.microsoft.com/en-us/library/9h3z1a69.aspx) in Batch Build mode
> Excel 2007 does [parallel recalculation](http://msdn2.microsoft.com/en-us/library/bb687899.aspx). Assuming the spreadsheet is large and doesn’t just contain sequential dependencies between cells, it usually scales linearly up to at least 8 cores.

kg-card-end: html

Herb is an industry expert on concurrent programming and general C++ guru, and of course he’s right on all three counts. I had completely forgotten about C++ compilation, or maybe it’s more fair to say *I blocked it out*. What do you expect from a guy with a BASIC lineage? Compilation time is a huge productivity drain for C++ developers working on large projects. Compilation time using `gcc` and `time make -j<# of cores + 1>` is the granddaddy of all multi-core programmer benchmarks. Here’s a representative result for [compiling the LAME 3.97 source](http://www.phoronix.com/scan.php?page=article&item=585&num=4):

kg-card-begin: html


| 1 | Xeon E5150 (2.66 GHz Dual-Core) | 12.06 sec |
| 1 | Xeon E5320 (1.86 GHz Quad-Core) | 11.08 sec |
| 2x | Xeon E5150 | 8.26 sec |
| 2x | Xeon E5320 | 8.45 sec |


kg-card-end: html

The absolute numbers seem kind of small, but the percentages are incredibly compelling, particularly as you add up the number of times you compile every day. **If you’re a C++ developer, you *need* a quad-core CPU yesterday.** Demand it.


But what about us managed code developers, with our lack of pointers and explicit memory allocations? Herb mentioned the parallel project builds setting in Visual Studio 2008; it’s under Tools, Options, Projects and Solutions, Build and Run.


![](https://blog.codinghorror.com/content/images/2025/04/image-77.png)


As promised, it’s defaulting to the number of cores I have in my PC – two. I downloaded the very largest .NET project I could think of off the top of my head, [SharpDevelop](http://www.icsharpcode.net/OpenSource/SD/Download/). The solution is satisfyingly huge; it contains 60 projects. I compiled it a few times in Visual Studio 2008, but task manager wasn’t showing much use of even my measly little two cores:


![](https://blog.codinghorror.com/content/images/2025/04/image-76.png)


I did see a few peaks above 50%, but it’s an awfully tepid result compared to the `make -j4` one. I see nothing here that indicates any kind of possible managed code compilation time performance improvement from moving to more than 2 cores. I’m sort of curious if Java compilers (or other .NET-like language compilers) do a better job of this.


Getting back to Kevin’s question: yes, if you are a software developer writing a desktop application that has something remotely parallelizable in it, **you should have whatever number of CPU cores on the desktop you need to test and debug your code**. I suggest starting with a goal of scaling well to two cores, as that appears to be the most challenging part of the journey. Beyond that, good luck and god speed, because everything I’ve ever read on the topic of writing scalable, concurrent software goes out of its way to explain in excruciating detail how hellishly difficult this kind of code is to write.


Here’s the second part of the answer I promised you earlier. The one you might not like. **Most developers *aren’t* writing desktop applications today. They’re writing web applications.** Many of them may be writing in scripting languages that aren’t compiled, but interpreted, like Ruby or Python or PHP. Heck, they’re probably not even threaded. And yet this code somehow achieves massive levels of concurrency, scales to huge workloads, and drives some of the largest websites on the internet. All that, without thinking one iota about concurrency, threading, or reentrancy. It’s sort of magical, if you think about it.


So in the sense that mainstream developers are modelling server workloads on their desktops, I agree, they *do* probably need as many cores as they can get.

[multicore cpu](https://blog.codinghorror.com/tag/multicore-cpu/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[performance improvement](https://blog.codinghorror.com/tag/performance-improvement/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
