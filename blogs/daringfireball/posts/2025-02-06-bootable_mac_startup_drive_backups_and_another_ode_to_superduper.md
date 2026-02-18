---
title: "Bootable Mac Startup Drive Backups, and Another Ode to SuperDuper"
date: 2025-02-06
url: https://daringfireball.net/2025/02/bootable_mac_startup_drive_backups_and_another_ode_to_superduper
slug: bootable_mac_startup_drive_backups_and_another_ode_to_superduper
word_count: 3583
---


Dave Nanian, [last week at the Shirt Pocket blog](https://www.shirtpocket.com/blog/index.php/shadedgrey/comments/happy_new_fix/):


> Just a quick post: macOS 15.3 is now out, and with it, a fix for
> the broken replicator. As such, macOS copying will work again with
> Erase, Then Copy backups. No update to SuperDuper is necessary
> (but feel free to install our v3.10 Beta 2, below). [...]
> Thanks for your patience as we waited for the fix from Apple. I
> know I’m relieved that I (hopefully) will no longer be bombarded
> with support because of it!


[You may recall](https://daringfireball.net/linked/2024/12/18/macos-15-2-bootable-backup-bug) that this was a bug introduced in MacOS 15.2, which prevented Shirt Pocket’s excellent [long-standing](https://daringfireball.net/search/superduper) utility [SuperDuper](https://www.shirt-pocket.com/SuperDuper/) from making a bootable clone of your startup drive. Great news, bug fixed, hurrah.


Back in December, though, when the bug had just started circulating, Mike Bombich, developer of [Carbon Copy Cloner](https://bombich.com/) (the long-standing also-excellent archrival to SuperDuper), wrote a post that I took to suggest that he thought the bug was not a bug, “[Bootable Backups Have Been Deprecated for Several Years](https://bombich.com/blog/2024/12/19/bootable-backups-have-been-deprecated-for-several-years)”:


> While some developers seem surprised by a change in macOS 15.2,
> we’ve known for several years that making bootable backups would
> eventually become impossible. We shifted CCC’s strategy away from
> relying on External Boot so our users wouldn’t be affected by this
> inevitable result.
> I took a few days off last week to help a family member, and
> returned to find the Mac community all aflutter with comments
> about bootable backups not working after the 15.2 update and
> comparisons of Apple to The Grinch. After reviewing a lot of
> comments on this subject, I felt it was time to weigh in. Apple is
> taking a lot of heat for this “bug” in 15.2, but if there is any
> finger-pointing here, I think it should be directed towards any
> developers that have misled their users into believing that ASR
> and “bootable backups” had any place in a backup/recovery strategy
> post-Big Sur.


That feels like some shade thrown toward Nanian and Shirt Pocket, but here we are with MacOS 15.3, and bootable startup drive clones are back, so I have to question who needs to don sunglasses here.


I don’t think anyone would dispute that “creating a bootable startup drive clone” has gotten complicated in the Apple Silicon era, which began with MacOS 11 Big Sur in late 2020. Not to mention the complications that were introduced with the switch from HFS+ to APFS with MacOS 10.13 High Sierra in 2017, and the read-only boot volume and SIP with MacOS 10.15 Catalina in 2019. M-series Macs boot weirder than Intel-based Macs. Not *bad* weird. I think it’s all justified in the pursuit of security (SIP stands for [System Integrity Protection](https://support.apple.com/en-us/102149), and is aptly named) and elegant system architecture. But booting is now *makes-things-much-more-difficult-than-before* weird for tools like SuperDuper and Carbon Copy Cloner.


It’s also true that from the perspective of *most* Mac users, all of these changes have been, unambiguously, changes for the better. Catastrophic boot drive errors seem to occur with less frequency than ever. Part of that is simply because SSDs are far more reliable than spinning hard disks, but part of it too is that APFS seems more reliable than HFS+ ever was. HFS+ wasn’t unreliable — and its reliability levelled up with the addition of journaling back in Mac OS X 10.3 Panther1 — but APFS seems more reliable. When catastrophe does strike, the path to recovery is better than ever. In the old days, you’d need to find a bootable system software DVD (or, going back in time, a CD, or a floppy...) or a bootable USB drive, and reinstall the OS from disk. In recent years, however, that’s been replaced by the built-in [MacOS Recovery](https://support.apple.com/guide/mac-help/intro-to-macos-recovery-mchl46d531d6/mac) system that lets you do things like run Disk Utility, restore from a Time Machine backup, reinstall the entire OS from scratch, and more. No hunting around for a special CD/DVD or thumb drive (that Murphy’s Law suggests you won’t have handy when you suddenly find yourself needing one). Just long-press the power button on your Mac and boom — you’re in Recovery mode.


I have no data to prove that APFS is more reliable than HFS+ was, so to check my gut feeling, I asked both John Siracusa (filesystem aficionado2) and Nanian (who works in the trenches of SuperDuper customer support). Both agreed that APFS is more reliable. Nanian further observed, though, that when things do go catastrophically wrong with an APFS disk now, it tends to be at a very low level — corruption at the container or volume level. And if Apple’s own Disk Utility can’t fix it, there aren’t any third-party tools that can.3 That’s the bad news. The good news is, if the problem really is just with uncorrectable corruption (and *not* a hardware failure with the device), you can use Recovery to fully erase the drive and container, clean install the OS, and restore your data from your backup drive using Migration Assistant — and that will almost certainly work.


So in some sense, the argument goes, there’s no need for bootable clones of a startup drive any more. Just clone your data, not your whole drive, to an external drive for backup purposes, and if something goes wrong with your startup volume:

1. [Boot into Recovery](https://support.apple.com/guide/mac-help/intro-to-macos-recovery-mchl46d531d6/mac).
2. Try repairing the startup disk using Disk Utility from within Recovery. Hierarchically, you do this at the volume level first, then container level, then the device itself. A device encompasses containers, containers encompass volumes, and you should repair from the inside out. This support document from Apple, “[Repair a Storage Device in Disk Utility on Mac](https://support.apple.com/guide/disk-utility/repair-a-storage-device-dskutl1040/mac)”, explains and illustrates the process.
3. If Disk Utility can’t fix it, use Recovery to erase the disk, then install the OS.
4. During the first boot after the clean install, choose the option to “restore” (which is effectively like running Migration Assistant) and choose your external drive, with the backup clone of your previous startup volume, as the source. In other words, treat your restored Mac as though it’s a brand-new Mac. (If you get to the point of creating a new, fresh user account, you’ve gone too far.)


The backup you use in step #3 above does not need to have MacOS installed on it, or, if it does have a bootable copy of MacOS, that version doesn’t need to be the same version of MacOS that Recovery clean installed on the internal drive. In SuperDuper, you can just use “Backup - all files” with Smart Update, which clones everything in the writeable “Data” volume, but doesn’t copy the OS from the read-only “System” (OS) volume (because it can’t, for technical reasons you and I need not worry about — seriously, this stuff will take you *deep* into the weeds).


But let me try to speedrun through what I, as a SuperDuper user, want to know and understand. To make a clone of your internal startup drive to an external drive, you want to use “Backup - all files”. (SuperDuper’s “Backup - user files” will only back up what’s in user account home folders inside */Users/*. That  will include most of your personal files, but it won’t include system-wide data that’s shared between all users, such as applications you’ve installed in the top-level */Applications/* folder, or everything in */Library/*. I’m sure some people have a need for “Backup - user files”, but I don’t. And it’s worth pointing out that an external drive that contains cloned data from “Backup - user files” cannot serve as the source for Migration Assistant. That’s a dealbreaker for me. The primary purpose of a SuperDuper backup, for me, is its ability to serve as the source for Migration Assistant, which, [as I’ve written previously](https://daringfireball.net/2020/11/the_m1_macs#fn2-2020-11-17), is an astonishingly good and useful tool.)


When you run “Backup - all files”, you have the following options:4

- *Erase, then copy* — This completely erases the external destination volume before copying over the entire contents of your internal startup drive. This takes longer than Smart Update, but, importantly, “Erase, then copy” will clone the *entire* internal disk, including the read-only System volume containing MacOS. This should leave you with a *bootable* clone of your startup drive.
- *Smart Update* — This does what you think a “smart” update would do. Instead of copying everything, every time, it just copies and erases what’s necessary to make the Data volume on the destination disk identical to the Data volume on the source disk. If you start with a fresh, empty external drive as the destination, it has to copy everything, but after that, Smart Update runs will be faster. But the nature of how it works means that it can only clone the read/write Data volume of your startup drive. That means it won’t copy the OS from the read-only System volume. No matter what else you do (which I’m about to cover), that’s OK, because the result of a Smart Update is an external drive containing all of your own files and installed apps, and, crucially, it’s a disk that you can use as the source for Migration Assistant.


So if you *always* use “Erase, then copy”, your SuperDuper external backups will always be bootable clones of your startup drive, with the same version of MacOS installed as your internal disk. The only downside to doing it this way is that backups take longer, because you’re erasing the external drive and copying everything every time. (You don’t have to supervise SuperDuper backups in any way, so how long they take doesn’t really matter much.)


If you *start* with “Smart Update”, you won’t have a bootable external drive (because the read-only System volume is never copied over), but you will have all your own files, and the external drive will work as a source for Migration Assistant.


If you *start* with “Erase, then copy” to create the initial backup clone, but *subsequently* use “Smart Update” for incremental backups, all of *your* data and installed apps will be updated on the external drive each time you back up. And the drive should remain a bootable backup — but the version of MacOS installed on the external drive will remain unchanged from the initial “Erase, then copy” backup. This is how I’ve been running SuperDuper.


## Why Bootable Backup Drives Still Matter


In the course of writing this article — which I’ve been thinking about, and researching, on and off since December, when the MacOS 15.2 replicator bug broke SuperDuper’s ability to create bootable backups — I’ve shaken some of my own longstanding assumptions about my backup needs. I’ve been making bootable clones with SuperDuper since whenever I started using it, which was over two decades ago. The earliest mention of SuperDuper on Daring Fireball is this post, explaining how I installed OS updates at the time, [from December 2004](https://daringfireball.net/2004/12/software_update):


> I use [SuperDuper](https://www.shirt-pocket.com/SuperDuper/) for cloning my entire startup drive. I highly
> recommend it.


Still true! I have no intention to stop making regular backups of my entire startup drive using SuperDuper. But: do I care anymore whether they’re bootable? If you’d asked me before December, I would have said yes, definitely. Why? Because, my thinking went, if something catastrophic happened to my internal startup drive, and I was working on something urgent, I’d want to get back up and working again as soon as possible. Rather than wait for MacOS Recovery to reinstall the OS on the internal drive and then wait for Migration Assistant to copy my data from my external drive to the clean install of MacOS on the internal drive, I could just boot from the external backup drive and get back to work immediately.


I’ve been lucky enough over my now many years as a Mac user to have suffered very few disk calamities like that. But I’ve encountered them. And there have been situations when having an up-to-date bootable backup drive has been useful, if not crucial. But, upon reflection, I realize now that it’s been many many years since the last time I even thought to boot from my backup drive. I used to even periodically test that the backup drive was, in fact, bootable, as a precaution. I haven’t done that in years.


I mentioned above that for my regular backup cloning, I use SuperDuper’s Smart Update, which leaves the read-only installation of MacOS on the backup drive unchanged. I just checked today and while my MacBook Pro is running the current version of MacOS (15.3 Sequoia), the version on my cloned backup drive was 12.6.1 Monterey, which was released in October 2022. (That’s the last time I did a full “Erase, then copy” backup in SuperDuper.) That effectively means my backup drive *hasn’t* been bootable, or at least not *usefully* bootable. For example, all my email files are in the mailbox format expected by Apple Mail in MacOS 15.3; I doubt that Apple Mail from MacOS 12.6 can read those mailbox files. The same is probably true for just about every app — or at least every system app from Apple — that I use. Surely *some* software from MacOS 12.6 can’t read the files or settings from the software from MacOS 15.3, and I’ll bet a lot of it can’t. New software can often recognize old file formats generated by older versions of the software; old software can’t recognize new file formats that were introduced after the old software was written.


What you should do, if you really want bootable startup drive backups via SuperDuper, is use “Erase, then copy” after every MacOS software update. Or just use “Erase, then copy” every time. But the fact that I wasn’t doing this for the last two years doesn’t mean my cloned backup drive has been useless. It just means it’s only been useful for restoring backed-up data, not for booting my Mac. Which, when I think about it, is how I would have used it if I had needed to. I don’t work in a fast-paced production environment with tight deadlines. I think MacBooks really only run properly when booting from their internal drives, anyway. If something ever goes wrong with mine, I’ll try using Disk Utility to repair it, and if that fails, I’ll turn to MacOS Recovery to clean install the OS and then use Migration Assistant to copy my data back from my external backup drive.


Thinking about it, booting from an old version of MacOS on an external backup drive containing data from the current version of MacOS sounds like a good way to corrupt some of the files on that disk — subverting the entire purpose of a backup. (Most likely, if you try this, the Mac will simply fail to boot.) It’s reckless to boot from and “use” a backup drive for production when the source drive that it’s a clone of has failed — at that point, your backup drive is likely your only local copy of the data from that failed drive. It really only ought to be treated as a read-only source for restoration. And the way Macs are designed to work today, with MacOS Recovery and Migration Assistant, makes that pretty easy.


The last time I had a catastrophic problem with my startup drive was in 2010, and I wrote about how I recovered, gracefully and with no drama (nor, seemingly, an iota of lost data), in a piece I titled “[An Ode to DiskWarrior, SuperDuper, and Dropbox](https://daringfireball.net/2010/03/ode_to_diskwarrior_superduper_dropbox)”. More of my digital life is in the cloud — and thus replicated in at least one place other than my Mac’s startup drive — now than then. Off the top of my head, I’m hard pressed to think of anything I do on my Mac that isn’t synced to cloud storage via Dropbox, iCloud, or IMAP. Starting in 2014 I’ve also been a customer of [Backblaze](https://backblaze.com/thetalkshow), a set-it-and-forget-it online backup service (that, for many years, has been a regular sponsor of this site and The Talk Show, but I recommend it because it’s good, not because they have been and might someday again be a sponsor). That’s *another* copy of all my personal data backed up somewhere.5


Having my SuperDuper-cloned backup drive be bootable is nice to have, but I really can’t say I *need* it any more. 20, 15, even just 10 years ago, that wasn’t true — I really did want the ability to boot from my backup drive at a moment’s notice. But that’s really not true any more for me. It probably isn’t for you, either. It definitely isn’t true for most Mac users.


But it remains true for *some* people, who are using (or responsible for) Macs in high-pressure tight-deadline production environments. Live broadcast studios. Magazines or newspapers with a deadline for the printer that’s just hours (or minutes) away. Places with strict security/privacy rules that forbid cloud storage of certain critical files. If the startup drive on a production machine fails, they need to get up and running *now*. Plug in a backup drive, restart, and go. Anything longer than that is unacceptable.


That’s not me. That’s probably not you. But there are a lot of people whose work environment that describes. For as much as Apple Silicon Macs have become iOS-like devices in many ways, they’re still Macs at heart: workstations. There remain people inside Apple who know that, too.


---

1. Fun fact gleaned from [the Wikipedia entry for HFS Plus](https://en.wikipedia.org/wiki/HFS_Plus): “Codenamed *Sequoia* in development, HFS+ was introduced with the January 19, 1998, release of Mac OS 8.1.” I don’t know if that’s further proof that Apple has a penchant for reusing old code names, or if code-name reuse is simply inevitable for a nearly 49-year-old company that’s always been chockablock with secret projects. ↩︎
2. *Ding.* ↩︎︎
3. One of the ways that APFS is very “modern Apple” is that it’s largely a black box. In the HFS+ days, there was [Alsoft’s DiskWarrior](https://www.alsoft.com/) — which has always been able to perform seeming miracles, outright repairing (or at least restoring temporary access to) the contents of disks that Apple’s own Disk Utility couldn’t fix. DiskWarrior is still available [but it only works on HFS+ volumes](https://www.alsoft.com/requirements). I don’t think any third-party developers would have ever described HFS+ as “well” documented, [but it was documented](https://developer.apple.com/documentation/kernel/hfs), with APIs, in low-level ways that [APFS isn’t](https://developer.apple.com/documentation/foundation/file_system/about_apple_file_system) and almost certainly never will be. But: Alsoft does claim to be working on [a major new version that will support rebuilding APFS disks](https://www.alsoft.com/diskwarrior5apfs), so my fingers are crossed. ↩︎︎
4. SuperDuper also has options to just copy newer files, or just copy different files, but I never want to use these. ↩︎︎
5. It’s terrifying in hindsight just how much of my data existed only as a single copy on a single disk back in my youth. It’s surprising that any of it survived. As a kid/teen in the ’80s, everything of mine existed only on floppy disks. Even the smallest-capacity hard drives were exorbitantly expensive. Apple’s [Hard Disk 20](https://en.wikipedia.org/wiki/Hard_Disk_20) was a 20 megabyte external drive that cost $1,500 when it debuted in 1985, which is [about $4,400](https://www.bls.gov/data/inflation_calculator.htm) in today’s dollars. That was a ton of money. But the floppy disks of the time were just 400 KB — a Hard Disk 20 gave you the storage of 50 of them. But even floppy disks were expensive, to a kid. We’d fill them up faster than we could buy them, and we’d re-use the same floppies over and over when we needed a “new” one — often begrudgingly erasing whatever was previously on the old one. That was not great for data integrity on a storage medium so primitive that it was exposed to the air. In the ’90s we all had hard drives, but those hard drives were always almost full. We were constantly copying files off our hard drives to floppies for “storage”, to create a little free space. It felt like remarkable progress when [Zip disks](https://en.wikipedia.org/wiki/Zip_drive) appeared, which were like “super floppies”, each containing 100 MB. We lived our digital lives one catastrophic hard drive failure away from losing almost all of our files, and the hard drives of that era were, by today’s standards, flaky as hell. (If you heard your hard drive start to *click*, you panicked, and immediately began copying your most important files to another disk or disks.)
My grandparents’ generation lived through the Great Depression, and they wound up with, to my generation’s eyes, very odd ideas about the availability and abundance of food. Many of the people who grew up in an era when food was profoundly scarce, wound up treating food as a scarcity for the remainder of their lives. They ate whatever was on their plate, whether they enjoyed it or not, and they were offended by anyone who didn’t.
It’s clear to me that I came of age during an era of computing when storage was both scarce and unreliable. I like to think that I’ve adapted with the times, especially given what I do for a living. I *know* how different storage is today — abundant, cheap, reliable — but I still have *feelings* about my data that are rooted in the distant past. ↩︎︎



| **Previous:** | [‘Hot Tub’, a Hardcore Porn App for iOS, Hits AltStore in the E.U.](https://daringfireball.net/2025/02/hot_tob_hardcore_porno_app_eu) |
| **Next:** | [My 2024 Apple Report Card](https://daringfireball.net/2025/02/my_2024_apple_report_card) |


PreviousNext