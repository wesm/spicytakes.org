---
title: "Miscellaneous Updates/Corrections, Several of Which Aren’t Substantial Enough to Constitute a Full Article by Themselves, but Which Were Assembled Together Mainly as an Excuse to Use This Preposterously Long Title"
date: 2005-01-26
url: https://daringfireball.net/2005/01/misc_updates
slug: misc_updates
word_count: 1551
---


## Software Update Update


At the end of December, I wrote “[Software Update Tips and Voodoo](https://daringfireball.net/2004/12/software_update)”,
a look at my own procedures and recommendations for installing Mac OS X
system and security updates. I got a ton of feedback, but two main
points stood out.


First, many people objected to my description of Mac OS X’s Repair
Permissions feature. I wrote:


> But if you are not experiencing any symptoms that would
> indicate permission-related problems, there is no reason to run
> Repair Permissions. Repair Permissions is *not* a periodic
> maintenance task or a preventive measure. (Although, to be
> fair to everyone who thinks that it *is* a periodic maintenance
> task, some of [Apple’s own support documentation hints that it
> is](http://docs.info.apple.com/article.html?artnum=152064).)


The gist of the feedback is that many people *do* run it as a periodic
maintenance task, and believe they’re better off for doing so. And
conversely, that even if it’s unnecessary, it’s a do-no-harm sort of
thing.


I still stand behind my original advice, that Repair Permissions is
something you should turn to as a troubleshooting tool, but many of you
disagree. For those of you who report that Repair Permissions frequently
turns up files with incorrect permissions, however, I suspect it’s a
sign of some deeper problem with your Mac OS X installation. File
permissions and ownership don’t have a half-life — they don’t rot or
“go bad” or even change over time. If they’ve changed, some software had
to have changed them.


Of course, the reason people tend to run Repair Permissions immediately
after installing system and security updates is that installers are the
software most likely to modify these file attributes. It’s anecdotal
evidence at best, but for what it’s worth, I have two Macs on which I’ve
*never* run Repair Permissions, which have been updated with every system
and security update over the last two years, and which exhibit no
permission/ownership-related problems whatsoever.


But if you feel better running Repair Permissions after every update
installation, I don’t think there’s any harm in it.


Second, a number of people wrote to endorse the use of “combo” updaters
instead of the “delta” updaters used by Software Update. In a nut, the
delta updaters are smaller in size — for example, only containing the
files necessary to update a 10.3.6 installation to 10.3.7. The combo
updaters are larger, and can update any version of the current OS; e.g.
the 10.3.7 combo updater can update any version of Panther from
10.3.0 through 10.3.6.


The difference in size is significant. The [10.3.7 delta updater](http://www.apple.com/support/downloads/macosxupdate_10_3_7.html) is
26 MB; the [10.3.7 combo updater](http://www.apple.com/support/downloads/macosxcombinedupdate_10_3_7.html) is 97 MB.


Ostensibly, there should be no effective difference between using the
delta and combo updaters. If you start with two identical systems with
fresh 10.3.0 installations, and update the first machine using each of
the 10.3.x delta updaters, and update the second using the 10.3.7 combo
updater, the two machines should wind up with identical 10.3.7
installations.


If you use Software Update, it tries to automatically determine which
updater you need. If you’re currently running 10.3.6, Software Update
will use the delta installer to update your system to 10.3.7; if you’re
running 10.3.5 or earlier, it will use the combo updater. Thus if you
run Software Update regularly, your system will be updated using the
delta installers. If you’ve missed an update or two, or if you’ve
reinstalled 10.3.0 from scratch, Software Update will use the combo
installer.


In short, if you use Software Update — and I recommend that you do —
the Right Thing should just happen. You shouldn’t need to worry or even
know about the combo/delta distinction.


However, a vocal minority of users swear by the use of combo updaters.
The idea being that there are occasional problems caused by the delta
updaters, which problems can be avoided by using combo updaters. After
every system update, sites such as [MacFixIt](http://macfixit.com/) and [MacInTouch](http://macintouch.com/) publish reports from readers claiming that update problems were
fixed after running the combo updater.


The downside to using combo updaters for each update is inconvenience —
you need to download standalone installers and run them manually, rather
than relying on Software Update. But there’s certainly no harm in doing
so.


However, I don’t think it’s necessary. I use Software Update for all the
machines in the house, and the delta updaters have never caused a
problem. Again, I’m not arguing that the three active Macs here at
Daring Fireball HQ constitute a statistically significant sample size,
but my guess is that most of the people who run into problems with delta
updaters have diddled with files they ought not have diddled.


For example, MacFixIt and MacInTouch readers often report successfully
mixing and matching components from different revisions of the OS. Like
if there’s a bug, or supposed bug, related to some specific area in the
current OS, readers will report successfully replacing one or more
current system components with the same components from the previous
(non-buggy) OS revision. Or vice-versa, reverting to a previous OS
revision but hand-installing one or more components from the new
revision. For example, as part of its 10.3.7 coverage, MacInTouch
published [this report from reader Ken Marks](http://macintouch.com/panreader48.html):


> Following all the usual rules, repair permissions etc., I
> updated a G4 dual 1.25 MHz MDD from 10.3.6 to 10.3.7 using the
> combo updater.
> All went well, with one exception. My startup time increased an
> additional 38 seconds, most of which was represented by a menu
> bar normal in every way except for its color. It was blue. Upon
> completion of startup the menubar [*sic*] turned white and everything
> appeared to function normally.
> I have since returned to 10.3.6 from my backup with the
> exception that I used the ATI extensions from 10.3.7. My
> startup is now back to normal.


This is madness. I’m not denying that this worked for Mr. Marks, but
what he’s ended up with is a completely unsupported system
configuration. I suspect many of the people who encounter problems
with delta updaters have engaged in similar tomfoolery, and it’s no
wonder they encounter problems with subsequent updates. Apple designs
and tests the delta updaters to work against the standard installation
of the previous OS revision — once you’ve started diddling with
system files, all bets are off.


If you ever do encounter an update which contains a bug that you don’t
want to live with, what you should do is revert the entire OS to the
previous revision. This should be easy if you made a complete backup of
your startup volume before applying the update, as I’m sure you did. Or,
reinstall the OS from the installation discs, and then run the combo
updater for the revision you wish to revert to. Mixing and matching
individual files between OS revisions is a recipe for disaster, although
the disaster might not occur immediately.


## Prices Per Megabyte


In “[Small, Cheap, and Without a Display](http://daringfireball.net/2005/01/small_cheap_no_display)”, I wrote:


> This is worth restating: *Megabyte-for-megabyte, the iPod
> Shuffle is cheaper than its competition.* To my memory, this is
> the first product in Apple’s history where this is so.


A number of readers pointed out that this is also true of [Xserve RAID](http://www.apple.com/xserve/raid/), which compares very favorably on a cost-per-megabyte basis to
similar products from other companies. E.g., Ina Fried reported for CNet
News that Oracle is switching to and endorsing Xserve RAID:


> Oracle has identified the Apple product as one of several
> storage systems that would make a good low-cost alternative to
> the types of high-end monolithic storage systems that have
> traditionally been used to store Oracle databases.
> Additionally, Oracle is using the Xserve RAID in its own
> technology department to store e-mail, voice mail and calendar
> information.
> Oracle is using the Xserve RAID for a task once reserved for
> pricier Fibre Channel-based disk arrays. The software giant
> noted in a white paper that the Apple approach was about three
> times lower on a cost-per-megabyte basis.


(Thanks to Jake Seliger for the link.)


## The Other New ‘Dashboard’


Back in October, in the midst of a series of articles on Apple’s
various appearance themes in use on Mac OS X, I [mentioned a new one](https://daringfireball.net/2004/10/themes#motion-dashboard):


> Motion even goes so far as to offer yet another set of controls for use
> in [special palette windows which are called “dashboards”](http://www.apple.com/motion/workflow.html) (which
> term is likely to cause confusion when 10.4 ships, with its [Dashboard](http://www.apple.com/macosx/tiger/dashboard.html) desktop widgetry feature). It’s a Darth-Vaderish sort of thing:


This theme is no longer unique to Motion. Take a look at Apple’s
[screenshots displaying the new editing features in iPhoto 5](http://www.apple.com/ilife/iphoto/edit.html), and
you’ll see it there, too. This would appear to be Apple’s new, uh,
*standard* appearance for editing palettes for graphics-editing
software.


Leaving aside any arguments related to the aesthetic appeal of this UI or
the wisdom of introducing yet another Apple-sanctioned look-and-feel, I
really can’t believe Apple is referring to these tools as “dashboards”.
It’s not that the word doesn’t fit, but that it’s already being used for
the new [floating widget layer](http://www.apple.com/macosx/tiger/dashboard.html) in 10.4.



| **Previous:** | [Small, Cheap, and Without a Display](https://daringfireball.net/2005/01/small_cheap_no_display) |
| **Next:** | [Promotional Consideration](https://daringfireball.net/2005/01/promotional_consideration) |


PreviousNext