---
title: "The Great DF Random Slowdown Should Be Over"
date: 2018-09-20
url: https://daringfireball.net/2018/09/df_slowdown
slug: df_slowdown
word_count: 482
---


This week, DF has seemed incredibly slow for *some* people, *sometimes*. [Here’s a Twitter search for tweets to me with the word “slow” this week](https://twitter.com/search?l=&q=slow%20to%3Agruber%20since%3A2018-09-17%20until%3A2018-09-20&src=typd). This was killing me, because I pride myself on Daring Fireball being a fast-loading website, and because this was a pretty big week content-wise.


It was not my server, and had nothing to do with higher levels of traffic from my [iPhone XS](https://daringfireball.net/2018/09/the_iphones_xs) and [Series 4 Apple Watch](https://daringfireball.net/2018/09/apple_watch_series_4) reviews. When DF itself is slow — which happens rarely but does happen — you almost always see DF’s trademark #4a525a slate gray background first, then the elements of the page slowly fill in. If you experienced slowness this week, you probably just saw a white background in your browser tab, and then all of a sudden the whole thing filled in. This sometimes took 30-60 seconds. Long story short, it was taking that long for the initial request to even get to my server; once it did, everything after that was as fast as usual. I’m still not sure what exactly was causing this, but I’ve worked around it by having [Cloudflare](https://www.cloudflare.com/) act as an HTTP/S proxy for daringfireball.net. If any of you continue to see slow page loads, let me know.


Second, there was an issue where requests using the “www” prefix over HTTPS were triggering an SSL certificate warning from Safari that the site might not be legitimate. Only when using the “www” prefix, and only over HTTPS, not HTTP, because it was an SSL problem. I hadn’t changed anything on my end, but the latest version of Safari has tightened its SSL security. (Which is good.) I’ve never made use of a “www” prefix at Daring Fireball — I hate that prefix. But you have to support it, because so many people type it out of habit. So I’ve always redirected requests for “www.daringfireball.net” to “daringfireball.net”. The problem is, because I don’t actually use the “www” domain, I never properly supported it in my SSL certificate. Until a few weeks ago, Safari would just let you get redirected; now it doesn’t.


I solved this problem using [Cloudflare](https://www.cloudflare.com/) too. In fact both problems were fixed the same way — by clicking one button in Cloudflare’s list of my DNS entries to allow Cloudflare to proxy HTTP/S requests. I switched to Cloudflare a year or so ago for managing my DNS, and I couldn’t be happier. It’s like magic. DNS can seem like voodoo (at least to me) but Cloudflare makes it easy. I don’t even pay them — I’m just using their free basic account level. This is *not* a sponsorship or ad — I just had to thank them for their wonderful service.


Anyway, I want to apologize to any of you affected by either of these issues.



| **Previous:** | [Apple Watch Series 4](https://daringfireball.net/2018/09/apple_watch_series_4) |
| **Next:** | [Bloomberg’s ‘The Big Hack’](https://daringfireball.net/2018/10/bloomberg_the_big_hack) |


PreviousNext