---
title: "Font Caches Gone Wild"
date: 2005-03-25
url: https://daringfireball.net/2005/03/font_caches_gone_wild
slug: font_caches_gone_wild
word_count: 1312
---


Thanks to a veritable avalanche of email regarding Monday’s [piece
on login delays caused by damaged font caches](https://daringfireball.net/2005/03/font_caches), I think I have
a pretty good idea what’s going on.


One thing I know is that it wasn’t just me — an awful lot of people
have been [stricken with this problem](http://discussions.info.apple.com/webx?14@11.BGeWalwgT7i.0@.68aa4cfd), and in some cases, it
was nearly crippling. One reader reported finding over 1 *gigabyte*
of “fontTablesAnnex” files in `/System/Library/Caches/`; and in
terms of login delays, [designer Cameron Moll](http://www.cameronmoll.com/) reported that
his login time had grown to *14 minutes*.


This is, clearly, a bug in Mac OS X 10.3.  Specifically, it’s a bug in
version 1.8.5 of the ATS framework.1
 Recall from Monday that “ATS” stands for “Apple Type Solution”
(although several readers seconded my suspicion that it previously
stood for “Apple Type Services”; regardless, all you need to know for
this discussion is that ATS is the Mac OS X subsystem that handles
fonts).


Version 1.8.5 shipped as part of the [Mac OS X 10.3.6](http://docs.info.apple.com/article.html?artnum=300080) update, the
release notes for which mention several font-related bugs that were
addressed in that release. So my guess is that *this* bug — where the
“fontTablesAnnex” caches grow without bound, leading to severe login
delays — was introduced as a side-effect of one of the bug fixes for
ATS.framework in 10.3.6.2


10.3.6 was released in October, and that gibes with my suspicion
that this is when the bug was introduced. It’s not a bug where
*boom*, you’re hit and logging into your account suddenly takes a
minute or longer. These font caches grow endlessly, but they tend to
grow slowly, and so the adverse effects tend to sneak up on you. I
began to suspect something was wrong around December; by February, I
was highly annoyed.


ATS.framework has not changed in either 10.3.7 or 10.3.8; version
1.8.5 is still current, and thus, the bug is still present.


Most users haven’t been affected by this bug, or if they have been,
it hasn’t been severe. I believe, but can’t prove, that the reason
for this is that the bug is only triggered if you have PostScript
fonts installed, or perhaps, *certain* kinds of PostScript fonts.


I believe this because:

1. Everyone who has written to me to say they too were hit by
this bug has reported having at least several PostScript fonts
installed.
2. Everyone I know who hasn’t been hit — no large font cache
files, no delays when logging in to their accounts — has no
PostScript fonts installed.


Group #2 includes everyone who runs with the stock set of fonts that
ship with the system from Apple — Apple only ships TrueType fonts.


I’d be interested to hear from anyone who can contradict either of
these suppositions; i.e. if you’ve been hit by this bug but have no
PostScript fonts installed, or if you have many PostScript fonts
installed in the system’s font folders, but haven’t been hit by the
bug.


This is not to say there’s anything wrong with PostScript fonts. Or,
if you’ve been hit, that there’s anything damaged or corrupt with
*your* PostScript font files. This is a bug in Mac OS X, plain and
simple.


My suspicion that the bug was introduced in 10.3.6 is further backed
by the investigative work of Arton Ragsdale, who sent me this report
by email:


> The problem with ATSServer and the font caches is both old and new.
> I have experienced many variable problems throughout the life of OS
> X, particularly 10.3, that were easily solved by erasing font
> caches (repeatedly as various problems reappeared).  I know you’ve
> always thought this was nonsense, but I can assure you it is not.
> It generally got better [through] 10.3.5, which seemed to clear up
> most of the problems.
> The 10.3.6 update however, brought with it a new version of
> ATS.framework updating version 1.8.4 to 1.8.5.  The major change in
> this update, which has yet to be addressed, is the behavior of
> scanning every single font in any of the three font folders
> (`/System/Library/Fonts/`, `/Library/Fonts/`, and
> `~/Library/Fonts/`) regardless of whether they are activated or
> not.  This takes an extremely long time if you have a large number
> of fonts.
> The computers I set up have about 500 fonts and many of them
> are quite old and of various types, which I believe adds to the
> problem.  I came to this conclusion by using a similar
> troubleshooting technique to the one you mentioned, using ssh
> to access the computer while it logged in.  But in addition to
> using `top` to narrow down the problem to ATSServer, I used
> `fs_usage` to find out exactly which processes were accessing
> which files.3  I discovered
> ATSServer accessing every single font on the computer.
> My solution to the problem is one of your big pet peeves, I
> replaced the ATS.framework hidden in
> `/System/Library/Frameworks/ApplicationServices.framework/Versions/
> A/Frameworks/ATS.framework` with the older version from 10.3.5. 
> Not the most elegant solution, but it has worked smoothly on 30 G5s
> loaded with all different kinds of graphics apps and I can keep the
> fonts where they belong, in the fonts folder.  It has worked with
> every version released since 10.3.6 but I wouldn’t recommend it to
> anyone who doesn’t use many fonts.


Arton’s investigation was thorough, and but he’s also correct that I
absolutely cannot endorse his solution of replacing version 1.8.5 of
ATS.framework with version 1.8.4 from Mac OS X 10.3.5. That it
worked for him is proof that it’s a bug in version 1.8.5 that is
causing these problems; that doesn’t mean replacing OS components
with versions from previous OS updates is a wise idea.


## My Advice


Better is to wait for Apple to fix the bug, as I believe they will
in Mac OS X 10.3.9 (and, one would hope, also in 10.4). For one
thing, this is a severe bug. For another, even though it isn’t
hitting everyone, it’s hitting a large number of users, and
designers in particular. Designers are the hardest-hit demographic
simply because they almost invariably have numerous PostScript fonts
installed (and conversely, non-designers are less likely to
install any PostScript fonts).


I have no first-hand knowledge that there will even *be* a 10.3.9
release, but the rumor mill says it’s imminent. Included in the
release notes for the latest build released to developers, as
reported by [MacRumors.com](http://www.macrumors.com/pages/2005/03/20050322220911.shtml), is this item:


> updated font management


And according to some site called [Think Secret](http://www.thinksecret.com/news/0503seeds.html):


> Mac OS X 10.3.9 will deliver dozens of other fixes and improvements
> when it is released, including improved startup times on systems with
> many fonts, FireWire audio performance fixes, an updated Kernel,
> improvements when waking from sleep, and more.


(I believe where Think Secret says “startup”, they mean “login”,
although perhaps these caching problems affect both startup and
login times.)


In the meantime, I believe this bug can be managed manually by
keeping an eye on the size of your font caches. If your
“fontTablesAnnex” files seem unduly large, or if the time it takes you
to log in seems unduly long, trash your font caches and restart.


**Update 17 April**: [10.3.9 is out](http://docs.info.apple.com/article.html?artnum=300966), and the fix is in:


> Addresses an issue in which the startup time in Mac OS X
> 10.3.6 through 10.3.8 may be extended if a large number of
> PostScript fonts are installed.


---

1. `/System/Library/Frameworks/ApplicationServices.framework/
Versions/A/Frameworks/ATS.framework`
↩︎
2. Feel free to substitute “issue” for “bug” if you prefer the euphemistic parlance of Apple’s release notes.
↩︎
3. Jonathan Rentzsch’s “[fs_usage Intro](http://rentzsch.com/macosx/fs_usageIntro)” is a terrific overview/introduction to the `fs_usage` tool.
↩︎



| **Previous:** | [Login Delays and Damaged Font Caches on Mac OS X 10.3](https://daringfireball.net/2005/03/font_caches) |
| **Next:** | [Caching Out](https://daringfireball.net/2005/03/caching_out) |


PreviousNext