---
title: "Captcha Control Coda"
date: 2004-11-08
url: https://blog.codinghorror.com/captcha-control-coda/
slug: captcha-control-coda
word_count: 106
---

I finally bit the bullet and formatted my [ASP.NET CAPTCHA server control](https://blog.codinghorror.com/an-aspnet-captcha-server-control/) as a CodeProject article. This version of the control has a few significant improvements over the last version:

- Optimized with use of HttpModule and Cache objects
- Removed ViewState for Captcha text (this isn’t secure, doh)
- Added .CaptchaChars property for specifying characters used in random CAPTCHA text


This has been through quite a bit of testing and refinement, and should be considered final – for now anyway. If I update it any further, I’ll do so through the CodeProject article, so leave comments there if you have any.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[httpmodule](https://blog.codinghorror.com/tag/httpmodule/)
[security](https://blog.codinghorror.com/tag/security/)
