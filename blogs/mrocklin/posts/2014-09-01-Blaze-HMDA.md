---
title: "Introducing Blaze - Practice"
date: 2014-09-01
url: https://mrocklin.github.io/blog/work/2014/09/01/Blaze-HMDA
slug: Blaze-HMDA
word_count: 814
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Grant](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

We look at data from the  [Home Mortgage Disclosure
Act](http://www.ffiec.gov/hmda/) , a collection of actions taken on
housing loans by various governmental agencies (gzip-ed csv file
 [here](http://files.consumerfinance.gov/hmda/hmda_lar-2012.csv.gz) )
(thanks to  [Aron Ahmadia](http://aron.ahmadia.net/)  for the pointer).
Uncompressed this dataset is around 10GB on disk and so we don’t want to
load it up into memory with a modern commercial notebook.

Instead, we use Blaze to investigate the data, select down to the data
we care about, and then migrate that data into a suitable computational
backend.

In this post we’re going to use the interactive  `Table`  object, which
wraps up a dataset and calls compute whenever we ask for something to be
printed to the screen. It retains the abstract delayed-evaluation nature
of Blaze with the interactive feel of NumPy and Pandas.

## Reducing the Dataset

That’s a lot of columns, most of which are redundant or don’t carry much
information. Let’s clean up our dataset a bit by selecting a smaller
subset of columns. Already this quick investigation improves our
comprehension and reduces the size of the dataset.

## More Complex Computation

Now that we can more clearly see what’s going on let’s ask a simple
question:

*How many times does each action occur in the state of New York?*

```
CPU times: user 13min 50s, sys: 5.23 s, total: 13min 55s
Wall time: 13min 55s
```

Great! Sadly, because it was reading through the CSV file and because it
was using a Pure Python backend, that computation took fourteen minutes.

## Moving to a Faster Backend

By default computations on CSV files use the streaming Python backend.
While robust for large files and decently fast, this backend parses the
CSV file each time we do a full-data operation, and this parsing is very
slow. Let’s move our reduced dataset to a more efficient and widely
accessible backend,  `sqlite` .

Yup, a little  `sqlite`  database just arrived

```
$ ls -lh hmda*

-rw-r--r-- 1 mrocklin mrocklin 2.7G Aug 25 13:38 hmda.db
-rw-r--r-- 1 mrocklin mrocklin  12G Jul 10 12:15 hmda_lar-2012.csv
```

## Working with SQL

Now that we’ve migrated our csv file into a sqlite database let’s redefine  `t` 
to use the SQL backend and repeat our computation.

```
CPU times: user 5.55 s, sys: 1.64 s, total: 7.19 s
Wall time: 7.46 s
```

*We’re about to repeat this same computation many times.  We’ll omit the table
result from here on out.  It will always be the same.*

## Create an index on state name

This was much faster, largely because the data was stored in a binary
format. We can improve the query speed significantly by placing an index
on the  `state_abbr`  field. This will cause the selection
 `t[t.state_abbr == 'NY']`  to return more quickly, eliminating the need
for an expensive full table scan.

Now we can ask this same query for many states at interactive
timescales.

```
CPU times: user 1.74 s, sys: 430 ms, total: 2.17 s
Wall time: 2.17 s
```

# Comparing against MongoDB

Because moving between computational backends is now easy, we can quickly
compare performance between backends. SQLite and MongoDB are similarly
available technologies, each being trivial to set up on a personal computer.
However they’re also fairly different technologies with varying communities.

Which performs faster for our sample computation?

```
CPU times: user 4.05 ms, sys: 701 µs, total: 4.76 ms
Wall time: 7.61 s
```

Almost exactly the same time as for SQLite.

We just did a complex thing easily.  If we weren’t familiar
with MongoDB we would need to learn how to set up a database, how to migrate
data from SQL to MongoDB, and finally how to perform queries.  Blaze eased that
process  *considerably* .

### Create an index on state name

Again we create an index on the state name and observe the performance
difference.

```
CPU times: user 4.13 ms, sys: 844 µs, total: 4.97 ms
Wall time: 954 ms
```

Here the indexed MongoDB system seems about twice as fast as the comparably
indexed SQLite system.

## Results

*Disclaimer: These results come from a single run.  No attempt was made to
optimize the backend configuration, nor was any consideration taken into
account about databases being warmed up.  These numbers are far from
conclusive, and are merely here to present the ease with which
intuitive-building experiments are easy with Blaze and the value of choosing
the right backend.*

# Conclusion

Blaze enables you to investigate, transform, and migrate large data
intuitively. You can choose the right technology for your application
without having to worry about learning a new syntax.

We hope that by lowering this barrier more users will use the right tool for
the job.

## More Information

* Documentation:  [blaze.pydata.org/](http://blaze.pydata.org/)
* Source:  [github.com/ContinuumIO/blaze/](http://github.com/ContinuumIO/blaze/)
* Install with [Anaconda](https://store.continuum.io/cshop/anaconda/): 
 `conda install blaze
`
