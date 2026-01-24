---
title: "Side by side issues"
date: 2004-08-18
url: https://blog.codinghorror.com/side-by-side-issues/
slug: side-by-side-issues
word_count: 354
---

This is something of a dying art, since Microsoft is doing their level best to pretend that .NET 1.0 doesn’t exist any more – but here are a few key utilities you’ll need when running .NET 1.0 and 1.1 side by side.


Each website on an IIS server must be bound to a specific .NET runtime; [this GUI utility](https://web.archive.org/web/20040718070215/http://www.denisbauer.com/NETTools/ASPNETVersionSwitcher.aspx) lets you quickly bind a website to the .NET version of your choices. Bear in mind that **as a developer you’re very likely to be running the crippleware version of IIS** which only allows a single website, and at most 10 connections (40 with registry hack) to that website. But on Server 2000 or Server 2k3, you can have as many websites as you like.


The language changes between .NET 1.0 and 1.1 are minimal, and in most cases you can actually load a VS.NET 2003 project in VS.NET 2002 without any problems, and vice versa. [This solution conversion utility](https://web.archive.org/web/20040715085358/http://www.codeproject.com/macro/vsconvert.asp) allows you to convert a VS.NET solution back and forth between 2002 and 2003 formats at will. You may want to check out [the author’s blog](https://web.archive.org/web/20040606002432/http://www.dacris.com/blog/) as well; not many posts, but some are rather interesting:

kg-card-begin: html

> **.NET - Blacklisted APIs - “The functions you were never meant to call” ** 
> Screen.GetWorkingArea() - Use instead, Screen.PrimaryScreen.WorkingArea (For some reason, GetWorkingArea takes 25 ms to complete).
> Application.DoEvents() - The call of the devil.
> Control.RecreateHandle() - There’s no reason why you should ever need to use this.
> Application.EnableVisualStyles() - Use a manifest. .NET 1.1 just doesn’t implement this function right.
> NativeWindow.ReleaseHandle() - Contains some nasty bugs.

kg-card-end: html

I had no idea high school seniors were this smart. :)


Also, this won’t affect many of you, but any .NET assemblies instantiated via an <OBJECT> tag in HTML will always always bind to the latest version of the .NET runtime on the machine. There is no concept of side by side for assemblies loaded this way. Shocking, but true. I would strongly advise against building object tag “deployed” .NET apps for anything non-trivial.

[.net 1.0](https://blog.codinghorror.com/tag/net-1-0/)
[.net 1.1](https://blog.codinghorror.com/tag/net-1-1/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[iis](https://blog.codinghorror.com/tag/iis/)
[gui utility](https://blog.codinghorror.com/tag/gui-utility/)
