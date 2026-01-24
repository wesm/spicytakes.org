---
title: "Classic ASP"
date: 2004-11-30
url: https://blog.codinghorror.com/classic-asp/
slug: classic-asp
word_count: 347
---

I just went to the [Radio Shack](http://www.radioshack.com) website to look for something, and after every click on the main page, I was greeted with this:


![](https://blog.codinghorror.com/content/images/2025/06/image-74.png)


If I was running a giant corporation, I think I’d hire coders who could develop a rational error handling strategy for our production website.


Of course, that’s much [easier to do in ASP.NET](http://www.codeproject.com/aspnet/ASPNETExceptionHandling.asp) than cruddy old classic ASP. I’m not a big fan of the ultra-leaky “winforms on the web” abstraction model, but there’s no denying that ASP.NET – and the .NET framework – is an order of magnitude improvement over ASP. That’s why I was appalled that in the otherwise interesting, [How Microsoft Lost the API War](http://www.joelonsoftware.com/articles/APIWar.html), Joel wrote:


> *And personally I still haven’t had time to learn .NET very deeply, and we haven’t ported Fog Creek’s two applications from classic ASP and Visual Basic 6.0 to .NET because there’s no return on investment for us. None. It’s just Fire and Motion as far as I’m concerned: Microsoft would love for me to stop adding new features to our bug tracking software and content management software and instead waste a few months porting it to another programming environment, something which will not benefit a single customer and therefore will not gain us one additional sale, and therefore which is a complete waste of several months, which is great for Microsoft, because they have content management software and bug tracking software, too, so they’d like nothing better than for me to waste time spinning cycles catching up with the flavor du jour, and then waste another year or two doing an Avalon version, too, while they add features to their own competitive software. Riiiight.*


It’s difficult to comprehend how a smart guy like Joel could be so blind to the massive, obvious benefits of a straight port to ASP.NET. Coherent global error handling is only the tip of the iceberg. At this point, you could not pay me enough to write in ASP.*


*Ok, you could. But it would be really expensive.

[asp](https://blog.codinghorror.com/tag/asp/)
[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[classic asp](https://blog.codinghorror.com/tag/classic-asp/)
[error handling](https://blog.codinghorror.com/tag/error-handling/)
