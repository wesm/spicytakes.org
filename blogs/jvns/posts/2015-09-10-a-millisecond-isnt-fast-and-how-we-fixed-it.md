---
title: "A millisecond isn't fast (and how we made it 100x faster)"
date: 2015-09-10
url: https://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/
slug: a-millisecond-isnt-fast-and-how-we-fixed-it
word_count: 637
---


Hi friends! For the first time today I’m going to tell you about my DAY
AT WORK (machine learning at Stripe) yesterday. =D. This is a
collaboration with [Kamal Marhubi](http://kamalmarhubi.com) who did this
profiling with me after work because I was so mad about the performance.


I used to think a millisecond was fast. At work, I have code that runs
some VERY_LARGE_NUMBER of times. It’s distributed and split up into
tasks, and an individual task runs the code more than 6 million times.


I wrote a benchmark for the Slow Code and found it could process
~1000 records/s. This meant that processing 6 million things would take
1.5 hours, which is Slow. The code is kind of complicated, so originally
we all thought this was a reasonable amount of time. But my heart was
sad.


Yesterday [Avi](https://twitter.com/avibryant) (who is the best) and I
looked at why it was so damn slow (~1 millisecond/record) in some more
depth. This code is open source so I can show it to you! We profiled using
VisualVM and, after doing some optimizations, found out that it was
spending all its time in `DenseHLL$x$6`. This is mystery Scala speak for
this code block from Twitter’s Algebird library that estimates the size of a HyperLogLog:


```
  lazy val (zeroCnt, z) = {
    var count: Int = 0
    var res: Double = 0

    // goto while loop to avoid closure
    val arr: Array[Byte] = v.array
    val arrSize: Int = arr.size
    var idx: Int = 0
    while (idx < arrSize) {
      val mj = arr(idx)
      if (mj == 0) {
        count += 1
        res += 1.0
      } else {
        res += java.lang.Math.pow(2.0, -mj)
      }
      idx += 1
    }
    (count, 1.0 / res)
  }

```


from
[HyperLogLog.scala](https://github.com/twitter/algebird/blob/c84d67836396757db881/algebird-core/src/main/scala/com/twitter/algebird/HyperLogLog.scala#L436-L455)


This is a little inscrutable and I’m not going to explain what this code
does, but `arrSize` in my case is 4096. So basically, we have
something like 10,000 floating point operations, and it takes about 1ms
to do. I am still new to performance optimizations, but I discussed it
with Kamal and we decided it was outrageous. Since this loop is **hardly
doing anything omg**, the obvious target is `java.lang.Math.pow(2.0, -mj)`, because that looks like the hardest thing. (note: Java is pretty fast. if you are doing normal operations like adding and multiplying numbers it should go REALLY FAST. because [computers are fast](http://jvns.ca/blog/2014/05/12/computers-are-fast/))


(note: [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832) is great and useful in
cases like this! Many CPU instructions take a nanosecond
or something. so 10K of them should be on the order of 10 microseconds
or so. Definitely not a millisecond.)


Kamal and I tried two things: replacing `Math.pow(2, -mj)` with `1.0 / (1 << mj)`, and writing a lookup table (since `mj` is a byte and has
256 possible values, we can just calculate 2^(-mj) for every possible
value up front).


The final performance numbers on the benchmark we picked were:


```
math.pow:         0.8ms
1.0 / (1 << mj):  0.017ms (!)
the lookup table: 0.008ms (!!!)

```


So we can literally make this code **100 times faster** by just changing
one line. Avi simultaneously came to the same conclusions and
made this pull request [Speed up HLL presentation by 100x](https://github.com/twitter/algebird/pull/491). Hooray!


I’m learning intuitions for when code is slower than it should be and it
is THE BEST. Being able to say “this code should not take 10s to process
10,000 records” is amazing. It is even more amazing when you can
actually fix it.

- worked with someone on understanding which of our machine learning models are doing the most work for us
- wrote 2 SQL queries to help someone on the Risk team find accounts with suspicious activity
- wrangled Scala performance (this) so that we can generate training sets for our machine learning models without tearing our hair out
