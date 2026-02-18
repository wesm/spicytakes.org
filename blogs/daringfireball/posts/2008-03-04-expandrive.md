---
title: "ExpanDrive"
date: 2008-03-04
url: https://daringfireball.net/2008/03/expandrive
slug: expandrive
word_count: 1169
---


[ExpanDrive](http://www.magnetk.com/expandrive) 1.01 is a new $29 file system extension for Mac OS X, based in part on [MacFUSE](http://code.google.com/p/macfuse/),1 that lets you mount SFTP servers as volumes in the Finder. I’ve been using ExpanDrive for a week and it is extremely impressive. I’ve never seen anything like it for the Mac. Magnetk, the company behind ExpanDrive, has a similar product for Windows called [SftpDrive](http://www.sftpdrive.com/) that’s been around for a while.


For many typical tasks, ExpanDrive is far more convenient and seamless than a standalone client like Interarchy or Transmit. You don’t have to worry about uploading or downloading, it works more like a USB flash drive — you just save and open files directly. If you open remote files checked out of an SVN (or other revision control system) repository, you can use the built-in SVN commands in BBEdit or TextMate, just as though the files were part of a repository checked out on your local drive. That’s always been a huge annoyance for me using the remote file editing features in standalone file transfer apps.


As a remote network protocol, it works better in the Finder than anything I’ve ever used on Mac OS X — far more responsive than WebDAV or AFP, both of which, for me, have always been one-way tickets to Beachball City. ExpanDrive’s low latency and reliability put .Mac’s WebDAV-based iDisk to shame. ExpanDrive even works well when you change networks — you can mount a volume, put your laptop to sleep, then wake it up on a different Wi-Fi network and the mounted SFTP volume continues to work as though nothing had changed.


ExpanDrive is not perfect, but the only significant downside I’ve encountered is that, because servers mounted via ExpanDrive are treated like first-class volumes by Mac OS X, you wind up with “.DS_Store” files on the remote volume. You can’t use [the hidden Desktop Services defaults preference](http://docs.info.apple.com/article.html?artnum=301711) to suppress them, because ExpanDrive’s volumes are treated by Mac OS X as local drives, not network shares, and that preference only applies to network shares. Spotlight, on the other hand, seems to know not to attempt to index ExpanDrive volumes.


**Update:** The .DS_Store problem [is a known issue](http://forum.magnetk.com/index.php/topic,588.0.html), and Magnetk developer Jeff Mancuso says a fix is planned for a future release.


## User Interface Notes


ExpanDrive *is* an application, and it must be running in order to mount volumes via SFTP. However, it’s a [UIElement](http://www.cocoadev.com/index.pl?LSUIElement) application — it does not appear in your Dock and doesn’t have a menu bar. Instead it appears as a system-wide menu bar item:


The main interface is decidedly minimal: a single window listing your saved “drives” (which are more or less equivalent to bookmarks in a typical file transfer app) and three buttons: “New Drive”, a contextual menu, and help. The green circle in the list indicates a drive that is currently mounted.


One thing that wasn’t obvious to me is how you edit the settings of a saved drive. For a mounted volume, the only items in the contextual menu are “Open in Finder” and “Unmount”:


The trick is that ExpanDrive only allows you to edit the settings of drives that aren’t currently mounted — *and* only shows that it’s even possible to do so when the drive is not mounted:


Those icons in the context menu are unnecessary; they’re distracting rather than helpful, and the whole idea of putting small icons next to every menu item feels Windows-y. The command keys are wrong: Command-C should never be used for anything other than Copy, and Command-D is a reasonable guess (from a user’s perspective) for “Duplicate”, but in ExpanDrive it’s mapped to “Delete”. Worse, when you delete a drive, you’re not prompted to confirm and can’t undo the deletion. “Connect” should use Command-K, and “Delete” should use Command-Delete — both of which shortcuts would parallel those of the Finder.


The Preferences window is a weird duck:


The Save button is positioned at a seemingly random position. The group box surrounding the checkboxes is entirely needless. And there’s no reason for both a Save button and regular window close button if both do the same thing, which, in this case, they do. (One might assume that if you don’t click Save, but simply close the window, changes are discarded, but that’s not the case.) The Save button and group box should be removed. (As should the cutesy option to disable “Superfluous visual effects”, which effects, so far as I can tell, are to fade ExpanDrive’s own windows in and out when they open and close.)


Lastly, if you attempt to quit ExpanDrive while drives are still mounted, you get this dialog, which could serve as the poster child for the *Don’t Use “Yes” and “No” as Button Names* campaign:


The buttons are named “Yes” and “No” but the dialog doesn’t even ask a question. Action verbs almost always make for better button names than “Yes” and “No”. Ideally, the user should be able to figure out what their options are even if they only read the button names and ignore the explanatory text. Compare and contrast to Apple’s dialog for the system’s Log Out command, which asks a clear question and uses actions for the button names:


## Installation


In addition to the ExpanDrive application, the installer also installs a filesystem extension in the top-level */Library* folder, along with some FUSE-related headers and library files. Similar to [my complaints regarding Google Desktop](http://daringfireball.net/2007/04/google_desktop_installer) a year ago, these files — what they are, where they go — are completely undocumented by Magnetk. In addition to the application, here’s what got installed on my machine:


```
/Library/Filesystems/fusefs.fs/
/Library/Frameworks/MacFUSE.framework:/
/usr/local/include:
    fuse/
    fuse.h
    ulockmgr.h
/usr/local/include/fuse:
    fuse.h
    fuse_common.h
    fuse_common_compat.h
    fuse_compat.h
    fuse_darwin.h
    fuse_lowlevel.h
    fuse_lowlevel_compat.h
    fuse_opt.h
/usr/local/lib:
    libfuse.0.0.0.dylib@
    libfuse.0.dylib*
    libfuse.a
    libfuse.dylib@
    libfuse.la*
    libulockmgr.0.0.0.dylib@
    libulockmgr.0.dylib*
    libulockmgr.a
    libulockmgr.dylib@
    libulockmgr.la*
    pkgconfig/
/usr/local/lib/pkgconfig:
    fuse.pc

```


There is no uninstaller, and it’s unclear to me whether the version of MacFUSE installed with ExpanDrive differs at all from the standard MacFUSE distribution. The [uninstallation instructions on Magnetk’s web site](http://www.magnetk.com/support/expandrive/installation) do not mention these files, but should.


---


Niggling criticisms of the UI and installer aside, ExpanDrive is without question worth a look for anyone who spends time editing files on remote servers. My first impression after reading ExpanDrive’s promotional description last week was that it sounded too good to be true. One week later, I’m pretty sure it actually *is* that good.


---

1. MacFUSE is an open source Mac implementation of the Linux FUSE system for extensible *userspace* (i.e. not running in the kernel) file systems. One of those that works with MacFUSE is [sshfs](http://fuse.sourceforge.net/sshfs.html), which more or less attempts to do the same thing as ExpanDrive. I have not used MacFUSE/sshfs, but ExpanDrive [seems better](http://discuss.joyent.com/viewtopic.php?pid=174203) than sshfs in every way: faster, more reliable, lower latency. Sshfs, for example, does not reconnect automatically when you change networks or wake from sleep; ExpanDrive handles these things with aplomb. ↩︎



| **Previous:** | [iPhone SDK Rumors and Speculation](https://daringfireball.net/2008/03/iphone_sdk_rumors) |
| **Next:** | [iPhone Enterprise and SDK: First Impressions and Questions](https://daringfireball.net/2008/03/iphone_sdk_impressions_and_questions) |


PreviousNext