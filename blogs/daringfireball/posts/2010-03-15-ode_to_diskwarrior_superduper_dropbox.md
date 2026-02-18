---
title: "An Ode to DiskWarrior, SuperDuper, and Dropbox"
date: 2010-03-15
url: https://daringfireball.net/2010/03/ode_to_diskwarrior_superduper_dropbox
slug: ode_to_diskwarrior_superduper_dropbox
word_count: 1515
---


Three weeks ago the hard drive in my MacBook Pro went bad. So far as I can tell, I didn’t lose a single byte of data. Here’s how.


First, what happened. I was on vacation for a few days with my wife immediately after Macworld Expo. Thursday 18 February was my first day back at home for a normal day of work. When I woke the machine up from sleep, everything was terribly slow. Closing windows. Opening new windows. Switching between apps. These things were all taking 30 seconds or longer. (I’d last used the machine on the airplane on my way home the night before. I noticed nothing wrong then.)


This was bad news, of course. So I saved everything that was open and rebooted. I gave it some time but the login screen didn’t appear.


So, I forced the machine to shut down and rebooted from my Snow Leopard installation disc. I ran Disk Utility and attempted to verify the MacBook Pro’s internal hard disk. Disk Utility reported that the disk was damaged in a way that it could not repair. This is extremely bad news.


I rebooted from an external hard drive, which was a clone of my internal hard drive made using [SuperDuper](http://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html). From this, I ran [DiskWarrior](http://www.alsoft.com/DiskWarrior/index.html) against my internal drive. It took a long time (three or four hours, perhaps), but DiskWarrior was able to create a new directory for my internal startup drive and mount it as a read-only volume. It looked like everything was in order, and it contained everything up to the point where I started seeing problems.


I then used SuperDuper to make a complete clone of *this* volume — the read-only volume reconstructed by DiskWarrior — to another external hard drive.


In many cases, DiskWarrior is able to replace a damaged volume’s problematic directory with the new repaired directory that it creates. In my case three weeks ago, however, DiskWarrior reported that it could not. It reported:


> DiskWarrior has successfully built a new directory for the disk
> named “Jiminy.” The new directory cannot replace the original
> directory because of a disk malfunction.
> A disk malfunction is a failure of or damage to any mechanical
> component of the disk device, or any component connected to it. The
> malfunction will likely worsen. Therefore, recovering your files
> from the DiskWarrior Preview as quickly as possible is essential.


So at this point I had:

1. The MacBook Pro’s internal hard drive, which Disk Utility stated could not be repaired, and which DiskWarrior stated was likely permanently damaged at the hardware level.
2. An external hard drive which contained a SuperDuper cloned version of the entire contents of my internal drive. Normally, the contents of this backup drive are one day old, because I run SuperDuper every night. However, in this case, the contents were over 10 days old, because I had been away from home — Macworld Expo followed immediately by a vacation.
3. A second external hard drive, which contained a fresh SuperDuper clone of the read-only version of my internal drive that DiskWarrior was able to restore.


#3, the second external drive, in theory should have at this point contained everything up until the moment I noticed the problems. But, having made this copy from a volume with serious underlying hardware problems, I considered it deeply suspect.


The best case: I’d reboot from volume #3, verify that everything seemed OK, and lose nothing.


The worst case: some or all data on volume #3 would prove to be corrupt, and I’d lose about 10 days of work, including my Keynote slides, notes, and research for my presentation at Macworld.


But even that didn’t concern me, because I use [Dropbox](http://dropbox.com/). That’s where I save all files I’m working on. My Keynote project was there. My OmniOutliner document containing the written version of my presentation was there. I wouldn’t lose email, either, because all my email accounts are IMAP, so they’re all backed on servers. The only truly important thing I could think of I might lose would be the last 10 days of data in my [Yojimbo](http://www.barebones.com/products/yojimbo/) library (which, as a database rather than a collection of small files, doesn’t play well with Dropbox and therefore isn’t stored there). Needless to say, though, I tend not to create many Yojimbo items while on vacation. [**Update, 18 March 2010:** Ends up you *can* [safely store your Yojimbo library on Dropbox](http://daringfireball.net/linked/2010/03/18/yojimbo-dropbox)].


I was lucky: volume #3, cloned from the directory recreated by DiskWarrior, was just fine. Thanks to DiskWarrior, I lost *nothing*. Thanks to Dropbox and SuperDuper, though, the whole process was stress-free, because I didn’t have much to lose even if DiskWarrior had not been able to salvage a non-corrupt image of the failed drive.


I’m sure the most commonly-used backup/recovery software for Mac users is Time Machine. I think the addition of Time Machine to Mac OS X is one of the best things Apple has ever done. It has saved data that would otherwise have been lost. And it’s great because you don’t have to invoke it manually, you just set it up and from the point forward it does its thing automatically. And, unlike SuperDuper, which only provides you with a snapshot clone of a drive, Time Machine provides a historical archive of each modification to every file.


However, I find terrific value in SuperDuper’s model. SuperDuper creates a bootable clone of your startup drive. With Time Machine, if your startup drive goes kaput, you’ve got to go through a lengthy restore process (and, in the case of hardware failure on the kaput drive, you need an extra bootable volume to restore *to*). With SuperDuper, you just plug in the clone, reboot, and you’re back up.


Here are the things I would like to impress upon you:

- Hard drives are fragile. Read as [much as you can bear](http://en.wikipedia.org/wiki/Hard_drives) to about how they work, how incredibly precisely they must operate in order to cram so many bits onto such small disks. It’s a miracle to me that they work at all. Every hard drive in the world will eventually fail. Assume that yours are all on the cusp of failure at all times. It’s good to be spooked about how long your hard drives will last.
- Buy a bunch of large external hard drives for use as backup volumes. It’s not enough to have one. If I only had one, I wouldn’t have been able to clone the volume DiskWarrior restored for me without taking a terrible chance and overwriting the known-good 10-day-old SuperDuper clone. It is no fun at all to spend money on hard drives whose only purpose is to be used in case one of your regular drives fails. But when you need them, it feels like the best money you’ve ever spent.
- Seriously, buy a few external drives, not just one. Buy another one to store off-site in case your home is burgled or there’s a fire or other catastrophe. Don’t use backup drives for any other purpose.
- Use SuperDuper to clone your startup volume (or volumes, plural, if you have several volumes used for primary daily storage). Run it every day. Use it even if you also use Time Machine. You will thank me when a drive fails and a few minutes later you’re right back where you were the night before. There are [other](http://www.bombich.com/) apps that serve a similar purpose. I haven’t tried them in years because SuperDuper has never let me down.
- Test your backups. Try booting from them once in a while just make sure they work.
- Use Dropbox. In addition to the fact that Dropbox is fast and reliable at copying files saved locally to Dropbox’s remote servers, Dropbox *also* remembers each *version* of each file you save. Dropbox provides syncing, remote storage, and simple versioning backup all at once. You can [trust it](http://www.randsinrepose.com/archives/2008/11/25/dumbing_down_the_cloud.html). All you do is save your files like you normally do. And unlike all my other recommendations here, you can use Dropbox for free. I suspect the only people who aren’t using Dropbox are those who haven’t tried it.
- My strategy for disk repair software: try Apple’s Disk Utility first, then, if it doesn’t fix everything, DiskWarrior. If DiskWarrior fails assume the drive is toast. If you don’t own DiskWarrior, [buy it immediately](http://www.alsoft.com/Buy/index.html). It has worked wonders for me many times over the past decade, and has never once made a problem worse. There are other disk utility apps. I haven’t used them, and consider myself so well served by Disk Utility and DiskWarrior that I see no reason to try.1


---

1. The best disk repair utility comparison I’ve ever seen, by far, is [David Shayer’s in TidBITS](http://db.tidbits.com/article/07451) back in 2003. (See also [his follow-up](http://db.tidbits.com/article/7696) to include TechTool Pro.) His conclusion: try Disk Utility first, and if it fails, try DiskWarrior. Seven years later I believe this advice stands. ↩︎



| **Previous:** | [iPhone Apps on the iPad](https://daringfireball.net/2010/03/iphone_apps_on_the_ipad) |
| **Next:** | [Mozilla, Video, and Mobile Computing](https://daringfireball.net/2010/03/mozilla_video_mobile) |


PreviousNext