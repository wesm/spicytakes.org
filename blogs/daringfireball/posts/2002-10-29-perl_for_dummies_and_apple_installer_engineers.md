---
title: "Perl for Dummies (And Apple Installer Engineers)"
date: 2002-10-29
url: https://daringfireball.net/2002/10/perl_for_dummies_and_apple_installer_engineers
slug: perl_for_dummies_and_apple_installer_engineers
word_count: 299
---


As noted at MacSlash, some users are [having problems](http://www.macslash.org/articles/02/10/23/1513202.shtml) with the [QuickTime 6.0.2](http://www.apple.com/quicktime/download/) installer for Mac OS X.


Ends up there’s a Perl script in the package, and the script uses “EQ” and “NE” for string comparison (“equals” and “not equals”, respectively). These operators were deprecated many years ago, in favor of the lowercase “eq” and “ne”.


The uppercase versions still work up through Perl 5.6.x, but are no longer supported in Perl 5.8. Jaguar ships with Perl 5.6.0, so the installer will work on a stock 10.2 system. But Apple’s own web site contains a how-to article that explains [how you can replace Perl 5.6 with 5.8](http://developer.apple.com/internet/macosx/perl.html). If you’ve done so, the QuickTime installer won’t work.


The script resides inside the installer package, here:


```
    QuickTime.pkg/Contents/Resources/preflight

```


The mistake is inexcusable, for several reasons.


For one thing, this sort of bug should *never* happen in a modern Perl script. One of the first lessons in every Perl beginners tutorial is that you should always start your scripts with the “-w” switch. In other words, the first line of Apple’s script should read:


```
	#!/usr/bin/perl -w

```


instead of:


```
	#!/usr/bin/perl

```


If it did, the script would generate an error, stating “Use of EQ is deprecated.”


I simply can’t emphasize strongly enough just how boneheaded it is not to use “-w”  —  for *any* script, let alone one which is going to be executed by *hundreds of thousands* of your customers. (The script probably ought to be running under the “use strict” pragma as well, but “-w” is all they needed to flag this mistake.)


You’d think after last year’s [iTunes installer fiasco](http://www.xlr8yourmac.com/OSX/itunes2_erased_drives.html), which was caused by a poorly-written shell script, Apple would have learned something.



| **Previous:** | [Stereotypical Fun](https://daringfireball.net/2002/10/stereotypical_fun) |
| **Next:** | [Wine](https://daringfireball.net/2002/11/wine) |


PreviousNext