---
title: "Misregistered"
date: 2004-06-08
url: https://daringfireball.net/2004/06/misregistered
slug: misregistered
word_count: 941
---


Never one to let actual research or reporting get in the way of a
good story, The Register’s Tony Smith published an [article about
yesterday’s security update](http://www.theregister.co.uk/2004/06/08/apple_os_x_patch/), in which he alleges that the
update does *not* block the [example exploits](http://www.unsanity.com/haxies/pa/whitepaper) published by
Unsanity:


> We installed the update on a Mac OS X 10.3.4 machine. After
> restarting the machine, we went straight to Unsanity’s web
> site, the [location of a pair of web pages that test the URI
> vulnerability](http://www.theregister.co.uk/2004/06/08/apple_os_x_patch/). Neither tests was blocked by the update,
> details of which can be found [here](http://docs.info.apple.com/article.html?artnum=61798).
> […]
> Unlike Paranoid Android, the code contained in the update
> remembers applications the user has permitted other
> applications to open, or those that the user has opened
> themselves. So it’s possible that the system is allowing
> access to the test site apps because they have already been
> run prior to the installation of the update.


In fact, this is exactly what is going on. The new confirmation
dialog that Launch Services presents to prevent unknown applications
from being launched automatically will only be presented for, well,
*unknown* applications.


In other words, any application that you’ve previously launched is
implicitly trusted by Launch Services. This includes the example
exploit applications at Unsanity and [http://test.doit.wisc.edu/](http://test.doit.wisc.edu/).
So if you previously tried these example exploits without disabling
the URI protocols they take advantage of, then these examples will
*still* work after installing Security Update 2004-06-07.


To be clear: Security Update 2004-06-07 blocks these example
exploits in exactly the way it is supposed to.


The inner workings of Launch Services are not documented publicly.
However, it’s clear that Launch Services has always kept track of
applications that have been launched. The tracking of
previously-launched apps is not new; what’s new is that Launch
Services will no longer automatically launch never-before-launched
apps without confirmation.


Here’s how I tested this. I have three Macs here, one of which is an
older iMac used for testing. That’s the machine I previously used to
test example exploits at the aforelinked sites. After installing
Security Update 2004-06-07 on this iMac, the example exploits still
worked.


I immediately suspected that the problem was that Launch Services
“remembered” those apps. Apple does not document where the Launch
Services database is stored on disk, but I deleted the following
files:

- `/Library/Caches/com.apple.LaunchServices.6B.csstore`
- `/Users/gruber/Library/Caches/com.apple.LaunchServices.UserCache.csstore`


I then restarted the machine. (I believe, but am not sure, that you
can’t just log out/in; you need to restart to nuke these files. And,
sometimes, the cache file gets written back to the disk after you
delete it but before the Mac restarts. I think this is because the
“live” Launch Services database is not stored on disk, but rather in
memory, and the above files are, as their pathnames indicate, merely
*caches* of this info. I.e. sometimes the old Launch Services
database will get rewritten to the cache file before you restart.
Sorry for all the wavering vagueness here in this parenthetical;
suffice it to say that Launch Services is more or less a black box,
but you *can* delete your existing LS database by deleting these
files and restarting, it’s just that sometimes, in my experience, it
doesn’t take.)


At this point, after deleting the LS caches and restarting, the
example exploits no longer worked on the iMac. On the other two Macs
here, neither of which had ever executed the example exploit apps,
Security Update 2004-06-07 blocked the exploits as advertised.


**Note:** I am *not* advising you to delete your Launch Services
cache files. Doing so will almost certainly do you no good
whatsoever.


Smith continues:


> The same site provides Paranoid Android, a utility that
> halts attempts to open apps from URIs and offers the user
> the choice of proceeding with the attempt or to cancel it.


That’s not what Paranoid Android does. Paranoid Android prevents all
“untrusted” URI protocols from working without confirmation,
including protocols which have nothing to do with the launching of
applications.


> Security Update 2004-06-07 does the same thing, but on our
> system it failed to do so.


Security Update 2004-06-07 is not at all like Paranoid Android.
Paranoid Android takes sweeping measures, by default, blocking all
URIs other than ‘http’, ‘https’, and ‘mailto’. Security Update
2004-06-07, on the other hand, makes a surgically precise
modification to the previous (vulnerable) behavior of Launch
Services: it *only* kicks in when Launch Services has been asked to
automatically launch a never-before-launched application.


> Users who prefer a ‘belts and braces’ approach to security
> may wish to stick with Paranoid Android, but we’d certainly
> recommend installing the new update in any case.


Bad advice. Even Unsanity agrees that [Paranoid Android is
obsoleted](http://www.unsanity.com/haxies/pa) by Security Update 2004-06-07:


> UPDATE: Security Update 2004-06-07 fixes the issues
> Paranoid Android was created to address. After installing
> the Security Update, you can safely uninstall Paranoid
> Android.


Of course, Unsanity doesn’t tell you *how* to uninstall Paranoid
Android. (The Uninstall button in their installer only removes the
Paranoid Android haxie module; it doesn’t remove any of the
Application Enhancer detritus spread across your top-level
`/Library` and `/System` folders (you did know that Application
Enhancer installs a bundle within your `/System` folder, right?).
Anyway, after running the uninstall command in the Paranoid Android
installer, you can uninstall the rest of the Application Enhancer
software using the Uninstall button in the Information tab of the
APE Manager panel in System Prefs). But you shouldn’t have to worry
about that, because you [didn’t install Paranoid Android](https://daringfireball.net/2004/05/help_viewer_security_update).



| **Previous:** | [Security Update](https://daringfireball.net/2004/06/security_update) |
| **Next:** | [So Witty](https://daringfireball.net/2004/06/so_witty) |


PreviousNext