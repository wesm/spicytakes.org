---
title: "Smart Crash Reports Addenda"
date: 2006-02-13
url: https://daringfireball.net/2006/02/scr_addenda
slug: scr_addenda
word_count: 1108
---


## Regarding the Permissions of the InputManagers Folder


The number one question from readers regarding my [Smart Crash
Reports missive](http://daringfireball.net/2006/01/smart_crash_reports) two weeks ago was, more or less, “I had no
idea that any app can install an input manager without permission,
and that these input managers load into every running application —
isn’t this a serious security hole waiting to be exploited?”


In short, no, not really. But that doesn’t mean the situation is
good.


It’s not a security hole, per se, but rather just one of many routes
a malicious application could take if it wanted to do something bad.
Once you launch an application, it can pretty much do *anything* it
wants within the confines of your home folder: read your mailboxes,
delete the contents of your Documents folder, and, yes,
surreptitiously add items to your InputManagers folder. But an app
can just as easily add items to any sub-folder in your Library
folder, including other code resource plug-ins like QuickTime
components, OSA scripting additions, (a.k.a. OSAXen), and contextual
menu items.


Any of these items could be used for nefarious purposes just as
easily as input managers — and any of them could be installed by
any running application at any time.


*Could* being the operative word. The expected behavior of any
application that wants to install any system-wide extension is that
it should ask permission first; apps that behave otherwise should be
shunned. But the system doesn’t enforce this, and I’m not sure it
could, other than to change the ownership or permissions on these
folders such that even administrator users would have to
authenticate before adding items to them. That may well be “safer”,
but it’s also more complex; the ownership and permissions of all
folders within your home folder have always been nice and simple on
Mac OS X: you own them, and you can read and write to any of them.


There are so many bad things a malicious app can do once it’s
running that it’d be nearly impossible to defend against them all,
individually; the best and only defense is not to launch software
you don’t trust. (And, of course, to back up regularly to a drive
that you don’t keep mounted all the time.)


One thought that occurred to me was that Apple should definitely
suppress the loading of any invisible items in the magic
auto-loading code extension folders. An app with deeply nefarious
intentions should not be able to install, say, an input manager
*and* make it invisible so that it doesn’t appear in the Finder.


I did a cursory investigation, and there’s good news and bad news:

- **Good:** Input managers whose names begin with a dot — the
traditional Unix way of marking a file “invisible” — are not
loaded.
- **Bad:** Input managers whose HFS invisible bit is set — the
real Mac way of marking a file invisible — *are* loaded.


This seems like an oversight, if not a bug. If it’s a good idea to
suppress some “invisible” input managers, the system should suppress
them all. And I can’t think of a single legitimate reason why anyone
would want invisible input managers (or contextual menu items,
QuickTime components, or scripting additions) to load.


If you’re worried about input managers being installed behind your
back, [this clever comment](http://macslash.org/comments.pl?sid=5966&cid=105831) on MacSlash offers instructions on
using Folder Actions to get a notification every time an item is
added to your InputManagers folder. (Even this isn’t bullet-proof
protection — a deeply clever malicious input manager could suppress
Folder Actions from firing.)


## Smart Crash Reports 1.1b1


Unsanity’s Slava Karpenko, lead developer of Smart Crash Reports,
has announced that the next release of Smart Crash Reports, in
public beta at this writing, [will no longer offer the silent
installation feature](http://www.unsanity.org/archives/000447.php). Instead, it now prompts the user with a
dialog box asking for permission. The dialog reads:


> **Would you like to install Smart Crash Reports?**
> Smart Crash Reports helps improve software by notifying its
> developers of problems when they happen. Participation is voluntary,
> but your support helps make our software better. For more
> information, visit http://smartcrashreports.com/.


This is a welcome change, and addresses my main argument directly:  system-wide extensions should never be installed without the user’s permission.


I would argue, however, that Unsanity’s description of Smart Crash
Reports, both in the dialog box on their web site, does not make
clear just what exactly it is: an input manager bundle installed in
*~/Library/InputManagers/*. Simple “how to uninstall” instructions
in the Smart Crash Reports [FAQ](http://www.unsanity.com/support?product=smartcrashreports) would do the trick.


## Apple’s Advice to Developers Who Want to See Their Own Crash Reports


From [Apple’s Technical Note TN2123](http://developer.apple.com/technotes/tn2004/tn2123.html):


> There is currently no way for third party developers to access the 
> reports submitted via CrashReporter. Apple is aware that there is 
> strong demand for such a facility (r. 3356232). Regardless, your 
> users can still submit crash logs to you manually. Moreover, 
> there’s no reason why your application couldn’t look at its crash 
> log on each launch and, if it has changed, ask the user whether 
> they want to submit it to your bug tracking system.


This is pretty much the same advice I offered, and many developers
do just this. (Apple certainly doesn’t recommend using an input
manager hack to modify the system’s Crash Reporter at runtime.)


## BugReporter


[Zonic’s BugReporter](http://www.zonic.co.uk/products/bugreporter/) is self-contained crash reporter available
to developers for a very low price ($50 for a single product, $100
for unlimited products; neither license has any restrictions unit
sales). From Zonic’s web page:


> BugReporter is a developer tool that allows applications to
> automatically invoke a bug-reporting system in the event of a
> crash.
> The BugReporter API is a simple “C” interface, providing maximum
> compatibility with development environments such as Carbon or
> Cocoa.
> It is distributed as a stand-alone library, and requires no
> additional resources, frameworks, or bundles. It can be invoked
> from both CFM or Mach-O applications, packaged in either
> single-file or bundled form.
> BugReporter allows bug reports to be submitted through email or
> over the web, enabling you to pass bug reports directly from an
> end user’s desktop to your internal support systems.


Plus, it’s a universal binary and supports both Xcode and
CodeWarrior. It’s used by apps like [GraphicConverter](http://www.graphicconverter.net/) and TLA
Systems’ [PCalc](http://pcalc.com/) and [DragThing](http://dragthing.com/).


## Adium


Lastly, developers who are worried about turning users off with
crash reporting dialog boxes should consider [Adium](http://adiumx.com/), whose built-in
crash reporter conveys a bit of crash-and-burn humor:



| **Previous:** | [Bedecked](https://daringfireball.net/2006/02/bedecked) |
| **Next:** | [Joyeur](https://daringfireball.net/2006/02/joyeur) |


PreviousNext