---
title: "Segmentation By Freshness"
description: "One of the biggest issues with media websites is dealing with 	high amounts of traffic. Media is all about getting eyeballs, but if 	you get too many hits at once, slow performance can cause problems "
date: 2008-06-24T00:00:00
tags: ["web development"]
url: https://martinfowler.com/bliki/SegmentationByFreshness.html
slug: SegmentationByFreshness
word_count: 965
---


One of the biggest issues with media websites is dealing with
	high amounts of traffic. Media is all about getting eyeballs, but if
	you get too many hits at once, slow performance can cause problems
	and damage your reputation. This problem is exacerbated by the
	bursty nature of this web traffic. You can be cruising along at a
	manageable rate, then get hit with a big news story which causes a
	big spike. One of our clients have seen spikes of two orders of
	magnitude in a matter of a couple of minutes.


The general solution in computing to speed up access to the same
	information is to use caches. If you keep requesting my home page
	the web server will build up a cache in memory so repeated requests
	avoid touching the disk.


It's easy to keep a cache for my website, because this page, like my
	entire site, is entirely static. Most media sites, however, contain a
	lot of dynamic content. You might not think there's much business
	logic on your average newspaper website, but once you start looking
	at advertising links, related stories, special features and the
	like, things get a good bit more interesting. A travel story to
	France might link to articles on french food, and advertising that
	knows that a web browser in Canada is interested in a holiday in
	the Loire Valley. Personalization makes this even worse, my personalized
	preferences should generate a personalized feature list on heavy red
	wines. Such logic is complex in its own right, it makes
	for a lot of computation with each request, and crucially it ruins
	most caching strategies.


The way to deal with this is to divide a page up into segments
	where each segment has a similar determination of freshness. The
	article on Loire travel can be relatively static, changing only to
	correct errors. A related article list which feeds off tags for
	âFranceâ and âLoireâ will change more often, but maybe only every
	few days. If we arrange this properly a request for a page with
	these two items may be able to gather everything from caches.


The most common way of doing this that I've seen is to form
	caches on the web server and assemble the page segments when the
	page gets hit. Tools like Sitemesh are a good option for this
	approach. As you write the page for 18th century loire delights, you
	include call-outs for sections like related articles. When you get
	the actual web request the web server takes the page and assembles
	the page from the separate pieces. Much of this can be cached in the
	web server, which avoids hitting the back-end domain logic and database.


An interesting possibility is to go even further and use the many
	caches that exist in the web itself. Most calls for this web page
	don't even reach my web server since my page gets cached many times
	along the way. If you build a web page dynamically and assemble it on
	the server, you have to take the hit to deliver the page. An
	alternative is to assemble the page on the client and then draw each
	segment from its own URL. Each segment could be cached in different
	places with different caching policies.


How might this work? We might store the static article content as
	XHTML at an URL like
	`http://gallifreyTimes/travel/18-century-loire-delights`. Inside that
	file we want to insert some related articles by looking up articles
	tagged with âloireâ and âfranceâ. In the static page we put in a
	simple âaâ tag.


```

  <a class = "relatedLinks" href = "relatedLinks/france+loire">Related Links</a>

```


In the header for the static page we link it to some javascript
	in a separate library file. When we download the Loire article the
	javascript runs and scans the article for elements with the right
	class: in this case an âaâ element with the ârelatedLinksâ
	class. (The [behavior
	library](http://bennolan.com/behaviour/) is a good way to do this.) When it finds the element it
	uses the information in the element to synthesize an URL for that
	segment. In this case it would use what's in the element's href
	attribute to come up with an URL like
	`http://gallifreyTimes/relatedArticles/france+loire`. Once
	it's got that URL it then gets the content and uses it to
	replace the original âaâ element. Since the related articles list is
	handled through an URL, other gets on that URL cause caches through
	the Internet to warm up, so there's a good chance that retrieving
	the page may never cause a hit on the original server.


This technique of using Javascript to replace a placeholder
	element with more content is a form of [Progressive
	Enhancement](http://en.wikipedia.org/wiki/Progressive_enhancement). The descriptions I've found for Progressive
	Enhancement focus on adding features for accessibility with limited
	browsers. This example also has that benefit. If I browse the page with a
	browser that has no javascript, I'll get a useful link. The general
	idea behind Progressive Enhancement is that the basic page served is
	useful on basic browsers, then we use techniques such as javascript
	to add in more fancy features.


In the context of caching, the value is that each progressive
	enhancement weaves in a lump of HTML with different freshness
	rules. The original page is static, the related links change daily,
	but both can be cached independently and weaved together. I can do
	all sorts of additional elements, as long as I take care to keep
	segment the page by the freshness rules. So I could include a
	personalized weather forecast based on the user's profile to every
	page by having the javascript pick up the user id from the http
	session, using it to construct an URL like
	`http://gallifreyTimes/personalWeather/martinfowler`,
	retrieving the content (which would often be cached on my hard
	drive) and weaving it into the page.
