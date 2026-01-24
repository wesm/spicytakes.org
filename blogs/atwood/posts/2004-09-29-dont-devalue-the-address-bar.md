---
title: "Don’t Devalue the Address Bar"
date: 2004-09-29
url: https://blog.codinghorror.com/dont-devalue-the-address-bar/
slug: dont-devalue-the-address-bar
word_count: 275
---

I was reading an interesting [entry in Rocky Lhotka’s blog](https://web.archive.org/web/20051018085438/http://www.lhotka.net/WeBlog/PermaLink.aspx?guid=b28971dc-ac4b-4494-8a21-7a5105a39b07) when something in the URL caught my eye:


> http://www.lhotka.net/WeBlog/PermaLink.aspx?guid=b28971dc-ac4b-4494-8a21-7a5105a39b07


I guess it’s a [DasBlog](https://web.archive.org/web/20040903235900/http://dasblog.net/) thing, but good lord: a globally unique ID in a blog hyperlink? Has it really come to this?

kg-card-begin: html

```
Dim g As Guid = Guid.NewGuid
Console.WriteLine(g.ToString)
2ac6857d-6fa4-43f6-9145-dfffaf00fd7a
```

kg-card-end: html

This is my GUID. There are many like it but this one is mine. My GUID is my best friend. It is my life. I must master it as I must master my life. Without me, my GUID is useless. Without my GUID I am useless.


It’s bad enough that so many websites **devalue the address bar with nonsensical geek-speak URLs**...

- [http://www.bestbuy.com/site/olspage.jsp?id=cat03037&type=category&navLevel=4&navHistory=cat00000%2Bcat03000%2Bcat03030](https://web.archive.org/web/20060208053625/http://www.bestbuy.com/site/olspage.jsp?id=cat03037&type=category&navLevel=4&navHistory=cat00000%2Bcat03000%2Bcat03030)
- [http://www.amazon.com/exec/obidos/tg/detail/-/0821277545/ref=pd_nfy_b_nr/104-4632089-1596752?v=glance&s=books&n=283155](http://www.amazon.com/exec/obidos/tg/detail/-/0821277545/ref=pd_nfy_b_nr/104-4632089-1596752?v=glance&s=books&n=283155)
- [http://listings.ebay.com/_W0QQa14Z1752QQalistZa14QQgcsZ1135QQpfidZ1413QQsocmdZListingItemList](https://web.archive.org/web/20051208010703/http://listings.ebay.com/_W0QQa14Z1752QQalistZa14QQgcsZ1135QQpfidZ1413QQsocmdZListingItemList)


...without adding GUIDs to the mix! How about something simpler that’s actually understandable?

- [http://www.cnn.com/2004/WEATHER/09/11/hurricane.ivan/index.html](http://www.cnn.com/2004/WEATHER/09/11/hurricane.ivan/index.html)
- [http://www.subversivecrossstitch.com/lifesucks.html](https://web.archive.org/web/20041123084438/http://www.subversivecrossstitch.com/lifesucks.html)
- [http://www.techreport.com/etc/2004q3/3dmark05/index.x?pg=1](https://web.archive.org/web/20041011075143/http://www.techreport.com/etc/2004q3/3dmark05/index.x?pg=1)*


Building crappy URLs is just plain laziness. With the rich set of tools provided by IIS and ASP.NET, we should be leveraging [404 handlers](https://web.archive.org/web/20040904022045/http://www.asp101.com/articles/wayne/extendingnamesaspx/default.asp) and [URL Rewriting](http://msdn.microsoft.com/asp.net/default.aspx?pull=%2Flibrary%2Fen-us%2Fdnaspp%2Fhtml%2Furlrewriting.asp) to build URLs that are **simple for people to understand**, instead of taking the low road and building URLs that are easy for machines to understand.


My favorite technique is to map the 404 handler in IIS, per website, to /404.aspx. I can then intercept page not found errors with ASP.NET code and Server. Transfer them as I see fit. If you want a more robust solution at the ISAPI level, we’ve also used [ISAPI Rewrite](http://www.isapirewrite.com) with great success.


*They should simplify this even further by making the default folder handler “index.x”, then just... [http://www.techreport.com/etc/2004q3/3dmark05/?pg=1](https://web.archive.org/web/20041011075143/http://www.techreport.com/etc/2004q3/3dmark05/index.x?pg=1)

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[web development](https://blog.codinghorror.com/tag/web-development/)
[urls](https://blog.codinghorror.com/tag/urls/)
