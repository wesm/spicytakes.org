---
title: "Visual Diff Tools"
date: 2004-06-28
url: https://blog.codinghorror.com/visual-diff-tools/
slug: visual-diff-tools
word_count: 284
---

I’m currently building a .NET library that constructs .MHT files, aka single file web page archives. That’s what you get when you perform a **File | Save As | Web Archive, Single File** operation in IE6. HTML is a great, standard format for building richly formatted one-off reports, but once you start including images, it becomes a pain to manage a set of files. Thus, the utility of combining everything into a single file.


Surprisingly, instead of some crazy proprietary Microsoft format like you’d expect, the file follows the simple [Multipart MIME Message RFC](http://www.ietf.org/rfc/rfc2557.txt) standard. Building an .MHT file is sort of like sending an email to yourself – go figure. It also [works via extension](https://web.archive.org/web/20040904235817/http://maf.mozdev.org/) in your precious Firefox, for those of you that enjoy slow rendering.


During development, I needed to reverse engineer what IE6 constructs, and use that as a comparison point for the output from my application. Unfortunately, the only file comparison tool I had access to was the crappy default “compare versions” function in Visual SourceSafe. It’s workable, but it’s kind of... ghetto.


Every developer should have a good diff tool in their toolkit. After a bit of research, I settled on [Araxis Merge](http://www.araxis.com/merge/) as my preferred tool for visual comparisons.


![](https://blog.codinghorror.com/content/images/2025/06/image-53.png)


It’s a pricey tool, but it’s come in very handy so far. The only regret I have is that VSS doesn’t allow the use of any external comparison tools, so you can’t integrate Merge with Visual Studio .NET.


Anyway, if like me, the only diff tool you ever used was the one in VSS – you may not know how much you’re missing.

[.net](https://blog.codinghorror.com/tag/net/)
[library](https://blog.codinghorror.com/tag/library/)
[mht files](https://blog.codinghorror.com/tag/mht-files/)
[web archive](https://blog.codinghorror.com/tag/web-archive/)
[html](https://blog.codinghorror.com/tag/html/)
[mime](https://blog.codinghorror.com/tag/mime/)
[rfc](https://blog.codinghorror.com/tag/rfc/)
[development](https://blog.codinghorror.com/tag/development/)
[reverse engineering](https://blog.codinghorror.com/tag/reverse-engineering/)
[file comparison](https://blog.codinghorror.com/tag/file-comparison/)
