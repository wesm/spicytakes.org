---
title: "Instead of restricting AI and algorithms, make them explainable"
description: "The steady increase in deployment of AI tools has led a lot of people     concerned about how software makes decisions that affect our lives. In one     example, its about âalgorithmicâ feeds in s"
date: 2024-07-30T00:00:00
tags: ["internet culture", "generative ai"]
url: https://martinfowler.com/articles/2024-restrict-algorithm.html
slug: 2024-restrict-algorithm
word_count: 806
---


The steady increase in deployment of AI tools has led a lot of people
    concerned about how software makes decisions that affect our lives. In one
    example, its about âalgorithmicâ feeds in social media that promote posts that
    drive engagement. A more serious impact can come from business decisions, such
    as how much premium to charge in car insurance. This can extend to affecting
    legal decisions, such as suggesting sentencing guidelines to judges.


Faced with these concerns, there is often a movement to restrict the use of
    algorithms, such as a recent activity in New York to [restrict how social media
    networks](https://www.theguardian.com/us-news/article/2024/jun/20/new-york-social-media-bill)
    generate feeds for children. Should we draw up more laws to fence in the
    rampaging algorithms?


In my view, the restricting the use of algorithms and AI here isn't the right
    target. A regulation that says a social media company should forego its
    âalgorithmâ for a reverse-chronological feed misses the fact that a
    reverse-chronological feed is itself an algorithm. Software decision-making can
    lead to bad outcomes even without a hint of AI in the bits.


**The general principle should be that decisions made by software must be
    explainable.**


When a decision is made that affects my life, I need to understand what led
    to that decision. Perhaps the decision was based on incorrect information.
    Perhaps there is a logical flaw in the decision-making process that I need to
    question and escalate. I may need to better understand the decision process so
    that I can alter my actions to get better outcomes in the future.


A couple of years ago I rented a car from Avis. I returned the car to the
    same airport that I rented it from, yet was charged an additional one-way fee
    that was over 150% of the cost of the rental. Naturally I objected to this, but
    was just told that my appeal against the fee was denied, and the customer
    service agent was not able to explain the decision. As well as the time and
    annoyance this caused me, it also cost Avis my future custom. (And thanks to the
    intervention of American Express, they had to refund that fee anyway). That bad
    customer outcome was caused by opacity - refusing to explain their decision
    meant they weren't able to realize they had made an error until they had
    probably incurred more costs than the fee itself. I suspect the error could be
    blamed on software, but probably too early for AI. The mechanism of the
    decision-making wasn't the issue, the opacity was.


So if I'm looking to regulate social media feeds, rather than ban AI-driven
    algorithms, I would say that social media companies should be able to show the
    user why a post appears in their feed, and why it appears in the position it
    does. The reverse-chronological feed algorithm can do this quite trivially, any
    âmore sophisticatedâ feed should be similarly explainable.


This, of course, is the rub for our AI systems. With explicit logic we can,
    at least in principle, explain a decision by examining the source code and
    relevant data. Such explanations are beyond most current AI tools. For me this
    is a reasonable rationale to restrict their usage, at least until developments
    to improve the explainability of AI bear fruit. (Such restrictions would, of
    course, happily incentivize the development of more explainable AI.)


This is not to say that we should have laws saying that all software
    decisions need detailed explanations. It would be excessive for me to demand a
    full pricing justification for every hotel room I want to book. But we should
    consider explainability as a vital principle when looking into disputes. If a
    friend of mine consistently sees different prices for the same goods, then we
    are in a position where justification is needed.


One consequence of this limitation is that AI can suggest options for a human
    to decide, but the human decider must be able to explain their reasoning
    irrespective of the computer suggestion. Computer prompting always introduces
    the the danger here that a person may just do what the computer says, but our
    principle should make clear that is not a justifiable response. (Indeed we
    should consider it as a smell for human to agree with computer suggestions too
    often.)


I've often felt that the best use of an opaque but effective AI model is
    as a tool to better understand a decision making process, possibly replacing
    it with more explicit logic. We've already seen expert players of go [studying the computer's play](https://www.scientificamerican.com/article/ais-victories-in-go-inspire-better-human-game-playing/) in order to improve their
    understanding of the game and thus their own strategies. Similar thinking
    uses AI to help understand tangled legacy systems. We rightly fear that AI
    may lead to more opaque decision making, but perhaps with the right
    incentives we can use AI tools as stepping stones to greater human
    knowledge.


---
