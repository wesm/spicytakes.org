---
title: "URL Rewriting to Prevent Duplicate URLs"
date: 2007-02-21
url: https://blog.codinghorror.com/url-rewriting-to-prevent-duplicate-urls/
slug: url-rewriting-to-prevent-duplicate-urls
word_count: 775
---

As a software developer, you may be familiar with [the DRY principle](http://www.artima.com/intv/dry.html): don’t repeat yourself. It’s absolute bedrock in software engineering, and it’s covered beautifully in [The Pragmatic Programmer](http://www.amazon.com/exec/obidos/ASIN/020161622X), and even more succinctly in [this brief IEEE software article](https://web.archive.org/web/20070224203931/http://www.pragmaticprogrammer.com/articles/may_04_oo1.pdf) (pdf). If you haven’t committed this to heart by now, go read these links first. We’ll wait.


Scott Hanselman recently [found out the hard way](http://www.hanselman.com/blog/GooglePageRanksConsideredSubtle.aspx) that the DRY principle also applies to URLs. Consider the multiple ways you could get to this very page:

- http://codinghorror.com/blog/
- http://www.codinghorror.com/blog/
- http://www.codinghorror.com/blog/index.htm


It’s even more problematic for Scott because he has two different domain names that reference the same content.


Having multiple URLs reference the same content is undesirable not only from a sanity check DRY perspective, but also because **it lowers your PageRank. **[PageRank](http://en.wikipedia.org/wiki/PageRank) is calculated per-URL. If 50% of your incoming backlinks use one URL, and 50% use a different URL, you aren’t getting the full PageRank benefit of those backlinks. The link juice is watered down and divvied up between the two different URLs instead of being concentrated into *one* of them.


So the moral of this story, if there is one, is to **keep your URLs simple and standard**. This is something the REST crowd has been [preaching for years](https://web.archive.org/web/20070224115015/http://www.megginson.com/blogs/quoderat/2007/02/15/rest-the-quick-pitch/). You can’t knock simplicity. Well, you [can](http://patricklogan.blogspot.com/2006/02/rest-and-soap.html), but you’ll be [crushed by simplicity’s overwhelming popularity](https://web.archive.org/web/20070227203449/http://google-code-updates.blogspot.com/2006/12/beyond-soap-search-api.html) eventually, so why fight it?


Normalizing your URLs isn’t difficult if you take advantage of [URL Rewriting](http://en.wikipedia.org/wiki/Rewrite_engine). URL Rewriting has been a [de-facto standard on Apache](http://httpd.apache.org/docs/2.0/misc/rewriteguide.html) for years, but has yet to reach mainstream acceptance in Microsoft’s IIS. I’m not even sure if [IIS 7](http://www.iis.net/default.aspx?tabid=7) supports URL Rewriting out of the box, although its new, highly modular architecture would make it [very easy to add support](https://web.archive.org/web/20070704124339/http://pietschsoft.com/Blog/Post.aspx?PostID=1312). It’s critical that Microsoft get a good reference implementation of an IIS7 URL rewriter out there, preferably one that’s compatible with the vast, existing [library of mod_rewrite rules](https://web.archive.org/web/20070225150731/http://www.myhtaccess.com/).


But that doesn’t help us today. If you’re using IIS today, you have two good options for URL rewriting; they’re both installable as [ISAPI filters](https://web.archive.org/web/20070307083652/http://www.iis-resources.com/modules/wfsection/article.php?articleid=9). I’ll show samples for both, using a few common URL rewriting rules that I personally use on my website.


The first is [ISAPI Rewrite](http://www.isapirewrite.com/). ISAPI Rewrite isn’t quite free, but it’s reasonably priced, and most importantly, it’s **nearly identical in syntax to the Apache mod_rewrite standard**. It’s also quite mature, as it’s been through quite a few revisions by now.

kg-card-begin: html

[ISAPI_Rewrite]
# fix missing slash on folders
# note, this assumes we have no folders with periods!
RewriteCond Host: (.*)
RewriteRule ([^.?]+[^.?/]) http://$1$2/ [RP]
# remove index pages from URLs
RewriteRule (.*)/default.htm$ $1/ [I,RP]
RewriteRule (.*)/default.aspx$ $1/ [I,RP]
RewriteRule (.*)/index.htm$ $1/ [I,RP]
RewriteRule (.*)/index.html$ $1/ [I,RP]
# force proper www. prefix on all requests
RewriteCond %HTTP_HOST ^test.com [I]
RewriteRule ^/(.*) http://www.test.com/$1 [RP]
# only allow whitelisted referers to hotlink images
RewriteCond Referer: (?!http://(?:www.good.com|www.better.com)).+
RewriteRule .*.(?:gif|jpg|jpeg|png) /images/block.jpg [I,O]


kg-card-end: html
The second option, [Ionic’s ISAPI Rewrite Filter](https://web.archive.org/web/20070225134755/http://cheeso.members.winisp.net/IIRF.aspx), is completely free. This filter has improved considerably since the last time I looked at it, and it appears to be a viable choice now. However, it uses its own rewrite syntax that is *similar* to the Apache mod_rewrite standard, but different enough to require some rework.
kg-card-begin: html


# fix missing slash on folders
# note, this assumes we have no folders with periods!
RewriteRule (^[^.]+[^/]$) $1/ [I,RP]
# remove index pages from URLs
RewriteRule  (.*)/default.htm$ $1/ [I,RP]
RewriteRule  (.*)/default.aspx$ $1/ [I,RP]
RewriteRule  (.*)/index.htm$ $1/ [I,RP]
RewriteRule  (.*)/index.html$ $1/ [I,RP]
# force proper www. prefix on all requests
RewriteCond %{HTTP_HOST} ^test.com [I]
RewriteRule ^/(.*) http://www.test.com/$1 [I,RP]
# only allow whitelisted referers to hotlink images
RewriteCond %{HTTP_REFERER} ^(?!HTTP_REFERER)
RewriteCond %{HTTP_REFERER} ^(?!http://www.good.com) [I]
RewriteCond %{HTTP_REFERER} ^(?!http://www.better.com) [I]
RewriteRule .(?:gif|jpg|jpeg|png)$ /images/block.jpg [I,L]


kg-card-end: html
The Ionic filter still has some quirks, but I loved its default logging capability. I could tell exactly what was happening with my rules, blow by blow, with a quick glance at the log file. However, I had a lot of difficulty getting the Ionic filter to install – I could only get it to work in IIS 5.0 isolation mode, no matter what I tried. Clearly a work in progress, but a very promising one.Of course, the few rewrite rules I presented above – URL normalization and [image hotlink prevention](https://blog.codinghorror.com/blocking-image-bandwidth-theft-with-url-rewriting/) – are merely the tip of the iceberg.They don’t call it the Swiss Army Knife of URL Manipulation for nothing. **URL rewriting should be an integral part of every web developer’s toolkit.** It’ll increase your DRYness, it’ll increase your PageRank, and it’s also central to [the concept of REST](https://web.archive.org/web/20070224115015/http://www.megginson.com/blogs/quoderat/2007/02/15/rest-the-quick-pitch/).

[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[seo optimization](https://blog.codinghorror.com/tag/seo-optimization/)
[url rewriting](https://blog.codinghorror.com/tag/url-rewriting/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[duplicate content](https://blog.codinghorror.com/tag/duplicate-content/)
