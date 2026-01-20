---
title: "The truth is out there"
subtitle: "The only thing stopping us from finding it is us."
date: 2023-05-12T16:23:17+00:00
url: https://benn.substack.com/p/the-truth-is-out-there
slug: the-truth-is-out-there
word_count: 1783
---


![](https://substackcdn.com/image/fetch/$s_!0y2U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85405101-c309-4adc-987a-b9037ac8fe2d_1200x1200.png)


Author’s preface:I’m toldthat some writers in the rationalist community preface their articles with an “epistemic status” that scores how confident the author is in the arguments they’re making. In writing this piece, I started to feel like these posts need a “Jared Kushnerstatus,” in which I rate the degree to which I know nothing about the subject, and am wandering into it with the unhinged confidence ofsome buffoonin a Harvard Business School class. I don’t know anything about chess or AI, but I did read most of the articles that I linked to, so: Jared Kushner status, 7/10.


---


Garry Kasparov was relieved.


In 1996, the chess grandmaster—the youngest-ever world champion and one of the best players in history—was playing his first game against Deep Blue, IBM's chess-playing supercomputer. Early in the game, Deep Blue offered up its pawnin a potential sacrifice. The move was bait: Had Kasparov taken the pawn, it would’ve set in motion a series of moves that would eventually tilt the game in Deep Blue’s favor.


The move itself was unremarkable; human players do things like this all the time. But computers—which Kasparov had been playing for years—typically played more mechanically. Prior to each move, they played out hundreds of millions of scenarios, and evaluated each based on the pieces that would be left on the board. This made computers overlymaterialistic, and prevented them from seeing the positional advantages that might come from sacrifices like Deep Blue’s pawn offering.


Initially, Kasparov was struck by the move. It revealed, as he put it, “a new kind of intelligence across the table.”


After the match, Kasparov realized he was mistaken. Some ethereal calculus hadn’t given Deep Blue a new intuition for the game; it found the movethrough brute force. “Deep Blue's computational powers were so great that it did in fact calculate every possible move all the way to the actual recovery of the pawn six moves later.” To Kasparov, this was an “inefficient, inflexible kind” of intelligence that could be gamed, tricked, and beaten.


His confidence, however, was short-lived. A year later, Kasparov famously lost to Deep Blue;1over the next two decades, chess-playing AIs blew past their human competitors,2to the point where it’s no longer interesting to watch the two play against each other.3


---


Author’s note: This next section references a blog post written inplain HTMLby an AI research scientist who graduated from Stanford in 1978, so: Jared Kushner status, 12/10.


---


What’s interesting, though, is that Kasparov wasn’t beaten because computers finally learned how to reason about chess. It was, asRichard Suttonargued in 2019,the opposite:


> Researchers always tried to make systems that worked the way the researchers thought their own minds worked—they tried to put that knowledge in their systems—but it proved ultimately counterproductive, and a colossal waste of researcher's time, when, through Moore's law, massive computation became available and a means was found to put it to good use.


According to Sutton, this has been the defining characteristic of AI research of the last 70 years. Researchers often assume that the best way to make an AI program better at some task is to teach it what they know, to “leverage their human knowledge of the domain.” But “the only thing that matters in the long run is the leveraging of computation:”


> The bitter lesson is based on the historical observations that 1) AI researchers have often tried to build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by search and learning.


Software designed this way did come with one weird quirk: Far from being rigid and formulaic in the way Kasparov expected, AI programs played with a sort of otherworldly flair. AlphaZero, a chess program built by DeepMind, doesn’t play like humans or standard computers; it plays,according to its creator Demis Hassabis, in a "third, almost alien, way" that’s like “chess from another dimension.”AlphaGo, DeepMind’s Go-playing AI, is “bit madcap,” makes “unorthodox opening moves,” and does things that are sometimes “downright incomprehensible.” PioSOLVER, a tool for evaluating poker hands, isboth dominant and sometimes suggests“really strange plays” that few professional poker players would make on their own. These programs are unnatural, but deadly superior.


All of this raises an uneasy question: If our strategies are so limited in these games—despite their precise rules and the centuries they’ve been studied—what else are we, relative to what’s possible, woefully bad at? What mazes are we trapped in, captive to our inability to see the logic that supercomputers can see?


Or, asBalaji Srinivasan put it in an interview with Lex Fridman:4


> A rat can be trained to turn at every even number or every third number in a maze to get some cheese. But evidently, it can't be trained to turn at prime numbers. Two, three, five, seven, and then eleven, and so on and so forth. That's just too abstract, and frankly, if most humans were dropped into a prime number maze, they probably wouldn't be able to figure it out either… And so the thing I think about a lot is just how many patterns in life are we just like these rats and we're trapped in a prime number maze?


---


Author’s note 2: We now return to more familiar footing—data teams, semantic layers, anddata angst. Jared Kushner status, 3/10.


---


Ever since the economy turned last spring, the data industry seems to have developed a creeping anxiety about its actual usefulness. In response, we’ve proposed a smattering of ideas that will finallyunlock our full potential.


Last fall, at dbt Labs’ annual conference, Ioffered up my solution: A return to well-worn operational models. Data teams should create simple abstractions of how their business works and use those as the foundation for everything they do. Think like an economist, I said. They model economies with supply and demand curves; we should model businesses withuser engagement loopsandgrowth models. I’ve been planning on turning that talk into a post here; in my spreadsheet of drafts, the note next to that idea says, “This is what we need more than anything. Best thing we can do as an analyst.”


On one hand, this still seems true. Companies are living ecosystems of incalculable complexity; these models—and their cousin, the now-trendysemantic layer—are our only means to reason about them.


On the other hand, this line of thinking sounds awfully similar to the trap Sutton is warning us about. Our business models and semantic layers are efforts to describe businesses as we see them; they are a “favored, human-centric approach,” and areourmethods—as opposed tothemethods—for reasoning about difficult and tangled problems. As Sutton argued, we often handicap ourselves by stubbornly sticking with these techniques; as Sutton predicted, we are, as data teams, also at least partially stalled in our own search for impact.


Which makes me wonder—for the problems that business analysts work on, what would it look like to run in the other direction, and favor approaches that leverage computation over human knowledge of the domain?


For example, consider how we might solve a pricing optimization problem. Today, we’d likely build a model that explains how we think pricing will affect different customers, add baseline inputs about our upsell and churn rates, and run a few sensitivity analyses by fiddling with those assumptions.


Tomorrow, we might use an AI for the analysis. But, if it’s still built on top of various semantic models that embed our own assumptions about how the world works—like segment classifications, or our methods for calculating various performance metrics—we could kneecap the AI’s potential by implicitly modeling the contents of our mind into the problem. Instead, perhaps we should be trying to remove ourselves and our semantics as much as possible, and let AI agents work on problems on their own terms.


Of course, I get that companies are not Go matches, which can be simulated millions of times in an instant. Moreover, corporate processes existonly as abstractions; there is no unbiased representation of a company as there is of a game of chess. Maybe—probably?—this is all hocus pocus, and a distraction from Doing the Real Work.


Still, part of me can’t escape Balaji’s prime number maze. Consider how far we are from the frontier of ideal performancein board games.5The space between our decisions and the optimal decisions in business domains—in marketing operations, in corporate finance, in sales strategy—must be immense. And surely there must be some way to close the gap.


---


Author’s postscript: This is the point that I shrug, say, “yeah, seems like a mess out there, good luck with that, but call me if you figure it out soI can invest it in and get an undeserved cut.” Jared Kushner status, 10/10.

[1](https://benn.substack.com/p/the-truth-is-out-there#footnote-anchor-1-120983523)

There’s a famous story from the first game of this rematch. Kasparov held the advantage, and on the forty-fourth move of the game, Deep Bluesent its rook halfway across the boardinto a position that, to even Kasparov's very discerning human eye, made no sense. Kasparov closed out the game easily, butwalked away rattled. What distant possibility had the computer seen that he couldn’t? What strategy did it devise that was beyond his creativity?


The answer, it turns out, was none of the above. The move was a glitch. Deep Blue had malfunctioned, and was programmed tochoose a move at randomwhen it didn’t know what to do. Rook to D1 was the number that the computer, frozen and stuck in a loop, drew out of a hat. More like Deep Blue screen of death, I guess.

[2](https://benn.substack.com/p/the-truth-is-out-there#footnote-anchor-2-120983523)

It’s as competitive asKobayashi versus the bear.

[3](https://benn.substack.com/p/the-truth-is-out-there#footnote-anchor-3-120983523)

One interesting related question: Why are we still interested in watching two people play chess, when games between two AIs would be far superior? When we watch sports, we generally watch the highest level of talent—the NBA over G League, the majors over the minors, and so on. Is it because we’re interested in the players as people? Because we want to live vicariously through their emotions? Because we actually like a flawed game? I truly don’t know. But in light of AIs potentially replacing us as artists, musicians, and writers, it seems relevant to figure out when and why we’re drawn to human creations.

[4](https://benn.substack.com/p/the-truth-is-out-there#footnote-anchor-4-120983523)

Good god, what a cursed sentence. What’s more, I’ve now mentioned Balajitwice on this blog, and both times have been positive. If I say his namethree more times, the Pomp Podcast will appear to gouge me with acrypto scam.

[5](https://benn.substack.com/p/the-truth-is-out-there#footnote-anchor-5-120983523)

As opposed to, say, tic-tac-toe, which we can playat the frontier.
