---
title: "Broken Windows"
date: 2004-06-04
url: https://daringfireball.net/2004/06/broken_windows
slug: broken_windows
word_count: 2027
---


Here’s a billion-dollar question: Why are Windows users besieged by
security exploits, but Mac users are not?


For the sake of this discussion, let’s consider the realm of
“security” to encompass any sort of software running on your
computer, which software you wish weren’t there. So we’re not just
talking about viruses/worms/Trojan horses — we’re talking about
crapware of any sort, including *adware* and *spyware*.


Adware is software that displays advertisements, typically in pop-up
windows. Web surfers have been cursed by pop-up ads for years, but
it’s common knowledge that they’re pretty much just a problem for
Windows users these days, because every modern browser other than
Internet Explorer has a pop-up blocking feature. If you have adware
installed on your computer, however, even switching to a
pop-up-blocking browser won’t make them stop — the ads are coming
from hidden applications running on your computer.


Spyware is any sort of software that secretly records information
about you — anything from the web sites you visit, to logging all
the keystrokes you type. Obviously, there’s a fine line between
spyware and Trojan horses.


What’s remarkable is this: Crapware is a problem of epidemic
proportions on Windows, but it is almost completely non-existent on
the Mac.


How big a problem is it on Windows? EarthLink offers a free program
called [Spy Audit](http://www.earthlink.net/spyaudit/) which scans your PC for various forms of
crapware; in March, they [published a report](http://www.earthlink.net/spyaudit/press/) showing that after
scanning over one million PCs, Spy Audit had identified nearly 30
million instances of “spyware”, nearly 28 instances per PC scanned.


Now, obviously, these results are bit self-selecting, in that the
people who suspect their PC has been infested by spyware are a lot
more likely run Spy Audit than those running clean systems. And
EarthLink is counting cookies from known adware-tracking web sites
as instances of “spyware”, which I find tenuous — but still, they
also found 5 million adware applications, and over 350,000 Trojan
horses and “system monitors”.


A similar audit of Macs might well find nefarious cookies, but would
it find adware or spyware? Any at all? If there exists any such
software for the Mac, I haven’t heard of it.


## No Place to Hide


It’s not like Mac OS X is impervious to crapware. Adware, for
example, is just software that displays ads. Anyone with an Intro to
Cocoa book could put together an application that displays ads in a
pop-up window.


One difference between Mac OS X and Windows, however, is that Mac OS
X doesn’t offer nearly as many places for nefarious software to
hide. A major aspect to the scourge of crapware is that it’s
extraordinarily difficult to find and remove it. This isn’t just
about “typical” users; even expert Windows users get hit by crapware
and can’t figure out how to get rid of it.


E.g. Dave Winer, who last week installed the “free” version of Kazaa
and ended up with “[Popups all over the place. Tons of virusware
installed.](http://archive.scripting.com/2004/05/27#servesMeRight)” Winer spent an entire day digging out.


Or, e.g., Paul Thurrott, long-time author of the [WinInfo](http://www.winnetmag.com/windowspaulthurrott/) web
site and [numerous](http://www.xphomenetworking.com/) [books](http://www.microsoft.com/mspress/books/6234.asp) [about](http://www.xpdigitalmedia.com/) Windows. Last week,
[Thurrott was hit by a Trojan horse](http://www.winnetmag.com/Articles/Print.cfm?ArticleID=42787):


> On Sunday night, while preparing for a trip Monday to New
> York, the notebook I had planned to bring was suddenly
> struck by the most malicious software (malware) I’ve ever
> encountered. This Trojan horse got through my defenses
> despite the fact that I was running the Release Candidate 1
> (RC1) version of Windows XP Service Pack 2 (SP2) with the
> firewall turned on. It was infuriating, and after hours of
> investigating, deep cleaning with various antivirus and
> spyware products, and consulting with my technical guru
> (Storage Update’s Keith Furman, a lifesaver), I finally
> gave up. As I write this commentary, I’m heading to New
> York by train, using a different machine, and my infected
> laptop is home, awaiting a complete wipeout. I never did
> completely clean up the machine, and I’m still frustrated
> by the defeat.


Given Thurrott’s consistent record as a [bona fide asshat](http://daringfireball.net/2004/01/the_hbomb#jackass)
regarding all things Mac, could this rate any higher on the
schadenfreude-o-meter? Hours of work to remove a Trojan, all in
vain, and resigned to a “complete wipeout”?


There are all sorts of ways that Windows executes software that
don’t have equivalents on Mac OS X. Services get installed in the
Windows Registry, and the Registry is an opaque labyrinth.


This just isn’t a problem on the Mac. Even if you ended up with
piece of crapware installed, there simply aren’t that many places
where it could hide. Assuming the crapware needs to launch itself
automatically, it’s either going to be installed in one of the
various /Library sub-folders, or it has to be listed in your user
account’s Startup Items in the Accounts panel of System Preferences.


## Zero Tolerance


You could argue that many Mac OS X users have no idea where their
Startup Items are listed, or about the contents of the various
/Library folders — but plenty of Mac users do. Certainly a Mac user
with the same expertise as Winer or Thurrott would know about these
locations.


We all benefit from the fact that the Mac community has zero
tolerance for vulnerabilities. Not just zero tolerance for security
*exploits*, but zero tolerance for *vulnerabilities*. In fact, there
is zero tolerance in the Mac community for crapware of any kind.


If some “freeware” software for the Mac surreptitiously installed
some sort of adware/spyware/crapware, there’d be reports all over
the Mac web within days. Uninstallation instructions would be posted
(and thus made available to all [via Google](http://daringfireball.net/2004/05/writing_for_google)), and the
developer who shipped the app would be excoriated.


Zero tolerance, on the part of the user community, is the only
policy that can work.


It’s similar to the “broken windows” theory of urban decay, which
holds that if a single window is left unrepaired in a building, in
fairly short order, the remaining windows in the building will be
broken. Fixing windows as soon as they are broken sends a message:
that vandalism will not be tolerated. But *not* fixing windows also
sends a message: that vandalism is acceptable. Worse, once a problem
such as vandalism starts, if left unchecked, it flourishes.


This theory was made famous in a 1982 article by [James Q. Wilson
and George L. Kelling in *The Atlantic Monthly*](http://www.theatlantic.com/politics/crime/windows.htm). They wrote:


> That link [between maintaining civil order and preventing
> crime] is similar to the process whereby one broken window
> becomes many. The citizen who fears the ill-smelling drunk,
> the rowdy teenager, or the importuning beggar is not merely
> expressing his distaste for unseemly behavior; he is also
> giving voice to a bit of folk wisdom that happens to be a
> correct generalization — namely, that serious street crime
> flourishes in areas in which disorderly behavior goes
> unchecked. The unchecked panhandler is, in effect, the
> first broken window. Muggers and robbers, whether
> opportunistic or professional, believe they reduce their
> chances of being caught or even identified if they operate
> on streets where potential victims are already intimidated
> by prevailing conditions. If the neighborhood cannot keep a
> bothersome panhandler from annoying passersby, the thief
> may reason, it is even less likely to call the police to
> identify a potential mugger or to interfere if the mugging
> actually takes place.


It should be obvious where we’re heading with this.


My answer to question posed earlier — why are Windows users
besieged with security exploits, while Mac users suffer none? — is
that Windows is like a bad neighborhood, strewn with litter,
mysterious odors, panhandlers, and untold dozens of petty
annoyances. Many Windows users are simply resigned to the fact that
their computers contain software that is not under their control.
And if they’ll tolerate an annoying application that badgers them
with pop-up ads, well, why *not* a spyware virus that logs every key
you type, then sends them back to the creator? (That’s a real virus,
by the way, [Korgo](http://www.overclockersclub.com/?read=8636435), which hit Windows at the end of May and is
spreading quickly.)


The Mac is like a good neighborhood, where the streets are clean and
the crime rate low. You don’t need bars on your windows in a good
neighborhood; you don’t need anti-virus software on the Mac.


Windows apologists have long argued that the only reason the Mac has
been so strikingly free of security exploits is that it has such a
smaller market share than Windows. This argument ignores numerous
facts, such as that the Mac’s share of viruses is effectively
*zero*; no matter how you peg the Mac’s overall market share, its
share of viruses/worms/Trojans is significantly disproportionate. Or
that the logical conclusion of this argument — that because of
Windows’s monopoly market share, malfeasant hackers would logically
*only* write software to attack Windows — would be to extend the
argument to *all* software, malicious or not, and it’s quite easily
disproven that “all software” is targeted only for Windows. Or
that, despite the Mac’s relatively small market share, a successful
virus/worm/Trojan attack against Mac OS X would likely garner
significantly more notoriety and fame; considering the recent
publicity given to *non-exploited* Mac OS X vulnerabilities, it’s
reasonable to expect that an outright exploit would result in an
avalanche of tech media hysteria.


The reason this argument is so popular with Windows apologists is
that it’s a convenient bit of rhetoric. They say it’s so, we say
it’s not. You can’t get past this argument, because *it can’t be
disproven* without the Mac OS actually attaining a Windows-like
market share.


So, let’s concede the point, just for the sake of argument:
*OK, fine, if the Mac had the same market share as Windows, the
tables would be turned and there’d be just as many Mac security
exploits as there are Windows exploits today.*


Now what? Given that the Mac is *never* going to attain a monopoly
share of the operating systems market — that merely expanding its
share to, say, 10 percent would be universally hailed as an
almost-too-good-to-be-true success — isn’t it thus only logical to
conclude that the Mac is forever “doomed” to be significantly more
secure than Windows?


While we’re conceding for the sake of argument, let’s address that
other popular canard of Windows apologia — that on the whole,
Windows XP is just as good, if not better, than Mac OS X. *OK, fine.
XP is as good as OS X; Windows Movie Maker is as good as iMovie;
Photoshop Album is better than iPhoto; etc.*


But is it fair to judge Mac-v.-Windows under factory-fresh
conditions? Wouldn’t an accurate comparison be better made a few
months down the road — after a nice sampling of the hundreds of new
Windows viruses discovered *each week* get a chance to find a home
on the Windows box? In the hands of a typical user, a six-month-old
Mac is almost certainly in similar working condition as when it left
the store; a six-month-old Windows PC, on the other hand, is likely
to be infested with multiple instances of crapware. And if it’s not,
it’s likely because the poor sap who bought it just got done
reinstalling from scratch.


You can argue about *why* this is so, but you don’t need to. You
can’t argue with the facts. Anti-virus software vendor [Sophos
reported yesterday that it found 959 new viruses](http://www.informationweek.com/shared/printableArticle.jhtml?articleID=21401332), *last month
alone*. How many of those do you think were for Mac OS X? Any at
all?


Arguing that it’s technically possible that the Mac could suffer
just as many security exploits as Windows is like arguing that a
good neighborhood could suddenly find itself strewn with garbage and
plagued by vandalism and serious crime. Possible, yes, but not
likely. The security disparity between the Mac and Windows isn’t so
much about technical possibilities as it is about what people will
tolerate.


And Mac users don’t tolerate shit.



| **Previous:** | [Security Cannot Be Spun](https://daringfireball.net/2004/05/security_cannot_be_spun) |
| **Next:** | [Security Update](https://daringfireball.net/2004/06/security_update) |


PreviousNext