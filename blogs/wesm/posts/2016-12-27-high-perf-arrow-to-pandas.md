---
title: "From Arrow to pandas at 10 Gigabytes Per Second"
date: 2016-12-27T00:00:00
tags: ["apache arrow", "pandas"]
slug: high-perf-arrow-to-pandas
word_count: 863
source_file: blog/high-perf-arrow-to-pandas/index.qmd
content_type: blog
---

<!-- PELICAN_BEGIN_SUMMARY -->

In this post I discuss some recent work in Apache Arrow to accelerate
converting to pandas objects from general Arrow columnar memory.

<!-- PELICAN_END_SUMMARY -->

## Challenges constructing pandas DataFrame objects quickly

One of the difficulties in fast construction of pandas DataFrame object is that
the "native" internal memory structure is more complex than a dictionary or
list of one-dimensional NumPy arrays. I won't go into the reasons for this
complexity, but it's something we're hoping to do away with as part of the
[pandas 2.0 effort][1]. There are two layers of complexity:

* pandas's memory representation for a particular data type may change
  depending on the presence of null values. Boolean data becomes `dtype=object`
  while integer data becomes `dtype=float64`.

* Upon calling `pandas.DataFrame`, internally pandas will "consolidate" the
  input by copying into its internal two-dimensional **block
  structure**. Constructing the precise block structure is the only true way to
  do **zero-copy** DataFrame construction.

To give you an idea of the overhead introduced by consolidation, let's look at
a benchmark. Consider the setup code, in which we create a dict of 100
`float64` arrays constituting a gigabyte of data:

```python
import numpy as np
import pandas as pd
import pyarrow as pa

type_ = np.dtype('float64')
DATA_SIZE = (1 << 30)
NCOLS = 100
NROWS = DATA_SIZE / NCOLS / np.dtype(type_).itemsize

data = {
    'c' + str(i): np.random.randn(NROWS)
    for i in range(NCOLS)
}
```

Then, we create a DataFrame with `pd.DataFrame(data)`:

```
>>> %timeit df = pd.DataFrame(data)
10 loops, best of 3: 132 ms per loop
```

(For those who are counting, that's **7.58 GB/second** *just* to do an internal
memory copy.)

An important thing to remember is that, here, we have already constructed
pandas's "native" memory representation (nulls would be `NaN` in the arrays),
but as a collection of 1D arrays.

## Converting from Arrow columnar memory to pandas

[Apache Arrow][2], a project I've been heavily involved with since its genesis
early in 2016, is a language-agnostic in-memory columnar representation and
collection of tools for interprocess communication (IPC) . It supports nested
JSON-like data and is designed as a building-block for creating fast analytics
engines.

Compared with pandas, Arrow has a more precise representation of null values in
a bitmap that is separate from the values. So, zero-copy conversion even to a
dict-of-arrays representation suitable for pandas requires more effort.

One of my major goals in working on Arrow is to use it as a high-bandwidth IO
pipe for the Python ecosystem. We can talk to the JVM, database systems, and
many different file formats by using Arrow as the columnar interchange
format. For this use case, it's important to be able to get back a pandas
DataFrame as fast as possible.

Over the last month I've done some engineering to construct pandas's native
internal block structure to achieve high bandwidth to Arrow memory. If you've
been following the [Feather file format][3], this work is all closely
interrelated.

Let's return to the same gigabyte of data from above, and be sure to add some
nulls:

```python
>>> df = pd.DataFrame(data)
>>> df.values[::5] = np.nan
```

Now, let's convert the DataFrame to an Arrow table, which constructs the Arrow
columnar representation:

```python
>>> table = pa.Table.from_pandas(df)
>>> table
<pyarrow.table.Table at 0x7f18ec65abd0>
```

To go back to pandas-land, call the table's `to_pandas` method. This supports a
multithreaded conversion, so let's do a single-threaded conversion for
comparison:

```python
>>> %timeit df2 = table.to_pandas(nthreads=1)
10 loops, best of 3: 158 ms per loop
```

This is **6.33 GB/s**, or about 20% slower than purely memcpy-based
construction. On my desktop, I can use all 4 cores to go even faster:

```python
>>> %timeit df2 = table.to_pandas(nthreads=4)
10 loops, best of 3: 103 ms per loop
```

At **9.71 GB/s**, this is not far from saturating the main memory bandwidth on
my consumer desktop hardware (but I am not an expert on this).

The performance benefits of multithreading can be more dramatic on other
hardware. While the performance ratio on my desktop is only **1.53**, on my
(also quad-core) laptop it is 3.29.

> Note that numeric data is a best-case scenario; string or binary data would
come with additional overhead while pandas continues to use Python objects in
its memory representation.

## Implications and roadmap

Since Arrow arrays, record batches (multiple arrays of the same length), and
tables (collections of record batches) can be easily zero-copy constructed from
many different sources, it is a flexible and efficient way to move tabular data
around between systems. By having high speed conversion to pandas, we can pay a
small conversion cost (5-10 GB/s is usually negligible compared with the IO
performance of other media) to obtain a fully-fledged pandas DataFrame.

In a separate blog post, I'll go into some of the technical details of Arrow's
low-overhead (and as often as possible: zero-copy) C++ IO subsystem.

As we forge ahead on the pandas 2.0 roadmap, we hope to further reduce the
overhead (to zero, in some cases) in interacting with columnar memory like
Arrow. A simpler memory representation will also make it easier for other
applications to interact with pandas at a low-level.

[1]: http://www.slideshare.net/wesm/python-data-wrangling-preparing-for-the-future
[2]: http://arrow.apache.org/
[3]: http://github.com/wesm/feather