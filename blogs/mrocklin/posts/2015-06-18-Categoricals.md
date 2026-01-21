---
title: "Pandas Categoricals"
date: 2015-06-18
url: https://mrocklin.github.io/blog/work/2015/06/18/Categoricals
slug: Categoricals
word_count: 637
---

**tl;dr: Pandas Categoricals efficiently encode and dramatically improve
performance on data with text categories**

*Disclaimer: Categoricals were created by the Pandas development team and not
by me.*

## There is More to Speed Than Parallelism

I usually write about parallelism.  As a result people ask me how to
parallelize their slow computations.
The answer is usually  **just use pandas**  in a better way

* Q:  *How do I make my pandas code faster with parallelism?*
* A:  *You don’t need parallelism, you can use Pandas better*

This is almost always simpler and more effective than using multiple cores or
multiple machines.  You should look towards parallelism only after you’ve
made sane choices about storage format, compression, data representation, etc..

Today we’ll talk about how Pandas can represent categorical text data
numerically.  This is a cheap and underused trick to get an order of magnitude
speedup on common queries.

## Categoricals

Often our data includes text columns with many repeated elements. Examples:

* Stock symbols –  `GOOG, APPL, MSFT, ...`
* Gender –  `Female, Male, ...`
* Experiment outcomes –  `Healthy, Sick, No Change, ...`
* States –  `California, Texas, New York, ...`

We usually represent these as text.  Pandas represents text with the  `object` 
dtype which holds a normal Python string.  This is a common culprit for slow
code because  `object`  dtypes run at Python speeds, not at Pandas’ normal C
speeds.

Pandas categoricals are a new and powerful feature that encodes categorical
data numerically so that we can leverage Pandas’ fast C code on this kind of
text data.

We can represent columns with many repeats, like gender, more efficiently by
using categoricals.  This stores our original data in two pieces

* Original data 
 ` Female, Male, Male, Female
`

1. Index mapping each category to an integer 
 `Female: 0
Male: 1
...
`
2. Normal array of integers 
 `0, 1, 1, 0
`

This integer array is more compact and is now a normal C array.  This allows
for normal C-speeds on previously slow object dtype columns.
Categorizing a column is easy:

Lets look at the result

Notice that we can store our genders much more compactly as single bytes.  We
can continue to add genders (there are more than just two) and Pandas will
use new values (2, 3, …) as necessary.

Our dataframe looks and feels just like it did before.  Pandas internals will
smooth out the user experience so that you don’t notice that you’re actually
using a compact array of integers.

## Performance

Lets look at a slightly larger example to see the performance difference.

We take a small subset of the NYC Taxi dataset and group by medallion ID to
find the taxi drivers who drove the longest distance during a certain period.

That took around 170ms.  We categorize in about the same time.

Now that we have numerical categories our computaion runs 20ms, improving by
about an order of magnitude.

We see almost an order of magnitude speedup after we do the one-time-operation
of replacing object dtypes with categories.  Most other computations on this
column will be similarly fast.  Our memory use drops dramatically as well.

## Conclusion

Pandas Categoricals efficiently encode repetitive text data.  Categoricals are
useful for data like stock symbols, gender, experiment outcomes, cities,
states, etc..  Categoricals are easy to use and greatly improve performance on
this data.

We have several options to increase performance when dealing with
inconveniently large or slow data.  Good choices in storage format,
compression, column layout, and data representation can dramatically improve
query times and memory use. Each of these choices is as important as
parallelism but isn’t overly hyped and so is often overlooked.

Jeff Reback gave a nice talk on categoricals (and other featuress in Pandas) at
 [PyData NYC 2014](https://www.youtube.com/watch?v=PUsntnCp65c)  and is giving
another this weekend at PyData London.
