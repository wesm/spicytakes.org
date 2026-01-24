---
title: "Saving URLs to MHTML via .NET"
date: 2004-09-13
url: https://blog.codinghorror.com/saving-urls-to-mhtml-via-net/
slug: saving-urls-to-mhtml-via-net
word_count: 211
---

I just posted another CodeProject article, Convert any [URL to a MHTML archive](https://web.archive.org/web/20041012004622/http://www.codeproject.com/vb/net/MhtBuilder.asp) using native .NET code. The title is a bit misleading; using my class, you can actually convert any URL to one of four formats in a single line of code:

- Web Page, complete (HTML plus files in subfolder)
- Web Archive, single file (MHTML only)
- Web Page, HTML only (HTML only)
- Text File (TXT only)


This mimics the **‘File | Save As’ menu in Internet Explorer **as closely as I could get it to. It’s pretty darn close, and quite handy. We are using IE as a basic reporting engine, and it’s a lot easier to email someone a report – or store it in a document management system – when you have a single MHTML file!


I knew IE had some crazy way of **saving a complete web page as a single file**, but I was as surprised as anyone else to find that IE’s “Web Archive” save option is based on an actual internet standard: RFC standard 2557, [compliant Multipart MIME Message](http://www.ietf.org/rfc/rfc2557.txt) (MHTML web archive). As I mentioned a few months ago in my post about [Visual Diff Tools](https://blog.codinghorror.com/visual-diff-tools/), this [should work in Firefox](http://maf.mozdev.org), too...

[.net](https://blog.codinghorror.com/tag/net/)
[mhtml](https://blog.codinghorror.com/tag/mhtml/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[web development](https://blog.codinghorror.com/tag/web-development/)
