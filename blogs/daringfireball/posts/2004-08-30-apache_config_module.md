---
title: "Apache Configuration Language Module for BBEdit 8"
date: 2004-08-30
url: https://daringfireball.net/2004/08/apache_config_module
slug: apache_config_module
word_count: 326
---


[BBEdit 8](http://www.barebones.com/products/bbedit/new.shtml) is out, and one of its major new features is support for
codeless language modules. (Previously, BBEdit language modules needed
to be compiled plug-ins written in C/C++.)


I’ve created a [codeless language module for Apache configuration
files](http://daringfireball.net/projects/apacheconfig/) (2 KB). It provides syntax coloring for comments and Apache
server directive keywords; by default, it claims any file whose name
ends with ‘.conf’ or ‘.htaccess’ (or whose name *is* ‘.htaccess’).


Download it, unzip it, and copy “Apache Configuration.plist” to:


```
~/Library/Application Support/BBEdit/Language Modules/

```


Then relaunch BBEdit. Configure via the Languages panel in BBEdit’s
preferences.


Creating codeless language modules is a cinch — each module is an XML
property list file. Appendix D in the BBEdit 8 user manual has complete
details on their syntax and format.


**Update 1:**  I was a beta-tester for BBEdit 8; I put this together a few weeks ago, not in the hour since BBEdit 8 was publicly released.


**Update 2:** Added `RewriteBase` to the list of keywords; thanks to Dan Carlson. If anyone else spots missing keywords, let me know.


**Update 3** (Wednesday, 1 Sep 2004):

- The module now has a [permanent home](http://daringfireball.net/projects/apacheconfig/) in my [Projects](http://daringfireball.net/projects/)
section. That page will always host the most recent revision.
- Added over 100 missing keywords. The keyword list is now a superset
of all server directives for Apache versions 1.3 and 2.0. Thanks to
everyone who sent me missing directives, but especially to Gregory
Ramsperger, who pointed me to the comprehensive list of server
directives at apache.org, which I inexplicably had overlooked.
- Added a wildcard to the ‘.htaccess’ filename suffix. This way, if
you open several files named “.htaccess” via Interarchy (or another
S/FTP client that supports the Edit With BBEdit protocol), the
module claims the files even though in BBEdit they appear with names
like “.htaccess#1”.



| **Previous:** | [Markdown 1.0](https://daringfireball.net/2004/08/markdown_10) |
| **Next:** | [We’ve Never Even Heard of This ‘iTunes Music Store’ of Which You Speak](https://daringfireball.net/2004/09/microsoft_tuesday) |


PreviousNext