---
title: "Recidivism risk algorithms are inherently discriminatory"
date: 2017-01-04
url: https://mathbabe.org/2017/01/04/recidivism-risk-algorithms-are-inherently-discriminatory/
word_count: 386
---


A few people have been sending me, via Twitter or email, [this unsurprising article](http://www.businessinsider.com/racial-bias-in-criminal-courts-2017-1) about how recidivism risk algorithms are inherently racist.


I say unsurprising because I’ve recently read a 2011 paper by Faisal Kamiran and Toon Calders entitled *[Data preprocessing techniques for classification without discrimination](http://download.springer.com/static/pdf/530/art%253A10.1007%252Fs10115-011-0463-8.pdf?originUrl=http%3A%2F%2Flink.springer.com%2Farticle%2F10.1007%2Fs10115-011-0463-8&token2=exp=1483465340~acl=%2Fstatic%2Fpdf%2F530%2Fart%25253A10.1007%25252Fs10115-011-0463-8.pdf%3ForiginUrl%3Dhttp%253A%252F%252Flink.springer.com%252Farticle%252F10.1007%252Fs10115-011-0463-8*~hmac=40acd34bc79dfb336102e58b347e57df9eefe91b8e986969f4ad8871be454258), *which explicitly describes the trade-off between accuracy and discrimination in algorithms in the presence of biased historical data (Section 4, starting on page 8).


In other words, when you have a dataset that has a “favored” group of people and a “discriminated” group of people, and you’re deciding on an outcome that has historically been awarded to the favored group more often – in this case, it would be a low recidivism risk rating – then you cannot expect to maximize accuracy and keep the discrimination down to zero at the same time.


Discrimination is defined in the paper as the difference in percentages of people who get the positive treatment among all people in the same category. So if 50% of whites are considered low-risk and 30% of blacks are, that’s a discrimination score of 0.20.


The paper goes on to show that the trade-off between accuracy and discrimination, which can be achieved through various means, is linear or sub-linear depending on how it’s done. Which is to say, for every 1% loss of discrimination you can expect to lose a fraction of 1% of accuracy.


It’s an interesting paper, well written, and you should take a look. But in any case, what it means in the case of recidivism risk algorithms is that any algorithm that is optimized for “catching the bad guys,” i.e. accuracy, which these algorithms are, and completely ignores the discrepancy between high risk scores for blacks and for whites, can be expected to be discriminatory in the above sense, because we know the data to be biased*.


* The bias is due to the history of heightened scrutiny of black neighborhoods by police which we know as broken windows policing, which makes blacks more likely to be arrested for a given crime, as well as the inherent racism and classism in our justice system itself that was so brilliantly explained out by Michelle Alexander in her book  [The New Jim Crow](http://newjimcrow.com/), which makes them more likely to be severely punished for a given crime.
