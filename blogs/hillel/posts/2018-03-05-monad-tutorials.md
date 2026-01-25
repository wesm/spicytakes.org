---
title: "Monad Tutorials for Other Topics"
date: 2018-03-05
url: https://www.hillelwayne.com/post/monad-tutorials/
slug: monad-tutorials
word_count: 395
---

“Mathematics doesn’t have a sense of time, but often we need to track time. So programmers borrow an idea from the field of formal logic and replace all functions `(f: A → B) ↦ f: A × T → B` where T is the partially ordered set `t1 ... tn`. If T is totally ordered we can then define a **mutation** as a tuple in `M ⊆ Var × Val × Val × T` such that `<x, a, b, t> ∈ M ⇔ x[b, t'] ∈ x'[a, t]`. The benefits of this should be obvious.”


“Just what is a **loop** anyway? Imagine you’re on a tricycle, delivering the paper to houses on a street. All of the houses with a *front yard*, you throw a paper into their yard. But as soon as you reach a house without a front yard, in addition to throwing a paper, you also throw a balloon filled with paint. Then you go home and eat some pizza. So a loop is just like a tricycle and the body is a pizza. Does that make sense?”


“You already use **functions**: every time you copy-paste code it’s like a little function! A function is just a way to copy-paste code without needing to hit “paste” a whole lot. In fact, a function is *exactly the same* as copy and paste and anybody who says otherwise is a snob who wants to keep programming too hard and elitist.”


“You don’t need to understand what a **test** is for. Just write something you want your program to do, and if it doesn’t do that, keep changing it until it does. There’s some important theoretical reasons here, but don’t worry about them. You care much more about the actual use of them, which is looking good in a whiteboard interview.”


“I don’t know why we keep obsessing over **imports**. Most people can get away just fine with making everything one big file, and then only when they actually need it, they can use imports. But we’ve made it a weird rite of passage in programming, where people don’t feel like they understand things until they’ve written a program with more than one file. We’re just making it hard for people.”


“A class is just the Hoare refinement of a modular term algebra, what’s the problem?”


*Thanks to [Vaibhav Sagar](http://vaibhavsagar.com/) and [Soham Chowdhury](https://mrkgnao.github.io/) for feedback!*
