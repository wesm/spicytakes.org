---
title: "Diseconomies of Scale and Lines of Code"
date: 2006-07-17
url: https://blog.codinghorror.com/diseconomies-of-scale-and-lines-of-code/
slug: diseconomies-of-scale-and-lines-of-code
word_count: 786
---

Steve McConnell on [diseconomies of scale](http://www.amazon.com/exec/obidos/ASIN/0735605351) in software development:


> **Project size is easily the most significant determinant of effort, cost and schedule [for a software project].***
> People naturally assume that a system that is 10 times as large as another system will require something like 10 times as much effort to build. But the effort for a 1,000,000 LOC system is *more* than 10 times as large as the effort for a 100,000 LOC system.
> [Using software industry productivity averages], the 10,000 LOC system would require 13.5 staff months. If effort increased linearly, a 100,000 LOC system would require 135 staff months. But it actually requires 170 staff months.


Here’s the single most important decision you can make on your software project if you want it to be successful: *keep it small.* Small may not accomplish much, but the odds of outright failure – a [disturbingly common outcome](https://blog.codinghorror.com/the-long-dismal-history-of-software-project-failure/) for most software projects – is low.


I don’t think the inverted, non-linear relationship between size and productivity on software projects will come as a shock to anyone; the guys at 37signals have been [banging](http://37signals.com/svn/archives2/when_big_groups_really_want_to_get_things_done_they_make_the_group_smaller.php) [their](http://37signals.com/svn/archives2/edward_hall_the_perfect_group_size_812.php) [drum](http://37signals.com/svn/archives2/the_disease_of_giants.php) on the virtues of small for over a year now. Isn’t [small the new big](http://sethgodin.typepad.com/seths_blog/2005/06/small_is_the_ne.html) already?


But what I really want to focus on here is **how you measure a project’s size**. What’s big? What’s small? McConnell is using lines of code (LOC) as his go-to measurement. Here’s a table that illustrates the relationship between project size and productivity:

kg-card-begin: html


| Project Size | Lines of code (per year) | COCOMO average |
| 10,000 LOC | 2,000 - 25,000 | 3,200 |
| 100,000 LOC | 1,000 - 20,000 | 2,600 |
| 1,000,000 LOC | 700 - 10,000 | 2,000 |
| 10,000,000 LOC | 300 - 5,000 | 1,600 |


kg-card-end: html

Lines of code is a reasonable metric to determine project size, but it also has some problems, which are well-documented in the Wikipedia entry [on lines of code](http://en.wikipedia.org/wiki/Source_lines_of_code):

kg-card-begin: html

```

/* How many lines of code is this? */
for (i=0; i<100; ++i) printf("hello");

```

kg-card-end: html

For one thing, different languages vary widely in the number of lines of code they produce. 100 lines of Perl will probably accomplish a lot more than 100 lines of C. So you have to be careful that you’re really comparing apples to apples. Furthermore, skilled developers know that the less code you write, the fewer bugs you’ve created – so they naturally distrust any productivity metric that weights absolute lines of code. And does code generation count?


Even with all its problems, the LOC metric is still where you should start, according to McConnell:


> My personal conclusion about using lines of code for software estimation is similar to Winston Churchill’s conclusion about democracy: **The LOC measure is a terrible way to measure software size, except that all the other ways to measure size are worse.** For most organizations, despite its problems, the LOC measure is the workhorse technique for measuring size of past projects and for creating early-in-the-project estimates of new projects. The LOC measure is the *lingua franca* of software estimation, and it is normally a good place to start, as long as you keep its limitations in mind.
> Your environment might be different enough from the common programming environments that lines of code are not highly correlated with project size. If that’s true, find something that is more proportional to effort, count that, and base your size estimates on that instead. Try to find something that’s easy to count, highly correlated with effort, and meaningful for use across multiple projects.


The Wikipedia article features this chart of Windows operating system size, in lines of code, over time:

kg-card-begin: html


| 1993 | Windows NT 3.1 | 6 million |
| 1994 | Windows NT 3.5 | 10 million |
| 1996 | Windows NT 4.0 | 16 million |
| 2000 | Windows 2000 | 29 million |
| 2002 | Windows XP | 40 million |
| 2007 | Windows Vista | ~50 million |


kg-card-end: html

If you’re wondering how much code the average programmer produces per day, I think you might be [asking the wrong question](https://web.archive.org/web/20060718002238/http://blogs.msdn.com/philipsu/archive/2006/06/14/631438.aspx). Lines of code is certainly a key metric for determining project size, but it’s also easily manipulated and misinterpreted. It should never be the only data point used to make decisions; it’s just one of many signposts on the road that helps you orient your project.


*What are the other most significant determinants? Number two is the type of software you’re developing, and personnel factors is a very close third.

[software development](https://blog.codinghorror.com/tag/software-development/)
[programming](https://blog.codinghorror.com/tag/programming/)
[project management](https://blog.codinghorror.com/tag/project-management/)
[software scaling](https://blog.codinghorror.com/tag/software-scaling/)
[lines of code](https://blog.codinghorror.com/tag/lines-of-code/)
