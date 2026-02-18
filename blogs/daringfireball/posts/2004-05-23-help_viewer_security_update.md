---
title: "About the Help Viewer Security Update, and, Also, Why I Don’t Think You Need Paranoid Android"
date: 2004-05-23
url: https://daringfireball.net/2004/05/help_viewer_security_update
slug: help_viewer_security_update
word_count: 2614
---


[**Update 24 May:** If you just want to know the steps I recommend to
close the various URI-related vulnerabilities, see “[An Ounce of 
Prevention](https://daringfireball.net/2004/05/ounce_of_prevention)”.]


[**Update 23 May, 11:45 EST:** This article has been revised significantly.
Ordinarily, I do not make significant changes to an article in-place
after publishing, but in this case, I believe accuracy is paramount.
I’ve saved a copy of the [original article](https://daringfireball.net/misc/2004/05/help_viewer_security_update.orig.text) (in Markdown
format), if you’re interested.]


---


Late Friday, Apple released Security Update 2004-05-24, for
[Panther](http://www.apple.com/support/downloads/securityupdate__2004-05-24_(10_3_3).html) and [Jaguar](http://www.apple.com/support/downloads/securityupdate_2004-05-24_(10_2_8).html).


Apple’s description for the Panther version:


> This update delivers a number of security enhancements and is
> recommended for all Macintosh users. This update includes the
> following components:
> HelpViewer [*sic*]


The description for the Jaguar version:


> Security Update 2004-05-24 delivers a number of security
> enhancements and is recommended for all Macintosh users.
> This update includes the following components:
> Help Viewer
> Terminal


Indeed, these are the only updated components. (You can see for
yourself by downloading the updates. The `.pkg` updaters are
packages, which are just folders that the Finder treats as a single
file. Inside the package is a “Contents” folder, inside which is a
file named “Archive.bom”. (“bom” stands for “bill of materials”.)
You can use the `lsbom` command-line tool to list all of the updated
files specified in a `.bom` file.)


The updated version of Help Viewer for Panther is version 2.0.6. The
new version of Help Viewer fixes at least one specific security
exploit:  Help Viewer no longer executes scripts when it receives a
‘help:runscript’ URI which originates from any application other 
than Help Viewer itself.


Thus, after installing this security update, it is now safe to
assign the ‘help’ URI protocol to Help Viewer.


## About ‘help:runscript’ URIs


When I first wrote about this ‘help’ URI security exploit, I
mentioned that I wasn’t aware of any help books which actually took
advantage of this feature. That was sheer laziness on my part, and
for that I apologize. In fact, as a simple BBEdit multi-file search
for “help:runscript” shows, it’s a commonly used feature in many of
Apple’s own help books.


Most frequently, it’s used to create a link that opens an
application or a particular System Prefs panel. For example, each of
the Mac Help pages relating to sound — choosing an alert sound,
setting the volume, setting input sources, etc. — has a link at the
bottom that says, “Open Sound preferences for me”. If you click this
link, the System Prefs application launches, and displays the Sound
panel.


Help books are just HTML files. The source code for such a link
looks like this (note that I’ve added line breaks for readability;
the actual href attribute should be one long line):


```
<a href="help:runscript=
MacHelp.help/Contents/Resources/English.lproj/shrd/OpnApp.scpt%20
string='System:Library:PreferencePanes:Sound.prefPane'">
Open Sound preferences for me</a>

```


Because Help Viewer is the default handler for the ‘help’ URI
protocol, when any other application attempts to resolve such a URI,
it gets passed to Help Viewer. Prior to the version released in this
security update, you could pass a ‘help:runscript’ URI from any
source, and Help Viewer would execute the script specified in the
href attribute.


Hence the security problem — the ‘disk’ and ‘disks’ URI
protocols, ostensibly unrelated to ‘help’ — could be used by a
malfeasant to silently mount a disk image on your computer. Then, a
‘help:runscript’ URI could be used to launch apps on the mounted
disk image. This could happen simply by loading a web page; with a
couple of frame and meta refresh tags, the disk image could mount
and the script could execute without your having to click on
anything.


The stop-gap measure I recommended prior to the release of the
security update was to disable the ‘help’ URI protocol, using
RCDefaultApp (or More Internet or MisFox; any of which would do the
job). Doing so plugged the security hole, but also prevented *any*
‘help’ URIs originating outside Help Viewer from working. For
example, a ‘help:search’ URI will perform a search in Help Viewer;
e.g. to search for “sound volume”:


```
<a href="help:search='sound%20volume'%20bookID='Mac%20Help">
Search Help Viewer for information about 'sound volume'.</a>

```


Disabling ‘help’ disabled *all* help URIs; but the only dangerous
ones were ‘help:runscript’ URIs. This is exactly what the new
version of Help Viewer limits. You can try it for yourself. Here are
the two links shown above:


[
Open Sound preferences for me.](help:runscript=MacHelp.help/Contents/Resources/English.lproj/shrd/OpnApp.scpt%20string='System:Library:PreferencePanes:Sound.prefPane')


[
Search Help Viewer for information about ‘sound volume’.](help:search='sound%20volume'%20bookID='Mac%20Help)


The first — a ‘help:runscript’ URI — no longer works when
initiated from a web browser. Prior to the security update, it did.
(When passed a ‘help:runscript’ URI from another app, the updated
Help Viewer now logs a message to your console: “Help Viewer[4869]
help://runscript called by another application!”.)


The second — a ‘help:search’ URI — still works from any
application, if you have Help Viewer specified as your default
handler for ‘help’. This is a good thing; Apple has prevented
precisely what was dangerous, and nothing else.


It’s also worth noting that even when you disable the ‘help’
protocol, or point it at a dummy application such as Chess, Help
Viewer still handles all ‘help’ URIs which originate from within
Help Viewer itself. This makes sense, in the same way that web
browsers like Safari, Camino, and IE always handle ‘http’ URIs on
their own, no matter if they’re specified as your default web
browser.


Thus, if you’re paranoid, you can leave the ‘help’ protocol
disabled, and ‘help:runscript’ URIs will still work for you from
within Help Viewer. For what it’s worth, I have restored Help Viewer
as my default handler for ‘help’.


## About the Jaguar Update


The updated Help Viewer for Jaguar has been changed similarly to the
version for Panther: scripts are no longer executed when
‘help:script’ URIs originate from an app other than Help Viewer
itself.


I have confirmed that the updated version of Terminal for Jaguar
fixes the ‘telnet’ vulnerability. I do not know why this was fixed
for Jaguar, but not for Panther.


## What About Other Protocols? And What’s the Deal With Unsanity’s Paranoid Android?


Security Update 2004-05-24 for Panther contains nothing in response
to the [‘telnet’ URI vulnerability](https://daringfireball.net/2004/05/telnet_protocol) I wrote about Friday.
My advice remains that you should use [RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) to disable
the ‘telnet’ protocol. (Unless you’re running Jaguar, in which case
the updated version of Terminal removes the vulnerability.)


As for ‘disk’ and ‘disks’, you should leave these protocols
disabled as well. The specific security problem that led to this
discussion has been closed with the updated version of Help Viewer,
but it’s a terrible idea to allow disk images to mounted
automatically in response to a URI from a remote source, and it can
be exploited for harm. E.g., see the first example exploit linked
from [Unsanity’s Paranoid Android Whitepaper](http://www.unsanity.com/haxies/pa/whitepaper).


But first, what is Paranoid Android? Unsanity describes it thusly:


> A vulnerability in Apple’s Mac OS X results in a potential
> situation in which a malicious person could execute
> arbitrary commands on your machine, such as deleting your
> home directory, or doing other harmful actions. This
> vulnerability involves the use of URL “schemes”. These are
> the part of a web address that specifies what program
> should be used to handle the address.
> Paranoid Android can protect you from this potential
> vulnerability until Apple makes an official fix available.
> It does this by watching the URL schemes that are requested
> and delaying them until you’ve had a chance to say whether
> you’d like to proceed or not. If you know that the url
> that’s being loaded is legit, go ahead, but if it looks
> suspicious, Paranoid Android gives you an opportunity to
> cancel it.


But that only describes what Paranoid Android *does*, not what it
*is* or how it works. What it is is an Application Enhancer module,
a.k.a. a “haxie”. How it works, loosely, is that it injects code
and/or data into every running application — while haxies do not
modify the applications on disk, they do their thing by violating
the boundaries of protected memory.


Thus, Paranoid Android is a haxie that injects code into every
application, which code apparently intercepts calls to Launch
Services which are attempting to resolve URIs. It then presents a
confirmation dialog for any URI using a scheme that isn’t known to
be safe.


Thus, while Paranoid Android may well solve the problem of malicious
use of URI protocols and their default handlers as registered in
Launch Services, it may also introduce problems of its own.


The Paranoid Android Whitepaper, written by the developer of
Paranoid Android, Jason Harris, documents and links to two “benign
sample exploits”. Both are legitimate threats. The first uses the
‘disk’ protocol, and works like this:

1. A Mac OS X user visits a web page. (It doesn’t matter which
web browser is being used.)
2. Using frames and meta refresh tags, the web page sends a ‘disk’
URI, which, with default settings, causes a disk image to be
automatically mounted on the user’s system.
3. This disk image contains an application bundle, the Info.plist
file of which specifies that this app wants to register a custom
URI scheme. For example, in Unsanity’s sample exploit, the
pertinent snippet of Info.plist is this:
`<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>Malware URL</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>malware</string>
        </array>
    </dict>
</array>
`
which registers the application as the default handler for the
‘malware’ URI scheme. This could be any arbitrary string — the
point is that an application can register for its own custom
scheme.
4. Upon displaying this application in a Finder window, the
Finder automatically uses Launch Services to register the
application for the URI scheme it has asked to handle. (As far
as I can tell, the Finder only does this if the app has been
displayed — merely mounting the image doesn’t register the URI
scheme in my testing.)
5. After waiting a few seconds for the disk image to mount, the
remote server sends a URI using the protocol the application
just registered for. (E.g. in the case of Unsanity’s example, a
“malware:unused” URI.) The user’s web browser passes the URI
to Launch Services for resolution, and Launch Services launches
the application.


At this point, the user’s goose is potentially cooked — once the
application is launched, it has free reign. The only action the user
took was to load a web page; the rest happened automatically.


Thus, Unsanity’s whitepaper describes a legitimate threat. However,
I do not agree with their advice as to how to deal with this threat:


> Because this sample exploit registers its own URL scheme,
> none of the methods people had been using involving
> disabling certain scripts, moving Help.app or changing the
> ‘help’ URL scheme would protect against it. At this time,
> only Paranoid Android provides protection from it.


While indeed this has nothing to do with the ‘help’ scheme, it is
simply *not true* that “only Paranoid Android provides protection from
it.” If you have disabled the ‘disk’ and ‘disks’ protocols — and
turned off the “Open ‘safe’ files” preference in your web browser — this
exploit will fail, because the disk image will not be mounted.


Unsanity’s second sample exploit, added today, uses an ‘ftp’ URI
pointing to a directory on unsanity.com. With default settings on
Panther, ‘ftp’ URIs are handled by the Finder, which will in turn
mount the specified directory in the ‘ftp’ URI as though it were a
network server.


Once this happens, and the Finder displays the “OSXMalware”
application in that folder, it will once again register the custom
URI scheme specified in the app’s Info.plist file. (In this case,
‘guardian452’, which is a different protocol than the ‘malware’
scheme used in Unsanity’s ‘disk’ example.)


My testing indicates this is also a legitimate threat. The app won’t
get registered with Launch Services until the Finder displays it,
but I can make this happen automatically by invoking Unsanity’s
exploit with no Finder windows open; upon mounting the FTP directory
as a server volume, the Finder will create a new Finder window
displaying the directory’s contents.


When the web server subsequently sends a URI using the
newly-registered scheme, Launch Services launches the remote
application from the FTP server. *Boom.*


(Earlier revisions of this article indicated otherwise; at the time
this article was originally published, Unsanity’s ‘ftp’ example
exploit failed because the OSXMalware application didn’t have
executable permissions. They’ve since fixed the permissions, and
their example now works.)


Choosing any application other than the Finder as the default
handler for ‘ftp’ URIs closes this hole in the same way that
disabling the ‘disk’ and ‘disks’ protocols closes the first one.
Regular FTP apps do not mount remote FTP directories as though they
were server volumes.


This is a generalized and serious vulnerability in Mac OS X:

1. Remote web server causes a volume to be mounted in the file system,
and the contents of the volume are displayed by the Finder.
2. The now-mounted remote volume contains a malicious application
that contains an Info.plist file that asks to register a custom
URI scheme with Launch Services.
3. Upon displaying the malicious application, the Finder registers
the new URI scheme, as per the app’s Info.plist file.
4. After waiting a few seconds for steps 1-3 to occur, the remote
web server sends another URI, using the newly-registered scheme.
5. Launch Services will launch the remote application.


The key to prevention is to nip it at step #1, and prevent remote
servers from automatically mounting volumes in your file system.


To protect your Mac, you should definitely disable the following URI
protocols, using RCDefaultApp:

- disk:
- disks:
- afp:


You should also assign the ‘ftp’ protocol to any application other
than the Finder. (Or disable it, but I think that’s overkill.)


‘afp’ is the scheme for AppleShare servers; I have confirmed that
an ‘afp’ URI in the following form will allow a remote AppleShare
volume to be mounted automatically and silently:


```
afp://username:[email protected]/volume

```


Note that disabling the ‘afp’ protocol using RCDefaultApp will
*not* prevent you from connecting to AppleShare servers manually.
You can still connect to AppleShare servers using the Finder’s
Connect to Server command, or using the Network dingus in a Finder
window sidebar. Disabling the ‘afp’ protocol merely prevents ‘afp’
URIs from being passed to the Finder from other applications — e.g.
a web browser.


You must also make sure your web browser and ‘ftp’ handler do not
automatically expand or process quote-unquote “safe” files.


## Is Paranoid Android Necessary?


I cannot recommend the use of Paranoid Android. As far as I have
determined (and admittedly, that’s an important disclaimer), every
vulnerability handled by Paranoid Android can also be solved by
changing or disabling Mac OS X’s default URI handlers using
RCDefaultApp.


RCDefaultApp merely modifies your Launch Services settings, and
should therefore conflict with nothing. Paranoid Android uses
completely unsupported mechanisms to inject code into every running
application, and therefore has the potential to conflict with
anything.


That said, I have no knowledge of any problems or conflicts that
Paranoid Android *does* cause. I believe Jason Harris and Unsanity
have nothing but the best of intentions, and their example exploits
linked from the Paranoid Android Whitepaper were a significant
source of information for this article.


But my point is this: why run a haxie if you can close these
vulnerabilities without one?


If there is a demonstrable exploit that cannot be disabled by
supported means, I’d like to see it.



| **Previous:** | [Using the ‘telnet’ URI Protocol to Delete Files](https://daringfireball.net/2004/05/telnet_protocol) |
| **Next:** | [An Ounce of Prevention](https://daringfireball.net/2004/05/ounce_of_prevention) |


PreviousNext