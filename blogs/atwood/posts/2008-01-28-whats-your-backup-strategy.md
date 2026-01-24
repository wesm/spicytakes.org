---
title: "What’s Your Backup Strategy?"
date: 2008-01-28
url: https://blog.codinghorror.com/whats-your-backup-strategy/
slug: whats-your-backup-strategy
word_count: 1005
---

Jamie Zawinski’s [public service backup announcement](https://www.jwz.org/blog/2007/09/psa-backups/) starts off with a bang:


> **Option 1**: Learn not to care about your data. Don’t save any old email, use a film camera, and only listen to physical CDs and not MP3s. If you have no possessions, you have nothing to lose.


This is obviously meant as satire, but it’s disturbingly close to reality for me. I suppose everything in my life that’s worth capturing... well, let me put it this way: you’re reading it. When I said [make it public](https://blog.codinghorror.com/when-in-doubt-make-it-public/), I really meant it. Still, I’m fairly sure Jamie was kidding, and while Google may be a great service, it’s only a so-so backup mechanism. Let’s proceed to **option 2**, which goes something like this:

kg-card-begin: html

> You have a computer. It came with a hard drive in it. Go buy two more drives of the same size or larger. If the drive in your computer is SATA2, get SATA2. If it’s a 2.5" laptop drive, get two of those. Brand doesn’t matter, but physical measurements and connectors should match.
> Get external enclosures for both of them. The enclosures are under $30.
> Put one of these drives in its enclosure on your desk. Name it something clever like “Backup.” If you are using a Mac, the command you use to back up is this:
> `sudo rsync -vaxE –delete –ignore-errors / /Volumes/Backup/`
> If you’re using Linux, it’s something a lot like that. If you’re using Windows, go f*ck yourself.

kg-card-end: html

Yeah! Take that, Windows users! Hey, wait a second. *I* use Windows. Did I mention that Jamie is a funny guy? Moving on.


I’ve long been a fan of [inexpensive hard drive enclosures](https://blog.codinghorror.com/the-single-most-important-virtual-machine-performance-tip/). Jamie’s advice confirms my long held opinion that **multiple hard drives are the most effective and easy backup process you’ll ever find**. The [`rsync` command](https://en.wikipedia.org/wiki/Rsync) is more than a simple copy; it actually does a block-by-block comparison, only copying the differences. So instead of backing up the entire contents of your hard drive (again), you only back up the parts that changed since your last backup. This is commonly known as [incremental backup](http://en.wikipedia.org/wiki/Incremental_backup).


Incremental backups only have value if you’re doing them regularly, so it’s only natural to schedule this as a recurring task.

kg-card-begin: html

> If you have a desktop computer, have this happen every morning at 5AM by creating a temporary text file containing this line:
>     `0 5 * * * rsync -vaxE --delete --ignore-errors / /Volumes/Backup/`
>     and then doing `sudo crontab -u root that-file`
> If you have a laptop, do that before you go to bed. Really. Every night when you plug your laptop in to charge.
> If you’re on a Mac, that backup drive will be bootable. That means that when (WHEN) your internal drive scorches itself, you can just take your backup drive and put it in your computer and go. This is nice.
> When (WHEN) your backup drive goes bad, which you will notice because your last backup failed, replace it immediately. This is your number one priority. Don’t wait until the weekend when you have time, do it now, before you so much as touch your computer again. Do it before goddamned breakfast. The universe tends toward maximum irony. Don’t push it.
> That third drive? Do a backup onto it the same way, then take that to your office and lock it in a desk. Every few months, bring it home, do a backup, and immediately take it away again. This is your “my house burned down” backup.

kg-card-end: html

What I like about Jamie’s approach is that it’s totally [KISS](https://en.wikipedia.org/wiki/KISS_principle), yet it touches all the cornerstones of a solid backup strategy:

- Pick a simple backup strategy you can live with, such as [3-2-1](https://en.wikipedia.org/wiki/Glossary_of_backup_terms).
- Make incremental backups a part of your **daily routine**.
- Include an **off-site backup** in your strategy.


![](https://blog.codinghorror.com/content/images/2025/09/the-3-2-1-backup-strategy.png)


And for the dissenters, although I can’t imagine too many with the minimalist backup process Jamie outlined, there’s this *bon mot*:


> “OMG, three drives is so expensive! That sounds like a hassle!” **Shut up. I know things. You will listen to me. Do it anyway.**


There is, of course, [RoboCopy](https://en.wikipedia.org/wiki/Robocopy), and Windows now has extensive Linux support for native `rsync`. But let’s face it. I’m a Windows user. When I have a problem, **I buy software**. That’s why, after hearing so many great things about it, I recently purchased a copy of [Acronis True Image](https://www.acronis.com/en/products/true-image/).


![](https://blog.codinghorror.com/content/images/2025/09/acronis-true-image-2025.png)


Acronis does a lot of things, but most of all it’s **drive imaging software, a fancy GUI over the `rsync` command**. With Jamie’s recommended two external hard drives in tow, I can use Acronis to create a bootable mirror image of my hard drive. If anything at all goes wrong, I simply **swap hard drives, and I’m back in business**. I can even create those backup images incrementally and on a schedule. You don’t even technically need a second or third hard drive; if you have a large enough primary drive, Acronis will allow you to create a new, hidden partition to store a complete backup image. You can restore these disk images from within Windows proper, during pre-boot, or from bootable USB or optical media. It is very cool, a logical evolution of the more primitive drive imaging products I’ve used for years.


Of course, as much as I am enamored of it, you don’t have to spend thirty bucks on Acronis and even more for two external hard drives to have a decent backup strategy. Lots of people use completely internet based backup services, like Mozy, Carbonite, or JungleDisk, with varying degrees of success. One thing’s for sure: until you *have* a backup strategy of some kind, you’re screwed, you just don’t know it yet. If backing up your data sounds like a hassle, that’s because it is. **Shut up. I know things. You will listen to me. Do it anyway.**

[backups](https://blog.codinghorror.com/tag/backups/)
[data storage](https://blog.codinghorror.com/tag/data-storage/)
[disaster recovery](https://blog.codinghorror.com/tag/disaster-recovery/)
[backup strategies](https://blog.codinghorror.com/tag/backup-strategies/)
[data protection](https://blog.codinghorror.com/tag/data-protection/)
[storage solutions](https://blog.codinghorror.com/tag/storage-solutions/)
