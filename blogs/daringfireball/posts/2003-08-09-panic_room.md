---
title: "Panic Room"
date: 2003-08-09
url: https://daringfireball.net/2003/08/panic_room
slug: panic_room
word_count: 1087
---


Miscellaneous notes following up on Thursday’s “[Microtech’s Crashtacular Zio Driver](https://daringfireball.net/2003/08/microtechs_crashtacular_zio_driver.html)”.


## /System/Library/ vs. /Library/


Several readers wrote in to ask whether Microtech’s Zio installer asked me to authenticate before proceeding with its installation. Yes, it did — it *had to* in order to put the extension inside the `/System/` folder.


As to whether it’s good form for a third-party installer to put something in `/System/`, I don’t know. Under common circumstances, there are three active “Library” folders in Mac OS X, each of which can contain system components roughly analogous to the contents of the “System Folder” in the old Mac OS — things like fonts, preference files, extensions, and control panels. There’s a Library folder in each user’s home folder; any items in this folder are only active for that user. There’s a Library folder at the root level of the startup disk; the contents of this folder are active for all users. There’s also a Library folder inside the root-level System folder; this folder is also active for all users.


The purpose of the Library folder in your home folder is obvious: it allows multiple users to have their own preferences and different components installed.
But what’s the point of having two system-wide Library folders, `/Library/` and `/System/Library/`? The basic idea is that the entire `/System/` folder (which for all intents and purposes means the `/System/Library/` folder, since in most cases it’s the only item in `/System/`) is “owned” by the OS itself. You should neither add nor remove any items within `/System/`. The contents of the `/Library/` folder, on the other hand, are configurable by any user with admin privileges.


Take fonts, for example. The fonts in `/System/Library/Fonts/` are essential to the system; Mac OS X assumes all of these fonts will always be present. There aren’t many of them (25 on my system, around half of which are for Asian languages). The fonts in `/Library/Fonts/`, on the other hand, are not essential. An admin user can remove fonts from this folder with no ill effects.


So, why does Microtech’s Zio installer put the driver in `/System/Library/Extensions/` rather than `/Library/Extensions/`? I’m not quite sure. But I notice that other third-party kernel extensions (e.g. [USB Overdrive](http://usboverdrive.com/)) install themselves within `/System/Library/Extensions/`, and Apple’s own documentation [recommends this location](http://www.opensource.apple.com/projects/documentation/howto/html/kext_tutorials/loading_kexts.html), so it seems to be either necessary — or at least recommended — for certain types of extensions. My guess is that because kernel extensions execute within the holiest of holies — the kernel — they are required to be owned by the root user, and for security purposes also need to be located in a root-owned folder. But that is just a guess. If any of you device driver hackers can fill me in, please do.


And so while Microtech’s Zio driver is damnable for numerous reasons, installing itself within `/System/` isn’t one of them — no matter how hard it is to get it out of there once installed.


## Installer Etiquette


Several readers commented via email that my Zio saga was a prime example of why they don’t like using installers in general, preferring instead drag-and-drop from a disk image or folder. I agree, but drag-and-drop installation isn’t feasible for items that need to be located in privileged locations, such as `/System/Library/Extensions/`. An installer can put things anywhere after prompting for administrator authentication. But that’s exactly what makes people uncomfortable, and understandably so. Once granted admin privileges, an installer can stick things pretty much anywhere it wants.


Good installer etiquette calls for a complete listing of what will be installed and where, displayed in the readme information before anything actually gets installed. If any items are slated to be installed in privileged locations, a brief explanation should be offered explaining why. Sure, most users will ignore it — but higher-functioning users tend to care very much about such things.


Ideally, an installer should have the ability to uninstall; but if it at least tells you what it installed and where, you can perform the uninstallation manually.


John Bergmayer emailed a recommendation for [OSXPM](http://www.apple.com/downloads/macosx/system_disk_utilities/osxpackagemanager.html) (OS X Package Manager), a free (open source) utility that allows you to inspect the contents of .pkg installers to see what they’re going to install, and where. It also allows you to uninstall packages based on the information in `/Library/Receipts/`. [Jeff Harrell](http://homepage.mac.com/jharrell/blog/index.html) recommended a similar utility, also freeware, called [DesInstaller](http://krugazor.free.fr/software/desinstaller/DesInstaller.php). DesInstaller is easier to tinker with; OSXPM loses points by coming in the form of an installer that requires authentication and sticks the app in `/Applications/Utilities/`.


Lastly, the Finder in current seeds of Panther [allows you to remove files from the `/System/` directory](http://2lmc.org/spool/id/3168), after first prompting you for authentication. That sounds dandy, similar to how BBEdit prompts for authentication when you try to save changes to a root-owned file.


## More Kernel Panic Info


In Mac OS X 10.1 and earlier, kernel panics wrote out a bunch of console messages directly on top of the screen. The messages contained technical information that might help determine the source and cause of the panic.


It was garish, if not downright frightening. An older Apple Knowledge Base article entitled “[What Is a Kernel Panic?](http://docs.info.apple.com/article.html?artnum=106076)” includes a screenshot, along with this gem of advice for recording the info:


> When a kernel panic happens, the computer is in a non-responsive
> 	state. Since you cannot take a screen shot in this situation, type the
> 	information on another computer or write it out by hand. If you have
> 	the ability to photograph the computer screen without a flash, this may
> 	be preferred.


Jaguar improved the cosmetic aspects of kernel panicking by drawing something less intimidating on screen, with instructions on how to reboot. But the same generic message is displayed for all kernel panics, with no specific information related to the cause of the current kernel panic.


The information that 10.1 and earlier wrote to the screen is still available, however. As described in the Apple Knowledge Base article “[How to Log a Kernel Panic](http://docs.info.apple.com/article.html?artnum=106228)”, the panic info is automatically written to `/Library/Logs/panic.log`.


In the case of the panics caused by my Zio, however, there was no information logged. According to Dave Nanian (of [Shirt-Pocket Software](http://www.shirt-pocket.com/)), however, if the panic info is larger than around 2 KB, it won’t get logged. And so the likely reason my Zio panics weren’t logged is that the panic generated a large amount of info.



| **Previous:** | [Microtech’s Crashtacular Zio Driver](https://daringfireball.net/2003/08/microtechs_crashtacular_zio_driver) |
| **Next:** | [The One and Only Mac OS X Extensions Folder](https://daringfireball.net/2003/08/the_one_and_only_mac_os_x_extensions_folder) |


PreviousNext