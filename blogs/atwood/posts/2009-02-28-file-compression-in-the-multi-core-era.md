---
title: "File Compression in the Multi-Core Era"
date: 2009-02-28
url: https://blog.codinghorror.com/file-compression-in-the-multi-core-era/
slug: file-compression-in-the-multi-core-era
word_count: 730
---

I’ve been playing around a bit with file compression again, as we generate some very large backup files daily on [Stack Overflow](http://stackoverflow.com/).


We’re using the latest 64-bit version of [7zip](http://www.7-zip.org/) (4.64) on our database server. I’m not a big fan of more than [dual core on the desktop](https://blog.codinghorror.com/choosing-dual-or-quad-core/), but it’s a no brainer for servers. The more CPU cores the merrier! This server has two quad-core CPUs, a total of 8 cores, and I was a little disheartened to discover that neither RAR nor 7zip seemed to make much use of more than 2.


Still, even if it does only use 2 cores to compress, the 7zip algorithm is amazingly effective, and has evolved over the last few years to be [respectably fast](https://blog.codinghorror.com/revisiting-7-zip/). I used to [recommend RAR over Zip](https://blog.codinghorror.com/dont-use-zip-use-rar/), but given the increased efficiency of 7zip and the fact that it’s free and RAR isn’t, it’s the logical choice now.


Here are some quick tests I performed **compressing a single 4.76 GB database backup file**. This was run on a server with dual quad-core 2.5 GHz Xeon E5420 CPUs.

kg-card-begin: html


| 7zip | fastest | 5 min | 14 MB/sec | 973 MB |
| 7zip | fast | 7 min | 11 MB/sec | 926 MB |
| 7zip | normal | 34 min | 2.5 MB/sec | 752 MB |
| 7zip | maximum | 41 min | 2.0 MB/sec | 714 MB |
| 7zip | ultra | 48 min | 1.7 MB/sec | 698 MB |


kg-card-end: html

For those of you who are now wondering, *wow, if 7zip does this well on maximum and ultra, imagine how it’d do on ultra-plus*, don’t count on it. **There’s a reason most compression programs default to certain settings as “normal.” ** Above these settings, results tend to [fall off a cliff](https://blog.codinghorror.com/compression-and-cliffs/); beyond that sweet spot, you tend to get absurdly tiny increases in compression ratio in exchange for huge order of magnitude increases in compression time.


Now watch what happens when I switch 7zip to use the [bzip2 compression algorithm](http://en.wikipedia.org/wiki/Bzip2):


![](https://blog.codinghorror.com/content/images/2025/04/image-309.png)


We’ll compress that same 4.76 GB file, on the same machine:

kg-card-begin: html


| bzip2 | fastest | 2 min | 36 MB/sec | 1092 MB |
| bzip2 | fast | 2.5 min | 29 MB/sec | 1011 MB |
| bzip2 | normal | 3.5 min | 22 MB/sec | 989 MB |
| bzip2 | maximum | 7 min | 12 MB/sec | 987 MB |
| bzip2 | ultra | 21 min | 4 MB/sec | 986 MB |


kg-card-end: html

Why is bzip2 able to work so much *faster* than 7zip? Simple:


**7zip algorithm CPU usage**


![](https://blog.codinghorror.com/content/images/2025/04/image-308.png)


**bzip2 algorithm CPU usage**


![](https://blog.codinghorror.com/content/images/2025/04/image-307.png)


**Bzip2 uses more than 2 CPU cores to parallelize its work**. I’m not sure what the limit is, but the drop-down selector in the 7zip GUI allows up to 16 when the bzip2 algorithm is chosen. I used 8 for the above tests, since that’s how many CPU cores we have on the server.


Unfortunately, bzip2’s increased speed is sort of moot at high compression levels. The difference between normal, maximum, and ultra compression is a meaningless 0.06 percent. It scales beautifully in time, but hardly at all in space. That’s a shame, because that’s exactly where you’d like to spend the speed increase of parallelization. Eking out a percent of size improvement [could still make sense](https://web.archive.org/web/20090303014946/http://users.elis.ugent.be/~wheirman/compression/index.php#ranking), depending on the circumstances:


> *total time = compression time + n * (compressed file size / network speed + decompression time)*
> For instance, if you compress a file to send it over a network once, *n* equals one and compression time will have a big influence. If you want to post a file to be downloaded many times, *n* is big so long compression times will weigh less in the final decision. Finally, slow networks will do best with a slow but efficient algorithm, while for fast networks a speedy, possibly less efficient algorithm is needed.


On the other hand, the ability to **compress a 5 GB source file to a fifth of its size in two minutes flat** is pretty darn impressive. Still, I can’t help wondering how fast the 7zip algorithm would be if it was rewritten and parallelized to take advantage of more than 2 CPU cores, too.

[file compression](https://blog.codinghorror.com/tag/file-compression/)
[multi-core](https://blog.codinghorror.com/tag/multi-core/)
[7zip](https://blog.codinghorror.com/tag/7zip/)
[cpu cores](https://blog.codinghorror.com/tag/cpu-cores/)
[software optimization](https://blog.codinghorror.com/tag/software-optimization/)
