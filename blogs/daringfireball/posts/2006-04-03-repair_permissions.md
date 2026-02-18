---
title: "‘Repair Permissions’ Is Not a Recommended Step When Applying System Updates"
date: 2006-04-03
url: https://daringfireball.net/2006/04/repair_permissions
slug: repair_permissions
word_count: 678
---


Like most of the content in MacInTouch’s daily reports, there’s no
permalink, alas, but [today](http://www.macintouch.com/index.shtml#tip.2006.04.03.up), in a tidbit related to the release
of Mac OS X 10.4.6, there’s this dubious nugget:


> Rich Cruse notes an extra surprise in Mac OS X 10.4.6:
> As you know, with any update we are told to repair permissions
> before and after installing new system software or updates. With
> the 10.4.6 update, there is a new twist to the installation
> process and a welcome surprise after. After you install the update
> and are prompted to restart, the machine does its usual thing. It
> stays on the Grey Apple screen for a longer than usual time, but
> now instead of stalling, it restarts itself and boots normally.
> The welcome surprise is that after the machine boots up, a quick
> “Repair Permissions” says that everything is A-Okay. There were no
> repairs needed! That is a first! Perhaps they added a script to do
> exactly that, since most people haven’t a clue on how to or where
> to find the Disk Utility and Repair Permissions. All is fine so
> far with the update.


We are told to repair permissions before and after each update by
whom? Certainly not by Apple. Perhaps Cruse means “them”, the same
“them” who, in the classic Mac OS era, recommended zapping your PRAM
every time you need to reboot your Mac after the system was wedged
by a crashed app.


To be clear, perfectly clear: *Apple does not recommend that you do
this.* All you need to do before applying a system update is follow
the steps in the accompanying release notes, and nowhere therein has
it ever been mentioned that you should run Disk Utility’s Repair
Permissions feature before or after installing the update, let alone
doing so before *and* after.


[**Update:** And to be even more clear, the 10.4.6 updater does *not*
repair permissions as part of its installation process. The second
reboot for PowerPC-based Macs has nothing to do with permissions;
it’s because some of the components updated in 10.4.6 run very early
in the boot process and are installed after the first reboot. The
second reboot is so the machine can start up with those new components
in place. What’s still a mystery to me is why this double reboot only
applies to PowerPC machines; perhaps Intel-based Macs already have
up-to-date versions of these components?]


I wrote about the [simple steps I follow when applying system
updates](http://daringfireball.net/2004/12/software_update) a little over a year ago, and my advice still stands.
The only part of it that I truly consider essential is step 2: to
perform a full backup before applying the update. I use [SuperDuper](http://www.shirt-pocket.com/SuperDuper/)
to keep a mirror of my entire startup drive on a pair of external
FireWire disks which I rotate every few weeks.


**Important note if you, like me, back up to external hard drives:**
It’s a good idea to unmount and disconnect your external drives —
but especially your backup drive — before running a system update.
A buggy installer could damage or inadvertently delete files from
any mounted drive on your system. Remember the [iTunes 2
installer](http://www.xlr8yourmac.com/OSX/itunes2_erased_drives.html)? If your backup drive isn’t even connected, nothing
the installer does can possibly affect it.


Repairing permissions is a troubleshooting tool, not a regular
maintenance step. I have never run repair permissions on any of the
four Macs in active duty here at Daring Fireball HQ, and none of
them have had a single problem attributable to system and security
updates.1


It’s this simple: if it were good for your Mac, Apple would
recommend it. I guarantee you that the engineers on Apple’s
installer team know more than “they” do.


---

1. I’ll also add that “they” recommend running the full Combo updaters
with each update. Me? I just run Software Update. “They” make a lot
more work out of system updates than they need to.
↩︎



| **Previous:** | [Adios Avie](https://daringfireball.net/2006/03/adios_avie) |
| **Next:** | [Windows: The New Classic](https://daringfireball.net/2006/04/windows_the_new_classic) |


PreviousNext