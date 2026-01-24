---
title: "Oh Yeah? Fork You!"
date: 2008-05-15
url: https://blog.codinghorror.com/oh-yeah-fork-you/
slug: oh-yeah-fork-you
word_count: 711
---

In [Where Are All The Open Source Billionaires?](https://blog.codinghorror.com/where-are-all-the-open-source-billionaires/) I used this chart as an illustration:


![](https://blog.codinghorror.com/content/images/2025/04/image-114.png)


Because open source code is freely distributable, anyone can take that code and create their own unique mutant mashup version of it any time they feel like it. Whether anyone else in the world will *care* about their crazy new version of the code is not at all clear, but that’s not the point. If someone wants it bad enough, they can create it – or pay someone else to create it for them. This is known as [“forking.”](http://en.wikipedia.org/wiki/Fork_(software_development)) It’s the very embodiment of [freedom zero](https://blog.codinghorror.com/why-doesnt-anyone-give-a-crap-about-freedom-zero/), and it’s an essential part of [every open source license](https://blog.codinghorror.com/pick-a-license-any-license/).


But there are forks, and [there are *forks*](http://www.dwheeler.com/oss_fs_why.html#forking):


> What is different about a fork is *intent*. In a fork, the person(s) creating the fork **intend for the fork to replace or compete with the original project they are forking.**


That’s exactly what [happened to the Pidgin project](https://web.archive.org/web/20080516082940/http://www.productbeautiful.com/2008/05/02/why-product-management-is-open-sources-fatal-flaw/) recently.


> In their 2.4 release they changed the GUI action of the text field where the user types their IM from a manually re-sizable window, to a fixed size window that auto-re-sizes based on the amount of text typed. On the surface, this sounds like a minor change, but it triggered a massive user revolt! Why?


This is what they’re up in arms about:


![](https://blog.codinghorror.com/content/images/2025/04/image-113.png)


The developers, for whatever reason, dug in their heels on this one and refused to budge. You can read through some of the commentary [on the bug ticket](http://developer.pidgin.im/ticket/4986) to get an idea, but the general tenor was combative bordering on hostile. The bug was eventually closed as “won’t fix.”


The community’s response was swift: Oh yeah? [Fork you!](http://funpidgin.sourceforge.net/)


> Funpidgin is a fork of the popular open source client Pidgin which allows instant messaging with over twenty different protocols.
> What makes us different from the official client is that **we work for you**. Unlike the Pidgin developers, we believe the user should have the final say in what goes into the program.
> So far five new features have been added to Funpidgin upon requests from users, and all of them are optional. It is these options that make the use of Funpidgin enjoyable to a diverse range of people.


Funpidgin is a fork in the truest sense; the developers intend to *replace* Pidgin. But will it? Who knows. There are four possible outcomes from any fork:

1. **The fork dies**
Funpidgin languishes due to lack of attention from developers and users. Funpidgin eventually dies.
2. **The fork merges**
Funpidgin and Pidgin reach a consensus. The Funpidgin changes are folded back into Pidgin.
3. **The original dies**
Funpidgin becomes so popular that it draws developers and users away from Pidgin. Pidgin eventually dies.
4. **Both original and fork survive**
Funpidgin and Pidgin both succeed on their own terms, perhaps by attracting different audiences or meeting different user needs.


You can find examples of all four outcomes peppered throughout the history of open source software. You might think that the adoption of open source software licenses would lead to dozens if not hundreds of incompatible, slightly-different versions of the same stuff – bewildering users and developers alike. I’m not so sure. There’s a [tremendous amount of inertia](http://linuxmafia.com/faq/Licensing_and_Law/forking.html) around the open source projects that survive long enough to become popular. Consider the challenges the newly forked Funpidgin project now faces:

- A divided community of users and developers.
- Siphoning enough energy and attention away from an established project to remain viable.
- Differentiating themselves enough from Pidgin so that they aren’t viewed as useless or irrelevant.
- The original Pidgin project is free to take whatever parts of the Funpidgin open source code they deem appropriate and fold that into Pidgin, thus undermining the fork.


**Forking is incredibly difficult to pull off**. It is a painful, but necessary part of the evolution of open source software. Just as in real evolution, I suspect that most forks die in vast, nameless numbers, before they become strong enough to engender any forked progeny of their own. Forking is the absolute bedrock of open source software – but it is also not a path to be chosen lightly.

[open source](https://blog.codinghorror.com/tag/open-source/)
[forking](https://blog.codinghorror.com/tag/forking/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[open source licensing](https://blog.codinghorror.com/tag/open-source-licensing/)
[project management](https://blog.codinghorror.com/tag/project-management/)
