---
title: "DirectX Version Number Abuse"
date: 2006-08-20
url: https://blog.codinghorror.com/directx-version-number-abuse/
slug: directx-version-number-abuse
word_count: 179
---

Has anyone noticed that Microsoft defines “version” a little loosely when it comes to DirectX 9.0c? Here’s a screenshot of the [DirectX 9.0c download page](http://www.filehippo.com/download_directx/) on FileHippo:


![](https://blog.codinghorror.com/content/images/2025/04/image-759.png)


DirectX 9.0c was originally released in August 2004, according to [the DirectX Wikipedia entry](http://en.wikipedia.org/wiki/DirectX). But Microsoft has surreptitiously been updating DirectX 9.0c since August 2005 *without incrementing the version number.*


> It is not known why Microsoft has not used new version numbers for the updates to DX9.0c – including the December 2005 update versioning could now be at DX9.0j, although this is nowhere reflected in the internal code.


So do you want version 9.0c, 9.0c, 9.0c, or perhaps... 9.0c?


The versions are all fully backwards compatible, of course, but **why is Microsoft abusing version numbers this way?**


It’s impossible to tell what version of DirectX 9.0 you’re actually running. I've installed several games over the past year which inexplicably demanded to re-install DirectX 9.0c; now I know why.


At least Vista stops the madness by finally changing the [version number to DirectX 9.0L](https://web.archive.org/web/20060830050020/http://www.theinquirer.net/default.aspx?article=26220).

[directx](https://blog.codinghorror.com/tag/directx/)
[microsoft](https://blog.codinghorror.com/tag/microsoft/)
[versioning](https://blog.codinghorror.com/tag/versioning/)
[backwards compatibility](https://blog.codinghorror.com/tag/backwards-compatibility/)
[software development](https://blog.codinghorror.com/tag/software-development/)
