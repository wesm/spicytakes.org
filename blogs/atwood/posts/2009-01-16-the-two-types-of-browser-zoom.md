---
title: "The Two Types of Browser Zoom"
date: 2009-01-16
url: https://blog.codinghorror.com/the-two-types-of-browser-zoom/
slug: the-two-types-of-browser-zoom
word_count: 583
---

From the dawn of the web – at least since Netscape Navigator 4.x – it has been possible to resize the text on a web page. This is typically done through the View menu.


![](https://blog.codinghorror.com/content/images/2025/04/image-274.png)


This was fine in the early, primitive days of the web, when page layouts were simple and unsophisticated. Want the font to be three times larger? No problem! Pump it up until your eyes bleed; you’re unlikely to break the design, because there’s precious little *design* at all.


![](https://blog.codinghorror.com/content/images/2025/04/image-273.png)


But this was a time long before the web had become a platform for [full-blown applications](https://blog.codinghorror.com/who-killed-the-desktop-application/), with complex, dense, almost GUI-like designs.


The accepted web design guidance is that you should generally produce web page layouts that work at:

1. the default font size (obviously)
2. one size *below* the default font size
3. one size *above* the default font size


I agree, and you should be testing for this on your own websites. The handy keyboard equivalents in most browsers are:


Ctrl + 0   Reset font size to default


Ctrl + +   Make font one size larger


Ctrl + -   Make font one size smaller


(yes, holding down the Ctrl key and then scrolling your mouse scroll wheel works, too, but no real programmer [would use that](https://blog.codinghorror.com/going-commando-put-down-the-mouse/).)


It is important to let the user control their browsing experience. But I think that **the traditional method of font-only browser sizing is a solution whose time has come and gone**. There’s a better way. Opera was the first browser to introduce **full page zoom** as an alternative to traditional font sizing, but Firefox 3 is where most people actually experience it. In fact, in Firefox 3, it’s the *default* page sizing mode.


![](https://blog.codinghorror.com/content/images/2025/04/image-272.png)


Note that “Zoom Text Only” is unchecked. And for good reason. Compare for yourself. Here’s the Digg homepage using old-school Netscape 4.x style font scaling.


**Browser Font Scaling: Default**


![](https://blog.codinghorror.com/content/images/2025/04/image-271.png)

kg-card-begin: html

**Browser Font Scaling: Size +1**

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/04/image-270.png)

kg-card-begin: html

**Browser Font Scaling: Size +2**

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/04/image-269.png)


Digg follows the design rule of thumb I suggested above: it scales to font size +1, but beyond that, all bets are off. With the fonts at +2, the top menu is scrunched, the search box clipped, and the digg numbers are spilling out over the boxes. The “most recent” navigation element has completely disappeared! Now compare this with the newer method of full page zooming:


**Browser Full Page Zoom Scaling: Default**


![](https://blog.codinghorror.com/content/images/2025/04/image-268.png)

kg-card-begin: html

**Browser Full Page Zoom Scaling: Size +1**

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/04/image-267.png)

kg-card-begin: html

**Browser Full Page Zoom Scaling: Size +2**

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/04/image-266.png)


While the page does get wider, the full page zoom method has tremendous advantages:

1. Full page zoom works on almost every web page in the world, with no changes whatsoever by the web designers
2. Full page zoom scales far, *far* beyond the +1/-1 sizes that you can reasonably expect from traditional browser font sizing approaches.


To prove that full page zoom scales like nobody’s business, here’s a screenshot I captured of the Digg homepage scaled to fit the entire [width of my 1920 x 1080 monitor](https://web.archive.org/web/20090213055648/http://www.codinghorror.com/blog/images/digg-page-zoom-max-256.png). In comparison, increasing the fonts beyond +2 results in a jumbled, unreadable mess.


Honestly, I can’t see much use for traditional browser font sizing. It’s increasingly fragile on today’s web. I wish more browsers would take the lead from Firefox 3, and **adopt full page zoom as the new default page sizing method**.

[web development](https://blog.codinghorror.com/tag/web-development/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[browser zoom](https://blog.codinghorror.com/tag/browser-zoom/)
[web design](https://blog.codinghorror.com/tag/web-design/)
[typography](https://blog.codinghorror.com/tag/typography/)
