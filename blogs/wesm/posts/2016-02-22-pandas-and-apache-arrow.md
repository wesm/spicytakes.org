---
title: "Why pandas users should be excited about Apache Arrow"
date: 2016-02-22T00:00:00
tags: ["apache arrow", "pandas"]
slug: pandas-and-apache-arrow
word_count: 697
source_file: blog/pandas-and-apache-arrow/index.qmd
content_type: blog
---

<!-- PELICAN_BEGIN_SUMMARY -->

I'm super excited to be involved in the new open source [Apache Arrow][1]
community initiative. For Python (and R, too!), it will help enable

- Substantially improved data access speeds
- Closer to native performance Python extensions for big data systems like
  Apache Spark
- New in-memory analytics functionality for nested / JSON-like data

There's plenty of places you can learn more about Arrow, but this post is about
how it's specifically relevant to pandas users. See, for example:

* ["Python and Hadoop: A State of the Union"][2]
* ["Introducing Apache Arrow: A Fast, Interoperable In-Memory Columnar Data Structure Standard"][3]
* ["Introducing Apache Arrow: Columnar In-Memory Analytics"][4]

<!-- PELICAN_END_SUMMARY -->

## Accelerating data access for pandas users on Hadoop clusters

For average pandas users, the gold standard for storing and retrieving data on
local machines (or network file systems) is usually one of:

* CSV files, using `pandas.read_csv`
* HDF5 data format files, using `pandas.HDFStore`
* Another binary dataformat, like the [Blosc][6]-powered [bcolz][5]

But if your data is in a Hadoop cluster, it may not be as simple as reading a
file off disk. Here's some of the data-providing systems and storage formats
you can access from pandas:

<center>
<img src="../../images/arrow_pandas_image1.png" alt="Hadoop data access" width="60%"/>
</center>

Unfortunately, the quality of these data connections for pandas are highly
variable. I did an [in-depth exploration][7] to compare the performance of
retrieving a `pandas.DataFrame` with 1 million rows with a net footprint of
about 90 megabytes. Here is the performance summary:

<table>
  <tr>
  <th><strong>Method</strong></th>
  <th><strong>Speed (sec)</strong></th>
  <th><strong>vs HDF5</strong></th>
  <th><strong>vs read_csv</strong></th>
  <th><strong>Effective speed</strong></th>
  </tr>
  <tr>
  <td><strong>pandas.HDF5Store (uncompressed)</strong></td>
  <td>0.117</td>
  <td>1.0x</td>
  <td>0.05x</td>
  <td>769.23 MB/s</td>
  </tr>
  <td><strong>pandas.read_csv</strong></td>
  <td>2.43</td>
  <td>20.8x</td>
  <td>1.00x</td>
  <td>37.04 MB/s</td>
  </tr>
  <tr>
  <td><strong>Spark DataFrame.toPandas</strong></td>
  <td>13.6</td>
  <td>116.2x</td>
  <td>5.60x</td>
  <td>6.62 MB/s</td>
  </tr>
  <tr>
  <td><strong>Impala SELECT (via impyla)</strong></td>
  <td>15.3</td>
  <td>130.8x</td>
  <td>6.30x</td>
  <td>5.88 MB/s</td>
  </tr>
</table>

As the original author of both `read_csv` and `HDFStore`, these benchmarks make
me very proud, but it also shows what level of data access performance pandas
users should expect in general.

The price of data serialization can be directly seen in the Impala query
profile (note, this is a DEBUG Impala build):

```
Operator       #Hosts  Avg Time  Max Time  #Rows
------------------------------------------------
01:EXCHANGE         1     149ms     149ms  1.00M
00:SCAN HDFS        2     269ms     282ms  1.00M
```

So more than 90% of the execution time is data serialization.

The reasons why the Spark and HiveServer2 data access speeds are slow boil down
to a couple of factors:

* Data is transferred in a form that is expensive to deserialize.
* Data is passing through scalar Python objects (i.e. using
  `DataFrame.from_records` on a list of tuples) rather than going directly into
  pandas objects at the C API level.

Apache Arrow helps mitigate both of these problems. In the reasonably near
future, I expect things architecturally to look like this:

<center>
<img src="../../images/arrow_pandas_image2.png" alt="Arrow data access" width="50%"/>
</center>

Realistically, the performance of ingesting data into pandas via Arrow should
be significantly faster than reading a CSV (being binary and columnar).

It's important to note that using `pandas.read_csv` as a standard for data
access performance doesn't completely make sense. Parsing a CSV is fairly
expensive, which is why reading from HDF5 is 20x faster than parsing a CSV.

## On Apache Parquet

The [Apache Parquet][8] data format is a column-oriented binary storage format
for structured data optimized for IO throughput and fast analytics. Since it
was designed primarily for use in a MapReduce setting initially, most
development energy was poured into the [parquet-mr][9] Java implementation.

Last month I started getting involved in [parquet-cpp][10], a native C++11
implementation of Parquet. I'm pleased to report we've made great progress on
this in the last 6 weeks, and native read/write support for pandas users is
reasonably near on the horizon. I'll report here when I get the whole thing
working end-to-end.

## Summary and the road ahead

Data access performance is only one area where Arrow will help the Python
ecosystem. High performance Python extensions and native in-memory handling for
nested columnar data will also make a big impact. I look forward to sharing
ongoing progress updates.

[1]: http://arrow.apache.org
[2]: http://vision.cloudera.com/python-and-hadoop-a-state-of-the-union/
[3]: http://blog.cloudera.com/blog/2016/02/introducing-apache-arrow-a-fast-interoperable-in-memory-columnar-data-structure-standard/
[4]: http://www.dremio.com/blog/apache-arrow/
[5]: https://github.com/Blosc/bcolz
[6]: https://github.com/Blosc/c-bloscx
[7]: https://gist.github.com/wesm/0cb5531b1c2e346a0007
[8]: https://parquet.apache.org
[9]: https://github.com/apache/parquet-mr
[10]: https://github.com/apache/parquet-cpp