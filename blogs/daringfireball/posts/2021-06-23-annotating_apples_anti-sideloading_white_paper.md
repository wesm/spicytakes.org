---
title: "Annotating Apple’s Anti-Sideloading White Paper"
date: 2021-06-23
url: https://daringfireball.net/2021/06/annotating_apples_anti-sideloading_white_paper
slug: annotating_apples_anti-sideloading_white_paper
word_count: 2369
---


Apple today released a white paper arguing against proposed legislation that would mandate the ability to sideload apps (and thereby alternative app stores) on iOS/iPadOS:1 “[Building a Trusted Ecosystem for Millions of Apps](https://www.apple.com/privacy/docs/Building_a_Trusted_Ecosystem_for_Millions_of_Apps.pdf)”.2 I think it’s good, fair, and cogent. I highly encourage you to read it — it’s not long — then come back for my annotations below.


The paper opens with this quote from Steve Jobs, [announcing the iPhone SDK](https://tidbits.com/2007/10/17/steve-jobss-iphone-sdk-letter/):3


> “We’re trying to do two diametrically opposed things at once:
> provide an advanced and open platform to developers while at the
> same time protect iPhone users from viruses, malware, privacy
> attacks, etc. This is no easy task.” — Steve Jobs, 2007


As ever, Steve Jobs was a succinct and forceful communicator. That “diametrically opposed” tension he described at the outset, 14 years ago, remains exactly the core of Apple’s argument in this paper today.


Page 4, under a section subtitled “This approach to security and privacy has been highly effective”:


> Additionally, even users who prefer to only download apps from the
> App Store could be forced to download an app they need for work or
> for school from third-party stores if it is not made available on
> the App Store. Or they could be tricked into downloading apps from
> third-party app stores masquerading as the App Store.


This, to me, is perhaps *the* key point that sideloading proponents ignore. Arguments in favor of allowing sideloading on iOS, from users, tend to boil down to “*It’s my device, I should be allowed to install whatever I want. If most users want to stick with the App Store, that’s fine for them and they’ll keep all the benefits as they currently stand, while I and others will have the freedom to install whatever we want.*” That argument is not wrong! There *would* be benefits to allowing sideloading, exactly along the lines of how there are benefits to being able to install apps outside the App Store via TestFlight, enterprise distribution, and compiling apps from source code with Xcode.


Sideloading would take things to a new level though. TestFlight still requires some approval from Apple, and TestFlight distribution is limited to 10,000 users. Enterprise distribution requires an enterprise certificate from Apple. And compiling from source code requires a developer account, significant technical expertise, and, well, the source code to the app.


What the sideloading arguments ignore are the enormous tradeoffs involved. Yes, there would be benefits — a lot of cool apps that aren’t permitted in the App Store would be installable by as many iOS users as want to install them. But many non-technical users would inevitably wind up installing undesirable apps via work/school requirements or trickery that they could not be required or tricked into installing today. Consider just the example of “proctoring apps” that students are required to install for remote test taking. They’re a surveillance menace, [as the EFF reported in August](https://www.eff.org/deeplinks/2020/08/proctoring-apps-subject-students-unnecessary-surveillance).


Technically, yes, on platforms that allow it, sideloading is the user’s choice. But socially and psychologically, it often isn’t.4


Page 4:


> In the end, users would have to constantly be on the lookout for
> scams, never knowing who or what to trust, and as a result many
> users would download fewer apps from fewer developers.


This is another key point that cannot be overstated. As things stand today, you cannot “mess up” your iOS device by installing the wrong software. You can easily uninstall all traces of any app you do install with a tap-and-hold on the app’s icon. No app you install can [entrench invisible background agents that act like system software](https://chromeisbad.com/). And because of this, hundreds of millions of non-technical iOS users install far more software on their iOS devices than they do or did on their PCs — *including Macs*. This, despite the fact that PCs are far more powerful devices. Typical users install more apps on their less capable phones than they do on their far more capable PCs. This is as close as we can get to proof that Apple’s App Store model on iOS hasn’t just worked, but has proven to be wildly successful *and popular with users*.


Related point: An app’s ability to even *request* access to health data, or contacts, or to create a VPN, rests on App Store review. If an app says it’s a game but requests the entitlement to prompt the user for access to health data, Apple’s App Store review will reject it. An Epic-run App Store would be making parallel and different decisions about which entitlements to grant to which apps. A sideloaded app would make those decisions for itself. Surveillance tracking would go back to “whatever the app wants to do”.


Page 9:


> iPhone is used every day by over a billion people — for banking,
> to manage health data, and to take pictures of their families.
> This large user base would make an appealing and lucrative target
> for cybercriminals and scammers, and allowing sideloading would
> spur a flood of new investment into attacks on iPhone, well beyond
> the scale of attacks on other platforms like Mac.


Here Apple dances around the elephant in the room — the question of why iOS shouldn’t just work like the Mac with regard to non-App Store software. Apple’s deft argument is that there are far fewer Macs than iOS devices, making the Mac a less enticing target for scammers and crooks (including privacy crooks). That’s more or less the argument Windows proponents used to explain the profound prevalence of malware on Windows compared to the Mac back in the day, whilst Apple (and Mac proponents) argued otherwise, that the Mac actually was far more secure at a technical level.


But the truth Apple won’t come out and say is that it’s *both*. The Mac *was* more secure by design, but *also* a far less enticing target because of how many more users were (and still are) on Windows. And, today, iOS *is* more secure and private than the Mac. That’s the nature of the Mac as a full PC platform.


I’ll admit it: if Mac-style sideloading were added to iOS, I’d enable it, for the same reason I enable installing apps from outside the App Store on my Mac: I trust myself to only install trustworthy software. But it doesn’t make me a hypocrite to say that I think it would be worse for the platform as a whole.5


The Mac is fundamentally designed for users who are at least *somewhat* technically savvy, but tries its best to keep non-savvy users from doing things they shouldn’t. But you can always hurt yourself, sometimes badly, with any true power tool. The iPhone is the converse: designed first and foremost for the non-savvy user, and tries to accommodate power users as best it can within the limits of that primary directive.


Page 11:


> *The goal of App Review is to ensure that apps on the App Store
> are trustworthy* and that the information provided on an app’s App
> Store page accurately represents how the app works and what data
> it will access. We are constantly improving this process: we
> update and refine our tools and our methodology continuously.


The problem Apple is facing today is that it’s clear that one word in the above is inaccurate: the opening “the”. The above is *a* goal of the App Store — and I would argue that it remains the *primary* goal. But clearly the App Store serves another goal for Apple: making the company money. Exhibit A: [last year’s Hey fiasco](https://daringfireball.net/2020/06/hey_app_store_rejection_flimsiness). Nothing about Apple’s rejection of Hey (or, I’d wager, some number of *thousands* of other apps flagged by App Store review for similar reasons) was about trustworthiness. It was about money.


That’s a conflict of interest, and it detracts significantly from Apple’s entirely legitimate trustworthiness argument defending the App Store model for distribution. I remain convinced Apple wouldn’t be facing these regulatory pressures today [if they’d walked away from a strategy of maximizing App Store profits years ago](https://daringfireball.net/2021/06/app_store_the_schiller_cut), and I also think they could largely dissipate these pressures today by doing it now — better late than never.


Also on page 11:


> *Once users download an app through the App Store, they are able to
> control how that app functions and what data it is able to access*,
> using features such as App Tracking Transparency and permissions.
> Parents can further control what their kids buy with the Ask to
> Buy feature, how much time they spend on certain categories of
> apps with Screen Time features, and what data they share. Users
> are also able to centrally manage all app-related payments, and
> are able to easily view and cancel subscriptions that are paid for
> via In-App Payments. These controls could not be fully enforced on
> sideloaded apps.


All of this is true. But that last point, that *all* in-app subscriptions are listed in an obvious location, where it’s easy to unsubscribe, and you get email notifications before every renewal, is the singular reason why I think Apple should not — and should not be forced to — allow in-app purchases and especially subscriptions via developers’ own payment systems. What I endorse is allowing apps to direct users to the web to make purchases and subscriptions. In-app purchases vs. out-app purchases. Let Apple earn its cut by showing that in-app purchases have higher conversions.


My favorite example is The New York Times — by all accounts a reputable and trustworthy company. Subscribe to the Times in-app, where Apple gets a cut, and you can easily unsubscribe at any time with two taps in the Settings apps. Subscribe to the Times on their website, and you literally have to [call them on the telephone and argue with a Times rep](https://help.nytimes.com/hc/en-us/articles/360003499613-Cancel-your-subscription) whose job is to talk you out of unsubscribing.


The current in-app purchase requirements are incredibly reassuring to me, as a user. I subscribe to many publications and services through in-app purchase that I would not subscribe to otherwise. Let apps *offer* the ability to use their own purchasing systems, but make it clear they’re doing so on the web, not in-app. (That’s what Hey does — and people trust Hey because they trust the company behind it.)


Page 12, in a list of statistics of App Store “protections in action in 2020”:


> *Apple deactivated 244 million customer accounts due to fraudulent
> and abusive activity, including fake reviews*. It also rejected
> 424 million attempted account creations due to fraudulent and
> abusive patterns.


My reaction to these numbers: *Jiminy!*


Assuming these number are accurate, they explain Apple’s seeming nonchalance to the continuing existence of scam apps that do get into the App Store, and the pervasiveness of fraudulent reviews. They’re catching the overwhelming majority of them.


I still say: [not good enough](https://daringfireball.net/search/bunco+squad), especially on the task of identifying and eliminating *successful* scams. But, still, wow, those are big numbers.


---

1. Apple actually only talks about the iPhone in the white paper — the word “iPad” doesn’t appear once. But iPadOS and iOS are exactly the same in every regard discussed in the paper. I think Apple wisely focused on iPhone to keep it simple. I’ll do the same, and write only “iOS” as shorthand for “iOS and iPadOS” (and WatchOS and tvOS, for that matter). ↩︎
2. It’s a PDF, not a web page, which is typical for “white paper” type things. But the biggest downside to publishing it as a PDF is that it’s hard to read on a phone, which feels at least slightly ironic. (Kudos to Apple though for the PDF’s svelte 295 KB file size, despite being illustrated throughout.) ↩︎︎
3. Amusingly, Apple had to source Jobs’s quote to [TidBITS’s archived copy](https://tidbits.com/2007/10/17/steve-jobss-iphone-sdk-letter/) of Jobs’s open letter announcing the SDK, because Apple never gave it a permalink at apple.com. In his preface to TidBITS’s hosted copy of the letter, Adam Engst wrote:

Some things need to be in the permanent record, and since Apple
didn’t see fit to give a permanent URL to Steve Jobs’s letter
announcing that Apple would be creating an SDK for third party
iPhone native applications, I’m reproducing it below for future
reference.

Even Apple apparently now agrees the letter belongs in the permanent record. ↩︎︎
4. As an aside, this is why it would be a terrible idea to enrich WebKit into a full technical peer to native apps, or allow alternative web rendering engines empowered with such features, [as many web developers shortsightedly, and recklessly (and perhaps selfishly) desire](https://infrequently.org/2021/04/progress-delayed/). As things stand, WebKit allows users to go anywhere they want on the web, and install any web apps they want as apps on their iOS home screens — but WebKit’s limits are such that they can do so *without concern or any degree of technical savviness* because WebKit only offers functionality that is safe, secure, and private. Not to mention the fact that a world where any mobile app could be written as a pure web app would inevitably quickly devolve into a world where most apps are identical on iOS and Android, which is neither good for Apple *nor* for iOS users who prefer truly native iOS apps that fit in with Apple’s system-wide design idioms and integrate with iOS’s unique features. ↩︎︎
5. My spitball idea for sideloading would be for Apple to create a “developer mode” on iOS devices that allows for Mac-style sideloading of apps. Something that requires a *paid* Apple developer account. No one is going to get tricked or bamboozled into signing up for a $100/year ADC account. And when (not if) some users who enable it wind up installing foolish software, “developer mode” is a pretty good way of saying “you should know better”. And disabling “developer mode” would, if possible, render inert any software on the device installed via this means. Just my spitball. ↩︎︎



| **Previous:** | [The New York Times: ‘Sundar Pichai Faces Internal Criticism at Google’](https://daringfireball.net/2021/06/pichai_wakabayashi) |
| **Next:** | [Regarding the Safari 15 Public Betas for Mac and iOS](https://daringfireball.net/2021/07/safari_15_public_betas_for_mac_and_ios) |


PreviousNext