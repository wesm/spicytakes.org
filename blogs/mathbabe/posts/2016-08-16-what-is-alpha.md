---
title: "What is alpha?"
date: 2016-08-16
url: https://mathbabe.org/2016/08/16/what-is-alpha/
word_count: 942
---


Last week on [Slate Money](http://www.slate.com/articles/podcasts/slate_money/2016/08/hedge_funds_declining_u_s_productivity_and_vagina_technology_on_this_week.html) I had a disagreement, or at least a lively discussion, with Felix Salmon and Josh Barro on the definition of alpha.


They said it was anything that a portfolio returned above and beyond the market return, given the amount of risk the portfolio was carrying. That’s not different from [how wikipedia defines alpha](https://en.wikipedia.org/wiki/Alpha_(finance)), and I’ve seen it said in more or less this way in a lot of places. Thus the confusion.


However, while working as a quant at a hedge fund, I was taught that alpha was the return of a portfolio that was *uncorrelated* to the market.


It’s a confusing thing to discuss, partly because the concept of “risk” is somewhat self-referential – more on that soon – and partly because we sometimes embed what’s called the [capital asset pricing model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model) (CAPM) into our assumptions when we talk about how portfolio returns work.


Let’s start with the following regression, which refers to stock-based portfolios, and which defines alpha:


Now, the term term  refers to the risk-free rate, or in other words how much interest you get on US treasuries, which we can approximate by 0 because it’s easier to ignore them and because it’s actually pretty close to 0 anyway. That cleans up our formula:


In this regression, we are fitting the coefficients  and  to many instances of time windows where we’ve measured our portfolio’s return  and the market’s return  Think of market as the S&P500 index, and think of the time windows as days.


So first, defining alpha with the above regression does what I claimed it would do: it “picks off” that part of the portfolio returns that are correlated to the market and put it in the beta coefficient, and the rest is left to alpha. If beta is 1, alpha is 0, and if the error terms are all zero, you are following the market exactly.


On the other hand, the above formulation also seems to support Felix’s suggestion that alpha is the return that is not accounted for by risk. The thing is, it’s true, at least according to the [CAPM theory](https://en.wikipedia.org/wiki/Capital_asset_pricing_model) of investing, which says you can’t do better than the market, that you’re rewarded by market your risk in a direct way, and that everyone knows this and refuses to take on other, unrewarded risks. In particular, alpha in the above equation *should* be zero, but anything “extra” that you earn beyond the expected market returns would be represented by alpha in the above regression.


So, are we actually agreeing?


Well, no. The two approaches to defining alpha are very different. In particular, my definition has no reference to CAPM. Say for a moment we don’t believe in CAPM. We can still run the regression above. All we’re doing, when we run that regression, is measuring the extent to which our portfolio’s returns are “explained” by its overlap with the market.


In particular, we do not expect the true risk of our portfolio to be apparent in the above equation. Which brings us to how risk is defined, and it’s weird, because it cannot be directly measured. Instead, we typically infer risk from the volatility – computed as standard deviation – of past returns.


This isn’t a terrible idea, because if something moves around wildly on a daily basis, it would appear to be pretty risky. But it’s also not the greatest idea, as we learned in 2008, because lots of credit instruments like credit default swaps move very little on a daily basis but then suddenly lose tremendous value overnight. So past performance is not always indicative of future performance.


But it’s what we’ve got, so let’s hold on to it for the discussion. The key observation is the following:


> The above regression formula only displays the market-correlated risk, and the remaining risk is unmeasured. A given portfolio might have incredibly wild swings in value, but as long as they are uncorrelated to the market, they will be invisible to the above equation, showing up only in the error terms.
> Said another way, alpha is not truly risk-adjusted. It’s only market-risk-adjusted.


We might have an investment portfolio with a large alpha and a small beta, and someone who only follows CAPM theory would tell me we’re amazing investors. In fact hedge funds try to minimize their relationship to market returns – that’s the “hedge” in hedge funds – and so they’d want *exactly* that, a large alpha, a tiny beta, and quite a bit of risk. [One caveat: some people stipulate that a lot of that uncorrelated return is [fabricated through sleazy accounting](http://www.pionline.com/article/20050919/PRINT/509190734/investors-get-less-while-risking-more-reports-say).]


It’s not like I am alone here – for a long time people have been aware that there’s lots of risk that’s not represented by market risk – for example, other instrument classes and such. So instead of using a simplistic regression like the one above, people generalize everything in sight and use the [Sharpe ratio](https://en.wikipedia.org/wiki/Sharpe_ratio), which is the ratio of returns (often relative to some benchmark or index) to risks, where risks are measured by more complicated volatility-like computations.


However, that more general concept is also imperfect, mostly because it’s complicated and highly gameable. Portfolio managers are constantly underestimating the risk they take on, partly because – or entirely because – they can then claim to have a high Sharpe ratio.


How much does this matter? People have a colloquial use for the word alpha that’s different from my understanding, which isn’t surprising. The problem lies in the possibility that people are bragging when they shouldn’t, especially when they’re hiding risk, and especially especially if your money is on the line.
