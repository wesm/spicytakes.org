---
title: "Apple’s Plans for the DMA in the European Union"
date: 2024-01-26
url: https://daringfireball.net/2024/01/apples_plans_for_the_dma
slug: apples_plans_for_the_dma
word_count: 5597
---


Apple yesterday announced a broad, wide-ranging, and complex set of new policies establishing their intended compliance with the European Union’s Digital Markets Act, which comes into effect March 7. There is a lot to remark upon and numerous remaining questions, but my favorite take was from Sebastiaan de With on Twitter/X, *the day before* any of this was announced.


After [quipping](https://twitter.com/sdw/status/1750288120904655154) “Oh god please no” to a screenshot of the phrase “Spotify also wants to roll out alternate app stores”, [de With had this conversation](https://twitter.com/sdw/status/1750291816602300812):


de With:


> The EU is once again solving absolutely no problems and making 
> everything worse in tech. I gotta say, they are if anything highly 
> consistent.


“Anton”:


> Overly powerful, rent-seeking gatekeepers seem like a problem.


de With:


> I love that I can’t tell if you are talking about the EU or Apple in this case.


My second-favorite take, from that same thread, [was this from Max Rovensky](https://twitter.com/maxrovensky/status/1750600510346817950):


> DMA is not pro-consumer. 
> It’s anti-big-business. 
> Those tend to coincide sometimes, which makes it an easy sell for 
> the general public, but do actually read the DMA, it’s quite 
> interesting.


I’d go slightly further and describe the DMA as anti-*U.S.*-big-business, because as far as I can tell, nothing in the DMA adversely affects or even annoys any European tech companies. There are aspects of it that seem written specifically *for* Spotify, in fact.


But Rovensky’s framing captures the dichotomy. Anti-big-business regulation and pro-consumer results often do go hand-in-hand, but the DMA exposes the fissures. I do not think the DMA is going to change much, if anything at all, for the better for iOS users in the E.U. (Or for non-iOS users in the EU, for that matter.) And much like the [GDPR’s website cookie regulations](https://gdpr.eu/cookies/), I think if it has any practical effect, it’ll be to make things *worse* for users. Whether these options are better for developers seems less clear.


I’ve [often said](https://daringfireball.net/2021/06/app_store_the_schiller_cut) that Apple’s priorities are consistent: Apple’s own needs first, users second, developers third. The European Commission’s priorities put developers first, users second, and “gatekeepers” a distant third. The DMA prescribes not a win-win-win framework, but a win-win-lose one.


Apple is proud, stubborn, arrogant, controlling, and convinced it has the best interests of its customers in mind.


The European Commission is proud, stubborn, arrogant, controlling, and convinced it has the best interests of its citizens in mind.


Ever since this collision over the DMA seemed inevitable, starting about two years ago, I’ve been trying to imagine how it would turn out. And each time, I start by asking: Which side is smarter? My money has been on Apple. Yesterday’s announcements, I think, show why.


## Apple’s Proposed Changes


It’s really hard to summarize everything Apple announced yesterday, but I’ll try. Start with the main Apple Newsroom press release, “[Apple Announces Changes to iOS, Safari, and the App Store in the European Union](https://www.apple.com/newsroom/2024/01/apple-announces-changes-to-ios-safari-and-the-app-store-in-the-european-union/)”:


> “The changes we’re announcing today comply with the Digital 
> Markets Act’s requirements in the European Union, while helping to 
> protect EU users from the unavoidable increased privacy and 
> security threats this regulation brings. Our priority remains 
> creating the best, most secure possible experience for our users 
> in the EU and around the world,” said Phil Schiller, Apple Fellow. 
> “Developers can now learn about the new tools and terms available 
> for alternative app distribution and alternative payment 
> processing, new capabilities for alternative browser engines and 
> contactless payments, and more. Importantly, developers can choose 
> to remain on the same business terms in place today if they 
> prefer.”


Schiller is the only Apple executive quoted in the press release, and to my ear, his writing hand is all over the entire announcement. Apple was quite clear before the DMA was put into law [that they considered mandatory sideloading on iOS a bad idea for users](https://daringfireball.net/2021/11/federighi_sideloading_keynote_at_web_summit), and their announcement yesterday doesn’t back down an inch from still declaring it a bad idea.


Apple has also argued, consistently, that they seek to monetize third-party development for the iOS platform, and that being forced to change from their current system — (a) all apps must come from the App Store; (b) developers never pay anything for the distribution of free apps; (c) paid apps and in-app-purchases for digital content consumed in-app must go through Apple’s In-App Payments system that automates Apple’s 30/15 percent commissions — would greatly complicate how they monetize the platform. And now Apple has revealed a greatly complicated set of rules and policies for iPhone apps in the EU.


MG Siegler has a great — and fun — post [dissecting Apple’s press release line-by-line](https://spyglass.org/apple-to-eu-drop-dead/). Siegler concludes:


> I’m honestly not sure I can recall a press release dripping with 
> such disdain. Apple may even have a point in many of the points 
> above, but the framing of it would just seem to ensure that Apple 
> is going to continue to be at war with the EU over all of this and 
> now undoubtedly more. Typically, if you’re going to make some changes 
> and consider the matter closed, you don’t do so while emphatically 
> shoving your middle fingers in the air. 
> Some of these changes do seem good and useful, but most simply 
> [seem like](https://www.threads.net/@mgsiegler/post/C2iRgI8LH-H?ref=spyglass.org) convoluted changes to ensure the status quo actually 
> doesn’t change much, if at all. Just remember that, “importantly, 
> developers can choose to remain on the same business terms in 
> place today if they prefer.” What do you think Apple prefers?


The puzzle Apple attempted to solve was creating a framework of new policies — and over 600 new developer APIs to enable those policies — to comply with the DMA, while keeping the path of least resistance and risk for developers the status quo: Apple’s own App Store as it is.


So the first option for developers is to do nothing — to stay in Apple’s App Store, exclusively, under the existing terms. (Apple made a few announcements yesterday that are effective worldwide, not merely in the EU, [such as changes regarding the rules for streaming game services, mini-games, and mini-apps](https://developer.apple.com/news/?id=f1v8pyay). For the sake of brevity — well, *attempted* brevity — I’m focusing on E.U.-specific changes related to DMA compliance.)


One point of confusion is that some aspects of Apple’s proposed DMA compliance apply to the App Store across all platforms (iPhone, iPad, Mac, TV, Watch, and soon, Vision), but other aspects are specific to the iOS platform — which is to say, only the iPhone. Third-party [app marketplaces](https://developer.apple.com/support/alternative-app-marketplace-in-the-eu/)1 and [web browsers using non-WebKit rendering engines](https://developer.apple.com/support/alternative-browser-engines/) are only available on iOS specifically, meaning they are iPhone-only,2 and not available for iPadOS. Apple’s [main press release yesterday](https://www.apple.com/newsroom/2024/01/apple-announces-changes-to-ios-safari-and-the-app-store-in-the-european-union/) breaks out iOS changes and App Store changes separately, but on my first read did not make clear that the iOS changes did not apply to iPadOS.3


Here’s my summary of the options available to developers in the EU, under Apple’s proposal:

1. Stay in App Store under the current (pre-DMA) rules, exclusively. Developers that take this option:
  - Are not permitted to use any of the new *business terms* available in the EU, but new *iOS* platform options for the EU, such as alternate browser engines, are allowed. (Because they are required to be allowed.)
  - Because nothing business-related changes under this option, the existing worldwide rules apply for paid apps, subscriptions, and in-app purchases (IAP), including the 30/15 percent commission to Apple and a requirement that apps exclusively use Apple’s App Store payments system.
  - The Core Technology Fee (CTF) is *not* collected, because the business terms haven’t changed. (See below re: the CTF.)
2. Opt in to the new EU rules (all sub-options available under this choice require paying the Core Technology Fee for each app with over 1 million downloads in the EU):
  - After opting in to the new EU rules, developers can choose to
remain in the App Store, and:
    - Use Apple’s App Store payments system: 20/13 percent commission + CTF paid to Apple automatically.
    - Use a custom in-app payments system (e.g. Stripe): 17/10 percent commission + CTF paid to Apple.
    - Use external links from inside apps to the web for payments and subscriptions: 17/10 percent + CTF paid to Apple.
    - *The latter two options — using custom payment processing and/or external links to the web — are similar to the [announced-last-week External Payment Link entitlement policy](https://daringfireball.net/2024/01/coming_to_grips_with_apples_seemingly_unshakable_sense_of_app_store_entitlement), regarding the developer’s obligation to track these payments, report sales to Apple monthly, and submit to audits by Apple to ensure compliance.*
  - Distribute apps in one or more third-party marketplaces:
    - No option to use Apple’s App Store payment processing, because the apps aren’t coming from the App Store.
    - The only money due to Apple is the Core Technology Fee — there is no commission percentage on in-app transactions or links to the web.


Under option (2) — the catch-all for opting in to the new rules available in the EU — the sub-options are not mutually exclusive. Developers that opt in to the new EU rules can have (or keep) apps in the App Store *and* distribute those same apps, or different apps, via third-party app marketplaces. Or they can stay in the App Store exclusively (under the new business terms, with lower commissions but also the CTF), or they can distribute exclusively via app marketplaces.


Only options (1) and (2) are exclusive. However, once a developer opts in to the new EU rules, that decision is irrevocable. Quoting from the Q&A section of [Apple’s “Update on Apps Distributed in the European Union” document](https://developer.apple.com/support/dma-and-apps-in-the-eu/#faq):


> Developers who adopt the new business terms at any time will not 
> be able to switch back to Apple’s existing business terms for 
> their EU apps. Apple will continue to give developers advance 
> notice of changes to our terms, so they can make informed choices 
> about their businesses moving forward.


(That entire FAQ section is a good summary and worth reading.)


## The Core Technology Fee


[Apple’s description of the CTF](https://developer.apple.com/support/dma-and-apps-in-the-eu/#faq):


> The Core Technology Fee (CTF) reflects Apple’s investment in the 
> tools, technology, and services that enable developers to build 
> and share their apps with Apple users. That includes more than 
> 250,000 APIs, TestFlight, Xcode, and so much more. These tools 
> create a lot of value for developers, whether or not they share 
> their apps on the App Store. 
> The CTF only applies to developers who adopt the new terms for 
> alternative distribution and payment processing — and whose apps 
> reach exceptional scale. With membership in the Apple Developer 
> Program, eligible developers on the new business terms get a free 
> one million first annual installs per year for each of their apps 
> in the EU. See [terms](https://developer.apple.com/contact/request/download/alternate_eu_terms_addendum.pdf) for more details. Under the new business 
> terms for EU apps, Apple estimates that less than 1% of developers 
> would pay a Core Technology Fee.


Apple’s description is clear on the following point, but it’s worth reiterating: the CTF only applies to downloads above 1 million, like a marginal tax rate. So a developer whose app goes from 1,000,000 EU user downloads to 1,000,001 will only owe Apple €0.50 in Core Technology Fees. The CTF is recurring each year however, and updates count as downloads. Installing the same app on multiple devices does not count as multiple installations though.4 The CTF is calculated per user, per app, per year. (Apple has a [CTF calculator](https://developer.apple.com/support/fee-calculator-for-apps-in-the-eu/) developers can use to game scenarios of prices, distribution method, and download counts.)


In plain language, the DMA demands that Apple unbundle its monetization for the App Store from its monetization of the iOS platform. Apple’s existing, purely commission-based, monetization for iOS apps implicitly bundles together the value provided from the App Store and iOS.


So under option (1) — where developers choose the existing rules for App Store distribution, including App Store exclusivity — nothing changes and Apple collects its 30/15 percent commissions from App Store transactions.


But under option (2) — where developers opt in to the new EU rules — Apple’s monetization for the App Store is severed from its monetization for the iOS platform itself. That’s why the commission fees under the new EU rules are reduced to 20/13 percent for apps distributed through the App Store that use the App Store payment system, and 17/10 percent for apps distributed through the App Store that use custom payment processing. Effectively, Apple is saying that their fair share of App Store distribution is 17/10 percent, and that Apple’s own App Store payment processing is worth an additional 3 percent. (3 percent is almost indisputably a fair estimate for the cost of payment processing alone.)


And, that’s why apps distributed outside the App Store will *only* pay Apple the CTF, with no commission on sales. The commissions under the new EU rules are only for the App Store, so apps from marketplaces don’t pay them. The Core Technology Fee is how Apple proposes monetizing the value provided by iOS itself.


All developers who opt in to the new EU rules are subject to the CTF. No developers who remain in the App Store under existing policies are subject to the CTF.


## Marketplace Apps Are the Only Distribution Outside the App Store


Third-party marketplace apps are the only way for developers to distribute apps in the EU outside the App Store. Apple’s proposal has no option for direct downloads of apps from developer websites. Apple has rules for who can become an app marketplace. You have to be a company, not an individual. You must “provide Apple a stand-by letter of credit from an A-rated (or equivalent by S&P, Fitch, or Moody’s) financial Institution of €1,000,000 to establish adequate financial means in order to guarantee support for your developers and users.” [And more](https://developer.apple.com/support/alternative-app-marketplace-in-the-eu/). In short, the qualifications aren’t trivial, but nor are they overly complicated.


But marketplace apps must be real “stores”. A marketplace can decide to exclusively distribute apps from a certain category — like games — but must be open to submissions from any developer in that same category. Company XYZ can’t create a marketplace that only distributes XYZ’s own apps. That’s not a proper category. Nor would Apple consider to be a proper category something like, say, “Apps from companies founded by Harvard dropouts whose origins were depicted in fun movies by Aaron Sorkin.”


One key restriction for developers who wish to distribute through multiple stores (including Apple’s App Store): an installation from one store cannot overwrite an existing installation of the same app from another store. The user must manually delete the installation from the old store first, then re-install the app from the other store. Apple claims — reasonably, perhaps — that this restriction is because they don’t know whether a fresh installation from a different store will preserve the data from the app installed via the previous store.


But this also means that if, say, Meta starts distributing their apps through a third-party marketplace (perhaps their own Meta Store), and wishes to encourage iOS users to switch from App Store installations to installations from the Meta Store, each user who does so must delete their existing installations of Meta’s apps before installing the new ones.


Third-party marketplace apps — the actual app store apps — will not be permitted in Apple’s App Store. To install a marketplace app — and third-party app marketplaces [will be apps themselves](https://developer.apple.com/documentation/appdistribution/creating-an-alternative-app-marketplace/) — users must go to the marketplace app’s website. Safari (and other web browsers that adopt new APIs) will offer to install marketplace apps after confirmation from the user that they really want to install it. That [confirmation scaresheet](https://developer.apple.com/documentation/appdistribution/creating-an-alternative-app-marketplace/) and the subsequent installation is provided by the system.


Part of what makes the DMA a terrible law (in this writer’s estimation) is its ambiguity and inscrutable language. It’s completely unclear whether Apple’s proposal to only allow distribution of apps outside the App Store through marketplace apps is compliant. Many proponents of the DMA have been under the conviction that the DMA mandates gatekeeper platforms like iOS to permit direct downloads of apps from the web (like on PCs and Macs). Here’s Article 6, Section 4 of the DMA, boldface all-caps emphasis added:


> 4. The gatekeeper shall allow and technically enable the 
> installation and effective use of third-party software 
> applications **OR** software application stores using, or 
> interoperating with, its operating system and allow those software 
> applications **OR** software application stores to be accessed by 
> means other than the relevant core platform services of that 
> gatekeeper. The gatekeeper shall, where applicable, not prevent 
> the downloaded third-party software applications **OR** software 
> application stores from prompting end users to decide whether they 
> want to set that downloaded software application **OR** software 
> application store as their default. The gatekeeper shall 
> technically enable end users who decide to set that downloaded 
> software application **OR** software application store as their 
> default to carry out that change easily.


By Apple’s interpretation, all of those *or*’s would be *and/or*’s or *and*’s if the DMA demanded that iOS support both third-party marketplaces *and* direct installation of individual apps and games. See below regarding the uncertainty of this interpretation.


## Apple Will Still Review All Apps, But With Very Different Rules


All apps for iOS require an Apple Developer Program account.5 All apps and every update must still be submitted to Apple for notarization. After review, Apple will then forward apps to each marketplace where the app is distributed. The review policies for apps distributed via marketplace apps are entirely different from the App Store. [From Apple’s FAQ](https://developer.apple.com/support/dma-and-apps-in-the-eu/#faq), again:


> Developers can submit a single binary and will be able to choose 
> alternative distribution options in App Store Connect. 
> Notarization for iOS apps will check for: 
> Accuracy — Apps must accurately represent the developer, 
> capabilities, and costs to users. 
> Functionality — Binaries must be reviewable, free of serious 
> bugs or crashes, and compatible with the current version of iOS. 
> They cannot manipulate software or hardware in ways that 
> negatively impact the user experience. 
> Safety — Apps cannot promote physical harm of the user or 
> public. 
> Security — Apps cannot enable distribution of malware or of 
> suspicious or unwanted software. They cannot download executable 
> code, read outside of the container, or direct users to lower 
> the security on their system or device. Also, apps must provide 
> transparency and allow user consent to enable any party to 
> access the system or device, or reconfigure the system or other 
> software. 
> Privacy — Apps cannot collect or transmit private, sensitive 
> data without a user’s knowledge or in a manner contrary to the 
> stated purpose of the software.


Apple representatives I’ve been in briefings with — multiple times over the last two days — emphasized that *content* restrictions that apply to apps distributed in the App Store will not apply to those distributed exclusively in EU marketplaces. Adult content and pornography were cited as examples: porn apps will never be permitted in the App Store, but will not be rejected by Apple for distribution in marketplaces. That will be up to each individual marketplace.


Apple’s review process will continue to involve both automated checks and human review. Private API usage will *not* be permitted. This restriction, Apple believes, is kosher under the DMA under another provision of Article 6, Section 4, which states:


> The gatekeeper shall not be prevented from taking, to the extent 
> that they are strictly necessary and proportionate, measures to 
> ensure that third-party software applications or software 
> application stores do not endanger the integrity of the hardware 
> or operating system provided by the gatekeeper, provided that such 
> measures are duly justified by the gatekeeper.


So any third-party app that is prevented from appearing in the App Store because it uses private APIs or [SPIs](https://blog.eidinger.info/system-programming-interfaces-spi-in-swift-explained) will thus also be prevented from appearing in third-party marketplaces. Apps that attempt to circumvent sandbox restrictions, background processing restrictions, etc. will be considered by Apple to “endanger the integrity of the hardware or operating system”.


One oddity is that the DMA’s prohibition against content-based restrictions by gatekeepers is that Apple will not be permitted to reject apps or games for piracy or copyright violations. If a rando no-name developer submits for distribution on a third-party marketplace a game that features Buzz Lightyear, Donald Duck, Mario, and Donkey Kong going on a murderous *Grand-Theft-Auto*-style blood-soaked (among other bodily fluids) rampage, Apple will not be permitted to reject it on copyright violation grounds. They may not be permitted to reject an app titled “Tim Cook Is a Jerk” or “Apple Keynote” either. The DMA is clear that gatekeepers can only reject or block apps for technical reasons, not content reasons, no matter if the content is glaringly illegal. Under the DMA, it’s up to government entities and individual marketplaces to gate apps by content.


## The CTF Upends Expectations and Seems to Be Apple’s Defense Against Having Control Over iOS Wrested Away


One of Apple’s strategic concerns about the DMA is protecting the large (and still-growing) revenue it garners from third-party iOS apps. (Duh.) Another is protecting its customers’ privacy, safety, and user experience.


But Apple’s overriding concern is surely *control*. Control encompasses all of Apple’s concerns, from their own revenue to users’ experiences. Any form of compliance with the DMA necessarily implies Apple losing some control over the iOS platform. (Any users who switch from Safari, or any other WebKit-based browser, to a browser using Google Chrome’s Blink or Mozilla’s Firefox/Gecko rendering engines are [almost](https://daringfireball.net/linked/2015/07/31/safari-chrome-battery-life) [certainly](https://daringfireball.net/2017/05/safari_vs_chrome_on_the_mac#fn2-2017-05-24) going to see an adverse hit to battery life. But Apple must allow third-party web rendering engines on the iPhone in the EU, including through the App Store.6)


The CTF, I think, is Apple’s way of minimizing the risk of competing marketplace stores from their biggest rivals: Meta, Google, Microsoft, and Amazon (probably in that order). The EC is obsessed with payment processing and Apple’s commissions from IAP. Apple’s stance, from the inception of the App Store in 2008 through today, has been that they monetize the iOS platform solely through purchase commissions of paid apps, and because that’s the only way they monetize the platform, that’s one of the reasons the use of their own App Store payment system has been mandatory. (Apple also argues, with numerous meritable points, that there are user benefits to mandating the use of App Store payments. My favorite example are their subscription policies, including mandatory renewal notices and easy cancellation.) You can agree or disagree that this is a good policy, including the base assumption that Apple should seek to “monetize” the iOS platform in any way at all different from how they monetize MacOS7 — but that’s Apple’s stance.


The DMA is a direct attack on Apple’s entire monetization strategy. It mandates that alternate payment processing be available to apps in the EU, even from Apple’s own App Store, mandates permitting links to the web for payment, and mandates allowing apps to be distributed from outside the App Store. *Attack* is a strong word, but huge portions of the DMA are clearly targeting one platform: the iPhone/iOS.


The EC’s obsession with payment processing and commissions blinded them, I think, to the fact that Apple has always had other options for monetization. This Core Technology Fee, based on installations rather than purchases, is one of them.


The CTF disrupts the free/freemium model used by Apple’s biggest rivals and competitors. Meta’s apps are all free: WhatsApp, Instagram, Facebook, and now Threads. Meta has paid Apple effectively nothing for those apps, ever. The YouTube app offers IAP subscriptions but most of Google’s popular iOS apps are just completely free, so Google pays Apple nothing. Spotify has 500 million worldwide users, [split 40-60 between paid and free](https://techcrunch.com/2023/04/25/spotify-now-has-more-than-500m-users/) (ad-supported). That means Spotify likely has roughly 100 million free users on iOS — and Spotify pays Apple nothing.


If any of these companies, with hundreds of millions of EU users, opts in to the new EU rules (and thus opts out of the existing App Store rules), they’ll be on the hook to pay Apple hundreds of millions of dollars (well, euros — but they’re roughly 1:1) per year.


My first thought upon doing this back-of-the-envelope math was that the CTF was a poison pill. Of course none of these companies that pay Apple nothing to distribute their apps through the App Store would opt in to a new system that would require them to pay hundreds of millions of dollars per year, per app. Right? But then I realized that these companies operate at such enormous financial scale that “hundreds of millions of dollars” isn’t ridiculous to them.


Consider simply that Google pays Apple $20-fucking-BILLION dollars per year to keep Google Search as the default search engine in Safari. They may well consider paying Apple a mere $1 billion per year acceptable to run their own iOS marketplace in the EU. Likewise for Meta and Microsoft, which like Google are fabulously profitable. Probably not, however, for Spotify, [which has never been consistently profitable](https://www.engadget.com/spotify-grew-far-more-than-expected-but-is-still-losing-money-121553523.html). Not surprisingly, while Meta, Microsoft, and Google have refrained from comment, [Spotify is shocked](https://newsroom.spotify.com/2024-01-26/apples-proposed-changes-reject-the-goals-of-the-dma/) — shocked — at Apple’s proposed compliance with the DMA, describing it as “extortion” and “a complete and total farce”. (And MG Siegler thought *Apple’s* press release dripped with disdain.)


The DMA says Apple can’t make the App Store the exclusive distribution source for iOS apps in the EU, and can’t make its own payment system exclusive for apps from the App Store, either. But I don’t see anything in the DMA that says Apple is prevented from charging fees to developers.


The assumption from many App Store critics has been something like this: *We don’t like Apple’s current iOS App Store policies. The DMA demands Apple change those policies in the EU. Therefore Apple will surely change its policies in the EU to something we like, and that Apple loathes.* (And Mozilla, to name another outspoken critic of Apple’s restrictions and policies, [further assumed that Apple would change its worldwide policies on browser engines](https://www.theverge.com/2024/1/26/24052067/mozilla-apple-ios-browser-rules-firefox) to match the EU’s requirements in the DMA. They’re smoking the good stuff.)


That the DMA declares Apple’s existing terms no longer acceptable does not mean Apple’s only compliant response would be to cede most control over iOS. What Apple has proposed this week, across the board, indicates a desire to keep iOS (and the App Store across all platforms) as much in line with Apple’s desires as possible within the letter of the DMA. Anyone who thought Apple would propose different has not been paying attention *at all*.


## These Are Merely Proposals


I’ve emphasized throughout this piece the word *proposals*. That’s key, because no one, including Apple, knows whether the European Commission is going to find any or all of them compliant with the DMA. Apple has met with EC representatives dozens of times across several years regarding the DMA, but the way the EC works is that (1) they pass laws; (2) companies do all the work to attempt compliance with those laws; and only then (3) does the EC decide whether they comply. Companies like Apple don’t get to run ideas past the EC and get a thumbs-up or thumbs-down. They have to build them, then find out.


Which brings me back to my lede, and Sebastiaan de With’s quip that he couldn’t tell if a gripe about “overly powerful, rent-seeking gatekeepers” was about Apple, or about the EU.


The delicious irony in Apple’s not knowing if these massive, complicated proposals will be deemed DMA-compliant is that their dealings with the European Commission sound exactly like App Store developers’ dealings with Apple. Do all the work to build it first, and only *then* find out if it passes muster with  largely inscrutable rules interpreted by faceless bureaucrats.


---

1. “App marketplace” is Apple’s term for a third-party app store. I’m adopting it, because (a) it’s fair, plain, non-pejorative language; and (b) it deftly gets around any confusion between Apple’s first-party title-cased “App Store” and third-party generic “app stores”. For example, presumably because Apple holds a trademark for “App Store”, Amazon’s store for Android and Windows 11 apps (which has [existed since 2011](https://daringfireball.net/linked/2011/03/22/8-steps), with little fanfare, and, I think, very few users) is named [Amazon Appstore](https://www.amazon.com/gp/mas/get-appstore/android). [The text of the EU’s Digital Markets Act](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32022R1925#d1e2591-1-1) describes such stores, a bit formally, as “software application stores”. ↩︎
2. In 2022, iOS 16 dropped support for the [7th (and final) generation iPod Touch](https://everymac.com/systems/apple/ipod/specs/ipod-touch-7th-gen-a2178-2019-specs.html), which was released in 2019. So these changes in iOS 17 won’t come to iPod Touch holdouts either. ↩︎︎
3. Makes me wonder if Apple had this in mind when they renamed iOS for iPad to “iPadOS” [in June 2019](https://www.macrumors.com/2019/06/03/ios-for-ipad-renamed-ipados/). I suspect, however, that they created the iPadOS name only to reflect the growing disparity in features between the two platforms — things like side-by-side multitasking and now Stage Manager. (Also the fact that many new features destined, ultimately, for both platforms come to the iPhone a year ahead of the iPad, like Home screen widgets and lockscreen customization.) But it sure is a happy coincidence for Apple in retrospect with regard to the DMA. ↩︎︎
4. In theory this presents a perverse incentive for developers who opt in to the new EU rules: to release software updates less frequently than once every 12 months. But I think that’s impractical. What app can become so popular that it garners over 1 million downloads in the EU yet not issue regular software updates for bug fixes, new features, and adopting new iOS platform features? I play some older games that [haven’t issued updates in years](https://apps.apple.com/us/app/texas-holdem/id284602850), but those aren’t games with millions of active users. I think this loophole is purely hypothetical and not worth worrying about.
There’s also an attack vector: someone with a massive following could direct their fans to spite-download a competitor or enemy’s free app, costing them €0.50 per install. [Apple’s FAQ](https://developer.apple.com/support/dma-and-apps-in-the-eu/#dev-qa) includes an entire section about their defenses to prevent “install bombing”. ↩︎︎
5. This seemingly rules out Epic from offering an Epic Games Store, as the developer account Epic used for Fortnite was revoked after they violated the terms of the developer agreement with their in-app-payment-processing stunt. But Epic’s developer tools subsidiary [still has a developer account for Unreal Engine](https://daringfireball.net/2021/09/epic_apple_developer_accounts), so perhaps they can offer an Unreal Games Store instead? Unclear — as with so much else regarding this entire proposal. ↩︎︎
6. One feature browsers using third-party rendering engines won’t have is the ability to “Save to Home Screen”. That’s the feature that’s been in iOS [since the day the iPhone launched](https://daringfireball.net/2007/06/wwdc_2007_keynote) — a year ahead of native third-party apps and the App Store — that allows a web app to be saved to your Home screen from Safari to act like an app. (Apple even just brought this feature to MacOS 14 Sonoma this year [under the name “Add to Dock”](https://support.apple.com/en-us/104996).) Web developer proponents of “Progressive Web Apps” (PWAs) have been clamoring for third-party rendering engines on iOS so they can build web apps that use features WebKit on iOS doesn’t support. They’ll need to bundle their PWAs with the embedded third-party rendering engines, [Electron-style](https://daringfireball.net/2018/12/electron_and_the_decline_of_native_apps), and distribute them through EU marketplace apps, just like big-boy native apps written in Swift and Objective-C, if they want to use features unsupported by WebKit. (Or be satisfied running only in a tab inside a browser app that includes a non-WebKit engine.)
The fact that iOS browsers using third-party rendering engines will not be able to save PWAs as standalone apps on the Home screen does not appear to be written in any of [Apple’s documentation regarding BrowserEngineKit](https://developer.apple.com/documentation/browserenginekit), but it doesn’t need to be. There simply are no APIs to enable it, nor any clause in the DMA that requires it. I checked with a well-informed little birdie who confirmed that this will not be possible. As with almost every aspect of Apple’s DMA compliance proposals, those who anticipated a PC/Mac-style anything-goes install-whatever-software-you-want free-for-all are — if Apple’s interpretation of the DMA is largely correct — going to be sorely disappointed. ↩︎︎
7. Through 2009 — two years after the launch of the iPhone, one year after the launch of the iOS App Store — Apple sold Mac OS X version upgrades for $129. Meaning each time you upgraded from, say, 10.2 to 10.3, then again from 10.3 to 10.4, you had to pay $129. Mac fans would wait in line outside Apple Stores to buy these upgrades on launch day. From 2009’s Mac OS X 10.6 Snow Leopard through 2013’s Mac OS X 10.9 Mavericks, they sold version upgrades for $29 and then $19. As hard as it is for many longtime developers to accept that Apple charges a mandatory sales commission (or, now in the EU, a Core Technology Fee per-installation) for all third-party iOS apps, it would be even harder to make today’s iPhone users accept paying $129/year for version updates to iOS. In a sense, starting with the iPhone, Apple has shifted from monetizing its OSes by charging users a licensing fee to charging developers a privilege fee. ↩︎︎



| **Previous:** | [‘Like the Sixth Finger in an AI-Rendered Hand’](https://daringfireball.net/2024/01/the_sixth_finger) |
| **Next:** | [The Vision Pro](https://daringfireball.net/2024/01/the_vision_pro) |


PreviousNext