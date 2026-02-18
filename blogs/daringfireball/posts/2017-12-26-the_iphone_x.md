---
title: "The iPhone X"
date: 2017-12-26
url: https://daringfireball.net/2017/12/the_iphone_x
slug: the_iphone_x
word_count: 4624
---


The more popular a computer platform becomes, the more of a bind in which it inevitably finds itself. A platform is only “finished” when it is abandoned. It needs to evolve to remain relevant, but it’s difficult to change in unfamiliar ways without angering the base of active users. Adding new features on top of the familiar foundation only gets you so far — eventually things grow too complex, especially when what’s needed now is in conflict with a design decision that made sense a decade (or more) prior.


Eventually, inevitably, incremental improvements paint a platform into a corner. Something has to give.


This happened to the classic Mac OS in the mid-90s, when certain technical constraints of the OS made the platform seem anachronistic. The classic Mac OS had no protected memory and used cooperative, rather than preemptive, multitasking. No protected memory meant that every process on the system could read and write anywhere in RAM — both the memory of other processes and the memory of the OS itself. Cooperative multitasking meant that each app decided when to give up the CPU to other processes. If an app wanted to use the entire CPU, it could. In a sense, from today’s perspective, the original Mac was effectively just one process, and apps were more akin to plugins running within that process. In 1984, these were utterly reasonable design decisions. Protected memory, pre-emptive multitasking, and a powerful OS kernel just weren’t feasible on a computer with an 8 Mhz CPU and 128 kilobytes (*kilobytes*!) of RAM. In fact, there was no multitasking at all on the original Mac until Andy Hertzfeld released [Switcher](https://www.folklore.org/StoryView.py?project=Macintosh&story=Switcher.txt) in April 1985 — the forerunner of [MultiFinder](https://en.wikipedia.org/wiki/MultiFinder).1


The problem mid-90s Apple faced is that the Mac was popular because of its thriving library of excellent third-party software, but in trouble because of the creakiness of its underlying OS. But Apple couldn’t truly modernize the OS without breaking the application software — which is exactly what happened with Mac OS X. Old software ran in a virtual [“Classic” environment](https://arstechnica.com/gadgets/2001/04/macos-x/13/) — essentially, a virtualized version of the old classic Mac OS running within the modern Mac OS X. New software — apps that took advantage of Mac OS X’s modern APIs, new features, and new look-and-feel — needed to be written using different (Cocoa) or updated (Carbon) APIs. The transition worked, as evidenced by the Mac’s continued success today, but it took years — arguably close to a decade. And it was a painful, jarring transition for everyone involved: users, developers, and Apple itself.


---


With the iPhone X, Apple is attempting something I believe to be unprecedented — a complete ground-up rethinking of a fabulously popular and successful platform, *without* a disruptive, painful transition.


There are several parallels between the original 2007 iPhone and the original 1984 Macintosh. Both introduced new fundamental paradigms that quickly became the standards on competing platforms — the GUI in 1984, multitouch in 2007. Both were created by relatively small teams, led by Steve Jobs. But the biggest similarity — or at least the one most salient to this discussion — is that both were burdened at the outset by severe technical limitations. An 8 Mhz CPU, 128 KB of RAM, and 400 KB floppy disks (the original Mac’s only form of storage) were not enough. Likewise, the original iPhone’s CPU, 128 MB of RAM, and EDGE-based cellular networking were not enough. That both products succeeded — and became downright beloved, despite their technical limits — is testimony to the genius and talent of the designers and engineers who brought them to life.


There is a fundamental difference: the barrier the iPhone ran up against a decade into life wasn’t technical (as with the aforementioned architectural shortcomings of the classic Mac OS2), but rather conceptual. Here are some of the landmark changes to the iPhone as a platform over its decade of existence:

- iPhone 4 (2010): Retina display.
- iPhone 5 (2012): Aspect ratio changes from 3:2 to 16:9.
- iPhone 5S (2013): Touch ID.
- iOS 7 (2013): Cosmetic reboot of user interface.
- iPhone 6 and 6 Plus (2014): Larger screens.


Ultimately these were all evolutions of the original iPhone, though. There is a clear evolutionary path from 2007’s original iPhone to 2017’s iPad Pro and iPhone 8 models. The home button gained a superpower with the iPhone 5S — the ability to authenticate your identity by fingerprint — but only *in addition to* everything it did before. There were always two things and only two things on the front face of an iOS device — the touchscreen display and the home button. In fact, the iPhone X changes iOS in more fundamental ways than even the iPad did. In terms of the role between the display and the home button, the iPad really was — and remains today — “just a big iPhone”.


The iPhone X, however, creates a schism, akin to a reboot of the franchise.


Apple hasn’t called attention to this, but effectively there are two versions of iOS 11 — I’ll call them “iOS 11 X”, which runs only on iPhone X, and “iOS 11 Classic”, which runs on everything else.


The fundamental premise of iOS Classic is that a running app gets the entire display, and the home button is how you interact with the system to get out of the current app and into another. Before Touch ID, the home button was even labeled with a generic empty “app” icon, an iconographic touch of brilliance.3


Over time, the home button’s responsibilities grew to encompass these essential roles:

- Single-click with display off: wakes the device.
- Single-click with display on: takes you to home screen.
- Double-click: takes you to multitasking switcher.
- Triple-click: configurable accessibility shortcut.
- Rest finger: authenticate with Touch ID.
- Double-tap (without clicking): invoke Reachability.
- Press-and-hold: invoke Siri.


In iOS 11 X, almost every role of the home button has been subsumed by the display, with the remainder reassigned to the side button:

- Wake the device: tap the display.
- Go to the home screen: short swipe up from the bottom of display.
- Go to the multitasking switcher: longer swipe up from the bottom.
- Even better way to multitask: just swipe sideways on the home indicator.
- Accessibility shortcut: triple-click the side button.
- Authenticate: just look at the display.
- Reachability: swipe down on the bottom edge of display.
- Siri: press-and-hold side button.


The first few days using an iPhone X were rocky for me. My thumb kept reaching for the home button that wasn’t there, particularly for multitasking. After a week, it started feeling normal. Today, on the cusp of two months of use, I’m like “*What’s a home button?*” In fact, my acclimation to the iPhone X has made using an iPad feel anachronistic — I want to swipe up from the bottom to go home there too.


In short, with the iPhone X Apple took a platform with two primary means of interacting with the apps — a touchscreen and a home button — removed one of them, and created a better, more integrated, more organic experience.


One of the things Apple created to enable this has gotten a lot of attention: Face ID. But a few of the other things they’ve done to enable this have gone largely under the radar. Tapping anywhere on the display to wake it is so natural, it makes me wonder how we did without it for so long. (This is another frustration I have trying to use an iPad now — I tap the screen expecting it to wake up. It seems silly that I need to press a button.) The iPhone X display does not, alas, offer [the ProMotion feature](https://www.apple.com/newsroom/2017/06/ipad-pro-10-5-and-12-9-inch-models-introduces-worlds-most-advanced-display-breakthrough-performance/) introduced with the latest iPad Pros, which allows for dynamic screen refresh rates of up to 120 Hz. But it does track touch input at 120 Hz, double the rate of all other iPhones. The result of this is that the animations for gestures track your finger better. It feels less like an animation that is playing in response to your touch and more like your finger is actually manipulating and moving things on screen as though they are real objects. Of the numerous new technologies embedded in the iPhone X, the 120 Hz refresh rate for touch tracking is almost certainly the least important, but it really does contribute to making gestures feel like the one true way to interact with the system.


Tapping the display to wake the device, seeing a list of truncated notifications on the lock screen, and then seeing those notifications expand to preview their content once you’re recognized by Face ID — this just makes the iPhone X feel *alive* in a way that no other device does. You tap it to get its attention, and it recognizes that you are you.


The lock screen is far more useful now: you can just tap any notification to jump to it. With Touch ID, after you tap a particular notification in the middle of the display, you then must move your finger down to the home button to authenticate. I always found that annoying. Now that I’m used to the iPhone X, I find it to be intolerable.


Face ID is not a win versus Touch ID in every single way. There are trade-offs, primarily scenarios where Face ID fails. (It does seem to work with most sunglasses, for example, but not with Ray Bans, which, alas, happen to be my preferred brand.)


Consider the aforementioned process of opening a notification from the lock screen. Touch ID adds an extra step, every time, *even when it works perfectly*. Face ID is not perfect — it’s true that I wind up either authenticating a second time or resorting to entering my PIN more often than with Touch ID — but it only adds these extra steps *when it fails for some reason*. When it works perfectly, which for me is the vast majority of the time, the effect is sublime. It really does feel like my iPhone has no passcode protecting it. That was never true for Touch ID. Touch ID feels like a better way to unlock your device. Face ID feels like your device isn’t even locked.


This was the way the iPhone was meant to be used. When Steve Jobs demoed the original iPhone on stage at Macworld Expo in January 2007, it was just “slide to unlock”. There was no PIN. One of the ways the world has changed in the last decade is that we’re no longer naive about device security. I’m pretty sure I used my iPhones with no PIN code for a few years. Slide to unlock was fun. Entering a PIN is no fun.


Thanks to Face ID, no-PIN “slide to unlock” is back. This, to me, epitomizes the iPhone X. In ways small and large, it changes fundamental aspects of using an iPhone. But it does so in ways that are faithful to the spirit of the original iPhone.


---


It’s the big picture that interests me most about the iPhone X. Not this device, in particular, with this particular display (which is terrific), this particular camera system (which is terrific), etc. — but the ways it changes fundamental aspects of the platform, laying the groundwork for the next decade of iterative year-over-year improvements. But some particular details of this device are worth calling attention to:

- Apple Pay moving to Face ID has been a win for me. You now trigger it by double-clicking the side button. One of the things I find interesting about this change is that while it breaks from how Apple Pay works on other iPhones, it is consistent with how you invoke Apple Pay on Apple Watch. Same thing with being able to tap the display to wake it up — it’s now the same as on Apple Watch.
- The camera bump is bigger and more prominent than on any other iPhone, but somehow, to me, that makes it less objectionable. It’s a thing now. Whereas the first bumps, on the iPhone 6 and 6 Plus, were like blemishes. If you’re going to have a bump, have a fucking bump. I also like that the sides of the iPhone X camera bump are perpendicular to the back of the phone, not sloped. It looks less like a mere lens on the back of the phone and more like a *whole camera* on the back of the phone.
- After a few weeks, I became annoyed by the home indicator. Making it completely white or black is perhaps a good idea for new users, to make the affordance as visually prominent as possible. But once you get used to it, its extreme visual prominence gets in the way. I wish that it were more subtle, probably translucent. I expect the home indicator to become more subtle in future versions of iOS.4
- When an alarm from the built-in Clock app fires, it fades out in volume as soon as you look at the display. This is utterly charming.
- The hardware mute switch remains. If ever there were a time when Apple might get rid of it, iPhone X would have been it. That it remains on iPhone X suggests to me that Apple sees it as here to stay, at least for the foreseeable future. If, like me, you love the mute switch, you might be thinking “*Well of course they kept the mute switch, it would be terrible if they got rid of it.*” But they removed it from the iPad a few years ago, and Apple is famously averse to physical buttons (cf. the Touch Bar on the new MacBook Pros). And for reasons I’ve never been able to understand, Android handset makers seem willing to copy everything and anything from Apple they can get away with (and even things [they can’t get away with](https://en.wikipedia.org/wiki/Apple_Inc._v._Samsung_Electronics_Co.)), but [almost](http://www.techradar.com/news/oneplus-5-android-mute-button-feature) none have copied the iPhone’s mute switch, despite the fact that it’s extremely useful.
- Stainless steel looks and feels so much more luxurious than aluminum. The iPhone X doesn’t feel bigger than an iPhone 7 or 8 in my hand or pocket, but it does feel *heavier* and more serious.
- True Tone epitomizes the sort of feature that you stop noticing on the devices that have it, but which ruins you for devices that don’t. Retina resolution was like this, too. Since switching to the iPhone X, I’ve gone entire weeks without once thinking about True Tone at all. But if I pick up or glance at an iPhone without it, I’m skeeved out.
- One of the best ways to judge iPhone X after using it for a few weeks is to go back to an iPhone 7 (or any other previous iPhone). Things I notice instantly: the display looks very small, the colors look too cool at night (because of the aforementioned lack of True Tone), and the perfectly square corners of the display seem downright crude. The round display corners seemed like something that might feel gimmicky, but in practice, they feel organic and refined. As a wise man once pointed out, [rectangles with round corners are everywhere](https://www.folklore.org/StoryView.py?story=Round_Rects_Are_Everywhere.txt). As with True Tone, I stopped noticing the round corners on the iPhone X, but started noticing and being annoyed by the square corners on other iOS devices.
- I don’t notice the notch when using the phone in portrait orientation, and I only hold the phone in landscape when watching video, using the camera, or playing a game. And I don’t play many games. But Apple really should hide the notch in landscape (which, in fact, they do for the Camera app). Last week I was playing [Desert Golfing](https://kotaku.com/f-k-you-desert-golfing-aka-the-worst-best-game-in-th-1633266512)5 — a game that’s been updated to embrace the notch — and on one hole my ball went to the edge of the display and was hidden by the notch. I “fixed” it by rotating the phone 180 degrees to put the notch on the other side, but that’s ridiculous.
- The chins and foreheads on other iPhones now stick out to me far more than the notch on the X. They just scream “*Wasted space!*” to me.
- On the iPhone X, iOS 11 now uses small colored pill-shaped indicators in the top left “ear” when the phone is hosting an active hotspot session (blue), there’s an active mapping navigation session (blue), there’s a phone call in the background (green), or the screen is being recorded (red). With iOS Classic, these indicators use the same colors, but they take up the entirety of the status bar. The old design for these indicators gave them too much visual prominence, and completely prevented you from tapping the status bar to scroll the current view to the top. It never made any sense that you couldn’t use the scroll-to-top shortcut just because one of these indicators was active — every time I ran into that, it would occur to me that it was a clumsy design. On iPhone X these indicators finally feel like they have a proper home.
- The new status bar no longer has room for the numeric battery percentage. You can see the numeric percentage in Control Center, and on the lock screen while the device is charging, but there is no option for an always-on numeric battery percentage. I’ve never been a fan of the numeric battery percentage — to me, all it does is induce anxiety. The approximation of remaining battery life gleanable from the icon is all you need most of the time, I say. But, [some people disagree](https://www.wsj.com/articles/iphone-x-review-yes-there-are-reasons-to-pay-apple-1-000-1509724800). If this remains controversial, Apple should consider letting people choose between the icon and the numeric percentage.
- The new status bar design also gets the name of your carrier off the screen most of the time. (It’s still visible from the lock screen and from Control Center.) The carrier string in the status bar has always irritated me — it’s like they were getting an ad on my screen, even though I’m the one paying them.
- The glass back of the iPhone X does not pick up scratches or “[micro-abrasions](https://daringfireball.net/search/micro+abrasions)” like the jet black iPhone 7 does. I see two small, very fine micro-abrasions on mine (a space gray model), which I’ve been using for well over a month without any sort of case. My wife’s (a white model) has a few too. You have to look hard to see them, though.
- I still think iPhone X is too big to be the smallest iPhone. The device doesn’t feel too big in hand or pocket. As someone who has carried a 4.7-inch iPhone ever since the iPhone 6 three years ago, the iPhone X really does feel the same size, as a device. But the extra screen size from the edge-to-edge display [puts a serious crimp in one-handed reachability](https://twitter.com/sdw/status/940371524128727040?s=17). In addition to an even bigger Plus-sized version of iPhone X next year, I would love to see Apple introduce a smaller iPhone SE-sized phone with all the same features and design elements. I’m not holding my breath, but I’d love to see it. I’m not even saying I personally would prefer it (but I’d give it a try) — but it would be great for people who value one-handed reachability.
- Is the higher price of the iPhone X over the iPhones 8 justified? The 64 and 256 GB iPhone X models cost $999 and $1149, respectively. That’s $300 more than the equivalent iPhone 8, and $200 more than an iPhone 8 Plus. For that premium, you get a better camera, stainless steel (rather than aluminum) frame, an edge-to-edge OLED display with True Tone, and Face ID. But you also get something you can’t compare in [a checkmark comparison](https://www.apple.com/iphone/compare/) — a sort of *joie de vivre*. Critics of the iPhone X’s higher prices seem to me to be arguing not that *this* phone shouldn’t cost so much, but rather that *no* phone should. [As I argued earlier this year](https://daringfireball.net/2017/07/speculation_on_new_iphone_pricing), if we have laptops and tablets that cost more than $1000, why not phones too? Especially considering that for many, the phone is the most-used, most-important device in either or both their personal and professional lives.


---


I don’t recall a single review of the iPhones 8 that didn’t mention the much-more-highly-anticipated iPhone X (including [my own review](https://daringfireball.net/2017/09/the_iphones_8)). But you can’t understand iPhone X without mentioning iPhone 8, either. A few months after the iPad debuted in 2010, I wrote — trying to assuage the fears of those who saw the iPad as the end of the Mac — [that the heaviness of the Mac allows iOS to remain conceptually light](https://daringfireball.net/2010/12/future_of_the_mac_in_an_ios_world). In a similar vein, the familiarity of iPhone 8 allows iPhone X to reinvent anything, to break the platform’s foundational conventions.


No one is being forced to adapt to the changes of iPhone X. If you want a new iPhone that is familiar, you can get an iPhone 8 or 8 Plus with the same A11 “Bionic” system on a chip, a camera that is *almost* as good, a display that is *almost* as good, the tried and true Touch ID, and even new (to the iPhone platform) features like inductive charging — and you’ll save a few hundred dollars.


In the short term this fork in the platform is a hit to consistency. Unlocking the phone, going to the home screen, switching between apps, authenticating via biometrics, invoking Siri, taking screenshots, powering down the device — all of these tasks are accomplished in completely different ways on the iPhone X than any other iPhone to date, including the iPhones 8.


It’s unique in Apple history — if not all of consumer computing history — for the same version of the OS to present two distinct interfaces that are so markedly different, based solely on which hardware the OS is running. From a developer standpoint, iOS 11 is one OS with various different sizes (SE, regular, Plus, X, iPad, iPad Pro) and layouts. From a user perspective, though, the “OS” is how you interact with the system. Again, it’s as though there are two very different versions of iOS 11 — and I can’t stop thinking about how weird that is.


It’s nowhere near as different switching from an older iPhone to an iPhone X as it is switching from an iPhone to any Android device, for example. But it is different, at a fundamental level.


Why not bring more of what’s different on iPhone X to the other iPhones running iOS 11? iPhone X needs these gestures because it doesn’t have a home button. Classic iPhones *could* have supported them though — there’s no reason Apple couldn’t have added the swipe-up-from-bottom-to-go-home gesture to all iOS devices. And they could have then moved Control Center to a swipe down from the top right corner on all devices, too. I think they didn’t because they wanted a clean break, a clear division between the old and the new, the familiar and the novel.


And some aspects of the iPhone X experience wouldn’t work on older devices. You could in theory swipe up from the bottom to go home on a non-X iPhone, but you couldn’t swipe-up-from-the-bottom to unlock the lock screen, because that requires Face ID. Conversely, there is no room in the iPhone X experience for Touch ID. There is no “rest your finger here” in the experience. It wouldn’t matter if the fingerprint scanner were at the bottom of the display or on the back of the device — it would be incongruous.


What we’re left with, though, is truly a unique situation. Apple is attempting to move away from iOS’s historical interface one device at a time. Just the iPhone X this year. Maybe a few iPhone models next year. iPad Pros soon, too?6 But next thing you know, all new iOS devices will be using this, and within a few years after that, most iPhones in active use will be using it — without ever once having a single dramatic (or if you prefer, *traumatic*) platform-wide change.


The iPhone X is not the work of an overcautious company. It’s a risk to so fundamentally change the most profitable platform in the world. But Apple is gambling on the taste of the team who lived with the iPhone X during its development. Ossification is a risk with a platform as popular and successful as the iPhone — fear of making unpopular changes can lead a platform vendor to make no significant changes. Another risk, though, is hubris — making changes just for the sake of making changes that show off how clever the folks at Apple still are.


After two months using an iPhone X, I’m convinced Apple succeeded. The iPhone X is a triumph, a delightful conceptual modernization of a ten-year-old platform that, prior to using the iPhone X, I didn’t think needed a modernization. Almost nothing7 about the iPhone X calls undue attention to its cleverness. It all just seems like the new normal, and it’s a lot of fun.


---

1. How multitasking came to be on the original Mac [is a great story](https://www.folklore.org/StoryView.py?project=Macintosh&story=Switcher.txt). Long story short, Andy Hertzfeld single-handedly created Switcher while on a leave of absence from Apple. It just goes to show how insanely primitive the original Mac OS was that something like multitasking — even if it was, technically, more like the illusion of multitasking — could be added by a third-party system extension. ↩︎
2. Dating back to the NeXT era, Apple’s OS and API framework teams have proven themselves to be really good at building systems that, in their early days, push the limits of what is technically possible on the era’s hardware, but do so in ways that lay a solid foundation that scales for decades to come. It’s really quite remarkable the original 2007 iPhone’s OS and framework underpinnings could be traced back directly to a 1989 Unix workstation system. The same system now runs on wristwatches. ↩︎︎
3. I find it hard to consider a world where that button was marked by an icon that looked like a house (the overwhelmingly common choice for a “home” icon) or printed with the word “**HOME**” (the way iPods [had a “**MENU**” button](https://duckduckgo.com/?q=ipod+menu+button&t=hg&ia=images)). Early iPhone prototypes did, in fact, [have a “**MENU**” label on the button](https://www.cultofmac.com/488008/jony-ive-book-excerpt-iphone/).
I truly consider the iPhone home button icon the single best icon ever. It perfectly represented anything and everything apps could be — it was iconic in every sense of the word. ↩︎︎
4. [Apple added a similar indicator under the cellular/Wi-Fi/battery icons in iOS 11.2](https://www.macrumors.com/2017/12/02/apple-releases-ios-11-2/), as an affordance to suggest where you go to invoke Control Center. Rather than solid black or white, though, it is translucent. This is exactly what I’d like to see Apple do with the home indicator. ↩︎︎
5. My score to date: 4,134 strokes through 1,575 holes. ↩︎︎
6. As for how the iPhone X-style Face ID/no-home-button experience will work on iPad, it’s unclear to me whether Apple has already thought this all the way through. Why, for example, did Apple just this year introduce a new small-swipe-up-from-the-bottom gesture for the iPad to show the new Dock, when the iPhone X suggests that a small swipe up from the bottom is the future of getting back to the home screen? ↩︎︎
7. The way Apple wants software to handle the notch, in landscape orientation, is the one exception that springs to mind. ↩︎︎



| **Previous:** | [Marzipan](https://daringfireball.net/2017/12/marzipan) |
| **Next:** | [Apple Responds to Controversy on iPhone Batteries and Performance](https://daringfireball.net/2017/12/apple_iphone_batteries) |


PreviousNext