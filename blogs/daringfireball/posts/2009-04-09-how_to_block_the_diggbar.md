---
title: "How to Block the DiggBar"
date: 2009-04-09
url: https://daringfireball.net/2009/04/how_to_block_the_diggbar
slug: how_to_block_the_diggbar
word_count: 583
---


Last week Digg released something they call the DiggBar, which serves as both a new interface for Digg and doubles as a URL shortening service. The way it works is that you just add “digg.com/” at the *beginning* of any URL, and Digg creates a short URL in the form of *digg.com/1234*. Here’s an example DiggBar URL that points to google.com: [http://digg.com/d1nYVs](http://digg.com/d1nYVs). Further, the Digg homepage now links to these DiggBar URLs rather than linking directly to other web sites.


But unlike normal URL shortening services, when you load these Digg URLs, rather than redirect you to the original URL, Digg loads a page which *frames* the content of the original site. As a user, what you see is that the URL in your browser’s location field remains *digg.com/1234*, and the content of the destination site loads underneath a Digg-branded toolbar.


This, of course, is total bullshit.


All sorts of sites tried this sort of trickery back in the mid-’90s when Netscape Navigator 2.0 added support for the `<frameset>` tag. It did not take long for a broad consensus to develop that framing someone else’s site was wrong. URLs are the building block of the Web. They tell the user *where* they are. They give you something to bookmark to go back or to share with others.


The DiggBar breaks that, and I’ve seen no argument that makes it any more sense to support this than it does to support 1996-style `<frameset>` site embedding.


So, shortly after it was announced, I wrote code to block it from Daring Fireball. If you attempt to view most pages on DF through the DiggBar, [you’ll be greeted](http://digg.com/u1dQ6) with a special message just for Digg instead of the regular content of the page. Digg sends a tremendous amount of traffic to sites that make it to the top of their front page, but it’s the worst kind of traffic: mindless, borderline illiterates. Good riddance, really.


---


A lot of people have asked, so I figured I should explain how I’m doing it. The basic idea is that when a web page is loaded inside a frame, its [HTTP referrer](http://en.wikipedia.org/wiki/HTTP_referrer) is set to that of the parent (i.e. framing) page. In the normal, non-framing context, the referrer tells the address of the page from which the current page being requested was linked to.


Most pages on DF are served through PHP, so I added a short bit of PHP near the top that looks like this:


```
<?php
if (preg_match('#http://digg.com/\w{1,8}/*(\?.*)?$#',
                            $_SERVER['HTTP_REFERER']) ) {
    echo "<p>Special message for Digg users here.</p>";
    exit;
}
?>

```


The first line uses a regular expression to check if the HTTP referrer looks like a DiggBar URL, which, for my purposes, I’ve defined as “digg.com/” followed by exactly 1-8 letters or numbers and an optional trailing slash. It doesn’t attempt to block *all* referring URLs from Digg, just those that look like DiggBar pages. If the pattern matches, it prints a special message for Digg users and calls PHP’s standard `exit` function, which stops the rest of the page from being transmitted.


[**Update:** I’ve tweaked the regex pattern a bit so that it also matches DiggBar URLs with a trailing “/” and/or “?”.]


Some sites [use JavaScript](http://en.wikipedia.org/wiki/Framekiller) to completely block framing; I don’t want to do that, and, given DF’s configuration, it was easier for me to use PHP to target Digg specifically.



| **Previous:** | [New Daring Fireball T-Shirts](https://daringfireball.net/2009/04/new_df_tshirts) |
| **Next:** | [Twitter Clients Are a UI Design Playground](https://daringfireball.net/2009/04/twitter_clients_playground) |


PreviousNext