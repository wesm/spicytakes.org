---
title: "Searching all Craigslist.org Cities"
date: 2005-03-31
url: https://blog.codinghorror.com/searching-all-craigslistorg-cities/
slug: searching-all-craigslistorg-cities
word_count: 359
---

If you’ve ever used [Craigslist.org](http://www.craigslist.org/about/) – a fantastic and rather odd resource – you may have noticed that it’s heavily biased towards per-city searches. This is a pain if you want to do a national search across all cities that Craigslist.org operates sites for. A while back, I found a web page offering an all-city search, but I wasn’t happy with the performance. And now it’s been perma-banned by the Craigslist.org brass, so... time to roll up my sleeves and implement my own, improved [Craigslist.org “all cities” jobs search](https://web.archive.org/web/20050629235542/http://www.codinghorror.com/craigslist/).


My search is dramatically faster than [Chovy’s](https://web.archive.org/web/20050402034928/http://www.chovy.com/), because I use HTTP compressed queries and progressive `Response.Write` and `Response.Flush` output rendering as the queries are returned. This is one of my major beefs with ASP.NET; **there’s no way to do any kind of progressive page rendering using the ASP.NET architecture**. (And no, iframes do not count.) The entire page renders to a buffer, then – and *only* then – it is all displayed at once. Not exactly an ideal web experience if you’re building large pages.


Progressive output is particularly critical for a long-running web page process like this one. Otherwise you’d be sitting there looking at a whole lot of nothing until all ~30 cities were queried. Technically it takes the same amount of time, but **there’s a huge psychological difference between seeing immediate, if partial, results, and waiting the same amount of time looking at a blank screen.** I always try my best to design for progressive rendering, [even in Windows Forms](https://blog.codinghorror.com/perceived-performance-and-formpaint/).


Interestingly, I had to disable IIS6 dynamic compression to get `Response.Flush` to behave as expected. The good news is that [disabling IIS6 compression](https://web.archive.org/web/20050404070055/http://www.windowsforms.net/Forums/ShowPost.aspx?tabIndex=1&tabId=41&PostID=14142) can be done on a per-website per-folder basis:


> *I used the following commands from the InetpubAdminScripts directory:
> cscript adsutil.vbs set w3svc/{site#}/root/{vdir name}/DoStaticCompression False
> cscript adsutil.vbs set w3svc/{site#}/root/{vdir name}/DoDynamicCompression False
> To get the {site#}, click on the “Web Sites” node in the IIS manager and note the “Identifier” number in the right-hand Detail pane for the top-level website that contains the NTD application.*


My favorite Craigslist posting, by the way, is [this one](https://web.archive.org/web/20050404003359/http://filtersweep.shackspace.com/58988662.html).

[craigslist.org](https://blog.codinghorror.com/tag/craigslist-org/)
[web scraping](https://blog.codinghorror.com/tag/web-scraping/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[http compression](https://blog.codinghorror.com/tag/http-compression/)
[progressive rendering](https://blog.codinghorror.com/tag/progressive-rendering/)
