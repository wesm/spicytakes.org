---
title: "Computer Languages aren’t Human Languages"
date: 2006-08-31
url: https://blog.codinghorror.com/computer-languages-arent-human-languages/
slug: computer-languages-arent-human-languages
word_count: 677
---

Though I’ve become agnostic about the utterly meaningless [non-choice between VB.NET and C#](https://blog.codinghorror.com/choosing-between-net-pepsi-and-net-coke/), the inherited syntax of C leaves a lot to be desired, in my opinion. And not just in [the case sensitivity department](https://blog.codinghorror.com/the-case-for-case-insensitivity/). Daniel Appleman, in his excellent e-book, [VB.NET or C#, Which to Choose?](https://legacy.desaware.com/products/books/net/vborc/index.aspx), concurs:

kg-card-begin: html

> Here I risk stepping on some toes, because language syntax is very much a religious issue with many programmers. Certainly we all tend to prefer the language syntax we are familiar with, and C++ and Java programmers will certainly find a great deal that is familiar in C#.
> It should also be clear from this section that the differences between the two languages in this area really are minor. Both have virtually the same functionality.
> Nevertheless, on the subject of object syntax, I must give the win to VB.NET. Just look at the inheritance declarations:
> public class BClass: AClass, Iint
> Public Class BClass
> Inherits AClass
> Implements Iint
> Look at the words used to control inheritance:
> abstract, sealed, virtual
> MustInherit, NotInheritable, Overridable, Overrides, Shadows
> When it comes to looking at code and understanding what it does — especially later on when the original developer has left and some young programmer right out of college has to figure out what it does quickly to solve some obscure bug or add a new feature, which one is going to be easier to understand? Visual Basic .NET.

kg-card-end: html

Although I do agree with Appleman on this point – *void* is for sci-fi geeks; *nothing* is for human beings – in the big scheme of things, it’s barely relevant. If the success or failure of your project hinges on the minor syntax differences between two virtually identical .NET languages, you have much deeper problems than choice of language.


Although the [tradeoff between verbosity and succinctness](https://blog.codinghorror.com/in-defense-of-verbosity/) is worth considering, there are other risks here. **Computer languages, however verbose you make them, shouldn’t try to become proxy versions of spoken languages.** I’ve never worked with [AppleScript](http://en.wikipedia.org/wiki/AppleScript) before, but it fell into this trap in a big way. Here’s a sample bit of AppleScript code to illustrate:

kg-card-begin: html

tell application “Mori”
tell front document
set a to first item of selection
set b to second item of selection
set a’s note to (a reference to a’s) note & (a reference to b’s note)
end tell
end tell


kg-card-end: html
Looks almost like a paragraph, doesn’t it? John Gruber calls AppleScript the [English-Likeness Monster](http://daringfireball.net/2005/09/englishlikeness_monster):The idea was, and I suppose still is, that AppleScript’s English-like façade frees you from worrying about computer-science-y jargon like classes and objects and properties and commands, and allows you to just say what you mean and have it just work.

But saying what you mean, in English, almost never “just works” and compiles successfully as AppleScript, and so to be productive you still have to understand all of the ways that AppleScript actually works. But this is difficult, because **the language syntax is optimized for English-likeness, rather than being optimized for making it clear just what the f**k is actually going on.**

This is why Python and JavaScript, two other scripting language of roughly the same vintage as AppleScript, are not only better languages than AppleScript, but are easier than AppleScript, even though neither is very English-like at all. Python and JavaScript’s syntaxes are much more abstract than AppleScript’s, but they are also more obvious. (Python, in particular, celebrates obviousness.)AppleScript’s **natural language metaphor** turns out to be more of a curse than a blessing.Some languages are arguably more readable than others, of course, but keeping the goal of clarity front and center is far more important than bickering about relatively meaningless language choices. [You can write FORTRAN in any language](https://blog.codinghorror.com/you-can-write-fortran-in-any-language/), so choose whatever language you’re most comfortable with and *optimize for making it clear what the f**k is going on.*(I thought about letting the f-bomb drop in this post for emphasis, but my fireball isn’t quite as daring as John Gruber’s.)

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[syntax](https://blog.codinghorror.com/tag/syntax/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[c#](https://blog.codinghorror.com/tag/c-2/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
