---
title: "ASP.NET CAPTCHA control, improved"
date: 2004-10-02
url: https://blog.codinghorror.com/aspnet-captcha-control-improved/
slug: aspnet-captcha-control-improved
word_count: 206
---

I improved the [ASP.NET CAPTCHA server control](https://blog.codinghorror.com/an-aspnet-captcha-server-control/) I mentioned yesterday:

- Control respects all standard ASP.NET server control properties (font, border, accesskey, enabled, etcetera)
- Hide ViewState property (it’s required!)
- Added **CaptchaLength** property
- Added **CaptchaFontWarping** property
- Improve font sizing algorithm
- Improve warping algorithm (more mild distortion, no more drawing outside the box)
- Remove “1,0,I,O” from possible Captcha characters to prevent confusion in entering text
- Text is now optional
- Lots of other little improvements


If you are willing to sacrifice less OCR-ability for more human readability, you can adjust the CaptchaLength and CaptchaFontWarping properties to taste. For most applications, simply having a [CAPTCHA](http://www.captcha.net) of any sort is probably enough to block casual bot attacks, and shorter less warped phrases are definitely a lot easier to read. The default is 6 characters with medium warping, which is a good blend.


You can download the solution from my CodeProject article if you’re interested. There are only two projects in the solution; an ultra simple demo website and the control library itself.


To see a CAPTCHA in action, check out the [Yahoo mail signup page](http://edit.yahoo.com/config/eval_register?.intl=us&new=1). Refreshing the page will generate a new one every time...

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[captcha](https://blog.codinghorror.com/tag/captcha/)
[server control](https://blog.codinghorror.com/tag/server-control/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concept](https://blog.codinghorror.com/tag/programming-concept/)
