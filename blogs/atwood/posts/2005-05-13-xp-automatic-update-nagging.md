---
title: "XP Automatic Update Nagging"
date: 2005-05-13
url: https://blog.codinghorror.com/xp-automatic-update-nagging/
slug: xp-automatic-update-nagging
word_count: 336
---

Windows XP’s automatic update facility is clearly a good thing. Except when an update is installed that requires a reboot and you’re working on the computer at the time. Then you get this lovely dialog:


![](https://blog.codinghorror.com/content/images/2025/05/image-90.png)


As if I needed another reason to [hate dialog boxes.](https://blog.codinghorror.com/death-to-the-dialog-box/) This is perhaps the Naggiest. Dialog. Box. *Ever*. It can’t be dismissed. You get two choices – Restart Now, or Restart Later. **If you click Restart Later, it pops up again ten minutes later, like clockwork.** It belongs to wuauclt.exe, part of the Microsoft automatic update provider. I tried killing wuauclt.exe, and like a bad zombie movie, it keeps coming back.


I want automatic updates, but I also want to restart my computer when I feel like it. **Is there any way to turn off this incredibly annoying nag dialog? **UPDATE: Thanks to the many commenters, we now have at least two ways to disable Mister Naggy McNaggerson:


**1. Stop the “Automatic Updates” service.**

kg-card-begin: html

> Navigate to Control Panel | Administrative Tools | Services:
> Right click the Automatic Updates service and stop it. You can also do the same thing at the command line by typing:
> net stop wuauserv
> or you can type this, which does the same thing, and is a little easier to remember:
> net stop “automatic updates”
> After the service is stopped, the nag message stops, too. Then you can reboot when you have time. The service will restart when you reboot.

kg-card-end: html

**2. Modify Group Policy settings.**

kg-card-begin: html

> Start, Run “gpedit.msc” to bring up the group policy editor. Then navigate to the folder
> Local Computer Policy
> Computer Configuration
> Administrative Templates
> Windows Components
> Windows Update
> There are two settings and both will work, so it’s your choice. Either enable **No auto-restart for schedule Automatic Updates installations** or set **Re-prompt for restart with scheduled installations** to a long time interval, like 1440 minutes.

kg-card-end: html
[windows](https://blog.codinghorror.com/tag/windows/)
[xp](https://blog.codinghorror.com/tag/xp/)
[automatic updates](https://blog.codinghorror.com/tag/automatic-updates/)
[reboot nag](https://blog.codinghorror.com/tag/reboot-nag/)
[wuauclt](https://blog.codinghorror.com/tag/wuauclt/)
