---
title: "App Store Payments Will Have Increased Competition"
date: 2021-08-27
url: https://www.kalzumeus.com/2021/08/27/app-store-payment-competition/
slug: app-store-payment-competition
word_count: 1983
---


Late on Thursday, Apple announced some [refinements](https://www.apple.com/newsroom/2021/08/apple-us-developers-agree-to-app-store-updates/) to their App Store policies. The most important one is about so-called “steering”, which is the practice of letting customers know about out-of-app options for transacting with them. I couldn’t not write about the trifecta of payments, platform strategy, and video games. (Disclaimer: while I work at Stripe, these are my own opinions.)


**The bottom line:** This is likely to be important for app developers. I think people underappreciate the magnitude of the likely impact due to the incrementality of it. It *is not* what developers have asked for, which is the ability to pitch users *within the app itself* on consummating payments out-of-band, but it *also is not* simply a return to the status quo ante to this summer, when Apple announced it would rigorously enforce guidance against steering transactions off-platform.


To appreciate why, remember that a large share ([60% or so](https://www.gamesindustry.biz/articles/2021-05-19-62-percent-of-all-app-store-revenue-is-generated-from-game-transactions)) of revenue on the App Store is from games, and game developers are in the business of incentivizing users to take small incremental actions within a play session. Sometimes those incremental actions involve e.g. learning the UI of your [princess saving application](https://lostgarden.home.blog/2008/10/27/the-princess-rescuing-application-slides/), sometimes they advance the plot, and sometimes they directly achieve business goals for the developer.


Consider MiHoYo’s [Genshin Impact](https://genshin.mihoyo.com/en/), which I’ll use as an example because I think it is up there with Fortnite or WoW in terms of future expected impact on games industry practices.1 Genshin Impact is an extremely well-implemented gacha game.


Gacha games, and other games with virtual currency systems, are extraordinarily well-positioned to directly influence user payment behavior.


## “I haven’t heard ‘gacha’ before.”


Gacha games are named after the onomatopoeia describing vending machines in Japanese malls and arcades which dispense toys and trinkets for, typically, 100 to 200 yen (about $1-$2). The pool of trinkets is displayed prominently on the machine; which trinket you get is effectively randomized. If you had your heart set on a particular one, you might spend much more than $1 on getting it, and some children (and adults!) very much do.


Many very successful games have a monetization strategy which descends from a variant of this. Generally, there is game content (most typically, characters) gated on receiving a random draw within the game. Pulling these random draws is a core game mechanic with many systems supporting it. One can generally purchase draws both with limited free currency, awarded through gameplay (and capped on an absolute or periodic basis), and with a paid currency, which you can purchase with real money.


This is far from the only gaming monetization model, but its an extremely effective one, because it tends to naturally incentivize “whales” (high spenders) to go after the characters whom they most wish to play, and those whales can probabalistically spend surprisingly large amounts of money in small increments2.


## Motivating user behavior via linked rewards


OK, let’s go back to rewards systems and how they’re going to be used to modify payments choices.


Genshin Impact has a few hundred currencies. The one which converts into gacha pulls is called primogems. The game trains you early to do things for primogems. Open any chest in the game, get 2 primogems. Complete a main quest line, 100 primogems. Complete your daily commissions (short quests), 40 primogems.


Do I think Genshin Impact can incentivize out-of-game activities? Yes, I do, and I think they already do it in a way which feels not incredibly off-theme for the game world. Consider this request which one’s constant companion character sent via in-game email. (Truly, every application expands until it can handle email.)


Paimon, a character who directs you to do everything in the game world, is here directing you to take a customer satisfaction survey. Paimon *could be employed in a B2B SaaS company’s marketing department*, and would be crushing her KPIs, because unlike the typical marketer she has literally infinite gold to incentivize uptake with.


## This will inevitably happen to payments, too


The new policy change allows (and, importantly for companies which sensibly have low risk budgets because of platform risk, gives explicit imprimatur to) collecting users’ contact information in-app and then pitching them on payments out-of-app.


It’s trivial to imagine game companies incentivizing different purchasing choices because this is already a core competence. Here’s one of the most A/B tested screens in any free-to-play game: the one which has paid currency purchases spelled out in-app.


This is from the Windows version of the game, but the iPhone version is identical in presentation and price points. You can see that the team has played heavily with packaging options to get users to commit to paying for the product and pushing them to larger purchases over smaller ones. (Again, there’s an iceberg worth of intellectual effort put in here that this post will elide.)


Under prior prevailing guidance, if one had established one’s account after downloading the game from an app store (as opposed to the open Internet), one might be locked from purchasing the paid currency except through that app store. Similarly, the Playstation version’s currency is locked to only being useful on Playstation consoles (and external currency can’t be used).


Even if you were using an unlocked platform, such as Windows, you’d have little reason to visit the website to purchase. It’s… functional.


But. Imagine a tiny, tiny, tiny tweak to your daily quests, emails, notifications, etc.


> Paimon is starting a Substack wants to write you a letter. Give us your email address here. Privacy policy applies, see details etc etc. **Reward: 20 primogems.**


(The implicit cash value of 20 primogems is approximately 25 cents but they’re, of course, free to the Federal Reserve of Primogems. The most work I’ve ever done for 20 primogems? It very literally involves scaling mountains… and I had fun doing it.)


Followed later by:


> Traveller! I found a coded message from a renowned sage. I can’t make heads or tails of it, but I sent it to your email address.


That email will include an appropriately themed request to go to the newly revamped web purchasing experience for the paid currency. It will have been thoroughly reworked and received some TLC from designers and strategists. And it will, almost inevitably, offer a ~10% discount to the in-app prices for purchases.


This improves the margin on currency purchaes from about 70% to about 85%, at a stroke, which is an incredible **20% lift for one engineering sprint.**


Genshin Impact has transacted more than a billion dollars through app stores to date. Imagine that you are the PM of revenue for it. Not implementing this costs millions of dollars *per week you delay*.


## Games in real life: fewer dragons, better loot


I predict, with over 90% confidence, that games are going to implement experiences like this within 6 weeks. Genshin Impact will almost certainly roll it out by October.


This is available even for games without a gacha model specifically. Games which directly sell skins (cosmetic improvements) can similarly offer a bonus skin if you purchase your next one from their site. Games can “window” content releases; new expansions/levels/characters available direct on Friday and in-app on Sunday. Since launch windows are invariably spikey in games, this has outsized margin impacts even if the price in both places is the same.


Single app developers selling on a more traditional “license” model might not benefit as much, but presumably they’re pretty happy with the conversion rate and distribution afforded by the app stores. It’s mostly service developers who feel, somewhat justifiably, that after getting into a multi-month relationship with a customer they have a *relationship* and don’t feel like continuing to pay a finder’s fee indefinitely for their custom.


It will be interesting to see whether this affects B2B services as well, which are a much smaller portion of the App Store but which make up a huge amount of revenue transacted on other software platforms. Basecamp was extremely [vocally opposed](https://appleinsider.com/articles/21/04/26/app-store-hey-and-antitrust-an-interview-with-david-heinemeier-hansson-on-the-appleinsider-podcast) to being unable to sell SaaS accounts and also maintain an app for [Hey](https://het.com), their email product, and presumably they’ll likely experiment with ways to convince their users to go direct. Other businesses may choose the same.


It will also be interesting to see spillover effects of this on other ecosystems. Apple is a trendsetter in the industry; Steve Jobs effectively established a Schelling point that owning a customer relationship in digital goods was worth a 30% take rate, and everyone since has either been on that Schelling point or positioned in direct opposition to it. Relatively niche concerns such as whether one can take advantage of their distribution while also marketing to customers gained through it matter quite a bit, as their decisions will likely influence policies at many other ecosystems.


I, for one, am thrilled that there is a vibrant market in different ways to pay and be paid. It is clearly in the best interests of customers and businesses, and platforms ultimately succeed if and only if both sides of their marketplace are successful, so I expect it is (over the long run) positive for platforms as well.


Some might ask whether it is sporting to pay the user to change their transactional behavior. This is, to put it mildly, **not unprecedented** in payment ecosystems! Payment methods engage in an unending brutal competition for (term-of-art incoming) share of wallet, and the competitive axes include the ergonomics of the payment method, branding, customer perceptions of trust and risk, and also concrete economic inducement to use them. There is an entire subculture devoted to playing rewards cards off each other. Every credit card company has whales, too, and (at least in the U.S.3) they attract and maintain their custom by rebating them a portion of their spend.


All’s fair in love, war, and payments.


---


### Footnotes

1. A full discussion of why would include Chinese developers’ arrival onto the global AAA scene, Chinese/Japanese/Western gaming cultures and storytelling cultural tropes being interpreted through a Chinese lens, and the game just being rollickingly good fun. It has a phase as an exploration game almost as well-executed as Breath of the Wild (which it draws inevitable comparisons to) and another phase as a fascinatingly deep combat puzzler with thousands of interesting strategic choices and a fair bit of mechanical skill required. ↩
2. There’s an interesting discourse about whether gacha games are anti-consumer or not which I don’t have enough space to do justice to here. Broadly I think they have some challenges similar to gambling, insofar as many adults gamble recreationally and enjoy it, while some are clearly harmed by it. I used to think that free-to-play games’ dependence on whales was strong evidence that they were a negative development, but I heard an [argument from the CEO of Kongregate](https://www.slideshare.net/emily_greer/dont-call-them-whales-freetoplay-spenders-virtual-value-gdc-2015) which  changed my mind. Distilled to its essence, it is that “Many whales are simply employed professionals who enjoy what they enjoy, and professionals historically spend a lot of money on what they enjoy. Why should we have contempt for this in a video game when we don’t if it is e.g. figure skating or wine?” I recommend reading or [watching](https://www.youtube.com/watch?v=P7SDByLlCHw) the entire talk if you’re interested in this topic. ↩
3. There are a few national equilibria with regards to credit card rewards. In the United States, credit cards are relatively expensive for businesses to process. A large portion of that expense is rebated to end users in the form of rewards or cash back. In Europe, credit cards are (by regulation) relatively inexpensive to process, and end users do not enjoy rewards. In Japan, credit cards are relatively expensive to process, but financial institutions have exercised strong and <salaryman>doubtlessly totally uncoordinated</salaryman> discipline on capping rewards at 1%. It is not obvious which of these equilibria card issuers, businesses, or users *should* prefer; that different regions ended up in different equilibria was very path dependent. ↩
