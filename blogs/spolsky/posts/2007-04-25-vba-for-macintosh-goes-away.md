---
title: "VBA for Macintosh goes away"
date: 2007-04-25
url: https://www.joelonsoftware.com/2007/04/25/vba-for-macintosh-goes-away/
word_count: 839
---


The first few versions of Excel (1.0 through 4.0) had a rudimentary macro programming capability using a programming language so embarassing that it never had a name, although it was sometimes called XLM (its file extension).


In 1991, Visual Basic 1.0 had just shipped to rave reviews. Combining a graphical UI builder similar to NeXTSTEP’s Interface Builder with a simple Basic programming language that was highly compatible with QuickBasic, it rapidly became the best selling programming language, a position it maintained until [droves of developers switched to web development](https://www.joelonsoftware.com/articles/APIWar.html).


Much as professional programmers sneer at the Basic programming language, market research unambiguously showed that about 2/3rds of the kinds of accidental programmers who develop macros preferred Basic to other languages and perceived it to be easy.


Thus, the obvious choice for Excel’s next macro language was some version of Visual Basic.


There were a bunch of complicated requirements, though. Excel was cross platform. The Mac version sold very well. To be a good Mac player, Microsoft had to support Apple’s cross-application scripting architecture, Apple Events. Rather than implement two object models, the Excel team concluded that the object model for Excel had to be Apple Events compatible. For complicated reasons, the Visual Basic engine wasn’t object oriented “enough.” In particular, objects could have properties, but those properties couldn’t, themselves, be objects. Visual Basic 1.0 didn’t support things like “rows(1).cells(2).value” because the row object couldn’t contain another object.


The VB team implemented an all-new version, for both Macintosh (System 7 on Motorola 68k) and Windows (3.0 on 16 bit processors). This became Visual Basic for Applications, and, soon thereafter, the standalone version, Visual Basic 4.0.


The whole effort took quite a bit of work. However, it was seen as extremely “strategic.” Here’s what that meant. Microsoft thought that if people wrote lots and lots of VBA code, they would be locked in to Microsoft Office. They thought that no matter how hard their competitors tried (in those days, they were Borland, Lotus, and, to a far lesser extent, Claris), they would not be able to emulate the VBA programming environment and the gigantic Excel object model perfectly. At some point, any Excel VBA macro they tried to run would get in trouble and crash. This is the same reason apps under Mono, Wine, etc. hardly ever work the first time out of the box: in any large API or programming interface, there are so many subtle, undocumented details of the behavior, which programmers may be depending on without even realizing it, that any emulation environment will inevitably be imperfect. In the brittle world of programming, such imperfections often mean your program crashes long before it does anything useful. You don’t get partial credit when you try to emulate an API.


In essence, in addition to giving Excel users a nice programming language, Microsoft was building a highly strategic barrier to entry, and locking in Excel users, especially corporate users who are most likely to build large systems based on macros.


Eventually, all the Office apps came along: Word, Project, Access, Outlook. What was a strategic lock-in for Excel grew to have major strategic value for the whole Office system.


Last August Microsoft decided to [drop VBA](http://www.macnn.com/articles/06/08/07/ms.kills.virtualpc/) from the Macintosh versions of Office. Despite [complicated technical explanations](http://www.schwieb.com/blog/2006/08/08/saying-goodbye-to-visual-basic/), every development decision like this is based on a cost/benefit analysis. Mac users are less likely than Windows users to have business-critical macros, simply because Macs are rarer in large business.


But what’s really interesting about this story is how Microsoft has managed to hoist itself by its own petard. By locking in users and then not supporting *their own lock-in features*, they’re effectively making it very hard for many Mac Office 2004 users to upgrade to Office 2008, forcing a lot of their customers to reevaluate which desktop applications to use. It’s the same story with VB 6 and VB.Net, and it’s the same story with [Windows XP and Vista](http://biz.yahoo.com/seekingalpha/070420/32947_id.html?.v=1). When Microsoft lost the backwards-compatibility religion that had served them so well in the past, they threatened three of their most important businesses (Office, Windows, and Basic), businesses which are highly dependent on upgrade revenues.


PS: in researching this article, I tried to open some of my notes which were written in an old version of Word for Windows. Word 2007 refused to open them for “security” reasons and pointed me on a wild-goose chase of knowledge base articles describing obscure registry settings I would have to set to open old files. It is extremely frustrating how much you have to run in place just to keep where you were before with Microsoft’s products, where every recent release requires hacks, workarounds, and patches just to get to where you were before. I have started recommending to my friends that they stick with Windows XP, even on new computers, because the few new features on Vista just don’t justify the compatibility problems.


PPS: I was a member of the Excel Program Management team from 1991-1993, where I wrote the spec for VBA for Excel.
