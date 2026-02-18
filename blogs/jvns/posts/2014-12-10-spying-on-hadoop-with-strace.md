---
title: "Spying on Hadoop with strace"
date: 2014-12-10
url: https://jvns.ca/blog/2014/12/10/spying-on-hadoop-with-strace/
slug: spying-on-hadoop-with-strace
word_count: 1047
---


As you may already know, I really like strace. (It has a
[whole category on this blog](http://jvns.ca/categories/strace/)).
So when the people at Big Data Montreal asked if I wanted to give a talk
about stracing Hadoop, the answer was YES OBVIOUSLY.


I set up a small Hadoop cluster (1 master, 2 workers, replication set to 1) on
Google Compute Engine to get this working, so that’s what we’ll be talking
about. It has one 14GB CSV file, which contains part of this
[Wikipedia revision history dataset](https://cloud.google.com/bigquery/docs/dataset-wikipedia)


Let’s start diving into HDFS! (If this is familiar to you, I talked
about a lot of this already in [Diving into HFDS](http://jvns.ca/blog/2014/05/15/diving-into-hdfs/). There are new
things, though! At the end of this we edit the blocks on the data node
and see what happens and it’s GREAT.)


```
$ snakebite ls -h /
-rw-r--r--   1 bork       supergroup       14.1G 2014-12-08 02:13 /wikipedia.csv

```


## Files are split into blocks


HDFS is a distributed filesystem, so a file can be split across many
machines. I wrote a little module to help explore how a file is
distributed. Let’s take a look!


You can see the source code for all this in
[hdfs_fun.py](https://github.com/jvns/hadoop_fun/blob/20b8c4c8d4280da7d0543fd98473b79916435d9d/hdfs_fun.py).


```
import hdfs_fun
fun = hdfs_fun.HDFSFun()
blocks = fun.find_blocks('/wikipedia.csv')
fun.print_blocks(blocks)

```


which outputs


```
     Bytes |   Block ID | # Locations |       Hostnames
 134217728 | 1073742025 |           1 |      hadoop-w-1
 134217728 | 1073742026 |           1 |      hadoop-w-1
 134217728 | 1073742027 |           1 |      hadoop-w-0
 134217728 | 1073742028 |           1 |      hadoop-w-1
 134217728 | 1073742029 |           1 |      hadoop-w-0
 134217728 | 1073742030 |           1 |      hadoop-w-1
 ....
 134217728 | 1073742136 |           1 |      hadoop-w-0
  66783720 | 1073742137 |           1 |      hadoop-w-1

```


This tells us that `wikipedia.csv` is split into 113 blocks, which are
all 128MB except the last one, which is smaller. They have block IDs
1073742025 - 1073742137. Some of them are on hadoop-w-0, and some are on
hadoop-w-1.


Let’s see the same thing using strace!


```
 $ strace -f -o strace.out snakebite cat /wikipedia.csv | head

```


### Part 1: talk to the namenode!


We ask the namenode where /wikipedia.csv is…


```
connect(4, {sa_family=AF_INET, sin_port=htons(8020),
    sin_addr=inet_addr("10.240.98.73")}, 16)
sendto(4,
    "\n\21getBlockLocations\22.org.apache.hadoop.hdfs.protocol.ClientProtocol\30\1",
    69, 0, NULL, 0) = 69
sendto(4, "\n\16/wikipedia.csv\20\0\30\350\223\354\2378", 24, 0, NULL, 0) = 24

```


… and get an answer!


```

recvfrom(4,
"\255\202\2\n\251\202\2\10\350\223\354\2378\22\233\2\n7\n'BP-572418726-10.240.98.73-1417975119036\20\311\201\200\200\4\30\261\t
\200\200\200@\20\0\32\243\1\nk\n\01610.240.146.168\22%hadoop-w-1.c.stracing-hadoop.internal\32$358043f6-051d-4030-ba9b-3cd0ec283f6b
\332\206\3(\233\207\0030\344\206\0038\0\20\200\300\323\356&\30\200\300\354\372\32
\200\240\377\344\4(\200\300\354\372\0320\374\260\234\276\242)8\1B\r/default-rackP\0X\0`\0
\0*\10\n\0\22\0\32\0\"\0002\1\0008\1B'DS-3fa133e4-2b17-4ed1-adca-fed4767a6e6f\22\236\2\n7\n'BP-572418726-10.240.98.73-1417975119036\20\312\201\200\200\4\30\262\t
\200\200\200@\20\200\200\200@\32\243\1\nk\n\01610.240.146.168\22%hadoop-w-1.c.stracing-hadoop.internal\32$358043f6-051d-4030-ba9b-3cd0ec283f6b
\332\206\3(\233\207\0030\344\206\0038\0\20\200\300\323\356&\30\200\300\354\372\32
\200\240\377\344\4(\200\300\354\372\0320\374\260\234\276\242)8\1B\r/default-rackP\0X\0`\0
\0*\10\n\0\22\0\32\0\"\0002\1\0008\1B'DS-3fa133e4-2b17-4ed1-adca-fed4767a6e6f\22\237\2\n7\n'BP-572418726-10.240.98.73-1417975119036\20\313\201\200\200\4\30\263\t
\200\200\200@\20\200\200\200\200\1\32\243\1\nk\n\01610.240.109.224\22%hadoop-w-0.c.stracing-hadoop.internal\32$bd6125d3-60ea-4c22-9634-4f6f352cfa3e
\332\206\3(\233\207\0030\344\206\0038\0\20\200\300\323\356&\30\200\240\342\335\35
\200\240\211\202\2(\200\240\342\335\0350\263\257\234\276\242)8\1B\r/default-rackP\0X\0`\0
\0*\10\n\0\22\0\32\0\"\0002\1\0008\1B'DS-c5ef58ca-95c4-454d-adf4-7ceaf632c035\22\237\2\n7\n'BP-572418726-10.240.98.73-1417975119036\20\314\201\200\200\4\30\264\t
\200\200\200@\20\200\200\200\300\1\32\243\1\nk\n\01610.240.146.168\22%hadoop-w-1.c.stracing-hadoop.inte"...,
33072, 0, NULL, NULL) = 32737

```


The hostnames in this answer totally match up with the table of where we
think the blocks are!


### Part 2: ask the datanode for data!


So the next part is that we ask `10.240.146.168` for the first block.


```
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.146.168")}, 16) = 0
sendto(5, "\nK\n>\n2\n'BP-572418726-10.240.98.73-1417975119036\20\311\201\200\200\4\30\261\t\22\10\n\0\22\0\32\0\"\0\22\tsnakebite\20\0\30\200\200\200@", 84, 0, NULL, 0) = 84
recvfrom(5, "title,id,language,wp_namespace,is_redirect,revision_id,contributor_ip,contributor_id,contributor_username,timestamp,is_minor,is_bot,reversion_id,comment,num_characters\nIvan Tyrrell,6126919,,0,true,264190184,,37486,Oddharmonic,1231992299,,,,\"Added defaultsort tag, categories.\",2989\nInazuma Raigor\305\215,9124432,,0,,224477516,,2995750,ACSE,1215564370,,,,/* Top division record */ rm jawp reference,5557\nJeb Bush,189322,,0,,299771363,66.119.31.10,,,1246484846,,,,/* See also */,43680\nTalk:Goranboy (city),18941870,,1,,", 512, 0, NULL, NULL) = 512
recvfrom(5, "233033452,,627032,OOODDD,1219200113,,,,talk page tag  using [[Project:AutoWikiBrowser|AWB]],52\nTalk:Junk food,713682,,1,,210384592,,6953343,D.c.camero,1210013227,,,,/* Misc */,13654\nCeline Dion (album),3294685,,0,,72687473,,1386902,Max24,1156886471,,,,/* Chart Success */,4578\nHelle Thorning-Schmidt,1728975,,0,,236428708,,7782838,Vicki Reitta,1220614668,,,,/* Member of Folketing */  updating (according to Danish wikipedia),5389\nSouthwest Florida International Airport,287529,,0,,313446630,76.101.171.136,,,125", 512, 0, NULL, NULL) = 512

```


```
$ strace -e connect snakebite cat /wikipedia.csv > /dev/null
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.146.168")}, 16) = 0
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.146.168")}, 16) = 0
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.109.224")}, 16) = 0
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.146.168")}, 16) = 0
connect(5, {sa_family=AF_INET, sin_port=htons(50010), sin_addr=inet_addr("10.240.109.224")}, 16) = 0

```


This sequence matches up exactly with the order of the blocks in the
table up at the top! So fun. Next, we can look at the message the client
is sending to the datanodes:


```
sendto(5, "\nK\n>\n2\n'BP-572418726-10.240.98.73-1417975119036\20\311\201\200\200\4\30\261\t\22\10\n\0\22\0\32\0\"\0\22\tsnakebite\20\0\30\200\200\200@", 84, 0, NULL, 0) = 84

```


This is a little hard to read, but it turns out it’s a
[Protocol Buffer](https://code.google.com/p/protobuf/) and so we can
parse it pretty easily. Here’s what it’s trying to say:


```
OpReadBlockProto
header {
  baseHeader {
    block {
      poolId: "BP-572418726-10.240.98.73-1417975119036"
      blockId: 1073742025
      generationStamp: 1201
    }
    token {
      identifier: ""
      password: ""
      kind: ""
      service: ""
    }
  }
  clientName: "snakebite"
}

```


And then, of course, we get a response:


```
recvfrom(5,"title,id,language,wp_namespace,is_redirect,revision_id,contributo
r_ip,contributor_id,contributor_username,timestamp,is_minor,is_bot
,reversion_id,comment,num_characters\nIvanTyrrell,6126919,,0,true,264190184,,
37486,Oddharmonic,1231992299,,,,\"Addeddefaultsorttag,categorie
s.\",2989\nInazumaRaigor\305\215,9124432,,0,,224477516,,2995750,ACSE,12155643
70,,,,/*Topdivisionrecord*/rmjawpreference,5557\nJebBush,1
89322,,0,,299771363,66.119.31.10,,,1246484846,,,,/*Seea

```


Which is just the beginning of a CSV file! How wonderful.


### Part 3: Finding the block on the datanode.


Seeing the datanode send us the data is nice, but what if we want to get
even closer to the data? It turns out that this is really easy. I sshed
to my data node and ran


```
$ locate 1073742025

```


with the idea that maybe there was a file with `1073742025` in the name that had the block data. And there was!


```
$ cd /hadoop/dfs/data/current/BP-572418726-10.240.98.73-1417975119036/current/finalized
$ ls -l blk_1073742025
-rw-r--r-- 1 hadoop hadoop 134217728 Dec 8 02:08 blk_1073742025

```


It has exactly the right size (134217728 bytes), and if we look at the beginning, it contains exactly the data from the first 128MB of the CSV file. GREAT.


### Super fun exciting part: **Editing** the block on the datanode


So I was giving this talk yesterday, and was doing a live demo where I
was ssh’d into the data node, and we were looking at the file for the
block. And suddenly I thought… WAIT WHAT IF WE EDITED IT GUYS?!


And someone commented “No, it won’t work, there’s metadata, the checksum
will fail!”. So, of course, we tried it, because toy clusters are for
breaking.


And it worked! Which wasn’t perhaps super surprising because replication
was set to 1 and maybe a 128MB file is too big to take a checksum of
every time you want to read from it, but REALLY FUN. I edited the
beginning of the file to say `AWESOME AWESOME AWESOME` instead of
whatever it said before (keeping the file size the same), and then a
`snakebite cat /wikipedia.csv` showed the file starting with `AWESOME AWESOME AWESOME`.


So some lessons:

- I’d really like to know more about data consistency in Hadoop clusters
- live demos are GREAT
- writing a blog is great because then people ask me to give talks about
fun things I write about like stracing Hadoop


That’s all folks! There are [slides for the talk I gave](https://speakerdeck.com/jvns/spying-on-hadoop-with-strace), though
this post is guaranteed to be much better than the slides. And maybe
video for that talk will be up at some point.
