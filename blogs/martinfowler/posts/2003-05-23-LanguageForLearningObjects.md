---
title: "Language For Learning Objects"
description: "If I want to teach people object-orientation, which language should I use?"
date: 2003-05-23T00:00:00
tags: ["language feature", "programming environments", "ruby"]
url: https://martinfowler.com/bliki/LanguageForLearningObjects.html
slug: LanguageForLearningObjects
word_count: 432
---


**If I want to teach people object-orientation, which language should
I use?**


For the last couple of years the first choice language for learning
about objects has been Java. There's many good reasons to use
Java.

- It's widely known
- It uses a C based syntax which is becoming the dominant style.
- Free, high quality development environments are widely available
- Knowledge of Java helps in getting a job


For these reasons, I'd certainly not discourage the use of Java
(Although I would point out that C# has most of these attributes too
and would thus make a viable alternative.) However I wouldn't leave it just with Java. Java/C#/C++ show a certain
style of OO programming, and if you're going to introduce OO to people
I think it's good to show an alternative.


The alternatives I'd consider are [Ruby](http://ruby-lang.org/en/) and
[Python](http://python.org/). Both are dynamically typed languages, and
I think it's useful to have experiences in both static and dynamic
typing. Both languages are also
very useful - there's many a task that's easy to automate
with a quick script and I think every developer should have at least
one scripting language up their sleeve.


It's not such a big deal as which one of the two you should pick. Personally I'd go for
Ruby. Although Python is more widely used (and available), Ruby's more
pure in its OO (useful if that's what you're learning) and for me
feels significantly cleaner. Also Ruby has blocks: the ability to
easily create lumps of code as objects. Blocks are a powerful
programming tool that teaches a number of ideas about code structuring
that's hard to grasp otherwise - and provides an entry point for
functional languages.


Many people might ask âwhat about Smalltalk?â I can sympathize with
that since Smalltalk is still my favorite programming experience. But
the advantage of a scripting language is that it's something that a
professional programmer will use regularly, while even a
Smalltalk-lover like me hasn't cranked up an image in years.


All this raises another question - should you use a programming
language to teach OO. An alternative would be to discuss the
principles, perhaps illustrating with UML. I strongly believe you
should use a language primarily so that people can do things with
it. For me software design is much like mathematics. While you can get
a shallow appreciation by reading or listening you only really
understand it by doing. So to really understand OO you really have to
build something - and be encouraged to try it different ways in the
spirit of [PragDave's
Katas](http://pragprog.com/pragdave/Practices/Kata).
