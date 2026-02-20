---
title: "Note to those using Inno Setup…"
date: 2007-03-05
url: https://www.kalzumeus.com/2007/03/06/note-to-those-using-inno-setup/
slug: note-to-those-using-inno-setup
word_count: 118
---


… don’t forget to set the working directory for the shortcuts you create.  I had assumed Windows would automatically default to the program directory.  This is apparently not the case on some systems, and its been causing some extraordinarily quirky behavior for some of my users.  (v1.05 and 1.051 use Java’s facility to locate the working directory rather than using the directory the .exe is in, because that logic was causing problems for the Mac port.  Unfortunately, on at least some systems they’ll default to somewhere else instead.  I hadn’t noticed this problem because Inno Setup actually does set a sensible default working directory when you execute the program directly from the installer.)


*sigh* Time for a 1.052.
