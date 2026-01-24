---
title: "YSlow: Yahoo’s Problems Are Not Your Problems"
date: 2007-08-15
url: https://blog.codinghorror.com/yslow-yahoos-problems-are-not-your-problems/
slug: yslow-yahoos-problems-are-not-your-problems
word_count: 1492
---

I first saw [Yahoo’s 13 Simple Rules for Speeding Up Your Web Site](http://developer.yahoo.com/performance/rules.html) referenced in a [post on Rich Skrenta’s blog](https://web.archive.org/web/20070820063834/http://www.skrenta.com/2007/05/14_rules_for_fast_web_pages_by_1.html) in May. It looks like there were originally 14 rules; one must have fallen off the list somewhere along the way.

1. [Make Fewer HTTP Requests](http://developer.yahoo.com/performance/rules.html#num_http)
2. [Use a Content Delivery Network](http://developer.yahoo.com/performance/rules.html#cdn)
3. [Add an Expires Header](http://developer.yahoo.com/performance/rules.html#expires)
4. [Gzip Components](http://developer.yahoo.com/performance/rules.html#gzip)
5. [Put CSS at the Top](http://developer.yahoo.com/performance/rules.html#css_top)
6. [Move Scripts to the Bottom](http://developer.yahoo.com/performance/rules.html#js_bottom)
7. [Avoid CSS Expressions](http://developer.yahoo.com/performance/rules.html#css_expressions)
8. [Make JavaScript and CSS External](http://developer.yahoo.com/performance/rules.html#external)
9. [Reduce DNS Lookups](http://developer.yahoo.com/performance/rules.html#dns_lookups)
10. [Minify JavaScript](http://developer.yahoo.com/performance/rules.html#minify)
11. [Avoid Redirects](http://developer.yahoo.com/performance/rules.html#redirects)
12. [Remove Duplicate Scripts](http://developer.yahoo.com/performance/rules.html#js_dupes)
13. [Configure ETags](http://developer.yahoo.com/performance/rules.html#etags)


It’s solid advice culled from the excellent [Yahoo User Interface blog](https://web.archive.org/web/20070906094932/http://www.yuiblog.com/), which will soon be packaged into a [similarly excellent book](http://www.amazon.com/exec/obidos/ASIN/0596529309). It’s also available as a PowerPoint presentation delivered at the Web 2.0 conference.


I’ve also covered similar ground in my post, [Reducing Your Website’s Bandwidth Usage](https://blog.codinghorror.com/reducing-your-websites-bandwidth-usage/).


But before you run off and implement all of Yahoo’s solid advice, **consider the audience**. These are rules from Yahoo, which according to Alexa is one of the **top three web properties in the world**. And Rich’s company, Topix, is no slouch either – they’re in the top 2,000. It’s only natural that Rich would be keenly interested in Yahoo’s advice on how to **scale a website to millions of unique users per day.**


To help others implement the rules, Yahoo created a FireBug plugin, [YSlow](http://developer.yahoo.com/yslow/). This plugin evaluates the current page using the 13 rules and provides specific guidance on how to fix any problems it finds. And best of all, the tool rates the page with a score – a *score!* There’s nothing we love more than boiling down pages and pages of complicated advice to [a simple, numeric score](https://blog.codinghorror.com/the-high-score-table/). Here’s my report card score for yesterday’s post.


![](https://blog.codinghorror.com/content/images/2025/05/image-518.png)


To understand the scoring, you have to dissect the weighting of the individual rules, [as Simone Chiaretta did](http://codeclimber.net.nz/archive/2007/08/15/Dissecting-YSlow.aspx):

kg-card-begin: html


| **Weight 11** | 3. Add an Expires Header
4. GZip Components
13. Configure ETags |
| **Weight 10** | 2. Use a Content Delivery Network
5. Put CSS at the Top
10. Minify JavaScript
11. Avoid Redirects |
| **Weight 5** | 9. Reduce DNS Lookups
6. Move Scripts to the Bottom
12. Remove Duplicate Scripts |
| **Weight 4** | 1. Make Fewer Requests (CSS)
1. Make Fewer Requests (JS) |
| **Weight 3** | 1. Make Fewer Requests (CSS background images) |
| **Weight 2** | 7. Avoid CSS Expressions |


kg-card-end: html

My YSlow score of 73 is respectable, but I’ve already made some changes to accommodate its myriad demands. To get an idea of how some common websites score, Simone ran YSlow [on a number of blogs](http://codeclimber.net.nz/archive/2007/08/05/How-Slow-is-your-site-How-to-improve-the-performance.aspx) and recorded the results:

- Google: A (99)
- Yahoo Developer Network blog : D (66)
- Yahoo! User Interface Blog : D (65)
- Scott Watermasysk : D (62)
- Apple : D (61)
- Dave Shea’s mezzoblue : D (60)
- A List Apart : F (58)
- Steve Harman : F (54)
- Coding Horror : F (52)
- Haacked by Phil : F (36)
- Scott Hanselman’s Computer Zen : F (29)


YSlow is a convenient tool, but **either the web is full of terribly inefficient web pages**, or there’s something wrong with its scoring. I’ll get to that later.


The Stats tab contains a summary of the total size of your downloaded page, along with the footprint with and without browser caching. One of the key findings from Yahoo is that 40 to 60 percent of daily visitors [have an empty cache](https://web.archive.org/web/20070818003003/http://yuiblog.com/blog/2007/01/04/performance-research-part-2). So it behooves you to optimize the size of *everything* and not rely on client browser caching to save to you in the common case.


![](https://blog.codinghorror.com/content/images/2025/05/image-519.png)


YSlow also breaks down the statistics in much more detail via the Components tab. Here you can see a few key judgment criteria for every resource on your page...

- Does this resource have an explicit expiration date?
- Is this resource compressed?
- Does this resource have an ETag?


... along with the absolute sizes.


![yslow components](https://blog.codinghorror.com/content/images/uploads/2007/08/6a0120a85dcdae970b012877700c8f970c-pi.png)


YSlow is a useful tool, but it can be dangerous in the wrong hands. Software developers love optimization. [Sometimes too much](http://www.flounder.com/optimization.htm).


There’s some good advice here, but there’s also **a lot of advice that only makes sense if you run a website that gets millions of unique users per day**. Do you run a website like that? If so, what are you doing reading this instead of flying your private jet to a Bermuda vacation with your trophy wife? The rest of us ought to be a little more selective about the advice we follow. Avoid the temptation to blindly apply these “top (x) ways to (y)” lists that are so popular on Digg and other social networking sites. Instead, read the advice critically and think about the consequences of implementing that advice.


If you fail to read the Yahoo advice critically, you might make your site *slower*, as [Phil Haack unfortunately found out](http://www.haacked.com/archive/2007/08/13/speed-up-your-pages-and-improve-your-yslow-score-with.aspx). While many of these rules are bread-and-butter HTTP optimization scenarios, it’s unfortunate that a few of the highest-weighted rules on Yahoo’s list are downright dangerous, if not flat-out *wrong* for smaller web sites. And when you define “smaller” as “smaller than Yahoo,” that’s... well, almost everybody. So let’s take a critical look at the most problematic heavily weighted advice on Yahoo’s list.


**Use a Content Delivery Network (Weight: 10)**


If you have to ask how much a formal [Content Delivery Network](http://en.wikipedia.org/wiki/Content_Delivery_Network) will cost, you can’t afford it. It’s more effective to think of this as outsourcing the “heavy lifting” on your website – e.g., any large chunks of media or images you serve up – to external sites that are much better equipped to deal with it. This is one of the most important bits of advice I provided in [Reducing Your Website’s Bandwidth Usage](https://blog.codinghorror.com/reducing-your-websites-bandwidth-usage/). And using a CDN, below a reasonably Yahoo-esque traffic volume, can even slow your site down.


**Configure ETags (Weight: 11)**


ETags are a checksum field served up with each server file so the client can tell if the server resource is different from the cached version the client holds locally. Yahoo recommends turning ETags off because they cause problems on server farms due to the way they are generated with machine-specific markers. So unless you run a server farm, you should ignore this guidance. It’ll only make your site perform worse because the client will have a more difficult time determining if its cache is stale or fresh. It is possible for the client to use the existing last-modified date fields to determine whether the cache is stale, but [last-modified](http://perl.apache.org/docs/general/correct_headers/correct_headers.html#Last_Modified) is a weak validator, whereas [Entity Tag (ETag)](http://perl.apache.org/docs/general/correct_headers/correct_headers.html#Entity_Tags) is a strong validator. Why trade strength for weakness?


**Add an Expires Header (Weight: 11)**


This isn’t bad advice, per se, but it can cause huge problems if you get it wrong. In Microsoft’s IIS, for example, the Expires header is always turned off by default, probably for that very reason. By setting an Expires header on HTTP resources, you’re telling the client to *never check for new versions of that resource –* at least not until the expiration date on the Expires header. When I say never, I mean it – the browser won’t even *ask* for a new version; it’ll just assume its cached version is good to go until the client clears the cache, or the cache reaches the expiration date. Yahoo notes that they change the filename of these resources when they need them refreshed.


All you’re really saving here is the cost of the client pinging the server for a new version and getting a 304 not modified header back in the common case that the resource hasn’t changed. That’s not much overhead... unless you’re Yahoo. Sure, if you have a set of images or scripts that almost *never* change, definitely exploit client caching and turn on the [Cache-Control header](http://www.mnot.net/cache_docs/#CACHE-CONTROL). Caching is critical to browser performance; every web developer should have a deep understanding of [how HTTP caching works](http://www.mnot.net/cache_docs/). But only use it in a surgical, limited way for those specific folders or files that can benefit. For anything else, the risk outweighs the benefit. It’s certainly not something you want turned on as a blanket default for your entire website.. unless you like changing filenames every time the content changes.


I don’t mean to take anything away from Yahoo’s excellent guidance. Yahoo’s 13 Simple Rules for Speeding Up Your Web Site and the companion FireBug plugin, YSlow, are outstanding resources for the entire internet. By all means, read it. Benefit from it. Implement it. I’ve been banging away on [the benefits of GZip compression](https://blog.codinghorror.com/http-compression-and-iis-6-0/) for years.


But also **realize that Yahoo’s problems aren’t necessarily your problems**. There is no such thing as one-size-fits-all guidance. Strive to *understand* the advice first, then implement the advice that makes sense for your specific situation.

[performance](https://blog.codinghorror.com/tag/performance/)
[website optimization](https://blog.codinghorror.com/tag/website-optimization/)
[yahoo](https://blog.codinghorror.com/tag/yahoo/)
[yslow](https://blog.codinghorror.com/tag/yslow/)
[web development](https://blog.codinghorror.com/tag/web-development/)
