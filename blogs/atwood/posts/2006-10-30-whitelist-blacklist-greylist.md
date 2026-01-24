---
title: "Whitelist, Blacklist, Greylist"
date: 2006-10-30
url: https://blog.codinghorror.com/whitelist-blacklist-greylist/
slug: whitelist-blacklist-greylist
word_count: 786
---

I recently got into a spirited discussion about [Akismet](http://akismet.com/). What is Akismet?


> When a new comment, trackback, or pingback comes to your blog it is submitted to the Akismet web service which runs hundreds of tests on the comment and returns a thumbs up or thumbs down.


Akismet is awfully coy about the “tests” they run to distinguish between spam and everything else. I believe Akismet is essentially the same as the old [mt-blacklist](http://www.jayallen.org/projects/mt-blacklist/index-old) plugin I use to block trackback spam. But instead of manually entering blacklist terms, Akismet harnesses the [collective knowledge of the intarwebs](https://akismet.com/support/). As soon as one person blacklists something, it’s blacklisted for the entire Akismet community. And it definitely works. It’s so effective that [some people](http://www.hanselman.com/) use it as their only protection against spam comments and trackbacks. I think this is very unwise.


First of all, blacklists aren’t a panacea. They have their pros and cons. Just ask [Matt Mullenweg](http://photomatt.net/), the author of Akismet. He recently left [this comment](https://web.archive.org/web/20061019064327/http://elliottback.com/wp/archives/2006/09/23/akismet-hack/) on a blog post:


> Unfortunately, **the DNS realtime blacklists cause an unusually high false positive rate**, which is why we don’t use them anymore.


Interesting. And if you’re going to keep a blacklist, you might as well keep a greylist and whitelist, too:


![](https://blog.codinghorror.com/content/images/2025/05/image-396.png)


These three lists have been around as long as spam itself:


Items on the **Blacklist** are *never allowed through*. They are either held in a moderation queue, or deleted.


Items on the **Whitelist** are *always allowed through*.


Items on the **Greylist** are *held for human moderation*.


Akismet also offers a moderation queue, so it has aspects of a greylist as well. Instead of spending time maintaining a blacklist, you spend time staring down [a greylist moderation queue](http://www.problogger.net/archives/2006/07/29/comment-spam-is-akismet-ok/). I’m not so sure that’s an improvement. If you consider Akismet a success because you *ignore the moderation queue entirely*, have you really succeeded?


It’s also quite possible to use [whitelist attacks](https://web.archive.org/web/20061106073247/http://www.iampariah.com/blog/2005/12/whitelist-spam-attacks-threaten-blogs-and-email/) on blacklists, where spammers use innocent and legitimate URLs in their spam. I’ve had a few of these myself. Even if you don’t have a whitelist, attacks like this greatly reduce the effectiveness of a blacklist – legitimate domains end up blacklisted through collateral damage.


But let’s forget, for a moment, all the problems I just described with blacklists, whitelists, and greylists. **The core problem is relying on a single method of defense against spam. **Relying *only* on Akismet means:

1. You’ve added an external dependency to your website. [I hate dependencies](https://blog.codinghorror.com/dependency-avoidance/), and I always strive to keep the number of dependencies I accept to an absolute minimum.
2. If Akismet goes down, you either get inundated by spam while the floodgates are open, or nobody can comment/trackback. Neither scenario is desirable.
3. I get 75 spam trackbacks per *hour* on this blog. Multiply that the number of blogs on the internet, and you get an astronomically large number. Why should Akismet have to check every single one of those? Does Akismet have the capacity to scale that large? And is it reasonable to expect them to?


I can understand making the choice to use Akismet exclusively for trackbacks, where our options for combating spam are severely limited. But for comments, [abandoning CAPTCHA](https://blog.codinghorror.com/captcha-effectiveness/) in favor of Akismet is unforgivable. [Engtech](http://engtech.wordpress.com/) explains some of the problems with this approach in a recent comment:

kg-card-begin: html

> [Akismet] has been pretty effective, but there’s been a few interesting cases:
> compliment spam (“great post!” with website field linking to their p-rn/adsense splog site)
> only attacking blogs that appear to still have the default post as the first post — less likely to monitor spam.
> one p-rn spammer who finds political/pop culture keywords in a post and inserts human crafted messages. Like: “Some people say Matt Damon isn’t that good of an actor, I really liked him in Talented Mr. Ripley” whenever it finds a post with “Matt Damon”
> The one thing it has absolutely sucked at is spammers-to-be. People who are just testing out spam generation algorithms that have no payload. So you’ll get random gibberish from an IP address and it will take a few days for Akismet to learn.

kg-card-end: html

Hearing this pains me greatly. All the of the above could have been completely eliminated by using *both* methods: **CAPTCHA to validate that it’s a human, then Akismet to validate that it’s not human-entered spam.**


Akismet is a fine addition to our anti-spamming toolkit. But that doesn’t mean it’s a good idea to outsource your entire anti-spam effort to a single website, either. Anti-spam security starts at home. For best results, use [defense in depth](http://en.wikipedia.org/wiki/Defence_in_depth) and **combine local anti-spam measures, such as CAPTCHA, with Akismet as a backup.**

[security](https://blog.codinghorror.com/tag/security/)
[spam protection](https://blog.codinghorror.com/tag/spam-protection/)
[akismet](https://blog.codinghorror.com/tag/akismet/)
[blacklisting](https://blog.codinghorror.com/tag/blacklisting/)
[whitelisting](https://blog.codinghorror.com/tag/whitelisting/)
