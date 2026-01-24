---
title: "To Compile or Not To Compile"
date: 2005-03-03
url: https://blog.codinghorror.com/to-compile-or-not-to-compile/
slug: to-compile-or-not-to-compile
word_count: 479
---

I am currently in the middle of a way-overdue refactoring of [MhtBuilder](https://web.archive.org/web/20050308160043/http://www.codeproject.com/vb/net/MhtBuilder.asp), which `RegexOptions.Compiled` uses [regular expressions](https://blog.codinghorror.com/my-buddy-regex/) extensively. I noticed that I had sort of mindlessly added `RegexOptions.Compiled` all over the place. It says “compiled” so it must be faster, right? Well, like so many other things, [that depends](https://web.archive.org/web/20060415123811/http://blogs.msdn.com/bclteam/archive/2004/11/12/256783.aspx):


> *In [the case of RegexOptions.Compiled], we first do the work to parse into opcodes. Then we also do more work to turn those opcodes into actual IL using Reflection.Emit. As you can imagine, this mode trades increased startup time for quicker runtime: in practice, **compilation takes about an order of magnitude longer to startup, but yields 30% better runtime performance.** There are even more costs for compilation that should mentioned, however. Emitting IL with Reflection.Emit loads a lot of code and uses a lot of memory, and that’s not memory that you’ll ever get back. In addition. in v1.0 and v1.1, we couldn’t ever free the IL we generated, meaning you leaked memory by using this mode. We’ve fixed that problem in Whidbey. But the bottom line is that **you should only use this mode for a finite set of expressions which you know will be used repeatedly.***


In other words, this is something you *don’t* want to do casually, as I was. And 30% faster isn’t a very compelling performance gain to balance against those serious tradeoffs. Unless you’re in a giant loop, or processing humongous strings, it’s almost never worth it. The MSDN documentation also has this interesting tidbit:


> *To improve performance, **the regular expression engine caches all regular expressions in memory.** This avoids the need to reparse an expression into high-level byte code each time it is used.*


The second time you build your non-compiled Regex, no additional interpreting overhead is incurred. And you get that for free. Even though it sounds faster and all, you probably don’t want to use `RegexOptions.Compiled`. But what about `Regex.CompileToAssembly`?


This avoid the pitfalls associated with dynamic compilation by turning your regular expressions into a compiled DLL. There aren’t many articles describing how to do this, but [Kent Tegels](https://web.archive.org/web/20060104170723/http://sqljunkies.com/WebLog/ktegels/archive/2004/03/03/1412.aspx) dug up a few Regex articles with sample code showing how to take advantage of `Regex.CompileToAssembly`:

- [Programming with Regular Expressions in C#](http://www.informit.com/articles/article.asp?p=27313&seqNum=6)
- [C# Regular Expressions, Revisited](https://web.archive.org/web/20050315065013/http://www.ondotnet.com/pub/a/dotnet/2002/03/11/regex2.html)


It seems ideal – all the advantages of compilation with none of the disadvantages – but it adds one disadvantage of its own: your regular expressions are now **written in stone**. You can’t change them at runtime, and you have to know what you’re going to do entirely up front. This might be a worthwhile tradeoff at the end of a large project that uses regular expressions extensively, but still... *only 30% faster?* I’d want some actual benchmark numbers from my application before I could justify the loss of flexibility and the additional file dependency.

[regex](https://blog.codinghorror.com/tag/regex/)
[performance](https://blog.codinghorror.com/tag/performance/)
[compiled code](https://blog.codinghorror.com/tag/compiled-code/)
[memory management](https://blog.codinghorror.com/tag/memory-management/)
[reflection.emit](https://blog.codinghorror.com/tag/reflection-emit/)
