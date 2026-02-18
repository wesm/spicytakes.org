---
title: "iPhone Calendar Syncing"
date: 2008-08-01
url: https://daringfireball.net/2008/08/iphone_calendar_syncing
slug: iphone_calendar_syncing
word_count: 1262
---


With the 1.0 version of iPhone OS, calendar syncing between the Calendar app on the phone and iCal on your Mac worked like this:

- Everything went through iTunes.
- iTunes listed each of your iCal calendars, and you could choose which ones to sync to the iPhone.
- You had to choose one calendar as your main one; any events created on the iPhone would go to this calendar.


The biggest downside with this system was the obvious one: that syncing only occurred when you tethered your iPhone to your Mac and synced with iTunes. I, for one, am not a frequent iTunes syncer, so my desktop and iPhone calendars frequently were, well, out of sync.


The other problem with iPhone 1.0 calendar syncing was the lack of support for multiple calendars. Because you couldn’t create events on non-main calendars from the iPhone, it was really more like *syncing* with just one iCal calendar, plus *one-way merging* from as many other calendars as you wanted. Nor was there per-calendar color-coding on the iPhone — all events from all synced iCal calendars were effectively merged into one iPhone calendar.


iPhone OS 2.0, along with iTunes 7.7 and MobileMe, changes all of this. Solving the biggest problem with iPhone 1.0 calendaring — that syncing only happened when physically tethered to your Mac — requires MobileMe; more on that in a moment. The multi-calendar shortcomings, however, were ostensibly addressed, as well.


The iPhone OS 2.0 Calendar app now fully supports multiple calendars. There’s a new root-level screen in the app listing all calendars; you can choose to view events from all calendars (which view corresponds to the only view available in the old iPhone 1.0 Calendar app), or only those from any single calendar. New events created on the iPhone can be assigned to any writable calendar, and each calendar gets it own unique color.


But, inexplicably, the colors assigned to the calendars on your iPhone [do not correspond](http://www.macosxhints.com/article.php?story=20080710143428536) to the colors you’ve chosen for those same calendars in iCal, and there’s no apparent way to change the colors of calendars on the iPhone. So if you’ve got three calendars in iCal, say, Home/Work/Play, which are assigned the colors green/blue/orange, respectively, those same three calendars, when synced to your iPhone, may be assigned the colors red/orange/blue. It seems obvious that the colors should carry over to the iPhone from iCal — but if it’s a bug, it wasn’t fixed in iTunes 7.7.1.


## MobileMe Giveth, MobileMe Taketh Away


MobileMe syncing and iTunes syncing are mutually exclusive. If you turn on MobileMe syncing for calendars on your iPhone (Settings → Mail, Contacts, Calendars → Your MobileMe Account), iTunes no longer offers calendar syncing options when you tether your iPhone. The same goes for contacts.


The fundamentals of using MobileMe for over-the-air iPhone calendar (and contact) syncing have worked nearly flawlessly for me: create an event on my Mac or iPhone, and a few minutes later it appears on the other. (That Mac OS X only syncs iCal events and Address Book contact entries every 15 minutes doesn’t strike me as much of a hindrance.) And, in contrast with using iTunes for calendar syncing, the colors you associate with calendars in iCal are accurately mirrored on the iPhone.


So, using MobileMe solves *both* of my significant complaints regarding calendaring syncing with iPhone OS 1.0: events sync over the air, and it provides full support for multiple calendars. And unlike with iTunes syncing, it correctly syncs calendar colors from iCal.


That’s great. Too bad MobileMe introduces several *new* calendar syncing shortcomings.


The first is that MobileMe syncing is all-or-nothing. If you turn it on, all of your iCal calendars sync to both me.com and your iPhone. With iTunes syncing, you could — and still can — pick and choose which calendars to sync. I took advantage of this by creating a calendar on my Mac called, simply, “Mac Reminders”. I used this calendar for events which have alarms that I only want to appear on my Mac, not on my iPhone. With MobileMe, that’s not possible. Since all your calendars sync to MobileMe, every event you create with an alarm message will appear as an alert on both your Mac and iPhone. A useful feature, gone, and now I’m badgered with reminders popping up in two places at once on my office desk.


The other problem is that you [can’t sync read-only subscription calendars to your iPhone](http://support.apple.com/kb/TS1213). Things like holidays, sports schedules, movie releases — Apple publishes [an entire directory of them](http://www.apple.com/downloads/macosx/calendars/). The same goes for calendars published to the Internet from someone else using iCal. With iTunes syncing, you can include these read-only calendars on your iPhone. With MobileMe syncing, you cannot.


I thought about using the second limitation (subscription calendars not showing up on the iPhone) to work around the first (no way to set up a calendar with reminders that only appear on your Mac). My idea was that I could create a calendar online using, say, [Google Calendar](http://www.google.com/calendar) or [Backpack](http://www.backpackit.com/), subscribe to the ICS feed for that calendar in iCal on my Mac, and, since subscribed-to calendars don’t sync to MobileMe, I could use that calendar for any reminders I only want to see on my Mac. But, alas, I haven’t been able to figure out a way to do this — it doesn’t seem like events in subscribed-to calendars can trigger alarms in iCal. (If I’m wrong, please [let me know](http://daringfireball.net/contact/).)


One obvious solution would be an iCal update that lets you specify on a per-calendar basis which calendars should be synced to MobileMe. I think on-by-default would be fine, but somehow you should be able to create a calendar in iCal that doesn’t sync to MobileMe. But given Apple’s traditional schedule for adding new features of any significance, it seems unlikely that an iCal update like this would appear before Snow Leopard.


This lack of syncing specificity also applies to Address Book contacts. With tethered iTunes syncing, you can choose to sync only specific groups in Address Book. With MobileMe, contact syncing, as with calendars, is all or nothing.


Whither the “digital hub”? Much has been made over the fact that iTunes long ago outgrew its name, but the role it plays is central to the success of both Apple’s digital media and handheld device businesses. No, syncing calendars and contacts and email accounts to an iPhone doesn’t have anything to do with “tunes”. *But that which we call a rose by any other name would smell as sweet.* iTunes serves an essential role, that of the hub — one obvious place to go to manage everything that syncs to your iPod or iPhone.


The me.com MobileMe web site, perhaps, could serve as a hub. It does serve as the middleman for data — events and contacts never sync directly between your iPhone and computer — but as it stands today it offers no control over which calendars and contacts sync where. The MobileMe system preference pane could serve this purpose; right now, the only signficant change in this panel from its previous .Mac incarnation is the logo. Rather than a single checkbox for “Calendars”, it could offer one for each calendar. Or, perhaps the best option of all would be for iTunes to serve as the hub — one central place to manage all syncing, whether through USB or through the air.


But as it stands today, with MobileMe syncing, there is no hub.



| **Previous:** | [Not Yet Squirrelly](https://daringfireball.net/2008/07/not_yet_squirrelly) |
| **Next:** | [iPhone, iCal, and CalDAV](https://daringfireball.net/2008/08/iphone_ical_caldav) |


PreviousNext