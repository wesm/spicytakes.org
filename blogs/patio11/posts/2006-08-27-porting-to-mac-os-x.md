---
title: "Porting to Mac OS X"
date: 2006-08-27
url: https://www.kalzumeus.com/2006/08/28/porting-to-mac-os-x/
slug: porting-to-mac-os-x
word_count: 616
---


Roughly a month and a half after I first, foolishly, promised to have an OS X version of Bingo Card Creator, I’m actually close to releasing one.  Two major factors propelled me towards this:


I have one extremely dedicated customer who absolutely *had to have* Bingo Card Creator to teach her son reading.  She asked me whether I would have the Mac version done soon and I told her “Well, I certainly hope so”.  And then she went ahead and bought it, sight unseen.  I tried to refund her money because I can’t take money for a product which doesn’t officially exist yet but she would have none of it, so I quickly cobbled together a distribution which would work on a Mac (which basically meant zipping up my install directory and including instructions on how to double-click a JAR file) and rushed it out to her.  Apparently it worked pretty well, aside from a few niggles (not being associated with the file types it creates — the Windows version isn’t, either, as thats been somewhat low on the totem pole), and she sends me updates on how her son is loving reading and math nowadays.


So, given that I’m about to release v1.04, I thought it was as good a time as any to officially roll out the Mac version.  This is problematic because I wanted Bingo Card Creator to function as a native program does (i.e. no “find the coffee cup icon, then double click!” business).  I could accomplish that in about an hour of research and tinkering with the Mac Java SDK but, whoops, no Mac to actually use.  So I decided to outsource.


Enter RentACoder.  I offered the project up at $25 to port Bingo Card Creator (where “port” means “spend five minutes creating a native wrapper”).  It got accepted by somebody in Western Europe (I was sure it was going to be Eastern Europe or India at that price, as even if it is 10 minutes of work its not enough money to wake a programmer up in the West), and he’s busily working on it now.  He even managed to figure out how to do it such that I can do the update from v1.04 to 1.05, etc, on a Windows PC, which is great because it saves me money having to request the same service again (and will earn him a bonus).


Is there a market for Bingo Card Creator on the Mac?  Well, even if there wasn’t, I’ve got one customer who bought it already and so I’m rather committed. :)  Roughly 2% of my site’s visitors are using Macs, and every once in a (long) while I get a Mac specific search string.  I know a good portion of teachers and parents use Macs, although I suspect their share in that market is falling over time, so we’ll see if it generates any significant amount of sales.


Side note: Number of lines of codes changed for the Mac version?  Erm, **zero**.  I like being a Java Success Story (TM).  I will need to change my download page, though — probably use Javascript to detect whether its a Mac or PC and then redirect to the distribution as appropriate.


Version 1.04 is otherwise humming along.  I’ve got roughly 3 of my 5 slated features completed, and added 3 word lists (US presidents, states, and state capitals).  If anybody has suggestions for more word lists which aren’t math related (thats features 4 and 5), feel free to post them in the comments or drop me a line.  I’m thinking of including about 10 new ones concentrated outside of math/reading since my program should have those two fairly well covered.
