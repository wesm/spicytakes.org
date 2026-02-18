---
title: "How Should Mac Apps Be Distributed?"
date: 2009-09-17
url: https://daringfireball.net/2009/09/how_should_mac_apps_be_distributed
slug: how_should_mac_apps_be_distributed
word_count: 1103
---


Alexander Limi has a thoughtful piece regarding [the problems Mozilla has identified with the current installation process for Firefox on the Mac](http://limi.net/articles/improving-the-mac-installer-for-firefox/). As it stands, they’re following the common pattern of delivering the Firefox app on a disk image, which, when mounted, uses a background image and alias to the */Applications/* folder to encourage users to copy the app from the mounted image to their startup drive. Limi writes:


> Some common errors that we have seen repeatedly among informal
> testing with friends and family are:
> *They drag the application to their dock directly.* 
> *They think that starting Firefox is done by opening the disk
> image every time.* 
> This is very common, and the logic is that the first time they
> started Firefox, they had to do this, so they continue doing it.
> This makes starting Firefox a chore, since it takes a lot of
> clicks to accomplish.


I agree that disk images are problematic for lay users. The whole concept of a virtual volume is just too abstract. There’s a wonderful simplicity to the way that nearly all good Mac apps can be installed just by copying the *AppName.app* bundle to anywhere you want it on your hard drive, and that apps can be uninstalled simply by dragging that same bundle to the trash. Users don’t, of course, need to understand or even be aware that .app bundles are really just folders that the Finder treats as a single item. The only conceptual abstraction Mac users should need to know is that the icon *is* the app.


But to make this work for apps delivered by disk image, users have to understand that they must copy the app from the image to their startup drive. This is where some get lost.


The iPhone shows just how much simpler the concept of app installation — and just as importantly, *un*-installation — can be. There is only one place where iPhone apps can be: on one of the home screens. The entire file system has been abstracted away. If you see the app icon, it is installed. If you want to get rid of it, you just press and hold to invoke jiggle mode and tap that icon’s X button. Even better, there is nothing to “clean up” after an iPhone installation: no mounted image to unmount, no .zip or .dmg download file to throw away.


But while I agree with the problems associated with using disk images for Mac app distribution, my initial reaction was that I did not like Limi’s proposed solution: a disk image containing an installer app that is set to auto-run when the image is mounted.


What I don’t like about installers is that users don’t know what’s been installed where. (Yes, you can use the Show Files command in the installer File menu to see what’s going to be installed, but the only people who know about this command are those of us who aren’t confused by any of this stuff in the first place.)


But after thinking about this some more, it occurs to me that an installer for a Mac app — even if it’s merely copying a .app bundle to */Applications/* — arguably provides a more iPhone-like installation process. The iPhone’s App Store app is, effectively, an installer. You install by clicking an “Install” button; you uninstall by taking action on the app icon.


The difference, though, is that on the iPhone, the App Store isn’t just the conventional way of installing and updating apps, it is the only way. On the Mac, installers are considered at least slightly unconventional. It’s also the case that installers work *against* the wishes of some advanced users. Whenever I install a Mac app by drag and drop, I don’t put it in the root-level-of-the-startup-drive */Applications/* folder, but instead in the inside-my-user-account-home-folder *~/Applications/*, just as a simple way of keeping third-party apps separate from Apple’s system apps. Installers that hard-code the destination to the root-level Applications folder work against that.


In Firefox’s case, [Limi covers this scenario in an aside](http://limi.net/articles/improving-the-mac-installer-for-firefox/):


> Note that experienced Mac users should be able to cancel the
> installer at any time and drag the Firefox application to the
> location they want instead, thus there should be no loss of
> functionality or flexibility for them.


Perhaps that’s a good compromise, but I suspect that many experienced users, who would in fact prefer to install Firefox by drag and drop manually, would *not* cancel the installer to do so, on the reasonable assumption that if there is an installer, it must be doing something in addition to just copying the .app bundle. “Cancel the installer” does not sound like a good step in the instructions for installing software.


## Zip It


What I like best is the resurgent trend of delivering Mac apps as simple .zip archives (a technique that harkens back a decade to when Mac apps were typically delivered as StuffIt archives). Download the .zip file, double-click, and there’s the app. Just like with disk images, what users *should* do then is move the app to their Applications folder. But — and this is the advantage of using a zip archive over a disk image — *they don’t have to*. Users can just launch the app right from their Downloads folder, and it’ll work just fine. They can drag it to their Dock, and it’ll work just fine. It’s not tidy, but there’s no confusing abstraction like a virtual disk volume that will disappear after they log out for reasons they don’t understand.


And you know when you double-click certain non-app bundles of software, like Dashboard widgets and System Preference panes, and the Finder prompts to ask if you’d like to install it, and if you agree, the system goes and puts the bundle in the right location, like, say, *~/Library/Widgets/* or *~/Library/PreferencePanes/*?


Perhaps Apple should do something like that for .app bundles, where if you launch an app from *~/Downloads/*, it would prompt you to install the app, and if you agree, it would move it to the Applications folder and launch it from there.1


---

1. Patrick Dubroy proposed something along these lines two years ago in a fine essay titled “[Why Is Installing Software on a Mac So Complicated?](http://dubroy.com/blog/why-is-installing-software-on-a-mac-so-complicated/)”. And Lukas Mathis had two good pieces on Mac app distribution in July, [here](http://ignorethecode.net/blog/2009/07/24/installing-applications-on-the-mac-still-broken/) and [here](http://ignorethecode.net/blog/2009/07/25/more-on-installing-applications/). ↩︎



| **Previous:** | [Snow Leopard Compatibility Tweaks for That Thing I Wrote in January About Writing AppleScripts That Dynamically Target Either Safari or WebKit](https://daringfireball.net/2009/09/snow_leopard_applescript_perl_safari_webkit) |
| **Next:** | [Snow Leopard Adoption Rate](https://daringfireball.net/2009/09/snow_leopard_adoption_rate) |


PreviousNext