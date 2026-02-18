---
title: "Things you should know about stock options before negotiating an offer"
date: 2015-12-30
url: https://jvns.ca/blog/2015/12/30/do-the-math-on-your-stock-options/
slug: do-the-math-on-your-stock-options
word_count: 2469
---


Are you considering an offer from a private company, which involves stock options? Do you think those stock options might be worth something one day? Are you confused? Then read this! I’ll give you some motivation to learn more, and a few questions to consider asking your prospective employer.


I polled people on Twitter and 65% of them said that they’ve [accepted an offer without understanding how the stock options work](https://twitter.com/b0rk/status/682041239508746240).


I have a short story for you about stock options. First: stock options are BORING AND COMPLICATED AND AWFUL. They are full of taxes, which we all know are awful. Some people think they’re fun and interesting to learn about. I am not one of those people. However, if you have an offer that involves stock options, I think you should learn a little about them anyway.
All of the following assumes that you work for a private company that is still private when you leave it.


In this post I don’t want to explain comprehensively how options work. (For that, see [how to value your startup stock options](http://robertheaton.com/2015/11/02/how-to-value-your-startup-stock-options/) or [The Open Guide to Equity Compensation
](https://github.com/jlevy/og-equity-compensation)) Instead I want to tell you a story, and convince you to ask more questions, do a little research, and do more math.


I took a job 2 years ago, with a company with a billion-dollar-plus valuation. I was told “we pay less than other companies because our stock option offers are more generous”. Okay. I understood exactly nothing about stock options, and accepted the offer. To be clear: I don’t *regret* accepting the offer (my job is great! I ❤ my coworkers). But I do wish I’d understood the (fairly serious) implications at the time.


From my offer letter:


> the offer gives you the option to purchase [redacted]
> shares of Stripe stock. [We bias] our offers to
> place weight on your ownership in the company.


> I’m happy to talk you through how we think about the value of the
> options. As far as numbers: there are approximately [redacted]
> outstanding shares. We can talk in more detail about the current valuation and the strike price for your options.


This is a good situation! They were being pretty upfront with me. I had access to all the information I needed to do a little math. I did not do the math. Let me tell you how you can start with an offer letter like this and understand what’s going on a little better!


### what the math looks like (it’s just multiplication)


The math I want you to do is pretty simple. The following example stock option offer is not at all my situation, but there are some similarities that I’ll explain in a minute.


The example situation:

- stock options you’re being offered: 500,000
- vesting schedule: 4 years. you get 25% after the first year, then the rest granted every month for the remainder of the time.
- outstanding shares: 100,000,000 (the number of total shares the company has)
- company’s current valuation: 1 billion dollars


This is an awesome start. You have options to buy 0.5% of the shares of a billion dollar company. What could be better? If you stay with the company until it goes public or dies, this is easy. If the company goes public and the stock price is more than your exercise price, you can exercise your options, sell as much of the stock as you want to, and make money. If it dies, you never exercise the options and don’t lose anything. win-win. This is where options excel.


However! If you want to *ever* quit your job (in the next 5 years, say!), you may not be able to sell any of your stock for a long time. You have more math to do.


ISOs (the usual way companies issue stock options) expire 3 months after you quit. So if you want to use them, you need to buy (or “exercise”) them. For that, you need to know the exercise price. You also need to know the fair market value (current value of the stock), for reasons that will become apparent in a bit. We need a little more data:

- exercise price or strike price: $1. (This is how much it costs, per share, to buy your options.)
- current fair market value: $1 (This is how much each share is theoretically worth. May or may not have any relationship to reality)
- fair market value, after 3 years: $10


All this is information the company should tell you, except the value after 3 years, which would involve time travel. Let’s see how this plays out!


### time to quit


Okay awesome! You had a great job, you’ve been there 3 years, you worked hard, did some great work for the company, you want to move on. What next? Since your options vested over 4 years, you now have 375,000 options (75% of your offer) that you can exercise. Seems great.


Surprise! Now you need to pay hundreds of thousands of dollars to invest in an uncertain outcome. The outcomes (IPO, acquisition, company fails) are all pretty complicated to discuss, but suffice to say: you can lose money by investing in the company you work for. It may be a good investment, but it’s not risk-free. Even an acquisition can end badly for you (the employee). Let’s see exactly how it costs you hundreds of thousands of dollars:


**Pay the exercise price**:


The exercise price is $1, so it costs $375,000 to turn your options into stock. Your options go *poof* in three months, but you can keep the stock if you buy it now.


What?! But you only have 300k in the bank. You thought that was… a lot. You make an amazing salary (even $200k/year wouldn’t cover that). You can still afford a lot of it though! Every share costs $1, and you can buy as many or as few as you want. No big deal.


You have to decide how much money you want to spend here. Your company hasn’t IPO’d yet, so you’ll only be able to make money selling your shares if your company eventually goes public *AND* sells for a higher price than your exercise price. If the company dies, you lose all the money you spent on stock. If the company gets acquired, the outcome is unpredictable, and you could still get nothing for all the money you spend exercising options.


Also, it gets worse: taxes!


**Pay the taxes**:


The value of your stock has gone up! This is awesome. It means you get the chance to pay a lot of taxes! The difference in value between $1 (the exercise price) and $10 (the current fair market value) is $9. So you’ve potentially made $9 * 375000 = 3.3 million dollars.


Well, you haven’t actually made that, since you’re buying stock you can’t sell (yet). But your local tax agency *thinks* you have. In Canada (though I’m not yet sure) I might have to pay income tax on that 3 million dollars, whether or not I have it. So that’s an extra 1.2 million in taxes, without any extra cash.


The tax implications are super boring and complicated, and super super important. If you work for a successful company, and its value is increasing over time, and you try to leave, the taxes can make it totally unaffordable to exercise your options. Even if the company wasn’t worth a lot when you started! See for instance [this person describing how they can’t afford the taxes on their options](https://news.ycombinator.com/item?id=10695125). Early exercise can be a good defense against taxes (see the end of this post).


### my actual situation


I don’t want to get too far into this fake situation because when people tell me fake situations, I’m like “ok but that’s not real why should I care.” Here’s something real.


I do not own 0.5% of a billion dollar company. In fact I own 0%. But the company I work for *is* valued at more than a billion dollars, and I *do* have options to buy some of it. The options I’m granted each year would cost, very roughly, $100,000 (including exercise prices + taxes). Over 4 years, that’s almost half a million dollars. My after-tax salary is less than $100,000 USD/year, so by definition it is impossible for me to exercise my options without borrowing money.


The total amount it would cost to exercise + pay taxes on my options is more than all of the money I have. I imagine that’s the case for some of my colleagues as well (for many of them, this is their first job out of school). If I leave, the options expire after 3 months. I still do not understand the tax implications of exercising at all. (it makes me want to hide under my bed and never come out)


I was really surprised by all of this. I’d never made a financial decision much bigger than buying a $1000 plane ticket or signing a lease before. So the prospect of investing a hundred thousand dollars in some stock? Having to pay taxes on money that I do not actually have? super scary.


So the possibilities, if I want to ever quit my job, are:

1. exercise them somehow (with money I get from ??? somewhere ???).
2. give up the options
3. find a way to sell the options or the resulting stock


There are several variations on #3. They mostly involve cooperation from your employer – it’s possible that they’ll let you sell some options, under some conditions, if you’re lucky / if they like you / if the stars are correctly aligned. This post [How to sell secondary stock](http://blog.eladgil.com/2014/01/how-to-sell-secondary-stock.html) says a little more (thanks [@antifuchs](https://twitter.com/antifuchs)!). [This HN comment](https://news.ycombinator.com/item?id=10705646) describes a situation where someone got an offer from an outside investor, and the investor was told by the company to not buy from him (and then didn’t buy from him). Your employer has all the power.


Again, this isn’t a disaster – I have a good job, which pays me a SF salary despite me living in Montreal. It’s a fantastic situation to be in. And certainly having an option to buy stock is better than having nothing at all! But you can ask questions, and I like being informed.


### Questions to ask


Stock options are very complicated. If you start out knowing nothing, and you have an offer to evaluate this week, you’re unlikely to be able to understand every possible scenario. But you can do better than me!


When I got an offer, they were super willing to answer questions, and I didn’t know what to ask. So here are some things you could ask. In all this I’m going to assume you work for a US company.


**Basic questions:**

- how many stock options (# shares)
- vesting schedule (usually 4 years / 1 year “cliff”)
- how many outstanding shares
- company’s current valuation
- exercise price (per share)
- fair market value (per share: a made-up number, but possibly useful)
- if they’re offering ISOs, NSOs, or RSUs
- how long after leaving do you have to exercise?


Then you can do some basic math and figure out how much it would cost to exercise the options, if you choose to. (I have a friend who paid $1 total to exercise his stock options. It might be cheap!)


**More ambitious questions**


As with all difficult questions, before you accept an offer is the best time to ask, because it’s when you have the most leverage.

- will they let you sell stock to an outside investor?
- If you can only exercise for 3 months after leaving, is that negotiable? ([pinterest gives you the option of 7 years and worse tax implications. can they do the same?](http://www.businessinsider.com/pinterest-will-let-employees-exercise-options-for-seven-years-after-leaving-2015-3))
- If the company got sold for the current valuation (2X? 10X?) in 2 years, what would my shares be worth? What if the company raises a lot of money between now and then?
- Can they give you a summary of what stock & options other people have? This is called the “cap table”. (The reason you might want to know this: often VCs are promised that they’ll get their money *first* in the case of any liquidation event. Before you! Sometimes they’re promised at least a 3x return on their investment. This is called a “liquidation preference” 1.)
- What other downside protection do the VCs have? (see [this article](https://www.pehub.com/2015/05/unicorn-deals-offer-venture-investors-plenty-of-downside-protection/) for some of the possibilities)
- Do the VCs have participation? (there’s a definition of [participation and other stock option terms here](https://www.fenwick.com/publications/pages/explanation-of-certain-terms-used-in-venture-financing-terms-survey.aspx))
- Can you early exercise your options? I know someone who early exercised and saved a ton of money on taxes by doing it. [This guide](https://github.com/jlevy/og-equity-compensation) talks more about early exercising. 2
- Do your options vest faster if the company is acquired? What if you get terminated? (these possibilities are called “single/double trigger”)


If you have more ideas for good questions, [tell me!](https://twitter.com/b0rk) I’ll add them to this list.


### #talkpay


I think it’s important to talk about stock option grants! A lot of money can be at stake, and it’s difficult to talk about amounts in the tens or hundreds of thousands.


There’s also some tension about this topic because people get very emotionally invested in startups (for good reason!) and often feel guilt about leaving / discussing the financial implications of leaving. It can feel disloyal!


But if you’re trying to make an investment decision about thousands of dollars, I think you should be informed. Being informed isn’t disloyal :) The company you work for is informed.


### Do the math


The company making you an offer has lawyers and they should know the answers to all the questions I suggested. They’ve thought very carefully about these things already.


I wish I’d known what questions to ask and done some of the math  before I started my job, so I knew what I was getting into. Ask questions for me! :) You’ll understand more clearly what investment decisions might be ahead of you, and what the financial implications of those decisions might be.


Thanks for Leah Hanson and Dan Luu for editing help!


---

1. On liquidation preferences: Suppose a VC invests 100M, and is promised a 3x return on investment. If the company later sells for 300M (or less), the VC gets all of it and you get nothing. That’s it. Liquidation preferences are important to know about. ↩︎
2. On early exercise: I also know people who have *lost* a lot of money by early exercising, if it’s expensive and turns out to be worth nothing. The important thing is to understand what you’re allowed to do. ↩︎
