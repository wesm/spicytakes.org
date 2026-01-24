---
title: "Martin Fowler hates XSLT too"
date: 2005-07-05
url: https://blog.codinghorror.com/martin-fowler-hates-xslt-too/
slug: martin-fowler-hates-xslt-too
word_count: 383
---

I have no problem with XML. It’s a fine way to store hierarchical data in a relatively simple, mostly human-readable format. But I’ve always disliked its companion technology, [XSLT](http://www.w3.org/TR/xslt). While useful in theory – “using a simple XSLT transform, XML can be converted into anything!”– in practice, it takes painful contortions to do anything practical. Evidently I’m not alone; [Martin Fowler hates XSLT too](http://www.martinfowler.com/bliki/MovingAwayFromXslt.html):


> All of this site is written in simple XML documents and transformed to HTML. I find this works really well, and means I never have to worry about dealing with HTML formats. (Not that fancy layout is my style, as you can tell.) I’ve even written [a whole book that way](http://www.martinfowler.com/articles/writingInXml.html).
> For most of this time I’ve used XSLT as my transformation language. I’ve got pretty good with slinging XSLT around and getting it to do what I want.
> But no more.
> When I wrote the software for this Bliki (on a long flight) I did it in Ruby. Prior to that I used Ruby to do a new version of my home page. **My conclusion from this exercise was that using Ruby for XML transforms was much easier than using XSLT.**


I’ve had almost the same exact argument with a few developers I used to work with. After working through a bit of the XSLT necessary to accomplish something, **I concluded that it was easier and simpler to use procedural code to do the same thing.** Not always, of course, but most of the time. As Fowler points out, this does beg the question: what good is XSLT?


> I think this may raise some real questions about XSLT. There’s still much I like about the power of XSLT, but I hate the syntax and the walls you keep running into. I’m not going to convert my whole site over to Ruby tomorrow – most of the XSLT works fine - but I can certainly see my way to doing that at some point in the future. But the bigger question is whether you’re better off with scripting language for this kind of task than XSLT.


Maybe the idea of XSLT transforming XML into “anything” is fundamentally unrealistic – just more [Write Once, Run Anywhere](https://web.archive.org/web/20060617055621/http://archive.salon.com/tech/col/garf/2001/01/08/bad_java/index.html) snake oil.

[xml](https://blog.codinghorror.com/tag/xml/)
[xslt](https://blog.codinghorror.com/tag/xslt/)
[martin fowler](https://blog.codinghorror.com/tag/martin-fowler/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[ruby](https://blog.codinghorror.com/tag/ruby/)
