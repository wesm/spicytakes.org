---
title: "Programming for Luddites"
date: 2004-12-02
url: https://blog.codinghorror.com/programming-for-luddites/
slug: programming-for-luddites
word_count: 392
---

There was much handwringing last week when Somasegar announced what we *already knew*: VB.NET 2005 [will not have refactoring](https://web.archive.org/web/20080821054228/http://weblogs.asp.net/somasegar/archive/2004/11/19/267109.aspx). This resulted in a few [emotional outbursts](https://web.archive.org/web/20051220051137/http://dotnetjunkies.com/WebLog/demiliani/archive/2004/11/20/32819.aspx):


> *We don’t need toys like [the] MY [namespace], we need working tool like Refactoring!!*


How can Microsoft refuse us those magical software writing robots they’ve promised?! We demand the “code my application” button! But seriously:

1. **I generally question the value of any “automatic” refactoring tool**. Refactoring is a complex activity that implies a deep level of understanding of the code. How is this captured in a menu item that turns a variable into a property? Or a menu item that extracts a block of code into a new method? Furthermore, I’d question the competency of any developer who required a tool to perform these bread and butter coding tasks efficiently.
2. **Refactoring is a pure IDE task, and thus relatively easy to implement as an add-on.** That’s why you can buy a half-dozen [different refactoring tools](https://web.archive.org/web/20041204184842/http://www.xtreme-simplicity.net/CSharpRefactory.html) for VS.NET 2003, but nobody sells an Edit and Continue add on. Go figure.
3. **Do you really think Microsoft can produce a refactoring tool superior to the third party alternatives?** Refactoring is just a bullet point on a box for MS. Third parties bet their entire companies on refactoring add-ins. Who do you think is going to have the better product?


The IDE is important, unquestionably, but implying that the lack of refactoring support in your IDE somehow keeps you from being a professional developer is just plain stupid. You want to be a professional developer? [Stop worrying about the tools](http://www.nedbatchelder.com/blog/20041128T190631.html) and write some damn code:


> *I haven’t had an opportunity to use Eclipse’s luxuriant refactoring tools and quick fix doodads. I’m sure they make developers more productive, how could they not? **But they won’t help me decide how to refactor**, or what the right semantics are for an abstraction, or predict in which ways the system will have to change in the next release. They won’t help me find the simple path among the complex, or choose just the right words to describe my thoughts, or understand the user’s problem better. They may help me be a more productive coder, but they won’t help me write better software.*


Ultimately, tools don’t make you a better developer. Experience does.

[refactoring](https://blog.codinghorror.com/tag/refactoring/)
[vb.net](https://blog.codinghorror.com/tag/vb-net/)
[programming](https://blog.codinghorror.com/tag/programming/)
[software development practices](https://blog.codinghorror.com/tag/software-development-practices/)
[ide](https://blog.codinghorror.com/tag/ide/)
