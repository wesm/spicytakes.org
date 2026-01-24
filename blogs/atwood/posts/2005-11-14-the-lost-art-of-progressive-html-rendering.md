---
title: "The Lost Art of Progressive HTML Rendering"
date: 2005-11-14
url: https://blog.codinghorror.com/the-lost-art-of-progressive-html-rendering/
slug: the-lost-art-of-progressive-html-rendering
word_count: 425
---

One thing I dislike about ASP.NET is that **it renders the entire web page in memory before sending one single byte of that page to the browser. **Consider an ASP.NET page with an embedded DataGrid that relies on ten complex database queries over 15 seconds. Why can’t we serve up part of the page while we’re waiting for those DataGrid queries – so the user has something to look at? A blank page is a disappointing user experience. The strong psychological benefit of progressive rendering is [well documented](https://blog.codinghorror.com/when-writing-code-means-youve-failed/).


What’s even more galling is that HTML was originally designed to render progressively as content is received. Internet Explorer is perfectly capable of rendering partial HTML content. Netscape offered progressive rendering as far back [as version 1.0](https://web.archive.org/web/20051122153902/http://www.boutell.com/newfaq/history/fbrowser.html):


> *Netscape is the browser that introduced most all of the remaining major features that define a web browser as we know it. The first version of Netscape appeared in October 1994 under the code name “Mozilla.” **Netscape 1.0’s early beta versions introduced the “progressive rendering” of pages and images, meaning that the page begins to appear and the text can be read even before all of the text and/or images have been completely downloaded.** Version 1.1, in March 1995, introduced HTML tables, which are now used in the vast majority of web pages to provide page layout.*


See progressive HTML rendering in action via this MSDN sample:


![progressive-rendering-normal.gif](https://blog.codinghorror.com/content/images/uploads/2005/11/6a0120a85dcdae970b0128776fd74e970c-pi.gif)


![progressive-rendering-optimized.gif](https://blog.codinghorror.com/content/images/uploads/2005/11/6a0120a85dcdae970b0128776fd769970c-pi.gif)


This particular sample is a demonstration of IE’s table-layout attribute, which isn’t even necessary for Firefox to render the table progressively. But it really doesn’t matter which browser you use; the same “show as much as you can as soon as you can” rendering rule should apply to any web page you design.


If the pictured table was rendered as a DataGrid, progressive rendering support is moot. The page model of ASP.NET precludes a single byte of data being sent to the client until the entire page is rendered on the server. **There’s no opportunity for the browser to start displaying data to the user while the server is still chugging away on the data.** The user is stuck staring at a blank web page for the full 15 seconds until the operation completes on the server.


You can still write ASP.NET pages that properly stream data to the browser using **Response.Write** and **Response.Flush**. But you can’t do it within the normal ASP.NET page lifecycle. Maybe this is a natural consequence of the ASP.NET abstraction layer.


Regardless, it still sucks for users.

[html](https://blog.codinghorror.com/tag/html/)
[progressive rendering](https://blog.codinghorror.com/tag/progressive-rendering/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[internet explorer](https://blog.codinghorror.com/tag/internet-explorer/)
