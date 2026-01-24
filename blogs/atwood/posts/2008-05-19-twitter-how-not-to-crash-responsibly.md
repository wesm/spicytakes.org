---
title: "Twitter: How Not To Crash Responsibly"
date: 2008-05-19
url: https://blog.codinghorror.com/twitter-how-not-to-crash-responsibly/
slug: twitter-how-not-to-crash-responsibly
word_count: 563
---

In yesterday’s post on [Crashing Responsibly](https://blog.codinghorror.com/crash-responsibly/), I outlined a few ways to improve your application’s crash behavior. In the event that your application crashes – and oh, it will – why not turn that crash into something that:

- Records lots of diagnostic information **developers** can use to improve the application over time.
- Reassures **users** and provides them with helpful information.


With that in mind, let’s take a look at the Twitter crash page. How does it serve developers and users?


![](https://blog.codinghorror.com/content/images/2025/04/image-120.png)


I don’t mean to pick on Twitter; their bouts of downtime are near legendary at this point. Frankly, it’s been [discussed to death](https://blog.codinghorror.com/twitter-service-vs-platform/).


It’s unfortunate, because I love Twitter. Like Michael Lopp, I’m dangerously close to being [a Twitter fanboy](https://web.archive.org/web/20080519103935/http://www.randsinrepose.com/archives/2008/05/15/we_travel_in_tribes.html).


> The answer comes down to value. In the time that I’ve been using Twitter, it’s transformed from a curiosity to an essential service. What were seemingly random status updates have now become organized into organic conversational threads that bring a steady flow of relevant content across my desktop.


An “essential service” is exactly the kind of thing you *don’t* want to see error pages on. So, then, how does the Twitter error page fare?


Not so badly at first glance. It’s an attractive error page, styled to match Twitter, with some basic links and navigational elements. Let’s be generous and assume that the notification and logging of errors behind the scenes is taken care of. The Twitter developers must have access to a voluminous set of error logs by now.


But Twitter’s error page is **conspicuously lacking any real *information***. As an enthusiastic Twitter user presented with this error page, I am anything but reassured. Instead, I have some nagging questions:

- Is this an ephemeral, temporary error or some kind of scheduled downtime? How do I tell the difference?
- If this is scheduled downtime, when will it be over? Can I view the maintenance schedule, or the current status of the maintenance work?
- Is Twitter [down for everyone, or just me](http://downforeveryoneorjustme.com/)? Is there a place I can go to check Twitter’s current system health?
- Twitter has a reputation for unreliability. Where can I find out about Twitter’s ongoing efforts to improve their reliability?


There’s absolutely no mention of *any* of these things on the error page, the exact place I would care the most. Clicking through to the blog provides no relief, no mention of any availability work or maintenance schedules.


Furthermore, it’s difficult to take the glib claim that “we’re going to fix it up and have things back to normal soon” seriously. I’ve seen so much of the Twitter error page in the last year that I’ve lost confidence that these errors mean anything to anyone – or that they’re even recorded. This is the static error page that [cried wolf](http://en.wikipedia.org/wiki/The_Boy_Who_Cried_Wolf). Where’s the improvement over time from the collection and analysis of these errors?


I understand that Twitter has scaling problems I can only dream of. I don’t envy the amount of work they’ll have to undertake to fix this pernicious, systemic problem of massive scale.


But **I sure wish they could be a lot more transparent about it**.


Isn’t that what crashing responsibly is all about – establishing an honest, open dialog between users and developers, even at the worst possible moment of that relationship?

[software development](https://blog.codinghorror.com/tag/software-development/)
[crash handling](https://blog.codinghorror.com/tag/crash-handling/)
[twitter](https://blog.codinghorror.com/tag/twitter/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
