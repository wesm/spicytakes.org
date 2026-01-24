---
title: "Performance: Remoting vs. Web Services"
date: 2004-08-13
url: https://blog.codinghorror.com/performance-remoting-vs-web-services/
slug: performance-remoting-vs-web-services
word_count: 800
---

This question comes up periodically, and Microsoft has a fairly definitive whitepaper on the topic, Performance Comparison: .NET Remoting vs. ASP.NET Web Services. The article has a number of charts with crazy legends, so let me provide a better one:

kg-card-begin: html


| ASMX | Web Service |
| WS_TCP_Binary | Windows Service remoting host, TCP protocol, binary format |
| WS_TCP_Soap | Windows Service remoting host, TCP protocol, plaintext format |
| IIS_HTTP_Binary | IIS remoting host, HTTP protocol, binary format |
| IIS_HTTP_Soap | IIS remoting host, HTTP protocol, plaintext format |
| WS_HTTP_Binary | Windows service remoting host, HTTP protocol, binary format |
| WS_HTTP_Soap | Windows service remoting host, HTTP protocol, plaintext format |


kg-card-end: html

The short answer: remoting, using the TCP protocol, and hosted in a Windows service, is fastest. No surprises here. But that’s not the whole story. Some things you should know up front:


> *Note that the performance of the ASP.NET Web service has dropped so much so that it performs similar to WS_TCP_SOAP, WS_HTTP_SOAP and IIS_HTTP_SOAP. This drop in performance is due to two known issues in ASP.NET, which will be fixed in upcoming versions. One is the buffering issue as discussed earlier; other is related to DataSet serialization in ASP.NET.*


I believe the buffering issue has been fixed in 1.1; this article is from 2002. What hasn’t been fixed, however, is **the well-known “feature” of the DataSet object where it serializes as plaintext XML, even when you explicitly tell it to serialize as binary. **You’ll definitely want to keep that in mind, because this applies to all of the above approaches: it’s a huge problem. Luckily this is fixed in ADO.NET 2.0, and there are [some workarounds](https://web.archive.org/web/20051024150446/http://objectsharp.com/Blogs/datasetfaq/archive/2004/06/10/614.aspx) in the meantime. Anyway, let’s break this down piece by piece:

- **HTTP vs. TCP**. Even though TCP squeezes out more throughput in extreme scenarios, it’s hard to argue against the ubiquity of HTTP and port 80. It costs a little more, but you get proxies, compression, routing, and a lot more. Well worth it for the small cost.
- **Windows Service vs. IIS**. Really the same argument as above. Like HTTP, IIS is such a well understood entity. It gives you a lot of free bonus functionality you wouldn’t get in a vanilla service (think web farms for scalability). It’s hard to justify not using it, given the minor performance hit.
- **Binary vs. SOAP**. Binary is “poor man’s compression.” Plaintext/SOAP has the advantage of transparency, so if you can get a decent compression layer in there somewhere, you really don’t need binary. I can’t believe MS didn’t include a compression layer in their remoting stack, so you might as well plan on using binary for now. This ties directly into the serialization time, which can be significant on large objects/datasets; the improvement in performance can be dramatic.
- **Remoting vs. Web Service**. Where do I start? It depends how tightly coupled you want your application to be to your server-side API. Remoting is a little easier to get running with minimal work in the short term, but the long term benefits skew heavily towards Web Services. When you build a WS, you’ve built a truly generic HTTP interface layer that you can leverage for the foreseeable future. This isn’t a COM or CORBA flash in the pan.


The reason I dug this article out was at the request of a developer working on a performance problem. After I quizzed him for details, I found out they have a client app sending an **85,000 row DataSet down to the client via a remoting call**. They have an entirely different set of problems to worry about: why send down that much data? In my experience, this is typical of real world applications. A lot of hand wringing over minor performance differences – tied to what are really implementation details – doesn’t buy you much when your bottleneck is elsewhere. In the real world, it is highly unlikely that any of the above approaches will be a meaningful bottleneck; **a well designed API will win every time, no matter what protocol or interface it is using.** Therefore, you should pick the interface that is easiest to troubleshoot and maintain.


In my opinion, that’s **either a Web Service, or remoting hosted in IIS using the SOAP protocol.** It’s trivial to switch to binary protocol later; just flick a switch in your .config files. Web services and remoting aren’t all that different, and they are definitely evolving closer towards each other in .NET 2.0. I’ve worked with remoting extensively, and I like it, but I still think if you are going to put any effort into your server-side API at all – you should be building a web service.

[.net](https://blog.codinghorror.com/tag/net/)
[remoting](https://blog.codinghorror.com/tag/remoting/)
[web services](https://blog.codinghorror.com/tag/web-services/)
[performance](https://blog.codinghorror.com/tag/performance/)
[tcp](https://blog.codinghorror.com/tag/tcp/)
