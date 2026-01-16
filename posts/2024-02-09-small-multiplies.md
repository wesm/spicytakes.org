---
title: "Small multiplies"
subtitle: "If you’re good at something, just do that?"
date: 2024-02-09T17:32:24+00:00
url: https://benn.substack.com/p/small-multiplies
slug: small-multiplies
word_count: 2282
---


![](https://substackcdn.com/image/fetch/$s_!0G7j!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8389eda-c34c-463f-acc5-fce64268b507_1200x673.png)


> The moment, you own it, you better never let it goYou only get one shot, do not miss your chance to blowThis opportunity comes once in a lifetimeLose Yourself, Eminem


One way to think about Dan Campbell and the Detroit Lions is that they found a strategy that worked for a season, but didn’t work for a game.


For years, quants have been begging NFL coaches to go for it on fourth down more often. In 2006, David Romer, a prominent academic economist,published a formal mathematical modelthat found that coaches punt way more than they should, and frequently made “systematic, clear-cut, and overwhelmingly statistically significant departures from the decisions that would maximize teams’ chances of winning.” In 2009, Romer’s arguments—sparked by anunconventional fourth-down callby (now unemployed) Patriots’ coach Bill Belichick—startedgetting more attention. In 2014, theNew York Timescreated a (now defunct)Twitter botthat analyzed fourth down decisions in real time, and harassed coaches when they ignored the numbers and punted.


At first, coaches stuck to their conservative guns. From 2006 through 2017, NFL teams consistently went for it on fourth downabout ten percent of the time. But in 2018, things changed: Teams steadily started going for it more often. Today, the league-wide “go for it” rate isjust under twenty percent.


No coach has been more aggressive than Dan Campbell. In 2021, Campbell was hired as the Detroit Lions’ head coach. At that time, the highest single-season “go for it” rate was 25.4 percent, by the 2020 Philadelphia Eagles. Today, the three highest rates are the2021 Detroit Lions, at 29.5 percent; the2022 Detroit Lions, at 29.6 percent; and the2023 Detroit Lions, at 30.5 percent.


By at least one very crude measure, Campbell’s strategy has worked. After finishingdead lastin their conference in 2021, the Lions finishedthirdthis year—and, two weeks ago, were playing in the NFC championship game, one win away from making their first Super Bowl in franchise history.


WithEminem in the audience, the Lions took a big early lead against the San Francisco 49ers. The lead slipped, the game tightened, and twice in the second half, the Lions’ found themselves facing a fourth and short, inside the San Francisco thirty yard line. Twice, they had a choice: Kick a field goal, or play the way they have for the last three years, and go for it. Twice, they went for it.And twice, theygot stopped.


In at least a superficial sense, the two decisions cost the Lions the game. Their gambles took six potential points off the board;they lost by three.1


After the game, the mediapressed Campbellabout the two calls. Other NFL coachesblamed the nerdsand their dweeby models. The nerdsfired back. Armchair analysts—i.e.,randomtweetsIsaw—wondered what went wrong. Did the models not account for how good the Lions’ kicker was? Did they adjust for the pressure of the playoffs? For the game being in San Francisco? For the Detroit Lionsbeing the Detroit Lions? For thegreat disturbanceincosmic gravity of the NFLthat could render our entire understanding of the game, of its mathematical properties, and of the very physics of our universe, null and void?2


The unsatisfying truth is probably simpler than that: Neither fourth down decision mattered all that much. According toESPN’s models, on each fourth down attempt, the Lions increased their chances of winning by about 0.3 percent by going for it instead of kicking a field goal. Even if the models underestimate the importance of the choice by an order of magnitude—if the swing was three percentage points—thedecisionto go for it wasn’t all that consequential.


Put differently, in both cases, the Lions were given two coins, and had to choose which one to flip. One coin landed on heads fifty percent of the time, and the other landed on heads, at most, 53 percent of the time. If the Lions flipped heads, they’d take a huge advantage in the game; if they flipped tails, they’d be put at a huge disadvantage. Though theresultof the coin toss would clearly affect the outcome of the game, there isn’t much practical difference between which coin they choose to flip.


Flipping the favored coinover the course of the entire season,however, can make a big difference. Teams average about eight fourth downs a game. If, on one of those eight attempts—which is exactly how much more the Lions went for it this year compared to the NFL average—a team flipped the coin that landed on heads 53 percent of time instead of fifty, they’d win half a game more per season.3In a league in which a third of the teams were one win awayfrom either making the playoffs or missing them, that’s a significant swing, even if no individual choice is all that consequential.4


To overstylize the point, the Lions won in the regular season not just because they found an edge, but because they found an edge that theycould exploit a lot. In the playoffs, when they had two plays—two shots, two opportunities, to seize everything they ever wanted—that advantage was too small to matter. If you only get a couple rolls, playing the odds is still a crapshoot.


At a glance, all of this is sort of boring and obvious. The decision to go for it is a probabilistic gamble, and sometimes, the mathematically correct bet still loses. You canhit on twelveand bust; you can stand on nineteen and lose if the dealer draws twenty. That’s how probabilities work; we all know this. Still, I think it’s a useful analogy for a bad way to use data, for a good way to try to use data, and for a way to make data actually useful.


# Not data or intuition, but secret third thing


Most of the time, we don’t need data to make a decision. NFL coaches don’t need analysts to tell them to punt on fourth and twelve on their own 22-yard line. Blockbuster clerks didn’t need a neural net to tell them that people who likedHappy Gilmorewill probably likeThe Waterboy. None of us need to carefully study months of New York traffic data to figure out that we shouldn’t try todrive across Manhattanat 3 p.m. on a Friday afternoon. Venture capitalists don’t need a meticulous data room from every startup to pass on most investment pitches; product managers often don’t need to run detailed A/B tests to know if their customers like a new releases; bloggers don’t need to study their Substack dashboards to know when a post is a hit or a flop. As Amazon distinguished scientist Garrett van Ryzinput it, “when a project we work on succeeds, we don't need statistics to know it.”


Datahelps on the edges. It give us a slightly more promising coin when it’s fourth and three on your opponent’s 35-yard line; when you have to choose between recommendingThe WaterboyorBilly Madison; when you’re deciding between taking the Lincoln Tunnel or the Holland Tunnel; and when you’re excited about an investment but have a couple lingering concerns. That’s the entire point, in most cases—for data to make visible the small differences we can’t see on our own.5


In this light—that data won’t make any one decision that much better, but only bias it a bit more in our favor—it’s tempting to look for leverage by applying it to the most important decisions. In corporate contexts, there’s also a lot of prestige in these decisions. And so we say,put us in the boardroom, where our powers will be amplified by the importance of the issues that we apply them to.


We’re probably better off going in the exact opposite direction. Instead of analyzing how we can improve infrequent, high-leverage decisions, we should try to figure out how we can make thefrequent,low-leverage onesbetter.Be like a high-frequency trader, chasing small bits of mechanical alpha in every trade. Be like Google, and find ways to improve ad conversion rates by some tiny percentage. Don’t be intuition-driven or data-driven; be quantity-driven, and look exclusively for places where you can create a durable advantage through frequent, small—and in the aggregate, predictable—bets that you’ve tilted in your favor.


# Ok, a secret fourth thing


But actually? I think that’s mostly terrible advice. It’s more folklore and fairy tales about the predictive power of big data. Though it sounds easy enough—in reams of data about ad clicks, or user behaviors patterns, or NFL play-by-play logs, how hard can it be to find a few optimizations?—it’s actually very difficult to pull off. It took several years, millions of dollars, and aglobally famous competitionfor Netflix to improve their recommendations by ten percent. Even small improvements are hard to find.


It’s possible, though, to invert the problem. Rather than trying to make frequent decisions better, we probably should try to make good decisions more frequent. Don’t use data to get good at something we do a lot; use data to figure out what we’re good at, and then do it more often. Make data aStrengthsFinder©.


Was Mr. Beast that much better at hacking YouTube than other creators? Was Y Combinator that much better at selecting startups than other incubators? Was Taylor Swift that much better at making music than every other pop star? I’d argue no. They just found a small edge that they naturally had—Mr. Beast stumbled into a teen shock jock genre that people liked; YC had a popular brand and marketable founder; Taylor Swift made catchy and relatable songs—and they hammered it. Mr. Beast had made a videoevery five days for a decade; YC went from acceptingten companies per cohort to 400; Taylor Swift can’t stand in front of a microphonewithout announcing a new album.


It’s easy, I think, to get caught up in the allure of the big moment. We all want our fifteen minutes. If you’re a marketer, the glory is in theviral moment. If you’re a great writer, your legacy seemingly depends onyour magnum opus. And if you’re an NFL coach, your career depends on what happens in the playoffs. But no matter how good you are—at the thing, or at studying the data around the thing—you’ll never create a durable advantage by constantly betting the house. Those advantages come from theboring compounding of small biases.


In sports, however, you sometimes have to bet the house. In almost everything else we do, the results of our decisions are more fungible; we rarelyhaveto go risk everything in a winner-take-all championship game. We can find the things we’re a little bit better at than most, figure out how to run that play over and over and over, and let them multiply in an eternal regular season.

[1](https://benn.substack.com/p/small-multiplies#footnote-anchor-1-141528758)

Here’s a question about this that bothers me: How do you judge if Campbell’s analysis here was right? On one hand, it definitely wasn’t; they lost. On the other hand, he probably played the odds correctly? It seems crazy to define decisions only by their outcomes (very dumb things that shouldn’t work out sometimes do), but it also seems crazy to ignore the outcome? I think I’m still in thesame place I was on this years ago—“right” is basically a social definition, and a decision’s correctness depends on how much other people agree that it was correct.

[2](https://benn.substack.com/p/small-multiplies#footnote-anchor-2-141528758)

Millions of voices suddenlycried out in terror, and werethey’re being too loud.

[3](https://benn.substack.com/p/small-multiplies#footnote-anchor-3-141528758)

This is pretty similar to the Romer’s original estimates. In his 2006 paper, he found that being appropriately aggressive on fourth down would result in “an increase of about 2.1 percentage points in the probability of winning” any given game, and improve a team’s record by a little more than a third of a win per season.

[4](https://benn.substack.com/p/small-multiplies#footnote-anchor-4-141528758)

That said, one boneheaded play call may have cost the Lions; it just wasn’t either fourth down attempt. With 1:03 left in the fourth quarter, the Lions were down by ten, had the ball on 49ers three yard line, and, critically, still had all three timeouts left. If they were able to score without using a timeout, they could potentially get the ball back without needing to recover an onside kick. If theydidn’thave all of their timeouts, however, they needed to recover the kick—and because of a series of recent rule changes, the onside kick recovery rate in the NFL has collapsedfrom 15 percent to 5 percent.*


Inexplicably, on third down, the Lions ran the ball. They got stopped andthen called a timeout. Why?!! It makes no sense. Hustle to the line, and run a fourth down play. Kick a quick field goal and save yourself a chance to throw a Hail Mary when you’re down by seven. Anything. But how can you not save that timeout, when calling it all but guarantees you’ll lose?


* I’m all for theGreg Schiano and Jon Bois proposalto get rid of both kickoffs and onside kicks entirely. Under their proposal, when a team scores, they would be given the ball back on their own thirty. Rather than it being first and ten, however, it would automatically be fourth and fifteen. In most cases, the team would probably choose to punt, so the result would be more or less the same as a kickoff—the receiving team getting the ball around their own 25. But they could also just try to convert the fourth and fifteen, which would be risky, but, one, actually achievable, two, a normal football play unlike whatever nonsense an onside kick is, and three, very exciting. Plus, it would be easy to adjust the competitive balance of the rule. Want more recoveries? Make it fourth and ten. Want fewer? Make it fourth and 25 (but just notfourth and 26).

[5](https://benn.substack.com/p/small-multiplies#footnote-anchor-5-141528758)

We data folk sometimes sell a more dramatic narrative about data leading to some eureka moment—Burbnshould pivot to a photo-sharing app! Netflix shouldmake a political thriller!—but these momentsare few and far between.
