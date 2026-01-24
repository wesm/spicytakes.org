---
title: "Showstopper!"
date: 2004-08-23
url: https://blog.codinghorror.com/showstopper/
slug: showstopper
word_count: 1156
---

A friend of mine recently returned the book [Showstopper!](http://www.amazon.com/exec/obidos/ASIN/0029356717/) after an extended loan. If you haven’t heard of this book, allow me to quote the Amazon.com editorial summary:


> Showstopper! is a vivid account of the creation of Microsoft Windows NT, perhaps the most complex software project ever undertaken. It is also a portrait of David Cutler, NT’s brilliant and, at times, brutally aggressive chief architect.
> Cutler surely ranks as one of the most impressive software engineers the field has ever produced. After leading the team that created the VMS operating system for Digital’s VAX computer line – an accomplishment that most would regard as a lifetime achievement – he went on to conceive and lead the grueling multi-year project that ultimately produced Windows NT. Both admired and feared by his team, Cutler would let nothing stand in the way of realizing his design and often clashed with his programmers, senior Microsoft management, and even Gates himself.


I hadn’t looked at this book since I originally read it in 1996, and I found myself casually skimming through it, eventually re-reading the entire thing. It's a critical part of Microsoft’s history. Think about where Microsoft would be if the NT project, which began way back in 1988, had failed. Can you imagine running some variant of Windows 95 today?


It’s also interesting to note that **nobody is writing new operating systems any more**. The world has devolved into UNIX and NT camps exclusively. Without NT, I think we’d all be running UNIX at this point, for better or worse. It certainly happened to Apple; their next-generation [Copland OS](http://en.wikipedia.org/wiki/Copland?) never even got off the ground. And now they’re using [OS X](http://en.wikipedia.org/wiki/Mac_OS_X) which is based on Unix. There are some uncanny observations in the book that foreshadow this divide:


> Besides, NT would still meet the goals closest to Cutler’s heart: portability, reliability, and the ability to provide an alternative to Unix, the splintered high-end operating program.
> The last goal was crucial to Cutler. “Unix is like Cutler’s lifelong foe,” said one team member who’d worked with Cutler for nearly two decades. “It’s like his Moriarty [Sherlock Holmes’s nemesis]. He thinks Unix is a junk operating system designed by a committee of Ph.D.s. There’s never been one mind behind the whole thing, and it shows, so he’s always been out to get Unix. But this is the first time he’s had the chance.”


In many ways, the story of Windows NT is the story of [Dave Cutler](http://en.wikipedia.org/wiki/Dave_Cutler): he comes across as the **Ted Nugent anti-hero of software architects**. There are some very amusing anecdotes in the book about his gonzo management style:


> In truth, nobody worried about Rashid’s etiquette. Of all people, Cutler deserved indelicate treatment. Other Microsoft leaders viewed him as a bully. One senior executive usually responded to a Cutler complaint with the succint statement, “Fuck Dave.” When asked why, the executive excused his boorishnes with the reply, “Cutler tells me to fuck off all the time.”


Cutler keeps an incredibly low profile today, which is strange for an architect of his stature. You won’t find many interviews or articles about him. In fact, he still works at Microsoft today, and he was a key reason the 64-bit version of Windows XP even exists in the face of lackluster Intel support for 64-bit x86 extensions.


There are some interesting themes in the book that emerged after a second reading:

- **Eating your own dogfood.** I’ve long been a proponent of this technique. [Dogfooding keeps you honest](https://blog.codinghorror.com/the-difficulty-of-dogfooding/). NT development was perhaps the ultimate dogfood scenario: developing a new OS using the current build of that OS.
- **The importance of R&D**. By the time NT was truly viable on the desktop (Windows 2000), it was ten years after the initial 1989 design spec. This speaks volumes about strategic direction and R&D: if large corporations aren't actively planning ten years out, they’re probably not going to last very long. Nathan Myrhvold presents a document to Bill Gates on page 31 that outlines the risk of Unix, portable code, and RISC – all “DOS killers” – that was absolutely prophetic in hindsight.
- **Process vs. People**. It’s shocking how little formal process was involved in the development of NT. Microsoft didn’t really manage much at all: they just chose to build the company with the smartest people they could find and let them figure it out. This may sound surprising, but it clearly worked for NT, a project of almost unimaginable complexity. More supporting data on this can be found in McConnell’s [Quantifying Soft Factors](http://www.stevemcconnell.com/ieeesoftware/eic14.htm) editorial.
- **The importance of senior architectural oversight**. Cutler goes to great lengths to prevent people from optimizing for x86 in the early development of NT, despite the intense pressure to do so for performance reasons. He intuitively knew that sacrificing portability this early would cripple the future design of the OS. Although, ironically, there’s nothing left but x86 – the Alpha, Mips, PPC versions of NT were all discontinued due to lack of market demand – the NT kernel has evolved and survived, and now lives on the desktops of millions of everyday users, not just “power users.”
- **If it sounds like a bad idea, it probably is**. e.g., [Cairo](https://web.archive.org/web/20040703090327/http://www.winnetmag.com/Windows/Article/ArticleID/48/48.html). This was supposed to be Jim Allchin’s “vision” for next version of NT, what ultimately became NT 4.0. What the hell was Microsoft thinking? If you can’t explain what you plan to do in practical, meaningful terms – you’re probably full of crap. I can certainly empathize with Dave’s skepticism about Cairo, and in retrospect, he was correct. Cairo never went anywhere.


One of the last things Dave Cutler mentions in the book resonated with me:


> The end of a project was always a difficult time for him. He always pushed to outdo himself, never lingering for long over his achievements and eschewing any examination of his motives and psychology. “My motivation is I like to do this stuff. I just like to do this stuff,” he said. “I like to get [my code] done and see it work.” Rather than monumental, his concept was Sisyphean. He dared not speculate about the benefit of his labors for society. Nor did he concern himself with his place in the history of technology. He only looked forward, abolishing the past as he went on. “This isn’t the end,” he said. **“Ten years from now we’ll be designing another system, and everyone will be sitting around bemoaning that it will have to be compatible with NT. That will happen.”**


I am not so sure. Unix is 30 years old and would unquestionably rule today’s desktop if not for the existence of NT. Is it unreasonable to expect the NT kernel to last as long? In fact, I think it’s possible we may not see another “from the ground up” OS developed in our lifetimes.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[software architecture](https://blog.codinghorror.com/tag/software-architecture/)
