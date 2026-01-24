---
title: "iPod Hacking via Modem"
date: 2005-02-26
url: https://blog.codinghorror.com/ipod-hacking-via-modem/
slug: ipod-hacking-via-modem
word_count: 557
---

It’s the coolest hack in years – [The Sound of iPod](http://www.ipodlinux.org/stories/piezo/):


> *I got an iPod for Christmas. The *[*ipodlinux project*](http://www.ipodlinux.org/)* was one of the main reasons for my choice and so I started exploring the iPod as far as I was able to. I patched the bootloader and got some basic code to run but there was no way to access any hardware other than the two CPUs yet. To get the LCD, Clickwheel and the harddisk working we needed to reverse engineer the bootloader in the flashrom. But to do that we first had to find a way to get that code. Seems quite impossible without any knowledge about the IO-Hardware but I found a solution...*


His solution? **To output the BIOS using sound, old-school modem style! **[Vitanuova elaborates](https://web.archive.org/web/20050301014904/http://vitanuova.loyalty.org/weblog/nb.cgi/view/vitanuova/2005/02/25/1):


> *Thanks to Mako, I heard about a remarkable piece of reverse engineering. A reverse engineer (Nils Schneider) wanted to study the firmware of the Apple iPod in order to figure out how to write software that runs on iPods. But he experienced a chicken-and-egg problem: after learning how to write simple programs to run on an iPod, he found that he couldn’t figure out how to use the iPod’s I/O hardware (in order to extract a copy of the firmwire) without studying the firmwire first to see how Apple does I/O. At the same time, he couldn’t study the firmware without first extracting a copy of it.
> His ingenious solution was to use someone else’s technique for making the iPod squawk and squeak, in order to write a program that output the firmware as a series of sounds (which could then be recorded using a microphone, and analyzed using software on a PC in order to convert them back into a digital representation of the firmware). In effect, he turned the iPod and microphone system into an acoustic modem, and wrote his own modulation scheme for representing data as sound. He wasn’t using the iPod’s headphone jack; he was making the iPod itself squeak and squawk, using a *[*piezoelectric element*](http://en.wikipedia.org/wiki/Piezoelectricity)* somewhere inside the iPod. To protect against background noise, he had to put the iPod and the microphone together inside a padded box, and let them sit for eight hours.*


Totally badass. The last hack this clever was the incredible [trojan switcheroo](http://slashdot.org/articles/01/01/25/1343218.shtml) the DirecTV guys pulled on the card hackers in 2001:


> *Last Sunday night, at 8:30 pm EST, DirecTV fired their new gun. One week before the Super Bowl, DirecTV launched a series of attacks against the hackers of their product. DirecTV sent programmatic code in the stream, using their new dynamic code ally, that hunted down hacked smart cards and destroyed them. The IRC DirecTV channels overflowed with thousands of people who had lost the ability to watch their stolen TV. The hacking community by and large lost not only their ability to watch TV, but the cards themselves were likely permanently destroyed. Some estimate that in one evening, 100,000 smart cards were destroyed, removing 98% of the hacking communities’ ability to steal their signal. To add a little pizzazz to the operation, DirecTV personally “signed” the anti-hacker attack. The first 8 computer bytes of all hacked cards were rewritten to read “GAME OVER.”*


Truly funny, and masterfully done. A great read.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[hacking](https://blog.codinghorror.com/tag/hacking/)
[reverse engineering](https://blog.codinghorror.com/tag/reverse-engineering/)
[ipod](https://blog.codinghorror.com/tag/ipod/)
[hardware hacking](https://blog.codinghorror.com/tag/hardware-hacking/)
