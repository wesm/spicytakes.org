---
title: "Developing In Stockfighter With No Trading Experience"
date: 2015-10-30
url: https://www.kalzumeus.com/2015/10/30/developing-in-stockfighter-with-no-trading-experience/
slug: developing-in-stockfighter-with-no-trading-experience
word_count: 5040
---


[Starfighter](http://www.starfighters.io) is a company which makes fun programming challenges. One of our goals is inspiring engineers to take a whack at problems they might assume are “too difficult for me.” Both sets of levels for our first game, Stockfighter, give copious opportunities for this: one set has you do algorithmic trading and one set has you do low-level C and assembly coding, reverse engineering, and security research.


In my experience, the modal web developer probably does not believe they can do algorithmic trading or reverse engineering of assembly code. We strongly disagree: every great developer you know got there by solving problems they were unqualified to solve until they actually did it. That’s why we’re making an environment to let you sink your teeth into fun, hard problems at your own pace, in a supportive community, with us taking care of the scutwork so you can focus on the intellectually interesting bits.


I wrote the algorithmic trading levels (with, I rush to add, no background in finance myself), so I thought I’d write a little bit about how to get started with algorithmic trading for a generalist programmer.


(If this is the first time you’re hearing about Starfighter (the company) or Stockfighter (our first game), you may wish to read [starfighters.io](http://www.starfighters.io) or [why and how we’re intent on spending the next few years of our lives fixing dev hiring](http://sockpuppet.org/blog/2015/03/06/the-hiring-post/). If you’ve heard of us before and are wondering “Yeah yeah, when do you launch?”, the honest answer is “We bit off a very aggressive engineering schedule between building [a stock exchange](https://www.kalzumeus.com/2015/08/20/designing-and-building-stockfighter-our-programming-game/) and [an entire C toolchain](http://sockpuppet.org/blog/2015/07/13/starfighter/). The last few months have been pretty rough, but we’re almost done. The game is feature-complete, in private beta now, and will be coming to an Internet near you ‘shortly.’”)


## Mea Maxima Culpa, Finance Programmers


I apologize in advance to experienced finance programmers — some of this is simplified a little bit for general consumption. Other parts might accurately reflect how Stockfighter’s simulations work but might not be maximally true-to-life, as we occasionally have to break with reality for pedagogic or player-experience reasons. (Also, it’s entirely possible that I’m wrong with regards to details — feel free to ping me if you think I have material errors. They’re my fault rather than that of our trading advisors.)


## The Problem Stock Exchanges Solve


Andy wants to buy a stock. Beth wants to sell the same stock. A stock exchange gives Andy and Beth a place to transact where they know there is a high likelihood that a willing counterparty (someone who takes “the other side” of the trade) exists.


The stock exchange is built around a data structure called an **order book**. An order book records orders: offers to buy a stock or sell a stock. By convention, these are called **bids** and **asks** respectively. (If you need a mnemonic, try “both ‘bids’ and ‘buy’ begin with ‘b’”, but you’ll have this in your muscle memory by your second day of writing trading systems.)


For a trade to happen, a bid and an ask must **cross**: that is, the maximum price the buyer is willing to pay must be greater than or equal to the lowest price the seller is willing to sell at. You might find it handy to remember those prices as ‘limits’, for reasons which will become obvious later.


An order book is a **prioritized queue** (or two of them: one for bids, one for asks), ordered by **“priority”**: “What is the first order that an incoming order would cross with?” There exist a variety of prioritization schemes at various exchanges, and they have *huge* impacts on how trading happens on those exchanges. Stockfighter assumes the simplest and most common algorithm: price/time priority. Basically, an order always interacts with the best priced order on the opposite side of the book first. Ties are broken by the timestamp that the exchange accepted the resting order at.


Since the order book is split into two parts, it’s often useful to know what the best bid and the best ask are. This is often called the **quote**. It is expressed as “$BID / $ASK” or, in spoken language, “$BID by $ASK.” For example, if I quote Google to you at $750.05 / $750.06, that means someone is willing to buy it for up to $750.05 and someone is willing to sell it for at least $750.06. (More sophisticated traders might want to know the size available at those levels. A **level** is simply a price. Why not call it a price? I have a sneaking suspicion Wall Street invented many of these words to give customers the impression “This is all really, really difficult — pay us money and the complexity goes away.”)


## The Fundamental Order Book Algorithm


There exist multiple order types which an exchange can support. By far the most common is a limit order, which can be understood as “I want to buy X shares (or as many up to X as I can) for a price which is no more than Y” or “I want to sell X shares (or as many up to X as I can) for a price which is at least Y.”


For each limit order the exchange receives, it checks:

1. Does the order cross with an order presently resting on the order book? If yes, they **match**, for as many shares as possible (up to the number specified in the order).
2. Is the order fully satisfied yet? If no, goto 1 until the order no longer crosses with anything on the other side of the order book.
3. Is the order fully satisfied? If no, the remainder of the order now **rests** on the book.
4. For each order we matched with, write the fact of the match (the **fill** / **execution**) to the tape.


Steps 1 through 4 are, essentially, atomic with regards to all orders on the stock exchange. You’re guaranteed to not have two orders interleave execution — only one order is incoming at one time. It is either fully processed (potentially with part of it coming to rest on the book) or canceled before the next incoming order is processed.


## The Tape(s)


Markets are by nature distributed systems. To simplify all participants having the same view on reality (or as close to that as possible), they typically have a relatively slow way to get a current snapshot of the order book and relatively fast ways to get a stream of deltas to the order book as they come in — new orders, order cancellations, executions, etc. That stream is called a tape, because way back in the day it was physically printed on a ticker tape.


The Stockfighter exchange implementation exposes a few tapes to users: one of all executions (with a new message for each execution) and one of all quotes (with a new quote — containing an at-a-glance view of the order book state and last trade — each time someone either sends in or cancels an order).


Stockfighter also does not, at this point in time, directly expose orders/cancels via a publicly visible tape. This is a considered game design decision for Chapter 1. I’m calling this out here as “A significant way we deviate from reality”, which we’ll do any time we need to to make the game more fun for players.


## Order Types


We discussed the simplest and most common order type, limit orders, above. There are *many* order types supported by exchanges in the real world, all of them offering some benefit to at least some exchange participant. (Exchanges make money on every consummated trade, and they’re in vicious competition with each other for business, so they generally want to innovate on order types which offer particular customers things those customers want. They are constrained by the law and “not advantaging any participant overmuch against other participants, because that would chase the disadvantaged participants to a competitor.”)


Stockfighter supports three order types besides limit orders:


**Immediate-or-cancel (IOC) orders**: Exactly like a limit order, except if there is a part of the order which is not filled, that part is canceled rather than resting on the book.


**Fill-or-kill (FOK) orders**: Exactly like an immediate-or-cancel order, with one wrinkle: if the order can’t be fully filled for all shares it requests, it is canceled without causing *any* executions. (On real exchanges, this is sometimes described as “immediate-or-cancel all-or-nothing”, or “IOC AON.”)


**Market orders**: Market orders are what mom-and-pop retail investors use: they include a direction (buy or sell) and a quantity of shares to transact, but no price. They execute instantly and take whatever price the order book offers, again matching the most favorable prices first.


## Let’s Talk Liquidity


One of the fundamental problems with buying/selling *anything at all* is that one is not guaranteed to have a counterparty ready at any given moment. This makes it difficult to buy/sell your thing and forces you to take a worse price if you want certainty of execution.


Consider houses. Lining up a buyer for your house takes, typically, weeks or months of work. If you needed to sell your house not at “some time in the vaguely defined future” but “within the next five minutes”, you would have to offer the house at a *tremendous* discount to its market value. Similarly, if you wanted to buy a house immediately, you would probably need to pay a tremendous premium.


The housing market is said to be **illiquid**, or lacking in **liquidity**: you cannot conveniently transform houses into money or money into houses quickly without losing a lot of value.


The stock market is *incredibly liquid*: for any stock listed on an exchange, you can buy almost any quantity and sell almost any quantity, at any time the market is in session. No negotiation, no red tape, no uncertainty. Click a button on your computer and *bam* trade done.


This property of stock markets is optional, tremendously useful for some participants, and **very not free**. Liquidity is a thing that can be sold, and much of the money on Wall Street is made by selling it. Let’s walk you through how it happens, but first, a bit of an explanation about why people actually want to buy it.


There exists a tradeoff between price and execution certainty. If you send in a limit order, there exists the possibility that it will not execute. This probability is higher if the order wouldn’t cross with the current state of the order book, but even if it looks like it will, the market might well change before your order arrives at the exchange. Even if it *looks* like someone is willing to sell Google at $750 a share, if you send in a limit order for 100 shares at $750, you have *no guarantee* that you actually get any Google shares.


If you send in a market order for Google shares, you’re guaranteed to get all of them that you want (subject to the availability of them at any price), but you give up certainty about the exact price you get.


That’s a reasonable tradeoff for many market participants! A family doing some casual trades in their retirement account wanting to buy 20 Google shares (~$15,000 worth) doesn’t really care about the exact price they get. If Google moves by a few cents in the interim, that costs them only a few dollars of value. Oh well — they just want to have the Google, for whatever investing or speculative reason they had for placing the trade originally.


A professional trader, who cared a lot about getting the best possible price and was therefore willing to pay attention to the market all day, might say “Well, Google routinely swings around a bit, so I’ll put in an order at $748 and see what happens.” If they’re buying 10,000 shares at a time, that saves a meaningful amount of money… if that order gets hit at all. If they were wrong, then they don’t get their Googles… or they have to adjust their orders mid-day. That’s fine — executing trades is *their job*.


## Market Makers And The Spread


So the stock market exists to connect Andy and Beth. What happens if Andy and Beth want to trade a stock but are not both in the market at the same time? Enter the **market maker**. Once upon a time, market makers were designated individuals (called “specialists”), but these days it is often just “anyone running a market making strategy.”


A market maker’s job is TTTaaS: Teleportation and Time Travel as a Service. Suppose Andy wants to buy at 9:15 AM and Beth wants to sell at 9:30 AM. If neither Andy nor Beth are willing to wait, no trade would happen, and Andy, Beth, and the larger economy are all sad.


A market maker says “This is solvable. I sell Andy the stock he wants to buy at 9:15 AM. I then buy the stock back from Beth at 9:30 AM. I charge them slightly different prices and make a modest profit for holding onto the risk for 15 minutes. Then I do this **a lot**.”


(That’s the time-travel aspect. The teleportation aspect involves cross-venue arbitrage. Too complicated for today, but know that it exists.)


The difference between the price a market maker is willing to buy at and the price they are willing to sell at is called **the spread**. If you put in a market order, you’re guaranteed to “cross the spread”, effectively paying the market maker a small toll for guaranteed instant execution. (If you don’t want to cross the spread, just put in a limit order such that it rests on the book rather than immediately crosses, and hope that that limit order gets hit — again, no guarantees there.)


## How Wide Is The Spread?


The width of the spread — the price of liquidity — is set by the market, not the exchange. It arises from the frothy interactions of thousands of participants firing orders at the exchange.


In the bad old days before computers, stocks were priced in eighths of a dollar (multiples of 12.5 cents). The spread could never be any less than 12.5 cents, which is a substantial chunk of the transaction value for many stocks.


Additionally, specialists colluded with each other extensively, such that they agreed to quote only “odd eighths”, essentially widening the spread to an entire quarter. They collected a one quarter tax on every share of stock which traded, every time it traded, for *decades*. Specialists loved this system. Investors, not so much — somebody pays that tax.


These days the markets are decimalized — stocks trade in increments of a penny. (They are not allowed to trade in increments smaller than a penny, by federal regulation. This is unfortunate, because “the minimum spread is 0.01 dollars” is not any more rational than “the minimum spread is 0.125 dollars” — if someone is willing to provide liquidity for cheaper, we should encourage that.) Additionally, since anyone can trade from any computer hooked to the exchange, human specialists have largely been outcompeted by algorithmic traders — computers which place orders all day long trying to be the one market maker of hundreds who successfully captures that penny.


You may have heard about High Frequency Trading (HFT). There is no hard-and-fast definition of it. You should understand that most HFT firms are just executing market making strategies *really, really quickly* while in vicious competition with traditional market makers (whom they utterly crush, because computers are better at doing math fast than people are) and other HFT firms. This is a huge benefit to most people attempting to transact in a stock, because a) no one is forced to do business with the market makers (again, just use a limit order and accept the risk of not executing if you don’t want to pay for their liquidity-providing services) and b) the presence of HFTs competes the spread down to a penny in most highly-traded stocks. Since they’re legally prohibited from competing with price below the penny increment, they then have to compete on speed, and *that* competition has intensified to the point that HFTs routinely run up against “the speed of light” as an *annoying constraint on their engineering teams*.


## What Is The Risk In Being A Market Maker?


Your job is teleportation and time travel. Bad news: teleportation and time travel aren’t *actually* possible. This means you take on **risk**.


Consider the case where Andy wants to buy at 9:15 AM and Beth wants to sell at 9:30 AM. The market maker is *not aware of* Andy or Beth’s plans and *cannot be certain they will not change*. The market maker also *cannot know* what happens between 9:15 AM and 9:30 AM. The stock that they sold to Andy for $40 a share could soar in value to $50 a share when Beth wants to sell, costing them a loss of $10 a share.


This risk is the economic justification for liquidity having a price associated with it. If it were as simple as accepting “Hey, hold onto this stock for 15 minutes and then someone will ask for it — you have no price risk at all”, then it would cost as much as a coat check (“We’ll just throw that in for free”), and not “a small amount on every transaction” which turns into “billions of dollars over the course of the year.”


(You might sensibly be curious as to the impact on individual investors. Fair enough. I’m a small retail investor who trades very occasionally. I ran the math and, on my portfolio of ~$80,000, I’ve paid approximately $6 to market makers over the last ten years. This compares to e.g. $500 or so in commissions to my discount brokerage.)


## How Do You Manage Risk As A Market Maker?


This is the entire ball game. At the most basic level, you want to limit the amount of inventory you take in any stock in either direction and charge an appropriate price for liquidity.


Sophisticated market makers use statistical techniques, simulations, etc to try to guess the near-term future behavior of the market, using this to determine how much inventory they’re willing to hold at any given time and what prices to charge.


In the real world, market makers use a variety of other instruments to hedge their inventory risk with respect to any given stock. In the early levels of Stockfighter, we intentionally restrict you to thinking about only a single stock at a time (for simplicity), so your main levers are canceling your existing orders, adding new orders to the book at different price levels, and (in extremis) unloading your position by transacting with orders on the book placed by someone else.


(Probably another market maker. Fun fact: most orders resting on the orderbook at any given time, both in Stockfighter and in real life, are there because a market maker put them there. This was one of my fun takeaways from the research phase for this project: liquidity really *does* exist primarily because market makers are actively adding it.)


## The Simplest Market Maker That Can Possibly Work


1) Guess a current fair price for the stock. (The midpoint of the current quote might be a good first approximation, or perhaps the last price a trade happened at.)


2) Put that price on a number line.


3) Draw three equidistant ticks to the left of that price and three to the right. The distance between the ticks is up to you — you could use a set interval (say, 5 cents) or something sized relative to the price of the stock (say, 0.5% of the midpoint price).


4) Send orders into the exchange such that you currently have orders to buy or sell at each of those ticks. Sizing is up to you: the simplest thing that can possibly work is just “pick a number and use it everywhere.”


5) Wait.


6) Did someone transact with you? Great! Cancel all your outstanding orders. Now, do it all again.


7) Keep doing this until you make a squazillion dollars.


This is about as easy to implement as it looks. (My first market maker clocked in at about 144 lines of Ruby.)


Shockingly, if you’re the only market maker in the market, this will *actually work* most of the time. The monopoly supplier of liquidity makes money virtually by definition, particularly when the market does not quickly move in one direction and stay there.


In real life, you’re **not** the only market maker in the market, and you’re liable to get crushed if you try this, as you’re going to be systematically outcompeted for trades which are safe and you’ll systematically undercharge for trades which involve risk. Also, in real life, other people can look at how you choose to do business… and they have a lot of experience picking the pockets of naive market makers. Don’t say I didn’t warn you.


## Doing This In Stockfighter


Now that you know in broad strokes how to write a market maker, you’re probably wondering “OK, but how does one *actually do that?*”


In real life, you’d post about $30,000 of capital (bare minimum) with a broker, get access to their API, and then try not to bankrupt yourself while you learn the ropes. I can’t recommend most developers actually try this.


In Stockfighter, your fictional employer in the fictional game will give you lots of fictional money, backed by a reset button should you ever run out. We give you access to a REST API, which has everything you need to send in orders, get the status of orders, get quotes for stocks, and what have you. You can connect to the various tapes provided by the exchange over web sockets, but this isn’t necessary for our earlier levels — the vast majority of players will just write a for loop and poll every few seconds for updates.


This would be problematic if you were competing on speed with a HFT firm, but not only are our bots written in Ruby and not designed to be speed demons, we intentionally hobble them in the early levels to make it an inviting experience for programmers new to trading. (Our stock market maker bot is also literally the first trading program I ever wrote and close to the dumbest a market maker can possibly be, so clocking it shouldn’t be that difficult.)


In real life, most exchanges expose a quirky protocol called [FIX](http://www.fixtradingcommunity.org/). Stockfighter will support FIX in a later release, but for our Chapter 1 release, we have a simplified REST API with JSON. You’ll end up doing things like:


POST /venues/FOOEX/stocks/BAR/orders


with the order:


and get a response back like:


Take it from this web developer — you can be up and running on this API in a matter of minutes.


After you’re able to work with the API, you just have to use that to solve whatever challenge the level throws at you. One challenge might be “Here’s a venue (stock exchange) where a particular stock is traded by many bots, one of whom is running a poorly considered market making strategy. Implement a better one and make $X before time runs out.”


Our desired difficulty curve: our first level is a cakewalk if you’ve ever programmed with an API before. Our first few levels after that are solvable in an hour or so of donking around with the API. They range in conceptual difficulty from “A motivated CS102 student should be able to do this in a fairly straightforward fashion” to “You’ll feel pretty proud of yourself once the code works.”


We also have later, more challenging levels, calibrated to be a fun evening project for a developer skilled enough to make it to them. Many of the solutions would make a good conference talk: here are the dead ends I tried, here is the insight those gave me, here is the approach that ultimately worked, and here are the fun implementation details.


## Affordances We Built To Make This Easy


Every public endpoint of our API is documented. This includes code samples, sample responses, commentary on how one would actually use that endpoint in an application, and an in-page API explorer so you can run ad-hoc queries without needing to write any code. This is courtesy of [readme.io](https://readme.io), which is one of my favorite new SaaS apps.


We’re not releasing the API documentation publicly until the game formally launches, to avoid giving anyone the ability to pre-write clients for the game. (Though that earlier sample probably gives you enough to predict most of the API… hmm… well, good on you if you can do it from that.)


We will not be releasing first-party libraries for the API at launch, to give the community the opportunity to build them for yourselves. (“Can I write a e.g. Python library for the API and throw it up on Github?” Heck yes. “Can I use a client library someone else wrote to let me focus on the fun work involved in solving my levels?” I’d personally be very disappointed in an engineer who, in 2015, defaulted to scratchbuilding their own clients for every API they consumed. Starfighter loves OSS and the OSS culture. Go nuts.)


You can, of course, use any language capable of driving a REST API to play these levels. Or curl, for that matter. (To quote Chris Rock: “You can drive a car with your feet if you want to, but that doesn’t make it a good idea.” Memo to self: add a Drives Car With Feet badge to the game.)


## A Non-Trivial Sample Application


We built an in-browser trading application in React, which you’ll get instant access to once you open one of our trading levels. This interface is essentially what a day-trader would be working with… if their brokerage of choice made some pretty poor UX decisions because their dev team was one guy writing his first React app.


Wait, did I say that out loud? What I meant to say was: we produced an entire web-based trading interface, driven 100% through our API, which allows you to see the API actually getting worked with.


It has virtually complete coverage of our API, by necessity, so if you need to know how to e.g. interact with a web socket you can just right-click and View Source. We don’t “cheat” and do anything to make the API easier to consume for our own applications like e.g. adding private endpoints which pre-digest information for the client.


(Most of our bots don’t cheat, either — they interact with the stock exchange the same way your applications do, and have no privileged access to e.g. market data. There exist exceptions to this general rule, in particular, in Chapter 1 level 6. I won’t spoil it for you.)


## Further Reading


If you’re having trouble visualizing what an order book looks like, particularly as it gets mutated in response to incoming orders, I recommend taking a look at Chris Stucchio’s examples in [these](https://www.chrisstucchio.com/blog/2012/hft_apology.html) [three](https://www.chrisstucchio.com/blog/2012/hft_apology2.html) [essays](https://www.chrisstucchio.com/blog/2012/hft_whats_broken.html). They’re in the context of an argument that HFT is not as abusive as the engineering community often believes.


I happen to think that Chris has the right of that argument, but even if you don’t, read his examples closely, because Chris has a view of trade execution which can be reconciled with reality and Michael Lewis (of Flash Boys) does not, as you will quickly discover if you try to actually write out what Lewis says is happening in pseudo-code.


## What Happens If I Can Make A Market Maker?


In the process of learning to build a market maker, you’ll both demonstrate substantial practical engineering skills (e.g. working with a novel API, dealing with state, modeling a data structure that probably isn’t built into your language already, etc), learn some fun new things, and get a whirlwind tour of common Wall Street activities.


Each level of Stockfighter introduces you to a challenge which builds on the last, in the context of a narrative taking place in a simulated world. You can’t possibly screw up anything so badly that the reset button won’t fix it, and no money is actually on the line.


For example, after you have successfully built a toy market maker, we might give you a new level where that market maker is exposed to harsher conditions and tell you to adapt to them. (Fun intellectual exercise: read the section on risk and try to predict what features of a trading environment would make a market maker’s job harder.)


Market makers are among the first of many concepts Stockfighter will teach you. Our intention is that many generalist programmers, including folks who have never had the opportunity to do anything more interesting than a standard CRUD app, will discover (or develop) depths of engineering skill they didn’t know they had. That’s awesome regardless of what happens.


Our games are free to players. Most players will be playing Stockfighter simply because play is fun. We’ll always support that, but we want to support the engineering community in more direct ways as well. If you find that you’re a better engineer than your day job needs you to be, we might very well be able to find a job more suited to your abilities. Our business is introducing talented engineers to clients who want to hire them. They pay us if they hire you. We’ll have about 15 clients signed at launch, ranging from Wall Street institutions (“Want to learn how to do this when it *isn’t* a toy?”) to non-profits to startups with interesting engineering problems.


The market doesn’t believe there exist enough engineers who thrive when given a novel, hard problem. We think you’re out there, in multitudes, and we think there exist many other engineers who are on the cusp of greatness. We want to meet you and geek out together.


See you in the game in the near future. If you’d like to make sure you hear when we launch, and you’re not already on our email list, [fix that here](http://www.starfighters.io).
