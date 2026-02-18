---
title: "An Important Public Service Announcement Regarding Marker Felt on the iPhone"
date: 2007-09-19
url: https://daringfireball.net/2007/09/marker_felt_iphone
slug: marker_felt_iphone
word_count: 475
---


Let’s say you’re like me, at least insofar as (a) you have an iPhone; (b) you [despise](http://daringfireball.net/2007/06/iphone_first_impressions) the Marker Felt font used by the iPhone’s Notes app; and (c) you’ve installed the BSD subsystem, which allows you to access the iPhone’s underlying file system via SSH or SFTP.


If that’s the case, I have a suggestion for how to use (c) to solve problem (b).


If you delete these four files:


*/System/Library/Fonts/MarkerFeltThin.ttf*


and then restart your iPhone, you’ll be treated to a Notes app that looks like this:


I.e. Marker Felt is gone, and Notes substitutes Arial in its stead. I’m fairly certain that Notes’s text view is really a customized WebKit view — in fact, I believe that to be the case for *all* text editing views on mobile OS X — and so rather than crashing when the requested font is not available, it simply handles the problem by substituting another font.


It’d be nice if it substituted [Helvetica rather than Arial](http://daringfireball.net/2007/07/iphone_fonts), and perhaps that’s what would happen if one were to delete all traces of the Arial font, too. But I don’t know, because I haven’t tried it, because the iPhone’s arialuni.ttf font is 22.2 MB (megabytes!), and, given its name, I suspect it contains many Unicode glyphs not present in the OS’s other installed fonts.


Also, if you’re like me, you wouldn’t consider trying this unless you’ve backed up everything on your iPhone, are quite comfortable at the command line, and are unafraid of screwing the system up such that you need to restore the iPhone OS via iTunes.


[**Update, 27 April 2009**: And, to be clear, the above instructions work only against iPhone OS 1.x; they will not work on iPhone OS 2 or later.]


---


**Update:** Dozens of readers suggested that I try making copies of the Helvetica font files and renaming them to “MarkerFeltThin.ttf” and “MarkerFeltWide.ttf”. Two even claimed to have tried this, and that it worked. Alas, in my testing it, does not — and I suspect the readers who claim it does work are simply [confusing Arial and Helvetica](https://www.marksimonson.com/notebook/view/how-to-spot-arial/). Font names are embedded within the font files themselves, not just in the file names of the font files. For example, take any font on your Mac, make a copy of it, give it a random new file name, and then open it in Font Book: Font Book still knows the correct name of the font.


If anyone has really gotten this to work, and they’re certain they’re seeing Helvetica, not Arial, in Marker Felt’s place, please do let me know.



| **Previous:** | [Notes and Observations Regarding Apple’s Announcements From ‘The Beat Goes On’ Special Event, Which, Inexplicably, I Didn’t Bother to Publish Two Weeks Ago When They Were Relevant](https://daringfireball.net/2007/09/beat_goes_on) |
| **Next:** | [Actually, Not Much Better at All This Late Than Never](https://daringfireball.net/2007/09/this_late_than_never) |


PreviousNext