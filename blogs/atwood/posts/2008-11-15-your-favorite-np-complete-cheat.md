---
title: "Your Favorite NP-Complete Cheat"
date: 2008-11-15
url: https://blog.codinghorror.com/your-favorite-np-complete-cheat/
slug: your-favorite-np-complete-cheat
word_count: 747
---

Have you ever heard a software engineer refer to a problem as “NP-complete”? That’s fancy computer science jargon [shorthand for “incredibly hard](http://en.wikipedia.org/wiki/NP-complete)”:


> The most notable characteristic of NP-complete problems is that no fast solution to them is known; that is, the time required to solve the problem using any currently known algorithm increases very quickly as the size of the problem grows. As a result, **the time required to solve even moderately large versions of many of these problems easily reaches into the billions or trillions of years**, using any amount of computing power available today. As a consequence, determining whether or not it is possible to solve these problems quickly is one of the principal unsolved problems in Computer Science today.
> While a method for computing the solutions to NP-complete problems using a reasonable amount of time remains undiscovered, computer scientists and programmers still frequently encounter NP-complete problems. An expert programmer should be able to recognize an NP-complete problem so that he or she does not unknowingly waste time trying to solve a problem which so far has eluded generations of computer scientists.


You do want to be an *expert* programmer, don’t you? Of course you do!


NP-complete problems are like hardcore pornography. Nobody can define what makes a problem NP-complete, exactly, but [you’ll know it when you see it](http://en.wikipedia.org/wiki/I_know_it_when_I_see_it). Just this once, I’ll refrain from my usual practice of inserting images to illustrate my point.

kg-card-begin: html

(Update: I was shooting for a poetic allusion to the [P=NP problem](http://en.wikipedia.org/wiki/Complexity_classes_P_and_NP) here but based on the comments this is confusing and arguably incorrect. So I’ll redact this sentence. Instead, I point you to [this P=NP poll](http://www.cs.umd.edu/~gasarch/papers/poll.pdf) (pdf); read the comments from CS professors (including Knuth) to get an idea of how realistic this might be.)

kg-card-end: html

Instead, I’ll recommend a book Anthony Scian recommended to me: [Computers and Intractability](http://www.amazon.com/dp/0716710455): A Guide to the Theory of NP-Completeness.


![](https://blog.codinghorror.com/content/images/2025/04/image-229.png)


Like all the software engineering books I recommend, this book has a timeless quality. It was originally published in 1979, a shining testament to smart people attacking truly difficult problems in computer science: [“I can’t find an efficient algorithm, but neither can all these famous people.”](https://web.archive.org/web/20081204152351/http://max.cs.kzoo.edu/~kschultz/CS510/ClassPresentations/NPCartoons.html)


So how many problems are NP-complete? [Lots](http://en.wikipedia.org/wiki/List_of_NP-complete_problems).


Even if you’re a layman, you might have experienced NP-Completeness [in the form of Minesweeper](https://blog.codinghorror.com/programming-games-analyzing-games/), as [Ian Stewart explains](http://www.claymath.org/Popular_Lectures/Minesweeper/). But for programmers, I’d argue the most well known NP-completeness problem is the [travelling salesman problem](http://en.wikipedia.org/wiki/Travelling_salesman_problem).


> Given a number of cities and the costs of travelling from any city to any other city, what is the least-cost round-trip route that visits each city exactly once and then returns to the starting city?


The [brute-force solution](https://blog.codinghorror.com/hardware-assisted-brute-force-attacks-still-for-dummies/) – trying every possible permutation between the cities – might work for a very small network of cities, but this quickly becomes untenable. Even if we were to use theoretical CPUs our children might own, or our children’s children. What’s worse, every other algorithm we come up with to find an optimal path for the salesman has the same problem. That’s the common characteristic of NP-complete problems: they are **exercises in heuristics and approximation**, as illustrated by [this xkcd cartoon](http://xkcd.com/399/):


![](https://blog.codinghorror.com/content/images/2025/04/image-228.png)


What do *expert* programmers do when faced by an intractable problem? **They cheat**. And so should you! Indeed, some of the modern approximations for the Travelling Salesman Problem are *remarkably* effective.


> Various approximation algorithms, which quickly yield good solutions with high probability, have been devised. Modern methods can find solutions for extremely large problems (millions of cities) within a reasonable time, with a high probability of being just 2-3% away from the optimal solution.


Unfortunately, not all NP-complete problems have good approximations. But for those that do, I have to wonder: if we can get so close to an optimal solution by cheating, does it really matter if there’s no known algorithm to produce *the *optimal solution? If I’ve learned nothing else from NP-complete problems, I’ve learned this: **sometimes coming up with clever cheats can be more interesting than searching in vain for the perfect solution**.


Consider the [First Fit Decreasing](http://en.wikipedia.org/wiki/Bin_packing_problem#Analysis_of_heuristic_algorithms) algorithm for the NP-complete [Bin Packing problem](http://www.ams.org/featurecolumn/archive/bins1.html). It’s not perfect, but it’s incredibly simple and fast. The algorithm is so simple, in fact, it is regularly demonstrated at [time management seminars](https://web.archive.org/web/20090101060010/http://www.synergyinstituteonline.com/detail_article.php?artid=319). Oh, *and* it guarantees that you will get within 22% of the perfect solution every time. Not bad for a lousy cheat.


So what’s *your* favorite NP-complete cheat?

[computer science](https://blog.codinghorror.com/tag/computer-science/)
[np-complete problems](https://blog.codinghorror.com/tag/np-complete-problems/)
[algorithms](https://blog.codinghorror.com/tag/algorithms/)
[computational complexity](https://blog.codinghorror.com/tag/computational-complexity/)
