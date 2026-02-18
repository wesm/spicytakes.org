---
title: "Disabling Unsafe URI Handlers With RCDefaultApp"
date: 2004-05-20
url: https://daringfireball.net/2004/05/unsafe_uri_handlers
slug: unsafe_uri_handlers
word_count: 686
---


[**Update 24 May 2004:** If you just want to know the steps I recommend to
close the various URI-related vulnerabilities, see “[An Ounce of 
Prevention](https://daringfireball.net/2004/05/ounce_of_prevention)”.]


The crux of the [Mac OS X security advisory](http://secunia.com/advisories/11622/) announced earlier
this week is that certain of the system’s default handlers for
custom URI protocols expose exploitable security holes.

- The ‘help’ protocol, by default assigned to Help Viewer,
can be used to execute script files at a known path location on
your computer.
**Update, 22 May 2004:** Apple released
[Security Update 2004-05-24 for Panther](http://www.apple.com/support/downloads/securityupdate__2004-05-24_(10_3_3).html) (and a
separate [update for Jaguar](http://www.apple.com/support/downloads/securityupdate_2004-05-24_(10_2_8).html)). Included in this update
is a new version of Help Viewer, which eliminates this security
problem. After installing this security update, it is safe to
assign the ‘help’ URI protocol to Help Viewer. However, this
security update has no effect on the handling of the ‘disk’,
‘disks’, or ‘telnet’ protocols. See [this follow-up](https://daringfireball.net/2004/05/help_viewer_security_update) for
more details.
- The ‘disk’ and ‘disks’ protocols, by default assigned to
DiskImageMounter, allow disk images to be mounted in your file
system automatically.


The basic idea behind the exploit is that a malfeasant could set up
a web page that (a) mounts a disk image on your system, and then (b)
uses the ‘help’ protocol to trick Help Viewer into executing a
malicious script at a known path location on the disk image volume
automatically mounted in step (a).


This is for real, and potentially nasty. I have yet to see any
reports of the exploit actually being used maliciously, but it’s
worth protecting against. Here are a few simple things you can do to
protect your system:

1. [Download RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/), a free System Prefs panel from Rubicode.
Install it in the PreferencePanes folder in your Library folder.
2. Open System Prefs, then open the new Default Apps panel.
3. Click on the “URLs” tab.
4. Set the ‘disk’, ‘disks’, and ‘help’ protocols to 
“`<disabled>`”.


**Update:** You should also disable to the ‘telnet’ protocol; see
[here](https://daringfireball.net/2004/05/telnet_protocol) for details.


You should also open Safari’s preferences, and turn off the checkbox
“Open ‘safe’ files after downloading” — when turned on, this
setting allows disk images to be mounted automatically.


The fact that Help Viewer can execute scripts specified via ‘help’
protocol URIs is a feature that ostensibly allows for the creation
of somewhat interactive help books. E.g. an application’s help book
could contain an AppleScript, linked from the help book’s HTML, that
would illustrate some particular point. However, I’m unaware of any
help books that actually use this feature.


Disabling the ‘help’ URI protocol’s connection to Help Viewer will
*not* affect your normal use of the Help Viewer application.


## Why RCDefaultApp


MisFox and More Internet are similar utilities to RCDefaultApp, and
are also both free, but there is an important difference. MisFox and
More Internet both only show URI protocols registered through the
Internet Config system; RCDefaultApp also shows protocols registered
directly through Launch Services.


As I noted a few weeks ago in “[Fixing Corrupt Preferences for
Default Internet Helpers](http://daringfireball.net/2004/05/internet_helper)”, Internet Config is a set of APIs
that dates back to System 7. On Mac OS X, the Internet Config APIs
are still supported, but they’re just a layer on top of Launch
Services. From Apple’s “[Internet Config Reference Introduction](http://developer.apple.com/documentation/Carbon/Reference/Internet_Config/internet_config_ref/Introduction.html)”:


> Mac OS X applications should employ Launch Services and
> System Configuration for managing Internet preferences. In
> Mac OS X, Internet Config calls through to these newer APIs.
> Using them directly increases your application’s efficiency.


The ‘disk’ and ‘disks’ protocols are registered directly in Launch
Services, which means they aren’t displayed in MisFox or More
Internet. I.e., RCDefaultApp shows *all* the protocol handlers
registered on your system; MisFox and More Internet only display the
protocols that are registered through Internet Config.


Plus, version 1.1 of RCDefaultApp, released earlier this week,
introduced the feature that allows you to assign a protocol to
“`<disabled>`”. This is a more elegant solution than assigning
these protocols to dummy applications, such as Mac OS X’s Chess game.



| **Previous:** | [Like a Lead Zeppelin](https://daringfireball.net/2004/05/lead_zeppelin) |
| **Next:** | [Using the ‘telnet’ URI Protocol to Delete Files](https://daringfireball.net/2004/05/telnet_protocol) |


PreviousNext