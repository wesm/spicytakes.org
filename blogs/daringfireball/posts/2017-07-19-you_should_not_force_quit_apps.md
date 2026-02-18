---
title: "Public Service Announcement: You Should Not Force Quit Apps on iOS"
date: 2017-07-19
url: https://daringfireball.net/2017/07/you_should_not_force_quit_apps
slug: you_should_not_force_quit_apps
word_count: 1070
---


The single biggest misconception about iOS is that it’s good digital hygiene to force quit apps that you aren’t using. The idea is that apps in the background are locking up unnecessary RAM and consuming unnecessary CPU cycles, thus hurting performance and wasting battery life.


That’s not how iOS works. The iOS system is designed so that *none* of the above justifications for force quitting are true. Apps in the background are effectively “frozen”, severely limiting what they can do in the background and freeing up the RAM they were using. iOS is really, really good at this. It is so good at this that unfreezing a frozen app takes up *way* less CPU (and energy) than relaunching an app that had been force quit. Not only does force quitting your apps not help, it actually *hurts*. Your battery life will be worse and it will take much longer to switch apps if you force quit apps in the background.


[Here’s a short and sweet answer from Craig Federighi](https://www.macrumors.com/2016/03/10/force-quitting-apps-doesnt-help-battery/), in response to an email from a customer asking if he force quits apps and whether doing so preserves battery life: “No and no.”


Here, from the official support document on forcing applications to close, is [Apple’s own advice on *when* to use this feature](https://support.apple.com/en-us/HT201330):


> When you double-click the Home button, your recently used apps
> appear. The apps aren’t open, but they’re in standby mode to help
> you navigate and multitask. You should force an app to close only
> when it’s unresponsive.


**Update:** [MacDailyNews quotes a 2010 email from Steve Jobs](https://macdailynews.com/2010/06/29/steve_jobs_on_ios_multitasking_just_use_it_as_designed_and_youll_be_happy/):


> Just use [iOS multitasking] as designed, and you’ll be happy. No
> need to ever quit apps.


Just in case you don’t believe Apple’s senior vice president for software, Apple’s own official support documentation, or Steve Jobs, here are some other articles pointing out how this habit is actually detrimental to iPhone battery life:

- Fraser Speirs (back in 2012!): “[Misconceptions About iOS Multitasking](http://www.speirs.org/blog/2012/1/2/misconceptions-about-ios-multitasking.html)”
- Thorin Klosowski: “[Quitting All Your Apps in iOS Can Actually Worsen Battery Life](https://lifehacker.com/quitting-apps-in-ios-actually-worsens-battery-life-1560086834)”
- Kendall Baker: “[Stop Force Quitting Your iPhone Apps](https://medium.com/@kendallbaker/stop-force-quitting-your-iphone-apps-eb13d86caaa5)”
- The Wirecutter: “[What You Should (and Shouldn’t) Do to Extend Your Phone’s Battery Life](http://thewirecutter.com/blog/what-you-should-and-shouldnt-do-to-extend-your-phones-battery-life/#myth-close-quit-unused-apps)”
- Kyle Richter: “[The Force Quit Fallacy](http://martiancraft.com/blog/2016/02/force-quit-2/)”


This thing about force quitting apps in the background is such a pernicious myth that I’ve heard numerous stories from DF readers [about Apple Store Genius Bar staff recommending it to customers](https://twitter.com/schwa/status/152425874581491712). Those “geniuses” are anything but geniuses.


It occurs to me that some of the best examples *proving* that this notion is wrong (at least in terms of performance) are YouTube “speed test” benchmarks. There’s an entire genre of YouTube videos devoted to benchmarking new phones by running them through a series of apps and CPU-intensive tasks repeatedly, going through the loop twice. Once from a cold boot and the second time immediately after the first loop. [Here’s a perfect example, pitting a Samsung Galaxy S8 against an iPhone 7 Plus](https://www.youtube.com/watch?v=pn-2B82B1mg). Note that no apps are manually force quit on either device. The iPhone easily wins on the first loop, but where the iPhone really shines is on the second loop. The S8 has to relaunch all (or at least almost all) of the apps, because Android has forced them to quit while in the background to reclaim the RAM they were using. On the iPhone, all (or nearly all) of the apps re-animate almost instantly.


In fact, apps frozen in the background on iOS unfreeze so quickly that I think it actually helps perpetuate the myth that you should force quit them: if you’re worried that background apps are draining your battery and you see how quickly they load from the background, it’s a reasonable assumption to believe that they never stopped running. But they did. They really do get frozen, the RAM they were using really does get reclaimed by the system, and they really do unfreeze and come back to life that quickly.1


An awful lot of very hard work went into making iOS work like this. It’s a huge technical advantage that iOS holds over Android. And every iPhone user in the world who habitually force quits background apps manually is wasting all of the effort that went into this while simultaneously wasting their own device’s battery life and making everything slower for themselves.


This pernicious myth is longstanding and seemingly will not die. [I wrote about it at length back in 2012](https://daringfireball.net/2012/01/ios_multitasking):


> Like with any voodoo, there are die-hard believers. I’m quite
> certain that I am going to receive email from people who will
> swear up-and-down that emptying this list of used applications
> every hour or so keeps their iPhone running better than it would
> otherwise. Nonsense.
> [As Fraser mentions](http://www.speirs.org/blog/2012/1/2/misconceptions-about-ios-multitasking.html), yes, there are exceptional situations where an
> app with background privileges can get stuck, and you need to kill
> that app. The argument here is not that you should never have to
> kill any app using the multitasking switcher — the argument is
> that you don’t need to do it on a regular basis, and you’re not
> making anything “better” by clearing the list. Shame on the
> “geniuses” who are peddling this advice.


And don’t even get me started on people who completely power down their iPhones while putting them back into their pockets or purses.


---

1. The other contributing factor to believing that force quitting is good for your iPhone are the handful of apps that have been found to be repeated abusers of loopholes in iOS, such that they really do continue running in the background, wasting battery life. Most infamously, Facebook was caught playing silent audio tracks in the background to take advantage of APIs that allow audio-playing apps to play audio from the background. [They called it a “bug”](https://techcrunch.com/2015/10/22/facebook-says-it-fixed-a-bug-that-caused-silent-audio-to-vampire-your-iphone-battery/). In those cases force-quitting the apps really did help, and I see no reason to trust Facebook. So if you want to keep force quitting Facebook, go right ahead. But don’t let one bad app spoil the whole barrel. The Battery section in the iOS Settings app can show you which apps are actually consuming energy in the background — tap the clock icon under “Battery Usage” and don’t force quit any app that isn’t a genuine culprit. ↩︎



| **Previous:** | [iPhone Prelude](https://daringfireball.net/2017/07/iphone_prelude) |
| **Next:** | [Unordered Lists in Markdown](https://daringfireball.net/2017/07/unordered_lists_in_markdown) |


PreviousNext