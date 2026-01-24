---
title: "Penny Auctions: They’re Gambling"
date: 2009-05-25
url: https://blog.codinghorror.com/penny-auctions-theyre-gambling/
slug: penny-auctions-theyre-gambling
word_count: 953
---

Late last year, I encountered what may be nearly perfect [evil in business plan form](https://blog.codinghorror.com/profitable-until-deemed-illegal/): Swoopo. What is Swoopo? It’s a class of penny auction, where bidders pay for [the privilege of bidding](http://www.mercurynews.com/businessheadlines/ci_12431890):


> [Penny auctions] offer new televisions, computers, game consoles, appliances, handbags, gold bars and more for starting prices of a penny to 15 cents, depending on the site.
> To “win” a product, shoppers must first buy a bundle of 10 to 700 bids for 60 cents to $1 each. Shoppers use one each time they place a virtual bid on a product. Each bid raises the price of the item by a penny to 15 cents, depending on the site. Some have automatic bidding functions similar to eBay.
> Doing the math and not getting carried away is important: The final price of a product that retails for $100 might be $29, but the total price paid could be much more, depending upon the number of bids used. If a shopper bids 10 times at $1 a bid, for instance, the total price paid would jump to $39. And, there is the real possibility of using all your bids without getting the product.
> Auction winners generally get their item for about 65 percent off retail but could save as much as 98 percent if there are few bidders.
> Since the sites make the bulk of their revenue from the purchase of bids, they profit most when they feature a product that elicits a bidding war.


One of Swoopo’s investors recently contacted me via email, and I had to marvel at the size of the cojones you’d need to associate yourself with this kind of nastiness. Swoopo is evil beyond the likes of Saddam Hussein, The Balrog, OSB, Darth Vader, and Barbra Streisand – combined.


He wanted to talk to me on the phone about positioning, and staunchly maintained that there was *no* element of chance in a Swoopo “auction.” Once I stopped laughing, I told him these were my terms:


> If you believe in Swoopo, then data speaks much louder than words.
> Let’s conduct an experiment.
> Doesn’t have to be you, personally. Take n dollars, and use those n dollars in whatever strategy it takes to win items (of MSRP $399 or higher) on Swoopo.
> If Swoopo isn’t a game of chance or lottery, a skilled player should be able to win at least one item in this experiment, yes?
> I’d be happy to run this experiment and write about it on my blog. Just let me know what terms you think make sense.


I haven’t heard from him since. (Now I’m curious if *anyone* is willing to take on this experiment, under the same terms.)


Because **Swoopo is, at its heart, thinly veiled gambling**. The companies backing Swoopo and other Penny Auction sites are hoping unsophisticated regulatory agencies will buy the “It’s not a game of chance” argument if it’s wrapped in a lot of technical intarweb mumbo-jumbo they can’t fully comprehend.


But we’re no government flacks. We’re programmers, and many of us develop websites for a living. It’s a bit tougher to pull the wool over our eyes. In [Trying to Game Swoopo](https://web.archive.org/web/20101123104914/http://jcs.org/notaweblog/2009/03/06/trying_to_game_swoopo_com/), Joshua Stein pulled out everything in his programmer’s bag of tricks to win a Swoopo auction – and, predictably, [failed](https://web.archive.org/web/20100923211151/http://jcs.org/notaweblog/2009/03/11/trying_to_game_swoopo_com_part_2/).


> With all of this data available, I concluded that **there is no way to reliably win an auction on swoopo.com without using their bidbutler service**. There are delays on their network/servers in processing manual bids, whether intentional or just due to bad design, that cause manual bids placed with 1 or 2 seconds remaining not to be cast. users of their bidbutler service have an unfair advantage in that their bids are placed on the server side and are not subject to these delays.
> Since it is not possible to reliably place manual bids, the only way to guarantee that an auction can be won (while still coming out ahead) is to use the site’s bidbutler service with high ceilings on the number of bids and amount that one will let it bid up to. Those ceilings have to take into account the item’s current price, and will be lower the longer an item is being bid on.


As Joshua’s data shows, there is no way to win a Swoopo auction other than through sheer random chance – that is, your client-side bid happens to wind its way through the umpteen internet routers between the server and your computer in time, ending up at the top of a queue with dozens or hundreds of other bids placed within a fraction of a second of each other. And what’s worse, you may not have any chance at all, unless you place a server-side bet through their exploitatively expensive “bidbutler” service.


As I said in my original post, the only winning strategy at Swoopo, or any other penny auction site, is *not to play*. On Swoopo, there are nothing but millions of losers – and by that I mean they are gambling and losing millions of real dollars to the house. Which would be OK, I guess, **if it was properly regulated as gambling**. Swoopo and all these other penny auction sites should be regulated and classified as the online gambling sites in sheep’s clothing they really are.


Let’s see what we can do to hasten this process along. Warn your friends and family. Complain to the Better Business Bureau and other regulatory agencies. And if you feel as strongly as I do about this, please write your congressmen/women and urge them to regulate these exploitative penny auctions.

[e-commerce](https://blog.codinghorror.com/tag/e-commerce/)
[online auctions](https://blog.codinghorror.com/tag/online-auctions/)
[penny auctions](https://blog.codinghorror.com/tag/penny-auctions/)
[bidding strategies](https://blog.codinghorror.com/tag/bidding-strategies/)
[online shopping](https://blog.codinghorror.com/tag/online-shopping/)
