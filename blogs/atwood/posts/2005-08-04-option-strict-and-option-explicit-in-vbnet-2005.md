---
title: "Option Strict and Option Explicit in VB.NET 2005"
date: 2005-08-04
url: https://blog.codinghorror.com/option-strict-and-option-explicit-in-vbnet-2005/
slug: option-strict-and-option-explicit-in-vbnet-2005
word_count: 617
---

I just noticed that Option Explicit is on by default for new VB solutions in Visual Studio .NET 2005:


![](https://blog.codinghorror.com/content/images/2025/05/image-123.png)


It’s about damn time.


There’s nothing more vicious than making an innocent typo when referencing a variable and not knowing about it because the compiler silently declares a new variable for you:

kg-card-begin: html

```

MyStringName = “Pack my box with five dozen liquor jugs”
Console.WriteLine(MyStringNam)

```

kg-card-end: html

Just talking about it makes my eye twitch uncontrollably. It’s almost as bad as making a language case sensitive.


Option Explicit Off is pure, unmitigated evil, yet Option Explicit Off is the default in VS.NET 2002 and 2003. I’ve audited a half-dozen VB.NET projects where, months into development, the developers didn’t realize that it was off! Laugh all you want, but this is the power of default values.


Paul Vick pointed out that **VS.NET 2002 and later do in fact ship with Option Explicit On set by default**. What I really needed was an option not to work with knuckleheads who turn it off, because I got bitten with this one a few times.


I’m not sure that Option Strict is quite the no-brainer that Option Explicit is, but Dan Appleman sure has [strong feelings about it](https://web.archive.org/web/20050829183259/http://tutorials.lockergnome.com/library/20041104_exploring_net_volume_1.phtml):


> *One of the debates that has arisen with the arrival of Visual Basic .NET is the use of Option Strict. Option Strict turns on strong type checking. You’ve probably heard about “*[*evil type coercion*](http://vb.mvps.org/articles/pt199511.pdf)*” (pdf) in Visual Basic 6 – VB6’s habit of converting data types automatically based on its best guess of what you want to do. While this can be a convenience to programmers, it can also lead to obscure and unexpected bugs when VB’s guess does not correspond to what you intended.
> The incorporation of strict type checking into Visual Basic .NET represents one of the most important improvements to the language. Unfortunately, Microsoft showed a stunning lack of confidence in their decision to incorporate it by leaving Option Strict off by default. In other words, when you create a new VB.NET project, strict type checking remains off.
> Some argue that this is a good thing. Leaving Option Strict off allows VB.NET to automatically convert data types in the same way as VB6. Not only that, but with strict type checking off, VB.NET can automatically perform late binding on Object variables in the same way as VB6 (where a variable is of type “Object,” VB will perform a late bound call on the object, correctly calling the requested method if it exists).
> The people who make these arguments are wrong.
> You should ALWAYS turn Option Strict On for every application.*


He also calls this **Option Slow**, referring to the slow, expensive IL that must be emitted behind the scenes for this magical type conversion scheme to work – the source of endless “VB.NET is slower than C#” benchmarks.


I tend to agree that this probably shouldn’t be off by *default*, but it’s nowhere near as poisonous as Option Explicit. Option Explicit Off has no legitimate use. Option Strict Off has one clear use case: it’s great when you’re writing a lot of [late binding code](http://swigartconsulting.blogs.com/tech_blender/2005/03/granular_late_b.html). Let the IL deal with all the nasty, verbose type conversions. As Scott points out, we can now use **partial classes in VB.NET 2.0 to mark selected sections of code Option Strict Off** while leaving the rest Option Strict On. It’s the best of both worlds.


I guess I could be [critical of Microsoft](https://web.archive.org/web/20060103183127/http://loudcarrot.com/Blogs/dave/archive/2005/04/24/2566.aspx) for not having the balls to also turn Option Strict on by default, but I consider it a minor miracle that we even got Explicit. I’ll take it.

[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
