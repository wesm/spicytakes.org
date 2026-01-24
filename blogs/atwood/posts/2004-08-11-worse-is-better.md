---
title: "Worse Is Better"
date: 2004-08-11
url: https://blog.codinghorror.com/worse-is-better/
slug: worse-is-better
word_count: 839
---

Although it's a little hard to parse through, I was blown away by [The Rise of “Worse is Better”](https://web.archive.org/web/20040619155500/http://www.jwz.org/doc/worse-is-better.html), because it touches on a theme I've noticed emerging in my blog entries: **rejection of complexity**, even when complexity is the more theoretically correct approach.


> *Two famous people, one from MIT and another from Berkeley (but working on Unix) once met to discuss operating system issues. The person from MIT was knowledgeable about ITS (the MIT AI Lab operating system) and had been reading the Unix sources. He was interested in how Unix solved the PC loser-ing problem. The PC loser-ing problem occurs when a user program invokes a system routine to perform a lengthy operation that might have significant state, such as IO buffers. If an interrupt occurs during the operation, the state of the user program must be saved. Because the invocation of the system routine is usually a single instruction, the PC of the user program does not adequately capture the state of the process. The system routine must either back out or press forward. The right thing is to back out and restore the user program PC to the instruction that invoked the system routine so that resumption of the user program after the interrupt, for example, re-enters the system routine. It is called “PC loser-ing” because the PC is being coerced into “loser mode”, where “loser” is the affectionate name for “user” at MIT.
> The MIT guy did not see any code that handled this case and asked the New Jersey guy how the problem was handled. The New Jersey guy said that the Unix folks were aware of the problem, but the solution was for the system routine to always finish, but sometimes an error code would be returned that signaled that the system routine had failed to complete its action. A correct user program, then, had to check the error code to determine whether to simply try the system routine again. The MIT guy did not like this solution because it was not the right thing.
> The New Jersey guy said that the Unix solution was right because the design philosophy of Unix was simplicity and that the right thing was too complex. Besides, programmers could easily insert this extra test and loop. The MIT guy pointed out that the implementation was simple but the interface to the functionality was complex. The New Jersey guy said that the right tradeoff has been selected in Unix-namely, implementation simplicity was more important than interface simplicity.
> The MIT guy then muttered that sometimes it takes a tough man to make a tender chicken.*


And the money shot:


> *However, **I believe that worse-is-better, even in its strawman form, has better survival characteristics than the-right-thing**, and that the New Jersey approach when used for software is a better approach than the MIT approach.*


At the risk of sounding like a Linux fan, I believe this with every fiber of my being. You want examples? Just look around you.

- **The x86 architecture** that you're probably reading this webpage on is widely regarded as total piece of crap. And it is. But it's a piece of crap *honed to an incredibly sharp edge.* x86-64? Our children will probably be using it. Meanwhile, the [Itanic](https://en.wikipedia.org/wiki/Itanium) slips deeper into the North Sea every month.
- **The windows registry.** Ever notice how everything in .NET is done through simple plaintext .config files? Does that remind you at all of the hoary old .INI file? Or perhaps an apache configuration file? While the registry hive is theoretically superior, it's [subject to a lot of problems](https://blog.codinghorror.com/was-the-windows-registry-a-good-idea/) mostly related to its complexity. Lose a few bytes and it's corrupt; wave bye-bye to all your registry data. Oh yeah, and your OS install. Two steps forward, one step back.
- **COM**. ‘[nuff said](https://web.archive.org/web/20040708034048/http://www.microsoft.com/com/). Wouldn't you rather just build a web service? Or... *anything* else?
- **Java**. You hear this refrain over and over: Java is too academic, too needlessly complex. J2EE? Anything with “Enterprise” in the title, just substitute “Complicated.”


Whenever possible, **always err on the side of simplicity**. [Why use inheritance](https://weblogs.asp.net/rmclaws/210399)  when a simple object will do? Why use inheritance when you can use an interface? Why even write code at all when you can buy or steal open-source it? In the spirit of [Strunk and White](http://www.amazon.com/exec/obidos/ASIN/020530902X/), keep taking complexity away, and like words on a page, when you cannot remove any more – you're done.


Simple solutions survive and prosper because they work, and people can actually understand them. Don't presume that everyone's smart enough to handle the fancy complex solution; [optimism is a dangerous occupational hazard](https://blog.codinghorror.com/defeating-optimism/) for programmers. We should strive to build simple solutions whenever possible, even if we have to [occasionally hold our noses when doing it](https://blog.codinghorror.com/some-lessons-from-forth/).


The original article was written in 1991; there's a follow-up [Back to the Future: Is Worse (Still) Better?](https://web.archive.org/web/20040618192950/http://www.dreamsongs.com/NewFiles/WorseIsBetterPositionPaper.pdf), as well as a [Wiki on the topic](http://c2.com/cgi/wiki?WorseIsBetter) with many follow-up links.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[operating systems](https://blog.codinghorror.com/tag/operating-systems/)
[complexity](https://blog.codinghorror.com/tag/complexity/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
