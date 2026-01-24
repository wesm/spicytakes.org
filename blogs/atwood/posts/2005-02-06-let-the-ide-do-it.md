---
title: "Let the IDE do it"
date: 2005-02-06
url: https://blog.codinghorror.com/let-the-ide-do-it/
slug: let-the-ide-do-it
word_count: 605
---

On Bruce Eckel’s [Static vs. Dynamic](https://web.archive.org/web/20050305012918/http://mindview.net/WebLog/log-0066) [typing]:


> *Despite this, I’ve had some leanings back in the direction of static type checking. As you point out, the goal is to create solid components – the question is how to accomplish that? In a dynamic language you have the flexibility to do rapid experimentation which is highly productive, but to ensure that your code is airtight you must be both proficient and diligent at unit testing. In a language that leans towards static type checking, the compiler will ensure that certain things will not slip through the cracks, and this is helpful, although the resulting language will typically make you work harder for a desired result, and the reader must also work harder to understand what you’ve done. I think the impact of this is much greater than we imagine.
> In addition, I think that statically typed languages give the illusion of program correctness. In fact, they can only go so far in determining the correctness of a program, by checking the syntax. But I think such languages encourage people to think everything is OK, when in fact the requirement for unit testing is just as important. I also suspect that the extra effort required to run the gauntlet of the compiler saps some of the energy required to do the unit testing. And you bring up an interesting question in suggesting that a dynamically-typed language may require more unit testing than a statically typed language. Of this I am not convinced; I suspect the amount may be roughly the same and if I am correct it implies that the extra effort required to jump through the static type-checking hoops may be less fruitful than we might believe.
> **What is the best of both worlds?** In my own experience, it’s very helpful to create models in a dynamic language, because there is a very low barrier to redesigning as you learn. Possibly more important, you’re able to quickly try out your ideas to see how they work with actual data, to get some real feedback about the veracity of the model, and change the model rapidly to conform to your new understanding.*


Bruce goes on to halfheartedly propose modeling in one [dynamic] language and developing in another [static] language.* Is this a workable solution? Personally, I don’t see why we can’t have our cake and eat it too – in a single language. If we tightly couple [the IDE and the language](https://blog.codinghorror.com/its-the-ide-dummy/), **the IDE could warn us about static typing errors, but give us the flexibility to treat the types dynamically when we compile.** Give the IDE some functionality traditionally assigned to the compiler: that’s the true leap of faith, and the only way to deliver the best of both worlds.


I have also been remiss in not mentioning Wesner Moise’s posts on [next-generation IDE designs](https://web.archive.org/web/20050413182840/http://wesnerm.blogs.com/net_undocumented/2004/06/whidbey_may_mis.html):


> *Religious beliefs about key bindings will disappear, because most of those key combinations will become completely irrelevant in the new world. Yes, Don Box will finally kiss his Emacs goodbye. The new paradigm actually eliminates syntax errors (at least, they will be flagged immediately by the new graphical editor) and many semantic errors, because each edit operation directly alters, adds or deletes a node in the in-memory parse tree.*


This also supports the tight IDE and compiler coupling that I think will become the watermark for next generation languages over the next 5-10 years.


*It’s difficult to imagine reading a more unenthusiastic endorsement of static typing. Although it’s true that static typing hasn’t killed any puppies. Yet.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[static type checking](https://blog.codinghorror.com/tag/static-type-checking/)
[dynamic language](https://blog.codinghorror.com/tag/dynamic-language/)
[ide](https://blog.codinghorror.com/tag/ide/)
[unit testing](https://blog.codinghorror.com/tag/unit-testing/)
