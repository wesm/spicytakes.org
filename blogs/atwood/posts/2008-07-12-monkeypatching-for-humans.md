---
title: "Monkeypatching For Humans"
date: 2008-07-12
url: https://blog.codinghorror.com/monkeypatching-for-humans/
slug: monkeypatching-for-humans
word_count: 1131
---

Although [I love strings](https://blog.codinghorror.com/i-heart-strings/), sometimes the `String` class can break your heart. For example, in C#, there is no `String.Left()` function. Fair enough; we can roll up our sleeves and write our own function lickety-split:

kg-card-begin: html

```

public static string Left(string s, int len)
{
if (len == 0 || s.Length == 0)
return "";
else if (s.Length <= len)
return s;
else
return s.Substring(0, len);
}

```

kg-card-end: html

And call it like so:

kg-card-begin: html

```

var s = “Supercalifragilisticexpialidocious”;
s = Left(s, 5);

```

kg-card-end: html

Fairly painless, right?


But with the advent of C# 3.0, there’s an even better way – [extension methods](http://msdn.microsoft.com/en-us/library/bb383977.aspx). With an extension method, we “extend” the `String` to add the missing function. The code is fairly similar; I’ll highlight the changed parts in red.

kg-card-begin: html

```

public static string Left(this string s, int len)
{
if (len == 0 || s.Length == 0)
return "";
else if (s.Length <= len)
return s;
else
return s.Substring(0, len);
}

```

kg-card-end: html

And now we can call it **as if this very method existed on the String class as shipped**:

kg-card-begin: html

```

var s = “Supercalifragilisticexpialidocious”;
s = s.Left(5);

```

kg-card-end: html

Pretty slick. It’s difficult not to fall in love with extension methods, as they allow you to mold classes into exactly what you think they should be. This is fairly innocuous in C#, as **extension methods only allow you to add new functionality to classes**, not override, remove, or replace anything.


But imagine if you *could*.


Well, that’s exactly how it is in other, more dynamic languages such as Javascript, Python, Perl, and Ruby. Something as prosaic as C# extensions is old hat to these folks. In those languages, *you could redefine everything in the `String` class if you wanted to*. This is commonly known in dynamic language circles as [monkeypatching](http://en.wikipedia.org/wiki/Monkey_patch).


![](https://blog.codinghorror.com/content/images/2025/04/image-178.png)


If the idea of monkeypatching scares you a little, it probably should. Can you imagine debugging code where the `String` class had subtly different behaviors from the `String` you’ve learned to use? Monkeypatching [can be incredibly dangerous](http://avdi.org/devblog/2008/02/23/why-monkeypatching-is-destroying-ruby/) in the wrong hands, as Avdi Grimm notes:


> Monkey patching is the new black [in the Ruby community]. It’s what all the hip kids are doing. To the point that smart, experienced hackers reach for a monkey patch as their tool of first resort, even when a simpler, more traditional solution is possible.
> I don’t believe this situation to be sustainable. Where I work, **we are already seeing subtle, difficult-to-debug problems crop up as the result of monkey patching in plugins.** Patches interact in unpredictable, combinatoric ways. And by their nature, bugs caused by monkey patches are more difficult to track down than those introduced by more traditional classes and methods. As just one example: on one project, it was a known caveat that we could not rely on class inheritable attributes as provided by ActiveSupport. No one knew why. Every Model we wrote had to use awkward workarounds. Eventually we tracked it down in a plugin that generated admin consoles. It was overwriting `Class.inherited()`. It took us months to find this out.
> This is just going to get worse if we don’t do something about it. And the “something” is going to have to be a cultural shift, not a technical fix. I believe it is time for experienced Ruby programmers to wean ourselves off of monkey patching, and start demonstrating more robust techniques.


Try to imagine a world where **every programmer you know is a wannabe language designer, bent on molding the language to their whims**. When I close my eyes and imagine it, I have a vision of the apocalypse, a perfect, pitch-black storm of utterly incomprehensible, pathologically difficult to debug code.


I was just looking at random PHP plugin code the other day, and it was, frankly, crap. But that’s because *most code is crap*. [Including my own](https://blog.codinghorror.com/we-make-shitty-software-with-bugs/). It is, sadly, the statistical norm. That’s why [sites like The Daily WTF](https://blog.codinghorror.com/whats-wrong-with-the-daily-wtf/) are guaranteed to have more material than they can possibly ever publish for the next millennia. (Note to self: invest in this website). I can only imagine what that PHP plugin code would have looked like, had its developer been granted the ability to redefine fundamental PHP keywords and classes at will. These are the sort of thoughts that drive me to drink [Bawls](http://www.amazon.com/dp/B000NY30P0). And that stuff is disgusting.


You might say that PHP, sans the fundamental dynamic language ability to monkeypatch, is [just another crappy Blub language](http://weblog.raganwald.com/2006/10/are-we-blub-programmers.html). But there’s also a ton of [incredibly useful PHP code](https://blog.codinghorror.com/php-sucks-but-it-doesnt-matter/) out there. So it seems to me that the ability to monkeypatch doesn’t stop people from producing a huge volume of useful code, even in a kind of... horrible language. Some of it is even good!


While I acknowledge the power and utility of dynamic language monkeypatching, I know enough about programmers – myself *absolutely* included – to know the vast majority of us have absolutely no business whatsoever re-designing a programming language. There’s a reason some of the [most](http://en.wikipedia.org/wiki/Anders_Hejlsberg) [deeply](http://en.wikipedia.org/wiki/John_McCarthy_%28computer_scientist%29) [respected](http://en.wikipedia.org/wiki/Dennis_Ritchie) [computer](http://en.wikipedia.org/wiki/Guido_van_Rossum) [scientists](http://en.wikipedia.org/wiki/Niklaus_Wirth) in the world end up as language designers.


Perhaps then, given the risks, **monkeypatching should mean reaching for the meta-hammer as infrequently as humanly possible**. This is a position that Avdi himself espouses [in a followup comment](http://weblog.raganwald.com/2008/02/1100inject.html#8589089242300871488):

kg-card-begin: html

> I’m afraid a lot of people have missed the actual meat of my argument -- that dynamic extension of classes is currently overused in Ruby, in ways that are:
> Needless - another technique (such as a mixin, or locally extending individual objects) would have worked as well or better.
> Overcomplicated - the use of a monkey patch actually created more work for the author.
> Fragile - the solution is tightly bound to third-party internals, reducing the usefulness of the plugin or gem because it is prone to breakage.
> Excessively wide in scope - by hardcoding extensions to core classes, the author takes the choice to scope the change out of the plugin/gem user’s hands, further limiting utility.
> My point is that there are alternatives - often alternatives which are actually easier to implement and will make your plugin or gem more useful to the user.

kg-card-end: html

While I enjoy the additive nature of C# extensions, even those are enough to make me a little nervous, as mild as they are. Full-blown dynamic language monkeypatching goes even further; it might even be the ultimate expression of programming power. Is there anything more pure and godlike than **programming your own programming language?**


But if wielding that power doesn’t scare and humble you a little, too, then maybe you should leave the monkeypatching to the [really smart monkeys](http://www.paulgraham.com/langdes.html).

[c#](https://blog.codinghorror.com/tag/c-2/)
[extension methods](https://blog.codinghorror.com/tag/extension-methods/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[string manipulation](https://blog.codinghorror.com/tag/string-manipulation/)
