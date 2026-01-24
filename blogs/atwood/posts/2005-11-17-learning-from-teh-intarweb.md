---
title: "Learning from TEH INTARWEB"
date: 2005-11-17
url: https://blog.codinghorror.com/learning-from-teh-intarweb/
slug: learning-from-teh-intarweb
word_count: 496
---

I try to avoid posting entries from the [Mindless Link Propagation Department](http://www.25hoursaday.com/weblog/CategoryView.aspx?category=Mindless%20Link%20Propagation), but Adam Bosworth’s article [Learning from The Web](https://web.archive.org/web/20060315023532/http://acmqueue.com/modules.php?name=Content&pa=showpage&pid=337&page=1) is excellent and it deserves a careful read:

kg-card-begin: html

> *
> The Web taught us several unintuitive lessons:
> Simple, relaxed, sloppily extensible text formats and protocols often work better than complex and efficient binary ones
> It is worth making things simple enough that one can harness Moore’s law in parallel
> It is acceptable to be stale much of the time
> The wisdom of crowds works amazingly well
> People understand a graph composed of tree-like documents (HTML) related by links (URLs).
> Pay attention to physics
> Be as loosely coupled as possible.
> KISS. Keep it (the design) simple and stupid
> *

kg-card-end: html

In addition to all the architectural stuff Adam outlines, we can’t overlook the critical contribution of web browser user interface. **The browser popularized the web by making it dead simple to use**:

- The entire interface is driven by a **single mouse click**. Nary [a double-click in sight!](https://blog.codinghorror.com/double-click-must-die/) And none of the interface is obscured behind things like drop-down menus; it’s all immediately visible and immediately clickable.
- **The back button**. Easily the most profound innovation in user interface in the last ten years. Don’t like where you are? Go back to where you were. It’s totally natural.
- Each webpage **focuses on a single task**. Since websites are slow to load and can’t display much at once, designers were forced to stick to one task per page, along with a palette of relevant tasks for that activity. A refreshing change of pace from your typical monolithic application with its monster twenty-item cascading main menu.


These “webby” UI characteristics are now collectively known as [Inductive User Interface](https://blog.codinghorror.com/defending-perpetual-intermediacy/), and figure prominently in many newer client applications and operating systems.


Adam also defines some of the shortcomings of XML, and in the process, **proposes** **RSS as an all-out replacement for XML**:


> *Some of us learned these lessons seven or eight years ago and applied them to distributed computing. We had the explicit goal of using XML over HTTP to exchange information between applications via messages to build a loosely coupled, robust, Web-friendly model for distributed computing. In my humble opinion, however, we ignored or forgot lessons 3, 4, and 5.
> RSS 2.0 has reached the tipping point where it is universally understood. [. . .] It may well be that a lot of useful information is going to flow over the Web as either RSS 2.0 or Atom (or both, depending on the type the requester asks for). It addresses many of the serious limitations or outages in XML today.*


The last section on databases reads like a logical continuation of the “RSS defeats XML” thought, and more specifically, an argument in favor of [Google Base](http://blog.outer-court.com/archive/2005-11-16-n68.html). Did I mention that Adam works for Google?

[web technologies](https://blog.codinghorror.com/tag/web-technologies/)
[programming paradigms](https://blog.codinghorror.com/tag/programming-paradigms/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
[crowd wisdom](https://blog.codinghorror.com/tag/crowd-wisdom/)
