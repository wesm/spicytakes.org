---
title: "Code Smells"
date: 2006-05-18
url: https://blog.codinghorror.com/code-smells/
slug: code-smells
word_count: 1280
---

I’m often asked why the book [Refactoring](http://www.amazon.com/exec/obidos/ASIN/0201485672) isn’t included in my [recommended developer reading list](https://blog.codinghorror.com/recommended-reading-for-developers/). Although I own the book, and I’ve read it twice, I felt it was too prescriptive – if you see (x), then you must do (y). Any programmer worth his or her salt should already be refactoring aggressively. It’s so essential to the craft that if you have to read a book to understand how it works, you probably shouldn’t be a programmer in the first place.


There’s nothing wrong with codifying refactoring guidelines in a book. But the most important guideline is to **watch for warning signs in your own code – so called “**[**code smells**](http://en.wikipedia.org/wiki/Code_smell)**.”**


![](https://blog.codinghorror.com/content/images/2025/05/image-285.png)


Developing your “code nose” is something that happens early in your programming career, if it’s going to happen at all. I combined all the documented code smells I could find into this reference; most of these smells should be familiar to you.


### Code Smells Within Classes

kg-card-begin: html


| Comments | There’s a fine line between comments that illuminate and comments that obscure. Are the comments necessary? Do they explain “why” and not “what”? Can you refactor the code so the comments aren’t required? And remember, you’re writing comments for people, not machines. |
| Long Method | All other things being equal, a shorter method is easier to read, easier to understand, and easier to troubleshoot. Refactor long methods into smaller methods if you can. |
| Long Parameter List | The more parameters a method has, the more complex it is. Limit the number of parameters you need in a given method, or use an object to combine the parameters. |
| Duplicated code | Duplicated code is the bane of software development. Stamp out duplication whenever possible. You should always be on the lookout for more subtle cases of near-duplication, too. [Don’t Repeat Yourself!](http://www.artima.com/intv/dry.html) |
| Conditional Complexity | Watch out for large conditional logic blocks, particularly blocks that tend to grow larger or change significantly over time. Consider alternative object-oriented approaches such as decorator, strategy, or state. |
| Combinatorial Explosion | You have lots of code that does *almost* the same thing... but with tiny variations in data or behavior. This can be difficult to refactor – perhaps using generics or an interpreter? |
| Large Class | Large classes, like long methods, are difficult to read, understand, and troubleshoot. Does the class contain too many responsibilities? Can the large class be restructured or broken into smaller classes? |
| Type Embedded in Name | Avoid placing types in method names; it’s not only redundant, but it forces you to change the name if the type changes. |
| Uncommunicative Name | Does the name of the method succinctly describe what that method does? Could you read the method’s name to another developer and have them explain to you what it does? If not, rename it or rewrite it. |
| Inconsistent Names | Pick a set of standard terminology and stick to it throughout your methods. For example, if you have Open(), you should probably have Close(). |
| Dead Code | Ruthlessly delete code that isn’t being used. That’s why we have source control systems! |
| Speculative Generality | Write code to solve today’s problems, and worry about tomorrow’s problems when they actually materialize. Everyone loses in the “what if...” school of design. [You (Probably) Aren’t Gonna Need It](http://xp.c2.com/YouArentGonnaNeedIt.html). |
| Oddball Solution | There should only be one way of solving the same problem in your code. If you find an oddball solution, it could be a case of poorly duplicated code – or it could be an argument for the adapter model, if you really need multiple solutions to the same problem. |
| Temporary Field | Watch out for objects that contain a lot of optional or unnecessary fields. If you’re passing an object as a parameter to a method, make sure that you’re using all of it and not cherry-picking single fields. |


kg-card-end: html

### Code Smells Between Classes

kg-card-begin: html


| Alternative Classes with Different Interfaces | If two classes are similar on the inside, but different on the outside, perhaps they can be modified to share a common interface. |
| Primitive Obsession | Don’t use a gaggle of primitive data type variables as a poor man’s substitute for a class. If your data type is sufficiently complex, write a class to represent it. |
| Data Class | Avoid classes that passively store data. Classes should contain data *and* methods to operate on that data, too. |
| Data Clumps | If you always see the same data hanging around together, maybe it belongs together. Consider rolling the related data up into a larger class. |
| Refused Bequest | If you inherit from a class, but never use any of the inherited functionality, should you really be using inheritance? |
| Inappropriate Intimacy | Watch out for classes that spend too much time together, or classes that interface in inappropriate ways. Classes should know as little as possible about each other. |
| Indecent Exposure | Beware of classes that unnecessarily expose their internals. Aggressively refactor classes to minimize their public surface. You should have a compelling reason for every item you make public. If you don’t, hide it. |
| Feature Envy | Methods that make extensive use of another class may belong in another class. Consider moving this method to the class it is so envious of. |
| Lazy Class | Classes should pull their weight. Every additional class increases the complexity of a project. If you have a class that isn’t doing enough to pay for itself, can it be collapsed or combined into another class? |
| Message Chains | Watch out for long sequences of method calls or temporary variables to get routine data. Intermediaries are dependencies in disguise. |
| Middle Man | If a class is delegating all its work, why does it exist? Cut out the middleman. Beware classes that are merely wrappers over other classes or existing functionality in the framework. |
| Divergent Change | If, over time, you make changes to a class that touch completely different parts of the class, it may contain too much unrelated functionality. Consider isolating the parts that changed in another class. |
| Shotgun Surgery | If a change in one class requires cascading changes in several related classes, consider refactoring so that the changes are limited to a single class. |
| Parallel Inheritance Hierarchies | Every time you make a subclass of one class, you must also make a subclass of another. Consider folding the hierarchy into a single class. |
| Incomplete Library Class | We need a method that’s missing from the library, but we’re unwilling or unable to change the library to include the method. The method ends up tacked on to some other class. If you can’t modify the library, consider isolating the method. |
| Solution Sprawl | If it takes five classes to do anything useful, you might have solution sprawl. Consider simplifying and consolidating your design. |


kg-card-end: html

This list was derived from the [Smells to Refactorings PDF](http://industriallogic.com/papers/smellstorefactorings.pdf), and the [Smells to Refactorings Wiki](http://web.archive.org/web/20060610214930/http://wiki.java.net/bin/view/People/SmellsToRefactorings), which also provide additional guidance on the specific refactorings that might be helpful in each instance. The important thing, from my perspective, isn’t the refactoring – it’s **learning to recognize the scent of your own code**.


And if you want examples of the stinkiest code imaginable, [How to Write Unmaintainable Code](https://web.archive.org/web/20060513032145/http://thc.org/root/phun/unmaintain.html) is a good place to start.

[refactoring](https://blog.codinghorror.com/tag/refactoring/)
[code smells](https://blog.codinghorror.com/tag/code-smells/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[technical practices](https://blog.codinghorror.com/tag/technical-practices/)
