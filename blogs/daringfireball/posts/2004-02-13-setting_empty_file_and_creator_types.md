---
title: "Setting Empty File and Creator Types"
date: 2004-02-13
url: https://daringfireball.net/2004/02/setting_empty_file_and_creator_types
slug: setting_empty_file_and_creator_types
word_count: 853
---


OK, so I just demonstrated [how to set HFS file and creator types](https://daringfireball.net/2004/02/scripting_file_and_creator_types) using AppleScript, Perl, and shell scripts. But what if you don’t want to *set* the types, but instead *remove* them, so as to allow Launch Services to determine the file type and default app from the filename extension?


Yes, I’m a big fan of file type and creator metadata. But supporting file type and creator metadata isn’t mutually exclusive with supporting Launch Services-style filename extension app assignment. [Anti-HFS-metadata propaganda](https://daringfireball.net/2003/07/finding_avie) notwithstanding, Mac OS X currently offers a best-of-both-worlds approach to determining how a file is bound to a default application.


Top priority is given to custom per-file bindings assigned through the Finder’s Get Info command. These are stored in the resource fork of a file, in ‘`icns`’ and ‘`usro`’ resources, which, [as noted by Michael Tsai](http://mjtsai.com/blog/2004/01/27/bruce_horn_interview.html), is a bit surprising given Apple’s antipathy toward resource forks in the Mac OS X era. HFS creator type metadata has second priority, followed by filename extensions.


(Contrary to widespread misconception, HFS file and creator types are *not* stored in the resource fork, they’re simply metadata fields defined by the file system itself, just like the filename and date fields.)


This hierarchy, in which creator types have precedence over filename extensions, works great. (You can actually *see* the hierarchy using Rainer Brockeroff’s [XRay file info utility](http://www.brockerhoff.net/xray/).)


In general, the way I tend to make use of these rules is to rely on file type and creator metadata for files that I’m working on, but let filename extensions 
control files that I only want to read or view. If it’s an HTML file I’m editing, I want it to open in BBEdit; if it’s an HTML file I just want to read, however, then I want it to open in my default web browser. Thus, if I switch to a [new default web browser](https://daringfireball.net/2004/02/omniweb_5_public_beta), any HTML files which don’t have creator types switch with me automatically.


But so how do you strip file and creator types from a script?


The obvious solution would be to set the values to empty strings. E.g., in AppleScript:


```
tell application "Finder"
   set file type of this_file to ""
   set creator type of this_file to ""
end tell

```


Or in Perl:


```
MacPerl::SetFileInfo('', '', @ARGV);

```


But this doesn’t work. In the AppleScript version, the Finder fails with an error: “Can’t make some data into the expected type.” The Perl version runs without error, but the file type and creator fields end up getting set to garbage values, rather than empty strings.


The problem is that HFS file and creator types aren’t really strings; they’re OSType values, which are exactly four bytes. It’s relatively easy to treat a four-byte OSType value as a four-character MacRoman-encoded string, and so that’s how they’re typically displayed. It’s also easy to coerce a four-character string into an OSType. What you can’t do, however, is coerce to OSType a string of any other length. For example, the file type for PDF files is *not* ‘`PDF`’, but rather ‘`PDF `’, with a trailing space.


And thus the problem with the above script snippets — you can’t coerce a zero-length string into a four-byte OSType.


At one point in time back in the 1990s, the Apple-sanctioned way to specify “unknown” file and creator types was to use the value ‘`????`’. As far as I can tell, this is no longer officially sanctioned, but it does seem to work — if you set a file’s creator and file type to ‘`????`’, the Finder seems to treat it the same way it does un-typed files. Likewise for the value ‘`    `’ (four spaces).


But those are workarounds, not genuine solutions. My friend and former colleague Jim Correia provided me with the solution. The trick is to think like a C/C++ programmer (like Jim), not a scripter (like me). I was banging my head against the wall, trying to coerce an empty string into an empty OSType. But OSType values are never truly “empty” — they’re always exactly four bytes. What looks like an “empty” OSType is actually four bytes, *each byte with a value of zero*.


Jim’s AppleScript solution:


```
on main(filelist)
   set nullCh to ASCII character 0
   set nullFourCharCode to nullCh & nullCh & nullCh & nullCh
   repeat with this_file in filelist
      try
         tell application "Finder"
            set file type of this_file to nullFourCharCode
            set creator type of this_file to nullFourCharCode
         end tell
      on error error_message
         display dialog error_message
      end try
   end repeat
end main

```


`ASCII character 0` is a byte with the value zero; so we just create a string consisting of four of these characters, and we’re in business.


Here’s my translation to Perl:


```
#!/usr/bin/perl
use strict;
use warnings;
use MacPerl;
MacPerl::SetFileInfo("\0\0\0\0", "\0\0\0\0", @ARGV);

```


(Also, thanks to [Chris Nandor](http://use.perl.org/~pudge/journal/) — who maintains the entire Mac::Carbon bundle of Perl modules, including MacPerl — for pointing out via email that SetFileInfo() can take a *list* of file arguments, obviating the loop I used in my original Perl script yesterday.)



| **Previous:** | [Scripting File and Creator Types](https://daringfireball.net/2004/02/scripting_file_and_creator_types) |
| **Next:** | [48 Hours](https://daringfireball.net/2004/02/48_hours) |


PreviousNext