---
title: "An ASP.NET CAPTCHA Server Control"
date: 2004-10-01
url: https://blog.codinghorror.com/an-aspnet-captcha-server-control/
slug: an-aspnet-captcha-server-control
word_count: 194
---

A few days ago, I found a really cool [CAPTCHA](http://www.captcha.net) ASP.NET [code sample](http://www.brainjar.com/dotNet/CaptchaImage). I converted it to VB.NET and repackaged it as a full blown [ASP.NET server control](https://web.archive.org/web/20051124132103/http://samples.gotdotnet.com/quickstart/aspplus/doc/webctrlauthoring.aspx):


![](https://blog.codinghorror.com/content/images/2025/06/image-32.png)


It’s as simple as I could make it: a total drag and drop, set the (three) properties and forget it implementation. The only tricky part was dealing with the dynamically generated image. You will have to add this HttpHandler section to your web.config file when you use the **CaptchaControl**

kg-card-begin: html

```
<httpHandlers>
<add verb="*" path="CaptchaImage.aspx"
type="WebControlCaptcha.CaptchaImageStream, WebControlCaptcha" />
</httpHandlers>

```

kg-card-end: html

You can download the zipped VS.NET 2003 solution from [my CodeProject article](http://www.codeproject.com/useritems/CaptchaControl.asp?ref=blog.codinghorror.com) if you’re interested. There are only two projects in the solution; an ultra simple demo website and the control library itself.


I should also mention that I **tested this CAPTCHA against OCR software**, specifically [OmniPage Pro 14](http://www.scansoft.com/omnipage/?ref=blog.codinghorror.com). It does surprisingly well for a couple key reasons – low contrast, and all the characters are warped. It’s possible to defeat it, but it’s definitely not a trivial “drag to OCR window” situation. My kudos to BrainJar for coming up with this simple yet effective CAPTCHA.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[server control](https://blog.codinghorror.com/tag/server-control/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[httphandler](https://blog.codinghorror.com/tag/httphandler/)
