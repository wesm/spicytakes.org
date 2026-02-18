---
title: "Using the ‘telnet’ URI Protocol to Delete Files"
date: 2004-05-21
url: https://daringfireball.net/2004/05/telnet_protocol
slug: telnet_protocol
word_count: 475
---


[**Update 24 May 2004:** If you just want to know the steps I recommend to
close the various URI-related vulnerabilities, see “[An Ounce of 
Prevention](https://daringfireball.net/2004/05/ounce_of_prevention)”.]


In addition to the ‘disk’, ‘disks’, and ‘help’ URI protocols
mentioned [yesterday](https://daringfireball.net/2004/05/unsafe_uri_handlers), you should also turn off the ‘telnet’
protocol. By default, it’s assigned to Terminal; I recommend using
[RCDefaultApp](http://www.rubicode.com/Software/RCDefaultApp/) to set it to “<disabled>”.


The problem with Mac OS X’s default handling for ‘telnet://’ URIs is
that it treats whatever follows the slashes as an argument to the
`telnet` shell command. This includes the use of command-line
option switches. `telnet`’s “-n” switch can be used to specify a
text file in which a log of the telnet session will be written.


Thus, a URI such as:


```
telnet://-nFoo

```


will create — *or overwrite* — a file named “foo” in your home
folder. This file is empty, and it isn’t executed, but the fact that
it will overwrite an existing file with the same name is some
serious shit.


It will not overwrite folders (e.g. it won’t replace your Documents
folder with an empty file named “Documents”), and it will not
overwrite files to which you don’t have write privileges (thus it
can’t be used to overwrite essential system components).


But it *can* be used to overwrite any file on your computer to
which you do have write privileges, which includes pretty much any
file within your home folder.


To access files outside the root level of your home folder, simply
URL-encode the directory-separator slashes. This URI will write a
file named “foo” in your startup disk’s /tmp folder:


```
telnet://-n%2Ftmp%2Ffoo

```


Now we get nasty; this one will overwrite your Finder preferences
file:


```
telnet://-nlibrary%2Fpreferences%2Fcom.apple.finder.plist

```


For some reason, such URIs only work if the entire path is specified
using lowercase letters — despite the fact that the actual names
for the folders in the above example are “Library” and “Preferences”.


I first saw this ‘telnet’ exploit mentioned in [this comment from
“fukami” on Elizabeth Lawley’s Mamamusings](http://mamamusings.net/archives/2004/05/18/serious_os_x_security_problem.php#3001) weblog. [Jay Allen](http://www.jayallen.org/journey/2004/05/mac_os_x_highly_critical_security_flaw#comment-7506)
clued me in to the URL-encoded slashes trick that allows
this exploit to overwrite files outside your home folder.


## What About ssh?


Within minutes of posting this article, I started getting email
asking if the ‘ssh’ protocol has a similar hole. As far as I can
tell, it does not: I’m not aware of any way that an ‘ssh’ URI can be
used nefariously. For one thing, even though the ssh protocol can be
loosely described as a secure alternative to telnet, the `ssh` shell
command provides an entirely different set of command-line switches
than the `telnet` tool; `ssh` has no analogous switch to `telnet`’s
“-n”.



| **Previous:** | [Disabling Unsafe URI Handlers With RCDefaultApp](https://daringfireball.net/2004/05/unsafe_uri_handlers) |
| **Next:** | [About the Help Viewer Security Update, and, Also, Why I Don’t Think You Need Paranoid Android](https://daringfireball.net/2004/05/help_viewer_security_update) |


PreviousNext