---
title: "The Greatest Invention in Computer Science"
date: 2008-06-06
url: https://blog.codinghorror.com/the-greatest-invention-in-computer-science/
slug: the-greatest-invention-in-computer-science
word_count: 802
---

What do you think the single greatest invention in computer science is? Besides the computer itself, I mean.


![](https://blog.codinghorror.com/content/images/2025/08/ti-99-4a-loadscreen-2.png)


Seriously, before reading any further, pause here for a moment and consider the question.


![](https://blog.codinghorror.com/content/images/2025/08/ti-99-4a-press-1-for-ti-basic.png)


I’ve talked before about [how young](https://blog.codinghorror.com/the-two-types-of-programmers/) so-called modern computer programming languages really are, and it bears repeating for context.

kg-card-begin: html

> C is roughly as old as I am; FORTRAN is as old as my parents. But what about the new kids on the block? The TIOBE software [TCPI metrics page](https://web.archive.org/web/20080609230449/http://www.tiobe.com/content/paperinfo/tpci/index.html) provides some data on language popularity going back to the year 2001. Consider the tender age of many of the newest, hippest programming languages:
> [Perl](http://en.wikipedia.org/wiki/Perl) (1987)
> [Python](http://en.wikipedia.org/wiki/Python_programming_language) (1991)
> [Erlang](http://en.wikipedia.org/wiki/Erlang_programming_language) (1991)
> [Ruby](http://en.wikipedia.org/wiki/Ruby_programming_language)(1993)
> [Java](http://en.wikipedia.org/wiki/Java_programming_language)(1995)
> [JavaScript](http://en.wikipedia.org/wiki/JavaScript) (1995)
> [PHP](http://en.wikipedia.org/wiki/PHP) (1995)
> Ruby is barely a teenager. JavaScript and PHP haven’t even *hit* their teens yet.

kg-card-end: html

For all our talk about fancy new programming language features, I sometimes think we forget the one fundamental building block underlying all of them: the humble routine. Take it from Steve McConnell, who urges us to [Use Routines, Routinely](http://stevemcconnell.com/ieeesoftware/bp16.htm):


> Aside from the invention of the computer, **the routine is arguably the single greatest invention in computer science**. It makes programs easier to read and understand. It makes them smaller (imagine how much larger your code would be if you had to repeat the code for every call to a routine instead of invoking the routine). And it makes them faster (imagine how hard it would be to make performance improvements in similar code used in a dozen places rather than making all the performance improvements in one routine). In large part, **routines are what make modern programming possible.**


If you’re not old enough to remember life before routines, I thought James Shore had a great example of the stark difference in his excellent article [Quality With a Name](https://www.jamesshore.com/v2/blog/2006/quality-with-a-name):


Before structured programming:

kg-card-begin: html

```

1000 NS% = (80 - LEN(T$)) / 2
1010 S$ = ""
1020 IF NS% = 0 GOTO 1060
1030 S$ = S$ + " "
1040 NS% = NS% - 1
1050 GOTO 1020
1060 PRINT S$ + T$
1070 RETURN

```

kg-card-end: html

![](https://blog.codinghorror.com/content/images/2025/08/ti-99-4a-center-string-basic-code.png)


After structured programming:

kg-card-begin: html

```

public void PrintCenteredString(string text) {
  int center = (80 - text.Length) / 2;
  string spaces = "";
  for (int i = 0; i < center; i++) {
    spaces += " ";
  }
  Print(spaces + text);
}

```

kg-card-end: html

The humble routine is the backbone of all programming in any modern language. I’m sure you’re the very model of a modern major programmer, so I won’t bore you with a long explanation of why routines are a good idea. The [original 1998 IEEE McConnell article](https://ieeexplore.ieee.org/document/687957) covers the rationales behind routines quite well. There’s also a greatly expanded version of that material in Chapter 7 of [Code Complete 2](https://bookshop.org/p/books/code-complete-steve-mcconnell/12551815).


![](https://blog.codinghorror.com/content/images/2025/08/code-complete-2-page-161-162.png)


Routines are so fundamental to today’s programming that they are essentially invisible. **That’s the problem with routines: they only take a minute to learn, but a lifetime to master.** If bad unstructured programming was possible, so is bad structured programming. [You can write FORTRAN in any language.](https://blog.codinghorror.com/you-can-write-fortran-in-any-language/) Wrestling with the ineffable essence of a routine is, almost to a first approximation, what programming now *is*:

- How long should this routine be? How long is too long? How short is too short? When is code “too simple” to be in a routine?
- What parameters should be passed to this routine? What data structures or data types? In what order? How will they be used? Which will be modified as a result of the routine?
- What’s a good name for this routine? Naming is hard. [Really hard](https://blog.codinghorror.com/i-shall-call-it-somethingmanager/).
- How is this routine related to other nearby routines? Do they happen at the same time, or in the same order? Do they share common data? Do they really belong together? What order should they be in?
- How will I know if the code in this routine succeeded? Should it return a success or error code? How will exceptions, problems, and error conditions be handled?
- Should this routine *even exist at all?*


Good programmers – regardless of whatever language they happen to be working in – understand the importance of crafting each routine with [the utmost care](https://secretgeek.net/upsert_revisited). The routines in your code should be treated like tiny, highly polished diamonds, each one more exquisitely polished and finely cut than the last.


I’ll grant you this isn’t a particularly deep insight. It’s not even original advice. But if you believe, as I do, in constantly [practicing the fundamentals](https://blog.codinghorror.com/programming-is-hard-lets-go-shopping/), **you’ll never stop mastering the art of writing the perfect routine.**


It is, after all, the single greatest invention in computer science.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[technology trends](https://blog.codinghorror.com/tag/technology-trends/)
[computer science](https://blog.codinghorror.com/tag/computer-science/)
[routines](https://blog.codinghorror.com/tag/routines/)
