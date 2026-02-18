---
title: "Noted Interaction Design and Security Expert Margrethe Vestager Redesigns the iPhone’s NFC Support"
date: 2022-05-04
url: https://daringfireball.net/2022/05/vestager_nfc
slug: vestager_nfc
word_count: 1866
---


From the European Commission, “[Remarks by Executive Vice-President Vestager on the Statement of Objections Sent to Apple Over Practices Regarding Apple Pay](https://ec.europa.eu/commission/presscorner/detail/en/speech_22_2773)”:


> Today, the Commission has sent a Statement of Objections to Apple.
> We are concerned that Apple may have illegally distorted
> competition in the market for mobile wallets on Apple devices.


Apple took a vibrant, perfectly balanced market [where NFC payments were used by almost no one](https://www.cnbc.com/2014/09/11/apple-pay-faces-huge-challenges-paypal-exec.html) and turned it into a market where Apple Pay is accepted at most brick and mortar retailers and millions of iPhone users enjoy using it, with whatever credit and debit cards they choose. Let’s get back to a balanced market, right?


> Apple restricted access to key inputs that are necessary to
> develop and run mobile payment apps, so-called ‘mobile wallets’.


Apple Wallet is more than an app; it’s a feature built into the OS. The core of the E.C.’s complaint is that they think Apple should be legally required to allow third party developers to add features to the OS.


> NFC technology was developed by third parties, is standardised and
> available in almost all payment terminals in Europe. There are
> other technologies, such as those based on QR code, that can be
> used for mobile payments. But NFC technology is the most
> widespread in the EU, and allows for the safest and most seamless
> experience.


This passage, as well as much of the rest of the E.C.’s “statement of objections”, seeks to dismiss the hard work Apple has done to make Apple Pay successful. Yes, NFC is an industry standard, and Apple Pay is, in part, built on top of that. But before Apple Pay, NFC was hardly used, even though [Android had supported it since 2011](https://en.wikipedia.org/wiki/Google_Pay#Android_Pay_and_Google_Wallet_become_Google_Pay). When Apple Pay launched in late 2014, its support for the existing NFC infrastructure was so good, it worked with many credit card terminals that had no explicit support for “Apple Pay” specifically. [The Rite Aid pharmacy chain went so far as to disable its NFC terminals](https://daringfireball.net/2014/10/nfc_apple_pay), blocking even Google Wallet, which they officially supported, just to keep people from using Apple Pay — not for any sort of security or anti-fraud reasons, but because Rite Aid was part of the consortium behind the then-still-in-the-works [CurrentC](https://www.applicoinc.com/blog/happened-currentc-platform-innovation-fails/). CurrentC seems to be the sort of thing the E.C. is seeking to prop up — user-hostile but mid-sized-company-friendly.


Apple Pay was so easy to use people were using it at retailers who weren’t even Apple Pay partners. That’s not a credit to NFC, which had been in place for years. That’s a credit to Apple.


> Apple has built a closed ecosystem around its devices and its
> operating system, iOS. And Apple controls the gates to this
> ecosystem, setting the rules of the game for anyone who wants to
> reach consumers using Apple devices. But other app developers
> depend on the access to this ecosystem to develop innovative
> mobile wallets.


Translation: *Apple designs, implements, and controls iOS.* Amazing scoop from the E.C.’s crack investigation team.


> The potential for innovation in this space is enormous. But this
> innovation has been prevented by Apple refusing others to access
> NFC on its devices. As a result, various features of mobile
> wallets, such as *financial* complementary services, are simply
> not available. Because Apple is not challenged, it has little
> incentives to innovate itself.
> And this is important. Because this market is growing fast.
> Today, Apple Pay, is by far the largest NFC based mobile wallet
> on the market.


The E.C. complaint wavers between claiming Apple Pay dominates NFC payments on iPhones and dominates the entire industry. The latter was true as recently as October 2017, [when Apple Pay accounted for 90 percent of all contactless transactions globally](https://techcrunch.com/2017/10/23/apple-pay-now-in-20-markets-nabs-90-of-all-contactless-transactions-where-active/), where it was available. [As I noted at the time](https://daringfireball.net/linked/2017/10/24/apple-pay-90-percent), that’s a remarkable achievement for a platform that by all accounts is a distant second to Android in global market share.


[Here’s a study from last year](https://www.talkandroid.com/369056-google-pay-samsung-pay-dominated-by-apple-pay-us/) that claims in the U.S., Google Pay has 3 percent share, Samsung Pay 5 percent, and Apple Pay 92 percent. You know, your classic three-way neck-and-neck horse race.


As for innovation, just two months ago [Apple introduced Tap to Pay on iPhone](https://www.apple.com/newsroom/2022/02/apple-unveils-contactless-payments-via-tap-to-pay-on-iphone/), which Apple describes thus (italic emphasis added):


> Apple today announced plans to introduce Tap to Pay on iPhone. The
> new capability will empower millions of merchants across the US,
> from small businesses to large retailers, to use their iPhone to
> seamlessly and securely accept Apple Pay, contactless credit and
> debit cards, *and other digital wallets* through a simple tap to
> their iPhone — no additional hardware or payment terminal needed.
> Tap to Pay on iPhone will be available for payment platforms and
> app developers to integrate into their iOS apps and offer as a
> payment option to their business customers. Stripe will be the
> first payment platform to offer Tap to Pay on iPhone to their
> business customers, including the Shopify Point of Sale app this
> spring. Additional payment platforms and apps will follow later
> this year.


It’s the NFC payment terminals in retailers that are built to only accept credit and debit cards. With a system Apple has designed entirely on its own — the new Tap to Pay on iPhone system — they’re including support for other wallets from the get-go. I honestly don’t understand where the E.C. sees anticompetitive behavior with Apple Pay. What I see is market share dominance stemming from the hard work of designing better integration into iOS and iPhones and educating users about the feature. How else could the iPhone’s share of NFC payments so far exceed the iPhone’s share of mobile phone sales? I’m not saying Samsung and Google suck at this, per se, but Jennifer Bailey’s team at Apple is *really* good, and perhaps just as importantly, really *diligent* about this sort of thing.


Back to Vestager’s comments:


> Apple claims that for security reasons it cannot provide access to
> NFC for payments. According to Apple, security risks would
> increase if access were to be granted to third parties. We take
> security very seriously. Our investigation to date did not reveal
> any evidence that would point to such a higher security risk. On
> the contrary, evidence on our file indicates that Apple’s conduct
> cannot be justified by security concerns.


This dismissiveness on the part of the E.C. is infuriatingly facile. Could and should there be APIs that allow iOS apps to make use of NFC, securely? I think yes. I also think it’s quite likely that Apple is working on them. All sorts of features that were once only the purview of Apple in iOS are now open to third-party developers, like system-wide alternative keyboards, setting third-party apps to serve as default handlers for web browsing and email, and more. But there are always going to be features that are rightfully part of the system itself. And to a large extent, I think Apple Pay is one of them.


Consider the details of how NFC support might work for third-party “wallet” apps on iOS. I would imagine it work something like this:

1. Unlock your iPhone.
2. Open the third-party app you want to use.
3. Tap a button in the app to go into NFC search mode.
4. Hold the iPhone near the NFC terminal.
5. Re-authenticate with Face ID to confirm.


Would that satisfy the E.C.? It should, but I don’t know that it will, because that’s not as streamlined as paying with Apple Pay:

1. Double-click the hardware side button on the iPhone (no need for the iPhone to be unlocked).
2. Authenticate with Face ID/Touch ID.
3. Hold iPhone to NFC terminal.


Or consider the ultimate in convenience: [riding transit with Apple Pay express mode](https://support.apple.com/en-us/HT212171):

1. Just hold your locked iPhone near the reader. No buttons to click, no authentication necessary.


Express mode works with things like car keys, hotel rooms, and student IDs, too. This feature is so deeply integrated with the system that it can [even work when the iPhone is in power reserve mode when the battery is nearly depleted](https://support.apple.com/en-us/HT212171).


I don’t see how the security implications of any of these features — payments, car keys, getting into hotel and dorm rooms — are not obvious.


Should third-party wallet apps be allowed to take over the double-click-of-the-side-button feature? Should they be able to take over the volume buttons and mute switch too? Those buttons have been, and should remain, Apple’s purview. (Apple does allow camera apps to use the volume buttons as shutter buttons, like the system Camera app does, but, for example, you can’t make a game that uses the volume buttons as game controls, or an app that uses the mute switch to toggle between, say, light and dark modes.)


I mean, it’s all just ones and zeroes. Apple *could* allow users to add third-party wallet apps and grant them permission to be invoked simply by double-pressing the side button. But what happens then? Do you get an extra step where the user has to choose which wallet to use, Apple Wallet or a third-party one? Or does the third-party one replace Apple Wallet? What happens when you add a second third-party wallet app? It would get confusing very quickly.


Is it limiting that Apple Wallet is the only wallet on iOS? Yes. Is it simpler and easier to understand that way? Yes. Is that why Apple Pay dominates the contactless payment market worldwide, despite Android having supported NFC payments years before iOS did *and* having far larger market share in handset sales? I say yes, undoubtedly.


Is the E.C.’s argument that any third-party app should be able to wake up and respond to an NFC tap? As it stands, Apple can truthfully claim that using NFC with an iPhone is guaranteed to be secure and trustworthy. How could they claim that if they allowed third-party apps to take over that role? If that’s not what the E.C. is asking for, then the E.C. should describe, explicitly, what it is they are asking for.


Whose third-party wallet app is being stomped upon by iOS today? Who’s the aggrieved party here? To me it’s clear that the wallet itself belongs as part of the system. It’s the elements inside the wallet that should be open to third-party apps, which is exactly how Apple Wallet works. That NFC card readers in retail point-of-sale terminals only work with credit and debit cards isn’t Apple’s fault or responsibility, and Apple Pay integrates with any and all credit and debit cards that choose to support Apple Wallet. The E.C. complaint would make more sense if Apple Card was the only card Apple Wallet supported, but it’s not.


What, exactly, should Apple have done differently that would have appeased the E.C.? I genuinely can’t come up with an answer for this.



| **Previous:** | [More Rumors on Apple Obtaining the Rights to NFL Sunday Ticket](https://daringfireball.net/2022/04/apple_nfl_sunday_ticket) |
| **Next:** | [A Touching Goodbye for iPod](https://daringfireball.net/2022/05/touching_goodbye_for_ipod) |


PreviousNext