---
title: "Is It Time for 64-bit on the Desktop?"
date: 2007-11-09
url: https://blog.codinghorror.com/is-it-time-for-64-bit-on-the-desktop/
slug: is-it-time-for-64-bit-on-the-desktop
word_count: 1117
---

I’ve been wary of 64-bit on the desktop, as the benefits are usually outweighed by [the compatibility problems](https://blog.codinghorror.com/64-bit-desktop-vs-64-bit-server/). I agree that 64-bit operating systems are inevitable in the big scheme of things, but I’ve struggled to see the relevance of 64-bit for typical desktop and laptop users. It’s a novelty, albeit a necessary one for particular niche applications. However, I’m now beginning to think **we could see a fairly broad switch to 64-bit desktop operating systems over the next few years – **much sooner than I anticipated.


Why?

1. **64-bit versions of popular consumer desktop operating systems are commonly available**. Both Vista and OS X 10.5 fully support 64-bit apps out of the box, although evidently the [OS X kernel is still 32-bit](http://arstechnica.com/reviews/os/mac-os-x-10-5.ars/6).
2. **Memory is cheap. Dirt cheap.** As of this writing, you can buy 4 gigabytes of quality DDR2 memory for around $120. The memory industry has a nasty habit of switching to newer, faster, more expensive memory types over time, but it looks like this plateau might be here to stay. 4 GB of memory is no longer a rare extravagance for rich users; it’s becoming commonplace, even mundane.
3. **The 32-bit x86 architecture doesn’t scale very well beyond 2 gigabytes.** If you install 4 gigabytes of memory, you may find yourself wondering – [Dude, Where’s My 4 Gigabytes of RAM?](https://blog.codinghorror.com/dude-wheres-my-4-gigabytes-of-ram/) Good luck explaining to the average user why their computer says they only have 3 GB of memory, even though they *paid* for 4. It’s a tough sell. And honestly, who has time to listen to a bunch of arcane technical explanations for this bizarre limitation? People just want full use of the memory they paid for.
4. **Modern video cards do not play well with 32-bit memory limits.** Newer operating systems emphasize the importance of good, discrete video hardware. To get the full suite of cool desktop effects, through [Aero](http://en.wikipedia.org/wiki/Windows_Aero), [Beryl](https://web.archive.org/web/20071110175126/http://www.beryl-project.org/), or [Core Image](https://web.archive.org/web/20081225024332/http://developer.apple.com/macosx/coreimage.html), you need a decent midrange video card. I’d say the average amount of memory on a midrange video card today is 256 megabytes, and in the enthusiast class it’s closer to 512 megabytes. I can easily see that doubling over the next two years. That’s a massive chunk of the 32-bit address space carved out for required hardware. And if you’re a hardcore gamer or multiple monitor enthusiast with more than one video card, it’s worse. [Much worse](http://www.dansdata.com/askdan00015.htm).


The switch to 64-bit is interesting because there’s a certain air of finality to it. **It may be the last **[**bit transition**](https://blog.codinghorror.com/gigabyte-decimal-vs-binary/)** in our lifetimes.**

kg-card-begin: html


| 8-bit | 28 | 256 bits |
| 16-bit | 216 | 64 KB |
| 32-bit | 232 | 4 GB |
| 64-bit | 264 | 2 EB |


kg-card-end: html

Sure, nobody will ever need more than [640 kilobytes of memory](http://www.faktoider.nu/640kb_eng.html), but this is a whole new ballgame. To put the size of the 64-bit memory address space in context, here’s a chart showing the respective sizes of each. Note that the scale is *logarithmic*.


![Graph of 8,16,32,64 bit memory spaces on a logarithmic scale](https://blog.codinghorror.com/content/images/uploads/2007/11/6a0120a85dcdae970b012877701d33970c-pi.png)


The transition from 16 to 32 bit increased our address space by a factor of 65 thousand. That’s big. We’ve been in the 32-bit era since about 1992; that address space has been good for about thirty years, give or take a few. The transition from 32 to 64 bit, whenever we finally make it, will **increase our address space by a factor of *four billion***. Will there be a transition to 128-bit machines and operating systems? Absolutely. But I’m not sure it’ll happen while we’re still alive.


You certainly **won’t be upgrading to 64-bit applications for better performance**. Or at least you shouldn’t be, unless you enjoy disappointment. 64-bit offers compelling performance benefits on servers, but on desktops, it’s a bit of a wash. On one hand, the x86 architecture simply [works better in 64-bit mode](http://arstechnica.com/reviews/os/mac-os-x-10-5.ars/6):


> The x86 instruction set was created in the 16-bit era and has accumulated quite a bit of cruft going from 16-bit to 32-bit. Some of that cruft was wisely abandoned during the [transition from 32-bit to 64-bit](http://arstechnica.com/articles/paedia/cpu/x86-64.ars). **Applications compiled for x86_64 don’t just get larger registers, they get more registers, plus a more modern calling convention and more addressing modes**. Every 32-bit x86 application can benefit from these changes, it’s just a question of how significant that benefit will be.


On the other hand, stuff is just plain *larger* in 64-bit land – your pointers and data structures now take up twice as much room. That 2 megabytes of cache on your CPU won’t be able to fit as many things in as it used to.


Once you factor in the pros and cons, you end up with a 64-bit machine that runs desktop applications a few percentage points faster than the 32-bit machine it replaced. There are some exceptions, of course – most notably games and audio/video editing – but on average, performance remains roughly the same for typical desktop applications. It’s hard to find a definitive set of benchmarks that tell the entire 64-bit versus 32-bit performance story, but all the ones I’ve seen show rough parity.


I recently upgraded both my work and home machines to 4 GB of memory. Based on the positive Vista x64 experiences related by coworkers and Scott Hanselman, I took the plunge and upgraded to Vista x64. **It was the only way to use anything close to the full 4 GB of memory.** I resisted mightily, because I expected 64-bit driver and software problems, but much to my surprise, I’ve had none. Zero. Zilch. It’s been unbelievably smooth. Perhaps it’s because I waited a good six months after the initial release of Vista to move to x64, but everything “just works.” All my hardware has 64-bit drivers. Many of my applications even come in x64 flavors, and the ones that don’t still work flawlessly. I didn’t change any of the hardware other than adding memory, but I’d *swear* my system is more responsive under x64 in daily use. And I no longer run into certain [aggravating 32-bit operating system limits](https://blog.codinghorror.com/pushing-operating-system-limits/).


Of course, my original advice regarding 64-bit operating systems hasn’t changed. **Unless you have more than 2 GB of memory, there’s no reason to bother with 64-bit.** But have you priced memory recently? Now that 4 GB configurations are approaching mainstream, it’s encouraging to know that 64-bit operating systems are out there, and that they work with a minimum of fuss. It’s certainly taken long enough to tackle this problem. Hopefully we can stay with 64-bit for the foreseeable future, and leave that pesky 128-bit problem for our kids to deal with.

[64-bit](https://blog.codinghorror.com/tag/64-bit/)
[desktop](https://blog.codinghorror.com/tag/desktop/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[memory](https://blog.codinghorror.com/tag/memory/)
[compatibility](https://blog.codinghorror.com/tag/compatibility/)
