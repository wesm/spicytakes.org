---
title: "Changing the Windows XP Boot Screen"
date: 2005-10-01
url: https://blog.codinghorror.com/changing-the-windows-xp-boot-screen/
slug: changing-the-windows-xp-boot-screen
word_count: 256
---

We’re in the middle of an after-hours [MAME](http://www.mame.net/) arcade project at work.* As one of the final fit and finish steps, I did a bit of research on how to **replace the default Windows XP boot screen** with something a little more arcade-y. I came up with StarDock’s excellent [BootSkin](https://web.archive.org/web/20051013064920/http://www.stardock.com/products/bootskin/):


![](https://blog.codinghorror.com/content/images/2025/03/image-297.png)


This free app makes it painless to swap out your Windows XP boot screen or even create your own. The only downside is that you’re **limited to a 16 color 640x480 image**. Thankfully, that’s 16 colors of your choice, not the classic default 16 “Windows” colors. This appears to be a technical limitation of the XP boot process itself. The app packages up the images into “bootskins,” which are simply zip files with a .bootskin extension.


There are a few hundred [user created bootskins](https://web.archive.org/web/20061109162635/http://www.wincustomize.com/Skins.aspx?LibID=32) to choose from at WinCustomize. I found a **Windows 1.01 bootskin**, but the author didn’t do a good job of scaling the image, so it looked horrible. I reformatted it so it’s pixel perfect:

- [Windows 1.01 bootskin](https://web.archive.org/web/20061006160906/http://www.codinghorror.com/blog/files/Windows101.bootskin.zip) (3kb, remove .zip extension after download)


If you’re worried about the effects of this boot screen change, try it in a Virtual PC or VMWare image first. There’s a similar StarDock app, [LogonStudio](https://web.archive.org/web/20051102002322/http://www.stardock.com/products/logonstudio/), which allows you to customize the XP logon screen as well. I don’t need to bother with this; our MAME computer automatically logs a user in via the [TweakUI PowerToy](https://web.archive.org/web/20051004133747/http://www.microsoft.com/windowsxp/downloads/powertoys/xppowertoys.mspx) login tab.


*It’s impressive. There will be more on this later... ;)

[windows](https://blog.codinghorror.com/tag/windows/)
[bootscreen](https://blog.codinghorror.com/tag/bootscreen/)
[windows xp](https://blog.codinghorror.com/tag/windows-xp/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
