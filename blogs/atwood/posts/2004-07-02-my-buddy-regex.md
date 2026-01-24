---
title: "My Buddy, Regex"
date: 2004-07-02
url: https://blog.codinghorror.com/my-buddy-regex/
slug: my-buddy-regex
word_count: 674
---

I generally don’t subscribe to the UNIX religion, but there is one area where I am an unabashed convert: regular expressions.


Yeah, the syntax is a little scary, but for processing strings, nothing is more effective. The RegEx is the power drill of the programmer’s toolkit: not appropriate for every job, but *the* go-to tool for a lot of common jobs. And what could be more common than the humble string, particularly in this day and age of HTML, XML, SOAP, and other plain text formats? Most modern development languages have complete Regular Expression support – even in the IDE for things like search and replace.


Over the last four years I’ve experimented with a number of commercial, freeware, and even homegrown RegEx tools. In the .NET era, I started with [Expresso](https://web.archive.org/web/20040704081147/http://www.codeproject.com/dotnet/expresso.asp), and I recently found out about [Regulator](https://web.archive.org/web/20040811081650/http://royo.is-a-geek.com/iserializable/regulator/), which is hands down the most impressive free RegEx tool I’ve encountered to date. But that was before I met my new best friend, [RegexBuddy](https://www.regexbuddy.com/index.html):


![](https://blog.codinghorror.com/content/images/2025/06/image-51.png)


I belatedly realized after I created this screenshot I may have accidentally picked the complicated “run away screaming” example. Great for me as an intermediate regex user, but not so great for introducing people to the miracle of RegEx. So let me apologize by way of explanation: this RegEx captures all valid HTML 4.0 tags. It also exploits a very powerful feature called **named captures **–** **see the ?<element> and ?<attr> highlighted in that tannish-brown? In .NET you can refer to those matches with a very simple, logical syntax:

kg-card-begin: html

```
Dim mc As MatchCollection = reg.Matches(strHTML)
Dim m As Match
For Each m In mc
m.Groups("element").ToString
m.Groups("attr").ToString
Next
```

kg-card-end: html

The one unique, killer feature that RegexBuddy has is **super fast, real-time highlighting of all possible matches as you type the regular expression**. That has always been my complaint about RegEx composition: it’s difficult to tell beforehand what the effect of your RegEx will be until you “run” it and browse all the matches. With RegexBuddy, you don’t have to – just type and watch. No running required. But that’s not the only great feature: the RegEx [decomposition and pre-built library](http://www.regexbuddy.com/screen.html) are also best of breed. Needless to say, highly recommended, and currently my preferred tool. It’s not free, but TANSTAAFL.


Once you come to grips with the basics of regular expressions, you’ll want a handy cheat sheet of the syntax. The best one I’ve found is [VisiBone’s JavaScript foldout](http://www.visibone.com/javascript/foldouts.html). There’s also [an online version](http://www.visibone.com/regular-expressions/). All the VisiBone stuff is super cool, and brings back warm memories of those incredible Beagle Brothers posters I had for the Apple //.


However, the information density does get a little ridiculous on the VisiBone cards, so I’d go with the foldouts or the wall charts, unless you enjoy squinting a lot. If you just can’t get enough, and you want to learn about the thrilling history of RegEx and understand how they work under the hood (try to envision me stifling a yawn at this point) there’s also the [O’Reilly book](http://www.oreilly.com/catalog/regex2/).


You may not even need to know the syntax if you can drop prebuilt RegExes into your code. Why build what you can steal? There are a number of sites with growing prebuilt repositories of regular expressions:

- [https://web.archive.org/web/20040706023926/http://www.3leaf.com/resources/articles/regex.aspx](https://web.archive.org/web/20040706023926/http://www.3leaf.com/resources/articles/regex.aspx)
- [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
- [http://www.regexlib.com/](http://www.regexlib.com/) (available as a web service!)


Drunk with the power and possibility of regular expressions, you might start thinking regular expressions can do... well, just about anything. I’ve been there, and let me warn you up front: they can’t do recursion – or reverse matching from the rear of a string – without some mighty ugly hacks. This rules out a lot of potential uses, or at least relegates RegExps to a helper role. And that’s a good thing. Despite their undeniable power, RegExps aren’t a procedural programming language. In limited string processing roles, they’re perfect. That’s what they were designed to do. But can you imagine writing an entire application with that kind of crazy, nigh-indecipherable syntax Perl?

[regex](https://blog.codinghorror.com/tag/regex/)
[regular expressions](https://blog.codinghorror.com/tag/regular-expressions/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
