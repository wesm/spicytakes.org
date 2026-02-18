---
title: "The iOS Continental Drift Widens"
date: 2024-09-06
url: https://daringfireball.net/2024/09/the_ios_continental_drift_widens
slug: the_ios_continental_drift_widens
word_count: 4861
---


At the end of August, [Apple announced several more DMA compliance changes](https://developer.apple.com/news/?id=zglax7gc). They are worth examining in detail.


## Changes to the Mandatory Browser Choice Screen


> Developers of browsers offered in the browser choice screen in the
> EU will have additional information about their browser shown to
> users who view the choice screen, and will get access to more data
> about the performance of the choice screen. The updated choice
> screen will be shown to all EU users who have Safari set as their
> default browser. For details about the changes coming to the
> browser choice screen, view [About the Browser Choice Screen in the EU](https://developer.apple.com/support/browser-choice-screen/).


Some of the choice details of the new changes:


> All users with Safari as their default browser, including users
> who have already seen the choice screen prior to the update,
> will see the choice screen upon first launch of Safari after
> installing the update available later this year.
> The choice screen will not be displayed if a user already has a
> browser other than Safari set as default.
> The choice screen will be shown once per device instead of once
> per user.
> When migrating to a new device, if (and only if) the user’s
> previously chosen default browser was Safari, the user will be
> required to reselect a default browser (i.e. unlike other
> settings in iOS, the user’s choice of default browser will not
> be migrated if that choice was Safari).


I get that the entire point of this mandatory choice screen is that because iOS is, in DMA parlance, a designated “gatekeeping” platform, the presumption is that Apple has unfairly advantaged Safari by bundling it with the OS and making it the default. So, from the European Commission’s perspective, some significant number of iOS users are using Safari *only* because it is bundled and default, and would prefer and/or be better served — or even just equally served — using another web browser as their default. Thus, Safari gets treated differently. It’s not just another browser in a list of 11. It’s the only browser whose users will be forced to choose again even if they’ve already chosen it in iOS 17.4 or later. It’s the only browser whose users will be forced to choose again whenever they migrate to a new iPhone or iPad. What exactly is the point of forcing this screen per-device rather than per-user, other than to repeatedly irritate Safari users who own multiple iOS devices?


At what point do these restrictions punish Safari users who *want* to use Safari? I’d say the EC has crossed that point by forcing these rules on Apple. Another detail:


> Users will be required to scroll through the full list of
> browser options before setting a browser as default.


You know how in certain “terms and conditions” agreement screens, you can only “agree” after scrolling all the way to the bottom of the legalese that almost no one actually reads? That’s how the browser choice screen must now work. Almost nothing in iOS works like this, and I suspect more than a few users who spot their preferred browser above the fold in the randomized list will find it very confusing that after selecting their browser, “nothing happens”. This is legally-mandated bad interaction design.


> If Safari is currently in the user’s Dock or on the first page of
> the Home Screen and the user selects a browser that is not
> currently installed on their device from the choice screen, the
> selected browser will replace the Safari icon in the user’s Dock
> or in the Home Screen.


For 17 years, the iOS Home Screen has been consistently [spatial](https://daringfireball.net/2003/04/siracusa_on_the_finder). Wherever an app is placed on your Home Screen, it stays there. Now, obviously, the EC’s objection is that Apple has unfairly privileged Safari with default placement in the user’s Dock, and they are seeking to remove this privilege for any user who chooses a browser other than Safari on the choice screen. But surely some number of users will regret their choice. Or simply seek to open Safari while trying some other browser as their new default. But now, unlike the way iOS has worked for 17 years, the Safari icon won’t be where they left it. It’s also worth noting that apps in the iOS Dock don’t show their names, only their icons. There surely exist many satisfied Safari users who don’t even know what “Safari” is — they only know the blue-compass icon. And they know that whenever they open URLs from an email or text message, those URLs open in an interface with which they’re completely familiar. The browser choice screen does, of course, show the browsers’ icons, but still. This is legally-mandated confusion.


The list of browsers presented to users remains mostly unchanged from Apple’s previous browser choice screen: the 11 most-downloaded browsers in each member state of the EU. So each of the 27 EU nations has its own list. Apple lists the current browsers, per country, at the bottom of [their support page](https://developer.apple.com/support/browser-choice-screen/).


Here is a single list of all included browsers, sorted by how many of the 27 EU nations they’re included in. For the 9 browsers included in all 27 countries, I’ve randomized the order:

- Chrome, Google LLC (27)
- Edge, Microsoft Corporation (27)
- Opera, Opera Software AS (27)
- Brave, Brave Software (27)
- Safari, Apple (27)
- DuckDuckGo, DuckDuckGo, Inc. (27)
- Aloha, Aloha Mobile (27)
- Onion Browser, Mike Tigas (27)
- Firefox, Mozilla (27)
- You, SuSea Inc. (23)
- Ecosia, Ecosia (17)
- Vivaldi, Vivaldi Technologies (13)
- Web@Work, MobileIron (10)
- Web, AirWatch LLC (5)
- Want, Qwant (3)
- Browser, Maple Media Apps LLC (3)
- Access, BlackBerry Corporation (3)
- Seznam.cz, Seznam.cz a.s. (2)
- Presearch, Presearch.org Global Limited (1)
- Avast Secure Browser, AVAST Software (1)


I was familiar with most of the 9 browsers included in all 27 countries, and you probably are too. But I’d never heard of [Aloha](https://alohabrowser.com/) or [Onion Browser](https://onionbrowser.com/) — and Onion Browser in particular stands out for coming from an individual developer, Mike Tigas. ([Onion Browser also stands out for being open source](https://github.com/onionbrowser/onionbrowser).) Both Aloha and Onion are advertised as “privacy focused”, which seems particularly true for Onion Browser, which is connected to [Tor](https://torproject.org/). Aloha includes built-in ad-blocking and a geo-fence skipping VPN.


So 9 of the 11 spots are occupied by the same popular browsers across the entire EU. Of the other 11 browsers, the only one I’d ever heard of was [Ecosia](https://www.ecosia.org/), which, like DuckDuckGo, is better known as a search engine (and, like DuckDuckGo, is on the very short list of search engines Safari offers in most countries around the world).1


Did you know that [BlackBerry made an iOS browser](https://www.blackberry.com/us/en/products/blackberry-dynamics/blackberry-access), and that it’s oddly popular in Ireland, Poland, and Sweden? I did not. (Did you know that BlackBerry still exists? I did not.)


The entire point of this mandatory browser choice screen is to reach Safari users and make it as easy as possible for them to switch default browsers. But how many such users are there, who *should* switch? How many users are there who understand what a web browser is, what a default web browser is, are currently using Safari by default, but who see this choice screen and think “*Oh this is great, I had no idea I could switch to one of these other browsers, I’ll do it...*”? I’m sure there exist some such users. But I’m also sure there exist *other* users who don’t quite know what a web browser is, don’t know that the browser they’re currently using — and perhaps have been using for over a decade — is named “Safari”, and won’t know how to undo a mistake they might make on this browser choice screen. Users who already know how to change their default iOS web browser don’t need this mandatory choice screen; users who *don’t* know how to change their default browser might be stuck with a mistaken or regretted choice. Pick Safari and you will see this browser choice screen again; pick anything else, perhaps as a lark, and you’ll never see it again.


My guess is that, perhaps counterintuitively, the single biggest beneficiary of this mandatory browser choice screen will be Google Chrome, which I consider the single most dominant software monopoly in the world today. Users who already know they want to use a non-Safari browser and have set one as their default won’t even see this screen. Users who want to use Safari and *know* they want to use Safari will merely be annoyed by this screen (repeatedly). But non-technical users who are confused by this screen — and I guaranteed there are millions of such users in the EU alone — will surely just pick a browser they’ve heard of and hope they’ve made the right choice. Chrome is by far the most-used web browser in the world, and for some number of users the only one they’ve ever heard of.


Shortly after iOS 17.4 shipped in March — the first version with DMA compliance features, and thus the first with a mandatory browser choice screen for Safari users in the EU — there were a few stories about third-party browsers seeing an uptick in users. [This one from TechCrunch](https://techcrunch.com/2024/04/10/eu-dma-browser-choice-screen-early-impact/?guccounter=1) is perhaps the best example. The gains were mostly reported in [Bezos numbers](https://x.com/jsnell/status/481863414180896769) — relative gains with no absolute numbers. Aloha Browser “said users in the EU jumped 250% in March”. Opera reported “39% growth in users on iOS selecting its browser as their default specifically, from March 3 until April 4” — but that was *down* from 164% growth the previous month, *before* iOS had implemented the mandatory choice screen in the EU. The one browser that reported actual numbers was Brave:


> “The daily installs for Brave on iOS in the EU went from around
> 7,500 to 11,000 with the new browser panel this past March,” per a
> company spokesperson. “In the past few days, we have seen a new
> all time high spike of 14,000 daily installs, nearly doubling our
> pre-choice screen numbers.”


Since April, I’ve seen bupkis about any continuing “success” of the browser choice screen for small browsers. I suppose that played a part in the EC forcing Apple into the further concessions — especially re-presenting the browser choice screen to all EU iOS users who selected Safari in iOS 17.4, 17.5, or 17.6 already. But I think the truth is obvious: the vast majority of iOS users use Safari because they want to, spanning the gamut from informed nerds who appreciate Safari’s features, UI, and privacy, to non-technical typical users who just know they like the experience with Apple’s first-party ecosystem of apps and services.


But whatever the effect of this browser choice screen on iOS browser usage in the EU, it’s hard for me to see any way that Chrome doesn’t benefit from it the most. That seems like a perverse outcome for a law intended to regulate “large gatekeepers”. Chrome, [with 65 percent market share across all web browsing globally](https://gs.statcounter.com/browser-market-share/), is a bigger monopoly than iOS, Android, or Windows, and the *only* other browser with double-digit market share (19 percent) is Safari — the browser the EC is attempting to steer users away from.


## ‘Default’ Apps


Back to [Apple’s announcement](https://developer.apple.com/news/?id=zglax7gc) on its Developer News site:


> For users in the EU, iOS 18 and iPadOS 18 will also include a new
> Default Apps section in Settings that lists defaults available to
> each user. In future software updates, users will get new default
> settings for dialing phone numbers, sending messages, translating
> text, navigation, managing passwords, keyboards, and call spam
> filters. To learn more, view [Update on apps distributed in the
> European Union](https://developer.apple.com/support/dma-and-apps-in-the-eu/#app-controls).
> Additionally, the App Store, Messages, Photos, Camera, and Safari
> apps will now be deletable for users in the EU.


Keep in mind that at least since iOS 14 (four years ago), we’ve been able to remove any apps we want from our Home screens. It’s just that certain essential system apps can’t be *deleted* — when removed from your Home screen, [they remain available in the App Library](https://support.apple.com/en-us/108324). The App Library was a great addition to iOS, and probably should have come years sooner. But what the EC is demanding from Apple now is the ability to delete these apps. This is particularly tricky with the App Store app, because it’s through the App Store that one can reinstall deleted default iOS apps. Presumably, the App Store app will be reinstallable via Settings, one of only two non-deletable apps.2


What those cheerleading these changes miss is that deleting these core system apps doesn’t magically make iOS a modular system. Apple hasn’t announced any sort of API for third-party apps in the EU to handle SMS (and now RCS) cellular text messaging, and I don’t expect them to. Such an API would be a privacy and security nightmare.3 My guess is that if you try to delete the Messages app, iOS will show you a special confirmation alert warning you of the consequences, and if you proceed, your iPhone will simply no longer be able to send or receive SMS or RCS messages. And, obviously, iMessages. What a great feature.


Likewise, Apple hasn’t announced any sort of API for modular photo storage. Users who delete the system Photos and Camera apps won’t — at this writing — be able to choose some other app to handle photo storage. Photos and videos shot will still go to the system photo library. Images that users have previously stored on their devices will still be in the system photo library. There just won’t be an app from Apple to *show* the system photo library. My understanding is that, under the hood, neither Photos nor Camera are really “apps” in the traditional sense. They’re just thin wrappers around low-level system frameworks. The same system-level frameworks allow third-party apps to access the system photo library. Apple, seemingly, hasn’t been forced to allow third-party software to replace these low-level system frameworks. They’re just being forced to allow users to “delete” these thin wrappers that present themselves as apps to users. But the actual way that the system photo library works remains unchanged. It’s like if the Mac let you delete the Finder — the file system would still be there, but the user would have no way to browse it.


An OS with a fundamentally modular design, with APIs that allow nearly every system component to be replaced by third-party software, sounds like a great idea. But no major OS is actually architected like that. iOS certainly is not. So requiring Apple to allow apps like Photos and Camera to be “deleted” is purely facile, and betrays the European Commission’s technical ignorance. The EC bureaucrats issuing these dictums clearly have no idea how iOS actually works. They just know what they can see. iOS ships with a bunch of apps. All they care about is that now users in the EU will be able to delete those apps.


Sure, many photographers prefer using third-party camera apps to Apple’s system Camera app. But iOS has long offered rich support for using third-party camera apps, and with iOS 18 that support is getting even better, with users soon being able to [configure the Lock Screen button](https://9to5mac.com/2024/06/10/ios-18-lets-you-replace-the-lock-screens-flashlight-and-camera-buttons/) that was previously dedicated only to launch the system Camera app. (Same goes for the button heretofore dedicated to the system Flashlight “app” — that’s configurable in iOS 18 too.) Camera apps added to the Lock Screen [even gain special privileges in iOS 18](https://9to5mac.com/2024/06/12/ios-18-lock-screen-camera-api/) — for all users, worldwide, not just in the EU. Even the developers of third-party camera apps [don’t see any point to being able to delete the system Camera app](https://www.threads.net/@sdw/post/C_QlXgnPyeG).


So who benefits from being able to outright “delete” the Photos and Camera apps? As far as I can tell, only people suffering from OCD who are bothered that after removing them from their Home Screen, that they’re still listed in the App Library. It’s unclear to me whether users in the EU will be able to delete apps like Photos and Camera even if they don’t have any third-party photography apps installed, which would leave their iPhone in a state where there is no way to take new photos or view existing ones. This is performative regulation. None of this deletable apps nonsense increases competition; it merely increases the chances of profound user confusion.


To be clear, just like with the browser choice screen, I don’t think these “default apps” and “deletable apps” compliance concessions from Apple are going to matter much. By design, deleting apps in iOS is a multi-step process and requires a long tap-and-hold even to get into [jiggle mode](https://9to5mac.com/2024/08/13/iphone-mirroring-jiggle-mode-ios-18-mac/). Even novice users don’t accidentally delete apps. But it’s also true that there’s no measurable demand from users to be able to delete essential system apps. So what’s the point of requiring Apple to support this? Just to watch the company dance?


I mean why stop here? Why not require Apple to ship new iPhones with only Settings and Phone pre-installed? Why not mandate that users be allowed to delete the entire OS?


## Apple Intelligence and iPhone Mirroring


When [Apple announced](https://daringfireball.net/linked/2024/06/21/apple-intelligence-dma-financial-times), a few weeks after WWDC in June, that the two biggest features of the year — Apple Intelligence and iPhone Mirroring — would likely remain unavailable in the EU this year “due to the regulatory uncertainties brought about by the Digital Markets Act”, DMA supporters suspected spite as the motivation. [I quoted Ian Betteridge then](https://daringfireball.net/2024/06/eu_reaping_what_it_sows) and will quote him again, because I think [his reaction epitomizes this viewpoint](https://mastodon.well.com/@ianb/112655916280591098):


> So, Apple, which bits of the DMA does Apple Intelligence violate?
> Because unless you can actually tell us — which case we clearly
> have a bit of a problem with some of the claims you’ve made about
> how it works — or you’re talking bullshit, and just trying to get
> some leverage with the EU. Which is it Tim?
> I absolutely guarantee that people are going to swallow this “well
> you can’t make Apple Intelligence work thanks to the DMA!!” line
> without actually asking any questions about what it violates,
> because “well Apple said it and they don’t lie evah”


My response to Betteridge in June [holds up](https://daringfireball.net/2024/06/eu_reaping_what_it_sows), and looks even more prescient with these latest concessions from Apple.


As the DMA applies to Apple in particular, where I think DMA supporters go wrong is that they’re not really DMA supporters, but rather App Store opponents. What they feel strongly about is opposing Apple’s tight control over all third-party software on iOS, including, if not especially, control over payments for apps, games, and digital content accessed through native apps. And so they endorse and support the DMA because the DMA breaks that control. Because of the DMA, third-party app marketplaces for iOS now exist in the EU, and apps in Apple’s own App Store are able to opt into [new terms](https://developer.apple.com/support/dma-and-apps-in-the-eu/#payment-options) to use their own payment processing (in the EU). Thus, from the perspective of opponents of Apple’s App Store, the DMA must be a net good overall, because they see the point of the DMA (as it pertains to Apple at least) as being about breaking up the App Store’s stranglehold over all iOS third-party native software.


But that’s not really the point of the DMA at all. It’s just one byproduct of it. And a very high profile byproduct, because supporting alternative app marketplaces and alternative payment processing were regulations that Apple needed to comply with starting in March of this year. If your personal beef with Apple is the App Store model, it’s easy to see how you could conclude that the DMA is about breaking up that model. And if you think the DMA is mostly about breaking up the App Store model, it’s easy to see how you think it’s nonsense that Apple Intelligence and iPhone Mirroring would raise any compliance issues, and so withholding those features from EU users (along with a third feature, enhancements to SharePlay Screen Sharing) must be spite on Apple’s part.


The thinking, I presume, is that Apple is being spiteful by withholding these features from users in the EU, in the hopes that EU iOS users will turn against the DMA and somehow demand from their EC representatives that it be repealed or amended. But that’s facile. Apple made its case against the DMA, best exemplified by [Craig Federighi’s keynote address at Web Summit](https://daringfireball.net/2021/11/federighi_sideloading_keynote_at_web_summit) in Lisbon, Portugal, back in 2021 — to no avail. [The DMA passed by an overwhelming margin](https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-digital-markets-act) in the European Parliament: 588 votes in favor, 11 votes against, and 31 abstentions. It’s the law of the continent.


It makes no sense for Apple to withhold tentpole iOS features from EU citizens out of spite. Even if you think Apple is guided by its own self-interest above all else, their biggest self-interest is selling new iPhones. And the biggest new feature in this year’s iPhone 16 models is going to be Apple Intelligence, and the best new feature in iOS 18 is iPhone Screen Sharing. These features will sell iPhones — but not in the EU, at least this year.


The key is that the DMA is not a targeted attack on the App Store model. It’s a sweepingly broad attack on the entire idea of integration. And integration is Apple’s entire modus operandi. The integration of hardware and software designed to work together. The integration between different devices — [Continuity](https://www.apple.com/macos/continuity/) — that are designed to work together.


Also: the integration between different apps on the same device. Safari isn’t just *a* web browser that just happens to be Apple’s. It’s *the* web browser designed by Apple to do things *the iOS way* on iOS (and *the Macintosh way* on MacOS). If, as a user, you do things the Apple way — owning multiple Apple devices, using iCloud for sync, using Safari as your web browser — you get an integrated experience, with access on device A to the tabs open on device B, shared browsing history and bookmarks between all devices, and support for systemwide services and features. The default apps from Apple on a factory fresh iPhone are designed to work together and present themselves consistently. That’s not to say no one should use third-party apps that are alternatives to Apple’s own. Of course not. Surely almost every reader of Daring Fireball uses one or more third-party apps that are alternatives to Apple’s. I use several. But the built-in Apple apps, taken together, constitute the Apple-defined experience. Those really are the apps most non-expert users should use. And the best third-party alternatives — like [Fantastical](https://flexibits.com/fantastical) (calendar), [Cardhop](https://flexibits.com/cardhop) (contacts), [Overcast](https://overcast.fm/) (podcasts), and [Bear](https://bear.app/) (notes) — fit seamlessly within that overall Apple experience. They’re third-party apps that feel integrated with the first-party experience.


From the EC’s perspective, everything ought to be modular and commoditized. That’s their ideal for “competition”. A dominant position in “phones” and “tablets” shouldn’t give the company that makes those devices a leg up in the market for web browsers, email clients, messaging, or camera apps. But from Apple’s perspective, the iPhone isn’t merely a “phone”, a piece of commoditized hardware. That’s why the company generally eschews articles, speaking and writing not of “the iPhone” but just “iPhone”. For Apple, iPhone is an integrated experience, encompassing hardware, software, and services, all designed and engineered by Apple itself.


Now that we have proof that the DMA demands that Apple allow all apps other than Settings (and on iPhones, Phone) to be deleted, and to allow third-party defaults to be set for everything from contactless payments to password management to maps to translation and even keyboards (keyboards?), it’s obvious that the EC might also demand that users be able to specify a third-party “default” AI language model for Apple Intelligence. Not just the optional “world knowledge” layer that Apple is currently partnering exclusively with OpenAI to provide, but the base layer of Apple Intelligence with semantic personal knowledge. Apple Intelligence isn’t designed that way. It’s not a module or an “app”. It’s a deeply integrated layer of the system software. Faced with a decision from the EC that Apple either make all of Apple Intelligence open to third-party AI (including AI systems unvetted by Apple itself), or never offer Apple Intelligence in the EU, I think Apple would choose never to offer it in the EU.


As for iPhone Screen Sharing, gatekeeping platforms aren’t permitted under the DMA to preference other products or services from the gatekeeper itself. iPhone Screen Sharing only works between iPhones and Macs — computers made by Apple. That’s against the DMA — or, at least, the EC could clearly rule that it’s against the DMA.


If the DMA had been in effect 10 years ago, I don’t think Apple Watch would have been available in the EU until and unless the EC said it was permitted. Same for AirPods, which pair with Apple devices in a vastly superior but proprietary way compared to standard Bluetooth. Any sort of integration between an iPhone and another Apple device that isn’t available to third-party devices could be ruled to violate the DMA. By the letter of the DMA, the EC *should*, I think, rule that all such integration is a violation.


This uncertainty will likely clear over time. Perhaps the EC will rule that Apple Intelligence and/or iPhone Screen Sharing pose no violation to the DMA, and Apple can make those features available, as they exist today, in the EU. Like, maybe the EC commissioners themselves really just want to break up the App Store model and that’s it. But European Commission vice president Margrethe Vestager clearly believes that Apple Intelligence is anti-competitive and thus a violation of the DMA. [Speaking at Forum Europa in July](https://youtu.be/GmQ5SsMFbsU?t=4636), she said:


> I find that very interesting that they say we will now deploy AI
> where we’re not obliged to enable competition. I think that is
> the most sort of stunning open declaration that they know
> 100% that this is another way of disabling competition where they
> have a stronghold already.


She’s very clear that she believes Apple is “obliged to enable competition” with AI under the DMA. Apple Intelligence enables no competition at all. Something has to give here.


The EC’s apparent expectation is that because the European Union is so large and so essential to the world, Apple — along with the DMA’s other targeted “gatekeepers” — will bend to its will and henceforth design its products and services with the DMA in mind. Modularity over integration, at all layers of the stack. Thierry Breton, the EU internal market commissioner, [quipped in July](https://www.ft.com/content/898338c2-b9fd-4494-be3f-75b7c669c705): “Apple’s new slogan should be ‘act different’.”


[But the EU isn’t *that* large or essential](https://daringfireball.net/2024/03/eu_share_of_apples_revenue). The European Commission is beset by delusions of grandeur. What’s happening with Apple Intelligence and iPhone Screen Sharing this year is what I expect to happen with every new product or service Apple creates that integrates with iOS: they will come late, or never, to the EU. And all new products and services Apple creates integrate with iOS, so almost everything new from Apple will come late, or never, to the EU.


While not the *intention*, that’s the actual *effect* of the DMA.


---

1. The fact that DuckDuckGo and Ecosia are both the names of search engines supported within Safari *and* web browsers that are standalone alternatives to Safari is surely going to be a point of confusion for non-technical users. I’m not saying DuckDuckGo or Ecosia should not make their own browsers, or should have named them differently, but imagine the confusion if, instead of naming their browser “Chrome”, Google had named it “Google”. ↩︎
2. The other remaining un-deletable app is Phone, which I believe cannot be deleted to maintain compliance with laws that require all cellular phones, whether they have active SIM cards or not, to be able to place emergency service calls (e.g. 911 here in the U.S.). ↩︎︎
3. Note too that while Android has always offered APIs to allow third-party apps to handle SMS cellular messaging, popular messaging apps that support secure E2EE eschew it. Signal supported SMS on Android for over 10 years, but [announced in 2022 that it was removing SMS support](https://signal.org/blog/sms-removal-android/), for the good reason that they wanted to avoid any possible confusion about what was encrypted (all messages using the Signal protocol) and what wasn’t (all messages sent via SMS) within the Signal app. WhatsApp — the most popular messaging platform in most of the EU — has never supported SMS on Android. The remaining third-party SMS apps on Android seem like [a mess of shoddy adware and scamware](https://play.google.com/store/apps/details?id=sms.imessages.messaging.chat). ↩︎︎



| **Previous:** | [The Mac Is a Power Tool](https://daringfireball.net/2024/08/the_mac_is_a_power_tool) |
| **Next:** | [The iOS Continental Drift Fun Gap](https://daringfireball.net/2024/09/ios_continental_drift_fun_gap) |


PreviousNext