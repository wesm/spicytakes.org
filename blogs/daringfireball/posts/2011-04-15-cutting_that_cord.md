---
title: "Cutting That Cord"
date: 2011-04-15
url: https://daringfireball.net/2011/04/cutting_that_cord
slug: cutting_that_cord
word_count: 2074
---


## A Cursory High-Level Overview of the Current Status of Cloud-Based Syncing and iOS Devices


After Apple’s iPad 2 introduction event last month, I ran into [Josh Topolsky](http://www.joshuatopolsky.com/), and, of course, we talked about what we thought of it. Topolsky made an interesting observation: that the iPad 2 epitomized how Apple seems to be a generation ahead of its competitors on the device side — both hardware and software — but a generation *behind* on the cloud side.


I’ve been thinking about the iPad in this context ever since, and I think it’s a perfect synopsis of the state of iOS. There will be no tablet this year from any competitor that matches the iPad 2 in terms of elegance, battery life, or build quality. No competing OS will match iOS in terms of on-the-device user experience.


But most iPad competitors have little-to-no reliance on a connection to a desktop PC, the way an iPad does. Even RIM’s PlayBook is, in some sense, ahead in this regard. The PlayBook, as it is going to ship, is not a standalone device. [It requires a tethered BlackBerry phone](http://www.wired.com/gadgetlab/2011/03/doa-rim-will-ship-playbook-without-mail-messaging-or-contacts/) in order to do email, contacts, calendaring, or messaging — but it doesn’t require a PC.


Michael Gartenberg has a good line: “[‘Post-PC’ does not mean ‘Sans-PC’](http://www.macworld.com/article/159077/2011/04/gartenberg.html)” — to wit, that just because the iPad requires a tethered PC doesn’t mean Apple is wrong that the iPad is a “post-PC” device.


People arguing the other way aren’t hard to find. C.K. Sample: “[Dear Apple: You’re Not ‘Post-PC’ Until You Cut the Cord](http://www.sampletheweb.com/2011/03/04/dear-apple-youre-not-post-pc-until-you-cut-the-cord/)”. Paul Hontz: “[If iPads Are ‘Post-PC Devices’ Why Must I Sync With iTunes Before I Can Use One?](http://thestartupfoundry.com/2011/03/05/if-ipads-are-“post-pc-devices”-why-must-i-sync-with-itunes-before-i-can-use-one/)”.


Fair question. Chad Olson, following up on Gartenberg’s piece for Macworld, [proffers an answer](http://thisischadolson.wordpress.com/2011/04/07/the-cable/):


> For the sake of argument, let’s assume that Apple is working on a
> way for the iPad to exist on its own. To “cut the cord” so
> to speak. (And to clarify, every time I say “iPad” I mean to
> say “any iOS device”)
> In order for Apple to do this they would have to have an answer
> for three key iTunes functions:
> getting your stuff onto your new iPad
> updating iOS
> backing up and restoring your iPad


To Olson’s list I’d add one more: device activation. Those are the four reasons iPhones, iPads, and iPod Touches require you to sync with a Mac or PC running iTunes.


I think it’s worth considering these as discrete problems, rather than thinking about this as a single “*Apple should eliminate the dependency on tethered syncing to desktop iTunes*” issue.


Apple TV 2 shows the way forward. It’s an iOS device that works independently. Take it out of the box, plug it in, turn it on, enter your iTunes Store credentials — done. But Apple TV 2 doesn’t store content; it only does streaming. And because it only does streaming, there’s no initial sync for music or video, and there’s no need for anything to be backed up. If your Apple TV goes belly-up, you don’t lose any data.


So of the four reasons why other iOS devices require tethering to iTunes running on a Mac or Windows PC, Apple TV only tackles — and admittedly only needs to tackle — two of them: device activation and software updates.


I suspect those are the first two desktop iTunes dependencies that Apple will eliminate for iPhones and iPads. If Apple TV can activate itself and update its own software, there’s no reason iPhones and iPads couldn’t do the same. I’m not saying it’s an easy technical problem to solve — see, for example, [the problems Microsoft has had with updates to Windows Phone 7 devices](http://blog.seattlepi.com/microsoft/2011/03/24/microsofts-windows-phone-7-update-process-in-one-word-fail/) — but clearly, it’s technically feasible.


One obvious problem: what to do if there isn’t enough free storage space on the device? Perhaps, in that case, the updater would suggest either freeing up some space or plugging the device into iTunes on a Mac or PC to update the software the old-fashioned way. A less obvious problem: even if/when over-the-air software updates are enabled for iPhones and iPads, should Apple still present tethered-to-a-computer updating as the *preferred* update mechanism? The reason: iTunes backs up the device before installing the update. An iPad that’s never been synced to a computer is an iPad that’s never been backed up.


That’s important, because I don’t think over-the-air backups or media syncing are coming soon. Wireless networking just isn’t fast enough. I’m not talking about Wi-Fi syncing over a local network to iTunes running on your Mac or PC — [that may well be coming soon](http://news.google.com/news/more?q=ipod+wi+fi+syncing+itunes&hl=en&prmd=ivnsufd&bav=on.2,or.r_gc.r_pw.&um=1&ie=UTF-8&ncl=dB-zgbTzGVSaOYMtsMcJ1nF0VAicM&ei=njemTbGtMMea0QGjkKHxCA&sa=X&oi=news_result&ct=more-results&resnum=1&ved=0CC0QqgIwAA), but it wouldn’t solve the “how can these devices be ‘post-PC’ if they require a PC?” problem. We’re not talking about why the iPad needs a USB cable; we’re talking about why it needs a PC, period.


Apple gets a rap for being bad at, or simply not caring about, “the cloud”, but that’s not accurate. It’s just that they’re moving things there one piece at a time. It’s already the case that a large amount of songs, movies, TV shows — and especially apps — are purchased from the iTunes Store by iOS users directly from their iPhones and iPads. That’s the first step Apple took away from iTunes (on the Mac/PC) as a required hub.


So I’m thinking the iPad and iPhone won’t drop their connection to iTunes running on a PC in one fell swoop. It’ll be incremental, with new-device activation and software updates coming next. At that point, you’ll be able to use them without owning a PC. If you *want* to sync large libraries of music and video, you’ll still need a PC running iTunes, but if you have a large music/video library in the first place, you must have a PC already, so that’s not really a problem.


It just isn’t technically feasible to have people backing up and restoring 32 or 64 GB of data to the cloud. It can take hours to download a single HD movie from iTunes over a Wi-Fi connection, and upload speeds are far slower than download speeds. iOS devices aren’t behind Android in this regard, because Android doesn’t do complete device backups/restores over the cloud. (Android devices don’t do complete backups/restores, period.1)


## You Get Better at What You Do


Jason Fried had a good cover story for Inc. magazine last month, [on how to get good at making money](http://www.inc.com/magazine/20110301/making-money-small-business-advice-from-jason-fried_Printer_Friendly.html). His advice in a nutshell: *you get good at making money by actually making money*:


> I can’t say enough about bootstrapping. Whether you’re starting
> your first business or your next one, my advice is to bootstrap
> it. Bootstrapping forces you to think about making money on Day
> One. There’s a fundamental difference between a bootstrapped
> business and a funded business. It’s all about which side of the
> money you’re on. From Day One, a bootstrapped business has no
> choice but to make money. There’s no cushion in the bank and not
> much in the pockets. It’s make money or go home. To a bootstrapped
> business, money is air.
> On the other hand, from Day One, a funded business is all about
> spending money. There’s a pile in the bank, and it’s not there to
> collect interest. Your investors want you to hire, invest, and
> buy. There’s less — and in some cases, no — pressure to make
> money. While that sounds comforting, I think it ultimately hurts.
> It replaces the hustle, the scrap, the fight, with a false comfort
> of “we can worry about that later.”


Eye-rollingly obvious, perhaps, but so is much of the best but most-ignored advice in life. Almost nothing worthwhile is easy, and it’s hard to just jump in and be good at something difficult right off the bat. Think, say, of Twitter, whose business plan, such that it is, has always been something along the lines of “*Get big and popular, then just flip the switch and start making money when we feel like it.*” There is no switch.


The only reliable way to succeed at anything is to actually do it, repeatedly, with concentrated effort. True for individuals, and true for organizations. Athletes, artists, businesses.


Making money is not easy. Apple has gotten good at making large profits every quarter by building up to that — making ever-increasing profits all along, quarter after quarter after quarter, device after device after device.


Syncing to the cloud is not easy, either. I think Apple is smart enough to realize that they’re never going to just “flip a switch” and replace the entirety of iTunes’s desktop syncing with equally reliable over-the-air cloud syncing all at once. The only way Apple’s going to get good at cloud syncing is by actually *doing* cloud syncing.


And they are, in small ways.


Personal internet connections just aren’t ready for moving huge chunks of data around. Where iOS devices are behind the curve, competitively, is in cloud-based syncing for small bits of data. iPhone and iPad owners need MobileMe to get no-fuss wireless syncing for calendars, contacts, and bookmarks. I like MobileMe a lot, and it’s been very reliable for me for a few years now. But, at $99/year, it’s not something most iOS users have, and thus, most iOS users don’t get over-the-air syncing of calendars, contacts, and bookmarks. That’s not competitive today. (I’d love to know exactly what percentage of iOS users do use MobileMe.) I’ll bet nearly all Android users have Google accounts, and thus get calendars and contacts and many other bits of application data synced over-the-air a few minutes after they take their phones out of the box.


The announcement many people seem to be waiting for is for Apple to tell iOS users they no longer need iTunes on the Mac or Windows. The announcement *I’d* like to see is for iOS users to no longer need to pay for MobileMe to wirelessly sync calendars, contacts — and any other small bits of data from apps from the App Store.


iBooks does this. If you pause while reading a book on your iPad, then resume reading on your iPhone, it picks up on the same page in the book. Kindle and a bunch of other e-reading services do this too. The point isn’t that iBooks is unique or ahead of the curve in this regard. It’s that *you don’t need MobileMe for iBooks.* It’s all handled by the iTunes Store itself. You buy books on your device, you read them on your device, and your history, bookmarks and other metadata all get synced to your iTunes account in the cloud. And it works great. But a lot more apps should work like this. Should wireless Safari bookmark syncing cost $99 a year? Shouldn’t it be easy for iOS game developers to sync progress for the same game across multiple devices using the same iTunes account? App Store developers shouldn’t have to rely on another third party — Dropbox — for this sort of functionality.


And those third-party iOS developers that *are* depending upon Dropbox — there’s a veritable cottage industry of Dropbox text editors alone — have a far better syncing experience than Apple’s own creative apps. The iPad versions of the iWork suite and GarageBand are exquisite apps — easily some of the best-designed user experiences for creative software ever made. But the process of getting, say, a slide deck created in Keynote on your iPad open in Keynote on your iMac is downright antediluvian. Google Docs has *none* of the UI panache, but the syncing is invisible. You just open Google Docs, and there are your files. Doesn’t matter which machine you used to edit or create them, or which machine you’re using now, they’re all just there. That’s part of the overall experience.


That’s where Apple is behind.


---

1. At least not without rooting (Android equivalent of jailbreaking) the device [and using third-party software](http://matrixrewriter.com/android/). On some Android 2.2 (and later) phones — those that stick closest to stock Android — you can re-download all your previously downloaded apps from the Android Market on a new device, and [some app settings](http://developer.android.com/guide/topics/data/backup.html) are synced over-the-air to your Google account. But you don’t get backups or syncing of stuff like photos, videos, or music. ↩︎



| **Previous:** | [Tweetbot 1.0](https://daringfireball.net/2011/04/tweetbot) |
| **Next:** | [Magic](https://daringfireball.net/2011/04/magic) |


PreviousNext