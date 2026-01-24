---
title: "WebFileManager updated"
date: 2005-01-10
url: https://blog.codinghorror.com/webfilemanager-updated/
slug: webfilemanager-updated
word_count: 140
---

I updated the [WebFileManager CodeProject article](http://www.codeproject.com/aspnet/WebFileManager.asp) with some enhancements. It now supports zipping files and column sorting:


![](https://blog.codinghorror.com/content/images/2025/05/image-41.png)


I included both the [code-behind and inline code](https://blog.codinghorror.com/code-behind-vs-inline-code/) versions of the page in the solution archive this time. There’s also a new dependency on [SharpZipLib](http://www.icsharpcode.net/OpenSource/SharpZipLib/Default.aspx), assuming you want the remote file zipping support.


I also found out the hard way that...

1. SharpZipLib, like the Java class it apes, is completely incapable of modifying an existing Zip archive. I wonder if .NET 2.0 includes any native support for Zip, GZip, etc.?
2. FireFox doesn’t support alignment in the <COLGROUP> tag. This makes specifying column attributes for alignment kind of a per-row pain in the butt. To be fair, CSS and HTML both kinda suck when referencing table columns. Cells and rows, yes, columns, not so much.

[c#](https://blog.codinghorror.com/tag/c-2/)
[sharpziplib](https://blog.codinghorror.com/tag/sharpziplib/)
[.net 2.0](https://blog.codinghorror.com/tag/net-2-0/)
[css](https://blog.codinghorror.com/tag/css/)
[html](https://blog.codinghorror.com/tag/html/)
