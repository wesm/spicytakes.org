---
title: "C# Snippet Parity"
date: 2006-02-21
url: https://blog.codinghorror.com/c-snippet-parity/
slug: c-snippet-parity
word_count: 423
---

Microsoft recently released a complete set of [C# code snippets](https://web.archive.org/web/20060411133845/http://msdn.microsoft.com/vstudio/downloads/codesnippets/default.aspx) for Visual Studio 2005. This brings C# to parity with VB.NET, which had many more code snippets “in the box.”


Unfortunately, Microsoft’s installation strategy for these new snippets leaves a lot to be desired. You can download and “install” all the snippets at once, but you must manually add each of the snippet folders via the Snippet Manager (Ctrl+K, Ctrl+B). I loves me some snippets, but this is unacceptable!


The snippets themselves, of course, are just individual XML files that end in .snippet sitting in a bunch of folders. There are two valid snippet paths: per-user and system-wide. The system-wide C# snippet path is:

kg-card-begin: html

```
C:Program FilesMicrosoft Visual Studio 8VC#Snippets1033
```

kg-card-end: html

There’s an index file in that folder, `SnippetsIndex.xml`, which appears to store the snippet paths. You might think editing this file would cause the folders to appear in the snippet browser (Ctrl+K, Ctrl+X). Seems logical, right?


Unfortunately, it’s not that easy.


I think that file *may* be used the first time the IDE is initialized, but edits to that file don’t appear in the Snippet Manager.


The real snippet paths are stored in the registry at:

kg-card-begin: html

```
[HKCUSoftwareMicrosoftVisualStudio8.0LanguagesCodeExpansionsVisual C#]
```

kg-card-end: html

Why they chose to store this stuff in the registry *and* in an XML file is beyond me. Anyway, I packaged the correctly pathed snippets and a registry file together. Now you can quickly get the snippets installed on your system without running a pointless installer that does virtually nothing for you.


You can go from tired...


![](https://blog.codinghorror.com/content/images/2025/05/image-209.png)


... to wired...


![](https://blog.codinghorror.com/content/images/2025/05/image-210.png)


... in no time at all. If you’ve forgotten the keyboard shortcuts for snippets, revisit my [snippet blog entry](https://blog.codinghorror.com/code-snippets-in-vsnet-2005/) to refresh your memory.


Microsoft provides 295 new C# code snippets, and they’re 508 KB in total size. I chose to package the snippets as a 7zip file for compression efficiency:

- ZIP: 229kb
- RAR: 73kb
- 7Zip: 56kb


To be fair to ZIP, it probably would have done better if the format supported solid archiving for this set of small files.


To decompress the archive, I recommend switching to [WinRAR](http://www.rarlab.com/) if you aren’t already. It supports 7zip as well as RAR and ZIP, but more importantly, it won the [best archive tool DonationCoder roundup](http://www.donationcoder.com/Reviews/Archive/ArchiveTools/index.html). I’m not a huge fan of the UI, but I encounter RAR files often enough that WinZIP isn’t cutting it any more.


[Download C# snippets and registry file](https://web.archive.org/web/20060907231953/http://www.codinghorror.com/blog/files/ms-csharp-snippets.7z.zip) (60kb 7zip archive)

[c#](https://blog.codinghorror.com/tag/c-2/)
[visual studio](https://blog.codinghorror.com/tag/visual-studio/)
[snippets](https://blog.codinghorror.com/tag/snippets/)
[code snippets](https://blog.codinghorror.com/tag/code-snippets/)
