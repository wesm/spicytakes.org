---
title: "Marking the end of pixel trackers in Basecamp emails"
date: 2019-08-28
url: https://signalvnoise.com/svn3/marking-the-end-of-pixel-trackers-in-basecamp-emails/
slug: marking-the-end-of-pixel-trackers-in-basecamp-emails
word_count: 326
---


When Mike Davidson [blew the lid off the invasive and appealing read receipts](https://mikeindustries.com/blog/archive/2019/06/superhuman-is-spying-on-you) in a new personal email client called Superhuman, it brought about a full discussion of email tracking in general. At Basecamp, this lead to the conclusion that we wanted nothing to do with such tracking.


It wasn’t like we were doing anything as nefarious as those nasty Superhuman trackers, but still, we used the default settings in our mailing list software, which aggregates open rates, and had our own diagnostics tracker, to provide debugging insight for support.


But neither of those two use cases felt compelling enough to justify tracking everyone’s emails all the time. Reading an email shouldn’t leave a long data trail, regardless of whether that trail is used in fairly innocuous ways, like an aggregate open-rate calculation, or in its most devious, like spying on whether a personal email has been seen and from where.


So we killed the diagnostics tracking and turned off the mailing list tracking too. Now the only “tracking” that emails from Basecamp will do is to mark the message you’re seeing in your email as read within the application (and only if you’re a registered user). A feature in service of the recipient, not the sender, not us.


The tech industry has been so used to capturing whatever data it could for so long that it has almost forgotten to ask whether it should. But that question is finally being asked. And the answer is obvious: This gluttonous collection of data must stop.


So we keep taking the steps at Basecamp to examine our use of data, stop collecting it unless its strictly necessary in service of customers, and cut down all the ways we may be sharing it with others (dumping Google Analytics from our marketing pages is next!).


Privacy isn’t just the right thing to do, it’s also better business. Discerning customers are already demanding it, and everyone else will too soon enough.

