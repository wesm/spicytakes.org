---
title: "Are You an XML Bozo?"
date: 2006-07-28
url: https://blog.codinghorror.com/are-you-an-xml-bozo/
slug: are-you-an-xml-bozo
word_count: 309
---

Here’s a helpful article that documents common pitfalls to [avoid when composing XML documents](http://hsivonen.iki.fi/producing-xml/). Nobody wants to be [called an XML Bozo](http://www.tbray.org/ongoing/When/200x/2004/01/11/PostelPilgrim) by Tim Bray, the co-editor of the XML specification, right?

kg-card-begin: html

> There seem to be developers who think that well-formedness is awfully hard — if not impossible — to get right when producing XML programmatically and developers who can get it right and wonder why the others are so incompetent. I assume no one wants to appear incompetent or to be called names. Therefore, I hope the following list of dos and don’ts helps developers to move from the first group to the latter.
> Don’t think of XML as a text format
> Don’t use text-based templates
> Don’t `print`
> Use an isolated serializer
> Use a tree or a stack (or an XML parser)
> Don’t try to manage namespace declarations manually
> Use unescaped Unicode strings in memory
> Use UTF-8 (or UTF-16) for output
> Use NFC
> Don’t expect software to look inside comments
> on’t rely on external entities on the Web
> Don’t bother with CDATA sections
> Don’t bother with escaping non-ASCII
> Avoid adding pretty-printing white space in character data
> Don’t use `text/xml`
> Use XML 1.0
> Test with astral characters
> Test with forbidden control characters
> Test with broken UTF-*

kg-card-end: html

I’m a little ambivalent about XML, largely due to what [John Lam](http://www.iunknown.com/) calls “The Angle Bracket Tax.” I think [XSLT is utterly insane](https://blog.codinghorror.com/martin-fowler-hates-xslt-too/) for anything except the most trivial of tasks, but I [do like XPath](https://blog.codinghorror.com/interactive-xpath-expression-builder/) – it’s sort of like SQL with automatic, joinless parent-child relationships.


But XML is generally the least of all available evils, and if you’re going to use it, you might as well follow the rules.

[xml](https://blog.codinghorror.com/tag/xml/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
