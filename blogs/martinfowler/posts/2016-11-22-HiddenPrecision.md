---
title: "Hidden Precision"
description: "Sometimes when I work with some data, that data is more precise than   I expect. One might think that would be a good thing, after all precision is good, so   more is better. But hidden precision can "
date: 2016-11-22T00:00:00
tags: ["bad things"]
url: https://martinfowler.com/bliki/HiddenPrecision.html
slug: HiddenPrecision
word_count: 383
---


Sometimes when I work with some data, that data is more precise than
  I expect. One might think that would be a good thing, after all precision is good, so
  more is better. But hidden precision can lead to some subtle bugs.


```
const validityStart = new Date("2016-10-01");   // JavaScript
const validityEnd = new Date("2016-11-08");
const isWithinValidity = aDate => (aDate >= validityStart && aDate <= validityEnd);
const applicationTime = new Date("2016-11-08 08:00");

assert.notOk(isWithinValidity(applicationTime));  // NOT what I want
```


What happened in the above code is that I intended to create an inclusive date range by
  specifying the start and end dates. However I didn't actually specify dates, but
  instants in time, so I'm not marking the end date as November 8th, I'm marking the end
  as the time 00:00 on November 8th. As a consequence any time (other than midnight)
  within November 8th falls outside the date range that's intended to include it.


Hidden precision is a common problem with dates, because it's sadly common to have a
  date creation function that actually provides an instant like this. It's an example of
  poor naming, and indeed general poor modeling of dates and times.


Dates are a good example of the problems of hidden precision, but another culprit
  is floating point numbers.


```
const tenCharges = [
  0.10, 0.10, 0.10, 0.10, 0.10,
  0.10, 0.10, 0.10, 0.10, 0.10,
];
const discountThreshold = 1.00;
const totalCharge = tenCharges.reduce((acc, each) => acc += each);
assert.ok(totalCharge < discountThreshold);   // NOT what I want
```


When I just ran it, a log statement showed `totalCharge` was
  `0.9999999999999999`. This is because floating point doesn't exactly
  represent many values, leading to a little invisible precision that can show up at
  awkward times.


One conclusion from this is that you should be extremely wary of representing money
  with a floating point number. (If you have a fractional currency part like cents, then
  usually it's best to use integers on the fractional value, representing €5.00 with 500,
  preferably within a [money type](https://martinfowler.com/eaaCatalog/money.html))
  The more general conclusion is that floating point is tricksy when it comes to
  comparisons (which is why test framework asserts always have a precision for
  comparisons).


## Acknowledgements

Arun Murali, James Birnie, Ken McCormack, and Matteo Vaccari

    discussed a draft of this post on our internal mailing list.