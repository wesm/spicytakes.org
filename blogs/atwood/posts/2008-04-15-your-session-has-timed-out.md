---
title: "Your Session Has Timed Out"
date: 2008-04-15
url: https://blog.codinghorror.com/your-session-has-timed-out/
slug: your-session-has-timed-out
word_count: 869
---

How many times have you returned to your web browser to be greeted by this unpleasant little notification:

kg-card-begin: html

> Your session has timed out. Please sign in again.

kg-card-end: html

If you’re anything like me, the answer is *lots*. What’s worse is that you’re usually kicked out of whatever page context you were working in. You have to manually log in again, remember what you were doing, then navigate back to where you were and resume your work.


Most programmers look at these sort of **browser session timeouts** as a necessary evil – sometimes even as a security “feature.” I know my bank website zealously logs me out of its web interface if I’m idle for more than five minutes. I’m not sure either one of these reasons are particularly justifiable.


**As a programmer, I understand why session expiration occurs.** The HTTP protocol that the web is built on is *stateless*. That means every individual request your browser sends to a web server is a newborn babe, cruelly born into a world that is utterly and completely oblivious to its existence. The way modern web applications get around this is by telling the browser to send a small, unique value back to the website with each request – this is known as a [HTTP cookie](http://en.wikipedia.org/wiki/HTTP_cookie). It sounds a lot tastier than it looks:


> Content-type: text/html
> Cookie: **SessionId=5451297120**


While there are privacy concerns with cookies, it is a generally accepted practice today – at least for the [first-party cookie flavors](http://www.opentracker.net/en/articles/all-about-cookies-third-party.jsp). While it is *possible* to maintain state without cookies, it’s painful and awkward.


Every web request to that server will include its own cookie and associated session id until it expires, usually many months or even years hence. The browser definitely isn’t the forgetful party here.


It’s up to the *server* to correlate the unique session identifier sent by the browser with your individual identity, context, settings, and preferences. This is usually stored in a database of some kind, keyed by your session identifier. For performance reasons, some chunk of session information also ends up in the server’s memory; there’s no need to reach all the way out to the database the next twenty-six times you obsessively refresh your Facebook profile page.


Still, that doesn’t explain why the web server mysteriously forgets about us. If anything, the server has all the information it needs to remember you, even if you walked away from your computer for a week. So why *does* the server choose to arbitrarily forget about you in an hour?

1. **Performance.** Consider a highly trafficked web site. If the website tried to keep sessions alive for an entire month, that could cause the session table to grow to millions of records. It’s even worse if you think about it in terms of user information cached in memory; a measly few kilobytes of memory state per user doesn’t sound like much, but multiplied by a few million, it absolutely is. If this data wasn’t expired and dumped on some schedule, it would quickly blow up the web server.
2. **Security.** The [magic cookie](http://en.wikipedia.org/wiki/Magic_cookie) that stores your session can potentially be stolen. If that cookie never expires, you have an infinitely long vulnerability window to [session hijacking](http://en.wikipedia.org/wiki/Session_hijacking). This is serious stuff, and mitigation strategies are limited. The best option, short of encrypting the entire connection from end to end via HTTPS, is to keep a tight expiration window on the session cookie, and regenerate them frequently.


That’s the why of browser session timeouts from the programmer’s perspective. But that doesn’t make it right. Far from it.


**As a user, I can say pretty unequivocally that session expiration *sucks*.** Is it really so unreasonable to start doing something in your web browser, walk away for an hour – maybe even for a few hours – then come back and expect things to *just work?*


As programmers, I think we can do better. It is possible. I am inundated with session timeout messages every day from a variety of sources, but I’ve never *once* seen a session expiration message from Gmail, for example. Here’s what I suggest:

1. Create a background JavaScript process in the browser that **sends regular heartbeats to the server**. Regenerate a new cookie with timed expiration, say, every 5 or 10 minutes.
2. If you’re worried about session hijacking – and [you *really* should be](http://news.bbc.co.uk/2/hi/technology/6929258.stm) – **use a HTTPS protected connection**. This is an absolute no-brainer for financial institutions of any kind.


I wish more developers would **test their web applications for session timeout issues. **Despite all rumors to the contrary, your users will not be dedicating their entire lives to using your web application in a punctual and timely manner. They have phone calls to take, meetings to go to, other websites and applications to attend to.


Is it really fair to kick users all the way out of your web application, or worse, blindly reject data they’ve submitted – just because they were *impudent* enough to wait a few hours since their last supplication to the web server gods? In most web apps, the penance is awfully severe for such a common sin.

[security](https://blog.codinghorror.com/tag/security/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[web sessions](https://blog.codinghorror.com/tag/web-sessions/)
[http](https://blog.codinghorror.com/tag/http/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
