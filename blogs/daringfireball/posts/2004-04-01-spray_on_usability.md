---
title: "Ronco Spray-On Usability"
date: 2004-04-01
url: https://daringfireball.net/2004/04/spray_on_usability
slug: spray_on_usability
word_count: 2986
---


This one is funny.


Eric S. Raymond — the renowned Linux/Open Source evangelist/essayist —
couldn’t figure out how to connect to a shared printer. So [he wrote an
essay describing the problem](http://www.catb.org/~esr/writings/cups-horror.html) (the UI for printer configuration
on his Linux system is horrible) and proposing a solution (open source
developers should do a better job with UI design). Raymond wrote:


> The configuration problem is simple. I have a desktop machine named
> ‘snark’. It is connected, via the house Ethernet, to my wife Cathy’s
> machine, which is named ‘minx’. Minx has a LaserJet 6MP attached to it
> via parallel port. Both machines are running Fedora Core 1, and Cathy
> can print locally from minx. I can ssh minx from snark, so the network
> is known good.
> This should be easy, right? *hollow laughter* Famous last words…


(**Side note:** *parallel port*? What year is it in the Raymond
household?)


Raymond’s description and criticism of the usability problems he
encountered trying to achieve this are accurate and apt. The gist of it
is that what seemed like the obvious way to go about the task was in
fact completely wrong, and worse, there was no indication from the
system that he wasn’t on the right track.


This setup alone is sort of funny — **Linux Advocate Struggles to
Configure Printer** — ha-ha. Even funnier considering past statements
from Raymond regarding Linux-vs.-Windows usability; e.g. the foreward for
the book “Everyday Linux”, [wherein he wrote](http://everydaylinux.com/):


> Conventional wisdom has it that Linux is doomed to a niche role on the
> desktop because it’s too difficult for Aunt Tillie to run. But the days
> when Linux was really more complex to administer than a Windows machine
> are long past us. In the last three years the open-source community has
> made enormous strides in simplifying installation and normal
> housekeeping and presenting it through graphical user interfaces — to
> the point where it’s really quite a bit easier over time to maintain a
> Linux box than a Windows machine, whether you’re an expert techie or
> not.


I mean, come on, it’s funny that the guy who wrote that couldn’t connect
to a shared printer.


But it’s when Raymond begins proposing “solutions” to the problem —
where “the problem” is the larger issue of open source software
usability in general, not just the specific case of CUPS printer
configuration — that things get hilarious.


In his [follow-up article](http://www.catb.org/~esr/writings/luxury-part-deux.html), Raymond summarizes his proposal
thusly:


> A few days ago I uttered a rant on user-interface problems in the
> Common Unix Printing System. I used it to develop the idea that the
> most valuable gift you can give your users is the luxury of ignorance
> — software that works so well, and is so discoverable to even novice
> users, that they don’t have to read documentation or spend time and
> mental effort to learn about it.


Sounds good, on the surface. And indeed, most of the follow-up article
is devoted to the congratulatory email Raymond received in response to
part one:


> This rant made it onto all the major open-source news channels, so I
> was expecting a fair amount of feedback (and maybe pushback). But the
> volume of community reaction that thundered into my mailbox far
> surpassed what I had been expecting — and the dominant theme, too, was
> a bit of a surprise. Not the hundreds of iterations of “Tell it,
> brother!”, nor the handful of people who excoriated me as an arrogant
> twerp; those are both normal features of the response when I fire a
> broadside. No, the really interesting part was how many of the letters
> said, in effect, “Gee. And all this time I thought it was just me…”


I agree that this is an interesting response, but not for the reason
Raymond does. What I find interesting about the “I thought it was just
me” response is that it points to the gaping hole in Raymond’s proposal,
but which he doesn’t acknowledge.


Raymond’s recommendations center around the idea that open source
developers need to meet the needs of “Aunt Tillie”, whom Raymond defines
as “the archetypal nontechnical user”. (Hereafter referred to as *A.T.*,
because the name *Aunt Tillie* is so queer that it makes yours truly a
tad queasy.) The idea being that if open source software is usable by
A.T., then it’ll meet the usability needs of everyone else, too.


But the whole A.T. angle is quite disingenuous. It wasn’t A.T. who
couldn’t connect to a shared printer. *It was Raymond himself who
couldn’t figure it out.* Yes, I see the point that if it were so easy
and obvious that A.T. could do it, a nerd like Raymond could do it too.
But this is putting the horse way in front of the carriage. In what
world does the “archetypal nontechnical user” have two computers
connected by Ethernet? When A.T. needs to configure a printer, it’s
going to be connected directly to her computer, not shared over a
network.


By focusing on A.T., Raymond is ignoring the actual depth of the
problem. It’s easy to say, *The open source community needs to do
better, we need to create software A.T. can use.* But they’re so far
away from this right now that even an expert like Eric Raymond can’t
figure out how to use their software.


The “I thought I was the only one” letters that Raymond found so
interesting aren’t coming from the A.T.-set; they’re coming from Linux
geeks who read essays written by Eric Raymond. And they’re frustrated by
open source software’s terrible usability. The problem isn’t just that
dear old A.T. can’t use desktop Linux — the problem is that even Linux
geeks have trouble figuring it out.


Furthermore, the “I thought I was the only one” response raises the
question: what planet are these guys from? Isn’t it common knowledge
that desktop Linux usability tends to suck? How can anyone write an
essay proposing to fix this without mentioning, let alone responding to,
Matthew Thomas’s seminal essay, [“Why Free Software usability tends to
suck”](http://web.archive.org/web/20051125183807/http://mpt.phrasewise.com/discuss/msgReader$173)?


## Easy Rider


Raymond writes as though they’re almost there, but just need, you know,
the finishing touches. The extra yard. The cherry on top. The *pièce de
résistance*. I.e., *We’ve got the hard part done — the under-the-hood
foundation — now we just need a better UI and we’ll be set.*


But this is not a radical new direction for open source desktop
software. What Raymond is proposing, in fact, is *no change at all*.
This idea, that the hard work of development is in building the
underlying foundation, and that the easy part is writing a “GUI
wrapper”, has been the Linux/Unix way all along.


Raymond’s proposal is predicated on the idea that good UI design and
development is easy, that developers simply need to keep dear old A.T.
in mind and the design will fall into place. Raymond writes:


> None of this is rocket science. The problem isn’t that the right things
> are technically difficult to do; CUPS is already supposed to have
> discovery of active shareable queues as a feature. The problem is that
> the CUPS designers’ *attitude* was wrong. They never stepped outside
> their assumptions. They never exerted the mental effort to forget what
> they know and sit down at the system like a dumb user who’s never seen
> it before — and they never watched a dumb user in action!


And again:


> As I said before, the point of this essay is not especially to bash on
> the CUPS guys. They’re no worse than thousands of projects out there,
> and that is the point. We talk about world domination, but we’ll
> neither have it nor deserve it until we learn to do better than this. A
> lot better.
> It’s not like doing better would be difficult, either. None of the
> changes in CUPS behavior or documentation I’ve described would be
> technical challenges; the problem is that these simple things never
> occurred to developers who bring huge amounts of already-acquired
> knowledge to bear every time they look at their user interfaces.


Oh, I see: the problem is that Linux developers are just so fucking
smart that they overlook the problems faced by “dumb users” such as dear
old A.T. But everything will fall into place with just a little attitude
adjustment.


Well, allow me to retort.


UI development *is* the hard part. And it’s not the last step, it’s the
first step. In my estimation, the difference between:

- software that performs function X; and
- software that performs function X, with an intuitive
well-designed user interface


isn’t just a little bit of extra work. It’s not even twice the work.
It’s an entire *order of magnitude* more work. Developing software with
a good UI requires both aptitude and a lot of hard work. Raymond
acknowledges neither.


It’s not something every programmer can learn. *Most* programmers don’t
have any aptitude for UI design whatsoever. It’s an art, and like any
art, it requires innate ability. You can learn to be a better writer.
You can learn to be a better illustrator. But most people can’t write
and can’t draw, and no amount of practice or education is going to make
them good at it. Improved, yes; good, no.


Conversely, some people who are good UI designers aren’t programmers.
But the rock stars are the guys who can do both, and they are few and
far between.


If there’s a glib, nutshell synopsis for why Linux desktop software
tends to suck, it’s this: Raymond and his ilk have no respect for anyone
but themselves.


They have no respect for the fact that UI design is a special talent.


They have no respect for the fact that good UI design requires a
tremendous amount of time and effort.


And, most importantly, they have no respect at all for real users. The
idea that GUI software needs to be designed for “dumb users” — which is
Raymond’s own term, and an indication of what he really means when he
refers to dear old A.T. — is completely wrong.


Great software developers don’t design for morons. They design for
smart, perceptive people — *people just like themselves*. They have
profound respect for their users.


## Show Me the Money


This is not a Mac thing. Well, it is, but what I mean is that it’s not
*just* a Mac thing. There are a lot of developers creating good UIs for
Windows, for the web, and for other platforms. And, yes, there are even
developers creating great UIs for software running on Linux.


But the undeniable truth is this: successful open source software
projects tend to be at the developer-level, not the end-user level.
I.e., successful open source projects have *programming* interfaces, not
*user* interfaces. Apache, Perl, Python, GCC, PHP, the various SQL
databases. The list of fantastic open source developer software is long.


The list of fantastic open source GUI software is short. This is not a
function of chance.


The open source revolution has done nothing to change the fact that the
best-designed, most-intuitive user interfaces are found in closed-source
commercial software.


I’m not saying all commercial software is well-designed, nor that all
free software is poorly-designed — what I’m saying is that software
that does provide a well-designed, intuitive interface tends to be
closed and commercial. The bigger the software, the more likely this is
to be true.


The most obvious explanation is that the open source model does not work
well for producing software with good usability. Everything in Raymond’s
article hints at this truth. (Not to mention MPT’s aforementioned
[essay](http://web.archive.org/web/20051125183807/http://mpt.phrasewise.com/discuss/msgReader$173), which addresses this directly.)


Good user interfaces result from long, hard work, by talented developers
and designers.


The distributed, collaborative nature of open source software works for
developer-level software, but works *against* user-level software.
Imagine a motion picture produced like a large open source project.
Different scenes written and directed by different people, spread across
the world. Editing decisions forged by group consensus on mailing lists.
The result would be unfocused, incoherent, and unenjoyable.


Movies are collaborative art, but require [strong direction](http://kubrickfilms.warnerbros.com/). So it
is with end user software.


One exception is the Mozilla project, which has released two very
well-designed web browsers, Camino and Firefox. But Mozilla’s long
development was in large part fueled by full-time Netscape engineers.
And look at how well that’s worked out for Netscape.


Talented programmers who work long full-time hours crafting software
need to be paid. That means selling software. Remember the old open
source magic formula — that one could make money giving away software
by selling “services and support”? That hasn’t happened — in terms of
producing well-designed end user software — and it’s no wonder why. In
Raymond’s own words, the goal is:


> software that works so well, and is so discoverable to even novice
> users, that they don’t have to read documentation or spend time and
> mental effort to learn about it.


It’s pretty hard to sell “services and support” for software that fits
that bill. The model that actually works is selling the software itself.
This is politically distasteful to open source zealots, but it’s true —
and it explains the poor state of usability in open source software.


Raymond also complains about CUPS’s shoddy and inaccurate documentation,
but that’s just another side of the same glove. Technical documentation
is also hard work, and requires talent to be done well. Writers need
paychecks, too. (Trust me.)


## Mac and Windows vs. Linux


Raymond is quite complimentary to Mac software in these articles — he
holds it up as an example for Linux developers to emulate. But he fails
to acknowledge that most Mac software — such as the System Prefs panel
you use to connect to a shared printer — is closed source, and produced
by full-time professional engineers.


He also fails to acknowledge another uncomfortable truth: Unix nerds who
care about usability are switching to Mac OS X in droves. In fact, [most
of them have already switched](http://diveintomark.org/archives/blinks/2004/03/#b20040329041348). This trend isn’t necessarily a
market share bonanza for Apple — all the “Unix nerds who care about
usability” in the world amount to only a fraction of a percent of the
general population. But it’s a trend that bodes poorly for usable
desktop Linux software. Most of the talented developers still using
desktop Linux are either cheapskates or free-software political zealots.


This isn’t to say desktop Linux isn’t growing in use. It is, and will
continue to. But it’s growing at the bottom end of the market — cheap
$400 computers from Wal-Mart. That’s a market where software usability
is not a key feature.


Raymond’s stance toward Windows, however, is childish. E.g., he writes:


> If the designers were half-smart about UI issues (like, say, Windows
> programers [*sic*]) they’d probe the local network neighborhood and omit the
> impossible entries. If they were really smart (like, say, Mac
> programmers) they’d leave the impossible choices in but gray them out,
> signifying that if your system were configured a bit differently you
> really could print on a Windows machine, assuming you were unfortunate
> enough to own one.


I question how “unfortunate” one would be, at least in this situation,
given that it’s easy to configure a shared printer with Windows XP. In
fact, even dear old A.T. might actually have a chance to make this work,
if she were given the head start Raymond himself had at the beginning of
his adventure (i.e., with the network already set up, and the printer
already connected to and shared from the other PC).


This sort of task-driven interface is Windows’s forte. Those
step-by-step “wizards” are generally irritating for advanced users who
want to do something the wizard doesn’t quite support, but for basic
tasks — like, say, connecting to a shared printer across the room —
they work. And they make these tasks approachable for dear old A.T.


And they’re the result of a lot of work by a lot of well-paid full-time
Microsoft engineers.


It’s common for the Linux hacker set to poke fun at Windows’s
wizard-style configuration tools, but the entire desktop Linux user
interface is a pale imitation of Windows — much, much more of a rip-off
of Windows than Windows ever was of the Mac. But the resemblance is
merely cosmetic; functionally, desktop Linux is nowhere near as usable
as Windows.


---


There’s an old engineering adage: “Fast, good, cheap: pick two.” (Where
“fast” regards development time, not performance.) Desktop Linux
software is cheap (free) and fast (release early, release often), but
it’s not good.


Or, perhaps one could argue that it is cheap, and eventually it’s going
to be good, but it’s getting there very slowly.


Windows and Mac OS, on the other hand, are fast and good. For the sake
of this discussion, it doesn’t matter which is better and which is
improving faster. What matters is that neither is cheap. It’s very
difficult to beat the fast/good/cheap rule.


For example, look at how much Mac OS X has improved in the last three
years alone. Even if desktop Linux is improving — and I do think it is
— it’s improving at a much slower pace than Mac OS X.


It’s easy to ridicule the estimated 2006-or-2007 ship date for Longhorn,
the next major release of Windows. But do you doubt for a moment that
Longhorn will provide more improvements from Windows XP than desktop
Linux will gain during the same period?


More often than not, you get what you pay for.



| **Previous:** | [Marcia, Marcia, Markdown](https://daringfireball.net/2004/03/marcia_marcia_markdown) |
| **Next:** | [Sundry ‘Spray-On’ Clarifications and Corrections](https://daringfireball.net/2004/04/sundry_spray_on) |


PreviousNext