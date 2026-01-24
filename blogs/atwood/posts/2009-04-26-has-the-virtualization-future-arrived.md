---
title: "Has The Virtualization Future Arrived?"
date: 2009-04-26
url: https://blog.codinghorror.com/has-the-virtualization-future-arrived/
slug: has-the-virtualization-future-arrived
word_count: 537
---

On the eve of the Windows 7 [release candidate](https://web.archive.org/web/20090429010051/http://community.winsupersite.com/blogs/paul/archive/2009/04/26/windows-7-release-candidate-availability.aspx), Microsoft announced that Windows 7 will include a fully licensed, [virtualized copy of Windows XP](https://web.archive.org/web/20090427125940/http://community.winsupersite.com/blogs/paul/archive/2009/04/24/secret-no-more-revealing-virtual-windows-xp-for-windows-7.aspx):


> XP Mode consists of the Virtual PC-based virtual environment and a fully licensed copy of Windows XP. It will be made available, for free, to users of Windows 7 Professional, Enterprise, and Ultimate editions via a download from the Microsoft web site. XP Mode works much like today’s Virtual PC products, but with one important exception: it does not require you to run the virtual environment as a separate Windows desktop. Instead, as you install applications inside the virtual XP environment, they are published to the host OS, with shortcuts placed in the Start Menu. Users can run Windows XP-based applications alongside Windows 7 applications under a single desktop.


I’ve been talking about [our virtual machine future](https://blog.codinghorror.com/our-virtual-machine-future/) for years. Shipping a fully licensed, virtualized XP along with [some editions](http://www.penny-arcade.com/comic/2007/02/02/) of Windows 7 has *huge* implications for backwards compatibility in the Windows world.


For one thing, [Windows XP is ancient](https://blog.codinghorror.com/windows-xp-our-new-favorite-legacy-operating-system/). While XP may have been the apple of 2001’s eye, in computing dog years, it’s basically... *dead*. The original system requirements for Windows XP are almost comically low:

- 233 MHz processor
- 64 MB of RAM (128 MB recommended)
- Super VGA (800 x 600) display
- CD-ROM or DVD drive
- Keyboard and mouse


It doesn’t take much to virtualize an OS as old as Windows XP today. I was able to cram a full Windows XP image into [641 MB of disk space](https://blog.codinghorror.com/creating-smaller-virtual-machines/), and depending on what sort of apps you’re running, 256 MB of memory is often plenty.


The attraction of virtualizing older operating systems is that it **throws off the eternal yoke of backwards compatibility**. Instead of bending over backwards to make sure you never break any old APIs, you can build new systems free of the contortions and compromises inherent in guaranteeing that new versions of the operating system *never* break old applications.


Modern virtualization solutions can make **running applications in a virtual machine almost seamless**, as in the [coherence mode of Parallels](http://www.parallels.com/products/coherence/), or the unity mode of VMWare. Here’s a shot of Internet Explorer 7 running under OS X, for example.


![](https://blog.codinghorror.com/content/images/2025/04/image-357.png)


From the user’s perspective, it’s just another application in a window on their desktop. They don’t need to know or care if the application is running in a virtual machine. Substitute Windows 7 for OS X, and you get the idea. Same principle. Virtualization delivers nearly perfect backwards compatibility, because you *are* running a complete copy of the old operating system alongside the new one.


While the [screenshot gallery](https://web.archive.org/web/20090504053627/http://www.winsupersite.com/win7/xp_mode_pre_shots.asp) makes it clear to me that this feature of Windows 7 is not nearly as seamless as I’d like it to be, it’s a small but important step forward. **The demand for perfect backwards compatibility has held the industry back for too long**, and having an officially blessed virtualization solution available in a major operating system release (albeit as a downloadable extra, and only in certain editions) opens the door for innovation. It frees software developers from the crushing weight of their own historical software mistakes.

[virtualization](https://blog.codinghorror.com/tag/virtualization/)
[windows 7](https://blog.codinghorror.com/tag/windows-7/)
[xp mode](https://blog.codinghorror.com/tag/xp-mode/)
[virtual pc](https://blog.codinghorror.com/tag/virtual-pc/)
[virtual machine](https://blog.codinghorror.com/tag/virtual-machine/)
