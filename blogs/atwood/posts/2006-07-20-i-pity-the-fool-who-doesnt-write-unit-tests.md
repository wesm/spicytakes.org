---
title: "I Pity The Fool Who Doesn’t Write Unit Tests"
date: 2006-07-20
url: https://blog.codinghorror.com/i-pity-the-fool-who-doesnt-write-unit-tests/
slug: i-pity-the-fool-who-doesnt-write-unit-tests
word_count: 681
---

J. Timothy King has a nice piece on [the twelve ](https://web.archive.org/web/20060818033649/http://www.jtse.com/blog/2006/07/11/twelve-benefits-of-writing-unit-tests-first)[benefits of writing unit tests first](https://web.archive.org/web/20060818033649/http://www.jtse.com/blog/2006/07/11/twelve-benefits-of-writing-unit-tests-first). Unfortunately, he seriously undermines his message by ending with this:


> However, if you are one of the [coders who won’t give up code-first], one of those curmudgeon coders who would rather be right than to design good software... Well, you truly have my pity.


Extending your pity to anyone who doesn’t agree with you isn’t exactly the most effective way to get your message across.


![](https://blog.codinghorror.com/content/images/2025/08/mr-t-in-suit-with-american-flag.jpg)


[Consider Mr. T](https://en.wikipedia.org/wiki/Mr._T). He’s been pitying fools since the early 80s, and the world is still awash in foolishness.


It’s too bad, because the message is an important one. The general adoption of unit testing is one of the most fundamental advances in software development in the last 5 to 7 years.


> How do you solve a software problem? How do they teach you to handle it in school? What’s the first thing you do? You think about how to solve it. You ask, “What code will I write to generate a solution?” But that’s backward. The first thing you should be doing – In fact, this is what they say in school, too, though in my experience it’s paid more lip-service than actual service – The first thing you ask is not “What code will I write?” The first thing you ask is “How will I know that I’ve solved the problem?”
> We’re taught to assume we already know how to tell whether our solution works. It’s a non-question. Like indecency, we’ll know it when we see it. We believe we don’t actually need to think, before we write our code, about what it needs to do. This belief is so deeply ingrained, it’s difficult for most of us to change.


King presents a list of 12 specific ways adopting a test-first mentality has helped him write better code:

1. Unit tests prove that your code actually works
2. You get a low-level regression-test suite
3. You can improve the design without breaking it
4. It’s more fun to code with them than without
5. They demonstrate concrete progress
6. Unit tests are a form of sample code
7. It forces you to plan before you code
8. It reduces the cost of bugs
9. It’s even better than code inspections
10. It virtually eliminates coder’s block
11. Unit tests make better designs
12. It’s faster than writing code without tests


Even if you only agree with a quarter of the items on that list – and I’d say at least half of them are true in my experience – that is a huge step forward for software developers. You’ll get no argument from me on the overall [importance of unit tests](https://blog.codinghorror.com/good-test-bad-test/). I’ve increasingly come to believe that **unit tests are so important that they should be a first-class language construct**.


However, I think the test-first dogmatists tend to be a little too religious for their own good. **Asking developers to fundamentally change the way they approach writing software overnight is asking a lot.** Particularly if those developers have yet to write their first unit test. I don’t think any software development shop is ready for test-first development until they’ve adopted unit testing as a standard methodology on every software project they undertake. [Excessive religious fervor](https://web.archive.org/web/20060807134358/http://codebetter.com/blogs/jeffrey.palermo/archive/2006/03/28/141920.aspx) could sour them on the entire concept of unit testing.


And that’s a shame, because **any tests are better than zero tests.** And isn’t unit testing just a barely more formal way of doing the ad-hoc testing we’ve been doing all along? I think [Fowler](https://web.archive.org/web/20060813175724/http://emw.inf.tu-dresden.de/de/pdai/Forschung/refactoring/refactoring_html/node7.html) said it best:


> Whenever you are tempted to type something into a print statement or a debugger expression, write it as a test instead.


I encourage developers to see the value of unit testing; I urge them to get into the habit of writing structured tests alongside their code. That small change in mindset could eventually lead to bigger shifts like test-first development – but you have to crawl before you can *sprint*.

[unit testing](https://blog.codinghorror.com/tag/unit-testing/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
[coding practices](https://blog.codinghorror.com/tag/coding-practices/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
