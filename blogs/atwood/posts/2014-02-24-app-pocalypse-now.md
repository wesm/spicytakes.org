---
title: "App-pocalypse Now"
date: 2014-02-24
url: https://blog.codinghorror.com/app-pocalypse-now/
slug: app-pocalypse-now
word_count: 1793
---

I’m getting pretty sick of being nagged to install your damn apps.


![](https://blog.codinghorror.com/content/images/2025/05/image-545.png)


XKCD helpfully [translates](http://xkcd.com/1174/):


![](https://blog.codinghorror.com/content/images/2025/05/image-546.png)


Yeah, there are [smart app banners](https://developer.apple.com/library/ios/documentation/AppleApplications/Reference/SafariWebContent/PromotingAppswithAppBanners/PromotingAppswithAppBanners.html), which are marginally less annoying, but it’s amazing how quickly we went from “Cool! Phone apps that [finally don’t suck!](https://blog.codinghorror.com/the-iphone-software-revolution/)” to this sad, eye rolling, oh-great-of-*course*-you-have-an-app-too state of affairs.


!["Would you like to install our free app?!?" is the new "It looks like you're writing a letter!"](https://blog.codinghorror.com/content/images/2025/09/image-18.png)


Four years, give or take a few months, if you were counting. So what happened?


## Millions of pointless apps


Your platform now has a *million* apps? Amazing! Wonderful! What they don’t tell you is that 99% of them are awful junk that nobody would ever want.


Let’s start with the basics. How do you know which apps you need? How do you get them installed? How do you keep them updated? How many apps can you reasonably keep track of on a phone? On a tablet? Just the home screen? A few screens? A dozen screens? When you have millions of apps out there, this rapidly becomes less of a “slap a few icons on the page” problem and more of a search problem like the greater web. My son’s iPad has more than 10 pages of apps now, we don’t even bother with the pretense of scrolling through pages of icons, we just go straight to search every time.


![](https://blog.codinghorror.com/content/images/2025/05/image-547.png)


The more apps out there, the more the app stores are clogged with mediocre junk, the more the overall noise level keeps going up, which leads directly to this profligate nagging. Companies keep asking *how can we get people to find and install our amazing app* instead of the one question they really should have asked.


*Why the hell are we building an app in the first place?*


I want to know who exactly is going to all the trouble of installing the McDonalds app on their device instead of simply visiting the McDonalds website in the browser as needed. What problem does that app solve for [french fry enthusiasts](https://web.archive.org/web/20140101075512/http://aht.seriouseats.com/archives/2010/05/the-burger-lab-how-to-make-perfect-mcdonalds-style-french-fries.html) that it needs to be permanently installed on your device? Why are they giving away free Big Macs just to get people to install this thing?


## Fragmentation into parallel and incompatible app worlds


It was so much easier when iOS was totally dominant and the iPhone was the only player. Before the iPad and tablets. Before Android got decent in 4.0 and Google standardized the Play store. Now there are, at minimum, *four* radically different mobile platforms that every serious app player has to support:

1. Android phone
2. iOS phone
3. iOS tablet
4. Android tablet


(For extra credit: how many of these are actually “mobile”?)


Unless you’re careful to build equivalent apps in all those places, it’s like having multiple parallel Internets. “No, sorry, it’s not available on that Internet, only the iOS phone Internet.” Or even worse, only on the United States iOS phone Internet.


If you’re feeling generous, we should technically include Windows 8 and Windows Phone in here too. All with different screen dimensions, development stacks, UI guidelines, and usage patterns. Oh and by the way, that’s assuming no other players emerge as serious contenders in the computing device market. *Ever.*


At the point where you find yourself praying for a duopoly as one of the better possible outcomes, that’s… not a good sign.


## Paying for apps became a race to the bottom


Buying an app is the modern [Support Your Favorite Small Software Vendor Day](https://blog.codinghorror.com/today-is-support-your-favorite-small-software-vendor-day/). I was always fine with dropping ten or twenty bucks on software I loved. I’m a software engineer by profession; apps are cheaper so I can buy even more of them.


Have you ever noticed that the people complaining about apps that cost $3.99 are the same people dropping five bucks on a cup of fancy coffee without batting an eyelash? Me too, and [I’m with the coffee people](https://web.archive.org/web/20140112071431/http://www.joshlehman.com/thoughts/stop-using-the-cup-of-coffee-vs-0-99-cent-app-analogy/). $3.99 for your app? *Outraaageous! *


> Now, contrast this with your app, Mr. Developer. I don’t know you from Adam. You’re pitching digital Instant Refresher Juice 1.0 to me in the form of a new app. The return I’m going to get is questionable at best. I already have 30 apps on my phone, some of them very good. Do I need another one? I don’t use the 30 I have. The experience I’m going to get from adding one more app is not trustable. I’m assured of nothing. Last week I bought an app for 99 cents and it was terrible. I used it once, for 15 seconds. I could be shoving $1 straight down the toilet again for all I know. Your app, good sir, is a total gamble. Sure, it’s only a $1 gamble… but it’s a gamble and that fact matters more than any price you might place on it.


For some reason I don’t completely understand, mobile app review systems are frequently of questionable value, so all you really have to go on are the screenshots and a bit of text provided by the developer.


Imagine you bought your coffee, only to open the lid and find it was only half full, or that it wasn’t coffee at all but lemonade. If only 1 in 5 cups of coffee you bought actually contained coffee, a $3.99 price for that coffee starts to seem unreasonably high. **When you buy an app, you don’t really know what you’re going to get.**


Turns out, the precious resource here isn’t the money after all. *It’s your time.* In a world of millions of apps, free is the correct and only price for most apps except those rare few of extreme, easily demonstrable value – probably from well known brands of websites you already use daily. So hey, everything is *free!* Awesome! Right? Well…


## When apps are free, you’re the product


I know, I know, I’m sick of this trite phrase too. But if the market is emphatically proving that free is the only sustainable model for apps, then this is the new reality we have to acknowledge.


![](https://blog.codinghorror.com/content/images/2025/05/image-548.png)


Nothing terrifies me more than an app with no moral conscience in the desperate pursuit of revenue that has full access to everything on my phone: contacts, address book, pictures, email, auth tokens, you name it. I’m not excited by the prospect of installing an app on my phone these days. It’s more like a vague sense of impending dread, with my finger shakily hovering over the uninstall button the whole time. All I can think is **what shitty thing is this “free” app going to do to me so they can satisfy their investors?**


For the sake of argument, let’s say the app is free, and the developers are ethical, so you trust that they won’t do anything sketchy with the personal information on your device to make ends meet. Great! But they still have to make a living, don’t they? Which means doing anything *useful* in the app requires buying three “optional” add-ons that cost $2.99 each. Or there are special fees for performing certain actions. Isn’t this stuff you would want to know before installing the app? You betcha. Maybe the app is properly tagged as “offering in-app purchases” but **the entire burden of discovering exactly what “in-app purchases” means, and how much the app will ultimately cost you, is placed completely on your shoulders.** You, the poor, bedraggled user.


## The app user experience is wildly inconsistent


Have you ever tried actually *using* the Amazon app on iOS, Android, and Windows? iOS does the best, mostly because it’s been an app platform for longer than the others, but even there, the Amazon app is a frustrating morass of missing and incomplete functions from the website. Sure, maybe you don’t need the full breadth of Amazon functions on your phone, though that’s debatable on a tablet. But natural web conveniences like opening links in new tabs, sharing links, the back button, searching within the page, and zooming in and out are available inconsistently, if at all.


The minute you begin switching between platforms – say you use an iOS tablet and an Android phone and a Windows 8 touch laptop, like I do – you’ll find there are *massive* differences between the Amazon apps (and the eBay apps, and the Netflix apps, and the..) on these different platforms. At some point, you just get fed up with all the inconsistencies and oddities and quirks and say to hell with these apps, **can I please just use the website instead?**


Now, if your website is an awful calcified throwback to 2003, like eBay, then the mobile apps can be a valauble opportunity to [reinvent your user interface](https://blog.codinghorror.com/will-apps-kill-websites/) without alienating all your existing users. If there’s one thing I love about tablet and phone design it’s that their small screens and touch interfaces force people to [think simpler](https://blog.codinghorror.com/in-pursuit-of-simplicity/). This is a good thing. But if you don’t eventually take those improvements home to the mothership, you’re creating two totally different and incompatible UIs for doing the same things.


It seems like a fool’s errand to dump millions of dollars of development time into these radically different, siloed app platforms when Amazon could have spent it improving their website and making that experience scale a bit better to every device out there.


## The World Wide App


But that’s not an option, because apparently the web is dead, and mobile apps are the future. I’m doing my best to resist a sudden uncontrollable urge to use my Ledge Finder app to find the nearest ledge to jump from right now.


![To me, the most amazing thing about Snapchat, Uber, and a few other apps is they all don't need the web. | @semil nobody is going to be using the web soon.](https://blog.codinghorror.com/content/images/2025/09/image-148.png)


The tablet and phone app ecosystem is slowly, painstakingly reinventing everything I hated about the computer software industry before the web blew it all up. Even [fans are concerned](http://parislemon.com/post/77357979234/a-new-glue-for-a-new-kingdom):


> I’m waiting for something that will unify the world of apps and make manually going to an App Store to find a new app as weird as typing in a URL to find a new website. My bet is that this won’t be Facebook. Instead, I would not bet against some young upstart, perhaps one inspired upon reading about a $19 billion deal, to go heads-down and come up with something crazy.


I’ll have more to say about this soon, but I expect there to be an explosion of new computing devices all over the world in the next few decades, not a contraction. Sometimes the craziest solution is the one that’s been right there in front of you the whole time.

[user experience](https://blog.codinghorror.com/tag/user-experience/)
[app development](https://blog.codinghorror.com/tag/app-development/)
