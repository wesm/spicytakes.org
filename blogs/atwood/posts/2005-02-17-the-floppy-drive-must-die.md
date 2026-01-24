---
title: "The Floppy Drive Must Die"
date: 2005-02-17
url: https://blog.codinghorror.com/the-floppy-drive-must-die/
slug: the-floppy-drive-must-die
word_count: 559
---

I’m currently building up my [new Pentium M system](http://www.silentpcreview.com/article218-page1.html) for HTPC duties. This means doing a bench (open air) install, clean OS build and [Prime95 torture test](http://www.mersenne.org/freesoft.htm) burn in. I also flash the BIOS to the latest revision from the manufacturer’s support page. Sometimes the motherboards are fairly up to date out of the box, but this one was four BIOS revisions behind – maybe because it’s a relatively new model and thus not quite “baked” yet.


Flashing the BIOS is one of those “must be done from a bootable DOS disk” operations. And it’s a pain every single time, mainly because **the PC industry can’t seem to rid itself of the crappy legacy 1.44mb floppy diskette drive.** Why must every new motherboard have a 1.44mb floppy diskette connector, cable, and corresponding BIOS/boot settings? Is there anything more useless? It’s not like floppies were ever very good. Where do I begin? The “depends on the phase of the moon, brand of media, and which computer it was formatted on” unreliability? the unbearable slowness? the miniscule storage size?


**The floppy drive must die.** If Apple can drop the floppy from the 1998 iMac, why can’t the PC industry kill this pernicious thing off *seven years later?* Good lord.


Of course, there are alternatives:

1. **External USB floppy drive**. I have one. It’s a last resort when I can’t make anything else work. Support for this is surprisingly robust; plug it in and it’s nearly indistinguishable from a hard-wired floppy.
2. **Bootable CDROMs** have been around at least as long as the iMac, and are quite mature. Ironically, you still need a boot floppy image to [make a CD bootable](http://www.nu2.nu/bootcd/); the CD boot process emulates a floppy boot, which loads CD-ROM drivers to read the rest of the CD. Elegant, it ain’t.
3. **Bootable USB 2.0 flash drives** aren’t quite as widely supported as bootable CDROMs, but it’s getting there. This is the true heir to the floppy drive... er, throne. Such as it is.


You’ll need a few things to get your computer booting from a USB flash drive, though:

- Obviously, a good USB flash drive, I highly recommend the PQI Intelligent Stick, the “smallest and lightest USB drive.” I don’t know about that, but these things are really tiny – and they even have a cute little activity LED. Stay away from no-name “USB 2.0” flash drives with abysmal transfer rates.
- A **USB boot formatter**. Try the free HP [USB Disk Storage format tool](https://web.archive.org/web/20050223014739/http://h18007.www1.hp.com/support/files/hpcpqdt/us/download/20306.html). You’ll also need some (groan) [DOS boot files](https://web.archive.org/web/20051028152726/http://aaltonen.us/downloads/HPUSBFW_BOOTFILES.zip). [Bootdisk.com](http://www.bootdisk.com/) is also a great resource for stuff like this – which makes [bootcd.com](http://www.ultimatebootcd.com/) seem awfully inevitable, if someone can foot the bandwidth bill.
- **BIOS support** is key – getting this new motherboard to boot from my 512mb flash drive was not easy. It doesn’t appear in the standard boot sequence BIOS options (CDROM, HDD, removable) – “removable” does not apply to USB flash drives, which doesn’t make sense to me. I had to not only enable “boot from other device,” but also disconnect the CDROM and HDD power cables. After I did that, it booted up like a champ.


I guess the price we pay for all this glorious backwards compatibility is sanity. Don’t even get me started on PS/2 keyboard and mouse ports.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[hardware](https://blog.codinghorror.com/tag/hardware/)
[bios](https://blog.codinghorror.com/tag/bios/)
[legacy technology](https://blog.codinghorror.com/tag/legacy-technology/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
