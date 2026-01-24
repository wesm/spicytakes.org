---
title: "Don’t Be Afraid to Break Stuff"
date: 2004-11-04
url: https://blog.codinghorror.com/dont-be-afraid-to-break-stuff/
slug: dont-be-afraid-to-break-stuff
word_count: 332
---

One warning sign I look for when working with other developers is **fear of breaking the code**. The absolute worst systems I’ve worked on are the ones where the developers practically tiptoe around the source code.


The main problem with fear of breaking the code is the **implicit assumption that any code is really that good to begin with**. All the code we write is broken. Your code. [My code](https://blog.codinghorror.com/we-make-shitty-software-with-bugs/). Everyone’s code. Software development isn’t a science; it’s a process of continual refinement.


Now, I’m not proposing that every developer start ripping through a stable, production codebase and start rewriting it as an exercise. There’s certainly a learning curve that comes with any new codebase, and appropriate testing should always be performed. However, **I firmly believe that the absolute best way to learn a system is to break it.** Over and over. Start by breaking off a small piece. What happens when you turn that off? What are the consequences of deleting this variable? Does that function need to be here? If you can’t break that codebase, and then piece it back together again – in every way you can think of – then you’re going to be absolutely screwed when another developer breaks something. Or, even worse, a user breaks something. And they will, in ways you haven’t even considered.


Once you’ve broken enough stuff, a new codebase stops being scary, and starts being... sorta fun. Those [broken windows](http://www.artima.com/intv/fixit.html) will seem a lot less like intimidating roadblocks, and more like candidates for fixing – or at least boarding over. And while you’re at it, why not [remodel the place](http://c2.com/cgi/wiki?RefactorMercilessly=), too? When it comes to software, **controlled destruction breeds confidence.**


The most direct way to improve as a software developer is to be absolutely fearless when it comes to changing your code. Developers who are afraid of broken code are developers who will never mature into professionals.


So, go ahead. Break stuff!

[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[learning by breaking](https://blog.codinghorror.com/tag/learning-by-breaking/)
[code quality](https://blog.codinghorror.com/tag/code-quality/)
