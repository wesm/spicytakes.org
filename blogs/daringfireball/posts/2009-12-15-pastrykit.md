---
title: "PastryKit"
date: 2009-12-15
url: https://daringfireball.net/2009/12/pastrykit
slug: pastrykit
word_count: 1999
---


One of the recent themes here has been the topic of [iPhone OS web apps](http://daringfireball.net/2009/11/iphone_web_apps_alternative) — apps for the iPhone and iPod Touch that are built with nothing more than HTML, CSS, and JavaScript. And specifically, the issues of how good an experience iPhone web apps can offer, and how easy they are to develop, compared to native Cocoa Touch apps.


One area in particular where iPhone web apps fall short of native iPhone apps is scrolling. Take for example a long list, such as your full address book in Contacts, or all your songs in the iPod app. When you scroll these lists, you can *fling* the list, and the list will scroll at high speed after you let go. The effect is sort of like spinning a wheel with very little friction. With iPhone web apps, you can make a list that looks almost, maybe even exactly, like a native iPhone list view. But all web views on the iPhone scroll with almost no momentum. You can’t fling them. iPhone web views feel like they have a lot of scrolling friction.


This friction might make sense for regular web pages rendered on the iPhone’s small screen, where by “regular” I mean “not optimized specifically for display on the iPhone”. But it just feels slow — stuck — on iPhone-optimized apps.


If you’ve never taken notice of it, try it now, comparing something like your Contacts app list with an iPhone web app like [Showtime](http://showtime-app.com/). (In Showtime, tap “Watchlist” and then tap the “+” button to get a nice long list to scroll through.) Another good scrolling comparison: native iPhone Twitter clients like [Tweetie](http://www.atebits.com/tweetie-iphone/) and [Birdfeed](http://birdfeedapp.com/) versus iPhone web app Twitter clients like [Hahlo](http://hahlo.com/) and the new [Mobile Twitter](https://mobile.twitter.com/). The difference is significant, and far more than cosmetic. As [Justin Williams recently wrote](http://carpeaqua.com/2009/11/30/web-apps-scrolls-like-molasses/):


> I believe that with the current crop of Web technologies available
> in MobileSafari, apps like Hahlo, PocketTweets and Showtime could
> thrive as an alternative to their native counterparts if Apple
> allowed developers to *adjust the scrolling/drag coefficient of
> Mobile WebKit*. If you compare the scrolling speed of your Twitter
> timeline in Hahlo and Tweetie, the results are drastically
> different. Tweetie feels like it effortlessly scrolls based on
> how much momentum you exert in the scroll action, while Hahlo is
> being constrained by a fifty pound weight on its back.


Scrolling isn’t the only UI/experience issue where web apps seemingly can’t quite match what native iPhone apps can offer. Another is that MobileSafari [doesn’t allow for CSS fixed-position elements](http://furbo.org/2007/07/10/bittersweet/), which means you can’t make a toolbar that stays put at the very top or bottom of the screen without having it scroll away when you scroll the content.


And that’s just talking about the user experience side of things. The other side is that of development. Last month [I wrote](http://daringfireball.net/2009/11/iphone_web_apps_alternative):


> When you write a Cocoa Touch app for the iPhone, you’re not
> starting from scratch. You’re starting with the Cocoa Touch
> framework. As Faruk Ateş astutely points out in [his response to
> Koch](http://farukat.es/journal/2009/11/347-iphone-developers-arent-stupid-ppk), to discount the framework is to discount everything that
> sets the iPhone apart as a development platform. Not only are
> native iPhone apps faster and more capable than their web-app
> equivalents, but they’re easier to write.


Some readers objected to this, arguing, more or less, that no matter how good the Cocoa Touch framework is, native iPhone apps are harder to develop than web apps because one must learn both the app framework (Cocoa) *and* a new programming language, Objective-C. But that’s not really a fair comparison. It’s like saying it’s easier to run than to bike if you don’t know how to ride a bicycle.


Let’s clarify. Let’s specify that we’re talking about creating iPhone apps with great design and user experiences. Let’s acknowledge that to make anything great — anything at all, software or otherwise — one needs talent, experience, and familiarity and expertise with the necessary tools. If you’re already an expert web developer but have never programmed Cocoa software, then yes, there’s large time-consuming Step Zero in front of you before you can attempt to develop a native iPhone Cocoa Touch app. But, likewise, there are long-time Cocoa Mac (and a handful of even longer-time NeXT) developers who have no idea how to create a modern AJAX-y web app from HTML, CSS, and JavaScript — and who think *JavaScript* is the weird programming language.


What I’m saying is that talented Cocoa Touch developers have an easier job implementing the same iPhone app than talented web app developers do. The Cocoa Touch framework makes all sort of things free or easy. Things like smooth fast animation between views. Things like buttons and lists and toolbars that look just like other standard iPhone buttons, lists, and toolbars.


There do exist some open source frameworks for iPhone web app developers, so that one need not start from scratch implementing things to mimic Cocoa Touch UI elements. [iUI](http://daringfireball.net/linked/2007/07/11/iui), started by Joe Hewitt just a few weeks after the original iPhone debuted in July 2007, is one. [jQTouch](http://www.jqtouch.com/), by David Kaneda and based on jQuery, is another. (Showtime is built using jQTouch.)


But these frameworks don’t solve the problem with scrolling speed/friction, or fixed-position elements.


It ends up there is a company, however, that has developed an amazing iPhone web app framework which:

- Completely hides the address bar, even when running not from a saved-to-the-home app icon, but within a page in MobileSafari itself.
- Allows for fixed-position toolbars that never budge from the top when you scroll.
- *And*: sets its own scrolling friction coefficient, allowing you to fling long lists.


The company behind this web framework is Apple. And the framework is apparently named PastryKit.


## The Best iPhone Web App in the World


If you have an iPhone or iPod Touch handy, stop reading this and go here:


[http://help.apple.com/iphone/3/mobile/](http://help.apple.com/iphone/3/mobile/)


This is not a secret web site. In fact, it may well already be in your iPhone bookmarks — it’s where you get redirected when you choose the “iPhone User Guide” bookmark that’s included as one of the defaults for MobileSafari. I don’t know when Apple launched this PastryKit-powered version of the site, but it’s been under our noses for a while, with very little notice.1


If you don’t have an iPhone or iPod Touch handy, or if you do and you’re back after trying it out and want to poke at it with Safari’s Web Inspector, you can also load it in Mac or Windows Safari by setting the user agent string to MobileSafari 3.x in Safari’s [Develop menu](http://developer.apple.com/safari/library/documentation/AppleApplications/Conceptual/Safari_Developer_Guide/2SafariDeveloperTools/SafariDeveloperTools.html). (Without the MobileSafari user agent string, you’ll get redirected to a different iPhone help page; using a MobileSafari 2.x user agent string, you’ll see last year’s version of the User Guide, which is far less impressive technically.) Shrink your Safari window down to roughly iPhone dimensions before loading the site, because the UI will be laid out to fill the dimensions of the viewport when it loads.


The JavaScript source code has been minimized/optimized, but it’s not obfuscated, per se, so it’s easy to see that the framework is called PastryKit, and even a dilettante JavaScript hacker like me can follow along and see some of what’s going on. PastryKit accomplishes all three of the aforementioned things — hiding the MobileSafari address bar, providing fixed-position toolbars, and providing scrolling with momentum — by disabling regular scrolling and setting up its own view hierarchy and implementing its own scrolling.


From WebKit’s perspective, everything in this iPhone User Guide is in a view that is exactly the size of the viewport, so there’s nothing to scroll. PastryKit handles all of what the user sees as scrollable content. This is how on the iPhone it provides for lower-friction scrolling than provided by MobileWebKit itself — PastryKit does its own scrolling math. And it’s even more noticeable when running the app in *desktop* Safari with the user agent trick, because you never see Mac scrollbars, and can’t use your mouse scrollwheel to scroll the content. Everything related to scrolling is implemented within the app itself, in JavaScript.


After installing the User Guide app to your home screen and launching it from there, there’s really very little to suggest that it isn’t a native iPhone application. No MobileSafari address bar at the top, no MobileSafari toolbar at the bottom. Scrolling is fast and has momentum. It even works perfectly offline, because the contents of the user guide are stored locally in a database using HTML5.


It’s not perfect. Scrolling is smooth on my iPhone 3GS, but it’s a little janky on my old iPhone 3G and original iPhone. (Still better than the scrolling in any other web app I’ve ever seen, though — just not native-app-smooth.) Taps and gestures sometimes don’t register — this is most noticeable for me when I try to scroll as fast as I can with a quick finger swipe. Super-quick gestures, I suspect, sometimes slip through the JavaScript event filters.


The rubber-band “bounce” scrolling — where if the view is already at the top but you pull down in an attempt to scroll up and you see whitespace and it all just bounces back into place when you let go — breaks if you pull down all the way off the bottom of the display. What happens there is the view gets “stuck” in the position where it’s displaying the stretched-out whitespace at the top of the view; you can unstick it by just tapping somewhere in the content area.


And, lastly, it doesn’t work at all with the iPhone’s system-standard gesture where you can tap the status bar at the top of the screen (the bar that displays the carrier name, signal strength, time, and battery life) to scroll to the top. In MobileSafari, if you tap the status bar while running this app, the entire MobileSafari view scrolls to the top, which exposes the browser address bar. When running the User Guide app from the home screen, tapping the status bar simply has no effect. I presume the problem here is that there is no JavaScript event in mobile WebKit for status bar taps — the event goes to the iPhone app, and the web app running in WebKit inside the iPhone app can’t see it or register a handler to act upon it. From a user’s perspective, an iPhone web app launched from the home screen is just another app. But technically, it’s like a meta app — it’s a JavaScript app running inside a native iPhone app that just presents a full-screen WebKit view and loads the web app.


But on the whole this User Guide app and the PastryKit framework are rather amazing. The $64,000 question, though, is whether PastryKit is something Apple intends (or that a team within Apple hopes) to ship publicly. It seems like a lot of effort to build a framework this rich just for this iPhone User Guide, so I’m hopeful the answer is yes. Perhaps something integrated with the next major release of Dashcode? And, perhaps with integrated UI layout tools, along the lines of Interface Builder?


Here’s to hoping we haven’t heard the last of PastryKit, and that Apple continues work on making mobile WebKit an open alternative to the App Store.


## PastryKit / iPhone User Guide Demos


For the sake of posterity and for those of you without access to an iPhone or Safari, I’ve made [two screencasts showing the iPhone User Guide web app in action](https://daringfireball.net/misc/2009/12/user_guide_demos).


---

1. There’s a question on Stack Overflow from October 22 [asking about PastryKit](http://stackoverflow.com/questions/1143589/what-is-the-pastrykit-framework), and jQTouch developer David Kaneda has mentioned it a [few](http://twitter.com/jQTouch/status/6146839190) [times](http://twitter.com/jQTouch/status/6342882180) on Twitter, but those are the only references to it I’ve been able to find. ↩︎



| **Previous:** | [Who Do You Believe, Randall Stross or Your Own Lying Eyes?](https://daringfireball.net/2009/12/stross_lying_eyes) |
| **Next:** | [More on PastryKit](https://daringfireball.net/2009/12/more_on_pastrykit) |


PreviousNext