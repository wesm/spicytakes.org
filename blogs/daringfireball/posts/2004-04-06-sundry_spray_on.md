---
title: "Sundry ‘Spray-On’ Clarifications and Corrections"
date: 2004-04-06
url: https://daringfireball.net/2004/04/sundry_spray_on
slug: sundry_spray_on
word_count: 1358
---


## Parallel Ports


First, forget the crack about parallel ports. Please. You have
no idea how much email I got about this.


To answer the most frequent question, no, I wouldn’t throw out a
working, reliable laser printer just because it had a parallel
port interface. What *I* would do is spend $50-60 on something
like [this](http://netgear.com/products/prod_details.php?prodID=143&view=) so that I could just plug it into my network and
be done with it. But hooking it up to one computer and then
sharing it using software is perfectly reasonable.


## Mozilla


Also, forget what I wrote about the Mozilla project being an
example of an open source project that has produced some decent
GUI software (Camino and Firefox) thanks to extensive corporate
backing. Camino and Firefox *are* good apps, but [Matthew “MPT”
Thomas points out why they aren’t good examples](http://mpt.phrasewise.com/2004/04/03#a376) of the
point I was trying to make:


> Yes, Camino and Firefox were begun by Netscape programmers. But in the early
>   days of both projects (then known as Chimera and mozilla/browser, respectively),
>   those programmers ([Mike
>   Pinkerton](http://weblogs.mozillazine.org/pinkerton/) for Chimera, [Ben Goodger](http://bengoodger.com/) and
>   [Blake Ross](http://blakeross.com/) for mozilla/browser, and [Dave Hyatt](http://weblogs.mozillazine.org/hyatt/) for both) were
>   terrified that Netscape would shut them down.
> Camino and Firefox are as well-designed as they are because:
> they’re not designed by Netscape’s incompetent designers (like
>   the Mozilla suite, and especially Netscape 6/7, were),
> they have few primary developers, and
> those primary developers have become fairly good at design as well as
>   programming.
> Unfortunately the developers of most other Free Software projects
>   aren’t as good.


## Chicken vs. Egg


I argue:

1. The user interface — the entire user *experience* —
should be designed first, and the underlying implementation
should be built to support the design.
2. Thus, the traditional Unix/Linux development model, wherein
back-end implementations are written first, and GUI
“wrappers” are written around them later, is completely
backwards.


A bunch of people seem to think this argument is at least partly
undermined by the fact that Mac OS X wraps a GUI around CUPS,
the same underlying print architecture that gave Eric Raymond
fits. (MPT, for example, mentions this.)


But I don’t see this as a contradiction. For one thing, Mac OS
X’s print architecture is a lot more than just a “wrapper”
around CUPS. But even if I concede this point with regard to
CUPS, it’d be an exception, not the norm.


Yes, Mac OS X is built with lots of open source software under
the hood. But point #1 doesn’t imply that the entire
implementation needs to be written from scratch. Yes, Mac OS X
contains a lot of open source software under the hood — but
these components are used to implement Apple’s designs, not the
other way around.


## Switchers to Mac OS X


What seemed to tie a lot of knickers into knots — especially in
the Slashdot crowd — was my assertion that “Unix nerds who care
about usability are switching to Mac OS X in droves,” and that
those who remain are “either cheapskates or free-software
political zealots”.


I heard from Linux users who claim to be neither cheapskates nor
political zealots, but who have no intention of switching to Mac
OS X, under any circumstances, ever. The reasons vary, but
common ones include:

- Mac OS X does not have an option for “[focus follows mouse](http://www.wlug.org.nz/FocusFollowsMouse)”.
- Mac OS X does not allow you to use a different [window manager](http://xwinman.org/intro.html).
- You can’t change the way Mac OS X looks without resorting
to unsupported hacks.


But the particular reasons don’t really matter. It all boils
down to the fact that most aspects of Mac OS X are not designed
to be configurable or replacable; they are designed to be
usable, and to fit in with the design of the rest of the system.


They’re also designed to work specifically with Apple’s own
hardware — which many of these “I’m not a cheapskate but I
don’t want to pay for Apple hardware” types refuse to recognize
as a huge usability advantage for Mac OS X.


I didn’t say “Unix nerds” are switching to Mac OS X in droves; I
said “Unix nerds *who care about usability*”. People who want a
Unix system that just works, so they can get on with their real
work — those are the ones who are switching. As opposed to Unix
nerds whose interest is the computer itself, and who want to
tinker with it at any and every level — i.e. Unix nerds who do
not care about usability.


## Rootin’-Tootin’


Perhaps the biggest misconception is that I’m somehow “rooting
against” desktop Linux. I really don’t see how anything I’ve
written implies that, unless you subscribe to the “if you’re not
with us, you’re against us” school of thought.


Regardless, it’s not the case. I’m not rooting against desktop
Linux, nor have I ever claimed it can’t succeed. What I am
saying is:

1. It hasn’t succeeded yet.
2. It’s unlikely to succeed without direction and substantial
commercial support.


Where by “succeed” I mean “provide a terrific user experience”.


The commercial support is there. Companies like Novell and Red
Hat (and others) are employing teams of open source developers,
many of whom care very much about UI design. But the key word
here is *direction*.


Good UI design will never be forged by community consensus.
Bottom-up design won’t lead to a coherent and unified whole.
Cf. [John Siracusa’s comments about desktop Linux](http://www.usercreations.com/weblog/gems/SiracusaInterview.htm) in his
interview with Robb Beal:


> Right now, the Linux community values “diversity” too highly to ever
> get a single, consistent GUI, let alone a good one. At the same time,
> it holds on doggedly to its (often ancient) Unix-rooted traditions and
> conventions. Finally, it’s hard to get a really large group of Linux
> developers to do much of anything beyond a single “project.” A GUI is
> not a “project”. It’s the whole OS from the user’s perspective, and it
> must be from the creators’ perspective too or it will fail.
> I think Linux as an institution is allergic to a good, consistent GUI.
> Their priorities are reversed. They want to build a GUI on top of an
> OS. If they want to compete on the desktop, they should be building an
> OS to power their GUI. Of course, they don’t have a GUI, which is
> problem number one.
> They need to think of what they want the user experience to be, and
> then design a system that provides that experience. Period. This is so
> basic that even Apple forgets it from time to time. If you don’t know
> where you want to go, you’re never going to get there.


[Havoc Pennington](http://log.ometer.com/) — who works for Red Hat as a leading
developer/designer for the Gnome desktop — [gets it](http://log.ometer.com/2004-04.html#2):


> At Red Hat, we’re building the desktop team around a top-down
> design-first approach, driven by professional interaction designers.
> We’ll see how it works out. It will take some time before the first
> results are visible.


The key is that there’s never going to be a good desktop user
interface for Linux that pleases the Linux nerds who don’t care
about usability. If the reason you use Linux is that you value
tweakability over usability, or if you get off on the fact that
a normal person couldn’t sit down in front of your computer and
figure out how to use it, you’re probably not going to like a
system that doesn’t even *have* a replaceable “window manager”.
Trying to create a cohesive GUI system that appeals to these
guys is like trying to write music that appeals to the tone
deaf.


The worst part is that if anyone succeeds at putting together a
usable desktop for Linux, these anti-usability Linux advocates
will piss all over it.


It’s not worth listening to the opinions of assholes; and but
once you shut them off, they just get angrier.



| **Previous:** | [Ronco Spray-On Usability](https://daringfireball.net/2004/04/spray_on_usability) |
| **Next:** | [Preferences](https://daringfireball.net/2004/04/preferences) |


PreviousNext