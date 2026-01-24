---
title: "C# and the Compilation Tax"
date: 2007-05-11
url: https://blog.codinghorror.com/c-and-the-compilation-tax/
slug: c-and-the-compilation-tax
word_count: 1020
---

Over the last four years, I’ve basically given up on the idea that .NET is a multiple language runtime.

- The so-called choice between the two most popular languages, C# and VB.NET, is no more meaningful than the [choice between Coke and Pepsi](https://blog.codinghorror.com/choosing-between-net-pepsi-and-net-coke/). Yes, IronPython and IronRuby are meaningfully different dynamic languages, but they’re somewhere on the horizon and far from first-class IDE citizens.
- There’s simply **too much cognitive friction** when translating back and forth between these two very, very similar languages. Semicolons or underscores? Case sensitivity or case insensitivity? Parentheses or brackets? Arrays that begin at one, or arrays that begin at zero? To-may-to or to-mah-to? It’s just not worth the mental effort it costs to keep track of all these nitpicky little differences that can bite you so easily.
- Mixing source code in different languages is awkward at best. You have to segregate each language into its own compliable project. Separate – but equal. Sort of. Well, mostly.
- Most of the community has settled on C# as the de-facto standard, so you’re in for a rough slog of code translation if you want to stick with VB and cleanly integrate commonly available source code libraries into your codebase. And if you want to *understand* the code you’re absorbing into your application (note: this isn’t really optional in my experience), you better learn how to read it without a bunch of mental translation gymnastics. And once you’ve learned how to read and write the language well enough to integrate it, you’ve come full circle. Like me, you’ll be left wondering why you didn’t just cut out the translation penalty entirely and stick with one language in the first place.


This is not to say that you can’t do multiple language development in .NET. But most of the time, it isn’t worth the hassle. It’s less painful to move with the herd and [choose C# like everyone else](https://blog.codinghorror.com/the-slow-brain-death-of-vb-net/). For the most part, **I’ve learned to suck it up and pretend C# is the only .NET language**. I’ll even grudgingly admit that explicitly ending lines with semicolons is way better than the mish-mash of carriage returns and underscores we have in VB.NET. But there are still two things that drive me nuts about C#.


The first is the [evil of case sensitivity](https://blog.codinghorror.com/the-case-for-case-insensitivity/). As an advocate for people over machines, I have to go on record stating that case sensitivity in a programming language is wrong, and will *always* be wrong. I know the decision is written in stone at this point, and it’s never going to change, so I’ll leave it at that. It’s [a religious issue](https://blog.codinghorror.com/are-you-there-god-its-me-microsoft/), and we software developers are [nothing if not religious](https://blog.codinghorror.com/software-development-its-a-religion/). Let’s move on.


The second is **the C# compilation tax**. When working in C#, I’m constantly compiling the solution to ensure that I haven’t broken anything. It’s a ridiculous productivity tax in an endless loop: Write some code. Compile. Write a little more code. Compile. Change a function. Compile. Rename a variable. Compile. Refactor some methods. Compile. Then compile again, just to be sure. Wait a second... did I compile this yet? Compile!


Notice a pattern here? I’m going to prematurely wear out my CTRL, SHIFT, and B keys. When coding in C#, I feel like a monkey in a cage that dispenses food pellets when I press CTRL+SHIFT+B. It’s a complete waste of time, but you’re compelled to do it through perverse incentives in the IDE.


What’s particularly sad about this is that, in my experience, most C# developers think manually compiling all the time is a natural state of affairs. Well, it isn’t. In VB.NET we have this [clever little technology](https://web.archive.org/web/20070517053251/http://www.panopticoncentral.net/articles/947.aspx) we call **background compilation**. Background compilation saves you the effort of all that meaningless, repetitive, mind-numbing manual compilation. It’s very simple: as you type, imagine all that CTRL+SHIFT+B-ing happening automagically in the background for you.


With background compilation, *I know immediately when I’ve made a mistake*. I don’t have to wait until the next time I manually invoke the compiler. Let’s say I was to type in the following C# code:

kg-card-begin: html

string s;
s = 1;


kg-card-end: html
Well, that code looks fine in the editor. Until I compile. Contrast that with the VB.NET equivalent:
kg-card-begin: html


Dim s As String
s = 1


kg-card-end: html
The second I finish typing the assignment (e.g., move my cursor off the second line), the statement is flagged as an invalid assignment. No compilation necessary; it automatically appears as an ambient squiggly underline in the background.This is an admittedly trivial example, but background compilation makes my life so much easier in VB.NET. It reduces the turnaround time between mistake and fix to virtually nothing. And you can do other clever things with it, such as quickly renaming a function or variable to get an idea of where it’s being referenced via the stack of compiler errors that appear. If nothing else, it’s one less thing I have to remember to do: oh yeah, the C# IDE shows me basic syntax problems, but I gotta compile my C# to see what’s *really* broken. Doesn’t that seem like [unnecessary work](https://blog.codinghorror.com/dont-make-me-think-second-edition/) to you? It sure does to me.Background compilation is something that, unlike case sensitivity, is *not* written in stone, and possibly *could* be fixed. It’s an IDE feature, not a language feature. Here’s hoping the C# team eventually **recognizes the massive productivity drain of the C# compilation tax for the average developer**. If some developers are masochists who hate productivity, then make background compilation a configurable option they can turn off. They can march off in lockstep, back to their wheel of never-ending CTRL+SHIFT+B pain. More power to ’em.Personally, I’d rather let the computer do the grunt work of compiling in the background. Freed from the onerous compilation tax, no longer compulsively invoking the compiler every few minutes, I can spend more time concentrating on my code.I may have accepted the C# penance, but I wish the saints at Microsoft would see fit to grant this one small wish to a converted VB.NET sinner.

[c#](https://blog.codinghorror.com/tag/c-2/)
[.net](https://blog.codinghorror.com/tag/net/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[ide](https://blog.codinghorror.com/tag/ide/)
