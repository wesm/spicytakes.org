---
title: "I’ll See You Intel"
date: 2005-06-05
url: https://daringfireball.net/2005/06/see_you_intel
slug: see_you_intel
word_count: 1282
---


So this one’s going to have a short lifespan, given that come Monday’s
WWDC keynote, all of this weekend speculation is moot. But, come on,
how can I resist?


In a nut:

- Late Friday — 5 pm Pacific — CNet published an article by
reporter Stephen Shankland, and the title pretty much said it all:
“[Apple to ditch IBM, switch to Intel chips](http://news.com.com/Apple+to+ditch+IBM%2C+switch+to+Intel+chips/2100-1006_3-5731398.html)”.
- On Saturday, the Wall Street Journal [seconded](http://online.wsj.com/article/0,,SB111791696757050994,00.html) CNet’s story.
You need a paid subscription to read it, but Paul Thurrott — who
has been [writing about this](http://www.internet-nexus.com/2005_05_22_archive.htm) for weeks — [has an excerpt](http://www.internet-nexus.com/2005_05_29_archive.htm#111792724758537320).


It’s essential to note that neither CNet nor the Journal are reporting
this as a rumor. Two weeks ago, when the Journal first published
something about this, they left themselves several outs: the only
thing they reported as having happened for certain is that Apple had met
with Intel and was considering the switch. They explicitly mentioned
that talks could fall through; thus, regardless if it panned out, they
could claim the article was accurate.


This time, however, both CNet and the Journal are reporting this as a fait
accompli. Both reports flatly state that Apple is moving the entire
Mac platform to Intel processors, and Jobs is announcing it Monday at
the WWDC keynote.


CNet:


> Apple has used IBM’s PowerPC processors since 1994, but will begin a
> phased transition to Intel’s chips, sources familiar with the
> situation said. Apple plans to move lower-end computers such as the
> Mac Mini to Intel chips in mid-2006 and higher-end models such as the
> Power Mac in mid-2007, sources said.


The Wall Street Journal:


> Apple Computer Inc. is expected to announce Monday that it will begin
> shifting its Macintosh computer line next year to Intel Corp. chips,
> people familiar with the situation said.
> The move is a major change in strategy by Apple, a high-profile win
> for Intel, and a potential blow to International Business Machines
> Corp. and Freescale Semiconductor Inc., suppliers of the PowerPC
> chips that Apple has long used in its Macintosh systems.


What this means is that something extraordinary *must* occur: either
Apple is going to announce the biggest hardware transition in company
history (and, arguably, *industry* history), or, two well-respected news
organizations have committed enormous blunders.


Some of you may be willing to chalk this up to the latter, on the
grounds that you see all sorts of bullshit get published that doesn’t
pan out. That’s true, but not in CNet, which has a pretty good track
record, and certainly not in the Wall Street Journal, which many
consider the most-respected newspaper in the world (editorial page
politics being a wholly separate issue).


If it doesn’t happen, this is a catastrophic reporting blunder. There
is no “maybe” in either report.


No matter how [unlikely I think it is](http://daringfireball.net/2005/05/intelmania) that Apple is about to move
the Mac to Intel processors, I think it’s even *less* likely that the
Wall Street Journal would publish a story this wrong.


So, let’s assume here that it’s true. What then?


The only way this makes any sense is that there’s something else.
Something big. Not that CNet and the Journal have the story wrong, but
that they only have part of the story — and the part they don’t have
is what’s going to knock our socks off.


If there’s nothing more to the story — if it’s just a case of Apple
switching the Mac from PowerPC to x86 Intel processors — it makes no
sense. There is nothing in these reports that addresses any of the
issues that make this switch so improbable.


For one thing, if they announce tomorrow that they’re moving to Intel
processors, and but that high-end PowerMacs won’t make the transition
until “mid-2007” — as reported by CNet — how will Apple avoid the
[Osborne effect](http://en.wikipedia.org/wiki/Osborne_effect), wherein by pre-announcing future hardware, sales of
current hardware evaporate?


(And why would Apple transition lower-end machines like the Mac Mini
first? Apple has always introduced new processors at the high end, and
they trickle down the product line over the course of a few years.)


It can’t just be that they’re switching for kicks. It’s not
performance — sure, G5 processor speeds haven’t progressed as quickly
as Apple had hoped (and as Jobs had predicted publicly at WWDC two
years ago), but that’s a problem that has stricken the entire
semiconductor industry. As reported in the 30 May 2005 issue of [MDJ](http://macjournals.com/mdj/),
since the day of the G5 introduction at WWDC 2003, the top-of-the-line
G5 has seen a larger percentage increase in clock rate (2.0 to 2.7
GHz) than Intel’s Pentium 4 (3.2 to 3.8 GHz).


Some argue that it’s about cost, but I have yet to see a single such
argument backed by actual numbers — the cost per unit Apple would save
after switching.


So, there has to be something else. But what?


I can’t think of a single scenario, no matter how contrived, that both
fits with what CNet and the Journal have reported and makes sense for
Apple and its customers and developers. But I can think of a few
scenarios wherein CNet and the Journal are mostly or sort-of right.


## Intel, but Not x86


One idea is that Apple *is* switching to Intel processors, but *not*
to x86. Instead, perhaps, Intel is set to begin production of PowerPC
processors. This sounds unlikely, but is it any less likely than Apple
switching to x86?


Licensing-wise, I believe (but I could definitely be wrong) this could
happen, because of the rights Apple holds to the PowerPC platform. It
would certainly make sense for Apple, because it wouldn’t involve a
transition to a different CPU architecture. It wouldn’t be a switch;
it’d just be a new addition to the PowerPC family. Mac developers
wouldn’t need to recompile or rewrite their software; Apple wouldn’t
need to worry about people trying to get Mac OS X running on commodity
x86 PC hardware.


It might make sense for Intel, too. The Mac is no longer the only
major PowerPC platform. All three next-generation video game consoles
— PlayStation 3, Xbox 360, and Nintendo Revolution — are based on
PowerPC processors. Getting into the PowerPC business would not
necessarily mean only producing chips for Apple.


This would further explain why these stories have only centered around
Intel, and haven’t mentioned AMD.


But: the [Wall Street Journal report](http://online.wsj.com/article/0,,SB111791696757050994,00.html) explicitly states that Apple
is switching the Mac to x86:


> Apple’s decision, which comes after years of industry speculation and
> behind-the-scenes lobbying by Intel, could cause disruptions for
> users of the Macintosh. Among other things, application programs will
> have to be adapted to run on Intel’s x86 chips, the calculating
> engines used in most personal computers that run Microsoft Corp.’s
> Windows operating system.


## Emulation


Software emulation of the PowerPC instruction set on x86 processors,
with acceptable performance, still strikes me as completely
unfeasible. But what if I’m wrong?


MacRumors.com, for example, [points to](http://www.macrumors.com/pages/2005/02/20050225022048.shtml) a company called [Transitive Technologies](http://transitive.com/), whose slogan is: “Our software allows any software
application binary to run on any processor / operating system.”


And, as pointed out by Christopher Ong on the MacJournals-Talk mailing
list, Transitive’s board chairman is Peter van Cuylenburg, who —
according to his [biography on the Transitive web site](http://www.transitive.com/van_Cuylenburg.htm) — was
the president and COO of a certain company called NeXT Computer in
1992.


With a fast enough emulator, the transition to x86 could be just as
smooth as the 680 × 0-to-PowerPC transition a decade ago.



| **Previous:** | [Tiger Adoption Rate](https://daringfireball.net/2005/06/tiger_adoption_rate) |
| **Next:** | [Intel-Apple Odds and Ends](https://daringfireball.net/2005/06/intel_apple_odds_and_ends) |


PreviousNext