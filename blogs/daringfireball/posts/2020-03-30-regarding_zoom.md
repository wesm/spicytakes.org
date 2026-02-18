---
title: "Regarding Zoom"
date: 2020-03-30
url: https://daringfireball.net/2020/03/regarding_zoom
slug: regarding_zoom
word_count: 889
---


[Joseph Cox, reporting for Motherboard last week](https://www.vice.com/en_us/article/k7e599/zoom-ios-app-sends-data-to-facebook-even-if-you-dont-have-a-facebook-account):


> As people work and socialize from home, video conferencing
> software Zoom has exploded in popularity. What the company and its
> privacy policy don’t make clear is that the iOS version of the
> Zoom app is sending some analytics data to Facebook, even if Zoom
> users don’t have a Facebook account, according to a Motherboard
> analysis of the app. […]
> “That’s shocking. There is nothing in the privacy policy that
> addresses that,” Pat Walshe, an activist from Privacy Matters who
> has analyzed Zoom’s privacy policy, said in a Twitter direct
> message.


Zoom subsequently removed the Facebook integration code and [fast-tracked an update to the App Store](https://www.vice.com/en_us/article/z3b745/zoom-removes-code-that-sends-data-to-facebook). But still. This is a company with a history of playing fast and loose with privacy and security. You may recall last summer, when it came to light that the Mac version of Zoom secretly installed a web server, which remained installed and running even if you deleted the Zoom app from your machine. Shockingly, this enabled a security exploit that allowed hackers to take control of your Mac’s camera — the sort of privacy nightmare scenario that leads folks to tape over their cameras. [Zoom called this hidden unremovable-through-normal-means web server a feature, not a bug](https://daringfireball.net/linked/2019/07/10/nguyen-zoom). The bug was so insidious that [Apple had to push a silent MacOS update](https://techcrunch.com/2019/07/10/apple-silent-update-zoom-app/) to remove Zoom’s hidden web servers.


[I wrote at the time](https://daringfireball.net/linked/2019/07/10/zoom):


> I’m not prone to histrionics but this is genuinely outrageous —
> not even to mention the fact that Leitschuh reported this to Zoom
> months ago and Zoom effectively shrugged its corporate shoulders.
> If you ever installed Zoom, I’d go through the steps to eradicate
> it and never install it again.


This Facebook data issue is nowhere near as bad as the web server issue. But it betrays Zoom’s institutionally cavalier attitude to privacy. Their privacy policy [more or less grants them carte blanche to do whatever the hell they want](https://twitter.com/dhh/status/1243901794138218496).


Mistakes happen. Bugs happen. I not only forgive mistakes, I enjoy forgiving mistakes. But Zoom’s callous disregard for privacy does not seem to be a mistake. As Zoom itself said about the hidden web server they secretly installed on Macs, it’s a feature not a bug.


Alas, Zoom’s video conferencing technology is [best of breed](https://www.protocol.com/zoom-videoconferencing-history-profit), and because Zoom is easy to use and the quality is so high, it is exploding in popularity now that the whole world is working and socializing remotely. All of the following can be — and I believe are — true: Zoom is popular, useful, and [by their own admission](https://zoom.us/privacy) not trustworthy.


If you must use Zoom or simply want to use it, I highly recommend using it on your iPad and iPhone only.1 The iOS version is sandboxed and reviewed by the App Store. The Mac version of Zoom is not available through the App Store, which makes me trust it not a bit. Much of the Mac software I rely on every day is *not* from the App Store — but all of it comes from developers I trust, who have proven reputations.


Zoom is not on that list.


**Update:** On the Mac, Zoom requires the use of an installer, and Zoom’s installer experience is… [not confidence inspiring](https://twitter.com/cabel/status/1244784268993130499). The entire installation takes place [during the *preflight* stage of the installation](https://twitter.com/realmrpippy/status/1244741950562918400). Again, that’s clearly not an oversight or honest mistake. Everyone knows what “preflight” means. It’s a complete disregard for doing things properly and honestly on Zoom’s part. There’s no way to check what files will be installed, or where, before their installer has gone ahead and installed them. ([Hacker News thread with details](https://news.ycombinator.com/item?id=22706650).)


**Update 2:** [Zoom also has a web version](https://support.zoom.us/hc/en-us/articles/201362193-Joining-a-Meeting), with fewer features than the desktop app. If you need to use Zoom from your Mac, try that — using a private browser window — before you download and install their app.


In closing, I’ll turn the virtual mic over to Doc Searls, who wrote this in the closing paragraphs of [the first of a series of posts on Zoom and privacy](https://blogs.harvard.edu/doc/2020/03/27/zoom/):


> Here’s the thing: *Zoom doesn’t need to be in the advertising
> business*, least of all in the part of it that lives like a
> vampire off the blood of human data. If Zoom needs more money, it
> should charge more for its services, or give less away for free.
> Zoom has an extremely valuable service, which it performs very
> well — better than anybody else, apparently. It also has a
> platform with lots of apps with just as absolute an interest in
> privacy. They should be concerned as well. (Unless, of course,
> they also want to be in the privacy-violating end of the
> advertising business.)
> What Zoom’s current privacy policy says is worse than “You don’t
> have any privacy here.” It says, “We expose your virtual necks to
> data vampires who can do what they will with it.”


---

1. It’s worth noting that iPhones and iPads have much better front-facing cameras than any MacBook — you’ll look better on Zoom using one. ↩︎



| **Previous:** | [Curse Words](https://daringfireball.net/2020/03/curse_words) |
| **Next:** | [Amazon and Apple Strike Deal for Prime Video In-App Purchases and Subscriptions](https://daringfireball.net/2020/04/amazon_apple_prime_video) |


PreviousNext