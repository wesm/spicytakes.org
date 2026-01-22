---
title: "The $heriff tool: detect price discrimination while you shop"
date: 2015-07-10
url: https://mathbabe.org/2015/07/10/the-heriff-tool-detect-price-discrimination-while-you-shop/
word_count: 572
---


Today I want to tell you about [$heriff](http://sheriff.dynu.com/views/home), an awesome new tool I learned about recently. It’s currently an add-on to the Firefox and IE browsers, but it will be compatible with Chrome soon. I mention this because I think you will want to use it, partly for the good of scientific discovery, but partly for your own good.


Because here’s what $heriff does for you. It allows you to see how prices for goods you’re interested in buying would change depending on where the request is coming from. And sometimes the answer is “a lot,” even on [Staples.com](http://www.wsj.com/articles/SB10001424127887323777204578189391813881534) or [Amazon.com](http://arxiv.org/pdf/1307.4531v1.pdf).


I talked to one of the creators, Nikolaos Laoutaris, who works as a computer science researcher in Barcelona. Nikos described how he came across the idea of creating $heriff. Namely, he and a friend were discussing their upcoming vacation to a town in Austria, and they were both looking into booking the same type of room at the same hotel (at the same time, since they were doing it over Skype) and they were seeing very different prices.


The way it actually works is that there’s a way to “check” prices when you come across one, and the results pop up in a separate window. Here’s a screenshot of what happened with Nikos showed me $heriff checking on the price of a fancy camera at [digitalrev.com](http://www.digitalrev.com/):


The list corresponds to what price showed up when a bunch of servers at academic institutions were asked to send a price request that $heriff extracted from the local webpage. To be clear, your personal request for price, coming from your browser, might depend on location as well as your cookies and referral url, among other things, but these other prices correspond to “clean browsers,” with no browsing history, and no login history, making a request from a specific location. So those price variants correspond to location changes only.


There’s also a space below for “Results from local users,” and this is where you come in. If there’s a person with a $heriff add-on in your local area, the idea would be to use the information your browser collects to allow someone to compare their price with your price. In this way we would (slowly) also learn how prices change depending on browsing history. The more people who use $heriff and donate their data to the project (third party cookies, some browsing history, and prices), the faster we will learn about how prices vary.


Among other things, this could be a way of figuring out how to intentionally set your input data so that you get the best price for a given product.


A few notes:

- Local sales tax and shipping costs are valid reasons for prices to depend on location of the buyer, but they are typically added later, after the prices are shown.
- It’s possible that tariffs come into play, but they don’t seem consistent. Also, the prices vary too much to be accounted for by tariffs.
- Nikolaos Laoutaris and his colleagues [have also been doing great work](http://conferences.sigcomm.org/hotnets/2012/papers/hotnets12-final94.pdf) looking into how people are tracked, and how such information is used to steer them into environments of “search discrimination,” which means that which products or offers they are shown changes, rather than the prices themselves.
- Also, he’s part of a cool project called the [Data Transparency Lab](http://www.datatransparencylab.org/).


Get started with $heriff or learn more about Nikos’s work, by going [here](http://sheriff.dynu.com/views/home).
