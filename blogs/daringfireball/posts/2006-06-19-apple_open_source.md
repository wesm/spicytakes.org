---
title: "Why Apple Won’t Open Source Its Apps"
date: 2006-06-19
url: https://daringfireball.net/2006/06/apple_open_source
slug: apple_open_source
word_count: 1936
---


Tim Bray’s “[Time to Switch?](http://www.tbray.org/ongoing/When/200x/2006/06/15/Switch-From-Mac)” is a nice tangent to my “[And
Oranges](http://daringfireball.net/2006/06/and_oranges)” piece from Thursday; he’s considering the same Mac OS
X-to-Ubuntu route as Mark Pilgrim, and he lists both reasons why he
wants to switch, as well as some of the issues that would make it
unpleasant.


(His three cited “hard issues” that’d make it difficult to switch
more or less boil down to seamless hardware-OS integration; the “it
just works” factor that has always been one of the biggest
differentiating factors of the Mac: sleep/wake-up for laptops that
just works; WiFi that just works; and external display and video
projector support that just works.)


Bray also suggests — and this is something he’s pitched a few times
before — that Apple ought to release the source code to several of
the applications that come bundled with the OS:


> In particular, it’s bothered me for years that the Apple apps
> [aren’t Open Source](http://www.tbray.org/ongoing/When/200x/2004/03/14/OSMacApps); there are all these irritating
> little misfeatures and shortcomings that I’d be willing and
> maybe able to fix, and there are lots more like me. Since the
> apps are joined at the hip to OS X, there’d be no real
> downside to Apple.
> The real problem, it seems to me (and I think this bothers
> Mark more than he says), is Apple’s [paranoid communication
> culture](http://www.tbray.org/ongoing/When/200x/2005/03/29/Switch#p-1): it is forbidden to say anything except what
> it’s compulsory to say. Apple’s exterior is polished, shiny;
> and entirely opaque. Personally, I think their success has
> been about shipping good products, but I think they believe
> it’s a consequence of the tightness of the lip. I’d rather do
> business with a company I can talk to.


He does have a good technical case for why Apple might want to do
this. His argument, more or less, is that Apple doesn’t need to be
protective of the source to these apps (e.g. Mail, Safari, iCal,
iChat) for competitive reasons, because they’re inextricably tied to
Mac OS X technologies like Cocoa. If they released the source
to iCal, it’s not like it would be that much of a help in allowing
someone to port it or knock it off on Windows or Linux. It’d
probably be easier to do a rip-off of these apps on another platform
by completely re-implementing them rather than using their actual
Cocoa source code.


I.e. Bray is addressing the very common managerial reaction to the
idea of open sourcing proprietary software — that you can’t do it
because your software is a competitive advantage, and that giving
your competitors the source code to your apps would give away your
advantage. I think Bray is right that this doesn’t really apply to
the apps Apple bundles with the system — these apps are a valuable
asset and a major component of the appeal of Mac OS X, but their
strength is in their UI design, not in the code that implements the
designs. Anyone can rip off the best aspects of iCal or Mail just by
looking at them.


Bray further argues, correctly, that the source code to these apps
would be tremendously valuable as a learning tool for Mac
developers. Many good programmers, if not most, prefer to learn by
examining working example code.


Bray even makes it clear that he’d be happy with lowercase open
source, meaning that Apple could release the source code under a
somewhat restrictive license (i.e. not an [Open Source
license](http://www.opensource.org/)) that would forbid using the source code for software
on platforms other than Mac OS X.


These are all good points. But, unfortunately, Apple still can’t do
this. Well, technically, *won’t* do this, but the reasons why they
won’t are so strong that it might as well be *can’t*. (Or, rather,
the reasons are so strong from the perspective of Apple’s executive
management, which is really all that matters since that’s who would
need to make the decision.)


Bray is right that releasing the source code to these apps would be
unlikely to hurt Apple competitively against Windows or Linux, but
he overlooks another form of competition: existing versions of Mac
OS X. The role these apps play isn’t just to make Mac OS X look good
compared to Windows or Linux, but also to help make each new version
of Mac OS X look better than the previous one; i.e. to convince Mac
users that it’s worth paying for the latest upgrade.


If the source code to these apps were made available, the best
features from new versions of these apps could be ported back to
previous versions, lessening the incentive for users to upgrade.


Consider iChat. It seems quite possible that one of the features
planned for the 10.5 version of iChat might be tabbed chat
windows,1 and that this feature
would be considered a selling point for the OS. But if iChat were
already open sourced today, it’s almost a certainty that someone
would have already added tabbed windows to it. Kent Sutherland’s
[Chax](http://www.ksuther.com/chax/) is an input manager hack that adds tabs (and a slew of other
features) to iChat. It’s a clever hack, and works as advertised, but
to me, it very much feels like a hack. I.e. it doesn’t come close to
looking or working the way “tabbed iChat” would look/work if tabbed
chat windows were added to iChat by Apple. If Sutherland had access
to iChat’s source code, he probably could have added tabs to iChat
in a vastly less hacky (if not altogether unhacky) way.


That might be great for iChat users, but it wouldn’t be great for
Apple if they were hoping to use tabbed chat windows as a selling
point for Mac OS X 10.5. Just take a look at the [“new features”
marketing for Tiger](http://www.apple.com/macosx/newfeatures/); about half of it revolves around new
features in the apps Bray wants to see open sourced.


The problem is that even though Apple doesn’t charge for these apps
separately (like they do with the iLife and iWork suites), these
apps aren’t really gratis. They’re parts of the OS — not in the
technical sense, but in the product packaging sense. When you buy a
new version of Mac OS X, you don’t just get the operating system,
you get the OS plus a bunch of apps.


It’s not in Apple’s interests to add high-profile cool new features
to its applications in between major OS releases, and it wouldn’t be
in Apple’s interests to allow enterprising outside developers to do
so, either. This is one reason why Web Kit, the rendering framework,
is open source, but Safari, the application, is not.


The development strategy of unveiling all these new features at once
— in both the OS itself and in the bundled apps — has been
extraordinarily successful for Apple. How many software products can
you think of that have users lining up around the block for a
midnight release party?


It’s reasonable to assume that major new releases of Mac OS X would
still be successful even if Apple released several of its bundled
apps as open source, but would they be *as* successful? Even if you
think they would be — that not one sale’s worth of enthusiasm would
be spoiled — you certainly can’t prove it. And it seems to me
extremely hard to make the case that such a strategy would result in
a net *increase* of sales of new versions of Mac OS X.


Worse, I think it’s easy to make the argument that it *would* hurt
sales. These bundled apps like Safari, iChat, and iCal are one of
the biggest differences between Mac OS X and the classic Mac OS;
back then there was never as much application software that shipped
“for free” with the OS. And even the “free” browser and email client
came from Microsoft, not Apple. I think these apps are a big reason
why new releases of Mac OS X are a much bigger deal, publicity- and
enthusiasm-wise, than new releases of the classic Mac OS were.
(There were no midnight release parties for Mac OS 8.6.)


In short, releasing the source to these apps would be a risk. Not a
risk with a catastrophic downside, but a risk nonetheless. And the
potential upside — the best case scenario from Apple’s perspective
— wouldn’t result in any additional sales. So why take a chance?
Why mess with a strategy that has proven to be lucrative?


You can argue that this sucks, that it ought to be us, the users,
whose interests matter most. And that you shouldn’t have to pay $130
to upgrade your entire OS if the only new features you’re interested
in are in just one of the bundled applications. But that’s not how
it works. Apple is a for-profit corporation, and Mac OS X is one of
their most profitable and most successful products.


Perhaps you find it particularly galling that I’m more or less
saying that the reason they’re not going to do what Bray suggests —
despite the fact that following Bray’s suggestion really would be
cool for users and developers in all sorts of ways — is that it
might cost them upgrade sales from users who have already paid for
previous versions of Mac OS X. Such gall is one factor that drives
people to open source platforms.


But there’s a flip side to this equation, which is that developing
good software takes time and talent, and time and talent cost money.
Some portion of the revenue from sales of Mac OS X goes back into
funding development of future versions of Mac OS X.


This is the dichotomy between closed and open source software
development. I’m right there with Bray regarding the frustration of
using an app that’s very cool and really good but that there’s just
a couple of small things that I’d rather see done differently or
better, but which I can’t fix or change other than by petitioning
the developer to implement my suggestions. (Good luck writing “Dear
Apple” letters asking for tweaks to their software.) But while open
source software is, by definition, eminently tweakable, it also, in
general, is less likely to get to the point of being very cool and
really good in the first place. (E.g. where’s the open source
calendar app that’s as simple and uncluttered as iCal?)


Of course there are exceptions, like, say, [Adium](http://adiumx.com/), the open source
Mac OS X chat client that a lot of people flat-out prefer to iChat.
It has a most excellent tab implementation and supports a bunch of
IM platforms that iChat doesn’t, like Yahoo and MSN. Or [Camino](http://caminobrowser.org/),
the excellent Mac-native offshoot of the Mozilla project, and which
compares pretty well against Safari.


But no one is trying to make a buck by selling licenses or upgrades
to Adium or Camino. Open source software tends to improve in small,
steady, frequent increments. Established commercial software tends
to improve less frequently but in large gulps so as to entice users
to pay for upgrades.


The fact that Apple’s Macintosh business still fundamentally
revolves around profits from hardware sales does mean that it’s
possible that they could heed Bray’s suggestion (I’d say Safari
would be the mostly likely candidate, considering the success of the
Web Kit project), and if they do, I’ll be happy to have been wrong.


But don’t hold your breath.


---

1. Admittedly, this might just be wishful thinking on the part of yours truly. ↩︎



| **Previous:** | [And Oranges](https://daringfireball.net/2006/06/and_oranges) |
| **Next:** | [Interoperability and DRM Are Mutually Exclusive](https://daringfireball.net/2006/06/drm_interoperability) |


PreviousNext