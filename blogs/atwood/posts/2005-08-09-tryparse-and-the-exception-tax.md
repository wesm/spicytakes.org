---
title: "TryParse and the Exception Tax"
date: 2005-08-09
url: https://blog.codinghorror.com/tryparse-and-the-exception-tax/
slug: tryparse-and-the-exception-tax
word_count: 528
---

In .NET 1.1, TryParse is only [available for the Double datatype](https://web.archive.org/web/20060207121751/http://msdn.microsoft.com/library/en-us/cpref/html/frlrfSystemDoubleClassTryParseTopic.asp). Version 2.0 of the framework [extends TryParse](http://www.mikepope.com/blog/DisplayBlog.aspx?permalink=1239) to all the basic datatypes. Why do we care? Performance. Parse throws an exception if the conversion from a string to the specified datatype fails, whereas TryParse explicitly *avoids* throwing an exception.


Julia Lerman showed a screenshot of a cool little demo app demonstrating the performance difference between Parse and TryParse in a presentation of hers (ppt) that I stumbled across a few months ago. I was shocked how much faster TryParse was! I knew [exceptions were slow](https://web.archive.org/web/20050908004303/http://www.howzatt.demon.co.uk/articles/12May04.html), but… wow.


The original source for this sample app was a [BCL team blog entry](https://web.archive.org/web/20060208011119/http://blogs.msdn.com/bclteam/archive/2003/10/22/49710.aspx) from way back in October 2003. That code sample is pretty ancient by now, so I thought I’d pick it up and update it so that it at least loads in VS.NET 2005 beta 2. In the process of doing this, I found out that this little sample app has... er... some bugs. A lot of bugs, actually. Bugs that made this dramatic performance difference not so dramatic any more:


![](https://blog.codinghorror.com/content/images/2025/05/image-127.png)


So, yeah, parsing with exceptions is quite a bit slower, but not “did someone just downgrade my computer to a 486?” slower. The general rule of **avoiding exceptions in your primary code paths** still applies. That said, it’s not unreasonable to use exceptions for program flow when the situation warrants it, as [Alex Papadimoulis points out](http://weblogs.asp.net/alex_papadimoulis/archive/2005/04/01/396734.aspx):


> I think that there’s a general consensus out there that Exceptions should be limited to exceptional circumstances. But “exceptional” is a rather subjective adjective, so there’s a bit of a gray area as to what is and isn’t an appropriate use of Exceptions.
> Let’s start with an inappropriate use that we can all agree on. I can think of no better place to find [such an example](http://thedailywtf.com/ShowPost.aspx?PostID=22954) than TheDailyWTF.com. Although that particular block of code doesn’t exactly deal with throwing exceptions, it is a very bad way of handling exceptions. At the other extreme, exceptions are appropriate for handling environment failure. For example, if your database throws “TABLE NOT FOUND,” that would be the time to catch, repackage, and throw an exception.
> But it’s in the middle where there’s a bit of disagreement. One area in particular I’d like to address in this post is exceptions to business rules. I mentioned this as an appropriate before, but noticed there was quite a bit of disagreement with that. But the fact of the matter is, exceptions really are the best way to deal with business rule exceptions.


Alex concludes that, in this case, using exceptions to propagate errors across the tiers is a better solution. He’s **willing to pay the exception performance tax**:


> Less code, less mess. Nanoseconds slower? Probably. A big deal in the context of a web request going through three physical tiers? Not at all.


I totally agree. As long as you’re aware of the cost, this is a perfectly reasonable thing to do. An iron-clad adherence to the “avoid all exceptions” rule would be a net loss.


[Download the updated TryParse demo VS.NET 2005 solution](https://github.com/coding-horror/TryParse) (17kb zip)

[c#](https://blog.codinghorror.com/tag/c-2/)
[.net](https://blog.codinghorror.com/tag/net/)
[exception handling](https://blog.codinghorror.com/tag/exception-handling/)
[parsing](https://blog.codinghorror.com/tag/parsing/)
[performance](https://blog.codinghorror.com/tag/performance/)
