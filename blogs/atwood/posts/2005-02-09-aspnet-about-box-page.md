---
title: "ASP.NET About Box (Page)"
date: 2005-02-09
url: https://blog.codinghorror.com/aspnet-about-box-page/
slug: aspnet-about-box-page
word_count: 217
---

I had a request for an ASP.NET version of my [windows forms About Box](https://blog.codinghorror.com/about-the-about-box/). This is a good idea that I’ve considered in the past, so I took the time to convert it today:


![](https://blog.codinghorror.com/content/images/2025/05/image-47.png)


Clicking details will provide a dump of all loaded assemblies in summary form, with links to the full list of the attributes for each assembly – **exactly the same information the windows forms version provides**.


The main page is a HTML template; you can make it look however you want by modifying the markup – no recompilation required. To display entry assembly attributes, use the named properties defined in the About class, e.g., `Version <%=Version%>`, or call `EntryAssemblyAttrib(key)` with any arbitrary attribute key you want to display.


Oh, and [populate your damn assembly attributes](https://blog.codinghorror.com/populate-your-assemblyinfo/), because that’s where all this information is automatically derived from:

kg-card-begin: html

```
<Assembly: AssemblyTitle("About Page Demo")>
<Assembly: AssemblyDescription("A website demonstrating the About page")>
<Assembly: AssemblyCompany("Atwood Heavy Industries")>
<Assembly: AssemblyProduct("Demos")>
<Assembly: AssemblyCopyright(" 2005, Atwood Heavy Industries")>
<Assembly: AssemblyTrademark("All Rights Reserved")>
```

kg-card-end: html

I don’t think this is enough to justify another CodeProject article, so I’ll host it here and link it from the [comments in the original article](https://web.archive.org/web/20050310033510/http://www.codeproject.com/vb/net/aboutbox.asp).


Download the [ASP.NET About Page VS.NET 2003 project](https://web.archive.org/web/20060501133956/http://www.codinghorror.com/blog/files/AboutPage.zip) (12kb)

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[html template](https://blog.codinghorror.com/tag/html-template/)
[asp.net version](https://blog.codinghorror.com/tag/asp-net-version/)
[asp.net about box](https://blog.codinghorror.com/tag/asp-net-about-box/)
