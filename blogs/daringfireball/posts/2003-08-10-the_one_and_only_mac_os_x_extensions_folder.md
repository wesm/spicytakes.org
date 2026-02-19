---
title: "The One and Only Mac OS X Extensions Folder"
date: 2003-08-10
url: https://daringfireball.net/2003/08/the_one_and_only_mac_os_x_extensions_folder
slug: the_one_and_only_mac_os_x_extensions_folder
word_count: 575
---


So here’s the deal regarding third-party kernel extensions being installed in `/System/Library/Extensions/`.


Mac OS X uses a concept of *file-system domains* to control access to system resources. The four domains are: User, Local, Network, and System. The User domain is everything in your home folder. The Network domain contains resources shared across multiple Macs on a network; most users don’t use this. The Local domain consists of things that are shared across all users on a single machine; for example, the top-level Applications folder. Files in the Local domain can be added or removed by any users with administrator privileges.


The System domain consists of everything within the  `/System/` folder on the boot volume. It is owned and control by Mac OS X itself, and even admin users can’t modify its contents.


Each domain gets its own Library folder. That’s why there are two Library folders that affect all users, `/Library/` and `/System/Library/` — the first is for the admin-user-controlled Local domain, the second for the system-controlled System domain.


The rule of thumb: Everything in `/System/` is from Apple, and is considered an essential component of Mac OS X.


The exception, however, is `/System/Library/Extensions/`. This is the *only* folder that Mac OS X checks for kernel extensions that need to load during the boot process. Not all kernel extensions need to load during the boot process, but ones that do must go here or they won’t load.


This is documented in [Mac OS X System Overview, Chapter 9: The File System](http://developer.apple.com/documentation/MacOSX/Conceptual/SystemOverview/FileSystem/chapter_9_section_2.html#//apple_ref/doc/uid/20000986/BCIIGGHG). There, in listing the contents of a Library folder, the Extensions folder is described as:


> Device drivers and other kernel extensions (system domain only).


And because the “system domain” means everything within `/System/`, we can see that `/System/Library/Extensions/` is the only currently supported location for kernel extensions.


Non-boot loading kernel extensions — which are typically loaded by applications at run time — can go anywhere. Or at least, they can go anywhere where the apps that need them know to look for them. Some applications, such as [PGP](http://www.pgp.com/products/personal/index.html), install their non-boot-loading extensions in `/Library/Extensions/`. However, this is *not* an Apple-sanctioned location, and has no special properties.


More details on these issues, as well as some of the thinking behind the engineering decisions behind them, can be found in [this illuminating December 2002 post to Apple’s Darwin Development mailing list](http://lists.apple.com/archives/darwin-development/2002/Dec/msg00083.html) by Apple engineering manager Dean Reece. Wrote Reece:


> The reasons we don’t support [/Library/Extensions/] now are not
> 	really technical showstoppers, but adding another place for both BootX
> 	and the kext tools to look, plus managing two separate caches, adds
> 	some complexity with little real (end-user) benefit.  It also adds some
> 	(small) risk to the bootability of the system, since the more paths the
> 	booter has to traverse, the more chances that a corrupt root filesystem
> 	will be unbootable.  This was discussed during the design of the kext
> 	system, and we decided that both the risk and the benefit were small,
> 	so we decided on the simpler solution (one location).


Reece’s full post is well-worth reading if you’re even vaguely interested in this sort of thing. (Note that as a meager defense against email-address-harvesting spambots, Apple protects its public mailing list archives with a username and password — but they tell you the username and password to use in the authentication message.)



| **Previous:** | [Panic Room](https://daringfireball.net/2003/08/panic_room) |
| **Next:** | [Text Editing News](https://daringfireball.net/2003/08/text_editing_news) |


PreviousNext