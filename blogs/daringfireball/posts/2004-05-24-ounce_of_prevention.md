---
title: "An Ounce of Prevention"
date: 2004-05-24
url: https://daringfireball.net/2004/05/ounce_of_prevention
slug: ounce_of_prevention
word_count: 567
---


[**Update 7 June:** I’ve modified the instructions on this page
considerably in the wake of Security Update 2004-06-07, which closes
all of the known vulnerabilities. The instructions on this page are
current and up-to-date. If you’d like to see last revision of this
document *prior* to today’s update, [click here](https://daringfireball.net/misc/2004/05/ounce_of_prevention.orig.text).]


In a nutshell, here is my advice for how to close the various
URI-related vulnerabilities in Mac OS X. For more details, see my
previous articles:

- “[Using the ‘telnet’ URI Protocol to Delete Files](https://daringfireball.net/2004/05/telnet_protocol)”
- “[About the Help Viewer Security Update, and, Also,
Why I Don’t Think You Need Paranoid Android](https://daringfireball.net/2004/05/help_viewer_security_update)”


This page is intended to serve as a consolidated, comprehensive, and
to-the-point list of instructions for closing all known URI-related
vulnerabilities affecting Mac OS X. If new information or exploits
are identified, I plan to revise this document in-place.

1. If you haven’t done so already, install Security Update
2004-05-24. This fixes the Help Viewer ‘help:runscript’
vulnerability.
2. If you’re running Panther, upgrade to version 10.3.4 using
Software Update.  10.3.4 contains an updated version of Terminal
which closed the ‘telnet’ vulnerability.
(If you’re running Jaguar, the ‘telnet’ vulnerability was closed
in Software Update 2004-05-24.)
3. Install [Security Update 2004-06-07](http://docs.info.apple.com/article.html?artnum=25785). This update closes
all known remaining vulnerabilities. See Apple’s Knowledge Base
article for details of how they’ve closed the URI/Launch Services
vulnerabilities.


If you follow these three steps, my testing indicates that you’ll be
protected from all of the vulnerabilities publicized in the last
month. (Note to Jaguar users: you must upgrade to 10.2.8 in order to
install Apple’s recent security updates. This is a free update; all
previous versions of Jaguar, 10.2.0 - 10.2.7, will remain vulnerable
to these exploits. 10.2.8 is the only version of Jaguar that is
supported by Apple.)


To be cautious, you might still want to turn off Safari’s “Open
‘safe’ files after downloading” preference (or keep it turned off if
you unchecked it a few weeks ago, when these problems surfaced).
Although there are no remaining vulnerabilities I’m aware of that
can be abused using this preference, I think it’s unwise to think
there exists such a thing as a “safe file” that can be opened
automatically after downloading it.


## FAQ

- *What if I followed your previous instructions,
and used [RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) to disable URI protocols such as ‘afp’,
‘disk’, and ‘disks’? Do I need to re-enable these?*
Security Update 2004-06-07 *removes* the ‘disk’ and ‘disks’
protocols from your Launch Services database. These protocols
are no longer handled automatically by DiskImageMounter, thus,
you no longer need to worry about them.
As for ‘ftp’ and ‘afp’, you can now safely re-assign these URIs
to the Finder if you want. However, I still think a dedicated FTP
application (such as [Interarchy](http://www.interarchy.com/) or [Transmit](http://www.panic.com/transmit/)) is a better
choice for FTP. If you don’t know for a fact that you need ‘afp’
URIs, you almost certainly don’t need to worry about them.
- *What’s the best resource with
innocuous example exploits using these techniques?*
[http://test.doit.wisc.edu/](http://test.doit.wisc.edu/) has example exploits for
downloaded zip archives and disk images, and for the ‘afp’,
‘disk’, and ‘ftp’ protocols.
My testing, on three separate Macs, indicates that by following
the above instructions, all of these example exploits have been
closed.



| **Previous:** | [About the Help Viewer Security Update, and, Also, Why I Don’t Think You Need Paranoid Android](https://daringfireball.net/2004/05/help_viewer_security_update) |
| **Next:** | [Security Cannot Be Spun](https://daringfireball.net/2004/05/security_cannot_be_spun) |


PreviousNext