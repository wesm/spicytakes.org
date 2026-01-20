---
title: "pandas lightning talk SciPy 2011"
summary: "Video at SciPy 2011 Lightning Talk"
date: 2011-07-14T00:00:00
tags: ["video", "transcript"]
slug: scipy-2011-lightning-talk
word_count: 1385
source_file: transcripts/2011-07-14-scipy-2011-lightning-talk.md
content_type: transcript
event: "SciPy 2011 Lightning Talk"
video_url: "https://www.youtube.com/watch?v=3vrCCjmVnIk"
---

{{< video https://www.youtube.com/watch?v=3vrCCjmVnIk >}}

*This transcript and summary were AI-generated and may contain errors.*

## Summary

In this talk, I clarify that "there's a kind of a misconception that pandas is only for time series data. It's completely not true." My goal: creating "one of the best, if not the best, tools in any language for working with relational data, labeled data."

## Core Architecture

pandas provides labeled arrays that handle heterogeneous, size-mutable data—bringing R's data frame concept to Python. The library's foundation: automatic data alignment, indexing and reshaping capabilities, and missing data handling. It originated from my work at a hedge fund but was designed for broad applicability.

My vision: "trying to build a platform that could be used to essentially replace R, building the fundamental building blocks for statistics, for data manipulation, stuff that people in other scientific computing environments wish they had in Python."

## Technical Improvements

I consolidated the internal structure from two different classes for tabular data into a single implementation that "brings the best of both worlds," including better handling of missing data in non-floating point types.

After years of resistance, I admitted to "giving in" on two frequently requested features: support for n-dimensional structures beyond the original three-dimension limit, and label-based indexing for slicing and complex get/set operations.

## Data Operations and I/O

The talk covered improvements in pivoting and reshaping operations, showing how pandas could transform SQL-table-like structures into more analytically useful formats.

I/O received attention, with enhanced CSV reading and a complete overhaul of HDF5 PyTables-based storage. I described the original HDF5 implementation as something I "hacked out in an afternoon" as a prototype, which I subsequently rebuilt.

## Future Directions

Planned developments: sparse data structures optimized for mostly-NA data, time zone support, generic moving window functions, and enhanced group-by operations. I also mentioned collaborative work on statsmodels integration.

## Key Quotes

> "There's a kind of a misconception that pandas is only for time series data. It's completely not true."

> "I would like to make it one of the best, if not the best, tools in any language for working with relational data, labeled data."

> "Trying to build a platform that could be used to essentially replace R, building the fundamental building blocks for statistics, for data manipulation, stuff that people in other scientific computing environments wish they had in Python and haven't had for a long time."

> "If you use it, you find that it's not, send me an email. Either you can hack on it or let me know how it could be improved."

> "There used to be two classes with different internal implementations for tabular data. I fixed that. There's now just one. I think it brings the best of both worlds."

> "Usually in the past, pandas only handled three dimensions and less, which is really all you need for finance and econometrics, but people keep asking for greater than three, so I'm giving in."

> "Here's another thing that I gave into recently, adding fancier indexing, something I stonewalled on for years, it feels like, and I finally added."

> "Somebody emailed me and said, how do you store pandas objects in HDF5, and so I hacked out something in an afternoon, but it was just a prototype, so I went through and actually built something real."

---

## Transcript

All right.

All right.

I'll try to talk at least as fast as Peter here.

So I wanted to tell you about what I've been working on in pandas and some things that

I think are exciting.

I don't know if many of you have heard of this library, but basically we've got labeled

arrays that handle heterogeneous data that are also size mutable, so kind of like an

R data frame if you've ever used R. But basically I think there's a kind of a misconception

that pandas is only for time series data.

It's completely not true.

It happens to be very good for that, but also a lot of other things.

Key features are automatic data alignment with lots of indexing and reshaping.

It does missing data really well, both implicitly and explicitly.

It's got great time series stuff.

I've used Scikit's time series, but I find it hard to use.

And I work a lot with multiple time series, which isn't really very well supported in

Scikit's time series.

So if you've got time series data, find yourself struggling, take a look.

And there's a lot of stuff for doing SQL-like operations, merging, joining, that kind of

thing.

Of course, you know, I used to work for a hedge fund.

I built it inside a hedge fund.

It's extremely good for financial data.

People on the Internet have very good things to say about it.

I won't really go there.

I would like to make it one of the best, if not the best, tools in any language for working

with relational data, labeled data.

So if you use it, you find that it's not, send me an email.

Either you can hack on it or let me know how it could be improved.

Because this is really my main goal, is making it one of the best tools that's available

anywhere.

And, of course, trying to build a platform that could be used to essentially replace

R, building the fundamental building blocks for statistics, for data manipulation, stuff

that people in other scientific computing environments wish they had in Python and haven't

had for a long time.

So some of the new things.

Oh, wow.

That's amazing.

There's only two and a half minutes left.

I've heavily reworked the internals.

There used to be two classes with different internal implementations for tabular data.

I fixed that.

There's now just one.

I think it brings the best of both worlds.

There's a cool internal data structure.

It's kind of a prototype, but I'd like to do more with it.

Getting more eyes on it would be fantastic.

Handling of missing data and non-floating point D-types is better, and I'm working currently

on essentially laying the groundwork for an N-dimensional structure.

Usually in the past, pandas only handled three dimensions and less, which is really all you

need for finance and econometrics, but people keep asking for greater than three, so I'm

giving in.

Here's another thing that I gave into recently, adding fancier indexing, something I stonewalled

on for years, it feels like, and I finally added.

Integers, labels, you can slice with labels.

This is sort of inspired by Larry and Data Array and all that, so having that all there.

You can also set, which is cool, so you can do really fancy getting and setting on pandas

objects.

I worked a lot on robustifying the I-O, so you can read CSV files really easily, read

tabular structures very easily.

I really retooled the HDF5 PyTables-based storage, which was kind of a prototype somebody

emailed me and said, how do you store pandas objects in HDF5, and so I hacked out something

in an afternoon, but it was just a prototype, so I went through and actually built something

real.

Pivoting and reshaping data has gotten a lot better, so if you ever have data that looks

like this stored in a SQL table, it's indexed based on a couple of columns, and you want

to reshape that into something a little more useful, you can pivot it with the pivot function

and just specify here the bar and the foo column, and so you get reshaped data, which

you can then do computations on, but you can also, you know, forget about the syntax, this

is the panel data structure, but you can also slice along the other axes, so if you wanted

everything labeled one in the bar in the foo column, then you can get all that data labeled

like that.

I had an extra slide there.

Some other things that are exciting, sparse data structures, mostly NA, not mostly zero,

time zone support, generic moving windows functions, I'm working a lot on enhancing

group by and frequency conversions, and we're going to hack on it in stats models, getting

more integration there.

So thanks a lot, and yeah, let me know if you find it useful.