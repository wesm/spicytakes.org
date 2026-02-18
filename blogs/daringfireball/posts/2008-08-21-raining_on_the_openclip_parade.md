---
title: "Raining on the OpenClip Parade"
date: 2008-08-21
url: https://daringfireball.net/2008/08/raining_on_the_openclip_parade
slug: raining_on_the_openclip_parade
word_count: 1586
---


The OpenClip project, which debuted this week, [describes itself](http://www.openclip.org/faq.php) as “a non-profit, open-source, community-effort project, which promotes a framework for the iPhone that allows users to copy/paste between participating applications.”


The obvious shortcoming, compared to a hypothetical system-wide clipboard from Apple, is that apps which don’t explicitly support the OpenClip scheme don’t work with it — including all of Apple’s apps, like Mail and Safari. That’s to be expected. But it’s worse than that.


The OpenClip framework, by Zac White, is a very clever implementation of a fundamentally unwise idea. [White’s description of the project](http://zacwhite.com/blog/?p=158) on his own weblog is fairly open regarding its inherent problems. The [OpenClip.org](http://openclip.org/) web site, however, is hosted and written not by White but by [Proximi](http://magicpad.proximi.com/), the developers behind [MagicPad](http://daringfireball.net/linked/2008/08/05/magicpad). Their [developer FAQ](http://www.openclip.org/dfaq.php) states:


> How does it work?
> OpenClip utilizes a shared space on the iPhone. Applications that
> use the OpenClip framework can access this common area to write to
> and read from, allowing copy/paste between participating apps.


That struck me as curious, as I wasn’t aware of any inter-application “shared space” on the iPhone. White’s own description of how it works and the OpenClip source code itself show that such a description is disingenuous. The “How does it work?” section of their regular (i.e. non-developer) FAQ [is more technically accurate](http://www.openclip.org/faq.php):


> OpenClip utilizes an application’s ability to read into other
> application’s Documents directory. Applications that use the
> OpenClip framework can access this read only area to read pastes
> from other applications and then OpenClip can offer the newest data
> to the current application.


The fundamental problem the OpenClip project faces is that of data interchange. If you copy something in app A, and wish to paste it in app B, the clipboard data needs to exist somewhere where app A can write (when you copy), and where B can read (when you paste). On Mac OS X, the system provides this to Cocoa apps via the [NSPasteboard class](http://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSPasteboard_Class/index.html) and associated APIs. Individual applications don’t have to worry about the details of how and where clipboard data is stored; it’s an implementation detail completely managed by the system.


But even ignoring Mac OS X’s standard system-wide clipboard, apps on the Mac face no challenges when it comes to exchanging data with other apps via the file system. On the Mac, all apps can read and write wherever they want within your entire home folder. So if Mac apps A and B wish to share data with each other via a custom file format, they can both agree to do so via a shared file, in, say, the user’s Documents folder.


iPhone apps can’t do that. Or, more specifically, *third-party* iPhone apps written with the official iPhone SDK can’t do that; Apple’s own iPhone apps can do whatever they want.


## iPhone Sandboxing


The idea with *[sandboxing](http://en.wikipedia.org/wiki/Sandbox_(computer_security))* is that each app executes in its own space, with limited resources and with no ability to alter or modify anything outside its own sandbox. The downside is that some of the things Mac apps can do but which iPhone apps cannot are potentially very useful (and/or very cool). The upside is that those same things are potentially dangerous (both in terms of security and in terms of stability). It’s a trade-off.


Here’s how sandboxing works in iPhone OS 2.0. Given its shared roots with Mac OS X, the iPhone OS unsurprisingly has a very familiar file system layout. The system’s standard apps reside in a top-level folder named */Applications/*, just like on Mac OS X. Apps that you install via the App Store don’t go there, however. Instead, there is a separate Applications folder for these applications. In iPhone OS 2.0, that folder is at */private/var/mobile/Applications/*, but it doesn’t really matter exactly where it is. (*/private/var/mobile/* is more or less the iPhone equivalent of your home folder.)


Every time you install an application, a new sandbox is created within that Applications folder. The sandbox is a folder named with a [UUID](http://en.wikipedia.org/wiki/Uuid), for example, “68813987-A628-493F-90E2-A6ABCD922A89”. The application itself is installed inside the sandbox folder, along with its own directories for writing data. So, if you install two iPhone apps from the App Store, named, say, “Foo” and “Bar”, they’ll be installed in two separate sandboxes that look something like this at the file system level:


```
/private/var/mobile/Applications/04A74595-4DE8-4026-8459-63B2D153D13C/
    Documents/
    Foo.app/
    Library/
    tmp/

/private/var/mobile/Applications/77C9A482-F5F8-4284-9E16-C629763B9162/
    Bar.app/
    Documents/
    Library/
    tmp/

```


Each app gets its own Documents folder, its own Library folder, and even its own temporary scratch space (“tmp”). Each application can only write to the file system within its own sandbox directory. This isn’t just a guideline from Apple — it is enforced by the OS. Any attempt by an app to *write* to the file system outside its sandbox will fail.1


However, in iPhone OS 2.0, an app can *read* from anywhere in the file system. This serves as the basis for how OpenClip works.


## How OpenClip Works


As an API, White’s OCPasteboard class is a clone of Cocoa’s NSPasteboard. For every `NSwhatever` call in the standard Cocoa NSPasteboard class hiearchy, OpenClip offers a corresponding `OCwhatever`. The advantage to this design is twofold: first, it’s exactly what Cocoa developers are accustomed to on the Mac; second, if Apple eventually ports NSPasteboard to the iPhone OS, it’s likely to have a very similar API.


When an app using OpenClip copies data,2 it writes the data into two files within its own Documents folder:


```
Documents/
    OpenClip/
        OCGeneralPboard.data
        OCGeneralPboard.metadata
Foo.app/
Library/
tmp/

```


When an app using OpenClip pastes, the OpenClip framework peeks into the Documents folder of *every other app sandbox in the file system*, looking for the most recently-modified OpenClip data files. So if you have three apps, A, B, and C, and you copy something in A, then copy something else in B, then do a paste in C, C will paste the data copied from app B, because it was created more recently.


## The Problems


On his weblog, [White writes](http://zacwhite.com/blog/?p=158):


> How it works is relatively simple and doesn’t break the SDK
> agreement. OpenClip works by looking into the Documents folder of
> other applications to get their pastes. Applications are allowed
> to write all they want to their own Documents directory (for
> copy), so no foul there. Applications are also allowed to read
> outside their sandbox into the Documents directories for other
> apps (for paste), so no foul there.


This is not accurate. It’s more like “slipping through a temporary loophole” than “no foul”. In the Security section of [chapter 4 of Apple’s *iPhone OS Programming Guide*](http://developer.apple.com/iphone/library/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/ApplicationDesignGuidelines/chapter_5_section_5.html#//apple_ref/doc/uid/TP40007072-CH6-SW6), the sandbox is described by Apple as follows (boldface emphasis added):


> For security reasons, iPhone OS restricts an application and its
> preferences and data to a unique location in the file system. This
> location is part of the security feature known as the
> application’s “sandbox.” The sandbox is a set of fine-grained
> controls limiting access to files, preferences, network resources,
> hardware, and so on. In iPhone OS, an application and its data
> reside in a secure location **that no other application can access**.


Not simply that no other application can *write to*, but which no other application can *access*. That this restriction is not yet enforced at a technical level (such as is the case with an app attempting to *write* outside its own sandbox) does not mean it’s permitted.


And, indeed, in the 2.1b4 release of the iPhone OS, it *is* enforced. The OpenClip demo apps, which work as advertised on iPhone OS 2.0.2, do not work in the current 2.1 beta, because apps are no longer able to read or even *see* other apps’ sandboxes.3 To be clear, this change is clearly not in response to OpenClip; Apple began seeding the 2.1 betas with these tightened sandbox restrictions before OpenClip debuted, and the *iPhone OS Programming Guide* has stated all along that apps can’t “access” the contents of other sandboxes.


There is no “shared space” for iPhone apps to exchange data. (One workaround I’ve seen bandied about is to use the system-wide Address Book database as a storage location for shared clipboard data. Needless to say, such an implementation would not qualify as an intended use of the AddressBook framework.) Wishing it were otherwise doesn’t make it so.


The intent of OpenClip is fine. That there’s been [so much](http://blogsearch.google.com/blogsearch?hl=en&q=openclip) coverage [regarding OpenClip](http://www.techmeme.com/080820/p6#a080820p6) in the past 24 hours shows just how much demand there is for inter-application copy-and-paste. But developers would be foolish to adopt a framework that only works today because of a loophole in iPhone OS 2.0 that is *already closed* in iPhone OS 2.1.


---

1. This structure has another benefit in addition to security — it makes it easy for the system to remove all of an app’s data along with the app itself when you delete the app. No preference files or application support detritus can be left behind, because the entire sandbox folder is deleted when you delete the app. ↩︎
2. And I do mean “data”, not just text. OpenClip supports both text and images. ↩︎
3. In iPhone OS 2.1, an application using OpenClip would still work for copying and pasting within itself, because that only requires reading and writing to the app’s own sandbox. But you don’t need OpenClip for that. ↩︎



| **Previous:** | [Title Case Update](https://daringfireball.net/2008/08/title_case_update) |
| **Next:** | [Notes and Observations Regarding Yesterday’s ‘Let’s Rock’ Apple Special Event](https://daringfireball.net/2008/09/lets_rock_special_event) |


PreviousNext