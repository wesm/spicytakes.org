---
title: "Apple Mail and Hidden Tracking Images"
date: 2021-02-24
url: https://daringfireball.net/2021/02/apple_mail_and_hidden_tracking_images
slug: apple_mail_and_hidden_tracking_images
word_count: 756
---


In my [piece yesterday about email tracking images](https://daringfireball.net/linked/2021/02/23/email-spy-pixels) (“spy pixels” or “spy trackers”), I complained about the fact that Apple — a company that rightfully prides itself for its numerous features protecting user privacy — offers no built-in defenses for email tracking.


A slew of readers wrote to argue that Apple Mail *does* offer such a feature: [the option not to load any remote resources](https://www.theverge.com/22288190/email-pixel-trackers-how-to-stop-images-automatic-download) at all. It’s a setting for Mail on both Mac and iOS, and I know about it — I’ve had it enabled for years. But this is a throwing-the-baby-out-with-bath-water approach. What Hey offers — by default — is the ability to load regular images automatically, so your messages look “right”, but block all known images from tracking sources (which are generally 1×1 px invisible GIFs).


Typical users are never going to enable Mail’s option not to load remote content. It renders nearly all marketing messages and newsletters as weird-looking at best, unreadable at worst. And when you get a message whose images you *do* want to see, when you tell Mail to load them, it loads all of them — including trackers. Apple Mail has no knowledge of spy trackers at all, just an all-or-nothing ability to turn off all remote images and load them manually.


Mail’s “Load remote content in messages” option is a great solution to bandwidth problems — remember to turn it on the next time you’re using Wi-Fi on an airplane, for example. It’s a terrible solution to tracking. No one would call it a good solution to tracking if Safari’s only defense were an option not to load any images at all until you manually click a button in each tab to load them all. But that’s exactly what Apple offers with Mail. (Safari doesn’t block tracking images, but Safari does support content blocking extensions that do — one solution for Mail would be to enable the same content blocker extensions in Mail that are enabled in Safari.)


How does Hey know which images are trackers and which are “regular” images? They can’t know with absolute certainty. But they’ve worked hard on this feature, and [have an entire web page promoting it](https://hey.com/spy-trackers/). From that page:


> *HEY manages this protection through several layers of defenses.*
> First, we’ve identified all the major spy-pixel patterns, so we
> can strip those out directly. When we find one of those pesky
> pixels, we’ll tell you exactly who put it in there, and from what
> email application it came. Second, we bulk strip everything that
> even smells like a spy pixel. That includes 1x1 images, trackers
> hidden in code, and everything else we can do to protect you.
> Between those two practices, *we’re confident we’ll catch 98% of
> all the tracking that’s happening out there*.
> But even if a spy pixel sneaks through our defenses (and we vow to
> keep them updated all the time!), you’ll have an effective last
> line of defense: HEY routes all images through our own servers
> first, so *your* IP address never leaks. This prevents anyone from
> discovering your physical location just by opening an email. Like
> VPN, but for email.


Apple should do something similar: identify and block spy trackers in email by default, and route all other images through an anonymizing proxy service.1 And, like Hey, they should flag all emails containing known trackers with a shame badge. It’s a disgraceful practice that has grown to be accepted industry-wide as standard procedure, because the vast majority of users have no idea it’s even going on. Through reverse IP address geolocation, newsletter and marketing email services track not just *that* you opened their messages, but *when* you opened them, and *where you were* (to the extent that your IP address reveals your location).


No thanks. Apple should offer defenses against email tracking just as robust as Safari’s defenses against web tracking.2


---

1. Gmail has been proxying remote images in messages [since 2013](https://gmail.googleblog.com/2013/12/images-now-showing.html). ↩︎
2. Don’t get me started on how predictable this entire privacy disaster was, once we lost the war over whether email messages should be plain text only or could contain embedded HTML. Effectively all email clients are web browsers now, yet don’t have any of the privacy protection features actual browsers do. ↩︎︎



| **Previous:** | [How ‘Unlock With Apple Watch’ While Wearing a Face Mask Works in iOS 14.5](https://daringfireball.net/2021/02/unlock_with_apple_watch_with_face_mask) |
| **Next:** | [Adoption Is Low for COVID-19 Exposure Apps, Rendering Them Effectively Useless](https://daringfireball.net/2021/03/covid_19_exposure_apps) |


PreviousNext