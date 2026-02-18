---
title: "Tim Bray on iCal"
date: 2006-05-12
url: https://daringfireball.net/2006/05/tim_bray_on_ical
slug: tim_bray_on_ical
word_count: 1515
---


Tim Bray encountered [a nasty file corruption bug in iCal](http://www.tbray.org/ongoing/When/200x/2006/05/11/iCal-still-sucks):


> I’ve been using iCal for a couple of years now; never really loved
> it but it’s OK. Today for some reason my PowerBook locked up (no
> big gripe, this hardly ever happens) and when it came back up,
> iCal showed a little red splodge next to my calendar which when
> clicked said “iCal was unable to load the calendar. The file might
> be corrupted or temporarly (*sic*) unreadable. you can try again
> later or reset this calendar. Resetting the calendar will remove
> all calendar content.” *There are not words to express how much
> this sucks.* A programmer working for me who left this kind of hole
> in a personal-productivity application would be subject to
> dismissal.


This does suck, and Bray’s basic criticism as to why this shouldn’t
be possible is sound. But I don’t think he has it quite right.


Bray writes:


> Of course, in a sane world iCal would store a calendar named “Tim”
> in *Library/Calendars/Tim*, but they’re off in
> *Library/Application Support/iCal/Sources/<long-hexadecimal-string>*.
> And mine contained eight hundred thousand null bytes.


I’m not sure this is worth criticizing. The *Application
Support/iCal* sub-folder in the Library folder seems like as good a
place as any to store your calendar data. I certainly wouldn’t want
to see more applications claiming top-level-of-the-Library-folder
real estate.


The “long hex string” that identifies the calendar data is a [UUID](http://en.wikipedia.org/wiki/UUID)
— a universally unique identifier. For example:
“A562936C-62C8-468A-8F2A-E565823CB16B”. No two UUIDs should ever be
the same, not just on your system, but across *all* systems.1 They’re useful as file names in this
case because they never have to change — you can create a calendar
called “John’s Cal”, then a few weeks later change the name of that
calendar to “Gruber’s Stuff”, and UUID will remain the same.


That means (a) third party software that reads your iCal data (e.g.
Objectpark’s nifty MenuCalendarClock) still knows which calendar is
which, even if you change the display name of the calendar in iCal,
and (b) iCal doesn’t have to worry about file name collisions if you
subscribe to two different calendars with the same title.


It is, admittedly, a bit cryptic-looking, and I’m generally a fan of
nice, human-readable non-crufty file names. But these iCal data file
folders aren’t meant to be end-user-serviceable files; you’re meant
to interact with them solely through iCal, not the Finder.


Bray’s real beef is with the 800,000 null bytes in the calendar’s
ICS file. (ICS is a plain-text mostly-human-readable format; cf. this
[Apple Developer Connection article on iCalendar Files](http://developer.apple.com/internet/appleapplications/icalendarfiles.html).) It’s
unclear to me, though, whether the corrupted ICS file consisted of
nothing but the 800,000 null bytes, or whether those spurious null
bytes were stuck inside a file that still contained his calendar
data, too.


[**Update:** Tim Bray emailed me to clarify — the entire file
consisting of nothing but the null bytes. I.e. it was a file that
consisted of nothing but 800 KB of zeroes.]


Next, Bray gets prescriptive, under the section header “Dear Apple”:


> Here’s how you update a file containing valuable data safely:
> First, you write out the new version without touching the
> old version, and carefully check that it worked.
> Then, you move the old version aside, giving it name like
> Tim.ics.backup, and carefully check that the move worked.
> Then, you move the new version in to the location of the old
> version and carefully check that this worked.
> Then, you delete the backup. Even better, don’t; keep a few
> generations around.
> I don’t want to be rude. But a personal-productivity application
> that updates crucial high-value information files in place is
> Broken As Designed, and evidence of an extreme lack of
> professionalism.


This is reasonable advice — however, I’m pretty sure iCal *doesn’t*
update its ICS data files in-place. Inside the *Application
Support/iCal/Sources/*” folder, each calendar is stored as a bundle,
which is really just a folder (the names of which folders are the
aforementioned cryptic-looking UUIDs) with a “.calendar” extension.
Inside each calendar bundle are three files:

- corestorage.ics
- Index
- Info.plist


The *Info.plist* file is a simple property list containing the UUID
and display name of the calendar. I’m not sure what *Index* is for.
And *corestorage.ics* is the ICS-format file where your actual
calendar data is stored. This, presumably, is the file that
contained all those stray nulls on Bray’s system.


In the HFS+ file system on Mac OS X, each file has two dates
associated with it: a modification date, and a creation date. (On
some other file systems, there’s just one date associated with each
file: the modification date.) My corestorage.ics files all have a
creation date of today, which seems to hint that iCal *does* do
something along the lines of what Bray proposes when it writes your
data to disk: that is, write the data to a new file, then replace
the old file with the new one. In most applications, when you save,
the app just writes the data into the existing file.


To investigate further, I installed [Amit Singh’s `hfsdebug` tool](http://www.kernelthread.com/software/hfsdebug/)
— a command-line tool that allows you to inspect low-level HFS
attributes.


Every file on an HFS+ volume is assigned a Catalog Node ID. This ID
uniquely identifies that file on the volume, and it’s how aliases
continue to work even if you rename or move a file. `hfsdebug`
allows you to inspect these Catalog Node IDs. [**Update:** You can
also use the ‘-i’ switch for the `ls` command to get the inode for
any file; on HFS+ volumes this is almost always the same as the
Catalog Node ID.]


If, say, I open a text file in BBEdit, make a change, then save, the
Catalog Node ID remains the same, because BBEdit writes the updated
file contents back to the same file. This is true for most
applications in which you save document files via File → Save.2 [**Update:** I did not mean to imply,
in any way, that Mac apps that preserve file IDs when saving are
writing data in an unsafe way. Apple recommends several techniques
for updating files safely while preserving file IDs; e.g. the Carbon
[FSExchangeObjects](http://developer.apple.com/cgi-bin/search.pl?q=FSExchangeObjects) API. It’s a lot more involved than just opening
the file for writing and overwriting the old content.]


However, if I make a change to an iCal calendar, then quit iCal,
then re-inspect the corestorage.ics files with `hfsdebug`, I can see
that the Catalog Node IDs change. Point being: I’m pretty sure iCal
*does not* write to its data files in-place; it writes to a new
file, then replaces the old file with the new one.


Bray’s fourth point is the crux of the matter, however. There’s no
reason iCal couldn’t keep the previous file around. That way, if
anything happens that corrupts the current file, iCal could offer
the user the option of going back to the previous revision. Losing
an entire calendar is potentially devastating; losing the changes
from your current iCal session would be, in most cases, merely
annoying.


Disk space is cheap, calendar files are small, and calendar data is,
in many cases, very important. iCal ought to be as conservative as
possible with this data, and the most conservative thing it could do
is keep at least one backup revision stored for disaster recovery.3


I don’t think the data corruption itself, in this case, is a reason
to criticize iCal — given that it happened after Bray’s system
“locked up”, it’s quite possible that the corruption was caused by a
low-level problem far outside iCal’s control.


The problem is its meager data corruption recovery capabilities.
Wise users take this into their own hands, and back up all of their
important data on their own, every day. But most people don’t back
up regularly, nor would most Mac users even know where to look for
the calendar data files, which means most users in Bray’s situation
probably wind up losing their calendar data.


And Bray’s exactly right about that: it sucks.


---

1. You can play with this using the `uuidgen` command-line tool that ships with Mac OS X. Every time you type `uuidgen` at a shell prompt, you’ll get a new UUID. (BBEdit has a #uuid# glossary token that exposes the same system API.) ↩︎
2. TextMate has a “Perform atomic saves” preference setting — off by default — that writes to a new file each time you save. I have no idea why this would be desirable. ↩︎
3. On the other hand, an automatically backed-up data storage system might prove unpleasant in certain situations. Like, say, if you really want to delete a certain event from your calendar, you might not be happy to find out that the event data still resides on your system in the backed-up calendar data files that you didn’t even know existed. ↩︎



| **Previous:** | [Jackass of the Week: Rob Glaser](https://daringfireball.net/2006/05/rob_glaser_jackass) |
| **Next:** | [The Last Pixel](https://daringfireball.net/2006/05/the_last_pixel) |


PreviousNext