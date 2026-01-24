---
title: "The Six Dumbest Ideas in Computer Security"
date: 2005-09-13
url: https://blog.codinghorror.com/the-six-dumbest-ideas-in-computer-security/
slug: the-six-dumbest-ideas-in-computer-security
word_count: 350
---

Marcus Ranum, the [inventor of the proxy firewall](http://www.ranum.com/stock_content/about.html), brilliantly condenses why many security efforts are doomed from the start: they fall prey to the [The Six Dumbest Ideas in Computer Security](http://www.ranum.com/security/computer_security/editorials/dumb/) :

1. **Default Permit**
Also known as “on by default.” This one is huge, and it alone is why the phrase “Windows security” was such an oxymoron for so long. The good news is that Microsoft’s new policy of “[off by default](https://web.archive.org/web/20050901154121/http://www.windowsitpro.com/SQLServer/Article/ArticleID/42145/42145.html)” that kicked off with Windows Server 2003 is [really working](https://web.archive.org/web/20051123051152/http://blogs.technet.com/robert_hensing/archive/2005/02/17/375481.aspx).
2. **Enumerating Badness**
This is why blacklists are, and always will be, [a bad idea](http://www.paulgraham.com/falsepositives.html). They’re OK in helper roles for spot fixes, but as a primary means of defense, they are fatally flawed.
3. **Penetrate and Patch**
Security starts from the inside, not the outside. No amount of patching will fix a fundamentally bad security design. Should you be patching – or rearchitecting?
4. **Hacking is Cool**
It is interesting that society considers spammers “sleazy con artists” yet hackers are “whiz kids.” I think it has a lot to do with the financial motivations behind the crime. Maybe as hacking becomes more strongly associated with flat-out stealing, this will change.
5. **Educating Users**
A security system that fails to assume users are fallible and weak by default is destined to fail spectacularly. Education, at least when used as security spackle, doesn’t work.
6. **Action is Better than Inaction**
You can always recognize the pioneers from all the arrows in their backs. Progress is good, but careful progress is even better. Always do your homework before jumping on any bandwagon.


That’s the [condensed Reader’s Digest version](http://en.wikipedia.org/wiki/Reader's_Digest), but I highly recommend reading the rest of the article.


While we’re on the topic of security, TristanK has [an interesting rant on keyloggers](https://web.archive.org/web/20060614192712/http://blogs.technet.com/tristank/archive/2005/09/07/owapublishing.aspx). I think it’s a myth that you can protect yourself from the client PC anyway – the client is always suspect. That is, until client PCs start looking a lot more like Xbox 360, where you have to solder a modchip on the motherboard to run custom software.

[security](https://blog.codinghorror.com/tag/security/)
[computer security](https://blog.codinghorror.com/tag/computer-security/)
[cybersecurity](https://blog.codinghorror.com/tag/cybersecurity/)
[network security](https://blog.codinghorror.com/tag/network-security/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
