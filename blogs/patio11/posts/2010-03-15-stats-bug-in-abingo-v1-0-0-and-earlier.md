---
title: "Stats Bug In A/Bingo v1.0.0 and earlier"
date: 2010-03-15
url: https://www.kalzumeus.com/2010/03/16/stats-bug-in-abingo-v1-0-0-and-earlier/
slug: stats-bug-in-abingo-v1-0-0-and-earlier
word_count: 268
---


Many thanks to Ivan for reporting this one: there is a significant bug in A/Bingo calculation of z-scores for versions 1.0.0 and earlier, which borks substantially all z-score calculations and in some cases can change whether A/B test results are reported as statistically significant or not.


The bug is all of *one character* long:


I have fixed the bug (via the Slicehost console, on a Japanese cafe Internet PC, because I am stuck in Nagoya today again) and pushed the fix to the git repository.


## Does this make my results invalid?


You can probably **still have confidence** in results you got from A/Bingo previously. While the numerical calculation of the z-score was borked, it was borked in a subtle enough fashion that most statistically significant tests will retain their statistical significance under the borked calculation and most statistically insignificant tests will not gain statistical significance magically as a result of the borked calculation. (My quick eyeball suggests that it causes BCC to overstate the significance of tests which are very significant and understate the significance of tests which are insignificant, which is a very fortuitous set of properties for a random bug to have in an A/B testing framework.)


I have re-run statistical confidence tests for everything I’ve ever done for BCC that I still have data for, and **no experimental results changed** as a result of the error. Nonetheless, I deeply regret the bug, and will write unit tests for the statistics code as soon as I am physically capable of doing so to rule out the possibility of this sort of thing in the future.
