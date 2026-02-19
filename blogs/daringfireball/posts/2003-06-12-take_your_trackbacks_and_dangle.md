---
title: "Take Your TrackBacks and Dangle"
date: 2003-06-12
url: https://daringfireball.net/2003/06/take_your_trackbacks_and_dangle
slug: take_your_trackbacks_and_dangle
word_count: 3182
---


One of [Movable Type](http://movabletype.org/)’s most distinguishing features is something called TrackBack. I don’t use it for Daring Fireball, nor do I plan to.


TrackBack is somewhat notoriously difficult to explain. Six Apart (the company behind Movable Type) has a [Beginner’s Guide to TrackBack](http://www.movabletype.org/trackback/beginners/) that runs seven printed pages (although it contains numerous screenshots), the opening paragraphs of which contain the best brief description I’ve seen:


> In a nutshell, TrackBack was designed to provide a method of notification
> 	between websites: it is a method of person A saying to person B,
> 	“This is something you may be interested in.” To do that, person A sends a *TrackBack ping* to person B.
> ***TrackBack ping:** a ping in this context means a small message sent from one webserver to another.*
> And why would person B be interested in what person A has to say?
> Person A has written a post on his own weblog that comments on a post in
> 	Person B’s weblog. This is a form of remote comments—rather than posting
> 	the comment directly on Person B’s weblog, Person A posts it on his own
> 	weblog, then sends a TrackBack ping to notify Person B.
> Person A has written a post on a topic that a group of people are interested
> 	in. This is a form of content aggregation—by sending a TrackBack ping to
> 	a central server, visitors can read all posts about that topic. For example,
> 	imagine a site which collects weblog posts about Justin Timberlake. Anyone
> 	interested in reading about JT could look at this site to keep updated on
> 	what other webloggers were saying about his new album, a photo shoot in a
> 	magazine, etc.


Six Apart’s goals for TrackBack are quite ambitious — read further in the Beginner’s Guide to see some of the more advanced uses for TrackBack they envision — but to date, most TrackBackers are using the protocol only for the first purpose listed above: a notification from A to B when A’s web site links to B’s.


The problems with TrackBack are manifold.


First and foremost is that TrackBack a two-way protocol. Both sides of the transaction, pinger and pingee, need to speak TrackBack for a ping to work. This is not so much of a problem if both web sites are running, say, Movable Type. But if the site you’re linking to doesn’t support TrackBack, you can’t send it a TrackBack ping. Nor are you going to get TrackBacks from sites that link to you, when those sites don’t support TrackBack.


That sounds terribly obvious — that only TrackBack-enabled sites are going to send or receive TrackBack pings — but the ramifications are unsettling. A list of TrackBack pings on your site is only going to reflect incoming links from other web sites running TrackBack software. *But most web sites don’t speak TrackBack.* This means a list of TrackBacks is only going to reflect links coming from the relatively small circle of web sites running TrackBack software.


No dispute, it’s useful and interesting to see a list of web sites linking to a particular article or web site. But it makes no sense to limit such a list to a small subset of the web. Nor is it fair to expect all web sites to adopt the TrackBack protocol.


It’s important to note that TrackBack is most definitely not proprietary to Movable Type. Yes, Six Apart invented the protocol, and yes, most TrackBack-using sites are running Movable Type. But Six Apart has published an open [technical specification](http://www.movabletype.org/docs/mttrackback.html) to encourage other developers to support the protocol. They’ve also released a [standalone TrackBack CGI tool](http://www.movabletype.org/docs/tb-standalone.html), under the open source Artistic License, for use in non-Movable Type web sites that want to use TrackBack.


That’s all admirable, and so under no circumstances should my criticism of the TrackBack *protocol* be interpreted as criticism of Six Apart’s *intentions* for creating TrackBack in the first place.


But regardless if it’s an open protocol, you can’t expect all web sites to adopt TrackBack. Sending TrackBack pings is one thing — any machine connected to the Internet is ostensibly capable of that. The bigger problem is with *receiving* pings. You need software on a public web server to receive pings, which is a high and unfair barrier to entry.


Many web sites — especially personal web sites — are simply collections of static HTML files. You create a web page on your computer, you transfer it to your server. Now you have a web site. The entire reason the web took off so quickly, and has continued to grow, is that it’s really quite easy to create your own web site. If you can create HTML files, and you have access to a web server, you can make a web site.


And it’s not just [HTML-hand-coders](http://www.zeldman.com/daily/0403a.shtml#unsyndicate) and nerds who have [written](http://www.textism.com/article/661/) [their](http://www.hivelogic.com/298.html) [own](http://tbray.org/ongoing/When/200x/2003/04/20/XLamp) [weblog](http://www.rc3.org/cgi-bin/less.pl?arg=5150) software who aren’t included in the TrackBack game. Many web site publishing systems don’t involve software that runs on your server. [Radio UserLand](http://radio.userland.com/), for example, runs on your desktop. It’s actually a web server, but it runs on your machine, and then uses FTP to push your weblog files to the web as static HTML files. This means to receive TrackBack pings, your desktop computer would need to be publicly accessible over the Internet, 24 hours a day. Not only is this unlikely, it’s ill-advised. If you’re on dial-up, you’re not going to be connected 24 hours a day. And even if you have a broadband connection, you probably don’t have a static IP address, and there’s a good chance you’re behind a firewall of some sort. (UserLand is implementing TrackBack, but as noted in [Dave Winer’s TrackBack developer notes](http://backend.userland.com/trackback), it’s send-only for now. This is like being able to send birthday presents to others, but not receive any yourself.)


And then there’s Pyra’s [Blogger](http://www.blogger.com/), which powers thousands of weblogs, but which doesn’t support TrackBack. Blogger’s software doesn’t run on your desktop, but it doesn’t run on your server, either. It runs on *Pyra’s* servers, and they simply push static HTML files to your server via FTP.


Blogger sometimes gets a bad rap because it’s so constraining (and because of numerous problems with availability of the service — but I expect these reliability problems will decrease significantly as time goes on now that Pyra has been purchased by Google). But what Blogger gets right is that it’s so damn easy to get started with.


## Refer Madness


And so while Six Apart calls TrackBack a *notification* protocol, the way people really use it is as a *connection* protocol. Person A sends a TrackBack ping to B to say that a post on A’s web site is related to a post on B’s web site. Assuming B does something with this TrackBack info, there is now a connection between A and B. But there already exists a mechanism for establishing connections between web sites: links. And there are ways to track links that are much simpler than TrackBack.


Referrers, for one. When you follow a link from one web page to another, your browser includes *referrer* information in the HTTP headers of the request. The referrer should be the URL of the page from which you came; if you click on any of the links in this article, for example, the web site you’re heading to will get a referrer from this page at daringfireball.net.


Referrers are typically included in the log files generated by web servers. You can use these logs to track your referrers. Referrers are also available live, as each request comes in, accessible via scripting languages like PHP. (Other information is included in these HTTP headers, including which browser you’re using [a.k.a. your “user agent”], which is how sites can serve different content to users of different browsers.)


So, for example, you could write a PHP script to log each incoming referrer in a database (perhaps MySQL, since it is very fast, freely available, and works well with PHP). Then you could do something useful with that database, such as generate a table of your most frequent referrers. Or you could get specific, and produce separate tables for each article on your site, showing only the referrers pointing to each article.


And this is in fact what is going on with the new Referrers feature here at Daring Fireball. There is now a link in the sidebar to the [Referrers](https://daringfireball.net/referrers/) page, which lists every referrer to this site in the last 24 hours, sorted by frequency. And at the bottom of each individual article page is a list of referrers pointing to that article, going back 45 days.


(This list is quite long for some articles, which in turn might waste a sheet or two of paper when printing. Not to worry — thanks to a newly-added print media CSS style sheet, the referrers listing isn’t displayed in printed output. The print media style sheet should also fix the problem where [certain browsers](http://www.apple.com/safari/) would try to print Daring Fireball as it looks on screen: white text on a dark background. All browsers should now print pages from this site as black text with no background color. My apologies for any previously wasted ink.)


Referrer tracking is neither a new nor original idea. It is a built-in feature for web sites powered by UserLand’s [Manila](http://manila.userland.com/), e.g. [Matthew Thomas](http://mpt.phrasewise.com/stats/referers), [Dave Winer](http://scriptingnews.userland.com/stats/referers). But it’s cool, because if I want to display referrers to my site, no one who links to me has to do *any* extra work. The referrer info is right there in the HTTP header of every incoming request — every site is included, no special software required.


## Linking Should Be Enough


Which brings me to my main point: TrackBack is unnecessary as a connector between web sites. We already have something to connect web sites: the link. 
When links are followed, we can track referrers. But even before links are followed, it is possible to analyze and track links between web pages, by examining the pages’ source code and extracting the links.


So you could, in theory, write software to examine the source code of a few hundred thousand weblogs, and create a database of the links between these weblogs. If your software was clever enough, it could refresh its information every few hours, adding new links to the database nearly in real time.


This is, in fact, exactly what Dave Sifry has created with his amazing [Technorati](http://www.technorati.com/).
At this writing, Technorati is watching over 375,000 weblogs, and has tracked over 38 *million* links. If you haven’t played with Technorati, you’re missing out. For example, here is [Technorati’s “Link Cosmos” for Daring Fireball](http://www.technorati.com/cosmos/links.html?rank=&url=daringfireball.net&sub=Get+Link+Cosmos) — a frequently-updated list of sites that are linking here.


One advantage TrackBacks have over referrers is that TrackBacks contain more information, most especially a blurb of text. TrackBacks are like comments, in this way — they contain not only the URL of the web site sending the TrackBack, but also a small amount of text. But Technorati’s Link Cosmos offers blurbs of text as well — a small amount of text before and after the link in the article, which is usually enough to provide some useful context.


And so if the problem is that referrers alone do not provide enough useful information, Technorati is on the right track to a better solution. Not only is the Technorati web site available free of charge, but Mr. Sifry has also recently debuted a [programming API](http://developers.technorati.com/) that offers access to the same results the web site displays. Thus instead of sending you to the Technorati web site to see Daring Fireball’s link cosmos, I could display them right here on my own web site.


The key to understanding why Technorati is so damn cool is that all you need to do to get tracked is link. Just make a regular old link in a web page, like this: `<a href="http://www.technorati.com/">`. *That’s it.* There is no new protocol. No new software to run, either on your desktop computer or your server. Tracking your Technorati Link Cosmos is even less work than tracking your referrers.


All you need to do is link. Technorati does the rest.


And therein lies the weakness in the system, of course. Unlike a decentralized protocol like TrackBack, Technorati is utterly centralized; if Mr. Sifry decides to abandon the project, for whatever reason, where will we be? Well, we’ll be screwed. At least until someone else builds a similar system, which probably wouldn’t take long, given the highly addictive nature of Technorati. (It also strikes me as highly unlikely that Mr. Sifry will abandon the project, but people do get hit by buses. One takes one’s chances.)


## Miscellaneous Other Things I Don’t Like About TrackBack

- **It’s a pain in the ass to send TrackBacks.**


Movable Type ships with a bookmarklet (a small JavaScript applet that you can run from your web browser toolbar) the purpose of which is to make it easy to send a TrackBack to a particular article. But this only works if (1) you write your weblog posts using forms in a web browser, instead of a desktop client such as [Kung-Log](http://www.kung-foo.tv/kunglog.php) or [NetNewsWire](http://ranchero.com/netnewswire/); (2) you only want to send one TrackBack to one article — the bookmarklet doesn’t help if you want to send TrackBack pings to multiple web sites. The alternative to using the bookmarklet is to find and copy individual TrackBack URLs for every article you wish to ping. In contrast, referrer-tracking and Technorati don’t require any extra work at all.
- **Auto-discovery of TrackBack URLs depends on cryptic snippets of RDF.**


“Auto-discovery” is what makes the TrackBack bookmarklet work. Everyone agrees that entering TrackBack URLs by hand is a pain in the ass, so auto-discovery is a way for software to sniff out these TrackBack URLs for you. The way this is done is via small snippets of [RDF](http://www.xml.com/pub/a/2001/01/24/rdf.html), an XML format for describing online resources.


Example syntax, from Movable Type’s TrackBack sub-weblog:

`
<!--
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:trackback="http://madskills.com/public/xml/rss/module/trackback/"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
<rdf:Description
    rdf:about="http://www.movabletype.org/trackback/archives/000833.html"
    trackback:ping="http://www.movabletype.org/mt/trackback/57"
    dc:title="TrackBack in the Userland environment"
    dc:identifier="http://www.movabletype.org/trackback/archives/000833.html"
    dc:subject="TrackBack"
    dc:description="Dave Winer has put up a new document-in-progress called
    Trackback in the UserLand environment, which covers his work in implementing..."
    dc:creator="Anil"
    dc:date="2003-04-27T13:46:33-08:00" />
</rdf:RDF>
-->
`

Perhaps “cryptic” is too harsh a description, but RDF certainly isn’t the type of thing that one could be expected to generate by hand — and I feel strongly that web sites should be producible in a hand-editable format.
- **TrackBack doesn’t work well with static web pages.**


Static web pages are simply HTML documents that reside on a web server. Dynamic web pages, on the other hand, are generated on-the-fly by the web server. (See “[Bake, Don’t Fry](http://www.aaronsw.com/weblog/000404)”, by Aaron Swartz, for more on this distinction.)


Movable Type generates static web pages, by default. This is a good thing, in my opinion — but it means that Movable Type itself is not a good system for displaying TrackBack information. What happens is that Movable Type builds static web pages when you save an article. But then what if you receive a few TrackBacks — how are these TrackBacks displayed if the web pages are already built?


One solution would be to rebuild your web pages every time you receive a TrackBack. But this could take quite a bit of time, and would open your weblog to abuse by TrackBack-sending bastards. So what most TrackBack-using Movable Type users do is display TrackBacks in pop-up windows, the contents of which are generated dynamically by a CGI program, while leaving their actual weblog posts statically rendered.


Pop-up windows suck. (This same argument applies to Movable Type’s Comment feature.)


There are other ways around this, but they involve using PHP or other scripting languages to query your TrackBack database with each page request. Movable Type does not do this for you — you need to implement such integration yourself.


## Preemptive Responses to Certain Anticipated Pro-TrackBack Rebuttals


***You just don’t get it, Gruber. TrackBack is so much more than just a way to see who is linking to you.
***


Fine. Maybe I don’t get it. But I don’t see anyone using TrackBack for anything other than tracking links to their articles.


***TrackBack is not hard to implement.***


Yes it is. It’s not hard compared to, say, nuclear physics, but it is hard compared to making a plain old HTML web page.


***Referrers are ripe for abuse by spammers.***


True, as evident by some of the [referrers listed at Scripting News](http://scriptingnews.userland.com/stats/referers). But [TrackBack isn’t immune from abuse by spammers either](http://philringnalda.com/blog/2003/02/a_trackback_is_a_comment_except_when_its_spam.php), and might be a more appealing target because it allows for more information than just a URL to be displayed.


***OK, asshat. How can you advocate referrer-tracking over TrackBack, when you admit that the TrackBack protocol is much richer than referrers? The advantages you cite for referrer-tracking boil down to a lowest-common-denominator argument; i.e. you’re arguing that referrer-tracking is better than TrackBack because it includes web sites constructed using less sophisticated software. Thus couldn’t this same argument be used to say that everyone should use Wintel computers instead of Macs?***


The analogy doesn’t hold. Certainly the ubiquitous lowest-common-denominator status of Windows holds numerous advantages, not just for Microsoft and Intel, but also for users. But when someone decides to use a Mac instead of PC, because for him the Mac’s usability advantages outweigh the PC’s monopoly advantages, it is no skin off the backs of the PC majority. Whereas if you decide to display TrackBacks on your web site instead of referrers, you are excluding all of the people who aren’t able or willing to use TrackBack for their web sites.


For communication protocols and web standards, lowest-common-denominator status is generally a good thing. The opposite is true for desktop software and hardware.


## Give It Up


Several people deserve special thanks for the referrer system now in place here at Daring Fireball.


First and foremost, Dan Benjamin, who offered an enormous amount of help with the SQL. Actually, he pretty much did all the SQL work, and then explained it to me in explicit detail. He spent more time explaining it to me than he did writing the code in the first place. Dan Benjamin is [an absolute genius](http://www.hivelogic.com/310.html), indeed.


Second, Brent Simmons and Dean Allen, both of whom offer open source PHP/MySQL referrer-tracking packages. I used code from neither, but was inspired by both. [Brent’s system](http://ranchero.com/php/rollingreferers/) is more or less a clone of Manila’s (which he admits was his goal), [showing](http://ranchero.com/stats/referers.php) only referrers and a count; no target information is tracked. Dean’s [Refer](http://www.textism.com/tools/refer/) system, recently updated to version 2.0, is more chronologically-oriented, [showing](http://textism.com/refer/) the most recent 50 referrers, rather than showing referrers over a larger period of time sorted by frequency. Dean’s SQL was utterly beyond my comprehension, but his table layout was exquisite, and so I cribbed it.


Some day in the future, I may release the source code to my system. But that day is not today.



| **Previous:** | [Noted](https://daringfireball.net/2003/06/noted) |
| **Next:** | [TrackBack Addenda](https://daringfireball.net/2003/06/trackback_addenda) |


PreviousNext