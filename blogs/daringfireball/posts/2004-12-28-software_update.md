---
title: "Software Update Tips and Voodoo"
date: 2004-12-28
url: https://daringfireball.net/2004/12/software_update
slug: software_update
word_count: 1854
---


Last week, [Jeffrey Zeldman shared the procedure used at his design
studio for updating Mac OS X system software](http://www.zeldman.com/daily/1204d.shtml#macos1037). I hesitate to call
his tips “advice”, because he doesn’t use that term — rather, it’s
simply a statement of fact. *Here’s what we did, and we avoided any
problems.*


Some of his steps are quite sound, and I highly recommend them.
Others, I suspect, are entirely superfluous, hinging mostly on
superstition. I think it’s a list worth examining.


First, though, here’s the procedure *I* use when installing system
updates (e.g. from 10.3.6 to 10.3.7) and security updates.

1. *Wait at least one business day after the release of the update.*
By and large, Apple’s software updaters work exactly as they
should. But, every once in a while, a bad one slips through the QA
cracks. E.g. the [iTunes 2.0 installer](http://www.xlr8yourmac.com/OSX/itunes2_erased_drives.html) for Mac OS X could
erase entire volumes; or the QuickTime 6.0.2 installer, which
[wouldn’t work](https://daringfireball.net/2002/10/perl_for_dummies_and_apple_installer_engineers) on systems running newer versions of Perl than
the default system software.
So, I say, wait a day or two. If Apple releases an update on a
Friday, wait until Monday evening or Tuesday. See if any
widespread reports of problems appear on sites like [MacFixIt](http://macfixit.com/) and [MacInTouch](http://macintouch.com/). Key word here being *widespread*; a
small handful of unreproducible reports regarding problems after
running an update are inevitable. What I look for are clear signs
that something is wrong with the update.
2. *Run a full backup.* Of course you should have an automated
backup schedule in place, but, if, like most people, you only
create backups manually, now is the time to do it. Chalk it up to
Murphy’s Law. Yes, the odds are good that you will *never*
encounter a catastrophic problem while running Software Update — but if you do, and you don’t have a recent backup, you’ll wish you
did. If you have a working, recent backup, you can’t lose data.
**Update:** I use [SuperDuper](http://www.shirt-pocket.com/SuperDuper/) for cloning my entire startup drive. I highly recommend it.
3. *Log out. Then log back in while holding the Shift key.*
I’ll admit right up front that I have no evidence that this step
is in fact at all useful. My thinking is that it’s safer to run
Software Update under pristine login conditions, with no running
processes other than the system software. Logging out quits
anything running in your current session; logging back in while
holding Shift suppresses your login startup items.
You’re supposed to be able to run Software Update any time you
want, and I’m aware of no technical reason why you should quit
your running processes while it runs. But, you have to restart
after running Software Update anyway (for system and security
updates) — so I figure why not log out first and allow Software
Update to run under pristine conditions? Even if this is just
superstitious voodoo, it’s harmless voodoo. It only costs about a
minute of your time.
4. *Run Software Update. While it runs, don’t use other apps.*
Again, I have no evidence to indicate that this step is actually
useful. Software Update is designed to allow you to run it in the
background — you can surf the web with Safari even while Software
Update is installing an updated version of Safari. But, why take a
chance? I log in, I start Software Update, and I don’t do anything
else until it finishes.
5. *As soon as Software Update is done, restart.*


## Zeldman’s Tips


Zeldman’s pre-installation steps:


> Delete old font caches using [DeepSix](http://versiontracker.com/dyn/moreinfo/macosx/21905) or a similar tool. (I like
> [Font Cache Expunger](http://www.elara.com/), but the manufacturer of that free tool
> appears to be in transition.)


This is the first I’ve heard about any problems related to “font
caches”, and, judging from the product description, they seem to
mostly affect apps from Adobe, Macromedia, and Microsoft. Even if it’s
unnecessary voodoo, it’s likely harmless voodoo — the only downside
is the time it takes to rebuild the caches.


> Use [Cocktail’s](http://www.macosxcocktail.com/) Pilot mode to repair permissions, run cron
> scripts, prebind the system, and clean system, user, and internet
> caches. Set Pilot to restart upon finishing its tasks.


Here, I gently disagree. Mac OS X’s “Repair Permissions” feature is a
bit of a misnomer; “Restore Permissions” or “Reset Permissions” would
be a better name. “Repair” makes it sound as though files are broken
if their permissions are affected by this process; that’s not the
case. Files might have perfectly valid permissions but differ from
what’s expected by the Repair Permissions process.


[This Apple Knowledge Base article](http://docs.info.apple.com/article.html?artnum=25751) explains the Repair
Permissions process in detail, but here’s the basic gist:


> Many things you install in Mac OS X are installed from
>  package files (whose filename extension is “.pkg”). Each
>  time something is installed from a package file, a “Bill of
>  Materials” file (whose filename extension is “.bom”) is
>  stored in the package’s receipt file, which is kept in
>  /Library/Receipts/ . If you look in the Receipts folder, for
>  example, you should see all kinds of files that end with
>  .pkg, including some that were created when Mac OS X was
>  installed (for example, BaseSystem.pkg). Don’t worry, these
>  files don’t take up much disk space and you shouldn’t put
>  them in the Trash.
> Each of those “.bom” files contains a list of the files
>  installed by that package, and the proper permissions for
>  each file.
> When you use Disk Utility to verify or repair disk
>  permissions, it reviews each of the .bom files in
>  /Library/Receipts/ and compares its list to the actual
>  permissions on each file listed. If the permissions differ,
>  Disk Utility reports the difference (and corrects them if
>  you use the Repair feature).


However, just because a file’s current permissions differ from its
original permissions as specified in the corresponding ‘.bom’ file,
does not mean that the current permissions are “wrong”. The reason
this feature exists is that sometimes, the permissions *are* wrong,
causing some sort of problem, and running Repair Permissions solves
the problem.


But if you are not experiencing any symptoms that would indicate
permission-related problems, there is no reason to run Repair
Permissions. Repair Permissions is *not* a periodic maintenance task
or a preventive measure. (Although, to be fair to everyone who
thinks that it *is* a periodic maintenance task, some of [Apple’s own
support documentation hints that it is](http://docs.info.apple.com/article.html?artnum=152064).)


In fact, sometimes running Repair Permissions can *create* problems.
In fact, Zeldman himself was bitten by just such a problem earlier
this year, when he upgraded from Jaguar to Panther, [disastrously](http://www.zeldman.com/daily/0404d.shtml), and after recovering and getting Panther successfully running,
[wound up unable to print](http://www.zeldman.com/daily/0404g.shtml#print).


The problem in that case is that when upgrading from Jaguar (10.2) to
Panther (10.3), the Panther installer failed to create several new
user accounts, which were necessary for Panther but didn’t exist under
Jaguar and earlier versions of Mac OS X. The problem wasn’t triggered
until and if you ran Repair Permissions, because files which were
supposed to belong to these new “users” couldn’t be assigned to them
because the users didn’t actually exist.


Bits of harmless voodoo from the days of the old Mac OS included
rebuilding the desktop and zapping the PRAM. *Having problems? Rebuild
the desktop and zap the PRAM.* More often than not, doing these things
wouldn’t solve the problem, but, they didn’t cause any harm, either.
(And, occasionally, they *did* solve actual problems.) Non-technical
Mac users had no idea what these things actually meant, they simply
knew the magic keystrokes to invoke them, and if they were
experiencing problems they didn’t understand, these things were “worth
a shot”.


Mac OS X’s Repair Permissions feature is a modern equivalent. Just
remember that there’s no reason to invoke it unless you’re
experiencing problems; it’s not a preventive measure, and even when
it does make “repairs”, it’s not necessarily a sign that there was
anything wrong.


As for the remainder of the tasks in Cocktail’s “Pilot” mode, they’re
needless as well. Diddling your prebindings before running Software
Update is just wasted time, and those 3:15 am daily cron tasks are
inessential (mostly just cleaning up temporary files and archiving
logs).


Back to Zeldman’s tips:


> Run a full backup.


Yes, absolutely. Ignore this advice only if you don’t care about your data.


> In System Preferences, under Accounts: Startup Items, turn off
> third-party startup items such as Extensis Suitcase, DragThing,
> Default Folder, Ittec, and so on.


This seems like a bit of unnecessary work. Holding down Shift while
logging in temporarily suppresses these items. But Zeldman’s general
idea here is the same as mine: let Software Update run in a pristine
login environment.


> Remove external hard drives from the desktop by dragging their
> icons to the Trash.


Capital idea. There’s no downside, and it avoids any chance that you
might lose data on those volumes as a result of bugs in the installer
scripts.


> It is now safe to open System Preferences, download OS X 10.3.7
> update and run the installer. Hit RESTART when prompted to do so
> after the software finishes installing itself.


I’ll just note that beginning with Panther, you can invoke Software
Update from the Apple menu at any time.


Here are Zeldman’s post-installation steps:


> Delete font caches again.


As stated before, I’m unfamiliar with this entire issue of problematic
font caches, so take the following with a grain of untested salt:
re-deleting these caches is harmless, but probably unnecessary if you
also deleted them immediately prior to running Software Update.


> Use Cocktail’s Pilot mode to once again repair permissions, run
> cron scripts, prebind the system, and clean system, user, and
> internet caches, and so on. Let Cocktail restart the computer
> after these tasks have been performed..


All needless. After running Software Update, your prebindings should
be up-to-date — that’s what happens during the “Optimizing System
Performance” update stage that takes so much time. Doing this again
now is like taking a shower after taking a shower.


> Slowly bring back third-party startup items.


I can’t think of a good reason to do this slowly — I just log in
normally, and let my login items launch as usual. Only if I
encounter a problem during login would I consider enabling my login
items one at a time to identify conflicts. Remember that you can
always hold down the Shift key while logging in to suppress all login
startup items — so you should never find yourself in a situation where
a startup item gone bad prevents you from being able to log in.


> After working with the Mac for a while without experiencing
> problems, run another full backup.


More good advice (so long as you’re not so foolish as to replace your
pre-update backup with the post-update backup — keep them both, just
in case a problem pops up after your post-installation backup.).



| **Previous:** | [Markdown Licensing](https://daringfireball.net/2004/12/markdown_licensing) |
| **Next:** | [Apple to Announce ‘iWork’ Office Suite?](https://daringfireball.net/2005/01/iwork) |


PreviousNext