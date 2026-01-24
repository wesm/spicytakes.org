---
title: "Building Unbreakable Links"
date: 2004-08-25
url: https://blog.codinghorror.com/building-unbreakable-links/
slug: building-unbreakable-links
word_count: 279
---

I was reading through some of the [DataGrid Girl’s oh-so-cute article links](http://www.datagridgirl.com/articles.aspx), and I encountered a few dead ones. It’s not really Marcie’s fault; dead links are inevitable on any page as it ages. Such is the nature of absolute links. For example, this one:


> [http://msdn.microsoft.com/msdnmag/issues/02/03/cutting/cutting0203.asp](http://msdn.microsoft.com/msdnmag/issues/02/03/cutting/cutting0203.asp?ref=blog.codinghorror.com)


A few years ago, I had this thought: why do we use traditional absolute URLs any more? **Why not build all of our links using relative Google search terms?** For the above broken link, we can restate it like so:


> [http://www.google.com/search?q=msdnmag+asp.net+data+shaping&btnI=1](http://www.google.com/search?q=msdnmag+asp.net+data+shaping&btnI=1)


All you need to do is run a quick function to determine three or four of the most unique words on the page, then feed them to Google as query terms with the “I'm feeling lucky” parameter. **Now you have a permanent, unbreakable link to that content.** Well, permanent unless Google goes out of business, or the content disappears from the internet completely.


Of course, it’s unlikely everyone will adopt this approach for the most obvious reason: Google would become unbelievably powerful. They would be the “link DNS” for the entire internet. But as a practical solution to Marcie’s problem, I think it is totally workable. Whenever I link to articles in my code, I try to do so through very specific google search terms, which are likely to produce valid links many years from now – even if the content moves to a different place on the internet.


All I need is some sort of web-based tool to automatically parse a page and produce 4-5 unique words from that page. It’s sort of like [Googlewhacking](https://web.archive.org/web/20040726042019/http://www.googlewhack.com/), but with a more practical bent.

[urls](https://blog.codinghorror.com/tag/urls/)
[hyperlinks](https://blog.codinghorror.com/tag/hyperlinks/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[seo](https://blog.codinghorror.com/tag/seo/)
[search engine optimization](https://blog.codinghorror.com/tag/search-engine-optimization/)
