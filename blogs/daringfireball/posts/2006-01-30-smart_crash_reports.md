---
title: "Smart Crash Reports"
date: 2006-01-30
url: https://daringfireball.net/2006/01/smart_crash_reports
slug: smart_crash_reports
word_count: 5163
---


## Crash Logs and Apple’s Crash Reporter


Crash Reporter is an application that ships as part of the Mac OS X
system (*/System/Library/CoreServices/Crash Reporter.app*), and which
works in conjunction with an invisible background process named
“crashreporterd”.1  crashreporterd
sits around waiting for an app to crash, any app, and when one does,
it launches Crash Reporter, which in turn displays the familiar dialog
box showing you the stack trace of the process that just crashed,
along with a text field in which you can describe what you were doing
before the crash.


To the untrained eye, a stack trace looks like a bunch of hexadecimal
numbers and some programming source code tokens. To a seasoned Mac
developer, a stack trace is like a fingerprint-covered weapon left at
the scene of a crime. Not every crash report is useful, but sometimes
a single crash report is all a developer needs to pinpoint a bug.


Crash Reporter only sends these crash reports to Apple, and Apple
doesn’t share them (at least not officially). So even if it’s some
third-party developer’s app that crashed, the report goes to Apple,
not the developer of the application. Users can, however, submit crash
reports to developers manually; crash reports are automatically
written to log files in *~/Library/Logs/CrashReporter*.


Sending good bug reports to developers is not hard. You go to the
aforementioned CrashReporter logs folder,2 you select the log for the app that
just crashed, and you email it to the developer along with a
description of what you were doing when the crash occurred, or, if you
can reproduce the crash, precisely describe how to do so.


Like I said, not hard at all. However, even though it isn’t difficult,
most users don’t do it. For one thing, the vast majority of users have
no idea about any of this. They’ve never heard of the CrashReporter
logs folder, they don’t know where it is, and they don’t even know
that developers love to be sent crash reports. Also, many users are
under the misconception that third-party developers get access to the
crash reports sent via Apple’s Crash Reporter.


Lastly, even with savvy users who know about these things, there’s
human nature: it may well be easy to send a crash log to your friendly
neighborhood developer, but it’s even easier not to. If it takes more
than one or two clicks, people are going to skip it when they’re busy
or feeling lazy.


Whereas with Apple’s Crash Reporter, you literally just have to click
a button to send a crash log to Cupertino. Since you have to click
something to dismiss the Crash Reporter dialog anyway, it’s almost as
easy to send a report to Apple as it is not to.


So: crash logs are an incredibly helpful debugging aid for developers,
but, because Mac OS X’s built-in Crash Reporter only sends them to
Apple, developers don’t get to see nearly as many of the crash logs
from their software as they would like.


## Unsanity’s Smart Crash Reports


[In September](http://www.unsanity.org/archives/000424.php), Unsanity released [Smart Crash Reports](http://www.unsanity.com/smartcrashreports).
Smart Crash Reports is a combination of some Mac software and a web
service. The Mac software is an input manager extension, which
modifies Apple’s Crash Reporter app to send reports both to Apple
*and* to Unsanity’s web site. The web service allows other Mac
developers to register their software, and to then log in to
Unsanity’s web site to view the crash logs for their software. Smart
Crash Reports also allows developers to have their crash reports sent
directly to their own web site, rather than Unsanity’s.


Smart Crash Reports is offered by Unsanity free of charge, both to
users running the input manager, and to the developers receiving crash
reports by way of it.


Now, when I say SCR “modifies” Apple’s Crash Reporter, I do not mean
that the Crash Reporter application, on disk, is touched in any way.
It is modified in memory, when it launches. Input managers are loaded
by most Mac OS X applications — including all Cocoa apps, but also
many modern Carbon apps as well — soon after they launch.


The supported purpose for input managers is to allow developers to
define new ways for users to enter text. However, the code in an input
manager can pretty much do what it wants to inside an application’s
address space, and so thus, input managers have turned into an
unofficial channel for hacking system and application behavior. E.g.,
most of the hacks euphemistically described as “plug-ins” on Jon
Hicks’s [Pimp My Safari](http://pimpmysafari.com/) web site — such as Saft and PithHelmet —  are input manager hacks. “Plug-ins” implies the use of a
legitimate API intended for extending or modifying an application;
Safari, unfortunately, has no plug-in API,3 so any developer wishing to
extend or modify Safari must resort to unsupported mechanisms such as
input managers.


As stated before, every installed input manager loads into (nearly)
every application. Input managers that are targeting one specific
application, such as the way Saft and PithHelmet patch Safari or the
way Smart Crash Reports patches Crash Reporter, typically perform some
identifier checking so as only to deliver their actual payload inside the
application they’re targeting. But, no bones about it, the nature of
input managers is such that they’re loaded into *every* app on your
system. The basic gist is that when they’re loaded, they check to see
whether this app is the app they’re looking to patch, and if it isn’t,
do nothing more. Unsanity has gone so far as to [post a FAQ](http://www.unsanity.com/support.php?vf=32) with
example Objective-C code showing their technique:


```
- init
{
    if (self=[super init])
    {
        NSString* bundleID = [[NSBundle mainBundle] bundleIdentifier];

        if (bundleID && [bundleID 
                        isEqualToString:@"com.apple.CrashReporter"])
        {
            SInt32 sysVers;

            if (Gestalt(gestaltSystemVersion, &sysVers) == noErr &&
                                sysVers >= 0x1040 && sysVers < 0x1050)
            {
                // initialize SCR for CrashReporter
            }
        }
    }

    return self;
}

```


Translated to English, this code is an `init` method, which is what
gets called each time the input manager is loaded by an app that has
just launched. It checks to see if current bundle identifier is
“com.apple.CrashReporter”; if it isn’t, it does nothing more. If it
is, it checks to see that it’s running under Mac OS X 10.4.x, and if
so, patches Crash Reporter. (Unsanity’s example does not reveal any of
the actual code that patches Crash Reporter.)


Once installed and loaded, Smart Crash Reports only kicks in if the
application that crashed has registered its support for SCR. To do so,
developers add two keys to the info.plist XML file in their app
bundle. However, SCR can also kick in for non-application code
resources, such as QuickTime components, contextual menu items, input
managers, and, unsurprisingly, “haxie” modules for Unsanity’s
[Application Enhancer](http://www.unsanity.com/haxies/ape) (APE) system.


It’s worth clarifying here that Smart Crash Reports is not a haxie,
and works completeley independently of APE. APE, in and of itself, is
a meta-hack, providing an entirely new mechanism for additional hacks
to be added to your system. To install a haxie, you need to first
install the APE system and framework; to install an input manager, on
the other hand, you just copy it to your *~/Library/InputManagers*
folder. Input managers are hacks that take advantage of (or, perhaps
more accurately, abuse) Cocoa’s text input extension system; haxies
are hacks built for the APE system.


The fact that code resources can register for SCR raises a question:
If developer A has written, say, a contextual menu item plug-in that
registers with SCR, and developer B has written an app that registers
with SCR, and then app B crashes, what does the button in the SCR
dialog say? “Send to Apple and Developer B”? “Send to Apple and
Developer A and Developer B”? (That would be a long button.) And,
regardless what the button label says, who actually gets to see that
crash log?


I asked Slava Karpenko, the developer of Smart Crash Reports (along
with numerous other Unsanity products). He replied:


> The algorithm is very simple. SCR looks through the crashed
> thread and sees which of the identifiers it knows about
> appears higher in the stack trace. So if you have a
> contextual plug-in module “A” registered for their own match
> specifier inside an app “B” which also has registered, and
> you pull down the contextual menu, and choose something from
> the plugin A menu items, and it crashes, plug-in A’s identifier
> will show up higher in the stack trace, so the report will
> belong to the developer of A. So the button will say whatever
> caused the crash — if the [contextual menu item] appears
> higher in the crashed thread, then the developer A will get
> the log. If it is not present in the crashed thread at all,
> or a symbol from app appears higher than the one from the QT
> component, then the developer B will get the log.


In other words, if both a code resource and an application register
for SCR, it makes a reasonable attempt to guess which code caused the
crash and sends the report to that developer. This means that if a
haxie or input manager is causing an app to crash, the developer of
that app will not receive those crash logs — they’ll instead be sent
to the developer of the hack. All of Unsanity’s own haxies register
for SCR, for example, so application developers depending on Smart
Crash Reports will not see crash reports for for crashes unequivocally
caused by haxies. It can be argued whether this is good or bad, but
it’s not sneaky: the “Send to Unsanity and Apple” button that would
appear in the Crash Reporter dialog for a crash caused by a haxie
would make it clear to the user that Unsanity is taking the blame for
such a crash.


So: Smart Crash Reports is a free solution from Unsanity, which
attempts to modify Apple’s Crash Reporter app in as minimally invasive
a way as possible so that when an SCR-aware app crashes, Crash
Reporter will send the crash report both to Apple *and* to the
developer of the software involved with the crash.


## Automatic Installation


The dilemma facing application developers who wish to receive crash
reports via Smart Crash Reports is this: it only works if the Smart
Crash Reports input manager is installed. The vast majority of the
apps in [Unsanity’s list of SCR-aware software](http://www.unsanity.com/smartcrashreports/list/) use Smart Crash
Reports if it is already present; but if it is not, they don’t install
it. The developers of these apps are asking their users to download
and install Smart Crash Reports on their own.


However, Unsanity’s Smart Crash Reports SDK presents another option:
the automatic installation of the Smart Crash Reports input manager.
From Unsanity’s “[Smart Crash Reports for Developers](http://www.unsanity.com/images/previews/smartcrashreports/smartcrashreports-for-developers.pdf)”
documentation (PDF):


> It is possible to install the “client” part of Smart Crash Reports on
> the user’s computer from within your application (if you don’t want to
> tell users to download Smart Crash Reports installer from its home
> page). The Install API provides a streamlined, one-shot install
> interface so you can quickly deploy Smart Crash Reports from within
> your product with one function call.
> To implement the Smart Crash Reports install, download (if you haven’t
> already) the Smart Crash Reports SDK from its homepage:
> [http://www.unsanity.com/smartcrashreports/](http://www.unsanity.com/smartcrashreports/)
> Once it is downloaded, you need to link the SmartCrashReportsInstall.o
> and SmartCrashReportsInstall.h with your project and call a single
> function when you want to install Smart Crash Reports:
> `Boolean authenticationWillBeRequired = FALSE; 
> if (UnsanitySCR_CanInstall(&authenticationWillBeRequired)) 
>   UnsanitySCR_Install(authenticationWillBeRequired); 
> `
> This will silently attempt to install Smart Crash Reports, if it was
> not installed on user’s computer or if an older version was installed.


What they mean by “silent” here is that the user is never informed
that Smart Crash Reports has been installed. When an app that uses
this API call launches, it checks to see if Smart Crash Reports is
already installed (or if there’s an older version installed), and if
not, installs it. It does not ask permission beforehand, nor does it
report what it has done afterward.


This happens each time the app launches. So, if you notice the Smart
Crash Reports input manager and trash it, the next time you launch the
app, it will replace it.


I am aware of three applications that use this technique: Unsanity’s
own [Chat Transcript Manager](http://www.unsanity.com/ctm), Cocoatech’s recently-released
[Path Finder 4.0 and 4.0.1](http://www.cocoatech.com/pf4/), and Karelia’s [Sandvox](http://www.karelia.com/sandvox/) public
beta.


**Crux of this entire essay:** This behavior — the silent
installation of a system extension that modifies all applications — is both wrong and dangerous.


The situation gained notoriety last week when Bill Bumgarner, several
days after downloading and trying Sandvox, realized what Sandvox had
done and reported it on his weblog under the title “[Sandvox ‘Hidden’
Feature](http://friday.com/bbum/2006/01/20/sandvox-hidden-feature/)”:


> I was debugging a random crasher problem today and noticed that
> something called *Smart Crash Reports* appeared in the inventory of
> my Cocoa app’s list of frameworks and bundles.
> As it turns out, Sandvox silently installs Smart Crash Report in
> ~/Library/InputManagers/ when it is launched. As an input
> manager, SCR is thusly loaded into every Cocoa app launched and
> subsequently uses various non-supported mechanisms to modify the
> behavior of said application.
> Completely unacceptable. Sandvox is now gone from my system and
> will not return until this feature is “opt in” only.


Bumgarner is a software engineer at Apple, working on the Core Data
team; the “random crasher” he refers to in the post was unrelated to
Smart Crash Reports; what he’s saying is that he was debugging a crash
in software he’s working on, and while doing so, noticed the Smart
Crash Reports input manager in the stack trace.


Bumgarner is correct that this is completely unacceptable.
The reason why he’s right, however, was easily lost amid the specious
arguments in the comments attached to his post.


(Also noteworthy were Bumgarner’s follow-up posts: a [response from
Karelia developer Terrence Talbot](http://friday.com/bbum/2006/01/20/scr-response-from-sandvox/), and instructions from
Bumgarner on [how to disable the installation of Smart Crash
Reports](http://friday.com/bbum/2006/01/20/detecting-and-disabling-smart-crash-reporter/) (as well as any other input managers) by changing the
ownership and permissions of one’s *~/Library/InputManagers* folder.)


## The Point of This Argument


What matters is this: an application, in and of itself, should never
install an extension that modifies the system or otherwise diddles the
runtime environment of other applications, without the express
permission of the user. There are no exceptions to this rule.


Smart Crash Reports is by all accounts minimally invasive; “minimally
invasive”, however, is not the same thing as “non-invasive”.


One of the very best aspects of the Mac OS X user experience compared
to Windows or any other desktop environment is the ease with which
applications can be both installed and *uninstalled*. You copy from a
disk image to install, you move the app bundle to the Trash to
uninstall. That’s it. The ease and simplicity of this process is a
bragging point for the entire platform; this is one of the things many
Mac users demo when pitching Mac OS X to potential switchers.


It is also [Apple’s recommended method for distributing software](http://developer.apple.com/documentation/DeveloperTools/Conceptual/SoftwareDistribution/Concepts/sd_guidelines.html):


> Because an application keeps everything it needs within its
> bundle, simple drag-and-drop installation reduces file-system
> clutter and eliminates dependencies on items residing elsewhere
> in the file system. It also gives users the option of not
> copying items to their hard disks that they are not
> particularly interested in (such as Read Me files). To
> uninstall an application, all users have to do is remove the
> application bundle from the volume.


Conversely, most Mac users are displeased by software that requires
the use of an installer, especially for software they’re only trying
out. The implication of an installer is that more stuff will be put on
your disk than just the application bundle in the Applications folder,
and that more actions will be required to completely uninstall the app
than simply dragging it to the trash. (If you really are just putting
a copy of the app bundle in the Applications folder, don’t use an
installer.)


The implicit agreement with a drag-and-drop application installation
is that nothing will be left behind after moving the app to the Trash,
other than inert detritus such as preference files, caches, and other
application support files. What I mean by “inert detritus”4 is that such files, when left behind
after trashing an app, have no effect upon your system whatsoever
other than the nominal space they occupy on your hard drive. They are
data, not software.


And even if you’re the sort of obsessive neatnik who cares about
cleaning up such things, you know where to look. That’s why it’s
important for apps to store their preferences, caches, and application
support files in the standard Library sub-folders. (It’s also why I
have never seen the need for “uninstaller” utilities such as
[AppZapper](http://appzapper.com/) and [Yank](http://www.matterform.com/index.php?page=/yank/).)


An application that silently installs an input manager, on the other
hand, leaves behind software that will continue to be loaded into the
memory of every application on your system. Download Sandvox, try it
out, move it to your trash. You’ve still got Smart Crash Reports
installed, and it still loads into every app you launch. Worse, you
were never told it was being installed, and, because you installed
Sandvox (or Path Finder 4.0, or Chat Transcript Manager) via
drag-and-drop, there is no reason for you to believe that Smart Crash
Reports or anything like it might have been left behind.


An application that does anything out of the ordinary with regard to
its installed components must either (a) ship in the form of an
installer, preferably one which displays a manifest of every single
file that will be installed5; or
(b) if it’s an app that was installed normally, via drag-and-drop, it
must prompt you with a description of what it wants to install and ask
for permission before doing so.


A few examples:

- [BBEdit](http://www.barebones.com/products/bbedit/) and [TextMate](http://macromates.com/) both ship with command-line tools that can be
used to invoke these text editors from the Unix command-line. Both
ask permission before doing do, and both tell you where they go.
And for what it’s worth, command-line tools are far less intrusive
than input managers; if you leave the `bbedit` or `mate` tools
installed but get rid of the BBEdit and TextMate applications,
abandoned command-line tools are never going to cause any
conflicts or consume any resources, but yet BBEdit and TextMate
both do the right thing and ask before installing them.
- Rogue Amoeba Software’s [MemoryCell](http://rogueamoeba.com/freebies/) is a freeware menu extra
that displays the amount of memory being used by the current
application. The [NSMenuExtra](http://cocoadevcentral.com/articles/000078.php) API was never officially supported
by Apple, and, starting in Mac OS X 10.2, the system blocks
third-party menu extras from loading. So, MemoryCell ships with
[Menu Extra Enabler](http://www.unsanity.com/products/free), a freeware input manager hack from
Unsanity that patches SystemUIServer so that it loads all menu
extras, not just those from Apple. Rogue Amoeba ships MemoryCell
as an installer, with a Show Files command that clearly shows that
the Menu Extra Enabler input manager will be installed.
- [TLA Systems’ PCalc](http://www.pcalc.com/) 3.0 ships with a Dashboard widget. Rather
than auto-installing it, when you first launch PCalc it *asks* you
if you’d like the widget installed. (Do say yes, by the way: it’s
one of the handful of widgets I keep running all the time.) And
Dashboard widgets, like command-line tools, are far less intrusive
than the Smart Crash Reports input manager. It’s just the right
thing to do to ask permission before installing anything out of
the ordinary.


The point being: users should have zero worries about trying out an
app via a drag-and-drop installation. The only way for users not to be
worried about things being installed behind their backs is for nothing
to be installed behind their backs.


## Things That Are Not in Dispute or Not Relevant to This Argument

- *Whether Smart Crash Reports is buggy or causes any conflicts or
consumes unnecessary system resources, or, said another way,
whether Smart Crash Reports will cause anything undesirable to
happen if it is installed in your system.*
Irrelevant. Smart Crash Reports could be the most bug-free,
best-engineered piece of software in Macintosh history and it
wouldn’t make this acceptable. Indeed, I have no evidence, nor
have seen any reports, that Smart Crash Reports version 1.0.2 has
any undesirable side effects when installed on Mac OS X 10.4.3 or
10.4.4. (If any pack-rat readers out there still have a copy of
Smart Crash Reports 1.0.1 — the first non-beta public release of
SCR — sitting in their downloads folder, I’d appreciate being
sent a copy. **Update**: Got it, thanks.)
The argument against the auto-installation of Smart Crash Reports
isn’t that SCR causes any particular known harm; the argument is
that no app should silently install system-wide hacks, period.
What’s the alternative? That developers should feel free to
install any system-wide hacks they want, without warning, so long
as they’re not aware of any bugs or memory leaks or conflicts?
That way lies madness.
- *Whether crash logs are useful to developers.* Not disputed.
Crash reports are of tremendous value to developers. Being against
the auto-installation of SCR does not imply that one denies that
crash logs are useful to developers. There are other ways to do
this.
- *Whether Mac OS X should have a standard mechanism for
developers to obtain crash logs from their apps in the field.*
Irrelevant. I think it should, many developers think it should.
Unsanity thinks it should. But it doesn’t, which means that
developers who want to see their software’s crash logs need to
implement something of their own. That doesn’t give them the right
to implement such a feature any way they choose.
- *Whether registering for Smart Crash Reports support is less work
for developers, possibly much less work, than rolling their own
homegrown crash reporting systems.* Irrelevant. It could well be
that adding support for SCR is many times less work than any other
option; that doesn’t make it right.
- *Whether Unsanity’s intentions for Smart Crash Reports are purely
altruistic; i.e. whether the one and only reason for SCR’s
existence is to solve the very real problem of developers having
no drop-in solution for obtaining crash logs from their software.*
Again, irrelevant. There are several other ways this could be done
which do not entail diddling every process on the system.


## The Problem With Smart Crash Reports


To reiterate: the point of this entire piece is not to argue against
Smart Crash Reports itself, but rather the silent installation of it
by applications.


The right thing to do is what most SCR-aware software does — use it
if it’s there, but do nothing if it isn’t. The problem is that without
automatic installation, Smart Crash Reports isn’t going to be there
most of the time. You can ask users to download it and install it
separately, but it doesn’t offer much in the “what’s in it for me”
equation to make it seem worthwhile. It’s developers who want crash
logs, not users, and while you can make the argument that it’s in
users’ own interest to allow developers access to crash logs — which
should allow the developers to fix more bugs and produce better
software, which the users in turn will benefit from — that’s an
indirect benefit.


The architecture of Smart Crash Reports is such that it leads to a
chicken-and-egg problem — it’s not useful unless the input manager is
installed, but users don’t have much motivation to install the input
manager on their own.


Hence the appeal of automatic installation.


It would be acceptable for applications to *offer* to install Smart
Crash Reports, so long as they provide a fair description of what it
does and how it works. I think developers are wary of this, however,
because they realize that a fair description of SCR sounds rather
unsavory — that users will be turned off if the first thing they
see from a new application is a dialog box talking about crashes and
unsupported modifications to Apple’s Crash Reporter app.


If you think your users would be turned off by an accurate description
of something, that doesn’t mean you should do it without telling them.
It means you shouldn’t be doing whatever it is you don’t want to tell
them about.


For me, I understand what Smart Crash Reports does, I understand why
developers consider crash logs to be helpful, and I don’t believe it
causes any harmful side effects.


I still don’t want it installed on my system.


It does me no good whatsoever. When an app crashes, in most cases, I
already send crash logs to the developer of the software in question.
(Most of the crashes I see are in beta software, and knowing how to
send in a crash report is something you learn on the first day of Beta
Testing School.)


You might be almost certain that Smart Crash Reports won’t cause any
problems, but I’m *completely* certain that if it isn’t installed at
all, it definitely won’t.


(I have suppressed the automatic installation of Smart Crash Reports
by placing an empty text file named “Smart Crash Reports” in my
InputManagers folder. Using the Finder’s Get Info command, I locked
the file, which prevents it from being overwritten by the “Smart Crash
Reports” input manager bundle.)


## Suggested Alternatives


There are far better ways for developers to get access to their crash
logs than by linking against Smart Crash Reports. What seems easiest
to me would be to monitor your application’s crash log file in
*~/Library/Logs/CrashReporter/*. Each time your app launches, read your
own crash log and look for the date of the most recent crash. If it’s
more recent than the last time you checked the log, your app crashed,
and you can ask the user for permission to send the text of the crash
log via email or HTTP.


Other developers have devised their own systems. Michael Tsai’s
[C-Command](http://c-command.com/) family of apps all contain a custom crash reporter,
MJTCrashReporter, of his own design. Even though I use SpamSieve and
BBAutoComplete constantly, and I beta test both applications, I have
never seen either of them crash — so I’ve never actually seen Tsai’s
crash reporter in action. I asked him how it works, and he replied:


> When the application starts up, it uses [`signal (3)`](http://developer.apple.com/documentation/Darwin/Reference/ManPages/man3/signal.3.html) to
> register for the signals that indicate crashes. When the app
> crashes, it calls the signal handler, which launches
> MJTCrashReporter and then quits the app. MJTCrashReporter waits
> a second or two to give the system time to write the crash log
> file, then it brings up its crash reporter window, pre-filled
> with the default address from Address Book and the latest crash
> log. To send the report, it makes an HTTP POST to
> c-command.com. I treat most crash reports as regular tech
> support issues, so I have the server send them to me as e-mails
> with the user’s address in the reply-to.


Absolutely beautiful. Also: doesn’t interfere a whit with any other
software on the system. Tsai also pointed out another advantage to
rolling one’s own crash reporter system: backwards compatibility.
Unsanity’s SCR only works on 10.4 or later; Tsai’s works all the
way back to Mac OS X 10.2, which his applications still support.


I was a beta tester for Path Finder 4, and when the Smart Crash
Reports integration with auto-installation was added, I complained to
the beta mailing list, more or less with a nutshell digest of this
essay.


Path Finder developer Steve Gehrman responded, in part:


> I think it will become fairly common in new apps, but I’ll add a
> check box, and we can put something in the readme file.
> It’s incredibly valuable for me to know when my app crashes.  Without
> it, I would have no way of knowing.
> The programmer at Unsanity is insanely brilliant and I trust his code
> 100%.  If it came from another source, I would not use it.


What he ended up adding was a hidden `defaults` preference6 to suppress Path Finder’s
auto-installation of SCR each time it launched. Far from ideal, but,
I’m sorry to admit, enough to get me to shut up about it at the time.


A few days ago, I wrote to Gehrman to ask him some questions about
Path Finder’s auto-installation of of SCR, and he replied that he’d
already replaced Smart Crash Reports in the upcoming 4.0.2 Path Finder
update:


> I think SCR is valuable, but I coded another solution works
> just as well and is even safer.  The new crash reporter in PF
> 4.0.2 just checks the crash log on launch and if it notices a
> new crash entry, it will ask the user [for permission to send]
> that information to us.


Which, of course, is exactly the idea I was going to suggest to him.
Path Finder 4.0.2 will even display a dialog similar to Crash
Reporter’s, with the contents of the stack trace and a field for the
user to enter comments. This simple change eliminates my only
significant gripe about Path Finder 4.


I can think of only two downsides to third-party developers
implementing their own crash reporting systems within their
applications. One, because there isn’t an open source library or
framework that does this already, it’s more work than linking against
SCR. But it’s a not a complicated problem. (And the “extra work” part
would be solved if someone released a good implementation as open
source.)


The other thing is that application-based crash reporters leave one
group of developers out — those developing non-application code
resources, like, say, haxies.


---

1. In Unix tradition, such background processes are called *daemons*, from which word comes the “d” at the end of many of their names. E.g. the Apache web server daemon is “httpd”.  ↩
2. The full name of the application bundle is “Crash Reporter.app”, with a space; the name of the folder where the logs are stored is “CrashReporter”, sans space.  ↩
3. I’m not talking about regular browser content-handling plug-ins like those for Flash or QuickTime; I’m talking about a plug-in API for adding browser application features like those provided by Saft and PithHelmet.  ↩
4. “Inert Detritus” would be a great name for a weblog.  ↩
5. Apple’s installer application has a command in the File
menu — Show Files — which does just this. I use this command every time I
install software from an installer.  ↩
6. `defaults write com.cocoatech.PathFinder InstallSmartCrashReporter NO` ↩



| **Previous:** | [Macworld Expo 2006 in Review](https://daringfireball.net/2006/01/mwsf_2006) |
| **Next:** | [Bedecked](https://daringfireball.net/2006/02/bedecked) |


PreviousNext