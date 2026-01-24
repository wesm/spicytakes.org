---
title: "Transfer Mode Downgraded"
date: 2006-09-04
url: https://blog.codinghorror.com/transfer-mode-downgraded/
slug: transfer-mode-downgraded
word_count: 305
---

I noticed when I was burning the Vista RC1 DVD that...

1. It took *forever*, e.g. nearly an hour
2. My PC was very sluggish during the burn


I began to suspect something was awry with the IDE controller that the DVD-R drive is connected to. I navigated to **Device Manager**, expanded the **IDE ATA/ATAPI controllers** tree node, right-clicked the **Parallel ATA Controller** node and selected properties.


And what do I find on the Secondary Channel tab? Sure enough, **Transfer mode downgraded**.


![](https://blog.codinghorror.com/content/images/2025/05/image-338.png)


This behavior is, of course, *by design*. Microsoft [automatically downgrades the transfer mode](https://web.archive.org/web/20061106070421/http://www.microsoft.com/whdc/device/storage/IDE-DMA.mspx) on a Parallel or Serial ATA channel after receiving more than six CRC errors on that channel. At least you can see when this has happened – Microsoft provides the little yellow alert pictured above, along with some alerts in the system Event Log.


CRC errors are *very* dangerous for a hard drive – that means you’ve got some serious hardware problems. **But for a DVD or CD drive, it probably just means you tried to read a scratched disc.** You can [override this obnoxious behavior](https://web.archive.org/web/20061004035332/http://www.neowin.net/forum/lofiversion/index.php/t19007.html) in the registry.


I flipped the switch back to “Let BIOS select transfer mode,” rebooted, and I was on my way:


![](https://blog.codinghorror.com/content/images/2025/05/image-339.png)


However, depending on what Windows XP has decided to do here, you may need to uninstall the channel (just right-click it in Device Manager to do this). Don’t worry, uninstalling won’t cause any problems. Just reboot and the channel will be redetected with default settings.


To illustrate how important proper PATA/SATA transfer mode settings are, here’s how long it took to burn a Vista RC1 DVD on my PC before and after:


in PIO mode: **56 minutes**.
in Ultra DMA 2 mode: **4 minutes**.


Friends don’t let friends use Programmed I/O Mode.

[hardware](https://blog.codinghorror.com/tag/hardware/)
[ide controller](https://blog.codinghorror.com/tag/ide-controller/)
[transfer mode](https://blog.codinghorror.com/tag/transfer-mode/)
[device manager](https://blog.codinghorror.com/tag/device-manager/)
[crc errors](https://blog.codinghorror.com/tag/crc-errors/)
