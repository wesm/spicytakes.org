---
title: "Masquerading as Mobile Safari to Get Websites to Serve HTML5 Video to Safari on Mac OS X"
date: 2010-11-12
url: https://daringfireball.net/2010/11/masquerading_as_mobile_safari
slug: masquerading_as_mobile_safari
word_count: 996
---


## The iPad User Agent String Trick


First, some practical advice. In my piece last week [about uninstalling Flash Player from Mac OS X](http://daringfireball.net/2010/11/flash_free_and_cheating_with_google_chrome), I suggested using Chrome as a fall-back for viewing Flash content when you need it. This works because Chrome uses its own self-contained version of Flash, not the system-wide version. This works, but I’ve since found an even better workaround for Safari.


First, make sure you’ve turned on Safari’s Develop menu. (It’s a checkbox in the “Advanced” panel of Safari’s preferences window.) Then, whenever you run into a video player that claims to require Flash Player, invoke the Develop → User Agent → Mobile Safari 3.2.2 — iPad command. This reloads the current page, but with Safari claiming to be Mobile Safari running on the iPad. It does not change the way that Safari renders the page — i.e., it doesn’t make the desktop Safari render pages with zooming or layout differences to mimic the way Mobile Safari renders pages on the iPad. All it does is tell Safari to identify itself as Mobile Safari to the server. The result is that if the server does any sort of user-agent detection to figure out whether to serve video using Flash or HTML5, you’ll get the HTML5 version. (Wikipedia provides [a good layman’s overview](http://en.wikipedia.org/wiki/User_agent) of user agent strings.)


This trick makes video work in Safari on Mac OS X — with no Flash — from Flickr, Vimeo embeds, TED, MSNBC, and probably any other site that offers video that works on the iPad. This doesn’t work for *all* video, but it should work for any video that works on the iPad.


I’ve set a custom keyboard shortcut for this menu command in System Preferences. [Here’s a screenshot showing how to set it up.](https://daringfireball.net/misc/2010/11/safari-custom-shortcut.png) Note that the menu title is just “Mobile Safari 3.2.2 — iPad”. Even though it’s in a sub-menu, you don’t need to list the hierarchy of menus, just the name of the menu item itself, no matter how far nested it is. You *do* need to get the name of the menu item exactly right, however. Copying and pasting it from the sentence earlier in this paragraph should work.


When you switch the user agent string like this in Safari, it only persists for that particular window. Other windows still identify themselves as Safari on Mac OS X. You *can* set a permanent custom user agent string for Safari, but it requires the `defaults` command line tool. I don’t recommend this — it breaks other things, unrelated to Flash1 — but [here’s the command](http://snipt.net/binaryghost/change-safari-useragent-to-ipad/). (You can undo it by typing “`defaults delete com.apple.safari CustomUserAgent`” at the command line.)


That this works for so many sites shows that Safari on Mac OS X is perfectly capable of playing a lot of video on the web that seemingly requires Flash. Web developers should start serving video via the HTML5 `<video>` tag by default, [and fall back to Flash if the `<video>` tag isn’t supported](http://henriksjokvist.net/archive/2009/2/using-the-html5-video-tag-with-a-flash-fallback). If it works on the iPad without Flash, it should work on a Mac without Flash.


## The Politics


This is not about politics, or any sort of idealism about how things should be. I’ve removed Flash from my system, and suggest you do the same, because of two facts:

1. Without Flash installed, my Mac uses less ambient CPU power. The machine runs cooler, faster, and the battery lasts longer.
2. Video that plays back via the HTML5 video tag instead of Flash Player is smoother and uses less power. My MacBook Pro’s fan almost always kicks in when I play 720p video via Flash. It almost never kicks in when I play 720p video without Flash.


Those two facts are beyond dispute.


I am not assigning blame here. Maybe you think that this is Adobe’s fault — that Flash Player is junky software. Maybe you think that it’s Apple’s fault — that Mac OS X doesn’t provide the sort of APIs that a browser plugin like Flash needs to run more efficiently and take advantage of hardware H.264 decoding. There are also many different political arguments to be made — about Apple leveraging its control to marginalize a competing company’s platform, or about Flash being a closed-source proprietary platform with a single implementation. Several people — e.g. [here](http://simurai.com/post/1520282329/html5-ads), and [here](http://www.google.com/buzz/dclinton/4ETfPTVe1Vz/The-best-solution-I-found-is-to-use-a-flash) — argue that even if Flash goes away, its use in web advertising will be replaced by HTML5 animation, and that such animation could use just as much CPU time and consume as much battery life as Flash does today — and, even worse, might be harder to block than Flash is today.


I have opinions on who’s to blame technically. I have opinions on the politics. I disagree that HTML5 animation will suffer the same performance issues that Flash does today. (The argument that there’s no use getting rid of Flash *today* because HTML5 animation might be just as big a problem *in the future* reminds me of the sort of people who argue that there’s no use switching from Windows to Mac OS X to avoid malware because if everyone did it, the malware makers might switch to targeting Mac OS X.) But those things are all beside the point. What I’m arguing here is about practical advantages, right now, today. Two facts: (1) longer battery life and lower ambient CPU usage, and (2) better video playback.


Both Safari and my entire computer as a whole run better today than they did before I uninstalled Flash. Uninstall Flash on your Mac and see for yourself.


---

1. A few of the problems I noticed after setting Safari to masquerade as iPad Mobile Safari all the time: links to the iTunes store broke, and [TypeKit](http://typekit.com/) web fonts broke. Also, many sites, like Gmail, will default to serving you an iPad-optimized layout instead of the “regular” layout. ↩︎



| **Previous:** | [Apple’s Pricing Advantage](https://daringfireball.net/2010/11/apples_pricing_advantage) |
| **Next:** | [Where Are the Android Killer Apps?](https://daringfireball.net/2010/11/where_are_the_android_killer_apps) |


PreviousNext