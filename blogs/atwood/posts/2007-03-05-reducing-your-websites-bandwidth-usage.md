---
title: "Reducing Your Website’s Bandwidth Usage"
date: 2007-03-05
url: https://blog.codinghorror.com/reducing-your-websites-bandwidth-usage/
slug: reducing-your-websites-bandwidth-usage
word_count: 1838
---

Over the last three years, this site has become far more popular than I ever could have imagined. Not that I’m complaining, mind you. Finding an audience and opening a dialog with that audience is the whole point of writing a blog in the first place.


But on the internet, [popularity is a tax](https://blog.codinghorror.com/the-popularity-tax/). Specifically, a bandwidth tax. When [Why Can’t Programmers... Program?](https://blog.codinghorror.com/why-cant-programmers-program/) went viral last week, outgoing bandwidth usage spiked to **nearly 9 gigabytes in a single day**:


![codinghorror bandwidth usage, 2/24/2007 - 3/4/2007](https://blog.codinghorror.com/content/images/uploads/2007/03/6a0120a85dcdae970b0120a86d8357970b-pi.png)


That was enough to completely saturate two T1 lines – nearly 300 KB/sec – for most of the day. And that includes the time we disabled access to the site entirely in order to keep it from taking out the whole network.* After that, it was clear that something had to be done. **What can we do to reduce a website’s bandwidth usage?**


**1. Switch to an external image provider.**


Unless your website is an all-text affair, images will always consume the lion’s share of your outgoing bandwidth. Even on this site, which is extremely minimalistic, the size of the images dwarf the size of the text. Consider [my last blog post](https://blog.codinghorror.com/your-code-oop-or-poo/), which is fairly typical:

kg-card-begin: html


| Size of post text | ~4,900 bytes |
| Size of post image | ~46,300 bytes |
| Size of site images | ~4,600 bytes |


kg-card-end: html

The text only makes up about ten percent of the content for that post. To make a dent in our bandwidth problem, we must deal with the other ninety percent of the content – the images – first.


Ideally, we shouldn’t have to serve up any images at all: we can outsource the hosting of our images to an external website. There are a number of free or nearly-free image sharing sites on the net which make this a viable strategy:

- [Imageshack](http://www.imageshack.us/)
ImageShack offers free, unlimited storage, but has a 100 MB per hour bandwidth limit for each image. This sounds like a lot, but do the math: that’s 1.66 MB per minute, or about 28 KB per second. And the larger your image is, the faster you’ll burn through that meager allotment. But it’s incredibly easy to use – you don’t even have to sign up – and according to their [common questions page](https://imageshack.com/faq), anything goes as long as it’s not illegal.
- [Flickr](http://www.flickr.com/)
Flickr offers a free basic account with limited upload bandwidth and limited storage. Download bandwidth is unlimited. Upgrading to a paid Pro account for $25/year removes all upload and storage restrictions. However, Flickr’s [terms of use](http://www.flickr.com/terms.gne?legacy=1) warn that “professional or corporate uses of Flickr are prohibited,” and all external images require a link back to Flickr.
- [Photobucket](http://www.photobucket.com/)
Photobucket’s free account has a storage limit and a download bandwidth limit of 10 GB per month (that works out to a little over 14 MB per hour). Upgrading to a paid Pro account for $25/year removes the bandwidth limit. I couldn’t find any relevant restrictions in their terms of service.
- [Amazon S3](http://aws.amazon.com/s3)
Amazon’s S3 service allows you to direct-link files at a cost of 15 cents per GB of storage, and 20 cents per GB transfer. It’s unlikely that would add up to more than the ~ $2 / month that seems to be the going rate for the other unlimited bandwidth plans. It has worked well for at least one other site.


I like ImageShack a lot, but it’s unsuitable for any kind of load, due to the hard-coded bandwidth limit. Photobucket offers the most favorable terms, but Flickr has a better, more mature toolset. Unfortunately, I didn’t notice the terms of use restrictions at Flickr until I had already purchased a Pro account from them. So we’ll see how it goes. **Update:** it looks like Amazon S3 may be the best long-term choice, as many (if not all) of these photo sharing services are blocked in corporate firewalls.


Even though this ends up costing me $25/year, it’s still an incredible bargain. I am offloading 90% of my site’s bandwidth usage to an external host for [a measly 2 dollars](http://imdb.com/title/tt0088794/quotes) a month.


And as a nice ancillary benefit, I no longer need to [block image bandwidth theft with URL rewriting](https://blog.codinghorror.com/blocking-image-bandwidth-theft-with-url-rewriting/). Images are free and open to everyone, whether it’s abuse or not. This makes life much easier for legitimate users who want to view my content in the reader of their choice.


Also, don’t forget that [favicon.ico](http://en.wikipedia.org/wiki/Favicon) is an image, too. It’s retrieved more and more often by today’s readers and browsers. Make favicon.ico as small as possible, because it can have a [surprisingly large impact on your bandwidth](http://www.hanselman.com/blog/FavIconicoCanBeABandwidthHog.aspx).


**2. Turn on HTTP compression.**


Now that we’ve dealt with the image content, we can think about ways to save space on the remaining content – the text. This one’s a no-brainer. Enable HTTP compression on your webserver for roughly two-thirds reduction in text bandwidth. Let’s use my last post as an example again:

kg-card-begin: html


| Post size | 63,826 bytes |
| Post size with compression | 21,746 bytes |


kg-card-end: html

We get a 66% reduction in file size for every bit of text served up on our web site – including all the JavaScript, HTML, and CSS – by simply flipping a switch on our web server. The benefits of HTTP compression are so obvious it *hurts*. It’s reasonably straightforward to set up [in IIS 6.0](https://blog.codinghorror.com/http-compression-and-iis-6-0/) , and it’s extremely easy to set up [in Apache](http://httpd.apache.org/docs/2.0/mod/mod_deflate.html).


Never serve content that isn’t HTTP compressed. It’s as close as you’ll ever get to free bandwidth in this world. If you aren’t sure that HTTP compression is enabled on your website, use this [handy web-based HTTP compression tester](https://web.archive.org/web/20070308004133/http://www.port80software.com/products/httpzip/compresscheck), and *be* sure.


**3. Outsource Your RSS feeds.**


Many web sites offer RSS feeds of updated content that users can subscribe to (or “syndicate”) in RSS readers. Instead of visiting a website every day to see what has changed, RSS readers automatically pull down the latest RSS feed at regular intervals. Users are free to read your articles at their convenience, even offline. Sounds great, right?


It is great. Until you realize just how much bandwidth all that RSS feed polling is consuming. It’s staggering. Scott Hanselman told me that **half his bandwidth was going to RSS feeds**. And Rick Klau noted that 60% of his page views were RSS feed retrievals. The entire RSS ecosystem depends on properly coded RSS readers; a single badly-coded reader could pummel your feed, pulling uncompressed copies of your RSS feed down hourly – even when it hasn’t changed since the last retrieval. Now try to imagine *thousands* of poorly-coded RSS readers, all over the world. That’s pretty much where we are today.


Serving up endless streams of RSS feeds is something I’d just as soon outsource. That’s where [FeedBurner](http://www.feedburner.com/) comes in. Although I’ll gladly outsource image hosting for the various images I use to complement my writing, I’ve been hesitant to hand control for something as critical as my RSS feed to a completely external service. I emailed [Scott Hanselman](http://www.hanselman.com/blog/), who switched his site over to FeedBurner a while ago, to solicit his thoughts. He was gracious enough to call me on the phone and address my concerns, even walking me through FeedBurner using his login.


I’ve switched my feed over to FeedBurner as of 3pm today. The switch should be transparent to any readers, since I used some mod_rewrite [ISAPIRewrite](https://blog.codinghorror.com/url-rewriting-to-prevent-duplicate-urls/) rules to do a seamless, automatic permanent redirect from the old feed URL to [the new feed URL](http://feeds.feedburner.com/codinghorror/):

kg-card-begin: html

# do not redirect feedburner, but redirect everyone else
RewriteCond User-Agent: (?!FeedBurner).*
RewriteRule .*index.xml$|.*index.rdf$|.*atom.xml$
http://feeds.feedburner.com/codinghorror/ [I,RP,L]


kg-card-end: html
And the best part is that immediately after I made this change, I noticed a huge drop in per-second and per-minute bandwidth on the server. I suppose that’s not too surprising if you consider that the feedburner stats page for this feed are currently showing about **one RSS feed hit per second**. But even compressed, that’s still about 31 KB of RSS feed per second that my server no longer has to deal with.It’s a substantial savings, and FeedBurner brings lots of other abilities to the table beyond mere bandwidth savings.**4. Optimize the size of your JavaScript and CSS**The only thing left for us to do now is reduce the size of our text content, with a special emphasis on the elements that are common to every page on our website. CSS and JavaScript resources are a good place to start, but the same techniques can apply to your HTML as well.There’s a handy [online CSS compressor](http://www.cssdrive.com/index.php/main/csscompressor/) which offers three levels of CSS compression. I used it on the main [CSS file for this page](https://web.archive.org/web/20070316111007/http://www.codinghorror.com/blog/styles-site.css), with the following results:
kg-card-begin: html
original CSS size2,299 bytesafter removing whitespace1,758 bytesafter HTTP compression615 bytes
kg-card-end: html
We can do something similar to the JavaScript with this [online JavaScript compressor](https://web.archive.org/web/20070312180651/http://fmarcia.info/jsmin/test.html), based on Douglas Crockford’s [JSMin](http://javascript.crockford.com/jsmin.html). But before I put the JavaScript through the compressor, I went through and refactored it, using shorter variables and eliminating some redundant and obsolete code.
kg-card-begin: html
original JS size1232 bytesafter refactoring747 bytesafter removing whitespace558 bytesafter HTTP compression320 bytes
kg-card-end: html
It’s possible to use similar whitespace compressors [on your HTML](http://www.alentum.com/ahc/index.htm), but I don’t recommend it. I only saw reductions in size of about 10%, which wasn’t worth the hit to readability.Realistically, whitespace and linefeed removal is doing work that the compression would be doing for us. We’re just adding a dab of human-assisted efficiency:
kg-card-begin: html
RawCompressedUnoptimized CSS2,299 bytes671 bytesOptimized CSS1,758 bytes615 bytes
kg-card-end: html
It’s only about a 10 percent savings once you factor in HTTP compression. The tradeoff is that CSS or JavaScript lacking whitespace and linefeeds has to be pasted into an editor to be effectively edited. I use Visual Studio 2005, which automatically “rehydrates” the code with proper whitespace and linefeeds when I issue the autoformat command.Although this is definitely [a micro-optimization](https://blog.codinghorror.com/micro-optimization-and-meatballs/), I think it’s worthwhile since it reduces the payload of every single page on this website. But there’s a reason it’s the last item on the list, too. We’re just cleaning up a few last opportunities to squeeze every last byte over the wire.After implementing all these changes, I’m very happy with the results. I see a considerable improvement in bandwidth usage, and my page load times have never been snappier. But, these suggestions aren’t a panacea. **Even the most minimal, hyper-optimized compressed text content can saturate a 300 KB/sec link if the hits per second are coming fast enough.** Still, I’m hoping these changes will let my site weather the next Digg storm with a little more dignity than it did the last one – and avoid taking out the network in the process.*The ironic thing about this is that [the viral post in question](https://blog.codinghorror.com/why-cant-programmers-program/) was completely HTTP compressed text content *anyway*. So of all the suggestions above, only the RSS outsourcing would have helped.

[web development](https://blog.codinghorror.com/tag/web-development/)
[bandwidth optimization](https://blog.codinghorror.com/tag/bandwidth-optimization/)
[website performance](https://blog.codinghorror.com/tag/website-performance/)
[image optimization](https://blog.codinghorror.com/tag/image-optimization/)
[content delivery network](https://blog.codinghorror.com/tag/content-delivery-network/)
