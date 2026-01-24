---
title: "The Antidote to ASP.NET Smart Navigation"
date: 2004-10-27
url: https://blog.codinghorror.com/the-antidote-to-aspnet-smart-navigation/
slug: the-antidote-to-aspnet-smart-navigation
word_count: 303
---

One of the issues I have with ASP.NET is that it is **postback crazy**. Virtually nothing of significance can be done in pure browser client code with ASP.NET out of the box.* You have to Submit() the specially formed ASP.NET HTML form to the server, and all the event magic happens server side.


While this is nice from an abstraction standpoint, it’s kind of a pain for the client. Having tons of postbacks in the middle of the form causes “flicker” and loss of page scroll position. It can also be a serious performance issue if you have tons of viewstate that gets submitted to the server over and over. I am definitely not a fan of doing a lot of stuff in JavaScript and DOM on the browser – been there, done that – but we almost have the opposite extreme in ASP.NET.


One of the tricks MS introduced to **combat the loss of page scroll position on postback** is something called SmartNavigation. Unfortunately, it’s [horribly broken](https://web.archive.org/web/20051120004553/http://weblogs.asp.net/ksamaschke/archive/2003/04/27/6085.aspx). A friend recently referred me to an article by Brad McCabe which outlines the most elegant workaround I’ve seen so far – it lets you [retain page position between postbacks](https://web.archive.org/web/20041212052631/http://www.aspnetpro.com/NewsletterArticle/2003/09/asp200309bm_l/asp200309bm_l.asp) in a very generic way. And not a single named anchor in sight!


Better workarounds are on the horizon with ASP.NET 2.0. I hear we’ll be able to use XMLHTTP requests [to do “background” postbacks](https://web.archive.org/web/20051029044704/http://www.dotnetjunkies.com/Tutorial/E80EC96F-1C32-4855-85AE-9E30EECF13D7.dcik) in some scenarios. We’ve gone this route before, too. It works, but it’s still painful, mostly because the browser is a hideous development platform. If ASP.NET 2.0 can abstract away the pain, and retain browser compatibility, then I’m for it.


*Now, there are some third party ASP.NET server controls which expose a lot of exotic client side behaviors. But none of the default controls do.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[postback](https://blog.codinghorror.com/tag/postback/)
[server-side](https://blog.codinghorror.com/tag/server-side/)
[smartnavigation](https://blog.codinghorror.com/tag/smartnavigation/)
[performance](https://blog.codinghorror.com/tag/performance/)
