---
title: "An Exercise Program for the Fat Web"
date: 2019-05-30
url: https://blog.codinghorror.com/an-exercise-program-for-the-fat-web/
slug: an-exercise-program-for-the-fat-web
word_count: 1349
---

When I wrote about [App-pocalypse Now](https://blog.codinghorror.com/app-pocalypse-now/) in 2014, I implied the future still belonged to the web. And it does. But it’s also true that the web has changed a lot in the last 10 years, much less the last 20 or 30.


![](https://blog.codinghorror.com/content/images/2025/02/image-262.png)


Websites have gotten a lot… *fatter*.


While I think it’s irrational to pine for the bad old days of [HTML 1.0 websites](http://info.cern.ch/), there are some legitimate concerns here. The best summary is Maciej Cegłowski’s, [The Website Obesity Crisis](http://idlewords.com/talks/website_obesity.htm):


> To channel a famous motivational speaker, I could go out there tonight, with the materials you’ve got, and rewrite the sites I showed you at the start of this talk to make them load in under a second. In two hours.
> Can you? Can you?
> Of course you can! It’s not hard! We knew how to make small websites in 2002. It’s not like the secret has been lost to history, like Greek fire or Damascus steel.
> But we face pressure to make these sites bloated.
> I bet if you went to a client and presented a 200 kilobyte site template, you’d be fired. Even if it looked great and somehow included all the tracking and ads and social media crap they insisted on putting in. It’s just so far out of the realm of the imaginable at this point.


The whole article is essential; you should stop what you’re doing and read it now if you haven’t already. But if you don’t have time, here’s the key point:


> This is a screenshot from an NPR article discussing the rising use of ad blockers. The page is 12 megabytes in size in a stock web browser. **The same article with basic ad blocking turned on is 1 megabyte.**


That’s right, through the simple act of running an ad blocker, you’ve reduced that website’s payload by twelve times. Twelve! That’s like the most effective exercise program *ever!*


Even the traditional advice to keep websites lean and mean for mobile no longer applies because new mobile devices, at least on the Apple side, are *faster than most existing desktops and laptops.*


![The iPhone XS is faster than an iMac Pro on the Speedometer 2.0 JavaScript benchmark. It's the fastest device I've ever tested. Insane 45% jump over the iPhone8/X chip. How does Apple do it?!](https://blog.codinghorror.com/content/images/2025/09/image-5.png)


Despite [claims to the contrary](https://danluu.com/web-bloat/), the bad guy isn’t web bloat, per se. **The bad guy is *advertising***. Unlimited, unfettered ad  “tech” has creeped into everything and subsumed the web.


Personally I don’t even want to run ad blockers, and I didn’t for a long time – but it’s increasingly difficult to avoid running an ad blocker unless you want a clunky, substandard web experience. There’s a *reason* the most popular browser plugins are inevitably ad blockers, isn’t there? Just ask Google:


![](https://blog.codinghorror.com/content/images/2025/02/image-263.png)


So it’s all the more surprising to learn that Google is suddenly [clamping down hard on adblockers](https://9to5google.com/2019/05/29/chrome-ad-blocking-enterprise-manifest-v3/) in Chrome. Here’s what the author of uBlock Origin, an ad blocking plugin for Chrome, [has to say](https://github.com/uBlockOrigin/uBlock-issues/issues/338#issuecomment-496009417) about today’s announcement:


> In order for Google Chrome to reach its current user base, it had to support content blockers – these are the top most popular extensions for any browser. Google strategy has been to find the optimal point between the two goals of growing the user base of Google Chrome and preventing content blockers from harming its business.
> The blocking ability of the webRequest API caused Google to yield control of content blocking to content blockers. Now that Google Chrome is the dominant browser, it is in a better position to shift the optimal point between the two goals which benefits Google’s primary business.
> The deprecation of the blocking ability of the webRequest API is to gain back this control, and to further instrument and report how web pages are filtered, since the exact filters which are applied to web pages are useful information which will be collectable by Google Chrome.


The ad blockers themselves are arguably just as complicit. Eye/o GmbH owns [AdBlock](https://adblockplus.org/) and [uBlock](https://www.ublock.org/), employs 150 people, and in 2016 they had 50 million euros in revenue, of which about 50% was profit. Google’s [paid “Acceptable Ads” program](https://help.getadblock.com/support/solutions/articles/6000092027-why-does-adblock-allow-non-intrusive-ads-) is a way to funnel money into adblockers to, uh, *encourage* them to display certain ads. With money. Lots… and lots… of money. 🤑


We simultaneously have a very real web obesity crisis, and a looming crackdown on ad blockers, seemingly the only viable weight loss program for websites. What’s a poor web citizen to do? Well, there is one thing you can do to escape the need for browser-based adblockers, at least on your home network. Install and configure [Pi-Hole](https://pi-hole.net/).


![](https://blog.codinghorror.com/content/images/2025/02/image-264.png)


I’ve talked about the amazing Raspberry Pi before in the context of [classic game emulation](https://blog.codinghorror.com/the-raspberry-pi-has-revolutionized-emulation/), but this is another brilliant use for a Pi.


Here’s why it’s so cool. If you disable the DHCP server on your router, and let the Pi-Hole become your primary DHCP server, **you get automatic DNS based blocking of ads for every single device on your network**. It’s kind of scary how powerful DNS can be, isn’t it?


![](https://blog.codinghorror.com/content/images/2025/02/image-265.png)


My Pi-Hole took me about 1 hour to set up, start to finish. All you need is

- a [Raspberry Pi 3b+ kit](https://www.amazon.com/dp/B07BC7BMHY/) $59
- a quality [32GB SD card](https://www.amazon.com/dp/B00WR4IJBE/) $9
- an ethernet cable


I do recommend the 3b+ because it has [native gigabit ethernet](https://www.pidramble.com/wiki/benchmarks/networking) and a bit more muscle. But [literally any Raspberry Pi](https://discourse.pi-hole.net/t/what-model-raspberry-pi-should-i-use-for-pi-hole/9635) you can find laying around will work, though I’d *strongly* advise you to pick one with a wired ethernet port since it’ll be your DNS server.


I’m not going to write a whole [Pi-Hole installation guide](https://www.smarthomebeginner.com/pi-hole-tutorial-whole-home-ad-blocking/), because there are lots of great ones out there already. It’s not difficult, and there’s a slick web GUI waiting for you once you complete initial setup. For your initial testing, pick any IP address you like on your network that won’t conflict with anything active. Once you’re happy with the basic setup and web interface:

- Turn OFF your router’s DHCP server – existing leases will continue to work, so nothing will be immediately broken.
- Turn ON the pi-hole DHCP server, in the web GUI.


![](https://blog.codinghorror.com/content/images/2025/02/image-266.png)


Once you do this, all your network devices will start to grab their DHCP leases from your Pi-Hole, which will *also* tell them to route all their DNS requests through the Pi-Hole, and that’s when the ✨ magic ✨ happens!


![](https://blog.codinghorror.com/content/images/2025/02/image-267.png)


All those DNS requests from all the devices on your network will be checked against the ad blacklists; anything matching is quickly and silently discarded **before it ever reaches your browser.**


![](https://blog.codinghorror.com/content/images/2025/02/image-268.png)


(The Pi-Hole also acts as a [caching DNS server](https://discourse.pi-hole.net/t/will-pi-hole-slow-down-my-network/2048), so repeated DNS requests will be serviced rapidly from your local network, too.)


If you’re worried about stability or reliability, you can easily add a cheap battery backed USB plug, or even a second backup Pi-Hole as your secondary DNS provider if you prefer belt and suspenders protection. Switching back to plain boring old vanilla DNS is as easy as unplugging the Pi and flicking the DHCP server setting in your router back on.


At this point if you’re interested (and you should be!), just give it a try. If you’re looking for more information, the project has an [excellent forum](https://discourse.pi-hole.net/) full of FAQs and roadmaps.


![](https://blog.codinghorror.com/content/images/2025/02/image-269.png)


You can even [vote for your favorite upcoming features](https://discourse.pi-hole.net/c/feature-requests?order=votes)!


I avoided the Pi-Hole project for a while because I didn’t need it, and I’d honestly rather jump in later when things are more mature.


![](https://blog.codinghorror.com/content/images/2025/02/image-270.png)


With the latest Chrome crackdown on ad blockers, now is the time, and I’m impressed how simple and easy Pi-Hole is to run. Just find a quiet place to plug it in, spend an hour configuring it, and promptly proceed to forget about it forever as you enjoy a lifetime subscription to *a glorious web ad instant weight loss program across every single device on your network with (almost) zero effort!*


Finally, an exercise program I can believe in.

[website performance](https://blog.codinghorror.com/tag/website-performance/)
[web optimization](https://blog.codinghorror.com/tag/web-optimization/)
[online advertising](https://blog.codinghorror.com/tag/online-advertising/)
