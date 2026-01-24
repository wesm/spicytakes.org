---
title: "Why Objects Suck, Revisited"
date: 2004-09-20
url: https://blog.codinghorror.com/why-objects-suck-revisited/
slug: why-objects-suck-revisited
word_count: 200
---

I recently blogged about how pure [object oriented programming is oversold](https://blog.codinghorror.com/why-objects-suck/). Well, evidently [Paul Graham agrees with me](http://www.paulgraham.com/noop.html):


> *Object-oriented programming generates a lot of what looks like work. Back in the days of fanfold, there was a type of programmer who would only put five or ten lines of code on a page, preceded by twenty lines of elaborately formatted comments. Object-oriented programming is like crack for these people: it lets you incorporate all this scaffolding right into your source code. Something that a Lisp hacker might handle by pushing a symbol onto a list becomes a whole file of classes and methods. So it is a good tool if you want to convince yourself, or someone else, that you are doing a lot of work.*


I’ve found that **a little object orientation goes a long way**. Pushing too far into “everything must be an object” territory leads to, well, exactly what Paul describes above – giant masses of repetitive code that someone is going to have to maintain. I like to err on the side of simplicity, and that typically means the approach that produces the least volume of source code.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[object-oriented programming](https://blog.codinghorror.com/tag/object-oriented-programming/)
