---
title: "More on PastryKit"
date: 2009-12-17
url: https://daringfireball.net/2009/12/more_on_pastrykit
slug: more_on_pastrykit
word_count: 1021
---


A bit more regarding [PastryKit](http://daringfireball.net/2009/12/pastrykit), Apple’s web framework for creating iPhone web apps with a look and feel very close to that of native iPhone apps.


## Apple’s Various JavaScript Frameworks


Jonathan “Wolf” Rentzsch posted [this terrific overview](http://rentzsch.tumblr.com/post/286536824/apples-myriad-javascript-frameworks) of the known JavaScript frameworks in use by various teams at Apple today. Some are public. Others, like PastryKit, are not. There’s a bit of overlap between them; in particular, several of them are very much patterned after Cocoa, not just in terms of MVC, but right down to details like class names. (I hadn’t heard of [Gianduia](http://lists.apple.com/archives/Webobjects-dev/2009/Nov/msg00296.html) before, but it [seems very deep](http://news.ycombinator.com/item?id=670244). Apple’s online retail team is using it for things like the [Genius Bar reservation system](http://concierge.apple.com/geniusbar/R206).)


But PastryKit is the only one that’s specifically targeted at building native-style iPhone user interfaces. Of the others, one does seem closely related to PastryKit: [TuneKit](http://www.apple.com/itunes/lp-and-extras/), the now-public framework for building iTunes LP and iTunes Extras content bundles. About 40 percent of the code in PastryKit and TuneKit is identical (if you discount the difference between the “PK” and “TK” class name prefixes). DF reader [Greg Sadetsky](http://gregsadetsky.com) emailed with the following comparison, after running the code through a prettifier to de-minimize it. First, this from PastryKit:


```
const PKTransitionDefaults = {
    duration: 0.5, delay: 0,
    removesTargetUponCompletion: false,
    revertsToOriginalValues: false
};
const PKTransitionStyles = [
    "-webkit-transition-property", 
    "-webkit-transition-duration",
    "-webkit-transition-timing-function",
    "-webkit-transition-delay",
    "-webkit-transition"
];

```


And then this identical-but-for-the-PK/TK-prefixes bit from TunesKit:


```
const TKTransitionDefaults = {
    duration: 0.5, delay: 0,
    removesTargetUponCompletion: false,
    revertsToOriginalValues: false
};
const TKTransitionStyles = [
    "-webkit-transition-property", 
    "-webkit-transition-duration",
    "-webkit-transition-timing-function",
    "-webkit-transition-delay",
    "-webkit-transition"
];

```


Et cetera. Either PastryKit and TuneKit are sibling projects, or they’re the work of the same person. (Also, [Daniel Dilger found references to “PastryKit”](http://www.roughlydrafted.com/2009/09/14/new-itunes-lp-and-extras-built-using-tunekit-framework-aimed-at-apple-tv/) in the *Wall-E* iTunes Extras bundle back in September.)


## iDisk Help


A few readers emailed to point out another instance of PastryKit in action: the help pages for the iDisk app for iPhone OS. If you have the iDisk app from the App Store installed, you can see this by tapping “Settings”, then “iDisk Help”. Looks just like the rest of the app, but there are a few tell-tale signs that it’s PastryKit running in a full-screen web view (e.g. tapping on the status bar doesn’t scroll to the top).


## Is PastryKit a Leftover From the Pre-SDK Days?


One common question I’ve seen (for one example, [in this Hacker News thread](http://news.ycombinator.com/item?id=997508)) is whether PastryKit could be a leftover from the “web apps are a really sweet solution to creating iPhone software” days. I’d say no. For one thing, there’s always been a user guide, and as I recall, the guide has always sort of basically followed the look-and-feel of a native app, but this current version for iPhone OS 3 is much better. In fact, if you set your user agent in Safari to MobileSafari 2 (rather than 3) and then load the [User Guide](http://help.apple.com/iphone/) you get an older version from iPhone OS 2.0, and it is far less impressive technically. No scrolling magic, no iPhone-style blue gradients when highlighting selected list rows, etc. Further, PastryKit takes advantage of features in mobile WebKit that were only added in iPhone OS 3.0. PastryKit is new.


## Apple’s Take on Web Apps Competing With the App Store


Lastly, there’s the question of how concerned Apple is, strategically, that a robust web app API and market would take away from the App Store. And if so, are they worried about the money? I’d guess probably not. I don’t think Apple’s 30 percent cut of App Store revenue is anything to sneeze at, and it’s growing fast. But there’s no question that the App Store exists to sell iPhones and iPod Touches, not the other way around.


A bigger concern might be the fact that web apps are cross-platform. Apple is currently using user-agent detection to prevent its PastryKit user guide apps from loading on anything other than MobileSafari, but I don’t think there’s any technical reason why these apps wouldn’t work just fine, and look almost the same, on both Android and WebOS. The font would be slightly different, since neither of those ship with Helvetica, but otherwise it’d look just like an iPhone app.


Cutting edge web development never seems to “just work” across different browsers, but these three — iPhone, Android, WebOS — are all based on the same WebKit rendering core. And even if per-platform tweaks are required, surely it’d be far less work than to develop separate native apps using the fundamentally different Cocoa Touch, Android, and [Mojo](http://developer.palm.com/) APIs.


I would hope Apple isn’t concerned about this. For one thing, desktop-targeted web apps haven’t dampened demand for Macs. If anything, the Mac has *thrived* as the web has replaced Windows as the most widespread software platform. I think Apple would do well to encourage web apps for *cross-platform* mobile software, and that doing so would not slow interest in native Cocoa Touch development for performance (especially games) and access to hardware (like the camera) not available to web apps. I also think it would benefit both iPhone users and Apple itself to have no-approval-necessary web apps thrive as an alternative to the tightly-controlled App Store.1 It’s human nature to [emphasize conflict and drama](http://scobleizer.com/2009/12/16/iphone-developers-abandoning-app-model-for-html5/), but there’s no reason why native iPhone apps *and* iPhone-optimized web apps can’t both be thriving, growing platforms.


But, well, [we don’t know](http://stevenf.tumblr.com/post/277830536/slightly-longer-version-of-a-tweet-from-this).


---

1. That’s not to say more capable web app APIs would be a panacea for all that ails the App Store. For one thing, many of the apps that Apple has blocked from the App Store couldn’t technically be reproduced as web apps. Google Voice, to name the most infamous example. For another, it isn’t much solace to a developer who just created an entire working native iPhone app in Cocoa Touch to be told that their work will not be published in the App Store but that they’re free to recreate the app from scratch using entirely different APIs and technologies. ↩︎



| **Previous:** | [PastryKit](https://daringfireball.net/2009/12/pastrykit) |
| **Next:** | [Why the HTML5 ‘Video’ Element Is Effectively Unusable, Even in Browsers Which Support It](https://daringfireball.net/2009/12/html5_video_unusable) |


PreviousNext