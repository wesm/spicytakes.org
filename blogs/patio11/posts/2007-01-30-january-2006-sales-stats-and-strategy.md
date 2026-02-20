---
title: "January 2007 Sales, Stats, and Strategy"
date: 2007-01-30
url: https://www.kalzumeus.com/2007/01/31/january-2006-sales-stats-and-strategy/
slug: january-2006-sales-stats-and-strategy
word_count: 823
---


**Executive summary**: January was my best month yet. I’m on target for making my goal of $1,000 a month sales by April. The redesign of my purchase page has been extraordinarily effective, particularly at moving people towards buying CDs. Google Checkout is saving me a not-insubstantial bit of money. AdWords, on the other hand, is borked and has a heavily negative ROI.


Sales:


> Total Sales: 28 (includes 5 CDs, 1 refund due to showstopper bug in Mac version)
> Gross Income: $698.65
> Income Less Fulfillment Costs (Paypal, CD fulfillment): **$655.70**


Expenses:


> GoDaddy: $5
> Web Hosting: $7 (I turned off Traffic Facts, wasn’t using it anymore on a regular basis)
> AdWords: $90 budgeted
> Total Expenses: **$102**


Total Profit: **$553.70**


Time accounting: I estimate I spent approximately 6 hours of work on Bingo Card Creator in January. Roughly half of that was development (finishing touches on v1.05, which has been in the works since about October, and also some hunting for bugs in the Mac version discovered after release) , 20 minutes answering emails and fulfilling those CD orders, and the remainder blogging, keeping track of AdWords, firing Robosoft to submit v1.05 to the major sites, and performing various and sundry tasks. I also spent approximately 4 hours working on my 2006 taxes, a major portion of which was caused by Bingo Card Creator.


Selected Key Statistics:


Number of sales directly attributable to Google AdWords: 1. (Yes, Virginia, that IS equivalent to taking $65 out my my wallet and setting fire to it.) Yep, need to get AdWords under control or cancel it, sooner rather than later. No reason to pay Google a tax just for the privilege of paying them a tax. Also intending to look into AdCenter when I get the time to do so.


Number of hits on typical weekday: 300.


Number of hits on typical weekend: 100. This is roughly equivalent to my typical peak performance back in November.


Visitor to download conversion rate: Steadily falling, to 16% overall. A major contributor to this is the fact that I’m getting insane traffic numbers from the search for “bingo cards” on Google, and that traffic is relatively poorly qualified (12% or so conversion rate). Highly qualified traffic, such as people responding to my CPC ads, continues to convert at about 25%. Yahoo and MSN are in the 18% range. I hope to improve my conversion rate later by making a fairly significant design change related to how the Download Free Trial button works… we’ll see if that helps.


Downloads: Google Analytics reports 1,100, up 200 from December and 300 from November. Hard to believe that back in September I was ecstatic when this number hit 200. I receive a major but probably declining portion of my total downloads from download sites, and I have stopped counting those exactly since the number they provide me is not actionable (regardless of whether it goes up or down I still submit all new version to every site that will take it automatically, and don’t see myself changing that policy anytime soon).


Confirmed Installs: 235. This has not been keeping pace with my increasing download numbers. I’m not entirely sure why. Interestingly, digging into the logs shows me that no less than a quarter of my paying customer base is checking for a new version at least monthly. This gives me a warm fuzzy feeling inside.


Priorities for February:

1. Get a handle on AdWords and AdCenter. AdWords needs to have positive ROI or it needs to get cut, it is as simple as that.
2. Redesign download and download confirmation page. I don’t like the lack of user friendliness for the download on some browser/OS combos, particularly IE7, which will only gain in market share in my segment in the coming months.
3. Add more content to website. Need to find a new method of attack to get some more sales growth rather than just resting on my laurels, which candidly is a fairly accurate description of my marketing for 3 months now.
4. Re-ship 1.05 on Mac after bugs are squashed. Build shrine to Andrey, my beleaguered Mac testing department.
5. Start using source control software (I nearly had a heart attack trying to revert to a Mac version that was known to be good).
6. Redo internal model of a bingo card. I realized when adding one of the key 1.05 features that I am passing 6 arguments through about 4 different classes because my abstraction that captures what a bingo set is is a poor abstraction for capturing what a bingo card is. The printer cares rather more about the card and less about the set. Time to add a new abstraction, which will greatly simplify changing the presentation of the card in the future, hopefully allowing me to add new features for printing and get Print Preview working. (That would make a decent 1.051 release.)
