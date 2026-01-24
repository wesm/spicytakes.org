---
title: "Tivoization and the GPL"
date: 2008-02-18
url: https://blog.codinghorror.com/tivoization-and-the-gpl/
slug: tivoization-and-the-gpl
word_count: 1383
---

The original [Tivo](http://en.wikipedia.org/wiki/TiVo) was one of the finest out of box experiences I’ve *ever* had as a consumer. I remember how exciting it was to tell friends about our newfound ability to pause live television, and how liberating it felt to be freed from the tyranny of television schedules. Imagine watching whatever you want, whenever you want! Of course, digital video recorders are no longer the rare, expensive creatures they were back in 2002, so some of that original Tivo luster is irretrievably lost.


But Tivo was more than a garden variety DVR. Its true beauty was the synthesis of an intuitive user interface, cool hardware, and [an elegant remote](https://blog.codinghorror.com/the-tivo-remote/). It fired on all cylinders. I loved my series one unit with a passion most people reserve for their newborn children. I upgraded it with an ethernet connector, and plopped in a larger hard drive so I could store a week’s worth of television. Never mind that I’d have to *quit my job* to actually have time enough to watch all those shows. Somehow, the mere *knowledge* that I had a zillion episodes of Seinfeld or the Simpsons available for immediate viewing gave me a warm, fuzzy feeling in the nether regions of my geek brain. It was a kind of beautiful, pure technological freedom.


![](https://blog.codinghorror.com/content/images/2025/04/image.png)


Under the hood, Tivo was based on Linux. With a series 1 box, you could access [all the standard *nix tools](http://www.hackaday.com/2005/01/04/network-and-shell-hacks-for-tivo-series-1/), and install some cool hacks including a [web UI](http://tivowebplus.sourceforge.net/). But all that ended when I upgraded from my Series 1 Tivo box to a Series 2. This epic [2003 Tivo community forum thread](https://web.archive.org/web/20080228020632/http://archive.tivocommunity.com/tivo-vb/showthread.php?s=81a24e16965de130d451167d32c6035e&threadid=97352&perpage=20&pagenumber=1) explains why:


> *Can the stand alone Series2 running 3.2 software be hacked to get a BASH prompt over the USB/Ethernet bridge?*
> No. The config files are protected by hashes, and the list and hash check program are in the kernel initrd, which is signed and checked by the boot ROM. Any changes and it will either replace the file or not boot at all.
> *Can the method used by people using DirectTivos running 3.1 be used on a stand alone 3.2?*
> No. Unlocked software exists for the DTivos (before Tivo updated it), but all the Series2 stand alones always had the protected OS and ROMs.
> *If it is not possible, is there any hope that it will be possible in the future?*
> Who knows? There was an initial hack (set a BASH_ENV variable that makes bash run a script), but Tivo now checks for that. Changing the boot ROM is difficult, as it’s soldered to the system board. If it’s flashable (I haven’t seen a definite yes or no), you still have to get into the system to run a flash program.


In other words, **Tivo added hardware protection in the Series 2 to prevent anyone from modifying the Tivo software**. Tivo became another Xbox or Playstation console – a locked-down, hardware protected platform. You’d somehow have to defeat the hardware protection (e.g., install a modchip or flash ROMs) before you can modify anything. It looks like Series 2 protection was finally defeated by 2005, but I was long gone from the Tivo ecosystem by then, so I never saw it happen.


It’s fair to ask “so what?” at this point. So we can’t hack Tivo’s series 2 hardware. I may not like it, but it’s their hardware, not mine. They can build whatever protections into it they want, right? Ah, but there’s the rub. **Tivo is based on Linux, and Linux is licensed under the GPL.** The GPL uses [a “copyleft” license](http://www.gnu.org/copyleft/):


> The simplest way to make a program free software is to put it in the public domain, uncopyrighted. This allows people to share the program and their improvements, if they are so minded. But it also allows uncooperative people to convert the program into proprietary software. They can make changes, many or few, and distribute the result as a proprietary product. People who receive the program in that modified form do not have the freedom that the original author gave them; the middleman has stripped it away.
> In the GNU project, our aim is to give all users the freedom to redistribute and change GNU software. If middlemen could strip off the freedom, we might have many users, but those users would not have freedom. So instead of putting GNU software in the public domain, we “copyleft” it. Copyleft says that anyone who redistributes the software, with or without changes, must pass along the freedom to further copy and change it. Copyleft guarantees that every user has freedom.


This concept of software freedom is embedded deeply into the GPL. As promised, we indeed have the freedom to see the Tivo source code, copy it, and change it. **Since the Tivo’s hardware validates the software, access to the Tivo software becomes effectively meaningless.** You can modify the software all you want, but you’ll never be able to run it on your own Tivo!


You might, in fact, argue that **Tivo subverted the very principles of the GPL they built their business on**. Richard Stallman certainly did. He felt so strongly about this [perceived subversion of the GPL](https://web.archive.org/web/20080303031944/http://fsfeurope.org/projects/gplv3/drm-and-gplv3) that he literally went back and *rebuilt the GPL license* to prevent what Tivo did:


> However, there are those that want to use GPL-covered software for this purpose, and they want to do so by turning [freedom number one](https://blog.codinghorror.com/why-doesnt-anyone-give-a-crap-about-freedom-zero/) into a sham, a facade. So they plan to do something like, make a modified version of the GPL-covered program, which contains code to restrict you, and distribute that to you and somehow arrange that you can’t really modify it, or if you modify it it won’t run, or if you modify it and operate it, it won’t operate on the same data.
> They do this in various ways. This is known as [Tivoization](http://en.wikipedia.org/wiki/Tivoization) because this is what the Tivo does. The Tivo includes some GPL-covered software. It includes a GNU+Linux system, a small one, but it does, and you can get the source code for that, as required by the GPL because many parts of GNU+Linux are under the GPL, and once you get the source code, you can modify it, and there are ways to install the modified software in your Tivo and if you do that, it won’t run, period. It does a checksum of the software and it verifies that it’s a version from them and if it’s your version, it won’t run at all. This is what we are forbidding, with the text we have written for GPL version three. It says that the source code they must give you includes whatever signature keys, or codes that are necessary to make your modified version run.


Businesses can no longer adopt GPL software, then incorporate hardware protections to effectively prevent the software freedoms that the GPL specifically guarantees. This is nothing less than a full frontal assault on everyone’s favorite technology, Digital Rights Management. Note that there is a sizable loophole, however. The final version of GPL v3 ([section 6](http://gplv3.fsf.org/dd3-faq)) states that the signing key does not have to be provided when the software is distributed to businesses. But this was clearly done only grudgingly, and after intense resistance; the FAQ chides us: “*we think it’s unfortunate that people would be willing to give up their freedom like this.”*


The way Tivo built their business around the GPL and then completely subverted it with hardware protection does rankle. But I also wonder how a company like Tivo could make money if users could simply recompile the Tivo software to stop phoning home and billing them. Like consoles, the Tivo hardware is typically sold at a big loss to subsidize the platform. If that hardware could be easily formatted and the software rebuilt, you’ve created a *permanent* loss leader. So I can empathize with their desire to control the platform.


I’m not sure where I stand on the tivoization clause in GPL v3. For what it’s worth, as much as I adored my Tivo, I abandoned the platform years ago as a lost cause. I’ve already said that I think a compelling product can make me overlook the DRM, so maybe my opinion is already suspect.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[gpl](https://blog.codinghorror.com/tag/gpl/)
