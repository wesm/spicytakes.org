---
title: "It’s a Malformed World"
date: 2006-11-13
url: https://blog.codinghorror.com/its-a-malformed-world/
slug: its-a-malformed-world
word_count: 339
---

[Bill de hra](http://www.dehora.net/journal/) recently highlighted a [little experiment Ian Hickson ran](http://lists.w3.org/Archives/Public/www-tag/2006Aug/0048.html) in August:

kg-card-begin: html

> I did a short study recently checking only for *syntax* errors in HTML documents, and the results were that of the 667416 files tested, 626575 had syntax errors. **Over 93%**. That’s only syntax errors in the HTML, not checking the CSS, the content types, the semantic errors (e.g. duplicate IDs – 86461 of those files had duplicated IDs), or any other errors.
> If you included those kinds of errors, you’d probably find that almost allpages had errors that would trigger this warning. Thus any sort of visible
> UI would be basically always saying “this page is broken”. That would not be good UI for the majority of users, who don’t care.

kg-card-end: html

Even [Tim-Berners Lee](http://en.wikipedia.org/wiki/Tim_Berners-Lee), the godfather of the Web, acknowledges that the move to enforce [well-formedness on the web](https://web.archive.org/web/20061126172409/http://dig.csail.mit.edu/breadcrumbs/node/166) with XHTML has failed:


> Some things are clearer with hindsight of several years. It is necessary to evolve HTML incrementally. The attempt to get the world to switch to XML, including quotes around attribute values and slashes in empty tags and namespaces all at once didn’t work. **The large HTML-generating public did not move, largely because the browsers didn’t complain.** Some large communities did shift and are enjoying the fruits of well-formed systems, but not all. It is important to maintain HTML incrementally, as well as continuing a transition to well-formed world, and developing more power in that world.


Perhaps this is why there’s [63 HTML validation errors](http://validator.w3.org/check?uri=http%3A%2F%2Fwww.google.com) on Google’s homepage right now. **Like** **it or not, we live in a world of malformed HTML.** Browsers aren’t compilers. They don’t fail spectacularly when they encounter invalid markup. And nor should they. HTML is, and always has been, tolerant by design. We’ll always be awash in a sea of [tag soup](http://essaysfromexodus.scripting.com/whatIsTagSoup).


Your browser doesn’t care if your HTML is well-formed. Your users don’t care if your HTML is well-formed. So *why should you?*

[html](https://blog.codinghorror.com/tag/html/)
[syntax errors](https://blog.codinghorror.com/tag/syntax-errors/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[xhtml](https://blog.codinghorror.com/tag/xhtml/)
[ui设计](https://blog.codinghorror.com/tag/uishe-ji/)
