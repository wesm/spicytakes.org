---
title: "Exploring, in Detail, Apple’s Compliance With the EU’s DMA Mandate Regarding Apple Watch, Third-Party Accessories, and the Syncing of Saved Wi-Fi Networks From iPhones to Which They’re Paired"
date: 2025-11-23
url: https://daringfireball.net/2025/11/apple_eu_dma_iphone_accessories_wi-fi_sync
slug: apple_eu_dma_iphone_accessories_wi-fi_sync
word_count: 5067
---


There have been several new features that have been delayed in the EU while Apple tried to make them compliant with the DMA. iPhone Mirroring [debuted over a year ago with iOS 18 and MacOS 15 Sequoia](https://support.apple.com/en-us/120421), but still remains unavailable today in the EU. Apple Intelligence [was delayed in the EU until iOS 18.4](https://9to5mac.com/2025/04/01/apple-intelligence-is-now-fully-supported-in-the-eu-with-ios-18-4/) in April, but was [available to most of the world in 18.1](https://www.macrumors.com/2024/10/28/apple-releases-ios-18-1/) last October. And, both most recently and briefly, the [live translation feature](https://support.apple.com/en-us/123185) for AirPods Pro 3, AirPods Pro 2, and AirPods 4, which debuted outside the EU with the launch of iOS 26.0 in September, [will only become available in the EU next month](https://www.apple.com/ie/newsroom/2025/11/live-translation-on-airpods-expands-to-the-eu/), with the launch of iOS 26.2.


But now comes word of the first feature that Apple is limiting or removing in an existing product to comply with the DMA: Wi-Fi network sync between iPhone and Apple Watch, which is poised to change in the EU next month, with the 26.2 releases of iOS and WatchOS. The news was broken by Nicolas Lellouche, [reporting for the French-language site Numerama](https://www.numerama.com/tech/2110247-lapple-watch-et-liphone-vont-perdre-une-fonction-en-europe-pour-la-premiere-fois-annonce-apple.html). I’m quoting here from Safari’s English translation of his original report:


> Apple has been warning for several months that it could one day,
> if it deems it necessary, disable functions in the European Union
> to “protect its users”. This day could arrive in December, with
> the iOS 26.2 update.
> On November 4, Apple announced to Numerama that it had made the
> decision to disable Wi-Fi synchronization between an iPhone and an
> Apple Watch in Europe so as not to have to comply with the
> European Commission’s request, which wants to force it by the end
> of 2025 to open the iPhone’s Wi-Fi to third-party accessories.
> This announcement follows the opening of the AirPods Live
> Translation function in Europe, with a new API to allow
> competitors to use the microphones and speakers of AirPods and
> iPhone simultaneously. [...]
> Apple indicates that the European Commission is asking it to
> replicate the link between an iPhone and an Apple Watch, but with
> third-party products. Apple, after thinking long about how to
> implement this function, finally decided to reject the European
> request. Since Europe requires that third-party products be
> treated like the Apple Watch, then Apple disables the function on
> Apple Watch. This allows it to comply with the DMA.


Lellouche’s report at Numerama broke this story (the reports at [MacRumors](https://www.macrumors.com/2025/11/06/iphone-apple-watch-wi-fi-sync-eu-ios/) and [9to5Mac](https://9to5mac.com/2025/11/05/ios-26-2-will-remove-a-key-iphone-and-apple-watch-feature-in-eu-per-report/) are both based on Numerama’s), but the above is not an accurate summary of what Apple is doing with iOS 26.2.1 Apple *is* complying with the DMA, and they’re *not* disabling Wi-Fi network synchronization between an iPhone and a paired Apple Watch. What Apple is doing, in order to comply with the DMA, is changing how Wi-Fi networks sync with Apple Watch (in the EU), and offering new APIs in the EU for third-party paired devices to put them on equal (or near-equal?) footing with Apple Watch (in the EU).


This change should be relatively limited. Honestly, I don’t think many Apple Watch users in the EU will even notice. But it is at least mildly annoying, and the relatively minor, very specific nature of this particular DMA mandate makes it a telling example of the European Commission’s overreach.


Currently, when you pair a new Apple Watch with an iPhone, iOS transfers to WatchOS the iPhone’s entire list of saved Wi-Fi networks and their passwords — directly, device-to-device. As iOS learns of new networks that the user joins from their iPhone, that information continues to be shared with any Apple Watches paired to that iPhone. The utility of this is that if you’re wearing your Apple Watch, but don’t have your iPhone nearby, your watch will join an available saved Wi-Fi network at your location. Let’s say you go for a run or walk, with only your Apple Watch, and you stop at a cafe for a beverage. If you’ve ever joined the Wi-Fi network at that cafe from your iPhone (or iPad or Mac, assuming you sync your Apple Keychain via iCloud), your Apple Watch will join that network automatically. It should, and in my personal experience does, just work.


The EU mandate to Apple is *not* that Apple must grant to third-party devices and their iOS companion applications this same functionality as it stands today — that is to say, access to the entire history of the iPhone’s known Wi-Fi networks. The EU mandate is that Apple must grant to third-party devices the same level of access to Wi-Fi network information that Apple Watch has. Apple is complying with this mandate in two ways: (a) by changing how much Wi-Fi network information an Apple Watch gets from the iPhone to which it is paired; and (b) creating a new framework in iOS 26.2 (gated by a new entitlement), [Wi-Fi Infrastructure](https://developer.apple.com/documentation/wifiinfrastructure), that provides a set of public APIs, available only to apps in the EU, to (per the framework’s description) “share Wi-Fi network credentials securely between devices and connected accessories.”


The change for Apple Watch in the EU is that starting with iOS 26.2, when a new (or reset) Apple Watch is set up, the Apple Watch will no longer have the user’s list of saved Wi-Fi networks automatically synced from their iPhone. Only future networks will be synced — the same level of access that the new Wi-Fi Infrastructure framework is making available to third-party accessories.


Under the new rules for Apple Watch in the EU, an existing (that is to say, already configured) watch that is upgraded to WatchOS 26.2 will still remember all Wi-Fi networks it already knew about. But a new Apple Watch will only be able to automatically connect to Wi-Fi networks that its associated iPhone saves *after* the Apple Watch was set up and paired. So when an EU Apple Watch owner with a new watch visits a known location, and doesn’t have their iPhone with them, the watch won’t be able to join that location’s Wi-Fi automatically, unless the paired iPhone has connected to and saved that network *after* the watch was paired.


With iOS 26.2, the behavior for users outside the EU will remain unchanged from iOS 26.1 and prior — both for Apple Watch and for third-party accessories.


A user’s Wi-Fi history can be used to glean significant information about them. Who they know (other homes’ networks), where they’ve been (medical providers, restaurants, airports), and more. Apple’s new policy for Apple Watch and third-party devices is DMA-compliant and prevents the sharing of historical networks, but with the sharing of future networks as the associated iPhone joins them, there’s still a risk here of third-party companies doing things with the user’s Wi-Fi network information that the user doesn’t understand, or want (but doesn’t realize they’ve consented to).


One way to look at Apple’s options for complying with this particular DMA mandate is by considering the extremes. On the one extreme, Apple could have just granted third-party peripherals in the EU the exact same access to users’ iPhone Wi-Fi network history that Apple Watch has gotten until now (and will continue to get outside the EU). On the other extreme, Apple could have cut off Wi-Fi network syncing to the Apple Watch altogether, requiring users to connect to each Wi-Fi network manually, using the Watch itself or the Apple Watch app on iPhone. Instead, Apple chose a middle ground — limiting Wi-Fi network history sync to the Apple Watch in the EU in ways that it isn’t limited anywhere else in the world, but granting third-party accessories in the EU access to these new Wi-Fi Infrastructure APIs that aren’t available outside the EU.


Critics might argue that while this middle ground is technically compliant with the DMA, it’s not compliant with the *intention* of the DMA, which would be for the Apple Watch not to lose any functionality in the EU, and for Apple to provide APIs to allow third-party devices all of the Wi-Fi syncing features currently available to Apple Watch. Apple would argue, and I agree, that the European Commission’s intentions are incoherent in this regard. The EC insists that Apple should protect users’ privacy and security, while also insisting that Apple grant access to third-party apps and devices that can potentially compromise users’ privacy and security.


There’s a reason why Apple isn’t offering the new Wi-Fi Infrastructure framework outside the EU, and that’s because they don’t believe it’s a good idea to grant any access at all to your saved Wi-Fi networks to third-party apps and devices. Especially without being able to specify, let alone enforce, a policy that Wi-Fi network information should be treated the way Apple treats it — remaining exclusively on device.


The skeptical take on Apple’s motivations in this situation is that Apple is spitefully removing functionality from Apple Watch rather than offering new APIs to provide third-party devices with the same functionality that Apple Watch currently has, and that Apple’s intention here is, somehow, primarily about trying to drive anti-DMA sentiment amongst its EU users. This is, in fact, the skeptical take on every single aspect of Apple’s compliance with the DMA: spiteful “malicious compliance” that, somehow, is intended to engender grassroots opposition to the DMA amongst Apple customers in the EU. I don’t think that’s an accurate take overall, but in this particular case with Apple Watch and Wi-Fi network sync, it’s almost silly.


Part of what makes this particular situation clarifying is that it’s so specific. It’s not about allowing third-party devices and their corresponding iOS apps to do *everything* that Apple Watches, and the Apple Watch iOS companion app, can do. It’s very specifically about the sharing of known Wi-Fi networks. (There will, surely, be other such situations to come regarding other features, for other Apple devices.) And as I described above, very few Apple Watch owners in the EU are likely to notice the change. How many Apple Watch users today realize that their watch automatically connects to known Wi-Fi networks when their iPhone is outside Bluetooth range?


If Apple were motivated by spite, and were trying to turn EU Apple Watch owners against the DMA, they’d just remove all Wi-Fi network syncing between the watch and its paired iPhone. Not just the historical list of all networks the iPhone has ever connected to, but the continuous sync of new networks the iPhone joins after the Apple Watch is paired. *That* would be a change Apple Watch users would be more likely to notice. But it’s not what Apple is doing. They’ve engineered an entire framework of public APIs to comply with the EC’s mandate.


But the reporting to date on this situation, starting with Numerama, paints the picture that Apple *is* dropping all Wi-Fi sync between WatchOS and iOS in the EU, and that Apple is refusing to make Wi-Fi network information available to third-party accessories.


[Here’s Michael Tsai](https://mjtsai.com/blog/2025/11/06/ios-26-2-to-remove-iphone-apple-watch-wi-fi-sync-in-eu/), after quoting from Tim Hardwick’s summary at MacRumors of Numerama’s report:


> It seems perfectly reasonable that if I have a third-party watch I
> should be able to opt into having my phone share Wi-Fi info with
> it. You can debate whether mandating this is the proper role of
> government, but the status quo is clearly anti-competitive and bad
> for the user experience. I’m open to hearing a story where Apple’s
> position makes sense, but so far it just seems like FUD to me.
> What is the argument, exactly? That Fitbit, which already has its
> own GPS, is going to sell your access point–based location
> history? That Facebook is going to trick you into granting access
> to their app even though they have no corresponding device?


Tsai is making a few wrong assumptions here. First, Apple *is* enabling users (in the EU) to opt into having their iPhone share Wi-Fi information with third-party devices. Second, this mandate is not specific to smartwatches — it applies to any devices that can pair with an iPhone and have corresponding iOS partner apps. So Meta, with their lineup of smartglasses, *does* have corresponding devices. And, [per Apple’s public statements](https://www.reuters.com/technology/apple-slams-metas-numerous-interoperability-requests-2024-12-18/), it is Meta in particular that has been zealously pursuing interoperability mandates pursuant to the DMA. I think it’s entirely possible that this entire issue regarding Wi-Fi network sharing was prompted by Meta’s interoperability requests to the European Commission.2


As for the argument regarding why Apple has chosen to comply in this way, what is essential to note is that *none* of this Wi-Fi network information shared between iOS and WatchOS *is ever sent to or seen by Apple*. Apple doesn’t see the network passwords, doesn’t see the names of the networks, and doesn’t even know when a device has joined a new network. All of this is exclusively on-device, and when the information is exchanged between an iPhone and paired Apple Watch, it’s transferred device-to-device. (This is also true when you use Apple’s features to share Wi-Fi passwords with nearby friends. It’s device-to-device and entirely private and secure. Apple doesn’t even know that person A sent a Wi-Fi password to person B, let alone know the name of the network or the password.)


[Here’s Rui Carmo, at Tao of Mac](https://taoofmac.com/space/links/2025/11/07/0732):


> As someone who relies a lot on the Watch (especially now that
> WhatsApp works locally on it), I’d say we have officially reached
> the point where Apple is on the verge of actively harming their
> user experience for no good reason whatsoever. I honestly don’t
> know if this is bull-headedness or malicious compliance.
> On the other hand, someone at the EU clearly prefers being in the
> limelight by regulating against evil US corporations in ways that
> affect very small parts of the general population rather than,
> say, go after Asian smart TV manufacturers that are present in
> millions of homes and resell data on Europeans’ TV viewing habits.


No notes on Carmo’s second point. But regarding the first, his opinion is founded on incorrect assumptions. Apple clearly thinks it’s a bad idea to share any Wi-Fi information at all with third-party devices, but they’ve created an entire new framework for use within the EU to allow it, just so they can continue syncing any Wi-Fi network information at all with Apple Watch. Far from harming the user experience, Apple is bending over backwards to make the Apple Watch experience as good as possible while balancing the privacy and security implications of this DMA mandate. Rather than take away all Wi-Fi network syncing, Apple is leaving most of it in place, and only eliminating (in the EU) the part at the very beginning, where, during the set up process, all of the current networks saved on the iPhone are synced to the Apple Watch.


Given the mandate regarding the DMA, and given the privacy implications of sharing any of this information with third-party developers and peripheral makers, personally, I think it would have been reasonable for Apple to take the extreme position of simply disallowing Wi-Fi network information syncing to any and all devices, including Apple Watches, in the EU. There is no reason to trust third-party developers with any of this information. But Apple isn’t doing that, and they’ve undertaken a significant software engineering effort — just for the EU — to support the path they’ve chosen. Carmo’s critique seems predicated on the assumption that Apple is just cutting off all Wi-Fi network sharing.


Given that Apple’s compliance needs to account for potentially untrustworthy device makers — whether by [intent](https://www.axios.com/2022/08/23/meta-lawsuit-settlement-facebook-location-tracking), or [incompetence](https://www.techradar.com/pro/security/portable-lifeprint-printer-app-on-ios-and-android-leaked-millions-of-user-photos-and-sensitive-data-this-is-what-we-know) — not syncing all known networks seems like a reasonable trade-off.


Leave it to [Tim Sweeney to espouse the maximalist perspective](https://x.com/TimSweeneyEpic/status/1986222627003023630?s=20):


> Why simply not ask the user whether or not to share WiFi history
> identically whether connecting to an Apple product or a Meta
> product?


That is, in fact, what Apple is doing. But the privacy implications for a user are, in fact, different when an iPhone’s saved Wi-Fi networks are shared to, say, a Meta product than to another Apple product. It’s worth emphasizing that the European Commission’s mandate does not permit Apple to require those third-party companies to treat this information with the same privacy protections that Apple does. Apple keeps that information exclusively on-device, but Apple is not permitted to require third-party peripheral makers to do the same.


Consider [the iOS system prompt for App Tracking Transparency](https://support.apple.com/en-us/102420): the user’s two choices are “Ask App Not to Track” and “Allow”. It’s a common and natural question why the first option is “Ask App Not to Track” rather than “Don’t Allow”. It would certainly look better if the options were “Don’t Allow” and “Allow”. But Apple deliberately made the first button “Ask App Not to Track” because ATT is, at least partially, a *policy*, not a complete technical guarantee. If an app prompts for ATT permission and the user chooses “Ask App Not to Track”, that app should definitely *not* go ahead and attempt to track the user’s activity across other apps. But, technically, it could try.3 I presume that if they do, if and when Apple notices, Apple will rap the developer’s knuckles in the App Store review process, or even suspend the app’s developer account. But one can see why Apple would want to avoid [such a pissing match with Facebook/Meta again](https://arstechnica.com/gadgets/2019/01/facebook-and-google-offered-gift-cards-for-root-level-access-to-ios-users-data/).4


Under the EU’s mandate to Apple regarding Wi-Fi network access for third-party devices and their corresponding iOS apps, Apple is not permitted even to set a policy that these apps must pinky swear to keep the information private and on-device. Nor is the EU itself demanding it. If a third-party device-maker wants to send your iPhone’s Wi-Fi network history and credentials to their servers and save it, that’s up to them, *not* Apple, per the EC. Apple sees that as a problem.5 You can argue — and some will, as I think Michael Tsai does in the passage I quote above, and as Tim Sweeney clearly does — that this ought to be up to the user. If a user says they’re fine with their Wi-Fi network information being shared with a third-party accessory they’ve paired with their iPhone, that’s up to them. That is a reasonable take. But I also think Apple’s perspective is reasonable as well — that they should be able to make products where this isn’t possible.


The “it should be up to the user” take benefits informed, technically savvy users. The “it shouldn’t be possible” take benefits uninformed, un-savvy users — users who in many cases have decided that they simply trust Apple. The iPhone brand message — the brand message behind the Apple ecosystem — is that Apple doesn’t allow things that are dangerous to security or privacy. I do not think most iPhone users expect a third-party device they pair to their iPhone to be able to send their entire history of Wi-Fi networks back to the company that made the device. (Most iPhone users also don’t realize how sensitive, privacy-wise, their complete Wi-Fi network history is.)


It’s fair to point out that the “it should be up to the user” take is more beneficial to third-party accessory makers than the “it shouldn’t be possible” take. And that this conflict of interest — where the same limitations that protect iPhone users’ privacy by definition disadvantage third-party devices in ways that Apple’s own devices that connect to iPhones are not — works not just in iPhone users’ favor, privacy-wise, but also in Apple’s favor, financially. Apple can sell more Apple Watches if they work better with iPhones than smartwatches from other companies do. That’s obviously true, but that’s just another way of saying that first-party products have inherent advantages that third-party products don’t, to which I say: *Duh*. Apple’s own peripherals, like Apple Watch, can do things that third-party peripherals can’t because Apple can trust its own devices, and its own software, in ways that it can’t trust devices and companion apps made by other companies.


It’s natural for a company to bootstrap a new product on the back of an existing successful one. Meta’s Threads social network, for example, uses the same usernames and sign-in system as Instagram, which is arguably the most successful social network in the world. Should Meta not have been permitted to do that? Or should they be forced to allow *anyone* to create new competing social networks using Instagram user accounts as the ID system?


It’d be pretty weird if Apple limited itself, when designing and engineering features that integrate experiences across *its own* devices, to what it would allow third-party developers to do. It’d be even weirder if Apple allowed third-party developers to do everything Apple’s own software can do.6


For at least the last [15 years](https://daringfireball.net/2010/05/nack_control), I’ve [repeatedly](https://www.google.com/search?q=site%3Adaringfireball.net%20apple%27s%20priorities%3A%20apple%20first%2C%20users%20second%2C%20developers%20third&udm=14) emphasized that Apple’s priorities [are in this order](https://daringfireball.net/2021/06/app_store_the_schiller_cut): Apple first, users second, developers third. The DMA attempts to invert that order, privileging developers first (in the ostensible name of fair competition with Apple, a designated “gatekeeper”), ahead of users, and ahead of Apple itself. So of course Apple is going to object to and resist mandates that require it to subordinate its own strategic desires — its own sense of how its products ought to be designed and engineered — especially when the primary beneficiary of the mandates aren’t users, but developers. Many of whom, especially the larger ones, are Apple’s competitors. But I also think it’s clear, with Apple in particular, that users prefer Apple’s priorities. People are happier with Apple putting users’ considerations ahead of developers’ than they are when developers are free to run roughshod over the software platform.


The clearest example of that is the App Store. It’s overwhelmingly developers, not users, who object to the App Store model — the exclusivity of distribution, the exclusivity of the vendor’s payment system, the vendor’s payment commissions, the vendor’s functional guidelines and restrictions, all of it. Users largely don’t have a problem with any of that. That’s why Apple [commissioned and then publicized a study](https://developer.apple.com/download/files/DMA-Study-Nov-2025.pdf), just this month, that showed that DMA-driven changes saved developers €20 million in commissions, but that reduction in commissions didn’t lower the prices users pay. Developer-focused observers [see that as a win for the DMA](https://pxlnv.com/linklog/apple-dma-commission-study/) — that’s €20 million in developers’ pockets that otherwise would have gone into Apple’s already overflowing pockets. But a user-focused observer might see that as clarifying regarding the fact that the DMA wasn’t designed to benefit users, and isn’t benefiting users in practice either. Apple doesn’t care about €20 million. They fart bigger than that. They do care about clarifying who the DMA prioritizes first, and that it’s not users. (And, of course, that it’s not Apple itself.)


Users love the App Store model. With Apple in particular, users, by and large, *like* the idea that the platforms have stringent guardrails. Many buy iPhones *because* Apple exerts such control over the platform, not *despite* it. But that control is exactly why Apple has been so singularly targeted by the European Commission regarding DMA mandates, despite the fact that Samsung by itself — let alone the Android platform as a whole — [sells more phones in Europe](https://www.gsmarena.com/smartphone_market_in_europe_slips_2_premium_phone_sales_on_the_rise-news-67978.php) (and [the world](https://counterpointresearch.com/en/insights/global-smartphone-share)) than Apple does.


The bottom line is that users setting up new Apple Watches in the EU will now get a slightly worse experience in the name of parity with accessories made by third-party companies. It remains to be seen whether users of third-party iPhone accessories and peripherals in the EU will see any benefit at all (because the companies that make their devices will need to adopt these new EU-exclusive Wi-Fi Infrastructure APIs in their iOS companion apps) — and, if the users of third-party iPhone accessories *do* see the benefit of Wi-Fi network information syncing to their devices, whether their privacy will be respected. But don’t make the mistake of thinking that Apple is complying the least bit spitefully with regard to this mandate.


---

1. I’m quoting Apple/Safari’s French-to-English translation, but the gist seems exactly the same in [Google’s translation](https://www-numerama-com.translate.goog/tech/2110247-lapple-watch-et-liphone-vont-perdre-une-fonction-en-europe-pour-la-premiere-fois-annonce-apple.html?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) as well. ↩︎
2. It remains to be seen whether Meta will actually use the new Wi-Fi Infrastructure framework to allow their accessories, like their [AI Glasses](https://www.meta.com/ai-glasses/), to obtain Wi-Fi network information from [Meta’s companion iOS app](https://apps.apple.com/us/app/meta-ai-vibes-ai-glasses/id1558240027). I’m guessing they almost certainly would, if the Wi-Fi Infrastructure APIs were available globally. But these APIs are exclusive to the EU. Will Meta deem it worth the engineering effort to support this feature only for users in the EU? We shall see.
It’s worth remembering that one of the initial DMA mandates the EU issued to Apple was that iOS must support third-party web browser rendering engines, and to comply with this, Apple spent significant (and I suspect that’s a vast understatement) engineering resources to create the [BrowserEngineKit and BrowserEngineCore](https://developer.apple.com/support/alternative-browser-engines/) frameworks, and here we are at the end of 2025, [nearly two years after Apple shipped those frameworks](https://mastodon.social/@stroughtonsmith/111820566793853249), and there are exactly zero browsers on iOS using alternative rendering engines. Zero. These frameworks might be the largest set of APIs ever created that never get used. I wouldn’t be surprised if the new Wi-Fi Infrastructure framework sees the same fate. (Meta might consider that a win, just knowing that Apple had to expend this effort for naught.) ↩︎︎
3. Apple has a good layperson-approachable [overview of App Tracking Transparency](https://developer.apple.com/app-store/user-privacy-and-data-use/). At a technical level, an app must prompt for and receive the user’s permission (via the Allow button in the system-provided ATT prompt) in order to access the device’s advertising identifier. From that document: “Unless you receive permission from the user to enable tracking, the device’s advertising identifier value will be all zeros and you may not track them as described above.”
But returning zeroes for the device’s advertising identifier doesn’t technically prevent a devious developer from attempting to uniquely identify and track the user by other means. If the button in the system prompt said “Don’t Allow”, rather than “Ask App Not to Track”, it would imply that Apple could guarantee the app isn’t tracking you (or trying to track you) without your permission. Apple can’t guarantee that, so they don’t imply that they can. ↩︎︎
4. I’m not aware of any instances where an app has been accused of disregarding the ATT “Ask App Not to Track” request, but surely it has happened. If you’re aware of any such accusations, and how Apple responded, [let me know](https://daringfireball.net/contact/). ↩︎︎
5. I’m not arguing here that the European Commission doesn’t care about user privacy, or that I think the European Commission doesn’t realize that Wi-Fi network information is quite sensitive. I’m sure they do care about user privacy and do realize that Wi-Fi network information is privacy-sensitive. What I do think is that the European Commission believes the privacy of this information should only be guarded by law, and that they already have laws in place that protect such information. And thus it’s not Apple’s place — especially now that they’ve been deemed a “gatekeeper” that has the power to stymie competition — to attempt to protect that information, whether by technical limitations or by policy.
Apple is certainly not opposed to privacy-protecting laws, in the abstract, but doesn’t see the law alone as protection enough. Apple’s perspective is that protecting their customers’ privacy is, in fact, Apple’s responsibility — and one of their most important responsibilities at that. It’s illegal to steal cars, but every carmaker still puts locks on the doors and requires a key to start the engine. In numerous ways, Apple sees the DMA as mandating, privacy-wise, that they create something akin to cars that don’t require keys, trusting EU law to keep them from being stolen. The European Commission only sees Apple’s protections as blocking would-be competitors, not would-be privacy thieves. ↩︎︎
6. In the old days, of course, with devices designed before the iPhone, this wasn’t weird. All software, whether first- or third-party, could do whatever it wanted to. Anyone could write a kernel extension. In the classic Mac OS days there was no “kernel” and we just had “extensions” and you could just drop one in your Extensions folder, restart, and boom, whatever system extension you just installed was now effectively part of the operating system. Any app could read and write anything on disk, including into the operating system. Go back far enough and apps could read *and write* (deliberately or accidentally) inside the memory of another running application. To split personal computing — not just PCs but all personal computing devices, in the plain sense of the words — into three eras, there was (1) the early era when all software was effectively “root”; (2) the middle era, still exemplified today by MacOS and Windows, when there were user-controlled protections on what could run as root; and (3) the modern era, as exemplified by iOS and stock Android, where the *vendor* controls what can run as root.
You can reasonably make the case — and expert-level users (read: nerds) often do — that the user should always be in control. *I bought the device, I should be able to run whatever software, with whatever privileges, I want.* That perspective is valid, but it also describes a class of devices — PCs — that privilege the autonomy of third-party developers over the vendor-controlled stability of the OS. The PC model, where accessory makers can offer software that runs with root (or root-like) escalated privileges, offers significantly greater opportunities for third-party accessory makers than the mobile model, where accessories are limited to whatever public APIs are provided by the device vendor for integration. But with the PC model, users can “mess up” their system by installing software they shouldn’t have, or that they regret having installed but don’t know how to remove. With the mobile model, users are technically prevented from installing anything that could “mess up” their system. It’s always about trade-offs. And with this particular trade-off, it’s very clear which model is more successful in the market. It’s not feasible to make computers intended for use by anyone and everyone which require any degree of technical knowledge or expertise to manage. ↩︎︎



| **Previous:** | [Meta Replaced the Native Windows WhatsApp App With a Shitty Web App](https://daringfireball.net/2025/11/meta_whatsapp_windows_shitty_web_app) |
| **Next:** | [Signal Secure Backups Are Now Available on iOS](https://daringfireball.net/2025/12/signal_secure_backups_are_now_available_on_ios) |


PreviousNext