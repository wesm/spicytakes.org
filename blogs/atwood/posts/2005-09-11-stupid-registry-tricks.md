---
title: "Stupid Registry Tricks"
date: 2005-09-11
url: https://blog.codinghorror.com/stupid-registry-tricks/
slug: stupid-registry-tricks
word_count: 631
---

Scott Hanselman’s [Power User Windows Registry Tweaks](https://web.archive.org/web/20051223150154/http://www.hanselman.com/blog/CommentView,guid,e4786810-658a-4079-8723-05fad6b1c721.aspx) has some excellent registry editing tweaks. I’ve spent the last few hours poring over those registry scripts, enhancing and combining them with some favorites of my own. Here are the results:


![](https://blog.codinghorror.com/content/images/2025/05/image-138.png)

- [Open Command Window Here](https://web.archive.org/web/20060418093757/http://www.codinghorror.com/blog/files/OpenCommandWindowHere.zip)
Adds a right-click menu to all Explorer folders that launches a command prompt window (cmd.exe) at that folder. Incredibly handy.
- [Force Start, Search to search all filetypes](https://web.archive.org/web/20060225204314/http://www.codinghorror.com/blog/files/SearchUnknownExtensionsForXP.zip)
For some godforsaken reason, Start, Search only searches files with [known extension associations](http://www.geekrant.org/2004/11/22/windows-xp-search) by default. I’ve run into this “feature” before and I nearly pulled my hair out trying to figure out why it couldn’t find the source file that I knew was there. This registry fix forces it to search all files, as you would expect. Really a no-brainer.

kg-card-begin: html
- [Improve the Disk Cleanup Wizard](https://web.archive.org/web/20071019180618/http://www.codinghorror.com/blog/files/ImproveDiskCleanup.zip)
Microsoft added a [Disk Cleanup wizard](https://web.archive.org/web/20060326093850/http://www.dummies.com/WileyCDA/DummiesArticle/id-2633,subcat-OS.html) in Windows 98, which all subsequent versions have inherited. It’s located at Start, Accessories, System Tools, Disk Cleanup. Unfortunately it kinda sucks. Via the wonders of registry editing, you can change this annoying, useless tool into something that’s actually *effective*:



Remove the time-consuming, useless “compress old files” rule
Make rules stricter for files in the temporary folder
Add rule to check entire disk for temporary files
Add rule to remove unnecessary files in Windows folder
Add rule to remove debug dump files


With these changes, I get a first run Disk Cleanup savings of ~11 megabytes on a clean Windows XP install in a VM. Nothing refreshes like giving the Windows undercarriage [a little how’s your father](http://www.imdb.com/title/tt0118655/quotes). If you can think of any other files in a typical Windows install that are completely safe to remove*, let me know, and I can modify the .reg file to incorporate them as well.


This should probably go without saying, but we are deleting stuff here. Use this at your own risk. For what it’s worth, I have used it on several of my machines and inside a VM with excellent results.

kg-card-end: html
- [My Computer right-click menu additions](https://web.archive.org/web/20060509170529/http://www.codinghorror.com/blog/files/AddMyComputerRightClickMenus.zip)
Wouldn’t it be cool if you could right click My Computer and bring up the registry editor? Or the service manager? Or Add/Remove Programs? With this registry editing batch file, you can. In fact, you can add as many commands to the My Computer right-click menu as you like. Once you try it, you’ll wonder why these menu options (see screenshot) aren’t there to begin with. I changed this script from a plain .reg file to a batch file that calls the REG.EXE command. Why? Because it’s far easier to modify this script to taste when you can see the actual right-click command lines as a plain string. For some reason, regedit can only import/export the REG_EXPAND_SZ key as a byte array, even though it’s just a basic string with an environment variable in it (e.g., %windir%). The alternative is to eschew the use of environment variables entirely and hard-code the windows and folder paths as plain REG_SZ strings.


In the cases where there are a number of modifications to the registry, I also included a copy of the unmodified registry key in the zip file. If you don’t like the results, delete the key and re-import the default registry file to get back to square one.


Scott’s post has some additional registry tweaks, including one that puts notepad.exe on every right click menu. I prefer to do this using the **built in Send To functionality**: just put a shortcut to the editor of your choice in the %USERPROFILE%SendTo folder and it will automatically appear in the right-click Send To list for all files. I suppose it is one more click, but I prefer it this way.


*Insert LINUX joke here.

[registry](https://blog.codinghorror.com/tag/registry/)
[windows](https://blog.codinghorror.com/tag/windows/)
[tweaks](https://blog.codinghorror.com/tag/tweaks/)
[command line](https://blog.codinghorror.com/tag/command-line/)
[file search](https://blog.codinghorror.com/tag/file-search/)
