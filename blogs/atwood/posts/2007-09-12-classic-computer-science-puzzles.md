---
title: "Classic Computer Science Puzzles"
date: 2007-09-12
url: https://blog.codinghorror.com/classic-computer-science-puzzles/
slug: classic-computer-science-puzzles
word_count: 619
---

Software developers do have a proclivity for puzzles. Perhaps that’s why books like [To Mock a Mockingbird](http://www.amazon.com/exec/obidos/ASIN/0394534913/) exist. It’s a collection of logic puzzles which is considered an introduction to lambda calculus, one of the core concepts of [Lisp](http://en.wikipedia.org/wiki/Lisp_programming_language).


![](https://blog.codinghorror.com/content/images/2025/03/image-74.png)


Such puzzle questions are [*de rigueur* for many programming interviews](https://blog.codinghorror.com/the-monopoly-interview/), though they’re often abused. There is a downside to thinking of programming languages as solutions to arbitrarily difficult abstract mathematical puzzles. That’s probably why Lisp has a rich reputation for being [powerful but simultaneously dense](https://web.archive.org/web/20071011114940/http://damienkatz.net/2007/01/the_volkswagen.html) and impenetrable.


I prefer to think of programming languages as utilitarian tools for **real world problems**. They let me accomplish pragmatic (and often prosaic) goals. PHP is about as unsexy a language as you’ll ever find, but does that matter when it’s the technology driving the current Boardwalk and Park Place of the web world? I’m not a fan of puzzle questions in interviews; I’d rather have potential developers [give me a presentation](https://blog.codinghorror.com/on-interviewing-programmers/) or [write a reasonably useful program](https://blog.codinghorror.com/why-cant-programmers-program/) in the real development environment they’ll be using on the job. Solve all the puzzles you want, but the only one we’re getting *paid *to solve is the customer’s problem.


That said, **many fundamental computer science concepts can be summarized well in puzzle form**, which aids tremendously in teaching and learning these key concepts. Here’s a quick list of the **classic computer science puzzles** that I remember from my university days:

kg-card-begin: html


| [Dining Philosophers](http://en.wikipedia.org/wiki/Dining_philosophers_problem)
Concurrency and Deadlocks | Five philosophers sit around a circular table. In front of each philosopher is a large plate of rice. The philosophers alternate their time between eating and thinking. There is one chopstick between each philosopher, to their immediate right and left. In order to eat, a given philosopher needs to use both chopsticks. How can you ensure all the philosophers can eat reliably without starving to death? |
| [Travelling Salesman](http://en.wikipedia.org/wiki/Travelling_salesman_problem)
P=NP | A salesperson has a route of cities that make up his or her beat. What’s the most efficient sales route that visits each city exactly once, and then returns to the home city? |
| [Eight Queens](http://en.wikipedia.org/wiki/Eight_queens_puzzle)
Algorithm Design | Given eight queens on a standard 8 x 8 chessboard, how many unique positions – exclusive of rotations and mirror images – can those eight queens occupy without attacking each other? |
| [Two Generals](http://en.wikipedia.org/wiki/Two_Generals%27_Problem)
Communication Protocols | Two armies, each led by a general, are preparing to attack a city. The armies are encamped outside the city on two mountains separated by a large valley. In order to capture the city, the generals must attack at exactly the same time. The only way for the generals to communicate is by sending messengers through the valley. Unfortunately, the valley is occupied by the city’s defenders, so there’s a chance any given messenger will be captured. Each general has no way of knowing if their messenger arrived. How do the generals coordinate their attack? |
| [Towers of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi)
Recursion | You have a stack of discs, from largest to smallest, that slide on to the first peg of a three peg board. Your goal is to move the entire stack of discs from the first peg to the third peg. However, you can only move the topmost disc of any peg, and smaller discs must always be placed on larger discs. How many moves will it take? |


kg-card-end: html

I consider this the “greatest hits” of classic computer science puzzles. But I’m sure I’ve forgotten a few. Are there any other puzzles I’ve missed that express fundamental computer science concepts, the type that would be taught in a typical undergraduate computer science course?

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[lambda calculus](https://blog.codinghorror.com/tag/lambda-calculus/)
[lisp](https://blog.codinghorror.com/tag/lisp/)
[puzzles](https://blog.codinghorror.com/tag/puzzles/)
