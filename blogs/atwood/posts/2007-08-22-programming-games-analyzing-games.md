---
title: "Programming Games, Analyzing Games"
date: 2007-08-22
url: https://blog.codinghorror.com/programming-games-analyzing-games/
slug: programming-games-analyzing-games
word_count: 810
---

For many programmers, **our introduction to programming was our dad forcing us to write our own games**. Instead of the shiny new Atari 2600 game console I wanted, I got a Texas Instruments TI-99/4a computer instead. That’s not exactly what I had in mind at the time, of course, but that fateful decision launched a career that spans thirty years.


Evidently, I’m not alone. Mike Lee [had a similar experience](https://web.archive.org/web/20071011215406/http://atomicwang.org/motherfucker/Index/A9267832-5BD9-475F-98E6-A8C269E91C4B.html):


> I was born in 1976, the same year as Apple, so my dad was just the right age to get into the early results of the home-brew movement. One of my few memories of early childhood is of him coming home with a Sinclair 2000 and a book of games. He sat there for hours typing in the code for Space Invaders, and we played it maybe 30 minutes before turning the machine off and undoing all his work.


As [did Shawn Oster](https://web.archive.org/web/20070919202822/http://a-simian-mind.blogspot.com/2007/05/what-i-learned.html):


> I’ve been developing software for 25 years, since I was 8, starting with a book called “Your First BASIC Program” that my dad bought me because we had a PC while all my friends were playing StarBlazers on their Apple IIs. He said if I wanted to play games then I could write one myself. At the time I was a bit disappointed (OK, crushed) but now... well, Dad, thank you.


That’s why it’s so fascinating to retrace the earliest computer games. The personal computer industry [grew up with us](https://blog.codinghorror.com/growing-up-with-the-microcomputer/). We learned how to program by [typing in those simple games](https://blog.codinghorror.com/the-best-of-creative-computing/) from magazines and books. Look closely, and you’ll find that those old game programs are the primitive origins of most programmers, the reptile brain stem we all collectively carry around in our heads.


Even a humble, simple little pack-in game like Minesweeper has deep roots going back to the days of punch cards:

kg-card-begin: html

> Minesweeper has its origins in the earliest mainframe games of the ’60s and ’70s. Wikipedia cites the earliest ancestor of Minesweeper as David Ahl’s [Cube](http://www.atariarchives.org/basicgames/showpage.php?page=53). But although Cube features “landmines,” it’s hard to consider this a predecessor of Minesweeper. In Cube, the mines are placed randomly and the only way to discover where they ends the game. You walk over a landmine and you die; you can’t avoid the landmines or know where they are before you take a chance.
> However, there are a number of very early “hide and seek” games about locating hidden spots on a grid. For example, in Bob Albrecht’s [Hurkle](http://www.atariarchives.org/basicgames/showpage.php?page=94), you have to find a creature hiding on a ten-by-ten grid. After each guess, you’re told in what general direction the Hurkle lies. Dana Noftle’s [Depth Charge](http://www.atariarchives.org/bcc1/showpage.php?page=251) is the same, but in three dimensions. Bud Valenti’s [Mugwump](http://www.atariarchives.org/basicgames/showpage.php?page=114) has multiple hidden targets, and after each guess, you get the approximate distance to each of them. Unlike Cube, these games match the general pattern of Minesweeper more closely: make a random guess to start, then start using the information provided by that first guess to uncover the hidden items. Of course, unlike Minesweeper (or Cube), the was no danger of “explosion,” the only constraint was finding the secret locations in a limited number of guesses.
> The closest ancestor to Minesweeper is probably Gregory Yob’s [Hunt the Wumpus](http://www.atariarchives.org/bcc1/showpage.php?page=247).
> Although it used an unorthodox grid (the original game used the vertices of a dodecahedron, and [a later version](http://www.atariarchives.org/morebasicgames/showpage.php?page=181) used Mbius strips and other unlikely patterns), the Wumpus evolved from its predecessors in many other ways.

kg-card-end: html

I was intrigued by the newfound connection between Minesweeper and [Hunt the Wumpus](https://web.archive.org/web/20070908205416/http://www.codinghorror.com/blog/files/wumpus_origin.htm), since the [Wumpus is my power animal](https://blog.codinghorror.com/your-personal-brand/).


Most of the early games weren’t even that much *fun*. Analyzing the game’s program was almost as enjoyable as playing it; the very act of typing it in and understanding the program was “game” enough for many of us. But some of these early games evolved and survived until today, as Minesweeper did – and it has become so ingrained into the public consciousness that it’s now the subject of hilarious parody videos. Despite Minesweeper’s simplicity (and popularity), it is also a surprisingly deep game of logic, as documented in the [Wikipedia entry](http://en.wikipedia.org/wiki/Minesweeper_(computer_game)):

- Analysis: single square, double square, shared mine
- NP-Completeness
- Mine probabilities
- Measuring Board Difficulty


Minesweeper is still popular with programmers today; [Automine](https://web.archive.org/web/20060831232221/http://students.washington.edu/ahou/automine/index.html), for example, is a Java program that automatically plays Minesweeper by reading the screen and manipulating the mouse.


The Minesweeper article is a part of the amazing [Beyond Tetris series](https://web.archive.org/web/20071010122319/http://www.gamesetwatch.com/column_beyond_tetris/) on GameSetWatch, in which many classic puzzle games are examined from the vantage point of a game designer and game programmer. I recommend it highly. Fair warning, though: don’t click through unless you have plenty of time on your hands. For a programmer, **analyzing games is almost as fun as playing them**.

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[game development](https://blog.codinghorror.com/tag/game-development/)
