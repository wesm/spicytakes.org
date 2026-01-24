---
title: "Stupid Command Prompt Tricks"
date: 2005-07-06
url: https://blog.codinghorror.com/stupid-command-prompt-tricks/
slug: stupid-command-prompt-tricks
word_count: 424
---

Windows XP isn’t known for its powerful command line interface. Still, one of the first things I do on any fresh Windows install is set up the [“Open Command Window Here”](https://web.archive.org/web/20060418093757/http://www.codinghorror.com/blog/files/OpenCommandWindowHere.zip) right click menu. And hoary old cmd.exe does have a few tricks up its sleeve that you may not know about.


![](https://blog.codinghorror.com/content/images/2025/05/image-113.png)


The first thing you’ll want to do is Start, Run, cmd.exe, then right click the window menu and choose properties. Be sure to enable the following quality of life improvements:

- Options | Command History | Buffer Size | 500
- Options | Command History | Discard Old Duplicates | True
- Options | Edit Options | QuickEdit Mode | True
- Layout | Screen buffer size | Height | 999
- Layout | Window size | Height | 50


Now we’ve got some room to actually see stuff! QuickEdit mode enables copying from the command prompt by intuitively dragging and right clicking with the mouse. Furthermore, you can paste what’s in the clipboard to the command line by right clicking with nothing selected.


And of course, set the font and colors to taste. I use green-screen style colors (background 0 55 0, foreground 0 255 0) with Lucida Console as pictured above. But if you prefer [Comic Sans](https://blog.codinghorror.com/comic-sans-the-font-of-the-gods/) here, be my guest! When exiting this dialog, you’ll be prompted to save. Make sure you select “Save properties for future windows with same title” so all future command prompts will benefit from these improved settings.


There are also a few helpful keyboard shortcuts that aren’t always widely known:

- Pressing arrow up selects a previous command from your command history; similarly, arrow down selects the next command.
- Pressing F7 pops up your command history list.
- You can drag n’ drop files or folders from an explorer window into a command prompt; this inserts the quoted path as if you had manually pasted it.
- [Tab completion](http://en.wikipedia.org/wiki/Tab_completion) is fully supported; type edit *.ini then hit TAB to iterate through all matches. Use SHIFT+TAB to move to the previous match. This works for partial filenames as you would expect, and in all commands.
- Tired of the typical "c:windowssystem32cmd.exe" window title? Change it using the TITLE command.
- ALT+ENTER takes your command prompt to full screen mode and back again.


If you’re really a hard-core cmd.exe junkie (or maybe a UNIX user), you may want to look into the [4nt command shell replacement](https://web.archive.org/web/20060414165242/http://msmvps.com/blogs/coad/archive/2005/02/19/36473.aspx). It’s a direct descendant of the venerable 4dos shell.

[command-line](https://blog.codinghorror.com/tag/command-line-2/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[cmd.exe](https://blog.codinghorror.com/tag/cmd-exe/)
[command prompt tricks](https://blog.codinghorror.com/tag/command-prompt-tricks/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
