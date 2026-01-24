---
title: "Will Apps Kill Websites?"
date: 2012-04-23
url: https://blog.codinghorror.com/will-apps-kill-websites/
slug: will-apps-kill-websites
word_count: 1263
---

I’ve been an eBay user since 1999, and I still frequent eBay as both buyer and seller. In that time, eBay has transformed from a place where geeks [sell broken laser pointers](http://en.wikipedia.org/wiki/EBay#Origins_and_history) to each other, into a global marketplace where businesses sell anything and everything to customers. If you’re looking for strange or obscure items, things almost nobody sells new any more, or grey market items for cheap, eBay is still not a bad place to look.


At least for me, eBay still basically works, after all these years. But one thing hasn’t changed: **the eBay website has always been difficult to use and navigate**. They’ve updated the website recently to remove some of the more egregious cruft, but it’s still *way* too complicated. I guess I had kind of accepted old, complex websites as the status quo, because I didn’t realize how bad it had gotten until I compared the experience on the eBay website with the experience of the eBay apps for mobile and tablet.


### eBay Website


![](https://blog.codinghorror.com/content/images/2025/04/image-622.png)


### eBay Mobile App


![](https://blog.codinghorror.com/content/images/2025/04/image-621.png)


### eBay Tablet App


![](https://blog.codinghorror.com/content/images/2025/04/image-620.png)


Unless you’re some kind of super advanced eBay user, you should probably avoid the website. The tablet and mobile eBay apps are just plain simpler, easier, and faster to use than the eBay website itself. I know this intuitively from using eBay on my devices and computers, but there’s also [usability studies](http://www.useit.com/alertbox/mobile-sites-apps.html) with data to prove it, too. To be fair, eBay is struggling under the massive accumulated design debt of a website originally conceived in the late 90s, whereas their mobile and tablet app experiences are recent inventions. **It’s not so much that the eBay apps are great, but that the eBay website is so very, *very* bad**.


The implied lesson here is to **embrace constraints**. Having a limited, fixed palette of UI controls and screen space is a *strength*. A strength we used to have in early Mac and Windows apps, but seem to have lost somewhere along the way as applications got more powerful and complicated. And it’s endemic on the web as well, where the eBay website has been slowly accreting more and more functionality since 1999. The nearly unlimited freedom that you get in a modern web browser to build whatever UI you can dream up, and assume as large or as small a page as you like, often ends up being harmful to users. It certainly is in the case of eBay.


If you’re starting from scratch, you should always [design the UI first](https://blog.codinghorror.com/ui-first-software-development/), but now that we have such great mobile and tablet device options, consider designing your site for the devices that have the strictest constraints first, too. This is the thinking that led to [mobile first design strategy](http://www.lukew.com/ff/entry.asp?933). It helps you stay focused on a simple and uncluttered UI that you can scale up to bigger and beefier devices. Maybe eBay is just going in the wrong direction here; **design simple things that scale up; not complicated things you need to scale down.**


[Above all else, simplify!](https://blog.codinghorror.com/in-pursuit-of-simplicity/) But why stop there? If building the mobile and tablet apps first for a web property produces a better user experience – why do we need the website, again? Do great tablet and phone applications make websites obsolete?


### Why are apps better than websites?

1. **They can be faster.**
No browser overhead of CSS and HTML and JavaScript hacks, just pure native UI elements retrieving precisely the data they need to display what the user requests.
2. **They use simple, native UI controls.**
Rather than imagineering whatever UI designers and programmers can dream up, why not pick from a well understood palette of built-in UI controls on that tablet or phone, all built for optimal utility and affordance on that particular device?
3. **They make better use of screen space.**
Because designers have to fit just the *important* things on 4 inch diagonal mobile screens, or 10 inch diagonal tablet screens, they’re less likely to fill the display up with a bunch of irrelevant noise or design flourishes (or, uh, advertisements). Just the important stuff, thanks!
4. **They work better on the go and even offline.**
In a mobile world, you can’t assume that the user has a super fast, totally reliable Internet connection. So you learn to design apps that download just the data they need at the time they need to display it, and have sane strategies for loading partial content and images as they arrive. That’s assuming they arrive at all. You probably also build in some sort of offline mode, too, when you’re on the go and you don’t have connectivity.


### Why are websites better than apps?

1. **They work on any device with a browser.**
Websites are as close to universal as we may ever get in the world of software. Provided you have a HTML5 compliant browser, you can run an entire universe of “apps” on your device from day zero, just by visiting a link, exactly the same way everyone has on the Internet since 1995. You don’t have to hope and pray a development community emerges and is willing to build whatever app your users need.
2. **They don’t have to be installed.**
Applications, unlike websites, can’t be visited. They aren’t indexed by Google. Nor do applications magically appear on your device; they must be explicitly installed. Even if installation is a one-click affair, your users will have to discover the app before they can even begin to install it. And once installed, they’ll have to [*manage* all those applications](http://www.hanselman.com/blog/AppsAreTooMuchLike1990sCDROMsAndNotEnoughLikeTheWeb.aspx) like so many Pokémon.
3. **They don’t have to be updated.**
Websites are always on the [infinite version](https://blog.codinghorror.com/the-infinite-version/). But once you have an application installed on your device, how do you update it to add features or fix bugs? How do users even know if your app is out of date or needs updating? And why should they need to care in the first place?
4. **They offer a common experience.**
If your app and the website behave radically differently, you’re forcing users to learn two different interfaces. How many different devices and apps do you plan to build, and how consistent will they be? You now have a community divided among many different experiences, fragmenting your user base. But with a website that has a decent mobile experience baked in, you can deliver a consistent, and hopefully *consistently great*, experience across *all* devices to all your users.


I don’t think there’s a clear winner, only pros and cons. But **apps will always need websites**, if for nothing else other than a source of data, as a mothership to phone home to, and a place to host the application downloads for various devices.


And if you’re obliged to build a website, why not build it out so it offers a *reasonable* experience on a mobile or tablet web browser, too? I have nothing against a premium experience optimized to a particular device, but shouldn’t all your users have a premium experience? eBay’s problem here isn’t mobile or tablets per se, but that they’ve let their core web experience atrophy so badly. I understand that there’s a lot of inertia around legacy eBay tools and long time users, so it’s easy for me to propose radical changes to the website here on the outside. Maybe the only way eBay can redesign *at all* is on new platforms.


Will mobile and tablet apps kill websites? A few, certainly. **But only the websites stupid enough to let them.**

[mobile apps](https://blog.codinghorror.com/tag/mobile-apps/)
[website vs app](https://blog.codinghorror.com/tag/website-vs-app/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[online marketplaces](https://blog.codinghorror.com/tag/online-marketplaces/)
