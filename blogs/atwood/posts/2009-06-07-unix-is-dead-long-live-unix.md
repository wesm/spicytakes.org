---
title: "Unix is Dead, Long Live Unix"
date: 2009-06-07
url: https://blog.codinghorror.com/unix-is-dead-long-live-unix/
slug: unix-is-dead-long-live-unix
word_count: 648
---

[Unix turns 40](https://web.archive.org/web/20090607080644/http://www.computerworld.com/action/article.do?command=printArticleBasic&taxonomyName=Operating+Systems&articleId=9133570&taxonomyId=89): The past, present and future of a revolutionary OS is fascinating reading.

kg-card-begin: html

> Forty years ago this summer, a programmer sat down and knocked out in one month what would become one of the most important pieces of software ever created.
> In August 1969, [Ken Thompson](http://en.wikipedia.org/wiki/Ken_Thompson) (pictured at left), a programmer at AT&T subsidiary Bell Laboratories, saw the month-long departure of his wife and young son as an opportunity to put his ideas for a new operating system into practice. He wrote the first version of Unix in assembly language for a wimpy Digital Equipment Corp. (DEC) PDP-7 minicomputer, spending one week each on the operating system, a shell, an editor, and an assembler.

kg-card-end: html

The article is accompanied by [a graph from wikipedia](http://commons.wikimedia.org/wiki/File:Unix_history-simple.png), illustrating the lineage of the Unix family.


![](https://blog.codinghorror.com/content/images/2025/04/image-385.png)


To me, Unix has become synonymous with [Linux](http://en.wikipedia.org/wiki/Linux), and the open source movement in general. The last *nixes standing shake out as follows:

kg-card-begin: html


| **Open Source** | **Mixed / Shared Source** | **Closed Source** |
| Minix
Linux
FreeBSD
NetBSD
OpenBSD
OpenSolaris | Mac OS X | AIX
OpenServer
HP/UX |


kg-card-end: html

I didn’t realize there were that many closed source Unix variants still surviving in the wild. It’s also odd how OS X brings us full circle with the original Unics and BSD licensing. If it’s lonely in the “Closed” column, imagine the existential angst of being the only vendor in the “Mixed / Shared Source” column. (NB: I think the currently tiny category Apple occupies represents the future of commercial software, but that’s a topic for another blog post.)


I’ve been primarily a Windows developer since the early 90s, but over time, **I’ve developed a grudging **[**respect**](https://blog.codinghorror.com/is-worse-really-better/)** for Unix**. I think Michael Feathers [summarized it best](http://beautifulcode.oreillynet.com/2008/01/on_loving_c.php):


> There’s something deep in software development that not everyone gets but the people at Bell Labs did. It’s the undercurrent of “the New Jersey Style,” “Worse is Better,” and “the Unix philosophy” – and it’s not just a feature of Bell Labs software either. You see it in the original Ethernet specification where packet collision was considered normal... and the same sort of idea is deep in the internet protocol. It’s deep awareness of design ramification – **a willingness to live with a little less to avoid the bigger mess and a willingness to see elegance in the real rather than the vision**.


I find this to be deeply and profoundly true in everything I’ve ever worked on as a programmer, and to the extent that Unix reflects these philosophies, it is undeniably on the right path. Unlike Rich Skrenta, I didn’t grow up [as a Unix developer](https://web.archive.org/web/20090612203932/http://www.skrenta.com/2007/05/giving_up_on_microsoft.html), so I have come late in life to this appreciation. Joel Spolsky’s take on the Unix / Windows divide, after reading [The Art of UNIX Programming](http://www.amazon.com/dp/0131429019), is [this](http://www.joelonsoftware.com/articles/Biculturalism.html):


> What are the cultural differences between Unix and Windows programmers? There are many details and subtleties, but for the most part it comes down to one thing: Unix culture values code which is useful to other programmers, while Windows culture values code which is useful to non-programmers. This is, of course, a major simplification, but really, that’s the big difference: are we programming for programmers or end users? Everything else is commentary.


So on one side, you have hundreds of command line applications, built in wildly different styles, with thousands of arcane command line parameters, all of which can be flexibly combined together to accomplish almost anything. And on the other side, you have the [windows registry](https://blog.codinghorror.com/was-the-windows-registry-a-good-idea/) and [MFC](http://en.wikipedia.org/wiki/Microsoft_Foundation_Class_Library).


Sometimes, [you just can’t win](https://blog.codinghorror.com/because-they-all-suck/).


So, yes, I’m a fan of Unix. And I’m also a fan of Windows. I think it’s worth studying what both are getting right and wrong, because as a programmer, I’m a fan of whatever the heck *works*.

[unix](https://blog.codinghorror.com/tag/unix/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[linux](https://blog.codinghorror.com/tag/linux/)
[software development](https://blog.codinghorror.com/tag/software-development/)
