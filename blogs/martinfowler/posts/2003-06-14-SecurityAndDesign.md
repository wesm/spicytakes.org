---
title: "Security And Design"
description: "This last week I had the pleasure of wandering around Florida speaking with Dan Sandlin and David LeBlanc at a series of Microsoft architecture councils. For those who don't know David LeBlanc wrote t"
date: 2003-06-14T00:00:00
tags: ["team organization", "security"]
url: https://martinfowler.com/bliki/SecurityAndDesign.html
slug: SecurityAndDesign
word_count: 245
---


This last week I had the pleasure of wandering around Florida
speaking with Dan Sandlin and David LeBlanc at a series of Microsoft
architecture councils. For those who don't know David LeBlanc
wrote the very popular book [Writing Secure
Code](https://www.amazon.com/gp/product/0735617228/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0735617228&linkCode=as2&tag=martinfowlerc-20) with Michael Howard. At each of the session I would do a
talk / q&a on [P of
EAA](https://martinfowler.com/books/eaa.html) (which got a JavaWorld [award](http://www.javaworld.com/javaworld/jw-06-2003/jw-0609-eca-p3.html) this week) and David would follow on security.


One thing that interested me was that several people found the
	combination odd - implying that few people would be interesting in
	two such diverse topics. I think this is at the heart of problems
	about security in the industry. Security is seen as some separate
	topic area which sits in its silo. Yet security isn't something you
	can just add to an application by putting in a few encapsulated
	classes here and there. Security thinking should pervade a whole
	team - particularly on applications that are available on the
	internet or a large corporate intranet.


To be fair there's room for people to focus on security
	issues. There's a lot of stuff to know about on security. But
	everyone should have a reasonable knowledge about it. As David
	points out: many eyeballs don't lead to secure code - you need many
	*educated* eyeballs. One of the things I like about David's
	attitude is that educating developers is a key part of the picture,
	with less emphasis on review steps with security groups.
