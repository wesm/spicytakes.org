---
title: "The First Rule of Programming: It’s Always Your Fault"
date: 2008-03-20
url: https://blog.codinghorror.com/the-first-rule-of-programming-its-always-your-fault/
slug: the-first-rule-of-programming-its-always-your-fault
word_count: 756
---

You know the feeling. It’s happened to all of us at some point: you’ve pored over the code a dozen times and *still* can’t find a problem with it. But there’s some bug or error you can’t seem to get rid of. There just has to be something wrong with the machine you’re coding on, with the operating system you’re running under, with the tools and libraries you’re using. There just *has to be!*


No matter how desperate you get, don’t choose that path. Down that path lies voodoo computing and [programming by coincidence](http://pragmaticprogrammer.com/the-pragmatic-programmer/extracts/coincidence). In short, madness.


It’s frustrating to repeatedly bang your head against difficult, obscure bugs, but don’t let desperation lead you astray. An essential part of [being a humble programmer](https://blog.codinghorror.com/why-im-the-best-programmer-in-the-world/) is realizing that whenever there’s a problem with the code you’ve written, **it’s always your fault**. This is aptly summarized in [The Pragmatic Programmer](http://www.amazon.com/exec/obidos/ASIN/020161622X) as “Select Isn’t Broken”:


> In most projects, the code you are debugging may be a mixture of application code written by you and others on your project team, third-party products (database, connectivity, graphical libraries, specialized communications or algorithms, and so on) and the platform environment (operating system, system libraries, and compilers).
> It is possible that a bug exists in the OS, the compiler, or a third-party product-- but this should not be your first thought. It is much more likely that the bug exists in the application code under development. It is generally more profitable to assume that the application code is incorrectly calling into a library than to assume that the library itself is broken. Even if the problem *does* lie with a third party, you’ll still have to eliminate your code before submitting the bug report.
> We worked on a project where **a senior engineer was convinced that the select system call was broken on Solaris**. No amount of persuasion or logic could change his mind (the fact that every other networking application on the box worked fine was irrelevant). He spent weeks writing workarounds, which, for some odd reason, didn’t seem to fix the problem. When finally forced to sit down and read the documentation on select, he discovered the problem and corrected it in a matter of minutes. We now use the phrase “select is broken” as a gentle reminder whenever one of us starts blaming the system for a fault that is likely to be our own.


The flip side of [code ownership](https://blog.codinghorror.com/you-gotta-own-it/) is *code responsibility*. No matter what the problem is with your software – maybe it’s not even your code in the first place – **always assume the problem is in your code** and act accordingly. If you’re going to subject the world to your software, take full responsibility for its failures. Even if, technically speaking, you don’t have to. That’s how you earn respect and credibility. You certainly don’t earn respect or credibility by endlessly pawning off errors and problems on other people, other companies, other sources.


Statistically, you understand, it is incredibly rare for any bugs or errors in your software *not* to be your fault. In [Code Complete](http://www.amazon.com/exec/obidos/ASIN/0735619670), Steve McConnell cited two studies that proved it:


> A pair of studies performed [in 1973 and 1984] found that, of total errors reported, **roughly 95% are caused by programmers**, 2% by systems software (the compiler and the operating system), 2% by some other software, and 1% by the hardware. Systems software and development tools are used by many more people today than they were in the 1970s and 1980s, and so my best guess is that, today, an even higher percentage of errors are the programmers’ fault.


Whatever the problem with your software is, take ownership. Start with your code, and investigate further and further outward until you have definitive evidence of where the problem lies. If the problem lies in some other bit of code that you don’t control, you’ll not only have learned essential troubleshooting and diagnostic skills, you’ll also have an audit trail of evidence to back up your claims, too. This is certainly a lot more work than shrugging your shoulders and pointing your finger at the OS, the tools, or the framework – but it also engenders a sense of trust and respect you’re unlikely to achieve through finger pointing and evasion.


If you truly aspire to being a humble programmer, you should have no qualms about saying “hey, this is my fault – and I’ll get to the bottom of it.”

[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[debugging techniques](https://blog.codinghorror.com/tag/debugging-techniques/)
[self-accountability](https://blog.codinghorror.com/tag/self-accountability/)
[programming errors](https://blog.codinghorror.com/tag/programming-errors-2/)
