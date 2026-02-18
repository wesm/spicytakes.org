---
title: "Palm Saturday"
date: 2009-06-05
url: https://daringfireball.net/2009/06/palm_saturday
slug: palm_saturday
word_count: 1481
---


The iPhone was introduced at Macworld Expo on 9 January 2007. On that day, Palm Inc. was screwed. Their relevance in the industry had already been slowly draining, and they not only had no available products in the same league as the iPhone, they had no *future* products in the same league.


For all the mistakes Palm made to get to that point, and they clearly made many, it’s quite possible that they have done *everything* right since then. They abandoned whatever then passed for their product plan. They [hired Jon Rubinstein](http://www.time.com/time/printout/0,8816,1902833,00.html) and gave him control over building a new hardware and software engineering division. They hired not just new engineers, but great designers and all sorts of [other smart and talented people](http://www.readwriteweb.com/readwritehire/2009/02/palm-hires-chuq-von-rospach-as.php) essential to building a world-class engineering, design, and developer culture.


In short, they did something few companies, no matter how deeply [in trouble](http://news.google.com/news?q=gm), ever do: they recognized that they were screwed and took drastic action. It’s an overused phrase, but in this case it is true: they’ve bet the company.


Palm designed, built, and released the Pre, WebOS, and an app store, all in about two years. I’ve not yet seen or used an actual Pre, but I have been using the WebOS, emulated on my Mac, as a member of Palm’s beta SDK program, and it is excellent. It is hard to imagine how Palm could have produced anything better in the same amount of time. The question is whether even the best they could do is still too little, too late.


Even if, for the sake of argument, we concede that Palm has caught up to the iPhone technically, Apple has a two year *marketing* head start, too. 
The iPhone has already joined the iPod as not just a tech culture hit, but a *pop* culture hit. Everyone knows what an iPhone is. It also has worldwide distribution; the Pre is exactly where the iPhone was two years ago: on one carrier, only in the U.S. The iPhone’s popularity has led to third-party developer support, and third-party developer support has in turn made the iPhone even more popular. It’s a virtuous circle. That sweaty “[Developers, developers, developers, developers](http://www.youtube.com/watch?v=8To-6VIJZRE)” rant is probably the smartest thing Steve Ballmer has ever said.


But so what does the Pre have that the iPhone lacks? The two biggest differences are its hardware keyboard and that it has a different exclusive U.S. carrier, Sprint. But Sprint is smaller than AT&T. Imagine instead if the Pre were launching tomorrow morning on Verizon. *That* might have proved to be an interesting advantage against the iPhone.


That leaves the keyboard. I’ve been thinking about this ever since the keyboard-less iPhone launched, and it is my theory that a hardware keyboard is a significant selling point for only one group of customers: those who already own a phone with a hardware keyboard, and that group is a niche. A nice niche, but a niche nonetheless.


Here’s why. Most normal people have yet to buy their first smartphone. That’s why the stakes are so high — it’s a wide open market frontier, but it won’t remain that way for long. Normal people aren’t planning to do much typing on their new smartphones, and they’re probably right. Any smartphone QWERTY keyboard, software or hardware, is going to be better than what most people are used to, which is pecking things out on a phone with a 0-9 numeric keypad.


I type far better on my iPhone than I expected I’d be able to, and that seems to be true for everyone I know who owns one. The only people who struggle with the iPhone keyboard are those who are already accustomed to a hardware smartphone keyboard. It is definitely different.


Here’s what Dieter Bohn of PreCentral wrote in [his Pre review](http://www.precentral.net/palm-pre-review#Palm-Pre-Hardware):


> I’ve been using QWERTY keyboards on phones for over seven years
> now and I had no problem adjusting to the Palm Pre. If you’re
> looking for a comparison, I’ll say that it’s not as good as your
> standard BlackBerry keyboard, but for 90% of people it’s going to
> be much better than the iPhone’s on-screen software keyboard.


My take is that his seven years of hardware keyboard use have warped his perspective. He’s got it backwards: for 90 percent of people, *it doesn’t make a difference* whether the keyboard is hardware or software.


So while the comparisons between the Pre and iPhone are obvious and inevitable, I think the Pre stands a much stronger chance of stealing customers away from RIM than from Apple. For as good as the Pre is, and I’m convinced it is excellent, it just doesn’t have much to offer that would sway someone considering an iPhone. But for someone considering a BlackBerry, the Pre might look very sweet: a big bright screen, a beautiful modern user interface design, a kick-ass mobile web browser, and, yes, a hardware keyboard. The Pre is the BlackBerry Bold done right.


Another aspect where the Pre is different than the iPhone is in nerd appeal. Here’s a passage from [Jason Chen’s Pre review for Gizmodo](http://gizmodo.com/5277499/palm-pre-review):


> Opening multiple apps at once really does slow down the phone
> enough to be noticeable. In fact, if you’re doing something
> particularly intensive, you’ll actually notice your music *stutter*,
> which we’ve never experienced once on the iPhone. Ever. The
> problem with giving you the ability to open a lot of apps at once
> means you need to police yourself and close them when they’re not
> in use. But it’s damn well worth it. Being able to view a PDF,
> then flipping over to Messaging to answer a text, then over to Music
> to change a song, then over to email to tap out a quickie—that’s
> *computing*.


What’s fascinating about this passage is that Chen clearly intends for it to be taken as a compliment — he is praising the Pre’s multitasking support and interface. But these exact words also summarize perfectly why Apple has withheld multitasking from third-party iPhone applications. The Pre will let you run too many apps at the same time and suffer the consequences. The iPhone will not.


Palm has chosen a different trade-off than Apple in this regard, and it might help them carve out a segment of the market that the iPhone does not, and probably never will, appeal to — the “*don’t treat me like a child, let me shoot myself in the foot if I want to, I despise artificial constraints imposed upon me*” crowd. Some expert users will see the Pre’s stance as a huge win.


## Regarding the Mojo SDK and Eating Their Own Dogfood


One misconception I’ve seen this week is that the Pre’s “web-based” SDK is similar to the development situation for the iPhone during its first year. This is false, but it’s easy to see the confusion because of all the talk about WebOS apps being written using “HTML, CSS, and JavaScript”.


Prior to Apple’s release of the Cocoa Touch APIs and App Store, the developer story for the iPhone was “just write iPhone-optimized web apps”, where by “web apps” they meant “web sites” — something delivered from a remote web server that ran within a page in MobileSafari.


Yes, Palm’s Mojo SDK is based on HTML and CSS for layout and JavaScript for programming. But it includes a real API for WebOS-specific things. JavaScript executing in a WebOS app can do many things that JavaScript running in a browser web page cannot. It’s conceptually very similar to Mac OS X’s Dashboard — WebOS apps are like Dashboard widgets, not web pages. They’re installed on the device, not loaded over the web from a server.


What was frustrating for would-be iPhone Cocoa developers during the period where Apple was telling them to “just write web apps” was that Apple itself, of course, was writing its own iPhone apps using Objective-C. It just wasn’t (and isn’t) possible to write an iPhone web app that looked or felt anywhere near as nice as a real Cocoa Touch iPhone app.


But Mojo, on the other hand, *is* what Palm is using to write its own WebOS apps. They’re up to their ears in Mojo [dogfood](http://en.wikipedia.org/wiki/Eat_one's_own_dog_food). Third-party WebOS apps have the potential to be just as nice as Palm’s WebOS apps, because they’re all written using the Mojo APIs.


It’s an open question whether Mojo will prove to be a weakness (because it’s slower than compiled code), strength (because HTML, CSS, and JavaScript are so familiar to so many existing developers), or non-issue. But however this question is resolved, Palm’s own WebOS apps are in the same boat as third-party apps, which is nothing at all like the pre-SDK iPhone situation.



| **Previous:** | [More on Palm’s WebOS ‘Media Sync’](https://daringfireball.net/2009/06/more_on_webos_media_sync) |
| **Next:** | [WWDC 2009 Predictions](https://daringfireball.net/2009/06/wwdc_2009_predictions) |


PreviousNext