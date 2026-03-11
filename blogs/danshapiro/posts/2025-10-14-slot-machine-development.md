---
title: "Slot Machine Development"
date: 2025-10-14
url: https://www.danshapiro.com/blog/2025/10/slot-machine-development/
word_count: 679
---


Something new is possible.


Four weeks ago, I braved the gaggle of Waymos nosing around the Presidio to check out [Connected Stack](https://www.connectedstack.ai/). I plopped next to my buddy James Cham, notorious partner at [Bloomberg Beta](https://github.com/Bloomberg-Beta/Manual). We started swapping stories while earnest founders pitched their wares on stage. James started telling me strange things about his portfolio companies’ latest discoveries. I was skeptical.


“You’ve got to meet Justin. He’s doing incredible things.”


A few hours later at Piccino, I found [Justin McCarthy](https://www.strongdm.com/blog/author/justin-mccarthy?utm_source=chatgpt.com), CTO of StrongDM, scooping up gnocchi at a table made from a large subsection of a redwood tree.


He started telling me about his efforts to scale the use of AI in development. I furrowed my brow. “If there’s one thing I’ve learned about AI development”, I said as I grabbed the burrata, “it’s this: you have to review *every* checkin. If you don’t, things things go farkakte, fast”.


Justin stared at me.


I faltered.


I mean… it’s always been that way… maybe less, lately?


Then Justin explained something to me very obvious. *If* your AI can accurately judge its own work, to at least a first approximation. *If* your AI can follow directions. And *if* you are willing to pay.


**You can delegate all your work in parallel and pick the winner.**


![](https://www.danshapiro.com/blog/wp-content/uploads/2025/10/image.png)


That’s it. That’s the trick. Pull the wheels until the software springs forth.


Dispatch a half-dozen requests to write the code. Have each instance test itself. That might be a unit test suite, that might be having an LLM inspect the output, that might be navigating the page with Playwright or – more likely – it might be all of the above. Everyone turns in their homework, and an LLM picks the winner.


What if it’s a total bust? No problem: keep the message thread going. Tell the losers why they lost, and get another round of iterations.


Slot-machine development is just N versions in parallel, a judge, and a budget.


And… it doesn’t seem right.


First, it’s remarkably expensive. But only if you’re thinking in terms of a $20/month ChatGPT subscription. If you’re thinking of it in terms of cost per developer-hour? I’ve tried it, and frankly it’s hard to spend as much on tokens in a day, as you pay an engineer in an hour.


Second, it seems daunting to build tests that good. But of course, the AI helps with that part too. I’ve gone from “AI writes unit tests” to “AI writes Cypress tests” to “AI has Playwright and just faffs around for a bit”. It’s astonishing, but the latter requires little more than a good prompt (“You’re a power user of localhost:8000 and you’re bent on breaking it; try everything”) and time to go get coffee.


Finally, and I think the real reason. It just feels… wasteful. I remember being hunched over the chatgpt terminal, waiting for each token to arrive. When something went off the rails – panic! Abort, reprompt, nudge, pray. Spending ten times the tokens on five parallel attempts feels like lighting money on fire.


But that’s just the fear talking.


[Everything old is new again](https://gse.ufsc.br/bezerra/disciplinas/Confiabilidade/docs/n-versionprogramming.pdf?utm_source=chatgpt.com).  As the value of tokens climbs faster than the cost, we can justify using more of them as we do more important work. First we learned to scale training compute. Then we learned to scale reasoning tokens in series. Now – inference tokens in parallel.


Things just keep getting more interesting.


*Notes:*

- *[Ryan Kanno](https://nocruft.com/) makes the outstanding point that delegating to **different** models in parallel is way better than many instances of the same model*.
- *Arjun may have been the original source of “slot machine development”. He’s building a beautiful, simple tool to do it for you at [https://www.superconductor.dev/](https://www.superconductor.dev/).*
- *Before that, Anthropic [called their own products a slot machine](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf), although they only dared to pull it once at a time.*
- *And it looks like Anthropic got it from [Roger Goldfinger](https://rgoldfinger.com/blog/2025-07-26-claude-code-is-a-slot-machine/), way back in the early days of… July?*

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
