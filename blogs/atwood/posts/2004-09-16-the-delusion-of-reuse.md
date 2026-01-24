---
title: "The Delusion of Reuse and the Rule of Three"
date: 2004-09-16
url: https://blog.codinghorror.com/the-delusion-of-reuse/
slug: the-delusion-of-reuse
word_count: 398
---

I’m currently reading [Facts and Fallacies of Software Engineering](http://www.amazon.com/exec/obidos/ASIN/0321117425) by Robert Glass. It’s definitely a worthwhile book, although I do have two criticisms:

1. Someone really, really needs to buy Robert Glass a copy of [Strunk and White’s Elements of Style](https://www.amazon.com/Elements-Style-Fourth-William-Strunk/dp/020530902X/ref=sr_1_1?crid=2Q10CJCTQHO6U&dib=eyJ2IjoiMSJ9.jgkWgRmNc_jSC-01JvFtVMHoBCIWLbWEOfL8z5XKxrQYBm48aQUmDtTbAnIoQBMKwc1n43S6Kt_8dSljpx5FakK5WQn1Zi-8mG0yERqnwyn_JIzX1C3uuBAjSd6uUgMw7aqjOPbrSGZYPQVtbGgaofTZmLQN2PLmM3U4sFtU6fKaG4wBzVDU9b3kSy9aAJ9qF9pq588v9Uh0YJ7yD1InH147dSiIGkqon14qKTsRXiE.g0x4XGliNwQMVUC5k7AuHL9MHFibsbiDuyZNjHC3YXQ&dib_tag=se&keywords=Strunk+and+White%E2%80%99s+Elements+of+Style&qid=1746020770&sprefix=strunk+and+white+s+elements+of+style%2Caps%2C277&sr=8-1). Or at least get him a decent editor. There’s some great information here, but his overly florid writing style gets in the way.
2. Quite a few of the 55 facts and fallacies presented here will be old news to anyone familiar with the most popular books on my [reading list for developers](https://blog.codinghorror.com/recommended-reading-for-developers/). For example, “Adding people to a late project makes it later.” That’s well understood, and Glass doesn’t cover enough new ground with these chestnuts to justify the two or three pages each one adds to the book.


That said, I am really enjoying the parts of the book that cover the more obscure topics. For example, the **Rule of Three**:


> *There are two “Rules of Three” in reuse: (a) It is three times as difficult to build reusable components as single use components, and (b) a reusable component should be tried out in three different applications before it will be sufficiently general to accept into a reuse library.*


I have found this to be universally true in the projects I’ve worked on. If anything, I think this rule underestimates the cost: **I believe writing a truly reusable class is an order of magnitude harder than writing a single use class.** Sometimes the right thing to do is resist the urge to write “general purpose” solutions. Sure, it’s better in the long run to have a widget library you can use forever, but that doesn’t get your current project done any faster. Furthermore, how confident are you that the so-called “general purpose” solution you built will actually work for these… unknown future projects? Have you tried it?


You can’t know if you have a strong case for reuse unless you’ve tried – and possibly failed – to use that same bit of code on *at least* three different projects, with three different audiences.


Until you’ve invested the additional effort to implement that “reusable” code with different developers and different problem domains, all you have is the **delusion of reuse**. Be careful, because I’ve seen too many developers fall into this trap. Myself included.

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
[code reuse](https://blog.codinghorror.com/tag/code-reuse/)
[technical writing](https://blog.codinghorror.com/tag/technical-writing/)
[software engineering](https://blog.codinghorror.com/tag/software-engineering/)
