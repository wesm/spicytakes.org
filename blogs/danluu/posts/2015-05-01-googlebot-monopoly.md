---
title: "The googlebot monopoly"
date: 2015-05-01
url: https://danluu.com/googlebot-monopoly/
slug: googlebot-monopoly
word_count: 698
---


TIL that Bell Labs and a whole lot of other websites block archive.org, not to mention most search engines. Turns out I havea broken website linkin a GitHub repo, caused by the deletion of an old webpage. When I tried to pull the original from archive.org, I found that it's not available because Bell Labs blocks the archive.org crawler in their robots.txt:

```
User-agent: Googlebot
User-agent: msnbot
User-agent: LSgsa-crawler
Disallow: /RealAudio/
Disallow: /bl-traces/
Disallow: /fast-os/
Disallow: /hidden/
Disallow: /historic/
Disallow: /incoming/
Disallow: /inferno/
Disallow: /magic/
Disallow: /netlib.depend/
Disallow: /netlib/
Disallow: /p9trace/
Disallow: /plan9/sources/
Disallow: /sources/
Disallow: /tmp/
Disallow: /tripwire/
Visit-time: 0700-1200
Request-rate: 1/5
Crawl-delay: 5

User-agent: *
Disallow: /

```

In fact, Bell Labs not only blocks the Internet Archiver bot, it blocks all bots except for Googlebot, msnbot, and their own corporate bot. And msnbot was superseded by bingbotfive years ago!

A quick search using a term that's only found at Bell Labs1, e.g., “This is a start at making available some of the material from the Tenth Edition Research Unix manual.”, reveals that bing indexes the page; either bingbot follows some msnbot rules, or that msnbot still runs independently and indexes sites like Bell Labs, which ban bingbot but not msnbot. Luckily, in this case, a lot of search engines (like Yahoo and DDG) use Bing results, so Bell Labs hasn't disappeared from the non-Google internet, but you're out of luckif you're one of the 55% of Russians who use yandex.

And all that is a relatively good case, where one non-Google crawler is allowed to operate. It's not uncommon to see robots.txt files that ban everything but Googlebot. Runninga competing search engineand preventing a Google monopoly is hard enough without having sites ban non-Google bots. We don't need to make it even harder, nor do we need to accidentally2ban the Internet Archive bot.

P.S. While you're checking that your robots.txt doesn't ban everyone but Google, consider looking at your CPUID checks to make sure that you're using feature flagsinstead of banning everyone but Intel and AMD.

BTW, I do think there can be legitimate reasons to block crawlers, including archive.org, but I don't think that the common default many web devs have, of blocking everything but googlebot, is really intended to block competing search engines as well as archive.org.

2021 Update: since this post was first published, archive.org started ignoring being blocked in robots.txt and archives posts where they are blocked in robots.txt. I've heard that some competing search engines do the same thing, so this mis-use of robots.txt, where sites ban everything but googlebot, is slowly making robots.txt effectively useless, much like browsers identify themselves as every browser in user-agent strings to work around sites that incorrectly block browsers they don't think are compatible.

A related thing is that sites will sometimes ban competing search engines, like Bing, in a fit of pique, which they wouldn't do to Google since Google provides too much traffic for them to be able get away with that, e.g.,Discourse banned Bing because they were upset that Bing was crawling discourse at 0.46 QPS.

---

1. At least until this page gets indexed. Google has a turnaround time of minutes to hours on updates to this page, which I find pretty amazing. I actually find that more impressive than seeing stuff on CNN reflected in seconds to minutes. Of course search engines are going to want to update CNN in real time. But a blog like mine? If they're crawling a niche site like mine every hour, they must also be crawling millions or tens of millions of other sites on an hourly basis and updating their index appropriately. Either that or they pull updates off of RSS, but even that requires millions or tens of millions of index updates per hour for sites with my level of traffic.[return]
2. I don't object, in principle, to a robots.txt that prevents archive.org from archiving sites -- although the common opinion among programmers seems to be that it's a sin to block archive.org, I believe it's fine to do that if you don't want old versions of your site floating around. But it should be an informed decision, not an accident.[return]
