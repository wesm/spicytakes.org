---
title: "Firefox Excessive Memory Usage"
date: 2006-03-13
url: https://blog.codinghorror.com/firefox-excessive-memory-usage/
slug: firefox-excessive-memory-usage
word_count: 257
---

I like Firefox. I’ve even grown to like it slightly more than IE6, mostly because it has a far richer add-on ecosystem.


But I have one serious problem with Firefox:


![](https://blog.codinghorror.com/content/images/2025/05/image-229.png)


This screenshot was taken after a few days of regular Firefox usage. That’s **over 900 megabytes of memory for a single, non-tabbed instance of Firefox**.


What’s going on? Well, according to my tests, **Firefox never seems to release any of the memory it uses – until you close *all* instances of Firefox.** If you spend enough time browsing the web, and never close Firefox completely, you’ll consume nearly a gigabyte of memory!


Because I often keep at least one browser window open for research or reminder purposes, this bites me *a lot*. I’ll look at Task Manager and Firefox will **regularly be gobbling up over 400 megabytes**. This isn’t uncommon. It’s normal.


I don’t ever recall having this problem with IE 6.


Of course, I can close all instances of Firefox and reduce memory usage back to zero, but why should I have to? I’ve read the techweb news article on the controversy around Firefox and memory usage, and I’ve implemented the workaround suggested in that article:

1. Within Firefox, enter “about:config” (minus the quotation marks) in the address bar.
2. Scroll down to the entry “browser.sessionhistory.max_total_viewers” and double-click it.
3. In “Enter integer value” field, type...


Sadly, this fix did very little to address the problem. The above screenshot was taken *after* setting that value to 1!f

[browser](https://blog.codinghorror.com/tag/browser/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
[firefox](https://blog.codinghorror.com/tag/firefox/)
[web browser](https://blog.codinghorror.com/tag/web-browser/)
[memory usage](https://blog.codinghorror.com/tag/memory-usage/)
