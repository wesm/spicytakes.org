---
title: "The Hugging Will Continue Until Morale Improves"
date: 2015-12-04
url: https://blog.codinghorror.com/the-hugging-will-continue-until-morale-improves/
slug: the-hugging-will-continue-until-morale-improves
word_count: 1894
---

I saw in today’s news that Apple [open sourced their Swift language](https://t.co/KpC9xID5kU). One of the most influential companies in the world explicitly adopting an open source model – that’s great! I’m a believer. One of the big reasons [we founded Discourse](https://blog.codinghorror.com/civilized-discourse-construction-kit/) was to build an open source solution that anyone, anywhere could use and safely build upon.


![It's not that Unix won -- just that closde source lost. Big time.](https://blog.codinghorror.com/content/images/2025/09/image-23.png)


People were also encouraged that Apple was so refreshingly open about this whole process and involving the larger community in the process. They even hired from the community, which is something I always urge companies to do.


![@siracusa Apple hired Homebrew's creator to build swift-package-manager github.com/apple/swift-pa...](https://blog.codinghorror.com/content/images/2025/09/image-24.png)


Also, not many people were, shall we say… *fans*… of Objective C as a language. There was a lot of community interest in having another viable modern language to write iOS apps in, and to Apple’s credit, they produced Swift, and even promised to open source it by the end of the year. And they delivered, in a deliberate, thoughtful way. (Did I mention that [they use CommonMark](https://github.com/apple/swift-cmark)? That’s kind of awesome, too.)


One of my heroes, Miguel de Icaza, happens to have *lots* of life experience in open sourcing things that were not exactly open source to start with. He applauded the move, and even made a small change to his Mono project in tribute:


![When Swift was open sourced today, I saw they had a Code of Conduct. We had to follow suit, Mono has adopted it: github.com/mono/mono/blob...](https://blog.codinghorror.com/content/images/2025/09/image-25.png)


Which I also thought was kinda cool.


It surprises me that anyone could ever object to the mere *presence* of a code of conduct. But [some people do](https://medium.com/@jmspool/safe-conferences-are-deliberately-designed-2849b6cd3658).

kg-card-begin: html

> A weak Code of Conduct is a placebo label saying a conference is safe, without actually ensuring it’s safe.
> Absence of a Code of Conduct does not mean that the organizers will provide an unsafe conference.
> Creating safety is not the same as creating a feeling of safety.
> Things organizers can do to make events safer: Restructure parties to reduce unsafe intoxication-induced behavior; work with speakers in advance to minimize potentially offensive material; and provide very attentive, mindful customer service consistently through the attendee experience.
> Creating a safe conference is more expensive than just publishing a Code of Conduct to the event, but has a better chance of making the event safe.
> Safe conferences are the outcome of a deliberate design effort.

kg-card-end: html

I have to say, I don’t understand this at all. Even if you do believe these things, why would you say them *out loud?* What possible constructive outcome could result from you saying them? It’s a textbook case of honesty [not always being the best policy](https://blog.codinghorror.com/trust-me-im-lying/). If this is all you’ve got, just say nothing, or wave people off with platitudes, like politicians do. And if you’re [Jared Spool](https://en.wikipedia.org/wiki/Jared_Spool), notable and famous within your field, it’s even worse – what does this say to everyone else working in your field?


Mr. Spool’s central premise is this:


> Creating safety is not the same as creating a feeling of safety.


Which, actually … isn’t true, and runs counter to everything I know about empathy. If you’ve ever watched It’s Not About the Nail, you’ll understand that **a *feeling* of safety is, in fact, what many people are looking for**. It’s not the whole story by any means, but it’s a very important starting point. An anchor.


People understand you [cannot possibly protect them](https://medium.com/@ag_dubs/no-true-conference-organizer-dd0ff11294a) from every single possible negative outcome at a conference. That’s absurd. But they also want to hear you stand up for them, and say out loud that, yes, these are the things we believe in. This is what we know to be true. Here is how we will look out for each other.


I also had a direct flashback to Deborah Tannen’s groundbreaking [You Just Don’t Understand](http://www.amazon.com/dp/0060959622/?tag=codihorr-20), in which you learn that **men are all about fixing the problem**, so much so that they rush headlong into any remotely plausible solution, without stopping along the way to actually *listen* and appreciate the depth of the problem, which maybe… can’t really even *be* fixed?


> If women are often frustrated because men do not respond to their troubles by offering matching troubles, men are often frustrated because women do … he feels she is trying to take something away from him by denying the uniqueness of his experience … if women resent men’s tendency to offer solutions to problems, men complain about women’s refusal to take action to solve the problems they complain about.
> Since many men see themselves as problem solvers, a complaint or a trouble is a challenge … Trying to solve a problem or fix a trouble focuses on the message level. But for most women who habitually report problems at work or in friendships, the message is not the main point … trouble talk is intended to reinforce rapport by sending the metamessage “We’re the same; you’re not alone.”
> Women are frustrated when they not only don’t get this reinforcement but, quite the opposite, feel distanced by the advice, which seems to send the metamessage “We’re not the same. You have the problems; I have the solutions.”


Having children really underscored this point for me. The quickest way to turn a child’s frustration into a screaming, explosive tantrum is to **try to fix their problem for them**. This is such a hard thing for engineers to wrap their heads around, particularly male engineers, because we are *all about* fixing the problems. That’s what we do, right? That’s why we exist? We fix problems?


I once wrote this in reply to an [Imgur](https://community.imgur.com/) discussion topic about navigating an “emotionally charged situation:”


> Oh, you want a master class in dealing with emotionally charged situations? Well, why didn’t you just say so?
> **Have kids.** Within a few years you will learn to be an expert in dealing with this kind of stuff, because what nobody tells you about having kids is that for the first ~5 years, they are constantly. freaking. the. f**k. out.
> [46 Reasons My Three Year Old Might Be Freaking Out](https://web.archive.org/web/20161226224504/http://jasongood.net/365/2012/12/46-reasons-why-my-three-year-old-might-be-freaking-out/)
> If this seems weird to you, or like some kind of made up exaggerated hilarious absurd brand of humor, oh trust me. It’s not. Real talk. *This is actually how it is.*
> In their defense, it’s not their fault: they’ve never felt fear, anger, hunger, jealousy, love, or any of the dozen other incredibly complex emotions you and I deal with on a daily basis. So they learn. But along the way, there will be many many many manymanymanymany freakouts. And guess who’s there to help them navigate said freakouts?
> You are.
> [What works](https://blog.codinghorror.com/how-to-talk-to-human-beings/) is surprisingly simple: 
> Be there
> Listen
> Empathize, hug, and echo back to them
> *Don’t* try to solve their problems! DO NOT DO IT! Paradoxically, this only makes it way worse if you do. Let them work through the problem on their own. They always will – and knowing someone trusts you enough to figure our your own problems is a major psychological boost.
> You gotta [lick your rats](http://learn.genetics.utah.edu/content/epigenetics/rats/), man.
> (protip: this works identically on adults and kids. Turns out most so-called adults aren’t fully grown up. Who knew?)


I guess my point is that rats aren’t so different from people. We all want the same thing. Comfort from someone who can tell us that the world is safe, the world is not out to get you, that bad things can (and might) happen to you but you’ll still be OK* *because *we will help you*. We’re all in this thing together, you’re a human being much like myself and we love you.


**That’s why a visible, public code of conduct is a good idea, not only at an in-person conference, but also on a software project like Swift, or Mono.** But programmers being programmers – because they spend all day every day mired in the crazy world of infinitely recursive rules from their OS, from their programming language, from their APIs, from their tools – are rules lawyers *par excellence*. Nobody on planet Earth is better at arguing to the death over a set of completely arbitrary, made up rules than the average programmer.


I knew in my heart of hearts that someone – and by someone I mean a programmer – would inevitably complain about the fact that Mono had added a code of conduct, another “unnecessary” ruleset. So I made a programmer joke.


![When Swift was open sourced today, I saw they had a Code of Conduct. We had to follow suit, Mono has adopted it: github.com/mono/mono/blob... | @migueldeicaza I find these rules offensive and will be fining a complaint](https://blog.codinghorror.com/content/images/2025/09/image-26.png)


This is the second time in as many days that I made what I *thought* was an obvious joke on Twitter that was interpreted seriously.


![When someone starts at Discourse, I have the talk with them. "You remember your family? Forget them. Look at me. *We* are your family now."](https://blog.codinghorror.com/content/images/2025/09/image-27.png)


OK, maybe sometimes my Twitter jokes aren’t very good. Well, you know, that’s just, like… [*your opinion*, man](https://www.youtube.com/watch?v=6yfvuPk8xd4). I should probably switch from Twitter to Myspace or Ello or Google Plus or Snapchat or something.


But it bothered me that people, any people, would think I actually asked new hires to put the company above their family.* Or that I didn’t believe in a code of conduct. I guess some of that comes from having ~200k followers; once your audience gets big enough, [Poe’s Law](https://en.wikipedia.org/wiki/Poe%27s_law) becomes inevitable?


Anyway, I wanted to say I’m sorry. And I’m particularly sorry that [eevee](http://eev.ee/), who wrote that *awesome* PHP is a Fractal of Bad Design article [that I once riffed on](https://blog.codinghorror.com/the-php-singularity/), thought I was serious, or even worse, that my joke was in bad taste. Even though the [negative article about Discourse](http://eev.ee/blog/2015/09/17/the-sad-state-of-web-app-deployment/) eevee wrote did kinda hurt my feelings.


![@samsaffron @JakubJirutka programmers should not have feeling that is a liability](https://blog.codinghorror.com/content/images/2025/09/image-28.png)


I know we have our differences, but if we as programmers can’t come together through our collective shared horror over PHP, the Nickelback of programming languages, then clearly I have failed.


To show that **I absolutely do believe in the value of a code of conduct**, even as public statements of intent that we may not completely live up to, even if we’ve never had any incidents or problems that would require formal statements – I'm also adding a code of conduct as defined by [contributor-covenant.org](http://contributor-covenant.org/) to the [Discourse project](https://github.com/discourse/discourse). We’re all in this open source thing together, you’re a human being [very much like us](https://blog.codinghorror.com/what-if-we-could-weaponize-empathy/), and we vow to treat you with the same respect we’d want you to treat us. This should not be controversial. It should be common. And saying so matters.


If you maintain an open source project, I strongly urge you to consider formally adopting a code of conduct, too.


![When Swift was open sourced today, I saw they had a Code of Conduct. We had to follow suit, Mono has adopted it: github.com/mono/mono/blob... | @migueldeicaza I find these rules offensive and will be fining a complaint | @codinghorror hugs!](https://blog.codinghorror.com/content/images/2025/09/image-29.png)


The hugging will continue until morale improves.

kg-card-begin: html
kg-card-end: html
[swift](https://blog.codinghorror.com/tag/swift/)
[apple](https://blog.codinghorror.com/tag/apple/)
[open source](https://blog.codinghorror.com/tag/open-source/)
[programming languages](https://blog.codinghorror.com/tag/programming-languages/)
[software development concepts](https://blog.codinghorror.com/tag/software-development-concepts/)
