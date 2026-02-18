---
title: "Scripting File and Creator Types"
date: 2004-02-12
url: https://daringfireball.net/2004/02/scripting_file_and_creator_types
slug: scripting_file_and_creator_types
word_count: 785
---


Mac OS X brings together two worlds of scripting — traditional Mac OS AppleScript, and traditional Unix scripting (by which I mean anything that can start with “#!”, including both shell scripting and languages like Perl, Python, and Ruby). Apple has been pretty serious about supporting both types of scripts — for example, the system-wide [Script Menu](http://www.apple.com/applescript/scriptmenu/) supports both.


The same goes for Brent Simmons’s [Big Cat Scripts](http://ranchero.com/bigcat/), a free contextual menu plug-in that runs scripts in two different contexts — against selected files, and against selected text.


The Big Cat plug-in adds a new “Scripts” sub-menu to your contextual menus; the contents of the Scripts sub-menu are the scripts you place in your `~/Library/Application Support/Big Cat Scripts/` folder. Inside that folder are two more folders, “Files” and “Text”. The scripts you put in the Files folder are used when you control-click on one or more files; the scripts in Text are used when you control-click on a text selection in an app like BBEdit.


I don’t use Big Cat for text scripting, but I use it almost daily for file scripting. There are a bunch of ways you can execute scripts against file selections, including Apple’s aforementioned Script Menu, but Big Cat’s contextual menu is both convenient and fast.


One of the tasks I use it for is changing HFS file and creator type metadata. For example, to take a text file and assign it to open in BBEdit, you’d set the file’s creator type to ‘`R*ch`’ (and you might as well set its file type to ‘`TEXT`’ while you’re at it).


You can accomplish this task using any of Mac OS X’s supported scripting languages.


Here’s an AppleScript:


```
on main(file_list)
   repeat with this_file in file_list
      try
         tell application "Finder"
            set file type of file this_file to "TEXT"
            set creator type of file this_file to "R*ch"
         end tell
      on error error_message
         display dialog error_message
      end try
   end repeat
end main

```


The `main()` handler is Big Cat’s convention; the selected files are passed to this handler as a list.


Here’s a tcsh shell script:


```
#!/bin/tcsh
while ("$*" != "")
    /Developer/Tools/SetFile -t "TEXT" -c "R*ch" "$1"
    shift
end

```


And here it is in Perl:


```
#!/usr/bin/perl
use strict;
use warnings;
use MacPerl;
MacPerl::SetFileInfo("R*ch", "TEXT", @ARGV);

```


Purely in terms of language syntax, I prefer the Perl version. (So shoot me.) But the AppleScript version is the only one that will work on a stock Mac OS X installation. The shell script version uses the `SetFile` tool, which is present only if you’ve installed the Mac OS X developer tools. The Perl version requires the MacPerl module — which in turn requires not only the Mac OS X developer tools, but also knowing [how to install Perl modules from CPAN](http://www.perldoc.com/perl5.8.0/lib/CPAN.html).


But even if you have installed the developer tools and know your way around CPAN, the AppleScript version has one other advantage — the Finder takes notice of what the script has done. Remember last week, when [I wrote about Nudge](http://daringfireball.net/2004/01/nudge), Rainer Brockerhoff’s contextual menu plug-in that convinces the Finder to update its file views, which is occasionally necessary because the Finder sometimes doesn’t notice when items have changed? Well, one of the many ways the Finder’s views can fall out of sync with the file system is when changes are made at the command-line level.


So, for example, take a file named index.html, which has no file or creator type associated with it. Thus, its “ownership” is determined by filename extension, which for a `.html` file probably means it’s owned by your preferred web browser. If you use a shell or Perl script to change the file and creator types, the icon for the file, as displayed by the Finder, won’t change immediately. The Finder will notice eventually — like if you switch to another app and back, or if you click on another file in the window, then click again on the file whose metadata you just changed. But it’s highly unsatisfying to run a script that says “make this a BBEdit text file”, and but not have the file’s icon changed immediately to reflect that the script actually worked as intended.


With the AppleScript version, you don’t have this problem. The Finder obviously notices that the file’s metadata has changed, because it’s the Finder itself that changes the file’s creator and file type info.


So, even in cases where I feel like it would take less time for me to write a script using Perl, I’ll use AppleScript instead if I plan to invoke the script from Big Cat’s contextual menu.



| **Previous:** | [OmniWeb 5 Public Beta](https://daringfireball.net/2004/02/omniweb_5_public_beta) |
| **Next:** | [Setting Empty File and Creator Types](https://daringfireball.net/2004/02/setting_empty_file_and_creator_types) |


PreviousNext