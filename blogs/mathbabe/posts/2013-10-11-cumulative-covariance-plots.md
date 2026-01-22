---
title: "Cumulative covariance plots"
date: 2013-10-11
url: https://mathbabe.org/2013/10/11/cumulative-covariance-plots/
word_count: 503
---


One thing I do a lot when I work with data is figure out how to visualize my signals, especially with respect to time.


Lots of things change over time – relationships between variables, for example – and it’s often crucial to get deeply acquainted with how exactly that works with your in-sample data.


Say I am trying to predict “y”: so for a data point at time t, we’ll say we try to predict y(t). I’ll take an “x”, a variable that is expected to predict “y”, and I’ll demean both series x and y, hopefully in a causal way, and I will rename them x’ and y’, and then, making sure I’ve ordered everything with respect to time, I’ll plot the cumulative sum of the product x'(t) * y'(t).


In the case that both x'(t) and y'(t) have the both sign – so they’re both bigger than average or they’re both smaller than average, this product is positive, and otherwise it’s negative. So if you plot the cumulative sum, you get an upwards trend if things are positively correlated and downwards trend if things are negatively correlated. If you think about it, you are computing the numerator of the correlation function, so it is indeed just an unscaled version of total correlation.


Plus, since you ordered everything by time first, you can see how the relationship between these variables evolved over time.


Also, in the case that you are working with financial models, you can make a simplifying assumption that both x and y are pretty well demeaned already (especially at short time scales) and this gives you the cumulative PnL plot of your model. In other words, it tells you how much money your model is making.


So I was doing this exercise of plotting the cumulative covariance with some data the other day, and I got a weird picture. It kind of looked like a “U” plot: it went down dramatically at the beginning, then was pretty flat but trending up, then it went straight up at the end. It ended up not quite as high as it started, which is to say that in terms of straight-up overall correlation, I was calculating something negative but not very large.


But what could account for that U-shape? After some time I realized that the data had been extracted from the database in such a way that, after ordering my data by date, it was hugely biased in the beginning and at the end, in different directions, and that this was unavoidable, and the picture helped me determine exactly which data to exclude from my set.


After getting rid of the biased data at the beginning and the end, I concluded that I had a positive correlation here, even though if I’d trusted the overall “dirty” correlation I would have thought it was negative.


This is good information, and confirmed my belief that it’s always better to visualize data over time than it is to believe one summary statistic like correlation.
