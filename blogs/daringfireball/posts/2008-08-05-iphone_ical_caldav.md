---
title: "iPhone, iCal, and CalDAV"
date: 2008-08-05
url: https://daringfireball.net/2008/08/iphone_ical_caldav
slug: iphone_ical_caldav
word_count: 519
---


One of [my chief complaints](http://daringfireball.net/2008/08/iphone_calendar_syncing) about the way iPhone calendar syncing works with MobileMe and iCal is that it’s all-or-nothing — when you turn on MobileMe calendar syncing on your iPhone, all your local iCal calendars appear on your iPhone. I want a way to have some calendars appear only on my Mac, for events and reminders which I don’t want to see on my iPhone — something you can easily do when syncing calendars to your iPhone via iTunes instead of MobileMe.


Because MobileMe doesn’t sync subscription calendars, I tried using Google Calendar to work around this. The idea was that I’d put these “I don’t want the alarm to appear on my iPhone” events in my Google Calendar account, then subscribe to that calendar in iCal using the ICS feed. It didn’t work, because the alarms for the events don’t appear in the ICS feeds that Google Calendar produces.


But it ends up that about a week ago, [Google enabled CalDAV support for Google Calendar](http://www.google.com/support/calendar/bin/answer.py?answer=99357), and it works pretty well with iCal on Mac OS X Leopard. ([CalDAV](http://en.wikipedia.org/wiki/CalDAV) is an industry standard for client-server calendar sharing over WebDAV.) As per Google’s instructions, you connect iCal to Google Calendar using the Account panel in iCal’s preferences. Once you’ve done so, your primary calendar in your Google account appears in a new section in the iCal source list:


In the above screenshot, “Google” is the name I gave the account in iCal’s Accounts panel. “Mac Reminders” is the name of the primary calendar in my Google account.


Unlike with ICS calendar subscriptions, which are read-only, iCal offers full read-write support for CalDAV calendars. You can create, edit, and delete events in Google Calendar entirely through iCal. But, as with ICS subscriptions, CalDAV calendars cannot sync to MobileMe. (They do sync via iTunes, but, as with ICS calendars, read-only.)


This is actually quite odd, because Apple is a leading proponent of the CalDAV standard. [iCal Server](http://www.apple.com/server/macosx/features/ical.html) — the calendaring component in Mac OS X Server — is built around CalDAV. And since Apple itself uses Mac OS X Server (at least in the software engineering division), the company’s enterprise calendars use CalDAV, which means neither Apple’s own calendars nor those of Mac OS X Server customers can sync in both directions to the iPhone. *Awkward.*


So my guess is that this is simply a feature Apple hasn’t gotten to yet, and that full CalDAV support will eventually make it to the iPhone. But in the meantime, you can take advantage of the situation, if, like me, you wish to create calendars in iCal that *don’t* sync with MobileMe.1


---

1. This raises the question of what to do if you use Google Calendar, and *do* want your Google Calendar account to sync with your iPhone. The answer is [BusySync](http://www.busymac.com/), the fantastic $25 shared calendar utility from BusyMac. With BusySync, you can subscribe to your Google Calendar account in a way that makes it appear in iCal as a normal (local) calendar. ↩︎



| **Previous:** | [iPhone Calendar Syncing](https://daringfireball.net/2008/08/iphone_calendar_syncing) |
| **Next:** | [Is the iPhone NDA About Patents?](https://daringfireball.net/2008/08/iphone_nda_patents) |


PreviousNext