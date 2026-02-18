---
title: "A Quick, Possibly Incomplete Guide to What Gets Installed by the Google Desktop Installer"
date: 2007-04-04
url: https://daringfireball.net/2007/04/google_desktop_installer
slug: google_desktop_installer
word_count: 1172
---


Mac software is usually distributed in a way that encourages simple drag-and-drop installation. A disk image or zip archive that the user opens, then a single file (or bundle) that the user can drag to somewhere such as the Applications folder. Uninstallation in such cases requires dragging the same file to the Trash.


When that’s not possible or feasible, usually due to software that requires additional components, I much prefer when software uses Apple’s own installer tool. One of the nice features of Apple’s installer is the Show Files command in the File menu, which gives you a nice listing of everything the installer is going to install, *before* it happens.


Today, Google released [Google Desktop for Mac](http://desktop.google.com/mac), which, in a nutshell, is more or less a competitor to Spotlight. I’ve only had time to give it a cursory examination, but it’s clearly a deep and complex set of software. I say “set” because Google Desktop is not just one piece of software, it’s a system with numerous components. A simple drag-and-drop installation wouldn’t work.


But Google doesn’t use Apple’s standard installer, either. Google Desktop is delivered using another new Google app, called Google Updater. This app is a meta installer for various Google Mac apps, including, as of today, Google Desktop, Earth, Notifier, and Picasa Uploader. It doesn’t contain the software for any of these apps; instead, it downloads the latest version when you choose to install or update one of them. It also provides a simple one-button interface for uninstalling these apps.


It’s a slick, easy-to-use piece of software, but alas, it lacks anything like the aforementioned Show Files feature of Apple’s installer. There’s no way to tell what files it’s going to install, or where.


This matters with Google Desktop, because there are a lot of files, and they’re installed into some interesting — if not suspicious — locations.


I won’t install software like this on my main machine without knowing everything that’s going to be installed. So I installed Google Desktop on a test machine — an iMac G4 running Mac OS X 10.4.9. Before the installation, I used the Unix `ls` command to generate a list of every file on the startup drive. I ran the same command again after installation and searched for differences.


**Update:** It ends up that behind the scenes, Google Updater does its thing by downloading and installing software via standard .pkg installer packages, which means they leave behind BOM (“bill of material”) receipts in */Library/Receipts/*, and so you can inspect them with the `lsbom` tool to see what was installed where. That doesn’t do you any good *before* you run Google Updater, though.

- */Applications/* — Two apps are installed here, Google
Desktop.app and Google Updater.app. Google Desktop.app is the
software that shows you the sort of Quicksilver-ish query and
results window when you tap Command-Command to invoke Google
Desktop.1
- */Library/InputManagers/GoogleModLoader/* — Uh-oh. Google
Desktop installs an input manager hack in the local domain
Library folder. That means it is installed for *all* users on
the machine, and injects code into *every* Cocoa application you
launch. Google Updater does not give you the option to install
such files in your per-user Library folder.
A discussion of why input managers are suspect is beyond the
scope of this article. Matt Neuburg’s “[Are Input Managers the
Work of the Devil?](http://db.tidbits.com/article/08430)” TidBits article is a good introduction
and overview. Also relevant, especially with regard to
installing these things silently, is my own piece on [Smart
Crash Reports](http://daringfireball.net/2006/01/smart_crash_reports).
- */Library/Application Support/Google/* — Two things here. One
is a second app bundle named “Google Updater.app”. I’m not sure
what the difference is, but the Google Updater.app in the
*/Applications/* folder weighs just 108 KB, the one here in
*/Library/Application Support/Google/* weighs 2.8 MB. My guess
is that this is the real updater app, and the one in
*/Applications/* is just a springboard that launches this app.
The second thing in this folder is a folder named Mods. Inside
are three bundles: CaminoGoogleDesktop.gmod,
SafariSearchResults.gmod, and SafariWebHistory.gmod. I presume
these “mods” are the code bundles injected by the
GoogleModLoader input manager. Judging by the names, that means
the only apps that are targeted by these “mods” are Safari and
Camino. I don’t know what they’re supposed to do; none of the 
Google Desktop documentation seems to say. The gist seems to be
GoogleModLoader is more or less like SIMBL — a meta-hack framework
for input manager patches that ostensibly target specific
applications.
- */Library/Google/Google Desktop/* — This is where the index files
are stored. On my test system, they’re about 60 MB for a system with
about 70 GB of data on disk.
- */Library/LaunchDaemons/* — Two files for [launchd](http://developer.apple.com/macosx/launchd.html) here:
com.google.Desktop.Daemon.plist and
com.google.Desktop.StatsUploader.plist
- */Library/PreferencePanes/* — GoogleDesktop.prefpane is the
System Prefs panel that lets you configure the options for
Google Desktop.
- */System/Library/Frameworks/CoreServices.framework/Versions/A/
Frameworks/Metadata.framework/Versions/A/Support/Spotlight/* —
This one is baffling to me. My understanding is that it’s a
major no-no for third-party software to install anything in the
*/System/Library/* hierarchy other than kernel extensions.
Google creates this “Spotlight” folder, which contains a binary
file named “mdimport”. I presume this is how Google Desktop
piggybacks on Spotlight for file system notifications using
the same exclusion rules as Spotlight.
Is this legitimate? I’d love to hear from anyone at Apple or
Google about this, on or off the record.
- Speaking of kernel extensions, there is */Library/Google/Google
Desktop/GoogleDesktopDaemon.bundle/Contents/Resources/
GDFSNotifications.kext*. It’s not installed in the standard
*/System/Library/Extensions/* folder, but if you poke around
with `kextstat | grep google` at the command line, you can see
that it gets loaded dynamically. (Thanks to Jon Wight of [Toxic
Software](http://toxicsoftware.com/blog/).)


There are also a bunch of cache files in various *Library/Cache* folders, and the search indexes for each user seem to be stored in *~/Library/Application Support/Google/Google Desktop/Index/*.


## Uninstalling


Uninstalling seems to work as you’d hope. The uninstaller offers to leave your indexes behind, which is a nice touch. All of the software is removed when you uninstall — the apps, the GoogleModLoader input manager, and the “mod” hacks themselves. Some folders and preference files are left behind, but they’re inert. It seems safe to say you can try Google Desktop out, and if you don’t like it, you can use the Google Updater to uninstall it, leaving no significant detritus or software behind.


## The Processes


After installing Google Desktop, the following processes are launched when you log in and run in the background, along with how much real memory they consume, according to Activity Monitor:

- Google Desktop (this is the app you see in the Dock) — 11 MB
- GoogleDesktopAgent (there are two copies of this process) — 8 MB
- Google Updater Helper — 3 MB
- GoogleDesktopDae — 24 MB


That’s about 45 MB of real memory. Not huge, but significant.


---

1. I.e. a double-tap on the Command key. Which is a very clever shortcut — I like it. ↩︎



| **Previous:** | [EMI to Offer DRM-Free Online Music](https://daringfireball.net/2007/04/emi_drm_free_music) |
| **Next:** | [Apple Computer](https://daringfireball.net/2007/04/apple_computer) |


PreviousNext