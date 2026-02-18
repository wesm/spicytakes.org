---
title: "Coming to Grips With Apple’s Seemingly Unshakable Sense of Entitlement to Its Commissions From Third-Party iOS Apps"
date: 2024-01-17
url: https://daringfireball.net/2024/01/coming_to_grips_with_apples_seemingly_unshakable_sense_of_app_store_entitlement
slug: coming_to_grips_with_apples_seemingly_unshakable_sense_of_app_store_entitlement
word_count: 1808
---


[Tim Sweeney, on Twitter/X, yesterday at 10:30am](https://twitter.com/TimSweeneyEpic/status/1747280541362102287/):


> As of today, developers can begin exercising their 
> court-established right to tell US customers about better prices 
> on the web. These awful Apple-mandated confusion screens are over 
> and done forever.


That take didn’t last long.


[Sweeney, yesterday at 7:00pm](https://twitter.com/TimSweeneyEpic/status/1747408148799881390), after Apple released [the details of its intended compliance](https://daringfireball.net/linked/2024/01/16/apple-guidelines-external-purchase-links) with the anti-steering (*anti-anti-steering*?) mandate from the Epic v. Apple case:


> A quick summary of glaring problems we’ve found so far: 
> Apple has introduced an anticompetitive new 27% tax on web 
> purchases. Apple has never done this before, and it kills price 
> competition. Developers can’t offer digital items more cheaply 
> on the web after paying a third-party payment processor 3-6% 
> and paying this new 27% Apple Tax.
> [Sweeney’s points 2–4, complaining about Apple’s stringent design, 
> presentation, and privacy demands regarding external links, 
> omitted.] 
> Epic will contest Apple’s bad-faith compliance plan in 
> District Court.


Sweeney’s description makes it sound as though Apple is demanding its commission from all web sales for apps and services that have an iOS app. They’re not. They’re only demanding the commission from web sales that occur within 7 days of a user tapping through to the web from [the new External Purchase Links entitlement](https://developer.apple.com/support/storekit-external-entitlement-us/) in an app. Any app or service that already sells over the web, without paying a cent to Apple, can continue to do so in exactly the same way.


Also, Apple *has* done this before: what they announced yesterday is almost exactly in line [with their compliance with Netherlands regulations pertaining to dating apps in 2022](https://daringfireball.net/2022/02/going_dutch).


Before yesterday:

- iOS app developers could sell digital content and subscriptions over the web, without paying Apple any commission.
- iOS apps outside [the “reader” category](https://daringfireball.net/linked/2021/09/01/apple-anti-steering-relaxation) could not link to, nor even tell users about, those web purchases from within their apps.


After yesterday:

- Apps that wish to link to — or, I think, even inform users about — web purchasing options from within their iOS apps must (a) still offer Apple’s IAP for those items; (b) pay Apple its adjusted 27/12 percent commissions on web sales that come from inside iOS apps; (c) send Apple sales data monthly and submit to audits of their sales; and (d) follow Apple’s stringent design edicts for these in-app links to the web.
- Apps that do not link out to their web stores from within their iOS apps using Apple’s new External Purchase Links entitlement can continue whatever they were doing before yesterday. For apps that do nothing new, Apple is collecting nothing new.


I’m only surprised that Sweeney was seemingly surprised by any of this. He genuinely seemed to think that Apple not only would, but *had to* allow links from within apps to the web for purchases without collecting any commission on those sales, and that developers could present those links however they chose.


I’m glad that Sweeney and Epic plan to contest this, because I’m genuinely curious whether Judge Yvonne Gonzalez Rogers sees Apple’s solution as complying with her injunction against their prior anti-steering rules. But I think it *does* comply.


---


To be clear, I think Apple should allow apps *other than games* to just tell users they can pay/buy/subscribe/whatever on the web, without any commission. That the rules which have applied only to “reader” apps since early 2022 should be extended to all apps other than games, perhaps alongside a requirement (which doesn’t apply to “reader” apps) that apps taking advantage of this *also* offer in-app purchasing.


I’d draw an exception for games — an exception that surely Sweeney would disagree with completely, given that he’s in the games business — because games are different, and hefty un-circumventable revenue commissions to platform owners are clearly standard for the video game industry. The iPhone and iPad are not PCs; they’re consoles for games and apps.


But I’m not sure at all that Apple is doing anything contrary to the law. Sweeney (and other critics of Apple’s stewardship of iOS as a tightly controlled console) believe Apple both shouldn’t and *legally can’t* comply with the anti-steering injunction this way. I only believe Apple shouldn’t, not that they legally can’t.


Most critics of Apple’s control over all iOS software are seemingly of the view that iPhones and iPads should, on principle, be largely like the Mac, where the App Store is an option, not the only game in town for software distribution. Personally, [I am on the record wishing that Apple would allow some sort of “expert” or “developer” mode](https://daringfireball.net/2021/06/annotating_apples_anti-sideloading_white_paper) — chock full of warnings, perhaps even requiring a developer account to enable — that would basically offer the same options for installing third-party software on iOS as there are on the Mac. That’s me, personally, an expert user. But even setting aside every penny of revenue generated by the App Store,1 I see and understand many of the reasons why Apple wouldn’t want to do this. There are a lot of Mac users whose Macs are overrun by adware and other scammy software. I’m not talking about viruses or malware, even — but apps that just abuse the largely free-for-all nature of the Mac platform.


Basically, there’s an argument that iOS devices should be more like traditional PCs (including the Mac), on ethical or moral grounds. The “*it’s my device, I should decide and control what software runs on it*” argument. I get it. But I also get that most consumers’ Windows PCs, and many Macs,2 are riddled with bad software (privacy invasive, resource hogging, and all sorts of [anti-user shenanigans](https://mjtsai.com/blog/2021/12/22/grammarly-disables-spell-checking-globally/) you’d never think of) that App Store policies forbid. App Store review is far from perfect — I mean come on, [that should go without saying](https://daringfireball.net/search/app+store+rejection) — but it is undeniable that adversarial software is not a problem for *any* typical users on iOS. Nothing you install from the App Store can damage your iPhone or iPad experience. Nothing you install from the App Store is difficult to uninstall if you don’t like it. The same is true of dedicated game consoles like Switch, PlayStation, and Xbox — and to a lesser degree (because Google’s Play Store review seems comparatively lax) for Android.


But the cynical take is that it’s all about the money for Apple. Maybe the cynics are right! Let’s just concede that they are, and that Apple will only make decisions here that benefit its bottom line. My argument remains that Apple *should not* be pursuing this plan for complying with the anti-steering injunction by collecting commissions from web sales that initiate in-app. Whatever revenue Apple would lose to non-commissioned web sales (for non-games) is not worth the hit they are taking to the company’s brand and reputation — this move reeks of greed and avarice — nor the increased ire and scrutiny of regulators and legislators on the “anti-Big-Tech” hunt.


Apple should have been looking for ways to *lessen* regulatory and legislative pressure over the past few years, and in today’s climate that’s more true than ever. But instead, their stance has seemingly been “*Bring it on.*” Confrontational, not conciliatory, conceding not an inch. Rather than take a sure win with *most* of what they could want, Apple is seemingly hell-bent on trying to keep *everything*. To win in chess all you need is to capture your opponent’s king. Apple seemingly wants to capture every last piece on the board — even while playing in a tournament where the referees (regulators) are known to look askance at blatant poor sportsmanship (greed).


Apple’s calculus should be to balance its natural desire to book large amounts of revenue from the App Store with policies that to some degree *placate*, rather than antagonize, regulators and legislators. No matter what the sport, no matter what the letter of the rulebook says, it’s never a good idea to piss off the refs.


That’s a metric buttload of pennies to set aside, to be sure. ↩︎


iOS App Store policy critics often point to the Mac as all the evidence they need that Apple could open up software distribution on iOS with no ill effects to users. I wrote about this back in 2021, in a piece titled “[Annotating Apple’s Anti-Sideloading White Paper](https://daringfireball.net/2021/06/annotating_apples_anti-sideloading_white_paper)”. Quoting from that column, which begins with a quote from [Apple’s white paper](https://www.apple.com/privacy/docs/Building_a_Trusted_Ecosystem_for_Millions_of_Apps.pdf):


> Page 9:
> iPhone is used every day by over a billion people — for banking, 
> to manage health data, and to take pictures of their families. 
> This large user base would make an appealing and lucrative target 
> for cybercriminals and scammers, and allowing sideloading would 
> spur a flood of new investment into attacks on iPhone, well 
> beyond the scale of attacks on other platforms like Mac.
> Here Apple dances around the elephant in the room — the question 
> of why iOS shouldn’t just work like the Mac with regard to non-App 
> Store software. Apple’s deft argument is that there are far fewer 
> Macs than iOS devices, making the Mac a less enticing target for 
> scammers and crooks (including privacy crooks). That’s more or 
> less the argument Windows proponents used to explain the profound 
> prevalence of malware on Windows compared to the Mac back in the 
> day, whilst Apple (and Mac proponents) argued otherwise, that the 
> Mac actually was far more secure at a technical level.
> But the truth Apple won’t come out and say is that it’s *both*. 
> The Mac *was* more secure by design, but *also* a far less 
> enticing target because of how many more users were (and still 
> are) on Windows. And, today, iOS *is* more secure and private than 
> the Mac. That’s the nature of the Mac as a full PC platform.
> I’ll admit it: if Mac-style sideloading were added to iOS, I’d 
> enable it, for the same reason I enable installing apps from 
> outside the App Store on my Mac: I trust myself to only install 
> trustworthy software. But it doesn’t make me a hypocrite to say 
> that I think it would be worse for the platform as a whole.
> The Mac is fundamentally designed for users who are at least 
> *somewhat* technically savvy, but tries its best to keep non-savvy 
> users from doing things they shouldn’t. But you can always hurt 
> yourself, sometimes badly, with any true power tool. The iPhone is 
> the converse: designed first and foremost for the non-savvy user, 
> and tries to accommodate power users as best it can within the 
> limits of that primary directive.


All the more pertinent today, [as Apple faces down the March 7 deadline for compliance with the E.U.’s Digital Markets Act](https://daringfireball.net/2024/01/vestager_cook) that ostensibly mandates sideloading on iOS. ↩︎︎
