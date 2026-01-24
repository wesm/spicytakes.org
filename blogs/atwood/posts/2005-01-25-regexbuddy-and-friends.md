---
title: "RegexBuddy and Friends"
date: 2005-01-25
url: https://blog.codinghorror.com/regexbuddy-and-friends/
slug: regexbuddy-and-friends
word_count: 282
---

Jan Goyvaerts released a new version of [RegexBuddy](http://www.regexbuddy.com/cgi-bin/affref.pl) today. I’ve talked about this tool before – it’s easily the [best Regex tool](https://blog.codinghorror.com/my-buddy-regex/) available. Some feature highlights for this version are:

- Built in **GREP tool**
- Visual **regular expression debugging** support
- Full unicode support


The GREP tool is an unexpected bonus; it’s a mini version of his full [PowerGrep](http://www.powergrep.com) application, which I use occasionally. GREP is a natural (and very UNIX-y) progression once you’ve mastered regular expressions; consider the utility of Regexes on files and folders instead of strings and you’ve got the idea. Jan also maintains the excellent and free [www.regular-expressions.info](http://www.regular-expressions.info/) tutorial site. It’s a great reference.


Have you noticed that **the Visual Studio .NET find dialog supports regular expression searches**? That’s the good news. The bad news is, Microsoft decided to use bizarro world regular expression syntax. Many of the key Regex tokens are the same, but they behave in ways I wouldn’t expect from a Regex search. For example, searching for “[a-z]+” results in a match on entire words, but it *also* results in per-character matches in the word unless you tick the “Match whole word” option. So be prepared for some trial and error. Why couldn’t Microsoft just use standard Regex syntax, like the built in .NET Regex classes? If it’s a compatibility issue, why not let us select between bizarro and standard Regex syntax? I also heard that the VS.NET 2005 find dialog has the same problem, which is disappointing.


There is at least one add-in that provides standard [Regex find support in VS.NET](https://web.archive.org/web/20050204015443/http://www.codeproject.com/csharp/SearcherAddIn.asp) 2003. I’ve tried it, and it needs a bit of polishing, but it’s functional.

[regex](https://blog.codinghorror.com/tag/regex/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[tools](https://blog.codinghorror.com/tag/tools/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
