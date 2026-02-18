---
title: "Putting What Little We Actually Know About Chrome OS Into Context"
date: 2009-07-10
url: https://daringfireball.net/2009/07/chrome_os_context
slug: chrome_os_context
word_count: 2518
---


It has seemed obvious for some time that Google would someday release a PC OS. I became convinced after they released Android: if they’re creating and giving away a free OS for phones, why not PCs, too? But I expected that Google’s eventual PC OS was going to be an expanded meant-for-a-bigger-screen version of Android — sort of the inverse of what Apple did for the iPhone. Apple took a PC OS and whittled it down to a fundamental core, then built new handheld-specific UI libraries and APIs on top. The hypothetical PC version of Android I’m imagining would have entailed1 taking the core of the mobile Android OS and creating new meant-for-a-PC libraries and APIs on top.


So it’s not weird that Chrome was announced. But what *is* weird is *how* it was announced. And, despite the title of the weblog post in which the announcement was made — “[Introducing the Google Chrome OS](http://googleblog.blogspot.com/2009/07/introducing-google-chrome-os.html)” — nothing has actually been introduced. There aren’t even any screenshots, let alone a demo or any specific technical information. With an expected ship date of “the second half of 2010”, it’s a textbook example of vaporware.


I don’t get the timing. Why announce it now, when it clearly isn’t close to ready? Why not at I/O, Google’s developer conference six weeks ago? Or why not wait until it’s ready to release to developers? I like facts, demos, and best of all, shipping products. I don’t like vague promises.


## Web Apps as Native Apps


It’s certainly interesting and ambitious to state that the entire application platform will consist of web apps. If anyone was going to build such an OS, it’d be Google. Much of the initial commentary regarding Chrome OS has been wholly positive, but one common note of skepticism has been with regard to the “web apps are the only apps” aspect, with the frequent point of comparison being to the 1.0 release of the iPhone OS. E.g., [Nick Mediati at PC World](http://www.pcworld.com/article/168068/is_chrome_os_the_future_of_computing_i_hope_not.html):


> Both users and app developers are still hungry for so-called
> “native” applications — that is, software designed for a particular
> operating system. A prime example? The iPhone. At the 2007
> Worldwide Developers Conference, Apple discussed a “pretty sweet”
> way of developing apps for the iPhone: Web apps. While the Apple
> executives onstage spoke of the potential and power of Web apps,
> many developers and users groaned. They didn’t just want Web apps,
> they wanted real apps—apps that could take full advantage of the
> technology the iPhone offered.


(As an aside, in the 2007 WWDC keynote, Steve Jobs didn’t describe writing web apps as a “pretty sweet” solution for developers who wanted to write software for the iPhone; he described it as a “[*very* sweet solution](http://mjtsai.com/blog/2007/06/13/a-very-sweet-solution/)”. I described it as a “[shit sandwich](http://daringfireball.net/2007/06/wwdc_2007_keynote)”.)


Mediati was right that not just developers but *users* wanted native third party apps for the iPhone. The difference from what Google is promising with Chrome, however, is that web apps *will* be the native apps on the system. Presumably all of the default applications from Google itself will themselves be the Google web apps we already know. It’s an eating-your-own-dog-food issue. What irked about Apple’s endorsement of iPhone-optimized web apps as a “really sweet solution” was that, of course, none of the iPhone’s built-in apps were web apps. They were all written in Objective-C with Cocoa Touch. Apple’s own iPhone apps set a high bar for user experience — a height that could not (and still can’t) be reached with web apps running in MobileSafari.


Chrome OS sounds a lot more like Palm’s WebOS than it does the iPhone. Palm isn’t just telling third-party developers to write apps using HTML, CSS, and JavaScript, they’re doing it themselves with the WebOS’s built-in apps. In fact, considering how web-app centric Google is and always has been, Palm’s WebOS is fundamentally more Google-y than Android, a platform where native apps are written in Java.


One thing to note regarding WebOS, too, is that while a WebOS app is written with HTML, CSS, and JavaScript and runs within a WebKit frame, it can do more than a regular “web app” running in a browser. The runtime exposes additional JavaScript APIs specific to the WebOS environment. Regular web apps — ones you “run” by telling a regular web browser to load via a URL — can’t do things like access the hardware camera or post one of those cool WebOS system-wide notifications at the bottom of the screen. Or, taking the flip side, you couldn’t just take a WebOS app and run it in a web browser on any other platform. There’s a big potential difference between “web apps” and “apps written using web technologies”. If you’re a programmer, I’m sure you understand that; if you’re not, I worry that it sounds like semantic hair-splitting. The best example I can think of are Mac OS X Dashboard widgets: they too are written using HTML, CSS, and JavaScipt, but they don’t work anywhere other than Mac OS X.


I presume that there will be similar Chrome OS-specific APIs for web apps optimized to run on Chrome. But who knows? From the description in the announcement, it sounds like Chrome OS “apps” really could just be web pages. Will it support things like importing photos and videos from a camera? Again, I presume so. But then what gets stored locally and what gets stored remotely, on Google-managed servers in the quote-unquote “cloud”? Something would have to be stored locally, because uploading video (and even just full-size photos) over the Internet can be slow and expensive.


## The Driver Issue


Microsoft has to deal with a veritable mountain of device drivers because Windows has to run on every “Windows PC”. But Microsoft made this problem for themselves. It is Microsoft that decided Windows would run everywhere on everything. No one says Chrome OS is going to run on all, or even *most* PCs. I wouldn’t be surprised if it’s only supported for use on new PCs that are specifically certified to work with it. Hence the hardware partner list in the otherwise almost information-less “[Chrome OS FAQ](http://chrome.blogspot.com/2009/07/google-chrome-os-faq.html)” Google posted tonight.


## Chrome Will Not Be a ‘Linux Distribution’


Renai LeMay’s “[No Thanks Google, We’ve Got Ubuntu](http://www.zdnet.com.au/insight/software/soa/No-thanks-Google-we-ve-got-Ubuntu/0,139023769,339297306,00.htm)” captures another common reaction to Chrome:


> In this context, Google’s decision to create its own Linux
> distribution and splinter the Linux community decisively once
> again can only be seen as foolhardy and self-obsessive.
> Instead of treading its own path, Google should have sought to
> leverage the stellar work already carried out by Mark Shuttleworth
> and his band of merry coders and tied its horse to the Ubuntu cart.


“Linux” means different things to different people. At a precise technical level, Linux is not an operating system. It is a [kernel](http://en.wikipedia.org/wiki/Kernel_(computing)) that can serve as the core for an operating system. What most people mean by “Linux”, though, is an operating system built around the Linux kernel. For use as a desktop PC operating system, all the various “Linux distributions” are basically the same thing: variations of Gnome or KDE sitting atop the ancient [X Window System](http://en.wikipedia.org/wiki/X_Window_System).


Ubuntu is almost certainly the pinnacle of these distributions, but they’re all conceptually the same thing, and the only significant difference is the choice between Gnome and KDE, and even there you’re just choosing between two different environments that are conceptually modeled after Microsoft Windows. The entire X Windows/Gnome/KDE “desktop Linux” racket has never caught any traction with real people.  Almost no one wanted it, wants it, or will want it.


My theory on this is rather simple. Early versions of Gnome and KDE were pretty much just clones of the Microsoft Windows UI. They’ve diverged since then, and I’d say Ubuntu’s default Gnome desktop is in most ways better from a design and usability standpoint than Windows Vista. But it’s still fundamentally a clone of Windows — menu bars within the window, minimize/maximize/close buttons at the top right of the window, the ugly single-character underlines in menu and button names. At a glance it looks like Windows with a different theme. The idea being that if you want Windows users to switch to Gnome or KDE, you’ve got to make it feel familiar. But that’s not how you get people to switch to a new product. People won’t switch to something that’s just a little bit better than what they’re used to. People switch when they see something that is *way* better, *holy shit* better, *wow, this is like ten times better*.2


So I think Gnome and KDE are stuck with a problem similar to the [uncanny valley](http://en.wikipedia.org/wiki/Uncanny_valley). By establishing a conceptual framework that mimicks Windows, they can never really be that much different than Windows, and if they’re not that much different, they can never be that much better. If you want to make something a lot better, you’ve got to make something a lot different.


Whatever Chrome OS turns out to be, it isn’t going to be that kind of “Linux”. They’re using the Linux kernel, yes, but they’re building something new and original on top of that. Linux is to Chrome OS what BSD is to Apple’s iPhone OS — which is to say something that users will never see, smell, or notice.


Everything from TiVo to Palm’s WebOS uses Linux as the kernel for its operating system — using the commodity underlying operating system (in the comp-sci sense of the term) and ignoring the commodity user interface systems. Here’s the telling line from Google’s announcement:


> The software architecture is simple — Google Chrome running within
> a new windowing system on top of a Linux kernel.


From a user-level perspective, Chrome isn’t going to look, act, or work anything like Windows. And that’s why Google has a chance to make something that might actually prove popular in a way that Ubuntu hasn’t.


## An Odd Name


I’m sure what I’m about to suggest is anathema to Google employees, but in addition to the sky high vapor-to-bits ratio, there’s another aspect of the Chrome OS announcement that reminds me of Microsoft: the name. In the same way that Microsoft has used “Windows” to describe very different things — both a computer operating system and [an online suite of web apps](http://home.live.com/) — Google is now using “Chrome” to describe two very different things.


A web browser is very different from an OS, even if the OS only runs the browser. Google themselves recently conducted a survey that suggests that most regular people [do not understand at all what a “web browser” is](http://googlesystem.blogspot.com/2009/06/browser-is-search-engine.html). If regular people are confused about what a browser is, it’s a good bet they’re even more confused about what an “OS” is. Calling them both “Chrome” isn’t going to help clarify the matter. Install Chrome the browser on your PC and if you don’t like it, you can delete it and you’re right back where you were. Install Chrome the OS on your PC and if you don’t like it, you can delete it and you have a blank hard drive. I’m not predicting that people will mistakenly install one when they meant to install the other; I’m just saying that significantly different things should have significantly different names.


## Client-Services, Not Client-Server


There have been numerous client-server systems throughout the history of the computer industry. Some [popular](http://en.wikipedia.org/wiki/VT100); some [not](http://news.cnet.com/Ellison-resurrects-network-computer/2100-1001_3-233137.html). The basic idea behind all of them is that you have many cheap client machines that users actually sit in front of, connected to a few expensive server machines that do most of the actual computing. The complexity is almost entirely on the server side, managed, presumably, by professional experts. A single client machine, unconnected to the network, is pretty much useless.


Chrome OS is in many ways a return to that model. Web apps largely consist of server-side code, with a relatively thin layer of JavaScript that runs on the client. Data, too, mostly resides on the network, not the client machine.


But there’s a big difference. The Chrome OS model isn’t about thin clients connecting to *a* server. It’s about thin clients connecting to *many* and *any* servers. One of the few sure things about Chrome OS is that it’s going to work well with Google’s own web apps, but the web is open, and Google is a strong proponent of open web standards. Everyone will have the opportunity to write web apps that run just as well in Chrome OS as Google’s own.


At an abstract level, there is much appeal to this concept. With all of your data and all of the software you use online, you have nothing to back up. Nothing to migrate when you buy a new computer — just log in from a different Chrome OS machine and there’s all your stuff.


But at a practical level, how well will this actually work? Is it feasible to use Chrome OS as your sole computer? If not, how big is the market for “secondary” computers, especially as (a) more and more people buy laptops to serve as their primary machines, and (b) more and more people buy iPhones and Pres and Android-based mobile phones? I say: not very big. In short, will Chrome OS pass the dog food test: is it something Google’s own engineers will want to use?


I’m skeptical about the prospects of any new system or product that isn’t intended for use by the people creating it. Gmail, for example, is the best web mail system because it was designed to be used not just by “typical” users but by expert users, including the engineers at Google who made it. The iPhone is simple enough to appeal to almost anyone, but guess which phone the people who created it use?


Make something intended not for your own use, but for use by dummies, and you’ll usually wind up creating something dumb. The future of computing probably is in the direction of thin clients connecting to network services for storage and software, but my hunch is that Chrome OS is too thin.


---

1. Or, perhaps, it *will entail* rather than *would have entailed*, as I’m not convinced that the existence of Chrome OS precludes Google from also releasing a PC version of Android. It sure would be odd for Google to produce two competing netbook-optimized OSes, but what little we do know about Chrome OS so far is, well, a little odd. And because they’re both open source, it could be that Android continues evolving into a credible PC OS through community effort alone. ↩︎
2. The group that’s the most enthusiastic about Gnome and KDE desktop Linux systems consists of those who care the most about the political and licensing aspects. With regard to the freedoms that stem from the software being open source, something like Ubuntu isn’t just, say, ten times better than Windows or Mac OS X, it is *infinitely* better. ↩︎



| **Previous:** | [Mobile Phone Keyboards](https://daringfireball.net/2009/07/mobile_phone_keyboards) |
| **Next:** | [Simplenote](https://daringfireball.net/2009/07/simplenote) |


PreviousNext