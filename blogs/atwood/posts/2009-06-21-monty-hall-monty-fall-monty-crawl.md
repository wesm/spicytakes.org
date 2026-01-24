---
title: "Monty Hall, Monty Fall, Monty Crawl"
date: 2009-06-21
url: https://blog.codinghorror.com/monty-hall-monty-fall-monty-crawl/
slug: monty-hall-monty-fall-monty-crawl
word_count: 946
---

Remember [The Problem of the Unfinished Game](https://blog.codinghorror.com/the-problem-of-the-unfinished-game/)? And the almost 2,500 comments those two posts generated? I know, I like to pretend it didn’t happen, either. Some [objected to the way](http://paulbuchheit.blogspot.com/2009/01/question-is-wrong.html) I asked the question, but it was a simple question asked in simple language. I think what they’re *really* objecting to is **how unintuitive the answer is**.


Which reminds me of another question that you’ve probably heard of:

kg-card-begin: html

> Suppose the contestants on a game show are given the choice of three doors: behind one door is a car; behind the others, goats. After a contestant picks a door, the host, who knows what’s behind all the doors, opens one of the unchosen doors, which reveals a goat. He then asks the contestant, “Do you want to switch doors?”
> **Should the contestant switch doors?**

kg-card-end: html

This is, of course, [the Monty Hall problem](http://en.wikipedia.org/wiki/Monty_Hall_problem). It’s been covered to death, and quite well I might add, by dozens of writers who are [far](https://web.archive.org/web/20090803041359/http://www.codingthewheel.com/archives/21-and-the-monty-hall-paradox) [more](http://dilbertblog.typepad.com/the_dilbert_blog/2008/04/monte-hall-prob.html) [talented](https://web.archive.org/web/20090714025945/http://www.letsmakeadeal.com/problem.htm) than I.


What’s interesting about this problem, to me at least, is not the solution, but the vehemence with which people react to the solution – as described in [The Drunkard’s Walk](http://www.amazon.com/dp/0375424040): How Randomness Rules Our Lives.


![](https://blog.codinghorror.com/content/images/2025/04/image-388.png)


> It appears to be a pretty silly question. Two doors are available – open one and you win; open the other and you lose – so it seems self-evident that whether you change your choice or not, your chances of winning are 50/50. What could be simpler? The thing is, Marilyn [said in her column](https://web.archive.org/web/20090803041358/http://www.marilynvossavant.com/articles/gameshow.html) that it is better to switch.
> Despite the public’s much-heralded lethargy when it comes to mathematical issues, Marilyn’s readers reacted as if she’d advocated ceding California back to Mexico. Her denial of the obvious brought her an avalanche of mail, 10,000 letters by her estimate. If you ask the American people whether they agree that plants create the oxygen in the air, light travels faster than sound, or you cannot make radioactive milk by boiling it, you will get double-digit disagreement in each case (13 percent, 24 percent, and 35 percent, respectively). But on this issue, **Americans were united: Ninety-two percent agreed Marilyn was wrong.**


Perhaps the public can be forgiven their ignorance, but what of the experts? Surprisingly, the mathematicians fare little better.


> Almost 1,000 Ph.D.s wrote in, many of them math professors, who seemed especially irate. “You blew it,” wrote a mathematician from George Mason University. From Dickinson State University came this: “I am in shock that after being corrected by at least three mathematicians, you still do not see your mistake.” From Georgetown: “How many irate mathematicians are needed to change your mind?” And someone from the U.S. Army Research Institute remarked, “If all those Ph.D.s are wrong the country would be in serious trouble.” Responses continued in such great numbers and for such a long time that after devoting quite a bit of column space to the issue, Marilyn decided she would no longer address it.
> The army PhD who wrote in may have been correct that if all those PhDs were wrong, it would be a sign of trouble. But Marilyn *was* correct. When told of this, [Paul Erdos](http://en.wikipedia.org/wiki/Paul_Erdos), one of the leading mathematicians of the 20th century, said, “That’s impossible.” Then, when presented with a formal mathematical proof of the correct answer, he still didn’t believe it and grew angry. Only after a colleague arranged for a computer simulation in which Erdos watched hundreds of trials that came out 2-to-1 in favor of switching did Erdos concede that he was wrong.


You may recognize Paul Erdos from a [particularly obscure XKCD cartoon](http://xkcd.com/599/) last week. So if *you* feel like an idiot because you couldn’t figure out the Monty Hall problem, take heart. **The problem is so unintuitive one of the most notable mathematicians of the last century couldn’t wrap his head around it.** That’s... well, that’s *amazing*.


How can something that seems so obvious be so wrong? Apparently our brains are not wired to do these sorts of probability problems very well. Personally, I found the text of Jeffrey Rosenthal’s [Monty Hall, Monty Fall, Monty Crawl](http://www.probability.ca/jeff/writing/montyfall.pdf) (pdf) to be the most illuminating, because it asks us to consider some related possibilities, and how they might affect the outcome:


> **Monty Fall Problem**: In this variant, once you have selected one of the three doors, the host slips on a banana peel and accidentally pushes open another door, which just happens not to contain the car. Now what are the probabilities that you will win, either by sticking with your original door, or switching doors?
> **Monty Crawl Problem**: Once you have selected one of the three doors, the host then reveals one non-selected door which does not contain the car. However, the host is very tired, and crawls from his position (near Door #1) to the door he is to open. In particular, if he has a choice of doors to open, then he opens the smallest number available door. (For example, if you selected Door #1 and the car was indeed behind Door #1, then the host would always open Door #2, never Door #3.) Now what are the probabilities that you will win the car if you stick versus if you switch?


Paul Erdos was brilliant, but even he realized his own limits when presented with the highly unintuitive Monty Hall problem. For his epitaph, he suggested, in his native Hungarian, “Végre nem butulok tovább.” This translates into English as “I’ve finally stopped getting dumber.”


If only the rest of us could be so lucky.

[mathematics](https://blog.codinghorror.com/tag/mathematics/)
[probability](https://blog.codinghorror.com/tag/probability/)
[game theory](https://blog.codinghorror.com/tag/game-theory/)
[monty hall problem](https://blog.codinghorror.com/tag/monty-hall-problem/)
[decision-making](https://blog.codinghorror.com/tag/decision-making/)
