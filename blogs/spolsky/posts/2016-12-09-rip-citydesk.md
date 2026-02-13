---
title: "RIP CityDesk"
date: 2016-12-09
url: https://www.joelonsoftware.com/2016/12/09/rip-citydesk/
word_count: 572
---


Here’s a quick history of the technology behind Joel on Software.


Version one was on Manila, created by [Dave Winer](http://scripting.com/). Dave was the one who convinced me to blog, by blogging himself, and by creating what was, I think, the first public blogging platform at editthispage.com. My site was joel.editthispage.com and back in 1999 people thought it was pretty spiffy that you could get your own subdomain like that.


In order to use my own domain, I registered joelonsoftware.com and took an old IBM desktop computer (probably running Windows NT 4.0), shoved it in a closet, and [ran my own copy of Manila](https://www.joelonsoftware.com/2001/06/14/20010614/). The first time Slashdot linked to me it melted down. We upgraded the memory from 256M to 512M and it recovered.


In those days all the cool kids wrote their own blogging platforms. I wrote [CityDesk](https://www.joelonsoftware.com/2001/10/12/what-does-citydesk-do/). In what turned out to be a monumentally wrong bet, I thought that people would want to blog on Windows, with all the slick WYSIWYG editing goodness that wasn’t yet available in early versions of HTML. CityDesk kept your entire website in a SQL database (Microsoft Jet, the backend of Access) and had a frontend like a word processor. Every time you needed to publish, it generated the entire site as a set of html pages, which it then uploaded to an ftp server for you. That worked “OK” for 10 pages. By the time this site was over 1000 pages, even on modern super speedy computers with flash drives, it took something like 5 minutes to publish.


Over the years the CityDesk code base (VB 6.0, another bad bet) stopped running on the latest versions of Windows. Nobody else cared but by that time I was using a custom version of CityDesk which only ran on Windows XP. So until recently, I had a virtual machine set up with Windows XP running in there, and a copy of CityDesk. That virtual machine runs on a modern Windows box which I don’t use for any other purpose, so it lives under a desk in a cave somewhere and I have to remote desktop into it. Lately, I haven’t been able to do that. I’m not sure why.


Doesn’t matter. [Matt Mullenweg](https://ma.tt/) over at WordPress has been trying to get me to move Joel on Software over to WordPress for so long it’s not even funny. I finally gave in. An astonishingly talented group of people were collected who created the port you are looking at now. I owe a huge debt of gratitude to [Chris Hardie](https://chrishardie.com/), [Sarah Semark](http://triggersandsparks.com/), [Valerie Kalantyrski](http://tilesandthesea.com/), [Michelle Langston](http://planewhimsy.com/), [Daniel Robert](http://danielwrobert.com/), [James Tien](https://softmanjournal.wordpress.com/), and

[Steve Seear](http://steveseear.org) for weeks of hard work on creating this almost perfect port of 16 years of cruft, preserving over 1000 links with redirects, hand crafting html and css to preserve awful formatting, some of which was created before CSS was in use, and doing some monumental heroics to keep just about everything about the old site in its new WordPress home.


I also want to thank our host [Pressable](http://pressable.com/).


OK, I haven’t blogged too much since getting a puppy and [“officially” retiring on the tenth anniversary of Joel on Software](https://www.joelonsoftware.com/2010/03/14/puppy/). I won’t have too much time to blog now, either, but now that we’re on WordPress, it’s a million times easier, so I’ll probably throw up some things here that I’ve written anyway, like internal documents from Fog Creek and Stack Overflow.


See you soon!
