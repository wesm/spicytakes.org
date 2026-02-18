---
title: "Windows: The New Classic"
date: 2006-04-06
url: https://daringfireball.net/2006/04/windows_the_new_classic
slug: windows_the_new_classic
word_count: 2239
---


“Holy shit!” seemed to be the consensus reaction to [Boot Camp](http://www.apple.com/macosx/bootcamp)’s
debut yesterday; it was [my reaction](http://daringfireball.net/linked/2006/april#wed-05-boot_camp), at least. But like many
seemingly shocking announcements from Apple in recent years, after
just a few hours, it now seems so... *obvious*.


As of just two days ago, though, it certainly didn’t seem like an
obvious move for Apple to officially or semi-officially support
dual-booting between Mac OS X and Windows on Mac hardware. It was
just a few weeks ago that [OnMac.net awarded over US$13,000](http://onmac.net/)
for a completely unofficial not-for-the-faint-of-heart hack to get
Windows XP running on Intel-based Macs. (I’m guessing many people
who pitched money into that prize pot regret it now.) And it brings
me no small amount of glee to point out that coverage of Boot Camp
at [Think Secret](http://thinksecret.com/news/0604bootcamp.html) and [AppleInsider](http://appleinsider.com/article.php?id=1650) only appeared *after*
Apple announced it. Waiting for the press release is certainly one
way to raise the accuracy of their rumor coverage.


If Apple had released Boot Camp a few days earlier on April 1, I
suspect most people would have thought it to be a gag, *à la*
Google’s [2004 April 1 announcement of Gmail](http://www.google.com/press/pressrel/gmail.html) (*“1 GB of email
storage for free? This is a gag, right? Right?”*).


But now that it’s here, Boot Camp does seem like an obvious move for
Apple, no? It’s a low-risk, no-lose proposition for them, and but
the potential upside is huge.


The old equation — decades old — is that most computers ran
Windows (or, if you go back far enough, DOS) and some other
ones, the ones from Apple, ran Mac OS. As of today, the new equation
is that all computers can run Windows, but some, the special ones
from Apple, also run Mac OS X. (Including other PC operating systems
like the various Linux distributions doesn’t really change the
equation.)


The distinction between these two equations may strike you as
subtle, but the difference is potentially momentous. The point is
that it recasts Macs from being “different” to being “special”.
Instead of occupying a separate universe from that of PC hardware,
it’s now a superset of PC hardware. Instead of choosing between a
Windows PC or a Mac — which decision, [as I wrote recently](http://daringfireball.net/2006/03/familiarity_breeds_a_user_base),
for most people is more accurately stated as “choosing between a
familiar Windows PC or an unfamiliar Mac” — you now get to choose
between a computer that can only run Windows or a computer that can
run *both* Windows and Mac OS X.


I.e. anything a regular PC can do a Mac can do, plus a Mac can do
something regular PCs can’t: run Mac OS X properly and legitimately.


This move extinguishes several of the qualms that prevent many
would-be switchers from actually getting off the fence and buying
their first Mac. Namely, the “I’m not comfortable switching to a
computer I’m wholly unfamiliar with” rationale. Boot Camp gives
switchers a comfortable out if they wind up not liking or in any way
regretting their switch to Mac OS X: they can use their Mac as a
bona fide first-class Windows box.


## The Boot Camp Target Market


Boot Camp is not about world domination or a direct frontal assault
on Microsoft’s Windows monopoly.1
No matter how cool Boot Camp is, it’s not even going to make sense
to most people out there, let alone actually get them to buy a Mac.
You try explaining “boot loaders” to your mom.


But Boot Camp is inordinately appealing to the higher end of the
market, the enthusiasts. Your typical civilian (i.e. non-enthusiast)
has no need — or at least *sees* no need — for dual booting. They
use email, they use a web browser, they want something useful to
happen when they plug a digital camera into their USB port.
Whichever OS comes on their computer is good enough for this.


But there are all sorts of uses for Boot Camp for nerds. Any sort of
Windows-only software, for example, is no longer an excuse not to
buy a Mac. Like, say, [games](http://cabel.name/2006/04/boot-camp-first-look-half-life-2-video.html). And for many of these people
(i.e. the enthusiast/nerd/”into computers” market) using Boot Camp
is *free* because they already have Windows XP installation discs
sitting around.


All Apple needs to do to be spectacularly successful with its
computer business in the next few years is to take just a few single
digits of market share away from Windows. Whatever market share
number you peg the Mac at — 2 percent, 5 percent, or anywhere in
between — you must keep in mind that it (that is, the Mac user
base) is not comprised of a random sample of just *any* 2-5 percent
of computer users in general. It’s a very specific self-selecting
segment of the market: people who care about their computers, and
who are willing to pay more for something better.


So even if Apple only has 2 percent of the total market today, it’s
2 percent from the *best part of the market*. And if they add another
percentage point or two or three, that’s going to come from the
juicy part of the market as well. (I’d wager a large sum that
Apple’s share of the profits in the total PC industry are
significantly higher than their share of units sales.)


For people in the market for a new laptop and who are at least
somewhat curious about Mac OS X, what reasons are there now *not* to
buy a MacBook? (Feel free to use your imagination to fast-forward a
few months to a time where Apple has a range of MacBook models
available.) The primary reason (not to buy a MacBook) that comes to
mind is “Well, I can save a few bucks with another brand,” but Apple
doesn’t really want customers like that anyway — people who shop
primarily based on price are generally lousy customers.


I’m reminded of this snippet from [John Siracusa’s lovely essay
marking the fifth anniversary of Mac OS X 10.0](http://arstechnica.com/reviews/os/osx-fiveyears.ars):


> After spending half my life watching smart, talented people ignore
> the Mac for reasons of circumstance or prejudice, it’s incredibly
> gratifying to live in a post-Mac OS X world. When I encounter a
> tech-world luminary or up-and-coming geek today, I just assume
> that he or she uses a Mac. Most of the time, I’m right. Even those
> with a conflicting affiliation (e.g., Linux enthusiasts) often use
> Apple laptops, if not the OS.


That’s the momentum and the market that Boot Camp will help keep
growing.


## Relishing the Comparison


Let’s look at what Apple has done here:

- Updated the firmware for Intel-based Macs, presumably to
emulate BIOS. As Apple says on the Boot Camp product page:

**EFI and BIOS**
- An in-place disk partitioning utility that allows you to create
a FAT-32 or NTFS disk partition on your startup drive *without*
reformatting the entire disk. The utility carves out 10 GB or
more from your existing HFS+ partition (assuming you have enough
free space) and leaves your existing data intact. This sounds
obvious — if you had to wipe your entire startup drive as part
of the partitioning process it’d keep a lot of people from even
trying Boot Camp — but this has proven to be a very difficult
problem. There are other third-party utilities that can do this,
but I’m not aware of any that come free with an OS.
[**Update:** Several readers have complained that this just isn’t
so, that numerous — perhaps even most — Linux distributions now
ship with in-place disk partitioning tools.]
- A new boot chooser that appears when you boot your machine
while holding down the Option key, which boot chooser sports a
nifty OS X-ish visual appearance (as opposed to the decidedly OS
9-ish appearance of the old “which startup folder/disk do you
want to use?” chooser). [**Update:** A couple of readers have
emailed to point out that the new startup boot chooser appearance
has been there all along with the Intel-based Macs, and isn’t new
to Boot Camp or yesterday’s firmware updates. That’s what I get
for not having an Intel-based Mac.]
- An updated Startup Disk system prefs panel that allows you to
select your Windows partition as your default system, as well as
a Windows version of the Startup Disk prefs panel so you can do
the same from Windows.
- A slew of Windows drivers for the hardware in these Macs.
Judging from first-day accounts, AirPort, audio, and
Mac-specific keyboard features like the eject key all “just
work”.


I point all this out to emphasize that despite the fact that the
entirety of Boot Camp, including the new firmware, has been clearly
labeled “beta” and not officially supported, Apple has gone out of
its way to make running Windows XP on Intel-based Macs a nice
experience. They want people to try this.


Right now, it’s a dual-boot situation, which is obviously less than
ideal. It’s not hard to imagine, though, that the version of Boot
Camp Apple is building into the upcoming Mac OS X 10.5 (a.k.a.
Leopard) will be a concurrent virtualization tool — i.e. that
Windows (and perhaps any other PC OS) could be hosted within a
running Mac OS X session, obviating the rather annoying need to
reboot to switch between OSes.


Do I know this? No. But it certainly seems like the obvious
direction for Boot Camp to take, and it’s certainly technically
possible. E.g. earlier today, their hand presumably forced by
Apple’s release of Boot Camp yesterday, [Parallels released a public
beta of their $50 Workstation](http://www.parallels.com/en/products/workstation/mac/) virtualization system for
Intel-based Macs. It’s like Virtual PC except, because there’s no
need to translate between the PowerPC and x86 instruction sets, it
executes the hosted virtual system at native speed. I think it’s a
safe bet that Apple plans to include something like this with Mac OS
X 10.5, for *free*.


And this points to the rather delicious conclusion that Apple is
casting Windows, including Vista, as the new Classic.


Boot Camp portends Apple’s intention to become a Windows-only PC
manufacturer no more than Classic served as a hedge against Apple’s
commitment to Mac OS X — that is, not at all.


The fear that Windows-on-Mac-hardware implies the eventual death or
marginalization of Mac OS X is baseless. Sure, third party
developers *could* start using “Just boot into Windows” as their
answer to questions regarding Mac support, but this is no more
likely to be popular or successful than it was for developers whose
OS X strategy was “Just use Classic”.


This is a move of supreme confidence — Apple relishes the
comparison between Mac OS X and Windows XP, and Microsoft has shown
enough of Vista via its widely-available beta seeds that Apple quite
obviously isn’t afraid of that comparison, either.


Windows is so ubiquitous that the vast majority of Mac users are
already quite familiar with it; I see no chance that Boot Camp is
going to cause any Mac users to realize that they’ve been missing
out on something better. But from the other side, Apple is
confident that most Windows users who give Mac OS X a shot are going
to prefer it — again, much in the same way that most long-time Mac
users preferred Mac OS X to the old Mac OS.


In the same way that Mac users found themselves in a race to go
Classic-free after switching to OS X, and that running apps through
Classic was viewed from the get-go as something to be done while
holding one’s nose, so too will Windows be viewed in the post-Boot
Camp world.


Microsoft can’t act like they care — Apple is doing nothing even
vaguely sketchy or wrong here, and while Apple isn’t paying
Microsoft a dime, anyone using Boot Camp legitimately is doing so by
way of a paid-for Windows license.


But everything about Boot Camp is calibrated to position
Windows-on-Mac as the next Classic-style ghetto — a compatibility
layer that you might need but that you wish you didn’t. Take Apple’s
“Word to the Wise” warning regarding Windows security:


> **Word to the Wise** 
> Windows running on a Mac is like Windows running on a PC. That
> means it’ll be subject to the same attacks that plague the Windows
> world. So be sure to keep it updated with the latest Microsoft
> Windows security fixes.


Even the Boot Camp logo:


reinforces this. It’s a bastardized variant of Microsoft’s Windows
logo, sans color, and with the whitespace between the four panels
forming a hidden “X”, *à la* the [hidden arrow in FedEx’s
logo](http://www.thesneeze.com/mt-archives/000273.php).2


They (Microsoft, that is) are stuck with the fact that in a fair
shoot-out, Mac OS X is better. It looks better, it’s better
designed, it’s more exciting, more intriguing, more satisfying. Cf.
[this joke from an anonymous poster](http://minimsft.blogspot.com/2006/03/vista-2007-fire-leadership-now.html#c114302448628930798) in the comments at
Mini-Microsoft’s weblog (attached to a post where Mini-Microsoft
rails against the current Microsoft leadership regime):


> What’s the difference between OS X and Vista?
> Microsoft employees are excited about OS X...


That joke just keeps getting funnier.


---

1. Was that redundant? ↩︎
2. Credit to Craig Hockenberry at [IconFactory](http://www.iconfactory.com/) for pointing this out to me via email. ↩︎



| **Previous:** | [‘Repair Permissions’ Is Not a Recommended Step When Applying System Updates](https://daringfireball.net/2006/04/repair_permissions) |
| **Next:** | [Several Asinine and/or Risky Ideas Regarding Apple’s Strategy That Boot Camp Does Not Portend](https://daringfireball.net/2006/04/asinine_and_or_risky_ideas) |


PreviousNext