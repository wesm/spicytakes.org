---
title: "Software Friction"
date: 2024-05-01
url: https://www.hillelwayne.com/post/software-friction/
slug: software-friction
word_count: 671
---

In his book [*On War*](https://www.clausewitz.com/readings/OnWar1873/BK1ch07.html), Clausewitz defines friction as the difference between military theory and reality:


> Thus, then, in strategy everything is very simple, but not on that account very easy.
> Everything is very simple in war, but the simplest thing is difficult. These difficulties accumulate and produce a friction, which no man can imagine exactly who has not seen war.
> As an instance of [friction], take the weather. Here, the fog prevents the enemy from being discovered in time, a battery from firing at the right moment, a report from reaching the general; there, the rain prevents a battalion from arriving, another from reaching in right time, because, instead of three, it had to march perhaps eight hours; the cavalry from charging effectively because it is stuck fast in heavy ground.


Ever since reading this, I’ve been seeing “friction” everywhere in software development:

- A vendor’s API doesn’t work quite as you thought it did, or it did and then they changed it.
- Bugs. Security alerts. A dependency upgrade breaks something.
- Someone gets sick. Someone’s kid gets sick. Someone leaves the company. Someone leaves for Burning Man.
- The requirements are unclear, or a client changes what they want during development. A client changes what they want *after* development.
- A laptop breaks or gets stolen. Slack goes down for the day.
- Tooling breaks. Word changes every font to wingdings. ([This is a real thing](https://answers.microsoft.com/en-us/msoffice/forum/all/word-changes-font-to-wingdings/688e0253-1fb7-4b4f-8407-568715e69e99))


This list is non-exhaustive and it’s not possible to catalogue all possible sources of friction.


### Some Properties of Friction


Friction matters more over large time horizons and large scopes, simply because more things can go wrong.


Friction compounds with itself: two setbacks are more than twice as bad as one setback. This is because most systems are at least *somewhat* resilient and can adjust itself around some problem, but that makes the next issue harder to deal with.


(This is a factor in the controversial idea of “don’t deploy on Fridays”. The friction caused by a mistake during deployment, or of needing to doing a rollback, would be made much worse by the friction of people going offline for the weekends. The controversy is between people saying “don’t do this” and people advocating for [systemic changes to the process](https://charity.wtf/2019/05/01/friday-deploy-freezes-are-exactly-like-murdering-puppies/). Either way the goal is to make sure friction doesn’t cause problems, it’s a debate over *how* exactly to do this.)


Addressing friction can also create other sources of friction, like if you upgrade a dependency to fix a security alert but the new version is subtly backwards incompatible. And then if you’re trying to fix this with a teammate who lives in a different timezone…


## Addressing Friction


Friction is inevitable and impossible to fully remove. I don’t think it’s possible to even fully anticipate. But there are things that can be done to reduce it, and plans can be made more resilient to it. I don’t have insight into how military planners reduce friction. This is stuff I’ve seen in software:


### Questions I have about friction


Is it useful to subcategorize sources of friction? Does calling a tooling problem “technical” as opposed to “social” friction do anything useful to us?


How do other fields handle friction? I asked some people in the construction industry about friction and they recognized the idea but didn’t have a word for it. What about event planners, nurses, military officers?


How do we find the right balance between “doing X reduces the effect of friction” and “*not* doing X is more efficient right now”?


Is friction important to *individuals*? Do I benefit from thinking about friction on a project, even if nobody else on my team does?


*Thanks for [Jimmy Koppel](http://www.jameskoppel.com/) for feedback. If you liked this post, come join my [newsletter](https://buttondown.email/hillelwayne/)! I write new essays there every week.*


*I train companies in formal methods, making software development faster, cheaper, and safer. Learn more [here](https://www.hillelwayne.com/consulting/).*


---


### Update 2024-05-30


I’ve collected some of the comments I received on this post [here](https://www.hillelwayne.com/comments/software-friction/).
