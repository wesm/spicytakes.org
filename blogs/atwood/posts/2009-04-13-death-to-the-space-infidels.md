---
title: "Death to the Space Infidels!"
date: 2009-04-13
url: https://blog.codinghorror.com/death-to-the-space-infidels/
slug: death-to-the-space-infidels
word_count: 1171
---

Ah, spring. What a wonderful time of year. A time when young programmers’ minds turn to thoughts of... ***never ending last-man-standing filibuster arguments about code formatting***.


Naturally.


And there is no argument more evergreen than the timeless [debate between tabs and spaces](http://www.jwz.org/doc/tabs-vs-spaces.html).


> On defaultly-configured Unix systems, and on ancient dumb terminals and teletypes, the tradition has been for the TAB character to mean *move to the right until the current column is a multiple of 8.* This is also the default in the two most popular Unix editors, Emacs and vi.
> In many Windows and Mac editors, the default interpretation is the same, except that multiples of 4 are used instead of multiples of 8.
> A third interpretation is for the ASCII TAB character to mean *indent to the next tab stop*, where the tab stops are set arbitrarily: they might not necessarily be equally distanced from each other. Most word processors can do this; Emacs can do this. I don’t think vi can do this, but I’m not sure.
> With these three interpretations, the ASCII TAB character is essentially being used as a compression mechanism, to make sequences of SPACE-characters take up less room in the file.


So, then, the question: should code* be indented with **spaces**...


![](https://blog.codinghorror.com/content/images/2025/04/image-350.png)


or with **tabs**?


![](https://blog.codinghorror.com/content/images/2025/04/image-349.png)


According to Cyrus, there’s [a third option](https://web.archive.org/web/20090604142339/http://blogs.msdn.com/cyrusn/archive/2004/09/14/229474.aspx): an unholy melding of **both tabs *and *spaces. **Apparently you can use tab for primary indentation alignment and then spaces on top of that for detail alignment. Like so:


![](https://blog.codinghorror.com/content/images/2025/04/image-348.png)


This way, in theory at least, the level of indent can be adjusted dynamically without destroying alignment. But I’m more inclined to think of it as combining all the complexity and pitfalls of both approaches, myself.


OK, so maybe you’re an enlightened coder. You’ve moved beyond mere earthbound issues like tabs vs. spaces on your personal path to code nirvana. Perhaps you have some kind of fancy auto-formatter that runs on every check in. Or, maybe you’re using a next-*next*-generation editor that treats code as “data” and the layout (including whitespace) as a “view,” making all these concerns largely irrelevant.


But there’s a deeper issue here to consider. **The only programming project with no disagreement whatsoever on code formatting is the one you work on alone**. Wherever there are two programmers working on the same project, there are invariably disagreements about how the code should be formatted. Sometimes serious disagreements. The more programmers you add, the more divisive those disagreements get. And handling those disagreements can be... tricky. Take this email I received from Philip Leitch:


> The place where I work currently has a developer (who is also the head of the development department), who will “clean up” the code of others.
> That is – reformat it, normally without changing what the code does, just changing the variable names, function names, but mainly moving things around to the way they like it.
> It is a little perplexing – and I’m interested to see what responses people have on this issue.


One of absolute worst, *worst* methods of [teamicide](https://blog.codinghorror.com/are-you-creating-micromanagement-zombies/) for software developers is to engage in these kinds of passive-aggressive formatting wars. I know because I’ve been there. They destroy peer relationships, and depending on the type of formatting, can also damage your ability to effectively compare revisions in source control, which is *really* scary. I can’t even imagine how bad it would get if the lead was guilty of this behavior. That’s leading by example, all right. *Bad* example.


The depressing thing about all this is that **code formatting matters more than you think**. Perhaps even enough to justify the endless religious wars that are fought over it. Consider the 1984 study by Soloway and Ehrlich cited in [Code Complete](http://www.amazon.com/dp/0735619670):


> Our studies support the claim that knowledge of programming plans and rules of programming discourse can have a significant impact on program comprehension. In their book called [The Elements of Programming Style](http://www.amazon.com/dp/0070342075), Kernighan and Plauger also identify what we would call discourse rules. Our empirical results put teeth into these rules: **It is not merely a matter of aesthetics that programs should be written in a particular style**. Rather there is a psychological basis for writing programs in a conventional manner: programmers have strong expectations that other programmers will follow these discourse rules. If the rules are violated, then the utility afforded by the expectations that programmers have built up over time is effectively nullified. The results from the experiments with novice and advanced student programmers and with professional programmers described in this paper provide clear support for these claims.


There’s actual data from honest-to-goodness experiments to support the hypothesis that consistent code formatting is *worth fighting for*. And there are dozens of studies backing it up, too, as Steve McConnell notes:


> In their classic paper [Perception in Chess](https://web.archive.org/web/20090419113310/http://www.sil.org/lingualinks/Literacy/ReferenceMaterials/BibliographyLiteracy/ChaseAndSimon1973.htm), Chase and Simon reported on a study that compared the abilities of experts and novices to remember the positions of pieces in chess. When pieces were arranged on the board as they might be during a game, the experts’ memories were far superior to the novices’. When the pieces were arranged randomly, there was little difference between the memories of the experts and the novices. The traditional interpretation of this result is that an expert’s memory is not inherently better than a novice’s but that the expert has a knowledge structure that helps him or her remember particular kinds of information. When new information corresponds to the knowledge structure – in this case, the sensible placement of chess pieces – the expert can remember it easily. When new information doesn’t correspond to a knowledge structure – the chess pieces are randomly positioned – the expert can’t remember it any better than the novice.
> A few years later, Ben Shneiderman duplicated Chase and Simon’s results in the computer-programming arena and reported his results in a paper called [Exploratory Experiments in Programmer Behavior](https://web.archive.org/web/20170223163857/http://link.springer.com/article/10.1007%2FBF00975629). Shneiderman found that **when program statements were arranged in a sensible order, experts were able to remember them better than novices. When statements were shuffled, the experts’ superiority was reduced.** Shneiderman’s results have been confirmed in other studies. The basic concept has also been confirmed in the games Go and bridge and in electronics, music, and physics.


So yes, absurd as it may sound, fighting over whitespace characters and other seemingly trivial issues of code layout is actually justified. Within reason of course – when done openly, in a fair and consensus building way, and without stabbing your teammates in the face along the way.


Choose tabs, choose spaces, choose whatever layout conventions make sense to you and your team. It doesn’t actually matter which coding styles you pick. What *does* matter is that you, and everyone else on your team, **sticks with those conventions and uses them consistently**.


That said, only a moron would use tabs to format their code.


*Unless you happen to be programming in [whitespace](https://web.archive.org/web/20090916185453/http://compsoc.dur.ac.uk/whitespace/) or [Python](http://www.python.org/).

[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
[coding standards](https://blog.codinghorror.com/tag/coding-standards/)
[text editors](https://blog.codinghorror.com/tag/text-editors/)
[indentation](https://blog.codinghorror.com/tag/indentation/)
