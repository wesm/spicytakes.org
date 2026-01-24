---
title: "Parsing: Beyond Regex"
date: 2005-04-01
url: https://blog.codinghorror.com/parsing-beyond-regex/
slug: parsing-beyond-regex
word_count: 565
---

I’ve blogged ad nauseam about how much [I love Regular Expressions](https://blog.codinghorror.com/if-you-like-regular-expressions-so-much-why-dont-you-marry-them/), but even the mighty regular expression has limits. As noted in [Daniel Cazzulini’s blog](http://weblogs.asp.net/cazzu/archive/2005/01/10/RegexParsing.aspx):


> ***A full-blown programming language cannot be parsed with regular expressions.** But given the limited number of programming languages (successful ones, let’s say), how big do you think is the niche for getting proficient with those tools/techniques?
> There is an immensely bigger amount of common problems and small parsing needs that are very cost-effectively solved with regular expressions. For example, you don’t need much more than that to parse XML, XPath, XPointer, DataBinder.Eval-like .NET expressions, templates, MSBuild property references, Postbuild commands, etc. etc. etc. So becoming proficient with regexes is much more important and relevant to solve day to day problems than mastering BNF, lex/yacc, or any other full-blown parsing techniques/tools, IMO.*


Indeed, when colorizing code with simple(ish) regular expressions, you’ll run into annoying edge conditions like this one:

kg-card-begin: html

```
Dim s as String
s = "This is a string with ""quotes"""
```

kg-card-end: html

Or, let’s say we wanted to parse out HTML tags with this naïve regular expression:

kg-card-begin: html

```
<tag[^>]*>(.*?)</tag>
```

kg-card-end: html

Seems solid enough, right? Well, there are problems. What about nested tags? What about a tag that contains improperly escaped characters, like this one (from a real blog, by the way):

kg-card-begin: html

```
<input type="submit" name="previewcomment" value="preview >>">
```

kg-card-end: html

While you can hack around these problems with more and more [regular expression cleverness](https://web.archive.org/web/20051026035131/http://weblogs.asp.net/rosherove/archive/2003/05/13/6963.aspx), you eventually paint yourself into a corner with complexity. Regular expressions don’t truly understand the code that they are colorizing – *but parsers do*. Depending on the problem you’re attacking, at some point you have to **bite the bullet and utilize a full-blown parser**.


Drazen Dotlic recently published an [interesting CodeProject article](https://web.archive.org/web/20050623081400/http://www.codeproject.com/aspnet/CSharpColorizer.asp) discussing how to use the CoCo-R parser to parse and colorize C#:


> *Why don’t existing tools provide better formatting and color coding? **Because parsing is hard.** I thought I knew well most of the C# language constructs before I started working on the Colorizer. Boy, was I wrong! Throughout the course of this project, I have run into several constructs I have never seen before. I have also learned to appreciate more the work of the guys building the C# compiler. If it takes a team of people in Microsoft to properly deal with this issue, how could I have done it alone and in my spare time?
> Sir Isaac Newton said “If I have seen farther than others, it is because I was standing on the shoulders of giants,” and in this case, I was standing on the shoulders of *[*Coco-R*](http://www.ssw.uni-linz.ac.at/Research/Projects/Coco/)*.
> Coco-R is a compiler compiler (I guess that’s where coco comes from). You have probably heard of tools like lex and YACC - Coco-R is a modern version of these tools. What’s really great about it is that there are ports to several languages including C#. This is very convenient because additional processing you may want to do during parsing can be written in the same language tool itself is written in - C#.*


Drazen’s article offers a HTTP handler and a web control that harness the CoCo-R parser to colorize and reformat code with a level of fidelity you’ll never get from regular expressions. Good stuff.

[parsing](https://blog.codinghorror.com/tag/parsing/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
