---
title: "The iPhones 14 Pro (and iPhones 14)"
date: 2022-09-15
url: https://daringfireball.net/2022/09/the_iphones_14_pro
slug: the_iphones_14_pro
word_count: 6624
---


There are two super interesting innovations with the iPhone 14 Pro and Pro Max. There aren’t any interesting innovations with the iPhone 14 or 14 Plus — which fact itself is actually pretty interesting, strategically.


## The Dynamic Island


The first super interesting thing about the iPhone 14 Pro models is the most obvious. It’s the feature Apple is highlighting, including putting its name on a title card, [in TV commercials](https://www.youtube.com/watch?v=WuEH265pUy4) that began running last week. It’s the feature every other major phone maker has, I’ll bet, already assigned teams to rip off.


The best ideas in any creative field often follow a counterintuitive pattern. The ideas are, in fact, original, highly innovative, and spring from very creative minds. But if well-executed — [always a big “if”](https://sive.rs/multiply) — once experienced, they seem incredibly obvious. The Dynamic Island is one of those ideas. Not only does the Dynamic Island now strike me as *the* obvious answer to what should be done with a sensor array cutout in a phone display,1 it’s so cool, so fun, so useful that it feels like an obvious reason why you should have a sensor array cutout in a phone display in the first place. When the iPhone X introduced the notch, there were a lot of people who thought Apple should have [hidden it](https://apps.apple.com/us/app/notcho/id1294836169) by drawing a black notch-height border across the top of the display. Only a fool would argue that the Dynamic Island would be better off hidden like that.


The Dynamic Island feels like a user interface element that deserves to be there, almost exactly as it looks, *even if there were no front-facing sensor cutouts*. It’s not merely some clever idea to do *something* useful with the cutout space, it’s an incredibly clever idea for a permanent on-screen UI for live activities, status, certain notifications, and small interactions. The fact that it completely and elegantly disguises the sensor cutout array is just the icing on the cake. It’s like watching [expert sleight-of-hand magicians vanish an object](https://www.youtube.com/watch?v=i0m8CC7Ovj8). The fact that you know you’re being fooled makes it even more fun. Dynamic Island is a genius idea and Apple has knocked the initial implementation out of the park.


I’ve been using an iPhone 14 Pro (space black) since last Thursday. One week in and I’m hooked. I have a regular iPhone 14 to test too, and I’m doing side-by-side comparisons with my year-old iPhone 13 Pro, but those phones feel outdated. Inert. Less fun and less useful. The Dynamic Island is that good.


I was walking around in Manhattan yesterday using turn-by-turn directions in Apple Maps and listening to a podcast in [Overcast](https://overcast.fm/) and I was keeping track of both, at the same time, while texting in Messages. The interactions are so lightweight it doesn’t feel like multitasking in a traditional sense because it doesn’t feel like you’re doing any context switching. Apple Maps, of course, has been updated to fully support Dynamic Island-specific APIs. Overcast, of course, has not (yet). But because Overcast uses Apple’s existing NowPlaying APIs, and Apple has connected those NowPlaying APIs to the Dynamic Island, Overcast — as well as any other third-party apps that support NowPlaying (just about every major audio playback app) or CallKit (e.g. Skype, WhatsApp, and Google Voice) — get very credible Dynamic Island support for “free”, right now, including audio waveforms. Long-press on Overcast’s minimal view in the Dynamic Island and, with a bit of haptic feedback, it morphs with a delightfully organic animation into an expanded view with playback controls, larger album art, etc. Everything you get in the Lock Screen widget-like view. This expanded view can be used creatively by developers. As suggested last week in Apple’s keynote, a sports app using Live Activities to show the score of a game could use the expanded view to show rich details about the current state of the game. Who’s on base in the Yankees game? How close to another three-and-out punt are the Dallas Cowboys?


These expanded views are like little versions of the apps that just live up there in the Dynamic Island. The Music app on MacOS — née iTunes — has had a miniplayer window right from the start. [Here’s Steve Jobs demoing it](https://www.youtube.com/watch?app=desktop&v=qL6QfvFu8fM&t=254) — “Boom”. In Music’s preferences, you can set the miniplayer to float atop all other windows on your desktop, so you can see it and use it even when using other applications. It’s a very new experience on iOS but instantly feels natural and completely unobtrusive.


There are a lot of different ways Apple could have gone with the basic idea of the Dynamic Island. They could have enabled a lot more functionality — made it more like vertical split-screen multitasking. But instead of increasing complexity system-wide, the Dynamic Island increases *simplicity*. It’s a major new feature but it *reduces* the cognitive load of using or checking the status of more than one app at a time. “Useful new feature” always sounds good, but new features generally increase complexity. The Dynamic Island is that rare gem that reduces complexity while adding utility.


Here’s a nice touch: When you start playing audio in an app, or initiate a phone or VoIP call, and you swipe up from the bottom of the screen to go to the home screen, the app you’re leaving doesn’t minimize into its home screen icon like it usually would. Instead, the app minimizes *into* the Dynamic Island, and the Dynamic Island sort of *absorbs* the app in a very organic animation. The Dynamic Island feels not merely like a shape or dedicated area at the top of the screen, but like a real *thing* with personality.2 I have genuine affection for it already.


## Live Activities Without the Dynamic Island


As a postscript related to the Dynamic Island, there’s a fascinating and important question that, as I publish this, I’m not sure we know the answer to. To wit: how are all these [Live Activity features](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) going to work with notched iPhones, including the brand-new iPhone 14 and 14 Plus? Apple is not going to turn the notch into a Dynamic Peninsula. But so where are things like live sports scores or updates on the arrival time for your hailed Uber or Lyft going to be displayed on iPhones other than the 14 Pro models? The answer seems to be that for iPhones without the Dynamic Island — which is to say every iPhone other than the 14 Pro models — [Live Activities will only be viewable on the Lock Screen](https://www.macrumors.com/2022/09/14/apple-live-activities-ios-16-1/), or when the app responsible for them sends an update. Without the Dynamic Island, there’s no way for the *user* to invoke a Live Activity except by pulling down from the top left of the screen to go to the Lock Screen. Here’s what Apple’s [developer documentation](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) currently states:


> Live Activities come in different views for the Lock Screen and
> the Dynamic Island. The Lock Screen view appears on all devices.
> Devices that support the Dynamic Island display Live Activities
> using the following views: a compact leading view, a compact
> trailing view, a minimal view, and an expanded view for the
> Dynamic Island.
> The expanded view appears when a person touches and holds a
> compact or minimal view in the Dynamic Island and when a Live
> Activity updates. On an unlocked device that doesn’t support the
> Dynamic Island, the expanded view appears as a banner for Live
> Activity updates.
> To make sure the system can display your Live Activity in each
> position, you must support all views.


This means that Dynamic Island isn’t just a cooler-looking presentation of a feature on other iPhones. It’s an entire incredibly useful interaction model *and* set of features that are exclusive to the iPhone 14 Pro and Pro Max. If this remains the case, I’d say that the Dynamic Island alone is a reason to upgrade to a 14 Pro, and a reason not to even consider buying the 14 or 14 Plus. Would I pay $200 — the price delta between the same-sized Pro and regular iPhone 14 models — just to get the Dynamic Island? Yes.


## Always-On Display


The second super interesting thing about the iPhones 14 Pro is the always-on display. *It is really weird.* Not weird because it’s a bad idea, but weird because battery life has always been, and remains, a precious resource to be conserved on smartphones. And, until now, one of the surest ways to run down your battery has been to leave your phone in an unattended state while the display remains on. When you look over to your side at your desk, where your iPhone rests face up, and the screen is *on* despite your knowing that you haven’t touched it in a while, it feels wrong. Like there’s a bug in iOS that’s preventing the screen from going to sleep or something. Over and over and over this past week, I’ve glanced at this iPhone 14 Pro in the always-on state, and I experienced a micro jolt of panic: *Whoa, why is the screen on? Oh, yeah, always-on...*.


The first thing I’ll emphasize is that always-on mode is pretty darn bright, and it is full color. If you use a colorful Lock Screen wallpaper, you’ll be looking at a colorful always-on display. It’s bright enough that you could use the phone without much concern even if the always-on state were the brightest the display ever got. You can see it clearly in bright sunlight. There have been Android phones with always-on displays for years, but many of them — when locked — are just black screens with dim white text for the time and date. On those phones, the always-on state is very distinctive from the actually-on state. On iPhone 14 Pro, at a glance, the always-on state looks like the actually-on state.


The always-on display I’m most familiar with is on Apple Watch, which added the feature three years ago [with the Series 5 models](https://daringfireball.net/2019/09/apple_watch_series_5). As a lifelong watch wearer, gaining an always-on display never seemed weird for Apple Watch. What seemed weird to me were the first four generations that *didn’t* offer it. (I spent a lot of words in [my review of the original Apple Watch](https://daringfireball.net/2015/04/the_apple_watch) complaining about the not-always-on display.) I did not expect an always-on display for iPhone to be hard to grow accustomed to, but for me, so far, it has been.


In a way, the always-on display mode for iPhone 14 Pro is the opposite of the Dynamic Island. The Dynamic Island I took to immediately — a *where’ve you been all my life?* feature. The always-on display is still startling me every time I glance at it. I suspect I will get used to it, but if I still feel so unsettled by it a few weeks from now, I might try turning it off and seeing if I miss it. Because the other difference from the Dynamic Island is that I’m still not sure what purpose it serves. (The answer, I suspect, is Live Activities, which aren’t shipping until iOS 16.1. Being able to see updates to a Live Activity on an always-on display sounds potentially useful.)


Technically, the always-on display is impressive. I don’t know what kind of difference in battery life it makes by disabling it, because I’ve just left it on, as it is by default, for the week I’ve been using this phone. While testing new iPhones, I tend to use them far more than I do in day-to-day life. I’m shooting more photos, taking more videos, and running battery-sucking tasks like benchmarks that I seldom run during the other 51 weeks of the year. It’s hard to test and examine a new phone for a week while simultaneously gauging typical-day, typical-use battery life. That said, I’ve been getting the general battery life I’d expect from a new iPhone that *didn’t* have an always-on display. I don’t know if that perception is going to hold up in the long run, with my actual day-to-day usage, but at the moment, battery life is not a factor in my ambivalence toward the feature.


## Camera System


Onward to the interesting, but not super interesting, aspects of the iPhone 14 Pro. It’s another solid year of camera improvements for the 14 Pro models. A nomenclatural change from Apple that I fully endorse is that they’re now calling the 1× camera the “main camera” instead of the “wide camera”. Calling 1× “wide” and 0.5× “ultra wide” broke my brain. The 1× camera is what most people use most of the time, and what some people use almost all the time. It *is* the main camera.


This year’s main camera is unlike any previous iPhone camera. Instead of a 12 MP sensor, its sensor is 48 MP. But unless you’re shooting RAW,3 it produces 12 MP photos. In 1× mode, the main camera is [binning](https://www.cnet.com/tech/mobile/samsung-s21-ultra-pixel-binning-adapts-photos-for-detail-or-the-dark/) those 48 megapixels to increase image quality by treating each 2 × 2 square of 4 actual pixels as a single virtual pixel to produce 12 MP images. And the main camera now offers, in addition to 1×, a 2× focal length. Because it’s a 48 MP sensor, the main camera doesn’t need to upscale (a.k.a. “digital zoom”) from a 1× original to produce 2× output. Instead, 2× just uses a crop of the sensor’s center 12 megapixels — without binning — to produce an optical 12 MP image. It’s two focal lengths from one camera and lens.


I did not have time over the past week to create a deep investigation into the iPhone 14 Pro’s image and video quality. But from what I’ve seen so far, 2× mode looks great. It should produce higher quality output than the dedicated 2× camera on, say, the iPhone 12 Pro — particularly in low light — and so far, I think it does.

Markdown Table
| iPhone 14 Pro | 35mm Equivalent |
| :-----------: | :-------------: |
| 0.5×          | 13mm            |
| 1×            | 24mm            |
| 2×            | 48mm            |
| 3×            | 77mm            |


| iPhone 14 Pro | 35mm Equivalent |
| 0.5× | 13mm |
| 1× | 24mm |
| 2× | 48mm |
| 3× | 77mm |



Having spent the last year with an iPhone 13 Pro — equipped with 0.5×, 1×, and 3×  cameras — I’m delighted to have 2× back as an optical focal length. In day-to-day usage, I’ve found 3× to be an awkward focal length — too zoomed-in for most of the scenes and portraits I’ve wanted to shoot, but not long enough for situations where I’d want a telephoto lens with a *lot* of throw. 2× iPhone lenses have always been roughly equivalent to 50mm lenses in traditional photography, and that focal length is considered normal. That’s really the term photographers use to describe a lens that is neither wide angle nor telephoto: *normal*. It’s the closest to the way our eyes perceive the world. When I shot on film 20 years ago, I seldom took my 50mm prime lens off my camera. It’s just a terrific focal length, and I expect to use the 2× focal length on the main camera a lot.4


Action mode is a new feature for video on all iPhone 14 models, pro and non-pro. It’s effectively a much more effective image stabilizer, sort of like a software gimbal. I used it while chasing some of my nieces and nephews around at a backyard birthday party over the weekend, and the results are impressive. It does require a lot of light — computationally it’s doing so much with each frame that it requires a fast shutter speed. But outdoors is where most “action” scenes occur.


## Our eSIM Future Is Here


All of the iPhone 14 models being sold in the U.S. this year are eSIM-only. iPhones have supported eSIMs since 2018, but I’d never used them before. For obvious reasons, when you review and test multiple phones per year, throughout the year, just swapping a SIM card between phones is super convenient. You just pop the SIM out of phone A and stick it into phone B and boom, your cellular connection is now active on phone B. No waiting for your carrier to deactivate phone A and activate phone B. But surely the overwhelming majority of iPhone users have *never* taken their SIM cards out. For almost everyone, physical SIM cards are antiquated, and I think Apple made the right move going eSIM-only here. SIM trays are the new floppy drives.


I went ahead and moved my own personal Verizon account from a SIM card to eSIM on this review phone so I could truly use it as my own. I did the transfer during the setup process for the new phone, while choosing how to transfer/restore data from my old (personal) iPhone 13 Pro to the new (review unit) iPhone 14 Pro. It took a few minutes for Verizon to process, but it just worked. Thumbs up from me. We’ll see how it goes when I try moving the eSIM to other devices throughout the year. But for the overwhelming majority of people, this seems great.5


Apple also provided reviewers with pre-paid eSIMs, so I’ve been able to test dual SIM support. It works pretty well, overall, but even after adding my temporary review unit secondary phone number to my iCloud ID, my group chats in iMessage have been fragmented for reasons I don’t understand. Maybe it’s just me, but I’ve found that iMessage never works consistently if you have more than one phone number in your iCloud ID. Multiple email addresses: fine. Multiple phone numbers: inconsistent confusion.


One concern I’ve heard from DF readers is about international travel. The old way of getting cell service while traveling internationally is to stop by a vending machine at the airport upon arrival and purchase a prepaid SIM card with a certain amount of data. You don’t need to do that anymore. You can prepay — before you leave home — for eSIMs from a bunch of different companies for over 190 different countries. [GigSky](https://www.gigsky.com/) is one such company. [Airalo](https://www.airalo.com/) is another. There are a bunch of others. You get an eSIM with 10 GB of data, for 30 days, for about $20 for just about any country in Europe.


All iPhone 14 models support up to 8 eSIMs, with up to 2 in active use. So you can just buy a prepaid eSIM before you leave home, set it up on your iPhone, and activate it when you arrive. I asked a few friends who travel internationally frequently and they all raved about the eSIM experience for temporary local data service. So not only are eSIM-only iPhones not a problem for international travel, eSIMs seem *superior* to the physical SIM way of doing things for that. (You can’t lose an eSIM, for one thing.)


Speaking of losing things, Apple’s talking points promoting eSIMs mention security. This actually never occurred to me before, but apparently thieves know it all too well: pop the SIM card out of a lost or stolen phone, and location tracking for the phone is greatly hindered. That can’t happen with eSIMs.


Last but not least: Apple has been putting U.S. customers on eSIMs for *all* new iPhones purchased in Apple retail stores since last year. I was not aware of this until Apple informed me, which means it doesn’t seem to have been a problem.


## Silicon


The regular iPhone 14 is clearly just an iterative improvement over the iPhone 13. Chip-wise, the iPhone 14 stays on the A15 “Bionic” from last year. But it is a very small upgrade from the iPhone 13. This was an uncomfortable marketing dance for Apple during the keynote, because heretofore, the non-Pro new iPhones got the latest version of the A-series chips each year. Last year, the regular iPhone 13 models (including the 13 Mini) got an A15 chip with a 4-core GPU. The iPhones 13 Pro, however, got A15 chips with a 5-core GPU. That 5-core GPU A15 is the chip in the iPhone 14 and 14 Plus. “One more GPU core” sounds like no big deal. “25 percent more GPU processing” sounds like a nice year-over-year upgrade. (More on this *last year’s Pro chip goes in this year’s non-pro phone* strategy below.)


The A16 chip in the iPhones 14 Pro seems, in my decidedly non-rigorous testing, to be about 10-15 percent faster than the 5-core A15, both in CPU and GPU processing. That’s not jaw-dropping, but it’s about the best we could hope for in a year when the chips haven’t moved to a next-generation fabrication process at TSMC. It’s also the case that benchmarking CPU and GPU performance and getting “scores” to compare for peak performance is just a terrible way of evaluating chips for mobile phones. For desktop computers, for computationally-expensive tasks, yes, benchmarks like that still matter. But what in the world is anyone doing with their phones that makes these benchmarks all that relevant regarding 10 or 20 percent differences in performance? Nothing. Using benchmarks like this to evaluate phone chips is like taking an electric vehicle to a racetrack and driving it with the pedal to the metal until the battery is dead, and using that to decide how efficient it is for daily driving in the real world.


Consider this hypothetical example. Let’s say a company comes out with a new system-on-a-chip for phones. Call it the X1 chip. A year later, they come out with the X2. In every single benchmark — single- and multi-core CPU, GPU, machine learning — the scores for the X2 are exactly the same as those of the X1. But, phones with the X2 get 20 percent longer battery life than phones with the X1. Is the X2 a significant year-over-year upgrade? Yes! A 20-percent improvement in battery life while maintaining CPU and GPU performance would be impressive (presuming performance and energy efficiency were already “good” in the X1 chip).


That’s the factor that gets overlooked in year-over-year silicon improvements when you only look at benchmark scores. The A16 is a bit faster. But battery life, according to Apple’s published specs, is effectively unchanged. Getting faster without reducing efficiency is a significant win. One step forward, without a step back.


The other silicon-related news this year is what Apple is calling the Photonic Engine. Here’s how Apple describes it:


> This dramatically improves photos taken in mid to low light, like
> indoors, right before the sun sets. Photonic Engine builds on the
> incredible computational photography capabilities of iPhone and
> furthers our image pipeline by doing Deep Fusion earlier in the
> process. Deep Fusion uses our powerful Neural Engine to take the
> best parts of multiple images on a pixel-by-pixel basis and
> combine them into an image that increases dynamic range and brings
> out extraordinary detail in low light. Photonic Engine now applies
> Deep Fusion to uncompressed images, enabling use of
> more data for more detail, more colors, and brighter colors.
> Photonic Engine combines with hardware capabilities for a big leap
> forward in low-light photo capabilities. Photonic Engine is a big
> advancement in computational photography and delivers better
> results in challenging lighting environments.


Basically, on the iPhone 13 models and earlier, Deep Fusion worked on the compressed JPEG or HEIC imagery; now it works on the RAW data direct from the sensor. This isn’t an A16-exclusive feature, because the non-pro iPhone 14 models have it too, but it is exclusive to this year’s new phones. iPhone 13 Pros running iOS 16 don’t get the Photonic Engine, because, I presume, it’s a hardware improvement to the pipeline between the camera sensors and the image signaling processor on the chips. Apple “silicon” isn’t just the SoC; it’s everything inside the phone that connects to the SoC. This level of integration across *everything* related to “hardware” is very difficult for the Android world to compete with.


In terms of room for improvement for future A-series chips and image signal processing, 4K ProRes video is still limited to 30 FPS max on the iPhone 14 Pro. Get your shit together, Apple. (It would be a lot of fun to transfer 4K 60 FPS ProRes video files at the USB 2.0 data speeds offered by Lightning.)


## Colorways and Materials


As mentioned above, the iPhone 14 Pro I’ve been using as my main phone for the last week is space black. It’s my favorite stainless steel iPhone colorway ever, by far, no question. In the entire history of the iPhone, I think it’s second only to the black/slate iPhone 5 from 2012. (Yes, [the one](https://support.apple.com/kb/sp655?locale=en_US) whose coating chipped over time. That visible wear and tear made the iPhone 5 look better, not worse — like a leather wallet or denim jeans. And yes, I dug my own iPhone 5 out of my museum to check if I still have as much affection for it as I recall. I do.6) I generally like buying anything that’s available in black in black. But this space black is a terrific black. For me, this might be as good as Apple’s ever going to get with stainless steel and a matte glass back.


I’m pretty sure I’ve registered this same complaint every year since the iPhone X, but I still wish Apple weren’t using stainless steel for the iPhone Pro models. It certainly looks nice that it’s polished to a high gloss, but steel is just so damn heavy. My tastes run toward smaller phones (pour one out for the Mini lineup, which, I fear, is gone for good), but also toward *lighter* phones. There’s no accounting for taste in colors, of course, so setting color aside, every single thing about the iPhone Pro models is better than the non-pro ones except for weight (206g vs. 172g, a factor of 1.2×). *But weight really matters for something you carry with you almost everywhere.* Two years ago I purchased an iPhone 12 rather than 12 Pro simply because I preferred the feel of it, both in hand and in pocket, and because by the fall of 2020 it seemed pretty clear I wouldn’t be traveling much, if at all, before the iPhones 13 arrived the next year and thus wouldn’t regret carrying the second-tier camera system. I miss the weight and feel of that phone to this day.


If ceramic is impractical as a material for iPhones (and I suspect it is, but man, those ceramic Apple Watch Edition models were *nice*), I hope that the Apple Watch Ultra heralds a possible switch from stainless steel to titanium for the iPhone Pro next year or thereafter.7


The iPhone 14 Pro Max unit Apple provided me with is deep purple. It’s fine, but it’s not as fun and nowhere near as purple as the purple iPhone 12 (non-pro) Apple released in April last year. [Look at that purple iPhone 12](https://www.apple.com/newsroom/2021/04/apple-introduces-iphone-12-and-iphone-12-mini-in-a-stunning-new-purple/). That’s a fun color. I really don’t get why Apple doesn’t release *any* iPhone Pro models in [bold fun colorways](https://basicappleguy.com/basicappleblog/nanochromatic). The “deep” in “deep purple” translates, to my eyes (and those of [others](https://twitter.com/AmyJane/status/1570524339958853632)), to “*clearly but subtly tinted in good lighting when viewed from just the right angle, but otherwise looks gray*”. Personally I’m as happy as Darth Vader with a freshly polished helmet with the 14 Pro’s space black, but for the untold millions of people out there who love fun colors, there remains no such thing in the iPhone Pro lineup. Seems inexplicable to me that “fun bold colors” and “best possible iPhone” have been mutually exclusive since [the Product Red iPhone 7 special edition](https://www.apple.com/newsroom/2017/03/apple-introduces-iphone-7-and-iphone-7-plus-productred-special-edition/) in March 2017.


Apple also provided me with a blue iPhone 14. It seems a bit unsatisfying to my eyes — too baby blue for anyone who wants a neutral colorway, but not nearly bold enough for someone seeking something *fun*. But it’s definitely blue, in all light, from all angles.


## The iPhones 14


In 2013, the new flagship iPhone was [the iPhone 5S](https://daringfireball.net/2013/09/the_iphone_5s_and_5c). If they’d followed their pattern from the previous few years, they’d have kept [2012’s iPhone 5](https://daringfireball.net/2012/09/iphone_5) in the lineup at reduced prices. Instead, the new 5S replaced the 5 at the top of the lineup, and Apple introduced the iPhone 5C — a phone with the iPhone 5’s internal specs, but on the outside, an all-new and distinctive design that Jony Ive described, quite aptly, as “[beautifully, unapologetically plastic](https://techcrunch.com/2013/09/10/iphone-5c/)”.


Apple, of course, didn’t explain why. Conventional wisdom speculated that the chamfered edges of the iPhone 5 were too expensive to produce, or that the black/slate model chipped too easily. (The dark version of the iPhone 5S was space gray, not black/slate.) I don’t think that was the reason at all. I simply think Apple wanted one iPhone and one iPhone alone to *look* like the best one, the king of the hill. Both from the outside — and from the inside, looking at the specs. The problem with the idea of selling the iPhone 5 at a lower price alongside the then-new 5S was that next to each other, the 5S didn’t look newer enough.


That strategy didn’t seem to work at the time. People I know who owned the 5C loved the thing and loved its “unapologetically plastic” design, but it didn’t seem to sell particularly well. In the 6 / 6S / 7 era, Apple went back to selling the prior years’ models at $100-increment lower prices. But Apple clearly never gave up on the basic idea of introducing two distinct tiers of new iPhones each year, with the flagship design sitting distinctively atop the lineup. Starting with the iPhone X and iPhone 8 five years ago, there have been two new iPhones each year: a good one, and an even better one. Even before they started using the word “pro” for iPhone names, there’s been one new model that’s pro (and pro-priced), and another new model that isn’t.

Markdown Table
|      | Pro                  | Regular          |
| ---- | -------------------- | ---------------- |
| 2017 | X                    | 8 (and 8 Plus)   |
| 2018 | XS (and XS Max)      | XR               |
| 2019 | 11 Pro (and Pro Max) | 11               |
| 2020 | 12 Pro (and Pro Max) | 12 (and 12 Mini) |
| 2021 | 13 Pro (and Pro Max) | 13 (and 13 Mini) |
| 2022 | 14 Pro (and Pro Max) | 14 (and 14 Plus) |


|  | Pro | Regular |
| 2017 | X | 8 (and 8 Plus) |
| 2018 | XS (and XS Max) | XR |
| 2019 | 11 Pro (and Pro Max) | 11 |
| 2020 | 12 Pro (and Pro Max) | 12 (and 12 Mini) |
| 2021 | 13 Pro (and Pro Max) | 13 (and 13 Mini) |
| 2022 | 14 Pro (and Pro Max) | 14 (and 14 Plus) |



The basic idea of introducing two tiers of a product each year is simple: market segmentation. Considering that the iPhone is Apple’s most popular product ever — and quite arguably the most successful product any company has ever made — it makes a lot of sense. But more subtle is Apple’s strategy for moving older models down the lineup at lower prices each year. *Only the non-pro iPhones move down the line.* The iPhone X was *replaced* by the XS. The XS was *replaced* by the 11 Pro. And no iPhone named “Pro” has ever moved down the lineup at a reduced price. If you want to buy an iPhone 14 Pro or Pro Max, you better buy it sometime between now and next year’s iPhone 15 event.


That means no 6.7-inch iPhone has ever been sold at less than the $1,100 starting price of the first one, the 11 Pro Max. (Which only had 64 GB of storage!) The iPhone 14 Plus breaks that pattern, starting at $900 (with a reasonable 128 GB of storage). And, I expect both the iPhone 14 and 14 Plus to remain in the lineup a year from now at $100 lower prices. If Apple keeps both sizes in the lineup for *two* years, you’ll be able to buy a 6.7-inch iPhone 14 Plus in 2024 for just $700. Big displays are no longer an exclusive upsell to the iPhone Pro tier.


Now, though, a new pattern has been introduced: only the iPhones Pro get the new generation A-series chip. The iPhone 14 thus is sort of a modern version of the iPhone 5C concept: an industrial design that is less premium-looking but more fun and colorful than the pro models, with the SoC from the previous year’s pro models. I’ll eat my hat if, next year, the A17 isn’t exclusive to the iPhones 15 Pro and the regular iPhones 15 don’t get this year’s A16. Chips now join display quality, camera quality, telephoto lenses, and premium materials as differentiating factors between the iPhones Pro — which, I’ll repeat, are *only* sold at the very highest prices — and the non-pro iPhones. Hardware costs money.


More interestingly — super interestingly, even — the Dynamic Island now introduces a *software* user experience differentiator. Because Live Activity views are only available on the Lock Screen of notched iPhones (and as fleeting non-user-invokable notifications, like Apple Maps’s turn-by-turn directions have been for years), Apple has now introduced major new *software* features that are only available on the iPhones Pro, via the Dynamic Island. There is a hardware component — the smaller sensor array and behind-the-display proximity sensor — but all of the Dynamic Island functionality could be exposed to notched iPhones, just in less cool-looking ways. That’s a design choice Apple has (apparently) made, not a function of production costs. It’s not just that the Dynamic Island looks better than the notch. It provides utility that just about any iPhone user would enjoy. At least any iPhone user who ever listens to music or podcasts, makes phone calls, hails rides with Uber or Lyft, or follows live sports. And the only way to get it is with a new iPhone 14 *Pro*.


I don’t think it’s a coincidence that the very same year Apple stopped holding 6.7-inch displays as an exclusive feature for the premium-priced Pro models is the same year they introduced the compelling Dynamic Island. I expect the Dynamic Island to remain iPhone-Pro-exclusive for years to come. It might come to the non-pro new iPhones in a few years, but if it does, that will coincide with some *new* iPhone-Pro-only flagship star-of-the-TV-commercials feature.


---

1. For a few days after last week’s keynote, I was thinking, vaguely, that perhaps MacBook Pros could go from a notch to a Dynamic Island eventually. Upon further consideration, though, I don’t think it would work. For one thing, the mouse cursor would disappear under the parts of the Dynamic Island that really are housing sensors. Yes, the cursor disappears under the MacBook Pro notch today, but it disappears under the *whole* notch, not patches of it. The entire point of the Dynamic Island is to create the convincing illusion that there is no sensor array cutout on the display, but a mouse cursor would continually spoil that illusion. The Dynamic Island concept is inherently touchscreen-exclusive. (Another factor: it’s weird enough that the MacBook Pro notch interrupts the menu bar. It’d be downright annoying for a Dynamic Island to dynamically push menus around as it expands and contracts. I suppose, on the Mac, the Dynamic Island could be of fixed width to avoid that issue, but then it would lose a lot of its playfulness and personality. “The Static Island” doesn’t have quite the same ring to it.) Lastly, the Mac just doesn’t need it.
I don’t think an iPhone-style Dynamic Island will ever come to iPads, either. For one thing, I’m inclined to think iPad bezels will never shrink to the point where the sensor array won’t fit behind them. For another, iPads now have mouse pointer support when connected to a trackpad and the same illusion-ruining factor I mentioned about the Mac would apply. But here’s an idea: perhaps the Dynamic Island would come to the iPad *purely in software*. The iPad hardware sensor array would still be hidden in the bezel surrounding the display, but iPadOS could render a pure software Dynamic Island on screen. That, I think, would work completely. You could rotate the iPad and the Dynamic Island would always be at the top. The mouse pointer wouldn’t disappear under any actual hardware sensors. It’d just be a black [stadium](https://en.wikipedia.org/wiki/Stadium_(geometry)) rendered entirely by software. It could actually be more elegant than the iPhone’s Dynamic Island because there’d be no sensors to disguise. ↩︎
2. I strongly suspect that Apple considers the ProMotion display to be essential to the Dynamic Island experience. Running its animations at 120 FPS makes the Dynamic Island feel alive. It sells the illusion that this ever-present black stadium is entirely a feature, not a tradeoff. Again I’ll turn to the analogy to sleight-of-hand magic: it’s not enough to perform the trick with the correct mechanics, the motion has to be perfectly smooth, too. ↩︎︎
3. In Settings → Camera → Formats, you can choose between 12 and 48 MP resolution for ProRAW. Approximate file sizes: 25 and 75 MB. ↩︎︎
4. If you tend to shoot almost everything on your iPhone at 1× simply because that’s the default, I encourage you to try using 2× for more day-to-day shooting if you have an iPhone that offers it. Using a normal lens does for your photography muscles what lifting weights does for your actual muscles. (I wish there were an option in Settings → Camera → Preserve Settings that allowed you to keep your last-used focal length each time you open the Camera app. There are times when I’d like to leave it at 2×.) ↩︎︎
5. While I’m talking about initial setup, let me repeat [my recommendation from last year](https://daringfireball.net/linked/2021/09/24/how-to-set-up-a-new-iphone-or-ipad): I cloned my existing iPhone 13 Pro to new iPhone 14 devices this week both by restoring from iCloud Backup and using the direct device-to-device Quick Start transfer. I highly recommend the device-to-device transfer. It might take a bit longer, but it moves almost *everything*, including your login credentials for almost every app. My biggest complaint about restoring from iCloud Backup is that while your data all gets restored, your login credentials don’t. ↩︎︎
6. I also have extraordinarily fond affection for the original iPhone. Is the original my favorite iPhone design ever? In some ways, of course. For chrissake [just look at Evans Hankey’s personal original iPhone](https://www.macg.co/aapl/2019/06/evans-hankey-le-nouveau-visage-du-design-produit-dapple-106737), after years of use. It might be the single most beautiful object in the entire *[Designed by Apple in California](https://www.apple.com/newsroom/2016/11/designed-by-apple-in-california-chronicles-20-years-of-apple-design/)* book. ↩︎︎
7. Regarding titanium’s advantages versus steel, [consider last year’s Apple Watch Series 7 lineup](https://support.apple.com/kb/SP860?viewlocale=en_US&locale=en_US) at 45mm:

Aluminum: 38.8g

Titanium sits almost exactly halfway between aluminum and steel, weight-wise. And a device designed to be solely available in titanium might prove even lighter, as the structure can be designed with [titanium’s extraordinary strength-to-density](https://en.wikipedia.org/wiki/Titanium) ratio in mind. Another comparison: the Apple Watch Ultra weighs 61.3g and the 45mm stainless steel Series 8 weighs 51.5g, but the Ultra is a *lot* bigger. The Apple Watch Ultra is closer in weight to the 45mm steel Series 8 than the steel Series 8 is to the aluminum one (38.8g). ↩︎︎



| **Previous:** | [Thoughts and Observations on Last Week’s ‘Far Out’ Apple Event](https://daringfireball.net/2022/09/thoughts_and_observations_on_last_weeks_far_out_apple_event) |
| **Next:** | [Apple Watch Ultra](https://daringfireball.net/2022/09/apple_watch_ultra) |


PreviousNext