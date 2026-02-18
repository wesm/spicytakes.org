---
title: "Bombs Away"
date: 2005-06-08
url: https://daringfireball.net/2005/06/bombs_away
slug: bombs_away
word_count: 2042
---


There were two major reasons why I didn’t think Apple would move the
Mac to x86 Intel processors:

1. To maintain compatibility with existing Mac software, they’d
need a way to run existing PowerPC Mac software on Intel-based
Macs at a reasonable speed, and I didn’t think that was possible.
2. They couldn’t just start selling x86-based Macs out of the
blue.
They’d have to pre-announce them to give developers time
to build
native x86 Mac software. But once they pre-announced
Intel-based
Macs, sales of existing PowerPC Macs would likely
tank.


On Sunday morning, [I wrote](http://daringfireball.net/2005/06/see_you_intel):


> The only way this makes any sense is that there’s something else.
> Something big. Not that CNet and the Journal have the story wrong,
> but that they only have part of the story — and the part they don’t
> have is what’s going to knock our socks off.


My two guesses as to what the “something else” could be were (a) that
Intel would be making PowerPC chips for Apple; or (b) that Apple had
found a way to emulate PowerPC-compiled software at acceptable speed on
Intel processors.


I placed my bet on (a), and, obviously, I lost. The answer was (b).
But I was right that one or the other had to be the case.


I bet on
(a) — Intel-produced PowerPC chips — because I thought it
would
solve both of the above problems. The correct answer, (b), only
solves
the first problem. My guess is that it was simply out of the
question,
completely unrealistic, to expect Intel to produce PowerPC
chips; I’m
guessing for anyone genuinely familiar with the
semi-conductor
industry, it was as ludicrous as a proposal for
Coca-Cola to start
producing Pepsi.


Rosetta — the technology that allows existing PowerPC software to
“just work” on Intel-based Macs — is the missing link that makes this
transition possible. “Emulator” is perhaps not quite an apt
description; Apple seems to prefer the term “translator”. The specific
description I’ve heard is that it is “dynamic binary software
translation”.
I’m curious to know more about how it works, but the
only important
questions are whether — as it was described in a slide
during the keynote
— it’s “Fast (enough)”, and how many important
apps run under it.
We should find out soon enough, when benchmarks
start leaking from seeded developers. (Their NDA forbids publishing
benchmarks based on the developer transition kit hardware, but come
on, you know they’re going to leak anonymously.)


Here’s the overview of how Rosetta works from Apple’s “[Universal Binary
Programming Guidelines](http://developer.apple.com/documentation/MacOSX/Conceptual/universal_binary/universal_binary.pdf)” documentation:


> When an application launches on a Macintosh using an Intel
> microprocessor, the kernel detects whether the application has a
> native binary. If the binary is not native, the kernel launches
> the binary using Rosetta. If the application is one of those that
> can be translated, it launches and runs, although not as fast as
> it would if run as a native binary. Behind the scenes, Rosetta
> translates and executes the PowerPC binary code.
> Rosetta runs in the same thread of control as the application.
> When Rosetta starts an application, it translates a block of
> application code and executes that block. As Rosetta encounters a
> call to a routine that it has not yet translated, it translates
> the needed routine and continues the execution. The result is a
> smooth and continual transitioning between translation and
> execution. In essence, Rosetta and your application work together
> in a kind of symbiotic relationship.
> Rosetta optimizes translated code to deliver the best possible
> performance on the nonnative architecture. It uses a large
> translation buffer, and it caches code for reuse. Code that gets
> reused repeatedly in your application benefits the most because it
> needs to be translated only once. The system uses the cached
> translation, which is faster than translating the code again.


Rosetta is not just a side note or afterthought; it is an essential
component in the transition strategy. It is not going to be marketed
with trumpets and banners. Rosetta’s role is that of the unsung hero.


There’s nothing glamorous about it, because in an ideal world, on the
day Apple begins shipping Intel-based Macs, all Mac OS X software will
have been updated to run natively on both architectures. But the world
is not ideal, and that is not going to happen. A year from now, at
WWDC 2006, most Mac OS X applications will be ready to run natively,
but not all. (And I can hear it now: those developers who haven’t yet
shipped universal binaries will be labeled “laggards” by Steve Jobs
during the keynote.)


Don’t forget also, however, that even those apps that are updated will
in many cases be available only as paid upgrades. Will there be
universal binaries of the Adobe and Microsoft suites? Yes, definitely.
Will they be free updates to the current versions? I doubt it.


If you’re holding on to any not-latest-and-greatest software, apps
that you perhaps only use occasionally — or something you no longer
actively use, but which you keep around for opening old files —
you’re going to want those copies of your software to work on an
Intel-based Mac.


Unlike the Classic environment — which runs apps in a visual ghetto
— most users may not even notice that a few of their apps are running
under Rosetta. (Assuming, again, that Rosetta’s performance is
adequate.)


Apple won’t trumpet Rosetta because they want to trumpet native apps,
and for good reason: apps recompiled for Intel Macs will be faster.
It’s similar in many ways to the 68K emulation that Apple delivered in
the transition a decade ago: everyone wants native apps for the new
architecture, but everyone is glad they can still execute their
existing apps when necessary.


Judging from the preliminary documentation, however, Rosetta is far
less comprehensive than the 68K emulator. The 68K emulator could
pretty much emulate *any* software — apps, drivers, control panels.
Rosetta is limited only to applications, and only certain ones at
that.


There’s a wee bit of uninformed hysteria regarding the fact that
Rosetta effectively emulates only a G3 processor; the Rosetta
documentation states it won’t run “code written specifically for
AltiVec” or “applications that require a G4 or G5 processor”.


But in most cases, apps that are capable of taking advantage of
AltiVec, fall back to non-AltiVec code branches when running on G3
processors. Exhibit A: Photoshop; if you have a machine with AltiVec,
it uses it, if you don’t it continues to work just fine.


One potential hiccup is that Rosetta is an all-or-nothing affair for each application. Again quoting from the Rosetta documentation:


> Rosetta must run the entire process when it translates. This has
> implications for applications that use third-party plug-ins or any
> other component that must be loaded at the time your application
> launches. All parts (application, plug-ins, or other components needed
> at launch time) must run either non-natively or natively. For example,
> if your application has both an x86 binary and a PowerPC binary, but
> it uses a plug-in that has only a PowerPC binary, then your
> application needs to run non-natively on a Macintosh using an Intel
> microprocessor in order to use the non-native plug in.


## The Osborne Effect


So, the first reason I didn’t think this would happen was an issue of
*could* — I didn’t think Apple could execute existing PowerPC code on
x86 machines with reasonable performance. And I’m happy to say it
looks like they’ve proved me wrong.


The second reason was an issue of *would* — I didn’t think Apple
would be willing to pre-announce a dramatic shift like this, knowing
that it would immediately detract from sales of existing PowerPC-based
Mac hardware.


And I was wrong on that point as well. Apple is marching into this
transition chin-first, and they’re simply going to take their lumps.


The question is not whether sales are going to be hurt; the question
is how badly. Especially as we get closer to the release of
Intel-based Macs next year, sales are going to drop. I’ve already
heard from numerous people claiming they’re delaying planned hardware
upgrades until the new Intel-based machines arrive. It doesn’t matter
if such reactions are irrational or emotional or uninformed — what
matters is that there exists X number of people who would have
purchased new Mac hardware in the coming months, but who instead are
now planning to wait for next year’s Intel-based Macs.


Apple’s attitude is clear: we’ll take a couple of quarters of weak
sales now, and make up for it next year when the new systems ship.
With growing iPod revenue, it’s entirely possible that Mac sales could
take a complete nosedive for the remainder of 2005 and Apple could
remain profitable. (It’s also possible that we will see some
outstanding price cuts on existing product lines in the coming
months.)


This transition period is going to be hard on Apple, not hard on Mac
users. If you’ve just purchased a machine recently, or need to buy one
soon, you’re no worse off than you would have been if Apple had
remained committed to producing new PowerPC hardware — today’s
machines would have been obsoleted by even-better machines next year
no matter what processors they contained. And no one is abandoning
PowerPC software development. I see no reason to expect Intel-only Mac
software in the near future. Universal Binaries take full advantage of
*both* Intel and PowerPC Macs. That’s worth repeating: Universal
Binaries take full advantage of *both* Intel and PowerPC Macs.


The “[Osborne Effect](http://en.wikipedia.org/wiki/Osborne_Computer_Corporation)” is named after the Osborne Computer
Corporation, who had a successful personal computer in the early 1980s
called the Osborne 1. Founder Adam Osborne began hyping their
next-generation machine before it was built, and his hype was so
effective that customers stopped buying Osborne 1s in anticipation.
They went bankrupt and never finished the project.


Nothing so spectacular is going to happen here. Even in the worst-case
scenario for Mac sales in the next 12 months, Apple is in no risk of
going bankrupt.


## Why Switch?


This announcement has caught both Apple’s customers and the rest of
the industry by surprise. Especially given the fact that sales of
PowerPC-based Mac hardware have never been stronger than they are now.
Apple’s 43 percent increase in quarterly sales from a year ago is
simply outstanding.


As trite as it sounds, I’m inclined to believe Jobs’s explanation
during the keynote, that Apple believes it can make better computers
down the road with Intel processors, and that the difference is enough
to justify this painful transition.


Maybe the PowerPC roadmap looks good, but the Intel roadmap looks
better. Or maybe they see the PowerPC roadmap as downright bleak —
e.g., say, no G5 PowerBooks in the foreseeable future, even if Apple
wanted to stick with the PowerPC.


The thinking seems to be: better to act now, from a position of
strength, and absorb the costs of the transition while the company is
doing well, rather than wait a few years and risk being forced to act
from a position of weakness or desperation.


“I stood up here two years ago in front of you, and I promised you
this,” Jobs said during the keynote, in front of a slide picturing a
3.0 GHz PowerMac G5. “And we haven’t been able to deliver that to you
yet.” He went on to say that they’d like to be offering G5 PowerBooks,
but can’t.


I’ve seen some interpret this as petulance or spite — that this
switch is just Jobs picking up his ball and leaving for another
playground because he feels IBM has embarrassed him. That
interpretation is foolish. I really think Jobs was just being honest,
or at least as honest as he could be in a public statement.


I think it boiled to a choice between two difficult options: either
initiate a painful and expensive transition to Intel processors, or
stick with PowerPC and fall behind.



| **Previous:** | [Classic Not Supported on Intel-Based Macs](https://daringfireball.net/2005/06/classic_not_supported) |
| **Next:** | [Together We Can Rule the Galaxy](https://daringfireball.net/2005/06/rule_the_galaxy) |


PreviousNext