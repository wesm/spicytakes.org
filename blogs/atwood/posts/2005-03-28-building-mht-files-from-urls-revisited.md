---
title: "Building Mht Files from URLs revisited"
date: 2005-03-28
url: https://blog.codinghorror.com/building-mht-files-from-urls-revisited/
slug: building-mht-files-from-urls-revisited
word_count: 244
---

I finally finished updating my CodeProject article, [Convert any URL to a MHTML archive using native .NET code](https://web.archive.org/web/20050405210358/http://www.codeproject.com/vb/net/MhtBuilder.asp). It’s based on [RFC standard 2557](http://www.ietf.org/rfc/rfc2557.txt), aka Multipart MIME Message (MHTML web archive). You may also know it as *that crazy File, Save As, “Web Archive, Single File” menu option* in Internet Explorer. It’s basically a way to package an entire web page as a (mostly) functional single file that can be emailed, stored in a database, or what have you. Lots of interesting possibilities, including quick and dirty offline functionality for ASP.NET websites using loopback HTTP requests.


This was a truly painful total rewrite, but it offers tons of new functionality:

- Completely rewritten!
- [Autodetection of content encoding](https://blog.codinghorror.com/there-aint-no-such-thing-as-plain-text/) (e.g., international web pages), tested against multi-language websites
- Now [correctly decompresses](https://blog.codinghorror.com/net-webclient-and-deflate/) both types of HTTP compression
- Supports completely in-memory operation for server-side use, or on-disk storage for client use
- Now works on web pages with frames and iframes, using recursive retrieval
- HTTP authentication and HTTP Proxy support
- Allows configuration of browser ID string to retrieve browser-specific content
- Basic cookie support (needs enhancement and testing)
- Much improved regular expressions used for parsing HTTP
- Extensive use of VB.NET 2005 style XML comments throughout


If you’re interested, you can download the VS.NET 2003 solution from my blog until the CodeProject site gets updated. Here’s a screenshot of the demo app packaged with the Mht.Builder class:


![](https://blog.codinghorror.com/content/images/2025/05/image-150.png)

[.net](https://blog.codinghorror.com/tag/net/)
[mhtml](https://blog.codinghorror.com/tag/mhtml/)
[programming](https://blog.codinghorror.com/tag/programming/)
[web development](https://blog.codinghorror.com/tag/web-development/)
