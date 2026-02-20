---
title: "Designing And Building Stockfighter, Our Programming Game"
date: 2015-08-20
url: https://www.kalzumeus.com/2015/08/20/designing-and-building-stockfighter-our-programming-game/
slug: designing-and-building-stockfighter-our-programming-game
word_count: 7961
---


Stockfighter, Starfighter’s first programming game, is presently in private beta. We’re moving to dark launch (to clients and handpicked vict^H^H^H friends) next week. We’ll launch publicly immediately after the servers give us signs that they won’t go down in a roaring fire. I’d anticipate within 3 weeks of today, but you know how engineering schedules go.


(Starfighter is a company which is trying to solve engineering hiring. We make games/puzzles which one plays by programming. Think Minecraft meets Legos meets World of Warcraft meets a CS class — we’re giving people a fun little world to play in by programming with some pre-planted goals and then seeing what emerges. More on [our website](http://www.starfighters.io) or [here](https://www.kalzumeus.com/2015/03/09/announcing-starfighter/) if you’re curious.)


I wanted to talk a little about what we’ve built and why, both out of general interest and because I know some folks want some direction for how to prepare. I’m going to take the liberty of not spoiling actual levels, because discovery of them is a lot of fun, but will focus on the setting, infrastructure, and design goal.


# Picking The Fiction / Setting


We picked “cops and robbers on Wall Street” for the setting of our first game — making money by legitimate means (like charging for liquidity) and illegitimate means (like stealing it). Although my co-founders Thomas and Erin have done substantial work with securing real stock exchanges over their career, I have no particular background in finance. We’re also primarily interested in general engineering skills rather than e.g. quantitative trading specifically. So why start in finance?


Basically, rotating the player around a series of Wall Street institutions allowed us carte blanche to hang virtually any engineering challenge off a more-or-less cohesive narrative. Trading systems touch low-level coding, networking (all seven layers of hello OSI Model), APIs, end-user UI, databases, embedded systems, enterprise web frameworks, cutting-edge programming language research, Big Data, state management, etc etc.


The fiction also gives us excuses to be naughty, which is something we think many programmers are attracted to. Many CTFs (games which practice security skills) cast the player as a hacker breaking into something, which works to a point. You can get the same adversarial frisson in legal fashions on Wall Street, often by building things rather than strictly by breaking them. (Though, ahem, not all of the things our levels have you build are, strictly speaking, legal. That’s also part of the fun. The fact that you’re being naughty vis-a-vis institutions which are not well-liked in the programming community is also useful to us from a player-motivation perspective. I hope people will, in the course of robbing them blind, actually learn what major Wall Street institutions do for a living and come to a more nuanced understanding of their position in society.)


There are natural in-universe tie-ins for both player-versus-player contests (which we won’t ship at launch, but soonish) and for dealing directly with computer-controlled opponents. Wall Street is, after all, one big computer-controlled opponent.


Some folks have been surprised that our game is not more, you know, game-y. Couldn’t we have made e.g. an RPG or strategy game or similar? Yes, certainly, but we had some concerns of a social nature.


Cards on the table: I used to run a World of Warcraft raid guild before I went into business. (Business has less dragons and better loot.) My co-founders, on the other hand, feel about gaming approximately the way I feel about ballet: it’s great that it exists in the world and I’m glad people find enjoyment in it, but it isn’t for me. This view is shared by many talented engineers and would-be engineers.


As of 2015, we don’t gate entrance to the tech industry based on demonstrable enthusiasm for ballet. It is important to our founders that the industry is not gated by demonstrable enthusiasm for gaming-qua-gaming or related geek cultural signifiers, like e.g. a fantasy or sci-fi setting.


Starfighter doesn’t ever intend to build gates (gates *close*; that’s what they are for). We dynamite gates.


# Tech Trees


Stockfighter is divided into tech trees. A tech tree presents itself to the player as a series of challenges linked by narrative progression and pedagogy. Learn a new concept; beat a level; get introduced to new levels where you can build upon what you build and what you learned. (Fun game design challenge: how do we not bust you back to a blank editor between every level while simultaneously not making it feel like you’ve “already done this.”)


In architectural terms, a tech tree typically requires additional back-end engineering work on top of our general platform, and also some front-end engineering to make it playable in the browser. (About which, more later.)


We’re shipping two tech trees at launch: **automated trading** and **emulators and compilers**. My co-founder Erin [discussed writing our emulator](http://sockpuppet.org/blog/2015/07/13/starfighter/) already, so I’ll be covering mostly the trading tree today.


# Automated Trading


Automated trading is the classic problem people think of when they hear Wall Street. It’s topical: Flash Boys (a book about high-frequency trading) was on the New York Times bestseller list. It delivers on the “make a squazillion dollars using only your wits” fantasy for the game. (“Fantasy” is, in this sense, a term of art from game development: much like someone writing a novel or screenplay, a game designer wants to have intentional control over the player’s emotional state. If you’d like to read more about this, Raph Koster’s A Theory of Fun comes highly recommended.)


In Stockfighter’s automated trading tree, each level gives you a new scenario (randomly generated and assigned to a wee little copy of the world accessible only by you) and a plausible set of objectives. You achieve the objectives by driving our REST API, using any language/stack/tooling you’re comfortable with.


What we built to support trading:

- a limit order book, written in Go
- a stock exchange front-ended by a REST API, written in Go
- a settlement system, written in Go
- a world simulation for a universe of fictitious companies, written in Ruby
- several automated traders, written in Ruby
- a game master server, exposing a REST API, written in Go
- an internal message bus, about which more later
- a blotter interface (similar to a retail trader’s web application — think “what I see when I sign into eTrade”) written in React and consuming the exchange and game master APIs


I wrote most of this myself because Thomas and Erin were doing the technically ambitious parts of Stockfighter. No, really, compared to their stuff, scratch-building a stock exchange is actually fairly straightforward.


# Writing A Stock Exchange


My primary stack since 2010 has been Ruby on Rails. I love Rails, and we use it for our user-facing web application, but Rails is not the right choice to build a stock exchange. The biggest reason was concerns about raw performance.


Stockfighter doesn’t do “high-frequency trading” like Wall Street understands that term, although it does support (and have you actually *do*) what many lay people understand HFT to mean.


The difference is one of degree. Many lay people basically think that any algorithm placing orders is HFT. There are many prop shops — i.e. hybrid tech/finance companies using the company’s money to trade algorithmically — which have a timescale on the order of days rather than on the order of nanoseconds. Their individual orders (and the logic behind them) might be faster than a human can reasonably follow, but that’s still not HFT. (Acid test: if you have never worried about the speed of light between your systems, you’re not doing HFT. The [amateur trading from London on the Chicago Mercantile Exchange using MS-Freaking-Excel](http://www.bloombergview.com/articles/2015-04-21/guy-trading-at-home-caused-the-flash-crash) to place trades? Not HFT, guys.)


We abstract the notion of time quite a bit, but it was obvious that each exchange was going to have to be able to process thousands of orders a real-life second.


This would be… challenging in Rails. Low-complexity operations which do need to write to the DB typically hit about 300ms in my Rails experience. (Better, more experienced teams like the folks at Basecamp have gotten it to 50~100 ms in typical cases.) We would need to do thousands of them a second and, unlike a typical web application, we a) have a bursty, write-heavy, uncacheable load by nature and b) have some severe constraints with regards to requests affecting each other.


Why? Well, it is a stock exchange. The order book — the list of how many shares at what prices are currently available to be bought and sold — is (conceptually) a singleton sitting behind a global lock. (Per-exchange — Stockfighter will simulate thousands of exchanges simultaneously, but architecturally, it needed to consider the “Thousands of people hitting a single exchange at once” use case from the jump.) This is getting all the player and bot interaction. The matching engine has to be completely done with a particular order before starting processing of the next one.


We solved this in a roughly similar way to a real stock exchange: the order book is persisted entirely in memory, in Go.


Stockfighter is my first production system written in Go. The Google (et al) performance wizards have absolutely delivered. The language *screams* and, happily, it is possible for a mere mortal to actually ship a web server with it. (Note “server” but not application. More on that later.)


Incoming orders from the REST API or our internal message bus are passed to a single goroutine which manages ingress and egress to the order book. This goroutine writes the results of those orders to a series of tapes. A tape, physically, a buffered channel with a servicing go-routine. The tapes are then consumed by other parts of the systems to e.g. send execution notices to players/bots, update the quotes displayed by the API/UI, etc.


Our exchange is *blazingly fast*: we can process fairly complicated orders matching against a filled order book in on the order of 100 to 200 *nanoseconds*. Read operations are even faster. (I might eventually figure out some way to re-architect the exchange such that reads don’t touch the matching engine at all, but at present some of them do. Whoopsie.)


This is good — it allows players substantial latitude for experimentation with trading strategies (including ones which push the performance envelope), lets us run dozens or hundreds of bots per player, and keeps our infrastructure costs down to “less than a small fortune.” (We’re on EC2. At release, pending understanding how many users we have and what their typical behavior is, I anticipate that we’ll have a count-on-your-finger number of t2.micro instances for the stock exchanges.)


Getting this working was a bit of a beast. Our order book is represented internally as a red-black tree (Go implementation via [GoLLRB](https://github.com/petar/GoLLRB)). I had never actually used a red-black tree since finishing my CS degree. (Well, OK, they’re sitting down somewhere in MySQL or Postgres but I’ve never had to actually think about them before.) This is a preview of coming attractions for Stockfighter: even when we aren’t explicitly making tech decisions for pedagogic purposes, modeling the complexity of the stock market is a real engineering workout versus e.g. the typical CRUD application.


Bonus points: most players will, at some point, choose to represent the order book on their own machines. This is foundational to many trading strategies. If you want to golf cycles off to make your code faster, that will a) directly advantage you in later Stockfighter levels and b) be a fun opportunity to play with algorithms and data structures.


A quick case for a LLRB for the order book data structure: they tolerate arbitrary writes and deletes very well, are sorted, and let you do things like “Iterate over every price point on the tree from the low-price side and give me everything until you count up this many shares and *do it fast*.”


My main issue in this part of the development was managing concurrency. If I had cottoned onto the wisdom of the common Go pattern “Make a server object with one managing go-routine and have it tightly loop on a single channel of incoming requests” earlier, I probably would have a avoided a whole lot of deadlocks, crashes, and concurrency bugs caused by e.g. reading the order book for GET /venues/FOO/symbols/BAR at the same time a match was ongoing subsequent to someone POSTing a new order.


# Stock Exchange Simulations


There exists substantial prior art on funny-money stock exchange simulations. Most of them are cunning artifice — you’re not actually trading with another actor. When you put in an order, you receive the results suggested by a stock market simulation. Amalgamated Cat Food (ACF) is up today — you paid $45.32 for your shares! But you didn’t *buy them from anyone*. Your account just got incremented, but there is no corresponding sell anywhere. Your counterparty is a fiction.


There are excellent engineering reasons to do this and I won’t knock their decision, but Stockfighter had different goals.


Why? Well, a lot of the fun engineering problems in trading are caused by it actually *not* being reliably the case that you send in an order and it gets unproblematically matched at “the price.” **Markets are distributed systems.** The exchange’s view of reality and your trading system’s view of reality are, by necessity, separated by the great firewall known as “physics.” For maximum possible results, you have to be able to do things like accurately predict what the *future* state of the exchange is, because the order you’re composing right now will arrive in the *future* not the *present*, while being cognizant that *your present* view of the exchange’s state is actually the *exchange’s past.*


Sound hard? It is hard. You don’t have to worry about it for the first couple of levels… well, actually, let me take that back. We do not intentionally expose you to the speed of light as a limiting factor early in Stockfighter… but we can’t remove latency as being an actual limitation distributed systems have to overcome.


Here’s an example of how this manifests: I was very frustrated during development at one point, debugging a level I had written. The blotter interface was showing a quote with an ask for 500 shares available for $100. (You’ll pick up the market jargon quickly — an ask is an offer to sell a given quantity at a given price. If they want to buy, it’s called a bid.)


I sent in a market order for testing. A market order is a special order type which doesn’t specify a price — it says “I’ll pay literally anything, I just want guaranteed execution of this order *immediately.*” (Aside: Stockfighter will quickly teach players in a visceral fashion why Wall Street considers people who place market orders to be idiots. Use a limit order most of the time. If you need instant execution, use fill-or-kill or immediate-or-cancel with a suitably-generous-but-not-actually-unbounded price attached.)


My order came back saying that I had bought 0 shares. And the quote from the exchange now read “500 shares available at $120.”


*WHAT?!*


After a lot of spelunking, I figured out what happened: there was only one bot on the ask side of the order book during that level. That bot had an order resting on the book displayed on my screen. In the time between I hit the button and my order reaching the exchange, the bot had hit the REST API to cancel its order. Then my order arrived to an empty book, soaking up 0 shares. It was then canceled (because market orders are instantaneous). The bot then replaced its order, causing the exchange to issue a new quote, which made it back to my PC before I had time to blink. From my imperfectly attentive human perspective, it looked like the exchange and the bot were intentionally colluding to abuse me.


They’re not.


But that sort of interaction — orders resting on the book, cancels, timing issues, different views on reality, profiling incoming order flow (as reflected by the quotes or execution tapes) and using it to send in or cancel orders faster than the incoming flow can itself adjust, using executions from one exchange to drive decisions to send orders to another exchange, etc, are all *so fun* to play with. And to do that, you need other agents participating on the exchange with you, rather than the exchange being a single-player experience.


Enter the bots.


# Writing Bots


Since player-versus-player interaction causes a lot of social issues which we weren’t ready to design for for release, and since players are not reliably available to play a) at your skill level b) right-the-heck now, we knew we wanted AI to trade against for most levels. (Aside: We’ll support PVP in some levels of later chapters, for those players who enjoy it. If you just want to treat Stockfighter like an intellectual exercise and never have to worry about another human during your experience, that is a game mode we will always support.)


It fell upon me to write multiple trading algorithms. For context: I have an undergrad background in AI (enough to know that it’s largely not applicable to the problem at hand) and most of my investing experience was simply buying-and-holding rather than trading actively. (Aside: retail investors *should not trade actively.* If someone thinks Stockfighter has given them the confidence to try actively trading for real, I will bang my head into the wall several times and wonder how we can make the next chapter more clearly communicate how ROFLstomped one will be if one tries that.)


Luckily, the market has participants operating at all levels of skill. Markets are aggregation mechanisms for price signals, and they come to surprisingly sophisticated behavior even when composed out of relatively unsophisticated individual agents. As soon as we had multiple bots operating diverse strategies, we started to see fun emergent behavior.


An example, hopefully without spoiling too much: I did a technology preview of the game with a friend who has a Wall Street background. The only actual goal-oriented level in the game at the time was our tutorial, which just has you buy 100 shares to prove you’re mechanically capable of doing so.


(Aside: I could describe level 1 as “FizzBuzz for a REST API”, but we don’t. FizzBuzz is widely used to [quickly weed out non-programmers](http://blog.codinghorror.com/why-cant-programmers-program/) from engineering hiring processes, but the experience of being asked to do it is a little off-putting for experienced developers. Giving people an actual fun goal — demonstrate mastery over a new system! — allows us to covertly test core engineering skills without writing This Is A Test Of Core Engineering Skills at the top of the screen.)


Anyhow, my Wall Streeter friend sailed through the tutorial and asked what was next. I told him “Well, content-wise, I’ve got nothing. But you’re hooked up to a stock exchange and all the other participants are idiots. What do you think would be fun to do?” “How dumb are they?” “Pretty dumb.” “So dumb they would follow the stock all the way down to zero if someone was to manipulate it?” “Umm… I don’t know.” “Let’s see.”


Five minutes later, we had verified that unplanned interactions between bots who a) don’t collude, b) don’t know of the existence of each other aside from seeing the order book, and c) have no mental model of the player *can in fact* successfully model **sheer, unrestrained terror** if a player manipulates the market correctly.


We’ve found a small number of not-too-complicated bots to be the gift that keeps on giving for level design — remix them and tweak parameters and the behavior of “the market” is different on every playthrough but roughly configurable in advance. This made level development much, much less expensive than I had modeled it out as.


We’re shipping with six trading levels, but we’ll have Chapter 2 out the door with more, probably within a month or two of release, and we intend to continue shipping new chapters every 6~8 weeks, indefinitely.


Another fun thing consequence of being a games company: in real life, when the state of the art advances in trading algorithms, you throw out everything that was done before because it would now be predated heavily. Being predated is a victory condition for us — it means levels are winnable! As we get better at building trading algorithms internally and/or hire experts to do it for us, earlier dumber bots don’t end up as bitrot, they end up as valuable game content. For example, the bugged momentum following bots which were proximately at fault for the market cascade were too disruptive to keep in that level… but, well, they’re now a resource that one can deploy to a variety of purposes.


Even after we have very sophisticated market makers (if that is a new word for you, I promise, you’ll understand it by the end of level 3), our idiot market makers are still valuable content for people who are still learning the field.


# Simulating An Entire World Economy


Stockfighter’s trading levels are about *trading* rather than *investment*. It’s important that the markets dance to an internal logic, but it is less important that that logic be particularly complicated. We wanted the companies at issue to have plausible behavior — some do well, some do poorly, some are stable, some gyrate, and sometimes the entire market goes into bull or bear mode for uncertain reasons before unpredictably reversing. We’re not really concerned, though, with e.g. line-by-line analysis of the earnings report for Amalgamated Magitek Corporation.


So we faked it. I’m going to elide the details of the fakery here. Our order book and exchange server work like they have to work, so I’m happy to spill beans about implementation details. The world simulation, though, is “security sensitive” — if you understand the world simulation you can predict and influence the future. That’s an I-Win button for most of our trading levels.


“What if players reverse engineer your world simulation?” **Then I pin a freaking medal on that player** (and ask whether they’re happy in their current career).


I think you’ll be pleasantly surprised with some emergent features of the simulation.


At present, it’s totally opaque — the only thing you’ll learn about Amalgamated Magitek Corporation is what you surmise based on seeing a market for its shares develop organically out of the actions of various bots.


Some of the bots are performing market functions which are neutral with regards to the underlying, like a market maker. Some of the bots actually do care about AMC. Well, to the extent that a 200 line Ruby script can care about an earnings report.


It’s not perfectly realistic and isn’t designed to be.


For one, we abstract time heavily. It’s a lot more fun to play through one trading day every 5 seconds and thus get a year’s play done in a 30 minute session of watching your script run than it is for that to just represent the quiet post-bell lull in the morning on January 3rd.


For another, again for maximum fun, our simulated world is more volatile than the one we actually live in. The in-universe financial press would be an impossible job for someone who wasn’t actually manic depressive.


In the future, we’ll expose various elements of the simulation to players. For example, there is an in-universe Twitter. Seriously, that is an actual thing that exists. I pipe it to a text file and tail -f it as a debugging tool, because otherwise it is difficult to figure out whether e.g. the price is cratering because I inverted a comparison somewhere or the price is cratering because Amalgamated Magitek Corporation was hit with a terrorist attack.


The Magitek industry is, as they say, “politically exposed.” Plucky teenagers with outrageous hair hate them and blow up their buildings with disturbing regularity. They just have *no consideration* for the Imperial Pension Fund’s AMC holdings or the chaos that news will unleash on the markets.


(Aside: geek references are capped at about 5 to 10% of the stocks in the game — you’ll also see a lot of things like Red Tree Agriculture or Uganda Mining Inc. We also reference various things that only have value in a fictional universe, like unobtanium or Bitcoin.)


(Aside: I promise that’s the last Bitcoin joke I’ll make until we ship our cryptocurrency tech tree some months from now. Actually, no, I can’t promise that.)


Anyhow, we’ll expose the in-universe Twitter directly to players in a later chapter. You can try your hand at doing things like e.g. sentiment analysis or trading on news generated by the world simulation before other trades can react to it.


The best example yet of the flexibility this simulation gives us is in the 6th trading level. I won’t spoil the details here, but after I beat it the first time, I told Thomas and Erin “This level is why I signed on to this project.” It’s the capstone for the trading tree in Chapter 1.


A particular fact is inserted into the world simulation and bubbles up to the stock exchange. You’re asked to discover the fact. There are literally infinite ways to do it.


Players getting to level 6 are by construction pretty good at programming and will have learned enough about market microstructure to be effective at trading. Level 6 is, let me not mince words, *hard.* You have to synthesize what you’ve learned about market operations, about our particular implementation, and then stir in some special sauce of your own… and we give rather little direction on what that sauce needs to look like.


I expect that level to be very challenging, because it is *totally* out of left field, but it also rewards creativity. You can Big Data your way through it. You can Hadoop cluster your way through it. You can *probably* solve the hardest phase of it with an Excel spreadsheet. You can use Statistics 101 (if you figure out the right question to ask). You can even solve it *by eyeball* if you parse the right data and graph the right thing about it. I expect players to do all of these things, with substantial variation. I also expect the unexpected, in spades.


We can’t wait to see what you come up with.


# Level Design


Again, no spoiler on individual levels, but I’ll talk about what makes a good level from the perspective of Starfighter.


**Appropriate challenge progression**: Our desired curve is:

1. Early levels: Solvable by people learning to program with effort approaching an undergraduate lab session. Cakewalks for professional engineers.</p>
2. Middle Levels: Solvable by people who possess professional-grade engineering skills, even if they may not have professional-grade titles yet. Expect the level to require a bit of thought and execution quality but not to have much technical risk.
3. Later levels: Solvable by very skilled engineers, but requiring an investment of effort, and having a corresponding emotional payoff for it (a sense of mastery, learning new skills that you could reasonably take with you, etc).


I was asked how we difficulty curved our levels. My design process was to throw out a lot of real-world trading problems (thanks a million to our advisors from industry; all mistakes in interpretation are our fault alone), winnow to the ones which seemed most amenable to working on our system, and then arranging them in rough order of difficulty assuming the player takes the most straightforward route through the level. I then wrote ourselves a few levers for difficulty — for example, parameterization of the level goals (e.g. if it is too hard to make $1 million in a simulated year, edit a YAML file and now players only need $250k) and providing instructions/hints.


While we’re doing our technical burn-in, we’re also collecting feedback on whether we guessed right on difficulty levels.  We can titrate how difficult a level is in production by choosing between e.g. giving no instructions on the path forward, saying something like “The path forward is obliquely suggested by the API docs.”, giving in-universe hints in e.g. the level briefing, giving out-of-universe hints, and directly telling players “Here’s one way to do it; you produce code to that.”


Players can, naturally, also do this, which suggests that our earlier levels are likely to get easier over time as e.g. better tooling is available on Github or people post walkthroughs. That’s a natural and not-unhappy result from a game design perspective.


**Variety**: Starfighter is a company, not a one-off event or a mobile game. We expect to (eventually) have a relationship with players which is denominated in years, not minutes. Accordingly, we want to produce regular content updates with them feeling sufficiently distinct from each other that there is a reason to play.


**Variably difficulty**: We wanted players to be able to Choose Their Own Adventure. If you want to pick the most straightforward solution for a level which works, blast through it, and move on, go for it. If you want to golf your solution, go for it.


Some of the most fun I’ve ever had with another team’s CTF was on Stripe’s 3rd CTF, where automatic detection of e.g. program speed supported a thriving optimization metagame. An example: some players looked at a fly like “An O(N^2) loop which compares text word-for-word against a world list.” and eschewed the flyswatter “An O(N) loop which compares against a hash table.” in favor of an orbital ion cannon like “Pre-compile the dictionary into the executable as a trie or bloom filter.”


We have per-level leaderboards which give people a meaningful number to golf on, and additionally, we have discretion to (automatically or after human review) award additional badges for going above-and-beyond on a level. We’ll also do that outside of levels, too — I can imagine issuing badges for people who, e.g., write OSS clients for our API, submit documentation patches, responsibly report security issues, etc.


**Specified goals. Unspecified solutions.** A common pattern in CTF development is “Make a program which conforms to this toy interface.” A lot of the work on the player’s side involves understanding that interface (and, often, the undocumented quirks of it). The interface often dictates exactly what your algorithms/structures/general approach need to look like.


We prefer modeling the actual practice of engineering, where you build stuff not to satisfy an arbitrarily defined interface but to achieve some motivating goal. Figuring out what to actually build to achieve the goal is a substantial portion of the challenge of real engineering work — and a whole lot of fun! (Also, companies hiring engineers right now are often looking for folks who can, given an underspecified goal, successfully reduce it to working computer code.)


This lets us support multiple solutions trivially, if we pick goals which are sufficiently robust. Luckily, the Wall Street fiction gives us numerous options. I mean, when in doubt it’s “Here’s the world; make money.”, but things can be arbitrarily rich.


This also has some unplanned for benefits from our internal engineering perspective. The modal level orchestration for our trading levels is roughly ~50 lines of Ruby code. Most victory conditions can be *evaluated* in a function with less than 10 lines. (Level six? The most fun I’ve ever had which was judged by a single string comparison.)


# Level Orchestration


We have a GM server (“Game Master” is an RPG term): it a combination simulation of the world, judge, orchestrator of the non-player characters (bots), and opinionated producer of fun.


Our GM server is written in Go and exposes a REST API. (You could, in principle, play Stockfighter entirely through curl if someone told you what URLs to hit. That would be pretty spiffy. Tell me if you manage to do it.) This accepts commands like e.g. POST /levels/foobar, which creates a new instance of the foobar level.


GM’s level orchestration logic is actually kicked out to Ruby, mostly because I develop Ruby much faster than I develop Go and, since this code is less performance intensive than the stock exchange, we had some flexibility. Levels are plain-ol’ Ruby whose design was heavily influenced by Rails — convention over configuration, lots of reflection used to locate files given predictable naming schemes, etc. They also have a YAML configuration which allows us to adjust e.g. which bots are present in the level, what instructions are given to the player, etc.


The bots… well… every project which ships ships with one decision that you feel the need to say “Look, I know, I know, but it actually worked.” Our bots are all written in Ruby. The goroutine managing the level instance on the GM server periodically wakes up, opens a Ruby subprocess, unpickles the state of the world simulation and the bots, has the bots update themselves against the state of the exchange via the REST API, accepts the bots desired orders, makes them against the REST API, pickles the state of the simulation and the bots, and then sleeps until the entire process starts again in a few seconds.


Why? A combination of “That lets me write levels and bots in my best language”, “I wanted to ship in 2016” plus “If I did a slightly more obvious thing and kept all of our levels and bots constantly in memory rather than slicing them 500ms of the server’s attention every N seconds, then our memory requirements at launch would be measured in terabytes and go up from there.”


Why use Go for the server then, instead of e.g. Sinatra? Because Go’s concurrency story is much better than Ruby’s is.


# Front-End Engineering


A core design goal for Stockfighter is that it is quick to pick-up-and-play, right in the browser, without requiring one to have a complicated toolchain installed.


Why? First, from a strict conversion optimization perspective, I’d anticipate a heavy, heavy dropoff between signup and completing level 1 if my first instruction was “OK, get a fully-functioning C toolchain installed on your box. Now clone this repo.” or even “Download this Vagrant image.”


Second, this is *particularly* difficult for less-experienced engineers. They’re not the core of our business, not by a long-shot, but I want to support them to the extent possible. I want a CS101 classroom to be able to play Stockfighter together. Many practicing engineers don’t remember this, but a CS101 classroom finds installing e.g. a full Rails toolchain to be a *hard, frustrating, failure-filled experience.* (I’m a professional engineer using Rails for the last 8 years. If you gave me a blank Macbook and a day I could do install Rails… after a lot of Googling to check whether we still use rbenv and Bundler or if that changed since last week.)


So a hard requirement for both of our tech trees was that they be playable in the browser to start. After players are invested, they can get additional edge by working in their stack of choice locally, writing tools which sit on top of our systems, or even e.g. deploying code to EC2 or Heroku or what have you, but batteries had to be included out of the box.


Thomas and Erin build an entire in-browser C development toolchain which compiles down to assembly and then executes on a farm of emulated Arduino processors. I had the comparatively easier task of figuring out “What does the simplest version of automated trading that works look like?”


Answer: it’s manual trading! So we made a blotter interface — basically, a stripped-down retail day trader’s interface for monitoring the market, placing orders, and seeing executions. You can use the UI to poke at any of our levels and get a sense for what the “normal” behavior of the market is given that level’s load out of bots and stocks. You can also use it as a stepping stone for bootstrapping your first programs — there is no need to write e.g. code to poll whether your orders hit anything because we’ve already taken care of that for you, so all you need to do is focus on generating the right orders to send in. If you want, you can even totally replace the UI with your own web application — go nuts.


Another nuts option: if you feel confident in your trading abilities, it is at least theoretically possible to beat many of our trading levels the old fashioned way — by running the math in your head and keying in your orders faster than the other guy. This is hard mode, since the other guy is Ruby code, but given that we force him to sleep for 80~90% of every trading day it’s at least *possible.*


The UI also includes controls for level operation, like e.g. restarting the level if you get stuck.


It was obvious that given goals like “Make a million dollars!,” in the inevitable learning period you could quickly get yourself in an unwinnable state by e.g. losing 95% of your starting capital. The designed operation of our trading levels is “Play them, lose horribly, write a program, reset the level, run the program, have it crash with a bug, fix and re-run, lose modestly, adjust your approach, re-start the level, run the program, win.” (Folks have asked whether we’ll hold this against you. No, no, of course not. We log everything under the sun, but losing/restarting levels is planned. That capability is an advantage of doing this in a rich simulation as opposed to real life — you can go Knight Capital as many times as you want and no one loses their job!)


We did the UI in React, because it has a lot more going on than most CRUD apps.


DHH describes the sweet spot of my favorite stack (Rails-with-some-Javascript) as “documents with some dynamic sprinkles.” I really love that model, but it does not describe a trading interface. You have an incoming stream of events, many per second, updating part of the DOM, potentially hundreds of orders open whose state can mutate at any time and whose accurate display is important, and a variety of actions available to you at any time.


Obligatory learning curve aside, as this is my first React app, I’m loving React and the Flux architecture. (We use [Flummox](https://github.com/acdlite/flummox), which was — sadly — EOLed between us picking it and launching. I swear, all the jokes about JS frameworks are true. That said, of the available options it seemed to require the least boilerplate, which can be [further reduced with a sensible naming convention.](https://gist.github.com/patio11/b472ccb2df3e1fcce78c))


Our blotter interacts directly with the exchange API (unlike most retail trading applications, which interact with a brokerage which interacts with another party which interacts with the exchange). This was enormously useful as I was doing parallel development on both systems. Forcing me to write a fairly complicated application against our API burned out a lot of the usage niggles prior to them being exposed to players. (Oh, don’t worry, you’ll find plenty more.)


Requirements generated by the blotter, like “Polling for order status is just crazy after you have hundreds of them — we need some sort of pub/sub system accessible over a websocket.”, made the exchange better for a variety of trading applications.


Here’s an image, although it’s modestly more amusing when quotes are streaming in and things are updating constantly.


The big challenges for React development, aside from the learning curve, were state management when switching between levels (eventually solved by rethinking our store design) and dealing with lots and lots of UI repainting.


At one point I was playing a level with a hundred bots. Each of those bots sent in about a thousand orders a minute. Each order changes the quote for the stock, causing a separate websocket message. Each websocket message would cause my entire table of orders to refresh.


100,000 refreshes of a table with a thousand elements in a minute will, pretty reliably, melt your poor little Macbook.


We eventually solved this by using built-in React features like shouldComponentUpdate (basically, we got very detail-oriented regarding the performance-sensitive components like orders and quotes, made sure they would always render the same given the same prop and states, and then canceled the render if their prop/states were deep-equals equal) and using keys on child objects.


Fun fact about child keys: even if every child is itself immutable, if you choose keys poorly (like, say, simply making a unique ID on creation of the child UI element), updating a single order out of an in-memory list of 1,000 will cause the entire table to refresh, and if your child key is different than the key for the same element in the last version of the table, React’s magic DOM-diffing technology does not save your bacon. Instead, your bacon sizzles amicably on your Macbook.


After I got my head around that and started picking better child keys (appending the ID and modified timestamp is all you really need — same as Rails Russian-doll caching), our UI became *quite* snappy. I log into our staging environment (Amazon’s Oregon data center) from Tokyo and I can’t tell it’s not on localhost… except when the speed of light decides to play tricks on me.


# Supporting Technology


Our web application (signup/login/leaderboards/etc) is a bog-standard Rails 4 app. There is very little technically interesting about it, but it works and was quick to write — this is exactly Rails’ sweet spot.


You know whose sweet spot it is decidedly not? Go’s. I tried, I really did, but it would be very difficult to recommend Go for a web application at the moment.


The ORM we ended up using for e.g. our settlement service, [Gorm](https://github.com/jinzhu/gorm), is not anywhere near the level of maturity of ActiveRecord, and to get its (valuable!) feature set you have to tolerate a) throwing out most of the benefits of using a type-safe language and b) programming bugs which can cause statements which certainly look like they should generate SQL queries to just *silently not generate SQL queries*. In general, working with the database has been so painful in Go that I have been instead either a) hitting a REST endpoint on an internal API to have Rails do the DB access then return formatted JSON (which Go can actually consume fairly decently) or b) throwing the data at NSQ.


I have fallen in love with [NSQ](http://nsq.io/), an enterprise message bus for people who don’t ever want to have an enterprise message bus. The elevator pitch for it: write a textual message, tag it with a topic, and send it to your local NSQ daemon. On some other machine that doesn’t even know you exist, another program says “Apropos of nothing I’m a member of the $FOO channel and want a copy of $BAR topic messages which have not been processed by the $FOO channel yet. $FOO doesn’t exist yet? It does now. Hit me.” NSQ handles all the magic to make that happen.


We use it for *everything*. Rails controllers need a way to log analytics-style events? Pipe it to NSQ — we’ll make a decision on an analytics-provider later and, in the meanwhile, we’ll have [nsq_to_s3](https://github.com/chrusty/nsq-to-s3) just save them for us. Our settlement system needs executions from the stock exchange? Open a settlement channel on the executions topic; done. Executions *also* need to be logged somewhere? Sure, open a dumpToLog channel on that topic and use the provided nsq_to_file utility; done. We want a per-player list of historical UI actions taken by levels? Sure, no worries, have the GM server write to the levelActions topic, open a peristToDB channel on it, and use nsq_to_http to have those hit an internal API on our Rails app which takes care of that.


The best part? When you just assume the existence of NSQ everywhere, you don’t have to think about e.g. dropping more instances of a particular service on your infrastructure, routing requests, etc etc. You just fire-and-forget at the bus.


Actually, that isn’t *actually* the best part about NSQ. The best part is Stockfighter ships with about seven microservices and having them all understand every HTTP endpoint available would have been unwieldly. Instead, we standardized on a small set of common JSON object representations and then the topic names. This lets us do things like e.g. have our Arduino emulator slurp up quotes from the stock exchange simply by saying “Hey I’d like quotes, too” without the stock exchange even knowing that an Arduino *is a thing*.


For our services which communicate over HTTP, like e.g. the exchanges, we have to be a little smarter about routing because we can’t treat NSQ as the Magic Oracle Of Making Sure Messages Get Delivered. The short version of that story is [consul.io](https://consul.io), the longer version is a full infrastructure post because it gets complicated.


# Documentation


We’ve been using [readme.io](https://readme.io) for our player-facing documentation. I haven’t pushed our docs live yet (spoilers abound) but I *love* this service.

- The docs come out looking very pretty without me having to do any more CSS munging.
- The UX of the docs approaches that of e.g. a Stripe or Twilio rather than a Markdown file.
- There is an in-browser API explorer, so you can (if you want) copy/paste in your API key and, from the page describing e.g. our POST /venue/FOO/symbol/BAR/order endpoint, actually post a live order against one of our running stock exchanges. It displays the HTTP headers and full response in-line.


Readme.io is ridiculously fun. We’ll push the docs live to it when the game launches publicly.


# Further Reading About Trading


We’ve promised players a reading list to help with understanding Wall Street for generalist developers. Here’s a brief tour of my Amazon history over the last several months:

- [Flash Boys](http://www.amazon.com/Flash-Boys-Wall-Street-Revolt-ebook/dp/B00HVJB4VM/), Michael Lewis: I find this book impossible to avoid in a discussion of automated trading and yet difficult to recommend. Lewis is an exceptionally talented writer. I think many Starfighter players will come away from some of our levels saying “Michael Lewis, I have attempted to actually do the thing you said that the bad guys did, and that is, as a matter of engineering reality, *actually impossible.*” That said we’re totally ripping some levels off of his (highly entertaining) storytelling here. I mean, they named a computer program after a Greek god. How can we *not* make that into a level.
- [Flash Boys: Not So Fast](http://www.amazon.com/gp/product/B00P0QI2M2): A *much more lucid* take on HFT, by someone whose paycheck depended on being able to turn it into actual engineering artifacts.
- [Dark Pools: The Rise of the Machine Traders and the Rigging of the U.S. Stock Market](http://www.amazon.com/Dark-Pools-Machine-Traders-Rigging-ebook/dp/B006OFHLG6/), Scott Patterson: If the title doesn’t give the game away, spoiler alert: Patterson probably doesn’t consider “more engineers able to do algorithmic trading” to be a victory for truth and justice. (Of course it is! At the very least, consider it self-defense training.) That said, unlike Flash Boys, the discussion of issues/attacks strikes me (and our advisors) as being more tightly grounded in consensus reality. This book also includes an *excellent* history of the development of computerized exchanges in the US from about the 90s through today. It was particularly wild when I realized that our cute little toy hosted on a t2.micro was a $X0 million or $Y00 million engineering project back in living memory.
- I hesitate to recommend it based on the price, but if you want to pursue this topic *professionally* after Stockfighter, the Bible at Thomas’ last company was [Trading and Exchanges: Market Microstructure for Practitioners](http://www.amazon.com/Trading-Exchanges-Microstructure-Practitioners-Association-ebook/dp/B003ZSHIPE/).


That’s all I’ve got for today. Back into the code cave for us. We’ll see you in a few weeks!
