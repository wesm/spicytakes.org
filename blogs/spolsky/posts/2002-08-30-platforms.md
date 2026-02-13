---
title: "Platforms"
date: 2002-08-30
url: https://www.joelonsoftware.com/2002/08/30/platforms/
word_count: 1618
---


Most software developers, including Fog Creek Software, are perfectly happy just to write software applications. You know, programs that do something or solve some particular problem. But the brave among us want to change the world more significantly, and they choose to work on platforms: big giant slabs of software that don’t quite do anything out of the box, but which enable a whole world of new and interesting applications. So they write operating systems, or DBMSs, or language runtimes like Java, and they hope to attract independent software developers to create the great new applications that their platforms enable.


Almost by definition, an operating system is a platform. Many platforms live on top of operating systems, such as the Java Runtime. And don’t forget that Windows didn’t start out as an OS, it started out as a program you ran on DOS which (out of the box) didn’t do much of anything, but enabled software developers to create GUI applications for inexpensive Intel boxes.


It’s really, really important to figure out if your product is a platform or not, because platforms need to be marketed in a very different way to be successful. That’s because a platform needs to appeal to developers first and foremost, not end users.


I just had the good fortune to read an advance copy of [Rick Chapman’s excellent new book on stupidity](http://www.amazon.com/exec/obidos/tg/detail/-/1590591046/joelonsoftware) in the software industry. (Prediction: best seller). Being an analytical kind of guy, I look for common themes. One of the biggest themes in software industry failures is a platform vendor that didn’t understand that they were a platform vendor, so they alienated their key constituency: the developers.


Example: NetWare took so long to release reasonable tools for creating NLMs that when Unix and Windows NT came along with superior and cheaper development tools, they swept away the mindshare of server software developers.


Example: Apple has spent decades making life miserable for their developers. Every new OS for almost 20 years required tweaks and changes to application code. If you got too successful, Apple competed against you (although sometimes they had a hand puppet called Claris compete against you so they could pretend it wasn’t them.)


Example: Developing software for OS/2 1.0 required an investment of $3000 for the SDK, and you had to write all your own printer drivers if printing was important for you. Printing *was *important, so OS/2 had no applications.


But the counter-examples are just as interesting:


Example: The first versions of Windows included a *freely redistributable runtime* so that if you wrote a Windows application, you could sell it to anyone with DOS, you weren’t limited to the few weirdo dorks (me!) who bought Windows 1.0.


Example: Despite the [mistakes](https://www.joelonsoftware.com/articles/StrategyLetterV.html) that Sun made with Java, the runtime was always free and good Java tools were cheap or free, too. No other development platform became so predominant so quickly (even Visual Basic, the top selling computer language of all time, took years to ramp up.)


If you want a platform to be successful, you need massive adoption, and that means you need developers to develop for it. The best way to kill a platform is to make it hard for developers to build on it. Most of the time, this happens because platform companies either don’t know that they have a platform (they think it’s an application) or they get greedy (they want all the revenue for themselves.)


Greedy platform companies can’t stand the idea of all kinds of unwashed riffraff making money off of *their *platform, so they make it darn near impossible for anyone to develop for it. Probably the most spectacular failure illustrating this was IBM’s PS/2, with its huge portfolio of proprietary technologies, such as the new Microchannel architecture designed to insure that only IBM could make expansion cards. This is, of course, monumentally shortsighted. Nobody wanted PS/2s because, uh, add-in cards weren’t available and they were too expensive when they were. As a platform vendor, you’re only as successful as the people who build on you.


A more subtle problem is when platform vendors don’t think they have a platform, they think they have an application. To illustrate this I’m [once again](https://www.joelonsoftware.com/articles/fog0000000011.html) going to have to pick on [Groove](http://www.groove.net/).


“Why do you keep picking on Groove, Joel?” Three reasons:

- They have an interesting architecture that provides important platform functionality which I could really use in my own products,
- They make it impossible (or at least unrealistic) for ISVs to build on their platform, thus dooming themselves to oblivion, either out of greed or because they think Groove is an application, not a platform,
- and Groove inventor Ray Ozzie has a [weblog](http://www.ozzie.net/blog/), so he can answer me if he thinks I’m off the mark. ([He did](http://www.ozzie.net/blog/stories/2002/09/03/toJoelOnPlatforms.html).)


Here’s how I noticed the Groove problem. I’ve got a product, [CityDesk](http://www.fogcreek.com/CityDesk), for simple desktop web content management. Weblogs, company sites, small organizations, etc. — people who need content management but can’t afford the big systems, don’t control a server anywhere, or just can’t be bothered to mess with installing perl scripts on a server.


As a 1.0 product we’ve got our share of weaknesses. One of the big ones is that people want to collaborate on CityDesk sites over the Internet. A reasonable request. For the next major release, we have to do something about this limitation. Basically, we’ve got two choices. The traditional choice would be to do something client-server: make a CityDesk server you can install somewhere so that everyone can collaborate.


But another choice, which would maintain CityDesk’s benefit of not requiring anything on the server, would be to use a secure peer-to-peer architecture. Something exactly like what Groove provides.


So I thought of porting CityDesk to Groove. Then I noticed that

1. there is no free Groove runtime. Every single one of my customers would have to buy Groove.
2. nobody has Groove yet.


That doomed the Groove idea from the start. I talked to some of the Groove “[partners](http://www.groove.net/partners/top/)” who allegedly *are* developing software for Groove. “Was the Groove relationship worth anything?” I asked. “HA!” they said. “We paid $1500 and in exchange we get less than 10 clickthroughs a month from their web page. A waste of money. We couldn’t even get Groove to share their customer lists with us.”


This is not the kind of platform I want to develop for. Yet, technologically, it is *exactly* the kind of platform I want to develop for, but it’s controlled by a greedy (or clueless) company that is going to choke off their own oxygen — the compelling applications on top of Groove. Ray Ozzie is [going nuts](http://www.ozzie.net/blog/2002/08/28.html) about how cool weblogs are — where’s the weblog application for Groove? Who’s going to write one? [Evan Williams](http://www.evhead.com/), creator of [Blogger](http://www.blogger.com/)? Even Blogger Pro is only $35 a year and that doesn’t go very far to paying for a $99 Groove single user license.


What would happen if the Groove runtime were free? Follow the arc of Windows. It started out with a free runtime that let you run one GUI application at a time. Eventually, many people bought the full version to get the benefits of Windows file management, cut and paste between Windows applications, etc. Then Windows 3.0 came out and was so popular and had so many applications that it was bundled with every PC. Today Windows is like the television tax in Britain. Everybody pays it *except the developer* — when you’re writing software for Windows, it doesn’t cost one extra cent. In fact at no time in the history of Windows did developers ever have to worry about the cost of Windows itself.


Anybody who ever tried to sell software components (ActiveX controls, beans, etc.) knows that you have to have a royalty-free runtime or no developer will touch you with a 10 foot pole. Microsoft even lets you redistribute Jet, a complete relational database engine that is 9/10ths of Microsoft Access, for free. Heck, it’s preinstalled on Windows 2000.


If Groove wants to be a successful platform, they need to do the same thing. A free Groove redistributable would mean that hundreds of applications would spring up which would get the runtime spread far and wide. Many of those users would see the value in buying a full version of Groove with built in collaboration features. Groove services like the [hosted reflectors](http://www.groove.net/products/hosted/) would have a much larger potential audience.


Of course, they can continue down the path of Notes, assuming that the only way to sell software is to wow CEOs with cool Powerpoints and sell $1,000,000 corporate shelfware licenses. Eventually, this made some real money for Lotus, because Notes had one compelling application — email — built in. But imagine if the Notes runtime had been free. If Notes had a software industry sitting on top of it way back in the 80s, some dormroom startup might have made a compelling hypertext application for it instead and preempted the Web. The dreams of huge public Notes networks might have come true. Notes would be as common on PCs as Solitaire. Today it’s just [Another Email System](http://www.ozzie.net/blog/categories/groove/2002/08/20.html#a46), one without much of a future.


I keep picking on Groove, but only because there’s something interesting in there, one of the few technologies that’s interesting enough to care about. Yes, the Groove engineers are architecture astronauts. That’s OK. They’re building architecture. But they’re positioning it like an application and I don’t think Groove will be successful if they do that. Someone else will come along with a P2P architecture and sell it like a component, or make it an open source library (yes, I’m aware of JXTA), and that’s what software developers will use.
