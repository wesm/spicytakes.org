---
title: "iMessage’s Delivery Architecture Makes It Hard to Block Without Blocking All iOS Push Notifications"
date: 2025-12-09
url: https://daringfireball.net/2025/12/imessage_push_notifications_hard_to_block
slug: imessage_push_notifications_hard_to_block
word_count: 482
---


From Apple’s [iMessage Security Overview](https://support.apple.com/guide/security/imessage-security-overview-secd9764312f/web):


> Apple iMessage is a messaging service for iPhone, iPad, Mac, Apple
> Watch, and Apple Vision Pro. Relying on the Apple Push
> Notification service (APNs), iMessage lets users send texts and
> attachments like photos, contacts, locations, links, and emoji.
> Messages sync across all devices, enabling seamless conversations.
> Apple doesn’t store message content or attachments, which are all
> secured with end-to-end encryption so that no one but the sender
> and receiver can access them. Apple canʼt decrypt the data.


[This thread on Mastodon](https://mastodon.social/@magebarf/115686285616651788), prompted by [my wondering why Russia is blocking FaceTime but not iMessage](https://daringfireball.net/linked/2025/12/07/russia-blocks-facetime-and-snapchat), suggests that because iMessage messages are sent via APNs, a network (or entire nation) seeking to block iMessage could only do so by blocking all push notifications for iOS. That’s why on airplanes with “free messaging” on in-flight Wi-Fi, you usually also get all incoming push notifications, even for services that aren’t available on the free Wi-Fi. (It also explains why, on in-flight Wi-Fi and similar restricted networks, text-only messages go through, [but images and other attachments do not](https://infosec.exchange/@adamshostack/115696265565038136).)


[Here’s a support document from GFI Software](https://support.gfi.com/article/107782-when-blocking-imessage-push-notifications-are-blocked), which makes network appliances for enterprises and schools:


> The Exinda appliance gives administrators multiple options to stop
> or throttle applications that can use a lot of bandwidth in the
> network. An application that many would consider discardable or
> able to be easily limited in bandwidth is iMessage. When blocking
> or discarding iMessage traffic, users may experience an issue
> where all push notifications on iOS devices that have traffic
> going through the Exinda, i.e., on WiFi, will stop displaying.
> Root Cause: Apple uses the Apple Push Notification Service (APNS)
> to allow application creators to push out information to iOS
> devices. This includes mail servers being able to push out
> notifications of calendar and email, or app creators to be able to
> push text-based messages straight to the device.


Apple might have architected iMessage this way to make iMessage veto-proof with cellular carriers, who, at the time of [iMessage’s announcement in June 2011](https://www.apple.com/newsroom/2011/06/06New-Version-of-iOS-Includes-Notification-Center-iMessage-Newsstand-Twitter-Integration-Among-200-New-Features/), were already promoting iPhone push notifications as a reason to upgrade from a dumb phone to an iPhone with a more expensive plan. The carriers might have been tempted to block iMessage over cell networks to keep people using SMS, but they couldn’t without blocking all push notifications, which wouldn’t be tenable. But this architecture also makes iMessage hard to block in authoritarian countries where iPhones are even vaguely popular. (Maybe this helps explain why iMessage isn’t blocked in China, too?)


Draw your own conclusions about cellular carriers and enterprise network administrators being similar to authoritarian governments.



| **Previous:** | [Meta Says Fuck That Metaverse Shit](https://daringfireball.net/2025/12/meta_says_fuck_that_metaverse_shit) |
| **Next:** | [The Full Text of Marco Rubio’s Directive on State Department Typography, Re-Establishing Times New Roman](https://daringfireball.net/2025/12/full_text_of_marco_rubio_state_dept_directive_times_new_roman) |


PreviousNext