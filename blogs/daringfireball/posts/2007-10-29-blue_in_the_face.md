---
title: "Blue in the Face"
date: 2007-10-29
url: https://daringfireball.net/2007/10/blue_in_the_face
slug: blue_in_the_face
word_count: 850
---


[Reports abound](http://news.google.com/news?q=leopard+upgrade+blue+screen) regarding users suffering from a “blue screen” after upgrading to Leopard: they upgrade, reboot, and get stuck at a blank blue screen.


But, as far as I can tell, there is no mystery involved. There is one and only one known cause for this problem: [old versions of Unsanity’s Application Enhancer](http://www.unsanity.org/archives/haxies/leopard.php), a.k.a. APE. Versions 2.0.2 and 2.0.3 of APE are apparently inert but harmless on Leopard. But at least some, if not all, versions of APE preceding version 2.0.2 are incompatible, and will render the system unbootable if left in place during an upgrade. APE 2.0.2 was released in November 2006; 2.0.3 in March 2007.


To reiterate, the evidence as of this writing indicates that every single instance of a “blue screened” botched Leopard upgrade is attributable to the presence of APE.


[**Update, 10 pm EDT:** There are, on Apple’s discussion boards, reports of botched Leopard upgrades that do not involve the presence of any version of APE. However, I have yet to see a set of reproducible steps implicating anything specific as a culprit other than APE. One informed reader — who works as a Mac troubleshooting technician — has witnessed at least two “blue screen” Leopard upgrades on which no version of APE was present, and suspects the culprit in both cases to be latent hard disk problems. (Hence, perhaps, Apple’s suggestion to run `fsck` in single-user mode in the KBase article referenced below.)]


Unsanity’s response more or less boils down to, *APE users should check for updates and upgrade to the latest version.* That’s fine advice for any user who has knowingly installed APE, but the biggest problem seems to be that many of these blue screen sufferers had no idea APE was installed on their systems.


How could that be? The most common route is Logitech Control Center, the mouse “driver” software from Logitech. “Driver” in quotes because it’s utterly absurd and completely irresponsible for Logitech to base their mouse software on a completely and utterly unsupported-by-Apple system software modification. (If any readers are aware of other software that installs APE behind the scenes, please let me know.)


Logitech Control Center currently installs APE 2.0.3, but previous versions of their installer used older versions of APE, which versions render Leopard unbootable. This is particularly pernicious given that most people installing Logitech’s software have never even heard of APE or Unsanity, let alone realize that Logitech is installing it on their system. You can’t argue that users who don’t even realize they have APE installed should have known to check for an updated version of APE before upgrading to Leopard.


This is pretty much the worst case scenario of what can go wrong with an unsupported system modification like APE. (Methinks [this page](http://www.apple.com/downloads/macosx/drivers/logitechcontrolcenter.html) in Apple.com’s third-party software section is not long for this life.)


Apple posted [this KnowledgeBase article](http://docs.info.apple.com/article.html?artnum=306857) over the weekend regarding the conflict, which article, judging by the tone, was written through gritted teeth.


Apple’s recommended solution is to reinstall Leopard using the Archive and Install option, rather than the default Upgrade option. This is not proof that the default Upgrade installation is sketchy or mysteriously inconsistent; it is proof that APE is not a supported form of system software. The blue-screened upgrades aren’t failing, they’re doing exactly what they’re supposed to do: moving the existing software from the old system to the new Leopard system software. This includes APE.


Apple’s alternative recommendation (in the same KnowledgeBase article) is to remove APE by hand, by booting into single-user mode and issuing the following commands:


```
rm -rf /Library/PreferencePanes/Application\ Enhancer.prefpane
rm -rf /Library/Frameworks/ApplicationEnhancer.framework
rm -rf /System/Library/SystemConfiguration/ApplicationEnhancer.bundle
rm -rf /Library/Preferences/com.unsanity.ape.plist

```


The one that sticks out like a sore thumb is */System/Library/SystemConfiguration/ApplicationEnhancer.bundle*. Installing software in the */System/Library/* hierarchy is not supported. The only exception I’m aware of is */System/Library/Extensions/*, which is the [only location where kernel extensions that must load during the boot process can be installed](http://daringfireball.net/2003/08/the_one_and_only_mac_os_x_extensions_folder).


[**Update, 10 pm EDT:** Late this afternoon, Apple edited the article: It now recommends using `rm` to delete just */System/Library/SystemConfiguration/ApplicationEnhancer.bundle*, adding further credence to my theory that this software bundle, which is installed in a folder Apple explicitly states third-party developers should never touch, is the culprit.]


Here’s how Apple describes the System domain (the */System/Library/* hierarchy) in [Mac OS X: File System Overview](http://developer.apple.com/documentation/MacOSX/Conceptual/BPFileSystem/Articles/Domains.html):


> **System.** The system domain contains the system software
> installed by Apple. The resources in the system domain are
> required by the system to run. Items in this domain are located on
> the local boot (and root) volume. Users cannot add, remove, or
> alter items in this domain.


Even more explicit is Apple’s “[Installing Your Application on Mac OS X: Guidelines for Developers](http://developer.apple.com/tools/installerpolicy.html)” (italics added):


> **Off Limits**


It’s hard to see what more Apple could do to discourage the installation of software in */System/*. Unsanity and Logitech are responsible for these APE installations that render Leopard upgrades unbootable, but it’s Apple that’s getting the bad press and the “I’m stuck at a blue screen” support calls.



| **Previous:** | [Leopard](https://daringfireball.net/2007/10/leopard) |
| **Next:** | [Shipping Means Prioritizing](https://daringfireball.net/2007/10/shipping_means_prioritizing) |


PreviousNext