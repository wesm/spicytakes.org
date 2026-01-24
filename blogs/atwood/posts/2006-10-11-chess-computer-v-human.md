---
title: "Chess: Computer v. Human"
date: 2006-10-11
url: https://blog.codinghorror.com/chess-computer-v-human/
slug: chess-computer-v-human
word_count: 1302
---

I recently visited the [Computer History Museum](http://www.computerhistory.org/) in nearby San Jose, which has a new exhibit on the history of computer chess. Despite my total lack of interest in chess as a game, [computer chess](http://en.wikipedia.org/wiki/Computer_chess) has a special significance in the field of computer science. **Chess remains the most visible and public benchmark of the relentless increase in computer speed over the last 50 years.**


![](https://blog.codinghorror.com/content/images/2025/05/image-383.png)


There are two general strategies available to computer chess programs:

1. **Brute force search** or Type A. All possible positions are examined.
2. **Strategic AI** or Type B. Only good positions are examined.


As it turns out, computers have a hard time with the concept of “good.” That’s why the history of computer chess is dominated by Type A programs. The most famous Type A chess computer is probably IBM’s Deep Blue, which went through a number of incarnations before it defeated a reigning world chess champion in 1997.


I recently [built myself a new PC](https://blog.codinghorror.com/building-and-overclocking-a-core-2-duo-system/) based on the latest Intel Core 2 Duo chip. According to the [Fritz Chess Benchmark](https://web.archive.org/web/20100120110918/http://www.chess.com/download/view/fritz-12-benchmark), my current home PC is capable of evaluating approximately **4.45 million chess positions per second**. The figure is actually expressed as 4452 kilonodes per second (kN/s), a common unit of measurement for chess engines.


4.45 million chess positions per second *sounds* impressive, until you compare that with [the Deep Blue timeline](https://web.archive.org/web/20061025194354/http://www.research.ibm.com/deepblue/meet/html/d.3.1.shtml):

kg-card-begin: html


| Year | Positions/sec |
| 1985 | 50k |
| 1987 | 500k |
| 1988 | 720k |
| 1989 | 2 million |
| 1991 | 7 million |
| 1996 | 100 million |
| 1997 | 200 million |


kg-card-end: html

**The fastest desktop PCs are more than 15 years behind Deep Blue in computer chess**. Of course, Deep Blue was built using large arrays of custom hardware designed for the sole purpose of playing chess, so it’s a little unfair to directly compare it to a general-purpose, commodity CPU.


Chess is an inherently parallelizable problem. The dual and quad-core CPUs on the [Fritz Chess benchmark results page](https://web.archive.org/web/20100912162337/http://www.tomshardware.com:80/charts/desktop-cpu-charts-2010/Logic-Fritz-Chess,2419.html) almost exactly double the results of single-core CPUs of the same speed. You could certainly string together a bunch of these fast commodity desktops and build your way up to Deep Blue numbers. This fascinating ExtremeTech article on [building desktop chess computers](https://web.archive.org/web/20061023104630/http://www.extremetech.com/article2/0,1697,1915528,00.asp) indicates it would take 24 dual, dual-core 2.2 GHz Opteron machines to match Deep Blue. Or at least it would have in January 2006 when that article was written. But something more significant than commodity hardware scaling is going on here – Type B chess programs are finally emerging:


> **Despite its vastly inferior brute force, the Deep Blitz machine could already be a match for Deep Blue because of improvements in chess software.** Deep Fritz is able to evaluate lines of play to a similar depth because it successfully narrows its search only to the strongest lines of play.
> The data suggest that Deep Blue spent a lot of time evaluating bad moves but overcame this weakness through brute force. In a match between Deep Blue and the Deep Blitz machine running Deep Fritz or Deep Shredder, it seems unclear which machine would win. Obviously, Kasparov did not evaluate 200 million chess positions per second when he defeated Deep Blue in game 1 of the 1997 match, thus the 200 million positions per second number is not a requirement to play chess at the word championship level. It seems likely that Deep Fritz, which is more efficient at filtering out weak moves, is a far more ’intelligent’ chess program compared with Deep Blue’s software.


The latest [computer chess ratings](http://computerchess.org.uk/ccrl/) are determined solely by computer vs. computer play. Bram Cohen thinks the derived ratings from computer play are enough to crown the computer chess programs [champs over human grandmasters, too](http://bramcohen.livejournal.com/29624.html):


> What’s the best tournament chess game of all time? If by ‘best’ one means ‘best played’ then I'm afraid the answer is Zappa vs. Fruit. In this most recent world computer tournament, Zappa scored an astounding 10.5 out of 11, a better performance than any human has ever had in a human world championship, and against a stronger field than any human world champion has ever faced. Fruit came in a clear second, so this is the only tournament game we have between the two strongest chess players ever created. Of course, you’ll soon be able to buy the commercial version of Zappa and have it play against itself, resulting in a string of games most of which are better than any game ever played between two humans. Welcome to chess in the 21st century.
> Some humorous notes: Zappa and Fruit were both written by lone grad students in under two years. Dark horses obliterating the field is a common thing in AI. Zappa’s lone draw was ironically against the program which lost every other game in the entire tournament.
> Now that **computers are clearly better than humans at chess**, the question arises, can computers attempt to guess the strength of a game’s play based on the moves in that game? And can we use that method to evaluate ‘classic’ games? Do we really want to?


I think this is a dubious claim, particularly since it’s not based on any actual data from computer versus human games. Although Deep Blue did beat Kasparov in 1997, there’s ample evidence that Kasparov was the better player and he psyched himself out during the match. [All subsequent rematches](http://www.chessbase.com/newsdetail.asp?newsid=1229) between human world champions and computer chess programs have resulted in ties – including two with Kasparov himself in 2003. Statistician Jeff Sonas believes [computers will never consistently defeat](http://www.chessbase.com/newsdetail.asp?newsid=1244) the best human players:


> Computers are becoming more and more dominant against everyone but the top 200 players in the world. That is leading to an overall performance rating for computers that is getting higher and higher. However, the players in the top-200 are holding their ground even against the latest and greatest computers. Perhaps that group will soon shrink down to only the top-100, or the top-50, but not inevitably, and not irreversibly. As you can see from my previous graphics, there is no sign that the top-200 players are losing ground at all against the top computers.
> The top 20 humans (the 2700+ crowd) are managing a long string of drawn matches against computers, and the rest of the top-200 is averaging the same 35% to 40% score that they did a few years ago. So, amazing as it may seem, I don’t see any evidence that the top computers are suddenly going to take over the chess world. Of course the top computers are improving, mostly through hardware and software upgrades, but somehow the top humans are improving just as fast, in other ways.
> We are at a unique point in chess history, an unprecedented state of dynamic balance. **The top computers have caught up with the top grandmasters, and right now I’m not convinced that the computers will zoom past the grandmasters.** Everything depends on whether computers or grandmasters can improve faster, starting today. It may even be that the top humans can figure out how to improve their own anti-computer play, to the point that they will pull ahead again. Perhaps Garry Kasparov can lead the way once more.


I tend to agree. We may have reached an inflection point. The problem space of chess is so astonishingly large that incremental increases in hardware speed and algorithms are unlikely to result in meaningful gains from here on out.


Computer chess programs may have long ago crushed the rest of us in their inevitable Moore’s Law march, but the best 200 chess players in the world are still holding their ground.

[computer chess](https://blog.codinghorror.com/tag/computer-chess/)
[programming strategies](https://blog.codinghorror.com/tag/programming-strategies/)
[history of computer chess](https://blog.codinghorror.com/tag/history-of-computer-chess/)
[artificial intelligence](https://blog.codinghorror.com/tag/artificial-intelligence/)
[benchmarking](https://blog.codinghorror.com/tag/benchmarking/)
