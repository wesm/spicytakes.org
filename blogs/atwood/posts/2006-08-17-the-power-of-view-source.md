---
title: "The Power of “View Source”"
date: 2006-08-17
url: https://blog.codinghorror.com/the-power-of-view-source/
slug: the-power-of-view-source
word_count: 833
---

The 1996 JavaWorld article [Is JavaScript here to stay?](https://web.archive.org/web/20070303224837/http://www.javaworld.com/javaworld/jw-08-1996/jw-08-js-analysis.html) is almost amusing in retrospect. John Lam recently [observed ](https://web.archive.org/web/20061023204350/http://www.iunknown.com/articles/2006/08/14/some-more-photos-from-lang-net)that


> JavaScript is the world’s most ubiquitous computing runtime.


I think the answer is an emphatic *yes*.


JavaScript is currently undergoing a renaissance through AJAX. Sure, the AJAX-ified clones of Word and Excel are still pretty lame, but they’re the first baby steps on **the long road to rewriting every client application in the world in JavaScript.** The line between client executable and web page gets blurrier every day.


The meteoric rise in popularity of Ruby has also renewed interest in dynamic languages. And JavaScript may be the [most underappreciated dynamic language](https://web.archive.org/web/20070115225907/http://schf.uc.org/articles/2006/08/13/javascript-the-underappreciated-dynamic-language) of all. Unfortunately, it’s difficult to separate JavaScript from all its browser environment baggage and consider it [purely as a language](http://www.crockford.com/javascript/survey.html).


But these are both relatively recent developments. They’re important milestones, but they’re not the full story of JavaScript’s success. Not by a long shot. I attribute most of JavaScript’s enormous success to one long-standing menu item on every browser:


![](https://blog.codinghorror.com/content/images/2025/04/image-753.png)


**The view source menu is the ultimate form of open source.** It’s impossible to obfuscate or hide JavaScript running in a browser. The code that powers any AJAX application is right there in plain sight, for everyone to see, copy, and use. A complete set of JavaScript source code for the latest AJAX apps is never more than one HTTP download away. They’re literally *giving away* the source code for their application to *every user*.


Some people might see that as a huge business risk. I say if your business model is that dependent on clever, obfuscated source code tricks, it isn’t much of a business model.


I’ve read several complaints that .NET code is [too easy to decompile](https://blog.codinghorror.com/obfuscating-code/). Nonsense. It should be even *easier* to decompile. The real stroke of genius in JavaScript wasn’t closures, or XmlHttpRequest; it was **forcing people to share their source code with the community.** How do you think anyone found out about XmlHttpRequest in the first place? Through reading the documentation?


The entire JavaScript development community is predicated on instant, ubiquitous access to source code. This leads to what I call **“Code Darwinism:”** good techniques are seen immediately and reproduce promiscuously. Bad techniques never reproduce and die out.


![](https://blog.codinghorror.com/content/images/2025/04/image-754.png)


That’s why I'm not afraid to bust out a copy of [Reflector](http://www.aisto.com/roeder/dotnet/) and perform a little ad-hoc “View Source.” It’s common practice to decompile binary .NET assemblies, for a whole host of entirely valid reasons:

- You’ve encountered a possible bug in the code
- You don’t understand the code’s behavior
- You need to do something similar in your own code


Having the source code gives you the ability to fix your own problems – or even someone else’s problems. If you can see the source code, the binary is alive – it can *evolve*.


And you can still license your software and make money, even if you’re handing out the source code at the same time. [According to DesaWare](https://web.archive.org/web/20070317182623/http://www.devx.com/opinion/Article/20513), one of the most compelling software sales pitches is the phrase “source code included:”


> Providing source code is the only answer – it’s a way to say to the customer that if worst comes to worst, they can be their own alternate source. Even Microsoft has demonstrated this by providing Windows Source to certain customers, like large governments, who have the leverage to demand it. And, yes, escrow services should be sufficient for this purpose, but for some reason most customers don’t like that approach. Perhaps it’s lack of confidence in the long-term viability of the escrow services themselves? Or perhaps lack of faith in their own institutional memory to recall that such escrow arrangements had been made.
> There are some nice side benefits of having source code available: the ability to learn from someone else’s code, and the possibility of customizing components to suit specific needs, but those are smaller issues. Security is always a concern, but it is only applicable to software that has the potential to elevate the privilege of a user – something that applies to a relatively small number of software components.
> So what about the great closed source vs. open source debate? I’m never one to shy away from controversy, but that’s for another time and place. What we did by releasing our software was not open source by any stretch of the imagination. Our source code is licensed to individual developers for their own use – not for distribution. Does a true open source model make sense for the component world? I don’t know. What I do know is that source code availability provides a level of peace of mind for some developers that probably cannot be matched any other way.


We should do away with the pretense of hiding code. Let’s not only acknowledge that decompiling .NET code is trivial, **let’s *embrace* the power of “view source” by shipping source code along with our binaries.**

[javascript](https://blog.codinghorror.com/tag/javascript/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[dynamic languages](https://blog.codinghorror.com/tag/dynamic-languages/)
[web development](https://blog.codinghorror.com/tag/web-development/)
