---
title: "Pair Programming vs. Code Reviews"
date: 2007-11-18
url: https://blog.codinghorror.com/pair-programming-vs-code-reviews/
slug: pair-programming-vs-code-reviews
word_count: 1054
---

Tom Dommett wrote in to share his positive experience with [pair programming](http://en.wikipedia.org/wiki/Pair_programming):


> The idea is two developers work on the same machine. Both have keyboard and mouse. At any given time one is driver and the other navigator. The roles switch either every hour, or whenever really. The driver codes, the navigator is reading, checking, spell-checking and sanity testing the code, whilst thinking through problems and where to go next. If the driver hits a problem, there are two people to find a solution, and one of the two usually has a good idea.
> Other advantages include the fact that where two people have differing specialities, these skills are transferred. Ad-hoc training occurs as one person shows the other some tricks, nice workarounds, etcetera.
> The end result is that both developers are fully aware of the code, how it works, and why it was done that way. Chances are the code is better than one developer working alone, as there was somebody watching. It’s less likely to contain bugs and hacks and things that cause maintenance problems later.
> In a bigger team, the pairing can change each week so each team member is partnered with somebody different. This is a huge advantage, as it gets developers talking and communicating ideas in the common language of code.
> We found this to be as fast as working separately. The code got written quicker and didn’t require revisiting. And when it did need to change, more than one person was familiar with the code.


It’s an encouraging result. I applaud anything that gets teams to communicate better.


I’m intrigued by the idea of pair programming, but **I’ve never personally lived the pair programming lifestyle**. I do, however, enjoy working closely with other developers. Whenever I sit down to work side by side with a fellow developer, I always absorb a few of their tricks and techniques. It’s a fast track learning experience for both participants. But I’ve only done this in small doses. I’m a little wary of spending a full eight hours working this way. I suspect this might be fatiguing in larger doses, unless you’re very fortunate in [your choice of pairing partner](https://web.archive.org/web/20071121151934/http://geekswithblogs.net/dlussier/archive/2007/08/10/114551.aspx).


I’ve written about the [efficacy of code reviews](https://blog.codinghorror.com/code-reviews-just-do-it/) before. That is something I have personal experience with; I can vouch for the value of code reviews without reservation. I can’t help **wondering if pair programming is nothing more than code review on steroids**. Not that one is a substitute for the other – you could certainly do both – but I suspect that many of the benefits of pair programming could be realized through [solid peer review practices](http://www.processimpact.com/pubs.shtml#pr).


But code reviews aren’t a panacea, either, [as Marty Fried pointed out](https://web.archive.org/web/20071121134823/http://jcooney.net/archive/2004/01/31/355.aspx):


> My experience with code reviews has been a mixed bag. One of the problems seems to be that nobody wants to spend the time to really understand new code that does anything non-trivial, so the feedback is usually very general. But later, when someone is working on the code to either add functionality or fix bugs, they usually have lots of feedback (sometimes involving large hammers), but then it may be too late to be effective; the programmer may not even be around. I think it might be useful to have one anyway, but it’s hard to get a fellow programmer to tell his boss that another programmer did a bad job.


**The advantage of pair programming is its gripping immediacy: it is impossible to ignore the reviewer when he or she is sitting right next to you.** Most people will passively opt out if given the choice. With pair programming, that’s not possible. Each half of the pair *has* to understand the code, right then and there, as it’s being written. Pairing may be invasive, but it can also force a level of communication that you’d otherwise never achieve.


On the other hand, peer review scales a heck of a lot better than stacking physical bodies in the same area. Consider [the experiences of Macadamian](https://web.archive.org/web/20071121200250/http://www.macadamian.com/index.php?option=com_techarticle&task=view&id=1) with code review while working on the [WINE project](http://en.wikipedia.org/wiki/Wine_(software)):


> There were two processes in the WINE project that we weren’t used to: public peer reviews, where new code and patches were distributed in a mailing list to everyone involved in the project; and single committer, where the project leader had the final say over which patches were accepted into the source tree.
> We soon found out that Alexandre Julliard, who has been the maintainer of WINE and one of the key developers since 1994, was very particular about code going into the source tree. Our team’s patches were scrutinized, and when some were rejected, there was a lot of grumbling. “My code works, who does this guy think he is? We’re on a deadline here!” But as the project progressed, we realized we were producing our best code ever. Producing clean, well-designed code that was admitted into the source tree at first pass soon became a matter of pride. We also found that, despite the fact that the project was huge and spread worldwide, we knew exactly how the whole project was progressing since we saw every patch on the mailing list. We now conduct code reviews on every project, and on larger projects, we set up an internal mailing list and designate a single committer. It may be painful to set up code review at your company, and there may be some grumbling, but you will see big improvements in the quality and maintainability of your code.


I think both techniques are clearly a net *good*, although they each have their particular pros and cons. I encourage people who have experience with both pair programming and code reviews to share their experiences in the comments. Is one more effective than the other? Should we do both?


![](https://blog.codinghorror.com/content/images/2025/03/image-160.png)


In the end, I don’t think it’s a matter of picking one over the other so much as **ensuring you have more than one pair of eyes looking at the code you’ve written**, however you choose to do it. When your code is reviewed by another human being – whether that person is sitting right next to you, or thousands of miles away – you *will* produce better software. That I can guarantee.

[pair programming](https://blog.codinghorror.com/tag/pair-programming/)
[code reviews](https://blog.codinghorror.com/tag/code-reviews/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
