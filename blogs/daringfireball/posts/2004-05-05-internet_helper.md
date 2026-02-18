---
title: "Fixing Corrupt Preferences for Default Internet Helpers"
date: 2004-05-05
url: https://daringfireball.net/2004/05/internet_helper
slug: internet_helper
word_count: 1471
---


## The Problem


My preferred default FTP client is [Interarchy](http://www.interarchy.com/). I switched about two
months ago, after the release of Interarchy 7.


Last week, however, at some point shortly after upgrading to
Interarchy 7.1.1, the setting for my preferred FTP client became
unset, and, worse, I was unable to reset it to point to Interarchy.
I could set it to point to any other FTP client, just not
Interarchy, the one I wanted to set it to. My other helper app
preferences — for my email client and web browser — were
unaffected.


It was just my FTP helper, and it was only blocking me from setting it
to Interarchy.


Being that it was specific to Interarchy, I of course suspected that
either (a) there was some sort of bug in Interarchy 7.1.1; or (b) my
copy of Interarchy had somehow become corrupted; or (c) my
Interarchy preferences had somehow become corrupted (which, if true,
might be a manifestation of (a), of course, but that’s not a
distinction worth worrying about here).


But none of those were the source of my problem, because: (a) no
other Interarchy 7 users seem to have the problem; (b) I
re-downloaded and re-installed Interarchy 7.1.1, and also tried
reverting to Interarchy 7.0, neither of which helped; and (c) I
archived and removed my existing Interarchy preferences, letting
Interarchy create fresh ones, but to no avail.


Thus, even though it was specific to Interarchy, the problem seemed
to be with my Internet Config preferences.


## Brief Interpolation on the History of Internet Config (Feel Free to Skip This Entire Section if You’re a Long-Time Mac User or if You’ve Arrived Here via Google and Are Just Looking for the Solution to the Same Problem I Had)


[Internet Config](http://www.quinn.echidna.id.au/Quinn/Config/) provides a group of system-wide preferences
for Internet-related stuff. You can specify default helper apps for
different tasks — email, FTP, web browsing, Usenet — as well as
helpers for specific protocols like ‘http:’, ‘afp:’, ‘gopher:’, etc. (These
protocols aren’t even necessarily Internet-related; for example, Mac
OS X’s Help Viewer is the default handler for the ‘help:’ protocol.)


In older versions of Mac OS X, you could change some of these
settings via the Internet panel in System Preferences. Before that,
on Mac OS 8 and 9, you used the Internet Control Panel. And back in
System 7, you used the Internet Config application, which is where
it started.


Internet Config wasn’t invented by Apple. It was designed,
implemented, and released for free by Quinn “The Eskimo!” and Peter
N Lewis. It was useful, popular, and widely supported by the
developers of Internet client software for the Mac. Thus, Apple
adopted it and rolled into the system.


On Panther, however, the Internet System Preferences panel is no
more. The only way to see these prefs using software that ships with
Panther is to use Internet Explorer. (IE not only provides a UI to
modify these system-wide Internet Config settings, but it also
stores its own IE-specific private preferences inside the Internet
Config preferences. This always struck me as a very odd decision on
the part of IE’s engineers.)


Now that the Internet System Prefs panel is gone, it’s up to
individual applications to provide a way to set default protocol
handlers. Thus, Safari and Apple Mail provide preferences to specify
default apps for web and email. It is a bit weird to have to open
Safari to tell the system that you’d rather use FireFox.


Third-party developers are forging ahead, however. Mailsmith, for
example, now provides a button in its preferences window to set it
as the default email client, obviating the need to do so via Apple
Mail. And given that the author of Interarchy is Peter N Lewis —
co-inventor of Internet Config — it’s not surprising that
Interarchy 7’s preferences window allows you to specify it as the
default FTP client.


## The Symptoms


After the problem started, each time I launched Interarchy, it would
prompt me with a dialog asking if I’d like to use Interarchy as the
default FTP client. I’d click Yes, quit, relaunch, and but it would
ask me again.


You can change this setting at any time using a checkbox in
Interarchy’s prefs, “Use Interarchy for FTP”. Every time I opened
Interarchy’s prefs window, this checkbox was *un*checked. Check it,
close prefs, open prefs, and it’d be unchecked again.


The preference simply could not be set.


Although Apple has eliminated the Internet System Preferences panel,
it hasn’t eliminated the underlying Internet Config preferences
themselves. The OS just no longer offers a user interface to see and
change them. One solution, as mentioned above, is to use Internet
Explorer.


A better option is to use third-party software. [Alexander Clauss’s
MisFox](http://www.clauss-net.de/misfox/misfox.html) is a free application that allows you to see and change
all of the important Internet Config settings: default apps, file
mappings, and protocol helpers. (Clauss is the author of [iCab](http://www.icab.de/).)


But I couldn’t set my default FTP app to Interarchy using MisFox,
either. Same for Monkeyfood’s [More Internet](http://www.monkeyfood.com/software/MoreInternet/), a free System
Preferences panel that lets you edit and change Internet Config’s
protocol mappings. It was by using these tools that I determined
that my problem affected only Interarchy, and not other FTP clients
such as [Transmit](http://panic.com/transmit/) or [Fetch](http://www.fetchsoftworks.com/).


## The Solution


Although I hadn’t yet found the source of the problem, I had at
least eliminated some suspsects. It was not the Interarchy
application. It wasn’t Interarchy’s prefs data.


Plus, since I saw the same problem using MisFox and More Internet, I
figured it must be some sort of corruption in the file — or files
— that store my Internet Config settings. But what and where are
those files? The only obvious one is “com.apple.internetconfig.plist”.
The name is a giveaway, and the modification date changes when
you make changes to Internet Config settings.


Sadly, trashing this file — then immediately logging out and
logging back in — did not help. All my Internet Config prefs were
reset to factory settings, but I still could not assign Interarchy
as my default FTP app.


I found no other file in my home folder that had a name containing
“internet” and “config”, or a modification date that changed upon
making changes to Internet Config settings.


At this point, I was stuck. I was fairly certain that there were one
or more other files where the system was storing Internet Config
data, and that those files were in some way corrupt, but I had no
more guesses left as to where those files may be. Of course I tried
searching for a solution via Google, but found nothing. You know
you’re in deep shit when Google doesn’t have the answer to a
troubleshooting issue.


Then, I asked Rich Siegel, who suggested that the problem might be
related to [Launch Services](http://developer.apple.com/technotes/tn/tn2017.html). That sounded like a promising
idea, and in fact proved correct.


Here’s what I did:

1. I started by logging out and logging back in, holding down the
Shift key to suppress my normal login items.
2. I opened Terminal, and typed:
`cd /Library/Caches/
`
That’s the root-level Library folder, *not* the Library
folder in your home folder.
3. To delete the Launch Services cache files, I typed:
`sudo rm com.apple.LaunchServices*
`
4. I authenticated with my password.
5. I immediately restarted the machine.


This fixed the problem — albeit at the expense of deleting all of
my existing Launch Services preferences, which includes the mappings
that bind filename extensions to default applications. A minor
irritation, but certainly not a big deal.


I doubt that step #1 is necessary, but I didn’t want to take any
chances by deleting the Launch Services files while other
applications were running. It’s also possible that I could have
simply logged out and logged back instead of restarting at step #5;
but once again, why take a chance?


In hindsight, it’s easy to draw the connection between Launch
Services and Internet Config. E.g., [Apple’s developer introduction
for Internet Config](http://developer.apple.com/documentation/Carbon/Reference/Internet_Config/internet_config_ref/Introduction.html) states:


> Internet Config, a Mac OS 8 and 9 API, supports centralized entry
> and management of Internet preferences for all of a user’s Internet
> applications. For example, email programs and Web browsers can
> obtain a user’s name, email address, home page, incoming mail
> server, and similar preferences from one common place that is easily
> edited by the user via the Internet Config application.
> Mac OS X applications should employ Launch Services and System
> Configuration for managing Internet preferences. In Mac OS X,
> Internet Config calls through to these newer APIs. Using them
> directly increases your application’s efficiency.



| **Previous:** | [Just a Bunch of Links, but They’re Good Links, I Swear](https://daringfireball.net/2004/05/just_links) |
| **Next:** | [What to Do When Your Energy Saver Prefs Panel Won’t Load](https://daringfireball.net/2004/05/energy_saver) |


PreviousNext