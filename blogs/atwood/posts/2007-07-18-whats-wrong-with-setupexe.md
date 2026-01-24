---
title: "What’s Wrong With Setup.exe?"
date: 2007-07-18
url: https://blog.codinghorror.com/whats-wrong-with-setupexe/
slug: whats-wrong-with-setupexe
word_count: 779
---

Ned Batchelder shares a complaint about the [Mac application installation process](https://web.archive.org/web/20070728092414/http://www.nedbatchelder.com/blog/200706.html#e20070623T082532):

kg-card-begin: html

> Here’s what I did to install the application Foo [on the Mac]:
> Downloaded FooDownload.dmg.zip to the desktop.
> StuffIt Expander launched automatically, and gave me a FooDownload.dmg Folder on the desktop.
> At this point, nothing is happening, so I opened the folder, inside was a FooDownload.dmg icon.
> I opened that, a license agreement appears.
> I agreed to that, and a window appears with an application icon, and instructions to “Drag this icon to your Applications folder.”
> I have to find the Applications folder, and drop the icon into it.
> At this point, the application is installed. To clean up, I had to:
> Close the Applications folder.
> Close the window with the dragging instructions.
> Close the FooDownload.dmg Folder window.
> Get rid of the three (!) things on the desktop: The dmg, the FooDownload.dmg Folder, and the FooDownload.dmg.zip file.
> To me, that seems like a lot of manual steps. In the Windows world, you’ll sometimes find shareware where the author gives two options: an installer, or a zip file where you can do everything yourself. The Mac installation process is like the Windows do-it-all-yourself case.
> Again, I’m not trying to slam the Mac. I genuinely do not understand why on a platform that makes things really simple, where the mantra is that stuff “just works,” ordinary users are expected to do all these manual steps.

kg-card-end: html

I’ve often wondered the same thing – **why does the Mac require the user to jump through a bunch of manual hoops to install an application?** Why not use a traditional installer (a.k.a. setup.exe) that automates this manual work for you?


To be fair, Windows applications aren’t always delivered with installers, either. One of the apps I use is Kenny Kerr’s excellent [Window Clippings](https://web.archive.org/web/20070808023437/http://www.windowclippings.com/). It’s delivered as a single executable in a compressed ZIP file. It’s a pleasingly simple arrangement, but it’s also more work me, the user. Consider how I “install” Windows Clippings:


![Manual program installation screenshot](https://blog.codinghorror.com/content/images/uploads/2007/07/6a0120a85dcdae970b0120a86d9c1d970b-pi.png)


I have to:

1. Extract the executable from the ZIP file.
2. Create a WindowsClippings folder in the C:Program Files folder
3. Move the WindowsClippings.exe file to the new folder I just created
4. Create a start menu shortcut for WindowsClippings


That’s a lot of tedious, error-prone steps I have to perform before I can run the application. And no two users will have Windows Clippings installed the same way. Some may opt to run it from their desktop, or a temporary folder, or some other inappropriate location. Is this really what we want to subject our users to?


Even as a power user, I find this level of control not only unnecessary but onerous. That’s why it’s so strange to me that the “normal” Mac install parallels the sophisticated “power user” Windows install. A typical user doesn’t want this level of control, and they certainly don’t want to [learn about disks and folders](https://blog.codinghorror.com/filesystems-arent-a-feature/). They just want the application to work. **Wouldn’t a big giant button that says “Install Me” be a better experience for the user?**


Traditional Windows installers may be easier than a Mac-style manual install, but they aren’t exactly model citizens either. Most installers ask users dozens of questions across multiple wizard pages, along with the [inevitable end user license agreement](https://blog.codinghorror.com/does-anyone-actually-read-software-eulas/) you get strong armed into accepting.


![Setup program installation screenshot](https://blog.codinghorror.com/content/images/uploads/2007/07/6a0120a85dcdae970b0120a86d9c33970b-pi.png)


The WinAmp installer is fairly typical. It’s five pages long, and asks me to decide the following:

- Do you accept our [EULA](http://en.wikipedia.org/wiki/EULA)?
- What program options do I want installed? Visualization? Extra Audio Output? User Interface Extensions?
- What icons do I want installed? Start menu? Desktop? Quicklaunch? System Tray?
- Do I want to associate WinAmp with audio files? With CDs? With playlists?
- Where do I want WinAmp installed; at what path?
- Do I want shared settings for all users or individual settings?
- What are my internet connection settings? Do I have a proxy? Do I want to download needed codecs?


That’s [a whole lot of thinking](https://blog.codinghorror.com/dont-make-me-think-second-edition/) necessary to install a tiny little music player. And that’s the *minimal* install – the lite version that the WinAmp site does its best to hide from me!


Perhaps a better approach is the “No-Questions-Asked” installation featured in [JGSoft applications](http://www.just-great-software.com/).


![Setup, no questions asked installation](https://blog.codinghorror.com/content/images/uploads/2007/07/6a0120a85dcdae970b0120a86d9c4c970b-pi.png)


If only more applications – Mac or Windows – made it this easy on the user. That’s about as close as we can get today to the big giant “Install Me” button I think most users are looking for.

[installation process](https://blog.codinghorror.com/tag/installation-process/)
[mac applications](https://blog.codinghorror.com/tag/mac-applications/)
[dmg files](https://blog.codinghorror.com/tag/dmg-files/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software installation](https://blog.codinghorror.com/tag/software-installation/)
