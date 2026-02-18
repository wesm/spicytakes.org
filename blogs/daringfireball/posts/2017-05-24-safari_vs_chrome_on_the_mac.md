---
title: "Safari vs. Chrome on the Mac"
date: 2017-05-24
url: https://daringfireball.net/2017/05/safari_vs_chrome_on_the_mac
slug: safari_vs_chrome_on_the_mac
word_count: 1483
---


Eric Petitt, [writing for The Official Unofficial Firefox Blog yesterday](https://medium.com/the-official-unofficial-firefox-blog/browse-against-the-machine-e793c0fee917):


> I head up Firefox marketing, but I use Chrome every day. Works
> fine. Easy to use. Like most of us who spend too much time in
> front of a laptop, I have two browsers open; Firefox for work,
> Chrome for play, customized settings for each. There are multiple
> things that bug me about the Chrome product, for sure, but I‘m OK
> with Chrome. I just don’t like *only* being on Chrome. […]
> But talking to friends, it sounds more and more like living on
> Chrome has started to feel like their only option. Edge is broken.
> Safari and Internet Explorer are just plain bad. And
> unfortunately, too many people think Firefox isn’t a modern
> alternative.


In an update posted today, he walked that back:


> In my original post I made a personal dig about Edge, IE and
> Safari: “Edge is broken. Safari and Internet Explorer are just
> plain bad.” I’ve since deleted that sentence.
> It’s true, I personally don’t like those products, they just don’t
> work for me. But that was probably a bit too flip. And, if it
> wasn’t obvious that those were my personal opinions as a user, not
> those of the good folks at Firefox and Mozilla, then please accept
> my apology.


It’s easy when making an aside — and it’s clear that the central premise of this piece is about positioning Chrome as the Goliath to Firefox’s David, so references to Safari and IE are clearly asides — to conflate “*I don’t like X*” with “*X is bad*”. So I say we let it slide.1


But I’ve been meaning to write about Safari vs. Chrome for a while, and Petitt’s jab, even retracted, makes for a good excuse.


I think Safari is a *terrific* browser. It remains the one and only browser for the Mac that behaves like a native Mac app through and through. It may not be the fastest browser but it is fast. And its energy performance puts Chrome to shame. If you use a Mac laptop, using Chrome instead of Safari can cost you an hour or more of battery life per day.2


But Chrome is a terrific browser, too. It’s clearly the second-most-Mac-like browser for MacOS. It almost inarguably has the widest and deepest extension ecosystem. It has good web developer tools, and Chrome adopts new web development technologies faster than Safari does.


But Safari’s extension model is more privacy-conscious. For many people on MacOS, the decision between Safari and Chrome probably comes down to which ecosystem you’re more invested in — iCloud or Google — for things like tab, bookmark, and history syncing. Me, personally, I’d feel lost without the ability to send tabs between my Macs and iPhone via Handoff. **Update:** Unbeknownst to me, Chrome fully supports Handoff with iOS devices. Nice!


In short, Safari closely reflects Apple’s institutional priorities (privacy, energy efficiency, the niceness of the native UI, support for MacOS and iCloud technologies) and Chrome closely reflects Google’s priorities (speed, convenience, a web-centric rather than native-app-centric concept of desktop computing, integration with Google web properties). Safari is Apple’s browser for Apple devices. Chrome is Google’s browser for all devices.


I personally prefer Safari, but I can totally see why others — especially those who work on desktop machines or MacBooks that are usually plugged into power — prefer Chrome. DF readers agree. Looking at my web stats, over the last 30 days, 69 percent of Mac users visiting DF used Safari, but a sizable 28 percent used Chrome. (Firefox came in at 3 percent, and everything else was under 1 percent.)3


As someone who’s been a Mac user long enough to remember when there were *no* good web browsers for the Mac, having both Safari and Chrome feels downright bountiful, and the competition is making both of them better.


---

1. What really struck me about Petitt’s piece wasn’t the unfounded (to my eyes) dismissal of Safari, but rather his admission that he uses “Firefox for work,  Chrome for play”. I really doubt the marketing managers for Chrome or Safari spend their days with a rival browser open for “play”, and even if they did, I expect they’d have the common sense not to admit so publicly, and especially not in the opening paragraph of a piece arguing that their own browser is a viable alternative to the rival one. ↩︎
2. Back in December, when Consumer Reports rushed out their sensational report [claiming bizarrely erratic battery life](https://daringfireball.net/linked/2016/12/23/cr-mbp) on the then-new MacBook Pros (which was eventually determined to be [caused by a bug in Safari that Apple soon fixed](https://daringfireball.net/linked/2017/01/12/consumer-reports)), I decided to try to loosely replicate their test on the MacBook Pro review units I had from Apple. Consumer Reports doesn’t reveal the exact details of their testing, but they do describe it in general. They set the laptop brightness to a certain brightness value, then load a list of web pages repeatedly until the battery runs out. Presumably they automate this with a script of some sort, but they don’t say.
That’s pretty easy to replicate in AppleScript. I used that day’s leading stories on [TechMeme](https://www.techmeme.com/) as my source for URLs to load — 26 URLs total. When a page loads, my script waits 5 seconds, and then scrolls down (simulating the Page Down key), waits another 5 seconds and pages down again, and then waits another 5 seconds before paging down one last time. This is a simple simulation of a person actually reading a web page. While running through the list of URLs, my script leaves each URL open in a tab. At the end of the list, it closes all tabs and then starts all over again. Each time through the loop the elapsed time and remaining battery life are logged to a file. (I also logged results as updates via messages sent to myself via iMessage, so I could monitor the progress of the hours-long test runs from my phone. No apps were running during the tests other than Safari, Script Editor, Finder, and Messages.)
I set the display brightness at exactly 68.75 percent for each test (11/16 clicks on the brightness meter when using the function key buttons to adjust), a value I chose arbitrarily as a reasonable balance for someone running on battery power.
Averaged (and rounded) across several runs, I got the following results:

I no longer had a new 13-inch MacBook Pro without the Touch Bar (a.k.a. the “MacBook Esc”) — I’d sent it back to Apple. I included my own personal 2014 13-inch MacBook Pro and my old 2011 MacBook Air just as points of reference. I think the Air did poorly just because it was so old and so well-used. It still has its original battery.
I saw *no* erratic fluctuations in battery life across runs of the test. I procrastinated on publishing the results, though, and within a few weeks the whole thing was written off with a “*never mind!*” when Apple fixed the bug in Safari that was causing Consumer Reports’s erratic results.
Anyway, the whole point of including these results in this footnote is that I also ran the exact same test with Chrome on the 13-inch MacBook Pro With Touch Bar. The average result: 3h:40m. That’s 1h:50m difference. On the exact same machine running the exact same test with the exact same list of URLs, the battery lasted almost exactly 1.5 times as long using Safari than Chrome.
My test was in no way meant to simulate real-world usage. You’d have to be fueled up on some serious stimulants to read a new web page every 15 seconds non-stop for hours on end. But the results were striking. If you place a high priority on your MacBook’s battery life, you should use Safari instead of Chrome.
If you’re interested, I’ve posted my battery testing scripts for [Safari](https://gist.github.com/gruber/ad201668b31d21096456d7abf11acbd3) and [Chrome](https://gist.github.com/gruber/15d7183f04c2ac1c51ee6a2637925ebd). ↩︎︎
  - 15-inch MacBook Pro With Touch Bar: 6h:50m
  - 13-inch MacBook Pro With Touch Bar: 5h:30m
  - 13-inch MacBook Pro (2014): 5h:10m
  - 11-inch MacBook Air (2011): 2h:15m
3. If anyone has a good source for browser usage by MacOS users from a general purpose website like The New York Times or CNN, let me know. I honestly don’t know whether to expect that the split among DF readers is biased in favor of Safari because DF readers are more likely to care about the advantages of a native app, or biased in favor of Chrome because so many of you are web developers or even just nerdy enough to install a third-party browser in the first place. Wikimedia used to publish stats like that, but alas, [ceased in 2015](https://stats.wikimedia.org/wikimedia/squids/SquidReportClients.htm). ↩︎︎



| **Previous:** | [‘The Spy Who Loved Me’](https://daringfireball.net/2017/05/moore_spy_who_loved_me) |
| **Next:** | [Halide](https://daringfireball.net/2017/05/halide) |


PreviousNext