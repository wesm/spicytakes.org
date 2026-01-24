---
title: "Thanks For Ruining Another Game Forever, Computers"
date: 2016-03-25
url: https://blog.codinghorror.com/thanks-for-ruining-another-game-forever-computers/
slug: thanks-for-ruining-another-game-forever-computers
word_count: 1905
---

In 2006, after visiting the Computer History Museum’s exhibit on Chess, [I opined](https://blog.codinghorror.com/chess-computer-v-human/):


> We may have reached an inflection point. The problem space of chess is so astonishingly large that incremental increases in hardware speed and algorithms are unlikely to result in meaningful gains from here on out.


So. About that. Turns out I was kinda… *totally completely wrong*. The number of possible moves, or “problem space,” of Chess is indeed astonishingly large, estimated to be 1050:


> 100,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000


[Deep Blue](https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)) was interesting because it forecast a particular kind of future, a future where **specialized hardware enabled brute force attack of the enormous chess problem space**, as its purpose built chess hardware outperformed general purpose CPUs of the day by *many* orders of magnitude. How many orders of magnitude? In the heady days of 1997, Deep Blue could evaluate **200 million chess positions per second**. And that was enough to defeat Kasparov, the [highest ever ranked human player](https://en.wikipedia.org/wiki/Comparison_of_top_chess_players_throughout_history) – until 2014 at least. Even though one of its best moves was [the result of a bug](http://www.wired.com/2012/09/deep-blue-computer-bug/).


> 200,000,000


In 2006, about ten years later, according to the Fritz Chess benchmark, my PC could evaluate only 4.5 million chess positions per second.


> 4,500,000


Today, about twenty years later, that very same benchmark says my PC can evaluate a mere 17.2 million chess positions per second.


> 17,200,000


Ten years, four times faster. Not bad! Part of that is I went from dual to quad core, and these chess calculations scale almost linearly with the number of cores. An eight core CPU, no longer particularly exotic, could probably achieve ~28 million on this benchmark today.


> 28,000,000


I am not sure the scaling is exactly linear, but it’s fair to say that even now, *twenty years later*, a modern 8 core CPU is still about an order of magnitude slower at the brute force task of evaluating chess positions than what Deep Blue’s specialized chess hardware achieved in 1997.


But here’s the thing: none of that speedy brute forcing matters today. Greatly improved chess programs running on mere *handheld devices* can perform [beyond grandmaster level](https://en.wikipedia.org/wiki/Human%E2%80%93computer_chess_matches#Pocket_Fritz_4_.282009.29).


> In 2009 a chess engine running on slower hardware, a 528 MHz HTC Touch HD mobile phone running Pocket Fritz 4 reached the grandmaster level – it won a category 6 tournament with a performance rating of 2898. **Pocket Fritz 4 searches fewer than 20,000 positions per second. This is in contrast to supercomputers such as Deep Blue that searched 200 million positions per second.**


As far as chess goes, despite what I so optimistically thought in 2006, it’s been *game over* for humans for quite a few years now. The best computer chess programs, vastly more efficient than Deep Blue, combined with modern CPUs which are now finally within an order of magnitude of what Deep Blue’s specialized chess hardware could deliver, play at levels way beyond what humans can achieve.


**Chess: ruined forever.** Thanks, computers. You jerks.


Despite this resounding defeat, there was still hope for humans in the game of Go. The number of possible moves, or “problem space,” of Go is estimated to be 10170:


> 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000


Remember that Chess had a mere *fifty* zeroes there? Go has [more possible moves](https://en.wikipedia.org/wiki/Go_and_mathematics) than there are **atoms in the universe.**


Wrap your face around that one.


![](https://blog.codinghorror.com/content/images/2016/03/go-game.jpg)


Deep Blue was a statement about the inevitability of *eventually* being able to brute force your way around a difficult problem with the constant wind of [Moore’s Law](https://blog.codinghorror.com/moores-law-in-practical-terms/) at your back. If Chess is the quintessential European game, Go is the quintessential Asian game. Go requires a completely different strategy. Go means wrestling with a problem that is essentially impossible for computers to solve in any traditional way.


> A simple material evaluation for chess works well – each type of piece is given a value, and each player receives a score depending on his/her remaining pieces. The player with the higher score is deemed to be ‘winning’ at that stage of the game.
> However, Chess programmers innocently asking Go players for an evaluation function would be met with disbelief! No such simple evaluation exists. Since there is only a single type of piece, only the number each player has on the board could be used for a simple material heuristic, and there is almost no discernible correlation between the number of stones on the board and what the end result of the game will be.


Analysis of a problem this hard, with brute force completely off the table, is colloquially called “AI,” though that term is a bit of a stretch to me. I prefer to think of it as building systems that can learn from experience, aka [machine learning](https://en.wikipedia.org/wiki/Machine_learning). Here’s a talk which covers DeepMind learning to play classic Atari 2600 videogames. (Jump to the 10 minute mark to see what I mean.)


As impressive as this is – and it truly is – bear in mind that games as simple as Pac-Man still remain far beyond the grasp of Deep Mind. But what happens when you point a system like that at the game of Go?


DeepMind built a system, [AlphaGo](https://en.wikipedia.org/wiki/AlphaGo), designed to see how far they could get with those approaches in the game of Go. AlphaGo recently played one of the best Go players in the world, Lee Sedol, and [defeated him](https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol) in a stunning 4-1 display. Being the optimist that I am, I guessed that DeepMind would win one or two games, but a near total rout like this? Incredible. **In the space of just 20 years, computers went from barely beating the best humans at Chess, with a problem space of 1050, to definitively beating the best humans at Go, with a problem space of 10170.** How did this happen?


Well, a few things happened, but one unsung hero in this transformation is the humble video card, or GPU.


![](https://blog.codinghorror.com/content/images/2016/03/asus-380x-front.jpg)


Consider this breakdown of the [cost of floating point operations](https://en.m.wikipedia.org/wiki/FLOPS#Hardware_costs) over time, measured in **dollars per gigaflop**:

kg-card-begin: html


| 1961 | $8,300,000,000 |  |
| 1984 | $42,780,000 |  |
| 1997 | $42,000 |  |
| 2000 | $1,300 |  |
| 2003 | $100 |  |
| 2007 | $52 |  |
| 2011 | $1.80 |  |
| 2012 | $0.73 |  |
| 2013 | $0.22 |  |
| 2015 | $0.08 |  |


kg-card-end: html

What’s not clear in this table is that after 2007, **all the big advances in FLOPS came from gaming video cards** designed for high speed real time 3D rendering, and as an incredibly beneficial side effect, they also turn out to be crazily [fast at machine learning tasks](https://blogs.nvidia.com/blog/2016/01/12/accelerating-ai-artificial-intelligence-gpus/).


> The Google Brain project had just achieved amazing results — it learned to recognize cats and people by watching movies on YouTube. But it required 2,000 CPUs in servers powered and cooled in one of Google’s giant data centers. Few have computers of this scale. Enter NVIDIA and the GPU. Bryan Catanzaro in NVIDIA Research teamed with Andrew Ng’s team at Stanford to use GPUs for deep learning. As it turned out, 12 NVIDIA GPUs could deliver the deep-learning performance of 2,000 CPUs.


Let’s consider a related case of highly parallel computation. How much faster is a GPU at [password hashing](https://blog.codinghorror.com/speed-hashing/)?

kg-card-begin: html


| Radeon 7970 | 8213.6 M c/s |
| 6-core AMD CPU | 52.9 M c/s |


kg-card-end: html

Only **155 times faster** right out of the gate. No big deal. On top of that, CPU performance has largely stalled in the last decade. While more and more cores are placed on each die, which is great when the problems are parallelizable – as they definitely are in this case – the actual performance improvement of any individual core over the last 5 to 10 years is rather modest.


**But GPUs are still doubling in performance every few years**. Consider password hash cracking expressed in the rate of hashes per second:

kg-card-begin: html


| GTX 295 | 2009 | 25k |
| GTX 690 | 2012 | 54k |
| GTX 780 Ti | 2013 | 100k |
| GTX 980 Ti | 2015 | 240k |


kg-card-end: html

The latter video card is the one in my machine right now. It’s likely the next major revision from Nvidia, due later this year, will [double these rates again](http://wccftech.com/nvidia-pascal-gpu-gtc-2015/).


(While I’m at it, I’d like to emphasize how much it sucks to be an 8 character password in today’s world. **If your password is only 8 characters, that’s perilously close to no password at all.** That’s also why why your [password is  too damn short](https://blog.codinghorror.com/your-password-is-too-damn-short/) (probably). In fact, we just raised the *minimum* allowed password length on [Discourse](http://www.discourse.org/) to 10 characters, because annoying password complexity rules are much less effective in reality than [simply requiring longer passwords](http://arstechnica.com/security/2013/06/password-complexity-rules-more-annoying-less-effective-than-length-ones/).)


Distributed AlphaGo used 1202 CPUs and **176 GPUs**. While that doesn’t sound like much, consider that as we’ve seen, each GPU can be up to 150 times faster at processing these kinds of highly parallel datasets — so those 176 GPUs were the equivalent of adding ~26,400 CPUs to the task. Or more!


Even if you don’t care about video games, they happen to have a profound accidental impact on machine learning improvements. **Every time you see a new video card release, don’t think “slightly nicer looking games” think “wow, hash cracking and AI just got 2× faster… again!”**


I’m certainly not making the same mistake I did when looking at Chess in 2006. (And in my defense, I totally did not see the era of GPUs as essential machine learning aids coming, even though I am a gamer.) If AlphaGo was intimidating today, having soundly beaten the best human Go player in the world, it’ll be no contest after a few more years of GPUs doubling and redoubling their speeds again.


AlphaGo, broadly speaking, is the culmination of two very important trends in computing:

1. Huge increases in parallel processing power driven by consumer GPUs and videogames, which started in 2007. So if you’re a gamer, congratulations! You’re part of the problem-slash-solution.
2. We’re beginning to build sophisticated (and combined) algorithmic approaches for entirely new problem spaces that are far too vast to even begin being solved by brute force methods alone. And these approaches clearly work, insofar as they mastered one of the hardest games in the world, one that many thought humans would never be defeated in.


Great. Another [game ruined forever by computers](http://www.newyorker.com/tech/elements/in-the-age-of-google-deepmind-do-the-young-go-prodigies-of-asia-have-a-future). Jerks.


Based on our experience with Chess, and now Go, we know that computers will continue to beat us at virtually every game we play, in the same way that dolphins will always swim faster than we do. But what if that very same human mind was capable of not only building the dolphin, but continually refining it until they arrived at the [world’s fastest minnow](http://jacquesmattheij.com/another-way-of-looking-at-lee-sedol-vs-alphago)? Where Deep Blue was the more or less inevitable end result of brute force computation, AlphaGo is the beginning of a whole new era of sophisticated problem solving against far more enormous problems. **AlphaGo’s victory is not a defeat of the human mind, but its greatest triumph.**


(If you’d like to learn more about the powerful intersection of sophisticated machine learning algorithms and your GPU, read this excellent summary of AlphaGo and then download the [DeepMind Atari learner](https://github.com/kuz/DeepMind-Atari-Deep-Q-Learner) and try it yourself.)

[deep learning](https://blog.codinghorror.com/tag/deep-learning/)
[artificial intelligence](https://blog.codinghorror.com/tag/artificial-intelligence/)
[chess](https://blog.codinghorror.com/tag/chess/)
[computer history](https://blog.codinghorror.com/tag/computer-history/)
[algorithms](https://blog.codinghorror.com/tag/algorithms/)
