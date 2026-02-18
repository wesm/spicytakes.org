---
title: "Reading Between the iPhone OS 4.0 Lines"
date: 2010-04-09
url: https://daringfireball.net/2010/04/reading_between_the_iphone_os_4_lines
slug: reading_between_the_iphone_os_4_lines
word_count: 2213
---


A few months ago, I heard suggestions that Apple had tentative plans to release a developer beta of Mac OS X 10.7 at WWDC this June. That is no longer the case. Mac OS X 10.7 development continues, but with a reduced team and an unknown schedule. It’s my educated guess that there will be no 10.7 news at WWDC this year, and probably none until WWDC 2011.


Apple’s company-wide focus has since been focused intensely on one thing: iPhone OS 4.1 The number one priority at Apple is to grow mobile market share faster than Android. Anything that is not directly competitive with Android is on the back burner.


Several of the “tentpole”2 features in iPhone OS 4 that Apple promoted at yesterday’s event are directly related to this.


## Multitasking


“Multitasking” is a catchall term that, in the context of iPhone OS 4, encompasses several different things. On an OS like Mac OS X it’s simpler to understand — multiple apps (and faceless background-only processes) operate simultaneously. On an OS like iPhone OS, that’s not how it’s going to work, and for good reason. Memory and CPU are severely constrained on mobile devices compared to regular PC hardware.


Apps don’t run in windows, they run on the full screen. So when you leave one app and switch to another in iPhone OS 4, the *GUI* — the visual interface — is not going to continue updating in the background. What will happen, if the app is updated to support the new OS 4 APIs (which, I expect, all actively-maintained apps will be), is that the app will stay in memory but stop processing. Switch back and it’ll start processing again, right where it left off. Think pause/resume, as opposed to the current iPhone OS model of quit/relaunch.


The VOIP and background audio processing examples do not involve the full app continuing to run in the background. The way these things work in iPhone OS 4 is, more or less, that the app registers with the system for what specific things it wants to do in the background. When the user leaves one app for another, the app that is being put into the background receives an event from the OS telling it that it is about to be paused, and at this point it has a chance to store its state, ask for time in the background to complete a task like a file upload, and register specific *threads* that will continue performing specific lightweight tasks like audio playback.


Take Pandora for example. When in the background, what will be running is a faceless (no UI) thread that just streams audio. Only when you re-activate Pandora — tap its icon to open the full app — will the entire app start running again.


When the system is running low on memory, it will automatically quit the least-recently used app that is paused in the background. Users should not notice this, except that when next they go back to such an app that has been reaped by the system to reclaim its memory, it might take a few moments longer for the app to be ready, and it will be like today, where the app itself will be responsible for restoring context. And, thus, apps still must be written in a way that assumes they might be shut down by the system with only a few moments notice.


The result is that switching between two or three recently used apps will feel very snappy. Users do not have to think about or even be aware of concepts like launching and quitting. Those are implementation details. They just have to think about opening, or perhaps better put, *going to* one app at a time that will take up the full screen. Sort of like how you *go to* a web site — you *go to* apps on the iPhone. And, now, for apps like Skype and Pandora, users can think about apps that can continue to *do stuff* (play audio, receive incoming VOIP calls) even when they’re not *open*.


There is nothing about the new iPhone OS 4 multitasking that a user must learn. They might just notice that “switching back” to recently used apps, via the same old home screen icons, is snappier. For the most part, using background-capable third-party apps will be just like using the background-capable system apps from Apple.


It’s an efficient, clever way of making switching more useful and quicker.


It’s also very much like the “multitasking” system Android has had in place all along.


My understanding of how multitasking works on Android is that it’s pretty much like what I described above for iPhone OS 4: GUIs do not continue to update (and consume CPU time) in the background, but apps stay in memory when you switch from one to another, until the system runs low on memory, at which point it starts automatically and silently quitting the least-recently used ones. Background Android apps can register faceless threads to “do stuff”, like play audio. I don’t think such background threads on Android are limited to specific things like audio playback and VOIP as they are on iPhone OS 4.0, but Android’s multitasking model is far more like what Apple just announced for iPhone OS 4 than it is to a traditional PC OS like Mac OS X or Windows.


One neat feature of Android is a listing in its Settings app that shows you where your battery life has been consumed since your last charge. In my use of a Nexus One, very little is consumed by apps in the background. Battery life on the Nexus One is consumed mostly by the display and by the wireless networking. I suspect that’s largely true for the iPhone from version 1-3, and will continue to be true with iPhone OS 4.


Like copy-and-paste, it was inevitable that Apple would add multitasking to iPhone OS eventually. Whether it was always planned for this year I do not know, but once Android became Apple enemy number one, multitasking became a must-have catch-up feature. Adding it now takes away the first item on the Android-vs.-iPhone talking points list. (And despite its similarities to Android’s model, Apple is, of course, pitching it as original and innovative.)


As for why the iPhone 3G and second-generation iPod Touch don’t get multitasking with iPhone OS 4, that’s easy — those machines only have 128 MB of RAM. The 3GS and third-generation Touch both have 256. (The 8 GB iPod Touch still being sold today is like the iPhone 3G — second-generation hardware. It will not get multitasking with iPhone OS 4.) “Paused” apps on iPhone OS 4 are still resident in memory, so there’s just no way it would work with only 128 MB total (some of which, remember, goes to the system itself). The CPUs in the 3GS and latest iPod Touch are faster too, and that’s a factor, but I believe RAM is the central reason.


## iAds and Google


Ever since the Apple-Google rivalry turned into a war, there’s been [increased speculation](http://www.businessinsider.com/70-chance-apple-builds-its-own-search-engine-in-the-next-five-years-2010-3) that Apple might [launch its own search engine](http://www.businessweek.com/magazine/content/10_04/b4164028483414_page_4.htm).


The thinking is simple. If Apple wants to go to war with Google, then they’ll be tempted to go after Google’s crown jewels — search. Search is still and may well always remain Google’s most popular service. But Google doesn’t make money from search. They make money from advertising. If you want to fuck with Google, you go after advertising revenue.3


Now, it’s true that much — most? — of Google’s ad revenue comes from ads that are displayed alongside search results. Google search generates a tremendous amount of ad revenue. But that’s last decade’s battle. It doesn’t make much sense for Apple to take on Google in search, given Google’s tremendous lead in the space and Apple’s utter lack of expertise in the field. It takes longer for Mac OS X’s Spotlight to search my MacBook Pro’s hard disk than for Google to search its index of the entire web.


The war for search is old. Where’s the next battlefield for advertising? Mobile devices is one guess — a guess shared [by Google](http://techcrunch.com/2009/11/09/google-acquires-admob/) and Apple. And here’s a field where Apple is ahead, not behind.


Again, just like with multitasking, the idea that Apple would build support  for advertising into iPhone OS is obvious, something that I suspect they might have pursued sooner or later even if Android did not exist. There’s a tremendous amount of money at stake.


Now that Android is considered the number one threat to the iPhone, though, mobile advertising became an immediate priority.


Jobs’s pitch for iAds during the event yesterday wasn’t even coy about it being a *fuck-you* to Google. He emphasized first the idea that on mobile, unlike the desktop, search is not a good venue for advertising. The idea being that on the iPhone, people aren’t searching, they’re using apps, and therefore the prime space for ads on mobile devices is right there inside apps. I’m not arguing whether Jobs is correct about search not being good for ads on mobile — I don’t know — but clearly, when he says “search”, he means “Google search”. So that’s knock one against Google.


Jobs then showed examples of iAds — rich, cinematic, interactive software ads. They look like native iPhone software, but they’re written in straight HTML5 (so it’s a bonus fuck-you, to Adobe). The word Jobs used repeatedly was *emotion*. They’re intended to be about design and feeling. It’s about a venue for advertising that can *feel* like good TV commercials and full-page magazine ads. That’s knock two against Google. Google ads may well be effective, but they are not emotional. Consider the *Toy Story 3* iAd Jobs demoed. What kind of ad through Google could compare to that?


There’s a solid slice of the DF audience that firmly believes that all advertising is contemptible bullshit. They’ve already skipped to the end of this article. Some advertising, no matter the medium — TV, newspaper, magazine — is junk. But some is art. Commercial art, of course, but art nonetheless. Online advertising — mobile or not — has been largely devoid of this caliber of advertising. iAds is Apple’s attempt to enable high-caliber ads for mobile. [Jobs seemed more enthusiastic about iAds](http://lonelysandwich.com/post/508907690/steve-smiles) than anything else in the show yesterday.


So the anti-Google message with iAds was two-fold: first, search isn’t good for mobile ads; and second, Google — logical, engineering-driven Google — will never provide an ad platform for emotional advertising like design-driven Apple can. Jobs’s iAds pitch was not directed to consumers. It was directed to creatives in the ad industry — and creative developers who want something better than text ads inside their apps.


## Miscellany

- I detected one other veiled insult against Google during the event — Jobs’s emphasis during the multitasking segment about how seriously Apple values the privacy of iPhone users, with regard to data and location information. In the way that the standard knock against Apple is that they maintain too much control over the App Store, the standard knock against Google is that they don’t value user privacy. Jobs’s message: *You can trust Apple.*
- At the outset Jobs claimed Apple has sold 50 million iPhones to date and 35 million iPod Touches. They don’t reveal updates to those numbers all that often.
- Game Center is not about Google, since Google doesn’t have a gaming social network. (Yet?) But it sure seems like a shot against Facebook. Want to play Scrabble or compare your scores against your friends? Game Center aims to supplant Facebook for that sort of thing.
- iBooks for iPhone is not surprising. (At the press event for the iPad debut in January, someone asked Phil Schiller whether there’d be an iBooks app for the iPhone, and he paused, smiled real big, and said something like “That’s an interesting idea.”) Just like with the Kindle, metadata for bookmarks and your current page sync wirelessly between iBooks on different client devices. [If only the iPad’s iWork apps had this sort of wireless syncing.](http://www.macobserver.com/tmo/article/file_sharing_with_an_ipad_ugh/) Next question: where’s the Mac client? Or will they build it into iTunes for the Mac and Windows?


---

1. Shipping the iPad, of course, was a major priority, but like any new project at Apple, it was shipped by a team working in secret. Most of the company found out the details of the iPad when the rest of us did, and that’s why the iPad won’t get an iPhone OS 4 update until version 4.1 later this year — the plans for 4.0 were set and long in development before the iPad was revealed. ↩︎
2. “Tentpole” is Apple company lingo for major features in a product that can be promoted to customers. I hear it frequently from friends at the company, but can’t recall it being used in a keynote address before. ↩︎
3. If Microsoft still had the set of balls it had in the 90s, Internet Explorer would have been updated years ago to block web ads by default, including those from Google. ↩︎



| **Previous:** | [Why Apple Changed Section 3.3.1](https://daringfireball.net/2010/04/why_apple_changed_section_331) |
| **Next:** | [A Brief Review of Opera Mini for iPhone](https://daringfireball.net/2010/04/opera_mini_review) |


PreviousNext