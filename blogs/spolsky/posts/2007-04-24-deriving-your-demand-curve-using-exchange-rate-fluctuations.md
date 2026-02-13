---
title: "Deriving your demand curve using exchange rate fluctuations"
date: 2007-04-24
url: https://www.joelonsoftware.com/2007/04/24/deriving-your-demand-curve-using-exchange-rate-fluctuations/
word_count: 499
---


When I wrote that article about [how to set prices for software](https://www.joelonsoftware.com/articles/CamelsandRubberDuckies.html), I generally concluded that in many ways you were completely doomed:


> “The more you learn about pricing, the less you seem to know… I’ve been nattering on about this topic for well over 5000 words and I don’t really feel like we’re getting anywhere.”


In particular, to set prices well, you need to be able to plot your customers’ demand curves, and it’s almost impossible to figure out what your demand curve is, because it’s so hard to charge different customers different amounts and get any kind of reliable data.


Sometimes, though, you luck out.


If you’ve been selling a product priced in US dollars to customers in Europe, you might actually have a bit of useful data. You see, the US dollar has dropped a lot in the past year. As the dollar falls, your product has become cheaper and cheaper for Europeans.


I looked back on the last year of FogBugz data, dividing the price by the pound sterling exchange rate, and discovered that our single-user license have fluctuated between 64 and 74 pounds, while our ten packs have fluctuated between 49 and 56 pounds, approximately.


That gives me just enough data to plot a segment of the demand curve for English UK customers.


The data is not very conclusive, but it does support some things that I might have believed anyway:

- Large customers (on the left, enjoying the volume discount) are not price sensitive. There does not appear to be any correlation between price and sales. These are larger businesses that are used to spending money on things, and it’s not their money, anyway.
- Small customers (on the right) *are* price sensitive. They’re startups and small ISVs that are used to watching their budget. They exhibit a classic downward-sloping demand curve as economics would predict, and they like prices that end in 9 a bit better than prices around it (there’s a small bump below £70).


On this curve, demand is measured in units purchased per day in England the UK. I’ve left the Y-axis unlabeled because it’s confidential sales data, but the shape is accurate.


There are a lot of reasons to be skeptical about this data:

- Since the dollar has basically been marching downwards, lower prices (in £) correspond to later dates. I’ve tried to adjust for this but there could be any number of other reasons why sales are increasing in England the United Kingdom.
- The data are only based on sales in England the UK, where different economic factors may be in effect that don’t apply to US customers.
- Many of our customers may not be looking at the actual exchange rate, but estimating based on their imperfect approximate knowledge of exchange rates (just dividing by 2, for example, is probably common), or thinking in $.


Still, you may find this a useful technique to learn something about the demand curve for your product.
