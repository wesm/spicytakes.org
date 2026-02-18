---
title: "Intel-mania"
date: 2005-05-27
url: https://daringfireball.net/2005/05/intelmania
slug: intelmania
word_count: 966
---


[Moore’s Law](http://en.wikipedia.org/wiki/Moore's_law) states that every 18-24 months, CPU processing power
doubles.


Here then is another law: every 18-24 months, the tech industry will
be captivated by unsubstantiated rumors that Apple is switching the
Macintosh to Intel (or Intel-compatible) processors. Cf. “[Qwerty](https://daringfireball.net/2003/04/qwerty)”,
published here two years ago in the face of very similar rumors.


The current round of Apple-Intel rumors stems from [this report](http://online.wsj.com/article/0,,SB111680203134440188,00.html?mod=home_whats_news_us)
earlier this week in The Wall Street Journal’s “Heard on the Street”
column — the Journal’s equivalent of a rumor column. That link
requires a paid Journal subscription, but [Paul Thurrott has a long
excerpt](http://www.internet-nexus.com/2005_05_22_archive.htm#111685436354669360) on his weblog. Here’s how the Journal sources the
information:


> Two industry executives with knowledge of recent discussions
> between the companies said Apple will agree to use Intel chips …
> Talks between Apple and Intel could founder, as they have before,
> or Apple could be engaging in negotiations with Intel to gain
> leverage over IBM.


Note that the Journal does *not* imply that either “industry
executive” works at either Apple or Intel.


This rumor has gained traction because it’s fairly obvious that Apple
is not happy with IBM’s G5 production. When the PowerMac G5 was
introduced at WWDC 2003, Steve Jobs famously predicted they’d have
systems running at 3 GHz within a year. It’s now two years later and
Apple’s fastest system runs at only 2.7 GHz. That’s not to say a
top-of-the-line PowerMac G5 isn’t a nice computer, but you certainly
don’t hear any talk about them being the fastest PCs in the world
anymore.


So, yes, there’s a motive for Apple to consider such a switch. But
that doesn’t make it plausible. None of this week’s Apple-Intel rumor
reports seriously address the enormous hurdles Apple would face if
they made such a switch.


The biggest of which is, simply, software compatibility. All existing
Mac OS X software would need to be recompiled for an Intel processor
architecture. A decade ago, when Apple switched the Mac from
Motorola’s 680 × 0 family of processors to the PowerPC, the transition
was nearly seamless because the PowerPC was capable of emulating the
680 × 0 at very reasonable speeds. But emulation is out of the question
for a switch now — Intel chips may be faster than current PowerPC
G5s, but they are nowhere near fast enough to emulate them at an
acceptable speed.


The only plausible scenario I can imagine would be for Apple to
pre-announce the move to x86 (say, at WWDC) to get developers on board
a year or more in advance. The idea is that by the time Apple released
the new Intel-powered Macs, developers would have had time to develop,
test, and release Intel-compatible software updates.


The problem with this scenario is not technical. It’d be a piece of
cake for Apple to roll out an update of Xcode that generates such
dual-binary apps — the compiler at the heart of Xcode is [GCC](http://gcc.gnu.org/), and
if anything, GCC is better at generating x86 code than it is PowerPC
code. [Darwin](http://developer.apple.com/darwin/) already officially supports x86 processors, and it seems
quite plausible that Apple secretly keeps the rest of Mac OS X’s
source code compilable on x86 processors. (NextStep supported multiple
processor architectures.)


No, the obvious problem with this idea is marketing: the minute
Apple announces they’re moving to x86 processors, sales of current
hardware dry up. Who’s going to spend $3000 for a deprecated CPU
architecture?


But they’d have to pre-announce the move in order to give developers
time to recompile — and in some cases re-write portions of — their
software. Apple couldn’t just spring the new machines unannounced;
who’d buy a Mac that ran *no* existing third-party Mac software?


My advice is to pay no heed whatsoever to any Macintosh-to-Intel
rumors that don’t address this issue. The fact that it’s technically
possible doesn’t mean there’s a good business case for such a move.
It’s wise for Apple to keep such a move available as an option, in
case something drastic happens to the PowerPC processor family. But
the current performance gap, while serious, is far from drastic.


Also note that it is entirely possible that Apple is planning to use
Intel chips, but for something other than Mac CPUs. Perhaps a
next-generation iPod, or a new iPod-like consumer electronics media
gadget. Or maybe a next-generation AirPort system, with higher
bandwidth and range, based on [WiMAX](http://www.intel.com/netcomms/technologies/wimax/). Such a deal would make perfect
sense — Intel makes great chips, and Apple has been making great new
products other than Macs. But that’s not what the Journal and others
have reported; this week’s rumors are that Apple is moving the Mac to
Intel.


(Paul Thurrott even [managed to attach](http://www.internet-nexus.com/2005_05_22_archive.htm#111690362236228815) the Mac-to-Intel rumor
to the other great recurring Mac rumor fantasy — the fabled “tablet”
Mac. Just remember that a tablet-shaped gadget is not necessarily a
tablet-shaped Mac.)


Reading between the lines, I think this is less about whether Apple
actually intends to switch processors, and more about planted leaks
intended to spur IBM. (For what it’s worth, the Journal article
mentions this as a possibility; but few of the sites that breathlessly
linked to the story mentioned anything more than the “The Wall Street
Journal says Apple is moving the Mac to Intel!” part.) More than just
the money IBM makes from Apple under their current arrangement,
there’s also the pride/publicity factor: the underlying theme of this
rumor is that Apple might turn to Intel because IBM can’t compete
against Intel’s technology. Whether it’s a fair assessment or not,
it’s not the sort of idea IBM wants in the public’s conventional
wisdom.


My prediction: I’ll be writing about this again in 2007.



| **Previous:** | [I Suppose It Has to Be OK](https://daringfireball.net/2005/05/has_to_be_ok) |
| **Next:** | [Tiger Adoption Rate](https://daringfireball.net/2005/06/tiger_adoption_rate) |


PreviousNext