---
title: "Cringely’s Machinations"
date: 2006-04-22
url: https://daringfireball.net/2006/04/cringelys_machinations
slug: cringelys_machinations
word_count: 1151
---


Continuing on a theme from his [previous](http://www.pbs.org/cringely/pulpit/pulpit20060406.html) [two](http://www.pbs.org/cringely/pulpit/pulpit20060413.html) columns,
Robert X. Cringely is [still predicting that Apple will replace the
Mach kernel](http://www.pbs.org/cringely/pulpit/pulpit20060420.html) in Mac OS X 10.5 because it’s slower than the
kernels in Linux and FreeBSD. Mac OS X *is* slower than other
leading Unix-style OS’s [for server-based tasks](http://www.anandtech.com/mac/showdoc.aspx?i=2436), and I believe
the Mach kernel is the main reason for this, but it’s not that much
slower for graphical-user-interface-based tasks, and that’s really
what matters most for Mac users.


It isn’t ludicrous to speculate that 10.5 (or 10.6, or some
subsequent update even further out in the future) would feature a
new kernel — Mach is definitely not one of the best parts of Mac OS
X, and the kernel is so deeply under-the-hood that most users would
never notice. But I don’t think it’s likely. What’s likely is that
Apple will continue improving Mach’s performance incrementally, just
how they’ve been doing from 10.0 through 10.4.


(Also, just forget about Cringely’s explanation about “integer
calculations” being the cause of the performance difference. That’s
not it at all, and the real reasons are densely technical. Trust me
that it has nothing to do with “integer calculations”, which is a
claim that doesn’t even really make sense. Check out this snippet of
a thread from the Linux kernel development mailing list [in which
Linus Torvalds writes](http://kerneltrap.org/node/6506), “I claim that Mach people (and
apparently FreeBSD) are incompetent idiots,” if you want a taste for
the sort of issues that cause Mach to lag performance-wise.
**Update:** I point to this not because I think Torvalds is the
final word on kernel design, but simply to show that serious
arguments regarding the merits of Mach compared to Linux are deeply
technical and in many ways beyond the ken of laymen, yours truly
most definitely included.)


Anyway, what caught my attention is Cringely’s further speculation
that this new kernel will be for Intel-based Macs only:


> Speeding-up performance is great, but normally a system vendor
> won’t want to do that for older hardware, which might encourage
> some users to keep their old box and just add a new OS.  But in
> this case, Apple HAS NO installed base of Intel Macs to worry
> about having to compete with, so speeding up the OS becomes a
> no-brainer, especially if it simultaneously encourages PowerPC
> owners to upgrade so they can share in the fun.
> For this reason alone, I’m guessing that the new OS X Kernel won’t
> be backward compatible to Power Macs.  But this is just a guess.


That wouldn’t make any sense at all. If 10.5 has a new kernel, and
the new kernel doesn’t run on Power Macs, then it would mean that
*Mac OS X 10.5 wouldn’t run on Power Macs*. There is just no way
that Apple is going to ship PowerPC and Intel versions of Mac OS X
with two entirely different kernel architectures. And there’s just
no way that they’re not going to support PowerPC Macs fully in 10.5
— there’s just too much upgrade revenue to be made.
1


Plus, Apple has been increasing system performance on older hardware
with each successive release of Mac OS X — 10.1 was way faster than
10.0; 10.2 was noticeably faster than 10.1, etc. If Apple can make
10.5 noticeably faster than 10.4 on PowerPC hardware, they won’t
hesitate to do it. Because whatever hypothetical kernel improvements
might make 10.5 faster on PowerPC hardware, they’d make just as big
a difference on Intel-based Macs, and Intel-based Macs are
inherently faster.


I.e., these first-generation Intel-based Macs are so fast that Apple
doesn’t need to worry about suppressing performance on PowerPC Macs
to spur people to upgrade to new hardware. The Intel-based Macs are
selling themselves.


One more intriguing tidbit from Cringely’s column:


> Now for the interesting part: I believe that Apple will offer
> Windows Vista as an option for those big customers who demand it,
> but I also believe that Apple will offer in OS X 10.5 the ability
> to run native Windows XP applications with no copy of XP installed
> on the machine at all. This will be accomplished not by using
> compatibility middleware like Wine, but rather by Apple
> implementing the Windows API directly in OS X 10.5.
> […]
> I’m told Apple has long had this running in the Cupertino lab
> — Intel Macs running OS X while mixing Apple and XP
> applications. This is not a guess or a rumor, this something
> that has been demonstrated and observed by people who have
> since reported to me.


This strikes me as wildly ambitious — it’d be a fantastic
achievement, technically. Cringely cites Apple’s and Microsoft’s
1997 five-year patent cross-licensing agreement for why this might
be possible: Windows XP shipped in 2001, while the agreement was
still in effect. But patent cross-licensing is a far cry from
source-code cross-licensing.


Perhaps the hardest part about building a new implementation of an
existing standard such as the Windows application APIs is that you
not only have to achieve feature compatibility, you also have to
achieve *bug* compatibility — a Windows app running on Mac OS X
would need to behave exactly as it does on Windows. That also means
implementing not just the documented APIs but also the undocumented
ones, and the fact that they’re undocumented makes them rather hard
to implement.


The ongoing Vista fiasco indicates that Windows is so large and so
complicated that even Microsoft is having trouble producing a new
version of it.


Running Windows itself in a compatibility layer — *à la* the way
the Classic environment runs Mac OS 9 — would be a lot less work on
Apple’s part, and would almost certainly be a lot more compatible
with the zillions of Windows apps out there.


The difference with Cringely’s idea is that with his scheme, *every*
Mac running 10.5 would be able to run Windows software right out of
the box, not just those Macs on which a licensed copy of Windows is
installed. But there’s no reason for every Mac, or even most of
them, to be able to run Windows software.


Licensing fees for Windows aren’t necessarily skin off Apple’s back
— Apple can either continue with how they’re doing it now with Boot
Camp (i.e. “bring your own Windows”) or they can make pre-installed
Windows a build-to-order option at the Apple Store, which would mean
that people who wanted it would have to pay an additional $100 or
so.


---

1. I wouldn’t be surprised at all if 10.5 drops support for G3 processors; the last G3-based Macs to roll off the line are now a couple of years old, and in my experience they struggle running 10.4. ↩︎



| **Previous:** | [Initiative](https://daringfireball.net/2006/04/initiative) |
| **Next:** | [When ‘Smart’ Cut/Copy/Paste Attacks](https://daringfireball.net/2006/04/smart_cut_copy_paste) |


PreviousNext