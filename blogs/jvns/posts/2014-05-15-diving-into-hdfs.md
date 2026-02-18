---
title: "Diving into HDFS"
date: 2014-05-15
url: https://jvns.ca/blog/2014/05/15/diving-into-hdfs/
slug: diving-into-hdfs
word_count: 850
---


Yesterday I wanted to start learning about how HDFS (the Hadoop
Distributed File System) works internally. I knew that

- It’s distributed, so one file may be stored across many different
machines
- There’s a *namenode*, which keeps track of where all the files are
stored
- There are *data nodes*, which contain the actual file data


But I wasn’t quite sure how to get started! I knew how to navigate the
filesystem from the command line (`hadoop fs -ls /`, and friends), but
not how to figure out how it works internally.


[Colin Marc](http://twitter.com/colinmarc) pointed me to this great
library called [snakebite](https://github.com/spotify/snakebite) which
is a Python HDFS client. In particular he pointed me to the part of
the code that
[reads file contents from HDFS](https://github.com/spotify/snakebite/blob/master/snakebite/client.py#L966-L1033).
We’re going to tear it apart a bit and see what exactly it does!


### Getting started: Elastic MapReduce!


I didn’t want to set up a Hadoop cluster by hand, and I had some AWS
credit that I’d gotten for free, so I set up a small Amazon Elastic
MapReduce cluster. I worked on this with with
[Pablo Torres](https://twitter.com/ptn777) and
[Sasha Laundy](https://twitter.com/SashaLaundy) and we spent much of
the morning fighting with it and trying to figure out protocol
versions and why it wasn’t working with Snakebite.


What ended up working was choosing AMI version “3.0.4 (hadoop 2.2.0)”.
This is CDH5 and Hadoop protocol version 9. Hadoop versions are
*confusing*. We installed that and Snakebite version 2.4.1 and that
almost worked.


**Important things**:

- We needed to look at `/home/hadoop/conf/core-site.xml` to find the
namenode IP and port (in `fs.default.name`
- We needed to edit
[snakebite/config.py](https://github.com/spotify/snakebite/blob/25418007e93f99f6dc6807ca44d25287217e783f/snakebite/config.py)
to say ‘fs.default.name’ instead of ‘fs.defaultFS’. Who knows. It
worked.


Once we did this, we could run `snakebite ls /` successfully! Time to
move on to breaking things!


### Putting data into our cluster


I copied some Wikipedia data from one of Amazon’s public datasets like
this;


`hadoop distcp s3://datasets.elasticmapreduce/wikipediaxml/part-116.xml /wikipedia`


This creates a file in HDFS called `/wikipedia`. You can see more
datasets that are easy to copy into HDFS from Amazon at
[https://s3.amazonaws.com/datasets.elasticmapreduce/](https://s3.amazonaws.com/datasets.elasticmapreduce/).


### Getting a block from our file!


Now that we have a Hadoop cluster, some data in HDFS, and a tool to
look at it with (snakebite), we can really get started!


Files in HDFS are split into *blocks*. When getting a file from HDFS,
the first thing we need to do is to ask the namenode where the blocks
are stored.


With the help of a lot of snakebite source diving, I write a small
Python function to do this called `find_blocks`. You can see it in a
tiny Python module I made called
[hdfs_fun.py](https://github.com/jvns/hadoop_fun/blob/master/hdfs_fun.py).
To get it to work, you’ll need a Hadoop cluster and snakebite.


```

>>> cl = hdfs_fun.create_client()
>>> hdfs_fun.find_blocks(cl, '/wikipedia')
[snakebite.protobuf.hdfs_pb2.LocatedBlockProto at 0xe33a910,
 snakebite.protobuf.hdfs_pb2.LocatedBlockProto at 0xe33ab40

```


One of the first things I did was use `strace` to find out what data actually gets sent over the wire when I call this function. Here’s a snippet: ([the whole thing](https://gist.github.com/jvns/bc054ea0f38b5054fd3a))


Part of the request: asking for the block locations for the
`/wikipedia` file.


```

sendto(7,
"\n\21getBlockLocations\22.org.apache.hadoop.hdfs.protocol.ClientProtocol\30\1",
69, 0, NULL, 0) = 69
sendto(7, "\n\n/wikipedia\20\0\30\337\260\240]", 19, 0, NULL, 0) = 19

```


Part of the response: (I’ve removed most of it to point out some of
the important parts)


```

recvfrom(7,
"....BP-1019336183-10.165.43.39-1400088409498..........................
10.147.177.170-9200-1400088495802........................
BP-1019336183-10.165.43.39-1400088409498.............10.147.177.170-9200-1400088495802
\360G(\216G0\361G8\0\20\200\240\201\213\275\f\30\200\340\376]
\200\300\202\255\274\f(\200\340\376]0\212\306\273\205\340(8\1B\r/default-rackP\0
\0*\10\n\0\22\0\32\0\"\0\30\0\"\355", 731, 0, NULL, NULL) = 731

```


Back in our Python console, we can see what some of these numbers mean:


```

>>> blocks[0].b.poolId
u'BP-1019336183-10.165.43.39-1400088409498'
>>> blocks[0].b.numBytes
134217728L
>>> blocks[0].locs[0].id.ipAddr
u'10.147.177.170'
>>> blocks[0].locs[0].id.xferPort
9200
>>> blocks[1].b.poolId
u'BP-1019336183-10.165.43.39-1400088409498'
>>> blocks[1].b.numBytes
61347935L

```


So we have two blocks! The two `numBytes` add up to the total size of
the file! Cool! They both have the same `poolId`, and it also turns
out that they have the same IP address and port


### Reading a block


Let’s try to read the data from a block! (you can see the `read_block`
function here in
[hdfs_fun.py](https://github.com/jvns/hadoop_fun/blob/master/hdfs_fun.py)


```

>>> block = blocks[0]
>>> gen = hdfs_fun.read_block(block) # returns a generator
>>> load = gen.next()

```


If I look at `strace`, it starts with:


```

connect(8, {sa_family=AF_INET, sin_port=htons(9200),
    sin_addr=inet_addr("10.147.177.170")}, 16) = 0
sendto(8,
    "\nB\n5\n3\n(BP-1019336183-10.165.43.39-1400088409498\20\211\200\200\200\4\30\361\7\22\tsnakebite\20\0\30\200\200\200@",
    75, 0, NULL, 0) = 75

```


*Awesome*. We can see easily that it’s connecting to the block’s data
node (`10.147.177.170` on port `9200`, and asking for something with
id `BP-1019336183-10.165.43.39-1400088409498`). Then the data node
starts sending back data!!!


```

recvfrom(8, "ot, it's a painting. Thomas Graeme apparently lived in
the mid-18th century, according to the [[Graeme Park]] article. The
rationale also says that this image is "used on the biography
page about him by USHistory.org of Graeme Park." I cannot quite
figure out what this means, but I am guessing that it means the
uploader took this image from a page hosted on USHistory.org. A
painting of a man who lived in the mid-18th century is likely to be
the public domain, as claimed, but we have no good source", 512, 0,
NULL, NULL) = 512

```


AMAZING. We have conquered HDFS.


That’s all for this blog post! We’ll see if I do more later today.
