---
title: "The Tablet Turning Point"
date: 2014-11-11
url: https://blog.codinghorror.com/the-tablet-turning-point/
slug: the-tablet-turning-point
word_count: 867
---

Remember how people in the year 2000 used to say how crazy and ridiculous it was, the idea that Anyone Would Ever Run Photoshop in a Web Browser? I mean *come on*.


[Oops](https://thenextweb.com/creativity/2014/02/24/9-browser-based-photo-editing-tools/).


One of my big bets with [Discourse](https://www.discourse.org/) is that eventually, [*all* computers will be tablets](https://blog.codinghorror.com/the-pc-is-over/) of varying size, with performance basically indistinguishable from a two year old desktop or laptop.


[Apps are great and all](https://blog.codinghorror.com/app-pocalypse-now/), but there has to be some place for this year’s bumper crop of obscene amount of computing superpower to go. I like to use history as my guide, and I believe it’s going exactly the same place it did on desktops and laptops – that no-installing-anything friend of every lazy user on the planet, the inevitable path of least resistance, the **mobile web browser**.


![](https://blog.codinghorror.com/content/images/2025/02/image-118.png)


For the last few years, I’ve been buying every significant tablet device in the run up to the big holiday sales season, and testing them all, to see how many years are left until mobile devices catch up to desktops on general web and JavaScript performance.


How are we doing? Let’s benchmark some Discourse client-side [Ember](http://emberjs.com/) JavaScript code:

kg-card-begin: html


| iPhone 4 | June 2011 | 2031ms |
| iPhone 5 | Sept 2012 | 600ms |
| iPhone 5s | Sept 2013 | 300ms |
| iPhone 6 | Sept 2014 | 250ms |
| iPad Air 2 | Oct 2014 | 225ms |


kg-card-end: html

My Core i4770k desktop machine scores **180ms** in the same benchmark on the latest version of Chrome x64. I’d say we’re solidly within striking distance this year.


I don’t like to spend a lot of time talking about news and gadgets here, since the commentary will be irrelevant within a few years. But this year marks a key turning point for mobile and tablet performance, and I’ve lived with every iteration of these devices for the last couple of years, so I’ll make an exception.


Look at this [performance rampage](https://www.anandtech.com/show/8666/the-apple-ipad-air-2-review/3) the **iPad Air 2** goes on:


![](https://blog.codinghorror.com/content/images/2014/11/69018.png)


Just look at it! All the graphs are like this!


It’s hard to believe we now live in a world where the Apple “Premium” is no longer about aesthetics, but raw, unbridled, class-leading performance. And you know what? That’s something I can totally get behind.


Anyone who tells you the iPad Air 2 is some kind of incremental update must not actually use theirs. As someone who *does* regularly use his iPad, I can say without hesitation that this is a massively upgraded device. I grew to hate my old iPad Air because of the memory restrictions; I could barely have three tabs open in Mobile Safari without one of them paging out of memory. Thanks x64 and iOS7!


The bonded screen, touchid, the now-adequate-for-x64 2GB of RAM, the amazingly fast triple core CPU, the GPU, and yeah, it’s a little thinner. For performance, nothing else even comes close.


It’s so fast I sometimes forget I’m not using my [Surface Pro 3](https://www.microsoft.com/surface/en-us/products/surface-pro-3) with its 4GB RAM and Core i5 CPU. I get hassled when I bring my Surface to meetings, but I patiently explain that it’s a very nice third gen hardware design with a fully integrated keyboard cover, IE11 is a great touch browser, and that I’m mostly using the device as a tablet, as a sneak preview of what iPad 8 performance will look like. Based on today’s benchmarks with the iPad Air 2 – chronologically, the iPad “6” – I believe that’s about right.


I also purchased a [Nexus 9](https://www.amazon.com/Google-Nexus-Tablet-8-9-Inch-Black/dp/B00M6UC5B4). It’s the first device to ship with Android 5 and the vaunted Nvidia Tegra K1.


![](https://blog.codinghorror.com/content/images/2014/11/nexus-9-1.jpg)


I’m *very* impressed with Android 5.0; aesthetically I think it’s superior to iOS 8 in a lot of ways, and it is a clear step forward over Android 4. Anyone on older Android devices should definitely upgrade to Android 5 at their first opportunity.


Performance-wise, it is what I’ve come to expect from Android: [erratic](https://www.anandtech.com/show/8670/google-nexus-9-preliminary-findings/2). In our Discourse benchmarks, and the latest version of Chrome Android beta, it scores about 750ms, putting it somewhere between the 2011 iPhone 4s and the 2012 iPhone 5. That said, this is the fastest Android device I have ever laid hands on. I just wish it was consistently faster. A lot faster.


To that end, I’d like to ask for your help. We’ve identified some deep [bugs in the Android Chrome V8](https://web.archive.org/web/20150519151729/https://code.google.com/p/v8/issues/detail?id=2935) engine that cause fairly severe performance issues with JavaScript frameworks like Angular and Ember. (Desktop Chrome performance remains class leading; this is highly specific to the Android version of Chrome.) If you know anyone at Google, please ping them about this and see if it can be escalated. I’d love it if more Android users – including me – could have a better browser experience when using large JavaScript apps.


I hope over the next year the remaining Android 5 performance bumps can be ironed out. I still like the Nexus 9; if you’re a big fan of Google services like GMail, Docs, and Maps like I am, I definitely recommend it. The one I have will be a gift to my mom.

[mobile devices](https://blog.codinghorror.com/tag/mobile-devices/)
[tablets](https://blog.codinghorror.com/tag/tablets/)
[web performance](https://blog.codinghorror.com/tag/web-performance/)
[computing trends](https://blog.codinghorror.com/tag/computing-trends/)
[technology evolution](https://blog.codinghorror.com/tag/technology-evolution/)
