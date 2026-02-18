---
title: "FireWire Hysteria"
date: 2005-02-24
url: https://daringfireball.net/2005/02/firewire_hysteria
slug: firewire_hysteria
word_count: 1701
---


The big hubbub over yesterday’s revamped iPod line-up is that
FireWire cables are no longer included as a standard part of the
kit; only the USB cable is included by default. That’s not to say
the new iPods don’t support FireWire, however — they do, just like
always — it’s just that the FireWire cable is now a [$19 accessory](http://store.apple.com/1-800-MY-APPLE/WebObjects/AppleStore?productLearnMore=M9127G/A).


This has raised the hackles of some Mac users, for several reasons.
Mostly, however, it is a symbolic slight, in that it indicates that
Apple is no longer interested — or at the very least, not *as*
interested — in making the Mac iPod experience better than the
Windows iPod experience. All current Macs ship with both USB 2.0 and
FireWire ports, but FireWire synching is faster. FireWire is faster
for iPod users with Windows, too, but the simple fact is that on
PCs, USB 2.0 is much more commonplace than FireWire. The iPod
FireWire cable was included mostly for the benefit of Mac users.


But while it’s rankling to some Mac users, it’s not rankling to iPod
users in general, because, let’s face it, most iPod users,
especially new ones, aren’t using Macs. Thus instead of taxing
Windows users for the cost of an included FireWire cable they would
never use, Apple is now taxing Mac users $19 to get a better cable.


The advantages of FireWire over USB 2.0 (for use with iPods) are not
vast; I suspect most people who own Macs with USB 2.0 ports will
simply use the USB cable included with their new iPods. FireWire may
be better, but most people aren’t going to think it’s $19 better.
The advantages of FireWire over USB 1.1, however, *are* vast — and
so the people who are effectively forced to pay for the FireWire
cable are those whose Macs don’t have USB 2.0 ports. This includes
some machines that aren’t yet two years old (including yours truly’s
iBook G3).


But FireWire cables aren’t the only nicety gone from the new iPod
line-up. An AC adapter is no longer included with the iPod Mini,
and, oddly, the iPod Photo kit no longer includes an iPod Photo Dock
or AV cable. Without the Photo Dock and AV cable, an iPod Photo is
pretty much just an iPod with a color screen, rather than an iPod
with extra photo-related capabilities.


Not coincidentally, however, prices have been cut across the board.
The original 4 GB iPod Mini cost $249 and included a FireWire cable
and AC adapter; you can now get a new second generation 4 GB iPod
Mini for $199, a FireWire cable [for $19](http://store.apple.com/1-800-MY-APPLE/WebObjects/AppleStore?productLearnMore=M9127G/A), and an AC adapter
[for $29](http://store.apple.com/1-800-MY-APPLE/WebObjects/AppleStore?productLearnMore=M8636G/C), for a grand total of $247. (Or if you just want
the standalone AC adapter, you can get the USB power adapter and
forego the FireWire cable, saving $19.) This isn’t a bad deal at all
— especially considering the new Minis’ vastly improved battery
life (18 hours vs. 8 hours).


So at least in the case of the iPod Mini, it’s not so much that
prices have been cut, as that the accessories have been made *a la
carte*. Hence my use of the word “symbolic” earlier regarding the
nature of the slight to Mac users with this “no more free FireWire
cables” thing. Those cables never were free — you paid for them as
part of the total price of the iPod kit. And while their cost to
Apple is certainly far less than the $19 they’re charging for them
as standalone accessories, they still cost a couple of bucks. A
couple of bucks here, a couple of bucks there, and with over a
million iPods being sold per month, you’re talking about tens of
millions of dollars on FireWire cables that most iPod users (read:
Windows-using iPod users) weren’t using.


I’m less sympathetic, however, regarding Apple’s decision to the
same with the iPod Photo models; even though the new 60 GB iPod
Photo is $150 cheaper than the last one, it’s clearly still a
premium product. For $449, it wouldn’t hurt to throw the extra cable
in the box. The *a la carte* accessory pricing seems reasonable with
the low-cost iPod Mini; it seems stingy with the high-cost iPod
Photo.


Symbolism aside, this FireWire cable issue is not a big deal. It’s
not a technical change, it’s a marketing/packaging change. Ina
Fried’s report on the issue for CNet News is getting lots of play,
largely due to its sensational headline: “[Apple Takes a Step Away
From FireWire](http://news.com.com/2102-1041_3-5587951.html?tag=st.util.print)”. A more accurate headline would have read,
“Apple No Longer Includes FireWire Cable in iPod Box”.


With apologies to [Sigmund Freud](http://hv.greenspun.com/bboard/q-and-a-fetch-msg.tcl?msg_id=00BGBz), sometimes a cable is just
a cable.


## The iPod Shuffle Is FAT


Far less controversial, but more insidious, are the limitations
imposed on Mac users trying to use iPod Shuffles as portable disks.
Unlike hard-disk-based iPods, which can be formatted as either HFS+
or FAT32 volumes (for Mac and Windows use, respectively), the iPod
Shuffle can *only* be formatted as a FAT32 volume.


Mac OS X can mount FAT32 volumes just fine, but it can’t help the
fact that FAT32 is a crummy disk format. Look no further than this
somewhat euphemistically-titled support document in Apple’s
Knowledgebase: “[iPod shuffle: Certain characters in file names can
affect transferring files to and from the Mac](http://docs.info.apple.com/article.html?artnum=300560)”:


> iPod shuffle is an iPod that is formatted as FAT32, regardless of
> whether you are using it on a Mac or Windows computer. Because of
> this, files that have the following characters in their names are
> not allowed:
> . ” / \ [ ] : ; | = ,
> This also affects any characters you type using the Option or
> Control keys (like a bullet — Option-8).  Note that the period
> before the three character extension (.mp3, .aac, .jpg) is not
> considered as part of the file name in this case. This doesn’t
> affect audio files you copy inside of iTunes.


Compare and contrast with HFS+, where the one and only disallowed
character is the colon, HFS’s native directory separator. (Mac OS
X’s standard Save dialog box also disallows the use of ‘/’ in file
names, but that’s an artificial limitation imposed by Navigation
Services, not a limitation of the HFS+ format itself; the Finder
will happily allow you to use ‘/’ in your file names.)


Remember the days when DOS/Windows file name restrictions were a
target of mockery? E.g. the sarcastic “C:\ONGRTLNS.W95” full-page
newspaper ads Apple ran when Microsoft launched Windows 95. With the
iPod Shuffle, Windows’ limitations are now ours, too.


You can justify this numerous ways. E.g. that the iPod Shuffle is a
music player first, and portable disk drive second, and so the FAT32
disk format is but a secondary annoyance to Mac users. And if the
iPod Shuffle is indeed based partly on controller chips from
SigmaTel — [as speculated](http://www.macobserver.com/article/2004/10/20.14.shtml) at the outset of the pre-release
“Apple is going to release a flash-memory iPod” frenzy — perhaps
those controller chips already supported FAT32, and adding support
for HFS+ would have added time and expense to the Shuffle’s
development that Apple didn’t deem commensurate with the number of
people who’d use it (read: Mac users).


But since when is Apple a company that takes the easy way out?
Perhaps this hasn’t generated any controversy simply because Mac
users have developed file-name-related calluses since the move to
Mac OS X.


Apple’s Knowledgebase article offers this delightful workaround:


> Does this mean you have to rename every file that contains these
> special characters you want to copy to iPod shuffle? Not at all.
> Just follow these steps to create an archive file that acts as an
> envelope for your other files, allowing you to keep your original
> file names intact. If you already tried copying the files
> separately, remove them from iPod shuffle first.
> Mac OS X 10.3 or later
> In the Finder, select the files you want to transfer.
> From the File menu, choose Create Archive.
> Name the archive without using any special characters.
> Copy the archive file to iPod shuffle.


While this would work, where by “work” I mean it would allow one to
use a Shuffle to transport files whose name contains any of the
forbidden characters, it is rather, well, shitty.


A much better, but slightly more complicated workaround would be to
create a read/write HFS+ disk image on the Shuffle, and use the disk
image for file storage. This adds a layer of abstraction — as does
Apple’s suggested solution of using zip archives — but at least
with a disk image you can browse and search for individual files, as
well as open and save them in-place. Plus, using Apple’s Disk
Utility, you can secure a disk image with encryption — a good idea
if you plan on storing files on a gadget that has a non-zero chance
of being lost or stolen.


But none of this is going to help typical Mac users. Encrypted disk
images are for nerds, and most Mac users aren’t regular readers of
Apple’s Knowledgebase.


Even knowing that there exist such things as “disk formats” is
beneath the radar of most Mac users (and Windows users, too, for
that matter). What’s going to happen is that Mac users will simply
try copying files to their Shuffles using the Finder, and when the
Finder complains that “one or more files could not be copied”,
they’re going to be lost as to why.


The “it just works” factor has been one of the hallmarks of the Mac
user experience since day one; using an iPod Shuffle as a disk drive
forces you to be aware of arcane and bizarre file naming
restrictions, and thus is utterly un-Mac-like. I’m not pointing this
out to claim it’s cause for alarm, that the sky is falling, or that
the iPod Shuffle “sucks”. I’m just saying it’s a little sad when
Apple Computer, of all companies, tells us that punctuation such as
‘=’ and ‘;’ are “special characters”.



| **Previous:** | [How to Create an ‘App of the Year’](https://daringfireball.net/2005/02/how_to_create_an_app_of_the_year) |
| **Next:** | [Kill ‘nav-commenters.gif’](https://daringfireball.net/2005/03/nav-commenters) |


PreviousNext