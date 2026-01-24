---
title: "Designing For Evil"
date: 2008-05-28
url: https://blog.codinghorror.com/designing-for-evil/
slug: designing-for-evil
word_count: 1468
---

Have you ever used [Craigslist](https://en.wikipedia.org/wiki/Craigslist)? It’s an almost entirely free, mostly anonymous [classified advertising](http://en.wikipedia.org/wiki/Classified_advertising) service which evolved from an early internet phenomenon into a service so powerful it is often accused of single-handedly [destroying the newspaper business](https://web.archive.org/web/20080906121753/http://www.sfweekly.com/2005-11-30/news/craig-list-com/). Unfortunately, these same characteristics also make Craigslist a particularly juicy target for spammers and evildoers. Who knows; maybe it’s karma.


I consider Craigslist a generally benevolent public service. Perhaps that’s why I was so disturbed by [John Nagle’s](https://web.archive.org/web/20080913181627/http://www.sitetruth.com/yhoo.html) wartime narrative of the raging [battle between Craigslist and spammers](http://techdirt.com/articles/20080523/0327151211.shtml).

kg-card-begin: html

> Spam on Craigslist has been a minor nuisance for years. Not any more. **This year, the spammers started winning and are taking over Craigslist.** Here’s how they did it. Craigslist tries to stop spamming by:
> Checking for duplicate submissions.
> Blocking excessive posts from a single IP address.
> Requiring users to register with a valid email address.
> Using a CAPTCHA to stop automated posting tools.
> Letting users flag postings they recognize as spam.
> Several commercial products are now available to overcome those little obstacles to bulk posting. CL Auto Posting Tool is one such product. It not only posts to Craigslist automatically, it has built-in strategies to overcome each Craigslist anti-spam mechanism:
> Random text is added to each spam message to fool Craigslist’s duplicate message detector.
> IP proxy sites are used to post from a wide range of IP addresses.
> E-mail addresses for reply are Gmail accounts conveniently created by Jiffy Gmail Creator (ed. note: this does *not* break Google’s CAPTCHA, as you can [[see in this screenshot]](https://blog.codinghorror.com/content/images/2015/08/jiffy_gmail_email_creator-81763-2.jpeg)
> An OCR system reads the obscured text in the CAPTCHA.
> Automatic monitoring detects when a posting has been flagged as spam and reposts it. 
> CL Auto Poster isn’t the only such tool. Other desktop software products are AdBomber and Ad Master. For spammers preferring a service-oriented approach, there’s ItsYourPost. With these power tools, the defenses of Craigslist have been overrun. **Some categories on Craigslist have become over 90% spam.** The personals sections were the first to go, then the services categories, and more recently, the job postings.
> Craigslist is fighting back. Its latest gimmick is phone verification. Posting in some categories now requires a callback phone call, with a password sent to the user either by voice or as an SMS message. Only one account is allowed per phone number. Spammers reacted by using VoIP numbers. Craigslist blocked those. Spammers tried using number-portability services like Grand Central and Tossable Digits. Craigslist blocked those. Spammers tried using their own free ringtone sites to get many users to accept the Craigslist verification call, then type in the password from the voice message. Craigslist hasn’t countered that trick yet.
> Much of the back and forth battle can be [followed in various forums](https://news.ycombinator.com/item?id=247724). It’s not clear yet who will win.

kg-card-end: html

I’ve used Craigslist quite a few times in the past, mostly to sell things that are too unwieldy to ship, with generally positive results. But that’s the “for sale” section, and the spammers seem to be concentrating on the personals and services. I was curious about this, so I delved into the local personals section in what I guessed to be the most popular category. (Note to my wife: this is *research!* Research! I *swear!*)


Almost immediately I found a personals ad with the following “image”:


![](https://blog.codinghorror.com/content/images/2025/04/image-129.png)


It’s an encoded wartime transmission from someone battling Craigslist spammers. It ends on this dire warning:

kg-card-begin: html

> 99.9% of the ads these days are fakes. Sad but true. REALLY, ALMOST ALL THE ADS ARE FAKE!

kg-card-end: html

But is it true? I saw some obvious spam in the personals section – all of which had been flagged for removal by the time I clicked on it – but certainly nothing to corroborate this 99.9% claim. I did a few unique term searches on random personals (my favorite at the moment is “no murderers please!”), and they came up unique.


Clearly, there’s a war on, and there have been casualties on both sides. Even if the spammers aren’t winning, every inch they gain **further undermines the community’s trust in Craigslist and devalues everyone’s participation**.


This is a topic I am acutely interested in as we build stackoverflow.com out. Like Craigslist, [Stack Overflow](http://stackoverflow.com/) will offer a rich experience for anonymous internet users. We will not require you to create an account or “login” to answer or ask questions. We’ll even track your reputation and preferred settings for you, as long as you allow us to store a standard browser cookie. While it’s true that we’ll initially be a low-value target due to limited traffic and a specialized audience, that will inevitably change over time. So you can expect some of the same measures on Stack Overflow (and, later, [Discourse](http://www.discourse.org/)) that Craigslist and Wikipedia use to **mitigate anonymous evil**:

- Some form of CAPTCHA.
- The ability to temporarily “lock” controversial questions so only registered users can edit or add responses.
- An automatic throttle if we see rapid, bot-like actions from your IP address.
- Some basic heuristics to detect “spammy” content, such as too many URLs, or typing inhumanly fast.
- An easy way for users with sufficient reputation to undo vandalism by reverting to an earlier version.


The community itself can also assist. Every question and answer on Stack Overflow can be rated Digg style; if a given bit of content rapidly accrues a large number of downmods, it is likely to be spam or inappropriate content, and will be automatically removed or directed into a moderation queue.


Don’t get me wrong. I’ve been humbled by the quality – and the sheer size – of the community that has grown up around this blog. I expect the overwhelming majority of people who participate in Stack Overflow will be upstanding Internet citizens. **Wikipedia is a living testament to the fact that goodness vastly outnumbers evil.** We good guys *can* win, if we have the forethought to put some controls in place first.


Allowing anonymous users to post creates a volatile situation where a dozen sufficiently motivated spammers can easily poison the well for *thousands* of typical users. These spammers don’t give a damn about the community we’re building together. All they care about is getting paid by posting their links anywhere and everywhere they can. They’ll run roughshod over as many websites and pages as possible in their frantic, abusive pursuit of money. If I didn’t so desperately want to choke the life out of each and every one of them, I might actually feel sorry for the poor bastards.


But here’s the problem: following the rules and being a good citizen is easy. Being evil is hard; it takes more work. Sometimes a lot more work. **The bad guys get *paid* to learn about their exploits.** Are you willing to educate yourself about the complex evil that a tiny minority of powerful users are prepared to unleash upon your site?


As with so many things in life, this is best illustrated by a scene from [Spaceballs](http://www.imdb.com/title/tt0094012/):


> So, Lone Starr... now you see that evil will always triumph, b*ecause good is **dumb**.*

kg-card-begin: html

As the good guys, we can't afford to be ignorant of the spammers' techniques. If that means spelunking through the grimiest corners of some [scummy black hat forums](https://www.blackhatworld.com/forums/), then so be it. I'll tell you this: I've never [nofollowed](http://en.wikipedia.org/wiki/Nofollow) a single link on this blog until today. The most effective way to fight the evil spammers is to understand them, and the first step toward understanding evil is openly linking to their tools and methods, exposing them to as much public scrutiny as possible.

kg-card-end: html

When you design your software, **work under the assumption that some of your users will be evil**: out to game the system, to defeat it at every turn, to cause interruption and denial of service, to attack and humiliate other users, to fill your site with the vilest, nastiest spam you can possibly imagine. If you *don’t* do that, you’ll end up with something like [blog trackbacks](https://blog.codinghorror.com/the-day-the-trackbacks-died/), which are irreparably busted at this point. Trackbacks are the source of countless untold hours of institutionalized spam pain and suffering, all because the initial designers apparently did not ask themselves one simple question: what if some of our users are evil?


![](https://blog.codinghorror.com/content/images/2025/04/dark-helmet-from-spaceballs-movie-1987-1.jpg)


Because when good is dumb, evil will always triumph.


Websites that allow users to post content will always be vulnerable to the actions of a handful of evil, spammy users. It’s not pleasant. It is a dark mirror into the ugly underbelly of human nature. But it’s also an unfortunate, unavoidable fact of life. And **when you fail to design for evil, you have failed your community.**

[spam](https://blog.codinghorror.com/tag/spam/)
[craigslist](https://blog.codinghorror.com/tag/craigslist/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[online advertising](https://blog.codinghorror.com/tag/online-advertising/)
