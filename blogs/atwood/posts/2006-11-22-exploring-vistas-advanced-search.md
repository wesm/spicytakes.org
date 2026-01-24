---
title: "Exploring Vista’s Advanced Search"
date: 2006-11-22
url: https://blog.codinghorror.com/exploring-vistas-advanced-search/
slug: exploring-vistas-advanced-search
word_count: 453
---

I used the file search function in Windows XP a lot, particularly to find groups of files. But the XP search syntax doesn’t work in Vista. Vista uses the [Windows Desktop Search query syntax](https://web.archive.org/web/20061207042018/http://www.microsoft.com/windows/desktopsearch/addresources/advanced.mspx). Which means


“*.vbproj;*.csproj”


becomes


“ext:(*.vbproj OR *.csproj)”


![](https://blog.codinghorror.com/content/images/2025/05/image-419.png)


Note that the boolean operator *must* be in all-caps to work. That was painful to figure out.


I highly recommend reading through the Windows Desktop Search advanced query reference. First of all, it’s completely different than searching in XP, so you’ll need to retrain your brain. But it’s also a far richer search paradigm than we ever had in XP. And you can **use** **the same CTRL+E search keyboard shortcut** that works in your browser to harness its power in Windows Explorer.


When you perform a search, note that the Search Tools menu is available; that’s our main interface for all the new search options.


![](https://blog.codinghorror.com/content/images/2025/05/image-420.png)


From here, you can bring up the Search Pane, which lets you filter your searches to particular file types, and includes an expandable Advanced Search pane.


![](https://blog.codinghorror.com/content/images/2025/05/image-421.png)


As you fill in values in the Advanced Search pane and click Search, the equivalent query terms will be populated in the CTRL+E search box. It’s a good way to learn basic search syntax. Once you’ve learned the new Vista search syntax, you won’t need the Search Pane training wheels any more; you can press CTRL+E and type in what you want. It’s Google-icious.


There’s also an important distinction between indexed search locations and non-indexed search locations. To see the difference, choose “Search Options” from the Search Tools menu.


![](https://blog.codinghorror.com/content/images/2025/05/image-422.png)


Most notably, **your search terms will only extend to file contents in indexed locations**. I’m also very glad to see search now ignores compressed files by default. This was a real pain in XP, which insisted on digging through 600 megabyte ZIP files as a part of any search.


To view indexed locations, or add your own, select Modify Index Locations from the Search Tools menu. On a default Vista install, there are only three indexed locations:

- Offline Files
- c:Program DataMicrosoftWindowsStart Menu
- c:Users


There is one big caveat here: **the full-text indexer only indexes file extensions that it understands**. To view or modify the list of file extensions the indexer understands, click the Advanced Options button on the Modify Index Locations dialog, then select the File Types tab.


![](https://blog.codinghorror.com/content/images/2025/05/image-423.png)


Perhaps the coolest new search feature is that **you can enter searches directly from the Windows start menu**. Try it. Hit the Windows key and just start typing search queries. There’s nothing to install, nothing to configure, searching *just works* in Vista. It’s about time.

[windows desktop search](https://blog.codinghorror.com/tag/windows-desktop-search/)
[search syntax](https://blog.codinghorror.com/tag/search-syntax/)
[query syntax](https://blog.codinghorror.com/tag/query-syntax/)
[advanced search](https://blog.codinghorror.com/tag/advanced-search/)
[windows explorer.](https://blog.codinghorror.com/tag/windows-explorer/)
