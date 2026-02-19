---
title: "Command Line Fun"
date: 2003-04-23
url: https://daringfireball.net/2003/04/command_line_fun
slug: command_line_fun
word_count: 728
---


## Command Line PHP


[PHP](http://php.net/) is a very popular open source web page scripting language. Typically, it runs as an Apache module. I’ve been tinkering with PHP the past few weeks, and the best thing I can say about it as a language is that it’s like a very simplified version of Perl. But it’s easy to use, especially for short scripts and processing web page forms, because it allows you to include scripting code directly in your HTML markup. Also, PHP is very fast.


Starting with version 4.3, PHP officially gained the ability to be run on the command line in Unix-ish environments — like Mac OS X. Ever since Mac OS X shipped, [Marc Liyanage](http://www.entropy.ch/) has been distributing a wonderful assortment of pre-built, easily-installed Unix software packages for Mac OS X, including up-to-date versions of PHP. However, his PHP package doesn’t include command-line support.


[Jason Perkins](http://somebodydial911.com/) has stepped up to the plate, with a [PHP command-line installer for Mac OS X](http://www.somebodydial911.com/archives/001059.php). Download, install, done. It’s that easy.


So, in summary, Apple ships an old version of the PHP Apache module with Mac OS X. Liyanage has an installer to upgrade the PHP Apache module to version 4.3. Perkins has an installer to add a PHP CLI binary in `/usr/local/bin/`.


## Trash-Savvy ‘rm’


Remember my suggestion a few weeks ago that the [Finder should move replaced files to the Trash](http://daringfireball.net/2003/03/i_love_it_because_its_trash.html) instead of completely overwriting them? Gary Kerbaugh has written a nifty shell script for Mac OS X that brings the same thinking to the Unix rm command: [The Born Again Remove Function](http://www.cs.ecu.edu/~collins/rm/rm.html). It’s an implentation of rm that moves files and folders to the Trash instead of deleting them.


The idea isn’t that you should replace the real rm command with Kerbaugh’s version, but that you should put it somewhere like `~/bin/`
(a folder named “bin” in your home folder), which in turn you put at the beginning of your PATH environment variable. Then, when you invoke rm in a Terminal session, your shell will find the version in `~/bin/` before it finds the system’s version in `/usr/bin/`. Alternatively, you could rename Kerbaugh’s script to something like “trash”, and then invoke it like this:


```

trash foo.*

```


[Rael Dornfest has more details](http://www.oreillynet.com/pub/h/334), including a helpful introduction, at O’Reilly’s Mac OS X Hacks web site.


## appswitch


[appswitch](http://web.sabi.net/nriley/software/#appswitch) is a wonderful and free command-line utility from Nicholas Riley. It’s been out for a while, but I haven’t seen much mention of it, which is somewhat odd, because it is *excellent*. From Riley’s description:


> If you use shell scripts to automate Mac OS X applications, you may
> need to switch between applications.  You could use AppleScript via
> osascript(1), but it would take several seconds for the
> script to compile and execute—or you could use
> appswitch, which works almost instantly.  Need to launch an
> X11 application from Terminal but the X server isn’t in front when you
> need it?  Use appswitch to fix the problem.  Or, if you’d
> like a version of the ps(1) utility which understands the
> concept of OS X applications, appswitch can help.
> appswitch requires Mac OS X 10.2 or later with Developer
> Tools installed.


But so what can you do? Well, you can do `appswitch -l` to get a list of all running applications, with useful info such as their creator codes and process IDs:


```

gruber% appswitch -l
       PSN   PID TYPE CREA NAME                 PATH
  131073.0   361 APPL lgnw loginwindow          /System/Library/CoreServices/log
  393217.0   447 APPL dock Dock                 /System/Library/CoreServices/Doc
  524289.0   449 APPL syui SystemUIServer       /System/Library/CoreServices/Sys
  655361.0   450 FNDR MACS Finder               /System/Library/CoreServices/Fin
  786433.0   454 APPL Dock DragThing            /Applications/DragThing 4.5.1/Dr
  917505.0   455 APPL snpZ Snapz Pro X          /Applications/Snapz Pro X/Snapz 
 2097153.0   464 APPL sfri Safari               /Applications/Safari.app        
 2228225.0   487 APPL asDB Script Debugger      /Users/gruber/Applications/Scrip
 2490369.0   614 APPL R*ch BBEdit               /Applications/BBEdit 7/BBEdit.ap
 2621441.0   634 APPL )DF% Super Get Info       /Users/gruber/Applications/Super
 2752513.0   635 APPL sgiK Super Get Info Helpe /Users/gruber/Applications/Super
 3145729.0   645 APPL trmx Terminal             /Applications/Utilities/Terminal
 3670017.0   712 APPL Nnw* NetNewsWire          /Users/gruber/Applications/NetNe
 4587521.0   790 APPL CHIM Camino               /Users/gruber/Applications/Camin

```


Or you can activate a process by name: `appswitch -a Camino`


Or by creator code: `appswitch -c CHIM`


Or by bundle identifier: `appswitch -i org.mozilla.navigator`


And best of all, appswitch is very, very fast. Like instantaneous fast.



| **Previous:** | [Sticky Business Redux: Web Browsers](https://daringfireball.net/2003/04/sticky_business_redux_web_browsers) |
| **Next:** | [Accommodating](https://daringfireball.net/2003/04/accommodating) |


PreviousNext