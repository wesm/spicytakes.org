---
title: "Code-Behind vs. Inline Code"
date: 2005-01-04
url: https://blog.codinghorror.com/code-behind-vs-inline-code/
slug: code-behind-vs-inline-code
word_count: 405
---

After religiously adhering to the new, improved code-behind model of ASP.NET for so long, I have to admit **it’s sort of refreshing to rediscover inline code ASPX pages again**. Deploying single web pages to a server without recompiling the entire solution? Making localized edits to single pages that take effect in real time? A single file that contains both code and markup in one convenient self-contained package? Revolutionary!


I’ve worked with code-behind for so long I actually didn’t even know how to convert a page to the code inline model. As expected, it’s quite simple:


1. Open the HTML (.aspx) view of an existing ASPX code-behind page.


2. Add or modify the following page directive:

kg-card-begin: html

```
<%@ Page Language="vb" Strict="True" %>

```

kg-card-end: html

3. Paste all the code from your existing code-behind (.vb) into a HTML script block:

kg-card-begin: html

```
<HEAD>
<SCRIPT language="vb" runat="server">
(page class code goes here)
</SCRIPT>
</HEAD>
```

kg-card-end: html

Only paste the code *inside* the page class, under the “Web Form Designer Generated Code” region. Don’t paste the class itself!


4. Don’t forget to add any imports your code needs; these can go just above the page directive.

kg-card-begin: html

```
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Text" %>
<%@ Import Namespace="System.Text.RegularExpressions" %>
<%@ Import Namespace="System.Configuration" %>
```

kg-card-end: html

5. Delete the associated .vb code-behind file.


That’s it! You now have a single file webpage that dynamically compiles. Copy that single file to a target website and, assuming it doesn’t have any other dependencies, it’ll load right up.


**Unfortunately, Inline ASPX pages also remind me of some things I didn’t miss from the bad old days of ASP programming**: spaghetti code, extremely limited intellisense, and crappy debugging. On the whole, I’ll stick with code-behind, but I might vacation in Inlineville from time to time.


Inline code pages clearly [have their place](https://web.archive.org/web/20050206002303/http://www.eggheadcafe.com/articles/20030518.asp); I use them mostly for utilities where ease of deployment into existing websites is the overriding concern. However, I do think you can also make a fairly compelling argument that **the current ASP.NET code-behind model is a bit too restrictive**; you end up with a humongous *web.dll* that has to be recompiled even if the tiniest bit of code in the most trivial web page in your solution changes. It’ll be interesting to see what kind of improved, hybrid behind/inline model we get in VS.NET 2005.

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[code-behind](https://blog.codinghorror.com/tag/code-behind/)
[inline code](https://blog.codinghorror.com/tag/inline-code/)
[aspx pages](https://blog.codinghorror.com/tag/aspx-pages/)
[web development](https://blog.codinghorror.com/tag/web-development/)
