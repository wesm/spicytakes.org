---
title: "Apple, Adobe, and Flash"
date: 2010-01-25
url: https://daringfireball.net/2010/01/apple_adobe_flash
slug: apple_adobe_flash
word_count: 2716
---


In my “[Tablet Musings](http://daringfireball.net/2010/01/tablet_musings)” piece two weeks ago, I speculated that Apple’s imminent tablet probably won’t support Flash, for all the same reasons the iPhone doesn’t. Reaction to this was polarized — typically either “duh, of course it won’t” or “no way, it *has* to support Flash”. You can see both reactions represented in [the thread on my piece at Hacker News](http://apps.ycombinator.com/item?id=1037401). One group is going to be very surprised come Wednesday.


I’ve been writing about this saga [for two years](http://daringfireball.net/2008/02/flash_iphone_calculus). My fascination with the subject is fueled by the fact that it’s so polarizing, and that it encompasses both technical and political issues.


## On Flash and Mac OS X Application Crashes


Two weeks ago [I wrote](http://daringfireball.net/2010/01/tablet_musings):


> To my knowledge, Apple controls the entire source code to the
> iPhone OS. That’s not to say they wrote the whole thing from
> scratch. Many low-level OS components are open source. But they
> have the source. If there’s a bug, they can fix it. If something
> is slow, they can optimize or re-write it. That is not true for
> Mac OS X, and Flash is a prime example. The single leading source
> of application crashes on Mac OS X is a component that Apple
> can’t fix.


Several readers asked me for the source for my accusation contained in that last sentence, that Flash is the “leading source of application crashes on Mac OS X”. (And good for them for asking; I’m not sure what I was thinking including that without sourcing it.)


Here’s the deal. On stage at the [WWDC 2009 keynote address last June](http://www.macworld.com/article/140897/2009/06/keynote.html), Apple senior vice president of software engineering Bertrand Serlet was explaining the new web content plugin mechanism for Safari in Snow Leopard. Rather than run within Safari’s application process, web content plugins now run in their own process, so if they crash, they (usually) don’t crash Safari itself. You get a broken little rectangle in the page where the plugin was executing, but the browser itself stays running.


Apple did this for two reasons. Serlet’s stated reason on stage was “crash resistance”, as mentioned above. As for why such crash resistance was worth implementing, Serlet explained that, based on data from the Crash Reporter application built into Mac OS X — the thing that asks if you’d like to send crash data to Apple after a crash — the most frequent cause of crashes across all of Mac OS X are (or at least *were*, pre-Snow Leopard) “plugins”.


Serlet didn’t name any specific guilty plugins. Just “plugins”. But during the week at WWDC, I confirmed with several sources at Apple who are familiar with the aggregate Crash Reporter data, and they confirmed that “plugins” was a euphemism for “Flash”.


In other words, in Apple’s giant pile of aggregate crash reports — from all app crashes on all Macs from all users who click the button to send these reports to Apple — Flash accounts for more of them than anything else. That doesn’t mean Flash somehow causes crashes in any various app. Presumably, most of the time it’s Safari or some other browser playing Flash content. And it’s worth noting that this doesn’t necessarily mean Flash is particularly crash-prone or poorly engineered. Think of it as a formula like this:


*total crashes = (crashing bugs) × (actual use)*


Flash’s number and severity of crashing bugs could well be somewhat low and it would still account for a large number of total crashes because it’s actually used *all the time* — by any Mac user with Flash content playing in a web page. And, if Flash Player for Mac OS X actually *is* poorly-engineered overly-buggy code, well, that’s even worse.


But there’s another reason why Apple created this new external process architecture for web content plugins in Snow Leopard: it was the only way they could ship Safari and the WebKit framework as 64-bit binaries. Flash Player is only available as a 32-bit binary. (This is true for other third-party web content plugins, like Silverlight, but Flash is the only one that ships as part of the system.) 64-bit apps cannot run 32-bit plugins. Apple doesn’t have the source code to Flash, so only Adobe can make Flash Player 64-bit compatible. They haven’t yet. So if Apple wanted Safari to be 64-bit in Snow Leopard (and they did), they needed to run 32-bit plugins like Flash in a separate process.


Maybe you don’t believe Apple that web content plugins are the most frequent source of crashes on Mac OS X. Maybe you don’t believe me and my unnamed sources at Apple that it’s Flash in particular that accounts for this. That’s cool, skepticism is good. So then in that case, maybe Bertrand Serlet blamed “plugin crash resistance” for political reasons, just to stick a knife in Adobe’s back, and the only reason Apple went with this external-process architecture was for the 64-bit/32-bit incompatibility.


But *that* just shines a light on the fact that Flash is still a 32-bit binary despite the fact that Apple wants to go 64-bit system-wide. Flash remains 32-bit and there’s nothing Apple can do about it. Instead of being able to make Flash 64-bit themselves, Apple had to engineer an entirely new plugin architecture.


This is why Apple wants to control the source code to the entire OS. If they want to go 64-bit with iPhone OS, it’s entirely in Apple’s own control to do so. And what happens if Apple goes to a new CPU architecture? For the components Apple controls the source code to, they can recompile for the new architecture. If the entire system doesn’t recompile cleanly for the new architecture, they can work on it until it does. For a component like Flash, where Adobe controls the source code, Apple instead has to wait.


Which situation do you think Apple is happier with? Mac OS X, where they had to create a new web content plugin architecture because Flash crashes frequently and isn’t 64-bit? Or iPhone OS, where they control the source code to every single component, and can do whatever they want, when they want?


Point is, even if you think Flash Player for Mac OS X is the greatest piece of software in the world and that a Flash Player for iPhone OS would run just fine, too — there’s no denying that Apple executives have said and continue to say anti-Flash things publicly. Apple doesn’t say much about Flash, but what they do say doesn’t sound like the sort of things they’d say if they were looking forward to supporting it *more* rather than *less*.


## The Proprietary Web


It’s probably pretty clear to regular DF readers that I don’t care for Flash, and that I’m hoping Apple never includes it in the iPhone OS. Might as well make my biases clear.


Why? At the core, because Flash is the only de facto web standard based on a proprietary technology. There are numerous proprietary web content plugins — including Apple’s QuickTime — but Flash is the only one that’s so ubiquitous that it’s a de facto standard. Flash is the way video is delivered over the web, and Adobe completely controls Flash. No other aspect of the web works like this. HTML, CSS, and JavaScript are all open standards, with numerous implementations, including several that are open source.


The simplest argument in favor of Flash support on the iPhone (and The Tablet, and everywhere) is that Flash is, by dint of its popularity and ubiquity, part of the web. But the best argument *against* Flash support is that it is harmful to the web as a whole to have something as important as video be in the hands of a single company, and the only way that’s going to change is if an open alternative becomes a compelling target for web publishers.


It’s a chicken-and-egg problem. Publishers use Flash for web video because Flash is installed on such a high percentage of clients; clients support Flash because so many publishers use Flash for web video. Apple, with the iPhone, is solving the chicken and egg problem. For the first time ever, there is a large and growing audience of demographically desirable users who don’t have Flash installed. If you want to show video to iPhone users, you need to use H.264.


Apple isn’t trying to replace Flash with its own proprietary thing. They’re replacing it with H.264 and HTML5. This is good for everyone but Adobe.


And yes, I know Flash does much more than just play video. But that’s the main thing everyone is talking about when they talk about Flash not working on the iPhone — video. And when you talk about other uses for Flash, you’re talking about serving as a software runtime, and whether you like it or not, Apple has a clearly stated opposition to third-party software runtimes for iPhone OS, and that policy seems to be working out pretty well for them.


Here’s an email I got from a DF reader:


> I was in line waiting for a coffee on Christmas day. In front of me
> was a kid, about nine or ten, who had an iPhone. He clearly had
> gotten it that morning. He was pushing frantically at a white box on
> a web page with the broken plug-in symbol. He was squeezing it,
> swiping it. He was frustrated and on the verge of getting pissed
> with his new toy. It seemed like he was trying to hit an online game
> page, probably one he was used to playing on the family PC. Finally
> I couldn’t take it anymore. I leaned over and said, “It won’t load
> Flash. It won’t play your Flash games.” His mom, ignoring him up to
> that point, was triggered by a stranger talking to her kid. “That’s
> okay honey,” she said, “we’ll get you a game from the App Store.”
> His response to this? He started working that device even harder. He
> didn’t want an App Store game; he wanted his Flash game. And that
> iPhone suddenly took a huge dive in value to him.
> Like it or not, Apple needs to come to terms with this. If only for the
> kids.


I think this anecdote, and this reader’s takeaway from it, accurately captures the feeling behind much of the “Apple has got to bend on this eventually” sentiment that’s out there.


But think about it from Apple’s perspective. How do you think this situation turned out in the long run? Do you think the kid told his mom to return the iPhone for a refund? Or, do you think they went home and started buying games from the App Store? That there was a period of initial frustration due to Flash games not playing doesn’t change the fact that they (a) bought an iPhone and (b) were set to buy games from the App Store.


I’m not arguing that Apple’s apparent executive-level antipathy toward Flash is about anything other than Apple’s own interests. (I do think, though, that Apple’s WebKit team is genuinely idealistic about helping the web as a whole.)


But while Apple may be acting spitefully, they’re not spiting themselves. The iPhone’s lack of Flash has not hurt it one bit. Perhaps that will change in the future, if Flash someday proves popular on other mobile platforms, but don’t hold your breath.


## Flash Performance on Mac OS X


In addition to the principled concerns outlined above regarding Flash being proprietary, there are also practical issues. One, Flash’s aforementioned crashiness on Mac OS X. Second, crashiness aside, its performance on Mac OS X is not as good as it is on Windows. And for video playback specifically, Flash’s performance pales compared to H.264 played through QuickTime. This is [not subjective](http://www.flickr.com/photos/adriannier/4275358738/). My machine is a two-year-old MacBook Pro. It plays full-screen H.264 video through QuickTime without problem. When I play full-screen Flash video, my fan kicks in within a few seconds, every time.


I’ve been hard on Flash Player for Mac OS X, but this performance situation is not entirely in Adobe’s hands. On Windows, Flash makes use of hardware decoding for H.264, if available. On Mac OS X, it does not. This is one reason why Flash video playback performs better on Windows than Mac OS X, and also why H.264 playback on Mac OS X is better through QuickTime (which does use hardware decoding).


According to Adobe, though, this is because they *can’t*. Here’s an entry from their [Flash Player FAQ](http://labs.adobe.com/technologies/flashplayer10/#FAQ):


> Q. Why is hardware decoding of H.264 only supported on the
> Windows platform?
> A. In Flash Player 10.1, H.264 hardware acceleration is not
> supported under Linux and Mac OS. Linux currently lacks a
> developed standard API that supports H.264 hardware video
> decoding, and Mac OS X does not expose access to the required
> APIs. We will continue to evaluate when to support this feature
> on Mac and Linux platforms in future releases.


Adobe platform evangelist Lee Brimelow recently posted a [weblog entry addressing this](http://theflashblog.com/?p=1641):


> But let’s talk more about the Flash Player on the Mac. If it is
> not 100% on par with the Windows player people assume that it is
> all our fault. The facts show that this is simply not the case.
> Let’s take for example the question of hardware acceleration for
> H.264 video that we released with Flash Player 10.1. Here you can
> see [some published results](http://i.engadget.com/2009/11/17/adobes-flash-player-10-1-beta-gpu-acceleration-tested-document/) for how much the situation has improved
> on Windows. Unfortunately we could not add this acceleration to
> the Mac player because Apple does not provide a public API to make
> this happen. You can easily verify that by asking Apple. I’m
> happy to say that we still made some improvements for the Mac
> player when it comes to video playback, but we simply could not
> implement the hardware acceleration. This is but one example of
> stumbling blocks we face when it comes to Apple.


I’m aware of no reason to dispute this. Windows is more hospitable to a third-party runtime like Flash than Mac OS X. I think most would agree that Apple is an opinionated company (to say the least), and they make opinionated products. The runtimes Apple cares about are Cocoa and WebKit. The Apple way to play H.264 is through the QuickTime APIs (and really, as of Snow Leopard the new QuickTime X APIs), not to write your own H.264 playback code that seeks to directly access hardware accelerators.


You can argue about why Apple has taken this stance. One could argue that it’s pragmatic — that Apple doesn’t allow third-party software access to things like hardware H.264 acceleration because it seeks to maintain a layer of abstraction between third-party software and the underlying hardware. One could argue that it’s political — that Apple is happy to make Flash look bad performance-wise because Flash is competitive with Apple products in several different regards. (E.g. you may wish that Hulu, which is entirely Flash-based, worked on your iPhone and worked better on your Mac. Apple wishes that Hulu’s content was going through the iTunes Store.)


I would argue that it’s *both* — that Apple’s distaste for Flash Player is both a matter of engineering taste (that third-party software should only have access to high-level APIs) *and* politics. But objectively, regardless of what you personally wish Apple would do with regard to Flash, if Adobe needs Apple to grant them further access to the hardware to make the *Mac* version of Flash Player better, what are the odds that they’d get that sort of low-level hardware access on the iPhone OS? (Hint: zero.)


I’ll leave the last word to Apple COO Tim Cook, [who a year ago said](http://www.businessweek.com/technology/content/jun2009/tc20090621_038917_page_2.htm), “We believe in the simple, not the complex. We believe that we need to own and control the primary technologies behind the products we make, and participate only in markets where we can make a significant contribution.”


Flash is owned and controlled by Adobe.



| **Previous:** | [Apple, Google, Bing, and Search](https://daringfireball.net/2010/01/apple_google_bing_search) |
| **Next:** | [‘A String of Masterpieces’](https://daringfireball.net/2010/01/string_of_masterpieces) |


PreviousNext