---
title: "Multiple /bin folders in ASP.NET"
date: 2004-11-15
url: https://blog.codinghorror.com/multiple-bin-folders-in-aspnet/
slug: multiple-bin-folders-in-aspnet
word_count: 217
---

About a week ago, Scott Hanselman posted a neat tip on [deploying multiple /bin folders](http://www.hanselman.com/blog/PermaLink.aspx?guid=4d0ef4fb-f8ae-4355-a658-3c0432c98dbe) in an ASP.NET application. What’s really cool about this is that it lets you build a **pseudo plugin architecture into your existing ASP.NET website.**


Scott documents it perfectly; I’m here to tell you that I tried it, and it works. In my case the folder structure was like so:


![](https://blog.codinghorror.com/content/images/2025/06/image-73.png)


As you can see, I added a pre-compiled utility **WebFileManager** to the existing **Linktron5000** website by dropping it into a subfolder, binaries and all. To get this to work, all I had to do was make one small change to the parent app Web.config:

kg-card-begin: html

```
<runtime>
<assemblyBinding xmlns="urn:schemas-microsoft-com:asm.v1">
<probing privatePath="WebFileManager/bin" />
</assemblyBinding>
</runtime>
```

kg-card-end: html

This sets up the probing path for the child assemblies. If you don’t do this, you’ll get “Assembly not found” exceptions. You also have to make a slight modification to the child .aspx page header, but this modification is safe to make in the original source file and can be permanent:

kg-card-begin: html

```
<%@ Assembly Name="WebFileManager" %>
<%@ Page Language="vb" AutoEventWireup="false"
Codebehind="WebFileManager.aspx.vb" Inherits="WebFileManager.WebFileManager"%>
```

kg-card-end: html

Note that I didn’t need the additional namespace page directive because this assembly has no namespace. Great tip, Scott. Recommended!

[asp.net](https://blog.codinghorror.com/tag/asp-net/)
[plugin architecture](https://blog.codinghorror.com/tag/plugin-architecture/)
[deployment](https://blog.codinghorror.com/tag/deployment/)
[folder structure](https://blog.codinghorror.com/tag/folder-structure/)
[web.config](https://blog.codinghorror.com/tag/web-config/)
