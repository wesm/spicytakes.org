---
title: "Wordcounting and Verbosity"
date: 2013-11-15
url: https://mrocklin.github.io/blog/work/2013/11/15/Functional-Wordcount
slug: Functional-Wordcount
word_count: 546
---

In a
 [blogpost](http://matthewrocklin.com/blog/work/2013/10/17/Introducing-PyToolz/) 
last month I announced  [PyToolz](http://toolz.readthedocs.org/)  a Python
implementation of the functional standard library.  Today I want to discuss the
wordcounting example in more depth, highlighting differences between
simple/verbose and complex/concise code.

**tl;dr:**  Library code reduces code-length at the cost of universal
comprehension.  Libraries simplify code for a subset of programmers while
alienating others.  This is behind the common complaint that functional
programming is hard to read.  We use word-counting as a case study.

### Verbose solution with simple terms

My standard wordcounting function looks like the following:

While long/verbose, this solution is straightforward and comprehensible to all
moderately experienced Python programmers.

### Concise solution with complex terms

Using the definition for  `stem`  above and the  `frequencies`  function from
 `toolz`  we can condense  `wordcount`  into the following single line.

While dense, this solution solves the problem concisely using
pre-existing functionality.

### Increasing readability with  `pipe`

The functional solution above with  `frequencies(map(stem, sentence.split()))`  is
concise but difficult for many human readers to parse.  The reader needs to
traverse a tree of parentheses to find the innermost element ( `sentence` ) and
then work outwards to discover the flow of computation.  We improve the readability of
this solution with the  `pipe`  function from  `toolz` .

To introduce  `pipe`  we consider the abstract process of doing laundry:

This pushes the data,  `clothes`  through a pipeline of functions,  `wash` ,  `dry` ,
and  `fold` .  This pushing of data through a pipeline of functions is a common
pattern.  We encode this pattern into  `toolz.pipe` .

Pipe pushes data (first argument) through a sequence of functions (rest of the
arguments) from left to right.  Here is another example.

Using  `pipe`  we can rearrange our functional wordcounting solution to the
following form

This code reads like a story from left to right.  We take a sentence,
split it into words, stem each word, and then count frequencies.  This is
sufficiently simple so that I am confident in the correctness of the result
after a brief review of the code.  There is little room for error.

*note: here we used a curried version of `map`.  See the [toolz
docs](http://toolz.readthedocs.org/en/latest/curry.html) for more info.*

### Discussion

The first solution uses lots of simple words.  The second solution uses a few
complex words.  Just as in natural language there are benefits and
drawbacks to a rich vocabulary.  The choice of suitable vocabulary largely
depends on the audience.

Long solutions of simple words are universally understandable but require
reader effort to construct meaning.  Most Python programmers can understand the
first solution without additional training but will need to expend effort to
deduce its meaning.  This is like the approach taken by  [Simple English
Wikipedia](http://simple.wikipedia.org/wiki/Main_Page) .

Concise solutions of complex words are not universally understandable but
do convey meaning more quickly if the terms are already known by the reader.
Additionally if the terms themselves are well tested then these solutions are
less prone to error.

A good vocabulary can concisely express most relevant problems with a small
number of terms.  The functional standard library (e.g.  `map` ,  `groupby` ,
 `frequencies` , …) is such a set.  Understanding a relatively few number of
terms (around 10-20) enables the concise expression of most common programming
tasks.  This set was developed and refined across decades of language
evolution.
