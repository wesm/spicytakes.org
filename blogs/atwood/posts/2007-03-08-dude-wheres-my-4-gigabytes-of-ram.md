---
title: "Dude, Where’s My 4 Gigabytes of RAM?"
date: 2007-03-08
url: https://blog.codinghorror.com/dude-wheres-my-4-gigabytes-of-ram/
slug: dude-wheres-my-4-gigabytes-of-ram
word_count: 975
---

Due to fallout from a recent computer catastrophe at work, I had the opportunity to salvage 2 GB of memory. I installed the memory in my work box, which brings it up to 4 gigabytes of RAM – 4,096 megabytes in total. But that’s not what I saw in System Information:


![Vista System Information, 4 GB installed, 32-bit operating system](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0128776ff963970c-pi.png)


Only 3,454 megabytes. *Dude, where’s my 4 gigabytes of RAM?*


The screenshot itself provides a fairly obvious hint why this is happening: **32-bit Operating System**. In any 32-bit operating system, the virtual address space is limited, by definition, to the size of a 32-bit value:

kg-card-begin: html

232 = 4,294,967,296

4,294,967,296 / (1,024 x 1,024) = 4,096


kg-card-end: html
As far as 32-bit Vista is concerned, the world ends at 4,096 megabytes. That’s it. That’s all there is. No ms.Addressing more than 4 GB of memory is *possible* in a 32-bit operating system, but it takes nasty hardware hacks like 36-bit [PAE](http://en.wikipedia.org/wiki/Physical_Address_Extension) extensions in the CPU, together with nasty software hacks like the [AWE API](http://en.wikipedia.org/wiki/Address_Windowing_Extensions). Unless the application is specifically coded to be take advantage of these hacks, it’s confined to 4 GB. Well, actually, it’s stuck with even less – 2 GB or 3 GB of virtual address space, at least on Windows.OK, so we’re limited to 4,096 megabytes of virtual address space on a 32-bit operating system. Could be worse.* We could be back in 16-bit land, where the world ended at 64 *kilobytes*. Brr. I’m getting the shakes just thinking about segments, and pointers of the near and far variety. Let us never speak of this again.But back to our mystery. Where, exactly, did the other 642 megabytes of my memory go? [Raymond Chen provides this clue](https://web.archive.org/web/20070316005930/http://blogs.msdn.com/oldnewthing/archive/2006/08/14/699521.aspx):In the absence of the /PAE switch, the Windows memory manager is limited to a 4 GB physical address space. Most of that address space is filled with RAM, but not all of it. **Memory-mapped devices (such as your video card) will use some of that physical address space, as will the BIOS ROMs.** After all the non-memory devices have had their say, there will be less than 4GB of address space available for RAM below the 4GB physical address boundary.Ian Griffiths offers [a more detailed explanation](https://web.archive.org/web/20070312004648/http://www.interact-sw.co.uk/iangblog/2005/08/05/is3gbenough):To address 4GB of memory you need 32 bits of address bus. (Assuming individual bytes are addressable.) This gives us a problem – the same problem that IBM faced when designing the original PC. You tend to want to have more than just memory in a computer – you need things like graphics cards and hard disks to be accessible to the computer in order for it to be able to use them. So just as the original PC had to carve up the 8086’s 1MB addressing range into memory (640K) and ‘other’ (384K), the same problem exists today if you want to fit memory and devices into a 32-bit address range: not all of the available 4GB of address space can be given over to memory.

For a long time this wasn’t a problem, because there was a whole 4GB of address space, so devices typically lurk up in the top 1GB of physical address space, leaving the bottom 3GB for memory. And 3GB should be enough for anyone, right?

So what actually happens if you go out and buy 4GB of memory for your PC? Well, it’s just like the DOS days – there’s a hole in your memory map for the IO. (Now it’s only 25% of the total address space, but it’s still a big hole.) So the bottom 3GB of your memory will be available, but there’s an issue with that last 1GB.And if you think devices can’t possibly need that much memory-mapped IO, I have some sobering news for you: by this summer, you’ll be able to buy video cards with *1 GB of video memory*.To be perfectly clear, this isn’t a Windows problem – **it’s an x86 hardware problem**. The memory hole is quite literally invisible to the CPU, no matter what 32-bit operating system you choose. The following diagram from Intel illustrates just where the memory hole is:
kg-card-begin: html

The proper solution to this whole conundrum is to use a 64-bit operating system. However, even with a 64-bit OS, you’ll still be at the mercy of your motherboard’s chipset and BIOS; make sure your motherboard supports using 4 GB or more of memory, as outlined in [this MSKB article](http://support.microsoft.com/kb/929605/en-us).

kg-card-end: html
kg-card-begin: html


264 = 18,446,744,073,709,551,616

18,446,744,073,709,551,616 / (1,024 x 1,024) / 8 = 2 exabytes


kg-card-end: html
In case you’re wondering, the progression is *giga, tera, peta, exa*.Although the performance [benefits of 64-bit](https://blog.codinghorror.com/64-bit-desktop-vs-64-bit-server/) are somewhat dubious on the desktop, **a 64-bit OS absolutely essential if you run applications that need to use more than 2 GB of memory.** It’s not common, but we’re getting there.The memory hole for IO still exists in the 64-bit world, but most modern BIOSes allow you to banish the IO memory hole (pdf) to some (for now) ridiculously high limit when you’re running a 64-bit OS. Don’t get too excited, though. The user-mode virtual address space in 64-bit Windows is a mere 8 terabytes. Suffice it to say that we won’t be running out of physical or virtual address space on 64-bit operating systems for the foreseeable future. It’s the final solution, at least for the lifetime of everyone reading this blog post today.Here’s one parting bit of advice: if, like me, you’re planning to stick with a 32-bit operating system for the next few years, **don’t waste your money on 4 GB of RAM. You won’t be able to use it all. Buy 3 GB instead.** Every motherboard I’m aware of will happily accept 2 x 1 GB and 2 x 512 MB DIMMs.*Could be [raining](http://imdb.com/title/tt0072431/quotes).

[hardware](https://blog.codinghorror.com/tag/hardware/)
[memory](https://blog.codinghorror.com/tag/memory/)
[ram](https://blog.codinghorror.com/tag/ram/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
[32-bit](https://blog.codinghorror.com/tag/32-bit/)
[address space](https://blog.codinghorror.com/tag/address-space/)
