---
title: "Hitting the High Notes"
date: 2005-07-25
url: https://www.joelonsoftware.com/2005/07/25/hitting-the-high-notes/
word_count: 3001
---


In March, 2000, I launched this site with [the shaky claim](https://www.joelonsoftware.com/articles/fog0000000074.html) that most people are wrong in thinking you need an idea to make a successful software company:


> The common belief is that when you’re building a software company, the goal is to find a neat idea that solves some problem which hasn’t been solved before, implement it, and make a fortune. We’ll call this the build-a-better-mousetrap belief. But the real goal for software companies should be converting capital into software that works.


For the last five years I’ve been testing that theory in the real world. The formula for [the company I started](http://www.fogcreek.com/About.html) with Michael Pryor in September, 2000 can be summarized in four steps:



| Best Working Conditions | → | Best Programmers | → | Best Software | → | Profit! |



It’s a pretty convenient formula, especially since our *real *goal in starting Fog Creek was to create a software company where* we would want to work.* I made the claim, in those days, that good working conditions (or, awkwardly, “building the company where the best software developers in the world would want to work”) would *lead* to profits as naturally as chocolate leads to chubbiness or [cartoon sex in video games leads to gangland-style shooting sprees](http://www.gamespot.com/news/2005/07/13/news_6129021.html).


For today, though, I want to answer just one question, because if this part isn’t true, the whole theory falls apart. That question is, does it even make sense to talk about having the “best programmers?” Is there so much variation between programmers that this even matters?


Maybe it’s obvious to us, but to many, the assertion still needs to be proven.


Several years ago a larger company was considering buying out Fog Creek, and I knew it would never work as soon as I heard the CEO of that company say that he didn’t really agree with my theory of hiring the best programmers. He used a biblical metaphor: you only need one King David, and an army of soldiers who merely had to be able to carry out orders. His company’s stock price promptly dropped from 20 to 5, so it’s a good thing we didn’t take the offer, but it’s hard to pin that on the King David fetish.


And in fact the conventional wisdom in the world of copycat business journalists and large companies who rely on overpaid management consultants to think for them, chew their food, etc., seems to be that the most important thing is reducing the *cost* of programmers.


In some other industries, cheap *is* more important than good. Wal*Mart grew to be the biggest corporation on Earth by selling cheap products, not good products. If Wal*Mart tried to sell high quality goods, their costs would go up and their whole cheap advantage would be lost. For example if they tried to sell a tube sock that can withstand the unusual rigors of, say, being washed in a washing machine, they’d have to use all kinds of expensive components, like, say, *cotton, *and the cost for every single sock would go up.


So, why isn’t there room in the software industry for a low cost provider, someone who uses the cheapest programmers available? (Remind me to ask Quark how that whole fire-everybody-and-hire-low-cost-replacements plan is working.)


Here’s why: duplication of software is free. That means that the cost of programmers is spread out over all the copies of the software you sell. With software, you can improve quality without adding to the incremental cost of each unit sold.


Essentially, *design adds value faster than it adds cost*.


Or, roughly speaking, if you try to skimp on programmers, you’ll make crappy software, and you won’t even save that much money.


The same thing applies to the entertainment industry. It’s worth hiring [Brad Pitt](http://images.google.com/images?hl=en&lr=&safe=on&q=brad+pitt&btnG=Search) for your latest blockbuster movie, even though he demands a high salary, because that salary can be divided by all the millions of people who see the movie solely because Brad is so damn *hot*.


Or, to put it another way, it’s worth hiring [Angelina Jolie](http://images.google.com/images?hl=en&lr=&safe=on&q=angelina+jolie&btnG=Search) for your latest blockbuster movie, even though she demands a high salary, because that salary can be divided by all the millions of people who see the movie solely because Angelina is so damn *hot*.


But I still haven’t proven anything. What does it mean to be “the best programmer” and are there really such major variations between the quality of software produced by different programmers?


Let’s start with plain old productivity. It’s rather hard to measure programmer productivity; almost any metric you can come up with (lines of debugged code, function points, number of command-line arguments) is [trivial to game](https://www.joelonsoftware.com/news/20020715.html), and it’s very hard to get concrete data on large projects because it’s very rare for two programmers to be told to do the same thing.


The data* *I rely upon comes from Professor Stanley Eisenstat at Yale. Each year he teaches a programming-intensive course, CS 323, where a large proportion of the work consists of about five programming assignments, each of which takes about two weeks. The assignments are very serious for a college class: implement a Unix command-line shell, implement a ZLW file compressor, etc.


There was so much griping among the students about how much work was required for this class that Professor Eisenstat started asking the students to report back on how much time they spent on each assignment. He has collected this data carefully for several years.


I spent some time crunching the data; it’s the only data sets I know of where we have dozens of students working on identical assignments using the same technology at the same time. It’s pretty darn controlled, as experiments go.


The first thing I did with this data was to calculate the average, minimum, maximum, and standard deviation of hours spent on each of twelve assignments. The results:



| Project | Avg Hrs | Min Hrs | Max Hrs | StDev Hrs |
| CMDLINE99 | 14.84 | 4.67 | 29.25 | 5.82 |
| COMPRESS00 | 33.83 | 11.58 | 77.00 | 14.51 |
| COMPRESS01 | 25.78 | 10.00 | 48.00 | 9.96 |
| COMPRESS99 | 27.47 | 6.67 | 69.50 | 13.62 |
| LEXHIST01 | 17.39 | 5.50 | 39.25 | 7.39 |
| MAKE01 | 22.03 | 8.25 | 51.50 | 8.91 |
| MAKE99 | 22.12 | 6.77 | 52.75 | 10.72 |
| SHELL00 | 22.98 | 10.00 | 38.68 | 7.17 |
| SHELL01 | 17.95 | 6.00 | 45.00 | 7.66 |
| SHELL99 | 20.38 | 4.50 | 41.77 | 7.03 |
| TAR00 | 12.39 | 4.00 | 69.00 | 10.57 |
| TEX00 | 21.22 | 6.00 | 75.00 | 12.11 |
| ALL PROJECTS | 21.44 | 4.00 | 77.00 | 11.16 |



The most obvious thing you notice here is the huge variations. The fastest students were finishing three or four times faster than the average students and as much as ten times faster than the slowest students. The standard deviation is outrageous. So then I thought, hmm, maybe some of these students are doing a terrible job. I didn’t want to include students who spent 4 hours on the assignment without producing a working program. So I narrowed the data down and only included the data from students who were in the top quartile of grades… the top 25% in terms of the quality of the code. I should mention that grades in Professor Eisenstat’s class are *completely *objective: they’re calculated formulaically based on how many automated tests the code passes and nothing else. No points are deducted for bad style or lateness.


Anyway, here are the results for the top quartile:



| Project | Avg Hrs | Min Hrs | Max Hrs | StdDev Hrs |
| CMDLINE99 | 13.89 | 8.68 | 29.25 | 6.55 |
| COMPRESS00 | 37.40 | 23.25 | 77.00 | 16.14 |
| COMPRESS01 | 23.76 | 15.00 | 48.00 | 11.14 |
| COMPRESS99 | 20.95 | 6.67 | 39.17 | 9.70 |
| LEXHIST01 | 14.32 | 7.75 | 22.00 | 4.39 |
| MAKE01 | 22.02 | 14.50 | 36.00 | 6.87 |
| MAKE99 | 22.54 | 8.00 | 50.75 | 14.80 |
| SHELL00 | 23.13 | 18.00 | 30.50 | 4.27 |
| SHELL01 | 16.20 | 6.00 | 34.00 | 8.67 |
| SHELL99 | 20.98 | 13.15 | 32.00 | 5.77 |
| TAR00 | 11.96 | 6.35 | 18.00 | 4.09 |
| TEX00 | 16.58 | 6.92 | 30.50 | 7.32 |
| ALL PROJECTS | 20.49 | 6.00 | 77.00 | 10.93 |



Not much difference! The standard deviation is almost exactly the same for the top quartile. In fact when you look closely at the data it’s pretty clear there’s *no discernable correlation between the time and score.* Here’s a typical scatter plot of one of the assignments… I chose the assignment COMPRESS01, an implementation of Ziv-Lempel-Welch compression assigned to students in 2001, because the standard deviation there is close to the overall standard deviation.


There’s just nothing to see here, and that’s the point. *The quality of the work and the amount of time spent are simply uncorrelated.*


I asked Professor Eisenstat about this, and he pointed out one more thing: because assignments are due at a fixed time (usually midnight) and the penalties for being late are significant, a lot of students stop before the project is done. In other words, the maximum time spent on these assignments is as low as it is partially because there just aren’t enough hours between the time the assignment is handed out and the time it is due. If students had unlimited time to work on the projects (which  would correspond a little better to the working world), the spread could only be *higher*.


This data is not completely scientific. There’s probably some cheating. Some students may overreport the time spent on assignments in hopes of gaining some sympathy and getting easier assignments the next time. (Good luck! The assignments in CS 323 are the same today as they were when I took the class in the 1980s.) Other students may underreport because they lost track of time. Still, I don’t think it’s a stretch to believe this data shows 5:1 or 10:1 productivity differences between programmers.


**But wait, there’s more!**


If the only difference between programmers were productivity, you might think that you could substitute five mediocre programmers for one really good programmer. That obviously doesn’t work. [Brooks’ Law](http://en.wikipedia.org/wiki/Brooks'_law), “StartFragment adding manpower to a late software project makes it later,” is why. A single good programmer working on a single task has no coordination or communication overhead. Five programmers working on the same task must coordinate and communicate. That takes a lot of time. There are added benefits to using the smallest team possible; the [man-month really is mythical](http://www.amazon.com/exec/obidos/tg/detail/-/0201835959/ref=nosim/joelonsoftware).


**But wait, there’s even more!**


The real trouble with using a lot of mediocre programmers instead of a couple of good ones is that no matter how long they work, they never produce something as good as what the great programmers can produce.


Five Antonio Salieris won’t produce Mozart’s Requiem. Ever. Not if they work for 100 years.


Five Jim Davis’s — creator of that unfunny cartoon cat, where 20% of the jokes are about how Monday sucks and the rest are about how much the cat likes lasagna (and those are the *punchlines!*) … five Jim Davis’s could spend the rest of their *lives *writing comedy and never, ever produce the Soup Nazi episode of Seinfeld.


The Creative Zen team could spend years refining their ugly iPod knockoffs and never produce as beautiful, satisfying, and elegant a player as the Apple iPod. And they’re not going to make a dent in Apple’s market share because the magical design talent is just* not there*. They *don’t have it*.


The mediocre talent just *never hits the high notes* that the top talent hits all the time. The number of divas who can hit the f6 in Mozart’s Queen of the Night is vanishingly small, and you just can’t perform The Queen of the Night without that famous f6.


Is software really about artistic high notes? “Maybe some stuff is,” you say, “but I work on accounts receivable user interfaces for the medical waste industry.” [Fair enough.](https://www.joelonsoftware.com/articles/FiveWorlds.html) This is a conversation about *software companies*, shrinkwrap software, where the company’s success or failure is directly a result of the quality of their code.


And we’ve seen plenty of examples of great software, the really high notes, in the past few years: stuff that mediocre software developers just *could not* have developed.


Back in 2003, Nullsoft shipped a new version of Winamp, with the following notice [on their website](http://web.archive.org/web/20031218024324/http://www.winamp.com/):

- Snazzy new look!
- Groovy new features!
- Most things actually work!


It’s the last part… the “Most things actually work!” that makes everyone laugh. And then they’re happy, and so they get excited about Winamp, and they use it, and tell their friends, and they think Winamp is awesome, all because they actually wrote on their website, “Most things actually work!” How cool is that?


If you threw a bunch of extra programmers onto the Windows Media Player team, would they ever hit that high note? Never in a thousand years. Because the more people you added to that team, the more likely they would be to have one real grump who thought it was unprofessional and immature to write “Most things actually work” on your website.


Not to mention the comment, “Winamp 3: Almost as new as Winamp 2!”


That kind of stuff is what made us love Winamp.


By the time AOL Time Warner Corporate Weenieheads got their hands on that thing the funny stuff from the website was gone. You can just see them, fuming and festering and snivelling like Salieri in the movie *Amadeus*, trying to beat down all signs of creativity which might scare one old lady in Minnesota, at the cost of wiping out anything that might have made people *like* the product.


Or look at the iPod. *You can’t change the battery*. So when the battery dies, *too bad. Get a new iPod*. Actually, Apple will replace it if you send it back to the factory, but that costs $65.95. Wowza.


Why can’t you change the battery?


My theory is that it’s because Apple didn’t want to mar the otherwise perfectly smooth, seamless surface of their beautiful, sexy iPod with one of those ghastly battery covers you see on other cheapo consumer crap, with the little latches that are always breaking and the seams that fill up with pocket lint and all that general yuckiness. The iPod is the most seamless piece of consumer electronics I have ever seen. It’s beautiful. It *feels* beautiful, like a smooth river stone. One battery latch can blow the whole river stone effect.


Apple made a decision based on *style*, in fact, iPod is full of decisions that are based on style. And style is not something that 100 programmers at Microsoft or 200 industrial designers at the inaptly-named Creative are going to be able to achieve, because they don’t have [Jonathan Ive](http://www.designmuseum.org/design/index.php?id=63), and there aren’t a heck of a lot of Jonathan Ives floating around.


I’m sorry, I can’t stop talking about the iPod. That beautiful thumbwheel with its little clicky sounds …  Apple spent *extra money* putting a speaker *in the iPod itself* so that the thumbwheel clicky sounds would come from the thumbwheel. They could have saved pennies … *pennies!* by playing the clicky sounds through the headphones. But the thumbwheel makes you feel like you’re in control. People like to feel in control. *It makes people happy to feel in control. *The fact that the thumbwheel responds smoothly, fluently, and *audibly* to your commands makes you *happy*. Not like the other 6,000 pocket-sized consumer electronics bit of junk which take so long booting up that when you hit the on/off switch you have to wait a minute to find out if anything happened. Are you in control? Who knows? When was the last time you had a cell phone that went on the instant you pressed the on button?


Style.


Happiness.


Emotional appeal.


These are what make the huge hits, in software products, in movies, and in consumer electronics. And if you don’t get this stuff right you may solve the problem but your product doesn’t become the #1 hit that makes everybody in the company rich so you can *all *drive stylish, happy, appealing, cars like the Ferrari Spider F-1 and still have enough money left over to build an ashram in your back yard.


It’s not just a matter of “10 times more productive.” It’s that the “average productive” developer never hits the high notes that make great software.


Sadly, this doesn’t really apply in non-product software development. Internal, in-house software is rarely important enough to justify hiring rock stars. Nobody hires Dolly Parton to sing at weddings. That’s why the most satisfying careers, if you’re a software developer, are at actual software companies, not doing IT for some bank.


The software marketplace, these days, is something of a winner-take-all system. Nobody else is making money on MP3 players other than Apple. Nobody else makes money on spreadsheets and word processors other than Microsoft, and, yes, I know, they did anti-competitive things to get into that position, but that doesn’t change the fact that it’s a winner-take-all system.


You can’t afford to be number two, or to have a “good enough” product. It has to be remarkably good, by which I mean, so good that people remark about it. The lagniappe that you get from the really, really, really talented software developers is your only hope for remarkableness. It’s all in the plan:



| Best Working Conditions | → | Best Programmers | → | Best Software | → | Profit! |

