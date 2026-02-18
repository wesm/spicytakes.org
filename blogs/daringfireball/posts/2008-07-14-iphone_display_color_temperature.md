---
title: "iPhone Display Color Temperature, and the Difference Between Builds 5A345 and 5A347 of the iPhone OS"
date: 2008-07-14
url: https://daringfireball.net/2008/07/iphone_display_color_temperature
slug: iphone_display_color_temperature
word_count: 468
---


So I [linked yesterday](http://daringfireball.net/linked/2008/07/13/color-temp) to a [piece by Jason Snell](http://www.macworld.com/article/134472/2008/07/iphone_display_warm.html) at Macworld regarding the different color temperature of new iPhone 3G displays. Snell asked iPhone product marketing director Bob Borchers (the same “Bob” from the iPhone Guided Tour videos, by the way) about the change, and Borchers said it was a deliberate design change.


At Ars Infinite Loop, however, [Clint Ecker is reporting](http://arstechnica.com/journals/apple.ars/2008/07/13/tip-updating-iphone-to-3a347-reduces-yellow-tinge) that the color change is slightly less warm/yellow in build 5A347 of the iPhone OS, as compared to build 5A345. This is confusing, so bear with me. 5A345 is the version that iPhone SDK members received as the final beta, and it is the version that many brand-new iPhone 3Gs shipped with from the factory. 5A347 is the very latest version, however, and so it is the one iTunes will download if you restore an iPhone.


I found that hard to believe — I had assumed that the differences between 345 and 347 were nearly insignificant. For example, if you have an iPhone with 5A345 installed, connect it to your computer, and tell iTunes to “Check for Updates”, iTunes will report: “This version of the iPhone software (2.0) is the current version.” I.e. iTunes does not treat 5A347 as an update for 5A345.


[This](http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version) is the URL iTunes pulls down when performing a version check for an iPhone. It is an XML document (gzip-encoded). The pertinent section looks like this:


```
<key>5A345</key>
<dict>
    <key>SameAs</key>
    <string>5A347</string>
</dict>

<key>5A347</key>
<dict>
    <key>Restore</key>
    <dict>
        <key>BuildVersion</key>
        <string>5A347</string>

        <key>DocumentationURL</key>
        <string>[…]</string>

        <key>FirmwareURL</key>
        <string>[…]</string>

        <key>ProductVersion</key>
        <string>2.0</string>
    </dict>
</dict>

```


(I replaced two long URLs with “[…]” for the sake of clarity.)


5A345 is explicitly marked as being the same as 5A347, at least for the purposes of recommended software updates.


It struck me as very unlikely that Apple would make a change as significant as tweaking the display color temperature at the last minute. But if they *were* to make a change like that, it seems even more unlikely that they would do so in a build that isn’t pushed out as an automatic update for iPhones running 5A345. So I asked a source at Apple on the iPhone engineering team who is, as they say, *familiar with the situation*, and my source told me there were no changes regarding display color temperature between 5A345 and 5A347, and that there’s no practical reason why someone with an iPhone with 5A345 installed should go through a complete system restoration just to get 5A347.


**Update:** Clearly, there is some variation in display color temperature between different iPhones, and even between different brand-new iPhone 3Gs. Whatever is causing this variation — my guess is slightly different screen components — isn’t related to versions 5A345 and 5A347 of the OS.



| **Previous:** | [The App Store, Day One](https://daringfireball.net/2008/07/app_store_day_one) |
| **Next:** | [Copy and Paste](https://daringfireball.net/2008/07/copy_and_paste) |


PreviousNext