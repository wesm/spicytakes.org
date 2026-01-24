---
title: "The Importance of Sitemaps"
date: 2008-10-12
url: https://blog.codinghorror.com/the-importance-of-sitemaps/
slug: the-importance-of-sitemaps
word_count: 1185
---

So I’ve been busy with [this Stack Overflow thing](https://blog.codinghorror.com/stack-overflow-none-of-us-is-as-dumb-as-all-of-us/) over the last two weeks. By way of apology, I’ll share a little statistic you might find interesting: the **percentage of traffic from search engines** at [stackoverflow.com](http://stackoverflow.com/).

kg-card-begin: html


| **Sept 16th**
one day after public launch | 10% |
| **October 11th**
less than one month after public launch | 50% |


kg-card-end: html

I try to be politically correct in discussing web search, avoiding the g-word whenever possible, desperately attempting to preserve the illusion that web search is actually a competitive market. But it’s becoming a transparent and cruel joke at this point. **When we say “web search” we mean one thing, and one thing only: Google**. [Rich Skrenta explains](https://web.archive.org/web/20081024055543/http://www.skrenta.com/2006/12/googles_true_search_market_sha.html):


> I’m not a professional analyst, and my approach here is pretty back-of-the-napkin. Still, it confirms what those of us in the search industry have known for a long time.
> The New York Times, for instance, gets nearly 6 times as much traffic from Google as it does from Yahoo. Tripadvisor gets 8 times as much traffic from Google vs. Yahoo.
> Even Yahoo’s own sites are no different. While it receives a greater fraction of Yahoo search traffic than average, Yahoo’s own flickr service gets 2.4 times as much traffic from Google as it does from Yahoo.
> My favorite example: According to Hitwise, [ex] Yahoo blogger Jeremy Zawodny gets 92% of his inbound search traffic from Google, and only 2.7% from Yahoo.


That was written almost two years ago. Guess which way those numbers have gone since then?


Google generally does a great job, so they deserve their success wholeheartedly, but I have to tell you: Google’s current position as the [start page for the internet](https://web.archive.org/web/20081019185509/http://www.skrenta.com/2007/01/winnertakeall_google_and_the_t.html) kind of scares the crap out of me, in a way that Microsoft’s dominance over the desktop PC never did. I mean, monopoly power over a desktop PC is one thing – but the internet is the whole of human knowledge, or something rapidly approaching that. Do we really trust one company to be a benevolent monopoly over... well, *everything?*


But I digress. **Our public website isn’t even a month old, and Google is already half our traffic**. I’m perfectly happy to feed Google the kind of quality posts (well, mostly) fellow programmers are creating on Stack Overflow. The traffic graph provided by Analytics is amusingly predictable, as well.


![](https://blog.codinghorror.com/content/images/2025/04/image-201.png)


Giant peak of initial interest, followed by the inevitable trough of disillusionment, and then the growing weekly humpback pattern of a site that actually (shock and horror) appears to be *useful* to some people. Go figure. Guess they call it crackoverflow for a reason.


We knew from the outset that Google would be a big part of our traffic, and I wanted us to rank highly in Google for one very selfish reason – **writing search code is hard**. It’s far easier to outsource the burden of search to Google and their legions of server farms than it is for our tiny development team to do it on our one itty-bitty server. At least not *well*.


I’m constantly looking up my own stuff via Google searches, and I guess I’ve gotten spoiled. I expect to type in a few relatively unique words from the title and have whatever web page I know is there appear instantly in front of me. For the first two weeks, this was definitely not happening reliably for Stack Overflow questions. I’d type in the *exact title* of a question and get nothing. Sometimes I’d even get copies of our content from evil RSS scraper sites that plug in their own ads of questionable provenance, which was downright depressing. Other times, I’d enter a question title and get a *perfect* match. Why was old reliable Google letting me down? Our site is simple, designed from the outset to be easy for search engines to crawl. What gives?


What I didn’t understand was the importance of a little file called [sitemap.xml](http://en.wikipedia.org/wiki/Sitemaps).


On a Q&A site like Stack Overflow, only the most recent questions are visible on the homepage. The URL to get to the *entire* list of questions looks like this:

kg-card-begin: html

```

http://stackoverflow.com/questions
http://stackoverflow.com/questions?page=2
http://stackoverflow.com/questions?page=3
..
http://stackoverflow.com/questions?page=931

```

kg-card-end: html

Not particularly complicated. I naively thought Google would have no problem crawling all the questions in this format. But after two weeks, it wasn’t happening. My teammate, Geoff, clued me in to Google’s webmaster [help page on sitemaps](http://www.google.com/support/webmasters/bin/answer.py?answer=40318&topic=13450):

kg-card-begin: html

> Sitemaps are particularly helpful if:
> Your site has dynamic content.
> Your site has pages that aren’t easily discovered by Googlebot during the crawl process – for example, pages featuring rich AJAX or Flash.
> Your site is new and has few links to it. (Googlebot crawls the web by following links from one page to another, so if your site isn’t well linked, it may be hard for us to discover it.)
> Your site has a large archive of content pages that are not well linked to each other, or are not linked at all.

kg-card-end: html

I guess I was spoiled by my previous experience with blogs, which are almost incestuously hyperlinked, where everything ever posted has a permanent and static hyperlink attached to it, with simple monthly and yearly archive pages. With more dynamic websites, this isn’t necessarily the case. The pagination links on Stack Overflow were apparently enough to prevent full indexing.


Enter `sitemap.xml`. The file itself is really quite simple; it’s basically a non-spammy, non-shady way to have a “page” full of links that you feed to search engines. A way that is officially supported and endorsed by all the major web search engines. An individual record looks something [like this](http://sitemaps.org/protocol.php):

kg-card-begin: html

```

<url>
<loc>http://stackoverflow.com/questions/24109/c-ide-for-linux</loc>
<lastmod>2008-10-11</lastmod>
<changefreq>daily</changefreq>
<priority>0.6</priority>
</url>

```

kg-card-end: html

The above element is repeated for each one of the ~27,000 questions on Stack Overflow at the moment. Most search engines assume the file is at the root of your site, but you can inform them of an alternate location through [robots.txt](http://en.wikipedia.org/wiki/Robots.txt):

kg-card-begin: html

```

User-Agent: *
Allow: /
Sitemap: /sitemap.xml

```

kg-card-end: html

There are also limits on size. The `sitemaps.xml` file cannot exceed 10 megabytes in size, with no more than 50,000 URLs per file. But you can have multiple sitemaps in a sitemap index file, too. If you have millions of URLs, you can see where this starts to get hairy fast.


**I’m a little aggravated that we have to set up this special file for the Googlebot to do its job properly**; it seems to me that web crawlers should be able to spider down our simple paging URL scheme without me giving them an explicit assist.


The good news is that since we set up our `sitemaps.xml`, every question on Stack Overflow is eminently findable. But when 50% of your traffic comes from one source, perhaps it’s best not to ask these kinds of questions.


![](https://blog.codinghorror.com/content/images/2025/04/image-200.png)


Just smile and nod and follow the rules like everyone else. I, for one, [welcome our pixelated Google overlords!](http://kottke.org/06/09/pixelated-google-overlords)

[seo](https://blog.codinghorror.com/tag/seo/)
[sitemap](https://blog.codinghorror.com/tag/sitemap/)
[search engine optimization](https://blog.codinghorror.com/tag/search-engine-optimization/)
[web traffic](https://blog.codinghorror.com/tag/web-traffic/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
