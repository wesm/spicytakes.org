---
title: "Pushing Operating System Limits"
date: 2007-10-01
url: https://blog.codinghorror.com/pushing-operating-system-limits/
slug: pushing-operating-system-limits
word_count: 871
---

Raymond Chen notes that if you have to ask where the operating system limits are, you’re [probably doing something wrong](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2007/03/01/1775759.aspx):


> If you're nesting windows [more than 50 levels deep](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2003/12/18/44379.aspx) or nesting menus [more than 25 levels deep](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2003/12/30/46594.aspx) or creating a dialog box with [more than 65535 controls](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2004/06/21/161375.aspx), or nesting tree-view items more than 255 levels deep, then your user interface design is in serious need of rethought, because you just created a usability nightmare.
> If you have to ask about the maximum number of [threads a process can create](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2005/07/29/444912.aspx) or the maximum [length of a command line](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2003/12/10/56028.aspx) or the maximum [size of an environment block](https://web.archive.org/web/20071011235956/http://blogs.msdn.com/oldnewthing/archive/2006/07/06/657868.aspx) or the maximum amount of data you [can store in the registry](https://web.archive.org/web/20071011235956/http://support.microsoft.com/kb/256986/), then you probably have some rather serious design flaws in your program.
> I'm not saying that knowing the limits isn't useful, but in many cases, if you have to ask, [you can't afford it](https://web.archive.org/web/20071011235956/http://listserv.linguistlist.org/cgi-bin/wa?A2=ind0405c&L=ads-l&P=12106).


In general, I agree with Raymond. Asking these kinds of questions definitely raises red flags. Edge conditions should never be a goal, and if your design is skirting that close to an operating system edge condition, you’re either doing something incredibly brilliant or incredibly stupid. Guess which one is [more common?](http://worsethanfailure.com/)


However, it can also be surprising **how quickly you can run into operating system limits –** even when you’re not doing anything that unusual.


When researching blog posts, I tend to open a lot of browser windows and tabs. At least twice per week, I have so many browsers and tabs open that I run into some internal limitation of the browser and I can’t open any more. My system gets a little wonky in this state, too: right-clicking no longer shows a menu, and I’m prevented from launching other applications. But if I close a few errant browser windows or tabs, everything goes back to normal.


I [prefer to use Internet Explorer](https://blog.codinghorror.com/non-native-ui-sucks/) for day-to-day browsing chores, but it appears that IE 7 is particularly vulnerable to these limitations. I ran a quick test in which I opened as many instances of the Yahoo home page as I could, with nothing else running:

kg-card-begin: html


| Maximum number of IE7 windows I can open | **39** |
| Maximum number of IE7 tabs I can open | **47** |


kg-card-end: html

I don’t think having 47 typical web pages open, spread across a couple instances of Internet Explorer on my three monitors, is so unreasonable. And yet that’s a hard limit I run into on a semi-regular basis. It’s annoying. It looks like IE6 had a similar limit; Theodore Smith found that [he could only open 38 pages](https://web.archive.org/web/20071008230558/http://www.incendiary.ws/node/177) before new windows were frozen. Firefox fares quite a bit better in the same test:

kg-card-begin: html


| Maximum number of Firefox 2 windows I can open | **55** |
| Maximum number of Firefox 2 tabs I can open | **100+** |


kg-card-end: html

These aren’t hard limits in Firefox; they’re practical limits. After I opened 55 Firefox windows, Vista automatically kicked me into Vista Basic mode due to Aero performance degradation. I was unable to close all the instances of Firefox, and I had to kill the task. Tabs worked better; I got bored opening new Yahoo homepage tabs after about seventy and gave up. I was able to close all the tabs without incident. I’m guessing you could have at least a hundred tabs open in Firefox before something suitably weird happened.


So we’ve learned that Internet Explorer sucks, right? Maybe. The results I saw are largely due to a key architectural difference between the two browsers. IE allows you to choose between opening web pages in the same iexplore.exe process (Open New Tab, Open New Window), or opening web pages in a new, isolated instance of iexplore.exe. **Unlike IE, Firefox only allows one Firefox.exe process, ever.** This clearly helps it scale better. But there is a downside: if any web page crashes, it will take down the entire firefox.exe process and every other web page you have open.


I understand the need for practical limits in the operating system. Most of the limits Raymond cites are so high that they’re borderline absurd. Can you imagine subjecting a user to a menu with 254 nesting levels? Open a zillion copies of notepad, and you’ll eventually have problems, too. I get that. The point is to **keep those operating system limits far enough above typical usage that developers and users – even power users – aren’t likely to run into them**.


I’m not sure if we’re running into an application or operating system limit here; I suspect a little bit of both. Still, I’m disappointed. A limit of only 47 tabbed web pages open at any time under Internet Explorer 7 seems artificially and unacceptably low to me. The introduction of the tabbed browsing metaphor makes it much more likely that users will open lots of web pages at the same time. I’d expect the developers on the IE team to test their application for moderately heavy usage scenarios like this. It’s another case of failing to test with [a reasonably large data set](https://blog.codinghorror.com/everything-is-fast-for-small-n/).

[operating system limits](https://blog.codinghorror.com/tag/operating-system-limits/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[usability concerns](https://blog.codinghorror.com/tag/usability-concerns/)
[system design](https://blog.codinghorror.com/tag/system-design/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
