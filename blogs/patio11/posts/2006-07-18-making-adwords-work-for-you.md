---
title: "Making AdWords Work For You"
date: 2006-07-18
url: https://www.kalzumeus.com/2006/07/19/making-adwords-work-for-you/
slug: making-adwords-work-for-you
word_count: 2154
---


There don’t seem to be any good crystalizations of the reams of data on the Internet, and the one thats do exist are on crazily SEO’d sites and I always feel a little dirty visiting them, so I thought I’d write this up.


The most important thing for succeeding with AdWords is that **you need to install analytics software**. Let me repeat that: you will have no clue whether your (potentially very expensive) AdWords campaign is actually making money unless you **install analytics software**. I really love Google Analytics because of its tight integration with AdWords, but if you want to use somebody else, hey, whatever floats your boat. And you need to enable conversion tracking for at least your trial downloads and ideally for your completed purchases.


The easiest way to do this is scatter your site with download links that all go to a central page (mine is thanks_for_downloading.htm) which has the tracking Javascript on it and a meta-refresh to the executable, plus a “if you don’t see your download starting within 5 seconds click here”. One thing I do is make sure all my links use text like “You should download our free trial to …” so that everyone who clicks on the link knows that they are committing to a download. The reason behind this is that if they click on a link saying “Free Trial” or something, see the download begin, and immediately hit cancel you’ll never know and you’ll think that person was a successful conversion.


OK, got your Analytics set up? Alright, here we go:


1) **Eyes on the prize.** The prize is conversions, to your trial and eventually to being satisfied customers who have paid you money. You’ll be buried in numbers — click-through rate (CTR), cost per click (CPC), number of clicks, number of impressions, conversion rate (CR), cost per conversion (aka cost per action, CPA), blah blah yackety smackety, and you can slice this data a million ways. There are only two numbers you care about: CR and CPA. Everything else is noise — potentially meaningful noise when you’re optimizing your ad, but otherwise its just noise. The only thing that will get you money is to get people to download your trial and decide to take the plunge. If it costs you $30 per trial download and you sell a $24.95 product, congratulations, you should a) get serious about optimizing your ads or b) cancel AdWords today.


2) **Opt out of the Google Content Network**. You can find this option in campaign settings. There is one simple reason for this: these sites fail to deliver customers who convert, which hurts CR and ups CPA. Or, in plain English, you pay them money and get nothing in return, so don’t pay them money! If you mistakenly leave them on for a week, like I did, you’ll very quickly figure out why: the vast majority of clicks are from “Made for AdSense” (MFA) pages, which are generally scrapes of content which exists elsewhere on the Internet, and more than a little bit shady. I assume that most of these folks are either site owners, bots, or users who are clueless enough that they land on a MFA page and take it to be valuable information (when they almost never are). None of these folks convert.


3) **Segment, segment, segment**. You can make multiple ad groups within a single campaign. Make use of this feature. An Ad Group should be thematically coherent: for example, one of my Ad Groups is based around the theme “You’re searching for something to make bingo cards, I provide something to make bingo cards”. Another is “You’re searching for information about Dolch sight words, I provide a resource to teach Dolch sight words”. If you’re smart your software solves one or several pains — pitch your ads on a per-pain basis. Why do this when you could save time by throwing everything in a single ad group? Because if you segment, your CTRs and CRs will be higher, since you’re showing the most relevant ad text to the searcher.


3) **Watch that CTR, but not toooo closely**. The best guess is that the average CTR is about 2%. If you’re at 1%, you’re still OK. If you’re at significantly above 2%, you’re *probably* OK (but see below). But if you’re below 1%, you’re going to start costing yourself money soon. The reason is you have a Quality Score, which is essentially a witches brew of factors that Google uses to determine whether they display your ad or not at a particular price. If your QS is low, Google will keep bumping up your minimum bid to be displayed. That costs you money, so you want to keep your QS nice and high, and one easy and transparent way to do so is keeping your CTR healthy.


4) **Writing ad copy**. God darn it Jim I’m an engineer, not a marketer. Here’s everything I know: include a call to action (“Download our free trial today.” works decently for me), make sure you use keywords from the search in the ad copy if possible, and speak directly to the pain. You can try out many ads at once — Google will automagically pick the one with the highest CTR for you. Thats Good For Google, since high CTRs mean they make money, but its not necessarily Good For You. You want ads with a high CR, because those are the ones that make *you* money. This means you should periodically check how your CR is doing and pull ads that aren’t making you money.


5) **The importance of landing pages**. You’ve got five seconds to overwhelm someone’s inborn defenses against spending time/money on your product. Make the use of them. Don’t be the silly advertiser who just directs everyone to the main page — have an optimized landing page for each ad group (or segment even beyond that — for each keyword, for each ad variation, whatever you can afford on your time budget). This means pages which speak to the pains which you solve. You want an example? Compare [www.bingocardcreator.com](http://www.bingocardcreator.com), which is a generic pitch of my software to my main niche (teachers), to my [landing page for sight words](http://www.bingocardcreator.com/dolch-sight-words-bingo.htm). Anyone landing on that page was looking for resources to teach sight words and clicked on an advertisement promising some variation of “I will save you time and money playing sight words bingo”. I greet them in a personal manner, immediately tell them download the free trial (something like 30% of the clickers do so immediately), and then go about pitching the activity (talking about the pain, basically) and providing them lots of reasons to believe that I’m the best possible solution to the pain.


6) **You probably don’t want to let Google budget for you.** Well, in one sense you do — you’ll establish a maximum you want to pay per month and Google will cap your expenditures at or near that maximum. This is good. What you don’t want is for Google to “spend up” to your maximum, which is what they will do by default if you let them budget for you. Lets pretend I have a budget of $30 for 30 days (I do). See, what happens under that setting is that they will adjust your bid timed to reach exactly $30 in 30 days… But if you only spend $5 in your first 10 days, then they’ll adjust your budget to hit the $25 target in 20 days… and they do this by bidding up your maximum cost per click. Supposing your click volume is not yet high enough, they’ll raise it again and again and again. You’re almost guaranteed to make your monthly limit. Great for Google, but there is a point at which you’re not making money (where your CPA * your conversion for demos to purchases exceeds your net profit per sale). You’re better off manually limiting your expenditure.


7) **There is likely more traffic than you can afford to service**. For a small advertiser, you are probably not able to absorb a click from everyone who wants to click on an ad in that day. So, reduce your maximum bid. It doesn’t matter if you’re in 1st position, 2nd position, 3rd position, or 17th position if you’re still maxing out your budget every day — I haven’t seen any difference in conversion rates based on where the ad is on the page (there is obviously a difference in CTR but, oh well, CTR only makes Google money).


8) **You only want qualified buyers to click your ads**. Here’s an issue for my business: I sell a program to make bingo cards which is targetted at teachers. I’ll accept orders from people who are not teachers, but I know if you’re not a teacher or a parent you’re highly unlikely to want to buy my product. So if you’re looking for something to print bingo cards for the game on Tuesday night I’m happy to show you my website for free (organic search) but not happy to pay a nickle to pitch my site to you. Yet I routinely end up paying $.15 to pitch to this person, because one of my campaigns is overly broad. You don’t want overly broad campaigns. There are three ways to target your niche more precisely:

- Exclusion words. I pay for someone searching “make custom bingo cards”, with broad matching (it will hit “make custom reading bingo cards”, for example). However, I can specify exclusion words, which means if they search for foo they don’t get one of my ads regardless of how many of my keywords they hit. Consider carefully whether you really want to pay for anyone searching for “free keyword keyword keyword”. Currently, my conversion from people searching for free stuff is pretty nice (its actually higher than folks who didn’t specify if they were searching for free stuff or not). Similarly, if your keywords are ambiguous, exclude words which would resolve the ambiguity against you. For example, if you’re selling gardening software to people searching for “potter” (I don’t know why you would do this, but play along), you’d want to exclude Harry Hermione Ron magic Hogwarts etc etc. Note that excluding words does not appear to decrease the amount of money you have to pay (I’m not totally positive about this), so you’re probably better off not paying for Potter in any event.
- Speaking your customers language. In general, especially if other software exists in your niche, the two to three word description of what your software does will be expensive. On the other hand, natural variations such as “How do I ” are likely to be very, very cheap. Listing off a couple dozen variations of that natural search query gets you lots of very qualified traffic for very cheap.
- Make your ad text clear as to what they get for clicking. Suppose you could come up with some ad text with an obscenely high CTR by slightly stretching the truth as to what was behind the link. This is NOT a good idea. Remember, CTR is money for Google, not for you. Ideally, you’d want ad text that turned off 100% of people who would not convert while still capturing 100% of people who would. You’ll not likely be able to do that, but you can audition various ad texts to see what gets the lower CPA. Here’s three ads from my “you’re looking for software to print bingo cards” ad group:


> [ Print Custom Bingo Cards](http://www.bingocardcreator.com/)


> Your own text or use our lessons.


> Download our free trial now!


> www.BingoCardCreator.com


> [
>  ](http://www.bingocardcreator.com/)


> [Bingo Cards for Teaching](http://www.bingocardcreator.com/)


> Print custom cards on your own PC.


> Download our free trial.


> `        <font color="green">www.BingoCardCreator.com</font> <a href="http://www.bingocardcreator.com/" onclick="javascript:_gaq.push(['_trackEvent','outbound-article','http://www.bingocardcreator.com']);" target="_blank"></a>
> `


> [Lessons Ready In Minutes](http://www.bingocardcreator.com/)


> Make your budget go farther and
> save prep time. Try for free!


> www.BingoCardCreator.com


[ ](http://www.bingocardcreator.com/)

- Here’s the results: variation #1 has a high CTR (6%) and a high CR (20%ish), but the CPA is poor compared to targetting teachers specifically (roughly quadruple what I pay elsewhere). The reason is that I pay a lot of money to pitch to folks who weren’t interested in teaching. Variation #2, on the other hand, has a lower CTR (4.5%) but a higher CR (unstable since I’ve only had it up for two days, but I’m estimating it will settle in the 40% region). Doing the math, thats roughly 50% extra downloads for the same amount of money (or, equivalently, 1/3rd off my CPA). Variation #3 just sucks as an ad (sub-1% CTR, no significant conversions) and it will be killed right after I get done with this post. You can see why it sucks, too: its not pitching anything at the pain people are searching for.
