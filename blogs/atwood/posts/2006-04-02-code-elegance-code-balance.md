---
title: "Code Elegance, Code Balance"
date: 2006-04-02
url: https://blog.codinghorror.com/code-elegance-code-balance/
slug: code-elegance-code-balance
word_count: 543
---

I’ve been reading a great book of [interviews with programmers](https://blog.codinghorror.com/programmers-as-human-beings/) circa 1989. One of the most fascinating interviews is with Wayne Ratliff, the author of [dBase](http://en.wikipedia.org/wiki/DBASE). Wayne’s description of **balance in programming** really resonated with me:


> Interviewer: Can you elaborate on this feeling for balance and elegance?
> Balance takes many forms. The code should be crisp and concise. You should be able to explain any module in one sentence, and things should be in alphabetical order, if possible. Just from a visual view of indentation, it shouldn’t go off the edge of the paper at any point. It shouldn’t have one “if” that’s huge and an “else” that’s small. Everything should be balanced everywhere. Balance is the key word.
> Interviewer: When you write code, does it come out balanced the first time, or does it need a lot of changes?
> I do a lot of changing. I like to make an analogy between writing code and sculpting a clay figure. You start with a lump of clay and then you scrape away, add more clay, then scrape away again. And every now and then you decide that a leg doesn’t look right, so you tear it off and put a new one on. There’s a lot of interaction.
> The ideal module should be a page long. If it grows beyond a page, I have to decide, now what is it I’m doing here? How many separate things am I working on? Should they be broken down into separate modules? Part of the elegance, and the balance, is that a certain level, in this layer-cake hierarchy of a program, all the modules should be about the same weight, same size, same duty, and same functionality.
> Interviewer: How does balance help a program?
> The program becomes maintainable. When you have a good balance, it’s as if you’ve discovered some basic physical underlying principle and implemented it. When things get really out of balance, you know something is wrong. There’s probably some inherent fault that makes it out of balance. Generally, when I get this feeling that something’s out of whack or one module is just too big, I think about what I’m doing, and I reorient or juggle the pieces.


I think you could sum up reams of programming advice with that one concept: balance. We’re striving for balance between complexity and simplicity. And we’re constantly evaluating and re-evaluating the tradeoffs we have to make to get there.


Balance also applies to the way you physically lay out your code. There’s a great visual device in [Code Complete’s](http://www.amazon.com/exec/obidos/ASIN/0735619670) layout chapter where the actual characters of code are replaced with black bars. Like [well-designed web pages](https://blog.codinghorror.com/conventions-and-usability/) in other languages, **you should be able to understand the general flow of the code even if you can’t read any of it**:


![](https://blog.codinghorror.com/content/images/2025/05/image-248.png)


The aesthetics of your code is purely an internal implementation detail. How you place your squigglies won’t affect users in the slightest. But attention to internal code layout details implies that you’re equally attentive to the external details. **If you’re structuring your code to be accurate, consistent, readable, and maintainable, your application will work better – because it’s balanced**.

[code quality](https://blog.codinghorror.com/tag/code-quality/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[code elegance](https://blog.codinghorror.com/tag/code-elegance/)
[code balance](https://blog.codinghorror.com/tag/code-balance/)
