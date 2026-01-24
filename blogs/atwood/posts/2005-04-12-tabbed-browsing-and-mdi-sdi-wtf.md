---
title: "Tabbed Browsing and MDI-SDI-WTF"
date: 2005-04-12
url: https://blog.codinghorror.com/tabbed-browsing-and-mdi-sdi-wtf/
slug: tabbed-browsing-and-mdi-sdi-wtf
word_count: 330
---

Cyrus bemoans the user interface [catastrophe known as tabbed browsing](https://web.archive.org/web/20051206001439/http://blogs.msdn.com/cyrusn/archive/2005/04/10/406971.aspx):


> *As far as I can tell, tabs just exist to violate the existing window management systems I have in the OSs I use. So all the built-in ways I know to use my system fly out the window (no pun intended).*


Well, Cyrus, I could go either way on tabbed UIs. My needs are much simpler: how about some **window management consistency in Microsoft’s own office suite?**


On one hand, you’ve got Word and Excel, which appear to be straight SDI. Or are they? As [Josh points out](http://flimflan.com/blog/), *not quite:*

kg-card-begin: html

> *
> Well, I don’t know what you’d call it, but I wouldn’t call it consistent.
> Open 2 documents in Word. Now open 2 documents in Excel.
> Both applications show 2 taskbar icons (seems SDI).
> Each app Windows menu lists the 2 open documents (seems MDI-ish).
> Now, click the top right X (close button) on a Word document. The current document closes.
> Now, click the top right X (close button) on an Excel document. BOTH Excel documents close.
> *

kg-card-end: html

Then you’ve got Microsoft Access, which has this bizarro hybrid MDI mode where every MDI window shows up in your windows taskbar, like so:


![](https://blog.codinghorror.com/content/images/2025/05/image-75.png)


As for Microsoft PowerPoint, I saved the weirdest for last. Unlike every other Office app, PowerPoint does not allow multiple instances. There can be only one PowerPoint, ever. And it gets weirder! Try opening two presentations and then clicking the “close application” button in the upper right corner of the PowerPoint window, as illustrated in this movie:


![PowerPoint movie](https://blog.codinghorror.com/content/images/uploads/2005/04/6a0120a85dcdae970b0120a86d4ab5970b-pi.gif)


When does “close application” not mean “close application”? Evidently whenever you have more than one document open in PowerPoint.


So here’s my question to Cyrus: how could tabbed interfaces be any worse than the complete and utter lack of window management consistency in Microsoft’s own office suite?

[user interface](https://blog.codinghorror.com/tag/user-interface/)
[tabbed browsing](https://blog.codinghorror.com/tag/tabbed-browsing/)
[mdi](https://blog.codinghorror.com/tag/mdi/)
[sdi](https://blog.codinghorror.com/tag/sdi/)
[window management](https://blog.codinghorror.com/tag/window-management/)
