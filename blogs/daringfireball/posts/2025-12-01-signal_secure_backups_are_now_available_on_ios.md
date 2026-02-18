---
title: "Signal Secure Backups Are Now Available on iOS"
date: 2025-12-01
url: https://daringfireball.net/2025/12/signal_secure_backups_are_now_available_on_ios
slug: signal_secure_backups_are_now_available_on_ios
word_count: 840
---


[Signal Support](https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups):


> Signal Secure Backups can help you safely restore your chats
> if something unexpected happens to your device (like dropping
> your phone in a lake). When this optional feature is enabled,
> your device will automatically back up your message history so
> you won’t lose important data if you get a new phone or
> reinstall Signal.
> Your Secure Backup Archive is end-to-end encrypted and protected
> by a cryptographically secure 64-character recovery key that is
> never shared with the Signal service. Without your unique recovery
> key, no one (including Signal) can read, decrypt, or restore any
> of the data in your Secure Backup Archive.


Signal’s cloud storage service is optional (of course), and available to all users free of charge. At the free tier, it will back up the complete text of users’ chat history and the last 45 days of file attachments (images, video, etc.). For $2/month (through in-app purchase in the iPhone app), Signal will remove the 45-day window on media attachments, and store up to 100 GB of attachments — which, for most users, should be their complete history. (I don’t remember how far back in time my iCloud iMessage storage goes, but, as I type this, it includes 772,004 messages and consumes 83.4 GB of storage. I have a *lot* of images in there. 100 GB of storage feels pretty good for $2/month. My personal Signal account backup size is just 408 MB, which jibes with my gut feeling regarding how much I use Signal compared to iMessage — about one-half of one percent as much.)


[Signal first announced this feature back in September](https://signal.org/blog/introducing-secure-backups/) in a blog post that has a lot of technical details about how it works, but [until a week ago](https://x.com/signalapp/status/1993018186690871409), it was only available on the Android version. It’s still labelled as a “beta” feature on iOS. I enabled it over the weekend and signed up for the $2/month subscription — both to back up all my attachments and to support the Signal Foundation. Now that I’m paying $2/month, however, I wish they’d stop periodically badgering me for donations when I launch the app.


I’m glad this feature became available when it did, and that I enabled it over the weekend. Yesterday I set up my personal new iPhone this year, and this morning, when I tried to transfer my Signal account from my old iPhone to the new one, after claiming to reach “100%” of the transfer, and the Signal app reporting on both the old (source) and new (destination) phones that the transfer was complete, the app crashed on both phones. After that, the Signal app was in factory-fresh state on both phones, without any trace of my account history. I then restored the new iPhone from my brand-new online Signal Secure Backup, and that worked perfectly. And it somehow took far, far less time than the old device-to-device transfer — maybe one minute, versus 15 minutes or so for the device-to-device transfer that wound up failing.


Until now, transferring my Signal account history from one phone to another always felt like delivering a crate full of eggs while riding a rickety old bicycle without brakes on a bumpy cobblestone street. Every time I did it device-to-device, it felt like I’d be lucky if it worked. And my experience trying it this morning — for the last time — proved me right. Signal proponents often defended this architecture by arguing that remaining only on device was a security benefit. In some ways that’s true, but there’s nothing “secure” about a transfer feature that loses all of your data if the transfer fails. (Signal data, by design, isn’t included in iCloud backups because Apple holds a key to unlock iCloud backups for customer service reasons, unless the user has enabled [Advanced Data Protection](https://support.apple.com/en-us/108756).) Permanently losing all your data is a different form of “insecurity” than having it exfiltrated by an attacker or exposed to law enforcement agencies via a warrant issued to the cloud backup provider, but it’s a form of insecurity nonetheless.


Signal’s top priority has always been protecting your data from being obtained by others. That’s a noble idea, and central to Signal’s brand. But by placing that priority so far above everything else, it meant, until now, that you’d lose your entire account history if you lost or broke your primary phone. This new secure backup system shows that your data can remain secure while also being backed up off device. I’m glad the feature is finally here, but it should have been here years ago. A user-hostile “lose your phone, lose your account history” architecture may well be “secure” in a technical sense, but it’s the sort of brittleness that’s kept Signal from achieving more mainstream use.



| **Previous:** | [Exploring, in Detail, Apple’s Compliance With the EU’s DMA Mandate Regarding Apple Watch, Third-Party Accessories, and the Syncing of Saved Wi-Fi Networks From iPhones to Which They’re Paired](https://daringfireball.net/2025/11/apple_eu_dma_iphone_accessories_wi-fi_sync) |
| **Next:** | [Bad Dye Job](https://daringfireball.net/2025/12/bad_dye_job) |


PreviousNext