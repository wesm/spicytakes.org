---
title: "The Case for Going Metro-Only on ARM"
date: 2011-09-20
url: https://daringfireball.net/2011/09/the_case_for_going_metro_only
slug: the_case_for_going_metro_only
word_count: 1124
---


[Jesper makes the case](http://waffle.wootest.net/2011/09/15/armed-with-evidence-to-the-contrary/) that Microsoft will allow desktop (i.e. traditional) Windows apps to run on ARM-based Windows 8 machines:


> Microsoft’s position on the environment duality is that the
> desktop half won’t even be loaded until you use it initially.
> Metro apps run in a new environment with more rapacious process
> and power management and may not unto itself mean doom for battery
> usage. With this in mind, Microsoft gets the chance to tout the
> only alternative that remains fully a tablet OS as long as you
> only do tablety things *and* that can be talked into running
> Office when the need arises.


Read the whole thing. His take is reasonable. If Windows 8 *does* ship with support for classic non-Metro apps on ARM machines, these will be the reasons why.


But there are *other* good reasons, I think, for why Microsoft should cut the cord cleanly and go Metro-only on ARM.


For one thing, no matter what Microsoft decides to do, there is going to be confusion. Windows 8 is going to support two different CPU architectures: x86 (a.k.a. “Intel”) and ARM. Same OS, two different CPU architectures — just like when Mac OS X supported both PowerPC and Intel. But when Apple switched to Intel, they included Rosetta, an emulation layer which allowed existing PowerPC apps to run on the new Intel machines without being recompiled by the apps’ developers. Microsoft has explicitly ruled out such an emulation layer for ARM — x86-compiled apps will not run on Windows 8 on ARM. What’s in question is whether existing Windows apps will be able to be recompiled/ported by the developers to run natively on ARM; if not, Windows on ARM will only support Metro apps.


So the inevitable confusion is that either way, no existing x86-compiled Windows apps will run on ARM machines. Intel-based Windows 8 machines will run everything. ARM-based Windows 8 machines will run only new compiled-for-ARM apps. In either scenario, there will be some apps that run on Intel-based Windows 8 machines but which don’t run on ARM-based ones.


Normal people do not understand what CPU architectures or binary instruction sets are. There is going to be confusion here either way. But everyone is going to be able to understand the difference between old-style Windows desktop apps and new-style Metro apps. Just look at them.


In the Metro-only for ARM scenario, Metro apps run on all machines, and classic Windows apps run only on Intel machines. In the allow-classic-apps-to-be-recompiled-for-ARM scenario, Metro still runs on all machines, but users need to know what CPU architecture a classic Windows app has been compiled for. So Microsoft’s choice is between (a) asking users to tell the difference between classic and Metro apps, or (b) asking users to tell the difference between classic apps that have been recompiled for ARM and those which are Intel-only.


These CPU transitions are hard. For app developers, it seldom involves just flipping a switch in the compiler. Look at Mac OS X, and the transition to Intel. Even now, six years after the transition was announced, [there are commonly used apps that can’t be used on Lion](http://quicken.intuit.com/support/help/install--register--and-convert/quicken-for-mac-compatibility-with-mac-osx-10-7-lion/GEN83208.html) because they’re still PowerPC (and Lion no longer includes Rosetta).


Apple had another advantage Microsoft will not: in 2006 Apple made a months-long one-way transition. Once started, Intel machines were the new ones, PowerPC machines were the old ones. Non-technical users may not understand the difference between PowerPC and Intel binaries (or Universal binaries that support both architectures), but they do understand that old software eventually stops working.


Microsoft isn’t switching from Intel to ARM; they’re adding ARM as a second supported architecture. The current plan is for brand-new Windows 8 tablets (and perhaps notebooks) next year, some of which are Intel-based and some of which are ARM-based. I think the easiest way to minimize confusion would be to market ARM-based Windows machines as “Metro only”. Intel gets classic Windows and Metro apps, ARM gets Metro.


## ‘Must’ Beats ‘Should’


[As Jesper points out](http://waffle.wootest.net/2011/09/15/armed-with-evidence-to-the-contrary/), Microsoft promises that even on Intel machines which support classic Windows software, if you don’t launch the Windows desktop, none of that code even loads, and you’ll get the performance benefits of Metro’s non-legacy design.


But humans aren’t entirely rational. In an ideal world, that sort of setup would work. Everyone would get on board with Metro as quickly as possible, and the classic Windows desktop would be available when necessary. But developers are human and thus have a natural tendency toward the path of least resistance. Developers are more likely to undertake more work (in this case, completely rewriting and redesigning apps for Metro, instead of merely recompiling classic apps) if they *must* rather than merely *should*.


Consider Flash. Apple ships two platforms, neither of which ships with support for Flash Player: Mac OS X and iOS. On the Mac, users can install Flash themselves. On iOS, they cannot. There are far more websites and online services that have undertaken the work to support iOS with non-Flash solutions — either through the App Store or through open web standards — than there are for the Mac.1


MLB has (excellent) native apps for watching live baseball games on the iPhone and iPad. On the Mac, they require the user to install Flash. Netflix has a good app for the iPhone and iPad. On the Mac, they require the user to install Silverlight. I could list dozens of similar examples.


Microsoft will not (and should not — it’d be suicidal) go Metro-only on all platforms with Windows 8. But if they go Metro-only on a subset of Windows 8 machines — compelling ARM-based ones that offer iPad-esque price and battery-life advantages — it will greatly encourage developers to write Metro apps. The message could be, more or less, “*Windows 8 supports an incredibly wide range of hardware, and Metro runs everywhere. But our most advanced mobile hardware designs are Metro only.*”


Otherwise, too many developers will think, *Why rewrite and redesign my entire app when I can just recompile it for the classic Windows desktop on ARM?*


Microsoft may well go that route, but if they do, I think it will hinder developer support for Metro.


---

1. It’s worth noting that Microsoft faces the same issue with Flash Player on Windows 8. In Metro, IE will not support any plugins, but the desktop version of IE will. Websites will be much more likely to serve web standards-based content to Metro users if they don’t have the option to tell Metro users to switch to the desktop version of IE in order to view Flash content. ↩︎



| **Previous:** | [Metro](https://daringfireball.net/2011/09/metro) |
| **Next:** | [The Fall Event](https://daringfireball.net/2011/09/fall_event) |


PreviousNext