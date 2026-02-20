---
title: "Tether: The Story So Far"
date: 2019-10-28
url: https://www.kalzumeus.com/2019/10/28/tether-and-bitfinex/
slug: tether-and-bitfinex
word_count: 6214
---


A friend of mine, who works in finance, asked me to explain what [Tether](https://tether.to/) was.


Short version: **Tether is the internal accounting system for the largest fraud since Madoff**.

excerpt

Read on for the long version.


## So you want to build a cryptocurrency exchange


The dominant use case for cryptocurrency is speculation. Speculators want to put value into the system, somehow have it become greater, and then take more value out of the system than they put in.


The cryptocurrency community includes many exchanges, each a group of affiliated companies, but it is sometimes clearer to view it as an single entity. It would have a series of ledgers, some mechanism for exchanging between the ledgers (taking a cut for each ledger hop and  sometimes for bookkeeping within a ledger), and onramps and offramps to traditional currencies (which the community calls “fiat”). From the point of view of the ecosystem, it doesn’t matter which company has those ramps, because value flows unimpeded within the ecosystem.


The ecosystem is *not* a single entity with unified control. Cryptocurrency is not [Liberty Reserve](https://en.wikipedia.org/wiki/Liberty_Reserve). It has, however, recapitulated Liberty Reserve’s architecture of a network of peer “exchangers” with a shared ledger between them to enable [hawala](http://www.in-formality.com/wiki/index.php?title=Hawala_(Middle_East,_India_and_Pakistan))-like transfers of value. In cryptocurrency’s case, those shared ledgers are blockchains rather than a single traditional database kept by an organizing entity.


Most exchanges do not have fiat onramps and offramps, but the ecosystem has to have them. Because the cryptocurrency community largely does not sell products or services other than speculation, there is no extrinsic sort of funding like you see in other businesses (e.g. no material revenue from customers). Every dollar that goes out to buy the clichéd Lambo is a dollar that went in from a speculator.


Having fiat onramps and offramps is extremely lucrative for an individual exchange, because retail traders largely use exchanges which give consumer Internet quality money movement capabilities. Professionals follow their volume. (To, ahem, rip their eyeballs out.)


Conceptually speaking, all that you need to have a cryptocurrency onramp/offramp is a banking relationship and some glue code. This is *quite complicated* for Bitcoin exchanges, because of anti-money-laundering (AML) and Know Your Customer (KYC) regulations.


The cryptocurrency ecosystem’s purported raison d’être is building permissionless money, and (descriptively) large sums of money flow between pseudonymous identities without any Compliance Department having asked any questions about them. Financial institutions, which are extremely heavily regulated by a global consensus that AML/KYC are core responsibilities for their industry, are *extremely* reluctant to bank cryptocurrency exchanges, even ones which (by the standards of the industry) are aboveboard.


But some cryptocurrency exchanges have an attitude towards compliance which is best described as “Bond villain.”


## Enter Bitfinex


Bitfinex, founded in 2012, became the largest international cryptocurrency exchange after Mt. Gox imploded in 2013/2014. It has the sort of complicated backstory you’d expect of a Bond villain cryptocurrency exchange.


The most relevant fact in the backstory: in 2016, Bitfinex suffered what Matt Levine describes (facetiously but not inaccurately) as the [inevitable fate of Bitcoin exchanges](https://www.bloomberg.com/opinion/articles/2017-10-03/bitcoin-traders-and-index-funds): they [lost $70 million of Bitcoin](https://www.bitfinex.com/posts/155) (~120k bitcoins) to hackers.


Bitfinex was insolvent as a result of this hack. The cryptocurrency community has an interesting understanding of the word “insolvent”; here it means “Their balance sheet shows greater liabilities to depositors than they have physical assets they could immediately satisfy the depositors with.” They owed more bitcoins (per their database) than they actually controlled on the blockchain.


Bitfinex conducted a “bail-in” to forestall the collapse of their firm.


In the ordinary course, a financial institution keeps a ledger of how much money it owes which depositors. The liability to the depositor increases as the depositor deposits more money (or earns interest) and decreases as they withdraw money (or pay fees, etc). Financial institutions routinely have customers which have balances in several currencies (or denominated in other things of value, like e.g. shares of Apple); conceptually, they work in the same fashion.


Bitfinex unilaterally decided that, since they could not satisfy all liabilities for Bitcoins anymore, they would apply a [36% “haircut”](https://www.reuters.com/article/us-bitfinex-hacked-hongkong/bitfinex-exchange-customers-to-get-36-percent-haircut-debt-token-idUSKCN10I06H) to all balances (bitcoin-denominated and otherwise) on the platform. In exchange for the haircut, they invented a new unit of account, the BFX token, which tracked dollar-denominated losses to the haircut. (At least one counterparty, Coinbase, has been [reported](https://twitter.com/nathanielpopper/status/933130228175552513?s=20) as having not been haircut. Presumably their lawyer said the word “[conversion](http://www.dmlp.org/legal-guide/elements-conversion)” and that was the end of that discussion.)


BFX tokens were tradeable on Bitfinex (of course), and after initially falling substantially below par, Bitfinex offered the option of redeeming them for equity in Bitfinex (which they arbitrarily decided was worth $1 per share). Eventually, they repurchased them at $1 per token.


But Bitfinex developed a problem with dollars.


## Banking a Bitcoin exchange


(You can verify representations made in this section from [Bitfinex’s lawsuit filed against Wells Fargo.](http://media.kalzumeus.com/tether-docs/bitfinex-sues-wells.pdf))


At the time, Bitfinex (theoretically a Hong Kong entity but whose location, like a Bond villain, changes moment-to-moment to fit the needs of the scene) was banking in Taiwan at Hwaitai Commercial Bank, KGI Bank, First Commercial Bank, and Taishin Bank.


Taiwanese banks do not have direct access to the U.S. financial system; they engage via correspondent banking relationships. These banks corresponded through Wells Fargo. Wells, in the wake of publicity about the Bitfinex hack, told the banks they would no longer clear USD wires to or from Bitfinex.


This meant that customers could no longer move money in or out of the casino, and a casino which can’t get money in or out can’t collect a rake. So Bitfinex a) sued Wells, fruitlessly and b) intensified their use of a company they had purchased (and, until the lawsuit, had prevaricated about being related to): Tether.


## How Tether works


Blockchain blockchain blockchain, blah blah blah.


Tether builds a USD/etc-denominated ledger on top of a collection of slow databases (Bitcoin, Ether, Tron, etc). They promised that entries in that ledger correspond to demand deposits held in reserve, meaning that customers can rely that one Tether is worth 1 USD (or one Tether euro is worth 1 EUR, etc).


You buy tethers from someone who has bought them from Tether, generally a cryptocurrency exchange or OTC desk. After buying them, you can use a client (or your exchange’s software) to send them to another address on the blockchain. Similar to Bitcoin, with the promise of less price swings due to the capability for redemptions and the promised reserve.


Tether is a “stablecoin.” Stablecoins are conceptually similar to a money market fund: a place to park money with minimal market risk. A money market fund is backed by short-term commercial paper; this genre of stablecoins were supposed to be backed by… well, that was cagey, but the answer rounded to “money in a bank.”


Why have stablecoins? They give cryptocurrency exchanges and their users a USD-denominated ledger to handle inter-exchange money movement and ease onramps and offramps between value in the cryptocurrency economy and value in the regulated economy, by causing the transaction (seen by a Compliance Department at a regulated financial institution) which moves money in or out of the ecosystem to occur at remoteness to the cryptocurrency exchange.


This is *not* the *messaged* purpose of stablecoins. Those are:

- quickly transfering between Bitcoin exchanges
- giving a safe-harbor still in crypto but with less volatility when not actively trading
- allowing you to self-custody USD balances so you’re not exposed to counterparty risk at each exchange you keep a balance at


The community extremely underestimates the degree to which the designed intent and best use case of Tether is facilitating money laundering. Specifically, it allows socially established individuals/firms trading at reputable OTC desks or exchanges to function as the bankers for the rest of the industry.


The cryptocurrency ecosystem largely believes that “If it’s all crypto, then YOLO”, requiring nowhere near compliant levels of KYC or AML for customers who transact only in cryptocurrencies. A representative example, from [Tether in 2015](https://web.archive.org/web/20150521003646/https://tether.to/faqs/):


> You can fund your account with bitcoins and convert to Tethers to stabilize your bitcoins and (sic) without having to undertake KYC.


Their customers prefer this, some because they would prefer to not have their identifying documents leaked when their cryptocurrency exchange is inevitably hacked, some because they philosophically disagree with regulation, some because they are evading taxes, and some because their business is international narcotics smuggling.


Since people believed Tether’s representations that a Tether was as good as a dollar, and could be surrendered for a dollar at any time, it quickly became the unit of account for most of the cryptocurrency community. At the point Bitfinex/Tether lost access to high-quality banking, there were about $55 million of Tethers in circulation. Tether [claims](https://wallet.tether.to/transparency) there are now more than $4 billion.


**Tether’s claim about reserves was a lie.**


Tether has routinely not had actual control of hundreds of millions of dollars of their purported reserves.


They have lied repeatedly about this fact.


While they promised their customers that Tether was backed by “traditional currency held in our reserves”, their reserves were actually accounting fictions; receivables from money launderers like Crypto Capital Corp, receivables from related parties such as Bitfinex, and cryptocurrencies.


This is a pretty robust accusation, but Tether has admitted to it [in court](http://media.kalzumeus.com/tether-docs/bitfinex-response-to-nyag.pdf).


## Where were the reserves kept in 2017 through today?


Tether has, in the words of Bitfinex CFO Giancarlo Devasini, “[banked like criminals](https://medium.com/hackernoon/the-curious-tale-of-tethers-6b0031eead87).”


After losing useful banking in Taiwan, Tether shuffled their reserves through a series of shell corporations, periodically getting them frozen when banks realized that they were banking a cryptocurrency exchange which was lying to them about their actual business.


Tether eventually found a bank willing to bank it: Noble Bank, in Puerto Rico. Noble’s board was against banking Tether:


> [Recent articles came] to the attention of the board, and there is a concern that if not managed correctly, that [our relationship with you could] cause blowback on Noble, and could negatively affect our relationship with BNY Mellon.


BNY Mellon is a large, NYC-based custodial bank. One of their functions is holding assets for banks from outside the U.S. inside the U.S.’ financial system. They don’t bank money launderers. Noble’s board was worried that BNY Mellon might fire Noble as a customer over the Tether relationship (and, broadly, the sort of controls environment and risk appetite that the relationship would be evidence of). If that happened, it would kill Noble.


Tether got Noble over the hump leading a $2 million Series A investment in Noble. (As an aside: there is a reason that professionals say “the e in email stands for [evidence](http://media.kalzumeus.com/tether-docs/bitfinex-invests-in-noble.pdf).”)


(“Was Noble a bank?” That gets into a fascinatingly deep tangent; suffice it to say that they were a regulated financial entity operating with high-quality access to the US financial system, which is close-enough-to-a-bank for Tether’s purposes.)


Tether then deposited minimally hundreds of millions of dollars into Noble, which [intrepid analysts](https://blog.bitmex.com/tether/) noticed when the [Puerto Rican financial regulator](http://www.ocif.pr.gov/Pages/default.aspx) reported that balances at International Financial Entities increased by almost 5X virtually overnight.


Tether warned customers to not talk about the banking details they were exposed to when onramping or offramping USD, because they were worried about their business coming to the attention of BNY Mellon.


[Someone talked](https://collection.cooperhewitt.org/objects/18612741/).


This instigated a predictable series of responses, ultimately killing Noble and forcing Tether to find another banking partner.


Tether moved their reserves to Deltec Bank, and ramped up their usage of Crypto Capital Corp.


## Crypto Capital Corp


Crypto Capital Corp is not a bank. Crypto Capital Corp is not kinda-sorta-bank-like if you squint at it. Crypto Capital Corp is not even a Bond villain.


**Crypto Capital Corp is a money launderer.**


Tether was their largest client. Other clients included Quadriga, the largest Canadian Bitcoin exchange, and Kraken. One of these two has collapsed due to the founder looting it. The other is [trying to put this chapter behind them](https://twitter.com/krakenfx/status/1187845897591382018).


Several governments, including [Poland](https://news.bloomberglaw.com/banking-law/crypto-capital-official-nabbed-in-polish-money-laundering-probe), believe the Colombian drug cartels were also clients.


This implies that Tether (and, by extension, the cryptocurrency ecosystem) played the part of the nail salon and Colombian drug cartels that of Jesse Pinkman in [Breaking Bad’s famous discussion](https://www.youtube.com/watch?v=ez6xH-su2xI) of how money laundering works. (Though in this situation the nail salon is also money laundering, but they’re the kinder, gentler, acceptable-at-the-best-parties sort of money launderers.)


CCC’s modus operandi was identifying banks with poor compliance controls and opening shell entities which it represented were engaged in real estate transactions, shuffling money in and out until the bank closed the account, then doing it again.


Tether purported in a [recent court filing](http://media.kalzumeus.com/tether-docs/bitfinex-discovery-request.pdf) to be shocked, shocked that their money launderer might have lied to them about the ownership structure of the shell corporations they directed customers towards; Crypto Capital was only supposed to lie *to the banks*.


> […] Crypto Capital never disclosed that several of the bank accounts to which Bitfinex’s customers transferred fiat funds were actually held and controlled by Spiral and Reggie Fowler, and not by Crypto Capital or any of its related entities.


## What did this look like for customers?


Bitfinex makes a pedantic distinction that only authorized customers (like Bitfinex) can deposit money with Tether and only those authorized customers can redeem it, a distinction they adopt or discard whenever the plot requires it. Bitfinex is Tether. This distinction is shell games within shell games.


When a customer would want to deposit money with Bitfinex, they would contact Crypto Capital Corp, who would give them the name, account number, and bank of a shell corporation (with names like “Global Trade Solutions A.G.”), with instructions to wire the shell corporation money with a lie designed to not rouse suspicion from their banks. (The lie in their support documentation was: “[Treasury transfer back to my own account](https://twitter.com/CasPiancey/status/1187790855341371392/photo/1)”).


It bears repeating at this point: Bitfinex knew that these were the instructions it should pass to customers, and [explicitly instructed customers](https://twitter.com/lawmaster/status/1052178530983956480/photo/1) to not reveal the wire instructions they were given, for fear of drawing official attention to the crimes they were committing.


> [Do not share these instructions] except with your financial institution. Divulging this information could damage not just yourself and Bitfinex, but the entire digital token ecosystem. Accordingly, you are cautioned that there may be severe negative effects associated with this information becoming public.


CCC would then increment Bitfinex’s balance with CCC, and provide Bitfinex with confirmation that they had received the wire. Bitfinex would then credit the customer with a Tether-denominated receivable on their books or with actual on-the-blockchain Tether.


When a customer wanted actual money in return for Tethers, they’d run the process in reverse. The customer would send Tether to Bitfinex. Bitfinex would make a “transfer” (accounting entry) on CCC’s books, using their online system, decrementing the amount CCC owed Bitfinex and incrementing the amount they owed Tether. CCC would then launder a wire to the customer, lying to their banks, and tell Bitfinex they had done it, then decrement the amount they owed Tether.


## Did Crypto Capital Corp actually have the money?!


**No, they did not.**


CCC’s principal architect, Reginald Fowler, was [skimming 10% of all deposits](http://media.kalzumeus.com/tether-docs/Crypto-Capital-Detention-Memorandum.pdf) in the system for his personal uses.


> This is corroborated by information contained in the Master US Workbook indicating that scheme members set up a “10% Fund” from the client deposits.


Those personal uses included, probably, [funding a football league](https://www.si.com/nfl/2019/05/01/alliance-american-football-reggie-fowler-investor-arrested-bank-fraud) which, and this is a quote, “[made a deal with the devil](https://www.ocregister.com/2019/04/05/aaf-goes-under-inside-the-sudden-collapse-of-the-alliance-of-american-football/)” and promptly collapsed when Fowler did what he has done [many times before](https://www.espn.com/nfl/news/story?id=1995986).


This was likely the primary way he was compensated.


Bitfinex claims to have believed, per their [court filings](http://media.kalzumeus.com/tether-docs/bitfinex-discovery-request.pdf), that CCC subsidized their services through net interest.


> [B]esides a nominal fee for each deposit or withdrawal, Crypto Capital charged no fee for these services to [Bitfinex] because it was able to earn substantial interest on the funds it held on [our] behalf in its accounts.


This would make sense for a [financial institution](https://www.kalzumeus.com/2019/6/26/how-brokerages-make-money/), but it doesn’t make sense for a money launderer, because risk-free assets generate very little interest (1% of a billion dollars *doesn’t pay for the minimum viable financial institution*) and because most ways to do this at scale require negotiating rates.


During the course of that negotiation, the bank is going to ask a question like “Wait, this only makes sense for me if you keep those assets deposited long-term, but you’re a real estate company. Why would you want that? Why would you want that *from me*? The thing you should want from me is a loan. I can do this on your assets if you bring me some of your loan business, which is *clearly* going to be an order of magnitude larger than your long-term deposits, because you are a real estate company. What projects are you working on right now that you expect to borrow about $10 billion for?”


Crypto Capital didn’t and couldn’t select banking partners on the basis of interest rates. They selected for extremely inattentive (or corruptable) compliance departments.


Because Bitfinex and other customers did not want to know the internal operations of their money launderer, they didn’t notice that CCC was routinely siphoning off their funds.


This could have gone on for quite a while. Think of a distinction the cryptocurrency community uses a lot: hot wallets (where an exchange keeps cryptocurrency for day-to-day use, connected to the Internet) and cold wallets (airgapped storage which isn’t connected to the Internet). They do this because they’re worried about getting the hot wallet taken by adversarial action (hackers). Bitfinex was using CCC, and not Deltec, to move money around because frequent wires draw adversarial attention; CCC is the hot wallet.


In an environment where more money is flowing into the hot wallet than flowing out, if you don’t audit the cold wallet, you wouldn’t notice adversarial action *against the cold wallet*. In separating the two for your security, you’ve played yourself. (Sound unlikely? It happened at Mt. Gox; the cold wallet had a leak in it. The [Wizsec broke the fraud and has a 40 minute presentation](https://www.youtube.com/watch?v=l70iRcSxqzo); [here are my notes](https://gist.github.com/patio11/598ec35c6c1675c97d93383f41b39b0b). It’s *glorious.*)


A function of Tether is to encourage far more actual money to flow into the ecosystem than flows out (“Why withdrawal all the way to a bank account when you can just withdrawal to Tether? It’s easier to invest back in, a much faster round-trip, and why would you *trust banks*.”), and so to the extent Tether’s balance was going up, the fact that it was being repeatedly siphoned off would not be noticed unless you were either a) the thieves or b) asking to get more money than inflows would cover.


That liquidity crisis happened in 2018, after regulators froze some CCC’s shell corporation bank accounts. By August 2018, CCC couldn’t pay outflows out of inflows and had exhausted their cash on hand. They explained that this was because they had some temporary liquidity problems caused by regulators.


That was a lie; CCC had liquidity problems, alright, but a major part of it was that the *money they had embezzled* was illiquid.


Word of this liquidity crisis got out. Quoting chat logs by a senior Bitfinex representative, who has not learned Stringer Bell’s dictum on the wisdom of keeping notes on a criminal )%#)(ing conspiracy:


> We are seeing massive withdrawals and we are not able to face them anymore unless we can transfer money out of [CCC].


By October 2018, rumors were circulating that Tether was insolvent. It [faced a bank run](https://twitter.com/patio11/status/1051560132235030528). The rumors were, bluntly, accurate; their reserves were a receivable from a money launderer who had stolen a portion of the money and gotten more of it frozen.


Some people in the cryptocurrency community expect that, after Bitfinex has convinced the regulators that Crypto Capital Corp was *their* money launderer and that Crypto Capital Corp owned Fictitious Real Estate Firm, LLC that regulators will give FREF, LLC’s money back to Bitfinex.


Hahahahahahahahaha. Let’s review precedent here to see whether that is a reasonable belief.


Mt. Gox created a U.S. subsidiary, Mutum Sigillum, LLC, directly to receive funds from U.S. customers and effect value transfers to/from the mothership. It did not complete a required money services business registration. Its accounts were [seized](http://cdn.arstechnica.net/wp-content/uploads/2013/05/Mt-Gox-Dwolla-Warrant-5-14-13.pdf). Mt. Gox’s bankruptcy administrator got in touch with the U.S. government and, because they were feeling merciful, the government offered a deal. The government would give back half of the $5 million back in return for Gox surrendering any claim to the rest. The administrator wisely [took the deal](https://www.mtgox.com/img/pdf/20170308_annoucement.pdf).


You are welcome to your estimate of how likely it is that regulators will show mercy on Bitfinex. My estimate: the frozen money is *gone*.


## So Tether was fully backed until Crypto Capital made off with the reserves?


That is an interesting theory, for which we have extremely little evidence, other than Tether’s claims and our estimation that they would not lie.


My competing theory: it was backed some of the time in the fashion they described, until it was backed some of the time by cryptocurrency, until it was backed some of the time by cryptocurrency and accounting shenanigans, until it was backed none of the time.


My theory keeps looking better and better as more evidence comes to light.


## How did Tether survive the bank run?


When your fraud has an operational hiccup, you have to fraud harder, or your fraud will be discovered!


[Lying for Money](https://www.amazon.com/Lying-Money-Legendary-Frauds-Workings-ebook/dp/B078WFT5JV) is the best book about financial fraud I’ve ever read. It explains why this is *a recurring pattern* in frauds: every fraud has a monetary hole in it. That is the very essence of fraud, it purports to have value where no value exists. Any operational hiccup being brought to light would expose the hole, and the fraud. This necessitates a *new fraud* to keep the old one running. This *digs the hole deeper* and *accelerates* the fraud to collapse, both because the fraud needs more victims, because the fraud naturally promises higher-than-achievable growth rates, and because it gets operationally more complicated to execute on.


We’ve seen this before in cryptocurrencies many, many times. Take Mt. Gox. Karpelès bought an exchange which was insolvent the day he bought it, due to a prior hack. To paper over the insolvency, he bought bitcoin with imaginary money while paying out very real money to sellers. This buying pressure increased the price of bitcoin, which deepened the dollar-denominated hole the fraud was in. The increased price of bitcoin both brought new dollars to the market and necessitated that he buy bitcoin *faster* to stay in place. This distracted him from key other responsibilities of running a fraudulent Bitcoin exchange, like counting your bitcoin periodically to ensure they aren’t going to the hackers who already hacked you insolvent. (Again, see the Wizsec presentation.)


Bitfinex spent months spinning plates to satisfy just enough withdrawal requests to avoid being undeniably insolvent.


Their tactics included:


**Satisfying withdraw requests with cryptocurrency.** “I can’t give you $1 million for 1 million tether but I can give you $1.01 million in Bitcoin.” The user accepts this because they could get cash at a banked exchange or OTC desk; note how this dynamic makes them (and their contra) an instrumentality of the fraud.


**Satisfying withdraw requests using money mules.** *Their lawyers* [describe this mechanism:](http://media.kalzumeus.com/tether-docs/nyag-filing-against-bitfinex.pdf) (bolding mine)


> **As explained to [New York’s] attorneys by [Bitfinex’] counsel: Bitfinex and Tether have also used** a number of other third party “payment processors” to handle client withdrawal requests, including various companies owned by Bitfinex/Tether executives, as well as **other “friends” of Bitfinex - meaning, human being friends of Bitfinex employees that were willing to use their bank accounts to transfer money to Bitfinex clients who had requested withdrawals.**


**Satisfying *Tether* withdrawal requests with *Bitfinex* customer funds.**


In October 2018, Bitfinex had customer (and corporate) funds at Deltec Bank, the last bank they could find which would work with them directly. Tether preferred to believe it had customer funds with Crypto Capital Corp. They did not; some money is gone, and more is frozen.


Bitfinex [swapped their actual money (at Deltec) for Tether’s imaginary money (at CCC)](https://www.bloomberg.com/opinion/articles/2019-04-26/things-got-weird-for-stablecoin-tether) and wired out ~$625 million to people demanding that Tether redeem their claims. This converted Bitfinex customer funds into claims against a money launderer who *does not have the money*.


Bitfinex changed the messaging with respect to reserves, several times, from being “fully backed by traditional currency” to “sufficiently backed by USD [with] assets always [exceeding] liabilities” to the current:


> Every tether is always 100% backed by our reserves, which include traditional currency and cash equivalents and, from time to time, may include other assets and receivables from loans made by Tether to third parties, which may include affiliated entities (collectively, “reserves”)


Incredibly, this worked for a little while, but the New York Attorney General’s office caught on and asked questions. Five months after actually sending the money to Tether redeemers, Bitfinex concocted documents purporting to have Tether “loan” Bitfinex money, secured by Bitfinex equity. This is another shell game.


As of April 30th, Bitfinex’s attorney claimed that they had cash and short-term securities which would cover ~74% of outstanding tethers. Here’s what their general counsel [swore](http://media.kalzumeus.com/tether-docs/bitfinex-response-to-nyag.pdf) to the court, shortly before April 30th, 2019.


> As of the date I am signing this affidavit, Tether has cash and cash equivalents (short term securities) on hand totaling approximately $2.1 billion, representing approximately 74 percent of the current outstanding tethers.


## Put another layer on it!


In May 2019, Bitfinex was running low on liquid valuable things again, and organized a bailout via selling $1 billion of a “utility token” ([unregistered securities offering](http://media.kalzumeus.com/tether-docs/leo-whitepaper-2019-05.pdf)).


Bitfinex received principally Tether and other cryptocurrencies in this offering. It’s important to understand what this did, and in lieu of a series of balance sheets, let’s make it a hypothetical user story.

- Bob deposited $100 with Bitfinex. Bob expects Bitfinex to have that money, at all times.
- Bitfinex used Bob’s $100 to pay a Tether client. (This causes Tether’s self-reported 74% score to *improve*.)
- Bitfinex now doesn’t have the money.
- Bob expects Bitfinex to have $100. It does not. Bitfinex will say it actually owes Bob 100 Tether, *which it does not have*, which is backed by a receivable from CCC, *which does not exist*.
- Bitfinex sells equity to other ecosystem participants, in exchange for Tether, Bitcoin, or anything else, really.
- Bitfinex believes it can now satisfy Bob’s claim against them.


Bitfinex has been “burning” the equity periodically via repurchasing it. They have messaged an intention to continue doing this as their business generates income and as they are vindicated by the judicial process against the regulators who froze CCC’s shell corporations’ bank accounts.


The cryptocurrency community largely chooses to believe that Bitfinex is repurchasing this equity with their own money. Running a Bitcoin exchange is, after all, a figuratively license to print money. Bitfinex has pinky sworn never to use their *other* figurative license to print money without it being backed. This time, the thinking goes, they are telling the truth.


Why would anyone buy a billion dollars of this equity?


Participants in the ecosystem understand that if they don’t hang together, they will hang separately.


**Bitfinex is *intimately involved* in their businesses.** One way to suborn a bank is to buy the bank. Bitfinex has done this; it resulted in them (partially) owning the bank(s).


Another way to suborn a bank is to involve the bank in illegal activity; this results in a similar ownership of the bank, since the bank’s continued survival is at your pleasure.


**Much of the cryptocurrency community is exposed here.** This includes firms and individuals who are in the part of the community which aspires to being legitimate. Expect many of them to get questions of the form “As someone who is very financially sophisticated, who went through mandatory compliance training most recently on XX/YY/ZZZZ, and who is very obviously bound by our AML regulations: *explain this wire transfer to me*.” or “At what date did your exchange cease doing business with Bitfinex? What due diligence did you run on them? When did you stop and why? Interesting. How many suspicious activity reports did you file about that?”


## The great Cryptocurrency Credit Bubble


Another reason for the ecosystem to back Bitfinex is that it keeps the music playing. The Cryptocurrency Credit Bubble unwinding would depress prices and volumes. Exchanges need prices and volumes to run their businesses.


“Credit bubble?” Yes, there can no longer be serious doubt about this: people bought Bitcoin with money that didn’t exist, pushing up the price of Bitcoin. **A lot of people currently think they are richer than they are.**


This is a reprise of Mt. Gox, where the Willy Bot (Karpelès) bought Bitcoin with imaginary money, paying out the sellers with real money, and deepening the insolvency of the exchange.


The only remaining argument is how much this happened and how intentional it was. I expect we’ll get material updates as litigation progresses, but the hole is lower bounded at hundreds of millions of dollars.


## Systemic risk


Tether should introduce the cryptocurrency community to the concept of *systemic risk*: after something is infrastructure, it gets into *everything*. When you withdrawal the infrastructure suddenly, a bunch of things break all at once, even ones that don’t look exposed, because of the transitive nature of the dependency graph.


An example of this in real life: money market funds, which have many surface similarities to Tether, likewise are critical load-bearing economic infrastructure. *Just one* money market fund “[broke the buck](https://www.investopedia.com/articles/economics/09/money-market-reserve-fund-meltdown.asp)” (declining to 97 cents) during the global financial crisis. And the real economy, which has many things in it which aren’t money market funds, and which has many money market funds to choose from, and which has high-quality options for backstopping money market funds, *went into barely restrained panic*.


Why? If you believe the asset is riskless for long enough it will find itself in the infinite variety of structures which need a riskless asset, and when those structures suddenly have a hole where their riskless asset should be, calamity quickly follows. There was the prospect of companies missing payroll, financial structures unwinding due to sudden unanticipated insolvency, etc. And so there was a massive outflow from money market funds *as a class* which put such strain on the commercial paper market that it nearly broke. The liquidity crisis’ downward spiral was only broken when the government guaranteed money market funds.


Where is Tether critical, load-bearing infrastructure? Lots of places. It represents most of the liquidity for many “altcoins” (cryptocurrencies which are less popular than the main ones, like Bitcoin/Ether). It is the unit of account and the internal reserve of many of the less-banked exchanges. It *very probably* functions as the credit supply which keeps liquidity in the system.


It remains to be seen whether there will be a lender of last resort who steps in to make Tether holders whole if and when the reserves vanish.


## So what’s up now?


Reggie Fowler, who appears to have been the primary architect of Crypto Capital Corp’s money laundering apparatus, was [arrested](https://www.justice.gov/usao-sdny/pr/arizona-man-and-israeli-woman-charged-connection-providing-shadow-banking-services) in the U.S. A co-conspirator is at large.


Ivan Manuel Molina Lee, who was the President (likely a paper relationship), was extradited from Greece to Poland on suspicion of having engaged in money laundering [for drug cartels](https://www.theblockcrypto.com/post/44591/ceo-of-crypto-capital-arrested-in-alleged-money-laundering-operation).


Oz Yosef, who Bitfinex’s senior executives dealt with directly (he’s the one they begged for money), was just [indicted](https://decrypt.co/10774/crypto-capital-founder-indicted-on-three-criminal-counts-after-companys-presidents-arrest) in New York.


Bitfinex maintains they are an innocent victim in all of this, and publicly professes that they believe that multiple regulators will return to them money seized from their money launderer’s shell corporations’ bank accounts.


Bitfinex and its principals have not yet been indicted by the U.S. Attorney for the Southern District of New York, but crucially, not in the same sense that you have not been indicted by the U.S. Attorney for the Southern District of New York.


## Who really broke this story?


Many of these facts have been rumored for years.


They gradually came to light by the usual process of journalism: listening carefully to what people say, taking notes, asking questions of people who would know, and reviewing documents.


Interestingly, very little of the journalism was originally done by people with press cards.


Most credit here belongs to a loosely connected group of Internet journalists / analysts, who some might be inclined to call trolls, but for them having scooped all the professionals. A partial list: [Bitfinexed](https://medium.com/@bitfinexed), [Jakal](https://twitter.com/intel_jakal), [Cas Piancey](https://twitter.com/CasPiancey), [Bennett Tomlin](https://twitter.com/BennettTomlin/), and [Bitmex’s research team](https://blog.bitmex.com).


I’ve included citations in-line when facts were eventually confirmed by government, admission by the guilty parties in court, or traditional or (the more reputable end of) cryptocurrency-enthusiast media.


Are more shoes going to drop? Very likely.


## Why do you care about this so much?


I don’t hold any position in cryptocurrencies. I continue to believe that they’ve produced substantially no value in the world. I’m not philosophically opposed to shorting them to zero, but the mechanics of doing that are non-trivial.


Example of the complexity: The best way to bet against Bitcoin while not having counterparty risk (if the cryptocurrency ecosystem vanishes in a fireball, will someone still be willing and able to pay you?) is via the futures markets, but to the extent that I had market-superior information here, the prediction would be “Bitcoin will quickly whipsaw *up* as people exchange tethers for the safe asset, and then decline”, and I have no confidence in that trade making enough money to pay for the liquidation risk and opportunity costs. (The instrument I really wish existed is put options on a Bitcoin ETF, but I’m conflicted in wanting that. If that ETF ever gets to market, it would improve the shortability of Bitcoin, but it would be terrible for the retail investors who bought into it.)


My intense skepticism of cryptocurrencies is probably the issue on which I am most in disagreement with many close friends, professional acquaintances, and some of the smartest people I know. That is part of the reason why the hobby of peeling back onion layers here is so engrossing: people really, passionately believe that there is *something here.* I’m intellectually curious. The thing people have told me exists should *smash* my interest buttons: *programmable money*! How could I not look!?


I have looked, quite a bit. I have not found a good use case yet, or the revolutionary technology advances that my friends tell me exist, but I have found some frauds.


And, for better or worse, fraud is also one of my weird hobbies.


## Did you know about this?


Kinda.


I did some similar investigation regarding Mt. Gox prior to it collapsing and had proof of the insolvency. People on HN doubted that I had done the work prior to the news dropping, and I really care about earning my Internet points, so I posted some hashes to the blockchain. Just kidding, to Twitter.


If you’re unfamiliar with this practice: it should be extremely difficult for me to cause a hash collision with an arbitrarily chosen value. (If not, sell all your crypto and get off the Internet because we’re all in for a very bumpy ride.) Accordingly, if I publish a hash to someplace I can’t edit and whose timestamps you trust, like Twitter, that proves that I had possession of the associated text as of that timestamp.


You can verify the hashes yourself, and should (or you’ll get stagemanaged like that time Craig Wright convinced the Economist and a Bitcoin core developer that he was Satoshi). For your convenience I’ve provided the command line; feel free to ask a trusted friend if you want to verify that.


I don’t think I got everything right, but you can check for yourself; I self-graded to save you some trouble.


**January 31st, 2018**: My [predictions](http://media.kalzumeus.com/tether-docs/bitfinex-01312018.md). SHA-1 hash: [65b3ad9af56704ee0150819bbbf166ec6eb8d4ae](https://twitter.com/patio11/status/958494488061595649)


Command line which will reproduce that hash:


`curl http://media.kalzumeus.com/tether-docs/bitfinex-01312018.md | shasum`


**Really short version**: Tether is basically solvent but laundering (right at that time); named some jurisdictions (partially right); mechanism is FBO accounts with attorneys (I think that was right once but didn’t describe them CCC or their Noble/Deltec accounts); predicted freezing of bank accounts (right); predicted liquidity crisis (right); predicted Kraken fails first (probably wrong; they were my guess at the time for who was most mixed up with Tether due to being an accessible onramp/offramp in the U.S.).


**March 15th, 2019**: My [predictions](http://media.kalzumeus.com/tether-docs/bitfinex-03152019.md). SHA-1 hash: [938d939059a23aa84ce493db0c4d542748f849a7](https://twitter.com/patio11/status/1106252558941577216)


Command line which will reproduce that hash:


`curl http://media.kalzumeus.com/tether-docs/bitfinex-03152019.md | shasum`


**Really short version**: Tether is insolvent (right). They collateralized with cryptocurrency (right). They’re insolvent because the market moved against them (uncertain; that shoe hasn’t dropped yet; prediction didn’t mention theft/freezing except to incorporate by reference the earlier prediction that did).


**May 15th, 2019**: My [predictions](http://media.kalzumeus.com/tether-docs/bitfinex-05152019.md). SHA-512 hash: [92e78ff9c8817bdaed2c7a3b6281d4aa419580e38bb3de590142428923a897eaadf145944b0336fc782915201a9e4597099fc05d591dca2b60361f998a111d8e](https://twitter.com/patio11/status/1128562676664156161)


Command line which will reproduce that hash:


`curl http://media.kalzumeus.com/tether-docs/bitfinex-05152019.md | shasum -a 512`


**Really short version**: The world’s biggest cryptocurrency hedge fund is a fraud.


This is a materially different story from the evidence on record today. I’m long popcorn futures for the coming litigation.


## Final thoughts?


I remain [annoyed with how complicit](https://www.kalzumeus.com/tweetstorms/1032033115408031744) our industry has been in enabling cryptocurrency scams.
