---
title: "Contextual Validation"
description: "In my writing endeavors, I've long intended to write a chunk of 	material on validation. It's an area that leads to a lot of 	confusion and it would be good to get some solid description of some 	of t"
date: 2005-12-07T00:00:00
tags: ["domain driven design", "application architecture"]
url: https://martinfowler.com/bliki/ContextualValidation.html
slug: ContextualValidation
word_count: 364
---


In my writing endeavors, I've long intended to write a chunk of
	material on validation. It's an area that leads to a lot of
	confusion and it would be good to get some solid description of some
	of the techniques that work well. However life is full of things to
	write about, rather more than time allows.


Some recent readings made me think about saying a few
	preliminary things on the topic. One common thing I see people do
	is to develop validation routines for objects. These routines come
	in various ways, they may be in the object or external, they may
	return a boolean or throw an exception to indicate failure. But one
	thing that I think constantly trips people up is when they think
	object validity on a context independent way such as an `isValid`
	method implies.


I think it's much more useful to think of validation as something
that's bound to a context - typically an action that you want to do.
Is this order valid to be filled, is this customer valid to check in
to the hotel. So rather than have methods like `isValid`
have methods like `isValidForCheckIn`.


One of the consequences of this is that saving an object to a
	database is itself an action. Thinking about it that way raises some
	important questions. Often when people talk about a context-free
	validity, they mean it in terms of saving to a database. But the
	various validity checks that make this up should be interrogated
	with the question âshould failing this test prevent saving?â


In [About Face](https://www.amazon.com/gp/product/1568843224/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1568843224&linkCode=as2&tag=martinfowlerc-20) Alan Cooper advocated that we shouldn't let
our ideas of valid states prevent a user from entering (and saving)
incomplete information. I was reminded by this a few days ago when
reading a draft of a book that [Jimmy Nilsson](http://www.jnsk.se/weblog/rss.xml) is working
on. He stated a principle that you should always be able to save an
object, even if it has errors in it. While I'm not convinced that this
should be an absolute rule, I do think people tend to prevent saving
more than they ought. Thinking about the context for validation may
help prevent that.


reposted on 03 Nov 2011
