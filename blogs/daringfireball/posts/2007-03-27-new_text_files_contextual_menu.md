---
title: "Creating New Text Files From the Finder’s Contextual Menu"
date: 2007-03-27
url: https://daringfireball.net/2007/03/new_text_files_contextual_menu
slug: new_text_files_contextual_menu
word_count: 338
---


So I saw [this post on TUAW](http://www.tuaw.com/2007/03/27/another-way-for-switchers-to-make-new-files/) about NuFile, a contextual menu plugin that gives you a shortcut to create new files in the Finder using the contextual menu.


I thought that sounded pretty cool, but I’d only ever use it for creating text files. So I wrote an AppleScript for Brent Simmons’s freeware [Big Cat Scripts Plugin](http://ranchero.com/bigcat/) that does just that. Here’s how to use it:

1. If you haven’t done so already, download and install [Big Cat
Scripts](http://ranchero.com/bigcat/).
2. Copy the script below, paste it into your script editor, and
save it in your *~/Library/Application Support/Big Cat
Scripts/Files/*. I named my script “New Text File”.
3. Control-click in any Finder window and choose your script from
the Scripts sub-menu.
4. A dialog box will appear, prompting you for a file name. Enter a name,
then click Create.
5. The file will be created and opened for editing in your preferred text
editor. (See below.)


Here’s the script:


```
on main()
   tell application "Finder"
      try
         set _folder to (the target of the front window) as alias
      on error
         beep
      end try

      display dialog ¬
         "New text file name:" default answer "" buttons ¬
         {"Cancel", "Create"} default button 2
      set _fname to text returned of result
      if exists file _fname of _folder then
         display alert "A file named ‘" & _fname & ¬
            "’ already exists in this folder." as informational
         return -- ends script
      end if

      set _path to quoted form of ((POSIX path of _folder) & _fname)
      do shell script "bbedit " & _path
   end tell
end main

```


The `do shell script` line at the end of the script assumes that your favorite text editor has a command-line tool, and that the tool is available in your shell’s `PATH`. If you use TextWrangler, change the “`bbedit`” tool to “`edit`”; if you use TextMate, change it to “`mate`”; and if you use SubEthaEdit, change it to “`see`”.



| **Previous:** | [The 2007 Daring Fireball Membership Drive](https://daringfireball.net/2007/03/2007_df_membership_drive) |
| **Next:** | [Regarding the Members-Only Feeds](https://daringfireball.net/2007/03/regarding_the_members_only_feeds) |


PreviousNext