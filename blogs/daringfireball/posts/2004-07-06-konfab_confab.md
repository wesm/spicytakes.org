---
title: "Konfab Confab"
date: 2004-07-06
url: https://daringfireball.net/2004/07/konfab_confab
slug: konfab_confab
word_count: 1854
---


Assorted follow-up points on the [Dashboard-vs.-Konfabulator](http://daringfireball.net/2004/06/dashboard_vs_konfabulator)
quote-unquote “controversy”:


## Rooting


If I regret anything about the original article, it’s that it might
be construed as my taking Arlo Rose and Perry Clarke to task,
personally, whereas my intended targets were the bystanders loudly
crying foul. To be clear, it wasn’t Rose and Perry who started or
unfairly fanned the flames.


The “Cupertino, Start Your Photocopiers” banner afront
[Konfabulator.com](http://konfabulator.com/) — that’s just good clean marketing fun. What
I did use against them were Rose’s histrionic comments to CNet’s Ina
Fried (e.g. *“It’s insulting, is what it is,” Rose said in a
telephone interview. “They could have at least offered to work with
us or to buy it.”*) But I realize how easy it is to have a quote
taken out of context by a publication like CNet, well-known
practitioners of the hype-any-conflict brand of journalism.


I have nothing against Rose or Clarke, and I’m certainly not rooting
against them.


## The Desk Accessory Analogy


I wasn’t the only person who presented desk accessories as prior
art. Arlo Rose, however, rejected this analogy in an [interview at
Geek Patrol](http://www.geekpatrol.ca/archives/2004/06/28/specialpatrolarlo.php):


> Matt: The point has been raised that Apple had a similar
> concept to the Dashboard in Desk Accessories back in the
> original OS. Do you think this at all validates the
> Dashboard as their own idea?
> Arlo: No, People keep bringing up Desk Accessories. Desk
> Accessories were just mini applications accessed via the
> apple menu. The idea behind K is not so much about the
> basic Widgets as it is about empowering people to easily
> create their own and this is the key part that Dashboard
> duplicates.


Rose is ignoring where the comparison is apt, which is in terms of
scope. Konfabulator widgets and Dashboard gadgets are very much
similar in scope to the roles taken by desk accessories. They are
very much a modern-day equivalent. By Rose’s logic espoused here, he
wouldn’t have had a problem with Dashboard if it were harder to
develop for.


Here’s the connection. Desk accessories were a set of APIs that
allowed early Mac developers to create tiny, focused, single-purpose
apps that could run alongside full applications. They were easily
accessible via the Apple menu (in fact, that was the only thing the
Apple menu was used for originally). Because of the insanely tight
resources — 128 total KB of RAM, 400 KB of disk space, and 8 MHz
CPUs — they were inherently difficult to develop. *You* try writing
a sliding puzzle game in 600 bytes. (Note that this very article is
already 1.6 KB in length; 1.7 including this parenthetical.)


Dashboard is a set of APIs that are going to allow Mac developers to
create tiny, focused, single-purpose apps that run alongside full
applications. They will be easily accessible via Exposé shortcuts.
Because these APIs are based on web standards implemented in
WebCore, they will be inherently easy to develop.


Others have compared Dashboard to Hypercard; e.g. [Dori Smith](http://www.backupbrain.com/2004_06_27_archive.html#a004042):


> It’s about all of us, programmer and non-programmer,
> scripter and non-scripter, being able to, for the first
> time, create little useful applications on our own Macs,
> using simple code and markup (i.e., HTML, CSS, and
> JavaScript; i.e., not AppleScript) that we probably already
> know something about, and then being able to share those
> widgets with anyone who has Tiger.


I would argue with her premise that Dashboard will allow
“non-scripters” to create anything at all — if you’re not a
scripter, it’s going to be tough to write JavaScript, and you don’t
write any JavaScript, your gadgets aren’t going to do much — but,
still, the comparison to Hypercard in terms of ease-of-use is apt.
Many times more Mac users will be able to write Dashboard gadgets
than can write GUI software for their Mac today.


The difference, of course, is that Hypercard was its own world unto
itself. Hypercard used its own scripting language (Hypertalk),
which, no matter how easy you thought it was, was something new to
learn, and something which didn’t work anywhere except in Hypercard. 
And, of course, Dashboard will let you use color.


Dashboard gadgets are like desk accessories in terms of scope — but
they’re different because they’re easier to create. They’re like
Hypercard stacks because they’re easy to create — but they’re different
because they’re based on cross-platform web development standards.


Clearly, much of the same thing can be said of Konfabulator — that
it’s relatively easy to develop for and is based on a standard
language like JavaScript. I never argued that Dashboard isn’t doing
very much the same thing as Konfabulator. But nothing in what
they’re doing is new. My point boils down to this: making it easier
to write client-side software using scripting languages is clearly
something that makes Mac OS X a better platform. That Konfabulator
offered something similar first doesn’t entitle them to anything.


## Look-and-Feel


Another argument against Dashboard is that its widgets “look like”
Konfabulator’s, that regardless of their implementation differences
it’s the fact that they share an unmistakable similarity in terms of
look-and-feel — that that’s what Apple has taken without recompense.


Widget aesthetics are indisputably a major factor in Konfabulator’s
appeal. And while none of the example Dashboard gadgets is
specifically reminiscent of any of the default Konfabulator widgets
— it’s clear that with Dashboard, Apple is aping the overall
gestalt of Konfabulator’s widget aesthetic.


But once again, this isn’t something new to Konfabulator. The
gestalt of widget aesthetics is very much the same as the gestalt of
skinning/theming — a craze that started many years before
Konfabulator existed. E.g., most of the “faces” in [Panic’s Audion](http://www.panic.com/audion/faces.php)
gallery could easily pass as Konfabulator widgets or Dashboard
gadgets — the irregular window shapes, the transparency, the alpha
channel blending. Same for [Winamp](http://www.winamp.com/skins/), whose “skins” probably
deserve to be recognized as the trailblazing example.


What sets Konfabulator’s widgets apart is that they’re
extraordinarily well done. Arlo Rose is a hyper-talented visual
designer; his widgets possess a certain *je ne sais quoi*. But
they’re still just skins, albeit extraordinarily well-done ones.


I don’t think it’s any surprise that Apple’s gadgets are
well-designed too.


Any remaining argument that Apple has “ripped off” Konfabulator
hinges on the idea that Konfabulator is greater than the sum of its
parts. The argument going something like this: *No, they didn’t
invent JavaScript, nor the idea of a scriptable runtime environment
for little single-purpose applets, nor the idea of
arbitrarily-skinnable UIs — but Konfabulator was the first to put
these ideas all together.*


I see Konfabulator as a well done implementation of existing ideas.
If you see it as something deeply innovative, then we’ve reached a
point where we’ll have to respectfully disagree.


## ‘Gadgets’ vs. ‘Widgets’


As for the nomenclatural confusion regarding “gadgets” vs.
“widgets”, here’s a blurb from an email I recieved from a WWDC
attendee:


> According to what I heard, the initial name was “gadgets”
> and Steve vetoed it when he heard it and so they used
> “Widgets”.


Obviously, this is merely scuttlebutt, but it does ring true.
Whatever the reason for Apple’s apparent switch to and appropriation
of “widget”, it’s unfortunate. To the casual observer, it certainly
contributes to the perception that Dashboard is Konfabulator
knock-off, and, worse, it’s unnecessarily antagonistic.


## The Value of Ideas


[Brent Simmons](http://inessential.com/?comments=1&postid=2874):


> What concerns me is the message the Dashboard thing sends.
> It goes like this, “If you come up with a good idea and
> develop a successful product, we might copy it and bundle
> it for free with the OS.”
> In other words, you could be penalized — heavily — for doing a
> good job, for doing exactly what every developer works very
> hard to do.
> It would take so little for Apple to have made the
> Konfabulator folks happy. Some money, some recognition.
> (“Little” is relative: little to Apple, big to the
> Konfabulator folks.) And it would let other developers know
> that Apple cares about OS X developers, that it *wants*
> people to develop for OS X, that it’s *safe* to come up
> with great ideas and great products.


Simmons has an interesting point here, that making Konfabulator’s
developers “happy” in the face of Dashboard would indirectly be good
for Apple too, by easing the concerns of other Mac developers.


My problem with this is that it’s indistinguishable from charity. If
Apple saw Konfabulator as a good idea but not a good implementation
— what would they have been paying for? Good will? Karma?


Where does the line get drawn? Should Apple have bought the rights
to [iCab](http://www.icab.de/) before shipping Safari?


The truth is, Apple *does* buy products from third-party developers.
A former Apple product manager told me via email, “The way [Apple
works] is to buy technology that is better or more promising than
what they may have in-house, and in the absence of such technology,
to invent their own.” Some recent examples: Final Cut (purchased
from Macromedia), SoundJam (now [iTunes](http://www.apple.com/itunes/)), LiveType (purchased from
Prismo, now part of [Final Cut Pro](http://www.apple.com/finalcutpro/)), Spruce Maestro (now part of [DVD
Studio Pro](http://www.apple.com/dvdstudiopro/)), and DVDirector (now part of both [iDVD](http://www.apple.com/ilife/idvd/) and DVD Studio
Pro).


What Apple doesn’t pay for are ideas. I suppose Simmons’s argument
is that it might be a good idea if they did — but I’m unaware of
*any* company that does.


In the comments of his weblog, [Jerry Kindall relays](http://www.jerrykindall.com/2004/06/30_widgets_are_web_pages.asp)
an appropriate anecdote as to the value of ideas versus
implementations of ideas:


> Science fiction writer Larry Niven once said, perceptively,
> that if a fan gives a writer an idea, and the writer goes
> on to write a story from it, the writer owes the fan a
> beer, but no more. Because coming up with ideas is the easy
> part. What matters is what you do with the idea, and I
> think Apple has done more. Arlo and Perry do deserve a beer
> for their trouble, but I don’t see what else Apple could
> owe them.


## Inclusive vs. Exclusive


Using thousands fewer words than I’ve blown on this topic, [Michael
Tsai simply nails it](http://mjtsai.com/blog/2004/06/30/gadget-development/):


> Developing for Dashboard is nothing like developing for Konfabulator. There was almost zero chance that I would develop a widget for Konfabulator. I’d have to [learn](http://konfabulator.com/workshop/) a completely new platform, and anyone who wanted to use my widget would have to buy a license for that platform’s runtime. Dashboard widgets, on the other hand, [are Web pages](http://weblogs.mozillazine.org/hyatt/archives/2004_06.html#005876). I already know HTML and CSS, and I have a collection of tools for working with them. The runtime is free. If I want to use Cocoa or Java, I can do that, too. […]
> The Konfabulator developers are in an unfortunate situation,
> partially of their own making, but what’s getting lost in that
> coverage is that the Mac is now a platform for writing client-side
> Web applications.



| **Previous:** | [The Last-Minute Push](https://daringfireball.net/2004/07/last_minute_push) |
| **Next:** | [Status](https://daringfireball.net/2004/07/status) |


PreviousNext