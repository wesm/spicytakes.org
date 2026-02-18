---
title: "It’s All Software"
date: 2011-06-14
url: https://daringfireball.net/2011/06/its_all_software
slug: its_all_software
word_count: 1064
---


Here’s Pascal-Emmanuel Gobry, [writing about iCloud](http://www.businessinsider.com/apple-icloud-microsoft-cloud-2011-6?op=1):


> Here’s how Google and Apple’s vision of the cloud differ: for
> Google, the cloud means cloud + web; for Apple, cloud computing
> means cloud + software, with the internet stuff happening behind
> the scenes.
> All of the cloud computing services Google offers to consumers,
> like email, word processing and spreadsheets, happen within the
> browser. To Google, the point of cloud computing is to replace
> desktop software with the web.


Many — maybe even most — observers share this view of the differences between Apple’s and Google’s approach to cloud-backed software. I think this view is wrong. Where Gobry writes “for Google, the cloud means cloud + web”, he glosses over what “web” is. Web apps like Google Docs and Gmail don’t somehow obviate the need for client-side software. They just change where the client-side software runs, and what APIs it is written against.


In both cases, there are client-side user-facing apps, and back-end services and canonical storage running on servers in the “cloud”. We don’t talk about “[AJAX](http://en.wikipedia.org/wiki/Ajax_(programming))” much any more because it’s become so ubiquitous. But what it means is client-side software written in JavaScript, running in a web browser, communicating with a server using APIs.


Client-side apps and cloud-based servers. Apple’s primary focus is on native Cocoa Touch and Cocoa apps running on iOS devices and Macs. Google’s primary focus is on HTML/CSS/JavaScript apps running in web browsers. Google is not getting away with less work. If anything, they’re doing more work, because it is *harder* to create good user experiences inside a web browser. Where Google benefits from its strategy is reach — Gmail and Google Docs run anywhere with a PC-caliber modern web browser. Cocoa apps run only on Apple-made devices.


Neither company is dogmatic about these priorities, however. Apple has web apps at MobileMe — which [I believe](http://daringfireball.net/linked/2011/06/13/icloud-web-interface) will soon become web apps for iCloud. Google has native apps written for Android (and don’t forget, for iOS, too). But there’s no mistaking where each company’s primary focus is.


The mistake — perhaps this is [where Josh Topolsky went wrong](http://daringfireball.net/linked/2011/06/13/icloud-web-interface) — is to think that what you see in your browser when you type gmail.com *is* Gmail. It’s not. It’s a web-based client to Gmail. Admittedly, it is the flagship client to Gmail — the place where you can manage everything regarding Gmail. And users can and even *should* think of it as *being* Gmail. It’s a complete encapsulation of a powerful fast email service. But a major chunk of it is a client-side app written in JavaScript. (View source in your browser and see.)


I’m biased, insofar as I consider Apple’s strategy more appealing than Google’s. But that’s because my interest lies in having the best possible user experience — the best-looking UIs, the lowest-latency responses, the smoothest animation, the most elegant designs. I share that interest with Apple. Google’s interest is in reaching the largest possible audience. That’s why I chose, at the outset of this paragraph, to say that I find Apple’s strategy “more appealing than”, rather than, say, “superior to”, Google’s. Apple’s strategy is correct for optimizing the quality of the user experience. Google’s strategy is correct for maximizing the number of users for its apps.


But don’t make the mistake of thinking that Google’s strategy involves less work. That’s what I meant last week, [when I wrote](http://daringfireball.net/2011/06/demoted):


> Google’s frame is the browser window. Apple’s frame is the
> screen. That’s what we’ll remember about today’s keynote ten
> years from now.


There’s a simplicity-based argument in favor of web-based apps. Nothing to install, no data that the user is responsible for managing and backing up. Apple solved this with the App Store, though — local native software with truly simple, obvious, easy installation and complete encapsulation of data. Yes, web apps are one solution to the problem of Mac and PC users having to be, to some extent, system administrators. But Apple’s App Store model shows that there are ways to solve that problem without eliminating native apps.


Josh Topolsky, [in his piece questioning Apple’s commitment to web-based apps](http://thisismynext.com/2011/06/13/icloud-apple-strategy-flaw/), wrote:


> There is no native application for the Mac or iOS that replicates
> the shared document editing of Google Docs; there’s no mail
> application that exists for the Mac which will allow me to access
> my important information from anywhere in the world with or
> without a device in hand; there is no photo sharing service for
> iOS or the Mac which is as flexible or accessible as Flickr.


The first clause isn’t true, I’d argue. Shared document editing is not an inherent advantage of Google Docs being web-based; a native client could do it just the same. As the document changes, those changes are reflected live in your browser by way of a stream of API calls between your browser, executing on some device in front of you, and Google’s remote web server. Shared document editing is a difficult problem to solve and Google Docs deserves credit for solving it well, but it has little to do with being rooted in a web browser.1


The third clause is about public sharing: web *sites* versus web apps. And agreed — Apple hasn’t addressed how iCloud will replace MobileMe’s galleries in this regard, and Flickr is better than MobileMe’s gallery anyway.


But that second clause — “there’s no mail application that exists for the Mac which will allow me to access my important information from anywhere in the world with or without a device in hand” — is key to Topolsky’s argument. Access anywhere. Where his argument falls down is “without a device in hand”. Many people may depend upon shared or even public PCs to access their Gmail and Google Docs accounts. But that’s a different audience than Apple’s. When am *I* without a device in hand? Never. As with MobileMe, there will be web app interfaces for iCloud for those times when all you have is a web browser on someone else’s machine, but Apple’s vision for “access anywhere” is “iPhone everywhere”.


---

1. And I’d argue that [SubEthaEdit](http://www.codingmonkeys.de/subethaedit/) is existence proof that shared document editing can work well in a native app with no web interface. ↩︎



| **Previous:** | [Demoted](https://daringfireball.net/2011/06/demoted) |
| **Next:** | [The Final Cut Pro X Backlash](https://daringfireball.net/2011/06/final_cut_pro_x_backlash) |


PreviousNext