---
title: "iOS 17.3, Now in Beta, Includes New ‘Stolen Device Protection’ Feature"
date: 2023-12-12
url: https://daringfireball.net/2023/12/ios_17-3_stolen_device_protection
slug: ios_17-3_stolen_device_protection
word_count: 771
---


Joanna Stern and Nicole Nguyen, [reporting for The Wall Street Journal](https://www.wsj.com/tech/personal-tech/apple-iphone-ios-update-stolen-device-protection-698d760e?mod=hp_lead_pos1) ([News+ link](https://apple.news/AruixbQhXQJOXck5uZRdbyw)):


> If you enable the new Stolen Device Protection, your iPhone will 
> restrict certain settings when you are away from a location 
> familiar to the iPhone, such as your home or work. Here’s the 
> rundown: 
> Apple ID password change: 
> *If you do nothing*: A thief can use the passcode to change 
> your Apple account password and lock you out. This move is the 
> key to thieves turning off Find My and wiping phones for resale. 
> Since you, the iPhone’s owner, don’t have the changed Apple ID 
> password, you can’t immediately locate your iPhone or remotely 
> wipe its data. 
> *With Stolen Device Protection*: If you want to change an Apple 
> ID password when away from a familiar location, the device will 
> require your Face ID or Touch ID. It will then implement an 
> hour-long delay before you can perform the action. After that hour 
> has passed, you will have to reconfirm with another Face ID or 
> Touch ID scan. Only then can the password be changed.


This sounds like a very thoughtful solution to a devilishly tricky problem: a combination of biometrics and a time delay, with exceptions for when you’re in a known location like work or home.


Stern and Nguyen reported a series of stories this year detailing how thieves — in some cases, organized crime rings — were taking advantage of the god-like powers of your device passcode, [the first in February](https://www.wsj.com/articles/apple-iphone-security-theft-passcode-data-privacya-basic-iphone-feature-helps-criminals-steal-your-digital-life-cbf14b1a?mod=article_inline) and [the follow-up in April](https://www.wsj.com/articles/the-iphone-setting-thieves-use-to-lock-you-out-of-your-apple-account-716d350d?mod=article_inline). The gist of it is that your device passcode/passphrase controls the keys to your entire digital kingdom. With the phone *and* your passcode, you can reset your iCloud account password *and* access the passwords saved in your keychain. Thieves were scamming people to glean their passcodes, then stealing their phones. This granted thieves access not just to the phones’ contents, but to the victims’ banking accounts. And resetting the victims’ iCloud passwords prevented the victims from remotely wiping, locking, or finding the stolen devices. (One way the scam would run: Chat up the victim in a bar, and offer to use the target’s phone to snap a photo of the victim and their friends. Surreptitiously [lock the phone out of Face ID](https://daringfireball.net/2022/06/require_a_passcode_to_unlock_your_iphone) when handing it back to the victim. Then, when next the victim wants to do anything on their phone, they need to enter their passcode. Either the thief or a partner in a team gleans the passcode. Then they steal the phone, knowing the device passcode.)


After Stern and Nguyen broke this story, a lot of people reasonably wondered why Apple allows you to reset your iCloud account password using only your device passcode. The reason is customer support: every single day, hundreds — maybe thousands? — of people are locked out of their iCloud account because they can’t remember the password. Android phones work the same way: you can reset your Google account password knowing only your device passcode. However many people are falling victim to thieves taking advantage of this, there are orders of magnitude more innocent users who *do* know their phone passcode, but have forgotten their iCloud/Google account password.


Stolen Device Protection addresses the problem well, with balance between security and convenience. No existing workaround is a true defense against a thief who knows your device passcode. (Locking your iPhone with Screen Time protections was suggested by many as a mitigation, but you can completely override Screen Time protections with the device passcode — it just adds a few extra steps.)


Stolen Device Protection will be off by default, but users will be prompted about the feature upon restarting after upgrading to 17.3. That’s a reasonable compromise. My only doubts about the feature are the “home” and “work” safe locations, where the hour-long delay is overridden. (You still need to authenticate with Face ID or Touch ID, though.) How are these locations determined? I’ve installed the first 17.3 beta on a spare iPhone, and after enabling Stolen Device Protection, I tried changing my iCloud password, [but I still need to wait an hour](https://daringfireball.net/misc/2023/12/stolen-device-protection-not-home.heic), even though I’m at home. (And this spare iPhone — my iPhone 13 Pro from last year — hasn’t left my house since September.)


Overall, this new feature is clearly a win for security — and a triumph of Joanna Stern and Nicole Nguyen’s investigative reporting.



| **Previous:** | [Beeper Mini Is Back, But Without Phone Number Registration](https://daringfireball.net/2023/12/beeper_mini_is_back) |
| **Next:** | [App Store Rankings as a Proxy for Social Network Momentum](https://daringfireball.net/2023/12/app_store_rankings_as_a_proxy_for_social_network_momentum) |


PreviousNext