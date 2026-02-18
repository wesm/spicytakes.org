---
title: "Something Is Rotten in the State of Cupertino"
date: 2025-03-12
url: https://daringfireball.net/2025/03/something_is_rotten_in_the_state_of_cupertino
slug: something_is_rotten_in_the_state_of_cupertino
word_count: 4449
---


In the two decades I’ve been in this racket, I’ve never been angrier at myself for missing a story than I am about Apple’s [announcement on Friday](https://daringfireball.net/2025/03/apple_is_delaying_the_more_personalized_siri_apple_intelligence_features) that the “more personalized Siri” features of Apple Intelligence, scheduled to appear between now and WWDC, would be delayed until “the coming year”.


I should have my head examined.


This announcement dropped as a surprise, and certainly took me by surprise to some extent, but it was all there from the start. I should have been pointing out red flags starting back at WWDC last year, and I am embarrassed and sorry that I didn’t see what should have been very clear to me from the start.


How I missed this is twofold. First, I’d been lulled into complacency by Apple’s track record of consistently shipping pre-announced products and features. Their record in that regard wasn’t perfect, but the exceptions tended to be around the edges. (Nobody was particularly clamoring for Apple to make a multi-device inductive charging mat, so it never generated too much controversy [when AirPower turned out to be a complete bust](https://daringfireball.net/2025/03/apple_is_delaying_the_more_personalized_siri_apple_intelligence_features#fn1-2025-03-07).) Second, I was foolishly distracted by the “Apple Intelligence” brand umbrella. It’s a fine idea for Apple to brand its AI features under an umbrella term like that, similar to how a bunch of disparate features that allow different Apple devices to interoperate are under the “[Continuity](https://www.apple.com/macos/continuity/)” umbrella. But there’s no such thing, technically speaking, as “Continuity”. It’s not like there’s an Xcode project inside Apple named Continuity.xcodeproj, and all the code that supports everything from AirDrop to Sidecar to iPhone Mirroring to clipboard sharing is all implemented in the same framework of code. It’s a marketing term, but a useful one — it helps Apple explain the features, and helps users understand them.


The same goes for “Apple Intelligence”. It doesn’t exist as a single thing or project. It’s a marketing term for a collection of features, apps, and services. Putting it all under a single obvious, easily remembered — and [easily promoted](https://www.creativebloq.com/design/print-design-publishing/apples-new-billboard-ads-are-um-not-great) — name makes it easier for users to understand that Apple is launching a new initiative. It also makes it easier for Apple to just say “*These are the devices that qualify for all of these features, and other devices — older ones, less expensive ones — get none of them.*”


Let’s say Apple were to quietly abandon the dumb Image Playground app next year. It just disappears from iOS 19 and MacOS 16. That would just be Apple eliminating a silly app that almost no one uses or should use. That wouldn’t be a setback or rollback of “Apple Intelligence”. I would actually argue that axing Image Playground would improve Apple Intelligence; its mere existence greatly lowers the expectations for how good the whole thing is.1


What I mean by that is that it was clear to me from the WWDC keynote onward that some of the features and aspects of Apple Intelligence were more ambitious than others. Some were downright trivial; others were proposing to redefine how we will do our jobs and interact with our most-used devices. That was clear. But yet somehow I didn’t focus on it. Apple itself strongly hinted that the various features in Apple Intelligence wouldn’t all ship at the same time. What they didn’t spell out, but anyone could intuit, was that the more trivial features would ship first, and the more ambitious features later. That’s where the red flags should have been obvious to me.


In broad strokes, there are four stages of “doneness” or “realness” to features announced by any company:

1. Features that the company’s own product representatives will demo, themselves, in front of the media. Smaller, more personal demonstrations are more credible than on-stage demos. But the stakes for demo fail are higher in an auditorium full of observers.
2. Features that the company will allow members of the media (or other invited outside observers and experts) to try themselves, for a limited time, under the company’s supervision and guidance. Vision Pro demos were like this at WWDC 2023. A bunch of us got to use pre-release hardware and in-progress software for 30 minutes. It wasn’t like free range “Do whatever you want” — it was a guided tour. But we were the ones actually using the product. Apple allowed hands-on demos for a handful of media (not me) at Macworld Expo [back in 2007 with prototype original iPhones](https://www.macworld.com/article/186251/ihnatkoiphone.html) — some of the “apps” were just screenshots, but most of the iPhone actually worked.
3. Features that are released as beta software for developers, enthusiasts, and the media to use on their own devices, without limitation or supervision.
4. Features that actually ship to regular users, and hardware that regular users can just go out and buy.


As of today — March 2025 — every feature in Apple Intelligence [that has actually shipped](https://9to5mac.com/2025/02/26/this-is-every-apple-intelligence-feature-thats-available-now/) was at level 1 back at WWDC. After the keynote, dozens of us in the press were invited to a series of small-group briefings where we got to watch Apple reps demo features like Writing Tools, Photos Clean Up, Genmoji, and more. We got to see predictive code completion in Xcode. What has shipped, as of today, they were able to show, in some functional state, in June.


For example, there was a demo involving a draft email message on an iPad, and the Apple rep used Writing Tools to make it “more friendly”. I was in a group of just four or five other members of the media, watching this. As usual, we were encouraged to interrupt with questions. Knowing that LLMs are non-deterministic, I asked whether, as the Apple rep was performing this same demo for each successive group of media members, the “more friendly” result was exactly the same each time. He laughed and said no — that while the results are very similar each time, and he hopes they continue to be (hence the laughing), there were subtle differences *sometimes* between different runs of the same demo. As I recall, he even used Undo to go back to the original message text, invoked Writing Tools to make it “more friendly” again, and we could see that a few of the word choices were slightly different. That answered both my explicit question and my implicit one: Writing Tools generates non-deterministic results, and, more importantly, what we were watching really was a live demo.


We didn’t get to try any of the Apple Intelligence features ourselves. There was no Apple Intelligence “hands on”. But we did see a bunch of features demoed, live, by Apple folks. In my above hierarchy of realness, they were all at level 1.


But we didn’t see *all* aspects of Apple Intelligence demoed. None of the “more personalized Siri” features, the ones that Apple, [in its own statement announcing their postponement](https://daringfireball.net/2025/03/apple_is_delaying_the_more_personalized_siri_apple_intelligence_features), described as having “more awareness of your personal context, as well as the ability to take action for you within and across your apps”. Those features encompass three main things:

- “Personal context” — Knowing details and information about you from a “semantic index”, built from the contents of your email, messages, files, contacts, and more. In theory, eventually, all the information on your device that you wish to share with Siri will be in this semantic index. If you can look it up on your device, Siri will be able to look it up on your device.
- “Onscreen awareness” — Giving Siri awareness of whatever is displayed on your screen. [Apple’s own example usage](https://www.apple.com/apple-intelligence/): “If a friend texts you their new address, you can say ‘Add this address to their contact card,’ and Siri will take care of it.”
- “In-app actions” — Giving Siri the ability, through the App Intents framework, to do things in and across apps that *you* can do, the old fashioned way (yourself) in and across apps. Again, here’s Apple’s own example usage:

You can make a request like “Send the email I drafted to April and
Lilly” and Siri knows which email you’re referencing and which app
it’s in. And Siri can take actions across apps, so after you ask
Siri to enhance a photo for you by saying “Make this photo pop,”
you can ask Siri to drop it in a specific note in the Notes app — without lifting a finger.


There were no demonstrations of *any* of that. Those features were all at level 0 on my hierarchy. That level is called vaporware. They were features Apple *said* existed, which they *claimed* would be shipping in the next year, and which they *portrayed*, to great effect, in the signature “Siri, when is my mom’s flight landing?” segment of the WWDC keynote itself, [starting around the 1h:22m mark](https://www.youtube.com/live/RXeOiIDNNek?t=4934). Apple was either unwilling or unable to demonstrate those features in action back in June, even with Apple product marketing reps performing the demos from a prepared script using prepared devices.


This shouldn’t have just raised a concern in my head. It should have set off blinding red flashing lights and deafening klaxon alarms.


Even the very engineers working on a project never know exactly how long something is going to take to complete. An outsider observing a scripted demo of incomplete software knows far less (than the engineers) just how much more work it needs. But you can make a rough judgment. And that’s where my aforementioned hierarchy of realness comes into play. Even outsiders can judge how close a public beta (stage 3) feels to readiness. A feature or product that Apple will allow the press to play with, hands-on (stage 2) is further along than a feature or product that Apple is only willing to demonstrate themselves (stage 1).


But a feature or product that Apple is unwilling to demonstrate, at all, is unknowable. Is it mostly working, and close to, but not quite, demonstratable? Is it only kinda sorta working — partially functional, but far from being complete? Fully functional but prone to crashing — or in the case of AI, prone to hallucinations and falsehoods? Or is it complete fiction, just an idea at this point?


What Apple showed regarding the upcoming “personalized Siri” at WWDC was *not* a demo. It was a concept video. Concept videos are bullshit, and a sign of a company in disarray, if not crisis. [The Apple that commissioned the futuristic “Knowledge Navigator” concept video](https://daringfireball.net/2011/11/companies_that_publish_concept_videos) in 1987 was the Apple that was on a course to near-bankruptcy a decade later. Modern Apple — the post-NeXT-reunification Apple of the last quarter century — does not publish concept videos. They only demonstrate actual working products and features.


Until WWDC last year, that is.


My deeply misguided mental framework for “Apple Intelligence” last year at WWDC was something like this: *Some of these features are further along than others, and Apple is showing us those features in action first, and they will surely be the features that ship first over the course of the next year. The other features must be coming to demonstratable status soon.* But the mental framework I should have used was more like this: *Some of these features are merely table stakes for generative AI in 2024, but others are ambitious, groundbreaking, and, given their access to personal data, potentially dangerous. Apple is only showing us the table-stakes features, and isn’t demonstrating any of the ambitious, groundbreaking, risky features.*


It gets worse. Come September, Apple held its annual big event at Apple Park to unveil the iPhone 16 lineup. Apple Intelligence features were highlighted in the announcement. Members of the media from around the world were gathered. That was a new opportunity, three months after WWDC, for Apple to demonstrate — or even better, offer hands-on access to the press to try themselves — the new personalized Siri features. They did not. No demos, at all. But they did promote them, once again, in the event keynote.2


But yet while Apple still wouldn’t demonstrate these features in person, they did commission and broadcast a TV commercial showing these purported features in action, presenting them as a reason to purchase a new iPhone — [a commercial they pulled, without comment, from YouTube this week](https://daringfireball.net/linked/2025/03/08/apple-pulls-bella-ramsey-ad-that-promoted-vaporware-personalized-siri-feature).


Last week’s announcement — “It’s going to take us longer than we thought to deliver on these features and we anticipate rolling them out in the coming year” — was, if you think about it, another opportunity to demonstrate the current state of these features. Rather than simply issue a statement to the media, they could have invited select members of the press to Apple Park, or Apple’s offices in New York, or even just remotely over a WebEx conference call, and demonstrated the current state of these features live, on an actual device. That didn’t happen. If these features exist in any sort of working state at all, no one outside Apple has vouched for their existence, let alone for their quality.


## Duke Nukem Intelligence


Why did Apple show these personalized Siri features at WWDC last year, and promise their arrival during the first year of Apple Intelligence? Why, for that matter, do they now claim to “anticipate rolling them out in the coming year” if they still currently do not exist in demonstratable form? (If they *do* exist today in demonstratable form, they should, you know, *demonstrate them*.)


I’m not trying to be obtuse here. It’s obvious why some executives at Apple might have *hoped* they could promote features like these at WWDC last year. Generative AI is the biggest thing to happen in the computer industry since previous breakthroughs this century like mobile (starting with the iPhone, followed by Android), social media (Meta), and cloud computing (Microsoft, Google, and Amazon). Nobody knows where it’s going but wherever it’s heading, it’s going to be big, important, and perhaps profitable. Wall Street certainly noticed. And prior to WWDC last year, Apple wasn’t in the game. They needed to pitch their AI story. And a story that involved nothing but table-stakes AI features isn’t nearly as compelling a story as one that involves innovative, breakthrough, ambitious personal features.


But while there’s an obvious appeal to Apple pitching the most compelling, most ambitious AI story possible, the only thing that was essential was telling a story that was true. If the truth was that Apple only had features ready to ship in the coming year that were table stakes compared to the rest of the industry, that’s the story they needed to tell. Put as good a spin on it as possible, but them’s the breaks when you’re late to the game.


The fiasco here is not that Apple is late on AI. It’s also not that they had to announce an embarrassing delay on promised features last week. Those are problems, not fiascos, and problems happen. They’re inevitable. Leaders prove their mettle and create their legacies not by how they deal with successes but by how they deal with — how they acknowledge, understand, adapt, and solve — problems. The fiasco is that Apple pitched a story that wasn’t true, one that *some* people within the company surely understood wasn’t true, and they set a course based on that.


The Apple of the Jobs exile years — the Sculley / Spindler / Amelio Apple of 1987–1997 — promoted all sorts of amazing concepts that were no more real than the dinosaurs of *Jurassic Park*, and promised all sorts of hardware and (especially) software that never saw the light of day. Promoting what you *hope* to be able to someday ship is way easier and more exciting than promoting what you *know* is actually ready to ship. However close to financial bankruptcy Apple was when Steve Jobs returned as CEO after the NeXT reunification, the company was already completely bankrupt of credibility. Apple today is the most profitable and financially successful company in the history of the world. Everyone notices such success, and the corresponding accumulation of great wealth. Less noticed, but to my mind the more impressive achievement, is that over the last three decades, the company *also* accumulated an abundant reserve of credibility. When Apple showed a feature, you could bank on that feature being real. When they said something was set to ship in the coming year, it would ship in the coming year. In the worst case, maybe that “year” would have to be stretched to 13 or 14 months. You can stretch the truth and maintain credibility, but you can’t maintain credibility with bullshit. And the “more personalized Siri” features, it turns out, were bullshit.


Keynote by keynote, product by product, feature by feature, year after year after year, Apple went from a company that you couldn’t believe would even remain solvent, to, by far, the most credible company in tech. Apple remains at no risk of financial bankruptcy (and in fact remains the most profitable company in the world). But their credibility is now damaged. Careers will end before Apple might ever return to the level of “if they say it, you can believe it” credibility the company had earned at the start of June 2024.


*Damaged* is arguably too passive. It was *squandered*. This didn’t happen to Apple. Decision makers within the company did it.


*Who* decided these features should go in the WWDC keynote, with a promise they’d arrive in the coming year, when, at the time, they were in such an unfinished state they could not be demoed to the media even in a controlled environment? Three months later, who decided Apple should double down and advertise these features in a TV commercial, and promote them as a selling point of the iPhone 16 lineup — not just any products, but the very crown jewels of the company and the envy of the entire industry — when those features still remained in such an unfinished or perhaps even downright non-functional state that they *still* could not be demoed to the press? Not just couldn’t be shipped as beta software. Not just couldn’t be used by members of the press in a hands-on experience, but could not even be shown to work by Apple employees on Apple-controlled devices in an Apple-controlled environment? But yet they advertised them in a commercial for the iPhone 16, when it turns out they won’t ship, in the best case scenario, until months after the iPhone 17 lineup is unveiled?


When that whole campaign of commercials appeared, I — along with many other observers — was distracted by the fact that *none* of the features in Apple Intelligence had yet shipped. It’s highly unusual, and arguably ill-considered, for Apple to advertise *any* features that haven’t yet shipped. But one of those commercials was not at all like the others. The other commercials featured Apple Intelligence features that were close to shipping. We know today they were close to shipping because they were either in the iOS 18.1 betas already, in September, or would soon appear in developer betas for iOS 18.2 and 18.3. Right now, today, they’ve all actually shipped and are in the hands of iPhone 16 users. But the “Siri, what’s the name of the guy I had a meeting with a couple of months ago at Cafe Grenel?” commercial was entirely based on a feature Apple still has never even demonstrated.


Who said “*Sure, let’s promise this*” and then “*Sure, let’s advertise it*”? And who said “*Are you crazy, this isn’t ready, this doesn’t work, we can’t promote this now?*” And most important, who made the call which side to listen to? Presumably, that person was Tim Cook.


Even with everything Apple overpromised (if not outright lied about) at the WWDC keynote, the initial takeaway from WWDC from the news media was wrongly focused on their partnership with OpenAI. The conventional wisdom coming out of the keynote was that Apple had just announced something called “Apple Intelligence” but it was powered by ChatGPT, when in fact, the story Apple told was that they — Apple — had built an entire system called Apple Intelligence, entirely powered by Apple’s own AI technology, and that it spanned from on-device execution all the way to a new Private Cloud Compute infrastructure they not only owned but are powering with their own custom-designed server hardware based on Apple Silicon chips. And that on top of all that, as a proverbial cherry on top, Apple *also* was adding an optional integration layer with ChatGPT.


So, yes, given that the news media gave credit for Apple’s own actual announced achievements to OpenAI, Apple surely would have been given even *less* credit had they not announced the “more personalized Siri” features. It’s easy to imagine someone in the executive ranks arguing “*We need to show something that only Apple can do.*” But it turns out they announced something Apple *couldn’t* do. And now they look so out of their depth, so in over their heads, that not only are they years behind the state-of-the-art in AI, but they don’t even know *what* they can ship or *when*. Their headline features from nine months ago not only haven’t shipped but still haven’t even been demonstrated, which I, for one, now presume means they *can’t* be demonstrated *because they don’t work*.


## ‘So Why the Fuck Doesn’t It Do That?’


In May 2011, [Fortune published an extraordinary look inside Apple by Adam Lashinsky](https://fortune.com/article/inside-apple/), at what we now know to be the peak, and (alas) end, of the Steve Jobs era. The piece opens thus:


> Apple doesn’t often fail, and when it does, it isn’t a pretty
> sight at 1 Infinite Loop. In the summer of 2008, when Apple
> launched the first version of its iPhone that worked on
> third-generation mobile networks, it also debuted MobileMe, an
> e-mail system that was supposed to provide the seamless
> synchronization features that corporate users love about their
> BlackBerry smartphones. MobileMe was a dud. Users complained about
> lost e-mails, and syncing was spotty at best. Though reviewers
> gushed over the new iPhone, they panned the MobileMe service.
> Steve Jobs doesn’t tolerate duds. Shortly after the launch event,
> he summoned the MobileMe team, gathering them in the Town Hall
> auditorium in Building 4 of Apple’s campus, the venue the company
> uses for intimate product unveilings for journalists. According to
> a participant in the meeting, Jobs walked in, clad in his
> trademark black mock turtleneck and blue jeans, clasped his hands
> together, and asked a simple question:
> “Can anyone tell me what MobileMe is supposed to do?” Having
> received a satisfactory answer, he continued, “So why the fuck
> doesn’t it do that?”
> For the next half-hour Jobs berated the group. “You’ve tarnished
> Apple’s reputation,” he told them. “You should hate each other for
> having let each other down.” The public humiliation particularly
> infuriated Jobs. Walt Mossberg, the influential Wall Street
> Journal gadget columnist, had panned MobileMe. “Mossberg, our
> friend, is no longer writing good things about us,” Jobs said. On
> the spot, Jobs named a new executive to run the group.


Tim Cook should have already held a meeting like that to address and rectify this Siri and Apple Intelligence debacle. If such a meeting hasn’t yet occurred or doesn’t happen soon, then, I fear, that’s all she wrote. The ride is over. When mediocrity, excuses, and bullshit take root, they take over. A culture of excellence, accountability, and integrity cannot abide the acceptance of any of those things, and will quickly collapse upon itself with the acceptance of all three.


---

1. Image Playground would make a ton of sense not as a consumer-facing app, but as an example project for developers. Long ago, Apple [used to share the source code for TextEdit](https://developer.apple.com/library/archive/samplecode/TextEdit/Introduction/Intro.html) as an example project for Mac developers. (TextEdit is actually a low-key great application, though. It’s genuinely useful, reliable, and understandable.) [Apple shares tons of sample code at WWDC each year](https://developer.apple.com/sample-code/wwdc/2024/). Image Playground would be a great sample project. The silly app icon even looks like something from a WWDC sample project. What Image Playground is *not* is a credible useful generative AI tool. Yet Apple keeps talking about it — and showing it off in new hardware demonstrations — like it’s something they should be proud of and that anyone might credibly use for real-world work or even personal purposes. Image Playground does exemplify just how state-of-the-art the generative AI features are in Apple Intelligence, but not in the way Apple seems to think. ↩︎
2. Skip to [the 53-minute mark of Apple’s September “It’s Glowtime” event](https://www.youtube.com/live/uarNiSl_uh4?t=3184) introducing the iPhones 16, and it’s Craig Federighi who says the following:

“Siri will be able to tap into your personal context to help you in ways that are unique to you. Like pulling up the recommendation for the TV show that your brother sent you last month. And Siri will gain onscreen awareness. So when your friend texts you about a new album, you’ll be able to simply say, ‘Play that.’ And then you’ll be able to take hundreds of new actions in your apps, like updating a friend’s contact card with his new address, or adding a set of photos to a specific album. With Siri’s personal context understanding and action capabilities, you’ll be able to simply say, ‘Send Erica the photos from Saturday’s barbecue’, and Siri will dig up the photos and send them right off.”

That’s about 40 seconds of keynote time I bet Federighi regrets — and that I suspect [he was skeptical about](https://9to5mac.com/2025/03/09/siri-apple-intelligence-ios-18-development-went-wrong/) including. It’s telling though that unlike WWDC, Apple didn’t *show* those features or spend even a full minute talking about at the iPhone 16 event — despite the fact that, ostensibly, those features should have been three months closer to shipping than they were in June. Federighi’s title is SVP of software, and Apple Intelligence and Siri are “software”, but John Giannandrea (SVP of machine learning and
AI strategy) is Federighi’s peer, not subordinate, [on the org chart](https://www.apple.com/leadership/) — both report directly to Tim Cook — and is responsible for Siri and Apple Intelligence. Why it was Federighi, not Giannandrea, pitching those features in the iPhone 16 event keynote almost certainly comes down to Federighi’s presentation skills and stage presence, not responsibility for the features themselves. But who’s going on camera to pitch these features and promise their future availability the next time? ↩︎︎



| **Previous:** | [A New System-Wide UI Look for iOS — Let Alone MacOS, Too — Would Be a Huge Deal](https://daringfireball.net/2025/03/new_ui_look_ios_would_be_a_huge_deal) |
| **Next:** | [A Postscript on the Singular Nature of Mark Gurman’s Reporting](https://daringfireball.net/2025/03/a_postscript_on_the_singular_nature_of_mark_gurmans_reporting) |


PreviousNext