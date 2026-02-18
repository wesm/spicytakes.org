---
title: "Intervals"
date: 2004-01-03
url: https://daringfireball.net/2004/01/intervals
slug: intervals
word_count: 463
---


Slogging through my year-end server logs, I noticed that a handful of IP addresses are asking for Daring Fireball’s RSS feed well over 100 times per day. Checking every 15 minutes — which itself is a bit overzealous in my opinion — would only add up to 96 hits a day. Anything more frequent than that, I consider abuse.


Ends up every one of them is using [Shrook](http://www.fondantfancies.com/shrook/), a $20 news aggregator for Mac OS X. That’s not to say every Shrook user is polling at an abusive clip, but that every one of my subscribers who *is* abusive, is using Shrook. Every one.


So, I think, there must be a bug in Shrook. Ends up, it’s a *feature*. Take a gander at the Checking panel in Shrook’s preferences:


This is, to say the least, a bit annoying. Now it’s true that Shrook isn’t downloading the entire feed each time it checks, as it respects the [HTTP 304 status code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.3.5). That’s the “not modified” status code, which is the web server’s way of telling the client that the requested resource hasn’t changed since the last time the client checked.


Thus, this is not a bandwidth issue. Shrook is only downloading the feed when it has actually changed. The problem is that these Shrook users are behaving like annoying little kids in the back seat of the car, except instead of ceaselessly asking “Are we there yet? Are we there yet?”, they’re asking “Has the feed changed yet? Has the feed changed yet?”


304 or no 304, however, it simply rubs me the wrong way to see people checking for updates this frequently. In NetNewsWire, for example, the most frequent polling interval is 30 minutes. (I have *my* copy of NetNewsWire set to poll once an hour.)


It’s worth noting that by default, Shrook does not behave this way. In fact, its default settings use “[Distributed Checking](http://www.fondantfancies.com/shrook/distfaq.php)”:


> Distributed Checking centrally coordinates the checking activity of
> multiple copies of Shrook subscribed to the same channel. This can keep
> each copy of Shrook updated within minutes of the channel itself
> updating, amongst other benefits.


What this means is that a Shrook user who is using Distributed Checking will only end up checking each subscribed feed a few times per day, but will receive a notification from Shrook’s centralized server within a few minutes of an update to each subscribed feed. You get the same results as with frequent polling, without abusing the server.


If you’re using Shrook, I encourage you either to use Distributed Checking (choose “Automatic” from the above menu in the prefs) or to choose an interval of 30 minutes or higher.



| **Previous:** | [Rob Enderle: Putting the ‘Anal’ in ‘Analyst’](https://daringfireball.net/2003/12/enderle) |
| **Next:** | [Die Hard](https://daringfireball.net/2004/01/die_hard) |


PreviousNext