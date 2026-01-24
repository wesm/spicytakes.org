---
title: "HTTP Compression via HttpModule"
date: 2004-11-03
url: https://blog.codinghorror.com/http-compression-via-httpmodule/
slug: http-compression-via-httpmodule
word_count: 301
---

I’ve talked about [HTTP compression in IIS 6.0](https://blog.codinghorror.com/http-compression-and-iis-6-0/), and [HTTP compression using Net.WebClient](https://blog.codinghorror.com/netwebclient-and-gzip/), but what about deploying ASP.NET websites to servers you don’t control, e.g., third party hosts? How can we enable compression in that scenario?


We can implement HTTP compression on a per-website basis in ASP.NET through a **compression HttpModule**. Sure enough, a little searching dug up the blowery.org [HttpCompressionModule](https://web.archive.org/web/20041109053750/http://www.blowery.org/code/HttpCompressionModule.html). And it works very well; the current version has been around a while, and already reflects a number of significant bugfixes. After modifying the Web.config...

kg-card-begin: html

```
<httpModules>
<add name="CompressionModule" type="blowery.Web.HttpCompress.HttpModule,
blowery.web.HttpCompress"/>
</httpModules>
```

kg-card-end: html

...and deploying the two dlls to the bin folder, it passes [the sniffer test](https://blog.codinghorror.com/sniff-this/): the HTTP compression header is set, and the pages are sent to the browser as gzipped binary data.


I did, however, run into one bug related to my [ASP.NET Unhandled Exception Handling HttpModule](https://web.archive.org/web/20041204122038/http://www.codeproject.com/aspnet/ASPNETExceptionHandling.asp) – for some reason, **the compression module prevented the exception module from dumping output to the webpage via Response.Write and Response.End**. The automatic emails and text logs worked fine, so the code was executing, but the response output methods had no effect. Clearly, some kind of problem related to having two HttpModules running at the same time... a quick change to the blowery source fixed that:

kg-card-begin: html

```
void CompressContent(object sender, EventArgs e) {
HttpApplication app = (HttpApplication)sender;
if (app.Server.GetLastError() != null) {
return;
}
[.. rest of code snipped]
```

kg-card-end: html

Basically, in the case of any Exception – if it bubbles up this far, it’s *definitely *unhandled – we want to return immediately and do nothing in the compression handler. I am not sure if this is the optimal fix, but without it, all I get is the default .NET exception page. And who wants that?

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[http compression](https://blog.codinghorror.com/tag/http-compression/)
[httpmodule](https://blog.codinghorror.com/tag/httpmodule/)
[web.config](https://blog.codinghorror.com/tag/web-config/)
[deployment](https://blog.codinghorror.com/tag/deployment/)
