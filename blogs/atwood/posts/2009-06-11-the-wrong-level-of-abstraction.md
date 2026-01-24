---
title: "The Wrong Level of Abstraction"
date: 2009-06-11
url: https://blog.codinghorror.com/the-wrong-level-of-abstraction/
slug: the-wrong-level-of-abstraction
word_count: 714
---

In [Why Isn’t My Encryption... Encrypting?](https://blog.codinghorror.com/why-isnt-my-encryption-encrypting/) we learned that your encryption is only as good as your *understanding* of the encryption code. And that the best encryption of all is *no* encryption, because you kept everything on the server, away from the prying eyes of the client.


In [The Bathroom Wall of Code](https://blog.codinghorror.com/the-bathroom-wall-of-code/) we learned the potential danger of copy-pasting code from the internet, and the continued importance of regular peer review for every line of code that enters your codebase, from whatever source.


I didn’t anticipate this series becoming a trilogy, but apparently it has, because Thomas Ptacek of Matsano Security wrote a [long blog entry about it](https://web.archive.org/web/20090707092021/http://www.matasano.com/log/1749/typing-the-letters-a-e-s-into-your-code-youre-doing-it-wrong/). A blog entry masquerading as an overly dramatic college screenplay, but still. These guys, unlike us, are real security experts, so it’s worth reading.


But you don’t have to read that screenplay, because I’m going to reveal the twist in the final act right here.

1. The root problem *wasn’t* failing to understand the encryption.
2. The root problem *wasn’t* copy and pasting code from the internet.
3. The root problem *wasn’t* failing to peer review the code.


Mr. Ptacek is absolutely right. The root problem was that **we were working at the wrong layer of abstraction**.


Rather than construct code from the low-level cryptography primitives provided in .NET, **we should have used a library to handle our encryption needs**. I’m reminded of a common Stack Overflow joke:


> Q: How do I write this in JavaScript?
> A: You don’t. You use [JQuery](http://jquery.com/).


You can save a tremendous amount of time and effort by using the browser-independent framework that JQuery has spent untold man-hours testing, debugging, and proving in the field. While there’s nothing *wrong* with writing JavaScript, why not speed your development time by writing to the library instead? As I’ve always said, [don’t reinvent the wheel, unless you plan on learning more about wheels](https://blog.codinghorror.com/dont-reinvent-the-wheel-unless-you-plan-on-learning-more-about-wheels/).


Abstractions are important. You could view most of computer programming history as slowly, painfully clawing our way up the evolutionary tree of abstraction – from assembly language, to C, to Java, to JavaScript, all the way up to JQuery, where the air starts to get pretty darn thin. We’ve already layered an operating system, web browser, *and* interpreted scripting language on top of each other to get to this point. It’s a testament to [the power of abstraction](https://blog.codinghorror.com/respecting-abstraction/) that any of it works at all.


Getting back to specifics: how can you stop programmers from working at the wrong layer of abstraction? One solution would be to **disallow the .NET encryption primitives entirely**. This is akin to Steve Gibson’s holy [crusade against raw socket programming](http://technet.microsoft.com/en-us/library/cc751041.aspx) in Windows XP. That’s one way to do it, I suppose. But putting roadblocks in front of programmers is tantamount to a challenge; why not offer them more attractive alternatives, instead?


Hiding the low-level encryption primitives feels like a temporary solution. That said, I’d *strongly* recommend marking some of the older encryption methods as **deprecated**, so programmers who do stumble down some dusty old code path at least have some warning sign that they’re using an algorithm with a lot of known vulnerabilities. I’m envisioning a [Clippy that pops up](https://blog.codinghorror.com/it-looks-like-youre-writing-a-for-loop/) with something like:


> “Hey! It looks like you’re using a method of encryption that’s widely regarded as insecure by security experts! Would you like to see alternatives?”


One of those alternatives would be a full-blown library, perhaps something like [Bouncy Castle](http://www.bouncycastle.org/), or [Keyczar](http://www.keyczar.org/), or [cryptlib](http://www.cs.auckland.ac.nz/~pgut001/cryptlib/). What could be easier than a `EncryptStringForBrowser()` method which has security and tamper-resistance built in, that’s part of a proven, domain-expert-tested set of code that thousands if not millions of developers already rely on?


Using encryption libraries doesn’t mean that crucial encryption mistakes will magically disappear overnight. But these libraries, because they force developers to work at a higher level of abstraction, do make it *harder* to misuse cryptography. And perhaps more importantly, usability improvements to the library can be better handled by the specialists who created the library, rather than the generalists working on the .NET framework itself.


So the next time you set out to write code – not just encryption code, *any* code – ask yourself: **am I working at the right level of abstraction?**

[security](https://blog.codinghorror.com/tag/security/)
[encryption](https://blog.codinghorror.com/tag/encryption/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[code review](https://blog.codinghorror.com/tag/code-review/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
