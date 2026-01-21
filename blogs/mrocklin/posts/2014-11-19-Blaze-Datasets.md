---
title: "Blaze Datasets"
date: 2014-11-19
url: https://mrocklin.github.io/blog/work/2014/11/19/Blaze-Datasets
slug: Blaze-Datasets
word_count: 965
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Grant](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr**  Blaze aids exploration by supporting full databases and
collections of datasets.

This post was composed using Blaze version 0.6.6.  You can follow along with
the following  [conda](http://conda.pydata.org/)  command.

```
conda install -c blaze blaze=0.6.6
```

When we encounter new data we need to explore broadly to find what exists
before we can meaningfully perform analyses.  The tools for this task are often
overlooked.

This post outlines how Blaze explores collections and hierarchies of datasets,
cases where one entity like a database or file or directory might hold
many tables or arrays.  We use examples from HDF5 files and SQL databases.
Blaze understands how the underlying libraries work so that you don’t have to.

## Motivating problem - Intuitive HDF5 File Navigation

For example, if we want to understand the contents of  [this set of HDF5
files](http://mirador.gsfc.nasa.gov/cgi-bin/mirador/granlist.pl?page=1&location=(-90,-180),(90,180)&dataSet=OMAERO&version=003&allversion=003&startTime=2014-11-05T00:00:01Z&endTime=2014-11-05T23:59:59Z&keyword=OMAERO&longname=OMI/Aura%20Multi-wavelength%20Aerosol%20Optical%20Depth%20and%20Single%20Scattering%20Albedo%201-orbit%20L2%20Swath%2013x24%20km&CGISESSID=958493efa9d8a96c5ba2d0b4d69c986d&prodpg=http://mirador.gsfc.nasa.gov/collections/OMAERO__003.shtml) 
encoding meteorological data then we need to navigate a hierarchy of
arrays.  This is common among HDF5 files.

Typically we navigate these files in Python with  `h5py`  or  `pytables` .

HDF5 files organize datasets with an internal file system.  The  `h5py`  library
accesses this internal file system through successive calls to  `.keys()`  and
item access.

This interaction between programmer and interpreter feels like a long and
awkward conversation.

Blaze improves the exploration user experience by treating the entire HDF5 file
as a single Blaze variable.  This allows users to both explore and compute on
larger collections of data in the same workflow.  This isn’t specific to HDF5
but works anywhere many datasets are bundled together.

## Exploring a SQL Database

For example, a SQL database can be viewed as a collection of tables.  Blaze
makes it easy to to access a single table in a database using a string URI
specifying both the database and the table name.

This only works if we know what table we want ahead of time.  The approach
above assumes that the user is  *already familiar with their data* .  To resolve
this problem we omit the table name and access the database as a variable
instead.  We use the same interface to access the entire database as we would
a specific table.

The  `db`  expression points to a SQLAlchemy engine.  We print the engine
alongside a truncated datashape showing the metadata of the tables in that
database.  Note that the datashape maps table names to datashapes of those
tables, in this case a variable length collection of records with fields for
measurements of flowers.

Blaze isn’t doing any work of the grunt work here, SQLAlchemy is.
 [SQLAlchemy](http://www.sqlalchemy.org/)  is a mature Python library that
interacts with a wide variety of SQL databases.  It provides both database
reflection (as we see above) along with general querying (as we see below).
Blaze provides a convenient front-end.

We seamlessly transition from exploration to computation.  We query for the
shortest and longest sepal per species.

Blaze doesn’t pull data into local memory, instead it generates SQLAlchemy
which generates SQL which executes on the foreign database.  The (much smaller)
result is pulled back into memory and rendered nicely using Pandas.

## A Larger Database

Improved metadata discovery on SQL databases overlaps with the excellent work
done by  [yhat](https://yhathq.com/)  on
 [db.py](http://blog.yhathq.com/posts/introducing-db-py.html) .  We steal their
example, the Lahman Baseball statistics database, as an example of a richer
database with a greater variety of tables.

Seeing at once all the tables in the database, all the columns in those tables,
and all the types of those columns provides a clear and comprehensive overview
of our data.  We represent this information as a
 [datashape](http://datashape.pydata.org/) , a type system covers everything from
numpy arrays to SQL databases and Spark collections.

We use standard Blaze expressions to navigate more deeply.  Things like
auto-complete work fine.

And we finish by a fun multi-table computation, joining two tables on year,
team, and league and then computing the average salary by team name and year

Looks good, we compute and store to CSV file with  `into`

(Final result here:  [salaries.csv](https://mrocklin.github.io/blog/storage/salaries.csv) )

## Beyond SQL

SQL isn’t unique, many systems hold collections or hierarchies of datasets.
Blaze supports navigation over Mongo databases,  [Blaze
servers](http://blaze.pydata.org/docs/latest/server.html) , HDF5 files, or even
just dictionaries of pandas DataFrames or CSV files.

None of this behavior was special-cased in Blaze.  The same mechanisms
that select a table from a SQL database select a column from a Pandas
DataFrame.

## Finish with HDF5 example

To conclude we revisit our motivating problem, HDF5 file navigation.

### Raw H5Py

Recall that we previously had a long back-and-forth conversation with the
Python interpreter.

### H5Py with Blaze expressions

With Blaze we get a quick high-level overview and an API that is shared with
countless other systems.

By default we see the data and a truncated datashape.

We ask for the datashape explicitly to see the full picture.

When we see metadata for everything in this dataset all at once the full
structure  becomes apparent.  We have two collections of arrays, all shaped
 `(1643, 60)` ; the collection in  `Data Fields`  holds what appear to be weather
measurements while the collection in  `Geolocation Fields`  holds coordinate
information.

Moreover we can quickly navigate this structure to compute relevant information.

## Final Thoughts

*Often the greatest challenge is finding what you already have.*

Discovery and exploration are just as important as computation.  By extending
the Blaze’s expression system to hierarchies of datasets we create a smooth
user experience from first introductions to data all the way to analytic
queries and saving results.

This work was easy.  The pluggable architecture of Blaze made it surprisingly
simple to extend the Blaze model from tables and arrays to collections of
tables and arrays.  We wrote about  [40 significant lines of
code](https://github.com/ContinuumIO/blaze/pull/825)  for each supported
backend.
