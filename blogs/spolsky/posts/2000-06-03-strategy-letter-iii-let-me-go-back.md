---
title: "Strategy Letter III: Let Me Go Back!"
date: 2000-06-03
url: https://www.joelonsoftware.com/2000/06/03/strategy-letter-iii-let-me-go-back/
word_count: 2103
---


When you’re trying to get people to switch from a competitor to your product, you need to understand *barriers to entry*, and you need to understand them a lot better than you think, or people won’t switch and you’ll be waiting tables.


In an [earlier letter](https://www.joelonsoftware.com/articles/fog0000000056.html), I wrote about the difference between two kinds of companies: the Ben and Jerry’s kind of company which is trying to take over from established competition, versus the Amazon.com kind of company which is trying a “land grab” in a new field where there is no established competition. When I worked on Microsoft Excel in the early 90’s, it was a card-carrying member of the Ben and Jerry’s camp. Lotus 123, the established competitor, had an almost complete monopoly in the market for spreadsheets. Sure, there were new users buying computers who started out with Excel, but for the most part, if Microsoft wanted to sell spreadsheets, they were going to have to get people to switch.


The most important thing to do when you’re in this position is to *admit it*. Some companies can’t even do this. The management at my last employer, Juno, was unwilling to admit that AOL had already achieved a dominant position. They spoke of the “millions of people not yet online.” They said that “in every market, there is room for two players: Time and Newsweek, Coke and Pepsi, etc.” The only thing they wouldn’t say is “we have to get people to switch away from AOL.” I’m not sure what they were afraid of. Perhaps they thought they were afraid to “wake up the sleeping bear”. When one of Juno’s star programmers (no, not me) had the *chutzpah*, the unmitigated *gall* to ask a simple question at a company meeting: “Why aren’t we doing more to get AOL users to switch?” they hauled him off, screamed at him for an hour, and denied him a promotion he had been promised. (Guess who took his talent elsewhere?)


There’s nothing wrong with being in a market that has established competition. In fact, even if your product is radically new, like eBay, you probably have competition: garage sales! Don’t stress too much. If your product *is* better in some way, you actually have a pretty good chance of getting people to switch. But you have to think strategically about it, and thinking strategically means thinking *one step beyond* the obvious.


The *only strategy *in getting people to switch to your product is to *eliminate barriers*. Imagine that it’s 1991. The dominant spreadsheet, with 100% market share, is Lotus 123. You’re the product manager for Microsoft Excel. Ask yourself: what are the barriers to switching? What keeps users from becoming Excel customers tomorrow?



| **Barrier** |  |
| 1. They have to know about Excel and know that it’s better |  |
| 2. They have to buy Excel |  |
| 3. They have to buy Windows to run Excel |  |
| 4. They have to convert their existing spreadsheets from 123 to Excel |  |
| 5. They have to rewrite their keyboard macros which won’t run in Excel |  |
| 6. They have to learn a new user interface |  |
| 7. They need a faster computer with more memory |  |



And so on, and so on. Think of these barriers as an obstacle course that people have to run before you can count them as your customers. If you start out with a field of 1000 runners, about half of them will trip on the tires; half of the survivors won’t be strong enough to jump the wall; half of *those* survivors will fall off the rope ladder into the mud, and so on, until only 1 or 2 people actually overcome all the hurdles. With 8 or 9 barriers, *everybody* will have one non-negotiable deal killer.


This calculus means that **eliminating barriers to switching** is the most important thing you have to do if you want to take over an existing market, because eliminating *just one barrier* will likely *double *your sales. Eliminate two barriers, and you’ll double your sales again. Microsoft looked at the list of barriers and worked on *all of them*:



| **Barrier** | **Solution** |
| 1. They have to know about Excel and know that it’s better | Advertise Excel, send out demo disks, and tour the country showing it off |
| 2. They have to buy Excel | Offer a special discount for former 123 users to switch to Excel |
| 3. They have to buy Windows to run Excel | Make a runtime version of Windows which ships free with Excel |
| 4. They have to convert their existing spreadsheets from 123 to Excel | Give Excel the capability to read 123 spreadsheets |
| 5. They have to rewrite their keyboard macros which won’t run in Excel | Give Excel the capability to run 123 macros |
| 6. They have to learn a new user interface | Give Excel the ability to understand Lotus keystrokes, in case you were used to the old way of doing things |
| 7. They need a faster computer with more memory | Wait for Moore’s law to solve the problem of computer power |



And it worked pretty well. By incessant pounding on eliminating barriers, they slowly pried some market share away from Lotus.


One thing you see a lot when there is a transition from an old monopoly to a new monopoly is that there is a magic “tipping point”: one morning, you wake up and your product has 80% market share instead of 20% market share. This flip tends to happen *very* quickly (VisiCalc to 123 to Excel, WordStar to WordPerfect to Word, Mosaic to Netscape to Internet Explorer, dBase to Access, and so on). It usually happens because the very last barrier to entry has fallen and suddenly it’s logical for everyone to switch.


Obviously, it’s important to work on fixing the obvious barriers to entry, but once you think you’ve addressed those, you need to figure out what the non-so-obvious ones are. And this is where strategy becomes tricky, because there are some non-obvious things that keep people from switching.


Here’s an example. This summer I’m spending most of my time in a house near the beach, but my bills still go to the apartment in New York City. And I travel a lot. There’s a nice web service, PayMyBills.com, which is supposed to simplify your life: you have *all *your bills sent to them, and they scan them and put them on the web for you to see wherever you may be.


Now, PayMyBills costs about $9 a month, which sounds reasonable, and I would consider using it, but in the past, I’ve had pretty bad luck with financial services on the Internet, like Datek, which made so many *arithmetic *mistakes in my statements I couldn’t believe they were licensed. So I’m willing to *try* PayMyBills, but if I don’t like it, I want to be able to go back to the old way.


The trouble is, after I use PayMyBills, if I don’t like it, I need to call every damn credit card company and change my address *again*. That’s a lot of work. And so the *fear* of how hard it will be* to switch back* is keeping me from using their service. Earlier I called this “stealth lock-in,” and sort of praised it, but if potential customers figure it out, oh boy are you in trouble.


That’s the barrier to entry. Not how hard it is to switch *in*: it’s how hard it might be to switch *out*.


And this reminded me of Excel’s tipping point, which happened around the time of Excel 4.0. And the biggest reason was that Excel 4.0 was the first version of Excel that could **write** Lotus spreadsheets transparently.


Yep, you heard me. **Write**. Not read. It turns out that what was stopping people from switching to Excel was that everybody else they worked with was still using Lotus 123. They didn’t want a product that would create spreadsheets that nobody else could read: a classic [Chicken and Egg problem](https://www.joelonsoftware.com/articles/fog0000000054.html). When you’re the lone Excel fan in a company where everyone else is using 123, even if you love Excel, you can’t switch until you can participate in the 123 ecology.


To take over a market, you have to address *every* barrier to entry. If you forget just one barrier which trips up 50% of your potential customers, then *by definition*, you can’t have more than 50% market share, and you will never displace the dominant player, and you’ll be stuck on the sad (omelet) side of chicken and egg problems.


The trouble is that most managers only think about strategy one step at a time, like chess players who refuse to think one move ahead. Most of them will say, “it’s important to let people convert *into* your product, but why should I waste my limited engineering budget letting people convert *out?*“


That’s a childish approach to strategy. It reminds me of independent booksellers, who said “why should I make it comfortable for people to read books in my store? I want them to buy the books!” And then one day Barnes and Nobles puts *couches* and *cafes* in the stores and practically *begged* people to read books in their store without buying them. Now you’ve got all these customers sitting in their stores for *hours* at a time, mittengrabben all the books with their filthy hands, and the probability that they find something they want to buy is linearly proportional to the amount of time they spend in the store, and even the dinkiest Barnes and Nobles superstore in Iowa City rakes in hundreds of dollars a *minute* while the independent booksellers are going out of business. Honey, Shakespeare and Company on Manhattan’s Upper West Side did *not* close because Barnes and Nobles had cheaper prices, it closed because Barnes and Nobles had *more human beings in the building*.


The mature approach to strategy is not to try to force things on potential customers. If somebody *isn’t even your customer yet,* trying to lock them in just isn’t a good idea. When you have 100% market share, come talk to me about lock-in. Until then, if you try to lock them in now, it’s too early, and if any customer catches you in the act, you’ll just wind up locking them *out*. Nobody wants to switch to a product that is going to eliminate their freedom in the future.


Let’s take a more current example: ISPs, a highly competitive market. Something that virtually no ISP offers is the ability to get your email forwarded to another email address *after you quit their service*. This is small-minded thinking of the worst sort, and I’m pretty surprised nobody has figured it out. If you’re a small ISP trying to get people to switch, they are going to be worrying about the biggest barrier: telling all their friends their new email address. So they won’t even want to try your service. If they do try it, they won’t tell their friends the new address for a while, just in case it doesn’t work out. Which means they won’t be getting much email at the new address, which means they won’t really be trying out the service and seeing how much better they like it. Lose-lose.


Now suppose one brave ISP would make the following promise: “Try us. If you don’t like us, we’ll keep your email address functioning, and we’ll forward your email for free to any other ISP. For life. Hop around from ISP to ISP as many times as you want, just let us know, and we’ll be your permanent forwarding service.”


Of course, the business managers would have fits. Why should we make it *easy* for customers to leave the service? That’s because they are short sighted. These are *not your customers now*. Try to lock them in *before* they become your customers, and you’ll just lock them *out*. But if you make an honest promise that it will be easy to back out of the service if they’re not happy, and suddenly you eliminate one more barrier to entry. And, as we learned, eliminating even a single barrier to entry can have a dramatic effect on conversions, and over time, when you knock down that last barrier to entry, people will start flooding in, and life will be good for a while. Until somebody does the same thing to you.
