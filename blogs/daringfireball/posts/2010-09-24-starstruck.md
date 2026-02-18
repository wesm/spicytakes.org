---
title: "Star-Struck"
date: 2010-09-24
url: https://daringfireball.net/2010/09/starstruck
slug: starstruck
word_count: 456
---


Last year I started an official DF Twitter account: [@daringfireball](http://twitter.com/daringfireball). Everything I post to Daring Fireball gets posted to that Twitter account automatically. Effectively, it’s a Twitter version of the DF RSS feed.


Part of the system I wrote to auto-tweet these posts is my own URL shortener. Because it seemed fun and looked sharp, I registered the domain name [✪df.ws](http://✪df.ws/). How? Thanks to [Internationalized Domain Names (IDN)](http://en.wikipedia.org/wiki/Internationalized_domain_name), domain names can now include Unicode glyphs. The DNS system was original conceived as ASCII-only, and IDN works around that by mapping domain names containing non-ASCII characters back to ASCII via an encoding method called [Punycode](http://en.wikipedia.org/wiki/Punycode). For example, the Punycode representation of “[✪df.ws](http://✪df.ws/)” is “[xn—df-oiy.ws](http://xn--df-oiy.ws/)”.1


At the outset, the only downside I foresaw to using this domain for my short URLs is that it wasn’t something people could type by hand. But how often do you type shortened URLs by hand? I almost always copy and paste them.


What I didn’t foresee was the tremendous amount of software out there that does not properly parse non-ASCII characters in URLs, particularly IDN domain names. Twitter clients (including, seemingly, every app written using Adobe AIR, which includes some very popular Twitter clients), web browsers (including Firefox), and, for a few months, even the Twitter.com website wasn’t properly identifying DF’s short URLs as links.


Worse, some — but, oddly, not all — of AT&T’s DNS servers for 3G wireless clients choke on IDN domains. This meant that even if you were using a Twitter client that properly supports IDN domains, these links *still* wouldn’t work if your 3G connection was routing through one of AT&T’s buggy DNS servers.


I was [stubbornly defiant](http://daringfireball.net/linked/2009/11/27/df-twitter) about this — particularly with regard to Twitter clients that didn’t parse these URLs correctly. But the problems never got better. AT&T’s buggy DNS servers remain a problem. TweetDeck still doesn’t grok non-ASCII URLs. Firefox still doesn’t open them correctly.


So, I give up. I’ve switched to a pure-ASCII domain name for short links: “df4.us”. If you previously tried following @daringfireball on Twitter and gave up because the links didn’t work, [you should try again](http://twitter.com/daringfireball).


---

1. I frequently get asked how and where I registered a non-ASCII domain name. Many — probably most, in fact — domain name registrars don’t support IDN. I used [Dynadot](http://www.dynadot.com/) to register mine, and consider myself a satisfied customer. Actually using an IDN domain has, as outlined above, proven to be an enormous pain in the ass, but registering and managing the settings for the domain itself, at Dynadot, has been no problem at all. ↩︎



| **Previous:** | [Regarding Ashok Kumar’s Track Record on Apple](https://daringfireball.net/2010/09/kumar_track_record) |
| **Next:** | [Apple Is No Longer Bundling Flash Player With Mac OS X](https://daringfireball.net/2010/10/apple_no_longer_bundling_flash_with_mac_os_x) |


PreviousNext