---
title: "I Believe in Murphy’s Law"
date: 2007-10-26
url: https://daringfireball.net/2007/10/murphys_law
slug: murphys_law
word_count: 602
---


Here’s how I recommend installing major new OS releases for typical users. (Atypical users would include anyone who ran developer seeds of the OS.)


First, make a complete backup of your current boot volume to an external FireWire drive using [SuperDuper](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html). ([Carbon Copy Cloner](http://www.bombich.com/software/ccc.html) would be my second choice.)


If you don’t back up daily — or at least very regularly — you’re foolish. If you don’t back up before upgrading your OS, you’re *really* foolish.  I use SuperDuper’s “Smart Update” feature to clone my boot volume every night — the “smart” aspect is that it only changes the files that have changed since the previous backup. Before I install an upgrade, I quit every running app and run a fresh backup to create a snapshot of my boot volume. That way, if anything goes wrong, I can revert to exactly the state the system was in before installing the upgrade.


Next, boot from your external backup volume to make sure that it works. What you want to see is something that looks *exactly* like booting from your regular internal hard drive. Since I’ve been using SuperDuper, this has always been the case — I have never failed to successfully boot from my backup drive. Better safe than sorry, though, so I never skip this step.


Next, shut down the computer, and *unplug the external backup volume*. The odds of an OS installation corrupting a plugged-in FireWire volume are very small. The odds of an OS installation corrupting a FireWire volume that is *not* plugged in are *zero*.


Then boot from the installer DVD, follow the on-screen instructions, and perform a default upgrade. The default upgrade is the best choice for most users almost all the time. The reason Apple makes it the default and most obvious way to upgrade is that it’s the most convenient, and *most tested* upgrade path.


[**Update 28 Aug 2009:** Starting with Snow Leopard, instead of booting from the DVD directly, you should instead pop in the installer DVD and launch the “Install Mac OS X” app on the disc. This will reboot your machine from the DVD, yes, but first it will download any necessary software updates that have come out since the disc was pressed. It’s a subtle but very nice improvement to the installer.]


Arguments that there is [something mysteriously dangerous or deficient](http://www.macjournals.com/news/despicable.html) about the default upgrade procedure — and that you should do a clean install instead, followed by tedious hours manually migrating software and data and preferences from your old installation — are voodoo. Apple’s installer engineers spend a *ton* of time making the default upgrade procedure as convenient as possible.


If you’re not a typical user; like, say, if you’ve been running pre-release developer seeds of Leopard, or if you’ve diddled with your 10.4 system software in unholy ways and really would like a factory-fresh start with 10.5, then I recommend the Archive and Install option. (That’s what I do, when upgrading from previous developer seeds.)


So, in short:

1. Do a complete backup clone to an external FireWire drive.
2. Test that the backup is indeed bootable and up to date.
3. Unplug the backup drive.
4. Pop in the installer DVD and launch the “Install Mac OS X” app.


If anything goes wrong in step 4, you have nothing to worry about, because you know that you have a complete, bootable backup.


Most people, of course, skip directly to step 4. And the odds are it’ll work out just fine for them. I say, why take a chance?



| **Previous:** | [Feedery](https://daringfireball.net/2007/10/feedery) |
| **Next:** | [Leopard](https://daringfireball.net/2007/10/leopard) |


PreviousNext