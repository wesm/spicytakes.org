---
title: "Curly’s Law: Do One Thing"
date: 2007-03-01
url: https://blog.codinghorror.com/curlys-law-do-one-thing/
slug: curlys-law-do-one-thing
word_count: 716
---

In [Outliving the Great Variable Shortage](https://web.archive.org/web/20070305162706/http://blog.objectmentor.com/articles/2007/02/26/outliving-the-great-variable-shortage), Tim Ottinger invokes Curly’s Law:


> A variable should mean one thing, and one thing only. It should not mean one thing in one circumstance, and carry a different value from a different domain some other time. It should not mean two things at once. It must not be both a floor polish and a dessert topping. It should mean One Thing, and should mean it all of the time.


The late, great [Jack Palance](https://en.wikipedia.org/wiki/Jack_Palance) played grizzled cowboy Curly Washburn in the 1991 comedy [City Slickers](http://www.imdb.com/title/tt0101587/). Curly’s Law is defined in this bit of dialog from the movie:


> Curly: Do you know what the secret of life is?
> Mitch: No, what?
> Curly: This. [holds up one finger]
> Mitch: Your finger?
> Curly: One thing. **Just one thing**. You stick to that and everything else don’t mean *shit*.
> Mitch: That's great, but what's the “one thing?”
> Curly: [smiles] That’s what you gotta figure out...


**Curly’s Law, Do One Thing,** is reflected in several core principles of modern software development:

- [**Don’t Repeat Yourself**](http://www.artima.com/intv/dry.html)
If you have more than one way to express the same thing, at some point the two or three different representations will most likely fall out of step with each other. Even if they don’t, you’re guaranteeing yourself the headache of maintaining them in parallel whenever a change occurs. And change *will* occur. Don’t repeat yourself is important if you want flexible and maintainable software.
- [**Once and Only Once**](http://c2.com/xp/OnceAndOnlyOnce.html)
Each and every declaration of behavior should occur once, and only once. This is one of the main goals, if not *the* main goal, when refactoring code. The design goal is to eliminate duplicated declarations of behavior, typically by merging them or replacing multiple similar implementations with a unifying abstraction.
- [**Single Point of Truth**](https://web.archive.org/web/20070929111037/http://www.faqs.org/docs/artu/ch04s02.html)
Repetition leads to inconsistency and code that is subtly broken, because you changed only some repetitions when you needed to change all of them. Often, it also means that you haven’t properly thought through the organization of your code. Any time you see duplicate code, that’s a danger sign. Complexity is a cost; don’t pay it twice.


Although Curly’s Law definitely applies to normalization and removing redundancies, *Do One Thing* is more nuanced than the various restatements of *Do Each Thing Once* outlined above. It runs deeper. Bob Martin refers to it as [The Single Responsibility Principle](https://web.archive.org/web/20070307080842/http://butunclebob.com/ArticleS.UncleBob.SrpInRuby):

kg-card-begin: html

> **The Single Responsibility Principle says that a class should have one, and only one, reason to change**. As an example, imagine the following class:
> class Employee
> {
>   public Money calculatePay()
>   public void save()
>   public String reportHours()
> }
> This class violates the SRP because it has three reasons to change:
> The business rules having to do with calculating pay.
> The database schema.
> The format of the string that reports hours.
> We don’t want a single class to be impacted by these three completely different forces. We don’t want to modify the Employee class every time the accounts decide to change the format of the hourly report, or every time the DBAs make a change to the database schema, as well as every time the managers change the payroll calculation. Rather, we want to separate these functions out into different classes so that they can change independently of each other.

kg-card-end: html

Curly’s Law is about choosing a single, clearly defined goal for any particular bit of code: **Do One Thing**. That much is clear.


But in choosing one thing, you are ruling out an infinite universe of other possible things you *could* have done. **Curly’s Law also means consciously choosing what your code *won’t* do.** This is much more difficult than choosing what to do, because it runs counter to all the natural generalist tendencies of software developers. It could mean breaking code apart, violating traditional OOP rules, or introducing duplicate code. It’s taking one step backward to go two steps forward.


Each variable, each line of code, each function, each class, each project should Do One Thing. Unfortunately, we usually don’t find out what that one thing *is* until we’ve [reached the end of it](https://blog.codinghorror.com/development-is-inherently-wicked/).

[programming concepts](https://blog.codinghorror.com/tag/programming-concepts/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[best practices](https://blog.codinghorror.com/tag/best-practices/)
[variable naming](https://blog.codinghorror.com/tag/variable-naming/)
[clean code](https://blog.codinghorror.com/tag/clean-code/)
