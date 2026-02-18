---
title: "It’s a Core Location Blacklist"
date: 2008-08-08
url: https://daringfireball.net/2008/08/core_location_blacklist
slug: core_location_blacklist
word_count: 419
---


Yesterday [I linked](http://daringfireball.net/linked/2008/08/06/blacklist) to a story about the discovery by Jonathan Zdziarski of a remote blacklist Apple is maintaining, supposedly, according to Zdziarski, to remotely disable rogue iPhone apps previously distributed through the App Store. [Dozens of other weblogs](http://blogsearch.google.com/blogsearch?hl=en&ie=UTF-8&q=Zdziarski+iphone&as_maxm=8&as_miny=2008&as_maxy=2008&as_minm=8&as_mind=5&as_maxd=7&as_drrb=b&ctz=240&c1cr=8%2F5%2F2008&c2cr=8%2F7%2F2008&btnD=Go) and [news sites](http://news.google.com/news?hl=en&ned=us&q=jonathan+zdziarski+blacklist&ie=UTF-8&as_drrb=q&as_qdr=w&as_mind=31&as_minm=7&as_maxd=7&as_maxm=8&nolr=1) have picked up the story.


But the story seems fishy. Here’s the entirety of the message [iPhone Atlas reported](http://www.iphoneatlas.com/2008/08/06/iphone-can-phone-home-and-kill-apps/) getting from Zdziarski:


> This suggests that the iPhone calls home once in a while to find out
> what applications it should turn off. At the moment, no apps have
> been blacklisted, but by all appearances, this has been added to
> disable applications that the user has already downloaded and paid
> for, if Apple so chooses to shut them down.
> I discovered this doing a forensic examination of an iPhone 3G. It
> appears to be tucked away in a configuration file deep inside
> Core Location.


It’s easy to see how the story got legs. Zdziarski is the author of two iPhone books — [one](http://www.amazon.com/exec/obidos/asin/0596518552/ref=nosim/daringfirebal-20) on jailbreak app development, and the upcoming *[iPhone Forensics](http://oreilly.com/catalog/9780596153892/)* from O’Reilly. And it’s no secret that Apple has promoted security as one of the benefits of the centralized, DRM-dependent App Store distribution model. Back in March when the App Store was announced, [here’s what Macworld reported](http://www.macworld.com/article/132424/2008/03/iphone_software_faq.html):


> Since each iPhone program will be digitally signed by its creator,
> this gives Apple the ability to “turn off the spigot,” as Steve
> Jobs put it, and revoke programs that don’t meet its standards.


So there may well be some sort of kill switch that Apple can deploy to remotely disable an app that’s already installed. But this list is not it.


Apple has no reason to hide such a configuration in a sneaky place. If it’s “tucked away in a configuration file deep inside” the Core Location framework, doesn’t it seem more likely that this list has something to do with, say, Core Location? Even the URL of the file in question hints at this:


`https://iphone-services.apple.com/clbl/unauthorizedApps`


An informed source at Apple confirmed to me that the “clbl” in the URL stands for “Core Location Blacklist”, and that it does just that. It is not a blacklist for disabling apps completely, but rather specifically for preventing any listed apps from accessing Core Location — an API which, for obvious privacy reasons, is covered by very strict rules in the iPhone SDK guidelines.



| **Previous:** | [Is the iPhone NDA About Patents?](https://daringfireball.net/2008/08/iphone_nda_patents) |
| **Next:** | [Memoranda](https://daringfireball.net/2008/08/memoranda) |


PreviousNext