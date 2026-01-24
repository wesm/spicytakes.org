---
title: "Serving at the Pleasure of the King"
date: 2011-10-15
url: https://blog.codinghorror.com/serving-at-the-pleasure-of-the-king/
slug: serving-at-the-pleasure-of-the-king
word_count: 1044
---

I enjoy my iPhone tremendously; I think it’s the most important product Apple has ever created and [one they were born to make](https://blog.codinghorror.com/the-iphone-software-revolution/). As a **consumer** who has waited far too long for the phone industry to get the swift kick in the ass it so richly deserved, I’m entirely on Apple’s side here.


But as a **software developer**, I am deeply ambivalent about an Apple dominated future. Apple isn’t shy about cultivating the experience around their new iOS products and the App Store. There are unusually strict, often mysterious rules around what software developers can and cannot do – at least if they want entry into the App Store. And once you’re in, the rules can and will change at any time. Apple has cracked down several times already:

- [Prohibiting applications that include external mechanisms for purchases](http://money.cnn.com/2011/07/25/technology/apple_kindle/index.htm)
- [Prohibiting applications that have sexual connotations or innuendo](https://web.archive.org/web/20100225080655/http://chillifresh.com/2010/02/20/5000-apps-banned-the-new-rules/)
- [Prohibiting applications with controversial satire](https://web.archive.org/web/20111017161602/http://www.wired.co.uk/news/archive/2011-05/3/smuggle-truck)
- [Prohibiting applications that can potentially be used for unauthorized downloads](https://web.archive.org/web/20111017164345/http://www.wired.co.uk/news/archive/2009-05/12/apple-rejects-iphone-bittorrent-app)


The developers involved are contractually prevented from even *discussing* specifically what happened to them by the terms of the app store. Those frustrating, inconsistent, opaque App Store experiences led developers to coin parodies such as [Apple’s Three Laws of Developers](https://web.archive.org/web/20111020045846/http://yourhead.tumblr.com/post/3320228508/apples-three-laws-of-developers):

1. A developer may not injure Apple or, through inaction, allow Apple to come to harm.
2. A developer must obey any orders given to it by Apple, except where such orders would conflict with the First Law.
3. A developer must protect its own existence as long as such protection does not conflict with the First or Second Law.


It is absolutely clear who is in charge when you submit an application to the App Store. **Apple developers serve at the pleasure of the king**.


![](https://blog.codinghorror.com/content/images/2025/11/Louis_XIV_of_France.jpg)


In Apple’s defense, this is done in the name of protecting the consumers from malicious, slimy, or defective applications. Sort of like [Nintendo’s Seal of Approval](https://en.wikipedia.org/wiki/Nintendo#License_guidelines), I guess.


![](https://blog.codinghorror.com/content/images/2025/04/image-553.png)


The court of the king is a lucrative place to be, but equally dangerous. While upgrading my iPhone to iOS 5 – an *excellent* upgrade, by the way – I was surprised to discover the following blurb in the feature notes:


> Safari Reader displays web articles sans ads or clutter so you can read without distractions. Reading List lets you save interesting articles to peruse later [like the popular Instapaper application], while iCloud keeps your list updated across all your devices.


Apple has since changed the page, but at the time I read it, there was a *direct linked reference* to [Instapaper](http://www.instapaper.com/), the popular “save this webpage to read later” application which Reading List is a clone of. I distinctly remember this mention, because I was shocked that they would be so open and overt about replacing a beloved third-party application. Perhaps it made Apple uncomfortable too; maybe that’s why they pulled the Instapaper text and link.


**If Microsoft added a feature to Windows that duplicated a popular application’s functionality, developers would be screaming bloody murder** and rioting in the, er, blogs and web forums. But in the Mac world, if the king deems it necessary, [then so it must be](http://www.marco.org/2011/06/06/safari-reader-and-instapaper).


> When iOS 5 and Lion ship, Apple will show a much larger percentage of iOS-device owners that saving web pages to read later is a useful workflow and can dramatically improve the way they read.
> If Reading List gets widely adopted and millions of people start saving pages for later reading, a portion of those people will be interested in upgrading to a dedicated, deluxe app and service to serve their needs better. And they’ll quickly find Instapaper in the App Store.


I’ve met Marco Arment, the developer of Instapaper, and I like Marco. He’s even been a guest [on the Stack Exchange podcast](http://blog.stackoverflow.com/2011/06/se-podcast-08/). This is a nice, optimistic interpretation, but the reality is a little scarier. I’m struggling to understand why anyone would buy Instapaper when they can click a button in Safari and have that web page delivered to any of their Macs or iOS devices for later reading via iCloud.


Ah, but wait – what about offline support? Yes, that’s something only Instapaper can deliver! [Or can it?](http://www.marco.org/2011/10/13/ios5-caches-cleaning)


> A common scenario: an Instapaper customer is stocking up an iPad for a long flight. She syncs a bunch of movies and podcasts, downloads some magazines, and buys a few new games, leaving very little free space. Right before boarding, she remembers to download the newest issue of The Economist. This causes free space to fall below the threshold that triggers the [new iOS 5 space] cleaner, which – in the background, unbeknownst to her – deletes everything that was saved in Instapaper. Later in the flight, with no internet connectivity, she goes to launch Instapaper and finds it completely empty.


That’s the problem with kings, you see. **Their rule is absolute law, but they can be capricious, erratic, and impulsive.** If you’re lucky enough to live under the rule of a fair and generous king, then you’ll do well. But historically speaking, monarchies have proven to be… unreliable.


![](https://blog.codinghorror.com/content/images/2025/11/Louis_XIV_of_France-bernard-pras-snacks.jpg)


I tend to agree with Marco that this is, in the big scheme of things, a minor technical problem. A private application cache not subject to iCloud syncing and space limitations would fix it. But it speaks volumes that Marco – a dedicated subject of the king – apparently had no idea this change was coming until it was on top of him. It’s negatively impacting his Instapaper business and his customers. It’s also concerning that this issue wasn’t resolved or at least raised as a serious concern during the lengthy iOS 5 beta. Perhaps Apple’s legendary secrecy is to blame. I honestly don’t know.


As a consumer, I like that Apple is perfectly willing to throw its software developers under a bus to protect me (or, more cynically, Apple itself). But as a software developer, I’m not sure I can cope with that and I am unlikely to ever develop anything for an iOS device as a result. If you choose to deliver software in the Apple ecosystem, this is simply the tradeoff you’ve chosen to make. **Apple developers serve at the pleasure of the king**.

[ios development](https://blog.codinghorror.com/tag/ios-development/)
[apple](https://blog.codinghorror.com/tag/apple/)
[software ecosystem](https://blog.codinghorror.com/tag/software-ecosystem/)
[app distribution](https://blog.codinghorror.com/tag/app-distribution/)
[app store policies](https://blog.codinghorror.com/tag/app-store-policies/)
