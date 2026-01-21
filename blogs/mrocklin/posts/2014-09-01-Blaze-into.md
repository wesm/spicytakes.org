---
title: "Introducing Blaze - Migrations"
date: 2014-09-01
url: https://mrocklin.github.io/blog/work/2014/09/01/Blaze-into
slug: Blaze-into
word_count: 346
---

*This work is supported by [Continuum Analytics](http://continuum.io)
and the [XDATA Grant](http://www.darpa.mil/program/XDATA)
as part of the [Blaze Project](http://blaze.pydata.org)*

**tl;dr Blaze migrates data efficiently between a variety of data stores.**

In our  [last post on Blaze expressions](./foo)  we showed how Blaze can execute
the same tabular query on a variety of computational backends.  However, this
ability is only useful if you can migrate your data to the new computational
system in the first place.  To help with this, Blaze provides the  `into` 
function which moves data from one container type to another:

The  `into`  function takes two arguments,  `a`  and  `b` , and it puts the data in
 `b`  into a container like  `a` .  For example, if we have the class iris dataset
in a CSV file ( `iris.csv`  includes measurements and species of various flowers)

```
$ head iris.csv
SepalLength,SepalWidth,PetalLength,PetalWidth,Species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
4.6,3.1,1.5,0.2,setosa
5.0,3.6,1.4,0.2,setosa
5.4,3.9,1.7,0.4,setosa
4.6,3.4,1.4,0.3,setosa
5.0,3.4,1.5,0.2,setosa
4.4,2.9,1.4,0.2,setosa
```

We can load this csv file into a Python list, a numpy array, and a Pandas
DataFrame, all using the  `into`  function.

#### List $\leftarrow$ CSV

#### NumPy $\leftarrow$ CSV

#### Pandas $\leftarrow$ CSV

Again, Blaze isn’t doing any of the work, it just calls out to the
 `read_csv`  function of the appropriate library with the right inputs.

## Demonstrating Breadth

We demonstrate breadth by moving data between more exotic backends

#### SQL $\leftarrow$ CSV

#### MongoDB $\leftarrow$ Pandas

`into`  doesn’t work just with csv files.  We can use it to convert between any
pair of data types.

And to demonstrate that it’s there

#### BColz $\leftarrow$ MongoDB

Finally we migrate from a Mongo database to a BColz out-of-core array.

## Robustness and Performance

Blaze leverages known solutions where they exist, for example migrating from
CSV files to SQL databases we use fast the built-in loaders for that particular
database.

Blaze manages solutions where they don’t exist, for example when migrating from
a MongoDB to a BColz out-of-core array we stream the database through Python,
translating types as necessary.

## More Information

* Documentation:  [blaze.pydata.org/](http://blaze.pydata.org/)
* Source:  [github.com/ContinuumIO/blaze/](http://github.com/ContinuumIO/blaze/)
* Install with [Anaconda](https://store.continuum.io/cshop/anaconda/): 
 `conda install blaze
`
