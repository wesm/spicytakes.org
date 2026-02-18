---
title: "Mobile Multitasking"
date: 2010-04-14
url: https://daringfireball.net/2010/04/mobile_multitasking
slug: mobile_multitasking
word_count: 1783
---


Daniel Eran Dilger [at Apple Insider](http://www.appleinsider.com/articles/10/04/09/apples_prohibition_of_flash_built_apps_in_iphone_4_0_related_to_multitasking.html):


> Other platforms have enabled multitasking by simply allowing any
> number of apps to run. This results in a mess for users because
> it’s up to them to manage which apps are running out of control or
> needlessly chewing up resources in the background. Android and
> Windows Mobile are both notorious for needing TasKiller or some
> other sort of manual process manager to keep battery life and
> performance in check.


I believe he’s right about Windows Mobile, but that’s no matter because Microsoft has abandoned Windows Mobile, and Windows Phone 7 will apparently ship with no multitasking, and, whenever multitasking eventually does appear in Windows Phone, it won’t be like that. But Dilger is flat-out wrong about Android. Shooting fish in a barrel, I know, but I think it’s worth clarifying this. If you want to understand the current mobile landscape, it’s essential to understand that, in broad terms, what Apple has unveiled for iPhone OS 4 is pretty similar to Android’s multitasking model. In both iPhone OS 4 and Android, users should never need to quit apps manually — when the system runs low on memory, it automatically quits least-recently-used background apps to free up more.


Now, it’s true that there *are* [task manager apps in the Android Market](http://www.google.com/search?q=android+market+task+killer). But they are not necessary. The Android system doesn’t come with one and doesn’t need one. And I strongly suspect that Google’s Android team is annoyed that these task manager apps are in the market, because their existence creates the impression that they’re necessary or useful. I’ve spent a few weeks on a Nexus One, and background apps don’t slow the system down and don’t need to be quit manually.


There are a lot of things I like better about the iPhone than Android. The multitasking architecture, however, has been an Android advantage, and iPhone OS 4, I think, will pretty much put them on equal footing in this regard. There *are* technical differences, [but they’re small differences](http://blog.rlove.org/2010/04/iphone-os-4-and-multitasking.html), not big ones.


On both Android and iPhone OS 4, non-frontmost apps can run, but in limited fashions, in the background. It’s not like on Mac OS X or Windows where background apps continue to run exactly as though they’re in the foreground. On iPhone OS 4, apps in the background — those that support “fast application switching” in Apple’s parlance — are effectively *paused*. They’re still in RAM, but they can’t get large amounts of CPU time. What they can do, though, is use a limited number of APIs from the system to perform certain tasks — the two examples so far are play audio (Pandora) and receive/maintain VOIP calls (Skype).


One can argue about which platform, Android or iPhone OS 4, has the better multitasking system. Maybe Android’s system is still better; my hunch is that Android allows background apps more freedom. Maybe the iPhone’s system is better; there are some fascinating technical details, like how [blocks and Grand Central Dispatch](http://developer.apple.com/mac/articles/cocoa/introblocksgcd.html) are now available for concurrent and background tasks. (Whatever you think of iPhone OS 4’s multitasking model, don’t make the mistake of thinking it’s simple; this is state of the art computer science.)1 In the end, I suspect opinion on the differences between Android and iPhone multitasking will fall along the same lines of the general question of Android-vs.-iPhone — Android offers a bit more freedom to developers, iPhone is more controlled and orderly, and tries to guarantee a more responsive system for the user.


But the differences in multitasking between the two are arguments about fine details, not the big picture.


## The New Priorities


The big difference is the jump from traditional operating systems. On traditional systems like Mac OS X and Windows, the fundamental idea behind a process is that once running, it will stay running until the process itself quits. On desktop systems like the Mac and Windows, that typically means that the user tells the app to quit (or, in Windows vernacular, “exit” — same thing). The user can do something like invoke the system-wide “Shut Down” or “Log Out” command, and then the system will send a quit event to all running applications — but that’s still managed by the user. It’s a way for the user to tell all apps to quit at once. And even then, it’s still up to each app to do whatever it wants on its way to quitting. It’s a *suggestion* to quit. All Mac users are familiar with the “Hey, this app can’t quit immediately, you’ve got documents open with unsaved changes” dialog box.


In this traditional model, if an app isn’t ready to quit, it can refuse to. Or, if it needs to run through a lengthy minute-long save operation upon quitting, it can do so. Yes, you can force-quit apps in any such operating system, but when you do, it’s more akin to forcing the app to crash. When you force-quit an app on the Mac, it’s abnormal.


It’s also the case that OSes such as Mac OS X, Windows, and desktop Linux use [swap](http://en.wikipedia.org/wiki/Swap_space) — when physical RAM runs low, the operating system will start paging chunks of memory to storage on disk. Relative to each other, RAM is fast and expensive; storage is slow but cheap. The tradeoff with swap is that you get to pretend your machine has more RAM than it really does, but it’s far slower than using only real RAM.


Mac OS X will never, in practical use, “run out of memory”. If you keep opening more and more applications and documents, it will slow down, using more and more swap. Eventually it will slow down to the point where it’s unusable. But it will not report running out of memory. The deal is: you launch an app, it’ll run, and it’ll stay running until it (the app) is ready to quit, memory (and responsiveness) be damned.


The new model, exemplified by mobile systems like the iPhone and Android, is that apps are not quit manually by the user. You, the user, just open them, and the system takes care of managing them after that. You don’t even have to understand the concept of quitting an application — in fact, you’re better off not worrying about it. There is no swap, so when memory runs low, something has to give. If the app is frontmost, it is running. If it is not frontmost, it might continue to run in limited fashion, but the system might pull the plug on it at any moment to reclaim its memory.


The original Mac OS — the one from the 1980s — also lacked swap. When it ran low on memory, it would simply refuse to launch more applications. You’d get a dialog box telling you there was not enough free memory to launch the app, and that you, the user, needed to quit other running applications to free additional memory.


The new way is to rethink the fundamental deal for processes. In the old model, processes that have already been launched get priority — once running, they stay running. In the new model, the user’s intentions get priority. You press the home button, you’re going to see the home screen in a moment, whether the app that was running was ready to be closed or not. If you want to open another app, it’s going to open immediately, even if the system has to pull the plug on an app in the background to free enough RAM.


On iPhone and Android, apps don’t decide when to quit. They must be ready to quit on short notice at any time. In current versions of iPhone OS, third-party apps are quit when the user hits the home button. The user is free to hit the home button at any time. The system effectively tells the frontmost app, “OK, you’re done” and the app has a few moments to save state or clean up. But after those moments, if the app is still busy, too bad — the system kills it.


And even with iPhone OS 4’s “multitasking”, apps must be ready to quit at any time on a moment’s notice. When the system runs low on free RAM, it will start quitting apps that are open in the background, and when it does so, it will not wait around for them to “do something”.2 The same is true for Android. This is a fundamental change to how multitasking systems work. It works because the apps for these systems have been written from the ground up to embrace this model.


It may well be that this model is temporary — that it’s a factor of the relatively restrictive amounts of RAM in these devices. At some point not too many years from now, we’ll have iPhones and iPads and Android devices with gigabytes of RAM, rather than megabytes, and at that point, we may well return to a more persistent model of multitasking. But in the short term, this is not going to change. And no matter how much RAM future devices contain, it’s never again going to be acceptable to make users wait before launching or switching contexts.


In the traditional model, the primary priority is keeping everything open. In this new model, the primary priority is that the system must always be responsive to the user. There is no waiting for swap. There are no slowdowns caused by background processes using significant amounts of CPU time.


You know what iPhone OS is missing that Mac OS X has? [The SPOD](http://en.wikipedia.org/wiki/Spinning_wait_cursor).


---

1. When Apple introduced blocks and Grand Central Dispatch, they pitched it primarily as their answer to the problem of how to deal with a world where computers are getting “faster” by adding more concurrent cores rather than simply doubling in speed every 18 months. GCD is useful for concurrent programming on single-core systems such as all current iPhone OS devices, but adding GCD to iPhone OS 4 gets my mind wondering about, say, a multi-core version of the A4 processor. (And I suspect the iPhone OS 4 kernel is pretty similar to the Snow Leopard kernel.) ↩︎
2. In fact, on iPhone OS 4, I believe that background apps don’t even get a moment’s warning before they’re killed. If an app wants to save state, it must do so immediately after the system informs it that it is going into the background. Once it is *in* the background, it won’t get a warning before it’s killed. ↩︎



| **Previous:** | [A Brief Review of Opera Mini for iPhone](https://daringfireball.net/2010/04/opera_mini_review) |
| **Next:** | [It’s Not the Control, It’s the Secrecy](https://daringfireball.net/2010/04/not_the_control_the_secrecy) |


PreviousNext