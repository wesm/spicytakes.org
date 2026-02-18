---
title: "If It Ain’t Broke"
date: 2004-04-23
url: https://daringfireball.net/2004/04/if_it_aint_broke
slug: if_it_aint_broke
word_count: 982
---


Around a month after Mac OS X 10.3 shipped, [I charted its adoption
rate among Safari-using Daring Fireball readers](http://daringfireball.net/2003/12/panther_adoption_rate). (This
tracking is possible because the Panther versions of Safari aren’t
available for Jaguar.) The gist is that about half of you upgraded
within the first few days of Panther’s release, and within a month,
somewhere between 75 to 80 percent of you had upgraded.


The stats for the first three weeks of this month put the current
number at just under 90 percent (89.675 percent, for you stat
nerds).


From its debut, Panther has been almost universally lauded as a
significant and worthy improvement over Jaguar. So, who are these
people who have upgraded as of April 2004, but waited several months
before doing so?


Some of these people purchased new Macs. If you were planning on a
new machine, why bother paying for a copy of Panther to upgrade
the machine you were getting ready to replace?


Most of these Panther-come-latelies, however, are just plain
cautious. People with work and deadlines, and for whom a stable and
reliable Mac running an older version of the OS is just fine, thanks
— deadlines don’t get moved just because your OS upgrade went awry.


Exhibit A: Jeffrey Zeldman, who upgraded from Jaguar to Panther
earlier this month. [It did not go well](http://www.zeldman.com/daily/0404d.shtml):


> My journey into Panther killed my Titanium PowerBook in stages. First
> came software failure: Apple applications such as Safari quit on
> launch; the machine could not find the network. Then came kernel
> panics. (This is where the machine reboots into a black and white Unix
> screen, spitting out Matrix-like error messages. To exit, you must type
> the appropriate Unix commands, which implies that you know what they
> are.) Finally, the machine would not boot, period.
> It took three days’ heavy digging to restore the Mac to operability.
> Along the way I discovered a couple of Apple design decisions that make
> sense under normal circumstances but turn problems into disasters when
> things go wrong.


His report detailing the entire experience is exquisitely detailed,
and well worth reading — even if you, just like me and the vast
majority of Panther users, upgraded to Panther without a hitch.


The fact the Panther upgrade worked perfectly for you, and for most
of us, is not proof that Mr. Zeldman must have done something wrong.


Nor is the fact that something went wrong for Mr. Zeldman an
indication that Apple “doesn’t test” their updaters, or that they
have rampant QA problems.


Bugs happen. Some will slip through even the tightest QA tests. It
has always been the case, and always will be, that every upgrade of
your OS ought to be preceded by a full backup.


Adding insult to injury, after he finally got Panther installed and
running, Zeldman allowed Software Update to bump the machine to
10.3.3, and [he ended up unable to print](http://www.zeldman.com/daily/0404g.shtml#print). The problem is that
for upgrades, the Panther installer doesn’t create several new
users, necessary for Panther, but which weren’t needed in previous
versions of Mac OS X. Running Disk Utility’s Repair Permissions
command can then leave you unable to print, because files which are
supposed to belong to these new “users” can’t be assigned to them
because the users don’t actually exist.


I ran into this problem myself shortly after upgrading, and [All OS
X’s Panther Printing Fix](http://www.allosx.com/1067395661/) utility corrected the problem.
Unfortunately for Mr. Zeldman, this utility only restored his
ability to print to a networked printer; [he’s still unable to print
to a USB printer connected to his machine](http://www.zeldman.com/daily/0404h.shtml#print2). (I would have
suggested this solution to Zeldman, but I’d forgotten about my
similar experience until he mentioned it in his aforementioned post
earlier today; I no longer remember trouble-shooting tips, I trust
Google to remember them for me.)


At the end of his first article detailing his Panther saga, Zeldman
writes:


> As a consumer platform, OS X is years ahead of the competition. As a
> platform for computer professionals with a solid Unix background, OS X
> is also years ahead. But I wonder if Apple has lost sight of the
> non-Unix-oriented creative professionals whose loyalty supported the
> company through its hardest times. There are many of us. We admire what
> Apple designs, we remain committed to the platform, and we want the
> company to succeed. But a simple OS upgrade should not fail, should not
> induce panic, and should not waste three days of a user’s life.


It’s also the case that design professionals tend to purchase
Apple’s higher-margin, top-of-the-line hardware. They’re not just
loyal Apple customers, they’re profitable Apple customers.


More to the point, however, is the uncomfortable fact that *many*
print design professionals are still using Mac OS 9 (or even 8.6).
There is a huge “it just works” advantage that Mac OS 9 holds over
OS X, and Zeldman’s recent experience exemplifies it.


OS updates didn’t always go perfectly on the old Mac OS, but when
they went wrong, they very seldom left your Mac unbootable. And
small point updates — going from X.x to X.y — tended not to
mysteriously break your ability to print.


When things went wrong on Mac OS 9, you could suss out the problem
by dragging files into or out of the Extensions folder and
restarting.


When things go wrong on Mac OS X, they often happen at a deeper
level. File permission and ownership problems, for example, are not
something a typical Mac user can deal with. It’s not enough that Mac
OS X doesn’t require any Unix nerdery whatsoever for day-to-day
use — it should *never* require Unix nerdery to recover from
software updates, either.



| **Previous:** | [Crying Wolf](https://daringfireball.net/2004/04/crying_wolf) |
| **Next:** | [Just a Bunch of Links, but They’re Good Links, I Swear](https://daringfireball.net/2004/05/just_links) |


PreviousNext