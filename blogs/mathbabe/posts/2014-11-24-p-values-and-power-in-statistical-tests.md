---
title: "P-values and power in statistical tests"
date: 2014-11-24
url: https://mathbabe.org/2014/11/24/p-values-and-power-in-statistical-tests/
word_count: 1000
---


Today I’m going to do my best to explain [Andrew Gelman’s recent intriguing post on his blog](http://andrewgelman.com/2014/11/17/power-06-looks-like-get-used/) for the sake of non-statisticians including myself (hat tip Catalina Bertani). If you are a statistician, and especially if you are Andrew Gelman, please do correct me if I get anything wrong.


Here’s [his post](http://andrewgelman.com/2014/11/17/power-06-looks-like-get-used/), which more or less consists of one picture:


I decided to explain this to my friend Catalina, because she asked me to, in terms she could understand as a student of midwifery. So I invented a totally fake set-up involving breast-fed versus bottle-fed babies.


Full disclosure: I have three kids who were both breast fed and bottle fed for various lengths of time and, although I was once pretty opinionated about the whole thing, I could care less at this point and I don’t think the data is in either (check [this out](http://www.stats.org/stories/breast_feed_nyt_jun_20_06.htm) as an example). So I’m not actually trying to make any political point.


Anyhoo, just to make things super concrete, I want to imagine there’s a small difference in weight, say at 5 years of age, between bottle fed and breast fed children. The actual effect is like 1.7 pounds at 5 years. Let’s *assume* that, which is why we see a blue line in the graph above at 1.7 with the word “assumed” next to it. You can decide who weighs more and if that’s a good thing or not depending on your politics.


OK, so that’s the underlying “truth” in the situation, but the point is, we don’t actually *know* it. We can only devise tests to *estimate* it, and this is where the graph comes in. The graph is showing us the distribution of our estimates of this effect if we have a crappy test.


So, imagine we have a crappy test – something like, we ask all our neighbors who have had kids recently how they fed their kids and how much those kids weighed at 5 years, and then we averaged the two groups. That test would be crappy because we probably don’t have very many kids overall, and the 5-year check-ups aren’t always exactly at 5 years, and the scales might have been wrong, or clothes might have been confusing the scale, and people might not have reported it correctly, or whatever. A crappy test.


Even so, we’d get some answer, and the graph above tells us that, if our tests are at a certain level of crappiness, which we will go into in a second, then very likely our estimate of the difference will come in between something like -22 pounds and +24 pounds. And the “most likely” answer would be the correct one, sure, but that doesn’t mean it’s all that likely to even come close – say within 2 pounds – of the “true effect”. In fact, if you make a band of width 4 centered around the “true effect” level, you’d definitely capture a smallish percentage of the total area under the curve. In fact, it looks like a good 45% of the area under the curve is in negative territory, so the chances are really very good that the test estimate, at this level of crappiness, would give you the wrong sign. That’s a terrible test!


Let’s be a bit more precise now about what we mean by “crappy.” The crappiness of our test is measured by its *[power](http://en.wikipedia.org/wiki/Statistical_power), *which is defined as “the probability that it correctly rejects the [null hypothesis](http://en.wikipedia.org/wiki/Null_hypothesis) – i.e. the hypothesis that the “true effect” is zero – when it is false.” In other words, power quantifies how well the test can distinguish between the blue line above and the line at zero. So if the bell curve were really really concentrated at the blue line, then more of the total area under the curve would be on the positive side of zero, and we’d have a much better test. Alternatively, if the true effect were much stronger, say at 25 instead of 1.7, then even with a test this imprecise, the power would be much much higher because the bulk of the bell curve would be to the right of zero.


On the one hand, power estimates are done by researchers, and they are attempting to achieve a power of at least 0.80, or 80%, so the above power of 0.06 is indeed extremely low and our test is indeed very crappy by researching standards. But on the other hand, since researchers are expected to estimate their power to be at least 0.80, there’s probably fudging going on and we might be trusting tests to be less crappy than they actually are. Also, I am no expert on how to accurately estimate the power of a test, but there’s an example [here](http://en.wikipedia.org/wiki/Statistical_power#Example), and in general it depends on your sample size (how many kids) and the actual effect size, as we have already discussed. In general it requires way more data to produce evidence of a small effect.


OK so now we have some general sense of what “crappiness” means. But what about the red parts?


Those are the “statistically significant” parts of the distribution. If we did our neighborhood kids test and we found an effect of 20 or -20, we’d be totally convinced, even though our test was crap. There are two take-aways from this. First, that “statistically significant” in the presence of a small actual effect and a crappy test means that we are wildly overestimating the effect. Second, that the red part on the left is about a third of the size of the red part on the right, which is to say that when we get a result that seems “statistically significant,” in the presence of a crappy test, it still has a one in four chance of being totally wrong.


In other words, when we have crappy tests, we just shouldn’t be talking about statistical significance at all. But of course, nobody can publish their results without statistical significance, so there’s that.
