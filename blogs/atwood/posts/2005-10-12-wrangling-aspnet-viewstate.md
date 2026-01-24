---
title: "Wrangling ASP.NET Viewstate"
date: 2005-10-12
url: https://blog.codinghorror.com/wrangling-aspnet-viewstate/
slug: wrangling-aspnet-viewstate
word_count: 251
---

Inspired by Scott Hanselman’s recent post on [ASP.NET viewstate wrangling](http://www.hanselman.com/blog/MovingViewStateToTheBottomOfThePage.aspx), here’s a roundup of tips for dealing with that ornery viewstate stuff. The first rule of thumb, of course, is to **turn it off whenever you can**. But sometimes you can’t.


I think the DotNetNuke developers were the first to realize that **moving the viewstate to the bottom of the page** makes the page much more Google-friendly. Google only indexes the first (n) bytes of the page, so if you have 12 kb of Base64 encoded schmutz in your header, that isn’t exactly helping people find your pages via Google searches. Scott Mitchell compares and contrasts several methods of [moving the viewstate input field](https://web.archive.org/web/20051125020426/http://scottonwriting.net/sowblog/posts/3536.aspx) to the bottom of the HTML form.


The benefits from **compressing viewstate** are [somewhat marginal](https://web.archive.org/web/20051030120434/http://www.mostlylucid.co.uk/archive/2004/01/03/694.aspx), nowhere near what you’d get from zipping plain text. but it’s still worth trying. Scott Hanselman points us to a nifty base page class that [automagically compresses viewstate](https://web.archive.org/web/20060411044221/http://www.hanselman.com/blog/CommentView,guid,febce059-7e7c-439e-af3d-c53d250b3e9c.aspx) for you.


There’s also an interesting [article on eggheadcafe](https://web.archive.org/web/20051026083023/http://www.eggheadcafe.com/articles/20040613.asp) about **moving viewstate to the server**. Peter Bromberg benchmarks the performance difference between viewstate on the client, and viewstate on the server in Session, Application, or Cache.


ASP.NET 2.0 brings a few much-needed [improvements to Viewstate](https://web.archive.org/web/20051024133545/http://www.nikhilk.net/ViewStateImprovements.aspx):

- Viewstate can be safely disabled without destroying intrinsic control behaviors thanks to a new container, [Controlstate](https://web.archive.org/web/20051125081523/http://pluralsight.com/blogs/fritz/archive/2004/07/01/472.aspx).
- An [improved formatter class](https://web.archive.org/web/20051125081738/http://pluralsight.com/blogs/fritz/archive/2004/06/03/408.aspx), ObjectStateFormatter, appears to reduce ViewState size by half.


Here’s to progress. Now pardon me while I crack my bullwhip. *Hyaa!!*

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[viewstate](https://blog.codinghorror.com/tag/viewstate/)
[viewstate management](https://blog.codinghorror.com/tag/viewstate-management/)
[dotnetnuke](https://blog.codinghorror.com/tag/dotnetnuke/)
[google seo](https://blog.codinghorror.com/tag/google-seo/)
