---
title: "A review of postmarketOS on the Xiaomi Poco F1"
date: 2022-08-25
url: https://drewdevault.com/2022/08/25/pmOS-on-xiaomi-poco-f1.html
slug: pmOS-on-xiaomi-poco-f1
word_count: 1475
---

I have recently had cause to start looking into mainline Linux phones which fall
outside of the common range of grassroots phones like the PinePhone (which was
my daily driver for the past year). The  [postmarketOS wiki](https://wiki.postmarketos.org/wiki/Devices)  is a great place
to research candidate phones for this purpose, and the phone I landed on is the
 [Xiaomi Poco F1](https://wiki.postmarketos.org/wiki/Xiaomi_Poco_F1_(xiaomi-beryllium)) , which I picked up on Amazon.nl (for ease of return in case
it didn’t work out) for 270 Euro. Phones of this nature have a wide range of
support from Linux distros like postmarketOS, from “not working at all” to
“mostly working”. The essential features I require in a daily driver phone are
(1) a working modem and telephony support, (2) mobile data, and (3) reasonably
good performance and battery life; plus of course some sane baseline
expectations like a working display and touchscreen driver.

The use of mainline Linux on a smartphone requires a certain degree of bullshit
tolerance, and the main question is whether or not the bullshit exceeds your
personal threshold. The Poco F1 indeed comes with some bullshit, but I’m pleased
to report that it falls short of my threshold and represents a significant
quality-of-life improvement over the PinePhone setup I have been using up to
now.

The bullshit I have endured for the Poco F1 setup can be categorized into two
parts: initial setup and ongoing problems. Of the two, the initial setup is by
far the worst. These phones are designed to run Android first, rather than the
mainline Linux first approach seen in devices like the PinePhone and Librem 5.
This means that it’s back to dealing with things like Android recovery,
fastboot, and so on, during the initial setup. The most severe pain point for
Xiaomi phones is unlocking the bootloader.

The only officially supported means of doing this is via a Windows-only
application published by Xiaomi. A  [reverse engineered](https://github.com/francescotescari/XiaoMiToolV2)  Java application
supposedly provides support for completing this process on Linux. However, this
approach comes with the typical bullshit of setting up a working Java
environment, and, crucially, Xiaomi appears to have sabotaged this effort via a
deliberate attempt to close the hole by returning error messages from this
reverse engineered API which direct the user to the official tool instead. On
top of this, Xiaomi requires you to associate the phone to be unlocked with a
user account on their services, paired to a phone number, and has a 30-day
waiting period between unlocks. I ultimately had to resort to a Windows 10 VM
with USB passthrough to get the damn thing unlocked. This is very frustrating
and far from the spirit of free software; Xiaomi earns few points for openness
in my books.

Once unlocked, the “initial setup bullshit” did not cease. The main issue is
that the postmarketOS flashing tool (which is just a wrapper around fastboot)
seemed to have problems writing a consistent filesystem. I was required to apply
a level of Linux expertise which exceeds that of even most enthusiasts to obtain
a shell in the initramfs, connect to it over postmarketOS’s telnet debugging
feature, and run fsck.ext4 to fix the filesystem. Following this, I had to again
apply a level of Alpine Linux expertise which exceeds that of many enthusiasts
to repair installed packages and get everything up to a baseline of workitude.
Overall, it took me the better part of a day to get to a baseline of “running a
working installation of postmarketOS”.

However: following the “initial setup bullshit”, I found a very manageable scale
of “ongoing problems”. The device’s base performance is excellent, far better
than the PinePhone — it just performs much like I would expect from a
normal phone. PostmarketOS is, as always, brilliant, and all of the usual
mainline Alpine Linux trimmings I would expect are present — I can SSH in,
I easily connected it to my personal VPN, and I’m able to run most of the
software I’m already used to from desktop Linux systems (though, of course, GUI
applications range widely in their ability to accomodate touch screens and a
portrait mobile form-factor). I transferred my personal data over from my
PinePhone using a method which is 100% certifiably absent of bullshit, namely
just rsyncing over my home directory. Excellent!

Telephony support also works pretty well. Audio profiles are a bit buggy, and I
can often find my phone using my headphone output while I don’t have them
plugged in instead of the speakers, having to resort to manually switching
between them from time to time. However, I have never had an issue with the
audio profiles being wrong during a phone call (the modem works, by the way);
earpiece and speakerphone both work as expected. That said, I have heard
complaints from recipients of my phone calls about hearing an echo of their own
voice. Additionally, DTMF tones do not work, but  [the fix](https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/823)  has already been
merged and is expected in the next release of ModemManager. SMS and mobile data
work fine, and mobile data works with a lesser degree of bullshit than I was
prepared to expect after reading the pmOS wiki page for this device.

Another problem is that the phone’s onboard cameras do not work at all, and it
seems unlikely that this will be solved in the near future. This is not really
an issue for me. Another papercut is that Phosh handles the display notch
poorly, and though pmOS provides a “tweak” tool which can move the clock over
from behind the notch, it leaves something to be desired. The  [relevant
issue](https://gitlab.gnome.org/World/Phosh/phosh/-/issues/552)  is being discused on the Phosh issue tracker and a fix is presumably
coming soon — it doesn’t seem particularly difficult to solve. I have also
noted that, though GPS works fine, Mepo  [renders incorrectly](https://redacted.moe/f/40dd2e96.png)  and Gnome Maps
has (less severe)  [display issues](https://redacted.moe/f/ce6414d5.png)  as well.

The battery life is not as good as the PinePhone, which itself is not as good as
most Android phones. However, it meets my needs. It seems to last anywhere from
8 to 10 hours depending on usage, following a full night’s charge. As such, I
can leave it off of the juice when I go out without too much fear. That said, I
do keep a battery bank in my backpack just in case, but that’s also just a
generally useful thing to have around. I think I’ve lent it to others more than
I’ve used it myself.

There are many other apps which work without issues. I found that  [Foliate](https://johnfactotum.github.io/foliate/) 
works great for reading e-books and  [Evince](https://wiki.gnome.org/Apps/Evince)  works nicely for PDFs (two
use-cases which one might perceive as related, but which I personally have
different UI expectations for). Firefox has far better performance on this
device than on the PinePhone and allows for very comfortable web browsing. I
also discovered  [Gnome Feeds](https://gfeeds.gabmus.org/)  which, while imperfect, accommodates my needs
regarding an RSS feed reader. All of the “standard” mobile Linux apps that
worked fine on the PinePhone also work fine here, such as Lollypop for music and
the Porfolio file manager.

I was pleasantly surprised that, after enduring some more bullshit, I was able
to get  [Waydroid](https://waydro.id/)  to work, allowing me to run Android applications on this
phone. My expectations for this were essentially non-existent, so any degree of
workitude was a welcome surprise, and any degree of non-workitude was the
expected result. On the whole, I’m rather impressed, but don’t expect anything
near perfection. The most egregious issue is that I found that internal storage
simply doesn’t work, so apps cannot store or read common files (though they seem
to be able to persist their own private app data just fine). The camera does not
work, so the use-case I was hoping to accommodate here — running my bank’s
Android app — is not possible. However, I was able to install F-Droid and
a small handful of Android apps that work with a level of performance which is
indistinguishable from native Android performance. It’s not quite there yet, but
Waydroid has a promising future and will do a lot to bridge the gap between
Android and mainline Linux on mobile.

On the whole, I would rate the Poco F1’s bullshit level as follows:

* Initial setup: miserable
* Ongoing problems: minor

I have a much higher tolerance for “initial setup” bullshit than for ongoing
problems bullshit, so this is a promising result for my needs. I have found that
this device is ahead of the PinePhone that I had been using previously in almost
all respects, and I have switched to it as my daily driver. In fact, this phone,
once the initial bullshit is addressed, is complete enough that it may be the
first mainline Linux mobile experience that I might recommend to others as a
daily driver. I’m glad that I made the switch.
