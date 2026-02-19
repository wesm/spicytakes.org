---
title: "TrackBack Addenda"
date: 2003-06-13
url: https://daringfireball.net/2003/06/trackback_addenda
slug: trackback_addenda
word_count: 1018
---


Clarifications, corrections, and notes regarding yesterday’s little [blurb on TrackBack](http://daringfireball.net/2003/06/take_your_trackbacks_and_dangle.html).


## So Am I Saying TrackBack Totally Sucks?


No. Not my point at all. Where I went wrong was in writing:


> The problems with TrackBack are manifold.


What I should have written instead is:


> The problems with using TrackBack for link tracking are manifold.


My criticism isn’t with the TrackBack protocol, but rather with using the TrackBack protocol for the purpose of keeping track of what other web sites are linking to yours. This is an important distinction, and while it’s the point I intended to make all along, it wasn’t entirely clear. The confusion is compounded, however, by the fact that many people think TrackBack is *only* for link tracking, which is an easy mistake to make, since it’s the only thing most people use it for.


Anil Dash, the senior-ranking non-Trott at Six Apart, understood. In his [Daily Links sub-blog](http://dashes.com/links/), he was nice enough to describe my article as “an excellent criticism of TrackBack”, but in the title attribute of the anchor tag, commented, “the biggest problem is that people confuse one use of the protocol for its entire realm of possibility. we’re working on fixing it.”


## Posts as Units of Measure


One of the main appeals of TrackBack is that it uses individual posts as its unit of measure. As opposed to, say, individual pages, or individual URLs. That’s a useful distinction. For example, here on Daring Fireball, the five most recent articles are displayed on the front page of the site — but their permanent homes are on individual archive pages. When you’re tracking referrers from here, you might see readers coming from `http://daringfireball.net/` and `http://daringfireball.net/2003/06/take_your_trackbacks_and_dangle.html`, but in fact, they’re coming from the same article. Numerous readers also pointed out that raw referrer-tracking makes no distinction between different URLs that point to a single resource, such as `daringfireball.net` and `www.daringfireball.net`.


TrackBack doesn’t suffer from this, because it uses the canonical permanent link as the URL for a post. (That still doesn’t make it an appropriate protocol for link tracking.)


## And So What Is TrackBack Good For?


Numerous people pointed to [Matt Haughey’s very nifty use of TrackBack](http://a.wholelottanothing.org/archives.blah/006625): he’s configured WinAmp to send his web site a TrackBack ping each time a new song starts playing. These TrackBacks constitute the “Now Playing” list in his sidebar. [Jerry Kindall](http://www.jerrykindall.com/) pitched in with an [AppleScript solution to do the same thing from iTunes](http://a.wholelottanothing.org/archives.blah/006627).


So there’s TrackBack being used for something very cool, but also totally unrelated to link tracking. [Paul Bausch’s response](http://www.onfocus.com/comments.asp?id=3218) to my article (and ensuing comment thread) contains numerous other examples of other uses for TrackBack, none of which offend my delicate sensibilities in the slightest.


## That Complexity Thing


A number of people complained, both via email and in their own weblogs, that it struck them as incongruous that I was both (a) criticizing TrackBack for being too complex; and (b) advocating a hand-rolled referrer-tracking solution involving PHP and MySQL. [E.g. Phillip Winn.](http://w6daily.winn.com/001456.html)


While I don’t know that I made it clearly, my point wasn’t that everyone should learn PHP and MySQL and write their own referrers system. My point was merely to show that if you simply want to track who is linking to your web site, referrer tracking is a better indication than TrackBack, because it includes everyone. Most people running TrackBack didn’t write their own TrackBack code — there’s no reason people should need to write their own referrer-tracking code either. It would make for a nice built-in feature for weblog systems.


## TrackBacks as Comments


Another common criticism is that I shouldn’t have compared TrackBacks to referrers, but rather to comments. *It’s not just a link — it’s a link and comment!* And indeed, many weblogs display comments and TrackBacks intermingled with each other.


But while TrackBack pings *do* contain a blurb of text, in practice, they usually make for poor comments, mainly because the blurb of text that’s sent from Movable Type is the article’s *excerpt*. The excerpt, in Movable Type, is an article attribute wherein the author can write a brief synopsis of the entire article. If left blank, the excerpt defaults to the first 20 words of the article. (This is all specific to Movable Type, but that’s what the vast majority of TrackBack users are powering their weblogs with.)


The problem is that Movable Type uses the excerpt field for several purposes. E.g. it’s also used in excerpted RSS feeds, like [mine](http://daringfireball.net/index.xml). So in an RSS feed, your excerpts are telling your subscribers what each article is about. Similarly, you could use the excerpts as synopses in a list of archived articles.


That’s a very different purpose than a comment on someone else’s weblog. It’s hard to write a single blurb that is appropriate in both contexts, and most people don’t even seem to try.


Imagine if I had both comments and TrackBacks enabled for Daring Fireball. The regular comments for yesterday’s article might look something like this:


```

    I think you're right, TrackBack stinks.
    - John Doe  [12 June 2003 1:15pm]
    

    You have some good points, but you underestimate
    how powerful TrackBacks can be. Very few people
    are currently taking advantage of everything
    TrackBack can do. For example, Matt Haughey is
    using TrackBack to update a "currently playing"
    list of music on his web site:
    http://a.wholelottanothing.org/archives.blah/006627
    - Jane Smith  [12 June 2003 1:24pm]
    

    You're a jagoff. Referrers are crap.
    - Anonymous  [12 June 2003 1:35pm]

```


But the “TrackBack comments” would tend to read like this:


```

    John Gruber writes about the problems with TrackBack.
    - Hugh Jass  blog.example.com/article/213
    

    Daring Fireball takes on TrackBack.
    - Anita Bath  weblog.weblog.web/archives/000123.html
    

    John Gruber compares TrackBack versus referrer-
    tracking and Technorati's Link Cosmos. Interesting.
    - Seymour Butz  whatever.example.com/blah.html

```


TrackBacks intermingled with actual comments tend to read like non sequiturs. Whereas the genuine comments are (hopefully) following a thread, the TrackBacks seemingly come out of nowhere. Example A: the comment thread for Mark Pilgrim’s “[How to Consume RSS Safely](http://diveintomark.org/archives/2003/06/12/how_to_consume_rss_safely.html#comments)”.



| **Previous:** | [Take Your TrackBacks and Dangle](https://daringfireball.net/2003/06/take_your_trackbacks_and_dangle) |
| **Next:** | [Internet Explorer](https://daringfireball.net/2003/06/internet_explorer) |


PreviousNext