---
title: "Avoiding Booleans"
date: 2005-10-28
url: https://blog.codinghorror.com/avoiding-booleans/
slug: avoiding-booleans
word_count: 448
---

Brad Abrams recently [posted](https://web.archive.org/web/20051126182024/http://blogs.msdn.com/brada/archive/2005/10/26/475085.aspx) another great excerpt from the unfortunately named [.NET Framework Standard Library Annotated Reference Volume 2](http://www.amazon.com/exec/obidos/ASIN/0321194454):


> **Avoid creating methods with Boolean parameters.** Boolean parameters make calls harder to read and harder to write.


Indeed. What *is* the difference between...

kg-card-begin: html

```

Authorization(“foo”, true)
Authorization(“foo”, false)

```

kg-card-end: html

Who knows? I’ve certainly made this mistake before. The SLAR recommends ditching the boolean in favor of an enumeration:

kg-card-begin: html

```

Authorization(“foo”, AuthorizationCompletion.Pending)
Authorization(“foo”, AuthorizationCompletion.Finished)

```

kg-card-end: html

Voila. Self-documenting code. If you’re not careful, boolean parameters become [magic numbers](http://en.wikipedia.org/wiki/Magic_number_(programming)).


Avoiding boolean parameters isn’t a new idea, of course; similar advice is dispensed by [C++ guru Herb Sutter](https://herbsutter.com/) in this [2002 C++ User’s Journal article](http://www.drdobbs.com/conversationstruth-or-consequences/184403845). What you may not realize, however, is that **it’s also a good idea to avoid booleans in your user interface**. Jef Raskin explains in his book, [The Humane Interface](http://www.amazon.com/exec/obidos/ASIN/0201379376):


> Check boxes can leave the user guessing what the alternative is. For example, if a check box labeled “Save to archive on closing” is checked, the data will be saved to an archive when the window is closed, but the label gives little clue as to what will happen if the box is not checked. Will the data be saved somewhere else, not saved at all, or will another option appear when you close the window? Often, the best solution is to use a set of radio buttons; they are not modal, and the user can clearly see not only the current state but also the alternative(s). Whether checkboxes or radio buttons are used, it is important to label with adjectives which describe the state of the affected object. If verbs are used as labels, the user does not know whether the action has taken place or is yet to take place.
> For one-of-many choices, radio buttons are already the standard, and there is rarely any reason to use other mechanisms. **Whenever possible, use radio buttons instead of checkboxes.** Checkboxes work reliably only when the value of the state controlled by the check is immediately visible or in short-term memory.


As a developer my go-to boolean UI element is the checkbox. If it can be true or false, it’s a checkbox, right? Like so:


![](https://blog.codinghorror.com/content/images/2025/03/image-341.png)


But what does the verb “Lock” *mean?* This checkbox violates the [Don’t Make Me Think](https://www.amazon.com/exec/obidos/ASIN/0321965515) rule. Now watch what happens when we change to adjectives and radio buttons:


![](https://blog.codinghorror.com/content/images/2025/03/image-340.png)


This is conceptually identical to the code sample; we simply switched from a boolean to an enumeration. It’s amazing how obvious the benefits are in retrospect, but it sure wasn’t obvious to me until today.

[enums](https://blog.codinghorror.com/tag/enums/)
[software development](https://blog.codinghorror.com/tag/software-development/)
[programming practices](https://blog.codinghorror.com/tag/programming-practices/)
[.net framework](https://blog.codinghorror.com/tag/net-framework/)
[user experience](https://blog.codinghorror.com/tag/user-experience/)
