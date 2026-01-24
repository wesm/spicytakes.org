---
title: "The Story of SkiFree"
date: 2005-12-18
url: https://blog.codinghorror.com/the-story-of-skifree/
slug: the-story-of-skifree
word_count: 432
---

Laurent Bourgeois sent in an amusing link to [the story of SkiFree](http://ski.ihoc.net/) in the words of Chris Pirih, the original Microsoft programmer who wrote it:


> I wrote SkiFree in C on my home computer, entirely for my own education and entertainment. One day while I was playing with it at work, the program manager for Windows Entertainment Pack happened to look over my shoulder and immediately decided he had to have this game. I called it WinSki, but the Microsoft marketroids hated that and decided, for inscrutable marketroidal reasons, to call it SkiFree. After some token resistance I let them have their way. Since the program was not originally a Microsoft product, Microsoft licensed it from me and paid me some trivial one-time fee (something like 100 shares of MSFT stock, no royalties) for its use.
> SkiFree was intended to run on a 386 PC with VGA display. Such computers were not very powerful, nothing like modern PCs that can do 3-D rendering at millions of textured polygons per second... No, in those days there wasn’t even any such thing as a “video accelerator” – the VGA was just a dumb pixel buffer hanging off the excruciatingly slow ISA bus. This made it pretty challenging to get good performance out of even simple sprite-oriented animation! Windows didn’t help matters any by introducing several layers of abstraction between the program and the video hardware... I discovered that it was worth almost any amount of preprocessing (on the “fast” 386 CPU) to reduce the amount of video I/O (over the slow ISA), so I designed a fairly clever algorithm to combine overlapping objects/erasures and blt minimal regions in each frame. The result was perfectly flicker-free transparent sprite animation at reasonable speed even on very slow computers, such as an old 286/EGA machine I found in the testing lab. Nowadays one would probably just render the sprites back-to-front in a memory buffer and blt the entire window on each frame.


Chris kindly provides an updated 32-bit version of SkiFree on his page as well.


I definitely remember SkiFree from the [Windows Entertainment Pack](http://en.wikipedia.org/wiki/Microsoft_Entertainment_Pack). What’s particularly scary is that many of these games have **their own highly detailed Wikipedia pages already –** including [a page on SkiFree](http://en.wikipedia.org/wiki/SkiFree). The infinite monkeys have been busy!


Evidently SkiFree evolved from an earlier text-mode skiing game Chris wrote for a VAX:


![](https://blog.codinghorror.com/content/images/2025/03/image-383.png)


And it was influenced by [Activision’s Atari 2600 Skiing cartridge](https://web.archive.org/web/20060116224610/http://www.atariage.com/software_page.html?SoftwareID=1280):


![](https://blog.codinghorror.com/content/images/2025/03/image-382.png)


Which brings us to the venerable SkiFree – **Windows 3.0 gaming at its finest**.


![](https://blog.codinghorror.com/content/images/2025/03/image-381.png)

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[vga display](https://blog.codinghorror.com/tag/vga-display/)
[c programming](https://blog.codinghorror.com/tag/c-programming/)
