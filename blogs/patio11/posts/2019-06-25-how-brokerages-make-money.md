---
title: "How Discount Brokerages Make Money"
date: 2019-06-25
url: https://www.kalzumeus.com/2019/6/26/how-brokerages-make-money/
slug: how-brokerages-make-money
word_count: 4510
---


This is outside of my usual software-oriented beat, but sometimes [people are wrong on the Internet](https://xkcd.com/386/). Most recently, people have been wrong about payment for order flow, an esoteric topic in the investing industry which seems vaguely unsavory to Hacker News [commenters](https://news.ycombinator.com/item?id=20005229), Michael Lewis [0], etc.


Explaining why payment for order flow isn’t a big deal requires a more in-depth discussion of discount brokerages. All stats below are as of 2018; citations for the annual reports are at the bottom.


## What is a discount brokerage?


A discount brokerage is a few things:


A discount brokerage is not a full-service brokerage, which used to charge several hundred 1970s dollars to place a single stock trade and which used to *call you* to convince you of the desirability of paying them several hundred dollars to place a single stock trade.


A discount brokerage is an [investing store](https://www.bloomberg.com/opinion/articles/2017-05-04/investing-stores-and-libyan-bribes), which exists to get the mass affluent [1]  to allocate a portion of their net worth to assets other than bank deposits and real estate, but is almost entirely indifferent to what they actually want to invest in. They carry a variety of products, like listed US stocks, perhaps a few bonds, probably mutual funds, perhaps options and futures, and the like, and feel about them about the same as Netflix feels about horror versus anime: it literally doesn’t matter as long as you consume it here.


A discount brokerage is a marketing operation which both does a lot of uncompensated education about investing and retirement savings and also spends a metric shedload on advertising, partially underwriting substantially all media which touches financial topics (and a lot of higher-end lifestyle media besides).


A discount brokerage is a retail franchise, similar in character to a bank or cell phone store, where absolutely nothing important happens in the branch offices other than convincing you that, if you call them, someone will be able to reset your password, check your account balance, or otherwise walk you through a routine customer service request. This brand promise is, fundamentally, true; they have some of the best telephone support operations on the planet.


A discount brokerage maintains many large, boring computer programs which interface with clearing, custody, and settlement firms and the banking system to move bits representing money around.


A discount brokerage is a thin user interface over a more complicated API to the financial markets, allowing an unsophisticated retail investor to send a limit order to buy five shares of Google trading on the New York Stock Exchange.


Those are all different ways of looking at reality, and are mostly true. Except that last one. Discount brokerages mostly don’t actually talk to stock exchanges; that’s a specialized, detail-oriented, extremely regulated, and hypercompetitive skill set whose market clearing price is literally lower than zero. We’ll get to that.


## Who are and are not discount brokerages?


Good examples of discount brokerages include [Charles Schwab](https://www.schwab.com/), [TD Ameritrade](https://www.tdameritrade.com), [E*Trade](https://www.etrade.com), and (arguably) [Interactive Brokers](https://www.interactivebrokers.com).


(I’m including Interactive Brokers mostly for comparison purposes. Schwab, TD Ameritrade, and E*TRADE all basically target the same customer: mass affluent Baby Boomers. Interactive Brokers targets professional and semi-professional active traders but happens to expose just enough of a front-end at just comparable enough terms to look like a discount broker.)


These are **not** the only places that do investing; they’re one particular part of one value chain which connects mass affluent Americans to the financial markets. Employer-sponsored retirement plans like 401ks are another; [Fidelity Investments](https://www.fidelity.com/), the largest 401k administrator, also has a (very materially sized) retail-facing brokerage operation. So does [Vanguard](https://investor.vanguard.com/home/), which is primarily a mutual fund provider. But since I’ve got to draw the line somewhere, and publicly traded ones are easier to get data on, I looked into those four.


Registered Investment Advisors (RIAs) aren’t discount brokers and yet have to be mentioned in a discussion of them. A RIA is, basically, an investment salesman who moonlights as an amateur psychologist with better math skills than most psychologists. They mostly charge a percentage of your net worth for amateur psychology, worksmanlike math, and non-expert-but-credentialed investing advice. The investment stores are happy to provide backend services to investment salesmen, because RIAs control a huge portion of the mass affluents’ investable assets. (There is an excellent, excellent [podcast episode](http://investorfieldguide.com/kitces/) about how every product innovation in investing in the last 50 years is the answer to the questions “How do RIAs get paid?” and “How do RIAs justify their pay by providing more value-adding services than the last iteration?”)


Rounding out the lot, there are fintechs like the robo-advisors ([Wealthfront](https://www.wealthfront.com/) and the like), which replace the RIA’s human with a computer. Full-service brokerages still exist, too.


And then there’s [Robinhood](https://www.robinhood.com), which is a discount brokerage whose marketing and product decisions probably do not assist their users in achieving successful outcomes.


## So how do discount brokerages make money?


### Net interest


Suppose I were to give you $100, in return for your promise to give it back when I wanted it and pay me 0.27% annualized interest in the meanwhile. Suppose you invested this in a virtually riskless bond, perhaps a mortgage-backed security with government backing, offering 2.53% annualized interest. You’d earn $2.26 in net interest in a year.


Suppose I were to give you $200 billion dollars. Now I’m the American middle class and you’re Charles Schwab. You would earn something like $5.8 billion dollars in net interest income. This would entirely pay for your sideline business in running a brokerage. Stocks, bonds, mutual funds, branch offices, call centers, blah blah blah, it all exists to justify [the only pricing page that matters](https://www.schwab.com/public/schwab/investing/accounts_products/investment/cash_solutions), and all the verbiage on the pricing page is about how much *you* pay *the customer*.


This is an exaggeration, but not much of one. 57% of Schwab’s revenues are from net interest. The firm could literally give away every other service; discount the mutual fund fees to zero, do away with commissions, etc etc, and they would still be profitable.


Schwab isn’t even the leader among discount brokerages in dependence on net interest. That would be E*TRADE, at about 67% of revenues. Interactive Brokers makes 49% and TD Ameritrade 51% in the segment.


(You’ll come up with a different number if you cursorily skim TD Ameritrade’s annual report. They have an Insured Deposit Agreement with [TD](https://www.td.com), the bank which owns them; TD kicks back $1.5 billion a year to be swept their client funds every night. “Sweeping” is a term of art by which money automatically leaves the brokerage accounts to rest peacefully on the balance sheet of a bank every night and then be back in the brokerage ready for the morning bell. The question of why a bank would happily pay billions of dollars for this is a fascinating digression into banking regulation and capital sufficiency ratios which this essay’s margins are too small to contain, but you can round it to “net interest income” and not be too wrong. All discount brokerages have a sweep available; how prominent they make the option and how they price it are product decisions.)


A bit of financial history: E*TRADE nearly went bankrupt in 2007 due to having chased yield into writing mortgages and buying asset-backed securities, principally backed by subprime mortgages. These imploded, in a very public fashion, resulting in customers doubting E*TRADE’s ability to satisfy claims or continue operating the day-to-day brokerage business. They were saved by [Citadel](https://www.citadel.com/), which is a large hedge fund that, by non-coincidence, is one of the internalizers that E*TRADE and the other brokerages use to access the public markets.)


Some people get mad about the financial industry for taking advantage of customers. I find it hard to get mad about a deal between willing counterparties, but if you think that Wall Street is soaking the US middle class, you should be monomanically focused on the interest spread between cash balances in brokerage accounts and high-interest bank accounts or money market funds. That is **the cost that does not call itself a cost**.


Brokerage customers keep ~10% of their assets in cash. The 200 basis point spread between cash in brokerage accounts and money market funds or insured bank accounts, *all of which are functionally riskless* [2] , is equivalent to a 20 bps asset management fee across the portfolio. Vanguard’s flagship funds charge about 10 bps for wrapping the entire stock market, SPY (an ETF, which structurally has lower costs) does it for 4 bps, and people think the roboadvisors might be expensive doing similar for 25 bps on top of the underlying investments… and the discount brokerages charge effectively 20 bps over all your assets *just for managing the tiny portion that is in cash, the easiest asset to manage*.


But instead people get mad about payment for order flow, because nobody writes books about Interest Rate Spreads Are Just Too Darn High.


### Commissions


Originally the “discount” in “discount brokerage” referred to commissions on trades, which are essentially a fee levied on successful API calls. In the bad old days of full-service brokerages, these were hundreds of dollars per trade. By the late 1990s the discount brokerages were doing them for tens of dollars; they’re currently single digit dollars and are destined for zero.


You can find the current, briefly non-zero prices on your brokerage or comparison website of choice. The contribution to revenue across the discount brokerages is minimal: 6.8% at Schwab, 28% at TD Ameritrade, and 17% at E*TRADE.


Interactive Brokers is the one standout, largely because it caters to high-volume professional and semi-professional traders; it makes 49% of revenues on commissions.


A name often mentioned by my acquaintances with respect to commissions is Robinhood, which decided to take the hundreds of millions of dollars that discount brokerages spend on ads every year and instead subsidize commissions straight to zero. This is both bold, disruptive innovation and *also* just an incremental extension of a pricing war which the larger brokerages have been engaged in for decades.


In addition to routinely shaving a buck or two off their list prices, Schwab is experimenting with zeroing commissions on their own ETFs. This realigns their revenue to the stocks (of money) rather than the flows, which makes the substantial majority of brokerage accounts that virtually never trade more lucrative and probably is better for investors (since “retail investors destroy value when trading” is about as citation-needed as “smoking causes lung cancer” at this point).


Zero-commission trading is a game of cross-subsidy. Cross-subsidy isn’t bad, per se; one of the ways that financial services stay so affordable is by firms competing with different mixes of cross-subsidization and specializing on their target customer profile.


Some larger financial firms are themselves opening up discount brokerages to use the subsidy to get greater share-of-assets and customer acquisition among desirable customers; Chase’s [YouInvest](https://www.chase.com/personal/investments/you-invest/pricing) product basically exists as one leg of a stool to get millennial professionals to use a Chase Sapphire card with their Chase Sapphire banking. Several banks have tried this before: Bank of America uses Merrill Lynch (specifically their Merrill Edge product) in the same fashion, and Capital One tried (and failed) to do similar with their Sharebuilder acquisition.


### Asset Management


Groceries are a famously low-margin business. One way to increase the margins is to vertically integrate: instead of selling branded Cheerios, you sell circular-shaped toasted whole grain cereal, and keep a portion of the money General Mills would have spent on advertising. You probably don’t actually *make* the cereal; you pay a specialist to do that for you.


Investment stores are a famously low-margin business. One way to increase the margins is to vertically integrate: instead of selling branded… you get the general idea.


Charles Schwab is, of the discount brokerages, the oldest and the one which figured out the formula: use (historically) RIAs to hawk Schwab-branded mutual funds as opposed to other mutual funds, use the boatload of marketing fees that you’re now not paying to a 3rd party to underwrite the development of the rest of the store, and successfully nail multiple generational transitions in how the financial industry made money. (Can I recommend [that podcast](http://investorfieldguide.com/kitces/) again; it is a fantastic oral history of the financial advice industry and, by extension, Schwab.)


Schwab made 32% of its revenue doing asset management, including 18% for mutual fund/ETF management and another 11% for “advice solutions.” (Schwab takes approximately 50 bps of assets under management for providing the service of talking to a human who are licensed to recommend things from the investment store, as opposed to people who can take orders for things from the investment store.)


TD Ameritrade earned about 10% for similar products, and E*TRADE about 3.8%. Interactive Brokers doesn’t have store-brand products and doesn’t appear to make a material amount of revenue from e.g. mutual fund marketing fees.


### Securities Lending


Many technologists know how shorting stock works: you borrow a share of a stock from someone, sell it for money, and eventually repurchase and return the share, hoping to profit from the decline in price of the stock.


The word “borrow” is important and often glossed over in this explanation. Retail traders often get the stock they short loaned to them by their brokerage as a courtesy (cross-subsidization, again!), but institutional traders (shorting large blocks of stock for potentially long time horizons) or anyone shorting “hard to borrow” stocks has to pay for the privilege. Who gets paid? The person who has the stock to loan out.


You might think that is the owner of the stock but… not always. A mutual fund, for example, might loan the attractive constituents of their portfolio to either increase returns or act as a less-transparent expense ratio. (Cross-subsidization, again!) Retail brokerages might loan out customer assets and just keep the fee.


[Schwab](https://client.schwab.com/secure/file/P-5182696/MKT33373-05.pdf) and [Interactive Brokers](https://ibkr.info/article/1838) both have opt-in programs where they’ll split the fee with the owner; IB explicitly splits it 50/50.


Most customers’ will not notice securities lending revenue; on a typical stock it might be 5 bps a year or less. (Across my portfolio, which is an unremarkable mix of ETFs and a few large-cap stocks, Interactive Brokers earns 14 bps and pays about 7.)


Some customers with concentrated positions in heavily-shorted stocks would hypothetically earn a lot if they were being paid for it. If, for example, one wanted the moral rectitude of a Bitcoin exchange combined with the clear-headed decisionmaking of smoking cannabis, one could hypothetically justify an investment in Aphria. Short sellers are presently willing to pay about 100% per year to short that stock… for [reasons](https://www.google.com/search?q=aphria+short+seller+report).


A better reason for a technologist to be long a stock a lot of people want to short is because they have earned it through services and, for whatever reason, not sold it. If you own a material amount of stock in a publicly traded technology company, particularly a material amount of stock which is not widely available at the moment, you should probably devote non-zero effort to understanding whether you’re allowed to loan that stock out and, if so, whether your brokerage will pay you to do that.


TD Ameritrade earned about 4.1% and E*TRADE earned 3.5% from securities lending. Schwab’s is upper bounded at 2.2%. Interactive Brokers was an outlier at about 9.7%. (These are all net of payments to clients; Schwab, notably, passes the fee revenue for their mutual funds to the fund shareholders.)


### Payment for Order Flow


Discount brokerages mostly (again, save Interactive Brokers) service retail clients. Retail clients almost by definition do not possess an informational edge on the market; they are buying stock because it is payday, because Jim Cramer shouted loudly, or because they love Apple products. They sell for similarly personal reasons. None of these is an edge by the standards of professional movers of money.


Everyone who buys or sells a financial asset pays for **liquidity**; the ability to quickly and definitively close a transaction at a particular agreed upon price. Houses are notably low in liquidity and that liquidity is extremely expensive; it takes months of work to sell them and the gap between natural buyers and natural sellers is very high. Publicly listed large cap US equities have extremely good liquidity; the bid/ask spread is extremely narrow and you can buy or sell, by retail investor standards, any amount at either price.


That is on the public markets, but retail investors get a *better deal* than the public markets. They get this deal from internalizers, who are something akin to an API gateway between the brokerages and the public markets.


It’s useful to understand that there are *many* public markets in the US and they don’t have the same order book; the prices can, in principle, momentarily differ from each other. One variant of high frequency trading exists to correct these momentary mispricings by arbitraging them away.


Regulation NMS obligates brokers to route orders to the venue offering the best price. This is logistically challenging to determine in real time, and takes specialized technical systems and skill. The internalizers offer this product to the discount brokerages and pay the brokerages to adopt it.


Why? Suppose a hypothetical stock is trading at $10.01 by $10.02. This means that sophisticated marketmakers (mostly) are willing to buy it for $10.01 or sell it for $10.02; they are, at this instant in time, ambivalent which of those two transactions happens, because doing this hundreds of thousands of times a day will generally result in them earning half a penny per share (half the spread) while taking on some risk.


The nature of the risk is that the price of the stock is not a pure random walk which can be statistically predicted. There is some underlying economic reality to it, and that economic reality can be perceived and acted upon by sophisticated people who don’t work for the marketmaker. This results in them being “run over”; a large order (or series of orders) can move the market away from the previously prevailing price, causing the marketmaker to have a position (which is something they want to minimize) which is now at a loss.


Principally, these underlying economic realities will be perceived (or caused!) by well-capitalized, informed traders like hedge funds, mutual funds, Goldman Sachs’ proprietary trading operation, etc etc.


**The risk of adverse selection is priced into the cost of liquidity.** If you are making markets in public, where Goldman Sachs can trade with you, you have to quote a wide enough spread such that even with Goldman occasionally running you over, you still make money.


HFTs, and other marketmakers, are good at this. They have to be; if they weren’t, they’d have gone out of business. It is a very competitive game.


If you could somehow make markets without informed traders—if you were guaranteed that Goldman could never trade with you—your risk would be lower and you could, therefore, provider tighter spreads. There is a way to do this; it is to trade exclusively with retail traders. They *can’t* run over you; they don’t have the informational edge or the capital to do so.


Thus internalizers make this offer to every discount broker: use us for execution. Most of your customers are indifferent to order routing; we’ll handle that hard work for you. For most of them, we’re going to make an instant decision to offer them *better execution than the public markets will give*; we’ll pay $10.011 instead of $10.01, for example. We can’t offer them worse, because the SEC will detect that and fine us gazillions of dollars for the pennies we picked up on the trade.


At scale, this is so lucrative and so riskless that, in addition rebating a bit of money to the retail investors, the internalizers pay their brokerages a commission. This is the “payment for order flow.”


Some people who read a lot about technology confuse this with buying the retail investor’s data. Citadel is one of the largest hedge funds in the world. Citadel does not run a machine learning algorithm on your neighbor’s GM trades in their IRA to inform their thinking of the true value of GM as a business. They can employ a team of rocket scientists to do that. The thing they buy vis your neighbor is *the opportunity to transact with him*, because doing so is virtually riskless given their setup.


**Payment for order flow is a minor footnote to the story of discount brokerages**, in the same fashion that HFT is basically irrelevant to retail traders except for decreasing their cost of trading by decimating spreads.


Schwab earned 1.4% of revenue from payment for order flow, TD Ameritrade about 8.4%, and E*TRADE about 6.1%.


Interactive Brokers has historically been [quite reticent](https://www.interactivebrokers.com/en/index.php?f=44074#section-pfof-drop) about participating in internalization, because it doesn’t play well with their sophisticated clients; they earn about 1.1% from it.


A major reason for the dispersion here is that some spreads are wider than others and, all else equal, you’d pay more to own a toll booth to risklessly collect a wider spread. Spreads on options are higher than that for equities and options trades are generally larger (one contract represents 100 shares and a trade may involve 2~4 legs with N contracts each). Options marketmakers thus pay more than equity internalizers on a per-trade basis.


The absolute amounts involved on a per-trade basis are peanuts: 9.7 cents (!) for Interactive Brokers to about $2.50 per trade for the other three.


Why Robinhood earns more than the discount brokerages for order flow is readily apparent: their product encourages options trading. This is bad for customers, principally because the supermajority of Robinhood customers do not understand options trading and the risk/reward calculus for them is even more borked than it is for the vast majority of people who engage in it. The options trades they engage in are also less liquid, and so have higher spreads, and so are more lucrative for marketmakers, but the thing you should be most concerned with is their product decisions which encourage options trading, not with the price of liquidity on those options trades.


(Indeed, while marketmaking for Robinhood options trades seems like a license to print money, a quick perusal of /r/wallstreetbets makes me wonder whether *taking the other side of all Robinhood trades* would be even better. I’m joking but I’m not sure how much I’m joking.)


Headlines like [Robinhood Gets Almost Half Its Revenue in Controversial Bargain With High-Speed Traders](https://www.bloomberg.com/news/articles/2018-10-15/robinhood-gets-almost-half-its-revenue-in-controversial-bargain-with-high-speed-traders) are virtually meaningless, as the above discussion of other monetization options should make clear. At scale, once their userbase actually has material cash in their accounts on any given day, they’ll likely make net interest, but pre-scale they may not even have the treasury function to do the work required to earn it safely. It’s a commentary on how low their revenue is (growth-stage startup optimizing for reach over revenue, film at 11), not a commentary on how beholden they are to Wall Street.


## Did anything useful come out of this research project?


Three things that I believe much more strongly than I did previously:


**Commissions in discount brokerages will go to zero.** Like most repricing, it will continue to be slow until it happens all at once. Interactive Brokers will likely still continue charging them, as it is least similar in character to the rest of the industry.


**Roboadvisors are a bad business below scale.** I have really liked the model as a user, but I am glad I’m an investor using a roboadvisor rather than an investor in a roboadvisor. The discount brokerage industry works because you can make decisions which are bad for users and lucrative for you (“Ahh you have entrusted me with cash money; let me park it safely and pay you 50 bps while keeping the next 150 bps for me, rather than parking it in the equally safe place any of my product managers could have implemented if they wanted to be fired instantly”); roboadvisors depend on making decisions which are good for users (“Let me minimize that cash drag for you”) and then being very explicit about costs which are anchored *very low.* (Again, hate to belabor a point, but Wealthfront charges 25 bps all-in (on top of the underlying ETFs) and every customer knows it; Schwab charges 18 bps for *cash management alone* and virtually no customer has ever even thought there could be a number there.)


**Some technologists I am acquainted with should know one esoteric thing about equities markets.** If you own a material amount of a publicly traded stock, and the supply of that stock is constrained, and some population of sophisticated people want to short it, maybe you should Charge More rather than letting your broker get that service from you for free. Speak to your trusted advisor, this can have fairly toothy consequences, etc etc.


### More reading


I put more effort into the math than I generally do for blog posts, but it’s entirely possible that I fumble-fingered something. Feel free to reproduce it. All of the above is exhaustively covered in public filings, principally:

- [Charles Schwab 2018 annual report](https://www.aboutschwab.com/annual-report)
- [TD Ameritrade 2018 annual report](https://s2.q4cdn.com/437609071/files/doc_financials/annual/2018/TD-Ameritrade-2018-Annual-Report.pdf)
- [E*TRADE 2018 annual report](https://cdn.etrade.net/1/19032622400.0/aempros/content/dam/etrade/about-us/en_US/documents/investor-relations/financials-sec-filings/quarterly-earnings/2018/Q4/10-K/2018-Q4-10K.pdf)
- [Interactive Brokers 2018 annual report](https://investors.interactivebrokers.com/download/2018-IBG-AR.pdf)


Another good magic word to know is “SEC Rule 606” if you ever want to know which internalizers are getting order flow, probably because you or someone you love is wrong on the Internet.


**Disclaimer**: I value my reputation as an honest broker (ba dum bum) a lot more than my extremely attenuated ability to influence peoples’ financial decisions, but for what it is worth: I do not have a material exposure to any company mentioned and don’t use affiliate links. My family uses Wealthfront and Interactive Brokers, mostly because [retail investors should mostly not pick stocks](https://training.kalzumeus.com/newsletters/archive/investing-for-geeks) and this setup is relatively amenable to [Americans living abroad](https://www.interactivebrokers.co.jp/jp/?f=13416).


[0]: Michael Lewis wrote a book so bad about the microstructure of securities markets that it Someone Is Wrong On The Internet’ed [a book](https://www.amazon.com/dp/B00P0QI2M2/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1) into being. You should read that one; it’s great.


[1]: This is a term of art thrown around in financial services and marketing generally. It corresponds to roughly 30% of the US population, basically those with financial assets above $100k or who are, due to strong income, are certain to get there soonish. The bottom 50% of the US by wealth largely doesn’t own brokerage accounts; the folks who are between those two markers are largely *unprofitable* accounts for the industry to service, but brokerages (and banks) have gotten reasonably good at playing the *very long game* about cost of customer acquisition and cohort math.


[2]: Anticipating an HN comment: “Brokerage accounts, money market funds, and bank accounts are not functionally riskless.” There’s a long and boring answer about SIPC versus FDIC insurance, the mechanics of Schwab and Interactive Brokers striping deposits across multiple banks to 4~10X dip on deposit insurance, and the implicit guarantee of money market funds in the wake of 2008 to avoid market contagion, but the short version is “I still think I’m right.”
