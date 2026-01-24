---
title: "Automated Hard Drive Defragmentation"
date: 2005-12-20
url: https://blog.codinghorror.com/automated-hard-drive-defragmentation/
slug: automated-hard-drive-defragmentation
word_count: 347
---

I tend to ignore **defragmenting my hard drive** until I belatedly realize it probably looks like swiss cheese by now:


![](https://blog.codinghorror.com/content/images/2025/03/image-385.png)


Wouldn’t it be nice if **the operating system took care of defragmentation all by itself in the background when I’m not using the computer?** Ah, to dream. Until that happens, there’s at least one simple workaround.


Windows XP includes a disk defragmenting utility in Start, Programs, Accessories, System Tools. What’s less commonly known, however, is that XP *also* includes the command line version of this utility, **defrag.exe**:

kg-card-begin: html

```

C:>defrag c: -f
Windows Disk Defragmenter
Copyright (c) 2001 Microsoft Corp. and Executive Software International, Inc.
Analysis Report
279 GB Total,  116 GB (41%) Free,  12% Fragmented (8% file fragmentation)
Defragmentation Report
279 GB Total,  116 GB (41%) Free,  0% Fragmented (0% file fragmentation)
C:>

```

kg-card-end: html

It’s easy enough to hook up automated disk drive defragmenting using defrag.exe and XP’s task scheduler. Just go to Start, Control Panel, Scheduled Tasks and click “Add Scheduled Task.” You’ll need to edit the task properties manually to set up the proper command line syntax, as pictured here:


![](https://blog.codinghorror.com/content/images/2025/03/image-384.png)


I assume the defrag utility needs to run as an administrator, so set the “Run as” section appropriately.


If you have more than one drive, you can set up multiple scheduled tasks, or use this Windows Script Host file to defragment all the drives in one fell swoop:

kg-card-begin: html

```

Option Explicit
Dim sh, fso, d
Set sh = WScript.CreateObject(“WScript.Shell”)
Set fso = CreateObject(“Scripting.FileSystemObject”)
For Each d in fso.Drives
If d.DriveType = 2 Then
sh.Run “defrag ” & d & “ -f -v”, 1, true
End If
Next

```

kg-card-end: html

I’m sure commercial disk defragmenters do a better job, but this one’s good enough – and it’s free! However, you may want to complement defrag.exe with SysInternals’ PageDefrag utility. Some crucial system files, such as the registry hive, are always locked while the OS is running. But with PageDefrag, you can defragment those files at boot time.

[disk defragmentation](https://blog.codinghorror.com/tag/disk-defragmentation/)
[operating system](https://blog.codinghorror.com/tag/operating-system/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[command line](https://blog.codinghorror.com/tag/command-line/)
[task scheduler](https://blog.codinghorror.com/tag/task-scheduler/)
