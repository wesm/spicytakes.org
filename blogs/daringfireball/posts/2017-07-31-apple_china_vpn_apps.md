---
title: "On Apple Removing VPN Apps From the App Store in China"
date: 2017-07-31
url: https://daringfireball.net/2017/07/apple_china_vpn_apps
slug: apple_china_vpn_apps
word_count: 1368
---


[From the company blog of ExpressVPN](https://www.expressvpn.com/blog/china-ios-app-store-removes-vpns/amp/), a major VPN provider serving users in China:


> We received notification from Apple today, July 29, 2017, at
> roughly 04:00 GMT, that the ExpressVPN iOS app was removed from
> the China App Store. Our preliminary research indicates that all
> major VPN apps for iOS have been removed.
> Users in China accessing a different territory’s App Store (i.e.
> they have indicated their billing address to be outside of China)
> are not impacted; they can download the iOS app and continue to
> receive updates as before. […]
> Users in China can continue to stay connected to the open internet
> with ExpressVPN’s apps for Windows, Mac, Android, and other
> platforms.


From [Paul Mozur’s report for The New York Times](https://mobile.nytimes.com/2017/07/29/technology/china-apple-censorhip.html):


> Sunday Yokubaitis, president of Golden Frog, a company that makes
> privacy and security software including VyprVPN, said its
> software, too, had been taken down from the app store.
> “We gladly filed an amicus brief in support of Apple in their
> backdoor encryption battle with the F.B.I.,” he said, “so we are
> extremely disappointed that Apple has bowed to pressure from China
> to remove VPN apps without citing any Chinese law or regulation
> that makes VPN illegal.”
> He added, “We view access to internet in China as a human rights
> issue, and I would expect Apple to value human rights over
> profits.”


That’s a popular sentiment — that Apple should have stood up to China’s demands and accepted the consequences, even if it meant losing sales in China. But it’s disingenuous to pretend that this situation is not fraught with complications.


It’s also disingenuous to claim Apple has “bowed to pressure from China
to remove VPN apps *without citing any Chinese law or regulation that makes VPN illegal*”. The very next paragraph in the Times story says:


> In a statement, Apple noted that the Chinese government announced
> this year that all developers offering VPNs needed to obtain a
> government license. “We have been required to remove some VPN apps
> in China that do not meet the new regulations,” the company said.
> “These apps remain available in all other markets where they do
> business.”


[Here’s a story from The South China Morning Post in January about this crackdown](http://www.scmp.com/news/china/policies-politics/article/2064587/chinas-move-clean-vpns-and-strengthen-great-firewall):


> Beijing has launched a 14-month nationwide campaign against
> unauthorised internet connections, including virtual private
> network (VPN) services, which allow users to bypass the country’s
> infamous “Great Firewall”.
> A notice released by the Ministry of Industry and Information
> Technology on Sunday said that all special cable and VPN services
> on the mainland needed to obtain prior government approval — a
> move making most VPN service providers illegal.


Here’s a story from earlier this month [about the Waldorf Astoria in Beijing being forced to remove the VPN service that had previously been provided for guests](http://technode.com/2017/07/19/vpns-continue-to-feel-the-pressure-as-a-beijing-luxury-hotel-halts-service/). New York Times reporter Paul Mozur (who lives in Beijing) posted to Twitter today [that Amazon is sending cease and desist letters to AWS customers using VPNs in China](https://twitter.com/paulmozur/status/891963757508706304). Apple is not alone.


Too many people reacting to this story think that it’s about Apple deciding to acquiesce to this particular demand regarding VPN apps. It’s not. The real issues are two-fold:

- Should Apple be doing business in China at all?
- Should the App Store remain the only way to install apps on iOS devices?


Neither of these are simple topics, and I would (and am about to) argue that neither question has a clear-cut “this is the right thing to do” answer.


First, let’s dispose of the notion that Apple could have chosen to defy the Chinese government and keep the VPN apps in the App Store. Technically, Apple could have done that. But if they had, there would have been consequences. My guess is that the Chinese government would move to block all access to the App Store in China, or even block access to all Apple servers, period. This would effectively render all iOS devices mostly useless. iPhones have been [sagging in popularity in China for a few years now](https://stratechery.com/2017/apples-china-problem/) — with no access to apps, their popularity would drop to zero. And Apple would have a lot of angry iPhone-owning users in China on its hands.


If Apple tugged on the “*We refuse to remove these VPN apps from the App Store*” thread, it would inextricably lead to their leaving the entire Chinese market. It’s easy to say “Apple shouldn’t have removed these apps.” It’s not so easy to say “Apple should pull out of China.” This is of course further complicated, politically, by the fact that the vast majority of Apple’s supply chain is in China.


You *can* say it though. Yes, China is Apple’s second-biggest market in the world, [accounting for almost $11 billion in revenue in the quarter that ended three months ago](https://www.cnbc.com/2017/05/03/apple-earnings-china-sales-tim-cook-enthusiastic.html). But Apple *could* take a stand and draw the line in the sand here.


If you really think VPN apps in the App Store is the hill Apple should die on in China, I get it. But I do not agree.


As I see it, there are only two scenarios:

- A China where people can buy and use iPhones, but can’t get VPN apps from the App Store.
- A China where people can’t buy or use iPhones.


The first scenario is obviously better for Apple financially. But I would argue that the first scenario is *also* better for the people of China.


The thing I keep thinking about is that iMessage and FaceTime are among the few protocols available inside China with end-to-end encryption. [The Chinese just started blocking WhatsApp a few weeks ago](https://www.nytimes.com/2017/07/18/technology/whatsapp-facebook-china-internet.html). I don’t know why they allow iMessage and FaceTime to continue working, but they do, and both of those protocols are designed from the ground up to *only* work using end-to-end encryption. There is no “off switch” for iMessage encryption that Apple can flip inside China. If you’re using iMessage, it’s encrypted. It would surprise no one if China started blocking iMessage and FaceTime, but for now, their availability is a real benefit to the people of China that seems to go largely unrecognized.


To me, the more interesting question isn’t whether Apple should be selling its products in China, but rather whether Apple should continue to make the App Store the only way to install apps on iOS devices. A full-on “install whatever you want” policy isn’t going to happen, but something like [Gatekeeper](https://support.apple.com/en-us/HT202491) on MacOS could.


Keep iOS App Store-only by default. Add a preference in Settings to allow apps to be downloaded from “identified developers” (those with an Apple developer certificate) in addition to the App Store. In that scenario, the App Store is no longer a single choke point for all native apps on the device.


The App Store was envisioned as a means for Apple to maintain strict control over the software running on iOS devices. But in a totalitarian state like China (or perhaps Russia, next), it becomes a source of control for the totalitarian regime.


I don’t expect Apple to do this. They’d rather deal with the negative consequences of the App Store as a choke point than give up the benefits (including the profits) of maintaining complete control over all software on the platform.1 But if you’re angry about Apple’s role in this VPN crackdown in China, I suggest you direct your anger at the App Store as the single source for third-party software.


---

1. It’s worth noting that it’s not quite true that all software on iOS must come from the App Store. Anyone with a developer account can compile and install apps on their iOS devices from Xcode. There are a number of open source apps for iOS that are [distributed this way](http://willhains.com/post/145882768224/introducing-kotoba). Open source VPN clients could be a workaround — albeit one with a high technical expertise barrier — for this VPN situation in China. ↩︎



| **Previous:** | [Unordered Lists in Markdown](https://daringfireball.net/2017/07/unordered_lists_in_markdown) |
| **Next:** | [Conjecture Regarding the Precise Details of the iPhone D22 Display Resolution](https://daringfireball.net/2017/08/d22_display_conjecture) |


PreviousNext