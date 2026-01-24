---
title: "Regular Expressions for Regular Programmers"
date: 2009-06-08
url: https://blog.codinghorror.com/regular-expressions-for-regular-programmers/
slug: regular-expressions-for-regular-programmers
word_count: 533
---

If you’ve followed my blog for any length of time, you know that **I am a total regular expression fanboy**. It’s almost [embarrassing](https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/) how much I love the damn things. I’m pretty sure my teammates roll their eyes every time they see yet another class I’ve touched that has `using System.Text.RegularExpressions` at the top. You might as well rename it to `JeffHasBeenHere`.


I say that because I end up writing a lot of string handling code, even when people [tell me I shouldn’t](https://blog.codinghorror.com/programming-is-hard-lets-go-shopping/). Now, I only advocate responsible and judicious [use of regular expressions](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/) when you happen to be dealing with strings. In the wrong hands, regular expressions can be dangerous. You might end up wondering if Q*Bert just vomited [all over your source code](https://blog.codinghorror.com/regex-use-vs-regex-abuse/). Or you might be programming in Perl. Is there any difference? ([instant rimshot](http://www.instantrimshot.com/))


But I digress. Although I love regex, I’ve never been a fan of the classic regular expression reference book, Friedl’s [Mastering Regular Expressions](http://www.amazon.com/dp/0596528124). I found it dry, a bit academic, and lacking in practical real world examples. It just didn’t speak to me as a working programmer in the way that regular expressions themselves did, and that was disappointing.


That’s why I was so excited to discover that two of the gnarliest regex gurus I knew – [Jan Goyvaerts](http://www.just-great-software.com/aboutjg.html) (author of [RegexBuddy](http://www.regexbuddy.com/cgi-bin/affref.pl?aff=jatwood) and [regular-expressions.info](http://www.regular-expressions.info/)) and [Steven Levithan](http://blog.stevenlevithan.com/) (author of [XRegExp](http://blog.stevenlevithan.com/code) and [RegexPal](http://regexpal.com/)) – were putting their heads together to create **a regular expression reference for the rest of us**. I *immediately* pre-ordered it sight unseen.


That book is [Regular Expressions Cookbook](http://www.amazon.com/dp/1449319432). It arrived a few days ago, and although my expectations were high, I think this book has exceeded even the loftiest expectations I had. It is *outstanding*.


![](https://blog.codinghorror.com/content/images/2025/04/image-386.png)


What I love about this book is two three things:

1. It’s filled with **practical, real world examples of RegEx use**. At every step of the way, from beginner to master level, you’re building regular expressions that are actually useful in the wild, and not just abstract, obtuse academic exercises in solving string matching puzzles.
2. It covers all the **common gotchas** that you inevitably run into when you start building non-trivial regular expressions. Things like the sometimes massive (and painful) differences between regex libraries in various languages, subtle regex flavor quirks, catastrophic backtracking, unicode support, and so forth. These are all presented in context of the solutions, exactly as you’d encounter them in real programming. I know because I have the scars to prove it.
3. It was **updated and revised in the second edition** to reflect current flavor differences with new recipes, plus a whole new chapter on source code and log files. It also covers [XRegExp](https://github.com/slevithan/xregexp), an emerging standard, fully-featured regex library for JavaScript.


Regular Expressions Cookbook manages to be simultaneously accessible and almost *ridiculously* comprehensive. I consider myself a fairly advanced regex user and about 50 pages in I’ve already had three big “oh, wow, I didn’t realize that” moments. In my mind, at least, this completely replaces the Friedl book as the go-to reference for programmers of any skill level or background who seek regular expression enlightenment.


Needless to say, *recommended*.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[string handling](https://blog.codinghorror.com/tag/string-handling/)
[system.text.regularexpressions](https://blog.codinghorror.com/tag/system-text-regularexpressions/)
