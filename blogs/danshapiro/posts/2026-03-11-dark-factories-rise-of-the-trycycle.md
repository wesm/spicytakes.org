---
title: "Dark Factories: Rise of the Trycycle"
date: 2026-03-11
url: https://www.danshapiro.com/blog/2026/03/dark-factories-rise-of-the-trycycle/
word_count: 1036
---


Companies are now producing [Dark Factories](https://www.danshapiro.com/blog/2026/02/you-dont-write-the-code/) – engines that turn specs into shipping software. The implementations can be complex and sometimes involve Mad Max metaphors. But they don’t have to be like that. **If you want a 5 minute factory, jump to [Trycycle](http://trycycle.ai) at the bottom.**


# The Engine in the Factory


Deep in their souls, Dark Factories are all built on the same simple breakthrough:


AI gets better when you do more of it.


How do you do “more AI” effectively? Software factories use two patterns. One of them I’ve already told you about – [slot machine development](https://www.danshapiro.com/blog/2025/10/slot-machine-development/). Instead of asking one AI, you ask three at once, and choose the best one. It feels wasteful, but it gives better results than any model could alone.


Does 3 models at a time seem wasteful? Well, wait until you meet the other pattern – the trycycle.


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image-1.png)

*The simplest trycycle*


It seems trivial, but it’s an unstoppable bulldozer that can bury any problem with time and tokens. And of course, you can combine it with slot machine development for a truly formidable tool.


Every software factory has a trycycle at its heart. Some of them are just surrounded by deacons and digraphs.


(And as a side note, they are all more fun with [freshell](http://freshell.net), which is free, open source, and makes managing agents a joy!)


Let’s meet the factories, shall we?


# Gastown


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image-3.png)


Steve Yegge saw this coming like a war rig down a cul-de-sac. His factory, Gastown, dropped the day after New Years and I was submitting PRs before the code was dry. It launched as a beautiful disaster, with mayors, convoys, and polecats fighting for guzzoline in the desert of your CPU. It’s now graduated to a [fully-fledged MMORPG for writing code](https://steve-yegge.medium.com/welcome-to-the-wasteland-a-thousand-gas-towns-a5eb9bc8dc1f). It’s amazing, it’s effective, and it’s pioneering in a fully Westworld sort of way.


# The StrongDM Attractor


Justin, the CTO of StrongDM, talks about the factory as a feedback loop. It used to be that when a model was fed its own output, it would break fix 9 things and break 10 – like a busy and productive company that was losing just a bit of money on every transaction. But sometime last year, the models crossed an invisible threshold of mediocrity and went from slightly-lossy to slightly-gainy. They started getting better with each cycle.


Justin’s team noticed, and built the StrongDM attractor to cash in.


If Gastown is Mad Max, StrongDM is Factorio: an infinitely flexible, wildly powerful system for constructing exactly the factory you need.


But the StrongDM team did something interesting – they didn’t ship their factory. Instead, they shipped [the specification for the Attractor](https://factory.strongdm.ai/products/attractor), so everyone can implement their own.


And you can absolutely implement your own! But you can also just steal the one I made for you.


# Kilroy


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image.png)


**[Kilroy](https://github.com/danshapiro/kilroy)** is a StrongDM Attractor written in Go (although it works with projects in any language). It has all the flexibility of the Attractor design, but it also ships with an actual functioning factory configuration, tests, sample files, and other things that make it more likely to work.


In theory, you don’t need Kilroy – you can just point Claude Code or Codex CLI  at the Attractor specification and burn some tokens. [My friend Harper built three](https://2389.ai/posts/the-dark-factory-is-a-dot-file/) (and you should read his post for some meditations on where the Attractor approach is heading).


In practice, it took the better part of a month for me and some wonderful contributors to polish up Kilroy to the point where it is now, so you may save yourself some time, tokens, and effort by just stealing this.


[**https://github.com/danshapiro/kilroy**](https://github.com/danshapiro/kilroy)


# Enter the Trycycle


![](https://www.danshapiro.com/blog/wp-content/uploads/2026/03/image-2.png)


Last night I was carefully building the dotfiles and runfiles for a Kilroy project – configuring the factory to build the project.


Then a thought struck.


What if this was just a skill?


Enter [Trycycle](http://trycycle.ai), the very simplest trycycle. It’s a very simple skill for Claude Code and Codex CLI that implements the pattern in plain english.

1. Define the problem
2. Write a plan
3. Is the plan perfect? If not, try again.
4. Implement the plan.
5. Is the implementation perfect? If not, try again.


That’s basically it. To use it, you open your favorite coding agent and say, “Use Trycycle to do the thing”. Then sit back and watch the tokens fly.


It’s simple because it’s just a skill. Under the hood, it adapts [Jesse](https://blog.fsck.com/)‘s amazing [Superpowers](https://github.com/obra/superpowers) for plan writing and executing. It will take you literally minutes to get started. Just paste this into your agent and you’re off to the three-wheel races.


`Hey agent! Go here and follow the installation instructions. https://raw.githubusercontent.com/danshapiro/trycycle/main/README.md `


Trycycle is barely 24 hours old as of the time of this writing. I’ve shipped well over a dozen features with it already, and I was in meetings most of the day. While I was having dinner it ported Rogue to WASM (!).  Last night it churned for 7 hours and 56 minutes and landed 6 features for [freshell](http://freshell.net).


The best part, though, is that because it’s just a skill, it’s instantly part of your dev flow. There’s no configuration or learning curve. If you want to understand it better, just ask. If you don’t like what it’s doing, have stern words.


[https://github.com/danshapiro/trycycle](https://github.com/danshapiro/trycycle)


# Which one to use?


Here’s how I’d decide right now.


If you want to become part of a **growing movement of collaborators** burning tokens together to build software, individually and collectively – try [Gastown](https://steve-yegge.medium.com/welcome-to-the-wasteland-a-thousand-gas-towns-a5eb9bc8dc1f).


If you want to invest in building a **powerful, configurable, sophisticated engine** that can drive your projects forward 24 hours a day – try [Kilroy](https://github.com/danshapiro/kilroy).


If you just want to **get things done right now**, give [Trycycle](https://github.com/danshapiro/trycycle) a spin. Heck, it’s fast enough that you can spin up a Trycycle while you read the docs on Kilroy and Gastown.


And whatever you choose, I recommend you do it with [freshell.net](http://freshell.net), because it’s just more delightful that way!


*Thanks to *[*Harper Reed*](http://harperreed.com)*, [Steve Yegge](https://steve-yegge.medium.com/), *[*Jesse Vincent*](http://fsck.com)*, *[*Justin Massa*](http://remixpartners.ai/)*, *[*Nat Torkington*](https://nathan.torkington.com/)*, *[*Marcus Estes*](https://vibes.diy/)*, and *[*Arjun Singh*](https://www.linkedin.com/in/arjun-singh-629216105/)* for reading drafts of this. *

[Powered by](https://follow.it)

You might want to [subscribe](https://www.danshapiro.com/blog/feed/) or [follow me on Twitter](https://www.twitter.com/danshapiro) so you don't miss new articles.
