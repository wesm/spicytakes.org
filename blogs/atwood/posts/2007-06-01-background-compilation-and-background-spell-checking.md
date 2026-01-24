---
title: "Background Compilation and Background Spell Checking"
date: 2007-06-01
url: https://blog.codinghorror.com/background-compilation-and-background-spell-checking/
slug: background-compilation-and-background-spell-checking
word_count: 1278
---

Dennis Forbes took issue with my recent post on [C# and the Compilation Tax](https://blog.codinghorror.com/c-and-the-compilation-tax/), offering this criticism, pointedly titled [“Beginners and Hacks](http://www.yafla.com/dforbes/2007/05/16.html):”


> Sometimes [background compilation and edit and continue] are there to coddle a beginner, carefully keeping them within the painted lines and away from the dangerous electrical sockets along the wall. That would explain why it was a more important feature in VB.NET than C#... not that VB.NET is any more trivial – it’s just a syntactic variant – but it is the language that beginner programmers are generally guided into.
> My experience has been that the best developers naturally start using less and less “helpers,” to the extreme where you have incontestably great developers like Linus Torvalds arguing against [fundamental helpers like interactive debuggers](http://www.xml.com/ldd/chapter/book/ch04.html).
> **I don’t buy the infinite monkeys on an infinite number of keyboards model of software development**. I can only envision tools like continuous compilation and edit and continue as the hand-holding of beginners, and the crutch of hacks.


Regardless of whether or not Dennis is buying it, **the infinite monkey software development model is what we’re stuck with**. I’m an advocate of designing practical systems that accommodate what actually happens in the real world – rather than the way we *wish* things worked. The present model of software development is clearly [monkeys all the way down](http://en.wikipedia.org/wiki/Turtles_all_the_way_down). And if you’re offended to be lumped in with the infinite monkey brigade, I’d say that’s *incontestable* proof that you’re one of us.


For every one Linus Torvalds, there are ten thousand [programmers who aren’t Linus Torvalds](https://blog.codinghorror.com/skill-disparities-in-programming/). I don’t expect this ratio to change any time soon, so any effort directed at helping typical developers with better tooling is a significant advancement in the state of software development. Yes, you could throw [emacs](http://en.wikipedia.org/wiki/Emacs) and volumes 1-5 of [The Art of Programming](http://www-cs-faculty.stanford.edu/~knuth/taocp.html) at your development team. Or you can buy them the best, most advanced development tools on the market. Which approach do you think will be more effective?


Ian Griffiths expressed his discontent with background compilation in [a completely different way](http://www.interact-sw.co.uk/iangblog/2007/05/15/language-choice):


> I hate VB.NET’s continuous bloody interference. I HADN’T FINISHED TYPING YET YOU STUPID COMPILER! CAN’T YOU SEE THAT? DOES IT LOOK TO YOU LIKE I’M DONE TYPING? DID IT NOT OCCUR TO YOU THAT THE REASON YOU’VE FOUND ALL THOSE ERRORS IS BECAUSE I’M NOT FINISHED YET?!! I’LL TELL YOU WHEN I WANT YOU TO CHECK MY WORK, AND NOT BEFORE!
> There. I feel better now.
> Yes, I’m sure rebuilding my C# applications every other keystroke, as Jeff apparently feels compelled to do, would have a negative effect on my productivity. How could it be otherwise when VB.NET’s less than helpful attempts to do that automatically are so very distracting? “[It looks like you’re writing a program. Would you like help?](https://blog.codinghorror.com/it-looks-like-youre-writing-a-for-loop/)” Oddly enough, I don’t feel the need to disrupt my train of thought continuously. So I would prefer it if VB.NET didn’t disrupt me automatically.


I respect the opinions of Dennis and Ian greatly. If you don’t have their blogs in your aggregator yet, you should. But I also respectfully disagree with both of them on this topic. If you find background compilation naggy – or if you think it’s strictly for beginners and hacks – then **you must really, *really* hate background spell checking**:


![Microsoft Word grammar and spelling checker](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d91b3970b-pi.png)


People absolutely *adore* background spell checking. It’s one of those rare “you’ll get it from me when you pry it out of my dead, cold hands” features that users will switch applications over. Automatic background red-squiggly-underline spell checking in HTML forms is one of the marquee features of Firefox 2.0. In fact, it’s [feature number two on the feature page](http://www.mozilla.com/en-US/firefox/features.html#experience), right under tabbed browsing.


**I see very little difference between background spell checking and background compilation.** To me, they’re no-brainers for the same reasons. I’m actually an excellent speller, to the point that I can (and do) work without a spell checker and rarely make mistakes. But having subtle background underlining effects when I’ve potentially made a spelling mistake is undeniably helpful to me, a self-professed excellent speller. I can ignore it when I know it’s wrong and keep on plowing ahead. But more often than not, I’ve actually made a typo, and I no longer have to methodically read through my writing several times to find it. With background spell checking, all I need to do is quickly scan through the red squiggly underlined text.


Mike Pope, a professional writer for Microsoft, also [defends background spelling and grammar checking](http://www.mikepope.com/blog/DisplayBlog.aspx?permalink=1753):


> I use the spell checker and grammar checker in Word all the time. These things are tools for me, ways to help somewhat with the grunt work of examining every letter of every word of every sentence in all the documents I edit. The spell checker finds words all the time that have been fumbled (often by me as I edit), although it finds many, many more that it thinks are errors but are just fine in context (e.g. lots of technical names). The grammar checker doesn’t have as much opportunity to be helpful, but it’s good at finding problems like subject-verb agreement when the subject of sentence has been edited but the verb has not.
> But these tools are often looked at askance. As I’ve noted before (I think), professional editors can be snotty about the grammar checker in particularly, focusing on errors that the checker doesn’t find, or constructions that confuse the grammar checker and make it believe it’s found an error when there is none. Similarly, virtually everyone has examples where the spell checker has missed words. The spell checker is helpless in the face of their-they’re-there confusion, for example.


The funny thing about this debate is that I’ve lived the zero-tooling lifestyle. It sucks. Here’s how I’ve composed every single blog entry I’ve ever written: **in a fixed-size HTML textbox**. In fact, I’m writing in it *right now*.


![Coding Horror editing menu](https://blog.codinghorror.com/content/images/uploads/2007/06/6a0120a85dcdae970b0120a86d91be970b-pi.png)


Despite my spelling prowess, I’ve posted many spelling mistakes to this blog. Using the most primitive of tools to compose these blog posts isn’t a glorious, sweeping validation of my expertise as a writer. If anything, it’s an indication of my idiocy, or at least **my unwillingness to let better tools help me be a better writer**. It’s absolutely nothing to be proud of. In fact, I’m a little ashamed to admit how neanderthal my blog tooling really is.


Neither background compilation nor background spell checking are *meant* to be crutches. Any reasonably competent person knows that tools are never substitutes for critical thinking about what you’re writing or coding – as Mike [so aptly points out](http://www.mikepope.com/blog/DisplayBlog.aspx?permalink=1753):


> Considering all this, the tools are pretty good at what they do. **But no matter how good they are, people need to understand the tools’ limitations, or for perhaps more fundamentally, the tools are just tools, and they should never have the last say.** Don’t let that computer boss you around.


Intentionally choosing not to use better tools because you’re afraid they will become a crutch is, at best, cruel and patronizing. And it’s usually a bad business decision to boot. Turn off background compilation – or background spell checking – if you must, but **background spell checking is on by default in Word and Firefox 2.0**. Is it a perfect solution to the spelling problem? No. Far from it. But for the average user, it’s an easy, automatic, unobtrusive way to see and correct common spelling errors. And background compilation, as in VB.NET, offers the same benefit for common coding errors.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
