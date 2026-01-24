---
title: "Url Shorteners: Destroying the Web Since 2002"
date: 2009-06-16
url: https://blog.codinghorror.com/url-shorteners-destroying-the-web-since-2002/
slug: url-shorteners-destroying-the-web-since-2002
word_count: 1069
---

Is anyone else as sick as I am of all the mainstream news coverage on Twitter? Don’t get me wrong, I’m a Twitter fan, and I’ve been a user since 2006. To me, it’s a form of [public instant messaging](https://blog.codinghorror.com/when-in-doubt-make-it-public/) – yet another way to [maximize the value of my keystrokes](https://blog.codinghorror.com/maximizing-the-value-of-your-keystrokes/). Still, I’m a little perplexed as to the media’s near-*obsession* with the service. If a day goes by now without the New York Times or CNN mentioning Twitter in some way, I become concerned. Am I really getting *all* the news? Or just the stupid, too long, non-140-character version of the news?


I guess I should be pleased that I was a (relatively) early adopter and advocate of software that has achieved the rarest of feats in the software industry – critical mass. Adoption by the proverbial “average user.” Whatever you may think of Twitter, consider this: as a software developer, you’ll be fortunate to build *one* project that achieves critical mass in your entire life. And even then, only if you are a very, *very* lucky programmer: in the right place, at the right time, with the right idea, working with the right people. Most of us never get there. I don’t think I will.


There is one side effect of this unprecedented popularity, though, that I definitely wouldn’t have predicted: **the mainstreaming of URL shortening services**. You can barely use Twitter without being forced into near-mastery of URL shortening. For example, this is the super-secret, patented formula I often use when composing my Twitter messages:


> “brief summary or opinion” [link for more detail]


Twitter only allows 140 characters in each status update. Some might view this as a limitation, but I consider it Twitter’s best feature. I am all for enforced brevity. Maybe that’s due to the pain of living through [a lifetime of emfail](https://blog.codinghorror.com/is-email-efail/). But depending on the size of the comment and the URL (and some URLs can be ridiculously long), I can’t *quite* fit everything in there without sounding like an SMS-addled teenage girl. This is where URL shortening comes in.


Now, I know what you’re thinking. You’re a clever programmer. *You* could implement some kind of fancy jQuery callback to shorten the URL, and replace the longer URL with the shorter URL right there in the text as the user pauses in typing. But you don’t even have to be that clever; most of the URL shortening services (that aren’t in their infancy) deliver a rather predictable size for the URLs they return. You could simply estimate the size of the URL post-shortening – maybe adding 1 character as a fudge factor for safety – and allow the update.


Twitter, I can assure you, is far more brain damaged than you can possibly imagine. It will indeed shorten URLs that fit in the 140 character limit (whoopee!), but it does *nothing* for URLs that don’t fit – it will not allow you to submit the message. All part of its endearing charm.


Lame, yes, but it means that the typical, mainstream browser-based Twitter user **is forced to become proficient with URL shortening services**. Due to the increased exposure they’ve enjoyed through Twitter’s meteoric rise to fame, the number of URL shortening services has exploded, and rapidly evolved – they’re no longer viewed as utility services to make URLs more convenient, but **a way to subjugate, control, and perhaps worst of all, “monetize” the web experience**.


This is dangerous territory we’re veering into now, [as Joshua Schachter explains](http://joshua.schachter.org/2009/04/on-url-shorteners.html).


> So there are clear benefits for both the service (low cost of entry, potentially easy profit) and the linker (the quick rush of popularity). But URL shorteners are bad for the rest of us.
> The worst problem is that shortening services add another layer of indirection to an already creaky system. A regular hyperlink implicates a browser, its DNS resolver, the publisher’s DNS server, and the publisher’s website. With a shortening service, you’re adding something that acts like a third DNS resolver, except one that is assembled out of unvetted PHP and MySQL, without the benevolent oversight of luminaries like Dan Kaminsky and St. Postel.


The web is little more than a maze of hyperlinks, and if you can insert yourself as an intermediary in that maze, you can transform or undermine the experience in fundamental ways. Consider the disturbing directions newer [URL shortening services are taking](http://en.wikipedia.org/wiki/URL_shortening#History):

- NotifyURL sends an email when the link is first visited.
- SnipURL introduces social bookmarking features such as usernames and RSS feeds.
- DwarfURL generates statistics.
- Adjix, XR.com and Linkbee are ad-supported models of URL shorteners that share the revenue with their users.
- bit.ly offers gratis click-through statistics and charts.
- Digg offers a shortened URL which includes not just the target URL, but an iframed version that includes a set of Digg-related controls called the Digg bar.
- Doiop allows the shortening to be selected by the user, and Unicode can be used to achieve really short URLs.


Believe it: **the humble hyperlink, thanks to pervasive URL shortening, can now be wielded as a weapon**. The internet is [the house that PageRank built](https://blog.codinghorror.com/markov-and-you/), and it’s all predicated on hyperlinks. Once you start making every link your special flavor of “shortened” link, framing the target content – heck, maybe wrapping it in a few ads for good measure – you’ve completely turned that system on its head.


What’s aggravating to me is that **the current situation is completely accidental**. If Twitter had provided a sane way to link a single word, none of these weaselly URL shortening clones would have reared their ugly heads at all. Consider how simple it is to decouple the hyperlink from the display text in, say, phpBB, or Markdown, or even good old HTML markup itself:

kg-card-begin: html

```

<a href=“http://example.com”>foo</a>
[url=http://example.com]foo[/url]
[foo](http://example.com)

```

kg-card-end: html

Every tiny URL is **another baby step towards destroying the web as we know it**. Which is exactly what you’d want to do if you’re attempting to build a business [on top of the ruins](http://www.readwriteweb.com/archives/bitly_alternative_to_tinyurl.php). Personally, I’d prefer to see the big, objective search engines who naturally sit at the center of the web offer their own URL shortening services. Who better to generate short hashes [of every possible URL](https://blog.codinghorror.com/url-shortening-hashes-in-practice/) than the companies who already have cached copies of every URL on the internet, anyway?

[social media](https://blog.codinghorror.com/tag/social-media/)
[url shortener](https://blog.codinghorror.com/tag/url-shortener/)
[software development](https://blog.codinghorror.com/tag/software-development/)
