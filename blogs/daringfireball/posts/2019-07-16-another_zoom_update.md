---
title: "Apple Is Sending Out Another Silent Update To Fix the Webcam Flaw in Zoom’s Partner Apps"
date: 2019-07-16
url: https://daringfireball.net/2019/07/another_zoom_update
slug: another_zoom_update
word_count: 488
---


[Nicole Nguyen, reporting for BuzzFeed News](https://www.buzzfeednews.com/article/nicolenguyen/ringcentral-and-zhumu-customers-vulnerability):


> The fallout from [Zoom’s massive webcam vulnerability](https://www.buzzfeednews.com/article/nicolenguyen/zoom-webcam-hacker-watching-you-vulnerability)
> continues. In [a report published today](https://twitter.com/karanlyons/status/1150774640899317760), security researcher
> Karan Lyons shows that the same flaw — which gave attackers easy
> access to laptop cameras and microphones — affects RingCentral,
> which is used by over 350,000 businesses, as well as Zhumu,
> essentially the Chinese version of Zoom.
> On July 16, Apple confirmed that it had released another silent
> update to Macs patching the vulnerability affecting Zoom’s partner
> apps. The update, which went out this morning, requires no user
> action, but may take some time to roll out to all impacted Macs.
> Lyons tweeted that Apple’s latest update takes action on 11
> different apps, all vulnerable to the Zoom webcam flaw.


So here’s an interesting question. I’ve [been](https://daringfireball.net/linked/2019/07/10/nguyen-zoom) [using](https://daringfireball.net/linked/2019/07/11/macos-zoom-update) the phrase “nonconsensual technology” to describe Zoom’s invisible web server that remained installed and running even after you deleted the Zoom app. But when Apple first issued a silent, emergency system update to remove Zoom’s software, a few DF readers emailed or [tweeted](https://twitter.com/braz/status/1149453237843582978) [to ask](https://twitter.com/mwa4/status/1149675707016105985): *Isn’t this “nonconsensual technology” too?*


Clearly, the answer sounds like yes at first. Users get no indication of the update, and “requires no user action” makes it sound like it’s mandatory. But there *is* a setting to control this, allowing Mac users to disable the automatic installation of such updates. On MacOS 10.14 Mojave, it’s in System Prefs → Software Update → Advanced ([screenshot](https://daringfireball.net/misc/2019/07/macos-10-14-system-prefs.png)); on 10.13 High Sierra, it’s in System Prefs → App Store ([screenshot](https://daringfireball.net/misc/2019/07/macos-10-13-system-prefs.png)). In both versions, the checkbox is labeled “Install system data files and security updates”, and resides at the bottom of the section that controls what gets installed automatically.


This option is enabled by default — even if you choose to install regular system updates manually — which is why the vast majority of Mac users are getting these “silent” updates automatically. But if you disable this option, even these silent updates won’t be installed automatically. I confirmed this with an Apple spokesperson, who emphasized that Apple only issues such updates “extremely judiciously”. Any pending security updates will be installed the next time you manually update software.


I think Apple has struck a nearly perfect balance here, between doing what’s right for most users (installing these rare emergency updates automatically) and doing what’s right for power users who really do want to control when updates — even essential ones — are installed. I also think Apple is doing the right thing by going to the press and explaining when they issue such updates. If I could tweak anything, it would be to have these updates show up in the regular list of pending software updates *if* you have “Install system data files and security updates” turned off.



| **Previous:** | [On Bill Gates’s ‘Greatest Mistake Ever’](https://daringfireball.net/2019/07/gates_biggest_mistake) |
| **Next:** | [Superhuman and Email Privacy](https://daringfireball.net/2019/07/superhuman_and_email_privacy) |


PreviousNext