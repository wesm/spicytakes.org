---
title: "WWDC 2010 Wrap-Up"
date: 2010-06-18
url: https://daringfireball.net/2010/06/wwdc_wrapup
slug: wwdc_wrapup
word_count: 1473
---


## Focus


Much has been made over the fact this was the first-ever WWDC where the Mac played no role, either in the keynote or in the sessions. But that wasn’t the only change — the IT track was dropped from the session schedule as well. The result was a conference that was very tightly focused, like no WWDC before. Even when the conference was all about Mac programming, it never felt like this, perhaps because “programming for the Mac” encompasses so many different things than “programming for iOS”.


One result of this focus was that it felt more like a single- or dual-track conference. From Tuesday through Friday, WWDC generally has a dozen or more simultaneous sessions and labs in each slot. But the big ones — the more general-purpose, applies-to-any-iOS-developer sessions — were *really* crowded. It wasn’t unusual to have to wait in a 10 minute line just to get into the room. And on Monday, the afternoon “State of the Union” sessions were all filled to capacity. I was in an overflow room downstairs, and even the overflow rooms were crowded. There weren’t more attendees this year than last, but it somehow felt a *lot* more crowded.


The tight focus of the conference was, I think, a reflection of the current focus of Apple itself. We may never see such a single-minded WWDC again.


## Attendees


I heard figures ranging from 55 to 65 percent for the number of first-time attendees. That’s a good thing, and not at all surprising.  Sessions were geared appropriately, with a significant number covering entry-level/intermediate material. This was especially true for some of the two-part sessions — the first part was often more about broad fundamentals than technical details. I heard some people complain about this, but I think the programming was clearly matched well to the demographics of the attendees.


If you’re bored at a session, get up and move to another. Or, go to a lab. (I wonder how many WWDC attendees underestimate the quality of the consulting available from the labs.)


One difference between this year and last is that a lot more of the developers I spoke to — both old friends and people I met for the first time — are doing full-time iOS development. Last year there were a lot more who were doing it on the side. And it’s not just the App Store — I met a bunch of developers doing full-time iOS app development for the enterprise.


The conference sold out in eight days this year. If attendance hadn’t been capped at 5,200, I wonder how many tickets Apple could have sold?


## The Videos


Used to be it took two months or even longer for Apple to release videos of the sessions from WWDC. Last year, they released them just three weeks after the conference ended, and lo, there was much rejoicing. This year, the videos were released yesterday, just six days after the end of the conference. Apple released the videos before I got around to finishing this little wrap-up.


This turnaround changes the dynamics of WWDC significantly. For one thing, there’s not nearly so much of a penalty for those who skip or who wished to attend but didn’t register before the sellout was announced. For another, even for attendees, it no longer seems like a big deal to skip sessions, and I feel less pressure when deciding between two (or more) concurrent sessions of interest.


And, more significantly perhaps, this year the videos are available free of charge to all registered Apple developers. [Previously](http://daringfireball.net/linked/2006/10/24/wwdc-videos), you had to pay at least $500 for access. The simple math is that there’s only room at Moscone West for 5,200 attendees, but there are way more than 5,200 developers whom Apple wants to have access to these sessions.


## Mac OS X 10.7


There *were* sessions with wee bits of 10.7-related information, if you read between the lines (or search for 10.7 references in the iOS 4 SDK frameworks — *cough*, AV Foundation, *cough*). 10.7 is clearly proceeding, and word on the street is that it’s picking up steam.


## iPhone 4


Apple should have put iPhone 4 units on display in Moscone, [like they did with the original iPhone](http://www.flickr.com/photos/x180/354638930/) at Macworld 2007, if only to inspire developers to create double-resolution artwork for the custom UI elements.


## GCD and Blocks


Speaking of AV Foundation, [Grand Central Dispatch](http://developer.apple.com/mac/articles/cocoa/introblocksgcd.html) is becoming pervasive. New APIs from Apple use blocks wherever there’s a callback. This is the design pattern of the future for Cocoa apps on both OSes.


What’s interesting (to me at least) is that GCD and blocks were originally pitched by Apple as their solution to the problem of how to take advantage of multicore CPUs. But all iOS devices, including the iPhone 4, use single-core CPUs. But that’s the beauty of GCD and blocks: it makes efficient use of *any* number of CPU cores, including just one. And the programming design pattern results in cleaner code — rather than having a callback routine with a context parameter (containing information pertaining to the current state), the callback and the context are encapsulated together inside the block.


The developers I spoke to who are using it already really like it. If anything, it’s a *bonus* that GCD works so well to create programs that make efficient use of multicore CPUs. And eventually we will get multicore CPUs in iOS devices, and when that happens, apps written for iOS 4 will already take advantage of them.


## The Low Point of the Keynote


Steve Jobs made a point of emphasizing that 95 percent of App Store rejections are for three reasons: (1) apps that crash; (2) apps that make use of private API calls; and (3) apps that don’t function as advertised. It’s interesting to know that these three reasons account for 19 out of 20 rejections, but it’s a straw-man argument to hold them as a refutation of App Store criticism: *no one is criticizing the App Store for rejections because of these things*.


And yes, I realize there are in fact people who don’t think Apple should reject apps for using private API calls, and you could probably find someone who thinks apps should be allowed to crash and falsely advertise their functionality, too. But if those were the *only* three reasons submissions were rejected from the App Store, there’d be no controversy.


I can’t say it better than I have before: [It’s not the control, it’s the secrecy](http://daringfireball.net/2010/04/not_the_control_the_secrecy) — that there clearly exist rules which are not written. The latest batch: [“widget” apps for the iPad and iPhone](http://www.macworld.com/article/151680/2010/06/myframe_rejection.html). The written rules state that you must stick to the Cocoa Touch APIs and WebKit. So several developers created apps that let you display multiple simultaneous “widgets” on screen at once. Sort of like Mac OS X’s Dashboard, and sort of like multitasking, but using nothing more than WebKit — HTML, JavaScript, and CSS.


There’s nothing in the developer agreement guidelines to suggest these apps wouldn’t be allowed. But, they’re not. And the problem is that the developers who made these apps only found out *after they had created the apps* and submitted them to the store. Obviously Apple can’t write guidelines that cover scenarios it hasn’t foreseen; but once something new comes up, their policies to handle it should be documented publicly.


The App Store review situation has improved significantly in the last year. It’s getting better, not worse. But Jobs’s defense of it had nothing at all to do with the aspects that remain problematic.


## The Oddest Point of the Keynote


Bringing Zynga on stage to demo FarmVille for iPad was a kill-two-birds-with-one-stone move: it was about not needing Flash (a high profile, popular game [that Adobe has held up as the first example](http://theflashblog.com/?p=1703) of what iPad users are missing out on) and, to a lesser extent, it was about Facebook (the current leader in social gaming).


But what a *weird* demo. Was that guy off-script or what? The demo seemed targeted specifically to existing FarmVille players, because I (having never played the game) couldn’t make heads or tails out of how one is supposed to play or what sort of entertainment it was supposed to provide.


## iMovie for iPhone


It’s interesting that Apple is going to sell it for $5 rather than include it in the system. I’m not sure why. My theory: most people wouldn’t use it if it were included free (because most people never edit videos), and those who *will* use it will happily spend $5 for it. I spent some time playing with it on the demo iPhone 4 units, and it’s a splendid app. Truly marvelous.



| **Previous:** | [‘First to Do It’ vs. ‘First to Do It Right’](https://daringfireball.net/2010/06/first) |
| **Next:** | [Apple’s System Apps](https://daringfireball.net/2010/06/apples_system_apps) |


PreviousNext