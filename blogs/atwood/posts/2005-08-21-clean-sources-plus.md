---
title: "Clean Sources Plus"
date: 2005-08-21
url: https://blog.codinghorror.com/clean-sources-plus/
slug: clean-sources-plus
word_count: 344
---

Omar Shahine’s [Clean Sources](https://web.archive.org/web/20051027104328/http://wiki.shahine.com/default.aspx/MyWiki/CleanSources.html) is a nifty little right-click app for .NET developers:


> This application does one thing. It adds an explorer shell menu to folders that when selected will recursively delete the contents of the bin, obj and setup folders. If you have a .NET project that you wish to share with someone, this is useful to remove the unnecessary stuff from the folder before you zip it up and send it off.


There’s one glaring omission here, though. **The source control bindings aren’t removed! **And neither are the local user setting files. I finally had some time, so...


Presenting **Clean Sources Plus**. It adds a right-click menu to folders that does the following:

- Removes bin, obj, Debug and Release folders
- Removes source control bindings from project and solution files
- Removes user setting files


The result is a very clean, minimal set of .NET solution files, suitable for upload or sharing.

kg-card-begin: html

Updated to version 1.1 on 11/10/05 with the following new features:

kg-card-end: html
- Added second context menu “Clean and Zip Sources” which also zips the entire folder contents into a single zip file. This zip file is placed in the root folder and shares the same name as the folder.
- The regex patterns used to determine what files and folders to delete are now set in the .config file. This way you can customize what gets deleted without recompiling.


I tested this with both C# and VB projects, but I’m not 100% sure it works for all other types of projects. It shouldn’t break anything, but I may have missed some oddball project type (database? setup?) source bindings. And I only tested against the typical SourceSafe bindings. Anyway, test it out and let me know if there are any issues.*

- [Download the Clean Sources Plus 1.1 VS.NET 2003 solution](https://github.com/coding-horror/CleanSourcesPlus)


You may also be interested in [TreeTrim](http://code.google.com/p/treetrim/), which is based on this project.


*If this app deletes all your source code, then it’s Omar’s fault.

[.net](https://blog.codinghorror.com/tag/net/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[coding tools](https://blog.codinghorror.com/tag/coding-tools/)
[development practices](https://blog.codinghorror.com/tag/development-practices/)
[automation](https://blog.codinghorror.com/tag/automation/)
